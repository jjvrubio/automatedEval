# XLSX → PDF (macOS / Microsoft Excel)

Resumen
-------
Esta carpeta contiene herramientas (AppleScript + VBA) para copiar archivos Excel y exportar hojas/worksheets a PDF usando Microsoft Excel en macOS. Las versiones actuales han sido ajustadas para: filtrar ficheros temporales, soportar `.xlsx`, `.xlsm` y `.xls`, evitar sobrescrituras (añadiendo sufijos temporales) y dejar logs de operación.

Requisitos
---------
- macOS con Microsoft Excel instalado y habilitado para scripting (System Preferences → Seguridad y privacidad → Acceso total al disco / Control del ordenador si se pide).
- AppleScript (incluido en macOS) y permisos para controlar Excel.
- Para la macro VBA: abrir `macro_enabled_workbook.xlsm` o pegar la macro en el Editor de VBA de Excel (Alt+F11) y ejecutar `ExportWorksheetsToPDF`.
- Opcional: `osascript` desde terminal para ejecutar los `.applescript`.

Qué hace cada archivo
----------------------
- `all XLXS to a folder.applescript` — Copia recursivamente todos los ficheros Excel (`.xlsx`, `.xlsm`, `.xls`) de la carpeta seleccionada a una carpeta destino `NOMBRE_CARPETA XLSXs/`. Ignora archivos temporales que empiecen por `~$` y evita sobrescribir archivos existentes añadiendo un sufijo timestamp.

- `worksheet-a-PDF.applescript` — Recorre los ficheros Excel de la carpeta seleccionada, abre cada archivo en Microsoft Excel, intenta seleccionar la hoja `Rubrica` (si existe) y, si no, la primera hoja. Ajusta el `PageSetup` a A4 y exporta a PDF; escribe trazas en `conversion_log.txt` en la misma carpeta.

- `Sub ExportWorksheetsToPDF().vb` — Macro VBA que recorre los ficheros en la carpeta seleccionada (soporta `*.xlsx`, `*.xlsm`, `*.xls`), exporta la hoja `Rubrica` o la primera hoja a PDF usando `ExportAsFixedFormat`, evita sobrescribir y escribe un log en `export_log.txt`.

Notas de seguridad
------------------
- No dejes credenciales ni datos sensibles en los scripts. Usa variables de entorno o ficheros de configuración fuera del repositorio cuando sea necesario.

Cómo probar (sin cambiar archivos originales)
--------------------------------------------
1. Abre Finder y copia una carpeta de prueba con un par de `.xlsx` pequeños.
2. Ejecuta `all XLXS to a folder.applescript` (doble click o `osascript PATH/TO/file.applescript`) y selecciona la carpeta raíz.
3. Comprueba el contenido de la carpeta destino.
4. Ejecuta `worksheet-a-PDF.applescript`, selecciona la carpeta con los `.xlsx` y revisa `conversion_log.txt`.

Siguiente pasos propuestos
-------------------------
- (Opcional) Añadir una versión CLI que use LibreOffice headless para conversiones batch en servidores (trade-off: puede no preservar layout exacto).
- Añadir tests automatizados que instancien Excel via AppleScript en un entorno controlado (difícil de automatizar en CI sin licencias).

Contacto
--------
Si quieres que aplique los cambios al repo (commit) y cree una rama `fix/xlsx-pdf-scripts`, lo hago y te muestro el diff antes del commit.
