import csv

import pytest

from p1_d2_engine.universe_eligibility import (
    apply_revenue_eligibility,
    eligible_d2_signal,
    prepare_universe_row,
    read_universe_csv,
)


def universe_row(**overrides):
    row = {
        "ticker": "TEST",
        "company": "Test Company",
        "country": "US",
        "security_type": "common_stock",
        "sector": "Technology",
        "industry": "Software",
        "market_cap_current": "1000000000",
        "market_cap_currency": "USD",
        "market_cap_as_of": "2026-10-01",
        "market_cap_source": "verified-provider-export",
        "operating_business": "true",
        "reit": "false",
        "bdc": "false",
        "pre_revenue": "false",
    }
    row.update(overrides)
    return row


def eligible_row(**overrides):
    return apply_revenue_eligibility(
        prepare_universe_row(universe_row(**overrides)),
        250_000_000,
        True,
    )


def test_market_cap_499m_is_below_minimum():
    result = eligible_row(market_cap_current="499000000")
    assert result["universe_preeligible"] is False
    assert result["universe_eligible"] is False
    assert result["universe_exclusion_reason"] == "market_cap_below_min"


def test_market_cap_500m_is_inclusive_minimum():
    assert eligible_row(market_cap_current="500000000")["universe_eligible"] is True


def test_market_cap_20b_is_inclusive_maximum():
    assert eligible_row(market_cap_current="20000000000")["universe_eligible"] is True


def test_market_cap_above_20b_is_excluded():
    result = eligible_row(market_cap_current="20000000001")
    assert result["universe_eligible"] is False
    assert result["universe_exclusion_reason"] == "market_cap_above_max"


def test_financial_sector_is_excluded():
    assert eligible_row(sector="Financials")["universe_exclusion_reason"] == "financial"


def test_reit_is_excluded():
    assert eligible_row(reit="true")["universe_exclusion_reason"] == "reit"


def test_bdc_is_excluded():
    assert eligible_row(bdc="true")["universe_exclusion_reason"] == "bdc"


def test_pre_revenue_is_excluded():
    assert eligible_row(pre_revenue="true")["universe_exclusion_reason"] == "pre_revenue"


def test_latest_fy_revenue_at_100m_is_false():
    prepared = prepare_universe_row(universe_row())
    result = apply_revenue_eligibility(prepared, 100_000_000, True)
    assert result["revenue_eligibility"] is False
    assert result["universe_eligible"] is False
    assert result["universe_exclusion_reason"] == "revenue_below_min"


def test_missing_latest_fy_revenue_remains_unknown():
    prepared = prepare_universe_row(universe_row())
    result = apply_revenue_eligibility(prepared, None, None)
    assert result["revenue_eligibility"] == "unknown"
    assert result["universe_eligible"] == "unknown"


def test_unknown_pre_revenue_is_preserved_without_rejecting_preeligibility():
    result = prepare_universe_row(universe_row(pre_revenue="unknown"))

    assert result["pre_revenue"] is None
    assert result["universe_input_status"] == "valid"
    assert result["universe_preeligible"] is True
    assert result["universe_eligible"] == "unknown"


def test_fresh_d2_signal_and_eligible_universe_is_eligible_signal():
    assert eligible_d2_signal(True, True, "fresh") is True


def test_unknown_universe_is_not_an_eligible_signal():
    assert eligible_d2_signal(True, "unknown", "fresh") is False


def test_unresolved_latest_fy_is_not_an_eligible_signal():
    assert eligible_d2_signal(True, True, "latest_fy_unresolved") is False


def test_invalid_market_cap_currency_and_security_type_are_explicit():
    assert prepare_universe_row(
        universe_row(market_cap_current="")
    )["universe_input_status"] == "missing_market_cap"
    assert prepare_universe_row(
        universe_row(market_cap_currency="EUR")
    )["universe_input_status"] == "unsupported_currency"
    assert prepare_universe_row(
        universe_row(security_type="mystery_security")
    )["universe_input_status"] == "invalid_security_type"


def test_universe_csv_requires_50_unique_rows_and_full_schema(tmp_path):
    path = tmp_path / "universe.csv"
    fieldnames = list(universe_row())
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(universe_row(ticker=f"TICKER{i}") for i in range(50))

    rows = read_universe_csv(path)

    assert len(rows) == 50
    assert rows[0]["market_cap_current"] == "1000000000"


def test_universe_csv_rejects_wrong_row_count(tmp_path):
    path = tmp_path / "universe.csv"
    fieldnames = list(universe_row())
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(universe_row())

    with pytest.raises(ValueError, match="exactly 50"):
        read_universe_csv(path)