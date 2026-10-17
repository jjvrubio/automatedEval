from __future__ import annotations

import argparse
import os
from collections import Counter
from dataclasses import fields
from datetime import datetime
from pathlib import Path

from .cik_mapper import build_ticker_map
from .d2_engine import ENGINE_VERSION, evaluate_company
from .io_utils import read_tickers, write_rows
from .models import D2Result, FactObservation
from .sec_client import SecClient

RESULT_COLUMNS = tuple(field.name for field in fields(D2Result))
PROVENANCE_COLUMNS = tuple(field.name for field in fields(FactObservation)) + (
    "ticker",
    "cik",
    "taxonomy",
    "source_url",
)


def diagnostics_markdown(total: int, results: list[dict], as_of: str) -> str:
    status_counts: Counter[str] = Counter(
        str(row.get("status")) for row in results if row.get("status")
    )
    nominal_statuses = {"candidate", "discard", "stale_selected_period", "latest_fy_unresolved"}
    fresh_statuses = {"candidate", "discard"}
    nominal_processable = sum(row.get("status") in nominal_statuses for row in results)
    fresh_processable = sum(
        row.get("status") in fresh_statuses and row.get("freshness_status") == "fresh"
        for row in results
    )
    nominal_coverage = nominal_processable / total if total else 0.0
    fresh_coverage = fresh_processable / total if total else 0.0
    d2_signals = sum(row.get("d2_signal") is True for row in results)
    latest_fy_unresolved_rows = [
        row
        for row in results
        if row.get("status") == "latest_fy_unresolved"
    ]
    lines = [
        "# P1.D2 diagnostics v0.3",
        "",
        f"engine_version: {ENGINE_VERSION}",
        "task: CODEX_TASK_03",
        f"as_of: {as_of}",
        "",
        f"- N0: {total}",
        f"- nominal_processable: {nominal_processable}",
        f"- fresh_processable: {fresh_processable}",
        f"- nominal_coverage: {nominal_coverage:.1%}",
        f"- fresh_coverage: {fresh_coverage:.1%}",
        f"- D2_signals: {d2_signals}",
        f"- latest_fy_unresolved count: {len(latest_fy_unresolved_rows)}",
        "",
        "## Status counts",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"| {status} | {count} |")
    lines += [
        "",
        "## Latest FY unresolved",
        "",
        "| Ticker | Selected FY | Latest annual period observed | Missing metric |",
        "|---|---|---|---|",
    ]
    for row in latest_fy_unresolved_rows:
        lines.append(
            "| {ticker} | {selected} | {latest} | {metric} |".format(
                ticker=row.get("ticker") or "",
                selected=row.get("selected_fy_t_end") or "",
                latest=row.get("latest_annual_period_end_observed") or "",
                metric=row.get("missing_latest_fy_metric") or "",
            )
        )
    lines += [
        "",
        "## Technical gate",
        "",
        "PASS" if fresh_coverage >= 0.70 else "FAIL",
        "",
        "> Do not tune D2 thresholds if this gate fails; fix data coverage first.",
    ]
    return "\n".join(lines) + "\n"


def run(args: argparse.Namespace) -> int:
    user_agent = os.environ.get("SEC_USER_AGENT", "").strip()
    if not user_agent:
        raise SystemExit(
            "Set SEC_USER_AGENT to an identifiable value, e.g. 'Your Name your@email.com'."
        )

    client = SecClient(user_agent=user_agent, cache_dir=args.cache_dir)
    ticker_map = build_ticker_map(client.ticker_map_raw(refresh=args.refresh))
    tickers = read_tickers(args.input)
    if args.limit:
        tickers = tickers[: args.limit]
    run_time = datetime.now().astimezone()
    as_of = run_time.date()
    as_of_timestamp = run_time.isoformat(timespec="seconds")

    results = []
    provenance = []
    statuses: Counter[str] = Counter()

    for ticker in tickers:
        identity = ticker_map.get(ticker)
        if identity is None:
            results.append(
                D2Result(
                    engine_version=ENGINE_VERSION,
                    ticker=ticker,
                    cik=None,
                    company=None,
                    status="missing_cik",
                    reason="Ticker not found in SEC mapping",
                ).to_row()
            )
            statuses["missing_cik"] += 1
            continue

        try:
            facts = client.companyfacts(identity.cik, refresh=args.refresh)
            result, used_facts = evaluate_company(
                ticker=ticker,
                cik=identity.cik,
                companyfacts=facts,
                company_name=identity.title,
                as_of=as_of,
            )
        except Exception as exc:  # explicit prototype-level capture; preserve error in output
            results.append(
                D2Result(
                    engine_version=ENGINE_VERSION,
                    ticker=ticker,
                    cik=identity.cik,
                    company=identity.title,
                    status="fetch_or_parse_error",
                    reason=f"{type(exc).__name__}: {exc}",
                ).to_row()
            )
            statuses["fetch_or_parse_error"] += 1
            continue

        results.append(result.to_row())
        statuses[result.status] += 1
        for fact in used_facts:
            provenance.append(fact.provenance_row(ticker, identity.cik))

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_rows(out_dir / "D2_results_v03.csv", results, RESULT_COLUMNS)
    write_rows(out_dir / "D2_provenance_v03.csv", provenance, PROVENANCE_COLUMNS)
    (out_dir / "D2_diagnostics_v03.md").write_text(
        diagnostics_markdown(len(tickers), results, as_of_timestamp), encoding="utf-8"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="P1.D2 SEC annual prototype")
    sub = parser.add_subparsers(dest="command", required=True)
    run_p = sub.add_parser("run", help="Run the prototype on a ticker CSV")
    run_p.add_argument("--input", default="input/tickers_technical.csv")
    run_p.add_argument("--output", default="output")
    run_p.add_argument("--cache-dir", default=".cache/sec")
    run_p.add_argument("--limit", type=int, default=None)
    run_p.add_argument("--refresh", action="store_true")
    run_p.set_defaults(func=run)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
