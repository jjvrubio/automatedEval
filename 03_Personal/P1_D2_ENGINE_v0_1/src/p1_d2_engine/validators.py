from __future__ import annotations

from datetime import date


def iso_date(value: str) -> date:
    return date.fromisoformat(value)


def duration_days(start: str, end: str) -> int:
    return (iso_date(end) - iso_date(start)).days + 1


def is_annual_duration(start: str, end: str, minimum: int = 330, maximum: int = 400) -> bool:
    days = duration_days(start, end)
    return minimum <= days <= maximum


def consecutive_annual_periods(
    older_end: str, newer_end: str, minimum_gap: int = 330, maximum_gap: int = 400
) -> bool:
    gap = (iso_date(newer_end) - iso_date(older_end)).days
    return minimum_gap <= gap <= maximum_gap
