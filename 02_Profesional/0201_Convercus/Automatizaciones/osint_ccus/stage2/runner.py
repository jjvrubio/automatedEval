"""Stage 2 orchestration with per-agent resumability."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Protocol

from stage1.csv_input import InputRow
from stage1.storage import Stage1Store

from .report import build_potentiality_report
from .storage import Stage2Store
from .deliverables import (
    company_deliverable_dirs,
    snapshot_provided_meddicc,
    write_company_deliverables,
)


CORE_THEMES = ("technology", "corporate", "expansion")


class Researcher(Protocol):
    def research_technology(
        self, row: InputRow, eligibility_context: dict[str, Any]
    ) -> tuple[dict[str, Any], dict[str, Any]]: ...

    def research_corporate(
        self, row: InputRow, eligibility_context: dict[str, Any]
    ) -> tuple[dict[str, Any], dict[str, Any]]: ...

    def research_expansion(
        self, row: InputRow, eligibility_context: dict[str, Any]
    ) -> tuple[dict[str, Any], dict[str, Any]]: ...

def eligible_rows(
    rows: list[InputRow],
    stage1_output_dir: Path,
) -> list[tuple[InputRow, dict[str, Any]]]:
    state_path = Path(stage1_output_dir) / "stage1_state.sqlite3"
    if not state_path.exists():
        raise FileNotFoundError(
            "No existe el estado de Etapa 1 en el directorio indicado."
        )
    selected: list[tuple[InputRow, dict[str, Any]]] = []
    with Stage1Store(state_path) as store:
        for row in rows:
            record = store.record(row.record_id)
            final = (record or {}).get("final_decision_json") or {}
            if final.get("eligibility_decision") == "ELIGIBLE":
                selected.append((row, _eligibility_context(record)))
    return selected


def run_stage2(
    candidates: list[tuple[InputRow, dict[str, Any]]],
    stage1_output_dir: Path,
    researcher: Researcher,
    force: bool = False,
    retry_errors: bool = False,
    provided_meddicc: dict[str, str] | None = None,
    use_provided_meddicc_as_context: bool = False,
    deliverables_root: Path | None = None,
) -> dict[str, Path]:
    output_dir = Path(stage1_output_dir)
    deliverables_root = Path(deliverables_root or output_dir / "deliverables")
    state_path = output_dir / "stage2_state.sqlite3"
    report_paths: list[Path] = []
    if provided_meddicc and len(candidates) != 1:
        raise ValueError(
            "Un MEDDICC/MEDDPICC aportado exige seleccionar exactamente "
            "una compañía elegible."
        )

    with Stage2Store(state_path) as store:
        total = len(candidates)
        for position, (row, eligibility) in enumerate(candidates, 1):
            print(f"[{position}/{total}] Etapa 2: {row.company_name}")
            store.ensure_row(row, eligibility)
            research_context = dict(eligibility)
            published_meddicc_path = None
            if provided_meddicc:
                source_name = Path(provided_meddicc["source_path"]).name
                snapshot_path = snapshot_provided_meddicc(
                    deliverables_root,
                    row.company_name,
                    source_name,
                    provided_meddicc["markdown"],
                )
                published_meddicc_path = snapshot_path
                store.save_provided_meddicc(
                    row.record_id,
                    Path(provided_meddicc["source_path"]),
                    provided_meddicc["sha256"],
                    provided_meddicc["markdown"],
                    snapshot_path,
                )
                if use_provided_meddicc_as_context:
                    research_context["provided_meddicc"] = {
                        "source_name": source_name,
                        "sha256": provided_meddicc["sha256"],
                        "document": provided_meddicc["markdown"],
                        "evidence_policy": (
                            "Documento aportado por el usuario. Conserva sus "
                            "etiquetas de hecho, interacción interna, señal, "
                            "hipótesis y laguna. No lo presentes como fuente web."
                        ),
                    }
                print(f"  · MEDDPICC aportado: {snapshot_path}")
            existing = store.record(row.record_id) or {}
            existing_technology = existing.get("technology_json") or {}
            if (
                not force
                and existing.get("technology_status") == "ok"
                and existing_technology.get("sector_eligibility")
                in {"excluded", "review"}
            ):
                print(
                    "  → Omitida por sector: "
                    f"{existing_technology.get('sector_eligibility')} "
                    f"({existing_technology.get('sector_profile', 'unknown')})."
                )
                continue
            tasks: tuple[
                tuple[
                    str,
                    Callable[
                        [InputRow, dict[str, Any]],
                        tuple[dict[str, Any], dict[str, Any]],
                    ],
                ],
                ...,
            ] = (
                ("technology", researcher.research_technology),
                ("corporate", researcher.research_corporate),
                ("expansion", researcher.research_expansion),
            )
            for theme, method in tasks:
                status = store.theme_status(row.record_id, theme)
                if not force and status == "ok":
                    print(f"  · {theme}: omitido (completado)")
                    continue
                if not force and status == "error" and not retry_errors:
                    print(f"  · {theme}: omitido (error previo)")
                    continue
                print(f"  · {theme}: investigando")
                store.mark_running(row.record_id, theme)
                try:
                    result, raw = method(row, research_context)
                    store.save_theme(row.record_id, theme, result, raw)
                    print(f"    → OK ({result.get('potentiality_score', 0)}/10)")
                    if (
                        theme == "technology"
                        and result.get("sector_eligibility")
                        in {"excluded", "review"}
                    ):
                        break
                except Exception as exc:
                    store.save_error(row.record_id, theme, repr(exc))
                    print(f"    → ERROR: {exc}")

            record = store.record(row.record_id)
            technology = (record or {}).get("technology_json") or {}
            sector_eligibility = technology.get("sector_eligibility")
            if sector_eligibility in {"excluded", "review"}:
                print(
                    "  → Investigación detenida por sector: "
                    f"{sector_eligibility} "
                    f"({technology.get('sector_profile', 'unknown')})."
                )
                continue

            core_complete = record and all(
                record.get(f"{theme}_status") == "ok" for theme in CORE_THEMES
            )
            if core_complete:
                if (
                    published_meddicc_path is None
                    and record.get("provided_meddicc_markdown")
                ):
                    stored_source = Path(
                        str(record.get("provided_meddicc_path") or "")
                    ).name
                    published_meddicc_path = snapshot_provided_meddicc(
                        deliverables_root,
                        row.company_name,
                        stored_source or "MEDDPICC aportado.md",
                        str(record["provided_meddicc_markdown"]),
                    )
                write_company_deliverables(record, deliverables_root)
                report_dir = company_deliverable_dirs(
                    deliverables_root, row.company_name
                )["stage2"]
                report_path = build_potentiality_report(
                    record,
                    report_dir,
                    provided_meddicc_snapshot=published_meddicc_path,
                )
                store.save_report_path(row.record_id, report_path)
                report_paths.append(report_path)
                print(f"  → Informe: {report_path}")
            else:
                print("  → Informe pendiente: faltan investigadores por completar.")

        records = store.records()
        audit_path = output_dir / "stage2_audit.jsonl"
        with audit_path.open("w", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        summary_path = output_dir / "stage2_summary.md"
        _write_summary(summary_path, records)

    outputs = {
        "state": state_path,
        "audit": audit_path,
        "summary": summary_path,
    }
    if len(report_paths) == 1:
        outputs["report"] = report_paths[0]
    return outputs


def _eligibility_context(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "employees": record.get("employees_json"),
        "locations": record.get("locations_json"),
        "revenue": record.get("revenue_json"),
        "decision": record.get("decision_json"),
        "final_decision": record.get("final_decision_json"),
    }


def _write_summary(path: Path, records: list[dict[str, Any]]) -> None:
    complete = sum(
        all(record.get(f"{theme}_status") == "ok" for theme in CORE_THEMES)
        for record in records
    )
    lines = [
        "# Resumen — Etapa 2",
        "",
        f"- Compañías registradas: {len(records)}",
        f"- Informes completos: {complete}",
        f"- Informes pendientes: {len(records) - complete}",
        "",
        "| Compañía | Sector | Tecnología | Corporativo | Expansión | MEDDICC | Informe |",
        "|---|---|---|---|---|---|---|",
    ]
    for record in records:
        report = (
            f"`{record['report_path']}`"
            if record.get("report_path")
            else ""
        )
        lines.append(
            f"| {record['company_name']} | "
            f"{(record.get('technology_json') or {}).get('sector_profile', 'legacy')} | "
            f"{record.get('technology_status') or 'pending'} | "
            f"{record.get('corporate_status') or 'pending'} | "
            f"{record.get('expansion_status') or 'pending'} | "
            f"{record.get('meddicc_status') or 'not_requested'} | {report} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
