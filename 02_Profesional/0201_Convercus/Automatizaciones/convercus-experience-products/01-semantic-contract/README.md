---
title: "Contrato semántico de producto"
aliases:
- "Baseline semántica de Convercus Experience Products"
language: es
version: "v0.1"
status: "activo"
date: "2026-07-17"
project: "Convercus Experience Products"
document_type: "índice de contrato semántico"
scope: "derivación TES mínima, controlada y versionada utilizable por los productos"
repository_role: "entrada al contrato semántico de producto"
semantic_authority: "derivación controlada; TES conserva la autoridad ontológica"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Contrato semántico de producto

## Estatuto

Este directorio contiene la derivación TES mínima, controlada y versionada que pueden utilizar los productos. No contiene el núcleo completo del TES y no posee autoridad para modificarlo.

La baseline vigente es `TES_CONVERCUS_BUILDER_2026_07_R1`, congelada el 17 de julio de 2026. Su composición, aplicabilidad y procedencia se declaran en [tes-baseline-manifest.yaml](tes-baseline-manifest.yaml).

La baseline histórica `TES-BUILDER-2026-07`, congelada el 16 de julio de 2026, se conserva sin modificación en [tes-baseline-manifest.TES-BUILDER-2026-07.yaml](tes-baseline-manifest.TES-BUILDER-2026-07.yaml). La denominación **TES Convercus Builder** designa el marco de construcción de productos y capacidades sobre Convercus; no equivale al producto específico **TES Experience Builder**.

## Contenido

- `source-excerpts/`: copias verificables e inmutables de los documentos seleccionados del paquete de cristalización v0.2.
- `product-interpretations/`: explicaciones de trabajo subordinadas al contrato, útiles para diseño y comunicación.
- `semantic-impact-log.md`: evaluaciones de cambios TES posteriores.
- `product-observations-log.md`: evidencia que el producto puede devolver a la gobernanza TES.

## Uso

Una traducción funcional debe citar el concepto o invariante del contrato del que deriva, declarar su categoría conforme a la regla de no invasión y explicitar pérdidas, mediaciones o capacidades no soportadas.

El contrato de sujetos incorporado pertenece inicialmente al TES Experience Builder. Su esquema JSON se conserva en el área técnica de ese producto; no se convierte automáticamente en contrato de la Convercus App.
