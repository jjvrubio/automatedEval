# Convercus Experience Products

## Propósito

Este directorio gobierna dos productos relacionados, pero distintos:

- **Convercus App**: demostrador mobile-first para clientes y futura superficie de participación.
- **Experience Builder**: herramienta estratégica para diseñar, simular, validar y publicar Experiences.

Ambos productos comparten el fundamento de Experiences, contratos de dominio, escenarios y referencias técnicas. No comparten automáticamente navegación, estados de interfaz ni componentes específicos.

## Relación entre productos

```text
Experience Builder
  diseña y valida
        ↓
Workflows
  ejecuta la orquestación
        ↓
Convercus App
  hace visible y vivible la participación
```

La App es la prioridad inmediata. El Builder se conserva como línea estratégica y no debe bloquear el desarrollo de la demo.

## Estructura actual

```text
convercus-experience-products/
├── 00-governance/
├── 01-shared-foundation/
├── 02-shared-contracts/
├── 03-shared-assets/
├── products/
│   ├── convercus-app/
│   └── experience-builder/
└── archive/
```

La estructura crecerá únicamente cuando exista trabajo real que depositar en cada área.

## Fuentes principales

1. [Definición conceptual de Experiences](01-shared-foundation/experience-definition.md).
2. [Arquitectura conjunta de los dos productos](00-governance/program-architecture.md).
3. [Límites de producto](00-governance/product-boundaries.md).
4. [Precedencia de fuentes](00-governance/source-precedence.md).
5. [Relación con Workflows](01-shared-foundation/workflows-relationship.md).

## Estado

- Estructura de programa: iniciada.
- Convercus App: preparada para comenzar implementación.
- Experience Builder: baseline v0.4.1 identificada y pendiente de incorporación controlada.
- Conexión con staging: pendiente.

## Próximo hito

Crear el prototipo de Convercus App en una rama de implementación independiente, comenzando con datos mock y un escenario canónico completamente simulable.
