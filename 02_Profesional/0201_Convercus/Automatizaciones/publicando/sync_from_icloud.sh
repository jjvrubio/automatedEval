#!/bin/bash

# Ruta local al repositorio clonado
REPO='/Users/juanjo/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research/pulse_images'

# Ruta a la carpeta en iCloud (con acento y espacios)
SOURCE="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research/imágenes para LinkedIn"

# Subcarpeta de destino en el repositorio
TARGET="."

# Acceder al repositorio
cd "$REPO" || { echo "❌ No se pudo acceder al repositorio en $REPO."; exit 1; }

# Crear carpeta si no existe
mkdir -p "$TARGET"

# Copiar archivos (sobrescribe si ya existen con mismo nombre)
cp "$SOURCE"/* "$TARGET" / 2>/dev/null || { echo "❌ Error al copiar archivos desde $SOURCE a $TARGET."; exit 1; }

# Verificar si hay cambios (sin commit innecesario)
if git diff --quiet && git diff --cached --quiet; then
  echo "✅ No hay cambios nuevos que sincronizar."
  exit 0
fi

# Añadir cambios al control de versiones
git add "$TARGET"

# Commit con fecha
DATE=$(date +"%Y-%m-%d %H:%M")
git commit -m "Sincronización desde iCloud → $TARGET: $DATE"

# Push a GitHub
git push origin main

echo "✅ Sincronización completada: $TARGET actualizado y subido a GitHub."