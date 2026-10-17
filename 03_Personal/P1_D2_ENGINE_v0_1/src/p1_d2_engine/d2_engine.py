from __future__ import annotations

from datetime import date
from typing import Any

from .fact_resolver import resolve_fact_selection
from .models import D2Result, FactObservation

ENGINE_VERSION = "0.3"


def evaluate_company(
    ticker: str,
    cik: int,
    companyfacts: dict[str, Any],
    company_name: str | None = None,
    as_of: date | None = None,
    revenue_growth_threshold: float = 0.10,
    margin_delta_threshold_pp: float = -2.0,
    strong_growth_threshold: float = 0.20,
    strong_margin_delta_pp: float = -3.0,
) -> tuple[D2Result, list[FactObservation]]:
    as_of = as_of or date.today()
    selection = resolve_fact_selection(companyfacts)
    base_result = {
        "engine_version": ENGINE_VERSION,
        "ticker": ticker,
        "cik": cik,
        "company": company_name,
        "latest_annual_period_end_observed": selection.latest_annual_period_end_observed,
    }

    if selection.status != "ok":
        conflict = selection.conflict or {}
        return (
            D2Result(
                **base_result,
                status=selection.status,
                reason=selection.reason,
                revenue_tag=selection.revenue_tag,
                freshness_status=selection.status,
                latest_fy_resolution_status=selection.status,
                missing_latest_fy_metric=selection.missing_latest_fy_metric,
                ambiguous_period=conflict.get("period"),
                ambiguous_tag_a=conflict.get("tag_a"),
                ambiguous_value_a=conflict.get("value_a"),
                ambiguous_tag_b=conflict.get("tag_b"),
                ambiguous_value_b=conflict.get("value_b"),
                available_operating_income_tags=(
                    ";".join(selection.available_operating_income_tags)
                    if selection.available_operating_income_tags
                    else None
                ),
            ),
            [],
        )

    older_key, newer_key = selection.pair
    r0 = selection.revenue_series[older_key]
    r1 = selection.revenue_series[newer_key]
    oi0 = selection.operating_income_series[older_key]
    oi1 = selection.operating_income_series[newer_key]

    selected_period_age_days = (as_of - date.fromisoformat(r1.end)).days
    latest_observed = selection.latest_annual_period_end_observed
    latest_fy_resolved = latest_observed is not None and r1.end == latest_observed
    freshness_status = "fresh" if latest_fy_resolved else "latest_fy_unresolved"

    if not latest_fy_resolved:
        return (
            D2Result(
                **base_result,
                status="latest_fy_unresolved",
                reason="The selected comparable FY is not the latest annual period observed",
                revenue_tag=selection.revenue_tag,
                fy_t_end=r1.end,
                fy_t_minus_1_end=r0.end,
                selected_fy_t_end=r1.end,
                selected_fy_t_minus_1_end=r0.end,
                selected_period_age_days=selected_period_age_days,
                freshness_status=freshness_status,
                latest_fy_resolution_status="latest_fy_unresolved",
                missing_latest_fy_metric=(
                    selection.missing_latest_fy_metric or "comparable_consecutive_FY_pair"
                ),
            ),
            [],
        )

    if r0.value == 0 or r1.value == 0:
        return (
            D2Result(
                **base_result,
                status="not_comparable",
                reason="Zero revenue in selected period",
                revenue_tag=selection.revenue_tag,
                fy_t_end=r1.end,
                fy_t_minus_1_end=r0.end,
                selected_fy_t_end=r1.end,
                selected_fy_t_minus_1_end=r0.end,
                selected_period_age_days=selected_period_age_days,
                freshness_status=freshness_status,
                latest_fy_resolution_status="resolved",
                missing_latest_fy_metric=None,
            ),
            [],
        )

    growth = r1.value / r0.value - 1.0
    om0 = oi0.value / r0.value
    om1 = oi1.value / r1.value
    delta_pp = 100.0 * (om1 - om0)
    candidate = growth >= revenue_growth_threshold and delta_pp <= margin_delta_threshold_pp
    strong = growth >= strong_growth_threshold and delta_pp <= strong_margin_delta_pp
    d2_signal = candidate

    return (
        D2Result(
            **base_result,
            status="candidate" if candidate else "discard",
            revenue_tag=selection.revenue_tag,
            fy_t_end=r1.end,
            fy_t_minus_1_end=r0.end,
            selected_fy_t_end=r1.end,
            selected_fy_t_minus_1_end=r0.end,
            selected_period_age_days=selected_period_age_days,
            freshness_status=freshness_status,
            latest_fy_resolution_status="resolved",
            missing_latest_fy_metric=None,
            revenue_fy_t=r1.value,
            revenue_fy_t_minus_1=r0.value,
            revenue_growth_fy_yoy=growth,
            operating_income_fy_t=oi1.value,
            operating_income_fy_t_minus_1=oi0.value,
            operating_margin_fy_t=om1,
            operating_margin_fy_t_minus_1=om0,
            om_delta_pp=delta_pp,
            candidate_d2=candidate,
            strong_signal=strong,
            d2_signal=d2_signal,
            universe_eligible="unknown",
        ),
        [r0, r1, oi0, oi1],
    )
