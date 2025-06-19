# ESBS_evaluacion_individual.py

## Documentación Técnica

### Descripción general
Este script automatiza la evaluación ultra-estricta de TFM (Trabajos Fin de Máster) en PDF, usando la API de OpenAI (GPT-4o) y una rúbrica configurable en JSON. Genera un informe en Markdown con tabla de puntuaciones y síntesis global.

### Estructura principal
- **Carga de configuración:** Lee la rúbrica y claves de puntuación desde un JSON.
- **Selección de PDF:** Usa un selector gráfico para elegir el archivo del estudiante.
- **Extracción de texto:** Extrae y tokeniza el texto del PDF.
- **Construcción del prompt:** Genera un prompt ultra-estricto con instrucciones, rúbrica y claves.
- **Llamada a OpenAI:** Envía el prompt y recibe la evaluación.
- **Parsing de resultados:** Extrae la tabla de puntuaciones y justificaciones.
- **Generación de informe:** Crea un `.md` con la tabla, síntesis y preguntas para el autor.

### Archivos clave
- `configuracion_evaluacion.json`: Rúbrica y criterios de evaluación.
- `rubrica_estructurada.json`: Estructura de la rúbrica para el prompt.
- `ESBS_evaluacion_individual.py`: Script principal.

### Principales funciones
- `cargar_configuracion(path)`: Carga el JSON de configuración.
- `construir_prompt_desde_config(...)`: Construye el prompt para el LLM.
- `EvaluadorTFM`: Clase para gestionar la llamada a OpenAI.
- `extraer_puntuaciones_tabla_md(tabla_md)`: Parsea la tabla Markdown generada por el LLM.
- `construir_tabla_evaluacion(rubrica, resultados)`: Genera la tabla final de puntuaciones.
- `save_evaluation_result(content, output_path)`: Guarda el informe `.md`.

### Personalización
- Modifica la severidad, criterios y ejemplos en `configuracion_evaluacion.json`.
- Ajusta el prompt y la lógica de parsing según necesidades de severidad o formato.

### Requisitos
- Python 3.8+
- openai >= 1.0.0
- PyPDF2, tiktoken, AppKit

---

## Guía de Usuario

### 1. Preparación
- Instala las dependencias: `pip install openai PyPDF2 tiktoken`.
- Configura tu clave OpenAI en la variable de entorno `MI_CLAVE_API_OPENAI`.
- Ajusta la rúbrica y criterios en `configuracion_evaluacion.json` según tus necesidades.

### 2. Ejecución
1. Ejecuta el script:
   ```bash
   python ESBS_evaluacion_individual.py
   ```
2. Selecciona el PDF del estudiante en el cuadro de diálogo.
3. Espera a que se genere el informe `.md` en la misma carpeta que el PDF.

### 3. Resultados
- El informe `.md` contendrá:
  - Tabla de puntuaciones por subcriterio.
  - Síntesis global.
  - Preguntas para el autor.

### 4. Consejos de uso
- Refina la severidad y los criterios en el JSON para ajustar el comportamiento del LLM.
- Si el informe no es suficientemente estricto, añade más detalle o ejemplos negativos en las claves de puntuación.
- Si hay errores de JSON, valida el archivo en https://jsonlint.com/.

### 5. Soporte
Para dudas o mejoras, consulta la documentación en el propio script o contacta con el responsable del sistema.

---

**Última actualización:** 19 de junio de 2025
