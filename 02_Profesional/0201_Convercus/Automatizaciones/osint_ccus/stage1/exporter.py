"""Export Stage 1 state to user-facing CSV, JSONL, and Markdown."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ADDED_COLUMNS = [
    "Research Record Id",
    "Research Status",
    "Canonical Company Name",
    "Validated # Employees",
    "Employees Value Type",
    "Employees As Of",
    "Employees Scope",
    "Employees Validation",
    "Employees Validation Reason",
    "Original Number of Retail Locations",
    "Retail Locations Value Type",
    "Locations As Of",
    "Locations Scope",
    "Locations Validation",
    "Locations Validation Reason",
    "Stage 1A Decision",
    "Stage 1A Reason",
    "Validated Annual Revenue EUR",
    "Revenue Value Type",
    "Revenue Fiscal Year",
    "Revenue Metric",
    "Revenue Original Value",
    "Revenue Original Currency",
    "Revenue Scope",
    "Revenue Validation",
    "Revenue Validation Reason",
    "Stage 1A Override",
    "Eligibility Decision",
    "Eligibility Reason",
    "Research Sources",
    "Research Error",
    "Revenue Research Error",
]


def _display_value(result: dict[str, Any] | None) -> str:
    if not result:
        return ""
    value_type = result.get("value_type")
    if value_type in {"exact", "estimate"} and result.get("value") is not None:
        return str(result["value"])
    if value_type == "minimum" and result.get("lower_bound") is not None:
        return f">={result['lower_bound']}"
    if (
        value_type == "range"
        and result.get("lower_bound") is not None
        and result.get("upper_bound") is not None
    ):
        return f"{result['lower_bound']}-{result['upper_bound']}"
    return ""


def _sources(*results: dict[str, Any] | None) -> str:
    urls: list[str] = []
    for result in results:
        for evidence in (result or {}).get("evidence", []):
            url = str(evidence.get("url") or "").strip()
            if url and url not in urls:
                urls.append(url)
    return " | ".join(urls)


def _enriched_row(record: dict[str, Any]) -> dict[str, Any]:
    original = dict(record.get("input_json") or {})
    employees = record.get("employees_json") or {}
    locations = record.get("locations_json") or {}
    decision = record.get("decision_json") or {}
    revenue = record.get("revenue_json") or {}
    final_decision = record.get("final_decision_json") or {}

    original_locations = original.get("Number of Retail Locations", "")
    validated_locations = _display_value(locations)
    if validated_locations:
        original["Number of Retail Locations"] = validated_locations

    original.update(
        {
            "Research Record Id": record["record_id"],
            "Research Status": record["status"],
            "Canonical Company Name": employees.get("canonical_company_name")
            or locations.get("canonical_company_name")
            or "",
            "Validated # Employees": _display_value(employees),
            "Employees Value Type": employees.get("value_type", ""),
            "Employees As Of": employees.get("as_of_date", ""),
            "Employees Scope": employees.get("scope", ""),
            "Employees Validation": decision.get("employees_decision", ""),
            "Employees Validation Reason": decision.get("employees_reason", ""),
            "Original Number of Retail Locations": original_locations,
            "Retail Locations Value Type": locations.get("value_type", ""),
            "Locations As Of": locations.get("as_of_date", ""),
            "Locations Scope": locations.get("scope", ""),
            "Locations Validation": decision.get("locations_decision", ""),
            "Locations Validation Reason": decision.get("locations_reason", ""),
            "Stage 1A Decision": decision.get("stage1a_decision", ""),
            "Stage 1A Reason": decision.get("stage1a_reason", ""),
            "Validated Annual Revenue EUR": _display_value(revenue),
            "Revenue Value Type": revenue.get("value_type", ""),
            "Revenue Fiscal Year": revenue.get("fiscal_year", ""),
            "Revenue Metric": revenue.get("metric", ""),
            "Revenue Original Value": revenue.get("original_value", ""),
            "Revenue Original Currency": revenue.get("original_currency", ""),
            "Revenue Scope": revenue.get("scope", ""),
            "Revenue Validation": final_decision.get("revenue_decision", ""),
            "Revenue Validation Reason": final_decision.get("revenue_reason", ""),
            "Stage 1A Override": (
                "YES" if final_decision.get("stage1a_override") is True else ""
            ),
            "Eligibility Decision": final_decision.get(
                "eligibility_decision", ""
            ),
            "Eligibility Reason": final_decision.get("eligibility_reason", ""),
            "Research Sources": _sources(employees, locations, revenue),
            "Research Error": record.get("error") or "",
            "Revenue Research Error": record.get("revenue_error") or "",
        }
    )
    return original


def export_all(
    records: list[dict[str, Any]],
    original_headers: list[str],
    output_dir: Path,
) -> dict[str, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    headers = list(original_headers)
    for column in ADDED_COLUMNS:
        if column not in headers:
            headers.append(column)

    enriched_rows = [_enriched_row(record) for record in records]
    enriched_path = output_dir / "stage1_enriched.csv"
    _write_csv(enriched_path, headers, enriched_rows)

    passed_path = output_dir / "stage1_pass_1a.csv"
    passed_rows = [
        row for row in enriched_rows if row.get("Stage 1A Decision") == "PASS_1A"
    ]
    _write_csv(passed_path, headers, passed_rows)

    eligible_path = output_dir / "stage1_eligible.csv"
    eligible_rows = [
        row for row in enriched_rows if row.get("Eligibility Decision") == "ELIGIBLE"
    ]
    _write_csv(eligible_path, headers, eligible_rows)

    audit_path = output_dir / "stage1_audit.jsonl"
    with audit_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    summary_path = output_dir / "stage1_summary.md"
    _write_summary(
        summary_path, records, enriched_path, passed_path, eligible_path
    )

    return {
        "enriched": enriched_path,
        "passed": passed_path,
        "eligible": eligible_path,
        "audit": audit_path,
        "summary": summary_path,
    }


def _write_csv(
    path: Path,
    headers: list[str],
    rows: list[dict[str, Any]],
) -> None:
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _write_summary(
    path: Path,
    records: list[dict[str, Any]],
    enriched_path: Path,
    passed_path: Path,
    eligible_path: Path,
) -> None:
    status_counts = Counter(record["status"] for record in records)
    decision_counts = Counter(
        (record.get("decision_json") or {}).get("stage1a_decision", "NO_DECISION")
        for record in records
    )
    eligibility_counts = Counter(
        (record.get("final_decision_json") or {}).get(
            "eligibility_decision", "PENDING_1B"
        )
        for record in records
    )
    lines = [
        "# Resumen de elegibilidad — Etapa 1",
        "",
        f"**Generado:** {datetime.now(timezone.utc).isoformat()}",
        f"**Compañías registradas:** {len(records)}",
        "",
        "## Decisiones",
        "",
        "| Decisión | Compañías |",
        "|---|---:|",
    ]
    lines.extend(
        f"| {decision} | {count} |"
        for decision, count in sorted(decision_counts.items())
    )
    lines.extend(
        [
            "",
            "## Elegibilidad final",
            "",
            "| Decisión | Compañías |",
            "|---|---:|",
        ]
    )
    lines.extend(
        f"| {decision} | {count} |"
        for decision, count in sorted(eligibility_counts.items())
    )
    lines.extend(
        [
            "",
            "## Estado técnico",
            "",
            "| Estado | Compañías |",
            "|---|---:|",
        ]
    )
    lines.extend(
        f"| {status} | {count} |" for status, count in sorted(status_counts.items())
    )
    lines.extend(
        [
            "",
            "## Archivos",
            "",
            f"- CSV enriquecido: `{enriched_path.name}`",
            f"- Compañías que superan 1A: `{passed_path.name}`",
            f"- Compañías elegibles tras 1B: `{eligible_path.name}`",
            "- Auditoría completa: `stage1_audit.jsonl`",
            "",
            "## Alcance",
            "",
            "La puerta 1A exige más de 100 empleados y más de 10 puntos de venta "
            "o servicio. La puerta 1B exige facturación estrictamente superior a "
            "15 millones de euros. Solo una compañía que supera ambas queda como "
            "`ELIGIBLE` para entrar al proceso OSINT posterior.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
