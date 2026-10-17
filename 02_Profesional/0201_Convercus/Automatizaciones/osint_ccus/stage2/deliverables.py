"""Human-facing Stage 2 deliverables, separated from resumable runtime state."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from stage1.deliverables import (
    company_deliverable_dirs,
    resolve_deliverables_root,
    safe_company_folder,
    write_eligibility_report,
)

THEME_FILES = (
    ("technology_json", "Tecnología.json"),
    ("corporate_json", "Corporativo.json"),
    ("expansion_json", "Expansión.json"),
)


def write_company_deliverables(
    record: dict[str, Any],
    root: Path,
) -> dict[str, Path]:
    dirs = company_deliverable_dirs(root, str(record["company_name"]))
    dirs["stage1"].mkdir(parents=True, exist_ok=True)
    dirs["research"].mkdir(parents=True, exist_ok=True)

    eligibility_path = write_eligibility_report(
        root,
        str(record["company_name"]),
        str(record["record_id"]),
        record.get("eligibility_json") or {},
    )

    outputs = {"eligibility": eligibility_path}
    for key, filename in THEME_FILES:
        result = record.get(key)
        if not result:
            continue
        path = dirs["research"] / filename
        path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        outputs[key.removesuffix("_json")] = path
    return outputs


def snapshot_provided_meddicc(
    root: Path,
    company_name: str,
    source_name: str,
    markdown: str,
) -> Path:
    sources = company_deliverable_dirs(root, company_name)["sources"]
    sources.mkdir(parents=True, exist_ok=True)
    path = sources / _safe_filename(source_name)
    path.write_text(markdown, encoding="utf-8")
    return path


def _safe_filename(value: str) -> str:
    name = Path(value).name
    cleaned = re.sub(r"[\x00-\x1f/:\\\\]+", " - ", name).strip(" .")
    return cleaned or "MEDDPICC aportado.md"
