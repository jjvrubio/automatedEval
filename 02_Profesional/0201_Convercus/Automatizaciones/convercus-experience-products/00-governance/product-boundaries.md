---
title: "Límites ontológicos, funcionales y técnicos"
aliases:
- "Límites de producto Convercus Experience Products"
language: es
version: "v0.1"
status: "activo"
date: "2026-07-17"
project: "Convercus Experience Products"
document_type: "política de gobernanza"
scope: "separación de autoridad TES, traducción funcional, implementación técnica y responsabilidades de producto"
repository_role: "norma de no invasión y delimitación entre productos"
semantic_authority: "producto subordinado a TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Límites ontológicos, funcionales y técnicos

## Regla de no invasión

> El TES Experience Builder y Convercus App no crean, redefinen ni corrigen conceptos ontológicos del TES.

Toda entidad, campo o componente introducido en el repositorio debe clasificarse como una de estas categorías:

1. derivación directa de un concepto TES;
2. traducción funcional de varios conceptos TES;
3. construcción propia del producto;
4. capacidad técnica;
5. elemento de interfaz.

La clasificación debe quedar en su contrato, decisión o especificación. Las construcciones propias del producto no adquieren por ello estatuto ontológico dentro del TES.

## Tres niveles de decisión

### Nivel ontológico TES

Responde qué son una acción situada, una Experience, un ecosistema, una secuencia, un arquetipo, la progresión o la medición. Su autoridad pertenece exclusivamente al TES.

### Nivel funcional de producto

Responde qué introduce el diseñador, qué guarda el sistema, qué aparece en el inspector, qué puede conectarse, qué se valida, qué se simula y qué es obligatorio. Gobierna la especificación de cada producto, bajo obediencia al contrato semántico.

### Nivel técnico

Responde qué JSON representa una entidad, qué campos son obligatorios, qué eventos llegan por API, qué reglas pueden ejecutarse y qué requiere middleware. Gobiernan el modelo de datos, las capacidades verificadas de plataforma y la arquitectura técnica.

## Límites entre productos

### Convercus App

Pertenece a la App la participación vivida: perfil, puntos, niveles, cupones, beneficios, noticias, intervenciones, próximas acciones, progresión visible y simulación de demos.

No pertenece a la App crear definiciones ontológicas, editar Workflows, publicar Experiences ni importar automáticamente el modelo de autoría del Builder.

### TES Experience Builder

Pertenece al Builder la traducción funcional que permite formular, diseñar, simular, validar, mapear a Workflows, publicar y versionar Experiences.

No pertenece al Builder gobernar el TES, convertir candidatos en canon, ser la aplicación cotidiana del miembro ni equiparar una Experience con un Workflow.

## Base compartida

Solo se comparten de forma deliberada contratos semánticos congelados, identificadores, escenarios, contratos de integración y activos realmente comunes. No se comparten por defecto navegación, estado de interfaz, componentes complejos, operaciones, permisos ni esquemas técnicos específicos de un producto.

La App puede simular participaciones sin que el Builder esté implementado. El Builder puede diseñar definiciones sin depender de componentes de la App.
