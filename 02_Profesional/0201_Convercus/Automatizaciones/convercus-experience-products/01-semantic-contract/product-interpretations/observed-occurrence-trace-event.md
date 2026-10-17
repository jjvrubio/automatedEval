---
title: "Ocurrencia observada, traza y Evento TES"
aliases:
- "Observed Occurrence, Trace and TES Event"
language: es
version: "v0.1"
status: "Product interpretation subordinate to TES — not a TES extension."
date: "2026-09-03"
project: "Convercus Experience Products"
document_type: "interpretación conceptual de producto"
scope: "distinción de producto entre Activity, ocurrencias observables, trazas y Eventos TES"
repository_role: "interpretación compartida para Demo Factory"
semantic_authority: "interpretación de producto subordinada a TES; no es una extensión de TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Ocurrencia observada, traza y Evento TES

> [!important] Product interpretation subordinate to TES — not a TES extension.
> Este documento registra una interpretación de producto subordinada a TES. No modifica, corrige ni extiende TES, y no introduce nuevas etapas en el Experience Ledger. Ante cualquier contradicción, prevalecen TES y la gobernanza semántica vigente.

## Propósito y alcance

Demo Factory debe **adaptar la capa de producto** a una distinción que ya está contenida en TES: no todo hecho observable es un Evento significativo. El trabajo requerido pertenece, por tanto, a la representación, instrumentación, reconstrucción y presentación del producto; no consiste en corregir ni ampliar TES.

Este documento proporciona vocabulario provisional para impedir que la arquitectura de producto confunda:

- aquello que puede observar o recibir técnicamente;
- la evidencia que permite reconstruir lo ocurrido;
- el reconocimiento contextual de un Evento dentro de una Experience;
- la proyección que la aplicación presenta como Activity.

Los términos técnicos introducidos aquí no adquieren por ello autoridad ontológica.

## Distinción establecida por TES

TES establece que no todo hecho observable es un Evento significativo. La significación de un Evento depende de la diferencia relevante que produce en una situación y debe poder comprenderse dentro de una Experience.

Por ello, la significación TES no debe modelarse como una propiedad intrínseca, incondicional y universal de todo hecho que un sistema observe. Una misma ocurrencia puede resultar relevante en el contexto de una Experience y no serlo en otro contexto.

La capa de producto no debe etiquetar de antemano toda compra, visita, reserva, clic, transacción, actualización o señal técnica como Evento TES por el mero hecho de haberla recibido o almacenado.

## Observed Occurrence como constructo de producto

Para fines de producto y arquitectura técnica, Demo Factory puede representar provisionalmente un hecho observable como `Observed Occurrence`.

`Observed Occurrence` designa un registro neutral de que algo observable ha ocurrido o ha sido comunicado al sistema. Puede conservar, según las necesidades técnicas, identidad, tipo, tiempo, procedencia, propiedades, correlación, fiabilidad o estado de recepción.

`Observed Occurrence` es un **constructo de producto/técnico**, no una nueva entidad TES. Su introducción no altera la definición TES de Evento ni añade un estadio al Experience Ledger.

Una ocurrencia observada no implica por sí sola:

- que exista una Experience aplicable;
- que haya sido reconocido un Evento TES;
- que emerja un Pattern;
- que se haya producido una transición o Progression;
- que exista Completion o Result;
- que deba concederse un Incentive o Reward.

## Trace como evidencia de reconstrucción

Una `Trace` pertenece al plano de instrumentación y reconstrucción. Proporciona evidencia de que una ocurrencia, condición o transición tuvo lugar, o de que fue registrada por una fuente concreta.

La traza puede respaldar el reconocimiento o la confirmación contextual, pero **Trace y Evento TES no son equivalentes**. La presencia de una traza no garantiza significación experiencial, y la arquitectura no debe elevar automáticamente cada traza al estatus de Evento TES.

Tampoco debe asumirse que una única traza basta siempre para reconstruir lo ocurrido. Una ocurrencia puede producir varias trazas; una traza puede ser parcial, duplicada, tardía o contradictoria; y la confirmación de una condición o transición puede requerir más de una evidencia. Estas posibilidades son consideraciones de producto e instrumentación, no nuevas reglas ontológicas de TES.

## Reconocimiento contextual relativo a Experiences

La significación de un Evento TES es contextual a una Experience. La arquitectura de producto debe preservar la posibilidad de evaluar una ocurrencia observada en relación con el contexto, estado, reglas y secuencia de cada Experience potencialmente aplicable.

Una arquitectura de producto puede necesitar que una misma ocurrencia observada sea evaluada en relación con:

- cero Experiences;
- una Experience;
- múltiples Experiences.

Esta cardinalidad es una **interpretación de producto fuertemente compatible con TES**, no una regla explícita de cardinalidad establecida por TES. En particular, no autoriza a declarar que una ocurrencia pertenezca semánticamente a varias Experiences sin evaluación contextual independiente.

La recepción de una ocurrencia tampoco produce automáticamente Progression. El reconocimiento contextual debe determinar si existe un Evento relevante y qué papel desempeña, si alguno, dentro de la Experience correspondiente.

## Dos planos que deben preservarse

La arquitectura debe mantener separados los siguientes planos:

### Instrumentación / reconstrucción

```text
Observed Occurrence → Trace → contextual recognition / confirmation
```

### Plano experiencial TES

```text
Event → Pattern → Sequence → Progression → Result → Measurement → Learning
```

El plano de instrumentación/reconstrucción puede alimentar el plano experiencial TES, pero **no debe insertarse en el TES Experience Ledger como etapas ontológicas adicionales**. `Observed Occurrence` y `Trace` ayudan al producto a observar, conservar evidencia y reconstruir; no redefinen cómo TES desarrolla una Experience.

## Pattern y colecciones de ocurrencias

`Pattern` debe conservar su significado TES: la regularidad que emerge de relaciones entre Eventos.

Una colección, acumulación o traza de ocurrencias no es automáticamente un Pattern. El volumen, la repetición o la coexistencia de registros no bastan por sí solos para establecer la regularidad experiencial relevante.

La capa de producto debe evitar que una consulta agregada, una lista cronológica o una coincidencia técnica se presenten como Pattern sin la interpretación y relación requeridas por TES.

## Activity como proyección de lectura

`Activity` debe tratarse como un **read model o proyección de presentación**, no como una fuente semántica o factual soberana.

Activity puede combinar, ordenar y presentar elementos derivados de ocurrencias, trazas, Eventos reconocidos, transiciones, intervenciones, incentivos, recompensas o resultados. Esa utilidad de presentación no convierte el feed de Activity en la autoridad sobre lo que ocurrió ni sobre lo que significa dentro de una Experience.

Las decisiones visuales o editoriales —por ejemplo, título, descripción, icono, tono, agrupación o fecha formateada— pertenecen a la proyección. No deben utilizarse como evidencia canónica ni como sustituto de la ocurrencia, la traza o la evaluación contextual.

## Distinciones que no deben colapsarse

La arquitectura y el lenguaje de producto no deben equiparar:

- acumulación de ocurrencias con Pattern;
- acumulación de ocurrencias con Sequence;
- Pattern con Sequence;
- Sequence con Progression;
- Progression con Completion;
- Completion con Result;
- Incentive con Reward;
- Incentive o Reward con Result;
- ocurrencia observable o Trace con Evento TES.

Cada concepto conserva su función y sus condiciones propias. La proximidad temporal, una representación común en Activity o la presencia dentro del mismo escenario de demo no justifican su fusión.

## Analytical hypothesis — coverage

`coverage` está inspirado por la teoría de cobertura de conjuntos y **NO es un concepto TES**. Su posible utilidad pertenece al análisis de producto y debe mantenerse fuera del vocabulario ontológico de TES salvo revisión formal motivada por evidencia.

### A. Observed-field coverage

Dado un universo de ocurrencias observadas `U` y subconjuntos `S_E` asociados con Experiences, las uniones, intersecciones y elementos no cubiertos pueden resultar útiles para analizar:

- solapamiento entre Experiences;
- redundancia aparente;
- porciones del comportamiento observable no relacionadas con ninguna Experience;
- concentración o dispersión de la observación entre Experiences.

La asociación de una ocurrencia con un subconjunto `S_E` presupone un criterio de evaluación de producto; no convierte la pertenencia matemática en reconocimiento automático de un Evento TES.

### B. Experience evidence/requirement coverage

El grado en que se han satisfecho las evidencias o los requisitos estructurales de una Experience es un problema analítico diferente. Puede referirse, por ejemplo, a qué evidencias requeridas están disponibles o qué condiciones han sido confirmadas.

Esta cuestión no debe confundirse con la cobertura de conjuntos del campo observado. Que muchas ocurrencias de `U` estén asociadas con una Experience no demuestra que sus requisitos estén satisfechos; del mismo modo, una Experience podría disponer de evidencia suficiente sin abarcar una porción extensa del campo observado.

Ninguna de estas dos nociones de coverage se define aquí como TES Progression. Tampoco se presupone que una representación porcentual sea válida para alguna de ellas.

La utilidad de ambas nociones de coverage queda **sujeta a falsificación adversarial en Demo Factory Session 3**.

## Condición de reapertura semántica

TES solo debería reconsiderarse si aparece un caso concreto que no pueda representarse coherentemente mediante la distinción existente:

```text
observable occurrence / trace → contextual recognition as TES Event
```

Ese caso deberá aportar evidencia efectiva de una laguna semántica. La incomodidad de implementación, la ausencia de un tipo técnico, una preferencia de nomenclatura o la necesidad de una proyección de interfaz no constituyen por sí solas evidencia suficiente para reabrir TES.
