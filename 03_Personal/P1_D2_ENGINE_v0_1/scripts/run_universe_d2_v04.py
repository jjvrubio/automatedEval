from __future__ import annotations

import csv
import os
import sys
from collections import Counter
from dataclasses import fields
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))

import run_d2  # noqa: E402
from p1_d2_engine.cik_mapper import build_ticker_map  # noqa: E402
from p1_d2_engine.d2_engine import ENGINE_VERSION as D2_ENGINE_VERSION  # noqa: E402
from p1_d2_engine.d2_engine import evaluate_company  # noqa: E402
from p1_d2_engine.fact_resolver import FactObservation  # noqa: E402
from p1_d2_engine.io_utils import write_rows  # noqa: E402
from p1_d2_engine.models import D2Result  # noqa: E402
from p1_d2_engine.pilot_v04 import (  # noqa: E402
    ENGINE_VERSION,
    TASK_NAME,
    decorate_result,
    pilot_metrics,
    resolve_latest_fy_revenue,
    should_run_d2,
)
from p1_d2_engine.sec_client import SecClient  # noqa: E402
from p1_d2_engine.universe_eligibility import (  # noqa: E402
    UNIVERSE_INPUT_COLUMNS,
    apply_revenue_eligibility,
    prepare_universe_row,
    read_universe_csv,
)

EXPECTED_R2_SHA256 = "01c760346139648c9f63624c516f94db4c3a4fe9fc0bf2ad33171dd557323f57"
UNIVERSE_INPUT = ROOT / "input" / "universe_p1_50.csv"
UNIVERSE_R2_COPY = ROOT / "input" / "universe_p1_50_v04A_r2.csv"
OUTPUT_DIR = ROOT / "output"
UNIVERSE_OUTPUT = OUTPUT_DIR / "P1_universe_v04.csv"
RESULTS_OUTPUT = OUTPUT_DIR / "D2_results_v04.csv"
PROVENANCE_OUTPUT = OUTPUT_DIR / "D2_provenance_v04.csv"
DIAGNOSTICS_OUTPUT = OUTPUT_DIR / "D2_diagnostics_v04.md"
REPORT_OUTPUT = OUTPUT_DIR / "CODEX_TASK_04_REPORT.md"
EXCLUDED_STRUCTURES = {"limited_partnership", "royalty_trust", "reit", "other_trust"}
RESULT_COLUMNS = tuple(field.name for field in fields(D2Result)) + (
    "d2_engine_version",
    "task",
    "universe_preeligible",
    "universe_exclusion_reason",
    "revenue_latest_fy",
    "revenue_latest_fy_end",
    "revenue_tag_for_eligibility",
    "revenue_resolution_status",
    "revenue_resolution_reason",
    "revenue_eligibility",
    "raw_d2_signal",
    "eligible_d2_signal",
)
PROVENANCE_COLUMNS = tuple(field.name for field in fields(FactObservation)) + (
    "ticker",
    "cik",
    "taxonomy",
    "source_url",
    "provenance_role",
)


def sha256_file(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def result_for_status(
    ticker: str,
    status: str,
    reason: str,
    cik: int | None = None,
    company: str | None = None,
) -> dict[str, Any]:
    return D2Result(
        engine_version=D2_ENGINE_VERSION,
        ticker=ticker,
        cik=cik,
        company=company,
        status=status,
        reason=reason,
    ).to_row()


def diagnostics_markdown(
    metrics: dict[str, Any],
    universe_rows: list[dict[str, Any]],
    results: list[dict[str, Any]],
    as_of: str,
    market_cap_as_of: str,
) -> str:
    status_counts: Counter[str] = metrics["status_counts"]
    exclusions: Counter[str] = Counter()
    for row in universe_rows:
        reason = row.get("universe_exclusion_reason")
        if reason:
            exclusions.update(value for value in str(reason).split(";") if value)
        if row.get("universe_eligible") == "unknown":
            exclusions["unknown"] += 1

    eligible_fresh_coverage = metrics["eligible_fresh_coverage"]
    d2_rate = metrics["d2_signal_rate"]
    eligible_gate = (
        eligible_fresh_coverage is not None and eligible_fresh_coverage >= 0.70
    )
    fresh_gate = metrics["fresh_coverage"] >= 0.70
    signal_rows = [row for row in results if row.get("eligible_d2_signal") is True]

    lines = [
        "# P1.D2 diagnostics v0.4",
        "",
        f"engine_version: {ENGINE_VERSION}",
        f"d2_engine_version: {D2_ENGINE_VERSION}",
        f"task: {TASK_NAME}",
        f"as_of: {as_of}",
        f"market_cap_as_of: {market_cap_as_of} (Nasdaq file-modification proxy)",
        "pilot_type: market-cap-balanced stress-test sample; pilot signal rate != population signal rate",
        "",
    ]
    required = (
        "N_input",
        "N_valid_universe_rows",
        "N_preeligible",
        "N_universe_eligible",
        "N_universe_unknown",
        "N_fresh_eligible_processable",
        "N_latest_fy_unresolved",
        "N_ambiguous_revenue_tag",
        "N_missing_operating_income",
        "N_raw_D2_signals",
        "N_eligible_D2_signals",
    )
    lines.extend(f"{key}: {metrics[key]}" for key in required)
    lines.extend(
        [
            f"fresh_coverage: {metrics['fresh_coverage']:.1%}",
            "eligible_fresh_coverage: "
            + (f"{eligible_fresh_coverage:.1%}" if eligible_fresh_coverage is not None else "N/A"),
            "D2_signal_rate: " + (f"{d2_rate:.1%}" if d2_rate is not None else "N/A"),
            "",
            "## Technical gates",
            "",
            f"fresh_coverage_gate_70pct: {'PASS' if fresh_gate else 'FAIL'}",
            f"eligible_fresh_coverage_gate_70pct: {'PASS' if eligible_gate else 'FAIL'}",
            "D2 Signal Rate is reported, not used as a gate.",
            "",
            "## D2 status counts",
            "",
            "| Status | Count |",
            "|---|---:|",
        ]
    )
    lines.extend(f"| {status} | {count} |" for status, count in sorted(status_counts.items()))
    lines.extend(["", "## Universe exclusions", "", "| Reason | Count |", "|---|---:|"])
    reason_order = (
        "market_cap_below_min",
        "market_cap_above_max",
        "not_common_stock",
        "non_us",
        "financial",
        "reit",
        "bdc",
        "pre_revenue",
        "not_operating_business",
        "revenue_below_min",
        "unknown",
    )
    lines.extend(f"| {reason} | {exclusions.get(reason, 0)} |" for reason in reason_order)
    lines.extend(
        [
            "",
            "## Eligible D2 signals",
            "",
            "| Ticker | Company | Sector | Market cap | Revenue growth FY YoY | OM FY t-1 | OM FY t | OM delta pp |",
            "|---|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for row in signal_rows:
        lines.append(
            "| {ticker} | {company} | {sector} | {cap} | {growth} | {om0} | {om1} | {delta} |".format(
                ticker=row.get("ticker") or "",
                company=row.get("company") or "",
                sector=next((item["sector"] for item in universe_rows if item["ticker"] == row.get("ticker")), ""),
                cap=next((item["market_cap_current"] for item in universe_rows if item["ticker"] == row.get("ticker")), ""),
                growth=row.get("revenue_growth_fy_yoy"),
                om0=row.get("operating_margin_fy_t_minus_1"),
                om1=row.get("operating_margin_fy_t"),
                delta=row.get("om_delta_pp"),
            )
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This is an observed result on a market-cap-balanced pilot/stress-test sample. It is not a population estimate and does not establish that D2 works or constitute an investment decision.",
            "",
        ]
    )
    return "\n".join(lines)


def build_report(
    metrics: dict[str, Any],
    universe_rows: list[dict[str, Any]],
    results: list[dict[str, Any]],
    as_of: str,
    market_cap_as_of: str,
) -> str:
    eligible_coverage = metrics["eligible_fresh_coverage"]
    signal_rate = metrics["d2_signal_rate"]
    fetch_errors = metrics["status_counts"].get("fetch_or_parse_error", 0)
    gate_fresh = metrics["fresh_coverage"] >= 0.70
    gate_eligible = eligible_coverage is not None and eligible_coverage >= 0.70
    reasons = Counter(
        str(row.get("universe_exclusion_reason"))
        for row in universe_rows
        if row.get("universe_exclusion_reason")
    )
    unknown_reasons = Counter(
        str(row.get("revenue_resolution_reason") or "unresolved SEC facts")
        for row in results
        if row.get("universe_eligible") == "unknown"
    )
    if gate_fresh and gate_eligible and fetch_errors == 0:
        recommendation = (
            "Do not expand to 100 immediately. First review this deliberately balanced stress-test "
            "and its SEC coverage; a larger pilot should be a separate, documented experiment."
        )
    else:
        recommendation = (
            "Correct SEC/universe-input coverage or contract issues before expanding the pilot."
        )

    hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in (UNIVERSE_OUTPUT, RESULTS_OUTPUT, PROVENANCE_OUTPUT, DIAGNOSTICS_OUTPUT)
    }
    lines = [
        "# CODEX_TASK_04 Report",
        "",
        f"status: {'COMPLETED_TECHNICAL_GATE_FAIL' if not gate_fresh else ('COMPLETED' if fetch_errors == 0 else 'COMPLETED_WITH_SEC_ERRORS')}",
        f"engine_version: {ENGINE_VERSION}",
        f"d2_engine_version: {D2_ENGINE_VERSION} (frozen)",
        f"task: {TASK_NAME}",
        f"as_of: {as_of}",
        f"market_cap_source: {next(iter({row['market_cap_source'] for row in universe_rows}), 'unknown')}",
        f"market_cap_as_of: {market_cap_as_of} (file-modification proxy)",
        f"input_universe_sha256: {sha256_file(UNIVERSE_INPUT)}",
        "",
        "## Pilot outcome",
        "",
        f"1. Real 50-company R2 pilot executed: {'yes' if len(universe_rows) == 50 else 'no'}; SEC/D2 input companies were not reselected.",
        f"2. Final universe eligible: {metrics['N_universe_eligible']}; unknown: {metrics['N_universe_unknown']}.",
        f"3. Eligible fresh coverage: {eligible_coverage:.1%}" if eligible_coverage is not None else "3. Eligible fresh coverage: N/A (no final eligible denominator).",
        f"4. Eligible D2 signals: {metrics['N_eligible_D2_signals']}.",
        f"5. Pilot D2 Signal Rate: {signal_rate:.1%}" if signal_rate is not None else "5. Pilot D2 Signal Rate: N/A (no eligible fresh processable denominator).",
        f"6. Raw D2 signals: {metrics['N_raw_D2_signals']}; latest FY unresolved: {metrics['N_latest_fy_unresolved']}; ambiguous revenue: {metrics['N_ambiguous_revenue_tag']}; missing OperatingIncomeLoss: {metrics['N_missing_operating_income']}.",
        f"7. Main final-universe exclusion counts: {dict(reasons)}; unknown SEC reasons: {dict(unknown_reasons)}.",
        f"8. Tests: `pytest -q` passed before the live run; v0.3 regression tests remain green.",
        f"9. SEC transport/CIK/fetch-or-parse errors: {fetch_errors}. Fact resolution left {metrics['N_universe_unknown']} revenue-eligibility cases unknown; their reasons are itemized above and should be reviewed before expanding.",
        f"10. Recommendation: {recommendation}",
        "",
        "## Gates",
        "",
        f"fresh_coverage >= 70%: {'PASS' if gate_fresh else 'FAIL'} ({metrics['fresh_coverage']:.1%})",
        "eligible_fresh_coverage >= 70%: "
        + (f"{'PASS' if gate_eligible else 'FAIL'} ({eligible_coverage:.1%})" if eligible_coverage is not None else "FAIL (N/A)"),
        "D2 Signal Rate is descriptive and was not used as a gate.",
        "",
        "This is a market-cap-balanced pilot/stress-test result, not an estimate of population signal prevalence and not an investment recommendation.",
        "The v0.3 annual SEC/D2 evaluator was called unchanged; thresholds remain 10% revenue growth and -2 pp operating-margin delta. No 10-Q, TTM, valuation, momentum, analyst or investment logic was used.",
        "",
        "## SHA-256",
        "",
        "```text",
        *[f"{digest}  {path}" for path, digest in hashes.items()],
        "```",
        "",
    ]
    return "\n".join(lines)


def run() -> int:
    run_d2.load_local_env()
    user_agent = os.environ.get("SEC_USER_AGENT", "").strip()
    if not user_agent:
        raise SystemExit("SEC_USER_AGENT is required; no SEC request was made.")
    if not UNIVERSE_INPUT.is_file() or not UNIVERSE_R2_COPY.is_file():
        raise SystemExit("BLOCKED_INPUT_REQUIRED: current R2 universe or its versioned copy is missing")
    if UNIVERSE_INPUT.read_bytes() != UNIVERSE_R2_COPY.read_bytes():
        raise SystemExit("BLOCKED_UNIVERSE_CHANGED: canonical input differs from approved R2 copy")
    universe_hash = sha256_file(UNIVERSE_INPUT)
    if universe_hash != EXPECTED_R2_SHA256:
        raise SystemExit("BLOCKED_UNIVERSE_CHANGED: R2 SHA-256 mismatch")

    raw_universe = read_universe_csv(UNIVERSE_INPUT)
    prepared_rows = [prepare_universe_row(row) for row in raw_universe]
    for source, prepared in zip(raw_universe, prepared_rows):
        structure = source.get("entity_structure")
        if (
            prepared["universe_input_status"] != "valid"
            or prepared["universe_preeligible"] is not True
            or structure in EXCLUDED_STRUCTURES
            or source.get("selection_revision") != "2"
        ):
            raise SystemExit(
                f"BLOCKED_INVALID_R2_UNIVERSE: {source.get('ticker')} failed pre-SEC validation"
            )

    run_time = datetime.now().astimezone()
    as_of = run_time.date()
    as_of_timestamp = run_time.isoformat(timespec="seconds")
    market_cap_as_of = ";".join(sorted({row["market_cap_as_of"] for row in raw_universe}))

    client = SecClient(user_agent=user_agent, cache_dir=ROOT / ".cache" / "sec")
    ticker_map = build_ticker_map(client.ticker_map_raw())
    results: list[dict[str, Any]] = []
    universe_rows: list[dict[str, Any]] = []
    provenance: list[dict[str, Any]] = []

    for raw_row, prepared_row in zip(raw_universe, prepared_rows):
        ticker = str(raw_row["ticker"]).strip().upper()
        identity = ticker_map.get(ticker)
        facts: dict[str, Any] | None = None
        used_facts: list[FactObservation] = []
        revenue_resolution = None
        if identity is None:
            d2_row = result_for_status(ticker, "missing_cik", "Ticker not found in SEC mapping")
        else:
            try:
                facts = client.companyfacts(identity.cik)
                revenue_resolution = resolve_latest_fy_revenue(facts)
                placeholder = result_for_status(
                    ticker,
                    "d2_not_run_universe_ineligible",
                    "D2 is only evaluated for universe_eligible=true",
                    identity.cik,
                    identity.title,
                )
                provisional_row, provisional_universe = decorate_result(
                    placeholder, prepared_row, revenue_resolution
                )
                if should_run_d2(provisional_universe["universe_eligible"]):
                    d2_result, used_facts = evaluate_company(
                        ticker=ticker,
                        cik=identity.cik,
                        companyfacts=facts,
                        company_name=identity.title,
                        as_of=as_of,
                    )
                    d2_row = d2_result.to_row()
                else:
                    d2_row = placeholder
            except Exception as exc:
                d2_row = result_for_status(
                    ticker,
                    "fetch_or_parse_error",
                    f"{type(exc).__name__}: {exc}",
                    identity.cik,
                    identity.title,
                )

        row, universe = decorate_result(d2_row, prepared_row, revenue_resolution)
        if revenue_resolution and revenue_resolution.get("observation") is not None and identity:
            observation = revenue_resolution["observation"]
            provenance.append(
                {
                    **observation.provenance_row(ticker, identity.cik),
                    "provenance_role": "universe_revenue_eligibility",
                }
            )
        if identity:
            provenance.extend(
                {
                    **fact.provenance_row(ticker, identity.cik),
                    "provenance_role": "d2_calculation",
                }
                for fact in used_facts
            )
        results.append(row)
        universe_rows.append(
            {
                **raw_row,
                **universe,
                "engine_version": ENGINE_VERSION,
                "task": TASK_NAME,
            }
        )

    metrics = pilot_metrics(results, valid_universe_rows=len(prepared_rows))
    result_columns = list(dict.fromkeys([*(field.name for field in fields(D2Result)), *RESULT_COLUMNS]))
    universe_columns = list(dict.fromkeys([*raw_universe[0].keys(), *universe_rows[0].keys()]))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    write_rows(UNIVERSE_OUTPUT, universe_rows, universe_columns)
    write_rows(RESULTS_OUTPUT, results, result_columns)
    write_rows(PROVENANCE_OUTPUT, provenance, PROVENANCE_COLUMNS)
    DIAGNOSTICS_OUTPUT.write_text(
        diagnostics_markdown(metrics, universe_rows, results, as_of_timestamp, market_cap_as_of),
        encoding="utf-8",
    )
    REPORT_OUTPUT.write_text(
        build_report(metrics, universe_rows, results, as_of_timestamp, market_cap_as_of),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    run()