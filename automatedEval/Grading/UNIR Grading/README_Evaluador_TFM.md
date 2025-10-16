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

### 🆕 Nuevas Funcionalidades (v4.0)

- **📄 Integración de extractos textuales** en preguntas (elimina consulta de páginas)
- **🔍 Búsqueda inteligente de datos específicos** (números, porcentajes, términos técnicos)
- **🎯 Preguntas autocontenidas** con evidencia textual integrada
- **🧠 Análisis crítico profundo** mediante IA para detectar inconsistencias
- **📊 Extracción ampliada de datos específicos** (financieros, metodológicos, técnicos)
- **⚡ Sistema de priorización de extractos** (datos numéricos → términos técnicos → contexto general)

### ✅ Funcionalidades v3.0 Consolidadas

- **🔄 Detección automática de formato de rúbrica** (MUDPE vs MUGPTD)
- **📊 Extracción inteligente de niveles reales** del contenido de la rúbrica
- **🎯 Prompt optimizado** para evaluaciones más precisas
- **🧹 Sistema depurado** sin funciones duplicadas o de respaldo
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

## 📄 Sistema de Integración de Extractos Textuales (v4.0)

### 🎯 Preguntas Autocontenidas

El sistema **genera preguntas que incluyen fragmentos específicos del documento** eliminando la necesidad de consultar páginas durante la evaluación del tribunal:

#### ✅ Antes (requería consultar páginas)

```text
¿Cómo justifica la metodología utilizada en el análisis financiero?
```

#### 🚀 Ahora (autocontenida con extractos)

```text
El documento presenta *ROI del 23.5% y VAN de €2.4M calculado con WACC del 8.2%*, 
pero posteriormente menciona que *el análisis de sensibilidad no fue aplicado debido 
a limitaciones de tiempo*. Dado que el documento afirma usar *metodología Monte Carlo 
para modelar incertidumbre*, ¿por qué estos cálculos críticos no incorporan 
variabilidad en las tasas de descuento?
```

### 🔍 Sistema de Búsqueda Inteligente de Extractos

#### Prioridad 1: Datos Numéricos Específicos

- **Porcentajes**: 32.88%, 29.97%, 15.6%
- **Valores monetarios**: €2.4M, $150,000
- **Métricas**: ROI, VAN, TIR, WACC, CTE
- **Indicadores de rendimiento**: ratios, coeficientes

#### Prioridad 2: Términos Técnicos y Metodológicos

- **Metodologías**: LEAN, Six Sigma, Monte Carlo, PESTEL
- **Herramientas**: Canvas, DAFO, Porter, Balanced Scorecard  
- **Conceptos teóricos**: frameworks, modelos, paradigmas
- **Variables de investigación**: dependientes, independientes

#### Prioridad 3: Contexto General

- **Conclusiones categóricas**: "se demuestra que", "queda evidenciado"
- **Limitaciones**: "no fue posible", "debido a restricciones"
- **Organizaciones**: nombres de empresas, instituciones

### 🎯 Ventajas del Sistema de Extractos Integrados

#### ✅ Para el Tribunal de Evaluación
- **⏱️ Ahorro de tiempo**: No necesita consultar páginas específicas del documento
- **🎯 Contexto inmediato**: Toda la información relevante está en la pregunta
- **📊 Datos específicos**: Números exactos, porcentajes y métricas incluidos
- **🔍 Evidencia directa**: Fragmentos textuales como prueba de los problemas identificados
- **📋 Profesionalismo**: Preguntas estructuradas con rigor académico

#### ✅ Para el Estudiante/Candidato
- **🎯 Claridad total**: Sabe exactamente qué fragmento del documento se está cuestionando
- **📖 Preparación enfocada**: Puede preparar respuestas específicas a datos concretos
- **⚖️ Transparencia**: No hay ambigüedad sobre qué aspectos son problemáticos
- **🧠 Reflexión profunda**: Debe justificar inconsistencias específicas identificadas

#### ✅ Para la Institución Académica
- **⭐ Calidad evaluativa**: Preguntas de mayor nivel técnico y especificidad
- **📊 Rigor metodológico**: Evaluación basada en evidencia textual concreta
- **🎓 Estándar profesional**: Proceso de evaluación comparable a revistas académicas
- **🔄 Consistencia**: Sistema automatizado reduce variabilidad entre evaluadores

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

### `generar_preguntas_dinamicas()` - 🆕 Generador con Extractos Integrados
**Función mejorada v4.0** que genera preguntas autocontenidas con extractos textuales específicos del documento.

### `analizar_documento_profundamente()` - 🆕 Análisis Crítico IA
**Nueva función** que utiliza OpenAI para analizar profundamente el documento e identificar inconsistencias específicas.

### `buscar_extracto_en_documento()` - 🆕 Extractor Inteligente de Fragmentos
**Nueva función** con sistema de prioridades: datos numéricos → términos técnicos → contexto general.

### `extraer_datos_especificos_tfm()` - 🆕 Extractor Universal de Datos
**Nueva función** que extrae 20+ tipos de datos específicos: financieros, metodológicos, técnicos, estadísticos.

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

### 🆕 Preguntas v4.0 - Con Extractos Integrados

#### Pregunta con Datos Financieros Específicos

```text
El análisis financiero presenta *ROI del 23.5% y VAN de €2.4M calculado con WACC del 8.2%*, 
pero posteriormente menciona que *el análisis de sensibilidad no fue aplicado debido a 
limitaciones de tiempo*. Dado que el documento afirma usar *metodología Monte Carlo para 
modelar incertidumbre*, ¿por qué estos cálculos críticos no incorporan variabilidad en 
las tasas de descuento, especialmente cuando el WACC del 8.2% no refleja el perfil de 
riesgo del proyecto según las limitaciones reconocidas?
```

#### Pregunta con Inconsistencias Metodológicas

```text
El modelo TO-BE muestra *incremento en la ineficiencia del tiempo de ciclo para el 
subproceso 'Diseño de instrumentos de evaluación y acreditación' (CTE desciende del 
32.88% en AS-IS al 29.97% en TO-BE)*, mientras que todos los otros subprocesos mejoran. 
El documento también indica que *la implementación de LEAN redujo desperdicios en un 
15% en promedio*, pero contradictoriamente afirma que *todos los rediseños TO-BE fueron 
uniformemente exitosos*. ¿Cómo se justifica esta inconsistencia específica donde un 
subproceso empeora 2.91 puntos porcentuales mientras se declara éxito universal?
```

#### Pregunta con Análisis Estadístico

```text
La investigación reporta *15 participantes en entrevistas semiestructuradas y 200 
encuestas con escala Likert*, obteniendo *75% de respuesta positiva en dimensión 1 
pero solo 60% en dimensión 2*. Sin embargo, *el análisis estadístico no incluye 
pruebas de normalidad ni tests de significancia*, y *la validez del instrumento no 
fue verificada mediante Alfa de Cronbach*. Considerando que estas deficiencias 
metodológicas comprometen la confiabilidad de los hallazgos, ¿cómo se garantiza 
que las diferencias observadas entre dimensiones son estadísticamente significativas 
y no producto del azar o sesgos muestrales?
```

### 📋 Preguntas v3.0 - Epistemológicas Clásicas

#### Pregunta Epistemológica Típica

```text
**Ruptura en la cadena de pensamiento**: Los objetivos formulados no derivan 
lógicamente de la problemática planteada, y la metodología aplicada no persigue 
coherentemente dichos objetivos. ¿Cómo se justifica esta desarticulación y qué 
evidencia sustenta que la metodología es la más adecuada para alcanzar los 
objetivos planteados?
```

#### Pregunta sobre Secuencia Metodológica

```text
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

### 🆕 Diagnóstico Mejorado (v4.0)

El sistema ahora incluye **logs detallados** para el sistema de extractos y análisis:

```logs
2025-10-16 10:15:23,456 [INFO] ✅ Pregunta con extractos - Enfoque: inconsistencia_metodologica
2025-10-16 10:15:23,456 [INFO]    📄 Extractos incluidos: 3 fragmentos
2025-10-16 10:15:23,456 [INFO]    📊 Datos específicos: ['32.88%', '29.97%', 'CTE']
2025-10-16 10:15:23,456 [INFO] Extraídos datos específicos: 15 números, 8 metodologías, 5 conceptos teóricos
```

### Logs del Sistema

Los logs se guardan en `evaluador_tfm_integrado.log` en la carpeta del TFM para debugging.

## 📈 Mejoras Futuras

### 🚀 Próximas Versiones (v5.0+)
- [ ] **Sistema multiidioma**: Extractos y preguntas en inglés/español
- [ ] **Integración Claude/Gemini**: Análisis comparativo entre LLMs
- [ ] **Dashboard web**: Gestión de múltiples evaluaciones TFM
- [ ] **API REST**: Integración con sistemas institucionales
- [ ] **Análisis longitudinal**: Comparación histórica de calidad TFM
- [ ] **Plantillas personalizables**: Adaptación a otras instituciones académicas

### 🔧 Mejoras Técnicas
- [ ] Soporte para Windows/Linux (AppKit → multiplataforma)
- [ ] Exportación directa a LaTeX/Word con formato institucional
- [ ] Validación cruzada entre múltiples evaluadores IA
- [ ] Sistema de feedback automático para estudiantes
- [ ] Integración con Turnitin/sistemas antiplagio

### 📊 Impacto y Adopción
- [ ] Métricas de mejora en calidad de TFMs evaluados
- [ ] Reducción de tiempo de evaluación (objetivo: 60% menos)
- [ ] Estudios de validez comparativa con evaluadores humanos
- [ ] Adopción en otras universidades y programas de máster

## 📝 Registro de Cambios

### v4.0 (Octubre 2025) - Sistema de Extractos Integrados

- 🚀 **Integración de extractos textuales** en preguntas del tribunal
- 🔍 **Búsqueda inteligente de datos específicos** con sistema de prioridades
- 📊 **Extracción ampliada** de datos financieros, metodológicos y técnicos
- 🎯 **Preguntas autocontenidas** eliminando consulta de páginas
- 🧠 **Análisis crítico profundo** con OpenAI para detectar inconsistencias
- ⚡ **Sistema de rotación de patrones** evitando repetición de preguntas
- 📈 **Extracción de 20+ tipos de datos** incluyendo ratios, indicadores, variables
- 🔧 **Función buscar_extracto_en_documento()** con 3 niveles de prioridad
- 📋 **Formato profesional** con extractos marcados en cursiva (*texto*)
- ✅ **Validación completa** con ejemplos reales (CTE, ROI, participantes)
- 🗑️ **Eliminación de funciones de respaldo** (sistema fail-fast con mensajes claros)

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

**Versión**: 4.0 - Sistema de Extractos Integrados  
**Última actualización**: 16 de Octubre 2025  
**Autor**: JJVR  
**Contacto**: Para soporte, crear issue en el repositorio  

> 🎉 **¡Revolucionario sistema de preguntas autocontenidas!** Ahora las preguntas del tribunal incluyen extractos específicos del documento, eliminando completamente la necesidad de consultar páginas durante la evaluación.