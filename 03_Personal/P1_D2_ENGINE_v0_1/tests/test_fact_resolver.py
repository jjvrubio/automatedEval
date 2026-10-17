from p1_d2_engine.fact_resolver import (
    annual_series,
    resolve_fact_selection,
    resolve_revenue,
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


def companyfacts(revenue_tags, operating_income):
    us_gaap = {
        tag: {"units": {"USD": annual_rows(values)}}
        for tag, values in revenue_tags.items()
    }
    us_gaap["OperatingIncomeLoss"] = {"units": {"USD": annual_rows(operating_income)}}
    return {"facts": {"us-gaap": us_gaap}}


def test_latest_filing_wins_for_same_period():
    facts = {
        "facts": {
            "us-gaap": {
                "OperatingIncomeLoss": {
                    "units": {
                        "USD": [
                            {
                                "start": "2023-01-01",
                                "end": "2023-12-31",
                                "val": 100,
                                "accn": "a",
                                "fy": 2023,
                                "fp": "FY",
                                "form": "10-K",
                                "filed": "2024-02-01",
                            },
                            {
                                "start": "2023-01-01",
                                "end": "2023-12-31",
                                "val": 110,
                                "accn": "b",
                                "fy": 2023,
                                "fp": "FY",
                                "form": "10-K/A",
                                "filed": "2024-03-01",
                            },
                        ]
                    }
                }
            }
        }
    }
    series = annual_series(facts, "operating_income", "OperatingIncomeLoss")
    obs = next(iter(series.values()))
    assert obs.value == 110
    assert obs.form == "10-K/A"


def test_conflicting_revenue_tags_are_ambiguous():
    rows_a = [
        {
            "start": "2023-01-01",
            "end": "2023-12-31",
            "val": 1000,
            "accn": "a",
            "fy": 2023,
            "fp": "FY",
            "form": "10-K",
            "filed": "2024-02-01",
        },
        {
            "start": "2024-01-01",
            "end": "2024-12-31",
            "val": 1100,
            "accn": "b",
            "fy": 2024,
            "fp": "FY",
            "form": "10-K",
            "filed": "2025-02-01",
        },
    ]
    rows_b = [dict(r) for r in rows_a]
    rows_b[1]["val"] = 900
    operating_rows = [dict(row, val=100) for row in rows_a]
    facts = {
        "facts": {
            "us-gaap": {
                "RevenueFromContractWithCustomerExcludingAssessedTax": {
                    "units": {"USD": rows_a}
                },
                "Revenues": {"units": {"USD": rows_b}},
                "OperatingIncomeLoss": {"units": {"USD": operating_rows}},
            }
        }
    }
    resolution = resolve_revenue(facts)
    assert resolution.status == "ambiguous_revenue_tag"
    selection = resolve_fact_selection(facts)
    assert selection.status == "ambiguous_revenue_tag"
    assert selection.conflict == {
        "period": "2024-01-01:2024-12-31",
        "tag_a": "RevenueFromContractWithCustomerExcludingAssessedTax",
        "value_a": 1100.0,
        "tag_b": "Revenues",
        "value_b": 900.0,
    }


def test_including_assessed_tax_standard_total_is_accepted():
    facts = companyfacts(
        {"RevenueFromContractWithCustomerIncludingAssessedTax": {2023: 1000, 2024: 1200}},
        {2023: 100, 2024: 110},
    )

    resolution = resolve_revenue(facts)
    selection = resolve_fact_selection(facts)

    assert resolution.status == "ok"
    assert resolution.tag == "RevenueFromContractWithCustomerIncludingAssessedTax"
    assert selection.status == "ok"
    assert selection.revenue_tag == "RevenueFromContractWithCustomerIncludingAssessedTax"


def test_new_revenue_tag_takes_over_after_historical_transition():
    facts = companyfacts(
        {
            "RevenueFromContractWithCustomerExcludingAssessedTax": {
                2019: 95,
                2020: 100,
                2021: 110,
            },
            "Revenues": {2020: 80, 2021: 90, 2022: 120, 2023: 130},
        },
        {2019: 9, 2020: 10, 2021: 11, 2022: 12, 2023: 13},
    )

    selection = resolve_fact_selection(facts)

    assert selection.status == "ok"
    assert selection.revenue_tag == "Revenues"
    assert [key[1] for key in selection.pair] == ["2022-12-31", "2023-12-31"]
    assert all(selection.revenue_series[key].tag == "Revenues" for key in selection.pair)


def test_selects_latest_pair_common_to_revenue_and_operating_income():
    facts = companyfacts(
        {"Revenues": {2020: 100, 2021: 110, 2022: 120, 2023: 130, 2024: 140}},
        {2021: 11, 2022: 12, 2023: 13},
    )

    selection = resolve_fact_selection(facts)

    assert selection.status == "ok"
    assert [key[1] for key in selection.pair] == ["2022-12-31", "2023-12-31"]
