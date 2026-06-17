# Exportar hoja "rúbrica" a PDF (Automatización)

Este módulo contiene la macro `ExportRubricaToPDF` (archivo `Export_Rubrica_To_PDF.bas`) para Excel en macOS que:

- Busca en una carpeta los libros Excel (.xlsx, .xlsm, .xls).
- Abre cada libro, busca la hoja cuyo nombre contiene "rúbrica" (insensible a acentos y mayúsculas) y la exporta a PDF en la misma carpeta.

Características importantes
- Evita sobrescribir PDFs añadiendo un sufijo con timestamp si ya existe el fichero.
- Por defecto el logging está DESACTIVADO porque muchos usuarios guardan los TFM en OneDrive y la creación del fichero `export_log.txt` puede fallar por placeholders / Files On‑Demand.

Cómo usar
1. Abrir Excel en macOS.
2. Importar el módulo `Export_Rubrica_To_PDF.bas` en el editor de Visual Basic (VBE) o pegar el contenido en un módulo nuevo.
3. Opcional: en la parte superior del módulo hay una constante `ENABLE_LOG`. Si quieres logs, cámbiala a `True`. Por defecto está en `False`.
4. Ejecutar la macro `ExportRubricaToPDF` y seleccionar la carpeta que contiene los ficheros TFM.

Notas y recomendaciones (OneDrive)
- Si guardas los TFM en OneDrive (Files On‑Demand), puede que algunos ficheros sean placeholders y no estén realmente descargados. En ese caso la macro puede fallar al intentar abrir o escribir en la carpeta.
- Recomendación más fiable: en Finder, clic derecho sobre la carpeta → OneDrive → "Always keep on this device" para asegurar que los archivos están locales.
- Alternativa: copia los ficheros a una carpeta local (por ejemplo `~/Desktop/TFM_prueba`) y ejecuta la macro allí.

Permisos macOS
- La macro usa AppleScript para algunos fallbacks (selección de carpeta y listado). Asegúrate de que Excel tiene permisos para controlar el Finder si macOS solicita autorización (Preferencias del Sistema → Seguridad y Privacidad → Privacidad → Automatización / Files and Folders).

Toggle de logging
- Variable: `Const ENABLE_LOG As Boolean = False` (línea superior del módulo).
- Si la pones a `True`, el macro intentará crear/actualizar `export_log.txt` en la carpeta seleccionada. Si falla, ofrece crear el log en el Escritorio.

Depuración rápida
- Si algo falla, ejecuta la macro sobre una carpeta local pequeña con 2-3 ficheros y pega aquí las líneas del `export_log.txt` (si se crea) o el `Err.Number` y `Err.Description` que aparezcan en pantalla.

Contacto
- Código mantenido en este repositorio. Si quieres, puedo crear una rama con la versión con logging activado y reintentos para que la pruebes sin afectar la rama `principal`.

---
Fecha de generación: 2025-10-28
