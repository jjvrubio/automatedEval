---
title: "Sesión 18 — Ámbito de validez de una afirmación derivada"
aliases:
- "Session 18 — Derived Claim Contextual Validity"
language: es
version: "v1.1"
status: "experiment under correction"
date: "2026-09-07"
project: "Convercus App"
document_type: "informe de experimento"
scope: "aplicabilidad contextual de una afirmación de suficiencia derivada"
repository_role: "evidencia ejecutable subordinada a ADR-001–005; no constituye promoción semántica ni arquitectónica"
semantic_authority: "experimento técnico de producto subordinado; no modifica TES ni el Contrato semántico de producto"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Sesión 18 — Ámbito de validez de una afirmación derivada

## A. Inspección del repositorio

Se revisaron la implementación y los ocho controles de Sesión 17, su consolidación, PSC-P01, ADR-005 y Architecture v0.5. La salida reutilizada es `AdmittedEvidenceSufficiencyClaim`, producida después de `evaluateJointAdmissibility()` y de la evaluación de K en `evaluateCrossSubjectEvidenceSufficiency()`.

Se preservó la secuencia de Sesión 17:

```text
Evidence A@P1 + Evidence B@P2
        ↓
premisa autoritativa aplicable
        ↓
admisibilidad conjunta
        ↓
K = A AND (B OR C)
        ↓
claim de suficiencia establecido
```

La evidencia original pasó **1 archivo / 5 tests**, pero quedó epistemológicamente limitada: la función solo establecía aplicabilidad cuando el contexto solicitado coincidía exactamente con el de derivación. Esta revisión separa esa evidencia de la corrección falsadora. La matriz corregida pasó **1 archivo / 6 tests**. Los tests de Sesión 17 permanecen sin modificación.

La revisión no consolida H18.

## B. Hipótesis H18

```text
H18 — Ámbito de validez de una afirmación derivada
```

Una afirmación de suficiencia obtenida a partir de Evidence conjuntamente admisible puede mantenerse semánticamente situada en el ámbito bajo el que fue derivada, sin asignarla por ello a un sujeto, propietario, beneficiario o entidad colectiva.

La autoridad de esa afirmación no se extiende automáticamente fuera del ámbito que justificó su derivación. La identidad de los sujetos, la identidad de la Evidence o la existencia de contexto situado compartido no bastan por sí solas para trasladar la afirmación a otro ámbito.

H18 se trató como hipótesis falsable. `S1` y `S2` son únicamente discriminadores experimentales; no son una ontología productiva de ámbitos.

### Corrección epistemológica

La v1.0 no demostraba por sí sola que la autoridad estuviera acotada por una base contextual competente. Demostraba que la implementación exigía igualdad exacta de contexto. Esta revisión introduce una base autoritativa explícita y direccional para el uso del claim desde `S1` hacia `S2`.

## C. Constantes

Se mantuvieron constantes:

- Evidence A@P1 y B@P2;
- `subjectRef` de P1 y P2;
- hunt, stay, property y booking compartidos;
- `AuthoritativePremise` aplicable a la derivación en S1;
- criterio K = A AND (B OR C);
- admisibilidad conjunta de Sesión 17;
- evaluación de suficiencia de Sesión 17;
- separación entre atribución, admisibilidad y suficiencia;
- resultado abierto `cannot-currently-establish`.

No se modificaron K, `evaluateJointAdmissibility()` ni la forma de `AuthoritativePremise`.

## D. Nueva variable

La única variable conceptual nueva fue:

```text
ámbito de validez de la afirmación derivada
```

La observación operacional fue:

```text
claim derivado + contexto solicitado
        ↓
aplicabilidad contextual
```

No se resolvieron sujeto/referente, propietario, beneficiario, Group, participación colectiva ni equivalencia general de ámbitos.

## E. Implementación mínima

Se mantiene [`derived-claim-contextual-validity.ts`](../prototype/src/demo-factory/derived-claim-contextual-validity.ts), con una función pura local:

```text
evaluateDerivedClaimContextualApplicability(
  claim,
  derivationContext,
  requestedContext
)
```

El contexto experimental conserva `S1`/`S2` como `scopeRef` y los datos situados de Sesión 17. La función distingue ahora:

1. el claim ya está `established`; y
2. el contexto solicitado coincide con el de derivación, como control local; y
3. el contexto es distinto, pero existe una `AuthoritativeContextualUseBasis` específica del claim que cubre direccionalmente `fromScopeRef → toScopeRef`.

Cuando no se cumple, devuelve `cannot-currently-establish`; no devuelve `false`, `not-valid`, `forbidden` ni `impossible`. La base no declara `S1 = S2`, no es simétrica y no prueba transitividad ni jerarquía.

La función no añade un campo al claim, no crea un repositorio, servicio, registro, resolver, jerarquía, API ni almacenamiento. El contexto de derivación se pasa explícitamente para evitar confundir la prueba de una consecuencia semántica con el mero almacenamiento de `scopeRef`.

El artefacto y sus literales quedan clasificados como:

```text
EXPERIMENTAL / PROVISIONAL / NOT PROMOTED
```

No se promovieron `ExperimentalClaimContext`, `AuthoritativeContextualUseBasis`, `scopeRef` ni `DerivedClaimContextualApplicability` a vocabulario del producto.

## F. Matriz experimental

| Caso | Evidence | Sujetos | Ámbito de derivación | Ámbito solicitado | Contexto compartido | Resultado observado |
|---|---|---|---|---|---|---|
| A — mismo ámbito | A+B | P1/P2 | S1 | S1 | Sí | `established` |
| B — ámbito distinto sin base adicional | A+B | P1/P2 | S1 | S2 | Sí, incluido booking | `cannot-currently-establish` |
| C — ámbito distinto con base aplicable | A+B | P1/P2 | S1 | S2 | Sí | `established` mediante cobertura direccional S1→S2 |
| D — base para otro destino | A+B | P1/P2 | S1 | S2 | Sí | `cannot-currently-establish` para una base S1→S3 |
| E — Evidence, sujetos y contexto iguales sin base | misma A+B | mismos sujetos | S1 | S2 | booking, stay, property y hunt iguales | `cannot-currently-establish` |
| F — claim no establecido | A+B insuficiente | P1/P2 | S1 | S1 | Sí | `cannot-currently-establish` |

El caso C es el falsador crítico: `S1 != S2` y aun así la utilización se establece mediante una base direccional. Los casos D y E comprueban, respectivamente, que la base debe cubrir el destino correcto y que Evidence, sujetos y contexto compartido no bastan sin esa base.

## G. Separación de etapas

La ejecución conserva esta cadena:

```text
atribución de Evidence
        ↓
admisibilidad conjunta
        ↓
evaluación de suficiencia K
        ↓
claim de suficiencia derivado
        ↓
evaluación de aplicabilidad contextual posterior
```

La última etapa no reevalúa K ni modifica la admisibilidad. Solo pregunta si el claim ya establecido puede sostenerse en el contexto solicitado con un control local o una base direccional explícita. Por ello:

```text
atribución != admisibilidad
admisibilidad != suficiencia
suficiencia != aplicabilidad contextual posterior
```

## H. Controles adversariales

### Same subjects != same scope

A@P1 y B@P2 conservan los mismos subjects en S1 y S2. Sin base de utilización, el resultado S1→S2 no se establece; con la base explícita, sí puede establecerse. La identidad de sujetos no decide el resultado.

### Same Evidence != claim transfer

El claim conserva las mismas referencias de Evidence A y B, pero su derivación en S1 solo puede utilizarse en S2 cuando una base direccional cubre esa utilización.

### Same booking != claim transfer

S1 y S2 comparten `booking-b17`, además de stay, property y hunt. El booking no actúa por sí solo como puente de autoridad contextual; el caso C demuestra que la base competente es una condición separada.

### Derived claim != universal claim

La cobertura direccional S1→S2 no transforma el claim en una afirmación global. Una base para S1→S3 no sirve para S2, y no se infieren simetría, transitividad o equivalencia general.

No se introdujeron owner, beneficiary, Group, `GroupId`, membership, participant, contributor ni claim colectivo.

## I. Análisis de falsación

| Falsador | Resultado |
|---|---|
| F1 — Transferencia legítima sin nueva base | No observada. El caso B permanece `cannot-currently-establish`; el caso C demuestra transferencia acotada con una base explícita. |
| F2 — El ámbito resulta irrelevante | No demostrado. La base debe cubrir la dirección y el destino; no se observó validez universal. |
| F3 — La afirmación necesita necesariamente un sujeto | No observado. El claim se reutiliza sin asignar sujeto/referente. Esta cuestión permanece `UNRESOLVED`. |
| F4 — El ámbito exige una nueva entidad con identidad/lifecycle | No observado. La función pura y local es suficiente para representar la base direccional experimental. |
| F5 — La afirmación hereda autoridad universal de K | No observado. K solo produce el claim después de la admisibilidad; la aplicabilidad contextual es posterior y limitada. |

No apareció condición STOP. La evidencia corregida elimina la circularidad de igualdad exacta, pero H18 todavía no se consolida: S1/S2 y la base direccional son fixtures experimentales y no se prueban persistencia, equivalencia, jerarquía, transitividad o autoridad productiva.

## J. Hallazgos semánticos

La formulación excesiva de v1.0, que queda retirada y no constituye un hallazgo:

```text
claim válido en S1 != claim válido en S2
```

se retira como hallazgo. La formulación respaldada por la corrección es:

```text
validez establecida en S1
no establece automáticamente
validez en S2
```

Además:

```text
S1 != S2
no impide necesariamente la utilización
cuando una base autoritativa direccional la cubre
```

```text
identidad de Evidence != portabilidad automática del claim derivado
```

```text
identidad de sujetos != identidad del ámbito del claim
```

```text
contexto compartido != transferencia automática de autoridad
```

```text
desigualdad de ámbito != inaplicabilidad necesaria
```

```text
cannot-currently-establish != not valid
```

El hallazgo no define qué es un ámbito productivo, cómo se determina, si existe jerarquía, ni si dos ámbitos pueden declararse equivalentes. `claim situated` no se convirtió en `claim colectivo`.

## K. Sujeto o referente de la afirmación

H18 pudo completarse manteniendo:

```text
claim subject/referent → UNRESOLVED
```

La función recibe el claim establecido como resultado de Sesión 17 y no le asigna sujeto, propietario, beneficiario, P1, P2, P1+P2 ni Group. Esta ausencia no impidió observar la limitación contextual buscada.

## L. Impacto sobre PSC-P01

```text
PSC-P01 → UNCHANGED PENDING CORRECTION REVIEW
```

La evidencia original era insuficiente para reforzar PSC-P01 porque la función imponía igualdad exacta. La corrección añade evidencia más discriminante: la aplicabilidad puede establecerse entre ámbitos distintos cuando existe una base autoritativa direccional, y no se establece sin ella.

La distinción ya registrada permanece:

```text
atribución del sujeto de Evidence
!=
ámbito en el que esa Evidence puede contribuir a una evaluación
```

También muestra una consecuencia relacionada:

```text
ámbito de derivación del claim
!=
ámbito solicitado posteriormente
```

No se crea `PSC-P02`. Hasta la consolidación posterior, PSC-P01 se conserva provisionalmente como `UNCHANGED`; no se promueve una nueva presión a partir del nombre de la base experimental. Tampoco se demuestra una forma productiva de ámbito ni se alcanza el umbral para modificar el contrato.

## M. Contrato semántico de producto

```text
Product Semantic Contract → OBSERVED PRESSURE / unchanged
```

H18 aporta evidencia corregida para revisar la diferencia entre contexto de derivación, base autoritativa de utilización y aplicabilidad contextual posterior, pero la prueba usa S1/S2 como fixtures y no demuestra que deba promoverse `ClaimScope`, `EvaluationScope` u otra entidad. No se edita el contrato.

## N. Impacto arquitectónico

```text
ADR-005 → supporting evidence / ACCEPTED / unchanged
Architecture v0.5 → ACTIVE / unchanged
new ADR → NOT NEEDED
architecture revision → NOT NEEDED
```

ADR-005 queda respaldado adicionalmente por la observación de que la autoridad del claim no excede automáticamente el ámbito de las premisas y del contexto de derivación. El delta no introduce una responsabilidad arquitectónica nueva.

## O. Cuarentena de nuevos artefactos

| Artefacto | Clasificación | Límite |
|---|---|---|
| `ExperimentalClaimContext` | `PROVISIONAL / NOT PROMOTED / UNRESOLVED` | Fixture para distinguir S1 y S2; no ontología de producto. |
| `AuthoritativeContextualUseBasis` | `EXPERIMENTAL / NOT PROMOTED` | Base direccional para el claim y destino concretos; no equivalencia, jerarquía o autoridad productiva. |
| `scopeRef` | `EXPERIMENTAL / NOT PROMOTED` | Discriminador observado; no autoridad semántica por almacenamiento. |
| `DerivedClaimContextualApplicability` | `EXPERIMENTAL / NOT PROMOTED` | Outcome local open-world; no enum general de validez. |
| `evaluateDerivedClaimContextualApplicability` | `EXPERIMENTAL / REVERSIBLE` | Función pura; no servicio ni motor de claims. |

## P. Cuestiones abiertas

Permanecen sin resolver:

- sujeto/referente del claim;
- participant/contributor;
- beneficiary;
- Group y membership;
- participación colectiva;
- acreditación y conflicto de autoridad;
- múltiples premises;
- jerarquía de ámbitos;
- equivalencia de ámbitos;
- transitividad de ámbitos;
- persistencia de ámbitos y claims;
- ubicación de `bookingRef`;
- asistencia externa;
- reconocimiento de solución;
- elegibilidad de incentivos;
- pistas ordenadas;
- latencia y ambigüedad;
- reconocimiento de Evento TES;
- contratos reales de API.

También quedan abiertas la nueva derivación legítima en S2, la indeterminación por falta de información sobre ámbito y cualquier regla productiva de equivalencia entre S1 y S2.

## Q. Veredicto final

```text
H18 → INCONCLUSIVE (corrección ejecutada; pendiente de consolidación)

ADR-005 → SUPPORTING EVIDENCE / ACCEPTED / unchanged

Architecture v0.5 → ACTIVE / unchanged

Product Semantic Contract → OBSERVED PRESSURE / unchanged

PSC-P01 → UNCHANGED PENDING CORRECTION REVIEW

new pressure → NO NEW PRESSURE REGISTERED

claim subject/referent → UNRESOLVED

Group → NOT REQUIRED BY H18 / UNRESOLVED

scope equality requirement → NOT ESTABLISHED AS A SEMANTIC RULE

authoritative contextual coverage → EXPERIMENTAL DIRECTIONAL BASIS / NOT PROMOTED

scope concept → EXPERIMENTAL DISTINCTION ONLY / NOT PROMOTED

Recommended next experimental frontier
→ choose from the residual uncertainty by evidence, with priority on
  claim subject/referent versus participant/contributor; do not assume
  Session 19 automatically.
```

La corrección demuestra que la implementación ya no necesita tratar `S_requested == S_derivation` como única condición: un claim establecido en S1 puede utilizarse en S2 cuando una base autoritativa direccional cubre explícitamente ese uso. Sin esa base, permanece `cannot-currently-establish`. Esto elimina la circularidad identificada, pero el resultado global sigue `INCONCLUSIVE` hasta la consolidación posterior, que esta sesión no realiza.
