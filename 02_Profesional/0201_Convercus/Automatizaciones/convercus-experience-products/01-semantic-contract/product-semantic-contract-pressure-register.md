---
title: "Registro de presiones sobre el Contrato semántico de producto"
aliases:
- "Product Semantic Contract Pressure Register"
language: es
version: "v0.1"
status: "activo"
date: "2026-09-07"
project: "Convercus Experience Products"
document_type: "registro epistemológico documental"
scope: "presiones observadas sobre el Contrato semántico de producto y condiciones de revisión"
repository_role: "seguimiento de evidencia sin modificar ni sustituir el contrato"
semantic_authority: "registro subordinado; no es TES, contrato semántico ni decisión arquitectónica"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Registro de presiones sobre el Contrato semántico de producto

## Propósito

Este registro hace visibles las tensiones semánticas respaldadas por evidencia de producto antes de que excepciones locales acumuladas vuelvan implícitamente obsoleto el contrato.

```text
nueva evidencia
        ↓
¿presiona al contrato?
        ↓ sí
registrar presión
        ↓
acumular evidencia y revisar
        ↓
mantener / refinar / rechazar
```

Una presión registrada no modifica el [Contrato semántico de producto](./README.md), no introduce conceptos y no autoriza arquitectura. Presión, refinamiento semántico y decisión arquitectónica son resultados distintos.

## Disciplina del registro

Cada entrada debe contener:

1. identificador;
2. fuente experimental;
3. distinción observada;
4. evidencia disponible;
5. autoridad afectada;
6. estado epistemológico;
7. qué no demuestra;
8. preguntas abiertas;
9. riesgo de promoción prematura;
10. condición para nueva experimentación;
11. condición para posible refinamiento del contrato.

Solo se registra como presión observada una tensión respaldada por evidencia. Cooperación, ayuda externa, participant/contributor, identidad de contribución, sujeto o ámbito del claim, solución, incentivos, orden, latencia, ambigüedad, conflicto, autoridad y participación colectiva son fuentes potenciales futuras; no constituyen entradas confirmadas hasta que un experimento produzca evidencia concreta.

## Estados epistemológicos

| Estado | Significado |
|---|---|
| `OPEN / EVIDENCE-BACKED PRESSURE` | Existe tensión demostrada, pero no una solución semántica suficientemente definida. |
| `REFINEMENT CANDIDATE` | La necesidad de una distinción concreta y su significado tienen evidencia suficiente para considerar un cambio. |
| `RESOLVED — NO CHANGE` | La revisión concluye que el contrato vigente puede expresar correctamente el comportamiento. |
| `RESOLVED — REFINED` | Una decisión gobernada introduce un refinamiento trazable. |
| `REJECTED` | Evidencia posterior refuta la presión o demuestra que procedía del artefacto experimental. |

## Umbral epistemológico para considerar un refinamiento

No existe un umbral numérico. Un refinamiento solo debe considerarse cuando la evidencia conjunta permita sostener que:

1. una distinción semántica es necesaria para representar comportamientos de producto legítimos;
2. no puede permanecer como detalle de Scenario;
3. no es únicamente consecuencia de un fixture o shape experimental;
4. su ausencia produce ambigüedad, contradicción o pérdida semántica recurrente;
5. existe evidencia suficiente para definirla sin inventar ontología adicional.

Una nueva propiedad, un nombre útil repetido o una presión acumulada no satisfacen por sí solos este umbral.

## Índice

| ID | Distinción observada | Fuente | Estado |
|---|---|---|---|
| `PSC-P01` | Atribución del sujeto de Evidence ≠ ámbito en el que puede contribuir a una evaluación | Sessions 17–18 | `OPEN / EVIDENCE-BACKED PRESSURE; STRENGTHENED BY ADDITIONAL EVIDENCE` |

## PSC-P01 — Atribución de Evidence y ámbito de contribución/evaluación

### Identificador

`PSC-P01`

### Fuente experimental

[Session 17 — Authority-Bounded Cross-Subject Evidence Composition Experiment](../products/convercus-app/docs/session-17-authority-bounded-cross-subject-evidence-composition.md).

### Distinción observada

```text
atribución del sujeto de Evidence
!=
ámbito en el que esa Evidence
puede contribuir a una evaluación
```

### Evidencia disponible

Evidence A@P1 y B@P2 conservan sus atribuciones individuales y pueden entrar como premises de una misma evaluación de suficiencia cuando un fixture autoritativo y scoped establece primero su admisibilidad conjunta. El experimento no necesita borrar `subjectRef`, asignar el claim a P1/P2 ni crear Group.

Los controles muestran que booking, stay, property y hunt compartidos, Evidence adicional, un premise fuera de scope o subjects no cubiertos no establecen esa admisibilidad por sí solos.

### Evidencia adicional — Sesión 18

La consolidación de Sesión 18 añade evidencia relacionada sin cambiar la distinción nuclear de PSC-P01:

```text
una afirmación derivada legítimamente en un ámbito
no obtiene automáticamente autoridad para ser utilizada en otro
```

La evidencia corregida distingue entre igualdad contextual y cobertura autoritativa. `S1 != S2` no impide necesariamente la utilización del claim cuando una base autoritativa explícita y aplicable cubre direccionalmente ese uso; sin esa base, el resultado permanece `cannot-currently-establish`.

Por tanto, la nueva evidencia se clasifica como:

```text
PSC-P01 → OPEN / EVIDENCE-BACKED PRESSURE
PSC-P01 → STRENGTHENED BY ADDITIONAL EVIDENCE
```

Esta consecuencia no convierte PSC-P01 en una teoría general sobre ámbitos, no exige `ClaimScope`, `EvaluationScope` o una entidad de autorización contextual, y no establece que toda afirmación tenga un ámbito persistente propio. `AuthoritativeContextualUseBasis`, `fromScopeRef` y `toScopeRef` permanecen artefactos experimentales no promovidos.

### Autoridad afectada

La presión afecta a la capacidad del Contrato semántico de producto para distinguir la atribución factual de Evidence del ámbito en el que puede contribuir a una evaluación. El eventual sujeto o referente de la afirmación derivada permanece una frontera relacionada, pero no forma parte de la distinción demostrada por PSC-P01. No modifica la autoridad TES ni concede autoridad normativa al fixture `AuthoritativePremise`.

### Estado epistemológico

```text
OPEN / EVIDENCE-BACKED PRESSURE

SUPPORTED WITH QUALIFICATION
como presión observada
```

La cualificación es que la competencia de un único premise se asume por construcción experimental. La evidencia no determina todavía qué concepto resolvería la presión.

### Qué NO demuestra

PSC-P01 no demuestra:

- qué son `ParticipationScope`, `EvaluationScope` o `ContributionScope`, ni que deban existir;
- que Participant y Contributor sean entidades distintas;
- que deba existir Group, membership o CollectiveParticipation;
- que las Evidence sean colectivas;
- quién o qué es el sujeto/referente del SufficiencyClaim;
- cuál es el ámbito semántico final del claim;
- quién es beneficiario de una consecuencia posterior;
- dónde deben residir booking, stay, property o scenario relations;
- que `coveredSubjectRefs` sea un modelo general de autorización;
- cómo se origina, acredita, revoca o combina autoridad.

### Preguntas abiertas

- ¿De qué o de quién habla un claim derivado de Evidence atribuida a P1 y P2?
- ¿Cuál es el ámbito del claim y cómo se diferencia de sus sujetos evidenciarios?
- ¿Es necesaria una distinción participant/contributor o basta conservar atribución y scope?
- ¿Cuándo una relación contextual pertenece a Evidence y cuándo al contexto de evaluación?
- ¿Puede el contrato vigente expresar la presión sin concepto nuevo?
- ¿Cómo cambia el análisis con varios premises, conflicto o revocación?

### Riesgo de promoción prematura

La presión podría transformarse indebidamente en Group, ParticipationScope, EvaluationScope, Contributor, membership o un authority service. También podría elevar `bookingRef`, `coveredSubjectRefs`, el premise opcional único o los outcome literals a semántica de producto por conveniencia.

### Condición para nueva experimentación

Una hipótesis posterior debe aislar exactamente una de las fronteras abiertas —nueva derivación en otro ámbito, participant/contributor, ayuda externa, acreditación o conflicto/múltiples premises— y mantener las demás sin resolver. En particular, una posible nueva derivación debería preguntar:

```text
¿puede la misma Evidence ser evaluada nuevamente en S2
bajo premisas aplicables a S2, produciendo una nueva afirmación,
sin confundir esa operación con la reutilización autorizada
de una afirmación derivada en S1?
```

```text
reutilización autorizada != nueva derivación
```

La naturaleza productiva general del ámbito permanece `UNRESOLVED`, pero no constituye una frontera experimental genérica en esta entrada. La selección requiere revisar esta entrada y el contrato vigente; PSC-P01 no selecciona la siguiente sesión.

### Condición para posible refinamiento del contrato

Debe existir evidencia adicional de que el contrato actual no puede representar correctamente un comportamiento legítimo sin una distinción semántica concreta, que la presión recurre fuera del fixture P1/P2 y que la distinción puede formularse sin inventar Group, participación colectiva u ontología adicional.
