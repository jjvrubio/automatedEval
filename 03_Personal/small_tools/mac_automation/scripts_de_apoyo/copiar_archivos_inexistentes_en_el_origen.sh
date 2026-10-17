#!/bin/zsh
set -euo pipefail

# 1. Define tus rutas aquí (usa comillas si tienen espacios)
C1="/Users/juanjo/Library/Mobile Documents/com~apple~CloudDocs/Libros"
C2="/Users/juanjo/Library/Mobile Documents/com~apple~CloudDocs/Libros_duplicados"
DRY_RUN="${1:---dry-run}"

tmp_names="/tmp/nombres_c1.txt"
log_file="$HOME/libros_copiados_por_nombre.txt"

find "$C1" -type f -exec basename {} \; 2>/dev/null | sort -u > "$tmp_names"

{
  find "$C2" -type f 2>/dev/null | while IFS= read -r archivo2; do
    nombre=$(basename "$archivo2")
    if ! grep -qxF "$nombre" "$tmp_names"; then
      if [[ "$DRY_RUN" == "--dry-run" ]]; then
        echo "[dry-run] mv -- '$archivo2' '$C1/'"
      else
        mv -nv -- "$archivo2" "$C1/"
      fi
    fi
  done
} | tee "$log_file"
