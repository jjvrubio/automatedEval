---
title: "ADR-004 — Separación de Experience Definition, Scenario y Demo Script"
aliases:
- "Separation of Experience Definition, Scenario and Demo Script"
language: es
version: "v1.0"
status: "aceptado"
date: "2026-09-04"
project: "Convercus Experience Products"
document_type: "registro de decisión de arquitectura"
scope: "separación de definición semántica, contexto situado y orquestación de demostración"
repository_role: "decisión de arquitectura de Demo Factory"
semantic_authority: "construcción técnica de producto subordinada; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
decision_id: "ADR-004"
decision_status: "accepted"
---

# ADR-004 — Separación de Experience Definition, Scenario y Demo Script

## Estado

**Aceptado.**

## Contexto

Demo Factory necesita representar tres responsabilidades relacionadas pero distintas:

- **Experience Definition:** definición semánticamente gobernada de una Experience, trazable a TES.
- **Scenario:** contexto situado de la demo. Puede aportar actores, roles, referencias de sujetos y contexto, condiciones iniciales, referencias a Experiences relevantes, fixture o checkpoint y límites permitidos de interacción de demo cuando sean necesarios.
- **Demo Script:** orquestación orientada al presentador. Puede aportar pasos ordenados, texto o instrucciones, referencias a acciones públicas, checkpoints o resultados de demo esperados y orientación de recuperación.

Antes de Session 7 esas responsabilidades existían como artefactos separados, pero no había evidencia de que un Script pudiera provocar comportamiento visible sin adquirir acceso directo al estado o convertirse en controlador. El experimento Hospitality añadió una sola acción pública, validada por el runtime, que lleva un checkpoint local de `pre-arrival-confirmed` a `checked-in` y deriva una entrada de Activity. La UI invoca esa acción a partir del Script; no conoce el identificador de acción, la transición ni la narrativa Hospitality.

La evidencia demuestra la viabilidad de la separación para ese camino mínimo. No demuestra que las formas TypeScript actuales sean modelos generales.

## Decisión

Demo Factory mantendrá la siguiente dependencia conceptual:

```text
Experience Definition
        ↑ referenced/instantiated by
Scenario
        ↑ demonstrated through
Demo Script
```

La interacción operacional seguirá exclusivamente este recorrido:

```text
Demo Script
      ↓
Public Action
      ↓
Runtime Boundary
      ↓
Controlled Runtime Transition
      ↓
Read Model / UI
```

Experience Definition gobierna significado; Scenario sitúa una demostración; Demo Script organiza cómo presentarla. El runtime conserva la autoridad operacional sobre acciones y estado mutable.

## Responsabilidades y límites obligatorios

### Experience Definition

Experience Definition puede declarar significado, relaciones e invariantes de una Experience de acuerdo con la baseline TES aplicable. Debe poder distinguirse y trazarse independientemente de los contextos y guiones que la utilicen.

Experience Definition no debe poseer:

- instrucciones para el presentador;
- narrativa específica de un prospecto, salvo que sea semánticamente intrínseca;
- estado de UI;
- checkpoints de demo;
- acciones de presentador.

### Scenario

Scenario aporta contexto situado y puede declarar el límite de interacción permitido para esa demo. Puede referenciar una Experience, pero no adquiere autoridad para redefinirla.

Scenario no debe:

- redefinir la semántica TES de Experience;
- convertirse en un motor genérico de workflow;
- implementar TES Progression o Result;
- absorber la narración del presentador por conveniencia;
- trasladar al dato declarativo reglas mutables que pertenecen al runtime.

### Demo Script

Demo Script identifica qué se demuestra y qué acción pública debe solicitarse. Puede declarar una expectativa observable para que composición y presentación se validen, pero esa expectativa no ejecuta ni autoriza por sí misma la transición.

Demo Script no debe:

- mutar directamente estado interno u oculto del runtime;
- implementar reglas de Experience;
- implementar recompensa, Progression o Result;
- eludir la validación del runtime;
- convertirse en un segundo controlador de la aplicación.

### Runtime

El runtime debe:

- ofrecer un límite público para las acciones permitidas;
- validar la identidad de la acción y su legalidad respecto al estado efectivo;
- poseer las transiciones de estado mutable;
- fallar explícitamente o devolver un resultado controlado ante una acción ilegal;
- exponer el estado resultante mediante read models o proyecciones;
- mantener la fuente operacional separada de su representación en Activity o UI.

## Cualificación de checkpoint

```text
Demo checkpoint != TES Experience Progression / Result / Completion
```

Esta desigualdad es obligatoria salvo que evidencia semántica validada y evidencia ejecutable futuras establezcan explícitamente otra relación. Los checkpoints Hospitality actuales son construcciones locales del runtime de demo. Sus nombres no los convierten en estados de Experience ni en afirmaciones TES.

## Relación con composición

Scenario, Experience Definition y Demo Script conservan identidad separada y pueden ser referenciados por la composición deseada definida en ADR-003. Bootstrap resuelve y valida sus referencias antes del render. La aplicación consume la composición efectiva y utiliza la frontera pública; no debe reconstruir la relación ni interpretar internamente el Script.

## Alcance excluido

Session 7 y este ADR no establecen:

- motores genéricos de scripts;
- ejecución multi-step;
- máquinas de estados arbitrarias;
- branching;
- grafos genéricos de checkpoints;
- varios Scripts concurrentes;
- participación colectiva en una Experience;
- evaluación de Experience;
- TES Progression, Result o Completion;
- semántica reutilizable de workflow;
- la forma final de identificadores, checkpoints, transiciones o errores;
- reutilización ya probada entre varios Scenarios o Scripts.

La transición singular y el uso de `steps[0]` son restricciones del experimento, no arquitectura promovida.

## Consecuencias

### Positivas

- Una misma Experience puede conservar significado independiente de una narración de venta concreta.
- El Scenario puede cambiar el contexto sin convertir el Script en fuente semántica.
- La presentación solicita comportamiento sin acceso privilegiado al estado interno.
- La validación y las transiciones permanecen testeables fuera de React.
- Read models y Activity pueden reflejar el resultado sin adquirir autoridad factual.
- Es posible cambiar UI, copy o secuencia de presentación sin redefinir Experience.

### Costes y obligaciones

- Las referencias entre artefactos necesitan validación y gobierno de versiones.
- El runtime debe ofrecer errores o resultados públicos suficientemente legibles.
- Las expectativas del Script y las transiciones permitidas del Scenario deben comprobarse sin duplicar reglas.
- Los nombres de checkpoints deben evitar interpretaciones semánticas no demostradas.
- La futura reutilización debe probarse empíricamente antes de generalizar cardinalidades o motores.

## Interpretaciones prohibidas

Este ADR no implica que:

- Scenario sea la ejecución de una Experience;
- Demo Script sea un workflow o command bus;
- un checkpoint represente progreso, resultado o finalización TES;
- una acción del presentador constituya por sí misma evidencia factual o un TES Event;
- Activity sea la fuente de verdad del cambio;
- todos los Scenarios necesiten acciones o checkpoints;
- todos los Scripts necesiten pasos ejecutables;
- la representación actual de un solo `presenterAction` sea normativa;
- `actionId` o checkpoint deban permanecer como strings libres;
- la frontera pública actual constituya una arquitectura multi-provider.

## Evidencia de aceptación

- Hospitality declara una única acción `confirm-arrival` en Scenario y la referencia desde el único paso del Demo Script.
- La acción del Script contiene identidad y evidencia, pero no contiene `fromCheckpoint` ni `toCheckpoint`.
- `DemoProvider.executeAction` constituye una frontera pública fuera de React.
- `MockDataAdapter` valida la acción y el checkpoint vigente antes de mutar estado.
- El adapter posee la transición y publica el checkpoint resultante mediante `AppSnapshot`.
- La acción añade un registro fuente y Activity se deriva mediante proyección.
- Las pruebas verifican el estado inicial, transición determinista, rechazo explícito de repetición, reset e independencia de Retail.
- La prueba de UI verifica invocación desde `/system`, estado resultante y Activity visible.
- La implementación no introduce tipos ni cálculos de TES Progression, Result o Completion.

Esta evidencia respalda la separación y la frontera. Un único Scenario, un único Script y un único paso no respaldan todavía reutilización general.

## Condiciones de reconsideración

La decisión se revisará si:

1. Scenario necesita codificar semántica sustancial de workflow o reglas;
2. Demo Script necesita acceso directo al estado interno para cumplir su función;
3. varios Scripts para un Scenario no pueden coexistir sin redefinir el Scenario;
4. lógica de ejecución específica de Experience migra al Script;
5. los checkpoints empiezan a funcionar como estados implícitos de Experience;
6. el mismo comportamiento útil puede representarse de forma más simple sin la separación triple;
7. la validación de referencias produce duplicación inevitable de reglas entre Scenario, Script y runtime;
8. nueva evidencia TES invalida la frontera semántica aquí establecida.
