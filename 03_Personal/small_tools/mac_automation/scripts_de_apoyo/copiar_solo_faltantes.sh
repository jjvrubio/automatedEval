#!/usr/bin/env bash
set -euo pipefail

# Copia desde ORIGEN hacia DESTINO solo archivos que no existan en DESTINO.
# Uso:
#   ./copiar_solo_faltantes.sh /ruta/origen /ruta/destino

if [[ $# -ne 2 ]]; then
  echo "Uso: $0 ORIGEN DESTINO"
  exit 1
fi

ORIGEN="$1"
DESTINO="$2"

if [[ ! -d "$ORIGEN" ]]; then
  echo "Error: ORIGEN no existe o no es directorio: $ORIGEN"
  exit 1
fi

mkdir -p "$DESTINO"

# --ignore-existing: no sobrescribe archivos ya presentes en DESTINO.
# --prune-empty-dirs: evita crear arbol vacio por exclusiones.
rsync -av --ignore-existing --prune-empty-dirs \
  --exclude ".DS_Store" \
  "$ORIGEN"/ "$DESTINO"/

echo "Copia completada."
