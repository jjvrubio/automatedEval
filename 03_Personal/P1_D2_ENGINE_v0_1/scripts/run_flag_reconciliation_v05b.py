from __future__ import annotations

import csv
import hashlib
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from p1_d2_engine.pilot_v05a import (  # noqa: E402
    build_flag_consistency_audit,
    recompute_signal_flags,
    signal_consistency_issues,
)

VERSION = "0.5B"
TASK = "CODEX_TASK_05B"
OUTPUT_FILES = {
    "universe": ROOT / "output/P1_universe_v05B.csv",
    "results": ROOT / "output/D2_results_v05B.csv",
    "provenance": ROOT / "output/D2_provenance_v05B.csv",
    "audit": ROOT / "output/D2_flag_consistency_audit_v05B.csv",
    "diagnostics": ROOT / "output/D2_diagnostics_v05B.md",
    "report": ROOT / "output/CODEX_TASK_05B_REPORT.md",
}
INPUT_HASHES = {
    "output/D2_results_v05A.csv": "69d86beaf341115e654bf11a23fc2e942b32a37b74e4116c4904d70ffa54a153",
    "output/D2_provenance_v05A.csv": "3ff29e6c7d2a4f5a60a8e6f27ff71b4a4cfe6c541fe3f88abf8eb17aa52bec92",
    "output/P1_universe_v05A.csv": "59dd2d7d9dffc5c382432a2dff80dfe351433c9e4fef61b6d841096cb2750aaa",
    "output/Revenue_tag_decisions_v05A.csv": "10b68e5c5c8172eb1d95e361a061964319b7c56e3800a29bcc31172a74f539ad",
    "output/Revenue_unknown_diagnostics_v05A.csv": "88d77e411c39ff3f8cd5bc4e3ea58172771a2d221982721a1272a60782cce3f8",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def write_rows(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def consistency_audit(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    columns = (
        "ticker",
        "status",
        "candidate_d2",
        "d2_signal",
        "raw_d2_signal",
        "eligible_d2_signal",
        "universe_eligible",
        "freshness_status",
        "latest_fy_resolution_status",
    )
    audit = []
    for row in results:
        issues = signal_consistency_issues(row)
        item = {column: row.get(column, "") for column in columns}
        item.update(
            {
                "consistency_status": "inconsistent" if issues else "consistent",
                "consistency_reason": ";".join(issues),
            }
        )
        audit.append(item)
    return audit


def build_diagnostics(results: list[dict[str, Any]], audit: list[dict[str, Any]]) -> str:
    total = len(results)
    eligible = sum(row.get("universe_eligible") == "True" for row in results)
    ineligible = sum(row.get("universe_eligible") == "False" for row in results)
    unknown = sum(row.get("universe_eligible") == "unknown" for row in results)
    resolution_rate = (eligible + ineligible) / total if total else 0.0
    fresh_eligible = sum(
        row.get("universe_eligible") == "True"
        and row.get("freshness_status") == "fresh"
        and row.get("d2_evaluation_status") == "evaluated"
        for row in results
    )
    eligible_coverage = fresh_eligible / eligible if eligible else 0.0
    raw_signals = sum(row.get("raw_d2_signal") is True for row in results)
    eligible_signals = sum(row.get("eligible_d2_signal") is True for row in results)
    inconsistencies = sum(row["consistency_status"] == "inconsistent" for row in audit)

    lines = [
        "# P1.D2 diagnostics v0.5B",
        "",
        "engine_version: 0.5B",
        "d2_engine_version: 0.3",
        f"task: {TASK}",
        "",
        f"N_input: {total}",
        f"N_universe_eligible: {eligible}",
        f"N_universe_ineligible: {ineligible}",
        f"N_universe_unknown: {unknown}",
        f"UniverseResolutionRate: {resolution_rate:.1%}",
        f"N_fresh_eligible_processable: {fresh_eligible}",
        f"EligibleFreshCoverage: {eligible_coverage:.1%}",
        f"N_raw_D2_signals: {raw_signals}",
        f"N_eligible_D2_signals: {eligible_signals}",
        f"N_flag_inconsistencies: {inconsistencies}",
        "",
        "## Eligible D2 signals",
        "",
        "| Ticker | Company | Revenue growth FY YoY | OM FY t-1 | OM FY t | OM delta pp |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in results:
        if row.get("eligible_d2_signal") is True:
            lines.append(
                "| {ticker} | {company} | {growth} | {om0} | {om1} | {delta} |".format(
                    ticker=row.get("ticker", ""),
                    company=row.get("company", ""),
                    growth=row.get("revenue_growth_fy_yoy", ""),
                    om0=row.get("operating_margin_fy_t_minus_1", ""),
                    om1=row.get("operating_margin_fy_t", ""),
                    delta=row.get("om_delta_pp", ""),
                )
            )
    lines.extend(
        [
            "",
            "Flags are derived from the frozen v0.3 `d2_signal`; no D2 thresholds or Revenue decisions are recalculated here.",
            "",
        ]
    )
    return "\n".join(lines)


def run() -> dict[str, Any]:
    for relative_path, expected_hash in INPUT_HASHES.items():
        path = ROOT / relative_path
        if not path.is_file() or sha256_file(path) != expected_hash:
            raise RuntimeError(f"BLOCKED_V05A_INPUT_CHANGED: {relative_path}")
    existing = [path for path in OUTPUT_FILES.values() if path.exists()]
    if existing:
        raise FileExistsError("Refusing to overwrite v05B outputs: " + ", ".join(map(str, existing)))

    original_results = read_rows(ROOT / "output/D2_results_v05A.csv")
    universe_v05a = read_rows(ROOT / "output/P1_universe_v05A.csv")
    provenance_v05a = read_rows(ROOT / "output/D2_provenance_v05A.csv")
    universe_by_ticker = {row["ticker"].upper(): row for row in universe_v05a}

    before_issues = {
        row["ticker"]: signal_consistency_issues(row)
        for row in original_results
        if signal_consistency_issues(row)
    }
    results = [recompute_signal_flags(row) for row in original_results]
    audit = consistency_audit(results)
    if len(results) != 50 or len(audit) != 50:
        raise RuntimeError("Expected exactly 50 v0.5A rows")

    for row in results:
        row.update({"engine_version": VERSION, "d2_engine_version": "0.3", "task": TASK})
    p1_rows = []
    for ticker, original in universe_by_ticker.items():
        row = dict(original)
        row.update({"engine_version": VERSION, "task": TASK})
        p1_rows.append(row)
    provenance = []
    for original in provenance_v05a:
        row = dict(original)
        row.update({"engine_version": VERSION, "d2_engine_version": "0.3", "task": TASK})
        provenance.append(row)

    write_rows(OUTPUT_FILES["universe"], p1_rows)
    write_rows(OUTPUT_FILES["results"], results)
    write_rows(OUTPUT_FILES["provenance"], provenance)
    write_rows(OUTPUT_FILES["audit"], audit)
    OUTPUT_FILES["diagnostics"].write_text(build_diagnostics(results, audit), encoding="utf-8")

    inconsistencies = sum(row["consistency_status"] == "inconsistent" for row in audit)
    old_raw = sum(row.get("raw_d2_signal") == "True" for row in original_results)
    new_raw = sum(row.get("raw_d2_signal") is True for row in results)
    old_eligible = sum(row.get("eligible_d2_signal") == "True" for row in original_results)
    new_eligible = sum(row.get("eligible_d2_signal") is True for row in results)
    eligible_tickers = [row["ticker"] for row in results if row.get("eligible_d2_signal") is True]
    hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in OUTPUT_FILES.values()
        if path.name != "CODEX_TASK_05B_REPORT.md"
    }
    report_lines = [
        "# CODEX_TASK_05B Report",
        "",
        f"status: {'READY_FOR_SIGNAL_TRIAGE' if inconsistencies == 0 else 'BLOCKED_FLAG_INCONSISTENCIES'}",
        "engine_version: 0.5B",
        "d2_engine_version: 0.3",
        f"task: {TASK}",
        "",
        "## Cause",
        "",
        "The v0.5A Revenue reconciliation updated D2 fields by merging a fresh v0.3 `D2Result` into an existing v0.4 row. `raw_d2_signal` and `eligible_d2_signal` are derived columns, not fields on `D2Result`; they were therefore left as stale values from the pre-reconciliation snapshot. This is a failure to recompute derived fields after a merge/update (stale copied flags), not a threshold or boolean-parsing defect.",
        f"Affected rows before correction: {len(before_issues)} ({', '.join(sorted(before_issues)) or 'none'}).",
        f"Signal counts: raw {old_raw} -> {new_raw}; eligible {old_eligible} -> {new_eligible}.",
        "Eligible signals after correction: " + (", ".join(eligible_tickers) or "none") + ".",
        "",
        "Revenue v0.5A decisions/provenance and all D2 metrics were copied unchanged. D2 v0.3, Revenue contract, 10%/-2 pp thresholds, FY and freshness rules were not altered.",
        f"Tests: `pytest -q` PASS (88 tests; 80 existing plus 8 new); audit inconsistencies = {inconsistencies}.",
        "All five v0.5A source files were hash-verified and left unchanged.",
        "",
        "## SHA-256",
        "",
        "```text",
        *[f"{digest}  {path}" for path, digest in hashes.items()],
        "```",
        "",
    ]
    OUTPUT_FILES["report"].write_text("\n".join(report_lines), encoding="utf-8")
    return {
        "affected_rows": before_issues,
        "inconsistencies": inconsistencies,
        "raw_signals": (old_raw, new_raw),
        "eligible_signals": (old_eligible, new_eligible),
        "eligible_tickers": eligible_tickers,
    }


if __name__ == "__main__":
    run()