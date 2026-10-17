from p1_d2_engine.pilot_v04 import (
    decorate_result,
    pilot_metrics,
    resolve_latest_fy_revenue,
    should_run_d2,
)


def annual_rows(values):
    return [
        {
            "start": f"{year}-01-01",
            "end": f"{year}-12-31",
            "val": value,
            "accn": f"{year}-K",
            "fy": year,
            "fp": "FY",
            "form": "10-K",
            "filed": f"{year + 1}-02-01",
        }
        for year, value in values.items()
    ]


def facts_with_revenue(revenue_by_tag, other_facts=None):
    facts = {
        tag: {"units": {"USD": annual_rows(values)}}
        for tag, values in revenue_by_tag.items()
    }
    if other_facts:
        facts.update(other_facts)
    return {"facts": {"us-gaap": facts}}


def eligible_universe():
    return {
        "ticker": "TEST",
        "company": "Test Company",
        "country": "US",
        "security_type": "common_stock",
        "sector": "Technology",
        "industry": "Software",
        "market_cap_current": 1_000_000_000,
        "market_cap_currency": "USD",
        "market_cap_as_of": "2026-10-06",
        "market_cap_source": "Nasdaq Stock Screener",
        "operating_business": True,
        "reit": False,
        "bdc": False,
        "pre_revenue": None,
        "universe_input_status": "valid",
        "universe_preeligible": True,
        "universe_exclusion_reason": None,
        "revenue_latest_fy": None,
        "revenue_eligibility": "unknown",
        "universe_eligible": "unknown",
    }


def test_latest_fy_revenue_resolves_without_operating_income():
    result = resolve_latest_fy_revenue(
        facts_with_revenue({"Revenues": {2024: 150_000_000, 2025: 175_000_000}})
    )

    assert result["status"] == "resolved"
    assert result["latest_annual_period_end_observed"] == "2025-12-31"
    assert result["revenue_latest_fy"] == 175_000_000
    assert result["revenue_tag"] == "Revenues"


def test_latest_fy_revenue_requires_latest_annual_end():
    facts = facts_with_revenue(
        {"Revenues": {2024: 150_000_000}},
        {
            "OperatingIncomeLoss": {
                "units": {"USD": annual_rows({2025: 20_000_000})}
            }
        },
    )

    result = resolve_latest_fy_revenue(facts)

    assert result["status"] == "unresolved"
    assert result["latest_annual_period_end_observed"] == "2025-12-31"
    assert result["revenue_latest_fy"] is None


def test_conflicting_latest_revenue_tags_remain_unknown():
    result = resolve_latest_fy_revenue(
        facts_with_revenue(
            {
                "Revenues": {2024: 150_000_000, 2025: 175_000_000},
                "SalesRevenueNet": {2024: 150_000_000, 2025: 140_000_000},
            }
        )
    )

    assert result["status"] == "ambiguous"
    assert result["revenue_latest_fy"] is None


def test_revenue_threshold_is_strictly_greater_than_100m():
    d2 = {
        "engine_version": "0.3",
        "ticker": "TEST",
        "status": "discard",
        "freshness_status": "fresh",
        "d2_signal": False,
    }
    revenue = resolve_latest_fy_revenue(
        facts_with_revenue({"Revenues": {2024: 100_000_000, 2025: 100_000_000}})
    )

    row, universe = decorate_result(d2, eligible_universe(), revenue)

    assert universe["revenue_eligibility"] is False
    assert universe["universe_eligible"] is False
    assert row["engine_version"] == "0.4"
    assert row["d2_engine_version"] == "0.3"


def test_fresh_d2_raw_signal_is_eligible_only_for_true_universe():
    d2 = {
        "engine_version": "0.3",
        "ticker": "TEST",
        "status": "candidate",
        "freshness_status": "fresh",
        "d2_signal": True,
    }
    revenue = resolve_latest_fy_revenue(
        facts_with_revenue({"Revenues": {2024: 110_000_000, 2025: 130_000_000}})
    )

    row, universe = decorate_result(d2, eligible_universe(), revenue)
    assert universe["universe_eligible"] is True
    assert row["raw_d2_signal"] is True
    assert row["eligible_d2_signal"] is True

    d2["freshness_status"] = "latest_fy_unresolved"
    stale_row, _ = decorate_result(d2, eligible_universe(), revenue)
    assert stale_row["raw_d2_signal"] is True
    assert stale_row["eligible_d2_signal"] is False


def test_pilot_metrics_are_conditional_on_eligible_fresh_processable():
    rows = [
        {
            "universe_preeligible": True,
            "universe_eligible": True,
            "status": "candidate",
            "_is_fresh_processable": True,
            "raw_d2_signal": True,
            "eligible_d2_signal": True,
        },
        {
            "universe_preeligible": True,
            "universe_eligible": "unknown",
            "status": "missing_operating_income",
            "_is_fresh_processable": False,
            "raw_d2_signal": False,
            "eligible_d2_signal": False,
        },
    ]

    metrics = pilot_metrics(rows, valid_universe_rows=2)

    assert metrics["N_universe_eligible"] == 1
    assert metrics["N_universe_unknown"] == 1
    assert metrics["N_fresh_eligible_processable"] == 1
    assert metrics["eligible_fresh_coverage"] == 1.0
    assert metrics["d2_signal_rate"] == 1.0


def test_d2_runs_only_after_final_universe_eligibility_is_true():
    assert should_run_d2(True) is True
    assert should_run_d2(False) is False
    assert should_run_d2("unknown") is False