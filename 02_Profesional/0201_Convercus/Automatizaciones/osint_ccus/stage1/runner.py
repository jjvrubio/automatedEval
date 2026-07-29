"""Stage 1A and 1B orchestration."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Protocol

from .csv_input import InputRow
from .deliverables import publish_stage1_records
from .exporter import export_all
from .policy import (
    StageDecision,
    StagePolicyResult,
    evaluate_criterion,
    evaluate_final_eligibility,
    evaluate_stage1a,
)
from .storage import Stage1Store


class Researcher(Protocol):
    def research_employees(
        self, row: InputRow
    ) -> tuple[dict[str, Any], dict[str, Any]]: ...

    def research_locations(
        self, row: InputRow
    ) -> tuple[dict[str, Any], dict[str, Any]]: ...

    def research_revenue(
        self, row: InputRow
    ) -> tuple[dict[str, Any], dict[str, Any]]: ...


def run_stage1a(
    rows: list[InputRow],
    original_headers: list[str],
    output_dir: Path,
    researcher: Researcher,
    force: bool = False,
    retry_errors: bool = False,
    deliverables_root: Path | None = None,
) -> dict[str, Path]:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with Stage1Store(output_dir / "stage1_state.sqlite3") as store:
        total = len(rows)
        for position, row in enumerate(rows, start=1):
            current_status = store.status(row.record_id)
            if not force and current_status == "ok":
                print(f"[{position}/{total}] Omitida (ya completada): {row.company_name}")
                continue
            if not force and current_status == "error" and not retry_errors:
                print(f"[{position}/{total}] Omitida (error previo): {row.company_name}")
                continue

            print(f"[{position}/{total}] Investigando: {row.company_name}")
            store.mark_running(row)
            try:
                employees, employees_raw = researcher.research_employees(row)
                locations, locations_raw = researcher.research_locations(row)

                employee_policy = evaluate_criterion(employees, threshold=100)
                location_policy = evaluate_criterion(locations, threshold=10)
                stage_policy = evaluate_stage1a(employee_policy, location_policy)
                decision = {
                    "employees_decision": employee_policy.decision.value,
                    "employees_reason": employee_policy.reason,
                    "locations_decision": location_policy.decision.value,
                    "locations_reason": location_policy.reason,
                    "stage1a_decision": stage_policy.decision.value,
                    "stage1a_reason": stage_policy.reason,
                }
                store.save_success(
                    row,
                    employees,
                    locations,
                    decision,
                    [employees_raw, locations_raw],
                )
                print(f"  → {stage_policy.decision.value}")
            except Exception as exc:
                store.save_error(row, repr(exc))
                print(f"  → ERROR: {exc}")

        records = store.records()
        outputs = export_all(records, original_headers, output_dir)
        documents_root = Path(deliverables_root or output_dir / "deliverables")
        publish_stage1_records(records, documents_root)
        outputs["documents_root"] = documents_root
        return outputs


def run_stage1b(
    rows: list[InputRow],
    original_headers: list[str],
    output_dir: Path,
    researcher: Researcher,
    force: bool = False,
    retry_errors: bool = False,
    approve_review: bool = False,
    deliverables_root: Path | None = None,
) -> dict[str, Path]:
    """Research revenue for Stage 1A passes in an existing state database."""
    output_dir = Path(output_dir)
    state_path = output_dir / "stage1_state.sqlite3"
    if not state_path.exists():
        raise FileNotFoundError(
            "No existe stage1_state.sqlite3 en el directorio indicado. "
            "Ejecuta primero la Etapa 1A."
        )

    with Stage1Store(state_path) as store:
        total = len(rows)
        for position, row in enumerate(rows, start=1):
            record = store.record(row.record_id)
            if not record or record.get("status") != "ok":
                print(
                    f"[{position}/{total}] Omitida (1A no completada): "
                    f"{row.company_name}"
                )
                continue
            if not force and record.get("revenue_status") == "ok":
                print(f"[{position}/{total}] Omitida (1B completada): {row.company_name}")
                continue
            if (
                not force
                and record.get("revenue_status") == "error"
                and not retry_errors
            ):
                print(f"[{position}/{total}] Omitida (error 1B previo): {row.company_name}")
                continue

            decision = record.get("decision_json") or {}
            original_value = decision.get("stage1a_decision", "REVIEW_REQUIRED")
            override = original_value == StageDecision.REVIEW_REQUIRED.value and approve_review
            if original_value == StageDecision.PASS_1A.value or override:
                effective_stage1a = StagePolicyResult(
                    StageDecision.PASS_1A,
                    (
                        "Aprobación humana explícita y auditable de la puerta 1A."
                        if override
                        else str(decision.get("stage1a_reason") or "Puerta 1A aprobada.")
                    ),
                )
            else:
                final_value = (
                    StageDecision.INELIGIBLE
                    if original_value == StageDecision.FAIL_1A.value
                    else StageDecision.REVIEW_REQUIRED
                )
                store.save_final_decision(
                    row,
                    {
                        "stage1a_original_decision": original_value,
                        "stage1a_effective_decision": original_value,
                        "stage1a_override": False,
                        "revenue_decision": "",
                        "revenue_reason": "No investigada: la puerta 1A no está aprobada.",
                        "eligibility_decision": final_value.value,
                        "eligibility_reason": "La compañía no supera automáticamente la puerta 1A.",
                    },
                )
                print(f"[{position}/{total}] Omitida por 1A: {row.company_name}")
                continue

            print(f"[{position}/{total}] Investigando facturación: {row.company_name}")
            try:
                revenue, revenue_raw = researcher.research_revenue(row)
                revenue_policy = evaluate_criterion(revenue, threshold=15_000_000)
                final_policy = evaluate_final_eligibility(
                    effective_stage1a, revenue_policy
                )
                final_decision = {
                    "stage1a_original_decision": original_value,
                    "stage1a_effective_decision": StageDecision.PASS_1A.value,
                    "stage1a_override": override,
                    "stage1a_override_reason": (
                        "Aprobación humana solicitada mediante CLI."
                        if override
                        else ""
                    ),
                    "revenue_decision": revenue_policy.decision.value,
                    "revenue_reason": revenue_policy.reason,
                    "eligibility_decision": final_policy.decision.value,
                    "eligibility_reason": final_policy.reason,
                }
                store.save_revenue_success(
                    row, revenue, final_decision, revenue_raw
                )
                print(f"  → {final_policy.decision.value}")
            except Exception as exc:
                store.save_revenue_error(row, repr(exc))
                print(f"  → ERROR 1B: {exc}")

        records = store.records()
        outputs = export_all(records, original_headers, output_dir)
        documents_root = Path(deliverables_root or output_dir / "deliverables")
        publish_stage1_records(records, documents_root)
        outputs["documents_root"] = documents_root
        return outputs
