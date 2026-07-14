# md2docx

CLI consolidado para convertir Markdown/Obsidian a DOCX con Pandoc.

Este es el punto canonico para sustituir los intentos repartidos en
`publicando`, `publish`, `doc_processing` y las carpetas historicas de
`Consolidacion_Markdown_DOCX`. Los intentos anteriores estan archivados en
`_archivo_intentos_antiguos_2026-06-29`; el flujo activo entra por este
directorio.

## Estructura

- `src/md2docx/cli.py`: entrada de linea de comandos
- `src/md2docx/config.py`: carga de perfiles YAML con herencia mediante `extends`
- `src/md2docx/pandoc_runner.py`: construccion y ejecucion del comando Pandoc
- `src/md2docx/pipeline.py`: orquestacion del flujo build
- `src/md2docx/postprocess.py`: punto de extension para post-procesado DOCX
- `configs/profiles/*.yaml`: perfiles de conversion

## Instalacion local

No hace falta instalar nada para usar el proyecto desde esta carpeta:

```bash
cd /Users/juanjo/Documents/Personal/JJVR/automatizaciones/03_Personal/Consolidacion_Markdown_DOCX
python md2docx.py profiles
```

Si quieres instalar el comando `md2docx` en un entorno virtual:

```bash
cd /Users/juanjo/Documents/Personal/JJVR/automatizaciones/03_Personal/Consolidacion_Markdown_DOCX
python -m pip install -e .
```

## Uso inicial

```bash
python md2docx.py build \
  --input /ruta/archivo.md \
  --profile research_article \
  --output /ruta/salida.docx
```

`--input` acepta varios Markdown en orden, util para generar un tema completo
desde varios epigrafes:

```bash
python md2docx.py build \
  --input "Tema 1 Epigrafe 1.md" "Tema 1 Epigrafe 2.md" "Tema 1 Epigrafe 3.md" \
  --profile docx_unir_theme \
  --output "TEMA 1 generado.docx"
```

Para ver todos los perfiles disponibles:

```bash
python md2docx.py profiles
```

## Tres escenarios canonicos

- `research_article`: articulos de investigacion, ensayos largos y piezas con
  citas. Activa `citeproc`, APA 7 e indice de profundidad 3.
- `commercial_proposal`: propuestas comerciales y ofertas. Usa indice corto,
  metadatos de propuesta, marca Convercus y la plantilla especifica
  `assets/templates/plantilla_oferta.docx`.
- `teaching_material`: material docente, lecciones y temas. Activa portada,
  `citeproc`, APA 7 e indice de profundidad 3.

Los tres perfiles heredan de `base_docx`, que define:

- entrada Markdown compatible con YAML frontmatter, tablas, fenced divs,
  resaltados y sintaxis Obsidian comun;
- filtro `filters/obsidian-docx.lua` para callouts, resaltados e imagenes
  `![[...]]`;
- filtro comun de indice `filters/docprep.lua`;
- plantilla Word predeterminada `assets/templates/plantilla_pulse.docx`. El
  perfil `commercial_proposal` la sustituye por `plantilla_oferta.docx`.

### Portada de propuestas comerciales

`commercial_proposal` conserva y completa la portada nativa de
`plantilla_oferta.docx`. El bloque inicial del Markdown debe seguir esta
estructura:

```markdown
# Subtitulo de la propuesta
# Titulo o nombre del cliente/proyecto
## Linea secundaria o caso de uso

> **Cliente final:** Ejemplo
> **Fecha:** 13 de julio de 2026
> **Version:** v0.2

---
```

El segundo `#` rellena el título, el primero rellena el subtítulo y el primer
`##`, junto con las líneas de control documental citadas con `>`, aparece
debajo. El filtro retira este bloque del cuerpo para evitar duplicados. El año
se obtiene de `date` en el frontmatter.

## Compatibilidad

Estos perfiles antiguos siguen existiendo como aliases o variantes heredadas:

- `docx_article` -> `research_article`
- `docx_offer` -> `commercial_proposal`
- `docx_class_material` -> `teaching_material`
- `docx_convercus_article` -> `research_article` con `resource_path` Convercus
- `docx_convercus_offer` -> `commercial_proposal` con `resource_path` Compactor
- `docx_unir_theme` -> `teaching_material` con `resource_path` UNIR
- `simple_docx`, `tfe_academico`, `linkedin_post` y `substack_post` se conservan
  para conversiones antiguas especificas.

## Frontmatter sugerido en Obsidian

```yaml
---
title: "Titulo del documento"
author: "Juan Jose Velasco"
doc_type: research_article
lang: es
toc: true
toc_depth: 3
bibliography: "/ruta/a/export-zotero.bib"
resource_path:
  - "/ruta/al/vault/obsidian"
---
```

Las citas ZotLit/Zotero deben quedar en sintaxis Pandoc, por ejemplo
`[@clave2026]` o `[@clave2026, p. 42]`. Los perfiles APA 7 activan
`--citeproc` y usan `assets/csl/apa-7th-edition.csl`.

## Sintaxis Obsidian soportada

El filtro `filters/obsidian-docx.lua` normaliza:

- Resaltados `==texto==` hacia resaltado nativo de Word.
- Callouts `>[!note]`, `>[!warning]`, etc. hacia tablas Word de una celda,
  con fondo suave, borde lateral por tipo e iconos gráficos de `SF Symbols`.
- Admonitions en bloques `ad-note`, `ad-warning`, etc. hacia el mismo tratamiento que los callouts.
- Embeds de imagen Obsidian `![[imagen.png]]` hacia imagenes DOCX, usando `resource_path`.

## Saltos de pagina y de seccion

El filtro `filters/page-section-breaks.lua` interpreta las lineas horizontales
Markdown como instrucciones de maquetacion para Word:

```markdown
---
```

Una linea genera un salto de pagina normal.

```markdown
---
---
```

Dos lineas consecutivas generan un salto de seccion de tipo **Pagina
siguiente**. Puede haber una linea en blanco entre ambas: Pandoc sigue
considerandolas consecutivas mientras no exista otro contenido. Los
delimitadores `---` del frontmatter YAML no se transforman.

El flujo canonico usa `plantilla_pulse.docx`. Si necesitas probar otra plantilla
sin tocar perfiles:

```bash
python md2docx.py build \
  --input documento.md \
  --profile commercial_proposal \
  --reference-doc /ruta/otra_plantilla.docx
```

## Notas

- Usa rutas absolutas o relativas validas en los perfiles YAML.
- Si `pandoc` no esta en PATH, el comando fallara con un mensaje claro.
