---
title: "Convercus App"
aliases:
- "Producto Convercus App"
- "Superficie de participación Convercus"
language: es
version: "v0.1"
status: "en desarrollo"
date: "2026-07-17"
project: "Convercus App"
document_type: "documento de entrada de producto"
scope: "propósito, estrategia, modos, pantallas y criterio conceptual de Convercus App"
repository_role: "índice rector del producto Convercus App"
semantic_authority: "producto subordinado a TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Convercus App

## Propósito

Convercus App es el producto prioritario del programa. Su primera entrega será una simulación mobile-first para demostrar a clientes cupones, noticias, puntos, niveles, actividad y Experiences.

## Estrategia

La aplicación se construirá directamente con Codex sobre React y TypeScript. Lovable se conserva únicamente como baseline histórica y referencia visual.

La primera demo será una instancia canónica de un sistema configurable. El horizonte es poder generar una versión personalizada a partir de una especificación estable y evolucionar después, mediante adaptadores y garantías adicionales, hacia una App operativa para clientes.

## Modos

- **Mock**: datos estables para construir y garantizar la demo.
- **Simulation**: eventos que modifican participaciones e intervenciones.
- **Staging**: integración gradual con la API real de Convercus.

## Pantallas iniciales

1. Inicio de sesión simulado.
2. Inicio personalizado.
3. Cupones.
4. Detalle y código de cupón.
5. Noticias y actividad.
6. Perfil y nivel.
7. Experiences cuando deban mostrarse explícitamente.
8. Panel interno de simulación.

## Criterio conceptual

Una Experience no se presentará necesariamente como tarjeta o reto. Puede hacerse visible mediante una intervención, noticia, recomendación, progreso, beneficio o próxima acción.

La App obedece a la baseline semántica declarada por el programa, pero requiere su propia traducción funcional de participación. No importa automáticamente entidades, operaciones ni esquemas de autoría del TES Experience Builder.

## Plan

El plan inicial de implementación se encuentra en [docs/implementation-plan.md](docs/implementation-plan.md).

- [Marco de la demo canónica](docs/canonical-demo-framework.md).
- [Protocolo inicial de especificación](docs/demo-specification-protocol.md).

## Estado

- Documentación: marco inicial incorporado.
- Prototipo: fases A0 y A1 completadas; GUI comercial mobile-first navegable.
- Presentación: modo iPhone disponible en `/showcase`; validación en dispositivo real reservada para A5.
- Datos mock: adaptador tipado, aislado y reiniciable con perfil, beneficios, noticias y actividad de demostración.
- Staging: pendiente.
