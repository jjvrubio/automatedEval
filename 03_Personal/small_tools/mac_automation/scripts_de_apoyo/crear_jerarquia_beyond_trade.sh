#!/usr/bin/env bash
set -euo pipefail

DEFAULT_BASE_DIR="$HOME/Library/CloudStorage/OneDrive-ConvercusGmbH/Convercus/GTM & Events/Events/Seminario - Beyond Trade"
BASE_DIR="${BEYOND_TRADE_BASE_DIR:-$DEFAULT_BASE_DIR}"

usage() {
  cat <<'EOF'
Uso:
  crear_jerarquia_beyond_trade.sh [ruta_base]

Opciones de configuracion:
  ruta_base               Sobrescribe la ruta destino para esta ejecucion.
  BEYOND_TRADE_BASE_DIR   Variable de entorno con la ruta destino por defecto.

Si no se indica nada, se usa una ruta por defecto en OneDrive del usuario actual.
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if [[ $# -gt 1 ]]; then
  echo "Error: demasiados argumentos." >&2
  usage
  exit 1
fi

if [[ $# -eq 1 ]]; then
  BASE_DIR="$1"
fi

mkdir -p \
  "$BASE_DIR/00_fuentes_evento" \
  "$BASE_DIR/01_publicacion/borradores" \
  "$BASE_DIR/01_publicacion/versiones" \
  "$BASE_DIR/01_publicacion/final" \
  "$BASE_DIR/02_activos_visuales/mapa_visual" \
  "$BASE_DIR/02_activos_visuales/instrucciones" \
  "$BASE_DIR/02_activos_visuales/generados" \
  "$BASE_DIR/02_activos_visuales/finales" \
  "$BASE_DIR/03_herramientas_operativas/tickets_bloom" \
  "$BASE_DIR/03_herramientas_operativas/matriz_dikw_bloom_jacquard" \
  "$BASE_DIR/04_registro_validacion/evidencias_recepcion" \
  "$BASE_DIR/04_registro_validacion/validacion_piloto" \
  "$BASE_DIR/04_registro_validacion/aprendizaje"

touch \
  "$BASE_DIR/00_fuentes_evento/Agenda y convocatoria v2.md" \
  "$BASE_DIR/00_fuentes_evento/Beyond Trade Minima.pptx" \
  "$BASE_DIR/00_fuentes_evento/Ecosistemas de Valor B2B2C.md" \
  "$BASE_DIR/03_herramientas_operativas/TES_Loom_Charter_Piloto_Beyond_Trade_v0_1.md"

echo "Jerarquia creada en:"
echo "$BASE_DIR"
