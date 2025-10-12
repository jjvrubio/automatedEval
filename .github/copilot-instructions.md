# Guía para Copilot en este repositorio

## Propósito del repositorio
Este repositorio contiene scripts y herramientas para automatizar tareas relacionadas con la evaluación de trabajos finales de máster (TFM), cumplimiento de normas APA, y otros procesos de automatización. Además, incluye configuraciones específicas para entornos macOS y scripts para la integración con servicios como OneDrive.

## Estructura del repositorio
- **`automatedEval/`**: Scripts relacionados con la evaluación automatizada de TFMs.
  - **`APA Report/`**: Scripts para verificar el cumplimiento de normas APA.
  - **`function_call_agent/`**: Funciones auxiliares para agentes de IA.
  - **`Grading/`**: Herramientas para calificación automatizada.
- **`METIS® Growth/`**: Scripts relacionados con análisis de crecimiento y métricas.
- **`publicando/`**: Herramientas para publicar contenido en plataformas como Substack y LinkedIn.
- **`venv_arm64/` y **`venv_intel/`**: Entornos virtuales para Python en arquitecturas ARM e Intel.

## Convenciones de codificación
- **Estilo de código**: Sigue las convenciones de PEP 8 para Python.
- **Nombres de archivos**: Utiliza nombres descriptivos y en inglés.
- **Documentación**: Cada script debe incluir comentarios claros y un encabezado con su propósito.

## Dependencias
Las dependencias de Python están listadas en `requirements.txt`. Usa el entorno virtual adecuado (`venv_arm64` o `venv_intel`) dependiendo de tu arquitectura.

## Tareas comunes
- **Ejecutar scripts**: Activa el entorno virtual correspondiente y ejecuta el script deseado.
- **Evaluar TFMs**: Usa los scripts en `automatedEval/` para análisis automatizado.
- **Publicar contenido**: Sigue las instrucciones en `publicando/` para publicar en plataformas específicas.

## Notas para Copilot
- **Contexto**: Este repositorio incluye scripts para tareas específicas. Asegúrate de entender el propósito de cada script antes de sugerir cambios.
- **Integración con macOS**: Algunos scripts dependen de herramientas específicas de macOS como `mdls` y `xattr`.
- **OneDrive**: Ten en cuenta los problemas conocidos con archivos de OneDrive al trabajar con Python.

## Contacto
Para preguntas o soporte, contacta al mantenedor del repositorio.
