from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class FactObservation:
    metric: str
    tag: str
    unit: str
    start: str
    end: str
    value: float
    form: str
    filed: str
    accession: str
    fy: int | None = None
    fp: str | None = None

    @property
    def period_key(self) -> tuple[str, str]:
        return (self.start, self.end)

    def provenance_row(self, ticker: str, cik: int) -> dict[str, Any]:
        row = asdict(self)
        accession_compact = self.accession.replace("-", "")
        source_url = (
            f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_compact}/"
            if accession_compact
            else None
        )
        row.update(
            {
                "ticker": ticker,
                "cik": cik,
                "taxonomy": "us-gaap",
                "source_url": source_url,
            }
        )
        return row


@dataclass
class D2Result:
    engine_version: str
    ticker: str
    cik: int | None
    company: str | None
    status: str
    reason: str | None = None
    revenue_tag: str | None = None
    fy_t_end: str | None = None
    fy_t_minus_1_end: str | None = None
    revenue_fy_t: float | None = None
    revenue_fy_t_minus_1: float | None = None
    revenue_growth_fy_yoy: float | None = None
    operating_income_fy_t: float | None = None
    operating_income_fy_t_minus_1: float | None = None
    operating_margin_fy_t: float | None = None
    operating_margin_fy_t_minus_1: float | None = None
    om_delta_pp: float | None = None
    candidate_d2: bool = False
    strong_signal: bool = False
    selected_fy_t_end: str | None = None
    selected_fy_t_minus_1_end: str | None = None
    latest_annual_period_end_observed: str | None = None
    selected_period_age_days: int | None = None
    freshness_status: str | None = None
    latest_fy_resolution_status: str | None = None
    missing_latest_fy_metric: str | None = None
    d2_signal: bool = False
    universe_eligible: str = "unknown"
    ambiguous_period: str | None = None
    ambiguous_tag_a: str | None = None
    ambiguous_value_a: float | None = None
    ambiguous_tag_b: str | None = None
    ambiguous_value_b: float | None = None
    available_operating_income_tags: str | None = None

    def to_row(self) -> dict[str, Any]:
        return asdict(self)
