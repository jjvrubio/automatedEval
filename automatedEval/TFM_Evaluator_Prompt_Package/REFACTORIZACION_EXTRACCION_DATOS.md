# Refactorización de Extracción de Datos - Documentación

## Cambios Implementados

### 🎯 Objetivos
- Externalizar toda la configuración hardcodeada a un archivo YAML configurable
- Mejorar la mantenibilidad y flexibilidad del sistema
- Facilitar la personalización por dominio académico
- Reducir la complejidad del código Python

### 📁 Archivos Creados
- `configuracion_extraccion_datos.yaml` - Configuración externa completa

### 🔧 Funciones Modificadas
- `extraer_datos_especificos_tfm()` - Refactorizada para usar YAML
- Añadidas funciones auxiliares:
  - `cargar_configuracion_extraccion()` - Carga configuración desde YAML
  - `inicializar_estructura_datos()` - Inicializa estructura basada en config

### 📋 Estructura del YAML

#### Categorías de Datos
```yaml
estructura_datos:
  numericos: [numeros_y_porcentajes, valores_financieros, ...]
  metodologicos: [metodologias_mencionadas, nombres_herramientas, ...]
  academicos: [conceptos_teoricos, variables_estudiadas, ...]
  organizacionales: [empresas_organizaciones, sectores_industrias, ...]
  problemas: [indicadores_problemas, frases_contradictorias]
```

#### Patrones Regex Configurables
```yaml
patrones_regex:
  numeros_porcentajes: '\d+(?:\.\d+)?%'
  valores_financieros: '[€$£¥S/]\s*\d+(?:,\d{3})*(?:\.\d+)?'
  # ... más patrones
```

#### Metodologías por Dominio
```yaml
metodologias:
  estrategicas: [PESTEL, PORTER, DAFO, SWOT, ...]
  financieras: [ROI, VAN, NPV, TIR, ...]
  operacionales: [LEAN, SIX SIGMA, SCRUM, ...]
  # ... más dominios
```

### 💡 Ventajas de la Refactorización

1. **Configurabilidad**: Modificar patrones sin tocar código Python
2. **Mantenibilidad**: Código más limpio y organizado
3. **Extensibilidad**: Fácil añadir nuevos dominios académicos
4. **Reutilización**: El YAML puede usarse en otros proyectos
5. **Validación**: Mejor manejo de errores con fallbacks
6. **Logging Mejorado**: Estadísticas detalladas de extracción

### 🚀 Uso

La función mantiene la misma interfaz:
```python
datos = extraer_datos_especificos_tfm(texto_tfm, resultados, logger)
```

Pero ahora internamente:
1. Carga configuración desde YAML
2. Inicializa estructura de datos dinámicamente  
3. Aplica patrones configurables
4. Respeta límites configurados
5. Proporciona estadísticas detalladas

### 🛡️ Fallbacks y Robustez

- Si falta el YAML, usa configuración por defecto reducida
- Manejo de errores regex con `try/except`
- Límites configurables para evitar sobrecarga
- Logging detallado para troubleshooting

### 📈 Beneficios Específicos

#### Antes (Hardcodeado)
- 400+ líneas con listas hardcodeadas
- Difícil modificar sin conocer Python
- Patrones regex mezclados con lógica
- Sin control de límites centralizado

#### Después (Configurable)
- ~100 líneas de lógica limpia
- Configuración externa fácil de modificar
- Separación clara de concerns
- Control granular via YAML

### 🔄 Compatibilidad

- **Backwards Compatible**: Misma interfaz de función
- **Graceful Degradation**: Funciona sin YAML (modo reducido)  
- **Error Handling**: Manejo robusto de errores de configuración

### 🎭 Casos de Uso Futuros

1. **TFM Técnicos**: Añadir metodologías de ingeniería al YAML
2. **TFM Salud**: Configurar patrones específicos médicos  
3. **TFM Educación**: Personalizar para marcos pedagógicos
4. **Multiidioma**: Patrones para documentos en inglés/francés

Esta refactorización convierte el sistema en una herramienta verdaderamente configurable y extensible para cualquier dominio académico.