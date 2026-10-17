#!/usr/bin/env zsh
# Detecta archivos duplicados por hash MD5 en un directorio dado

TARGET="${1:-.}"

if [[ ! -d "$TARGET" ]]; then
  print "Uso: $0 [directorio]" >&2
  exit 1
fi

print "Buscando duplicados en: $TARGET\n"

typeset -A hash_to_file

found_any=0

while IFS= read -r file; do
  hash=$(md5 -q "$file" 2>/dev/null) || continue
  if [[ -n "${hash_to_file[$hash]}" ]]; then
    if (( !found_any )); then
      found_any=1
    fi
    print "DUPLICADO (md5: $hash)"
    print "  Original : ${hash_to_file[$hash]}"
    print "  Duplicado: $file\n"
  else
    hash_to_file[$hash]="$file"
  fi
done < <(find "$TARGET" -type f)

if (( !found_any )); then
  print "No se encontraron duplicados."
fi
