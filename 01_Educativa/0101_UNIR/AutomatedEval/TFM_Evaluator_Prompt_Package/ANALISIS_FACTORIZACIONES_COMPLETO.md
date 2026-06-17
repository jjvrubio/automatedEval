# Análisis Completo de Factorizaciones - Sistema TFM
# ===================================================

## 🎯 Factorizaciones Implementadas

### ✅ **1. Configuración de Extracción de Datos**
- **Archivo:** `configuracion_extraccion_datos.yaml`
- **Beneficio:** 400+ líneas hardcodeadas → configuración externa
- **Incluye:** Patrones regex, metodologías por dominio, límites, estructura de datos

### ✅ **2. Plantillas de Análisis Crítico** 
- **Archivo:** `plantillas_analisis_critico.yaml`
- **Beneficio:** Prompts complejos externalizados y configurables
- **Incluye:** Instrucciones críticas, requisitos esenciales, ejemplos de formato, objetivos de análisis

### ✅ **3. Configuración del Sistema TFM**
- **Archivo:** `configuracion_sistema_tfm.yaml`
- **Beneficio:** Rutas, mensajes y configuraciones centralizadas
- **Incluye:** Rutas de archivos, configuración OpenAI, mensajes de diálogos, configuración de logging

/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/TFM_Evaluator_Prompt.yaml
### 📋 **4. Plantillas de Prompts de Evaluación**
**Ubicación identificada:** Función `construir_prompt_v2()`
```python
# ESTE BLOQUE PUEDE SER YAML:
partes = [
    "Eres un evaluador académico experto que debe evaluar un TFM según criterios específicos de rúbrica.",
    "",
    "CRITERIO A EVALUAR:",
    criterio,
    "",
    "INSTRUCCIONES DEL EVALUADOR:",
    instrucciones_base,
    "",
    f"NIVELES VÁLIDOS PARA ESTE CRITERIO (debes elegir EXACTAMENTE uno de estos):",
]
```

**Propuesta:** `plantillas_prompts_evaluacion.yaml`
```yaml
prompt_evaluacion:
  introduccion: "Eres un evaluador académico experto que debe evaluar un TFM según criterios específicos de rúbrica."
  secciones:
    - "CRITERIO A EVALUAR"
    - "INSTRUCCIONES DEL EVALUADOR" 
    - "NIVELES VÁLIDOS PARA ESTE CRITERIO"
    - "REGLAS DE EVALUACIÓN"
    - "FORMATO DE RESPUESTA (JSON válido)"
  
  reglas_evaluacion:
    - "Debes elegir EXACTAMENTE uno de los niveles listados arriba"
    - "Proporciona una justificación clara y específica"
    - "Incluye al menos 2 evidencias con citas exactas del texto"
    - "Cada evidencia debe incluir el número de página [P#]"
```

### 🏗️ **5. Configuración de Estructuras JSON**
**Ubicación identificada:** Múltiples funciones con estructuras JSON hardcodeadas
```python
# ESTE FORMATO PUEDE SER YAML:
'{',
f'  "nivel": "DEBE ser exactamente uno de: {" | ".join(niveles_rubrica)} | No evaluable",',
'  "justificacion": "Explicación detallada de por qué se asigna este nivel",',
'  "areas_mejora": "Recomendaciones específicas para mejorar (vacío si nivel máximo)",',
```

**Propuesta:** `esquemas_json_evaluacion.yaml`
```yaml
esquemas:
  evaluacion_criterio:
    nivel:
      tipo: "string"
      opciones_dinamicas: true
      descripcion: "DEBE ser exactamente uno de los niveles de la rúbrica | No evaluable"
    
    justificacion:
      tipo: "string"
      descripcion: "Explicación detallada de por qué se asigna este nivel"
    
    areas_mejora:
      tipo: "string"
      descripcion: "Recomendaciones específicas para mejorar (vacío si nivel máximo)"
    
    evidencias:
      tipo: "array"
      items:
        frase: "Cita exacta del texto"
        pagina: "P#"
```

### 📝 **6. Patrones de Análisis Local**
**Ubicación identificada:** Función `analizar_inconsistencias_locales()`
```python
# ESTOS PATRONES PUEDEN SER YAML:
patrones_conclusiones = [
    r'se concluye que.{10,100}',
    r'los resultados demuestran.{10,100}',
    r'se puede afirmar.{10,100}',
    r'queda demostrado.{10,100}',
    r'se evidencia que.{10,100}'
]
```

**Propuesta:** Incorporar en `configuracion_extraccion_datos.yaml`
```yaml
patrones_analisis_local:
  conclusiones_categoricas:
    - 'se concluye que.{10,100}'
    - 'los resultados demuestran.{10,100}'
    - 'se puede afirmar.{10,100}'
    - 'queda demostrado.{10,100}'
    - 'se evidencia que.{10,100}'
  
  inconsistencias_numericas:
    patron_base: '\d+(?:\.\d+)?%?'
    contexto_caracteres: 80
    minimo_numeros: 3
```

### 🎨 **7. Plantillas de Preguntas Dinámicas**
**Ubicación identificada:** Función `generar_pregunta_con_datos_especificos()`
```python
# ESTOS TEMPLATES ESTÁN HARDCODEADOS:
return f"""El documento establece *{extracto_metodologia}* planteando la hipótesis "{hipotesis_principal}" para evaluar {variable_principal} mediante {metodologia_principal} (página {evidencia_pagina}), sin embargo, {justificacion.lower()[:120]}"""
```

**Propuesta:** `plantillas_preguntas_dinamicas.yaml`
```yaml
plantillas_por_patron:
  investigacion_cientifica:
    template: |
      El documento establece *{extracto_metodologia}* planteando la hipótesis "{hipotesis_principal}" 
      para evaluar {variable_principal} mediante {metodologia_principal} (página {evidencia_pagina}), 
      sin embargo, {justificacion_truncada}. Dado que la validez interna requiere control riguroso 
      de variables confusoras y la validez externa depende de la representatividad muestral, 
      ¿cómo se garantiza que las limitaciones metodológicas identificadas no comprometen la 
      generalización de los hallazgos?
    
    campos_requeridos:
      - "variable_principal"
      - "hipotesis_principal" 
      - "metodologia_principal"
      - "evidencia_pagina"
```

### ⚙️ **8. Configuración de AppKit y Diálogos macOS**
**Ubicación identificada:** Funciones `seleccionar_archivo_pdf_docx()` y `elegir_rubrica_dialogo()`
```python
# ESTOS TEXTOS PUEDEN SER YAML:
panel.setTitle_("Selecciona el TFM del alumno")
panel.setMessage_("Elige el archivo PDF o DOCX del TFM")
```

**Ya incluido en:** `configuracion_sistema_tfm.yaml` ✅

### 🔧 **9. Configuración de OneDrive y Utilerías**
**Ubicación identificada:** Constantes y funciones de utilidades
```python
# ESTAS CONFIGURACIONES PUEDEN SER YAML:
ONEDRIVE_HINTS = ("OneDrive", "OneDrive - ")
MODELO_POR_DEFECTO = "gpt-4o-mini"
TEMPERATURA_POR_DEFECTO: float = 0.0
```

**Ya incluido en:** `configuracion_sistema_tfm.yaml` ✅

## 📊 **Resumen de Impacto**

### **Antes de Factorización:**
- **Líneas hardcodeadas:** ~800+ líneas
- **Archivos de configuración:** 0
- **Mantenibilidad:** Baja (requiere modificar código Python)
- **Reutilización:** Nula
- **Personalización:** Difícil

### **Después de Factorización Completa:**
- **Líneas hardcodeadas:** ~200 líneas de lógica
- **Archivos de configuración:** 4-5 archivos YAML especializados
- **Mantenibilidad:** Alta (modificación externa)
- **Reutilización:** Excelente (YAMLs reutilizables)
- **Personalización:** Trivial por dominio académico

## 🚀 **Próximos Pasos Sugeridos**

### **Prioridad Alta:** 
1. ✅ Configuración de extracción de datos
2. ✅ Plantillas de análisis crítico  
3. ✅ Configuración del sistema

### **Prioridad Media:**
4. 📋 Plantillas de prompts de evaluación
5. 🏗️ Esquemas JSON configurables
6. 🎨 Plantillas de preguntas dinámicas

### **Prioridad Baja:**
7. 📝 Patrones de análisis local (ya cubierto parcialmente)

## 💡 **Beneficios de Factorización Completa**

1. **🔧 Configurabilidad Total:** Cualquier aspecto modificable sin tocar código
2. **🎯 Especialización por Dominio:** YAMLs específicos para TFM técnicos/salud/educación
3. **🔄 Mantenimiento Simplificado:** Cambios de comportamiento via configuración
4. **📚 Reutilización:** YAMLs reutilizables en otros proyectos de evaluación
5. **🧪 Testing:** Configuraciones de prueba separadas de producción
6. **🌐 Internacionalización:** Plantillas en múltiples idiomas
7. **📈 Escalabilidad:** Nuevas metodologías/dominios sin cambios de código

La factorización convierte el sistema en una **plataforma configurable** verdaderamente flexible y extensible para cualquier contexto académico.