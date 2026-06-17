#!/bin/bash
# pandoc-obsidian-wrapper.sh
# Wrapper para corregir rutas desde Obsidian Pandoc plugin

# Ruta al pandoc real
PANDOC="/opt/homebrew/bin/pandoc"

# Log para diagnóstico
LOG="/tmp/pandoc-wrapper.log"
echo "=== $(date) ===" >> "$LOG"
echo "Argumentos recibidos ($#):" >> "$LOG"
printf '%s\n' "$@" >> "$LOG"

# Verificar que pandoc existe
if [[ ! -x "$PANDOC" ]]; then
    PANDOC=$(which pandoc)
fi

# Reconstruir argumentos fragmentados por el plugin
args=()
i=1

while [[ $i -le $# ]]; do
    arg="${!i}"
    
    # Si es una opción que toma valor (--lua-filter, --metadata-file, etc.)
    if [[ "$arg" =~ ^--(lua-filter|metadata-file|reference-doc|filter)= ]]; then
        # Separar opción y valor
        option="${arg%%=*}"
        value="${arg#*=}"
        
        # Quitar comillas del valor si existen
        value="${value#[\"\']}"
        value="${value%[\"\']}"
        
        # Reensamblar hasta encontrar .lua, .yaml, .docx, etc.
        while [[ ! "$value" =~ \.(lua|yaml|yml|docx|json)$ ]] && [[ $i -lt $# ]]; do
            ((i++))
            next="${!i}"
            # Quitar comillas finales si es el último fragmento
            next="${next%[\"\']}"
            value="$value $next"
        done
        
        args+=("${option}=${value}")
    else
        args+=("$arg")
    fi
    
    ((i++))
done

echo "Argumentos procesados:" >> "$LOG"
printf '%s\n' "${args[@]}" >> "$LOG"

# Ejecutar pandoc con argumentos reconstruidos
exec "$PANDOC" "${args[@]}"
