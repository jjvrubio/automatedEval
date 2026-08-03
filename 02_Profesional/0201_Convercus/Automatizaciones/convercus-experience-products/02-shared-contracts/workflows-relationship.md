---
title: "Relación entre Experiences y Workflows"
aliases:
- "Mapeo funcional Experiences–Workflows"
language: es
version: "v0.1"
status: "borrador de traducción funcional"
date: "2026-07-17"
project: "Convercus Experience Products"
document_type: "traducción funcional compartida"
scope: "distinción y relación ejecutiva entre Experiences y capacidades de Workflows"
repository_role: "marco de integración funcional sujeto a verificación técnica"
semantic_authority: "traducción funcional subordinada; no es definición TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Relación entre Experiences y Workflows

## Clasificación

Este documento es una **traducción funcional** apoyada en capacidades técnicas de Workflows. No es una definición ontológica TES. La premisa de producto confirmada es que Experiences utiliza la parte de la API relacionada con Workflows; el mapeo exacto debe verificarse técnicamente antes de implementarse.

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

La integración real queda pendiente de localizar y verificar contra el contrato técnico de staging. Hasta entonces no se inferirán nombres de endpoint, payloads ni capacidades ejecutables a partir de la relación conceptual.
