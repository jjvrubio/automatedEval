---
title: "Consolidación de la Sesión 18 — Ámbito de validez de una afirmación derivada"
aliases:
- "Session 18 Consolidation — Derived Claim Contextual Validity"
language: es
version: "v1.0"
status: "consolidated"
date: "2026-09-07"
project: "Convercus App"
document_type: "informe de consolidación epistemológica"
scope: "consolidación de la corrección falsadora sobre la aplicabilidad contextual de una afirmación derivada"
repository_role: "consolidación documental; no modifica TES, el Contrato semántico de producto ni la arquitectura"
semantic_authority: "análisis de producto subordinado; no constituye autoridad TES ni promoción arquitectónica"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Consolidación de la Sesión 18 — Ámbito de validez de una afirmación derivada

## A. Historial experimental

La Sesión 18 estudió una sola variable conceptual:

```text
ámbito de validez de una afirmación derivada
```

Se mantuvo la cadena de Sesión 17:

```text
Evidence A@P1 + Evidence B@P2
        ↓
premisa autoritativa de Sesión 17
        ↓
admisibilidad conjunta
        ↓
K = A AND (B OR C)
        ↓
afirmación de suficiencia
        ↓
aplicabilidad contextual posterior
```

### v1.0 — evidencia insuficientemente discriminante

La primera implementación establecía aplicabilidad cuando el contexto solicitado coincidía exactamente con el contexto de derivación. Esto aportó evidencia de viabilidad técnica, separación de etapas y continuidad local, pero no permitía distinguir entre:

```text
la autoridad está limitada por una base contextual competente
```

y:

```text
la función exige igualdad exacta de contexto
```

Por tanto, la v1.0 no constituye por sí sola evidencia suficiente para H18.

### v1.1 — corrección falsadora

La corrección conservó `S1 != S2` y añadió una base experimental explícita, acotada y direccional para el uso de un claim desde `S1` hacia `S2`.

La matriz corregida pasó **1 archivo / 6 tests**. La suite completa posterior pasó **13 archivos / 72 tests**, con typecheck y lint correctos. Los tests de Sesión 17 no fueron modificados.

El caso crítico fue:

```text
claim derivado en S1
+
solicitud en S2
+
base autoritativa aplicable S1 → S2
        ↓
established
```

El control sin esa base permaneció:

```text
cannot-currently-establish
```

La corrección elimina la circularidad metodológica de v1.0, pero no convierte los fixtures en conceptos productivos.

## B. Veredicto sobre H18

```text
H18 → SUPPORTED WITH QUALIFICATION
```

La evidencia corregida respalda que:

```text
validez establecida en S1
no establece automáticamente
validez en S2
```

Y también que:

```text
S1 != S2
no impide necesariamente
la utilización en S2
cuando existe una base autoritativa competente y aplicable que cubre ese uso
```

La conclusión consolidable es:

```text
la aplicabilidad contextual de una afirmación derivada
queda limitada por autoridad aplicable,
no por la mera igualdad o desigualdad de identificadores de ámbito
```

La cualificación es material. `S1` y `S2` son discriminadores experimentales, la competencia de la base se asume por construcción y no se han probado persistencia, jerarquía, equivalencia, transitividad, simetría, revocación, múltiples autoridades concurrentes ni una nueva derivación independiente en S2.

## C. Hallazgos consolidados

Quedan respaldados, dentro del alcance experimental:

```text
autoridad suficiente para derivar una afirmación en S1
!=
autoridad automática para utilizarla en S2
```

```text
mismo ámbito != única forma posible de legitimidad contextual
```

```text
desigualdad de ámbito != invalidez
```

```text
misma Evidence != portabilidad automática de la afirmación derivada
```

```text
mismos sujetos != portabilidad automática de la afirmación
```

```text
contexto compartido != transferencia automática de autoridad
```

```text
existencia de autoridad != autoridad aplicable al uso evaluado
```

La relación que queda respaldada es:

```text
premisas
        ↓
derivación legítima
        ↓
afirmación derivada
        ↓
nuevo uso contextual
        ↓
uso respaldado por autoridad suficiente y aplicable
```

Esto no establece que todo uso posterior exija una reevaluación independiente, una nueva acreditación, una nueva premisa, una nueva consulta ni un componente de autoridad. La forma productiva de sostener usos posteriores permanece `UNRESOLVED`.

La ausencia de base suficiente conserva el resultado open-world:

```text
cannot-currently-establish != not valid
ausencia de base suficiente != prohibición
```

## D. Hallazgo retirado de v1.0

La siguiente formulación queda expresamente retirada y no se consolida:

```text
afirmación válida en S1
!=
afirmación válida en S2
```

Era excesiva porque confundía la desigualdad de ámbitos con una negación de validez. La formulación consolidada es:

```text
validez establecida en S1
no establece automáticamente
validez en S2
```

La cobertura autoritativa puede sostener un uso entre ámbitos distintos sin afirmar que los ámbitos sean iguales.

## E. Cuarentena de artefactos

| Artefacto | Clasificación | Límite consolidado |
|---|---|---|
| `AuthoritativePremise` | `EXPERIMENTAL / NOT PROMOTED` | Fixture de Sesión 17; no autoridad productiva. |
| `coveredSubjectRefs` | `EXPERIMENTAL / NOT PROMOTED` | No modelo general de autorización, membership o relación. |
| `CrossSubjectMarkerEvidence.bookingRef` | `EXPERIMENTAL / NOT PROMOTED / UNRESOLVED` | No determina por sí solo ámbito ni autoridad. |
| `ExperimentalClaimContext` | `PROVISIONAL / NOT PROMOTED / UNRESOLVED` | `S1` y `S2` son discriminadores opacos, no ontología de producto. |
| `scopeRef` | `EXPERIMENTAL / NOT PROMOTED` | Almacenarlo no dota de autoridad semántica. |
| `AuthoritativeContextualUseBasis` | `EXPERIMENTAL / NOT PROMOTED` | Base concreta y direccional para el fixture; no equivalencia, jerarquía ni entidad de autorización productiva. |
| `fromScopeRef` / `toScopeRef` | `EXPERIMENTAL / NOT PROMOTED` | No establecen que toda utilización deba expresarse así. |
| `DerivedClaimContextualApplicability` | `EXPERIMENTAL / NOT PROMOTED` | Outcome local open-world; no enumeración general de validez. |
| `evaluateDerivedClaimContextualApplicability` | `EXPERIMENTAL / REVERSIBLE` | Función pura local; no servicio, motor, registro ni repositorio. |

El hallazgo no debe confundirse con el artefacto:

```text
AuthoritativeContextualUseBasis
!=
hallazgo semántico
```

El hallazgo es que la utilización posterior puede necesitar autoridad aplicable al nuevo contexto; la forma concreta de representar esa autoridad permanece abierta.

## F. Vigilancia S1 → S1

```text
S1 → S1
→ control local de continuidad
```

Este caso comprueba que un claim establecido puede mantenerse utilizable en el contexto de derivación dentro del fixture. No demuestra:

```text
mismo ámbito → aplicabilidad automática universal
mismo ámbito → validez perpetua
mismo ámbito → validez incondicional
```

La Sesión 18 no estudió caducidad, revocación, cambios de estado, latencia, temporalidad ni pérdida posterior de autoridad.

## G. Derivación frente a reutilización

Quedan separadas:

```text
autoridad para derivar != autoridad para reutilizar
```

```text
reutilización autorizada de una afirmación != nueva derivación de esa afirmación
```

Sesión 18 estudió la utilización posterior de un claim ya derivado en S1. No estudió reutilizar la Evidence original para ejecutar K de nuevo en S2. La nueva derivación en S2 permanece `UNRESOLVED`.

La reutilización autorizada puede requerir respaldo suficiente y aplicable al uso evaluado, pero esta consolidación no convierte esa condición en una obligación universal de comprobación independiente.

## H. Sujeto o referente de la afirmación

```text
claim subject/referent → UNRESOLVED
claim subject/referent → NOT REQUIRED BY H18
```

La afirmación derivada no fue asignada a P1, P2, P1+P2, propietario, beneficiario o Group. Esto no significa que una afirmación nunca necesite referente; solo que H18 pudo controlar la aplicabilidad contextual sin resolverlo.

## I. Group y semántica colectiva

```text
Group → NOT REQUIRED BY H17
Group → NOT REQUIRED BY H18
Group → UNRESOLVED
```

La evidencia acumulada muestra:

```text
múltiples sujetos → admisibilidad conjunta sin Group
claim derivado de Evidence de varios sujetos → aplicabilidad contextual sin Group
```

No se promueven `GroupClaim`, participación colectiva, membership ni equivalentes. Tampoco se concluye que Group no sea necesario para otros comportamientos del producto.

## J. Relación con ADR-005

```text
ADR-005 → ACCEPTED / unchanged
ADR-005 → supporting evidence
```

Sesión 18 refuerza el principio:

```text
autoridad del claim derivado
≤
autoridad + ámbito + madurez de sus premisas
```

En particular, una base suficiente para derivar no concede automáticamente autoridad universal para reutilizar el resultado. No se crea un ADR nuevo.

## K. Arquitectura v0.5

```text
Architecture v0.5 → ACTIVE / unchanged
new ADR → NOT NEEDED
architecture revision → NOT NEEDED
```

La corrección se resolvió con una función pura local y reversible. No descubrió una responsabilidad arquitectónica independiente. No se construyen capa de ámbito, capa de claims, servicio de autoridad, registro técnico, repositorio, persistencia, proveedor, API ni motor de políticas.

## L. PSC-P01

PSC-P01 conserva su distinción nuclear:

```text
atribución del sujeto de Evidence
!=
ámbito en el que esa Evidence puede contribuir a una evaluación
```

La Sesión 18 añade evidencia descendente relacionada:

```text
autoridad suficiente para derivar una afirmación en un ámbito
!=
autoridad automática para utilizarla en otro
```

Estado consolidado:

```text
PSC-P01 → OPEN / EVIDENCE-BACKED PRESSURE
PSC-P01 → STRENGTHENED BY ADDITIONAL EVIDENCE
```

No se reescribe PSC-P01 como una teoría general de ámbitos y no se crea PSC-P02.

## M. Contrato semántico de producto

```text
Product Semantic Contract → OBSERVED PRESSURE / unchanged
```

La evidencia aumenta la presión para distinguir atribución, contribución, derivación y utilización posterior cuando proceda, pero no identifica todavía una solución semántica concreta. No alcanza `REFINEMENT CANDIDATE` porque:

- `S1` y `S2` son fixtures;
- la forma `fromScopeRef → toScopeRef` es experimental;
- no se demuestra que la distinción no pueda resolverse como detalle de Scenario o contexto;
- no se prueba recurrencia fuera de este experimento;
- no se define una ontología productiva sin inventar `ClaimScope`, `EvaluationScope` o `ParticipationScope`.

El contrato no se modifica.

## N. Fronteras abiertas

Permanecen `UNRESOLVED`:

- identidad general de contribución;
- participant/contributor;
- sujeto/referente del claim;
- beneficiario;
- Group y membership;
- participación colectiva;
- acreditación, revocación y conflicto de autoridad;
- múltiples premises y autoridades concurrentes;
- equivalencia de ámbitos;
- jerarquía de ámbitos;
- transitividad de ámbitos;
- simetría de ámbitos;
- persistencia de ámbitos y afirmaciones;
- nueva derivación en S2;
- indeterminación por información insuficiente;
- ubicación de `bookingRef`;
- asistencia externa;
- reconocimiento de solución;
- elegibilidad de incentivos;
- pistas ordenadas;
- latencia y ambigüedad;
- reconocimiento de Evento TES;
- contratos reales de API.

No se selecciona una Sesión 19 ni se prescribe una frontera posterior.

## O. Candidatas posteriores, sin selección

| Candidata | Pregunta |
|---|---|
| Sujeto o referente | ¿De qué o de quién habla una afirmación derivada de Evidence atribuida a sujetos distintos? |
| Participant/contributor | ¿La atribución y la participación requieren roles distintos? |
| Acreditación de autoridad | ¿Qué hace competente a una fuente para autorizar una premisa? |
| Conflicto o concurrencia | ¿Qué ocurre con premises incompatibles o concurrentes? |
| Asistencia externa | ¿Cómo distinguir influencia, ayuda y contribución evidenciaria? |
| Nueva derivación en otro ámbito | ¿Puede la misma Evidence producir una nueva afirmación en S2 bajo premisas distintas? |

## P. Veredicto final

```text
H18 → SUPPORTED WITH QUALIFICATION

ADR-005 → ACCEPTED / unchanged / supporting evidence

Architecture v0.5 → ACTIVE / unchanged

new ADR → NOT NEEDED

architecture revision → NOT NEEDED

Product Semantic Contract → OBSERVED PRESSURE / unchanged

PSC-P01 → OPEN / EVIDENCE-BACKED PRESSURE
PSC-P01 → STRENGTHENED BY ADDITIONAL EVIDENCE

new semantic pressure → NOT NEEDED

AuthoritativeContextualUseBasis → EXPERIMENTAL / NOT PROMOTED

scopeRef → EXPERIMENTAL / NOT PROMOTED

S1 → S1 interpretation → LOCAL CONTINUITY CONTROL ONLY

claim subject/referent → UNRESOLVED / NOT REQUIRED BY H18

Group → NOT REQUIRED BY H17 / NOT REQUIRED BY H18 / UNRESOLVED

new derivation in S2 → UNRESOLVED

Recommended immediate next action
→ preservar la consolidación y revisar la evolución de PSC-P01 antes de
  seleccionar otra frontera experimental; no abrir automáticamente la Sesión 19.
```

Método preservado:

```text
hallazgo != artefacto
hallazgo != promoción
evidencia adicional != nueva presión
presión reforzada != refinamiento
refinamiento semántico != nueva arquitectura
autoridad de derivación != autoridad de reutilización
```
