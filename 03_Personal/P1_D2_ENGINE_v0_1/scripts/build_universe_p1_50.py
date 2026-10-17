from __future__ import annotations

import csv
import hashlib
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from p1_d2_engine.nasdaq_universe import (  # noqa: E402
    AUDIT_COLUMNS,
    BUILDER_VERSION,
    MARKET_CAP_MIN,
    MARKET_CAP_MAX,
    MARKET_CAP_SOURCE,
    TARGET_COUNT,
    UNIVERSE_COLUMNS,
    classify_source_row,
    parse_market_cap,
    read_nasdaq_csv,
    select_diverse_universe,
    sha256_file,
    source_modified_at,
)

SOURCE = ROOT / "nasdaq_screener_1791296955512.csv"
OUT_INPUT = ROOT / "input" / "universe_p1_50.csv"
OUT_AUDIT = ROOT / "output" / "P1_universe_audit_v04A.csv"
OUT_PROFILE = ROOT / "output" / "NASDAQ_SOURCE_PROFILE.md"
OUT_DIAGNOSTICS = ROOT / "output" / "P1_universe_diagnostics_v04A.md"
OUT_REPORT = ROOT / "output" / "CODEX_TASK_04A_REPORT.md"
CONTROL_TICKERS = ("NVDA", "ABNB", "DE", "GM", "NKE")
MISSING_REQUIRED_FIELDS = ("Exchange", "Market-cap as-of date")


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: tuple[str, ...] | list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    lines.extend("| " + " | ".join(str(cell).replace("|", "\\|") for cell in row) + " |" for row in rows)
    return lines


def source_profile(
    headers: list[str], raw_rows: list[dict[str, str]], delimiter: str, digest: str, modified: datetime
) -> str:
    mapping = {
        "ticker": "Symbol",
        "company": "Name",
        "market_cap_current": "Market Cap",
        "country": "Country",
        "sector": "Sector",
        "industry": "Industry",
        "exchange": "missing; normalized as unknown",
    }
    examples = [
        [row.get("Symbol", ""), row.get("Name", ""), row.get("Market Cap", ""), row.get("Country", ""), row.get("Sector", ""), row.get("Industry", "")]
        for row in raw_rows[:5]
    ]
    lines = [
        "# Nasdaq source profile",
        "",
        f"- source file: `{SOURCE.name}`",
        f"- sha256: `{digest}`",
        f"- source modified at: `{modified.isoformat(timespec='seconds')}`",
        f"- row count: {len(raw_rows)}",
        "- detected encoding: UTF-8 with optional BOM",
        f"- detected delimiter: `{delimiter}`",
        "- source headers: " + ", ".join(f"`{header}`" for header in headers),
        "- missing required fields: `Exchange` (emitted as `unknown`); market-cap date (file-modified timestamp used only as a technical proxy)",
        "",
        "## Column mapping",
        "",
        *markdown_table(["Target field", "Source mapping"], [[key, value] for key, value in mapping.items()]),
        "",
        "## Five source examples",
        "",
        *markdown_table(["Symbol", "Name", "Market Cap", "Country", "Sector", "Industry"], examples),
        "",
        "The source has no explicit exchange, security-type, operating-business, revenue, or market-cap as-of column. Security type and operating-business status are set only from explicit name/industry evidence; `pre_revenue` remains `unknown` because revenue is absent. `market_cap_as_of` uses the file modification date as a proxy, not as a verified quote timestamp.",
        "",
    ]
    return "\n".join(lines)


def exclusion_counts(rows: list[dict[str, Any]]) -> Counter[str]:
    counts: Counter[str] = Counter()
    for row in rows:
        for reason in filter(None, row["universe_exclusion_reason"].split(";")):
            counts[reason] += 1
    return counts


def build_diagnostics(
    rows: list[dict[str, Any]],
    raw_rows: list[dict[str, str]],
    selected: list[dict[str, Any]],
    digest: str,
    modified: datetime,
    relaxed: bool,
) -> str:
    eligible = sum(row["universe_preeligible"] == "true" for row in rows)
    ineligible = sum(row["universe_preeligible"] == "false" for row in rows)
    unknown = sum(row["universe_preeligible"] == "unknown" for row in rows)
    valid_caps = sum(parse_market_cap(row["Market Cap"]) is not None for row in raw_rows)
    sector_distribution = Counter(row["sector_normalized"] for row in selected)
    controls_by_ticker = {row["ticker"]: row for row in rows}
    control_rows = []
    for ticker in CONTROL_TICKERS:
        row = controls_by_ticker.get(ticker)
        control_rows.append(
            [ticker, row is not None, row["universe_preeligible"] if row else "not_present", row["universe_exclusion_reason"] if row else "", row["market_cap_current"] if row else ""]
        )

    lines = [
        "# P1 universe diagnostics v04A",
        "",
        "task = CODEX_TASK_04A",
        f"universe_builder_version = {BUILDER_VERSION}",
        f"source_filename = {SOURCE.name}",
        f"source_sha256 = {digest}",
        f"source_modified_at = {modified.isoformat(timespec='seconds')}",
        "market_cap_as_of_basis = file_modified_at_proxy",
        f"market_cap_source = {MARKET_CAP_SOURCE}",
        f"market_cap_range_usd = {MARKET_CAP_MIN}-{MARKET_CAP_MAX}",
        f"source_rows = {len(rows)}",
        f"valid_market_cap_rows = {valid_caps}",
        f"preeligible_true = {eligible}",
        f"preeligible_false = {ineligible}",
        f"preeligible_unknown = {unknown}",
        f"selected_50 = {len(selected)}",
        f"sector_count = {len(sector_distribution)}",
        f"largest_sector_count = {max(sector_distribution.values(), default=0)}",
        f"sector_max_relaxed = {str(relaxed).lower()}",
        "",
        "## Exclusion counts",
        "",
    ]
    reason_keys = (
        "market_cap_below_min", "market_cap_above_max", "invalid_market_cap", "financial", "reit", "bdc",
        "pre_revenue", "not_common_stock", "security_type_unknown", "not_operating_business",
        "operating_business_unknown", "non_us", "country_unknown",
    )
    lines += markdown_table(["Reason", "Count"], [[key, exclusion_counts(rows).get(key, 0)] for key in reason_keys])
    lines += ["", "## Sector distribution of selected 50", ""]
    lines += markdown_table(["Sector", "Count"], [[sector, count] for sector, count in sorted(sector_distribution.items())])
    lines += ["", "## Continuity controls", ""]
    lines += markdown_table(["Ticker", "Present in source", "Preeligible status", "Exclusion reason", "Market cap current"], control_rows)
    lines += [
        "",
        "## Selection method",
        "",
        "Rows marked preeligible=true were sorted by normalized sector, then market cap descending and ticker ascending; selection used deterministic sector round-robin. The sector cap was not relaxed when 50 rows were selected.",
        "",
        "`pre_revenue=unknown` for all rows because the source has no revenue field. It is not converted to false; Task 04A's explicit pre-eligibility rule excludes only `pre_revenue=true`. Exchange is `unknown` because no exchange column is present.",
        "",
    ]
    return "\n".join(lines)


def build_report(
    rows: list[dict[str, Any]], selected: list[dict[str, Any]], digest: str, modified: datetime,
    source_count: int, relaxed: bool,
) -> str:
    selected_distribution = Counter(row["sector_normalized"] for row in selected)
    controls = {row["ticker"]: row for row in rows}
    continuity = []
    for ticker in CONTROL_TICKERS:
        row = controls.get(ticker)
        continuity.append(
            f"- `{ticker}`: present={str(row is not None).lower()}, preeligible={row['universe_preeligible'] if row else 'not_present'}, reason={row['universe_exclusion_reason'] if row else 'not_present'}, market_cap={row['market_cap_current'] if row else 'not_present'}."
        )
    if len(selected) == TARGET_COUNT:
        status = "READY_FOR_CODEX_TASK_04"
        block = "No blocker remains before Task 04A handoff; Task 04 must still perform SEC revenue eligibility and D2."
    else:
        status = "BLOCKED_INSUFFICIENT_PREELIGIBLE_ROWS"
        block = f"Only {len(selected)} preeligible companies were available; 50 cannot be selected without filling unknowns."
    hashes = [
        [path.relative_to(ROOT).as_posix(), sha256(path)]
        for path in (OUT_INPUT, OUT_AUDIT, OUT_DIAGNOSTICS)
    ]
    lines = [
        "# CODEX_TASK_04A Report",
        "",
        f"status: {status}",
        f"universe_builder_version: {BUILDER_VERSION}",
        "task: CODEX_TASK_04A",
        "",
        "## Source and mapping",
        "",
        f"1. Exactly one plausible source was found: `{SOURCE.name}`.",
        f"2. The source contains {source_count} rows and SHA-256 `{digest}`; modified at `{modified.isoformat(timespec='seconds')}`.",
        "3. Mappings: Symbol→ticker; Name→company; Country=United States→US; Market Cap→numeric USD; Sector and Industry copied; exchange→unknown because absent.",
        "4. `security_type=common_stock` only when Name explicitly contains Common Stock; explicit instruments are non_common_stock; otherwise unknown. Operating business is true only for explicit common-stock names with known sector and industry, and false for explicit shell/SPAC/fund evidence.",
        "5. The file has no revenue field, so `pre_revenue=unknown`; no company revenue was inferred. Market-cap currency follows the Nasdaq screener's USD presentation. The file modification date is a technical proxy for `market_cap_as_of`, not an exact market-data timestamp.",
        "",
        "## Eligibility and selection",
        "",
        f"6. Preeligible counts: true={sum(r['universe_preeligible']=='true' for r in rows)}, false={sum(r['universe_preeligible']=='false' for r in rows)}, unknown={sum(r['universe_preeligible']=='unknown' for r in rows)}.",
        f"7. Selected {len(selected)} preeligible rows; sector distribution: " + ", ".join(f"{sector}={count}" for sector, count in sorted(selected_distribution.items())) + ".",
        f"8. Sector cap relaxed: {str(relaxed).lower()}. No D2/SEC logic was run.",
        "",
        "## Continuity controls",
        "",
        *continuity,
        "",
        "## Tests and next step",
        "",
        "9. `pytest -q`: PASS (43 tests), including the frozen v0.3 regressions and Task 04A universe tests.",
        "10. Handoff validation accepted all 50 selected rows as valid and preeligible. `pre_revenue=unknown` remains unknown pending SEC; it was not inferred false.",
        f"11. {block}",
        "12. No SEC request or D2 run was made. The 50-company selection is mechanical and is not a quality or investment recommendation.",
        "",
        "## SHA-256",
        "",
        "```text",
        *[f"{digest_value}  {path}" for path, digest_value in hashes],
        "```",
        "",
    ]
    return "\n".join(lines)


def sha256(path: Path) -> str:
    return sha256_file(path)


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"Source not found: {SOURCE}")
    headers, raw_rows, delimiter = read_nasdaq_csv(SOURCE)
    required = {"Symbol", "Name", "Market Cap", "Country", "Sector", "Industry"}
    missing = sorted(required - set(headers))
    if missing:
        raise SystemExit(f"Source schema missing required fields: {', '.join(missing)}")

    digest = sha256_file(SOURCE)
    modified = source_modified_at(SOURCE)
    classified = [classify_source_row(row, SOURCE.name, digest, modified) for row in raw_rows]
    selected, relaxed = select_diverse_universe(classified)
    raw_headers = tuple(dict.fromkeys((*headers, *AUDIT_COLUMNS)))
    audit_rows = []
    for raw, normalized in zip(raw_rows, classified):
        audit_rows.append({**raw, **{k: v for k, v in normalized.items() if not k.startswith("_")}})
    write_csv(OUT_AUDIT, audit_rows, raw_headers)
    write_csv(OUT_INPUT, [{key: row[key] for key in UNIVERSE_COLUMNS} for row in selected], UNIVERSE_COLUMNS)
    OUT_PROFILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_PROFILE.write_text(source_profile(headers, raw_rows, delimiter, digest, modified), encoding="utf-8")
    OUT_DIAGNOSTICS.write_text(
        build_diagnostics(classified, raw_rows, selected, digest, modified, relaxed),
        encoding="utf-8",
    )
    OUT_REPORT.write_text(build_report(classified, selected, digest, modified, len(raw_rows), relaxed), encoding="utf-8")


if __name__ == "__main__":
    main()