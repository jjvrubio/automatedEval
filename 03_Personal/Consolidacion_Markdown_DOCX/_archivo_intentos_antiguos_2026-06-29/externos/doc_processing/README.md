# Document processing

Utilidades personales para convertir documentos Markdown/Obsidian a formatos publicables.

Este repositorio está pensado para un flujo de trabajo basado en:

```text
Obsidian Markdown
→ normalización de embeds de Obsidian
→ conversión de SVG a PDF vectorial
→ filtros Lua de Pandoc, si existen
→ compilación PDF con Pandoc + XeLaTeX
```

El objetivo es mantener los archivos `.md` limpios dentro de Obsidian y concentrar la lógica de publicación en scripts, plantillas y filtros reutilizables.

---

## Script principal: `build-pdf-toc.sh`

`build-pdf-toc.sh` convierte un archivo Markdown a PDF usando `pandoc` y `xelatex`.

Está preparado para notas de Obsidian que pueden contener imágenes incrustadas con sintaxis propia, por ejemplo:

```markdown
![[figura.svg]]
![[subcarpeta/figura.svg]]
![[figura.svg|500]]
![[imagen.png]]
![[imagen.jpg]]
```

El script:

1. Convierte los archivos `.svg` de la carpeta de imágenes a `.pdf` vectorial con `rsvg-convert`.
2. Genera una copia temporal del Markdown original.
3. Traduce los embeds de Obsidian a sintaxis compatible con Pandoc.
4. Compila el PDF usando una plantilla LaTeX.
5. Aplica `callouts.lua` si el filtro existe junto al script.
6. Genera tabla de contenidos por defecto mediante Pandoc.

El Markdown original no se modifica.

---

## Tabla de contenidos

La tabla de contenidos se genera con Pandoc a partir de los encabezados Markdown:

```markdown
# Título del documento

## 1. Introducción

### 1.1. Contexto

## 2. Desarrollo

### 2.1. Primer argumento

## 3. Conclusión
```

Por defecto, `build-pdf-toc.sh` incluye tabla de contenidos con profundidad `3`, es decir:

```text
#
##
###
```

Esto equivale a llamar a Pandoc con:

```bash
--toc --toc-depth=3
```

### Opciones disponibles

```bash
./build-pdf-toc.sh [opciones] SRC_MD [OUT_PDF] [IMGDIR] [TEMPLATE_TEX]
```

Opciones:

- `--toc`: activa la tabla de contenidos. Es el comportamiento por defecto.
- `--no-toc`: desactiva la tabla de contenidos para un documento concreto.
- `--toc-depth N`: define la profundidad del índice. Por defecto: `3`.
- `--toc-title TEXTO`: define el título del índice. Por defecto: `Índice`.
- `--number-sections`: numera automáticamente las secciones.
- `-h`, `--help`: muestra la ayuda del script.

### Ejemplos

Generar PDF con índice por defecto:

```bash
./build-pdf-toc.sh articulo.md
```

Generar PDF con índice hasta nivel `##`:

```bash
./build-pdf-toc.sh --toc-depth 2 articulo.md
```

Generar PDF con índice hasta nivel `###` y secciones numeradas:

```bash
./build-pdf-toc.sh --toc-depth 3 --number-sections articulo.md
```

Generar PDF sin índice:

```bash
./build-pdf-toc.sh --no-toc articulo.md
```

Generar PDF con título personalizado para la tabla de contenidos:

```bash
./build-pdf-toc.sh --toc-title "Tabla de contenidos" articulo.md
```

Generar PDF indicando salida y carpeta de imágenes:

```bash
./build-pdf-toc.sh \
  --toc-depth 3 \
  "/ruta/al/articulo.md" \
  "/ruta/al/articulo.pdf" \
  "/ruta/a/imagenes"
```

---

## Argumentos posicionales

```bash
./build-pdf-toc.sh [opciones] SRC_MD [OUT_PDF] [IMGDIR] [TEMPLATE_TEX]
```

Argumentos:

- `SRC_MD`: archivo Markdown de entrada.
- `OUT_PDF`: ruta del PDF de salida. Si se omite, se crea junto al Markdown con extensión `.pdf`.
- `IMGDIR`: carpeta donde están las imágenes referenciadas por el Markdown. Si se omite, usa la carpeta del Markdown.
- `TEMPLATE_TEX`: plantilla LaTeX de Pandoc. Si se omite, usa `plantilla-pdf.tex` junto al script.

---

## Requisitos

Dependencias principales:

- `pandoc`
- `xelatex`
- `rsvg-convert`
- `perl`

En macOS, una instalación típica sería:

```bash
brew install pandoc librsvg
```

Para `xelatex`, instala una distribución LaTeX. Por ejemplo, MacTeX o BasicTeX.

Si usas BasicTeX, puede que necesites añadir paquetes LaTeX adicionales. La plantilla puede requerir paquetes como:

- `lastpage`
- `tcolorbox`
- `environ`
- `trimspaces`
- `etoolbox`
- `pgf`
- `pdfcol`

Instalación en modo usuario:

```bash
tlmgr init-usertree 2>/dev/null || true
tlmgr --usermode install lastpage tcolorbox environ trimspaces etoolbox pgf pdfcol
```

Dar permisos de ejecución al script:

```bash
chmod +x build-pdf-toc.sh
```

---

## Plantilla LaTeX y tabla de contenidos

Para que la tabla de contenidos aparezca correctamente en el PDF, la plantilla `plantilla-pdf.tex` debe incluir el bloque `$toc$` de Pandoc.

Una posición habitual es después de `\maketitle` y antes de `$body$`:

```latex
\begin{document}

$if(title)$
\maketitle
$endif$

$if(toc)$
$if(toc-title)$
\renewcommand*\contentsname{$toc-title$}
$endif$
{
\hypersetup{linkcolor=black}
\tableofcontents
\newpage
}
$endif$

$body$

\end{document}
```

Si la plantilla no contiene este bloque, el script puede enviar `--toc` a Pandoc, pero el índice no aparecerá en el lugar esperado del PDF.

---

## Cabeceras y pies de página

La plantilla puede leer cabeceras y pies desde el YAML front matter del Markdown mediante metadatos de Pandoc.

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

- Si `footer-center` se omite, la plantilla puede usar `\thepage`.
- Para numeración `Página X de Y`, usa `\\thepage\\ de \\pageref{LastPage}` en YAML.
- Si la plantilla usa `fancyhdr`, puede forzarse el estilo `fancy` también después de `\maketitle` para que cabeceras y pies aparezcan en la primera página.

---

## YAML recomendado para artículos largos

Para artículos que casi siempre deban llevar índice, el índice se controla mejor desde el script. El YAML puede mantenerse centrado en metadatos editoriales:

```yaml
---
title: "Título del artículo"
author: "Juan"
date: "2026-06-22"
lang: es

header-left: "Serie editorial"
header-right: "Documento de trabajo"
footer-left: "© Juan"
footer-center: "\\thepage\\ de \\pageref{LastPage}"
footer-right: "2026"
---
```

Y la profundidad del índice se decide al compilar:

```bash
./build-pdf-toc.sh --toc-depth 3 articulo.md
```

Para documentos excepcionales sin índice:

```bash
./build-pdf-toc.sh --no-toc articulo.md
```

---

## Tratamiento de imágenes y embeds de Obsidian

El script resuelve imágenes desde `IMGDIR`.

### SVG

Los SVG se convierten previamente a PDF vectorial:

```text
imagen.svg → imagen.pdf
```

Y los embeds de Obsidian:

```markdown
![[imagen.svg]]
![[subcarpeta/imagen.svg]]
![[imagen.svg|500]]
```

se transforman en:

```markdown
![](<IMGDIR/imagen.pdf>)
```

Cualquier prefijo de ruta dentro del embed se descarta y se usa el nombre del archivo dentro de `IMGDIR`.

### Imágenes raster y PDF

Los siguientes formatos se transforman sin conversión previa:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`
- `.gif`
- `.pdf`

Ejemplo:

```markdown
![[imagen.png]]
```

se transforma en:

```markdown
![](<IMGDIR/imagen.png>)
```

---

## Filtros Lua

Si existe un archivo `callouts.lua` junto al script, `build-pdf-toc.sh` lo aplica automáticamente:

```bash
--lua-filter="callouts.lua"
```

Si `callouts.lua` no existe, el PDF se genera igualmente sin aplicar ese filtro.

Esto permite mantener la transformación de callouts como una capa opcional, sin bloquear la exportación básica.

---

## Script anterior: `build-pdf.sh`

`build-pdf.sh` es la versión previa del flujo.

Características principales:

1. Convierte SVG a PDF vectorial.
2. Traduce embeds de Obsidian `![[...svg]]` a enlaces Pandoc `![](...pdf)`.
3. Compila usando `plantilla-pdf.tex` y `callouts.lua`.

Limitaciones frente a `build-pdf-toc.sh`:

- No activa tabla de contenidos por defecto.
- No incluye opciones `--no-toc`, `--toc-depth` ni `--toc-title`.
- Solo transforma embeds SVG.
- Requiere que `callouts.lua` exista.

Se recomienda usar `build-pdf-toc.sh` como script principal para artículos y documentos largos.

---

## Prueba de cabeceras y pies

El archivo `header-footer-test.md` puede usarse para verificar que los metadatos YAML llegan a la plantilla.

Generar el PDF de prueba:

```bash
./build-pdf-toc.sh --no-toc header-footer-test.md header-footer-test.pdf
```

Verificar por extracción de texto:

```bash
TMP=$(mktemp)
pdftotext header-footer-test.pdf "$TMP"
grep -n 'HFTEST-' "$TMP"
grep -nE '[0-9]+ de [0-9]+' "$TMP"
rm -f "$TMP"
```

El PDF generado `header-footer-test.pdf` debería excluirse de git porque es un artefacto reproducible.

---

## Notas de uso

- El Markdown original no se modifica.
- El script trabaja sobre una copia temporal.
- Si existe un PDF correspondiente a un SVG y está actualizado, no se regenera.
- Los embeds `![[subcarpeta/imagen.svg]]` se resuelven por nombre de archivo dentro de `IMGDIR`.
- La tabla de contenidos se genera desde los encabezados `#`, `##`, `###`, etc.
- Para artículos extensos, usa `--toc-depth 3`.
- Para documentos más breves o destinados a reutilización editorial, usa `--toc-depth 2`.
