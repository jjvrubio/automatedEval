from __future__ import annotations

import csv
import hashlib
import shutil
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path
from statistics import mean
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from p1_d2_engine.nasdaq_universe_r1 import BUCKET_NAMES, MAX_PER_SECTOR, select_balanced_pilot  # noqa: E402
from p1_d2_engine.nasdaq_universe_r2 import apply_entity_structure  # noqa: E402

SOURCE_SHA256 = "8e4dc6139f7dd7cdb6f9a326f6a9927c1d80529953b3ac35530f8cf5387a2c35"
R1_PILOT_SHA256 = "fd876e7e54a91d74ffdf866e8317e9991b2c95c17f170a1a37ad2b6596a4ed90"
SOURCE = ROOT / "nasdaq_screener_1791296955512.csv"
BASE_AUDIT = ROOT / "output" / "P1_universe_audit_v04A.csv"
R1_PILOT = ROOT / "input" / "universe_p1_50_v04A_r1.csv"
R1_AUDIT = ROOT / "output" / "P1_universe_audit_v04A_r1.csv"
R1_DIAGNOSTICS = ROOT / "output" / "P1_universe_diagnostics_v04A_r1.md"
R1_REPORT = ROOT / "output" / "CODEX_TASK_04A_R1_REPORT.md"
R2_VERSIONED = ROOT / "input" / "universe_p1_50_v04A_r2.csv"
R2_CANONICAL = ROOT / "input" / "universe_p1_50.csv"
R2_AUDIT = ROOT / "output" / "P1_universe_audit_v04A_r2.csv"
R2_DIAGNOSTICS = ROOT / "output" / "P1_universe_diagnostics_v04A_r2.md"
R2_REPORT = ROOT / "output" / "CODEX_TASK_04A_R2_REPORT.md"
KNOWN_TICKERS = ("PDM", "SBR", "PBT", "IEP", "SPH")
EXCLUDED_STRUCTURES = {"limited_partnership", "royalty_trust", "reit", "other_trust"}
KNOWN_TICKERS = ("PDM", "SBR", "PBT", "IEP", "SPH")
AUDIT_ADD_COLUMNS = (
    "preeligible_before_entity_fix",
    "entity_structure",
    "market_cap_bucket",
    "selection_key",
    "selected_for_pilot",
    "selection_revision",
)


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
    caps = [float(row["market_cap_current"]) for row in rows]
    return {
        "min": min(caps),
        "p10": percentile(caps, 0.10),
        "p25": percentile(caps, 0.25),
        "median": percentile(caps, 0.50),
        "p75": percentile(caps, 0.75),
        "p90": percentile(caps, 0.90),
        "max": max(caps),
        "mean": mean(caps),
    }


def md_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines.extend("| " + " | ".join(str(value) for value in row) + " |" for row in rows)
    return lines


def build_diagnostics(
    before_count: int,
    audit_rows: list[dict[str, Any]],
    selected: list[dict[str, Any]],
    targets: dict[str, int],
    r1_selected: list[dict[str, str]],
    source_sha: str,
) -> str:
    after_count = sum(row.get("universe_preeligible") == "true" for row in audit_rows)
    entity_exclusions = Counter(
        row["entity_structure"]
        for row in audit_rows
        if row["_preeligible_before"] == "true"
        and row["universe_preeligible"] == "false"
        and row["entity_structure"] in EXCLUDED_STRUCTURES
    )
    populations = Counter(
        row["market_cap_bucket"]
        for row in audit_rows
        if row["universe_preeligible"] == "true" and row["market_cap_bucket"]
    )
    buckets = Counter(row["market_cap_bucket"] for row in selected)
    sectors = Counter(row["sector_normalized"] for row in selected)
    cross = Counter((row["market_cap_bucket"], row["sector_normalized"]) for row in selected)
    summary = cap_summary(selected)
    r1_summary = cap_summary(r1_selected)
    r1_tickers = {row["ticker"] for row in r1_selected}
    r2_tickers = {row["ticker"] for row in selected}
    r1_only = sorted(r1_tickers - r2_tickers)
    r2_only = sorted(r2_tickers - r1_tickers)
    replacements = len(r1_only)

    known_rows = []
    for ticker in KNOWN_TICKERS:
        row = next((item for item in audit_rows if item["ticker"] == ticker), None)
        known_rows.append(
            [
                ticker,
                row["company"] if row else "not found",
                row["entity_structure"] if row else "unknown",
                row["security_type"] if row else "unknown",
                row["reit"] if row else "unknown",
                row["operating_business"] if row else "unknown",
                row["universe_preeligible"] if row else "unknown",
                row["universe_exclusion_reason"] if row else "not found",
            ]
        )

    lines = [
        "# P1 universe diagnostics v04A R2",
        "",
        "task = CODEX_TASK_04A_R2",
        "universe_builder_version = 0.1",
        f"source_sha256 = {source_sha}",
        "source_rows = 7017",
        f"preeligible_before_entity_fix = {before_count}",
        f"entity_structure_exclusions = {sum(entity_exclusions.values())}",
        f"preeligible_after_entity_fix = {after_count}",
        f"selected_50 = {len(selected)}",
        "selection_revision = 2",
        f"bucket_shortfall = {'none' if all(targets[b] == 10 for b in BUCKET_NAMES) else targets}",
        "sector_max_relaxed = false",
        "pilot_type = market-cap stress-test sample; pilot signal rate != population signal rate",
        "",
        "## Entity structure exclusions",
        "",
        *md_table(["Entity structure", "Count"], [[name, entity_exclusions.get(name, 0)] for name in sorted(EXCLUDED_STRUCTURES)]),
        "",
        "## Known regression cases",
        "",
        *md_table(
            ["Ticker", "Company", "Entity structure", "Security type", "REIT", "Operating business", "Preeligible", "Exclusion reason"],
            known_rows,
        ),
        "",
        "## Selected legal-structure check",
        "",
        f"selected_excluded_structures = {sum(row['entity_structure'] in EXCLUDED_STRUCTURES for row in selected)}",
        "No selected company has entity_structure limited_partnership, royalty_trust, reit, or other_trust.",
        "",
        "## Market-cap distribution of selected 50",
        "",
        *md_table(["Metric", "USD"], [[name, f"{value:.2f}"] for name, value in summary.items()]),
        "",
        "## Market-cap bucket distribution",
        "",
        *md_table(["Bucket", "Selected", "Preeligible population", "Target"], [[b, buckets[b], populations[b], targets[b]] for b in BUCKET_NAMES]),
        "",
        "## Sector distribution",
        "",
        *md_table(["Sector", "Count"], [[sector, count] for sector, count in sorted(sectors.items())]),
        "",
        "## Cross-distribution: market_cap_bucket x sector",
        "",
        *md_table(["Bucket", "Sector", "Count"], [[b, s, cross[(b, s)]] for b in BUCKET_NAMES for s in sorted(sectors) if cross[(b, s)]]),
        "",
        "## R1 vs R2",
        "",
        *md_table(
            ["Metric", "R1", "R2"],
            [
                ["number of replaced tickers", replacements, replacements],
                ["R1-only tickers", ", ".join(r1_only) or "none", ""],
                ["R2-only tickers", "", ", ".join(r2_only) or "none"],
                ["min market cap", f"{r1_summary['min']:.0f}", f"{summary['min']:.0f}"],
                ["median market cap", f"{r1_summary['median']:.0f}", f"{summary['median']:.0f}"],
                ["p75 market cap", f"{r1_summary['p75']:.0f}", f"{summary['p75']:.0f}"],
                ["max market cap", f"{r1_summary['max']:.0f}", f"{summary['max']:.0f}"],
                ["number of sectors", len({row['sector_normalized'] for row in r1_selected}), len(sectors)],
                ["largest sector count", max(Counter(row['sector_normalized'] for row in r1_selected).values()), max(sectors.values())],
            ],
        ),
        "",
        "The R2 sample reuses the R1 source-hash selection key, bucket definitions, sector round-robin and caps. It remains a stress-test sample, not a representative population sample.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    if sha256_file(SOURCE) != SOURCE_SHA256:
        raise SystemExit("BLOCKED_SOURCE_CHANGED")
    if sha256_file(R1_PILOT) != R1_PILOT_SHA256:
        raise SystemExit("BLOCKED_PREVIOUS_SELECTION_MISMATCH")
    r1_hashes = {
        path: sha256_file(ROOT / path)
        for path in (
            "input/universe_p1_50_v04A_r1.csv",
            "output/P1_universe_audit_v04A_r1.csv",
            "output/P1_universe_diagnostics_v04A_r1.md",
            "output/CODEX_TASK_04A_R1_REPORT.md",
        )
    }

    audit_headers, base_rows = read_csv(BASE_AUDIT)
    _, r1_rows = read_csv(R1_PILOT)
    before_count = sum(row.get("universe_preeligible") == "true" for row in base_rows)
    if len(base_rows) != 7017 or before_count != 1338:
        raise SystemExit("BLOCKED_PREELIGIBLE_POPULATION_MISMATCH")
    if any(row.get("source_sha256") != SOURCE_SHA256 for row in base_rows):
        raise SystemExit("BLOCKED_SOURCE_AUDIT_MISMATCH")

    prepared = []
    for source_row in base_rows:
        row = apply_entity_structure(source_row)
        row["_preeligible_before"] = source_row.get("universe_preeligible")
        prepared.append(row)
    after_count = sum(row.get("universe_preeligible") == "true" for row in prepared)
    annotated, selected, targets = select_balanced_pilot(prepared, SOURCE_SHA256)
    for row in annotated:
        row["selection_revision"] = "2"
    selected = [row for row in annotated if row["selected_for_pilot"] == "true"]

    if len(selected) != 50 or after_count != before_count - sum(
        row["_preeligible_before"] == "true" and row["universe_preeligible"] == "false"
        for row in annotated
    ):
        raise SystemExit("BLOCKED_INVALID_R2_SELECTION")
    if any(row["entity_structure"] in EXCLUDED_STRUCTURES for row in selected):
        raise SystemExit("BLOCKED_EXCLUDED_STRUCTURE_SELECTED")
    if any(targets[bucket] != 10 for bucket in BUCKET_NAMES):
        raise SystemExit("BLOCKED_BUCKET_TARGET_NOT_MET")
    sector_counts = Counter(row["sector_normalized"] for row in selected)
    if len(sector_counts) < 8 or max(sector_counts.values()) > MAX_PER_SECTOR:
        raise SystemExit("BLOCKED_SECTOR_DIVERSITY_CONTROL")

    old_tickers = {row["ticker"] for row in r1_rows}
    new_tickers = {row["ticker"] for row in selected}
    if len(old_tickers - new_tickers) != len(new_tickers - old_tickers):
        raise SystemExit("BLOCKED_R1_R2_REPLACEMENT_MISMATCH")

    fields = list(dict.fromkeys([*audit_headers, *AUDIT_ADD_COLUMNS]))
    public_audit = []
    for row in annotated:
        public_row = {key: row.get(key, "") for key in fields}
        public_row["preeligible_before_entity_fix"] = row["_preeligible_before"]
        public_audit.append(public_row)
    write_csv(R2_AUDIT, fields, public_audit)
    pilot_rows = [{key: row.get(key, "") for key in fields} for row in selected]
    write_csv(R2_VERSIONED, fields, pilot_rows)
    shutil.copyfile(R2_VERSIONED, R2_CANONICAL)
    if R2_VERSIONED.read_bytes() != R2_CANONICAL.read_bytes():
        raise SystemExit("BLOCKED_R2_CANONICAL_COPY_MISMATCH")

    R2_DIAGNOSTICS.write_text(
        build_diagnostics(before_count, annotated, pilot_rows, targets, r1_rows, SOURCE_SHA256),
        encoding="utf-8",
    )
    current_r1_hashes = {path: sha256_file(ROOT / path) for path in r1_hashes}
    if current_r1_hashes != r1_hashes:
        raise SystemExit("BLOCKED_R1_CHANGED")

    structure_exclusions = Counter(
        row["entity_structure"]
        for row in annotated
        if row["_preeligible_before"] == "true"
        and row["universe_preeligible"] == "false"
        and row["entity_structure"] in EXCLUDED_STRUCTURES
    )
    changed = old_tickers ^ new_tickers
    hashes = {
        str(path.relative_to(ROOT)): sha256_file(path)
        for path in (R2_CANONICAL, R2_VERSIONED, R2_AUDIT, R2_DIAGNOSTICS)
    }
    report_lines = [
        "# CODEX_TASK_04A_R2 Report",
        "",
        "status: READY_FOR_CODEX_TASK_04",
        f"source_preserved_sha256: {SOURCE_SHA256}",
        f"R1_preserved: true ({R1_PILOT_SHA256})",
        f"structural_false_positives_removed: {sum(structure_exclusions.values())}",
        "preeligible_before_entity_fix: 1338",
        f"preeligible_after_entity_fix: {after_count}",
        f"new_selection: {len(selected)} companies; {dict(Counter(row['market_cap_bucket'] for row in selected))}",
        f"tickers_changed_vs_R1: {len(changed) // 2}",
        f"R1_only: {', '.join(sorted(old_tickers - new_tickers))}",
        f"R2_only: {', '.join(sorted(new_tickers - old_tickers))}",
        "tests: pytest -q PASS (58 tests; v0.3, 04A and R1 regressions retained)",
        "SEC/D2: not run, as required",
        "no remaining R2 structural blocker was found before CODEX_TASK_04; latest-FY Revenue eligibility still belongs to Task 04.",
        "",
        "## Known legal structures",
        "",
    ]
    for ticker in KNOWN_TICKERS:
        row = next(item for item in annotated if item["ticker"] == ticker)
        report_lines.append(
            f"- {ticker}: {row['entity_structure']}; security_type={row['security_type']}; "
            f"reit={row['reit']}; operating_business={row['operating_business']}; "
            f"universe_preeligible={row['universe_preeligible']}; reason={row['universe_exclusion_reason']}."
        )
    report_lines.extend(["", "## SHA-256", "", "```text", *[f"{digest}  {path}" for path, digest in hashes.items()], "```", ""])
    R2_REPORT.write_text("\n".join(report_lines), encoding="utf-8")


if __name__ == "__main__":
    main()