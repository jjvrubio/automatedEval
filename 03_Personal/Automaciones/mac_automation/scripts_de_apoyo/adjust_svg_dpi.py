#!/usr/bin/env python3
"""
Reajusta el tamaño lógico de SVG exportados a un DPI dado para que mantengan
su dimensión física al importarlos en herramientas que asumen otro DPI.
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


LENGTH_RE = re.compile(r"^\s*([+-]?(?:\d+(?:\.\d*)?|\.\d+))\s*([A-Za-z%]*)\s*$")
ET.register_namespace("", "http://www.w3.org/2000/svg")


@dataclass(frozen=True)
class Length:
    value: float
    unit: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Ajusta width/height de SVG exportados a 300 dpi para que mantengan "
            "su tamaño físico cuando el destino asume 96 dpi."
        )
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        help="Archivos SVG o carpetas que contengan SVG.",
    )
    parser.add_argument(
        "--source-dpi",
        type=float,
        default=300.0,
        help="DPI asumido en el SVG de origen. Por defecto: 300.",
    )
    parser.add_argument(
        "--target-dpi",
        type=float,
        default=96.0,
        help="DPI que asumirá la herramienta de destino. Por defecto: 96.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Busca SVG dentro de carpetas de forma recursiva.",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Sobrescribe los archivos originales en lugar de crear copias.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Carpeta de salida para las copias ajustadas.",
    )
    return parser.parse_args()


def collect_svg_paths(inputs: list[str], recursive: bool) -> list[Path]:
    collected: list[Path] = []

    for raw_input in inputs:
        path = Path(raw_input).expanduser()
        if not path.exists():
            print(f"Aviso: no existe {path}", file=sys.stderr)
            continue

        if path.is_file() and path.suffix.lower() == ".svg":
            collected.append(path)
            continue

        if path.is_dir():
            pattern = "**/*.svg" if recursive else "*.svg"
            collected.extend(sorted(child for child in path.glob(pattern) if child.is_file()))
            continue

        print(f"Aviso: se omite {path} porque no es un SVG ni una carpeta.", file=sys.stderr)

    unique_paths = sorted(dict.fromkeys(collected))
    return unique_paths


def parse_length(raw_value: str | None) -> Length | None:
    if raw_value is None:
        return None

    match = LENGTH_RE.match(raw_value)
    if not match:
        return None

    return Length(value=float(match.group(1)), unit=match.group(2))


def format_length(length: Length) -> str:
    value = round(length.value, 6)
    if value.is_integer():
        value_str = str(int(value))
    else:
        value_str = f"{value:.6f}".rstrip("0").rstrip(".")
    return f"{value_str}{length.unit}"


def adjust_dimension(raw_value: str | None, scale_factor: float) -> str | None:
    parsed = parse_length(raw_value)
    if parsed is None:
        return None

    if parsed.unit not in {"", "px"}:
        return raw_value

    adjusted = Length(value=parsed.value * scale_factor, unit=parsed.unit)
    return format_length(adjusted)


def build_output_path(input_path: Path, output_dir: Path | None, in_place: bool, target_dpi: float) -> Path:
    if in_place:
        return input_path

    suffix = f"-{int(target_dpi) if float(target_dpi).is_integer() else str(target_dpi).replace('.', '_')}dpi"
    filename = f"{input_path.stem}{suffix}{input_path.suffix}"
    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir / filename
    return input_path.with_name(filename)


def adjust_svg_file(input_path: Path, output_path: Path, source_dpi: float, target_dpi: float) -> tuple[bool, str]:
    tree = ET.parse(input_path)
    root = tree.getroot()

    scale_factor = target_dpi / source_dpi
    original_width = root.get("width")
    original_height = root.get("height")
    adjusted_width = adjust_dimension(original_width, scale_factor)
    adjusted_height = adjust_dimension(original_height, scale_factor)

    if adjusted_width is None or adjusted_height is None:
        return False, "sin width/height ajustables"

    root.set("width", adjusted_width)
    root.set("height", adjusted_height)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    return True, f"{original_width} x {original_height} -> {adjusted_width} x {adjusted_height}"


def main() -> int:
    args = parse_args()

    if args.source_dpi <= 0 or args.target_dpi <= 0:
        print("Error: source-dpi y target-dpi deben ser mayores que cero.", file=sys.stderr)
        return 1

    svg_paths = collect_svg_paths(args.inputs, args.recursive)
    if not svg_paths:
        print("No se encontraron SVG para procesar.", file=sys.stderr)
        return 1

    processed = 0
    skipped = 0

    for svg_path in svg_paths:
        output_path = build_output_path(svg_path, args.output_dir, args.in_place, args.target_dpi)
        try:
            changed, detail = adjust_svg_file(svg_path, output_path, args.source_dpi, args.target_dpi)
        except ET.ParseError as exc:
            skipped += 1
            print(f"Omitido {svg_path}: XML no válido ({exc})", file=sys.stderr)
            continue
        except OSError as exc:
            skipped += 1
            print(f"Omitido {svg_path}: {exc}", file=sys.stderr)
            continue

        if changed:
            processed += 1
            print(f"OK  {svg_path} -> {output_path} | {detail}")
        else:
            skipped += 1
            print(f"SKIP {svg_path} | {detail}")

    print(f"\nProcesados: {processed} | Omitidos: {skipped}")
    return 0 if processed else 1


if __name__ == "__main__":
    raise SystemExit(main())