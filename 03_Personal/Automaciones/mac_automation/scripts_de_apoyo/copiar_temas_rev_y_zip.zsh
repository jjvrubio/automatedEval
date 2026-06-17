#!/bin/zsh
set -euo pipefail
setopt EXTENDED_GLOB NULL_GLOB

DEFAULT_ROOT="/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/UNIR/Actualización de Contenidos/Ecosistema Digital y Tecnologías Disruptivas/Curso 2026"
OPEN_FINDER=0
ROOT="$DEFAULT_ROOT"

for arg in "$@"; do
  if [[ "$arg" == "--open-finder" || "$arg" == "-o" ]]; then
    OPEN_FINDER=1
  else
    ROOT="$arg"
  fi
done

if [[ ! -d "$ROOT" ]]; then
  echo "Error: no existe la carpeta raíz: $ROOT"
  echo "Uso: $0 [--open-finder|-o] [\"/ruta/a/Curso 2026\"]"
  exit 1
fi

cd "$ROOT"

DEST="$ROOT/TEMAS"
mkdir -p "$DEST"

copied=()
theme_dirs=("$ROOT"/Tema\ <->(Nn/))

if [[ "${#theme_dirs[@]}" -eq 0 ]]; then
  echo "No se encontraron subcarpetas con el patrón: $ROOT/Tema N"
fi

for dir in "${theme_dirs[@]}"; do
  n="${dir:t}"
  n="${n#Tema }"
  file="$dir/tema_${n}_rev.docx"
  dest_file="$DEST/${file:t}"

  if [[ -f "$file" ]]; then
    cp -f "$file" "$dest_file"
    copied+=("$dest_file")
    printf 'Copiado: %s -> %s\n' "$file" "$dest_file"
  else
    printf 'No encontrado: %s\n' "$file"
  fi
done

count=${#copied[@]}
printf 'Copiados: %s\n' "$count"

if [[ "$count" -eq 0 ]]; then
  echo "No se encontraron archivos con el patrón esperado."
  exit 1
fi

echo "---"
echo "Copiados en: $DEST"

if [[ "$OPEN_FINDER" -eq 1 ]]; then
  open "$DEST"
  echo "Finder abierto en: $DEST"
fi
