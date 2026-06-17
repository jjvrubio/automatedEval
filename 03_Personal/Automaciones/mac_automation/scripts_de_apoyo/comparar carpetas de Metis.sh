#!/usr/bin/env zsh
# SECUNDARIA -> PIVOTE: lista archivos que faltan en PIVOTE o difieren en contenido.
# Modos:
#   mt   -> rápido (tamaño + mtime)
#   hash -> preciso (checksum de contenido con rsync -c)
#
# Uso:
#   diff_pivote_secundaria.zsh [-m mt|hash] [-i "glob1 glob2"] [-x "glob1 glob2"] [-o salida.(csv|json) | -f csv|json] PIVOTE SECUNDARIA
#
# Ejemplos:
#   diff_pivote_secundaria.zsh -m mt   ~/principal ~/sec
#   diff_pivote_secundaria.zsh -m hash -x ".git node_modules .DS_Store" ~/principal ~/sec
#   diff_pivote_secundaria.zsh -m hash -i "*.pdf *.docx" -o resultado.json ~/principal ~/sec
#   diff_pivote_secundaria.zsh -m hash -o resultado.csv ~/principal ~/sec

set -euo pipefail

autoload -Uz colors && colors
ok="$fg[green]"; warn="$fg[yellow]"; err="$fg[red]"; info="$fg[cyan]"; reset="$reset_color"

mode="hash"
includes=()
excludes=(.DS_Store)
out_file=""
out_fmt=""

# default output file when -o is not provided
default_out_file="/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/The Octavius/comparacion_metis.json"

usage() {
  cat <<EOF
Uso: ${0:t} [-m mt|hash] [-i "glob1 glob2"] [-x "glob1 glob2"] [-o RUTA_SALIDA] [-f csv|json] PIVOTE SECUNDARIA

Opciones:
  -m  Modo de comparación (defecto: hash)
        mt    -> tamaño + mtime
        hash  -> checksum contenido
  -i  Patrones a INCLUIR (globs, separados por espacios)
  -x  Patrones a EXCLUIR (globs, separados por espacios; por defecto: .DS_Store)
  -o  Fichero de salida (si no se indica, solo imprime por pantalla)
  -f  Formato de salida si usas -o (csv|json). Si no lo indicas, se infiere por extensión (.csv|.json).
  -R  Permuta los roles: trata el primer argumento como SECUNDARIA y el segundo como PIVOTE (útil cuando los archivos más recientes están en la secundaria)
  -G  Interfaz gráfica: abre un selector de carpetas (macOS) para elegir PIVOTE y SECUNDARIA y omite los argumentos posicionales.
  -h  Ayuda
EOF
}

swap_roles=0
gui=0
while getopts "m:i:x:o:f:hRG" opt; do
  case "$opt" in
    m) mode="$OPTARG" ;;
    i) IFS=' ' read -rA includes <<< "$OPTARG" ;;
    x) IFS=' ' read -rA xs <<< "$OPTARG"; excludes+=("${xs[@]}") ;;
    o) out_file="$OPTARG" ;;
    f) out_fmt="$OPTARG" ;;
  R) swap_roles=1 ;;
  G) gui=1 ;;
    h) usage; exit 0 ;;
    *) usage; exit 1 ;;
  esac
done
shift $((OPTIND-1))

if (( gui == 1 )); then
  # Pedir selección de carpetas mediante selector nativo de macOS
  if ! command -v osascript >/dev/null 2>&1; then
    print -P "${err}Error:${reset} no se encontró 'osascript' para la interfaz gráfica. Asegúrate de estar en macOS."
    exit 5
  fi
  pivot=$(osascript -e 'POSIX path of (choose folder with prompt "Selecciona la carpeta PIVOTE")' 2>/dev/null || true)
  sec=$(osascript -e 'POSIX path of (choose folder with prompt "Selecciona la carpeta SECUNDARIA")' 2>/dev/null || true)
  # eliminar slash final
  pivot=${pivot%/}
  sec=${sec%/}
  if [[ -z "$pivot" || -z "$sec" ]]; then
    print -P "${err}Error:${reset} selección cancelada o inválida."; exit 1
  fi
  print -P "${info}Info:${reset} rutas elegidas: PIVOTE='$pivot' SECUNDARIA='$sec'"
elif (( $# == 0 )); then
  # No se pasaron rutas: usar las rutas por defecto solicitadas
  pivot='/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/The Octavius/METIS™ Framework'
  sec='/Users/juanjo/Library/Mobile Documents/iCloud~md~obsidian/Documents/METIS'
  print -P "${info}Info:${reset} No se proporcionaron rutas; usando rutas por defecto para PIVOTE y SECUNDARIA." 
elif (( $# == 2 )); then
  pivot="${1:A}"
  sec="${2:A}"
else
  print -P "${err}Error:${reset} debes indicar ambas rutas PIVOTE y SECUNDARIA, o ninguna para usar las rutas por defecto.\n"; usage; exit 1
fi

# Si se solicitó permutar los roles, intercambiarlos aquí
if (( swap_roles == 1 )); then
  tmp="$pivot"
  pivot="$sec"
  sec="$tmp"
  print -P "${info}Info:${reset} roles permutados: ahora PIVOTE='$pivot', SECUNDARIA='$sec'"
fi

for d in "$pivot" "$sec"; do
  if [[ ! -d "$d" ]]; then
    print -P "${err}Error:${reset} '$d' no es una carpeta existente."
    exit 2
  fi
done

if ! command -v rsync >/dev/null 2>&1; then
  print -P "${err}Error:${reset} 'rsync' no está disponible."
  exit 3
fi

# Deducción de formato según extensión si no se pasó -f
if [[ -n "$out_file" && -z "$out_fmt" ]]; then
  case "${out_file:l}" in
    *.json) out_fmt="json" ;;
    *.csv)  out_fmt="csv" ;;
    *) print -P "${warn}Aviso:${reset} no se puede inferir formato de '${out_file}'. Usa -f csv|json."; exit 4 ;;
  esac
fi
# If no out_file provided, use default JSON file
if [[ -z "$out_file" ]]; then
  out_file="$default_out_file"
  out_fmt="json"
  print -P "${info}Info:${reset} No se proporcionó -o; escribiré el resultado en: $out_file (formato json)"
fi
if [[ -n "$out_fmt" && "$out_fmt" != "json" && "$out_fmt" != "csv" ]]; then
  print -P "${err}Error:${reset} formato '-f $out_fmt' no soportado. Usa csv|json."
  exit 4
fi

make_rsync_filters() {
  local -a args
  if (( ${#includes[@]} > 0 )); then
    for inc in "${includes[@]}"; do
      args+=(--include="$inc")
    done
    args+=(--include='*/' --exclude='*')
  fi
  if (( ${#excludes[@]} > 0  )); then
    for ex in "${excludes[@]}"; do
      args+=(--exclude="$ex")
    done
  fi
  echo "${(q)args[@]}"
}

rsync_base=(-rtiln --out-format='%i %n')
if [[ "$mode" == "hash" ]]; then
  rsync_base=(-rtiln -c --out-format='%i %n')
elif [[ "$mode" != "mt" ]]; then
  print -P "${warn}Aviso:${reset} modo desconocido '$mode', usando 'hash'."
  rsync_base=(-rtiln -c --out-format='%i %n')
fi

filters=($(make_rsync_filters))

print -P "${info}Pivote:${reset} $pivot"
print -P "${info}Secundaria:${reset} $sec"
print -P "${info}Modo:${reset} $mode"
(( ${#includes[@]} )) && print -P "${info}Incluye:${reset} ${includes[*]}"
(( ${#excludes[@]} )) && print -P "${info}Excluye:${reset} ${excludes[*]}"
[[ -n "$out_file" ]] && print -P "${info}Exportará:${reset} $out_file (${out_fmt:-detecta por extensión})"
print ""

# Ejecutar rsync desde SEC -> PIVOTE
out=()
while IFS= read -r line; do out+=("$line"); done < <(
  rsync "${rsync_base[@]}" ${filters[@]:-} -- "$sec/" "$pivot/"
)

typeset -a nuevos diferentes
for entry in "${out[@]}"; do
  [[ "$entry" == \>*\ * ]] || continue
  path="${entry#* }"
  piv_path="$pivot/$path"
  if [[ ! -e "$piv_path" ]]; then
    nuevos+=("$path")
  else
    diferentes+=("$path")
  fi
done

# --- Exportadores ---
json_escape() {
  # Escapa \, ", y control chars básicos para JSON
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\t'/\\t}"
  echo "$s"
}

stat_info() {
  # devuelve JSON con size y mtime para la ruta dada (POSIX path)
  local p="$1"
  if [[ ! -e "$p" ]]; then
    printf 'null'
    return
  fi
  # Usar stat de BSD (macOS)
  local size mtime
  size=$(stat -f "%z" -- "$p" 2>/dev/null || stat -c "%s" -- "$p" 2>/dev/null || echo 0)
  mtime=$(stat -f "%m" -- "$p" 2>/dev/null || stat -c "%Y" -- "$p" 2>/dev/null || echo 0)
  printf '{"size": %s, "mtime": %s}' "$size" "$mtime"
}

emit_json() {
  # Construcción segura del JSON: trabajamos con copias de los arrays
  print '{'
  print '  "nuevos": ['
  local -a _nuevos=("${nuevos[@]:-}")
  local ncount=${#_nuevos[@]}
  local i v sec_path piv_path
  for ((i=0;i<ncount;i++)); do
    v="${_nuevos[i]:-}"
    sec_path="$sec/$v"
    printf '    {"path": "%s", "sec": %s}%s\n' "$(json_escape "$v")" "$(stat_info "$sec_path")" $([[ $i -lt $((ncount-1)) ]] && echo ',' )
  done
  print '  ],'
  print '  "diferentes": ['
  local -a _diferentes=("${diferentes[@]:-}")
  local dcount=${#_diferentes[@]}
  for ((i=0;i<dcount;i++)); do
    v="${_diferentes[i]:-}"
    sec_path="$sec/$v"
    piv_path="$pivot/$v"
    printf '    {"path": "%s", "sec": %s, "piv": %s}%s\n' "$(json_escape "$v")" "$(stat_info "$sec_path")" "$(stat_info "$piv_path")" $([[ $i -lt $((dcount-1)) ]] && echo ',' )
  done
  print '  ]'
  print '}'
}

emit_csv() {
  print "status,path"
  for v in "${nuevos[@]}"; do
    # CSV sencillo: si hay comas o comillas, entrecomillar y duplicar comillas
    local p="$v"
    if [[ "$p" == *','* || "$p" == *'"'* ]]; then
      p="${p//\"/\"\"}"
      print "nuevo,\"$p\""
    else
      print "nuevo,$p"
    fi
  done
  for v in "${diferentes[@]}"; do
    local p="$v"
    if [[ "$p" == *','* || "$p" == *'"'* ]]; then
      p="${p//\"/\"\"}"
      print "diferente,\"$p\""
    else
      print "diferente,$p"
    fi
  done
}

# --- Salida por pantalla (humana) ---
if (( ${#nuevos[@]} == 0 && ${#diferentes[@]} == 0 )); then
  print -P "${ok}Sin diferencias: todo lo de la SECUNDARIA existe y coincide en la PIVOTE.${reset}"
else
  print -P "${warn}Resultados (SECUNDARIA → PIVOTE)${reset}"
  print -P "${warn}Nuevos en SEC (faltan en PIVOTE):${reset} ${#nuevos[@]}"
  (( ${#nuevos[@]} )) && printf '%s\n' "${nuevos[@]}" && print ""
  print -P "${warn}Diferentes (existen en PIVOTE pero NO coinciden):${reset} ${#diferentes[@]}"
  (( ${#diferentes[@]} )) && printf '%s\n' "${diferentes[@]}" && print ""
fi

# --- Exportación a fichero si se pidió -o ---
if [[ -n "$out_file" ]]; then
  case "$out_fmt" in
    json) { emit_json } > "$out_file" ;;
    csv)  { emit_csv  } > "$out_file" ;;
    "")   print -P "${err}Error:${reset} formato no resuelto. Usa -f csv|json o extensión .csv/.json."; exit 4 ;;
  esac
  print -P "${ok}Guardado:${reset} $out_file"
fi

# Exit code útil para CI
if (( ${#nuevos[@]} == 0 && ${#diferentes[@]} == 0 )); then
  exit 0
else
  exit 1
fi
