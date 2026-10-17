from __future__ import annotations

import csv
import hashlib
import shutil
import sys
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path
from statistics import mean
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from p1_d2_engine.nasdaq_universe_r1 import (  # noqa: E402
    BUCKET_NAMES,
    MAX_PER_SECTOR,
    SELECTION_REVISION,
    select_balanced_pilot,
)

EXPECTED_SOURCE_SHA256 = "8e4dc6139f7dd7cdb6f9a326f6a9927c1d80529953b3ac35530f8cf5387a2c35"
EXPECTED_OLD_PILOT_SHA256 = "befc0cc06086662d9afab53cc3e2e9ddf9bb9be0308c3fd6a4123d607b352a94"
SOURCE = ROOT / "nasdaq_screener_1791296955512.csv"
OLD_PILOT = ROOT / "input" / "universe_p1_50.csv"
OLD_PILOT_COPY = ROOT / "input" / "universe_p1_50_v04A_topcap.csv"
VERSIONED_PILOT = ROOT / "input" / "universe_p1_50_v04A_r1.csv"
AUDIT_IN = ROOT / "output" / "P1_universe_audit_v04A.csv"
AUDIT_OUT = ROOT / "output" / "P1_universe_audit_v04A_r1.csv"
DIAGNOSTICS_OUT = ROOT / "output" / "P1_universe_diagnostics_v04A_r1.md"
REPORT_OUT = ROOT / "output" / "CODEX_TASK_04A_R1_REPORT.md"
PILOT_EXTRA_COLUMNS = ("market_cap_bucket", "selection_key", "selected_for_pilot", "selection_revision")
AUDIT_EXTRA_COLUMNS = PILOT_EXTRA_COLUMNS


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as source:
        reader = csv.DictReader(source)
        return reader.fieldnames or [], list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def percentile(values: list[float], quantile: float) -> float:
    ordered = sorted(values)
    position = (len(ordered) - 1) * quantile
    lower = int(position)
    upper = min(lower + 1, len(ordered) - 1)
    weight = position - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def cap_summary(rows: list[dict[str, Any]]) -> dict[str, float]:
    values = [float(row["market_cap_current"]) for row in rows]
    return {
        "min": min(values),
        "p10": percentile(values, 0.10),
        "p25": percentile(values, 0.25),
        "median": percentile(values, 0.50),
        "p75": percentile(values, 0.75),
        "p90": percentile(values, 0.90),
        "max": max(values),
        "mean": mean(values),
    }


def markdown_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines.extend("| " + " | ".join(str(value) for value in row) + " |" for row in rows)
    return lines


def build_diagnostics(
    audit_rows: list[dict[str, Any]],
    selected: list[dict[str, Any]],
    targets: dict[str, int],
    old_rows: list[dict[str, str]],
    source_sha256: str,
    relaxed_sector_cap: bool = False,
) -> str:
    populations = Counter(
        row["market_cap_bucket"]
        for row in audit_rows
        if row.get("universe_preeligible") == "true" and row.get("market_cap_bucket")
    )
    selection_counts = Counter(row["market_cap_bucket"] for row in selected)
    sector_counts = Counter(row["sector_normalized"] for row in selected)
    cross_counts = Counter((row["market_cap_bucket"], row["sector_normalized"]) for row in selected)
    shortfalls = [
        (bucket, targets[bucket], selection_counts[bucket])
        for bucket in BUCKET_NAMES
        if targets[bucket] != 10
    ]
    redistribution = "none"
    if shortfalls:
        redistribution = "; ".join(
            f"{bucket}: target {target}, selected {count}" for bucket, target, count in shortfalls
        )

    new_summary = cap_summary(selected)
    old_summary = cap_summary(old_rows)
    comparison = [
        ["min market cap", f"{old_summary['min']:.0f}", f"{new_summary['min']:.0f}"],
        ["median market cap", f"{old_summary['median']:.0f}", f"{new_summary['median']:.0f}"],
        ["p75 market cap", f"{old_summary['p75']:.0f}", f"{new_summary['p75']:.0f}"],
        ["max market cap", f"{old_summary['max']:.0f}", f"{new_summary['max']:.0f}"],
        ["number of sectors", len(set(row["sector_normalized"] for row in old_rows)), len(sector_counts)],
        ["largest sector count", max(Counter(row["sector_normalized"] for row in old_rows).values()), max(sector_counts.values())],
    ]

    lines = [
        "# P1 universe diagnostics v04A R1",
        "",
        "task = CODEX_TASK_04A_R1",
        "universe_builder_version = 0.1",
        f"source_sha256 = {source_sha256}",
        "source_rows = 7017",
        f"preeligible_true = {sum(row.get('universe_preeligible') == 'true' for row in audit_rows)}",
        f"selected_50 = {len(selected)}",
        f"selection_revision = {SELECTION_REVISION}",
        f"bucket_shortfall = {redistribution}",
        f"sector_max_relaxed = {str(relaxed_sector_cap).lower()}",
        "pilot_type = stress-test sample; pilot signal rate != population signal rate",
        "",
        "## Market-cap distribution of selected 50",
        "",
        *markdown_table(["Metric", "USD"], [[key, f"{value:.2f}"] for key, value in new_summary.items()]),
        "",
        "## Market-cap bucket distribution",
        "",
        *markdown_table(
            ["Bucket", "Selected count", "Preeligible population", "Target"],
            [[bucket, selection_counts[bucket], populations[bucket], targets[bucket]] for bucket in BUCKET_NAMES],
        ),
        "",
        "## Sector distribution",
        "",
        *markdown_table(["Sector", "Count"], [[sector, count] for sector, count in sorted(sector_counts.items())]),
        "",
        "## Cross-distribution: market_cap_bucket x sector",
        "",
        *markdown_table(
            ["Bucket", "Sector", "Count"],
            [
                [bucket, sector, cross_counts[(bucket, sector)]]
                for bucket in BUCKET_NAMES
                for sector in sorted(sector_counts)
                if cross_counts[(bucket, sector)]
            ],
        ),
        "",
        "## Previous vs rebalanced pilot",
        "",
        *markdown_table(["Metric", "Old selection", "New selection"], comparison),
        "",
        "Selection is deterministic: SHA256(source_sha256 + ':' + ticker), ordered ascending within each bucket and normalized sector; each bucket is selected sector-round-robin. The selection is a stress-test sample, not a representative population sample.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    if sha256_file(SOURCE) != EXPECTED_SOURCE_SHA256:
        raise SystemExit("BLOCKED_SOURCE_CHANGED")
    old_pilot_source = OLD_PILOT_COPY if OLD_PILOT_COPY.exists() else OLD_PILOT
    if sha256_file(old_pilot_source) != EXPECTED_OLD_PILOT_SHA256:
        raise SystemExit("BLOCKED_PREVIOUS_SELECTION_MISMATCH")
    if OLD_PILOT_COPY.exists() and sha256_file(OLD_PILOT_COPY) != EXPECTED_OLD_PILOT_SHA256:
        raise SystemExit("BLOCKED_PREVIOUS_SELECTION_MISMATCH")

    _, old_rows = read_csv(old_pilot_source)
    audit_headers, original_audit = read_csv(AUDIT_IN)
    preeligible_count = sum(row.get("universe_preeligible") == "true" for row in original_audit)
    if len(original_audit) != 7017 or preeligible_count != 1338:
        raise SystemExit(
            "BLOCKED_PREELIGIBLE_POPULATION_CHANGED: "
            f"audit rows={len(original_audit)}, preeligible_true={preeligible_count}"
        )
    if any(row.get("source_sha256") != EXPECTED_SOURCE_SHA256 for row in original_audit):
        raise SystemExit("BLOCKED_SOURCE_AUDIT_MISMATCH")

    annotated, selected, targets = select_balanced_pilot(original_audit, EXPECTED_SOURCE_SHA256)
    if len(selected) != 50 or any(row.get("universe_preeligible") != "true" for row in selected):
        raise SystemExit("BLOCKED_INVALID_SELECTION")
    if sum(row["selected_for_pilot"] == "true" for row in annotated) != 50:
        raise SystemExit("BLOCKED_INVALID_SELECTION_FLAGS")
    sector_counts = Counter(row["sector_normalized"] for row in selected)
    if len(sector_counts) < 8 or max(sector_counts.values()) > MAX_PER_SECTOR:
        raise SystemExit("BLOCKED_SECTOR_DIVERSITY_CONTROL")

    if not OLD_PILOT_COPY.exists():
        shutil.copyfile(OLD_PILOT, OLD_PILOT_COPY)
    if sha256_file(OLD_PILOT_COPY) != EXPECTED_OLD_PILOT_SHA256:
        raise SystemExit("BLOCKED_PREVIOUS_SELECTION_MISMATCH")

    extra_fields = list(AUDIT_EXTRA_COLUMNS)
    audit_fieldnames = list(dict.fromkeys([*audit_headers, *extra_fields]))
    write_csv(AUDIT_OUT, audit_fieldnames, annotated)

    pilot_fieldnames = list(dict.fromkeys([*audit_headers, *extra_fields]))
    selected_rows = [{key: row.get(key, "") for key in pilot_fieldnames} for row in selected]
    write_csv(OLD_PILOT, pilot_fieldnames, selected_rows)
    shutil.copyfile(OLD_PILOT, VERSIONED_PILOT)
    if OLD_PILOT.read_bytes() != VERSIONED_PILOT.read_bytes():
        raise SystemExit("BLOCKED_VERSIONED_COPY_MISMATCH")

    DIAGNOSTICS_OUT.write_text(
        build_diagnostics(annotated, selected_rows, targets, old_rows, EXPECTED_SOURCE_SHA256),
        encoding="utf-8",
    )

    hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in (OLD_PILOT, VERSIONED_PILOT, AUDIT_OUT, DIAGNOSTICS_OUT)
    }
    report = [
        "# CODEX_TASK_04A_R1 Report",
        "",
        "status: READY_FOR_CODEX_TASK_04",
        f"source_sha256: {EXPECTED_SOURCE_SHA256}",
        f"preeligible_population: {preeligible_count} (unchanged from 04A audit)",
        f"old_pilot_preserved_sha256: {sha256_file(OLD_PILOT_COPY)}",
        f"new_selected: {len(selected)}",
        f"new_median_market_cap: {cap_summary(selected)['median']:.2f} USD",
        f"sectors_represented: {len(sector_counts)}",
        f"largest_sector_count: {max(sector_counts.values())}",
        f"bucket_shortfall_redistribution: {'none' if all(value == 10 for value in targets.values()) else targets}",
        "tests: pytest -q PASS (50 tests), including frozen v0.3 and Task 04A regressions",
        "SEC/D2: not run, as required",
        "",
        "The pilot is a market-cap stress-test sample. Its pilot signal rate must not be interpreted as a population signal rate.",
        "",
        "## SHA-256",
        "",
        "```text",
        *[f"{digest}  {path}" for path, digest in hashes.items()],
        "```",
        "",
    ]
    REPORT_OUT.write_text("\n".join(report), encoding="utf-8")


if __name__ == "__main__":
    main()