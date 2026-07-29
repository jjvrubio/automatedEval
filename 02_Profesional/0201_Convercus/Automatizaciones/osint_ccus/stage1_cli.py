#!/usr/bin/env python3
"""CLI and native macOS entry point for OSINT Stage 1."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

from stage1.csv_input import CsvValidationError, read_csv, selected_rows
from stage1.deliverables import resolve_deliverables_root
from stage1.gui import choose_csv, confirm_run
from stage1.research import OpenAIWebResearcher, ResearchError
from stage1.runner import run_stage1a, run_stage1b


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Etapa 1: valida empleados, puntos de venta/servicio y facturación."
        )
    )
    parser.add_argument(
        "--stage",
        choices=["1a", "1b", "all"],
        default="1a",
        help="Puerta a ejecutar. Por defecto: 1a.",
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="CSV de entrada. Si se omite, se abre el selector nativo de macOS.",
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument(
        "--accounts-output-root",
        type=Path,
        help=(
            "Raíz alternativa para documentos por empresa. Si se omite, se "
            "utiliza la carpeta que contiene el CSV."
        ),
    )
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument(
        "--approve-stage1a-review",
        action="store_true",
        help=(
            "Autoriza una única fila REVIEW_REQUIRED a entrar en 1B y registra "
            "la intervención humana en la auditoría."
        ),
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--model", default="gpt-5.6-terra")
    parser.add_argument(
        "--search-context-size",
        choices=["low", "medium", "high"],
        default="high",
    )
    return parser.parse_args()


def safe_stem(value: str) -> str:
    normalized = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._")
    return normalized or "companies"


def default_output_dir(input_path: Path) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return (
        Path(__file__).resolve().parent
        / ".runtime"
        / "runs"
        / f"{timestamp}_{safe_stem(input_path.stem)}"
    )


def load_project_env(path: Path) -> None:
    """Load .env without making python-dotenv a startup requirement."""
    try:
        from dotenv import load_dotenv
    except ImportError:
        if not path.exists():
            return
        for line in path.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            key = key.strip()
            value = value.strip().strip("\"'")
            if key:
                os.environ.setdefault(key, value)
        return
    load_dotenv(path)


def main() -> int:
    args = parse_args()
    load_project_env(Path(__file__).with_name(".env"))
    input_path = args.input
    selected_with_gui = input_path is None
    if input_path is None:
        input_path = choose_csv()
        if input_path is None:
            print("No se seleccionó ningún CSV.", file=sys.stderr)
            return 1

    try:
        headers, all_rows = read_csv(input_path)
    except CsvValidationError as exc:
        print(f"CSV no válido: {exc}", file=sys.stderr)
        return 2

    rows = selected_rows(all_rows, start=args.start, limit=args.limit)
    if args.approve_stage1a_review and len(rows) != 1:
        print(
            "--approve-stage1a-review exige seleccionar exactamente una fila.",
            file=sys.stderr,
        )
        return 2
    if args.stage == "1b" and args.output_dir is None:
        print(
            "La Etapa 1B exige --output-dir para reutilizar un estado 1A existente.",
            file=sys.stderr,
        )
        return 2
    output_dir = args.output_dir or default_output_dir(input_path)
    documents_root = resolve_deliverables_root(
        input_path, args.accounts_output_root
    )

    print(f"CSV: {input_path}")
    print(f"Filas válidas: {len(all_rows)}")
    print(f"Filas seleccionadas: {len(rows)}")
    print(f"Estado técnico y exportaciones CSV: {output_dir}")
    print(f"Documentos por empresa: {documents_root}")

    manifest = {
        "input": str(input_path.resolve()),
        "output_dir": str(output_dir.resolve()),
        "accounts_output_root": str(documents_root),
        "total_rows": len(all_rows),
        "selected_rows": len(rows),
        "start": args.start,
        "limit": args.limit,
        "model": args.model,
        "stage": args.stage,
        "approve_stage1a_review": args.approve_stage1a_review,
    }

    if args.dry_run:
        print(json.dumps(manifest, indent=2, ensure_ascii=False))
        for row in rows[:25]:
            print(f"- fila {row.source_row}: {row.company_name}")
        return 0

    calls_per_row = {"1a": 2, "1b": 1, "all": 3}[args.stage]
    if selected_with_gui and not confirm_run(
        company_count=len(rows),
        estimated_api_calls=len(rows) * calls_per_row,
        stage=args.stage,
    ):
        print("Ejecución cancelada.")
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_name = "stage1b_manifest.json" if args.stage == "1b" else "run_manifest.json"
    (output_dir / manifest_name).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    try:
        researcher = OpenAIWebResearcher(
            model=args.model,
            search_context_size=args.search_context_size,
        )
    except ResearchError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    try:
        if args.stage in {"1a", "all"}:
            outputs = run_stage1a(
                rows=rows,
                original_headers=headers,
                output_dir=output_dir,
                researcher=researcher,
                force=args.force,
                retry_errors=args.retry_errors,
                deliverables_root=documents_root,
            )
        if args.stage in {"1b", "all"}:
            outputs = run_stage1b(
                rows=rows,
                original_headers=headers,
                output_dir=output_dir,
                researcher=researcher,
                force=args.force,
                retry_errors=args.retry_errors,
                approve_review=args.approve_stage1a_review,
                deliverables_root=documents_root,
            )
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 4

    print(f"\nEtapa {args.stage.upper()} finalizada:")
    for name, path in outputs.items():
        print(f"- {name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
