from __future__ import annotations

import csv
import hashlib
import re
from collections import defaultdict
from datetime import datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any


BUILDER_VERSION = "0.1"
MARKET_CAP_MIN = Decimal("500000000")
MARKET_CAP_MAX = Decimal("20000000000")
TARGET_COUNT = 50
MAX_PER_SECTOR = 12
MARKET_CAP_SOURCE = "Nasdaq Stock Screener"

NON_COMMON_RE = re.compile(
    r"\b(etf|fund|preferred|warrant|right|unit|ordinary shares?|"
    r"american depositary shares?|depositary shares?|depositary receipts?|"
    r"notes?|debentures?)\b",
    re.IGNORECASE,
)
COMMON_STOCK_RE = re.compile(r"\bcommon stock\b", re.IGNORECASE)
REIT_RE = re.compile(r"\bREIT\b|real estate investment trust", re.IGNORECASE)
BDC_RE = re.compile(r"\bBDC\b|business development compan", re.IGNORECASE)
NON_OPERATING_RE = re.compile(
    r"blank checks?|shell compan|special purpose acquisition|"
    r"acquisition corp(?:oration)?",
    re.IGNORECASE,
)
FINANCIAL_TERMS = (
    "finance",
    "financial",
    "banks",
    "insurance",
    "capital markets",
)
SECTOR_NORMALIZATION = {
    "consumer cyclical": "Consumer Discretionary",
    "consumer discretionary": "Consumer Discretionary",
    "consumer defensive": "Consumer Staples",
    "consumer staples": "Consumer Staples",
    "telecommunications": "Communication Services",
    "communication services": "Communication Services",
    "basic materials": "Materials",
    "materials": "Materials",
    "health care": "Health Care",
    "healthcare": "Health Care",
}

UNIVERSE_COLUMNS = (
    "ticker",
    "company",
    "country",
    "security_type",
    "sector",
    "sector_normalized",
    "industry",
    "exchange",
    "market_cap_raw",
    "market_cap_current",
    "market_cap_currency",
    "market_cap_as_of",
    "market_cap_as_of_basis",
    "market_cap_source",
    "operating_business",
    "financial_sector",
    "reit",
    "bdc",
    "pre_revenue",
    "universe_preeligible",
    "universe_exclusion_reason",
    "source_filename",
    "source_sha256",
)

AUDIT_COLUMNS = (
    "ticker",
    "company",
    "country",
    "security_type",
    "sector",
    "sector_normalized",
    "industry",
    "exchange",
    "market_cap_raw",
    "market_cap_current",
    "market_cap_currency",
    "market_cap_as_of",
    "market_cap_as_of_basis",
    "market_cap_source",
    "operating_business",
    "financial_sector",
    "reit",
    "bdc",
    "pre_revenue",
    "universe_preeligible",
    "universe_exclusion_reason",
    "source_filename",
    "source_sha256",
)


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_market_cap(raw: Any) -> Decimal | None:
    if raw is None:
        return None
    text = str(raw).strip().replace(",", "").replace("$", "")
    match = re.fullmatch(r"([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*([KMBT])?", text, re.I)
    if not match:
        return None
    try:
        value = Decimal(match.group(1))
    except InvalidOperation:
        return None
    suffix = (match.group(2) or "").upper()
    multiplier = {"": 1, "K": 10**3, "M": 10**6, "B": 10**9, "T": 10**12}[suffix]
    return value * multiplier


def _bool(value: bool | None) -> str:
    return "unknown" if value is None else ("true" if value else "false")


def normalize_sector(sector: str) -> str:
    normalized = sector.strip()
    if not normalized:
        return "unknown"
    return SECTOR_NORMALIZATION.get(normalized.casefold(), normalized)


def classify_source_row(
    raw: dict[str, str],
    source_filename: str,
    source_sha256: str,
    modified_at: datetime,
) -> dict[str, Any]:
    ticker = (raw.get("Symbol") or "").strip().upper()
    company = (raw.get("Name") or "").strip()
    raw_country = (raw.get("Country") or "").strip()
    country = "US" if raw_country.casefold() == "united states" else (raw_country or "unknown")
    sector = (raw.get("Sector") or "").strip() or "unknown"
    industry = (raw.get("Industry") or "").strip() or "unknown"
    name_and_industry = f"{company} {industry}"
    cap_raw = (raw.get("Market Cap") or "").strip()
    market_cap = parse_market_cap(cap_raw)

    if NON_COMMON_RE.search(company):
        security_type = "non_common_stock"
    elif COMMON_STOCK_RE.search(company):
        security_type = "common_stock"
    else:
        security_type = "unknown"

    sector_lower = sector.casefold()
    industry_lower = industry.casefold()
    financial_sector: bool | None = None if sector == "unknown" else any(
        term in sector_lower or term in industry_lower for term in FINANCIAL_TERMS
    )
    reit: bool | None = None if industry == "unknown" else bool(REIT_RE.search(name_and_industry))
    bdc: bool | None = None if industry == "unknown" else bool(BDC_RE.search(name_and_industry))
    pre_revenue: bool | None = None

    non_operating = bool(NON_OPERATING_RE.search(name_and_industry)) or industry_lower in {
        "blank checks",
        "shell companies",
        "shell companies: blank checks",
    }
    if non_operating or security_type == "non_common_stock":
        operating_business: bool | None = False
    elif security_type == "common_stock" and sector != "unknown" and industry != "unknown":
        operating_business = True
    else:
        operating_business = None

    reasons: list[str] = []
    unknown_criteria = False
    if market_cap is None:
        reasons.append("invalid_market_cap")
        unknown_criteria = not cap_raw
        if cap_raw:
            unknown_criteria = False
    elif market_cap < MARKET_CAP_MIN:
        reasons.append("market_cap_below_min")
    elif market_cap > MARKET_CAP_MAX:
        reasons.append("market_cap_above_max")

    if country == "unknown":
        reasons.append("country_unknown")
        unknown_criteria = True
    elif country != "US":
        reasons.append("non_us")

    if security_type == "non_common_stock":
        reasons.append("not_common_stock")
    elif security_type == "unknown":
        reasons.append("security_type_unknown")
        unknown_criteria = True

    if financial_sector is True:
        reasons.append("financial")
    if reit is True:
        reasons.append("reit")
    if bdc is True:
        reasons.append("bdc")
    if pre_revenue is True:
        reasons.append("pre_revenue")

    if operating_business is False:
        reasons.append("not_operating_business")
    elif operating_business is None:
        reasons.append("operating_business_unknown")
        unknown_criteria = True

    explicit_exclusion = any(
        reason
        in {
            "market_cap_below_min",
            "market_cap_above_max",
            "non_us",
            "not_common_stock",
            "financial",
            "reit",
            "bdc",
            "pre_revenue",
            "not_operating_business",
        }
        for reason in reasons
    ) or (market_cap is None and bool(cap_raw))
    preeligible: bool | None
    if explicit_exclusion:
        preeligible = False
    elif unknown_criteria:
        preeligible = None
    else:
        preeligible = True

    return {
        "ticker": ticker,
        "company": company,
        "country": country,
        "security_type": security_type,
        "sector": sector,
        "sector_normalized": normalize_sector(sector),
        "industry": industry,
        "exchange": "unknown",
        "market_cap_raw": cap_raw,
        "market_cap_current": format(market_cap, "f") if market_cap is not None else "",
        "market_cap_currency": "USD" if market_cap is not None else "unknown",
        "market_cap_as_of": modified_at.date().isoformat(),
        "market_cap_as_of_basis": "file_modified_at_proxy",
        "market_cap_source": MARKET_CAP_SOURCE,
        "operating_business": _bool(operating_business),
        "financial_sector": _bool(financial_sector),
        "reit": _bool(reit),
        "bdc": _bool(bdc),
        "pre_revenue": _bool(pre_revenue),
        "universe_preeligible": _bool(preeligible),
        "universe_exclusion_reason": ";".join(dict.fromkeys(reasons)),
        "source_filename": source_filename,
        "source_sha256": source_sha256,
        "_market_cap_decimal": market_cap,
    }


def select_diverse_universe(
    rows: list[dict[str, Any]],
    target_count: int = TARGET_COUNT,
    max_per_sector: int = MAX_PER_SECTOR,
) -> tuple[list[dict[str, Any]], bool]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("universe_preeligible") == "true":
            groups[row["sector_normalized"]].append(row)
    for candidates in groups.values():
        candidates.sort(
            key=lambda row: (-row["_market_cap_decimal"], row["ticker"])
        )

    sectors = sorted(groups)
    selected: list[dict[str, Any]] = []
    selected_per_sector: dict[str, int] = defaultdict(int)
    cursor = {sector: 0 for sector in sectors}
    while len(selected) < target_count:
        made_progress = False
        for sector in sectors:
            if selected_per_sector[sector] >= max_per_sector:
                continue
            if cursor[sector] >= len(groups[sector]):
                continue
            selected.append(groups[sector][cursor[sector]])
            cursor[sector] += 1
            selected_per_sector[sector] += 1
            made_progress = True
            if len(selected) == target_count:
                break
        if not made_progress:
            break

    relaxed_max = False
    if len(selected) < target_count:
        remaining = []
        for sector in sectors:
            remaining.extend(groups[sector][cursor[sector] :])
        remaining.sort(key=lambda row: (-row["_market_cap_decimal"], row["sector_normalized"], row["ticker"]))
        selected.extend(remaining[: target_count - len(selected)])
        relaxed_max = bool(remaining)
    return selected, relaxed_max


def read_nasdaq_csv(path: str | Path) -> tuple[list[str], list[dict[str, str]], str]:
    path = Path(path)
    sample = path.read_bytes()[:8192].decode("utf-8-sig")
    try:
        delimiter = csv.Sniffer().sniff(sample, delimiters=",;\t|").delimiter
    except csv.Error:
        delimiter = ","
    with path.open(encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source, delimiter=delimiter)
        return reader.fieldnames or [], list(reader), delimiter


def source_modified_at(path: str | Path) -> datetime:
    return datetime.fromtimestamp(Path(path).stat().st_mtime).astimezone()