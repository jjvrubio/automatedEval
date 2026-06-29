#!/usr/bin/env bash
# Genera un PDF desde Markdown/Obsidian usando pandoc y xelatex.
# Pasos: (1) convierte SVG a PDF vectorial, (2) traduce embeds de Obsidian
# ![[...svg]] a sintaxis pandoc ![](...pdf) sobre una copia temporal, y
# (3) compila el PDF con plantilla LaTeX y filtro de callouts.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMPLATE_DEFAULT="$SCRIPT_DIR/plantilla-pdf.tex"

usage() {
  cat <<'EOF'
Uso:
  ./build-pdf.sh SRC_MD [OUT_PDF] [IMGDIR] [TEMPLATE_TEX]

Argumentos:
  SRC_MD        Ruta al Markdown de entrada.
  OUT_PDF       Ruta al PDF de salida. Si se omite, usa SRC_MD con extension .pdf.
  IMGDIR        Carpeta con los .svg/.pdf referenciados en el Markdown. Si se omite, usa la carpeta de SRC_MD.
  TEMPLATE_TEX  Plantilla de pandoc/LaTeX. Si se omite, usa plantilla-pdf.tex junto al script.

Requisitos:
  pandoc, xelatex, rsvg-convert, perl
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -lt 1 ]]; then
  usage >&2
  exit 1
fi

SRC="$1"
OUT="${2:-${SRC%.*}.pdf}"
IMGDIR="${3:-$(dirname "$SRC")}"
TEMPLATE="${4:-$TEMPLATE_DEFAULT}"

if [[ ! -f "$SRC" ]]; then
  echo "No existe el Markdown de entrada: $SRC" >&2
  exit 1
fi

if [[ ! -d "$IMGDIR" ]]; then
  echo "No existe la carpeta de imagenes: $IMGDIR" >&2
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

# 1) Convertir SVG -> PDF vectorial (solo si falta el PDF o el SVG es mas nuevo).
for svg in "$IMGDIR"/*.svg; do
  [ -e "$svg" ] || continue
  pdf="${svg%.svg}.pdf"
  if [ ! -f "$pdf" ] || [ "$svg" -nt "$pdf" ]; then
    echo "Convirtiendo $(basename "$svg") -> PDF"
    rsvg-convert -f pdf -o "$pdf" "$svg"
  fi
done

# 2) Traducir embeds de Obsidian ![[ruta/x.svg]] -> ![](IMGDIR/x.pdf)
#    en una copia temporal. Cualquier prefijo de ruta se descarta y se usa el
#    nombre de fichero dentro de IMGDIR con extension .pdf.
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT
TMP_MD="$TMP_DIR/articulo.md"
IMGDIR="$IMGDIR" perl -pe 's{!\[\[(?:[^]\n]*/)?([^]/]+)\.svg\]\]}{"![]($ENV{IMGDIR}/$1.pdf)"}ge' "$SRC" > "$TMP_MD"

# 3) Generar el PDF.
mkdir -p "$(dirname "$OUT")"
RESOURCE_PATH="$SCRIPT_DIR:$(dirname "$SRC"):$IMGDIR"
pandoc "$TMP_MD" -o "$OUT" \
  --template="$TEMPLATE" \
  --lua-filter="$SCRIPT_DIR/callouts.lua" \
  --pdf-engine=xelatex \
  --resource-path="$RESOURCE_PATH"

echo "PDF generado: $OUT"
