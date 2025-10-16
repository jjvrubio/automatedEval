# 📚 Sistema Modular de Validación de Referencias Bibliográficas

## 🎯 Descripción General

El **Sistema Modular de Validación de Referencias** es una herramienta independiente y reutilizable para validar referencias bibliográficas en múltiples formatos de documentos (PDF, DOCX) y estilos de cita (APA 7, IEEE, MLA).

### ✨ Características Principales

- ✅ **Extracción automática** de referencias desde PDF y DOCX
- ✅ **Validación multi-estilo** (APA 7, IEEE, MLA, Vancouver)
- ✅ **Detección inteligente** de patrones y componentes
- ✅ **Informes detallados** en JSON y Markdown
- ✅ **Completamente independiente** del sistema de evaluación TFM
- ✅ **Reutilizable** para ensayos, artículos, tesis, trabajos académicos

---

## 🚀 Instalación y Configuración

### Requisitos del Sistema

- **Python 3.8+**
- **macOS** (optimizado para entorno nativo)
- **Dependencias específicas** (ver `requirements_referencias.txt`)

### Instalación de Dependencias

```bash
# Navegar al directorio del sistema
cd /ruta/a/automatedEval/APA\ Report/

# Instalar dependencias
pip install -r requirements_referencias.txt

# Verificar instalación
python referencias_validator.py --help
```

### Dependencias Principales

```
pdfplumber>=0.9.0    # Procesamiento de PDFs
lxml>=4.9.0          # Procesamiento de DOCX
```

---

## 📖 Uso Básico

### Comando Principal

```bash
python referencias_validator.py --archivo DOCUMENTO --estilo ESTILO [opciones]
```

### Ejemplos de Uso

#### 1. Validar PDF con estilo APA
```bash
python referencias_validator.py --archivo tesis.pdf --estilo apa
```

#### 2. Validar DOCX con estilo IEEE y salida personalizada
```bash
python referencias_validator.py --archivo articulo.docx --estilo ieee --salida informe_ieee.json
```

#### 3. Validar con estilo MLA y formato Markdown
```bash
python referencias_validator.py --archivo ensayo.pdf --estilo mla --formato markdown
```

### Parámetros Disponibles

| Parámetro | Descripción | Opciones | Por defecto |
|-----------|-------------|----------|-------------|
| `--archivo` `-a` | Archivo a analizar | PDF, DOCX | **Requerido** |
| `--estilo` `-e` | Estilo de cita | apa, ieee, mla | `apa` |
| `--salida` `-s` | Archivo de salida | Ruta personalizada | Auto-generado |
| `--formato` `-f` | Formato del informe | json, markdown | `markdown` |

---

## 🏗️ Arquitectura del Sistema

### Módulos Principales

#### 1. `referencias_validator.py` - Módulo Principal
- **ExtractorReferencias**: Extrae referencias de PDF/DOCX
- **ValidadorReferencias**: Valida según estándares específicos
- **GeneradorInformes**: Crea informes en JSON/Markdown
- **Clases de datos**: ReferenciaAnalizada, InformeValidacion

#### 2. `config_referencias.py` - Configuración
- **Estilos de cita**: Patrones y reglas por estilo
- **Configuración de idiomas**: Español/Inglés
- **Tipos de publicación**: Artículo, libro, capítulo, tesis, web
- **Umbrales de validación**: Criterios de aprobación

#### 3. `utils_referencias.py` - Utilidades
- **DetectorPatrones**: Detección de idioma y tipos
- **LimpiadorTexto**: Normalización y limpieza
- **AnalizadorComponentes**: Extracción de componentes específicos
- **ValidadorFormato**: Validación específica por estilo

#### 4. `ejemplos_uso.py` - Casos de Uso
- Ejemplos prácticos de todas las funcionalidades
- Casos de prueba para diferentes escenarios
- Demostración de capacidades avanzadas

---

## 📊 Estilos de Cita Soportados

### 🔹 APA 7th Edition
**Formato autor**: `Apellido, I. M.`  
**Formato año**: `(2023)`  
**Ejemplo completo**:
```
García, J. M. (2023). Machine learning en educación. 
Revista de Tecnología Educativa, 45(3), 123-145. 
https://doi.org/10.1234/ejemplo
```

### 🔹 IEEE
**Formato autor**: `I. M. Apellido`  
**Formato título**: `"Título del artículo,"`  
**Ejemplo completo**:
```
J. M. García, "Machine learning en educación," 
Revista de Tecnología Educativa, vol. 45, no. 3, 
pp. 123-145, 2023.
```

### 🔹 MLA 8th Edition
**Formato autor**: `Apellido, Nombre`  
**Formato título**: `"Título del Artículo."`  
**Ejemplo completo**:
```
García, Juan Manuel. "Machine Learning en Educación." 
Revista de Tecnología Educativa, vol. 45, no. 3, 2023, 
pp. 123-145.
```

---

## 🔍 Funcionalidades Avanzadas

### Detección Automática de Idioma
El sistema detecta automáticamente si el documento está en español o inglés:
- **Palabras clave**: "referencias bibliográficas" vs "references"
- **Patrones lingüísticos**: Estructuras características de cada idioma
- **Adaptación automática**: Ajusta la extracción según el idioma detectado

### Tipos de Publicación Detectados
- **📄 Artículos de revista**: Journal articles
- **📚 Libros**: Books and monographs
- **📖 Capítulos de libro**: Book chapters
- **🎓 Tesis**: Thesis and dissertations
- **🌐 Recursos web**: Web resources and online content

### Componentes Validados
- ✅ **Autor(es)**: Formato según estilo
- ✅ **Año**: Formato y posición correcta
- ✅ **Título**: Capitalización y puntuación
- ✅ **Editorial/Revista**: Presencia y formato
- ✅ **URL**: Formato válido
- ✅ **DOI**: Formato estándar

---

## 📈 Informes Generados

### Formato JSON
```json
{
  "archivo_analizado": "documento.pdf",
  "estilo_validacion": "apa",
  "total_referencias": 25,
  "referencias_validas": 20,
  "referencias_con_errores": 5,
  "puntuacion_promedio": 0.83,
  "referencias": [...],
  "recomendaciones_generales": [...]
}
```

### Formato Markdown
```markdown
# 📚 Informe de Validación de Referencias

**Archivo analizado:** documento.pdf
**Estilo:** APA 7th Edition
**Fecha:** 16 de octubre de 2025

## 📊 Resumen Ejecutivo
- **Total referencias:** 25
- **Referencias válidas:** 20
- **Puntuación promedio:** 0.83/1.00
- **Cumplimiento:** 80.0%

## 🔍 Análisis Detallado
[Análisis individual de cada referencia...]
```

---

## 🧪 Casos de Uso

### 1. Evaluación de TFMs
```bash
# Validar todas las referencias de un TFM
python referencias_validator.py --archivo TFM_estudiante.pdf --estilo apa --salida validacion_tfm.json
```

### 2. Revisión de Artículos Académicos
```bash
# Validar artículo para revista IEEE
python referencias_validator.py --archivo articulo_investigacion.docx --estilo ieee
```

### 3. Corrección de Ensayos
```bash
# Validar ensayo con formato MLA
python referencias_validator.py --archivo ensayo_literatura.pdf --estilo mla --formato markdown
```

### 4. Auditoría de Tesis Doctoral
```bash
# Análisis exhaustivo de tesis doctoral
python referencias_validator.py --archivo tesis_doctoral.pdf --estilo apa --salida auditoria_completa.json
```

---

## ⚙️ Configuración Avanzada

### Personalizar Umbrales de Validación
Editar `config_referencias.py`:
```python
UMBRALES_VALIDACION = {
    "puntuacion_minima_aprobado": 0.7,
    "puntuacion_minima_excelente": 0.9,
    "porcentaje_referencias_validas_minimo": 80
}
```

### Añadir Nuevos Estilos
1. Definir patrones en `ESTILOS_CONFIGURACION`
2. Implementar validador específico en `ValidadorReferencias`
3. Añadir reglas especiales en `ValidadorFormato`

### Configurar Idiomas Adicionales
Añadir nuevas configuraciones en `IDIOMAS_CONFIGURACION`:
```python
"français": {
    "palabras_clave_referencias": ["références", "bibliographie"],
    "indicadores_autor": ["par", "auteur:"],
    # ...
}
```

---

## 🚨 Solución de Problemas

### Error: "pdfplumber no disponible"
```bash
pip install pdfplumber
```

### Error: "lxml no disponible"
```bash
pip install lxml
```

### No se detectan referencias
1. Verificar que el documento tenga sección de referencias
2. Comprobar que las palabras clave estén presentes
3. Revisar que el formato del documento sea compatible

### Validaciones incorrectas
1. Verificar que el estilo seleccionado sea correcto
2. Comprobar que las referencias sigan el formato estándar
3. Revisar la configuración en `config_referencias.py`

---

## 🔄 Integración con Otros Sistemas

### Uso como Módulo Python
```python
from referencias_validator import ValidadorReferencias, EstiloCita

# Crear validador
validador = ValidadorReferencias(EstiloCita.APA)

# Validar referencia individual
resultado = validador.validar_referencia(referencia_texto)

# Acceder a resultados
if resultado.es_completa:
    print(f"Referencia válida: {resultado.puntuacion}")
else:
    print(f"Errores: {resultado.errores}")
```

### API REST (Implementación Futura)
```python
# Endpoint propuesto
POST /api/validar-referencias
{
    "referencias": ["ref1", "ref2", ...],
    "estilo": "apa",
    "idioma": "español"
}
```

---

## 📝 Registro de Cambios

### v1.0 (Octubre 2025)
- ✅ Implementación inicial
- ✅ Soporte para APA, IEEE, MLA
- ✅ Extracción de PDF y DOCX
- ✅ Informes JSON y Markdown
- ✅ Detección automática de idioma
- ✅ Sistema modular completo

### Próximas Versiones
- 🔄 Soporte para Vancouver
- 🔄 Interfaz gráfica
- 🔄 API REST
- 🔄 Integración con Zotero/Mendeley
- 🔄 Validación de citas en texto

---

## 👥 Contribución y Soporte

### Estructura de Archivos
```
APA Report/
├── referencias_validator.py      # Módulo principal
├── config_referencias.py         # Configuración
├── utils_referencias.py          # Utilidades
├── ejemplos_uso.py              # Ejemplos y casos de uso
├── requirements_referencias.txt  # Dependencias
├── README_REFERENCIAS.md        # Esta documentación
└── [archivos de ejemplo]        # Casos de prueba
```

### Para Desarrolladores
1. **Fork** el repositorio
2. **Crear rama** para nueva funcionalidad
3. **Implementar** siguiendo estándares existentes
4. **Probar** con `ejemplos_uso.py`
5. **Documentar** cambios
6. **Pull request** con descripción detallada

### Contacto y Soporte
- **Documentación técnica**: Ver código fuente comentado
- **Casos de ejemplo**: Ejecutar `python ejemplos_uso.py`
- **Configuración**: Revisar `config_referencias.py`

---

## 🎉 Conclusión

El **Sistema Modular de Validación de Referencias** proporciona una solución completa, independiente y extensible para la validación de referencias bibliográficas en múltiples contextos académicos.

**Ventajas clave:**
- 🎯 **Precisión**: Validación específica por estilo
- 🔄 **Reutilizable**: Independiente del evaluador TFM
- 📊 **Completo**: Informes detallados y estadísticas
- 🛠️ **Extensible**: Fácil añadir nuevos estilos y funcionalidades
- 🌐 **Multiidioma**: Soporte español e inglés

**¡Listo para usar en producción!** 🚀