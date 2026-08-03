---
title: "Modelo de datos de sujetos"
aliases:
- "Representación técnica del contrato de sujetos"
language: es
version: "v0.1"
status: "modelo técnico inicial"
date: "2026-07-17"
project: "TES Experience Builder"
document_type: "documentación de modelo de datos"
scope: "esquema y ejemplo técnico de sujetos para el Experience Builder"
repository_role: "entrada al modelo técnico de sujetos específico del Builder"
semantic_authority: "operacionalización técnica subordinada; no redefine TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Modelo de datos de sujetos

Los archivos de este directorio son la representación técnica inicial del contrato de sujetos del TES Experience Builder:

- [subjects.schema.json](schemas/subjects.schema.json): esquema JSON Draft 2020-12.
- [subjects.example.json](examples/subjects.example.json): ejemplo conforme al contrato.

Su estatuto es **modelo técnico específico del Builder**. Operacionaliza una baseline semántica, pero no redefine el TES y no debe reutilizarse automáticamente como modelo de la Convercus App. Si la App necesita estos datos, se diseñará una proyección funcional propia y trazable.

## Estado de migración

El esquema y el ejemplo proceden de `TES-BUILDER-2026-07` y se conservan sin modificación como artefactos técnicos heredados. La cabecera de este documento declara la baseline vigente del repositorio, `TES_CONVERCUS_BUILDER_2026_07_R1`, pero eso no migra automáticamente los artefactos. Una nueva versión del modelo deberá evaluar el núcleo ampliado, actualizar `semantic_baseline_id`, generar fixtures nuevos y registrar sus hashes sin sobrescribir los heredados.
