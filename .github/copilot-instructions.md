# Guía para Copilot en este repositorio

## Propósito del repositorio
Sistema automatizado para evaluación académica de TFMs y gestión de contenido. Incluye validadores de normas APA, integraciones con APIs de IA (OpenAI/Anthropic), y herramientas específicas para macOS.

## Arquitectura del sistema

### Flujo principal de evaluación (`01_Educativa/0101_UNIR/AutomatedEval/`)
1. **Selección de documentos**: Selector nativo `NSOpenPanel` (Cocoa/AppKit) para UI consistente en macOS
2. **Extracción de contenido**: `pdfplumber` para PDF, `python-docx` para DOCX, `Quartz.PDFDocument` en algunos módulos
3. **Evaluación con IA**: OpenAI API (`gpt-4`) con prompts estructurados que siguen criterios UNIR
4. **Generación de informes**: Markdown y JSON como formatos de salida estándar

### Componentes modulares
- **`APA Report/`**: Sistema independiente de validación bibliográfica (ver [README](01_Educativa/0101_UNIR/AutomatedEval/APA Report/README.md))
  - Extrae referencias de documentos académicos
  - Valida contra patrones APA 7 con regex
  - Genera informes detallados en español/inglés
- **`function_call_agent/`**: Arquitectura de extracción modular
  - `functions/extractors.py`: Factory pattern para PDF/DOCX con type hints `Literal`
  - `functions/function_schemas.json`: Esquemas para function calling de OpenAI
- **`Completar Acta y Rúbrica/`**: Automatización web con Selenium
  - Variantes para Safari, Edge (drivers específicos)
  - Relleno automático de formularios UNIR desde Excel
- **`Grading/`**: Evaluación por palabras clave y criterios estructurados
  - `UNIR Grading/`: Evaluador refactorizado con YAML config + logger estructurado
  - `ESBS Grading/`: Variante para criterios ESBS
  - `palabras clave/`: Evaluación por keywords con extracción de fragmentos representativos

### Gestión de entornos
- **`venv_arm64/`**: Python 3.13 para Apple Silicon (`/opt/homebrew/opt/python@3.13`)
- **`venv_intel/`**: Python para arquitectura Intel
- **Razón**: Compatibilidades diferentes de `pyobjc` y dependencias nativas

## Convenciones críticas

### Patrón de selección de archivos (usado en 15+ scripts)
```python
from Cocoa import NSOpenPanel  # o AppKit.NSOpenPanel
panel = NSOpenPanel.openPanel()
panel.setCanChooseFiles_(True)
panel.setAllowedFileTypes_(["pdf", "docx"])
if panel.runModal() == Cocoa.NSModalResponseOK:
    return panel.URLs()[0].path()
```
- **No uses** `tkinter.filedialog` - rompe consistencia de UI
- **Siempre hidrata** archivos OneDrive antes de leer (ver patrón en `leer etiqueta finder.py`)

### Manejo de OneDrive
```python
def _is_onedrive_path(p: Path) -> bool:
    sp = str(p)
    return ("OneDrive" in sp) or ("/Library/CloudStorage/" in sp and "OneDrive-" in sp)
```
- **No usar** `Path.resolve()` antes de `exists()` en rutas OneDrive (causa fallos en APFS)
- Los archivos pueden estar "deshidratados" (solo marcadores) - verificar con `mdls` o `xattr`

### Integración con APIs de IA
- **OpenAI**: Usa `openai.api_key` desde `.env` (`MI_CLAVE_API_OPENAI`)
- **Gemini**: Usa `genai.configure(api_key=...)` desde `.env` (`MI_CLAVE_API_GEMINI`)
- **SerpAPI**: Para búsquedas (requiere `MI_CLAVE_API_SERPAPI`)
- **Prompts estructurados**: Sistema de evaluación sigue formato de criterios UNIR
```python
prompt = f"""Eres un evaluador académico experto siguiendo los criterios de UNIR. 
Evalúa el siguiente trabajo según el criterio:

Criterio: {criterio}
Trabajo: {descripcion_tfm}
"""
```
- **Output esperado**: Puntuación + justificación detallada
- **Nota**: OpenAI para evaluación académica (temperatura variable), Gemini para OSINT (temperatura 0.1 precisión)

### Gestión de dependencias
- Hay 3 archivos de requirements:
  - `requirements.txt`: Dependencias generales
  - `modulos-arm.txt` / `modulos-intel.txt`: Específicos por arquitectura
  - `01_Educativa/0101_UNIR/AutomatedEval/APA Report/requirements_referencias.txt`: Módulo independiente

## Tareas de desarrollo comunes

### Activar entorno correcto
```bash
# Detectar arquitectura
arch  # "arm64" o "i386"

# Activar
source venv_arm64/bin/activate  # o venv_intel
```

### Ejecutar evaluación de TFM
```bash
cd 01_Educativa/0101_UNIR/AutomatedEval
python autoEval.py  # Abre selector gráfico para rúbrica y TFM
```

### Validar referencias APA
```bash
cd "01_Educativa/0101_UNIR/AutomatedEval/APA Report"
python referencias_validator.py --interactivo
```

### Probar scripts de Selenium
Scripts en `Completar Acta y Rúbrica/` esperan:
- WebDriver correspondiente instalado (`chromedriver`, `safaridriver`, etc.)
- URL del formulario UNIR proporcionada vía diálogo AppleScript

## Flujos de datos principales

### TFM Evaluation Pipeline
```
Usuario selecciona TFM (NSOpenPanel) 
  → Extracción (pdfplumber/python-docx) 
  → Chunking por criterio 
  → OpenAI API (gpt-4) 
  → Rúbrica evaluadora 
  → Informe JSON/Markdown
```

### APA Report Validation
```
PDF/DOCX (selector NSOpenPanel)
  → Extracción de referencias (regex patterns APA 7)
  → Validación contra patrones
  → Informe JSON/Markdown (español/inglés)
```

### OSINT Pipeline
```
Consulta usuario (español)
  → SerpAPI (búsqueda Google España)
  → Scraping + parsing
  → Gemini 1.5 Pro (análisis financiero/técnico)
  → Síntesis con prompts estructurados
```

## Patrones arquitectónicos

### Factory Pattern (Extractores)
El módulo `function_call_agent/functions/extractors.py` usa `Literal` type hints para dispatch dinámico:
```python
def extract_text(file_path: str, source_type: Literal["pdf", "docx"]) -> str:
    # Dispatch basado en tipo
```
Mantén este patrón para nuevos formatos (XLSX, XML, etc.)

### Function Calling (OpenAI)
Schemas en `function_schemas.json` definen interfaz para function calling. Al agregar nuevas funciones:
1. Crear función en `functions/`
2. Agregar schema en `function_schemas.json`
3. Actualizar consumidor en script principal

## Patrones anti-pattern
- ❌ **No** usar `input()` para entrada de usuario - usa `NSOpenPanel` o diálogos AppleScript
- ❌ **No** asumir que archivos existen sin verificar OneDrive
- ❌ **No** mezclar librerías de extracción PDF (`PyPDF2` vs `pdfplumber`) - preferir `pdfplumber`
- ❌ **No** hardcodear rutas - los scripts deben funcionar desde cualquier ubicación
- ❌ **No** usar `resolve()` en rutas OneDrive antes de verificar existencia
- ❌ **No** mezclar APIs de IA - mantener consistencia: OpenAI para evaluación, Gemini para OSINT

## Testing y validación

### Tests de variabilidad (Grading/UNIR Grading/)
```bash
python test_variabilidad_evaluador.py
```
Verifica:
- Variabilidad por temperatura
- Extracción consistente de elementos únicos
- Hash de documento reproducible
- Determinismo con seed

### Logging y debugging
- `function_call_agent/utils/logger.py`: Debug logs con timestamps
- Habilitar: `debug_log(message="...", output_dir="logs/", title="evaluacion_1")`
- Logs se guardan en `logs/` para análisis post-ejecución

## Clave de referencia rápida

| Tarea | Ubicación | Patrón |
|-------|-----------|--------|
| Agregar criterio UNIR | `01_Educativa/0101_UNIR/AutomatedEval/Grading/UNIR Grading/` | YAML config + prompt |
| Nueva validación APA | `01_Educativa/0101_UNIR/AutomatedEval/APA Report/` | Regex pattern + test |
| Script macOS nativo | `03_Personal/Automatizaciones/mac_automation/scripts_de_apoyo/` | NSOpenPanel + Cocoa |
| Pipeline Pandoc | `02_Profesional/0201_Convercus/Automatizaciones/publicando/` | YAML profile + Lua filter |
| Busca OSINT | `02_Profesional/0201_Convercus/Automatizaciones/osint_ccus/osint-prospects.py` | SerpAPI → Gemini |

## Estado del proyecto (commits recientes)

Ver `01_Educativa/0101_UNIR/AutomatedEval/bitácora.md` para historial de decisiones arquitectónicas y cambios en proceso.

## Herramientas adicionales

### `02_Profesional/0201_Convercus/Automatizaciones/osint_ccus/`: Herramienta de búsqueda e inteligencia
- **Propósito**: Búsqueda OSINT integrada con APIs de IA (Gemini + SerpAPI)
- **Arquitectura**: 3 fases: búsqueda → análisis → síntesis
- **Configuración**: Requiere `.env` con `MI_CLAVE_API_GEMINI` y `MI_CLAVE_API_SERPAPI`
- **Entrada**: Consultas en español con filtros geográficos (España por defecto)
- **Salida**: Análisis financiero/técnico con temperatura baja (0.1) para precisión

### `02_Profesional/0201_Convercus/Automatizaciones/publicando/`: Pipeline Pandoc
- Convierte Markdown Obsidian → HTML (Substack) / DOCX (LinkedIn)
- Scripts bash: `pandoc-obsidian-wrapper.sh`, `sync_from_icloud.sh`
- Filtros Lua: `toc-policy.lua`, `toc-policy-bis.lua` (gestión de tablas de contenido)
- Archivos YAML de configuración por plataforma (`linkedin.yaml`, etc.)
- Subdirectorios `Posting/` y `TFE/` para variantes específicas

### `03_Personal/Automatizaciones/mac_automation/scripts_de_apoyo/`: Utilidades macOS
- **AppleScript**: `export_contacts_to_csv.applescript`, `export_streak_mail.applescript` (integración Contactos/Mail)
- **Python**: Limpieza de JSON (`clean_streak_notes.py`, `filter_notes_by_prefix.py`, `fix_and_filter.py`)
- **Shell**: `remove_office_languages.zsh` (limpieza bundles Office), `comparar carpetas de Metis.sh`
- **Lectura OneDrive**: `leer etiqueta finder.py` contiene patrón de hidratación de archivos

### `03_Personal/Articulos/METIS_Growth/`: Análisis de métricas
- Scripts Python con pandas y R para análisis estadístico
- Generación automática de rúbricas de evaluación estructuradas
- Templates para planes de acción correctiva (L1-L2, P1-P6 phases)

## Referencias clave
- [APA Report README](01_Educativa/0101_UNIR/AutomatedEval/APA Report/README.md) - Documentación del validador independiente
- [Scripts de apoyo README](03_Personal/Automatizaciones/mac_automation/scripts_de_apoyo/README.md) - Guía de utilidades macOS
- `01_Educativa/0101_UNIR/AutomatedEval/bitácora.md` - Historial de desarrollo y decisiones arquitectónicas
