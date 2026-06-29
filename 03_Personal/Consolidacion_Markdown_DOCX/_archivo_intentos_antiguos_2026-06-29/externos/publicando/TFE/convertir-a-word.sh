

# CONFIGURACIÓN DE RUTAS
BIB="/Users/juanjo/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research/Kaleida GM bibliografía.bib"
CSL="/Users/juanjo/Documents/Personal/JJVR/automatizaciones/publicando/apa-7th-edition.csl"
REFERENCE_DOC="/Users/juanjo/Documents/Personal/JJVR/automatizaciones/publicando/Para Pulse/plantilla_pulse_vacia.docx" # Esta palntilla la cambio cuando voya a publicar en pulse
LUA_PORTADA="/Users/juanjo/Documents/Personal/JJVR/automatizaciones/publicando/portada.lua"
LUA_DOCPREP="/Users/juanjo/Documents/Personal/JJVR/automatizaciones/publicando/docprep.lua"
IMGS="/Users/juanjo/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research/"

# VERIFICACIÓN DE ARGUMENTOS
if [ -z "$1" ]; then
  echo "❌ Debes proporcionar el nombre del archivo .md como argumento"
  exit 1
fi

# === Manejo robusto del segundo parámetro opcional: metadata file YAML===
if [ -n "$2" ]; then
  YAML="$2"
  if [ ! -f "$YAML" ]; then
    echo "❌ El archivo de metadatos no existe: $YAML"
    exit 1
  fi
  YAML_OPTION=(--metadata-file "$YAML")
else
  YAML_OPTION=()
fi


MD="$1"
DOCX="${MD%.md}.docx"


# VERIFICACIÓN DE EXISTENCIA DE ARCHIVOS
if [ ! -f "$MD" ]; then
  echo "❌ El archivo Markdown no existe: $MD"
  exit 1
fi

if [ ! -f "$BIB" ]; then
  echo "❌ El archivo .bib no existe: $BIB"
  exit 1
fi

if [ ! -f "$CSL" ]; then
  echo "❌ El archivo .csl no existe: $CSL"
  exit 1
fi

if [ ! -f "$REFERENCE_DOC" ]; then
  echo "⚠️ El archivo de plantilla Word no existe: $REFERENCE_DOC"
  echo "⏩ Continuando sin plantilla personalizada"
  REFERENCE_OPTION=()
else
  REFERENCE_OPTION=(--reference-doc "$REFERENCE_DOC")
fi



pandoc "$MD" -o "$DOCX" \
  --metadata-file="$YAML" \
  --metadata link-citations=true \
  --from markdown+fenced_divs \
  --lua-filter="$LUA_PORTADA" \
  --lua-filter="$LUA_DOCPREP" \
  --citeproc \
  --bibliography="$BIB" \
  --csl="$CSL" \
  --resource-path="$IMGS" \
  "${REFERENCE_OPTION[@]}" \
  --toc --toc-depth=2 \
  --verbose
  

if [ $? -ne 0 ]; then
  echo "❌ Error: Pandoc no ha podido completar la conversión."
  exit 1
fi


# === Resultado final ===
if [[ -f "$DOCX" ]]; then
  echo "✅ Conversión completada: $DOCX"
else
  echo "⚠️ Hubo un error al generar el archivo Word."
fi