"""CSV ingestion and normalization."""

from __future__ import annotations

import csv
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


CANONICAL_COLUMNS = (
    "Company Name",
    "# Employees",
    "Website",
    "Company Linkedin Url",
    "Number of Retail Locations",
)

ALIASES = {
    "company name": "Company Name",
    "company name ": "Company Name",
    "# employees": "# Employees",
    "website": "Website",
    "company linkedin url": "Company Linkedin Url",
    "number of retail locations": "Number of Retail Locations",
}


class CsvValidationError(ValueError):
    """Raised when an input CSV does not satisfy the Stage 1 contract."""


@dataclass(frozen=True)
class InputRow:
    record_id: str
    source_row: int
    values: dict[str, str]

    @property
    def company_name(self) -> str:
        return self.values["Company Name"].strip()


def _canonical_header(name: str) -> str:
    stripped = (name or "").strip()
    return ALIASES.get(stripped.casefold(), stripped)


def _record_id(source_row: int, row: dict[str, str]) -> str:
    identity = {
        "source_row": source_row,
        "company": row.get("Company Name", "").strip().casefold(),
        "website": row.get("Website", "").strip().casefold(),
        "linkedin": row.get("Company Linkedin Url", "").strip().casefold(),
    }
    payload = json.dumps(identity, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:20]


def read_csv(path: Path) -> tuple[list[str], list[InputRow]]:
    path = Path(path)
    if not path.exists():
        raise CsvValidationError(f"No existe el CSV: {path}")
    if path.suffix.casefold() != ".csv":
        raise CsvValidationError(f"El archivo debe tener extensión .csv: {path}")

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        source_headers = next(reader, None)
        if not source_headers:
            raise CsvValidationError("El CSV no contiene encabezados.")

        base_headers = [_canonical_header(name) for name in source_headers]
        canonical_headers: list[str] = []
        header_counts: dict[str, int] = {}
        for base in base_headers:
            header_counts[base] = header_counts.get(base, 0) + 1
            count = header_counts[base]
            if count > 1 and base in CANONICAL_COLUMNS:
                raise CsvValidationError(
                    f"La columna obligatoria '{base}' aparece más de una vez."
                )
            canonical_headers.append(base if count == 1 else f"{base} [{count}]")

        missing = [name for name in CANONICAL_COLUMNS if name not in canonical_headers]
        if missing:
            raise CsvValidationError(
                "Faltan columnas obligatorias: " + ", ".join(missing)
            )

        rows: list[InputRow] = []
        for source_row, raw in enumerate(reader, start=2):
            padded = list(raw) + [""] * max(0, len(canonical_headers) - len(raw))
            normalized = {
                canonical: (value or "").strip()
                for canonical, value in zip(canonical_headers, padded)
            }
            if not normalized["Company Name"]:
                continue
            rows.append(
                InputRow(
                    record_id=_record_id(source_row, normalized),
                    source_row=source_row,
                    values=normalized,
                )
            )

    return canonical_headers, rows


def selected_rows(
    rows: Iterable[InputRow],
    start: int = 0,
    limit: int | None = None,
) -> list[InputRow]:
    selected = list(rows)[start:]
    return selected if limit is None else selected[:limit]
