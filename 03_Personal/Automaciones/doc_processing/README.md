# Document processing

Utilidades personales para convertir documentos Markdown/Obsidian a formatos publicables.

## `build-pdf.sh`

Convierte un Markdown a PDF con `pandoc` y `xelatex`. Está pensado para notas de Obsidian que pueden contener imágenes SVG incrustadas con sintaxis `![[imagen.svg]]`.

El script:

1. Convierte los SVG de la carpeta de imágenes a PDF vectorial con `rsvg-convert`.
2. Genera una copia temporal del Markdown donde los embeds de Obsidian `![[...svg]]` se sustituyen por enlaces Pandoc `![](...pdf)`.
3. Compila el PDF usando `plantilla-pdf.tex` y el filtro `callouts.lua`.

### Requisitos

- `pandoc`
- `xelatex`
- `rsvg-convert` (`brew install librsvg`)
- `perl`

La plantilla usa varios paquetes LaTeX. En una instalación básica de TeX Live pueden hacer falta paquetes como `lastpage`, `tcolorbox`, `environ`, `trimspaces`, `etoolbox`, `pgf` y `pdfcol`.

Instalación en modo usuario:

```bash
tlmgr init-usertree 2>/dev/null || true
tlmgr --usermode install lastpage tcolorbox environ trimspaces etoolbox pgf pdfcol
```

### Uso

```bash
./build-pdf.sh SRC_MD [OUT_PDF] [IMGDIR] [TEMPLATE_TEX]
```

Argumentos:

- `SRC_MD`: Markdown de entrada.
- `OUT_PDF`: PDF de salida. Si se omite, se crea junto al Markdown con extensión `.pdf`.
- `IMGDIR`: carpeta donde están los SVG/PDF referenciados por el Markdown. Si se omite, usa la carpeta del Markdown.
- `TEMPLATE_TEX`: plantilla LaTeX. Si se omite, usa `plantilla-pdf.tex` en esta carpeta.

### Ejemplo

```bash
./build-pdf.sh \
  "/ruta/al/articulo.md" \
  "/ruta/al/articulo.pdf" \
  "/ruta/a/imagenes"
```

### Cabeceras y pies de página

La plantilla lee cabeceras y pies desde el YAML front matter del Markdown mediante metadatos de Pandoc.

Variables soportadas:

- `header-left`
- `header-center`
- `header-right`
- `footer-left`
- `footer-center`
- `footer-right`

Ejemplo:

```yaml
---
title: "Título del artículo"
author: "Convercus"
date: "2026"

header-left: "Convercus"
header-center: ""
header-right: "Beyond Trade"

footer-left: "Documento interno"
footer-center: "\\thepage\\ de \\pageref{LastPage}"
footer-right: "2026"
---
```

Notas:

- Si `footer-center` se omite, la plantilla usa `\thepage`.
- Para numeración `Página X de Y`, usa `\\thepage\\ de \\pageref{LastPage}` en YAML.
- La plantilla fuerza `fancy` también después de `\maketitle`, por lo que cabeceras y pies aparecen en la primera página cuando hay título.

### Prueba de cabeceras y pies

El archivo `header-footer-test.md` verifica que los metadatos YAML llegan a la plantilla.

Generar el PDF de prueba:

```bash
./build-pdf.sh header-footer-test.md header-footer-test.pdf
```

Verificar por extracción de texto:

```bash
TMP=$(mktemp)
pdftotext header-footer-test.pdf "$TMP"
grep -n 'HFTEST-' "$TMP"
grep -nE '[0-9]+ de [0-9]+' "$TMP"
rm -f "$TMP"
```

El PDF generado `header-footer-test.pdf` está excluido de git porque es un artefacto reproducible.

### Notas

- El Markdown original no se modifica.
- Si existe un PDF correspondiente a un SVG y está actualizado, no se regenera.
- Los embeds `![[subcarpeta/imagen.svg]]` se resuelven por nombre de archivo dentro de `IMGDIR`.
