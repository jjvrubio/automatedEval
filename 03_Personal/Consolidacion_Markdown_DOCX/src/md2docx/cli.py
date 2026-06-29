from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .config import list_profiles
from .pipeline import BuildOptions, run_build


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="md2docx",
        description="Convierte Markdown a DOCX usando perfiles Pandoc.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("profiles", help="Lista los perfiles disponibles")

    build = subparsers.add_parser("build", help="Compila un markdown a docx")
    build.add_argument(
        "--input",
        required=True,
        nargs="+",
        help="Ruta de uno o varios archivos markdown, en orden",
    )
    build.add_argument("--output", required=False, help="Ruta del archivo docx de salida")
    build.add_argument("--profile", required=True, help="Nombre del perfil YAML en configs/profiles")
    build.add_argument("--metadata", required=False, help="YAML de metadatos opcional")
    build.add_argument("--reference-doc", required=False, help="Plantilla DOCX opcional")
    build.add_argument(
        "--style-template",
        required=False,
        help="Plantilla DOCX para post-procesado de estilos (extension futura)",
    )

    return parser


def _default_output_for(md_path: Path) -> Path:
    return md_path.with_suffix(".docx")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    project_root = Path(__file__).resolve().parents[2]

    if args.command == "profiles":
        for profile_name in list_profiles(project_root):
            print(profile_name)
        return 0

    if args.command == "build":
        input_files = [Path(value).expanduser().resolve() for value in args.input]
        output_docx = (
            Path(args.output).expanduser().resolve()
            if args.output
            else _default_output_for(input_files[0])
        )

        opts = BuildOptions(
            input_md=input_files,
            output_docx=output_docx,
            profile_name=args.profile,
            metadata_file=Path(args.metadata).expanduser().resolve() if args.metadata else None,
            reference_doc=Path(args.reference_doc).expanduser().resolve() if args.reference_doc else None,
            style_template=Path(args.style_template).expanduser().resolve() if args.style_template else None,
        )

        try:
            run_build(project_root=project_root, opts=opts)
        except Exception as exc:  # pragma: no cover
            print(f"Error: {exc}", file=sys.stderr)
            return 1

        print(f"OK: generado {output_docx}")
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
