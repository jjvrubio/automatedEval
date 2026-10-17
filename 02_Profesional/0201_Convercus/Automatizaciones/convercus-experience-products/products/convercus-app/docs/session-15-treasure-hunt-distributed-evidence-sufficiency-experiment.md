---
title: "Session 15 — Treasure Hunt: Distributed Evidence and Sufficiency Experiment"
aliases:
- "Experimento de evidencia distribuida y suficiencia"
language: es
version: "v1.0"
status: "experiment completed"
date: "2026-09-06"
project: "Convercus App"
document_type: "informe de experimento"
scope: "evaluación de suficiencia de múltiples evidencias factuales independientes en un escenario unipersonal y no ordenado"
repository_role: "evidencia ejecutable posterior a Architecture v0.5; no constituye promoción arquitectónica"
semantic_authority: "experimento técnico de producto subordinado a ADR-001–005; no es TES ni una Experience Definition validada"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 15 — Treasure Hunt: Distributed Evidence and Sufficiency Experiment

## 1. Hypothesis

### H15 — Distributed Evidence Sufficiency

> Varias evidencias factuales e independientemente válidas pueden contribuir conjuntamente a un claim derivado de suficiencia, pero su pluralidad, cantidad u orden no establecen por sí solos esa suficiencia. El claim requiere un criterio scoped y autoritativo distinto del contenido factual de cada evidencia.

La formulación analítica usada para falsificarla fue:

```text
SufficiencyClaim = f(EvidenceSet, SituatedContext, SufficiencyCriterion)
```

No se adopta como fórmula arquitectónica ni convierte `EvidenceSet` en aggregate o `SufficiencyCriterion` en servicio.

| Subhipótesis | Predicción falsable | Resultado |
|---|---|---|
| H15a — Evidence independence | Cada evidencia conserva identidad factual sin contener suficiencia. | **SUPPORTED.** |
| H15b — Quantity is not sufficiency | A+B sí y B+C no, pese a igual cardinalidad. | **SUPPORTED.** |
| H15c — Duplicate evidence | A+A no satisface contribuciones distintas. | **SUPPORTED.** |
| H15d — Order independence | A,B y B,A producen el mismo claim. | **SUPPORTED.** |
| H15e — Open-world insufficiency | Falta de evidencia calificadora produce `not-established`, no failure. | **SUPPORTED WITH QUALIFICATION.** No se ensayaron latencia, ambigüedad o conflicto. |
| H15f — Sufficiency is not solution recognition | El outcome solo afirma suficiencia bajo K. | **SUPPORTED por límite estructural y ausencia de integración**, no por un recognizer alternativo. |
| H15g — Sufficiency is not TES Progression | No existe count, porcentaje ni semántica TES en el evaluator. | **SUPPORTED por inspección y tests de frontera.** |
| H15h — Partial incentive downstream | Puede ser una implicación posterior, nunca prueba retroactiva. | **NOT OPERATIONALLY TESTED.** El repositorio no tiene una frontera mínima de eligibility apropiada. |
| H15i — Activity downstream | Activity no participa en aggregation, criterio ni evaluation. | **SUPPORTED por independencia de módulo e inspección.** |

## 2. Why Treasure Hunt

Cooking Class tensionó una única evidencia contra más de un contexto de Experience. Treasure Hunt tensiona otra simplificación: que una evaluación derivada dependa de un único input factual atómico.

```text
Cooking Class
one Evidence → contextual relevance

Treasure Hunt Session 15
multiple independent Evidence → scoped sufficiency evaluation
```

El escenario permite distinguir cantidad, agregación y suficiencia usando tres contribuciones sin introducir grupo, secuencia, progresión, resultado o completion.

## 3. Scope

El experimento mantiene constantes:

```text
subjectRef  = business-guest-p
stayRef     = stay-s
propertyRef = business-hotel-h
huntRef     = treasure-hunt-t
criterion K = A AND (B OR C)
```

Su alcance es exclusivamente:

- un participante referenciado de forma estable, sin decidir su identidad de dominio;
- tres marcadores/evidencias factuales independientes;
- pistas deliberadamente unordered;
- consideración conjunta in-memory;
- evaluación pura de suficiencia;
- posible incentivo parcial solo como implicación downstream documentada.

Treasure Hunt permanece como `experimental situated scenario`, no como Product Experience Definition.

## 4. Explicit exclusions

Quedan fuera:

- participantes múltiples, contributors, grupos, memberships y atribución compartida;
- TES Event, Pattern, Sequence, Progression, Result, Measurement, Learning o Completion;
- solution recognition y Treasure Hunt completion;
- pistas ordenadas, habilitantes o causales;
- Experience Definition de Treasure Hunt;
- generic expression/rules/sufficiency engine o DSL;
- reward/incentive engine;
- Activity/UI integration;
- providers, registries, persistence, APIs, latency, confidence, identity resolution y conflict handling;
- cambios del Contrato semántico de producto, ADR-001–005 o Architecture v0.5.

## 5. Repository inspection

Antes del delta se comprobó:

- `evidence-relevance.ts` ya contenía una frontera pura para un claim diferente: relevancia contextual de una evidencia individual.
- Su autoridad experimental era clasificatoria y estaba limitada por scope/coverage; no debía reutilizarse por simetría.
- `EvidenceInput` contenía sujeto, contexto, procedencia, fiabilidad e interpretación opcional, pero su forma estaba vinculada a acciones demo y era más amplia de lo requerido.
- Activity y AppSnapshot eran read models derivados; no existía consumer productivo de los evaluators.
- `DemoProvider.executeAction()` ofrecía una frontera operacional para la única acción Hospitality, no una política de suficiencia o incentive eligibility.
- Los cupones existentes eran read models. Reutilizarlos para inferir eligibility habría convertido presentación en autoridad.
- Las dos formas actuales de `ExperienceDefinition` seguían provisionales y no eran necesarias.
- ADR-005 y Architecture v0.5 exigían evidencia neutral, claims acotados por premisas, indeterminación open-world y Activity downstream.
- Session 13 tenía 12 tests de relevance y el baseline completo registrado era 10 test files / 43 tests.

No se encontró contradicción con la documentación vigente.

## 6. Experimental model

Se añadieron tres formas locales y removibles:

```text
DistributedMarkerEvidence
  evidenceRef
  subjectRef
  huntRef
  stayRef
  propertyRef
  markerRef

EvidenceSufficiencyContext
  subjectRef
  huntRef
  stayRef
  propertyRef

TreasureHuntSufficiencyCriterion
  criterionRef
  authorityRef
  scope { huntRef, propertyRef }
  anchorMarkerRef
  alternativeMarkerRefs [B, C]
```

La función `evaluateEvidenceSufficiency()`:

1. selecciona Evidence situada en el mismo sujeto, hunt, stay y property;
2. conserva las referencias de records considerados;
3. deduplica únicamente contribuciones por `markerRef` para falsificar A+A;
4. comprueba que el criterio aplica al hunt/property;
5. evalúa el anchor A y al menos una alternativa B/C;
6. devuelve un claim trazable `established` o `not-established`.

Los nombres y shapes son mecanismos experimentales, no contratos promovidos. No se creó `EvidenceSet` persistente, aggregate, provider ni motor.

## 7. Authority Frontier

La autoridad experimental del criterio se representa mínimamente mediante `criterionRef`, `authorityRef` y scope. El fixture `scenario-policy:t@experiment-1` se trata como competente por construcción controlada únicamente para K.

```text
Independent factual Evidence
        +
Situated context
        +
scoped criterion fixture
        ↓
pure evaluation transformation
        ↓
SufficiencyClaim bounded by those premises
```

El evaluator no posee autoridad por ejecutar la transformación. `authorityRef` preserva procedencia experimental, pero no acredita por sí mismo autoridad real. No se han demostrado ownership, accreditation, lifecycle, versioning, conflict resolution ni provider topology para un criterio productivo.

`Evidence Sufficiency Authority` queda como término analítico provisional, no como componente arquitectónico.

## 8. Test matrix

| Caso | Evidence disponible | Expected | Observed | Resultado |
|---|---|---|---|---|
| A | `{}` | Sufficiency not established; no failure. | `not-established` | **PASS** |
| B | `{A}` | Not established. | `not-established` | **PASS** |
| Extra individual | `{B}` | Not established. | `not-established` | **PASS** |
| Extra individual | `{C}` | Not established. | `not-established` | **PASS** |
| C | `{B,C}` | Not established aunque count=2. | `not-established` | **PASS** |
| D | `{A,B}` | Established. | `established` | **PASS** |
| E | `{A,C}` | Established. | `established` | **PASS** |
| F | `{A,A}` con dos record IDs | Not established. | `not-established`; una contribución distinta | **PASS** |
| G | `[A,B]` frente a `[B,A]` | Mismo claim. | Outcomes estructuralmente iguales | **PASS** |
| H | `{A,B,C}` | Established, no más fuerte que A+B. | Mismo determination/reason; sin strength/progress | **PASS** |
| Scope adversarial | K fuera de property o B fuera de contexto | Not established. | `not-established` | **PASS** |
| I | Partial incentive downstream | Posibilidad documentada; no inferencia inversa. | No ejecutado por falta de eligibility boundary compatible. | **DOCUMENTED ONLY** |

Además, un test de frontera comprueba que el evaluator no importa ni menciona relevance, Activity, AppSnapshot, ExperienceDefinition, TES runtime semantics, incentive, reward o engine, y no contiene branch por `marker-a`.

## 9. Aggregation vs sufficiency

```text
aggregation
!=
sufficiency
```

La función considera juntos varios records, pero la cardinalidad no decide. B+C contiene dos evidencias y no establece suficiencia; A+B también contiene dos y sí satisface K. A+A conserva dos record IDs, pero aporta una sola contribución distinta y no satisface K.

No se materializa `Aggregation` como entidad. Es únicamente el acto in-memory de considerar records juntos.

## 10. Sufficiency vs solution recognition

```text
sufficiency established under K and T
!=
solution recognized / hunt solved / completion / TES Result
```

El evaluator no emite solución, completion, Result ni Event. Una futura solution-recognition boundary permanece `UNRESOLVED`: no se definen sus inputs, autoridad o relación exacta con el claim de suficiencia.

## 11. Sufficiency vs incentive

La relación permitida queda documentada así:

```text
SufficiencyClaim
        ↓
possible partial-incentive eligibility
        ↓
future operational authority / product policy
        ↓
presentation or use
```

No se implementó porque los cupones existentes son read models y `executeAction()` no representa eligibility. Usarlos habría creado autoridad retroactiva o infraestructura fuera de scope.

Por tanto:

- suficiencia no concede automáticamente un incentivo;
- la existencia de un incentivo no prueba suficiencia;
- un incentivo parcial no es TES Result ni Treasure Hunt completion;
- H15h queda como downstream implication no probada operacionalmente.

## 12. Open-world implications

`not-established` describe únicamente que la Evidence actualmente considerada no satisface K dentro del contexto. No significa `failed`, `false`, imposibilidad futura ni fracaso del participante.

En un sistema real, el mismo estado observable podría deberse a:

- Evidence todavía ausente o retrasada;
- validación pendiente;
- ambigüedad;
- identidad confusa;
- records duplicados;
- conflicto entre fuentes.

Latency, ambiguity, identity y conflict permanecen futuras Authority Frontiers/cualificaciones candidatas. No se añadieron state machines, confidence ni conflict engines.

## 13. Activity frontier

Activity no participa en:

- selección o agrupación de Evidence;
- deduplicación de contribuciones;
- aplicación de K;
- emisión del SufficiencyClaim.

La prueba de frontera verifica ausencia de dependencia con `ActivityItem` y `AppSnapshot`. Una proyección futura podría mostrar una evidencia o claim sin originarlo ni fortalecerlo, conforme a ADR-002 y ADR-005. No se implementó esa proyección ni su UX.

## 14. Semantic Product Contract

No se modificó el Contrato semántico de producto. Este escenario usa una única `subjectRef` estable sin decidir si representa loyalty member, booking owner, account, device holder, TES participant o ExperienceParticipation.

Trigger registrado:

```text
Semantic Product Contract review trigger:
first cooperative / multi-participant Treasure Hunt experiment
```

Esa revisión futura deberá cuestionar individual participant, contributor, group, membership, evidence attribution, shared evidence, group sufficiency y group outcome. Session 15 no responde ninguna de esas preguntas.

Segundo trigger registrado:

```text
ordered or enabling clues
→ separate future experiment
```

Deberá distinguir temporal order, causal enablement, narrative order y TES Sequence sin asumir equivalencias.

## 15. Evidence

La evidencia ejecutable obtenida es:

- una función pura separada recibe un conjunto readonly de Evidence, contexto y criterio explícito;
- las evidencias no contienen fields de suficiencia, progreso, solución, completion o reward;
- A+B y A+C satisfacen K;
- B+C y A+A no satisfacen K pese a cardinalidad dos;
- A,B y B,A producen outcomes iguales;
- A+B+C no genera un nivel más fuerte que A+B;
- criterios o Evidence fuera de scope no establecen suficiencia;
- falta de qualifying Evidence permanece `not-established`;
- el módulo no depende de relevance, Activity, runtime, ExperienceDefinition, incentive ni conceptos TES;
- la suite completa permanece verde tras añadir el experimento.

La evidencia factual se considera válida por construcción de fixture. No se prueba validación real, source competence o accreditation.

## 16. Claims supported

Con el alcance indicado, quedan respaldados:

- múltiples Evidence independientes pueden participar en una evaluación derivada;
- record count y número de contribuciones no establecen suficiencia;
- aggregation no establece suficiencia;
- un criterio scoped distinto de cada Evidence puede sostener un claim de suficiencia;
- suficiencia puede derivarse sin TES Progression, Result o Completion;
- Evidence unordered no implica TES Sequence;
- duplicar un record de la misma contribución no crea suficiencia;
- missing qualifying Evidence no prueba failure;
- más Evidence no produce por sí misma un claim más fuerte;
- Activity puede permanecer downstream.

## 17. Claims not supported

Session 15 no respalda:

- Treasure Hunt como Experience TES-validada o Product Experience Definition;
- solución, completion, TES Event, Pattern, Sequence, Progression, Result, Measurement o Learning;
- participación o suficiencia de grupo;
- contributor membership o shared evidence attribution;
- pistas ordered/enabling;
- generic rules, expression o sufficiency engine;
- eligibility, incentive o reward engine;
- integración Activity/UI;
- autoridad o acreditación productiva del criterio;
- provider architecture, persistence, APIs, latency, confidence, identity resolution o conflict resolution;
- cambios del Contrato semántico de producto;
- ADR-006 o Architecture v0.6.

## 18. Limitations

- K es un fixture deliberadamente pequeño y no demuestra otras formas de suficiencia.
- `anchorMarkerRef` más dos alternativas es una representation shape local, no un lenguaje de reglas.
- La deduplicación solo distingue contribuciones por `markerRef`; no resuelve duplicación factual general.
- Los fixtures se asumen factual e independientemente válidos.
- `authorityRef` no demuestra competencia ni acreditación real.
- No se ensayan evidencia pending, retrasada, ambigua, contradictoria o revocada.
- El único participante evita deliberadamente atribución colectiva.
- No hay consumer productivo ni integración runtime, Activity o incentive.
- Los outcome literals y reason codes son experimentales.

## 19. Architectural evaluation

El delta extiende experimentalmente el flujo de evaluación contextual de Architecture v0.5 sin modificarla. La nueva costura es una función separada porque relevance y sufficiency son claims diferentes.

```text
Independent factual Evidence
        ↓ considered together, without aggregate
Scoped experimental criterion + situated context
        ↓
Evidence sufficiency evaluation
        ↓
bounded SufficiencyClaim
        ↓ ?
future solution recognition / incentive policy / projection
```

No existe base para promoción automática. Este experimento produce Evidence, no ADR-006, Architecture v0.6, contrato compartido, Experience Definition o engine.

### Authority-laundering review

- K establece suficiencia por su contenido scoped, no porque el evaluator lo ejecute.
- `authorityRef` aporta trazabilidad experimental y no acredita autoridad productiva.
- Evidence records no adquieren el claim derivado.
- Más records, orden, UI, Activity o incentive no fortalecen el claim.
- Treasure Hunt no adquiere madurez semántica por ser el contexto narrativo.
- Los names y shapes TypeScript no se convierten en arquitectura.

## 20. Verdict

```text
H15 → SUPPORTED WITH QUALIFICATION
```

La evidencia soporta la separación entre múltiples hechos, consideración conjunta y suficiencia cualitativa scoped. Soporta también que count, duplicación, orden y evidencia extra no creen semántica de Progression, Result o Completion.

La cualificación es material: el criterio y su autoridad son fixtures controlados; no se valida accreditation real, solution recognition, incentivo operacional, fuentes live, conflictos, latencia ni semántica colectiva. H15h queda documentada pero no probada operacionalmente.

### Final adversarial review

| Pregunta | Respuesta |
|---|---|
| ¿A+B es suficiente por count? | **No**, satisface K; B+C demuestra la diferencia. |
| ¿A+A convierte dos records en dos contribuciones? | **No**, queda una contribución distinta. |
| ¿El orden altera el claim? | **No**, los outcomes son iguales. |
| ¿Se introdujo TES Sequence o Progression? | **No**, no hay orden, counts ni porcentajes normativos. |
| ¿Sufficiency se convirtió en Result/Completion? | **No**, esos conceptos no están en el módulo. |
| ¿El incentive prueba retroactivamente suficiencia? | **No**, no se integró y queda downstream. |
| ¿La ausencia se interpretó como failure? | **No**, el claim es `not-established`. |
| ¿El evaluator adquirió autoridad del criterio? | **No**, solo transforma premisas y conserva refs. |
| ¿Treasure Hunt se convirtió en Experience Definition? | **No**, no existe definition ni import correspondiente. |
| ¿Se refinó el Contrato semántico de producto? | **No**. |
| ¿Latency, ambiguity y conflict permanecen abiertos? | **Sí**. |
| ¿Group semantics permanecen fuera? | **Sí**. |
| ¿Ordered/enabling clues permanecen fuera? | **Sí**. |
| ¿El delta puede retirarse sin alterar ADR-001–005? | **Sí**, consta de un módulo/test aislados y este informe. |

### Recommended next step

Realizar una sesión separada de **evaluación y eventual promoción de H15** antes de ampliar Treasure Hunt. Esa sesión deberá decidir si la frontera mínima merece consolidación y qué cualificaciones conservar, sin diseñar todavía semántica cooperativa, pistas ordenadas, solution recognition o incentivos productivos.
