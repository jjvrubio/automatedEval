#!/usr/bin/env bash
# Genera un PDF desde Markdown/Obsidian usando pandoc y xelatex.
# Integra tabla de contenidos por defecto, conversión SVG -> PDF vectorial,
# traducción de embeds de Obsidian y filtros Lua opcionales.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_DEFAULT="$SCRIPT_DIR/plantilla-pdf.tex"
CALLOUTS_FILTER_DEFAULT="$SCRIPT_DIR/callouts.lua"

TOC=1
TOC_DEPTH=3
TOC_TITLE="Índice"
NUMBER_SECTIONS=0

usage() {
  cat <<'USAGE'
Uso:
  ./build-pdf-toc.sh [opciones] SRC_MD [OUT_PDF] [IMGDIR] [TEMPLATE_TEX]

Argumentos:
  SRC_MD        Ruta al Markdown de entrada.
  OUT_PDF       Ruta al PDF de salida. Si se omite, usa SRC_MD con extensión .pdf.
  IMGDIR        Carpeta con las imágenes referenciadas. Si se omite, usa la carpeta de SRC_MD.
  TEMPLATE_TEX  Plantilla de pandoc/LaTeX. Si se omite, usa plantilla-pdf.tex junto al script.

Opciones:
  --toc                 Activa tabla de contenidos. Es el comportamiento por defecto.
  --no-toc              Desactiva tabla de contenidos para un documento concreto.
  --toc-depth N         Profundidad del índice. Por defecto: 3.
  --toc-title TEXTO     Título del índice. Por defecto: Índice.
  --number-sections     Numera automáticamente las secciones.
  -h, --help            Muestra esta ayuda.

Ejemplos:
  ./build-pdf-toc.sh articulo.md
  ./build-pdf-toc.sh --toc-depth 2 articulo.md export/articulo.pdf assets
  ./build-pdf-toc.sh --no-toc articulo.md

Requisitos:
  pandoc, xelatex, rsvg-convert, perl
USAGE
}

POSITIONAL=()
while [[ $# -gt 0 ]]; do
  case "$1" in
    -h|--help)
      usage
      exit 0
      ;;
    --toc)
      TOC=1
      shift
      ;;
    --no-toc)
      TOC=0
      shift
      ;;
    --toc-depth)
      if [[ $# -lt 2 ]]; then
        echo "Falta valor para --toc-depth" >&2
        exit 1
      fi
      TOC_DEPTH="$2"
      shift 2
      ;;
    --toc-title)
      if [[ $# -lt 2 ]]; then
        echo "Falta valor para --toc-title" >&2
        exit 1
      fi
      TOC_TITLE="$2"
      shift 2
      ;;
    --number-sections)
      NUMBER_SECTIONS=1
      shift
      ;;
    --)
      shift
      POSITIONAL+=("$@")
      break
      ;;
    -*)
      echo "Opción no reconocida: $1" >&2
      usage >&2
      exit 1
      ;;
    *)
      POSITIONAL+=("$1")
      shift
      ;;
  esac
done

set -- "${POSITIONAL[@]}"

if [[ $# -lt 1 ]]; then
  usage >&2
  exit 1
fi

if ! [[ "$TOC_DEPTH" =~ ^[0-9]+$ ]]; then
  echo "--toc-depth debe ser un número entero." >&2
  exit 1
fi

SRC="$1"
OUT="${2:-${SRC%.*}.pdf}"
IMGDIR="${3:-$(dirname "$SRC")}"
TEMPLATE="${4:-$TEMPLATE_DEFAULT}"
CALLOUTS_FILTER="$CALLOUTS_FILTER_DEFAULT"

if [[ ! -f "$SRC" ]]; then
  echo "No existe el Markdown de entrada: $SRC" >&2
  exit 1
fi

if [[ ! -d "$IMGDIR" ]]; then
  echo "No existe la carpeta de imágenes: $IMGDIR" >&2
  exit 1
fi

if [[ ! -f "$TEMPLATE" ]]; then
  echo "No existe la plantilla: $TEMPLATE" >&2
  exit 1
fi

for binary in pandoc xelatex rsvg-convert perl; do
  if ! command -v "$binary" >/dev/null 2>&1; then
    echo "Falta dependencia requerida: $binary" >&2
    exit 1
  fi
done

# 1) Convertir SVG -> PDF vectorial, solo si falta el PDF o el SVG es más nuevo.
for svg in "$IMGDIR"/*.svg; do
  [ -e "$svg" ] || continue
  pdf="${svg%.svg}.pdf"
  if [ ! -f "$pdf" ] || [ "$svg" -nt "$pdf" ]; then
    echo "Convirtiendo $(basename "$svg") -> PDF"
    rsvg-convert -f pdf -o "$pdf" "$svg"
  fi
done

# 2) Traducir embeds de Obsidian en una copia temporal.
#    SVG:  ![[ruta/figura.svg]]      -> ![](<IMGDIR/figura.pdf>)
#    Raster/PDF: ![[ruta/figura.png]] -> ![](<IMGDIR/figura.png>)
#    También tolera alias/tamaño: ![[figura.svg|500]]
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
TMP_MD="$TMP_DIR/articulo.md"
IMGDIR="$IMGDIR" perl -pe '
  s{!\[\[(?:[^\]\n]*/)?([^\]/\|]+)\.svg(?:\|[^\]]*)?\]\]}{"![](<$ENV{IMGDIR}/$1.pdf>)"}ge;
  s{!\[\[(?:[^\]\n]*/)?([^\]/\|]+\.(?:png|jpe?g|webp|gif|pdf))(?:\|[^\]]*)?\]\]}{"![](<$ENV{IMGDIR}/$1>)"}gie;
' "$SRC" > "$TMP_MD"

# 3) Construir argumentos de Pandoc.
mkdir -p "$(dirname "$OUT")"
RESOURCE_PATH="$SCRIPT_DIR:$(dirname "$SRC"):$IMGDIR"

PANDOC_ARGS=(
  "$TMP_MD"
  -o "$OUT"
  --template="$TEMPLATE"
  --pdf-engine=xelatex
  --resource-path="$RESOURCE_PATH"
)

if [[ -f "$CALLOUTS_FILTER" ]]; then
  PANDOC_ARGS+=(--lua-filter="$CALLOUTS_FILTER")
fi

if [[ "$TOC" -eq 1 ]]; then
  PANDOC_ARGS+=(--toc --toc-depth="$TOC_DEPTH" -V "toc-title=$TOC_TITLE")
fi

if [[ "$NUMBER_SECTIONS" -eq 1 ]]; then
  PANDOC_ARGS+=(--number-sections)
fi

pandoc "${PANDOC_ARGS[@]}"

echo "PDF generado: $OUT"
