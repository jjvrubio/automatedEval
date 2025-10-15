# Evaluador TFM Integrado Ultraestricto

## 📋 Descripción General

El **Evaluador TFM Integrado Ultraestricto** es un sistema avanzado de evaluación automatizada de Trabajos Final de Máster (TFM) que implementa un **marco epistemológico riguroso** y un **sistema adaptativo universal** para generar evaluaciones expertas y preguntas analíticas de alto nivel académico.

### 🎯 Características Principales

- **🔄 Sistema Adaptativo Universal**: Detección automática de formatos MUDPE/MUGPTD
- **🎯 Detección automática de rúbricas** mediante etiquetas Finder de macOS
- **⚡ Evaluación ultraestricta** con extracción inteligente de niveles reales
- **🧠 Generación de preguntas expertas** basadas en análisis metodológico integral
- **📱 Soporte multiplataforma**: PDF y DOCX con marcas de página precisas
- **☁️ Integración con OneDrive** (hidratación automática de archivos)
- **📊 Exportación triple**: CSV, Markdown y JSON
- **🔍 Sistema de evidencias citables** con referencias exactas de página
- **🚫 Exclusión inteligente** de criterios de presentación oral

### 🆕 Nuevas Funcionalidades (v3.0)

- **🔄 Detección automática de formato de rúbrica** (MUDPE vs MUGPTD)
- **📊 Extracción inteligente de niveles reales** del contenido de la rúbrica
- **🎯 Prompt optimizado** para evaluaciones más precisas
- **🧹 Sistema depurado** sin funciones duplicadas
- **⚡ Generación mejorada de archivos MD/JSON**
- **🔍 Validación robusta** de niveles según formato detectado

## 📁 Estructura del Proyecto

```
/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/
├── Grading/UNIR Grading/
│   └── Evaluador_TFM_Integrado_ultraestricto.py   # Script principal
└── TFM_Evaluator_Prompt_Package/
    ├── plantillas_preguntas.yaml                  # Marco epistemológico
    ├── rubrica MUDPE.xlsx                         # Rúbrica MUDPE
    ├── rubrica MUGPTD.xlsx                        # Rúbrica MUGPTD
    └── Ultraestricto.md                          # Instrucciones de evaluación
```

## 🛠️ Requisitos del Sistema

### Dependencias Python
```bash
pip install pdfplumber python-docx pandas openai>=1.0 pyobjc pyyaml
```

### Variables de Entorno
```bash
export OPENAI_API_KEY="tu_clave_api_openai"
# o alternativamente:
export MI_CLAVE_API_OPENAI="tu_clave_api_openai"
```

### Requisitos del Sistema
- **macOS** (requerido para AppKit y etiquetas Finder)
- **Python 3.8+**
- **OpenAI API** con acceso a GPT-4

## 🚀 Uso del Sistema

### Ejecución Básica
```bash
cd "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/Grading/UNIR Grading/"
python Evaluador_TFM_Integrado_ultraestricto.py
```

### Flujo de Trabajo

1. **Selección de TFM**: Se abre un diálogo de macOS para seleccionar el archivo PDF/DOCX
2. **Detección de rúbrica**: 
   - Automática vía etiquetas Finder (`MUDPE` o `MUGPTD`)
   - Manual si no hay etiquetas
3. **Hidratación OneDrive**: Descarga automática si el archivo está "solo en la nube"
4. **Evaluación**: Análisis criterio por criterio con IA
5. **Generación de preguntas**: Preguntas expertas basadas en análisis epistemológico
6. **Exportación**: Archivos CSV y MD en la carpeta del TFM

## 📊 Sistema de Rúbricas

### Rúbricas Soportadas

| Etiqueta Finder | Archivo | Criterios | Exclusiones | Formato de Niveles |
|----------------|---------|-----------|-------------|-------------------|
| `MUDPE` | `rubrica MUDPE.xlsx` | 13 criterios | 10-13 (presentación) | Nivel 1-4 |
| `MUGPTD` | `rubrica MUGPTD.xlsx` | 8 criterios | 7-8 (presentación) | Suspenso/Aprobado/Notable/Sobresaliente |

### 🔄 Sistema Adaptativo de Detección

El sistema **detecta automáticamente** el formato de la rúbrica:

#### Formato MUDPE
- **Niveles detectados**: "Nivel 1", "Nivel 2", "Nivel 3", "Nivel 4"
- **Problemáticos**: Nivel 1 (crítico)
- **Mejorables**: Nivel 1-2 (requieren mejoras)
- **Satisfactorios**: Nivel 3-4

#### Formato MUGPTD  
- **Niveles detectados**: "Suspenso (0-4)", "Aprobado (5-6)", "Notable (7-8)", "Sobresaliente (9-10)"
- **Problemáticos**: Suspenso (crítico)
- **Mejorables**: Suspenso y Aprobado (requieren mejoras)
- **Satisfactorios**: Notable y Sobresaliente

### 🎯 Extracción Inteligente de Niveles

El sistema **no usa nombres de columnas** sino que **extrae niveles reales** del contenido:

```python
# Antes (problemático): ['N1', 'N2', 'N3', 'N4']
# Ahora (correcto): ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4']
```

Esto garantiza que el modelo de IA use los **niveles exactos** de la rúbrica.

## 🧠 Marco Epistemológico

El sistema implementa un marco epistemológico avanzado para la generación de preguntas expertas:

### Análisis por Secciones

#### 📝 Resumen
- Integración justificación teórica y económica
- Derivación lógica de objetivos
- Coherencia metodológica
- Cierre objetivo-resultado

#### 🎯 Justificación
- Magnitud cuantitativa y cualitativa del problema
- Árbol de problemas (causas primarias/secundarias)
- Estado del arte y benchmarking
- Transformación problema-objetivo

#### 🎯 Objetivos
- Cadena de pensamiento: justificación → objetivos → metodología → conclusiones
- Verificación de alineación problema-objetivo
- Coherencia metodológica
- Cierre del círculo en conclusiones

#### 📈 Análisis Estratégico
- Secuencia metodológica: PESTEL → Porter → Competidores → MEFE → DAFO
- Aplicación coherente entre metodologías
- Integración análisis externo-interno
- Rigor en aplicación de herramientas

### Patrones Problemáticos Detectados

1. **Desarticulación Lógica**: Falta de conexión entre secciones
2. **Secuencia Metodológica Incorrecta**: Aplicación desordenada de herramientas
3. **Superficialidad en Herramientas**: Aplicación formal sin rigor
4. **Incongruencia Cuantitativa**: Datos no sustentados

## 📋 Salidas del Sistema

### Archivo CSV (`evaluacion_tfm_resultado.csv`)
```csv
criterio,nivel,justificacion,areas_mejora,evidencias
"Claridad objetivos","N3","Objetivos bien definidos","Mejorar especificidad","[{'frase': '...', 'pagina': 'P5'}]"
```

### Archivo Markdown (`evaluacion_tfm_informe.md`)
```markdown
# Informe de Evaluación TFM

## Criterio 1: Claridad de objetivos
- **Nivel alcanzado**: N3
- **Justificación**: Los objetivos están claramente definidos...
- **Evidencias**:
  - Fragmento específico (Página: P5)
- **Áreas de mejora**: Mejorar la especificidad...

## Preguntas para la Defensa

1. **Ruptura en la cadena de pensamiento**: Los objetivos formulados...
```

## ⚙️ Configuración Avanzada

### Parámetros del Modelo
```python
MODELO_POR_DEFECTO = "gpt-4o-mini"
TEMPERATURA_POR_DEFECTO = 0.0
```

### Rutas de Configuración
```python
RUBRICAS_POR_ETIQUETA = {
    "MUDPE": "ruta/a/rubrica_MUDPE.xlsx",
    "MUGPTD": "ruta/a/rubrica_MUGPTD.xlsx",
}

RUTA_INSTRUCCIONES_MD = "ruta/a/Ultraestricto.md"
```

## 🔧 Funciones Principales

### `main()` - Función Principal
Coordina todo el flujo de evaluación desde la selección del archivo hasta la exportación.

### `evaluar_tfm_completo()` - Motor de Evaluación
Ejecuta la evaluación criterio por criterio usando OpenAI API con **detección automática de niveles reales**.

### `detectar_formato_rubrica()` - 🆕 Sistema Adaptativo
**Nueva función** que detecta automáticamente el formato de la rúbrica (MUDPE vs MUGPTD) analizando el contenido real.

### `generar_preguntas_dinamicas()` - Generador de Preguntas Expertas
Implementa el marco epistemológico para generar preguntas analíticas de alto nivel con **adaptación automática al formato**.

### `es_nivel_problematico()` / `nivel_es_mejorable()` - 🆕 Evaluación Adaptativa
**Nuevas funciones** que evalúan niveles según el formato específico de la rúbrica detectada.

### `seleccionar_rubrica_por_etiquetas()` - Detección Automática
Lee etiquetas Finder y selecciona la rúbrica apropiada.

### `leer_tfm()` - Extractor de Texto
Procesa archivos PDF/DOCX y añade marcas de página para evidencias.

### `construir_prompt_v2()` - 🆕 Prompt Optimizado
**Prompt mejorado** que especifica claramente los niveles válidos y mejora la precisión de las evaluaciones.

## 🆕 Mejoras Técnicas Implementadas (v3.0)

### ✅ Correcciones Críticas
- **Eliminación de funciones duplicadas** que causaban errores
- **Extracción correcta de niveles reales** en lugar de nombres de columnas
- **Validación robusta** usando `niveles_reales` detectados
- **Prompt restructurado** para mayor claridad y precisión

### ✅ Sistema Adaptativo Universal  
- **Detección automática** del formato MUDPE/MUGPTD
- **Evaluación adaptativa** de niveles problemáticos/mejorables
- **Generación contextual** de preguntas según el formato
- **Compatibilidad total** con ambos programas académicos

### ✅ Mejoras de Robustez
- **Eliminación de código duplicado** y limpieza arquitectural
- **Manejo mejorado de errores** en evaluación y exportación
- **Logs detallados** para debugging y seguimiento
- **Exportación garantizada** de archivos MD/JSON

## 🎓 Ejemplos de Preguntas Generadas

### Pregunta Epistemológica Típica
```
**Ruptura en la cadena de pensamiento**: Los objetivos formulados no derivan 
lógicamente de la problemática planteada, y la metodología aplicada no persigue 
coherentemente dichos objetivos. ¿Cómo se justifica esta desarticulación y qué 
evidencia sustenta que la metodología es la más adecuada para alcanzar los 
objetivos planteados?
```

### Pregunta sobre Secuencia Metodológica
```
**Alteración de secuencia analítica**: El análisis estratégico no sigue la 
secuencia metodológica prescrita (PESTEL → Porter → Competidores → MEFE → DAFO). 
¿Qué fundamentación epistemológica justifica esta variación y cómo se garantiza 
la validez del diagnóstico estratégico resultante?
```

## 🐛 Resolución de Problemas

### Errores Comunes

#### Error: "No se encontró la rúbrica"
- **Causa**: Archivo de rúbrica no existe
- **Solución**: Verificar rutas en `RUBRICAS_POR_ETIQUETA`

#### Error: "OpenAI API key not found"
- **Causa**: Variable de entorno no configurada
- **Solución**: `export OPENAI_API_KEY="tu_clave"`

#### Error: "No se pudo leer el archivo"
- **Causa**: Archivo OneDrive no hidratado
- **Solución**: El sistema intenta hidratar automáticamente

#### Error: "identificar_patrones_problemas() takes 3 positional arguments but 4 were given"
- **Causa**: Funciones duplicadas (resuelto en v3.0)
- **Solución**: ✅ **Solucionado** - funciones duplicadas eliminadas

#### Error: "Nivel 'N1' no encontrado en rúbrica"
- **Causa**: Uso de nombres de columnas en lugar de niveles reales (resuelto en v3.0)
- **Solución**: ✅ **Solucionado** - extracción inteligente de niveles implementada

### 🆕 Diagnóstico Mejorado (v3.0)

El sistema ahora incluye **logs detallados** para facilitar el debugging:

```
2025-10-15 19:21:53,698 [INFO] Rúbrica detectada: MUDPE (13 criterios)
2025-10-15 19:21:53,698 [INFO] Formato de rúbrica detectado: MUDPE
2025-10-15 19:21:53,698 [INFO] Niveles reales detectados: ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4']
```

### Logs del Sistema
Los logs se guardan en `evaluador_tfm_integrado.log` en la carpeta del TFM para debugging.

## 📈 Mejoras Futuras

- [ ] Soporte para Windows/Linux
- [ ] Integración con más LLMs (Claude, Gemini)  
- [ ] Dashboard web para múltiples evaluaciones
- [ ] Análisis estadístico comparativo
- [ ] Exportación a LaTeX/Word
- [ ] Validación cruzada entre evaluadores IA
- [ ] Sistema de plantillas de preguntas personalizable

## 📝 Registro de Cambios

### v3.0 (Octubre 2025) - Sistema Adaptativo Universal
- ✅ **Sistema adaptativo automático** MUDPE/MUGPTD
- ✅ **Extracción inteligente de niveles reales** de rúbricas
- ✅ **Eliminación de funciones duplicadas** y depuración del código
- ✅ **Prompt optimizado** para evaluaciones más precisas
- ✅ **Validación robusta** según formato detectado
- ✅ **Logs mejorados** para debugging
- ✅ **Generación garantizada** de archivos MD/JSON

### v2.0 (2025) - Marco Epistemológico
- Implementación del framework epistemológico para preguntas expertas
- Sistema de análisis metodológico integral
- Generación de preguntas contextualizadas

### v1.0 (2024) - Versión Base
- Evaluación básica con rúbricas fijas
- Exportación CSV y Markdown
- Integración con OpenAI

---

**Versión**: 3.0 - Sistema Adaptativo Universal  
**Última actualización**: 15 de Octubre 2025  
**Autor**: JJVR  
**Contacto**: Para soporte, crear issue en el repositorio  

> 🎉 **¡Sistema completamente funcional y depurado!** El evaluador TFM ahora funciona de manera robusta con detección automática de formatos y evaluaciones precisas.