from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_tickers(path: str | Path) -> list[str]:
    with Path(path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if "ticker" not in (reader.fieldnames or []):
            raise ValueError("Input CSV must contain a 'ticker' column")
        return [str(row["ticker"]).strip().upper() for row in reader if row.get("ticker")]


def write_rows(
    path: str | Path,
    rows: Iterable[dict],
    fieldnames: Sequence[str] | None = None,
) -> None:
    rows = list(rows)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(dict.fromkeys(key for row in rows for key in row))
    if not rows and not fieldnames:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(fieldnames), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
