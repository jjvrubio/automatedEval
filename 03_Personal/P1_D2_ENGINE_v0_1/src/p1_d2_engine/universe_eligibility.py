from __future__ import annotations

import math
import csv
from typing import Any
from pathlib import Path


UNIVERSE_ENGINE_VERSION = "0.4"
MIN_MARKET_CAP = 500_000_000
MAX_MARKET_CAP = 20_000_000_000
MIN_LATEST_FY_REVENUE = 100_000_000
FINANCIAL_SECTORS = {"financial", "financial services", "financials", "finance"}
SECURITY_TYPES = {
    "common_stock",
    "preferred_stock",
    "adr",
    "etf",
    "fund",
    "debt",
    "other",
}
BOOLEAN_COLUMNS = ("operating_business", "reit", "bdc", "pre_revenue")

UNIVERSE_INPUT_COLUMNS = (
    "ticker",
    "company",
    "country",
    "security_type",
    "sector",
    "industry",
    "market_cap_current",
    "market_cap_currency",
    "market_cap_as_of",
    "market_cap_source",
    *BOOLEAN_COLUMNS,
)

UNIVERSE_RESULT_COLUMNS = (
    "ticker",
    "company",
    "country",
    "security_type",
    "sector",
    "industry",
    "market_cap_current",
    "market_cap_as_of",
    "market_cap_source",
    *BOOLEAN_COLUMNS,
    "universe_input_status",
    "universe_preeligible",
    "universe_exclusion_reason",
    "revenue_latest_fy",
    "revenue_eligibility",
    "universe_eligible",
)


def read_universe_csv(path: str | Path) -> list[dict[str, str]]:
    """Read the independent pilot input without inferring or repairing values."""
    with Path(path).open(newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        headers = reader.fieldnames or []
        missing = [column for column in UNIVERSE_INPUT_COLUMNS if column not in headers]
        if missing:
            raise ValueError(f"Universe CSV is missing required columns: {', '.join(missing)}")
        rows = list(reader)

    if len(rows) != 50:
        raise ValueError(f"P1 pilot input must contain exactly 50 rows; found {len(rows)}")
    tickers = [str(row.get("ticker") or "").strip().upper() for row in rows]
    nonempty_tickers = [ticker for ticker in tickers if ticker]
    if len(nonempty_tickers) != len(set(nonempty_tickers)):
        raise ValueError("P1 pilot input contains duplicate tickers")
    return rows


def _parse_boolean(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().casefold()
        if normalized == "true":
            return True
        if normalized == "false":
            return False
    return None


def _parse_market_cap(value: Any) -> float | None:
    if value is None or (isinstance(value, str) and not value.strip()):
        return None
    try:
        parsed = float(value)
    except (TypeError, ValueError):
        return None
    return parsed if math.isfinite(parsed) else None


def prepare_universe_row(raw: dict[str, Any]) -> dict[str, Any]:
    """Validate and apply current-data exclusions without consulting SEC facts."""
    row = {column: raw.get(column) for column in UNIVERSE_INPUT_COLUMNS}
    for column in UNIVERSE_INPUT_COLUMNS:
        if isinstance(row[column], str):
            row[column] = row[column].strip()

    cap_raw = row["market_cap_current"]
    market_cap = _parse_market_cap(cap_raw)
    row["market_cap_current"] = market_cap
    parsed_flags = {column: _parse_boolean(row[column]) for column in BOOLEAN_COLUMNS}
    row.update(parsed_flags)

    input_status = "valid"
    if not row["ticker"] or not row["country"] or not row["sector"]:
        input_status = "invalid_universe_input"
    elif cap_raw is None or (isinstance(cap_raw, str) and not cap_raw.strip()):
        input_status = "missing_market_cap"
    elif market_cap is None:
        input_status = "invalid_universe_input"
    elif str(row["market_cap_currency"]).upper() != "USD":
        input_status = "unsupported_currency"
    elif not row["market_cap_as_of"] or not row["market_cap_source"]:
        input_status = "invalid_universe_input"
    elif any(
        value is None and column != "pre_revenue"
        for column, value in parsed_flags.items()
    ):
        input_status = "invalid_universe_input"
    elif str(row["security_type"]).casefold() not in SECURITY_TYPES:
        input_status = "invalid_security_type"

    exclusion_reason: str | None = None
    if input_status != "valid":
        exclusion_reason = "invalid_universe_input"
    elif row["country"].upper() != "US":
        exclusion_reason = "non_us"
    elif str(row["security_type"]).casefold() != "common_stock":
        exclusion_reason = "not_common_stock"
    elif market_cap < MIN_MARKET_CAP:
        exclusion_reason = "market_cap_below_min"
    elif market_cap > MAX_MARKET_CAP:
        exclusion_reason = "market_cap_above_max"
    elif str(row["sector"]).strip().casefold() in FINANCIAL_SECTORS:
        exclusion_reason = "financial"
    elif row["reit"] is True:
        exclusion_reason = "reit"
    elif row["bdc"] is True:
        exclusion_reason = "bdc"
    elif row["pre_revenue"] is True:
        exclusion_reason = "pre_revenue"
    elif row["operating_business"] is not True:
        exclusion_reason = "not_operating_business"

    row.update(
        {
            "universe_input_status": input_status,
            "universe_preeligible": exclusion_reason is None,
            "universe_exclusion_reason": exclusion_reason,
            "revenue_latest_fy": None,
            "revenue_eligibility": "unknown",
            "universe_eligible": False if exclusion_reason else "unknown",
        }
    )
    return row


def apply_revenue_eligibility(
    prepared_row: dict[str, Any],
    revenue_latest_fy: float | None,
    sec_reporting_compatible: bool | None,
) -> dict[str, Any]:
    """Resolve final eligibility using latest-FY SEC revenue, not market data."""
    row = dict(prepared_row)
    row["revenue_latest_fy"] = revenue_latest_fy

    if not row.get("universe_preeligible"):
        row["revenue_eligibility"] = "unknown"
        row["universe_eligible"] = False
        return row

    if revenue_latest_fy is None or not math.isfinite(float(revenue_latest_fy)):
        row["revenue_eligibility"] = "unknown"
        row["universe_eligible"] = "unknown"
    elif revenue_latest_fy <= MIN_LATEST_FY_REVENUE:
        row["revenue_eligibility"] = False
        row["universe_eligible"] = False
        row["universe_exclusion_reason"] = "revenue_below_min"
    else:
        row["revenue_eligibility"] = True
        if sec_reporting_compatible is True:
            row["universe_eligible"] = True
        elif sec_reporting_compatible is False:
            row["universe_eligible"] = False
            row["universe_exclusion_reason"] = "invalid_universe_input"
        else:
            row["universe_eligible"] = "unknown"
    return row


def eligible_d2_signal(
    d2_signal: bool,
    universe_eligible: bool | str,
    freshness_status: str | None,
) -> bool:
    return (
        d2_signal is True
        and universe_eligible is True
        and freshness_status == "fresh"
    )