from __future__ import annotations

import re
from typing import Any


ROYALTY_TRUST_RE = re.compile(r"\broyalty\s+trust\b", re.IGNORECASE)
REALTY_TRUST_RE = re.compile(r"\brealty\s+trust\b", re.IGNORECASE)
REAL_ESTATE_INVESTMENT_TRUST_RE = re.compile(
    r"\breal\s+estate\s+investment\s+trust\b", re.IGNORECASE
)
LIMITED_PARTNERSHIP_RE = re.compile(
    r"\blimited\s+partnership\b|(?<![A-Za-z0-9])L\s*\.\s*P\s*\.?(?![A-Za-z0-9])|"
    r"(?<![A-Za-z0-9])LP(?![A-Za-z0-9])",
    re.IGNORECASE,
)
OTHER_TRUST_RE = re.compile(r"\btrust\b(?=\s+(?:common\s+stock|class\s+[A-Z]|$))", re.IGNORECASE)
EXPLICIT_NON_OPERATING_RE = re.compile(
    r"\b(?:fund|blank checks?|shell compan|special purpose acquisition)\b", re.IGNORECASE
)


def _append_reason(row: dict[str, Any], reason: str) -> None:
    existing = [value for value in str(row.get("universe_exclusion_reason") or "").split(";") if value]
    if reason not in existing:
        existing.append(reason)
    row["universe_exclusion_reason"] = ";".join(existing)


def apply_entity_structure(row: dict[str, Any]) -> dict[str, Any]:
    """Overlay only explicit, high-confidence legal-structure exclusions on frozen 04A rows."""
    result = dict(row)
    name = str(result.get("company") or "")
    sector = str(result.get("sector") or "").strip()
    security_type = str(result.get("security_type") or "unknown")
    operating_business = str(result.get("operating_business") or "unknown")

    if ROYALTY_TRUST_RE.search(name):
        structure = "royalty_trust"
        result["security_type"] = "non_common_stock"
        result["operating_business"] = "false"
        _append_reason(result, "not_common_stock")
        _append_reason(result, "not_operating_business")
        result["universe_preeligible"] = "false"
    elif REAL_ESTATE_INVESTMENT_TRUST_RE.search(name) or (
        REALTY_TRUST_RE.search(name) and sector.casefold() == "real estate"
    ):
        structure = "reit"
        result["reit"] = "true"
        _append_reason(result, "reit")
        result["universe_preeligible"] = "false"
    elif LIMITED_PARTNERSHIP_RE.search(name):
        structure = "limited_partnership"
        result["security_type"] = "non_common_stock"
        _append_reason(result, "not_common_stock")
        result["universe_preeligible"] = "false"
    elif OTHER_TRUST_RE.search(name):
        structure = "other_trust"
        result["security_type"] = "non_common_stock"
        result["operating_business"] = "false"
        _append_reason(result, "not_common_stock")
        _append_reason(result, "not_operating_business")
        result["universe_preeligible"] = "false"
    elif security_type == "common_stock" and operating_business == "true" and not EXPLICIT_NON_OPERATING_RE.search(name):
        structure = "corporation"
    else:
        structure = "unknown"

    result["entity_structure"] = structure
    return result


def apply_entity_structure_to_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [apply_entity_structure(row) for row in rows]