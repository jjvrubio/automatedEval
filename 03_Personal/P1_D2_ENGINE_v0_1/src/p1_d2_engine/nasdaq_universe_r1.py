from __future__ import annotations

import hashlib
from collections import Counter, defaultdict
from decimal import Decimal
from typing import Any


SELECTION_REVISION = 1
BUCKET_TARGET = 10
MAX_PER_SECTOR = 8
BUCKETS = (
    ("B1_0_5_1B", Decimal("500000000"), Decimal("1000000000")),
    ("B2_1_2B", Decimal("1000000000"), Decimal("2000000000")),
    ("B3_2_5B", Decimal("2000000000"), Decimal("5000000000")),
    ("B4_5_10B", Decimal("5000000000"), Decimal("10000000000")),
    ("B5_10_20B", Decimal("10000000000"), Decimal("20000000000")),
)
BUCKET_NAMES = tuple(bucket[0] for bucket in BUCKETS)


def market_cap_bucket(value: Any) -> str | None:
    try:
        cap = Decimal(str(value))
    except Exception:
        return None
    for index, (name, lower, upper) in enumerate(BUCKETS):
        if lower <= cap and (cap <= upper if index == len(BUCKETS) - 1 else cap < upper):
            return name
    return None


def make_selection_key(source_sha256: str, ticker: str) -> str:
    return hashlib.sha256(f"{source_sha256}:{ticker.strip().upper()}".encode("utf-8")).hexdigest()


def _bucket_targets(populations: dict[str, int], target_each: int = BUCKET_TARGET) -> dict[str, int]:
    targets = {name: min(target_each, populations.get(name, 0)) for name in BUCKET_NAMES}
    deficit = target_each * len(BUCKET_NAMES) - sum(targets.values())
    while deficit:
        short_buckets = [name for name in BUCKET_NAMES if targets[name] < target_each]
        if not short_buckets:
            break
        progressed = False
        for short_name in short_buckets:
            short_index = BUCKET_NAMES.index(short_name)
            donors = [
                name
                for name in BUCKET_NAMES
                if targets[name] < populations.get(name, 0)
            ]
            donors.sort(key=lambda name: (abs(BUCKET_NAMES.index(name) - short_index), BUCKET_NAMES.index(name)))
            if donors:
                targets[donors[0]] += 1
                deficit -= 1
                progressed = True
                if deficit == 0:
                    break
        if not progressed:
            break
    return targets


def select_balanced_pilot(
    audit_rows: list[dict[str, Any]],
    source_sha256: str,
    target_each: int = BUCKET_TARGET,
    max_per_sector: int = MAX_PER_SECTOR,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, int]]:
    """Select a reproducible market-cap stress-test sample from frozen 04A rows."""
    annotated: list[dict[str, Any]] = []
    for source_row in audit_rows:
        row = dict(source_row)
        row["market_cap_bucket"] = market_cap_bucket(row.get("market_cap_current")) or ""
        row["selection_key"] = make_selection_key(source_sha256, str(row.get("ticker") or ""))
        row["selected_for_pilot"] = "false"
        row["selection_revision"] = str(SELECTION_REVISION)
        annotated.append(row)

    candidates = [row for row in annotated if row.get("universe_preeligible") == "true"]
    populations = Counter(row["market_cap_bucket"] for row in candidates if row["market_cap_bucket"])
    targets = _bucket_targets(dict(populations), target_each)
    if sum(targets.values()) < target_each * len(BUCKET_NAMES):
        raise ValueError(
            "BLOCKED_INSUFFICIENT_PREELIGIBLE_ROWS: "
            f"only {sum(targets.values())} can be assigned across the five buckets"
        )

    by_bucket_sector: dict[str, dict[str, list[dict[str, Any]]]] = {
        name: defaultdict(list) for name in BUCKET_NAMES
    }
    for row in candidates:
        bucket = row["market_cap_bucket"]
        if bucket:
            by_bucket_sector[bucket][row.get("sector_normalized") or "unknown"].append(row)
    for sector_groups in by_bucket_sector.values():
        for rows in sector_groups.values():
            rows.sort(key=lambda row: (row["selection_key"], row["ticker"]))

    selected: list[dict[str, Any]] = []
    bucket_selection: Counter[str] = Counter()
    sector_selection: Counter[str] = Counter()
    for bucket in BUCKET_NAMES:
        within_bucket: Counter[str] = Counter()
        pointers: Counter[str] = Counter()
        target = targets[bucket]
        while bucket_selection[bucket] < target:
            available_sectors = [
                sector
                for sector, rows in by_bucket_sector[bucket].items()
                if pointers[sector] < len(rows) and sector_selection[sector] < max_per_sector
            ]
            if not available_sectors:
                raise ValueError(
                    "BLOCKED_SECTOR_DIVERSITY_CAP: "
                    f"cannot fill {bucket} target {target} while respecting max {max_per_sector} per sector"
                )
            sector = min(
                available_sectors,
                key=lambda value: (within_bucket[value], sector_selection[value], value),
            )
            row = by_bucket_sector[bucket][sector][pointers[sector]]
            pointers[sector] += 1
            within_bucket[sector] += 1
            sector_selection[sector] += 1
            bucket_selection[bucket] += 1
            row["selected_for_pilot"] = "true"
            selected.append(row)

    return annotated, selected, targets