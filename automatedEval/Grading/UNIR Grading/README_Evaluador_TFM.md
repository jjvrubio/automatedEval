# Evaluador TFM — Resumen práctico (versión concisa)

Este README ha sido simplificado para reflejar el estado actual del proyecto tras la preparación y publicación de la release `v1.0`.

Propósito rápido:
- Instrucciones de ejecución mínimas.
- Requisitos y dependencias esenciales.
- Indicaciones sobre seguridad y ubicación de archivos relevantes.

Estado actual
- Release publicada: tag `v1.0` (ver en GitHub releases).
- Branch de release: `release/v1.0` (creada y subida).
- Backup comiteado: `automatedEval_backup_20251026_211903.zip` (en la raíz del repo).
- Archivos históricos movidos a `archive/UNIR_Grading/`.
- Scripts APA consolidados en `automatedEval/APA Report/`.

Requisitos básicos
- Python 3.8+ (se recomienda usar `venv_arm64` en macOS/ARM).
- Dependencias (instalar en el venv):
```bash
pip install -r requirements.txt
# o al menos:
pip install pdfplumber python-docx pandas openai pyyaml
```
- Variable de entorno obligatoria:
```bash
export OPENAI_API_KEY="tu_clave_api_openai"
```

Ejecución rápida
1. Activa el entorno virtual (ejemplo):
```bash
source ./venv_arm64/bin/activate
```
2. Ejecutar versión integrada (producción):
```bash
python "automatedEval/Grading/UNIR Grading/Evaluador_TFM_Integrado_ultraestricto.py"
```
3. Ejecutar versión de diagnóstico (SafeFix) para pruebas locales sin riesgos:
```bash
python "automatedEval/Grading/UNIR Grading/Evaluador_TFM_SafeFix.py"
```

Comportamiento importante
- Fail‑fast: si faltan los YAML de configuración o la API key, el script aborta mostrando un error claro.
- Determinismo: la temperatura por defecto está fijada a 0.0 para evitar variabilidad entre ejecuciones.
- Salidas: CSV, JSON y Markdown se generan EN LA MISMA CARPETA que el TFM seleccionado. Las preguntas de clarificación se guardan únicamente en el Markdown.

Seguridad y notas operativas
- GitHub detectó una credencial en un commit durante la preparación del release — rota/rehabilita la credencial si no lo has hecho ya.
- El backup ZIP fue comiteado por seguridad; si prefieres no mantener binarios en el repo, muévelo fuera y añade su patrón a `.gitignore`.

Ubicación de archivos clave
```
automatedEval/
├─ Grading/UNIR Grading/
│  ├─ Evaluador_TFM_Integrado_ultraestricto.py
│  ├─ Evaluador_TFM_SafeFix.py
│  ├─ configuracion_extraccion_datos.yaml
│  └─ configuracion_sistema_tfm.yaml
├─ TFM_Evaluator_Prompt_Package/ (plantillas y rúbricas)
├─ "APA Report"/ (validadores y utilidades APA)
└─ archive/UNIR_Grading/ (archivos históricos)
```

Pruebas y debugging
- Para pruebas sin usar la API: ejecuta `Evaluador_TFM_SafeFix.py` (logging más verboso, fallbacks locales).
- Si quieres, puedo añadir un test pytest que haga mock de OpenAI y verifique la equivalencia CSV↔JSON y que las preguntas se escriben solo en MD.

Acciones realizadas por mí
- Actualicé este README para reflejar el estado real y las decisiones de release (v1.0).

¿Quieres que:
1) haga commit y push de este README a `principal` ahora (recomendado), o
2) revises aquí y me pides cambios antes del commit?

---

Versión breve creada automáticamente para mantener claridad operativa.

# Evaluador TFM — Documentación (estado actual)

Esta documentación resume el estado actual del evaluador TFM tras la preparación de la release `v1.0` y la integración de las correcciones de robustez (SafeFix).

Objetivos rápidos:
- Describir cómo ejecutar el evaluador integrado y la versión de diagnóstico (SafeFix).
- Explicar las garantías de seguridad y fail‑fast añadidas (YAML obligatorio, comprobación de API key).
- Indicar la ubicación actual de scripts relevantes, backups y release.

## Resumen de funcionalidades (práctico)

- Detección automática de rúbricas (`MUDPE` / `MUGPTD`) cuando están presentes.
- Evaluación por criterios con export normalizado a CSV, JSON y un informe Markdown.
- Generación de preguntas de clarificación/defensa en Markdown (guardadas únicamente en el MD).
- Fail‑fast: el proceso aborta si faltan los ficheros YAML de configuración o la credencial de OpenAI.
- Determinismo: temperatura por defecto fijada a 0.0 para reproducibilidad.

Nota: la versión de diagnóstico `Evaluador_TFM_SafeFix.py` existe para pruebas y contiene hooks de logging y mocks útiles para testear sin la API real.

## Estado del repositorio y release

- Branch release: `release/v1.0` (creada y subida a remoto).
- Tag publicado: `v1.0` (ya publicado en GitHub). Puedes ver la release en:
  https://github.com/jjvrubio/automatedEval/releases/tag/v1.0
- Backup ZIP creado y comiteado: `automatedEval_backup_20251026_211903.zip` (en la raíz del repo).
- Scripts históricos relacionados con UNIR Grading han sido movidos a `archive/UNIR_Grading/` y los scripts APA se consolidaron en `automatedEval/APA Report/`.
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
│   ├── Evaluador_TFM_Integrado_ultraestricto.py   # Script principal
│   ├── configuracion_extraccion_datos.yaml        # Config extracción
│   ├── plantillas_analisis_critico.yaml          # Plantillas análisis
│   ├── configuracion_sistema_tfm.yaml            # Config sistema
│   ├── test_debugging_system.py                  # Tests debugging
│   ├── SOLUCION_DUPLICACION_PREGUNTAS.md        # Doc debugging
│   └── README_Evaluador_TFM.md                  # Esta documentación
├── TFM_Evaluator_Prompt_Package/
│   ├── plantillas_preguntas.yaml                  # Marco epistemológico
│   ├── rubrica MUDPE.xlsx                         # Rúbrica MUDPE
│   ├── rubrica MUGPTD.xlsx                        # Rúbrica MUGPTD
│   └── Ultraestricto.md                          # Instrucciones de evaluación
└── APA Report/                                    # Sistema independiente
    ├── referencias_validator.py                   # Validador referencias
    ├── config_referencias.py                      # Config referencias
    ├── utils_referencias.py                       # Utilidades
    ├── ejemplos_uso.py                           # Ejemplos
    └── README_REFERENCIAS.md                     # Doc referencias
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

## 🔧 Sistema de Configuración Externa (v4.1)

### Archivos de Configuración YAML

#### `configuracion_extraccion_datos.yaml`
Contiene patrones de extracción y metodologías por dominio:
```yaml
estructura_datos:
  metodologias: []
  datos_numericos: []
  terminologia_tecnica: []

patrones_regex:
  numeros_porcentajes: "[0-9]+(?:[.,][0-9]+)?%"
  valores_monetarios: "[€$£¥][0-9]+(?:[.,][0-9]+)?"
  
metodologias_por_dominio:
  tecnologia: ["machine learning", "big data", "IoT"]
  educacion: ["constructivismo", "aprendizaje cooperativo"]
```

#### `plantillas_analisis_critico.yaml`
Plantillas para análisis crítico y generación de preguntas:
```yaml
plantillas_analisis:
  objetivos_generales:
    - "Analizar la rigurosidad metodológica del estudio"
    - "Evaluar la coherencia entre objetivos y metodología"
    
  requisitos_esenciales:
    - "Uso de extractos específicos del documento"
    - "Preguntas basadas en inconsistencias detectadas"
```

#### `configuracion_sistema_tfm.yaml`
Configuración general del sistema:
```yaml
rutas_archivos:
  ruta_instrucciones_md: "TFM_Evaluator_Prompt_Package/Ultraestricto.md"
  carpeta_plantillas: "TFM_Evaluator_Prompt_Package/"

configuracion_openai:
  modelo_por_defecto: "gpt-4o-mini"
  temperatura: 0.0
  max_tokens: 4000
```

### Ventajas de la Configuración Externa

- ✅ **Mantenibilidad**: Cambios sin modificar código
- ✅ **Flexibilidad**: Adaptación rápida a nuevos dominios
- ✅ **Extensibilidad**: Fácil agregar nuevos patrones
- ✅ **Consistencia**: Configuración centralizada
- ✅ **Debugging**: Parámetros configurables para testing

## 🔍 Sistema de Debugging Avanzado (v4.1)

### Características del Sistema de Debugging

#### 🔑 Identificación Única de Documentos
```python
# Generación de hash único por documento
documento_hash = hashlib.md5(texto_tfm.encode('utf-8')).hexdigest()[:12]
logger.info(f"🔑 Hash del documento: {documento_hash}")
```

#### 📋 Verificación de Unicidad
- **Detección de duplicaciones**: Evita preguntas idénticas entre TFMs
- **Análisis de extractos**: Verifica que cada pregunta use contenido específico
- **Sistema de similitud**: Detecta extractos genéricos vs específicos

#### 📝 Logging Extensivo
```python
logger.info(f"📏 Longitud del texto: {len(texto_tfm)} caracteres")
logger.info(f"🎯 Prompts enviados a OpenAI con identificación única")
logger.info(f"✅ Pregunta generada con extracto específico: {extracto[:50]}...")
```

### Funciones de Debugging Implementadas

#### `analizar_documento_profundamente()` - Mejorado
- **Hash de documento**: Identificación única para tracking
- **Verificación de especificidad**: Asegura preguntas documento-específicas
- **Logging detallado**: Tracking completo del proceso de análisis

#### `analizar_inconsistencias_locales()` - Sistema de Fallback
- **Análisis local**: Funciona sin OpenAI para testing
- **Extracción específica**: Busca contenido real del documento
- **Verificación de contexto**: Valida que los extractos sean específicos

#### Funciones de Utilidad
```python
def verificar_unicidad_preguntas(pregunta: str, historial: List[str]) -> bool
def calcular_similitud_extractos(extracto1: str, extracto2: str) -> float
def extraer_fragmentos_con_numeros(texto: str, numeros: List[str]) -> List[str]
```

### Testing del Sistema de Debugging

#### `test_debugging_system.py`
Script específico para probar la unicidad de preguntas:
```bash
python test_debugging_system.py
```

**Resultado esperado**:
```
✅ NO SE DETECTARON DUPLICACIONES - Sistema funcionando correctamente
```

### Resolución de Problemas Detectados

#### ❌ Problema Original
Preguntas idénticas generándose para diferentes TFMs.

#### ✅ Solución Implementada
1. **Sistema de hash único** por documento
2. **Extracción mejorada** de fragmentos específicos
3. **Verificación de contexto** real vs genérico
4. **Fallbacks identificables** cuando no hay contenido específico
5. **Testing automatizado** para verificar unicidad

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

## 🔗 Sistemas Relacionados

### 📚 Sistema de Validación de Referencias (Independiente)

En el directorio `APA Report/` se encuentra un **sistema modular independiente** para validación de referencias bibliográficas:

#### Características
- ✅ **Completamente independiente** del evaluador TFM
- ✅ **Reutilizable** para ensayos, artículos, tesis
- ✅ **Multi-formato**: PDF, DOCX
- ✅ **Multi-estilo**: APA 7, IEEE, MLA
- ✅ **Multi-idioma**: Español, inglés

#### Uso básico
```bash
cd "../APA Report/"
python referencias_validator.py --archivo documento.pdf --estilo apa
```

#### Documentación
Ver `APA Report/README_REFERENCIAS.md` para documentación completa.

### 🔄 Integración Futura

Aunque ambos sistemas funcionan de manera independiente, una futura integración podría incluir:

- **Validación automática** de referencias durante la evaluación TFM
- **Informe combinado** con evaluación de contenido + referencias
- **Análisis de calidad** bibliográfica como criterio adicional

## 📈 Historial de Versiones

### v4.1 (Octubre 2025) - Debugging y Configuración Externa
- ✅ **Sistema de debugging avanzado** con hash único por documento
- ✅ **Configuración externa YAML** para patrones y plantillas
- ✅ **Verificación de unicidad** de preguntas entre TFMs
- ✅ **Funciones de extracción mejoradas** para contenido específico
- ✅ **Sistema de testing** automatizado para debugging

### v4.0 (Septiembre 2025) - Extractos Integrados
- ✅ **Integración de extractos textuales** en preguntas
- ✅ **Sistema de búsqueda inteligente** de datos específicos
- ✅ **Preguntas autocontenidas** con evidencia integrada
- ✅ **Análisis crítico profundo** con IA
- ✅ **Extracción ampliada** de datos especializados

### v3.0 (Agosto 2025) - Sistema Adaptativo
- ✅ **Detección automática** de formato de rúbrica
- ✅ **Extracción de niveles reales** del contenido
- ✅ **Sistema adaptativo universal** MUDPE/MUGPTD
- ✅ **Eliminación** de funciones duplicadas
- ✅ **Mejoras** en robustez y exportación

### v2.0 (Julio 2025) - Marco Epistemológico
- ✅ **Marco epistemológico** avanzado
- ✅ **Análisis por secciones** estructurado
- ✅ **Detección** de patrones problemáticos
- ✅ **Generación** de preguntas expertas

### v1.0 (Junio 2025) - Versión Inicial
- ✅ **Evaluación básica** por criterios
- ✅ **Exportación** CSV y Markdown
- ✅ **Integración** con OpenAI API
- ✅ **Soporte** PDF y DOCX

## 🎯 Conclusión

El **Evaluador TFM Integrado Ultraestricto v4.1** representa la evolución más avanzada del sistema de evaluación automatizada, incorporando:

- **🔧 Robustez técnica** con debugging avanzado
- **⚙️ Configuración externa** para máxima flexibilidad
- **🎯 Precisión mejorada** con verificación de unicidad
- **📊 Análisis específico** por documento
- **🔗 Ecosistema completo** con sistema de referencias independiente

El sistema está listo para **producción académica** y proporciona evaluaciones de **calidad profesional** para TFMs de cualquier dominio académico.

---

**📧 Soporte**: Ver documentación técnica en archivos de configuración YAML y scripts de debugging.

**🔄 Actualizaciones**: Sistema modular preparado para expansión y mejoras continuas.

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