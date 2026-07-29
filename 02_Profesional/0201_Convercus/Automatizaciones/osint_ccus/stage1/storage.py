"""SQLite state store for resumable Stage 1 runs."""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .csv_input import InputRow


class Stage1Store:
    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(self.path)
        self.connection.row_factory = sqlite3.Row
        self._migrate()

    def _migrate(self) -> None:
        self.connection.execute(
            """
            CREATE TABLE IF NOT EXISTS company_research (
                record_id TEXT PRIMARY KEY,
                source_row INTEGER NOT NULL,
                company_name TEXT NOT NULL,
                input_json TEXT NOT NULL,
                employees_json TEXT,
                locations_json TEXT,
                decision_json TEXT,
                revenue_json TEXT,
                final_decision_json TEXT,
                raw_response_json TEXT,
                status TEXT NOT NULL,
                error TEXT,
                revenue_status TEXT,
                revenue_error TEXT,
                updated_at TEXT NOT NULL
            )
            """
        )
        existing = {
            str(row["name"])
            for row in self.connection.execute(
                "PRAGMA table_info(company_research)"
            ).fetchall()
        }
        additions = {
            "revenue_json": "TEXT",
            "final_decision_json": "TEXT",
            "revenue_status": "TEXT",
            "revenue_error": "TEXT",
        }
        for column, sql_type in additions.items():
            if column not in existing:
                self.connection.execute(
                    f"ALTER TABLE company_research ADD COLUMN {column} {sql_type}"
                )
        self.connection.commit()

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> "Stage1Store":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def status(self, record_id: str) -> str | None:
        row = self.connection.execute(
            "SELECT status FROM company_research WHERE record_id = ?",
            (record_id,),
        ).fetchone()
        return str(row["status"]) if row else None

    def mark_running(self, row: InputRow) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            INSERT INTO company_research (
                record_id, source_row, company_name, input_json, status, updated_at
            ) VALUES (?, ?, ?, ?, 'running', ?)
            ON CONFLICT(record_id) DO UPDATE SET
                source_row = excluded.source_row,
                company_name = excluded.company_name,
                input_json = excluded.input_json,
                status = 'running',
                error = NULL,
                revenue_json = NULL,
                final_decision_json = NULL,
                revenue_status = NULL,
                revenue_error = NULL,
                updated_at = excluded.updated_at
            """,
            (
                row.record_id,
                row.source_row,
                row.company_name,
                json.dumps(row.values, ensure_ascii=False),
                now,
            ),
        )
        self.connection.commit()

    def save_success(
        self,
        row: InputRow,
        employees: dict[str, Any],
        locations: dict[str, Any],
        decision: dict[str, Any],
        raw_responses: list[dict[str, Any]],
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            UPDATE company_research SET
                employees_json = ?,
                locations_json = ?,
                decision_json = ?,
                raw_response_json = ?,
                status = 'ok',
                error = NULL,
                updated_at = ?
            WHERE record_id = ?
            """,
            (
                json.dumps(employees, ensure_ascii=False),
                json.dumps(locations, ensure_ascii=False),
                json.dumps(decision, ensure_ascii=False),
                json.dumps(raw_responses, ensure_ascii=False),
                now,
                row.record_id,
            ),
        )
        self.connection.commit()

    def save_error(self, row: InputRow, error: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            UPDATE company_research SET
                status = 'error',
                error = ?,
                updated_at = ?
            WHERE record_id = ?
            """,
            (error, now, row.record_id),
        )
        self.connection.commit()

    def save_revenue_success(
        self,
        row: InputRow,
        revenue: dict[str, Any],
        final_decision: dict[str, Any],
        raw_response: dict[str, Any],
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        current = self.connection.execute(
            "SELECT raw_response_json FROM company_research WHERE record_id = ?",
            (row.record_id,),
        ).fetchone()
        raw_responses = []
        if current and current["raw_response_json"]:
            raw_responses = json.loads(current["raw_response_json"])
        raw_responses.append(raw_response)
        self.connection.execute(
            """
            UPDATE company_research SET
                revenue_json = ?,
                final_decision_json = ?,
                raw_response_json = ?,
                revenue_status = 'ok',
                revenue_error = NULL,
                updated_at = ?
            WHERE record_id = ?
            """,
            (
                json.dumps(revenue, ensure_ascii=False),
                json.dumps(final_decision, ensure_ascii=False),
                json.dumps(raw_responses, ensure_ascii=False),
                now,
                row.record_id,
            ),
        )
        self.connection.commit()

    def save_revenue_error(self, row: InputRow, error: str) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            UPDATE company_research SET
                revenue_status = 'error',
                revenue_error = ?,
                updated_at = ?
            WHERE record_id = ?
            """,
            (error, now, row.record_id),
        )
        self.connection.commit()

    def save_final_decision(
        self,
        row: InputRow,
        final_decision: dict[str, Any],
    ) -> None:
        now = datetime.now(timezone.utc).isoformat()
        self.connection.execute(
            """
            UPDATE company_research SET
                final_decision_json = ?,
                updated_at = ?
            WHERE record_id = ?
            """,
            (
                json.dumps(final_decision, ensure_ascii=False),
                now,
                row.record_id,
            ),
        )
        self.connection.commit()

    def record(self, record_id: str) -> dict[str, Any] | None:
        row = self.connection.execute(
            "SELECT * FROM company_research WHERE record_id = ?",
            (record_id,),
        ).fetchone()
        return self._decode(row) if row else None

    def records(self) -> list[dict[str, Any]]:
        rows = self.connection.execute(
            "SELECT * FROM company_research ORDER BY source_row"
        ).fetchall()
        return [self._decode(row) for row in rows]

    @staticmethod
    def _decode(row: sqlite3.Row) -> dict[str, Any]:
        record = dict(row)
        for key in (
            "input_json",
            "employees_json",
            "locations_json",
            "decision_json",
            "revenue_json",
            "final_decision_json",
            "raw_response_json",
        ):
            record[key] = json.loads(record[key]) if record.get(key) else None
        return record
