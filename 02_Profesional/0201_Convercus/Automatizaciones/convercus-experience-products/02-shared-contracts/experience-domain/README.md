---
title: "Contrato de dominio de Experiences"
aliases:
- "Dominio compartido de Experiences"
language: es
version: "v0.1"
status: "en preparación"
date: "2026-07-17"
project: "Convercus Experience Products"
document_type: "contrato funcional compartido"
scope: "entidades e invariantes de Experiences compartibles entre App y Builder"
repository_role: "contrato candidato del dominio experiencial compartido"
semantic_authority: "traducción funcional subordinada; contrato no aprobado"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Contrato de dominio de Experiences

## Estado y estatuto

Este contrato se encuentra en preparación. Su objetivo será expresar traducciones funcionales realmente compartidas sin acoplarlas a la interfaz de la App ni del Builder.

La siguiente lista es un inventario candidato, no una definición ontológica ni un contrato aprobado. Cada entidad deberá citar su procedencia semántica, clasificarse conforme a la regla de no invasión y declarar sus invariantes y pérdidas de significado antes de implementarse.

## Entidades iniciales

```text
ExperienceDefinition
ExperienceParticipation
SignificantEvent
PatternHypothesis
Sequence
ProgressionState
Intervention
Incentive
Reward
ObservedOutcome
Measurement
ReusableLearning
WorkflowReference
```

## Principio de separación

El Builder crea y modifica definiciones. La App representa participaciones. Los contratos comunes deben permitir relacionarlas sin compartir estado de interfaz.

Los esquemas TypeScript y fixtures se incorporarán cuando exista una traducción funcional trazable. Una necesidad técnica de la App no convierte por sí sola una entidad candidata en contrato compartido.
