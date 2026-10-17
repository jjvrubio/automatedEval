---
title: "Session 17 — Authority-Bounded Cross-Subject Evidence Composition Experiment"
aliases:
- "Experimento de admisibilidad conjunta de evidencia entre sujetos"
language: es
version: "v1.0"
status: "experiment completed"
date: "2026-09-06"
project: "Convercus App"
document_type: "informe de experimento"
scope: "admisibilidad conjunta, acotada por una premisa autoritativa, de Evidence atribuida a sujetos distintos"
repository_role: "evidencia ejecutable posterior a Session 16; no constituye promoción arquitectónica ni modelo de Group"
semantic_authority: "experimento técnico de producto subordinado a ADR-001–005; no modifica TES ni el Contrato semántico de producto"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 17 — Authority-Bounded Cross-Subject Evidence Composition Experiment

## A. Repository inspection

Se inspeccionaron ADR-005, Architecture v0.5, Sessions 15–16, `evidence-relevance.ts`, `evidence-sufficiency.ts` y sus tests. El estado previo era:

```text
Evidence attributed to one subject
        ↓ same situated context
evaluateEvidenceSufficiency
        ↓
K = A AND (B OR C)
```

El evaluator de Session 15 filtraba Evidence por una única `subjectRef`. Esto preservaba correctamente su experimento, pero impedía probar P1/P2 sin descartar B@P2 o borrar su atribución. No existían consumers productivos, Group, membership, participant/contributor entities, EvidenceSet aggregate ni infraestructura de authority.

Se reutilizaron:

- `DistributedMarkerEvidence` y sus facts neutrales;
- `TreasureHuntSufficiencyCriterion` y K sin cambios;
- la distinción `established` / `not-established` como mecanismo experimental;
- la evaluación pura de contribuciones distintas;
- el contexto hunt/stay/property de Session 15;
- ADR-005 como invariante rector.

La verificación focalizada inicial pasó **2 test files / 23 tests** después del delta mínimo. La verificación completa final pasó **12 test files / 66 tests**, además de typecheck, lint y build.

## B. Hypothesis

### H17 — Authority-bounded cross-subject evidence composition

> Evidence atribuida a sujetos distintos puede tratarse como premisas conjuntamente admisibles de una misma evaluación contextual de suficiencia solo hasta donde lo sostenga una premisa autoritativa y scoped aplicable a ese contexto. El contexto factual o situado compartido no establece por sí mismo esa autoridad. La admisibilidad conjunta no implica por sí misma identidad de Group, membership, participación colectiva, group Evidence, group sufficiency o group outcome.

H17 se evaluó sin protegerla con arquitectura: el caso sin premise, el scope incorrecto, los sujetos incorrectos y el booking compartido debían impedir establecer admisibilidad conjunta sin producir prohibición o failure.

## C. Constants

Se mantuvieron constantes desde Session 15:

```text
Evidence A
Evidence B
criterion K = A AND (B OR C)
unordered clues
neutral factual Evidence
same sufficiency transformation
same open-world distinction
```

También se mantuvieron hunt, stay, property y booking en los casos principales. K no recibió subject refs ni reglas de cooperación. El cambio primario fue:

```text
subjectRef(A) != subjectRef(B)
```

## D. New variable

La única variable nueva fue:

```text
authority-bounded cross-subject evidence composition
```

Su observación operacional fue:

```text
joint admissibility
```

El término desnudo `composition` no se usa para nombrar la operación y no se confunde con Desired/Effective Demo Composition.

Se preservaron tres etapas:

```text
Evidence attribution
        !=
joint admissibility
        !=
sufficiency evaluation
```

## E. Minimal implementation

Se añadió `cross-subject-evidence-admissibility.ts`, con:

- `CrossSubjectMarkerEvidence`, que conserva `subjectRef` y añade el `bookingRef` factual necesario para el caso de contexto compartido;
- `CrossSubjectEvaluationContext`, un fixture situado con `evaluationRef`, hunt, stay, property y booking;
- `AuthoritativePremise`, fixture separado de K con identity, provenance, scope y subjects cubiertos;
- `evaluateJointAdmissibility()`, que decide únicamente si los records situados pueden entrar juntos;
- `evaluateCrossSubjectEvidenceSufficiency()`, que no intenta K hasta que la etapa anterior queda establecida.

Se extrajo en `evidence-sufficiency.ts` la misma evaluación de K como `evaluateAdmittedEvidenceSufficiency()`. El wrapper de Session 15 sigue filtrando por su sujeto único y delega en esa función; sus 15 tests permanecen verdes. La extracción evita duplicar K y no cambia sus reglas.

El outcome de suficiencia cross-subject no contiene `subjectRef`, owner o beneficiary: Session 17 no decide a quién pertenece el claim eventual.

Deliberadamente no se añadieron:

- Group, membership, participation o contributor entities;
- EvidenceSet o persistence;
- service, registry, provider, repository o engine;
- authority accreditation o cardinality model;
- Experience Definition, TES concepts, Activity, runtime, incentive o UI;
- cambio de ADR, arquitectura o Contrato semántico de producto.

La firma recibe como conveniencia un premise opcional. Esto no establece relaciones 1:1, 1:N, N:1 o N:N entre premises y evaluation contexts; toda cardinalidad permanece unresolved.

## F. Test matrix

| Caso | Evidence | Subject attribution | Situated context | Applicable authoritative premise | Joint admissibility | ¿Sufficiency intentada? | Resultado de suficiencia |
|---|---|---|---|---|---|---:|---|
| A — same-subject control | A+B | A@P1, B@P1 | mismo hunt/stay/property/booking | No requerida para el control | `established / same-subject-control` | Sí | `established` bajo K |
| B — authorized cross-subject | A+B | A@P1, B@P2 | mismo scope S1 | Premise P1/P2 aplicable a S1 | `established / applicable-authoritative-premise` | Sí, después de admisibilidad | `established` bajo K |
| C — no authority | A+B | A@P1, B@P2 | mismo scope S1 | Ausente | `cannot-currently-establish` | No | No emitido |
| D — wrong scope | A+B | A@P1, B@P2 | evaluation S1 | Premise para otra evaluation | `cannot-currently-establish` | No | No emitido |
| E — wrong subjects | A+B | A@P1, B@P3 | mismo scope S1 | Premise solo P1/P2 | `cannot-currently-establish` | No | No emitido |
| F — shared context without authority | A+B | A@P1, B@P2 | mismo booking B17, hunt, stay y property | Ausente | `cannot-currently-establish` | No | No emitido |
| Adversarial — extra Evidence | A+B+C | A@P1, B@P2, C@P2 | mismo scope S1 | Ausente | `cannot-currently-establish` | No | No emitido |

Un octavo test comprueba separación estructural: Evidence no contiene premise/admissibility; K no contiene subjects cubiertos; el premise no contiene anchor/alternatives; y el módulo no introduce `composeEvidence`, Group, Membership, Participant, Contributor, TES Progression/Completion/Event, Activity, AppSnapshot, service, registry o repository.

## G. Adversarial findings

### Authority and K

No se encontró acoplamiento oculto. K conserva únicamente anchor A y alternativas B/C. La relación P1/P2 vive en el premise y se evalúa antes. El caso C demuestra que K(A,B) no llega a ejecutarse sin admisibilidad.

### Attribution and participation

`subjectRef` permanece atribución factual. No se crea Participant, Contributor o owner del claim. El resultado cross-subject no asigna el SufficiencyClaim a P1, P2 ni a una entidad colectiva.

### Situated context and semantic authority

Booking B17, stay, property y hunt son facts de scope. El caso F comparte todos y aun así no establece admisibilidad sin premise. Esto refuta el shortcut del fixture `same booking → admissible`, pero no afirma que booking nunca pueda ser condición de una política futura.

### Fixtures and architecture

`AuthoritativePremise`, sus covered subjects, el premise opcional único, los literals y los shapes son mecanismos de falsificación. `authorityRef` conserva procedencia experimental, no acredita legitimidad productiva. No se promueven como contratos.

## H. Falsification analysis

| Criterio | Observación | Resultado |
|---|---|---|
| F1 — Cross-subject entra sin premise | El caso C bloquea el intento de K. | **No ocurrió.** |
| F2 — Shared context crea admisibilidad | El caso F conserva booking compartido y no establece admisibilidad. | **No ocurrió.** |
| F3 — Group persistente es imprescindible | La frontera funciona sin identidad colectiva. | **No ocurrió.** |
| F4 — K debe decidir admisibilidad | Las etapas están separadas y K se reutiliza sin subjects. | **No ocurrió.** |
| F5 — Nueva responsabilidad arquitectónica | El delta es local, removible y gobernado por ADR-005. | **No ocurrió.** |

No apareció contradicción material ni condición STOP. H17 no se clasifica plenamente `SUPPORTED` porque la competencia del premise se asume por construcción y no se prueban múltiples premises, accreditation, revocation o conflict.

## I. Semantic findings

| Distinción | Evaluación de evidencia | Estado |
|---|---|---|
| Evidence attribution ≠ joint admissibility | A@P1/B@P2 no basta en C y F. | **SUPPORTED en el alcance.** |
| Joint admissibility ≠ sufficiency | B establece admisibilidad antes de aplicar K; C–F no intentan K. | **SUPPORTED en el alcance.** |
| Shared situated context ≠ authority over joint admissibility | F mantiene booking/hunt/stay/property compartidos sin authority premise. | **SUPPORTED WITH QUALIFICATION:** se prueba un fixture, no toda relación contextual. |
| Multiple subjects ≠ Group | P1/P2 funcionan sin Group y el outcome no crea owner colectivo. | **SUPPORTED como no-necesidad experimental; no define ontología futura.** |

Estas conclusiones son findings experimentales y evidencia adicional para ADR-005, no invariants arquitectónicos automáticamente promovidos.

La tensión candidata recibe evidencia:

```text
Evidence subject attribution
!=
scope in which Evidence may contribute
```

Pero aún no se promueve: solo se ha ensayado una relación P1/P2 bajo un fixture autoritativo.

## J. Product Semantic Contract pressure

```text
Product Semantic Contract → REVIEW WARRANTED / unchanged
```

Session 17 aporta evidencia suficiente para revisar la diferencia entre atribución factual de Evidence y scope de participación/evaluación: dos subjects pueden contribuir como premises de un mismo claim sin borrar su atribución y sin crear Group.

No aporta evidencia suficiente para definir participant, contributor, collective participation, membership o Group. Por eso no alcanza `REFINEMENT CANDIDATE` para un modelo concreto y no se modifica el contrato en esta sesión.

La revisión futura debe comenzar por las distinciones observadas, no por una solución colectiva asumida.

## K. Architecture impact

ADR-005 gobierna completamente el experimento:

- Evidence conserva atribución factual separada del claim;
- joint admissibility es otro claim derivado acotado por premise y scope;
- ausencia de authority queda como `cannot-currently-establish`, no prohibition;
- K no gana autoridad sobre sujetos;
- runtime y Activity no intervienen.

Architecture v0.5 ya representa Evidence y premises convergiendo en contextual evaluation. La etapa local de admisibilidad no exige una nueva layer o topología; es una transformación contextual previa a otro claim derivado.

```text
ADR-005 → ACCEPTED / unchanged
Architecture v0.5 → ACTIVE / unchanged
new ADR → NOT NEEDED
architecture revision → NOT NEEDED
```

No se crea ADR-006 ni Architecture v0.6.

## L. Unresolved items

Permanecen `UNRESOLVED`:

- contribution identity general;
- participant/contributor distinction;
- beneficiary, subject u ownership del SufficiencyClaim;
- Group identity y membership;
- collective/shared participation;
- group Evidence, group sufficiency y group outcome;
- authority accreditation, revocation y conflict;
- cardinalidad entre authority premises y evaluation contexts;
- composición o concurrencia de varios premises;
- external actor assistance/influence frente a Evidence contribution;
- solution recognition;
- incentive eligibility;
- ordered/enabling clues;
- latency, ambiguity, identity confusion y conflict;
- TES Event recognition y APIs reales.

No se modeló ninguno bajo un nombre alternativo.

## M. Final verdict

```text
H17 → SUPPORTED WITH QUALIFICATION

ADR-005 → ACCEPTED / unchanged
Architecture v0.5 → ACTIVE / unchanged
Product Semantic Contract → REVIEW WARRANTED / unchanged
Group concept → NOT REQUIRED BY THIS EXPERIMENT / UNRESOLVED

Recommended next experimental frontier
→ claim beneficiary / participation scope
  under cross-subject admitted Evidence
```

La cualificación principal es que un único premise fixture se considera competente por construcción. El experimento demuestra que tal premise puede mantener separadas atribución, admisibilidad y suficiencia sin Group; no demuestra de dónde procede su autoridad, cómo se acredita, cuántas evaluations cubre o cómo se compone con otros premises.

Antes del siguiente experimento conviene consolidar H17 documentalmente. La siguiente frontera experimental deberá preguntar a quién o a qué scope se atribuye el claim derivado cuando sus evidencias admitidas pertenecen a subjects distintos, sin presuponer beneficiary, collective participation ni Group. External assistance, ordered clues, solution recognition e incentive eligibility deben permanecer fuera.
