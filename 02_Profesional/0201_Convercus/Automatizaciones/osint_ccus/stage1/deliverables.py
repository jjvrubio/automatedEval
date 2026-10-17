"""Per-company Stage 1 Markdown deliverables."""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .presentation import effective_criterion_decision, original_decision_note


def resolve_deliverables_root(
    csv_path: Path,
    override: Path | None = None,
) -> Path:
    if override is not None:
        return Path(override).expanduser().resolve()
    return Path(csv_path).expanduser().resolve().parent


def company_deliverable_dirs(
    root: Path, company_name: str
) -> dict[str, Path]:
    company = Path(root) / safe_company_folder(company_name)
    return {
        "company": company,
        "stage1": company / "01 - Elegibilidad",
        "stage2": company / "02 - Potencialidad",
        "research": company / "02 - Potencialidad" / "Investigación",
        "sources": company / "02 - Potencialidad" / "Fuentes aportadas",
    }


def safe_company_folder(value: str) -> str:
    cleaned = unicodedata.normalize("NFC", str(value))
    cleaned = re.sub(r"[\x00-\x1f/:\\\\]+", " - ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")
    return cleaned[:150] or "Empresa sin nombre"


def publish_stage1_records(
    records: list[dict[str, Any]],
    root: Path,
) -> list[Path]:
    paths: list[Path] = []
    for record in records:
        eligibility = {
            "employees": record.get("employees_json") or {},
            "locations": record.get("locations_json") or {},
            "revenue": record.get("revenue_json") or {},
            "decision": record.get("decision_json") or {},
            "final_decision": record.get("final_decision_json") or {},
        }
        paths.append(
            write_eligibility_report(
                root,
                str(record["company_name"]),
                str(record["record_id"]),
                eligibility,
            )
        )
    return paths


def write_eligibility_report(
    root: Path,
    company_name: str,
    record_id: str,
    eligibility: dict[str, Any],
) -> Path:
    stage1_dir = company_deliverable_dirs(root, company_name)["stage1"]
    stage1_dir.mkdir(parents=True, exist_ok=True)
    path = stage1_dir / "Resultado Etapa 1.md"
    employees = eligibility.get("employees") or {}
    locations = eligibility.get("locations") or {}
    revenue = eligibility.get("revenue") or {}
    decision = eligibility.get("decision") or {}
    final = eligibility.get("final_decision") or {}
    final_label = final.get("eligibility_decision") or _pending_label(decision)
    lines = [
        "---",
        f'company: "{_yaml(company_name)}"',
        f"record_id: {record_id}",
        f"generated_utc: {datetime.now(timezone.utc).isoformat()}",
        "stage: 1",
        f"eligibility_decision: {final_label}",
        "---",
        "",
        f"# Resultado de elegibilidad: {company_name}",
        "",
        "| Criterio | Valor validado | Decisión |",
        "|---|---:|---|",
        f"| Empleados | {_value(employees)} | "
        f"{effective_criterion_decision(eligibility, 'employees')} |",
        f"| Puntos de venta/servicio | {_value(locations)} | "
        f"{effective_criterion_decision(eligibility, 'locations')} |",
        f"| Facturación anual EUR | {_value(revenue)} | "
        f"{final.get('revenue_decision') or 'PENDING_1B'} |",
        f"| **Elegibilidad final** | | **{final_label}** |",
        "",
    ]
    note = original_decision_note(eligibility)
    if final.get("eligibility_reason"):
        lines.extend(["## Motivo", "", str(final["eligibility_reason"]), ""])
    elif decision.get("stage1a_reason"):
        lines.extend(["## Resultado 1A", "", str(decision["stage1a_reason"]), ""])
    if note:
        lines.extend(
            [
                "## Revisión de la puerta 1A",
                "",
                note,
                "",
                "Las diferencias entre cifras se conservan en la evidencia como "
                "trazabilidad, pero no se muestran como conflicto cuando no "
                "cambian el resultado del umbral.",
                "",
            ]
        )
    lines.extend(
        [
            "## Trazabilidad",
            "",
            "La evidencia completa y las respuestas estructuradas se conservan "
            "en el estado técnico reanudable de `osint_ccus`.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _pending_label(decision: dict[str, Any]) -> str:
    stage1a = decision.get("stage1a_decision")
    if stage1a == "PASS_1A":
        return "PENDING_1B"
    return str(stage1a or "PENDING")


def _value(result: dict[str, Any]) -> str:
    value_type = result.get("value_type")
    if value_type == "exact" and result.get("value") is not None:
        return str(result["value"])
    if result.get("lower_bound") is not None:
        return f">= {result['lower_bound']}"
    if result.get("upper_bound") is not None:
        return f"<= {result['upper_bound']}"
    return "No validado"


def _yaml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')
