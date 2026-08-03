---
title: "Proceso de cambio semántico"
aliases:
- "Evaluación de cambios TES en producto"
language: es
version: "v0.1"
status: "activo"
date: "2026-07-17"
project: "Convercus Experience Products"
document_type: "proceso de gobernanza semántica"
scope: "evaluación, decisión y trazabilidad de cambios TES frente a la baseline de producto"
repository_role: "procedimiento obligatorio de cambio semántico"
semantic_authority: "producto subordinado a TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Proceso de cambio semántico

## Regla general

El producto utiliza una baseline TES identificada y congelada. No sigue automáticamente «la última versión» del TES. Un cambio externo inicia una evaluación y solo llega al producto mediante una nueva decisión versionada.

## Evaluación de impacto

Para cada cambio TES se responderá:

1. ¿Ha cambiado una definición relevante?
2. ¿Afecta a alguna entidad del producto?
3. ¿Afecta a alguna pantalla o interacción?
4. ¿Afecta al modelo de datos?
5. ¿Exige una migración?
6. ¿O no tiene impacto funcional?

## Resultados posibles

- `no_impact`: se conserva la baseline y se documenta la evaluación.
- `clarification_only`: se aclara el contrato sin cambio funcional, con versión y trazabilidad.
- `functional_change`: se modifica una traducción funcional.
- `interaction_change`: se adapta una interacción o representación.
- `data_migration`: se diseña y valida una migración explícita.
- `unsupported`: el producto declara que todavía no puede representar la definición.
- `deferred`: se mantiene la baseline vigente hasta una revisión posterior.

## Registro mínimo

Cada evaluación debe indicar identificador, fecha, fuente TES y versiones, baseline actual, conceptos afectados, impacto por producto, decisión, responsable y referencias a cambios o migraciones. El historial se conserva en [semantic-impact-log.md](../01-semantic-contract/semantic-impact-log.md).

Las referencias TES almacenadas en datos nunca se migran de forma automática solo porque aparezca una versión más reciente.
