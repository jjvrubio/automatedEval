---
title: "Precedencia de fuentes"
aliases:
- "Jerarquía de autoridad TES y producto"
language: es
version: "v0.1"
status: "activo"
date: "2026-07-17"
project: "Convercus Experience Products"
document_type: "política de gobernanza semántica"
scope: "orden de autoridad entre TES, contrato semántico, modelos de producto, interfaz y técnica"
repository_role: "regla superior de interpretación del repositorio"
semantic_authority: "producto subordinado a TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Precedencia de fuentes

## Principio de autoridad

El TES es un sistema ontológico y editorial autónomo, externo a este repositorio. Mantiene en exclusiva la autoridad para crear, definir, distinguir, revisar o retirar conceptos ontológicos.

El contrato semántico del producto es una derivación controlada del TES: fija qué definiciones y relaciones adopta una versión del producto, pero no sustituye al TES ni adquiere autoridad sobre él.

## Orden de precedencia

Cuando exista conflicto se aplica, sin excepciones silenciosas, este orden:

```text
Definición ontológica TES
        >
Contrato semántico de producto
        >
Modelo funcional
        >
Modelo de interacción
        >
Representación visual
        >
Conveniencia técnica
```

Las decisiones registradas pueden resolver cómo obedece el producto a una fuente superior, pero no pueden invertir esta precedencia ni redefinir el TES.

## Reglas de interpretación

- Una maqueta no redefine el dominio.
- Un dato mock no confirma una capacidad de API.
- Un endpoint no define por sí mismo el significado de una entidad.
- Un Workflow no equivale por sí mismo a una Experience.
- Una agrupación visual no fusiona entidades del modelo.
- Una construcción propia del producto no adquiere estatuto ontológico.
- Una fuente TES más reciente no sustituye automáticamente la baseline congelada del producto.
- Las contradicciones, pérdidas de significado y mediaciones se registran y versionan.

## Cuando el significado no puede implementarse directamente

El producto debe adoptar una de estas decisiones y documentarla:

1. declarar la limitación;
2. introducir una mediación explícita;
3. reducir el alcance;
4. marcar la capacidad como no soportada.

No debe fingir una equivalencia falsa por conveniencia visual o técnica.

## Ubicación de la autoridad externa

El corpus TES continúa fuera del repositorio. La procedencia concreta de cada extracto aceptado se registra en el [manifiesto de baseline](../01-semantic-contract/tes-baseline-manifest.yaml). El directorio fuente actualmente utilizado es:

```text
/Users/juanjo/Library/CloudStorage/OneDrive-ConvercusGmbH/Convercus/CX experience builder
```
