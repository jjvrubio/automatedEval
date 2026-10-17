"""Resumable SQLite state for Stage 2 specialist agents."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from stage1.csv_input import InputRow


THEMES = ("technology", "corporate", "expansion", "meddicc")


class Stage2Store:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self._migrate()

    def _migrate(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS potentiality_research (
                record_id TEXT PRIMARY KEY,
                source_row INTEGER NOT NULL,
                company_name TEXT NOT NULL,
                input_json TEXT NOT NULL,
                eligibility_json TEXT NOT NULL,
                technology_json TEXT,
                technology_raw_json TEXT,
                technology_status TEXT,
                technology_error TEXT,
                corporate_json TEXT,
                corporate_raw_json TEXT,
                corporate_status TEXT,
                corporate_error TEXT,
                expansion_json TEXT,
                expansion_raw_json TEXT,
                expansion_status TEXT,
                expansion_error TEXT,
                meddicc_json TEXT,
                meddicc_raw_json TEXT,
                meddicc_status TEXT,
                meddicc_error TEXT,
                provided_meddicc_path TEXT,
                provided_meddicc_sha256 TEXT,
                provided_meddicc_markdown TEXT,
                provided_meddicc_snapshot_path TEXT,
                report_path TEXT,
                updated_at TEXT NOT NULL
            )
            """
        )
        existing = {
            str(row["name"])
            for row in self.connection.execute(
                "PRAGMA table_info(potentiality_research)"
            ).fetchall()
        }
        for column in (
            "meddicc_json",
            "meddicc_raw_json",
            "meddicc_status",
            "meddicc_error",
            "provided_meddicc_path",
            "provided_meddicc_sha256",
            "provided_meddicc_markdown",
            "provided_meddicc_snapshot_path",
        ):
            if column not in existing:
                self.connection.execute(
                    f"ALTER TABLE potentiality_research ADD COLUMN {column} TEXT"
                )
        self.connection.commit()

    def save_provided_meddicc(
        self,
        record_id: str,
        source_path: Path,
        sha256: str,
        markdown: str,
        snapshot_path: Path,
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            UPDATE potentiality_research SET
                provided_meddicc_path = ?,
                provided_meddicc_sha256 = ?,
                provided_meddicc_markdown = ?,
                provided_meddicc_snapshot_path = ?,
                meddicc_status = 'provided',
                meddicc_error = NULL,
                report_path = NULL,
                updated_at = ?
            WHERE record_id = ?
            """,
            (
                str(source_path),
                sha256,
                markdown,
                str(snapshot_path),
                now,
                record_id,
            ),
        )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> "Stage2Store":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def ensure_row(
        self,
        row: InputRow,
        eligibility: dict[str, Any],
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            INSERT INTO potentiality_research (
                record_id, source_row, company_name, input_json,
                eligibility_json, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(record_id) DO UPDATE SET
                source_row = excluded.source_row,
                company_name = excluded.company_name,
                input_json = excluded.input_json,
                eligibility_json = excluded.eligibility_json,
                updated_at = excluded.updated_at
            """,
            (
                row.record_id,
                row.source_row,
                row.company_name,
                json.dumps(row.values, ensure_ascii=False),
                json.dumps(eligibility, ensure_ascii=False),
                now,
            ),
        )
        self.connection.commit()

    def theme_status(self, record_id: str, theme: str) -> str | None:
        self._validate_theme(theme)
        row = self.connection.execute(
            f"SELECT {theme}_status FROM potentiality_research WHERE record_id = ?",
            (record_id,),
        ).fetchone()
        return str(row[0]) if row and row[0] else None

    def mark_running(self, record_id: str, theme: str) -> None:
        self._validate_theme(theme)
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            f"""
            UPDATE potentiality_research SET
                {theme}_status = 'running',
                {theme}_error = NULL,
                updated_at = ?
            WHERE record_id = ?
            """,
            (now, record_id),
        )
        self.connection.commit()

    def save_theme(
        self,
        record_id: str,
        theme: str,
        result: dict[str, Any],
        raw_response: dict[str, Any],
    ) -> None:
        self._validate_theme(theme)
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            f"""
            UPDATE potentiality_research SET
                {theme}_json = ?,
                {theme}_raw_json = ?,
                {theme}_status = 'ok',
                {theme}_error = NULL,
                report_path = NULL,
                updated_at = ?
            WHERE record_id = ?
            """,
            (
                json.dumps(result, ensure_ascii=False),
                json.dumps(raw_response, ensure_ascii=False),
                now,
                record_id,
            ),
        )
        self.connection.commit()

    def save_error(self, record_id: str, theme: str, error: str) -> None:
        self._validate_theme(theme)
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            f"""
            UPDATE potentiality_research SET
                {theme}_status = 'error',
                {theme}_error = ?,
                updated_at = ?
            WHERE record_id = ?
            """,
            (error, now, record_id),
        )
        self.connection.commit()

    def save_report_path(self, record_id: str, report_path: Path) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            UPDATE potentiality_research SET report_path = ?, updated_at = ?
            WHERE record_id = ?
            """,
            (str(report_path), now, record_id),
        )
        self.connection.commit()

    def record(self, record_id: str) -> dict[str, Any] | None:
        row = self.connection.execute(
            "SELECT * FROM potentiality_research WHERE record_id = ?",
            (record_id,),
        ).fetchone()
        return self._decode(row) if row else None

    def records(self) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            "SELECT * FROM potentiality_research ORDER BY source_row"
        ).fetchall()
        return [self._decode(row) for row in rows]

    @staticmethod
    def _decode(row: sqlite3.Row) -> dict[str, Any]:
        record = dict(row)
        for key in (
            "input_json",
            "eligibility_json",
            "technology_json",
            "technology_raw_json",
            "corporate_json",
            "corporate_raw_json",
            "expansion_json",
            "expansion_raw_json",
            "meddicc_json",
            "meddicc_raw_json",
        ):
            record[key] = json.loads(record[key]) if record.get(key) else None
        return record

    @staticmethod
    def _validate_theme(theme: str) -> None:
        if theme not in THEMES:
            raise ValueError(f"Tema de Etapa 2 no válido: {theme}")
