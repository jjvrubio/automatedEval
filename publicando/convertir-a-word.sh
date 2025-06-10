#!/bin/bash
# Script: convertir-a-word-avanzado.sh
# Objetivo: Convertir un archivo .md a .docx con Pandoc
# - Inserta salto de página antes de la bibliografía
# - Genera citas con citeproc y bibliografía automática
# - Aplica estilo APA 7 y tabla de contenido opcional

##!/bin/bash

#!/bin/bash
# Script: convertir-a-word-avanzado.sh

# CONFIGURACIÓN DE RUTAS
BIB="/Users/juanjo/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research/Kaleida GM bibliografía.bib"
CSL="/Users/juanjo/Documents/Personal/JJVR/automatizaciones/publicando/apa-7th-edition.csl"
REFERENCE_DOC="/Users/juanjo/Documents/Personal/JJVR/automatizaciones/publicando/Para Pulse/plantilla pulse.docx" # Esta palntilla la cambio cuando voya a publicar en pulse

# VERIFICACIÓN DE ARGUMENTOS
if [ -z "$1" ]; then
  echo "❌ Debes proporcionar el nombre del archivo .md como argumento"
  exit 1
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

LUA_FILTER="/Users/juanjo/Documents/Personal/JJVR/automatizaciones/publicando/pagebreak.lua"

# EJECUCIÓN DE PANDOC
pandoc "$MD" -o "$DOCX" \
  --citeproc \
  --bibliography="$BIB" \
  --csl="$CSL" \
  "${REFERENCE_OPTION[@]}" \
  --lua-filter="$LUA_FILTER" \
  --toc \
  --metadata link-citations=true \
  --verbose \

