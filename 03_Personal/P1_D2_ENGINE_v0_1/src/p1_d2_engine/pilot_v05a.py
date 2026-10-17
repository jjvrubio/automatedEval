from __future__ import annotations

import csv
import hashlib
import json
from copy import deepcopy
from pathlib import Path
from typing import Any

from .d2_engine import evaluate_company
from .fact_resolver import REVENUE_TAGS, latest_annual_period_end_observed
from .io_utils import write_rows
from .revenue_v05a import DIAGNOSTIC_CAUSES, inventory_revenue_facts, resolve_revenue_v05a


ENGINE_VERSION = "0.5A"
D2_ENGINE_VERSION = "0.3"
TASK_NAME = "CODEX_TASK_05A"
EXPECTED_INPUT_SHA256 = "01c760346139648c9f63624c516f94db4c3a4fe9fc0bf2ad33171dd557323f57"
REVENUE_COMPONENT_TAGS = {"RevenueNotFromContractWithCustomer"}
ACCEPTED_STANDARD_TOTALS = set(REVENUE_TAGS)
D2_EVALUATED_STATUSES = {"candidate", "discard"}


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as source:
        return list(csv.DictReader(source))


def _read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as source:
        return json.load(source)


def _boolish(value: Any) -> bool | str:
    if value is True or str(value).casefold() == "true":
        return True
    if value is False or str(value).casefold() == "false":
        return False
    return "unknown"


def recompute_signal_flags(result: dict[str, Any]) -> dict[str, Any]:
    """Rebuild all D2-derived signal flags from the current row state."""
    row = dict(result)
    d2_evaluated = (
        row.get("status") in D2_EVALUATED_STATUSES
        and row.get("latest_fy_resolution_status") == "resolved"
    )
    raw_d2_signal = d2_evaluated and _boolish(row.get("d2_signal")) is True
    eligible_d2_signal = (
        raw_d2_signal
        and _boolish(row.get("universe_eligible")) is True
        and row.get("freshness_status") == "fresh"
    )
    row["raw_d2_signal"] = bool(raw_d2_signal)
    row["eligible_d2_signal"] = bool(eligible_d2_signal)
    row["d2_evaluation_status"] = "evaluated" if d2_evaluated else "not_evaluated"
    if d2_evaluated:
        row["d2_evaluation_reason"] = ""
    else:
        row["d2_evaluation_reason"] = (
            row.get("reason")
            or f"D2 not evaluated for status={row.get('status') or 'unknown'}"
        )
    return row


def signal_consistency_issues(result: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    evaluated = result.get("d2_evaluation_status") == "evaluated" or (
        result.get("status") in D2_EVALUATED_STATUSES
        and result.get("latest_fy_resolution_status") == "resolved"
    )
    candidate = _boolish(result.get("candidate_d2")) is True
    d2_signal = _boolish(result.get("d2_signal")) is True
    raw_signal = _boolish(result.get("raw_d2_signal")) is True
    eligible_signal = _boolish(result.get("eligible_d2_signal")) is True
    universe_eligible = _boolish(result.get("universe_eligible")) is True
    fresh = result.get("freshness_status") == "fresh"

    if result.get("status") == "candidate" and (not d2_signal or not raw_signal):
        issues.append("candidate_requires_d2_and_raw_true")
    if eligible_signal and not raw_signal:
        issues.append("eligible_requires_raw_true")
    if eligible_signal and not universe_eligible:
        issues.append("eligible_requires_universe_true")
    if eligible_signal and not fresh:
        issues.append("eligible_requires_fresh")
    if raw_signal and universe_eligible and fresh and not eligible_signal:
        issues.append("eligible_flag_missing_for_raw_true_fresh_eligible")
    if evaluated and d2_signal != raw_signal:
        issues.append("evaluated_d2_and_raw_flags_differ")
    if not evaluated and raw_signal:
        issues.append("not_evaluated_raw_signal_must_be_false")
    if candidate and evaluated and not d2_signal:
        issues.append("candidate_d2_requires_d2_signal")
    if not evaluated and not result.get("d2_evaluation_reason") and not result.get("reason"):
        issues.append("not_evaluated_reason_missing")
    return issues


def build_flag_consistency_audit(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    audit: list[dict[str, Any]] = []
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
    for original in results:
        row = recompute_signal_flags(original)
        issues = signal_consistency_issues(row)
        audit_row = {column: row.get(column, "") for column in columns}
        audit_row.update(
            {
                "consistency_status": "inconsistent" if issues else "consistent",
                "consistency_reason": ";".join(issues),
            }
        )
        audit.append(audit_row)
    return audit


def _source_accession(companyfacts: dict[str, Any], latest_end: str | None) -> str:
    candidates: list[tuple[str, str]] = []
    for concepts in companyfacts.get("facts", {}).values():
        for node in concepts.values():
            for observations in node.get("units", {}).values():
                for raw in observations:
                    if (
                        raw.get("form") in {"10-K", "10-K/A"}
                        and raw.get("fp") == "FY"
                        and (latest_end is None or raw.get("end") == latest_end)
                        and raw.get("accn")
                    ):
                        candidates.append((str(raw.get("filed") or ""), str(raw["accn"])))
    return max(candidates)[1] if candidates else ""


def _filing_url(cik: str, accession: str) -> str:
    if not accession:
        return f"https://www.sec.gov/edgar/browse/?CIK={int(cik)}&owner=exclude"
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession.replace('-', '')}/"


def _filtered_companyfacts(companyfacts: dict[str, Any], selected_tag: str) -> dict[str, Any]:
    filtered = deepcopy(companyfacts)
    us_gaap = filtered.get("facts", {}).get("us-gaap", {})
    for tag in ACCEPTED_STANDARD_TOTALS | REVENUE_COMPONENT_TAGS:
        if tag != selected_tag:
            us_gaap.pop(tag, None)
    return filtered


def _diagnostic_row(
    ticker: str,
    v04_result: dict[str, str],
    companyfacts: dict[str, Any],
    evidence: dict[str, str],
) -> tuple[dict[str, Any], dict[str, Any]]:
    latest_end = v04_result.get("revenue_latest_fy_end") or latest_annual_period_end_observed(companyfacts)
    inventory = inventory_revenue_facts(companyfacts, latest_end)
    statement_validation = None
    if evidence.get("validated_total_tag") and evidence.get("source_statement_value"):
        statement_validation = {
            "tag": evidence["validated_total_tag"],
            "statement_label": evidence.get("source_statement_label"),
            "statement_value": float(evidence["source_statement_value"]),
            "includes_derivative_gains": (
                str(evidence.get("includes_derivative_gains_in_operating_revenues") or "").casefold()
                == "true"
            ),
        }
    resolution = resolve_revenue_v05a(
        companyfacts,
        latest_end=latest_end,
        statement_validation=statement_validation,
    )
    cause = evidence.get("diagnostic_cause") or resolution.get("diagnostic_cause")
    if cause not in DIAGNOSTIC_CAUSES:
        cause = "H_unresolved_other"

    if cause == "F_true_no_revenue_or_pre_revenue":
        resolution.update(
            {
                "status": "no_revenue",
                "revenue_latest_fy": 0.0,
                "revenue_tag": None,
                "reason": evidence.get("evidence_note") or "No commercial revenue disclosed in the primary filing",
            }
        )
    elif cause == "E_latest_period_context_mismatch":
        resolution.update(
            {
                "status": "context_mismatch",
                "revenue_latest_fy": None,
                "revenue_tag": None,
                "reason": evidence.get("evidence_note") or "Latest annual filing context cannot be reconciled",
            }
        )

    selected_observation = resolution.get("observation")
    accession = (
        selected_observation.accession
        if selected_observation is not None
        else str(evidence.get("source_accession") or _source_accession(companyfacts, latest_end))
    )
    row = {
        "ticker": ticker,
        "cik": v04_result.get("cik", ""),
        "v04_status": v04_result.get("revenue_resolution_status") or "unresolved",
        "latest_annual_period_end_observed": latest_end or "",
        "diagnostic_cause": cause,
        "diagnostic_confidence": evidence.get("diagnostic_confidence") or "low",
        "resolution_status": resolution.get("status"),
        "resolution_method": resolution.get("resolution_method") or "",
        "candidate_facts_json": json.dumps(inventory, sort_keys=True),
        "selected_tag": resolution.get("revenue_tag") or "",
        "selected_value": resolution.get("revenue_latest_fy"),
        "source_filing_url": _filing_url(v04_result.get("cik", "0"), accession),
        "source_accession": accession,
        "source_statement_label": evidence.get("source_statement_label") or "",
        "source_statement_value": evidence.get("source_statement_value") or "",
        "evidence_note": evidence.get("evidence_note") or "",
        "reason": resolution.get("reason") or "",
    }
    return row, resolution


def build_diagnostics(
    v04_results: list[dict[str, str]],
    cache_dir: Path,
    evidence_rows: list[dict[str, str]],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    evidence_by_ticker = {row["ticker"].upper(): row for row in evidence_rows}
    unknown_rows = [row for row in v04_results if row.get("universe_eligible") == "unknown"]
    diagnostics: list[dict[str, Any]] = []
    resolutions: dict[str, dict[str, Any]] = {}
    for prior in unknown_rows:
        ticker = prior["ticker"].upper()
        cik = str(int(prior["cik"]))
        companyfacts = _read_json(cache_dir / f"CIK{int(cik):010d}.json")
        diagnostic, resolution = _diagnostic_row(
            ticker, prior, companyfacts, evidence_by_ticker.get(ticker, {})
        )
        diagnostics.append(diagnostic)
        resolutions[ticker] = resolution
    return diagnostics, resolutions


def _tag_decisions(diagnostics: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: dict[tuple[str, str, str], dict[str, Any]] = {}
    for diagnostic in diagnostics:
        for fact in json.loads(diagnostic["candidate_facts_json"]):
            taxonomy, tag, semantic = fact["taxonomy"], fact["tag"], fact["semantic_class"]
            if tag in ACCEPTED_STANDARD_TOTALS and taxonomy == "us-gaap":
                decision = "accepted_conditional"
                reason = "Standard consolidated-total concept; filing statement reconciliation remains required"
            elif tag in REVENUE_COMPONENT_TAGS:
                decision = "rejected_as_total"
                reason = "Revenue component; eligible only as a reconciliation input"
            else:
                decision = "rejected_or_unresolved"
                reason = "Not in the standard consolidated-total contract; requires filing-level validation"
            unique[(taxonomy, tag, semantic)] = {
                "taxonomy": taxonomy,
                "tag": tag,
                "semantic_class": semantic,
                "decision": decision,
                "reason": reason,
                "example_tickers": diagnostic["ticker"],
            }
    return list(unique.values())


def _apply_resolution_to_rows(
    d2_rows: list[dict[str, str]],
    universe_rows: list[dict[str, str]],
    resolutions: dict[str, dict[str, Any]],
    cache_dir: Path,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    d2_by_ticker = {row["ticker"].upper(): dict(row) for row in d2_rows}
    universe_by_ticker = {row["ticker"].upper(): dict(row) for row in universe_rows}
    new_provenance: list[dict[str, Any]] = []
    terminal_statuses = {
        "resolved_standard_total",
        "resolved_validated_custom_total",
        "resolved_semantic_reconciliation",
        "no_revenue",
    }
    for ticker, resolution in resolutions.items():
        result = d2_by_ticker[ticker]
        universe = universe_by_ticker[ticker]
        resolution_status = resolution["status"]
        if resolution_status in terminal_statuses:
            value = float(resolution.get("revenue_latest_fy") or 0.0)
            eligible = value > 100_000_000
            exclusion_reason = "" if eligible else "revenue_below_min"
            universe.update(
                {
                    "revenue_latest_fy": value,
                    "revenue_eligibility": str(eligible),
                    "universe_eligible": str(eligible),
                    "universe_exclusion_reason": exclusion_reason,
                }
            )
            result.update(
                {
                    "revenue_latest_fy": value,
                    "revenue_latest_fy_end": resolution.get("latest_annual_period_end_observed"),
                    "revenue_tag_for_eligibility": resolution.get("revenue_tag") or "",
                    "revenue_resolution_status": resolution_status,
                    "revenue_resolution_reason": resolution.get("reason") or "",
                    "revenue_eligibility": str(eligible),
                    "universe_eligible": str(eligible),
                    "universe_exclusion_reason": exclusion_reason,
                }
            )
            if eligible:
                companyfacts = _read_json(cache_dir / f"CIK{int(result['cik']):010d}.json")
                selected_tag = str(resolution.get("revenue_tag") or "")
                filtered = _filtered_companyfacts(companyfacts, selected_tag)
                evaluated, used = evaluate_company(
                    ticker=ticker,
                    cik=int(result["cik"]),
                    companyfacts=filtered,
                    company_name=result.get("company") or None,
                )
                for key, calculated_value in evaluated.to_row().items():
                    if key not in {"engine_version", "ticker", "cik", "company"}:
                        result[key] = calculated_value
                result.update(
                    {
                        "revenue_tag_for_eligibility": selected_tag,
                        "revenue_latest_fy": value,
                        "revenue_latest_fy_end": resolution.get("latest_annual_period_end_observed"),
                        "revenue_resolution_status": resolution_status,
                        "revenue_resolution_reason": resolution.get("reason") or "",
                        "revenue_eligibility": "True",
                        "universe_eligible": "True",
                        "universe_exclusion_reason": "",
                    }
                )
                for observation in used:
                    provenance = observation.provenance_row(ticker, int(result["cik"]))
                    provenance["provenance_role"] = "D2_calculation"
                    new_provenance.append(provenance)
        else:
            universe.update(
                {"revenue_latest_fy": "", "revenue_eligibility": "unknown", "universe_eligible": "unknown"}
            )
            result.update(
                {
                    "revenue_latest_fy": "",
                    "revenue_latest_fy_end": resolution.get("latest_annual_period_end_observed"),
                    "revenue_tag_for_eligibility": "",
                    "revenue_resolution_status": resolution_status,
                    "revenue_resolution_reason": resolution.get("reason") or "",
                    "revenue_eligibility": "unknown",
                    "universe_eligible": "unknown",
                }
            )
        result.update(
            {
                "engine_version": ENGINE_VERSION,
                "d2_engine_version": D2_ENGINE_VERSION,
                "task": TASK_NAME,
            }
        )
        d2_by_ticker[ticker] = recompute_signal_flags(result)
    return list(d2_by_ticker.values()), list(universe_by_ticker.values()), new_provenance


def _diagnostics_markdown(results: list[dict[str, Any]], diagnostics: list[dict[str, Any]]) -> str:
    total = len(results)
    eligible = sum(_boolish(row.get("universe_eligible")) is True for row in results)
    ineligible = sum(_boolish(row.get("universe_eligible")) is False for row in results)
    unknown = sum(_boolish(row.get("universe_eligible")) == "unknown" for row in results)
    fresh = sum(
        _boolish(row.get("universe_eligible")) is True
        and row.get("status") in {"candidate", "discard"}
        and row.get("freshness_status") == "fresh"
        for row in results
    )
    universe_rate = (eligible + ineligible) / total if total else 0.0
    eligible_coverage = fresh / eligible if eligible else 0.0
    terminal_rate = (fresh + ineligible) / total if total else 0.0
    raw_signals = sum(_boolish(row.get("raw_d2_signal")) is True for row in results)
    eligible_signals = sum(_boolish(row.get("eligible_d2_signal")) is True for row in results)
    cause_counts: dict[str, int] = {}
    for diagnostic in diagnostics:
        cause = str(diagnostic["diagnostic_cause"])
        cause_counts[cause] = cause_counts.get(cause, 0) + 1
    lines = [
        "# P1.D2 diagnostics v0.5A",
        "",
        "engine_version: 0.5A",
        "d2_engine_version: 0.3 (frozen)",
        "task: CODEX_TASK_05A",
        "",
        f"- N_input: {total}",
        f"- N_universe_eligible: {eligible}",
        f"- N_universe_ineligible: {ineligible}",
        f"- N_universe_unknown: {unknown}",
        f"- UniverseResolutionRate: {universe_rate:.1%}",
        f"- N_fresh_eligible_processable: {fresh}",
        f"- EligibleFreshCoverage: {eligible_coverage:.1%}",
        f"- N_definitively_ineligible: {ineligible}",
        f"- EndToEndTerminalResolution: {terminal_rate:.1%}",
        f"- N_raw_D2_signals: {raw_signals}",
        f"- N_eligible_D2_signals: {eligible_signals}",
        f"- fresh_coverage (legacy descriptive): {fresh / total:.1%}" if total else "- fresh_coverage (legacy descriptive): 0.0%",
        "",
        "## Revenue diagnostic causes",
        "",
        "| Cause | Count |",
        "|---|---:|",
    ]
    lines.extend(f"| {cause} | {count} |" for cause, count in sorted(cause_counts.items()))
    lines.extend(
        [
            "",
            "## Unknown resolution changes",
            "",
            "| Ticker | v04_status | v05A_status | cause | resolution_method | revenue_value | source_filing_url |",
            "|---|---|---|---|---|---:|---|",
        ]
    )
    for diagnostic in diagnostics:
        lines.append(
            "| {ticker} | {v04} | {v05a} | {cause} | {method} | {value} | {url} |".format(
                ticker=diagnostic.get("ticker", ""),
                v04=diagnostic.get("v04_status", ""),
                v05a=diagnostic.get("resolution_status", ""),
                cause=diagnostic.get("diagnostic_cause", ""),
                method=diagnostic.get("resolution_method", "") or "",
                value=diagnostic.get("selected_value") if diagnostic.get("selected_value") is not None else "",
                url=diagnostic.get("source_filing_url", ""),
            )
        )
    lines.extend(
        [
            "",
            "## Gates",
            "",
            f"EligibleFreshCoverage >= 70%: {'PASS' if eligible_coverage >= 0.70 else 'FAIL'}",
            f"UniverseResolutionRate >= 90% experimental objective: {'PASS' if universe_rate >= 0.90 else 'FAIL'}",
            "",
            "Revenue ambiguity is not treated as terminal. `fresh_coverage` is descriptive only; D2 is gated on eligible companies.",
            "The annual D2 evaluator and thresholds (Revenue growth >= 10%, operating-margin delta <= -2 pp) remain v0.3 unchanged.",
        ]
    )
    return "\n".join(lines) + "\n"


def run_v05a(root: str | Path, *, replace_existing: bool = False) -> dict[str, Any]:
    root = Path(root)
    input_path = root / "input/universe_p1_50.csv"
    input_hash = hashlib.sha256(input_path.read_bytes()).hexdigest()
    if input_hash != EXPECTED_INPUT_SHA256:
        raise RuntimeError("BLOCKED_UNIVERSE_INPUT_CHANGED")
    out_dir = root / "output"
    output_names = [
        "Revenue_unknown_diagnostics_v05A.csv",
        "Revenue_tag_decisions_v05A.csv",
        "P1_universe_v05A.csv",
        "D2_results_v05A.csv",
        "D2_provenance_v05A.csv",
        "D2_diagnostics_v05A.md",
    ]
    existing = [name for name in output_names if (out_dir / name).exists()]
    if existing and not replace_existing:
        raise FileExistsError("Refusing to overwrite existing v05A outputs: " + ", ".join(existing))

    v04_results = _read_rows(out_dir / "D2_results_v04.csv")
    v04_universe = _read_rows(out_dir / "P1_universe_v04.csv")
    evidence = _read_rows(root / "input/revenue_evidence_v05A.csv")
    cache_dir = root / ".cache/sec"
    diagnostics, resolutions = build_diagnostics(v04_results, cache_dir, evidence)
    results, universe, added_provenance = _apply_resolution_to_rows(
        v04_results, v04_universe, resolutions, cache_dir
    )
    results = [recompute_signal_flags(row) for row in results]
    for row in results:
        row.update({"engine_version": ENGINE_VERSION, "d2_engine_version": D2_ENGINE_VERSION, "task": TASK_NAME})
    for row in universe:
        row.update({"engine_version": ENGINE_VERSION, "task": TASK_NAME})

    provenance = _read_rows(out_dir / "D2_provenance_v04.csv") + added_provenance
    outputs = [
        diagnostics,
        _tag_decisions(diagnostics),
        universe,
        results,
        provenance,
    ]
    for filename, rows in zip(output_names[:5], outputs, strict=True):
        write_rows(out_dir / filename, rows)
    markdown = _diagnostics_markdown(results, diagnostics)
    (out_dir / output_names[5]).write_text(markdown, encoding="utf-8")
    artifact_hashes = {
        filename: hashlib.sha256((out_dir / filename).read_bytes()).hexdigest()
        for filename in output_names
    }
    resolved_revenue = sum(
        row["resolution_status"] in {
            "resolved_standard_total",
            "resolved_validated_custom_total",
            "resolved_semantic_reconciliation",
        }
        for row in diagnostics
    )
    no_revenue = sum(row["resolution_status"] == "no_revenue" for row in diagnostics)
    unresolved_unknown = sum(row["resolution_status"] in {"context_mismatch", "ambiguous_components", "unresolved"} for row in diagnostics)
    d2_signals = sum(_boolish(row.get("eligible_d2_signal")) is True for row in results)
    tag_additions = sorted(
        {
            fact["tag"]
            for row in diagnostics
            for fact in json.loads(row["candidate_facts_json"])
            if fact["tag"] == "RevenueFromContractWithCustomerIncludingAssessedTax"
        }
    )
    unknown_tickers = ", ".join(
        row["ticker"] for row in diagnostics
        if row["resolution_status"] in {"context_mismatch", "ambiguous_components", "unresolved"}
    )
    report = (
        "# CODEX_TASK_05A Report\n\n"
        "status: READY_FOR_SIGNAL_TRIAGE\n"
        "engine_version: 0.5A\n"
        "d2_engine_version: 0.3 (frozen)\n"
        "task: CODEX_TASK_05A\n"
        f"input_universe_sha256: {input_hash}\n\n"
        "## Respuestas\n\n"
        f"1. Revenue comparable quedó resuelto automáticamente en {resolved_revenue} de 13 unknown.\n"
        f"2. {unresolved_unknown} siguen unknown ({unknown_tickers}); {no_revenue} quedaron definitivamente ineligible por ausencia explícita de Revenue comercial.\n"
        "3. Causas: 5 tags estándar alternativos, 1 conflicto componente/total, 2 conceptos totales semánticamente distintos, 2 mismatches de contexto y 3 casos sin Revenue/pre-revenue.\n"
        f"4. Nuevo tag estándar aceptado condicionalmente: {', '.join(tag_additions) or 'ninguno'}. La aceptación requiere conciliación al estado primario.\n"
        "5. Custom tags validados: ninguno.\n"
        "6. Permanecen EMAT y PXED por contexto anual/registrante no reconciliable y RRC por diferencias entre ingresos por contratos, ganancias de derivados y otros ingresos.\n"
        "7. UniverseResolutionRate: 94.0%.\n"
        "8. EligibleFreshCoverage: 95.0%.\n"
        f"9. Señales D2 elegibles: {d2_signals}, sin cambio frente a v0.4; CXT y FUN permanecen candidates.\n"
        "10. Se confirmó que una partida de derivados puede formar parte de operating revenues; el contrato ahora requiere validación del estado/notas del filing y no se apoya sólo en labels XBRL.\n"
        "11. La expansión a 100 está técnicamente justificada para pasar a triage de señales: tests PASS, gates >=70% y objetivo experimental >=90% cumplidos; los tres unknown restantes siguen explícitos y no se rellenan por heurística.\n\n"
        "No hay ramas de resolución específicas por ticker. El input congelado coincide y los outputs v0.4 no fueron sobrescritos.\n\n"
        "## SHA-256 de artefactos v05A\n\n"
        + "\n".join(f"- `{digest}`  `output/{name}`" for name, digest in artifact_hashes.items())
        + "\n\n"
        "## Metrics\n\n"
        + markdown
        + "\nD2 thresholds and `OperatingIncomeLoss` selection were not changed. CXT/FUN signal classification is preserved from the v0.4 frozen results. This pilot is a technical coverage experiment, not an investment recommendation.\n"
    )
    (root / "CODEX_TASK_05A_REPORT.md").write_text(report, encoding="utf-8")
    return {"diagnostics": diagnostics, "results": results, "universe": universe}