# 📚 Validador de Referencias Bibliográficas

## 🎯 Descripción

Sistema **modular independiente** para validar referencias bibliográficas en documentos académicos. Compatible con múltiples formatos de archivo, estilos de cita e idiomas.

## ✨ Características Principales

- ✅ **Extracción automática** desde PDF y DOCX
- ✅ **Múltiples estilos**: APA 7, IEEE, MLA
- ✅ **Multiidioma**: Español e inglés
- ✅ **Informes detallados**: JSON y Markdown
- ✅ **Completamente independiente**: No requiere otros sistemas
- ✅ **Reutilizable**: TFMs, ensayos, artículos, tesis

## 🚀 Instalación Rápida

```bash
# Navegar al directorio
cd "APA Report"

# Instalar dependencias
pip install -r requirements_referencias.txt

# Verificar instalación
python referencias_validator.py --help
```

### Dependencias
- `pdfplumber>=0.9.0` - Para procesar PDFs
- `lxml>=4.9.0` - Para procesar DOCX
- `pyobjc` - Para selector nativo de macOS (opcional, fallback disponible)

### 📱 Compatibilidad
- **✅ macOS**: Selector nativo NSOpenPanel + gestión OneDrive
- **⚡ Otros sistemas**: Fallback automático a selección manual
- **☁️ OneDrive**: Hidratación automática de archivos en la nube

## 📖 Uso Básico

### 🎮 Modo Interactivo con Selector Nativo (Recomendado)
```bash
# Lanza interfaz con selector de archivos nativo de macOS
python referencias_validator.py --interactivo
```
- **🍎 Selector nativo de macOS** - NSOpenPanel como el evaluador TFM
- **☁️ Compatible con OneDrive** - Hidratación automática de archivos en la nube
- **📋 Configuración guiada** paso a paso
- **💡 Ideal para nuevos usuarios**

### 🎯 Modo Comando (Directo)
```bash
python referencias_validator.py --archivo DOCUMENTO --estilo ESTILO [opciones]
```

### 🔄 Modo Semi-Interactivo
```bash
# Si omites --archivo, abre selector gráfico automáticamente
python referencias_validator.py --estilo apa
```
- **📁 Selector automático** si no especificas archivo
- **🍎 Interfaz nativa** idéntica al evaluador TFM

### Ejemplos Comunes

#### Validar TFM con estilo APA
```bash
python referencias_validator.py --archivo tfm_estudiante.pdf --estilo apa
```

#### Validar artículo con estilo IEEE
```bash
python referencias_validator.py --archivo articulo.docx --estilo ieee --formato json
```

#### Validar ensayo con estilo MLA
```bash
python referencias_validator.py --archivo ensayo.pdf --estilo mla --salida informe_mla.md
```

## 📊 Parámetros Disponibles

| Parámetro | Descripción | Opciones | Por defecto |
|-----------|-------------|----------|-------------|
| `--archivo` `-a` | Archivo a analizar | PDF, DOCX | **Requerido** |
| `--estilo` `-e` | Estilo de cita | apa, ieee, mla | `apa` |
| `--salida` `-s` | Archivo de salida | Ruta personalizada | Auto-generado |
| `--formato` `-f` | Formato del informe | json, markdown | `markdown` |

## 🎯 Estilos de Cita Soportados

### APA 7th Edition
```
García, J. M. (2023). Machine learning en educación. 
Revista de Tecnología Educativa, 45(3), 123-145. 
https://doi.org/10.1234/ejemplo
```

### IEEE
```
J. M. García, "Machine learning en educación," 
Revista de Tecnología Educativa, vol. 45, no. 3, 
pp. 123-145, 2023.
```

### MLA 8th Edition
```
García, Juan Manuel. "Machine Learning en Educación." 
Revista de Tecnología Educativa, vol. 45, no. 3, 2023, 
pp. 123-145.
```

## 📋 Validaciones Realizadas

### Componentes Verificados
- ✅ **Autor(es)**: Formato según estilo
- ✅ **Año**: Formato y posición
- ✅ **Título**: Capitalización y puntuación
- ✅ **Editorial/Revista**: Presencia y formato
- ✅ **URL**: Formato válido
- ✅ **DOI**: Formato estándar

### Tipos de Publicación Detectados
- 📄 **Artículos de revista**
- 📚 **Libros**
- 📖 **Capítulos de libro**
- 🎓 **Tesis**
- 🌐 **Recursos web**

## 📊 Informes Generados

### Formato Markdown (Por defecto)
```markdown
# 📚 Informe de Validación de Referencias

**Archivo:** documento.pdf
**Estilo:** APA 7th Edition
**Cumplimiento:** 80.0%

## 📊 Resumen
- Referencias válidas: 20/25
- Puntuación promedio: 0.83/1.00

## 🔍 Análisis Detallado
[Análisis individual de cada referencia...]
```

### Formato JSON
```json
{
  "archivo_analizado": "documento.pdf",
  "estilo_validacion": "apa",
  "total_referencias": 25,
  "referencias_validas": 20,
  "puntuacion_promedio": 0.83,
  "referencias": [...]
}
```

## 🧪 Casos de Uso

### 1. Evaluación de TFMs
```bash
python referencias_validator.py --archivo TFM_estudiante.pdf --estilo apa
```

### 2. Revisión de Artículos
```bash
python referencias_validator.py --archivo articulo.docx --estilo ieee --formato json
```

### 3. Corrección de Ensayos
```bash
python referencias_validator.py --archivo ensayo.pdf --estilo mla
```

### 4. Auditoría de Tesis
```bash
python referencias_validator.py --archivo tesis.pdf --estilo apa --salida auditoria.json
```

## 🔧 Funcionalidades Avanzadas

### Detección Automática de Idioma
- Identifica automáticamente español e inglés
- Adapta la búsqueda de secciones de referencias
- Ajusta patrones de validación por idioma

### Extracción Inteligente
- Detecta automáticamente la sección de referencias
- Filtra encabezados y pies de página
- Identifica tipos de publicación

### Validación Específica por Estilo
- Reglas específicas para cada estilo de cita
- Detección de errores comunes
- Sugerencias de mejora personalizadas

## 🛠️ Arquitectura del Sistema

### Módulos Principales
```
APA Report/
├── referencias_validator.py      # Módulo principal
├── config_referencias.py         # Configuración
├── utils_referencias.py          # Utilidades
├── ejemplos_uso.py              # Ejemplos
├── requirements_referencias.txt  # Dependencias
└── README_REFERENCIAS.md        # Documentación técnica
```

### Clases Principales
- **ExtractorReferencias**: Extrae referencias de PDF/DOCX
- **ValidadorReferencias**: Valida según estándares
- **GeneradorInformes**: Crea informes JSON/Markdown

## 🧪 Verificar Funcionamiento

### Ejecutar Ejemplos
```bash
python ejemplos_uso.py
```

### Script de Instalación
```bash
./instalar_sistema.sh
```

## ⚙️ Configuración Personalizada

### Umbrales de Validación
Editar `config_referencias.py`:
```python
UMBRALES_VALIDACION = {
    "puntuacion_minima_aprobado": 0.7,
    "porcentaje_referencias_validas_minimo": 80
}
```

### Añadir Nuevos Estilos
1. Definir patrones en `config_referencias.py`
2. Implementar validador en `ValidadorReferencias`
3. Añadir reglas en `ValidadorFormato`

## 🚨 Solución de Problemas

### Dependencias faltantes
```bash
pip install pdfplumber lxml
```

### No se detectan referencias
- Verificar sección de referencias en el documento
- Comprobar palabras clave ("Referencias", "Bibliography")
- Revisar formato del documento

### Validaciones incorrectas
- Verificar estilo seleccionado
- Comprobar formato de referencias
- Consultar ejemplos en `config_referencias.py`

## 🔗 Integración

### Como Módulo Python
```python
from referencias_validator import ValidadorReferencias, EstiloCita

validador = ValidadorReferencias(EstiloCita.APA)
resultado = validador.validar_referencia(referencia_texto)

if resultado.es_completa:
    print(f"Válida: {resultado.puntuacion}")
else:
    print(f"Errores: {resultado.errores}")
```

### Con Otros Sistemas
- Independiente del evaluador TFM
- Compatible con cualquier flujo de trabajo
- API modular para integración futura

## 📈 Ventajas del Sistema

### 🎯 **Independencia**
- No interfiere con otros sistemas
- Ejecutable por separado
- Sin dependencias externas complejas

### 🔄 **Reutilización**
- TFMs, ensayos, artículos, tesis
- Múltiples contextos académicos
- Diferentes instituciones

### 📊 **Calidad**
- Validación específica por estilo
- Informes profesionales
- Estadísticas detalladas

### 🛠️ **Extensibilidad**
- Fácil añadir nuevos estilos
- Configuración modular
- Personalización flexible

## 🎉 Conclusión

El **Validador de Referencias** es una herramienta **independiente, profesional y reutilizable** para la validación de referencias bibliográficas en cualquier contexto académico.

**¡Listo para usar en producción!** 🚀

---

**📖 Documentación completa**: `README_REFERENCIAS.md`  
**🧪 Ejemplos**: `python ejemplos_uso.py`  
**⚙️ Configuración**: `config_referencias.py`