# Consolidación del repositorio — 2026-10-17

## Resultado y alcance

Se separaron los 869 cambios inicialmente preparados y el archivo sin seguimiento
por proyecto. El trabajo actual queda integrado en `principal`, empezando por
Convercus App. Se preservaron los 1308 archivos presentes en el índice inicial:
ninguno falta en disco. Los únicos contenidos recibidos retocados durante esta
consolidación son los dos `.gitignore` y la errata `.docxm` → `.docx` del ejemplo
en el README de Markdown/DOCX. Se añadieron este informe y el de Convercus.

| Orden | Proyecto | Commit | Verificación |
| --- | --- | --- | --- |
| 1 | Convercus App / Demo Factory / Sports Season | `5797c7c` | TypeScript, lint y build PASS; producto actual 63/63; suite completa 159 PASS y 22 FAIL |
| 2 | OSINT | `802ee4a` | 20/20 unittest; integra la rama original y la corrección MEDDICC recibida |
| 3 | UNIR / instrucciones Qwen | `65cab8d` | Seis documentos UTF-8 no vacíos |
| 4 | P1.D2 | `229ee1f` | 88/88 pytest |
| 5 | Markdown/DOCX | `78c4a39` | 10/10 unittest; plantilla con ZIP íntegro y XML válido |
| 6 | small_tools / macOS / SVG | `4350025` | 3/3 pytest de correo; sintaxis shell de los nuevos scripts y Python verificada |
| 7 | Ajustes del repositorio | `0c814a7` | Exclusiones locales, configuración recibida y retirada de subtítulos ya preparada |

La incorporación de Convercus a `principal` fue un avance rápido, comprobando
que la referencia anterior era antecesora de la nueva. OSINT se integró con un
merge que conserva la versión recibida: respecto a su rama original únicamente
difieren `stage2/runner.py` y `tests/test_stage2.py`, por la corrección y prueba
del contexto `provided_meddicc`. Ningún otro cambio de esa rama se omite.

## Limitaciones verificadas

La suite completa de Convercus **no pasa**. Se conservan los 21 fallos del último
informe y se identifica otro de Sesión 40 que participa sin seleccionar persona.
No se modificaron pruebas, evidencias históricas ni código para ocultarlos.
El detalle y los comandos están en
[el informe de Convercus](../02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/docs/git-consolidation-2026-10-17.md).
No se realizó una nueva validación visual del producto ni de la plantilla Word.
Las utilidades de correo y copia se validaron sin mover correos ni archivos reales.

Comandos de los demás proyectos, desde su directorio correspondiente:

- OSINT y Markdown/DOCX: `python3 -m unittest discover -s tests -q`.
- P1.D2: `../../venv_arm64/bin/python -m pytest`.
- Correo, desde la raíz: `venv_arm64/bin/python -m pytest -q 03_Personal/small_tools/mac_automation/scripts_de_apoyo/test_move_sent_messages.py`.

## Archivos que permanecen únicamente en disco

- Convercus: `00-governance.zip`, `products/convercus-app.zip` y `products/convercus-app/docs.zip`.
- `03_Personal/P1_D2_ENGINE_v0_1.zip`.
- Backup de `apollo-accounts-export.backup-before-stage1-update.csv`.
- `package-lock.json` vacío en la raíz, donde no existe `package.json`.

Las fuentes, datasets de entrada y evidencias referenciadas sí se conservan en
Git. En particular, los dos `pre-build-sources.tar.gz` se mantienen como evidencia.
No se borró ningún archivo local como consecuencia de las exclusiones.

## Cierre de ramas y preservación histórica

Las ramas locales ya incorporadas (`feature/convercus-app-simulator`,
`docs/convercus-lovable-guide`, `feature/osint-ccus-agentic-pipeline`,
`feature/maintenance-scripts` y `release/v1.0`) se retiran tras guardar etiquetas
locales `archive/2026-10-17/…` con sus puntas exactas. El punto inicial `66b2465`
se conserva en la etiqueta local `backup/pre-consolidation-20261017`.

Dos ramas se conservan renombradas, sin declarar sus cambios pendientes como
integrados:

- `archive/2026-10-17/auto-fix-problems` (`f207c51`): contiene alternativas de
  exportación VBA/PDF (nombre de salida, ajuste de página y manejo de archivos)
  distintas del producto actual. No se sustituyen las macros vigentes ni se
  retira el AppleScript actual sin una validación funcional específica en Excel.
- `archive/2026-10-17/comparar-carpetas` (`3881a0b`): el copiado de Excel y lectura
  de etiquetas ya coinciden con la versión actual; la comparación de carpetas
  actual añade `-R` y `-G`. Se conserva la rama para mantener su genealogía y
  documentación antiguas sin reintroducir rutas obsoletas.

El stash de 2025 (`592ffb8`) se conserva intacto, con una etiqueta local adicional
`backup/stash-pre-consolidation-20261017`. De sus 59 archivos modificados, 57
coinciden byte a byte con los actuales. Los dos restantes son `importarActa.py`
(la versión actual incorpora modo no interactivo) y
`Evaluador_TFM_Integrado_ultraestricto.py` (con ampliaciones posteriores). El stash
incluye además documentación WIP y una copia histórica del comparador de carpetas.
No se aplica sobre la versión actual ni se elimina.

La sincronización prevista publica únicamente `principal`, por avance normal,
sin reescribir el historial remoto. Las etiquetas de respaldo, ramas archivadas
y stash permanecen locales; no se borran ramas remotas.

## Recuperación local

En `/private/tmp/git-consolidation-20261017/` se guardaron el índice inicial,
los parches completos de cambios preparados y sin preparar, las referencias y
`before-consolidation.bundle` (todas las referencias originales, incluido stash).
También contiene logs de verificación de Convercus y comparaciones de contenido.
Es una copia temporal complementaria; las etiquetas locales preservan el historial.
