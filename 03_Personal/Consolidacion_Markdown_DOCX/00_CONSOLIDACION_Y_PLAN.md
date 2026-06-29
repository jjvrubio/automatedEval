# Consolidacion Markdown -> DOCX

## Objetivo
Concentrar en una sola carpeta los esfuerzos existentes para conversion Markdown/Obsidian a DOCX con Pandoc + filtros Lua + plantillas Word, y preparar una base clara para construir un programa Python unificado.

## Que se consolido
Se copiaron componentes desde dos zonas:

- 02_Profesional/0201_Convercus/Automatizaciones
- 03_Personal/Automaciones

Subcarpetas creadas:

- 01_publish_minimo: pipeline simple y portable (convert.sh + perfil + filtro TOC)
- 02_publicando_pipeline: variantes de publicacion y politicas TOC
- 03_tfe_pipeline: pipeline academico con portada, citas y bibliografia
- 04_postprocessing_docx: utilidades Python para aplicar estilos y comparar DOCX
- 05_plantillas: YAML y plantillas DOCX de publicacion
- 06_documentacion: notas tecnicas y criterios editoriales
- 07_referencia_personal: piezas de soporte personal reutilizables

## Hallazgos clave de la excavacion

1. Hay 3 lineas de trabajo validas y complementarias:
- Pipeline minimo (publish): sencillo, estable y ideal como nucleo.
- Pipeline academico (publicando/TFE): mas potente para portada, bibliografia y secciones.
- Post-procesado DOCX (scripts Python): agrega capacidad de homogeneizar estilos y control de calidad.

2. Hay duplicidad funcional en TOC:
- Filtro para insertar campo TOC en OpenXML.
- Opcion de ToC via Pandoc/metadata.
- Politicas de ToC por categoria semantica (doc_category / doc_class).

3. Existen rutas absolutas en scripts heredados:
- Algunos scripts dependen de rutas locales de usuario para BIB, CSL y plantillas.
- Recomendacion: parametrizar todo con argumentos CLI y/o archivo de configuracion.

4. El enfoque mas robusto para Word final es mixto:
- Generar DOCX con Pandoc usando reference-doc.
- Aplicar post-procesado opcional de estilos (aplicar_estilos_docx.py) cuando haga falta una homogeneidad estricta.

## Recomendacion de arquitectura para el nuevo programa Python

Crear un CLI unico con este flujo:

1) Carga de configuracion
- Config global YAML (rutas base, perfiles, filtros, plantillas).
- Config por proyecto (academico, linkedin, substack, informe interno).

2) Preproceso de Markdown
- Normalizacion opcional de sintaxis Obsidian.
- Validaciones basicas de front matter.

3) Compilacion Pandoc
- Ejecucion de Pandoc desde Python (subprocess) con perfiles/filtros seleccionados.
- Soporte de metadatos y reference-doc.

4) Post-proceso DOCX opcional
- Aplicar estilos desde plantilla maestra.
- Comparar salida con una referencia (QA automatizado).

5) Reporte final
- Resumen de conversion, advertencias y artefactos generados.

## Contrato minimo recomendado para la CLI

Comando sugerido:

python md2docx.py build --input archivo.md --profile tfe --metadata meta.yaml --reference-doc plantilla.docx --output salida.docx

Perfiles iniciales:

- simple_docx
- tfe_academico
- linkedin_post
- substack_post

## Orden de implementacion sugerido

1. Implementar version minima funcional con perfil simple_docx.
2. Integrar perfil tfe_academico (portada + docprep + citeproc).
3. Parametrizar rutas absolutas existentes en scripts heredados.
4. Integrar post-proceso de estilos como bandera opcional (--apply-style-template).
5. Agregar modo audit para comparar DOCX (--compare-with).

## Riesgos conocidos

- Diferencias de estilos entre plantillas Word pueden producir resultados no deterministas si no se fija una plantilla canonica.
- Filtros Lua con log por print pueden ensuciar stdout en pipelines automatizados.
- Uso mixto de doc_class y doc_category puede generar politicas TOC inconsistentes.

## Decisiones de unificacion propuestas

- Estandar semantico unico: usar doc_category (y mantener alias legacy doc_class por compatibilidad).
- Politica TOC unica: centralizar en un solo filtro Lua.
- Convencion de metadata unica: title, author, date, lang, doc_category, toc, toc-depth.

## Proximo entregable recomendado

Crear una carpeta src para el nuevo programa con:

- src/md2docx/cli.py
- src/md2docx/config.py
- src/md2docx/pandoc_runner.py
- src/md2docx/pipeline.py
- src/md2docx/postprocess.py
- configs/profiles/*.yaml

y reutilizar directamente archivos de esta consolidacion como base inicial.
