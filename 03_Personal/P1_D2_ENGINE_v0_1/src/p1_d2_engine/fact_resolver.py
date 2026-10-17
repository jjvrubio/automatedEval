from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any

from .models import FactObservation
from .validators import consecutive_annual_periods, is_annual_duration


REVENUE_TAGS = (
    "RevenueFromContractWithCustomerExcludingAssessedTax",
    "RevenueFromContractWithCustomerIncludingAssessedTax",
    "Revenues",
    "SalesRevenueNet",
)
OPERATING_INCOME_TAG = "OperatingIncomeLoss"
ALLOWED_FORMS = {"10-K", "10-K/A"}


@dataclass
class RevenueResolution:
    status: str
    tag: str | None
    series: dict[tuple[str, str], FactObservation]
    reason: str | None = None
    pair: list[tuple[str, str]] | None = None
    conflict: dict[str, Any] | None = None


@dataclass
class FactSelection:
    status: str
    revenue_tag: str | None
    revenue_series: dict[tuple[str, str], FactObservation]
    operating_income_series: dict[tuple[str, str], FactObservation]
    pair: list[tuple[str, str]]
    latest_annual_period_end_observed: str | None
    missing_latest_fy_metric: str | None = None
    reason: str | None = None
    conflict: dict[str, Any] | None = None
    available_operating_income_tags: list[str] | None = None


def _parse_fact(metric: str, tag: str, unit: str, raw: dict[str, Any]) -> FactObservation | None:
    start = raw.get("start")
    end = raw.get("end")
    if not start or not end:
        return None
    form = raw.get("form")
    fp = raw.get("fp")
    if form not in ALLOWED_FORMS or fp != "FY":
        return None
    if not is_annual_duration(start, end):
        return None
    try:
        value = float(raw["val"])
    except (KeyError, TypeError, ValueError):
        return None
    return FactObservation(
        metric=metric,
        tag=tag,
        unit=unit,
        start=start,
        end=end,
        value=value,
        form=form,
        filed=str(raw.get("filed") or ""),
        accession=str(raw.get("accn") or ""),
        fy=int(raw["fy"]) if raw.get("fy") is not None else None,
        fp=fp,
    )


def annual_series(
    companyfacts: dict[str, Any], metric: str, tag: str, unit: str = "USD"
) -> dict[tuple[str, str], FactObservation]:
    node = companyfacts.get("facts", {}).get("us-gaap", {}).get(tag, {})
    rows = node.get("units", {}).get(unit, [])
    series: dict[tuple[str, str], FactObservation] = {}
    for raw in rows:
        obs = _parse_fact(metric, tag, unit, raw)
        if obs is None:
            continue
        key = obs.period_key
        current = series.get(key)
        # Same economic period may be repeated/restated in later filings.
        if current is None or (obs.filed, obs.accession) > (current.filed, current.accession):
            series[key] = obs
    return series


def _annual_observation(metric: str, tag: str, unit: str, raw: dict[str, Any]) -> FactObservation | None:
    return _parse_fact(metric, tag, unit, raw)


def latest_annual_period_end_observed(companyfacts: dict[str, Any], unit: str = "USD") -> str | None:
    latest: str | None = None
    us_gaap = companyfacts.get("facts", {}).get("us-gaap", {})
    for tag, node in us_gaap.items():
        for raw in node.get("units", {}).get(unit, []):
            obs = _annual_observation("observed", tag, unit, raw)
            if obs is None:
                continue
            if latest is None or date.fromisoformat(obs.end) > date.fromisoformat(latest):
                latest = obs.end
    return latest


def _latest_two_keys(series: dict[tuple[str, str], FactObservation]) -> list[tuple[str, str]]:
    keys = sorted(series, key=lambda k: date.fromisoformat(k[1]))
    for idx in range(len(keys) - 1, 0, -1):
        newer = keys[idx]
        older = keys[idx - 1]
        if consecutive_annual_periods(older[1], newer[1]):
            return [older, newer]
    return []


def revenue_series_by_tag(
    companyfacts: dict[str, Any],
) -> dict[str, dict[tuple[str, str], FactObservation]]:
    return {
        tag: annual_series(companyfacts, "revenue", tag)
        for tag in REVENUE_TAGS
        if annual_series(companyfacts, "revenue", tag)
    }


def _conflicting_revenue_tags(
    candidates: dict[str, dict[tuple[str, str], FactObservation]],
    tolerance: float = 0.005,
    periods: set[tuple[str, str]] | None = None,
) -> dict[str, Any] | None:
    tags = list(candidates)
    for idx, tag_a in enumerate(tags):
        for tag_b in tags[idx + 1 :]:
            common = sorted(
                set(candidates[tag_a]).intersection(candidates[tag_b])
                & periods
                if periods is not None
                else set(candidates[tag_a]).intersection(candidates[tag_b]),
                key=lambda k: date.fromisoformat(k[1]),
                reverse=True,
            )
            for key in common:
                a = candidates[tag_a][key]
                b = candidates[tag_b][key]
                base = max(abs(a.value), abs(b.value), 1.0)
                if abs(a.value - b.value) / base > tolerance:
                    return {
                        "period": f"{key[0]}:{key[1]}",
                        "tag_a": tag_a,
                        "value_a": a.value,
                        "tag_b": tag_b,
                        "value_b": b.value,
                    }
    return None


def resolve_revenue(companyfacts: dict[str, Any], tolerance: float = 0.005) -> RevenueResolution:
    candidates: list[tuple[str, dict[tuple[str, str], FactObservation], list[tuple[str, str]]]] = []
    for tag in REVENUE_TAGS:
        series = annual_series(companyfacts, "revenue", tag)
        pair = _latest_two_keys(series)
        if pair:
            candidates.append((tag, series, pair))

    if not candidates:
        return RevenueResolution("missing_revenue", None, {}, "No usable annual revenue tag")

    conflict = _conflicting_revenue_tags({tag: series for tag, series, _ in candidates}, tolerance)
    if conflict is not None:
        return RevenueResolution(
            "ambiguous_revenue_tag",
            None,
            {},
            (
                "Conflicting revenue tags: "
                f"{conflict['tag_a']} vs {conflict['tag_b']} "
                f"for {conflict['period']}"
            ),
            conflict=conflict,
        )

    primary_tag, primary_series, primary_pair = candidates[0]

    return RevenueResolution("ok", primary_tag, primary_series, pair=primary_pair)


def resolve_operating_income(companyfacts: dict[str, Any]) -> dict[tuple[str, str], FactObservation]:
    return annual_series(companyfacts, "operating_income", OPERATING_INCOME_TAG)


def latest_two_common_periods(
    revenue: dict[tuple[str, str], FactObservation],
    operating_income: dict[tuple[str, str], FactObservation],
) -> list[tuple[str, str]]:
    common = sorted(set(revenue).intersection(operating_income), key=lambda k: date.fromisoformat(k[1]))
    for idx in range(len(common) - 1, 0, -1):
        newer = common[idx]
        older = common[idx - 1]
        if consecutive_annual_periods(older[1], newer[1]):
            return [older, newer]
    return []


def _common_pairs(
    revenue: dict[tuple[str, str], FactObservation],
    operating_income: dict[tuple[str, str], FactObservation],
) -> list[list[tuple[str, str]]]:
    common = sorted(set(revenue).intersection(operating_income), key=lambda k: date.fromisoformat(k[1]))
    pairs: list[list[tuple[str, str]]] = []
    for idx in range(len(common) - 1, 0, -1):
        newer = common[idx]
        older = common[idx - 1]
        if consecutive_annual_periods(older[1], newer[1]):
            pairs.append([older, newer])
    return pairs


def available_operating_income_tags(companyfacts: dict[str, Any]) -> list[str]:
    us_gaap = companyfacts.get("facts", {}).get("us-gaap", {})
    return sorted(tag for tag in us_gaap if "OperatingIncome" in tag or "OperatingLoss" in tag)


def _missing_metrics_at_latest_fy(
    revenue_candidates: dict[str, dict[tuple[str, str], FactObservation]],
    operating_income_series: dict[tuple[str, str], FactObservation],
    latest_end: str | None,
) -> str | None:
    if latest_end is None:
        return "latest_annual_period_end_observed"
    missing: list[str] = []
    if not any(obs.end == latest_end for series in revenue_candidates.values() for obs in series.values()):
        missing.append("Revenue")
    if not any(obs.end == latest_end for obs in operating_income_series.values()):
        missing.append(OPERATING_INCOME_TAG)
    return ";".join(missing) or None


def resolve_fact_selection(companyfacts: dict[str, Any], tolerance: float = 0.005) -> FactSelection:
    latest_observed = latest_annual_period_end_observed(companyfacts)
    revenue_candidates = revenue_series_by_tag(companyfacts)
    if not revenue_candidates:
        return FactSelection(
            status="missing_revenue",
            revenue_tag=None,
            revenue_series={},
            operating_income_series={},
            pair=[],
            latest_annual_period_end_observed=latest_observed,
            missing_latest_fy_metric="Revenue",
            reason="No usable annual revenue tag",
        )

    op_series = resolve_operating_income(companyfacts)
    if not op_series:
        return FactSelection(
            status="missing_operating_income",
            revenue_tag=next(iter(revenue_candidates)),
            revenue_series=next(iter(revenue_candidates.values())),
            operating_income_series={},
            pair=[],
            latest_annual_period_end_observed=latest_observed,
            missing_latest_fy_metric=OPERATING_INCOME_TAG,
            available_operating_income_tags=available_operating_income_tags(companyfacts),
        )

    selectable: list[tuple[date, str, dict[tuple[str, str], FactObservation], list[tuple[str, str]]]] = []
    for tag, revenue_series in revenue_candidates.items():
        for pair in _common_pairs(revenue_series, op_series):
            selectable.append((date.fromisoformat(pair[1][1]), tag, revenue_series, pair))

    if not selectable:
        return FactSelection(
            status="not_comparable",
            revenue_tag=None,
            revenue_series={},
            operating_income_series=op_series,
            pair=[],
            latest_annual_period_end_observed=latest_observed,
            missing_latest_fy_metric=_missing_metrics_at_latest_fy(
                revenue_candidates, op_series, latest_observed
            ),
            reason="No two common consecutive annual periods",
        )

    _, tag, revenue_series, pair = max(selectable, key=lambda item: item[0])
    conflict = _conflicting_revenue_tags(
        revenue_candidates,
        tolerance,
        periods=set(pair),
    )
    if conflict is not None:
        return FactSelection(
            status="ambiguous_revenue_tag",
            revenue_tag=None,
            revenue_series={},
            operating_income_series={},
            pair=[],
            latest_annual_period_end_observed=latest_observed,
            missing_latest_fy_metric=_missing_metrics_at_latest_fy(
                revenue_candidates, op_series, latest_observed
            ),
            reason=(
                "Conflicting revenue tags: "
                f"{conflict['tag_a']} vs {conflict['tag_b']} "
                f"for {conflict['period']}"
            ),
            conflict=conflict,
        )

    return FactSelection(
        status="ok",
        revenue_tag=tag,
        revenue_series=revenue_series,
        operating_income_series=op_series,
        pair=pair,
        latest_annual_period_end_observed=latest_observed,
        missing_latest_fy_metric=_missing_metrics_at_latest_fy(
            revenue_candidates, op_series, latest_observed
        ),
    )
