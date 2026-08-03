---
title: "Convercus Experience Products"
aliases:
- "Programa conjunto Convercus App y Experience Builder"
language: es
version: "v0.2"
status: "activo"
date: "2026-07-17"
project: "Convercus Experience Products"
document_type: "documento de entrada al repositorio"
scope: "arquitectura, autoridad, productos y organización general del programa"
repository_role: "índice rector del repositorio"
semantic_authority: "producto subordinado a TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Convercus Experience Products

## Propósito

Este repositorio alberga dos productos relacionados, pero independientes:

- **Convercus App**: demostrador mobile-first para clientes y futura superficie de participación.
- **TES Experience Builder**: herramienta estratégica para diseñar, simular, validar y publicar Experiences.

Ambos obedecen al TES, sistema ontológico y editorial externo al repositorio. El repositorio no contiene ni gobierna el núcleo TES: incorpora solamente derivaciones controladas, congeladas y versionadas mediante un contrato semántico de producto.

## Cadena de autoridad y traducción

```text
TES — autoridad ontológica y editorial externa
        │
        │ derivación controlada, trazable y versionada
        ▼
Contrato semántico de producto
        │
        │ traducción funcional explícita
        ▼
Convercus App / TES Experience Builder
        │
        ├── modelo funcional
        ├── modelo de interacción
        ├── modelo de datos
        ├── prototipo
        └── integraciones técnicas
```

El producto nunca depende de una idea abstracta de «la última versión del TES». Cada versión declara la baseline semántica contra la que fue construida. Un cambio del TES abre una evaluación de impacto; no modifica automáticamente el producto.

## Relación operativa entre productos

```text
TES Experience Builder
  diseña y valida
        ↓
Workflows
  ejecutan parte de la orquestación
        ↓
Convercus App
  hace visible y vivible la participación
```

La App es la prioridad inmediata. El Builder se conserva como línea estratégica y no debe bloquear la demo.

## Estructura actual

```text
convercus-experience-products/
├── 00-governance/          # autoridad, límites y procesos de cambio
├── 01-semantic-contract/   # derivación TES congelada y trazable
├── 02-shared-contracts/    # traducciones funcionales compartidas
├── 03-shared-assets/       # activos realmente reutilizables
├── products/
│   ├── convercus-app/
│   └── experience-builder/
└── archive/
```

## Referencias de gobierno

1. [Precedencia de fuentes](00-governance/source-precedence.md).
2. [Límites y niveles de producto](00-governance/product-boundaries.md).
3. [Proceso de cambio semántico](00-governance/semantic-change-process.md).
4. [Retorno de observaciones al TES](00-governance/tes-observation-process.md).
5. [Baseline del contrato semántico](01-semantic-contract/README.md).
6. [Arquitectura conjunta](00-governance/program-architecture.md).
7. [Relación funcional con Workflows](02-shared-contracts/workflows-relationship.md).

## Estado

- Gobernanza TES–producto: incorporada.
- Baseline semántica vigente: `TES_CONVERCUS_BUILDER_2026_07_R1`.
- Baseline histórica preservada: `TES-BUILDER-2026-07`.
- Convercus App: A0 y A1 completadas; GUI mobile-first navegable con datos mock y modo de presentación iPhone.
- TES Experience Builder: contrato de sujetos y modelo técnico inicial incorporados.
- Validación en iPhone real: comprometida para A5; el marco visual actual no sustituye pruebas en dispositivo.
- Conexión con staging: pendiente.
