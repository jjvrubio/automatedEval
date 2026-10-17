from __future__ import annotations

from collections import Counter
from typing import Any

from .fact_resolver import (
    REVENUE_TAGS,
    annual_series,
    latest_annual_period_end_observed,
)
from .universe_eligibility import eligible_d2_signal


ENGINE_VERSION = "0.4"
TASK_NAME = "CODEX_TASK_04"
REVENUE_TAG_TOLERANCE = 0.005
FRESH_D2_STATUSES = {"candidate", "discard"}


def resolve_latest_fy_revenue(companyfacts: dict[str, Any]) -> dict[str, Any]:
    """Resolve a single current FY revenue fact without synthesizing or merging tags."""
    latest_end = latest_annual_period_end_observed(companyfacts)
    candidates_by_tag = {
        tag: annual_series(companyfacts, "revenue", tag)
        for tag in REVENUE_TAGS
    }
    observations = [
        observation
        for series in candidates_by_tag.values()
        for observation in series.values()
        if observation.end == latest_end
    ]
    if latest_end is None or not observations:
        return {
            "status": "unresolved",
            "reason": "No allowed annual Revenue fact at the latest observed annual period",
            "latest_annual_period_end_observed": latest_end,
            "revenue_latest_fy": None,
            "revenue_tag": None,
            "observation": None,
        }

    period_keys = {observation.period_key for observation in observations}
    if len(period_keys) != 1:
        return {
            "status": "ambiguous",
            "reason": "Multiple annual Revenue period starts share the latest period end",
            "latest_annual_period_end_observed": latest_end,
            "revenue_latest_fy": None,
            "revenue_tag": None,
            "observation": None,
        }

    values = [observation.value for observation in observations]
    scale = max(max(abs(value) for value in values), 1.0)
    if max(values) - min(values) > REVENUE_TAG_TOLERANCE * scale:
        return {
            "status": "ambiguous",
            "reason": "Conflicting allowed annual Revenue tags at the latest period",
            "latest_annual_period_end_observed": latest_end,
            "revenue_latest_fy": None,
            "revenue_tag": None,
            "observation": None,
        }

    tag_order = {tag: index for index, tag in enumerate(REVENUE_TAGS)}
    selected = min(observations, key=lambda observation: tag_order[observation.tag])
    return {
        "status": "resolved",
        "reason": None,
        "latest_annual_period_end_observed": latest_end,
        "revenue_latest_fy": selected.value,
        "revenue_tag": selected.tag,
        "observation": selected,
    }


def decorate_result(
    d2_row: dict[str, Any],
    prepared_universe_row: dict[str, Any],
    revenue_resolution: dict[str, Any] | None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Attach v0.4 universe eligibility and pilot-only signal fields to frozen v0.3 output."""
    universe = dict(prepared_universe_row)
    if revenue_resolution and revenue_resolution["status"] == "resolved":
        revenue_value = revenue_resolution["revenue_latest_fy"]
        compatible = True
    else:
        revenue_value = None
        compatible = None

    from .universe_eligibility import apply_revenue_eligibility

    universe = apply_revenue_eligibility(universe, revenue_value, compatible)
    row = dict(d2_row)
    raw_signal = row.get("d2_signal") is True
    fresh = row.get("freshness_status") == "fresh"
    universe_state = universe.get("universe_eligible", "unknown")
    eligible_signal = eligible_d2_signal(raw_signal, universe_state, row.get("freshness_status"))

    row.update(
        {
            "engine_version": ENGINE_VERSION,
            "d2_engine_version": "0.3",
            "task": TASK_NAME,
            "universe_preeligible": universe.get("universe_preeligible"),
            "universe_exclusion_reason": universe.get("universe_exclusion_reason"),
            "revenue_latest_fy": universe.get("revenue_latest_fy"),
            "revenue_latest_fy_end": (
                revenue_resolution.get("latest_annual_period_end_observed")
                if revenue_resolution
                else None
            ),
            "revenue_tag_for_eligibility": (
                revenue_resolution.get("revenue_tag") if revenue_resolution else None
            ),
            "revenue_resolution_status": (
                revenue_resolution.get("status") if revenue_resolution else "unresolved"
            ),
            "revenue_resolution_reason": (
                revenue_resolution.get("reason") if revenue_resolution else "SEC facts unavailable"
            ),
            "revenue_eligibility": universe.get("revenue_eligibility", "unknown"),
            "universe_eligible": universe_state,
            "raw_d2_signal": raw_signal,
            "eligible_d2_signal": eligible_signal,
            "freshness_status": row.get("freshness_status"),
            "_is_fresh_processable": (
                row.get("status") in FRESH_D2_STATUSES and fresh
            ),
        }
    )
    return row, universe


def should_run_d2(universe_eligible: bool | str) -> bool:
    return universe_eligible is True


def pilot_metrics(results: list[dict[str, Any]], valid_universe_rows: int) -> dict[str, Any]:
    total = len(results)
    preeligible = sum(row.get("universe_preeligible") is True for row in results)
    eligible = sum(row.get("universe_eligible") is True for row in results)
    unknown = sum(row.get("universe_eligible") == "unknown" for row in results)
    fresh_processable = sum(bool(row.get("_is_fresh_processable")) for row in results)
    fresh_eligible_processable = sum(
        bool(row.get("_is_fresh_processable")) and row.get("universe_eligible") is True
        for row in results
    )
    raw_signals = sum(row.get("raw_d2_signal") is True for row in results)
    eligible_signals = sum(row.get("eligible_d2_signal") is True for row in results)
    statuses = Counter(str(row.get("status") or "unknown") for row in results)
    latest_fy_unresolved = statuses.get("latest_fy_unresolved", 0)
    ambiguous_revenue = statuses.get("ambiguous_revenue_tag", 0)
    missing_operating_income = statuses.get("missing_operating_income", 0)
    return {
        "N_input": total,
        "N_valid_universe_rows": valid_universe_rows,
        "N_preeligible": preeligible,
        "N_universe_eligible": eligible,
        "N_universe_unknown": unknown,
        "N_fresh_eligible_processable": fresh_eligible_processable,
        "N_fresh_processable": fresh_processable,
        "N_latest_fy_unresolved": latest_fy_unresolved,
        "N_ambiguous_revenue_tag": ambiguous_revenue,
        "N_missing_operating_income": missing_operating_income,
        "N_raw_D2_signals": raw_signals,
        "N_eligible_D2_signals": eligible_signals,
        "fresh_coverage": fresh_processable / total if total else 0.0,
        "eligible_fresh_coverage": fresh_eligible_processable / eligible if eligible else None,
        "d2_signal_rate": eligible_signals / fresh_eligible_processable
        if fresh_eligible_processable
        else None,
        "status_counts": statuses,
    }