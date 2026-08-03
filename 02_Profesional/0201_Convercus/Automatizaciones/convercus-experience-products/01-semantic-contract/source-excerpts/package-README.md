---
title: "Paquete de cristalización v0.2"
language: es
version: "v0.2"
status: "listo para integrar"
date: "2026-07-16"
project: "TES Experience Builder"
---

# TES Experience Builder — Paquete de cristalización v0.2

Este paquete está preparado para descomprimirse directamente en la raíz del repositorio independiente del TES Experience Builder.

## Contenido

- `01-contrato-semantico/01-guia-contrato-semantico.md`  
  Guía rectora del contrato semántico: niveles atómico, relacional y operativo.

- `01-contrato-semantico/02-subjects-contract.md`  
  Contrato completo del dominio Sistema de sujetos para la baseline v0.5.

- `08-data-model/schemas/subjects.schema.json`  
  JSON Schema inicial del sistema de sujetos.

- `08-data-model/examples/subjects.example.json`  
  Ejemplo válido de persistencia.

## Integración

Descomprimir el ZIP en la raíz del repositorio. El archivo no contiene una carpeta contenedora adicional.

```text
<repo>/
├── README.md
├── 01-contrato-semantico/
│   ├── 01-guia-contrato-semantico.md
│   └── 02-subjects-contract.md
└── 08-data-model/
    ├── schemas/
    │   └── subjects.schema.json
    └── examples/
        └── subjects.example.json
```
