#!/usr/bin/env python3
"""CLI for evidence-based potentiality research."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from stage1.csv_input import CsvValidationError, read_csv, selected_rows
from stage1.research import ResearchError
from stage1_cli import load_project_env
from stage2.research import Stage2WebResearcher
from stage2.runner import eligible_rows, run_stage2
from stage2.deliverables import resolve_deliverables_root


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Etapa 2: investigación exhaustiva de potencialidad."
    )
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--stage1-output-dir", type=Path, required=True)
    parser.add_argument(
        "--accounts-output-root",
        type=Path,
        help=(
            "Raíz alternativa de entregables por empresa. Si se omite, se "
            "utiliza la carpeta que contiene el CSV."
        ),
    )
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument(
        "--meddicc-file",
        type=Path,
        help=(
            "MEDDICC/MEDDPICC Markdown aportado para la única compañía "
            "seleccionada. Es la única fuente MEDDICC usada por el sistema."
        ),
    )
    parser.add_argument(
        "--use-meddicc-as-context",
        action="store_true",
        help=(
            "Envía el contenido del --meddicc-file como contexto a los "
            "investigadores pendientes de Etapa 2."
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


def main() -> int:
    args = parse_args()
    load_project_env(Path(__file__).with_name(".env"))
    accounts_output_root = resolve_deliverables_root(
        args.input, args.accounts_output_root
    )
    try:
        headers, all_rows = read_csv(args.input)
        del headers
        rows = selected_rows(all_rows, start=args.start, limit=args.limit)
        candidates = eligible_rows(rows, args.stage1_output_dir)
    except (CsvValidationError, FileNotFoundError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    provided_meddicc = None
    if args.use_meddicc_as_context and not args.meddicc_file:
        print(
            "--use-meddicc-as-context exige --meddicc-file.",
            file=sys.stderr,
        )
        return 2
    if args.meddicc_file:
        if len(candidates) != 1:
            print(
                "--meddicc-file exige seleccionar exactamente una compañía "
                "ELIGIBLE.",
                file=sys.stderr,
            )
            return 2
        if (
            not args.meddicc_file.exists()
            or args.meddicc_file.suffix.casefold() not in {".md", ".markdown"}
        ):
            print(
                "El MEDDICC/MEDDPICC debe ser un archivo Markdown existente.",
                file=sys.stderr,
            )
            return 2
        if args.meddicc_file.stat().st_size > 1_000_000:
            print(
                "El MEDDICC/MEDDPICC supera el límite de 1 MB.",
                file=sys.stderr,
            )
            return 2
        markdown = args.meddicc_file.read_text(encoding="utf-8")
        provided_meddicc = {
            "source_path": str(args.meddicc_file.resolve()),
            "sha256": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
            "markdown": markdown,
        }

    manifest = {
        "input": str(args.input.resolve()),
        "stage1_output_dir": str(args.stage1_output_dir.resolve()),
        "accounts_output_root": str(accounts_output_root),
        "selected_rows": len(rows),
        "eligible_rows": len(candidates),
        "model": args.model,
        "maximum_specialist_calls_per_company": 3,
        "provided_meddicc": (
            {
                "source": provided_meddicc["source_path"],
                "sha256": provided_meddicc["sha256"],
            }
            if provided_meddicc
            else None
        ),
        "use_meddicc_as_context": args.use_meddicc_as_context,
    }
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    for row, _ in candidates:
        print(f"- ELIGIBLE: {row.company_name}")
    if provided_meddicc and args.use_meddicc_as_context:
        print(
            "AVISO: el contenido del MEDDICC/MEDDPICC se enviará a la API "
            "como contexto para los investigadores de Etapa 2 pendientes."
        )
    if args.dry_run:
        return 0
    if not candidates:
        print("No hay compañías ELIGIBLE seleccionadas.", file=sys.stderr)
        return 2

    (args.stage1_output_dir / "stage2_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    try:
        researcher = Stage2WebResearcher(
            model=args.model,
            search_context_size=args.search_context_size,
        )
    except ResearchError as exc:
        print(str(exc), file=sys.stderr)
        return 3

    outputs = run_stage2(
        candidates,
        args.stage1_output_dir,
        researcher,
        force=args.force,
        retry_errors=args.retry_errors,
        provided_meddicc=provided_meddicc,
        use_provided_meddicc_as_context=args.use_meddicc_as_context,
        deliverables_root=accounts_output_root,
    )
    print("\nEtapa 2 finalizada:")
    for name, path in outputs.items():
        print(f"- {name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
