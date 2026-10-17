#!/usr/bin/env zsh

uso() {
  cat <<'EOF'
Uso:
  ./generar_docx_desde_lista.sh <lista_entrada.txt> <salida.docx>

Ejemplos:
  ./generar_docx_desde_lista.sh lista_tema8.txt tema8_rev.docx
  ./generar_docx_desde_lista.sh /ruta/lista_tema9.txt /ruta/tema9_rev.docx
EOF
}

if [[ $# -ne 2 ]]; then
  uso
  exit 1
fi

lista="$1"
salida="$2"

if [[ ! -f "$lista" ]]; then
  print -u2 "Error: no existe el archivo de lista: $lista"
  exit 1
fi
lista_abs="$(cd "$(dirname "$lista")" && pwd)/$(basename "$lista")"
base_dir="$(dirname "$lista_abs")"

files=()
faltan=0

while IFS= read -r line || [[ -n "$line" ]]; do
  line="${line%$'\r'}"
  [[ -z "$line" ]] && continue
  [[ "$line" == \#* ]] && continue

  if [[ "$line" == /* ]]; then
    entrada="$line"
  else
    entrada="$base_dir/$line"
  fi

  if [[ ! -f "$entrada" ]]; then
    print -u2 "Error: no existe el archivo listado: $entrada"
    faltan=1
    continue
  fi

  files+=("$entrada")
done < "$lista_abs"

if [[ ${#files[@]} -eq 0 ]]; then
  print -u2 "Error: $lista no contiene entradas válidas."
  exit 1
fi

if [[ "$faltan" -eq 1 ]]; then
  print -u2 "Error: hay archivos faltantes en la lista. No se genera salida."
  exit 1
fi

if pandoc "${files[@]}" -o "$salida"; then
  print "OK: generado $salida"
else
  print -u2 "Error: falló pandoc"
  exit 1
fi
exit 0
