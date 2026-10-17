from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class CompanyIdentity:
    ticker: str
    cik: int
    title: str


def build_ticker_map(raw: dict[str, Any]) -> dict[str, CompanyIdentity]:
    result: dict[str, CompanyIdentity] = {}
    for item in raw.values():
        ticker = str(item["ticker"]).upper().strip()
        result[ticker] = CompanyIdentity(
            ticker=ticker,
            cik=int(item["cik_str"]),
            title=str(item.get("title") or ""),
        )
    return result
