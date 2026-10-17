from datetime import datetime, timezone
from collections import Counter

from p1_d2_engine.nasdaq_universe import classify_source_row, select_diverse_universe
from p1_d2_engine.nasdaq_universe_r1 import (
    BUCKET_NAMES,
    market_cap_bucket,
    make_selection_key,
    select_balanced_pilot,
)
from p1_d2_engine.nasdaq_universe_r2 import apply_entity_structure, apply_entity_structure_to_rows


MODIFIED_AT = datetime(2026, 10, 6, tzinfo=timezone.utc)


def source_row(
    ticker="TEST",
    cap="1000000000.00",
    name="Test Operating Co. Common Stock",
    country="United States",
    sector="Technology",
    industry="Software",
):
    return {
        "Symbol": ticker,
        "Name": name,
        "Market Cap": cap,
        "Country": country,
        "Sector": sector,
        "Industry": industry,
    }


def classify(**overrides):
    return classify_source_row(
        source_row(**overrides),
        "nasdaq_screener.csv",
        "a" * 64,
        MODIFIED_AT,
    )


def test_cap_below_minimum_is_excluded():
    result = classify(cap="499999999")
    assert result["universe_preeligible"] == "false"
    assert result["universe_exclusion_reason"] == "market_cap_below_min"


def test_cap_at_minimum_is_included():
    assert classify(cap="500000000")["universe_preeligible"] == "true"


def test_cap_at_maximum_is_included():
    assert classify(cap="20000000000")["universe_preeligible"] == "true"


def test_cap_above_maximum_is_excluded():
    result = classify(cap="20000000001")
    assert result["universe_preeligible"] == "false"
    assert result["universe_exclusion_reason"] == "market_cap_above_max"


def test_financial_sector_is_excluded():
    result = classify(sector="Finance", industry="Major Banks")
    assert result["financial_sector"] == "true"
    assert result["universe_preeligible"] == "false"
    assert "financial" in result["universe_exclusion_reason"]


def test_reit_is_excluded_with_explicit_evidence():
    result = classify(name="Example REIT Inc. Common Stock", sector="Real Estate", industry="REIT")
    assert result["reit"] == "true"
    assert result["universe_preeligible"] == "false"


def test_bdc_is_excluded_with_explicit_evidence():
    result = classify(name="Example BDC Inc. Common Stock")
    assert result["bdc"] == "true"
    assert result["universe_preeligible"] == "false"


def test_etf_or_fund_is_not_common_stock():
    result = classify(name="Example Technology ETF")
    assert result["security_type"] == "non_common_stock"
    assert result["universe_preeligible"] == "false"
    assert "not_common_stock" in result["universe_exclusion_reason"]


def test_unknown_security_type_remains_unknown():
    result = classify(name="Example Operating Company")
    assert result["security_type"] == "unknown"
    assert result["universe_preeligible"] == "unknown"
    assert "security_type_unknown" in result["universe_exclusion_reason"]


def test_unknown_country_remains_unknown():
    result = classify(country="")
    assert result["country"] == "unknown"
    assert result["universe_preeligible"] == "unknown"
    assert "country_unknown" in result["universe_exclusion_reason"]


def eligible_pool(sector_count=6, rows_per_sector=12):
    sectors = ["Technology", "Industrials", "Health Care", "Energy", "Consumer Staples", "Materials"]
    return [
        classify(
            ticker=f"T{sector_index:02d}{row_index:02d}",
            cap=str(1_000_000_000 + row_index * 1_000_000 + sector_index),
            sector=sectors[sector_index],
        )
        for sector_index in range(sector_count)
        for row_index in range(rows_per_sector)
    ]


def test_selection_contains_50_preeligible_rows():
    selected, relaxed = select_diverse_universe(eligible_pool())
    assert len(selected) == 50
    assert relaxed is False


def test_all_selected_rows_are_preeligible():
    selected, _ = select_diverse_universe(eligible_pool())
    assert all(row["universe_preeligible"] == "true" for row in selected)


def test_sector_cap_holds_while_alternatives_exist():
    selected, relaxed = select_diverse_universe(eligible_pool())
    counts = Counter(row["sector_normalized"] for row in selected)
    assert relaxed is False
    assert len(counts) >= 5
    assert max(counts.values()) <= 12


def test_selection_is_deterministic():
    rows = eligible_pool()
    first, _ = select_diverse_universe(rows)
    second, _ = select_diverse_universe(list(reversed(rows)))
    assert [row["ticker"] for row in first] == [row["ticker"] for row in second]


def r1_candidates(rows_per_sector_per_bucket=2):
    caps = {
        "B1_0_5_1B": 750_000_000,
        "B2_1_2B": 1_500_000_000,
        "B3_2_5B": 3_500_000_000,
        "B4_5_10B": 7_500_000_000,
        "B5_10_20B": 15_000_000_000,
    }
    sectors = [f"Sector {index:02d}" for index in range(10)]
    rows = []
    for bucket_index, bucket in enumerate(BUCKET_NAMES):
        for sector_index, sector in enumerate(sectors):
            for row_index in range(rows_per_sector_per_bucket):
                rows.append(
                    {
                        "ticker": f"T{bucket_index:02d}{sector_index:02d}{row_index:02d}",
                        "sector_normalized": sector,
                        "market_cap_current": str(caps[bucket]),
                        "universe_preeligible": "true",
                    }
                )
    return rows


def test_r1_market_cap_bucket_boundaries():
    assert market_cap_bucket("500000000") == "B1_0_5_1B"
    assert market_cap_bucket("999999999") == "B1_0_5_1B"
    assert market_cap_bucket("1000000000") == "B2_1_2B"
    assert market_cap_bucket("2000000000") == "B3_2_5B"
    assert market_cap_bucket("5000000000") == "B4_5_10B"
    assert market_cap_bucket("10000000000") == "B5_10_20B"
    assert market_cap_bucket("20000000000") == "B5_10_20B"


def test_r1_selects_ten_per_bucket_and_exactly_50():
    annotated, selected, targets = select_balanced_pilot(r1_candidates(), "a" * 64)

    assert targets == {bucket: 10 for bucket in BUCKET_NAMES}
    assert len(selected) == 50
    assert sum(row["selected_for_pilot"] == "true" for row in annotated) == 50
    assert Counter(row["market_cap_bucket"] for row in selected) == Counter(
        {bucket: 10 for bucket in BUCKET_NAMES}
    )


def test_r1_selected_rows_are_eligible_and_within_range():
    _, selected, _ = select_balanced_pilot(r1_candidates(), "a" * 64)
    assert all(row["universe_preeligible"] == "true" for row in selected)
    assert all(500_000_000 <= int(row["market_cap_current"]) <= 20_000_000_000 for row in selected)


def test_r1_respects_sector_diversity_controls():
    _, selected, _ = select_balanced_pilot(r1_candidates(), "a" * 64)
    counts = Counter(row["sector_normalized"] for row in selected)
    assert len(counts) >= 8
    assert max(counts.values()) <= 8


def test_r1_selection_is_independent_of_input_order():
    rows = r1_candidates()
    _, first, _ = select_balanced_pilot(rows, "a" * 64)
    _, shuffled, _ = select_balanced_pilot(list(reversed(rows)), "a" * 64)
    assert {row["ticker"] for row in first} == {row["ticker"] for row in shuffled}


def test_r1_hash_selection_does_not_sort_by_market_cap_within_bucket():
    rows = r1_candidates(rows_per_sector_per_bucket=4)
    for index, row in enumerate(rows):
        bucket = row["market_cap_bucket"] if "market_cap_bucket" in row else None
        if bucket is None:
            bucket = market_cap_bucket(row["market_cap_current"])
        low, high = {
            "B1_0_5_1B": (510_000_000, 990_000_000),
            "B2_1_2B": (1_010_000_000, 1_990_000_000),
            "B3_2_5B": (2_010_000_000, 4_990_000_000),
            "B4_5_10B": (5_010_000_000, 9_990_000_000),
            "B5_10_20B": (10_010_000_000, 19_990_000_000),
        }[bucket]
        row["market_cap_current"] = str(high - (index % 4) * (high - low) // 3)

    mutated = [dict(row) for row in rows]
    for index, row in enumerate(mutated):
        bucket = market_cap_bucket(row["market_cap_current"])
        low, high = {
            "B1_0_5_1B": (510_000_000, 990_000_000),
            "B2_1_2B": (1_010_000_000, 1_990_000_000),
            "B3_2_5B": (2_010_000_000, 4_990_000_000),
            "B4_5_10B": (5_010_000_000, 9_990_000_000),
            "B5_10_20B": (10_010_000_000, 19_990_000_000),
        }[bucket]
        row["market_cap_current"] = str(low + (index % 4) * (high - low) // 3)

    _, first, _ = select_balanced_pilot(rows, "b" * 64)
    _, second, _ = select_balanced_pilot(mutated, "b" * 64)
    assert {row["ticker"] for row in first} == {row["ticker"] for row in second}


def test_r1_selection_key_uses_source_sha_and_ticker():
    import hashlib

    source_sha = "c" * 64
    ticker = "abcd"
    assert make_selection_key(source_sha, ticker) == hashlib.sha256(
        f"{source_sha}:ABCD".encode("utf-8")
    ).hexdigest()


def audit_row(company, sector="Energy", ticker="TEST"):
    return {
        "ticker": ticker,
        "company": company,
        "sector": sector,
        "industry": "Common equity",
        "security_type": "common_stock",
        "operating_business": "true",
        "financial_sector": "false",
        "reit": "false",
        "bdc": "false",
        "pre_revenue": "unknown",
        "universe_preeligible": "true",
        "universe_exclusion_reason": "",
    }


def test_sabine_royalty_trust_is_excluded_despite_nasdaq_common_stock_label():
    result = apply_entity_structure(audit_row("Sabine Royalty Trust Common Stock", ticker="SBR"))
    assert result["entity_structure"] == "royalty_trust"
    assert result["security_type"] == "non_common_stock"
    assert result["operating_business"] == "false"
    assert result["universe_preeligible"] == "false"


def test_permian_basin_royalty_trust_is_excluded():
    result = apply_entity_structure(audit_row("Permian Basin Royalty Trust Common Stock", ticker="PBT"))
    assert result["entity_structure"] == "royalty_trust"
    assert result["universe_preeligible"] == "false"


def test_piedmont_realty_trust_in_real_estate_is_reit():
    result = apply_entity_structure(
        audit_row("Piedmont Realty Trust Inc. Class A Common Stock", "Real Estate", "PDM")
    )
    assert result["entity_structure"] == "reit"
    assert result["reit"] == "true"
    assert result["universe_preeligible"] == "false"


def test_real_estate_company_without_realty_trust_is_not_reit_by_sector_alone():
    result = apply_entity_structure(
        audit_row("Laureate Education Inc. Common Stock", "Real Estate", "LAUR")
    )
    assert result["entity_structure"] == "corporation"
    assert result["reit"] == "false"
    assert result["universe_preeligible"] == "true"


def test_limited_partnership_entity_suffix_is_non_common_stock():
    for ticker, name in (
        ("IEP", "Icahn Enterprises L.P. Common Stock"),
        ("SPH", "Suburban Propane Partners L.P. Common Stock"),
    ):
        result = apply_entity_structure(audit_row(name, ticker=ticker))
        assert result["entity_structure"] == "limited_partnership"
        assert result["security_type"] == "non_common_stock"
        assert result["universe_preeligible"] == "false"
        assert "not_common_stock" in result["universe_exclusion_reason"]


def test_lp_inside_word_does_not_trigger_limited_partnership():
    result = apply_entity_structure(audit_row("Help Corporation Common Stock"))
    assert result["entity_structure"] == "corporation"
    assert result["universe_preeligible"] == "true"


def test_all_five_regression_entities_are_preeligible_false():
    cases = (
        ("PDM", "Piedmont Realty Trust Inc. Class A Common Stock", "Real Estate"),
        ("SBR", "Sabine Royalty Trust Common Stock", "Energy"),
        ("PBT", "Permian Basin Royalty Trust Common Stock", "Energy"),
        ("IEP", "Icahn Enterprises L.P. Common Stock", "Energy"),
        ("SPH", "Suburban Propane Partners L.P. Common Stock", "Consumer Discretionary"),
    )
    rows = apply_entity_structure_to_rows(
        [audit_row(name, sector, ticker) for ticker, name, sector in cases]
    )
    assert all(row["universe_preeligible"] == "false" for row in rows)


def test_r2_reselection_keeps_50_buckets_and_excludes_legal_structures():
    rows = r1_candidates(rows_per_sector_per_bucket=4)
    excluded_names = {
        rows[0]["ticker"]: "Sabine Royalty Trust Common Stock",
        rows[1]["ticker"]: "Icahn Enterprises L.P. Common Stock",
        rows[2]["ticker"]: "Piedmont Realty Trust Inc. Class A Common Stock",
    }
    prepared = []
    for row in rows:
        source = audit_row(
            excluded_names.get(row["ticker"], f"{row['ticker']} Corporation Common Stock"),
            row["sector_normalized"],
            row["ticker"],
        )
        source.update(row)
        source["company"] = excluded_names.get(row["ticker"], source["company"])
        prepared.append(apply_entity_structure(source))
    _, selected, targets = select_balanced_pilot(prepared, "d" * 64)

    assert len(selected) == 50
    assert all(value == 10 for value in targets.values())
    assert all(row["entity_structure"] not in {"limited_partnership", "royalty_trust", "reit", "other_trust"} for row in selected)