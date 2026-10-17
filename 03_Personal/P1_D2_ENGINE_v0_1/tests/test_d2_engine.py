import json
from datetime import date
from pathlib import Path

from p1_d2_engine.d2_engine import evaluate_company
from p1_d2_engine.cli import diagnostics_markdown


def fixture(name: str):
    path = Path(__file__).parent / "fixtures" / name
    return json.loads(path.read_text(encoding="utf-8"))


def test_candidate_signal():
    result, provenance = evaluate_company(
        "TEST",
        1,
        fixture("companyfacts_candidate.json"),
        "Test Co",
        as_of=date(2025, 3, 1),
    )
    assert result.status == "candidate"
    assert result.candidate_d2 is True
    assert result.d2_signal is True
    assert result.universe_eligible == "unknown"
    assert result.freshness_status == "fresh"
    assert result.latest_fy_resolution_status == "resolved"
    assert round(result.revenue_growth_fy_yoy, 6) == 0.2
    assert round(result.operating_margin_fy_t_minus_1, 6) == 0.15
    assert round(result.operating_margin_fy_t, 6) == 0.10
    assert round(result.om_delta_pp, 6) == -5.0
    assert len(provenance) == 4


def _annual_rows(values):
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


def _de_like_companyfacts():
    return {
        "facts": {
            "us-gaap": {
                "Revenues": {
                    "units": {"USD": _annual_rows({2023: 100, 2024: 120, 2025: 140})}
                },
                "OperatingIncomeLoss": {
                    "units": {"USD": _annual_rows({2023: 15, 2024: 12})}
                },
            }
        }
    }


def test_de_like_latest_fy_missing_operating_income_is_unresolved():
    result, _ = evaluate_company(
        "DE_FIXTURE",
        2,
        _de_like_companyfacts(),
        as_of=date(2026, 10, 6),
    )

    assert result.status == "latest_fy_unresolved"
    assert result.selected_fy_t_end == "2024-12-31"
    assert result.latest_annual_period_end_observed == "2025-12-31"
    assert result.freshness_status == "latest_fy_unresolved"
    assert result.latest_fy_resolution_status == "latest_fy_unresolved"
    assert result.missing_latest_fy_metric == "OperatingIncomeLoss"
    assert result.d2_signal is False
    assert result.revenue_growth_fy_yoy is None


def test_latest_fy_unresolved_is_excluded_from_fresh_coverage():
    fresh, _ = evaluate_company(
        "FRESH",
        1,
        fixture("companyfacts_candidate.json"),
        as_of=date(2025, 3, 1),
    )
    unresolved, _ = evaluate_company(
        "DE_FIXTURE",
        2,
        _de_like_companyfacts(),
        as_of=date(2026, 10, 6),
    )

    diagnostics = diagnostics_markdown(
        2,
        [fresh.to_row(), unresolved.to_row()],
        "2026-10-06T12:00:00+00:00",
    )

    assert "nominal_processable: 2" in diagnostics
    assert "fresh_processable: 1" in diagnostics
    assert "nominal_coverage: 100.0%" in diagnostics
    assert "fresh_coverage: 50.0%" in diagnostics
    assert "latest_fy_unresolved count: 1" in diagnostics
    assert "| DE_FIXTURE | 2024-12-31 | 2025-12-31 | OperatingIncomeLoss |" in diagnostics
    assert "## Latest FY unresolved" in diagnostics
    assert "\nFAIL\n" in diagnostics


def test_absolute_age_over_365_days_can_still_be_fresh():
    result, _ = evaluate_company(
        "LAST_FY",
        4,
        fixture("companyfacts_candidate.json"),
        as_of=date(2026, 10, 6),
    )

    assert result.selected_period_age_days > 365
    assert result.selected_fy_t_end == result.latest_annual_period_end_observed
    assert result.status == "candidate"
    assert result.freshness_status == "fresh"
    assert result.d2_signal is True


def test_nvda_like_latest_pair_remains_fresh():
    result, _ = evaluate_company(
        "LATEST_PAIR",
        5,
        fixture("companyfacts_candidate.json"),
        as_of=date(2026, 10, 6),
    )

    assert result.latest_fy_resolution_status == "resolved"
    assert result.selected_fy_t_end == result.latest_annual_period_end_observed
    assert result.freshness_status == "fresh"
    assert result.d2_signal is True


def test_missing_operating_income_is_not_reconstructed():
    revenue = _annual_rows({2023: 100, 2024: 120})
    facts = {
        "facts": {
            "us-gaap": {
                "Revenues": {"units": {"USD": revenue}},
                "NetIncomeLoss": {"units": {"USD": _annual_rows({2023: 8, 2024: 9})}},
            }
        }
    }

    result, _ = evaluate_company("NOOP", 3, facts, as_of=date(2025, 3, 1))

    assert result.status == "missing_operating_income"
    assert result.missing_latest_fy_metric == "OperatingIncomeLoss"
    assert result.operating_income_fy_t is None
    assert result.d2_signal is False
