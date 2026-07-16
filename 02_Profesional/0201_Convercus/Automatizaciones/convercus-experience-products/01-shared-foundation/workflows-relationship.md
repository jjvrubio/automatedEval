# Relación entre Experiences y Workflows

## Distinción principal

**Experiences** es la funcionalidad de Convercus que configura y gobierna transformaciones situadas. **Workflows** proporciona parte de la capacidad técnica utilizada para ejecutar su orquestación.

```text
Experience
├── transformación y patrón
├── secuencia y progresión
├── resultado, medición y aprendizaje
└── ejecutabilidad
    └── uno o varios Workflows
```

## Workflow

Un Workflow puede aportar:

- Disparadores.
- Condiciones.
- Transiciones.
- Acciones.
- Intervenciones.
- Integración con otros servicios.

Una automatización o un Workflow complejo no constituye automáticamente una Experience.

## Experience Builder

El Builder debe permitir diseñar en lenguaje de experiencia y traducir o mapear esa definición a capacidades de Workflows sin exponer innecesariamente su complejidad técnica.

## Convercus App

La App consume los efectos de la orquestación:

- Estado de participación.
- Próxima acción.
- Intervenciones.
- Progresión.
- Incentivos y recompensas.
- Resultados visibles.

La App no necesita presentar el Workflow al cliente. El panel interno de simulación sí podrá mostrarlo con fines de demostración y diagnóstico.

## Estado técnico

La documentación Swagger revisada no expone todavía un servicio identificado claramente como Experiences o Workflows. La integración real queda pendiente de localizar y verificar su contrato técnico.
