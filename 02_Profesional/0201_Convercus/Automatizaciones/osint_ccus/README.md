# Módulo OSINT: El Analista Fantasma

Sistema automatizado de inteligencia competitiva y prospección comercial basado en la arquitectura RAG (Retrieval-Augmented Generation).

## 🎯 Propósito

Construir un "Notebook Inteligente" usando la API de Gemini 1.5 Pro para automatizar la investigación OSINT, análisis de oportunidades comerciales y generación de informes ejecutivos.

## 🏗️ Arquitectura

El sistema implementa 4 módulos especializados:

### 1. El Cazador (`modules/hunter.py`)
- **Función**: Búsqueda automática de fuentes relevantes
- **API**: SerpAPI (Google Search)
- **Output**: Lista de URLs filtradas por relevancia

### 2. El Recolector (`modules/collector.py`)
- **Función**: Extracción de contenido desde URLs
- **Capacidades**: 
  - Scraping HTML (BeautifulSoup)
  - Extracción PDF (pdfplumber)
  - Rate limiting automático
- **Output**: Texto limpio listo para análisis

### 3. El Cerebro (`modules/brain.py`)
- **Función**: Análisis secuencial con LLM
- **Modelo**: Gemini 1.5 Pro (2M tokens de contexto)
- **Características**:
  - Carga de prompts desde archivos Markdown
  - Análisis multi-fase con contexto acumulativo
  - Temperatura baja (0.1) para precisión analítica

### 4. El Reportero (`modules/reporter.py`)
- **Función**: Generación de informes estructurados
- **Formatos**: Markdown (con front matter YAML), JSON
- **Características**: 
  - Templates configurables
  - Índices automáticos
  - Exportación futura a DOCX/PowerPoint

## 📁 Estructura de Directorios

```
osint_ccus/
├── main.py                    # Orquestador principal
├── modules/
│   ├── hunter.py             # Módulo de búsqueda
│   ├── collector.py          # Extractor de contenido
│   ├── brain.py              # Motor de análisis con Gemini
│   └── reporter.py           # Generador de reportes
├── prompts/
│   ├── 01_system.md          # Contexto y rol del analista
│   ├── 02_trigger.md         # Prompt de búsqueda inicial
│   ├── 03_analysis.md        # Diagnóstico estratégico
│   ├── 04_synthesis.md       # Construcción de narrativa
│   └── 05_report.md          # Template de reporte final
├── reports/                  # Salida de análisis
├── .env                      # Variables de entorno (no versionado)
└── README.md                 # Este archivo
```

## ⚙️ Configuración

### 1. Variables de Entorno

Crear archivo `.env` en el directorio `osint_ccus/`:

```env
MI_CLAVE_API_SERPAPI=tu_clave_serpapi
MI_CLAVE_API_GEMINI=tu_clave_gemini
```

### 2. Dependencias

Instalar paquetes necesarios:

```bash
cd /Users/juanjo/Documents/Personal/JJVR/automatizaciones
source venv_arm64/bin/activate  # o venv_intel según tu arquitectura

pip install serpapi google-generativeai pdfplumber requests beautifulsoup4 python-dotenv
```

### 3. Verificar Estructura

```bash
cd osint_ccus
python -m modules.hunter    # Test del cazador
python -m modules.collector # Test del recolector
python -m modules.brain     # Test del cerebro
```

## 🚀 Uso

### Ejecución del Sistema

```bash
cd osint_ccus
python osint-prospects.py
```

El script presenta una interfaz interactiva con diálogos nativos de macOS.

### Flujo de Ejecución

1. **Búsqueda**: Genera queries estratégicas y busca fuentes (SerpAPI)
2. **Recolección**: Descarga y extrae contenido (HTML + PDF)
3. **Análisis**: Ejecuta 5 prompts secuenciales con Gemini:
   - System (contexto)
   - Trigger (extracción de datos)
   - Analysis (scoring + SWOT)
   - Synthesis (narrativa comercial)
   - Report (documento final)
4. **Reporte**: Genera Markdown estructurado en `reports/`

## 📊 Output Esperado
El sistema guía al usuario a través de diálogos nativos de macOS:

1. **Carga de Configuración**: Lee system prompt y escenarios desde `Instrucción para Gems.md`
2. **Selección de Escenario**: Dropdown con 4 opciones (Expansión, Consolidación, M&A, Turnaround)
3. **Datos de Empresa**: Campos para nombre de empresa y contexto adicional
4. **Confirmación**: Diálogo de confirmación antes de consumir créditos API
5. **Ejecución del Pipeline**:
   - Búsqueda de fuentes (SerpAPI)
   - Extracción de contenido (HTML + PDF)
   - Análisis multi-fase con Gemini (5 prompts secuenciales)
   - Generación de reporte Markdown
6. **Finalización**: Diálogo con ruta al reporte generado
- **Fuentes**: URLs consultadas con descripción

Archivo típico: `reporte_Inditex_20260111_153045.md`

## 🔧 Personalización

### Modificar Prompts

Editar archivos en `prompts/`:
- Ajustar scoring de fit estratégico
- Cambiar framework analítico (SWOT → Porter's 5 Forces)
- Personalizar templates de reporte

### Ajustar Búsqueda

En `main.py`, modificar `keywords`:

```python
keywords = [
    "innovación tecnológica",
    "funding ronda inversión",
    "asociaciones estratégicas"
]
```

### Extender Capacidades

- **Nuevos extractores**: Implementar `_extract_xlsx()` en `collector.py`
- **Análisis adicional**: Agregar `06_competitive.md` en `prompts/`
- **Export avanzado**: Implementar `generate_pptx()` en `reporter.py`

## 📈 Comparación con NotebookLM

| Característica | NotebookLM (Web) | Analista Fantasma |
|----------------|------------------|-------------------|
| **Interfaz** | GUI arrastrar/soltar | CLI automatizado |
| **Fuentes** | Manual (upload) | Automático (búsqueda) |
| **Contexto** | ~500K tokens | 2M tokens (Gemini 1.5 Pro) |
| **Análisis** | Single-pass | Multi-fase secuencial |
| **Prompts** | Predefinidos | Personalizables (Markdown) |
| **Output** | Chat interactivo | Markdown ejecutivo |
| **Integración** | Ninguna | Pipeline programático |

## 🛠️ Solución de Problemas

### Error: "Faltan claves en .env"
- Verificar que `.env` existe en `osint_ccus/`
- Confirmar nombres de variables: `MI_CLAVE_API_SERPAPI`, `MI_CLAVE_API_GEMINI`

### Error: "pdf_support_missing"
- Instalar: `pip install pdfplumber`

### Pocas fuentes encontradas
- Ajustar `config.max_sources` en `main.py`
- Modificar queries en `keywords`

### Rate limiting de APIs
- Aumentar `scrape_delay` en `Config`
- Considerar implementar retry logic en `hunter.py`

## 📚 Referencias

- [Gemini API Docs](https://ai.google.dev/docs)
- [SerpAPI Python Client](https://serpapi.com/integrations/python)
- [pdfplumber Documentation](https://github.com/jsvine/pdfplumber)

## 🔄 Próximas Mejoras

- [ ] Export a PowerPoint (`python-pptx`)
- [ ] Análisis de sentimiento en redes sociales
- [ ] Integración con LinkedIn API para perfiles
- [ ] Cache de búsquedas para evitar re-procesamiento
- [ ] UI web con Flask/Streamlit para no-técnicos

---

**Autor**: Sistema Automatizado  
**Última actualización**: 2026-01-11  
**Versión**: 1.0
