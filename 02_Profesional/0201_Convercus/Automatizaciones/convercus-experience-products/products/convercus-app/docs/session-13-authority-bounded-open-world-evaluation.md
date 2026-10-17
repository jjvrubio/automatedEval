---
title: "Session 13 — Authority-Bounded Open-World Evaluation Experiment"
aliases:
- "Experimento open-world acotado por autoridad"
language: es
version: "v1.0"
status: "experiment completed"
date: "2026-09-04"
project: "Convercus App"
document_type: "informe de experimento"
scope: "claims contextuales limitados por competencia, scope y cobertura de autoridad disponible"
repository_role: "evidencia ejecutable previa a consolidación de una posible ADR-005"
semantic_authority: "experimento técnico de producto; no es TES ni arquitectura aceptada"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 13 — Authority-Bounded Open-World Evaluation Experiment

## 1. Repository inspection

### Topología encontrada

La implementación real coincide con el baseline descrito:

```text
Product Experience Definition candidates (documentales, no ejecutables)
        ↓ refs y criterios reproducidos en fixture de test
ActivityCompletionEvidence + ExperienceRelevanceContext
        ↓
evaluateEvidenceRelevance
        ↓
EvidenceRelevanceOutcome experimental

Activity / AppSnapshot: rama separada, sin dependencia con el evaluator
```

- `evidence-relevance.ts` contenía el evaluator puro de Session 11.
- `evidence-relevance.test.ts` contenía Cooking Class, Family Adventure, Active Challenge y un catálogo situado.
- `ActivityClassification` contenía solo `shared-hotel-activity` y `sport-wellness`.
- La clasificación estaba almacenada dentro de `Scenario.activityCatalogue`; Scenario era por tanto autoridad de facto, solo experimental.
- No existía ningún consumer del evaluator fuera de su test.
- No había consumer runtime, bootstrap, provider, React, AppSnapshot ni Activity.
- Activity se construía exclusivamente mediante `projectSnapshot()` desde `ActivitySourceRecord` y seguía siendo read model.
- `domain/contracts.ts::ExperienceDefinition` seguía siendo el contrato funcional rico/provisional.
- `demo-factory/contracts.ts::ExperienceDefinition` seguía siendo el descriptor mínimo `id/name/tesBaseline` resuelto por bootstrap.
- Las Product Experience Definitions de Session 10 seguían siendo `READY WITH EXPLICIT GAPS — non-executable candidate`.
- ADR-001–004 y los informes Session 11–12 estaban presentes y no exigían cambios.

### Evaluator previo

El evaluator anterior recibía solo Evidence + ExperienceContext y devolvía:

```ts
{ relevant: boolean; reason: string }
```

`false` representaba mismatch, actividad ausente o falta de intersección clasificatoria. No recibía authority/coverage y no podía distinguir un negativo conocido de conocimiento incompleto.

### Consumers y compatibilidad

No se encontraron consumers externos. Esto permitió retirar el booleano local sin migración, adapter ni dual contract. La ausencia de consumers es un hecho de repositorio, no evidencia de que la forma nueva deba convertirse en API pública.

## 2. Baseline compatibility

No se encontró contradicción material con ADR-001–004 ni con la baseline v0.4.

| Baseline | Compatibilidad preservada |
|---|---|
| ADR-001 | No se usa `tesBaseline`, naming, bootstrap ni resolución runtime como autoridad. TES no se modifica. |
| ADR-002 | Evaluation permanece separada de runtime state y read models; Activity no participa. |
| ADR-003 | No cambia manifest, bootstrap ni effective composition. La authority fixture no se presenta como provider/registry. |
| ADR-004 | Definition aporta criterio, Scenario aporta contexto/catálogo, pero ninguno ejecuta reglas de Experience ni Progression. |
| Session 11 | Evidence neutral, evaluación pura, inmutabilidad, orden y Activity downstream sobreviven. El booleano se sustituye porque no tenía consumers. |
| Session 12 | El invariant open-world se convierte en evidencia ejecutable sin promoverlo a arquitectura. |

Diferencias no materiales: la autoridad dejó de estar implícita en las clasificaciones del Scenario y pasó a ser un tercer input explícito del experimento. No se rediseñó el Scenario productivo porque los contextos solo existen en tests.

### Baseline ejecutable

Antes del cambio, `npm run check` pasó con typecheck, lint, build, **10 test files y 38 tests**.

## 3. Hypothesis y falsifiers

### H13

> Para Evidence y ExperienceContext constantes, el tipo de claim que puede emitir una evaluación contextual está limitado por competencia, scope y cobertura de la autoridad disponible. Ausencia de autoridad suficiente no autoriza un claim negativo.

```text
EvaluationOutcome = f(Evidence, ExperienceContext, AvailableAuthority)
```

### Subhipótesis

| ID | Hipótesis | Resultado |
|---|---|---|
| H13a | Membership positiva, competente y en scope sostiene positive. | **SUPPORTED** |
| H13b | Exclusión explícita, competente y en scope sostiene negative. | **SUPPORTED** |
| H13c | Ausencia en conocimiento incomplete permanece undetermined. | **SUPPORTED** |
| H13d | Ausencia bajo cobertura scoped exhaustive puede sostener negative. | **SUPPORTED** |
| H13e | Authority ausente o fuera de scope permanece undetermined. | **SUPPORTED** |
| H13f | Claims competentes conflictivos permanecen undetermined/conflicting sin precedence. | **SUPPORTED** |
| H13g | Evaluator deriva pero no clasifica ni adquiere autoridad TES/factual. | **SUPPORTED WITH QUALIFICATION** por inspección y test de imports/strings. |
| H13h | Activity permanece downstream y no altera el status epistémico. | **SUPPORTED WITH QUALIFICATION**: no hay integración Activity real, solo se prueba ausencia de dependencia y una proyección local que conserva el outcome. |

### Falsifiers intentados

| Falsifier | Observación |
|---|---|
| Ausencia en catálogo incomplete produce negative | No: produce `undetermined/incomplete-classification-knowledge`. |
| Missing authority produce negative | No: produce `undetermined/missing-classification-authority`. |
| Conflicto se resuelve por precedence inventada | No: produce `undetermined/conflicting-classification-authority`. |
| Branch por Experience ID | No existe y el test renombra la ref conservando resultado. |
| Evaluator inventa clasificaciones | No: solo consume assertions explícitas. |
| Activity es input | No se importa ni se recibe. |
| Activity convierte undetermined en negative | La proyección mínima conserva la misma referencia/outcome. No se modificó UI. |
| `tesBaseline` certifica autoridad | No aparece en el evaluator. |
| `ExperienceDefinition` certifica autoridad | No aparece en el evaluator. |
| Bootstrap implica validación | Bootstrap no participa. |
| Se reconoce TES Event | No existen Event, recognition ni interpretation en la costura. |
| Hace falta engine/registry/taxonomy platform | No; una función pura y fixtures bastan. |
| Cambiar authority no cambia el claim | Falsado: con Evidence+Context constantes, incomplete produce undetermined y exhaustive produce negative. |
| Hace falta semántica nueva de Experience | No; se reutilizan los criterios de Session 10–11. |

## 4. Experimental delta

El delta se limita a dos archivos existentes y este informe:

1. `evidence-relevance.ts`:
   - mueve las assertions clasificatorias fuera de Scenario;
   - añade una representación local de authority, scope y coverage;
   - recibe `availableAuthorities` como tercer argumento;
   - sustituye `relevant: boolean` por un outcome de `positive | negative | undetermined` con reason y authority refs.
2. `evidence-relevance.test.ts`:
   - mantiene Cooking Class y los contextos Family/Active;
   - introduce fixtures explícitos para membership, exclusion, incomplete, exhaustive, missing/out-of-scope y conflict;
   - reemplaza 7 tests de Session 11 por 12 tests que preservan sus invariants y añaden H13.
3. Este documento registra hipótesis, falsificación, evidencia y evaluación.

No se añade módulo de authority, registry, service, provider, taxonomy, persistence, runtime integration ni UI.

## 5. Authority representation

La forma experimental mínima es:

```text
ActivityClassificationAuthority
├── authorityRef
├── competence = activity-classification
├── scope
│   ├── propertyRef
│   └── catalogueVersion
├── coverage = incomplete | exhaustive
└── claims[]
    ├── activityId
    ├── classification
    └── relation = includes | excludes
```

Representa únicamente lo necesario:

- **positive:** assertion `includes` explícita;
- **exclusion:** assertion `excludes` explícita;
- **coverage:** `incomplete` o `exhaustive` dentro del scope;
- **missing:** lista vacía o authority cuyo scope/version no coincide;
- **conflict:** dos authorities scoped con assertions positiva y negativa incompatibles.

La competencia está fijada al literal `activity-classification`; no modela niveles, delegación o acreditación. `authorityRef` conserva identidad, no demuestra por sí misma legitimidad. Los tests tratan los fixtures como competentes por construcción controlada.

Esta forma **no es arquitectura final**: los dos valores de coverage, claims, scope y referencias son mecanismos de falsificación. No se propone schema universal, catálogo, trust model, precedence ni provider.

## 6. Evaluation outcome representation

El booleano previo se elimina porque no tenía consumers y colapsaba dos claims distintos. La representación local es una unión discriminada:

```text
positive
  authoritative-membership

negative
  explicit-exclusion
  scoped-exhaustive-absence

undetermined
  context-insufficient
  activity-not-in-scenario
  missing-classification-authority
  incomplete-classification-knowledge
  conflicting-classification-authority
```

Cada outcome conserva `evidenceRef`, `experienceRef` y `authorityRefs`. Esto hace imposible para un consumer TypeScript leer `false` sin saber si se estableció NOT X o simplemente no pudo establecerse X.

Los nombres no constituyen una ontología ni enum arquitectónico final. Distinguimos tres tipos de claim porque son el objeto del experimento, no porque agoten todos los estados futuros.

## 7. ADR-001 guardrail

Se verificó explícitamente que el source del evaluator no contiene:

- `tesBaseline`;
- `ExperienceDefinition`;
- `bootstrap`;
- IDs de Family Adventure o Active Challenge.

El evaluator no inspecciona nombre de artefacto, baseline, status runtime ni resolución. `definitionRef` solo identifica el contexto del outcome y cambiarlo no altera determination/reason cuando los criterios permanecen iguales.

Por tanto:

```text
tesBaseline ≠ validation certificate
runtime Experience descriptor ≠ semantic authority
bootstrap resolution ≠ semantic validation
```

Session 13 no reabre ADR-001 ni resuelve la nomenclatura de Experience artifacts.

## 8. Activity Authority Frontier

La dependencia actual sigue siendo unidireccional:

```text
Evidence + Context + Authority
        ↓
EvaluationOutcome
        ↓ possible future projection
Activity
```

`evidence-relevance.ts` no importa `ActivityItem`, `ActivitySourceRecord` ni `projectSnapshot`. Activity no origina evidencia, clasificación o outcome. No se construyó una batería UI porque no existe integración que falsificar.

Un test crea una proyección local mínima `{ label, sourceOutcome }` y verifica que conserva por referencia el outcome `undetermined`; el label no lo fortalece ni reinterpreta. Esto solo prueba la posibilidad de no escalar autoridad, no diseña Activity UX ni un projector productivo.

Riesgo pendiente: una UI futura podría mostrar “no relevante” para un outcome indeterminado o descartar `reason/authorityRefs`. Esa posibilidad no existe en el runtime actual porque el outcome todavía no se proyecta.

## 9. Test matrix

Evidence y ExperienceContext se mantienen constantes en B–F. Solo cambia authority/coverage.

| Caso | Evidence | ExperienceContext | Authority / coverage | Expected | Observed | Veredicto |
|---|---|---|---|---|---|---|
| A — positive control | Cooking Class | Family Adventure, same stay/property | `includes shared-hotel-activity`, incomplete suficiente para positivo | positive | `positive/authoritative-membership` | PASS |
| B — explicit negative | Cooking Class | Active Challenge, same stay/property | `excludes sport-wellness`, scoped competent | negative | `negative/explicit-exclusion` | PASS |
| C — incomplete | Cooking Class | Active Challenge, same stay/property | solo `includes shared-hotel-activity`, incomplete | undetermined | `undetermined/incomplete-classification-knowledge` | PASS |
| D — exhaustive | Cooking Class | Active Challenge, same stay/property | mismo set sin sport-wellness, exhaustive en property+version | negative | `negative/scoped-exhaustive-absence` | PASS |
| E — missing | Cooking Class | Active Challenge, same stay/property | ninguna authority | undetermined | `undetermined/missing-classification-authority` | PASS |
| E2 — out of scope | Cooking Class | Active Challenge, same stay/property | exclusion en otra catalogue version | undetermined | `undetermined/missing-classification-authority` | PASS |
| F — conflicting | Cooking Class | Active Challenge, same stay/property | include y exclude sport-wellness desde dos authorities, sin precedence | undetermined/conflicting | `undetermined/conflicting-classification-authority` | PASS |

Tests adicionales confirman neutralidad del input, constancia de context, no-ID branching, scope gaps, pureza, repeatability, order independence y Activity separation.

## 10. Verification

| Check | Baseline | Final |
|---|---|---|
| Typecheck | PASS | PASS |
| Lint | PASS | PASS |
| Test files | 10 passed | 10 passed |
| Tests | 38 passed | **43 passed** |
| Build Vite/PWA | PASS | PASS |

El archivo focalizado contiene **12 tests**, todos verdes. El aumento neto es de 5 porque reemplaza los 7 tests anteriores. La suite completa preserva presenter action/checkpoint, reset, Activity projection y aislamiento Retail.

No se encontraron branches por Experience ID en el evaluator.

## 11. Files changed

### Nuevos

- `products/convercus-app/docs/session-13-authority-bounded-open-world-evaluation.md`

### Modificados

- `products/convercus-app/prototype/src/demo-factory/evidence-relevance.ts`
- `products/convercus-app/prototype/src/demo-factory/evidence-relevance.test.ts`

### Eliminados

- Ninguno.

No se modificaron ADR, Product Experience Definitions, contratos globales, manifests, bootstrap, providers, AppSnapshot, Activity o UI.

## 12. Authority laundering review

### Upstream

- Evidence no contiene relevance, classification, Experience ref, `significant` ni interpretation.
- Experience criterion no se trata como clasificación factual de Cooking Class.
- Scenario declara existencia local y scope/version; ya no contiene la assertion clasificatoria.
- Authorities aportan assertions explícitas bajo scope/coverage.
- Naming, `tesBaseline` y bootstrap están ausentes.

Resultado: no se detecta laundering upstream dentro del experimento. El fixture presupone competencia; esa es una simplificación declarada, no un certificado real.

### Evaluator

- No inventa clases ni añade defaults.
- No resuelve conflictos por orden.
- No convierte absence en negativo salvo `coverage: exhaustive` scoped.
- Solo deriva un claim relacional y devuelve la autoridad utilizada.

Resultado: no se detecta laundering interno. Riesgo: la palabra `exhaustive` es confiada como assertion del fixture y no se verifica externamente; hacerlo requeriría governance fuera del alcance.

### Downstream

- No existe consumer runtime/UI.
- La proyección mínima conserva el outcome original.
- Activity no participa y no puede elevar autoridad hoy.

Resultado: no hay laundering downstream implementado. El riesgo futuro es omitir qualifiers al presentar.

## 13. Evidence

La ejecución demuestra realmente:

```text
same Evidence
+ same ExperienceContext
+ different AvailableAuthority / coverage
        ↓
different legitimate claim type
```

En concreto:

- membership positiva explícita sostiene positive sin cobertura exhaustiva;
- exclusión explícita sostiene negative dentro del scope;
- ausencia bajo conocimiento incomplete no sostiene negative;
- la misma ausencia bajo cobertura exhaustive scoped sí puede sostener negative;
- authority ausente o fuera de versión permanece undetermined;
- conflicto sin precedence permanece undetermined/conflicting;
- el evaluator no necesita convertirse en classification source;
- Activity puede seguir fuera del cálculo.

La evidencia discrimina ejecutablemente:

```text
we cannot establish X
        ≠
we have established NOT X
```

## 14. Unexpected findings

- El evaluator no tenía consumers; el booleano podía retirarse sin compatibilidad temporal.
- La clasificación estaba más acoplada a Scenario de lo que sugería el diagrama conceptual de Session 11. Separarla fue necesaria para variar solo authority.
- `reason` ya distinguía causas técnicas, pero no impedía que todas se consumieran como `false`.
- Una authority fuera de `catalogueVersion` es indistinguible de authority no disponible para ese scope, aunque exista físicamente.
- La evidencia positiva necesita menos cobertura que la negativa por ausencia: una membership explícita basta; la exclusión por omisión exige exhaustividad declarada.
- Conflicto y coverage pueden interactuar: una afirmación positiva frente a una authority exhaustiva que la excluye permanece conflicto, no precedence.
- Activity estaba completamente desacoplada; una prueba UI habría añadido ruido sin nueva evidencia.

## 15. Claims supported by evidence

- Neutral Evidence puede permanecer independiente de evaluación relativa a Experience.
- Para Evidence+Context constantes, authority/coverage puede cambiar el claim legítimo.
- Ausencia en conocimiento incomplete no justifica negative.
- Un negative por ausencia requiere cobertura suficientemente exhaustive y scoped.
- Exclusión explícita competente puede sostener negative sin declarar catálogo global completo.
- Missing, out-of-scope y conflicting authority pueden conservarse como undetermined.
- El evaluator no necesita clasificar, reconocer Event ni consultar TES/runtime.
- Scenario puede conservar contexto/catálogo sin ser la fuente implícita de todas las clasificaciones.
- Activity puede permanecer downstream y ajena al outcome.

## 16. Claims NOT supported by evidence

- Qué actor debe ser classification authority en producción.
- Que Scenario, property catalogue o provider sea autoridad final.
- Taxonomy universal o forma final de activity classification.
- Cómo se acredita competencia o se verifica exhaustividad.
- Precedence, merge o resolución de conflictos.
- Schema/API final de authority u outcome.
- Que los literales `positive/negative/undetermined` sean vocabulario transversal.
- TES Event recognition o equivalencia relevant→Event.
- SignificantEvent migration.
- Pattern, Sequence, Progression, Result, Measurement o Learning.
- Participation, group semantics o Treasure Hunt.
- Persistencia, audit, event sourcing o provider topology.
- UI/Activity final ni reglas de proyección de qualifiers.
- Completitud semántica de `ExperienceDefinition`.
- Necesidad de modificar ADR-001 o publicar Architecture v0.5.

## 17. Limitations

- Todas las authorities son fixtures locales y su competencia se acepta por construcción.
- Solo se usa una property, una catalogue version, una actividad y dos clasificaciones.
- `incomplete/exhaustive` es un binario experimental; cobertura real podría ser parcial por campo, tiempo o subset.
- Scope solo incluye property+catalogue version; no contempla territorio, canal, tenant o intervalo temporal.
- No se comprueba firma, owner, vigencia ni cadena de delegación.
- No hay grados de reliability, confidence o evidence sufficiency.
- La lógica de varias clasificaciones aceptables solo se prueba con un elemento por Experience.
- No hay aliases, jerarquías ni mappings entre taxonomías.
- El catálogo Scenario es una lista simple y no declara su propia completitud.
- El evaluator es síncrono, puro e in-memory; no demuestra que evaluación real sea order-independent.
- El outcome no se consume en runtime ni se proyecta en Activity real.
- Los documentos candidate de Experience no se resuelven; sus criterios se reproducen manualmente en test.
- Ninguna API real valida que pueda obtenerse Evidence neutral o classification authority separada.
- El type-level contract no impide que código JavaScript entregue authority falsa.

## 18. Architectural evaluation

H13 aporta evidencia suficiente para consolidar en una sesión posterior el invariant:

> Un claim de relevancia está acotado por Evidence, ExperienceContext y autoridad disponible; ausencia de conocimiento no equivale a negativo.

No se promueve automáticamente. La representación elegida sigue siendo un mecanismo experimental. ADR-001–004 sobreviven. ADR-005 no se crea y Architecture v0.5 no se publica.

La futura consolidación deberá decidir si el invariant es suficientemente estable para ADR-005 y separar esa decisión de:

- outcome enum;
- authority schema;
- taxonomy;
- provider/registry;
- conflict policy;
- Event recognition.

## 19. Session 13 verdict

**SUPPORTED WITH QUALIFICATION.**

H13a–H13f sobreviven directamente a la matriz. H13g–H13h están respaldadas por separación estructural y pruebas, pero no por integración real. La cualificación también refleja que competence, coverage y scope son assertions controladas, no autoridades productivas verificadas.

El resultado no depende solo de tests verdes: los tests distinguen exactamente incapacidad de establecer X frente a establecimiento de NOT X y no necesitan infraestructura adicional.

## 20. Recommended next step

Realizar una **sesión de consolidación/evaluación arquitectónica exclusivamente documental** sobre H13. Debe decidir si el invariant, no las formas TypeScript, está maduro para proponer ADR-005 en una sesión posterior.

No crear ADR-005 todavía. No publicar Architecture v0.5. No avanzar a Treasure Hunt hasta haber decidido y documentado qué parte de H13 se promueve y qué parte continúa experimental.

## Revisión adversarial final

1. **¿Cambió el claim por authority y no por Evidence/Context?** Sí; el test central solo cambia `coverage` con los demás inputs iguales.
2. **¿La autoridad es real?** No; es un fixture tratado como competente. El experimento prueba propagación de límites, no acreditación.
3. **¿Exhaustive se convirtió en verdad universal?** No; está acotado a property+catalogue version.
4. **¿El evaluator inventa negativos?** Solo deriva ausencia negativa cuando una authority scoped afirma exhaustividad; no verifica la verdad de esa assertion.
5. **¿Se usa Experience ID?** Solo se devuelve como referencia; no participa en branch o criterio.
6. **¿Se lavó autoridad mediante `tesBaseline`/Definition/bootstrap?** No; están ausentes y testeados como strings prohibidos en source.
7. **¿Scenario sigue siendo authority final?** No en el experimento; conserva catálogo/scope, mientras classification claims llegan separadas. La arquitectura final sigue abierta.
8. **¿Se inventó precedence?** No; conflicto permanece indeterminado.
9. **¿Activity fortalece el claim?** No; no es consumer real y la proyección mínima conserva el outcome.
10. **¿Undetermined es un TES concept?** No; es un literal de mecanismo experimental para preservar una diferencia epistemológica.
11. **¿Negative equivale a Event no reconocido?** No; únicamente niega relevancia bajo criterio/scope/authority concretos.
12. **¿Los tests protegen una arquitectura deseada?** Protegen falsifiers explícitos; no crean services, engines o taxonomías para conseguirlos.
13. **¿Qué podría invalidar el experimento?** Una API sin evidencia neutral, clasificación inseparable del payload, authority no expresable, coverage no confiable o evaluación necesariamente stateful.
14. **¿Treasure Hunt se tocó?** No; no hay múltiples sujetos, agregación, clues, suficiencia ni group outcome.
