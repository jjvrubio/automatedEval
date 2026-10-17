#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(pwd)"
MAP_FILE="repo_restructure_map.tsv"
APPLY=false

usage() {
  cat <<'EOF'
Uso:
  bash "03_Personal/Automatizaciones/mac_automation/scripts_de_apoyo/reestructurar_repo.sh" [opciones]

Opciones:
  --root <ruta>      Root del repositorio (default: directorio actual)
  --map <archivo>    Archivo TSV con origen y destino (default: repo_restructure_map.tsv)
  --apply            Ejecuta los movimientos (por defecto solo simula)
  -h, --help         Muestra esta ayuda

Formato del mapa (TSV):
  origen<TAB>destino

Ejemplo:
  automatedEval<TAB>01_Educativa/0101_UNIR/AutomatedEval
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --root)
      ROOT_DIR="$2"
      shift 2
      ;;
    --map)
      MAP_FILE="$2"
      shift 2
      ;;
    --apply)
      APPLY=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Opcion no reconocida: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ ! -d "$ROOT_DIR" ]]; then
  echo "Root no existe: $ROOT_DIR" >&2
  exit 1
fi

MAP_PATH="$ROOT_DIR/$MAP_FILE"
if [[ ! -f "$MAP_PATH" ]]; then
  echo "Mapa no encontrado: $MAP_PATH" >&2
  exit 1
fi

move_count=0
skip_count=0
error_count=0

echo "Root: $ROOT_DIR"
echo "Mapa: $MAP_PATH"
if [[ "$APPLY" == true ]]; then
  echo "Modo: APPLY (se ejecutaran movimientos)"
else
  echo "Modo: DRY-RUN (solo simulacion)"
fi

echo
while IFS=$'\t' read -r src_rel dst_rel extra; do
  # Ignora comentarios y lineas vacias
  [[ -z "${src_rel// }" ]] && continue
  [[ "${src_rel:0:1}" == "#" ]] && continue

  if [[ -n "${extra:-}" ]]; then
    echo "[ERROR] Linea invalida (demasiadas columnas): $src_rel"
    ((error_count+=1))
    continue
  fi

  src_abs="$ROOT_DIR/$src_rel"
  dst_abs="$ROOT_DIR/$dst_rel"

  if [[ ! -e "$src_abs" ]]; then
    echo "[SKIP] No existe origen: $src_rel"
    ((skip_count+=1))
    continue
  fi

  if [[ -e "$dst_abs" ]]; then
    echo "[SKIP] Destino ya existe: $dst_rel"
    ((skip_count+=1))
    continue
  fi

  dst_parent="$(dirname "$dst_abs")"

  if [[ "$APPLY" == true ]]; then
    mkdir -p "$dst_parent"
    mv "$src_abs" "$dst_abs"
    echo "[MOVE] $src_rel -> $dst_rel"
  else
    echo "[PLAN] mkdir -p \"$dst_parent\""
    echo "[PLAN] mv \"$src_abs\" \"$dst_abs\""
  fi

  ((move_count+=1))
done < "$MAP_PATH"

echo
echo "Resumen:"
echo "  Movimientos planificados/ejecutados: $move_count"
echo "  Omitidos: $skip_count"
echo "  Errores: $error_count"

if [[ "$APPLY" == false ]]; then
  echo
  echo "Para aplicar cambios reales:"
  echo "  bash \"03_Personal/Automatizaciones/mac_automation/scripts_de_apoyo/reestructurar_repo.sh\" --root \"$ROOT_DIR\" --map \"$MAP_FILE\" --apply"
fi
