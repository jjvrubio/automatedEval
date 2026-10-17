from p1_d2_engine.revenue_v05a import (
    DIAGNOSTIC_CAUSES,
    RESOLUTION_STATUSES,
    inventory_revenue_facts,
    resolve_revenue_v05a,
)
from p1_d2_engine.pilot_v05a import build_diagnostics


def annual(tag, value, *, end="2024-12-31", taxonomy="us-gaap", label=None):
    year = end[:4]
    return {
        "facts": {
            taxonomy: {
                tag: {
                    "label": label or tag,
                    "units": {
                        "USD": [
                            {
                                "start": f"{year}-01-01",
                                "end": end,
                                "val": value,
                                "accn": "0000000000-25-000001",
                                "fy": 2024,
                                "fp": "FY",
                                "form": "10-K",
                                "filed": "2025-02-01",
                            }
                        ]
                    },
                }
            }
        }
    }


def add_concept(facts, taxonomy, tag, value, label=None):
    facts["facts"].setdefault(taxonomy, {})[tag] = annual(
        tag, value, taxonomy=taxonomy, label=label
    )["facts"][taxonomy][tag]
    return facts


def test_alternative_standard_consolidated_total_is_resolved():
    resolution = resolve_revenue_v05a(
        annual("RevenueFromContractWithCustomerIncludingAssessedTax", 125_000_000)
    )

    assert resolution["status"] == "resolved_standard_total"
    assert resolution["revenue_latest_fy"] == 125_000_000


def test_topic606_subset_does_not_replace_total_with_non_topic606_component():
    facts = annual("RevenueFromContractWithCustomerExcludingAssessedTax", 90_000_000)
    add_concept(facts, "us-gaap", "RevenueNotFromContractWithCustomer", 10_000_000)

    resolution = resolve_revenue_v05a(facts)

    assert resolution["status"] == "ambiguous_components"
    assert resolution["revenue_latest_fy"] is None


def test_utility_operating_revenue_total_wins_over_customer_contract_subset():
    facts = annual("Revenues", 596_160_000)
    add_concept(facts, "us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax", 570_510_000)

    resolution = resolve_revenue_v05a(facts)

    assert resolution["status"] == "resolved_semantic_reconciliation"
    assert resolution["revenue_tag"] == "Revenues"


def test_extractives_keep_material_other_income_reconciliation_ambiguous():
    facts = annual("Revenues", 311_551_500)
    add_concept(facts, "us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax", 298_816_400)
    add_concept(facts, "us-gaap", "DerivativeGainLossRevenue", 12_000_000, "Derivative gain included in other income")

    resolution = resolve_revenue_v05a(facts)
    inventory = inventory_revenue_facts(facts)

    assert resolution["status"] == "ambiguous_components"
    assert any(row["semantic_class"] == "other_income_component" for row in inventory)


def test_utility_derivative_inside_operating_revenue_requires_filing_validation():
    facts = annual("Revenues", 596_160_000)
    add_concept(facts, "us-gaap", "RevenueFromContractWithCustomerExcludingAssessedTax", 570_510_000)
    add_concept(facts, "us-gaap", "DerivativeInstrumentsNotDesignatedAsHedgingInstrumentsGainLossNet", 4_180_000)

    unresolved = resolve_revenue_v05a(facts)
    reconciled = resolve_revenue_v05a(
        facts,
        statement_validation={
            "tag": "Revenues",
            "statement_label": "Operating revenues",
            "statement_value": 596_160_000,
            "includes_derivative_gains": True,
        },
    )

    assert unresolved["status"] == "ambiguous_components"
    assert reconciled["status"] == "resolved_semantic_reconciliation"
    assert reconciled["revenue_tag"] == "Revenues"


def test_custom_total_requires_filing_level_exact_reconciliation():
    facts = annual("CustomConsolidatedRevenue", 50_000_000, taxonomy="jjvr")
    resolution = resolve_revenue_v05a(
        facts,
        latest_end="2024-12-31",
        validated_custom_total={
            "taxonomy": "jjvr",
            "tag": "CustomConsolidatedRevenue",
            "accession": "0000000000-25-000001",
            "statement_value": 50_000_000,
        },
    )

    assert resolution["status"] == "resolved_validated_custom_total"
    assert resolution["resolution_method"] == "validated_custom_total"


def test_unvalidated_custom_tag_is_not_selected_as_total():
    resolution = resolve_revenue_v05a(
        annual("CustomConsolidatedRevenue", 50_000_000, taxonomy="jjvr")
    )

    assert resolution["status"] == "unresolved"
    assert resolution["revenue_latest_fy"] is None


def test_component_only_fact_is_not_selected_as_consolidated_total():
    resolution = resolve_revenue_v05a(
        annual("ProductRevenue", 50_000_000, label="Revenue by Product Segment")
    )

    assert resolution["status"] == "unresolved"


def test_conflicting_same_period_standard_totals_remain_ambiguous():
    facts = annual("Revenues", 100_000_000)
    add_concept(facts, "us-gaap", "SalesRevenueNet", 90_000_000)

    resolution = resolve_revenue_v05a(facts)

    assert resolution["status"] == "ambiguous_components"


def test_latest_annual_period_is_mandatory():
    facts = annual("Revenues", 100_000_000, end="2023-12-31")
    facts["facts"]["us-gaap"]["OperatingIncomeLoss"] = annual(
        "OperatingIncomeLoss", 1, end="2024-12-31"
    )["facts"]["us-gaap"]["OperatingIncomeLoss"]

    resolution = resolve_revenue_v05a(facts, latest_end="2024-12-31")

    assert resolution["status"] == "context_mismatch"


def test_status_and_cause_vocabularies_are_explicit():
    assert "resolved_semantic_reconciliation" in RESOLUTION_STATUSES
    assert "ambiguous_components" in RESOLUTION_STATUSES
    assert len(DIAGNOSTIC_CAUSES) == 8


def test_all_13_pilot_unknowns_receive_a_diagnostic_cause(tmp_path):
    tickers = ("AAON", "BV", "EMAT", "EVRG", "FRNM", "HYMC", "IDT", "IMVT", "LFUS", "MATW", "PXED", "RRC", "WEX")
    causes = (
        "A_alternative_standard_total_revenue_tag",
        "A_alternative_standard_total_revenue_tag",
        "E_latest_period_context_mismatch",
        "D_multiple_total_concepts_semantically_different",
        "F_true_no_revenue_or_pre_revenue",
        "F_true_no_revenue_or_pre_revenue",
        "A_alternative_standard_total_revenue_tag",
        "F_true_no_revenue_or_pre_revenue",
        "A_alternative_standard_total_revenue_tag",
        "A_alternative_standard_total_revenue_tag",
        "E_latest_period_context_mismatch",
        "D_multiple_total_concepts_semantically_different",
        "C_component_vs_total_conflict",
    )
    v04_rows = []
    evidence = []
    for index, ticker in enumerate(tickers, 1):
        cik = 1_000_000 + index
        v04_rows.append(
            {
                "ticker": ticker,
                "cik": str(cik),
                "universe_eligible": "unknown",
                "revenue_latest_fy_end": "2024-12-31",
            }
        )
        (tmp_path / f"CIK{cik:010d}.json").write_text(
            __import__("json").dumps(annual("Revenues", 200_000_000)), encoding="utf-8"
        )
        evidence.append(
            {
                "ticker": ticker,
                "diagnostic_cause": causes[index - 1],
                "diagnostic_confidence": "high",
                "source_statement_label": "Revenue",
                "source_statement_value": "200000000",
                "evidence_note": "Primary filing reviewed",
            }
        )

    diagnostics, _ = build_diagnostics(v04_rows, tmp_path, evidence)

    assert {row["ticker"] for row in diagnostics} == set(tickers)
    assert all(row["diagnostic_cause"] in DIAGNOSTIC_CAUSES for row in diagnostics)
    assert len({row["diagnostic_cause"] for row in diagnostics}) >= 5


def test_resolver_has_no_ticker_specific_branches():
    from pathlib import Path

    source = Path(__file__).parents[1] / "src/p1_d2_engine/revenue_v05a.py"

    assert not any(
        ticker in source.read_text(encoding="utf-8")
        for ticker in ("AAON", "BV", "EMAT", "EVRG", "FRNM", "HYMC", "IDT", "IMVT", "LFUS", "MATW", "PXED", "RRC", "WEX")
    )


def test_coverage_metrics_use_eligible_and_input_denominators():
    from p1_d2_engine.revenue_v05a import coverage_metrics

    metrics = coverage_metrics(
        [
            {"universe_eligible": True, "_is_fresh_processable": True},
            {"universe_eligible": "unknown", "_is_fresh_processable": False},
            {"universe_eligible": False, "definitively_ineligible": True},
        ]
    )

    assert metrics["UniverseResolutionRate"] == 2 / 3
    assert metrics["EligibleFreshCoverage"] == 1.0
    assert metrics["EndToEndTerminalResolution"] == 2 / 3