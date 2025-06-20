# Evaluador Estricto TFM (UNIR)

## Descripción General
Este script automatiza la evaluación ultraestricta de Trabajos Fin de Máster (TFM) en formato PDF o DOCX, utilizando la API de OpenAI y una rúbrica configurable en CSV. El resultado es un informe estructurado en Markdown y un archivo CSV con los resultados.

---

## Manual de Usuario

### Requisitos previos
- macOS con Python 3.8+ instalado
- Acceso a la API de OpenAI (clave en `.env`)
- Dependencias instaladas: `openai`, `pdfplumber`, `docx`, `python-dotenv`, `pandas`, `pyobjc`
- Rúbrica en formato CSV y, opcionalmente, instrucciones en Markdown

### Instalación de dependencias
```sh
pip install openai pdfplumber python-docx python-dotenv pandas pyobjc
```

### Configuración
1. Crea un archivo `.env` en la misma carpeta que el script con tu clave de OpenAI:
   ```
   MI_CLAVE_API_OPENAI=sk-...
   ```
2. Asegúrate de tener la rúbrica CSV y, si lo deseas, el archivo de instrucciones Markdown en la ruta indicada en el script.

### Ejecución
1. Ejecuta el script desde la terminal:
   ```sh
   pythonw 'Evaluador estricto TFM.py'
   ```
2. Selecciona el archivo TFM (PDF o DOCX) cuando aparezca el selector.
3. El script evaluará el TFM y generará dos archivos en la misma carpeta:
   - `evaluacion_tfm_resultado.csv`: Resultados tabulares
   - `evaluacion_tfm_informe.md`: Informe detallado en Markdown

### Notas de uso
- La primera ejecución tras reiniciar el Mac puede tardar en mostrar el selector de archivos.
- El script funciona tanto con PDF como con DOCX.
- El log de la ejecución se guarda en `evaluador_tfm.log`.

---

## Documentación Técnica

### Estructura del Script
- **configurar_openai()**: Carga la clave API desde `.env` y configura el cliente OpenAI.
- **configurar_logger()**: Inicializa el logger para consola y archivo.
- **seleccionar_archivo()**: Muestra el selector de archivos usando AppKit (NSOpenPanel).
- **cargar_rubrica()**: Lee la rúbrica desde CSV o Excel.
- **cargar_instrucciones_md_opcional()**: Lee instrucciones adicionales desde un archivo Markdown.
- **leer_tfm()**: Extrae el texto del TFM desde PDF o DOCX.
- **evaluar_criterio()**: Llama a OpenAI para evaluar cada criterio de la rúbrica.
- **evaluar_tfm_completo()**: Itera sobre todos los criterios y compila los resultados.
- **exportar_resultados()**: Exporta los resultados a CSV y Markdown.
- **main()**: Orquesta todo el flujo.

### Variables y rutas clave
- **.env**: Clave API de OpenAI
- **ruta_rubrica**: Ruta absoluta al archivo de rúbrica CSV
- **ruta_instrucciones**: Ruta opcional al archivo de instrucciones Markdown

### Dependencias
- openai
- pdfplumber
- python-docx
- python-dotenv
- pandas
- pyobjc (AppKit)

### Salidas
- `evaluacion_tfm_resultado.csv`: Resultados tabulares por criterio
- `evaluacion_tfm_informe.md`: Informe detallado en Markdown
- `evaluador_tfm.log`: Log de la ejecución

### Personalización
- Puedes modificar la rúbrica CSV para adaptarla a otros criterios.
- El prompt y las instrucciones pueden personalizarse en el archivo Markdown de instrucciones.

---

## Solución de problemas
- Si el selector de archivos tarda en aparecer, consulta la sección de optimización en la documentación.
- Si hay errores de importación, revisa que todas las dependencias estén instaladas en el entorno correcto.
- Si la clave de OpenAI no se encuentra, revisa el archivo `.env`.

---

## Contacto y soporte
Para dudas o mejoras, contactar con el autor del script o el responsable de automatizaciones.
