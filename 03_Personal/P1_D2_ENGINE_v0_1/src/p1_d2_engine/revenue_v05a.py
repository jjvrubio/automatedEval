from __future__ import annotations

import re
from datetime import date
from typing import Any

from .fact_resolver import (
    ALLOWED_FORMS,
    REVENUE_TAGS,
    _parse_fact,
    annual_series,
    latest_annual_period_end_observed,
)


RESOLUTION_STATUSES = {
    "resolved_standard_total",
    "resolved_validated_custom_total",
    "resolved_semantic_reconciliation",
    "ambiguous_components",
    "no_revenue",
    "context_mismatch",
    "unresolved",
}
DIAGNOSTIC_CAUSES = {
    "A_alternative_standard_total_revenue_tag",
    "B_custom_total_revenue_tag",
    "C_component_vs_total_conflict",
    "D_multiple_total_concepts_semantically_different",
    "E_latest_period_context_mismatch",
    "F_true_no_revenue_or_pre_revenue",
    "G_filing_or_taxonomy_anomaly",
    "H_unresolved_other",
}
REVENUE_WORDS = re.compile(r"revenue|sales|derivative|other income", re.IGNORECASE)
SEGMENT_WORDS = re.compile(r"segment|disaggregat|by product|by geography", re.IGNORECASE)
OTHER_INCOME_WORDS = re.compile(r"derivative|gain.?loss|other income", re.IGNORECASE)
NON_TOPIC606_TAG = "RevenueNotFromContractWithCustomer"
TOTAL_TAGS = set(REVENUE_TAGS)
TOLERANCE = 0.005


def _semantics(tag: str, label: str, taxonomy: str) -> str:
    text = f"{tag} {label}"
    if SEGMENT_WORDS.search(text):
        return "segment_or_component"
    if OTHER_INCOME_WORDS.search(text):
        return "other_income_component"
    if tag == NON_TOPIC606_TAG:
        return "non_topic606_component"
    if "RevenueFromContractWithCustomer" in tag:
        return "topic606_subset"
    if taxonomy == "us-gaap" and tag in TOTAL_TAGS:
        return "consolidated_total"
    if taxonomy != "us-gaap":
        return "unknown_semantics"
    return "unknown_semantics"


def inventory_revenue_facts(
    companyfacts: dict[str, Any], latest_end: str | None = None
) -> list[dict[str, Any]]:
    """Inventory annual revenue/sales facts across taxonomies without selecting them."""
    facts = companyfacts.get("facts", {})
    rows: list[dict[str, Any]] = []
    for taxonomy, concepts in facts.items():
        for tag, node in concepts.items():
            label = str(node.get("label") or node.get("description") or "")
            if not REVENUE_WORDS.search(f"{tag} {label}"):
                continue
            for unit, raw_rows in node.get("units", {}).items():
                for raw in raw_rows:
                    observation = _parse_fact("revenue_candidate", tag, unit, raw)
                    if observation is None or (latest_end and observation.end != latest_end):
                        continue
                    rows.append(
                        {
                            "taxonomy": taxonomy,
                            "tag": tag,
                            "label": label,
                            "unit": unit,
                            "start": observation.start,
                            "end": observation.end,
                            "value": observation.value,
                            "form": observation.form,
                            "filed": observation.filed,
                            "accession": observation.accession,
                            "fy": observation.fy,
                            "fp": observation.fp,
                            "semantic_class": _semantics(tag, label, taxonomy),
                        }
                    )
    return sorted(rows, key=lambda row: (row["taxonomy"], row["tag"], row["unit"]))


def _same_value(left: float, right: float, tolerance: float = TOLERANCE) -> bool:
    scale = max(abs(left), abs(right), 1.0)
    return abs(left - right) / scale <= tolerance


def _result(
    status: str,
    latest_end: str | None,
    observation: Any = None,
    reason: str | None = None,
    cause: str = "H_unresolved_other",
    conflict: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return {
        "status": status,
        "resolution_method": status.removeprefix("resolved_") if status.startswith("resolved_") else None,
        "reason": reason,
        "latest_annual_period_end_observed": latest_end,
        "revenue_latest_fy": observation.value if observation is not None else None,
        "revenue_tag": observation.tag if observation is not None else None,
        "observation": observation,
        "diagnostic_cause": cause,
        "conflict": conflict,
    }


def resolve_revenue_v05a(
    companyfacts: dict[str, Any],
    *,
    latest_end: str | None = None,
    validated_custom_total: dict[str, Any] | None = None,
    statement_validation: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve a consolidated annual total; custom concepts require filing-level evidence."""
    latest_end = latest_end or latest_annual_period_end_observed(companyfacts)
    if latest_end is None:
        return _result("unresolved", None, reason="No validated annual filing context", cause="G_filing_or_taxonomy_anomaly")

    candidates: dict[str, Any] = {}
    for tag in REVENUE_TAGS:
        series = annual_series(companyfacts, "revenue", tag)
        current = [obs for obs in series.values() if obs.end == latest_end]
        if current:
            candidates[tag] = max(current, key=lambda obs: (obs.filed, obs.accession))

    if validated_custom_total:
        tag = str(validated_custom_total.get("tag") or "")
        taxonomy = str(validated_custom_total.get("taxonomy") or "")
        accession = str(validated_custom_total.get("accession") or "")
        if taxonomy != "us-gaap" and tag and accession:
            for raw in companyfacts.get("facts", {}).get(taxonomy, {}).get(tag, {}).get("units", {}).get("USD", []):
                obs = _parse_fact("revenue", tag, "USD", raw)
                if obs and obs.end == latest_end and obs.accession == accession:
                    statement_value = validated_custom_total.get("statement_value")
                    if statement_value is not None and float(statement_value) == obs.value:
                        return _result(
                            "resolved_validated_custom_total",
                            latest_end,
                            obs,
                            cause="B_custom_total_revenue_tag",
                        )

    if not candidates:
        older = [
            obs
            for tag in REVENUE_TAGS
            for obs in annual_series(companyfacts, "revenue", tag).values()
        ]
        zero_revenue = [obs for obs in older if obs.end == latest_end and obs.value == 0]
        if zero_revenue:
            return _result(
                "no_revenue",
                latest_end,
                zero_revenue[0],
                reason="Latest annual revenue fact is explicitly zero",
                cause="F_true_no_revenue_or_pre_revenue",
            )
        if older:
            return _result(
                "context_mismatch",
                latest_end,
                reason="Revenue facts exist, but not at the latest observed annual end",
                cause="E_latest_period_context_mismatch",
            )
        return _result(
            "unresolved",
            latest_end,
            reason="No standard annual total or filing-validated custom total",
        )

    observations = list(candidates.values())
    if len(observations) == 1:
        selected = observations[0]
        if selected.tag == "RevenueFromContractWithCustomerExcludingAssessedTax":
            component = annual_series(companyfacts, "revenue", NON_TOPIC606_TAG)
            matching = [obs for obs in component.values() if obs.end == latest_end and obs.value > 0]
            if matching and abs(matching[0].value) / max(abs(selected.value), 1.0) > TOLERANCE:
                return _result(
                    "ambiguous_components",
                    latest_end,
                    reason="Material non-Topic-606 revenue exists without a reconciled consolidated total",
                    cause="C_component_vs_total_conflict",
                )
        return _result(
            "resolved_standard_total",
            latest_end,
            selected,
            cause=(
                "A_alternative_standard_total_revenue_tag"
                if selected.tag not in {
                    "RevenueFromContractWithCustomerExcludingAssessedTax",
                    "Revenues",
                    "SalesRevenueNet",
                }
                else "H_unresolved_other"
            ),
        )

    total = candidates.get("Revenues")
    contracts = [obs for tag, obs in candidates.items() if "RevenueFromContractWithCustomer" in tag]
    if total is not None and contracts:
        other = annual_series(companyfacts, "revenue", NON_TOPIC606_TAG)
        other_obs = next((obs for obs in other.values() if obs.end == latest_end), None)
        if other_obs is not None and _same_value(total.value, contracts[0].value + other_obs.value):
            return _result(
                "resolved_semantic_reconciliation",
                latest_end,
                total,
                cause="C_component_vs_total_conflict",
            )

        material_nonoperating = [
            row
            for row in inventory_revenue_facts(companyfacts, latest_end)
            if row["semantic_class"] == "other_income_component"
            and abs(float(row["value"])) / max(abs(total.value), 1.0) > TOLERANCE
        ]
        if material_nonoperating:
            validation = statement_validation or {}
            validated_operating_total = (
                validation.get("tag") == total.tag
                and "operating revenue" in str(validation.get("statement_label") or "").casefold()
                and validation.get("includes_derivative_gains") is True
                and validation.get("statement_value") is not None
                and float(validation["statement_value"]) == total.value
            )
            if validated_operating_total:
                return _result(
                    "resolved_semantic_reconciliation",
                    latest_end,
                    total,
                    reason="Filing statement and note validate the operating-revenue total and derivative presentation",
                    cause="D_multiple_total_concepts_semantically_different",
                )
            return _result(
                "ambiguous_components",
                latest_end,
                reason="The broader total includes material other-income components",
                cause="C_component_vs_total_conflict",
                conflict={"total_tag": total.tag, "component_tags": [row["tag"] for row in material_nonoperating]},
            )

        return _result(
            "resolved_semantic_reconciliation",
            latest_end,
            total,
            cause="D_multiple_total_concepts_semantically_different",
        )

    if all(_same_value(obs.value, observations[0].value) for obs in observations[1:]):
        selected = total or observations[0]
        return _result("resolved_standard_total", latest_end, selected)

    return _result(
        "ambiguous_components",
        latest_end,
        reason="Multiple same-period standard totals differ without a semantic reconciliation",
        cause="D_multiple_total_concepts_semantically_different",
        conflict={"tags": list(candidates), "values": [obs.value for obs in observations]},
    )


def classify_diagnostic_cause(
    resolution: dict[str, Any], inventory: list[dict[str, Any]], *, filing_context_valid: bool = True
) -> str:
    cause = str(resolution.get("diagnostic_cause") or "H_unresolved_other")
    if cause not in DIAGNOSTIC_CAUSES:
        return "G_filing_or_taxonomy_anomaly" if not filing_context_valid else "H_unresolved_other"
    if not filing_context_valid:
        return "E_latest_period_context_mismatch"
    if not inventory and resolution.get("status") == "no_revenue":
        return "F_true_no_revenue_or_pre_revenue"
    return cause


def coverage_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    eligible = sum(row.get("universe_eligible") is True for row in rows)
    ineligible = sum(row.get("universe_eligible") is False for row in rows)
    unknown = sum(row.get("universe_eligible") == "unknown" for row in rows)
    fresh = sum(row.get("_is_fresh_processable") is True and row.get("universe_eligible") is True for row in rows)
    definitive = sum(row.get("definitively_ineligible") is True for row in rows)
    return {
        "N_input": total,
        "N_universe_eligible": eligible,
        "N_universe_ineligible": ineligible,
        "N_universe_unknown": unknown,
        "UniverseResolutionRate": (eligible + ineligible) / total if total else 0.0,
        "N_fresh_eligible_processable": fresh,
        "EligibleFreshCoverage": fresh / eligible if eligible else None,
        "N_definitively_ineligible": definitive,
        "EndToEndTerminalResolution": (fresh + definitive) / total if total else 0.0,
        "fresh_coverage": sum(row.get("_is_fresh_processable") is True for row in rows) / total if total else 0.0,
    }