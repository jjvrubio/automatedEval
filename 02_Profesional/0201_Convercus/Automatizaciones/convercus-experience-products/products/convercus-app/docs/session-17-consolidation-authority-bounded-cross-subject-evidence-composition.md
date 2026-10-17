---
title: "Consolidación de la Sesión 17 — Composición de evidencia entre sujetos acotada por autoridad"
aliases:
- "Session 17 Consolidation — Authority-Bounded Cross-Subject Evidence Composition"
language: es
version: "v1.0"
status: "consolidated"
date: "2026-09-07"
project: "Convercus App"
document_type: "informe de consolidación epistemológica"
scope: "evaluación y cuarentena de los findings de Session 17 y primera presión observada sobre el Contrato semántico de producto"
repository_role: "consolidación documental sin refinamiento semántico ni promoción arquitectónica"
semantic_authority: "análisis de producto subordinado; no modifica TES ni el Contrato semántico de producto"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Consolidación de la Sesión 17 — Composición de evidencia entre sujetos acotada por autoridad

## A. Veredicto sobre H17

```text
H17 → SUPPORTED WITH QUALIFICATION
```

La evidencia confirma que un premise autoritativo y aplicable puede acotar la admisibilidad conjunta de Evidence atribuida a P1 y P2 antes de evaluar K. Sin premise, con scope incorrecto, subjects no cubiertos o solo contexto compartido, la admisibilidad no puede establecerse actualmente y la suficiencia no se intenta.

La cualificación principal permanece intacta: la competencia del premise se asumió por construcción dentro de un fixture. Session 17 no demuestra origen, accreditation, revocation, conflicto, cardinalidad ni forma productiva de esa autoridad.

No apareció contradicción material entre [el informe experimental](./session-17-authority-bounded-cross-subject-evidence-composition.md), el código y sus ocho tests. La verificación focalizada de esta consolidación pasó **1 test file / 8 tests**.

## B. Evidencia consolidada

Con alcance explícitamente experimental quedan respaldadas estas separaciones:

```text
atribución de Evidence
!=
admisibilidad conjunta
```

```text
admisibilidad conjunta
!=
evaluación de suficiencia
```

```text
hecho contextual autoritativo
!=
autoridad sobre la consecuencia inferida
```

```text
pluralidad de sujetos
!=
necesidad de Group para H17
```

El caso P1/P2 autorizado conserva `subjectRef` en cada Evidence, establece joint admissibility mediante un premise separado de K y solo entonces obtiene suficiencia bajo A+B. Los controles sin premise, fuera de scope, con P3, booking compartido o Evidence extra conservan `cannot-currently-establish` sin afirmar prohibición, false, impossible o failure.

La formulación general:

```text
autoridad sobre un hecho
!=
autoridad sobre toda inferencia derivada de ese hecho
```

se consolida como consecuencia analítica de ADR-005. No constituye un ADR nuevo.

## C. Qué NO demuestra Session 17

Session 17 no demuestra:

- que Group sea innecesario en general;
- identidad, membership, participación, Evidence, suficiencia u outcome colectivos;
- que `subjectRef` sea Participant, Contributor, account, owner o beneficiary;
- que el claim pertenezca a P1, P2, P1+P2 o una entidad colectiva;
- que compartir booking, stay, property, hunt u objective autorice cooperación;
- admisibilidad universal de Evidence atribuida al mismo sujeto;
- identidad general de contribución;
- autoridad, accreditation, revocation o conflict productivos;
- cardinalidad entre authority premises y evaluation contexts;
- solution recognition, incentive eligibility, pistas ordenadas o TES Event recognition;
- necesidad de un concepto semántico o responsabilidad arquitectónica nueva;
- que el Contrato semántico de producto deba refinarse ya.

## D. Cuarentena de artefactos experimentales

| Artefacto o forma | Clasificación | Límite |
|---|---|---|
| `AuthoritativePremise` | **EXPERIMENTAL / NOT PROMOTED** | Fixture que conserva identity, provenance y scope; no es componente de autoridad. |
| `coveredSubjectRefs` | **EXPERIMENTAL / NOT PROMOTED** | Resuelve P1/P2; no es modelo general de autorización, relación o membership. |
| `CrossSubjectMarkerEvidence.bookingRef` | **EXPERIMENTAL / NOT PROMOTED / UNRESOLVED** | No decide si booking pertenece a Evidence o al contexto de evaluación. |
| Single optional premise parameter | **FIXTURE CONVENIENCE / NOT PROMOTED** | No demuestra cardinalidad 1:1, 1:N, N:1 o N:N. |
| Joint-admissibility outcome literals/reasons | **EXPERIMENTAL / NOT PROMOTED** | Expresan la distinción open-world local, no vocabulario de producto. |
| Cross-subject context/evidence shapes | **PROVISIONAL / NOT PROMOTED** | No son Product Semantic Contract, API ni shared contracts. |
| `authorityRef` y `premiseRef` | **EXPERIMENTAL TRACEABILITY** | Identifican fixtures; no acreditan competencia. |

La ubicación de booking, stay, property y scenario relations permanece estructuralmente abierta:

```text
Evidence A@P1 + Evidence B@P2
        +
relaciones contextuales situadas
        +
premises autoritativos aplicables
```

No se refactoriza el código para anticipar esa solución.

## E. Control de sujeto único

```text
A@P1 + B@P1
→ regression control only
```

El caso comprueba que extraer la evaluación de K no rompió Session 15 y que Session 17 no impuso retroactivamente un requisito cross-subject al caso unipersonal.

No demuestra:

```text
same subject → automatic admissibility
```

La admisibilidad general intra-sujeto no fue la variable de H17 y permanece fuera del alcance de esta consolidación.

## F. Relación con ADR-005

Session 17 aporta **supporting evidence for ADR-005**:

- la atribución permanece factual y separada de joint admissibility;
- joint admissibility es un claim derivado limitado por premise y scope;
- K es otra premisa separada y no decide quién puede contribuir;
- falta de authority suficiente no se convierte en prohibición;
- booking factual no blanquea autoridad sobre su consecuencia;
- Activity/runtime no originan ni fortalecen los claims.

No contradice ADR-005, no exige amendment y no descubre una responsabilidad arquitectónica independiente. El flujo contiene dos transformaciones contextuales encadenables, ambas gobernadas por el mismo principio de no escalado de autoridad.

```text
ADR-005 → ACCEPTED / unchanged
new ADR → NOT NEEDED
```

## G. Impacto arquitectónico

Architecture v0.5 ya representa neutral factual Evidence y authoritative premises convergiendo en contextual evaluation. La etapa experimental de joint admissibility no exige Evidence Composition Layer, service, registry, aggregate o topología adicional.

```text
Architecture v0.5 → ACTIVE / unchanged
architecture revision → NOT NEEDED
```

La presión semántica observada no equivale a presión arquitectónica:

```text
presión sobre el Contrato semántico → sí
nueva responsabilidad arquitectónica → no demostrada
```

No se crea ADR-006 ni Architecture v0.6.

## H. Revisión del Contrato semántico de producto

Se revisó el [Contrato semántico de producto](../../../01-semantic-contract/README.md) sin editarlo. El índice contiene una salvaguarda importante: el contrato de sujetos incorporado pertenece inicialmente al Experience Builder y «no se convierte automáticamente en contrato de la Convercus App». Por ello H17 no contradice un contrato App colectivo ya cristalizado; ese contrato no existe.

La [interpretación de producto vigente](../../../01-semantic-contract/product-interpretations/experience-understanding.md), explícitamente subordinada al contrato, favorece en varios puntos una lectura individual:

- «Mantiene el estado y la progresión de cada participante».
- La experiencia vivida se describe como recorrido de «una persona».
- El estado representa «la situación actual de una participación concreta».
- La operación resuelve «el estado de participación».
- «Cada cliente necesita su propio estado y recorrido».
- Entre las preguntas abiertas figura dónde guardar «el estado individual de progresión».

Estas formulaciones son coherentes con los experimentos anteriores, pero no expresan todavía el caso donde A@P1 y B@P2 conservan atribución y contribuyen bajo authority a una misma evaluación.

La presión observada es:

```text
atribución del sujeto de Evidence
!=
ámbito en el que esa Evidence
puede participar en una evaluación
```

Esto tensiona la simplificación:

```text
un sujeto = un ámbito de participación = un ámbito de evaluación
```

La revisión concluye:

```text
Product Semantic Contract
→ REVIEWED / OBSERVED PRESSURE / unchanged
```

No alcanza `REFINEMENT CANDIDATE`: la evidencia no determina si la solución eventual es un concepto, una relación, una cualificación de scope o ninguna entidad nueva.

## I. Registro de presiones semánticas

Se crea el [Registro de presiones sobre el Contrato semántico de producto](../../../01-semantic-contract/product-semantic-contract-pressure-register.md) como disciplina documental ligera, no como software ni fuente normativa.

Su primera entrada es:

```text
PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ SUPPORTED WITH QUALIFICATION como presión observada
```

PSC-P01 registra la distinción Evidence subject attribution ≠ contribution/evaluation scope, la evidencia P1/P2, sus límites, preguntas, riesgo de promoción y condiciones separadas para experimentar o considerar refinamiento.

Una presión acumulada no modifica el contrato. El umbral es epistemológico: necesidad recurrente de una distinción concreta, no resoluble como detalle de Scenario ni reducible a fixtures, y evidencia suficiente para expresarla sin ontología adicional.

## J. Fronteras que permanecen abiertas

Permanecen `UNRESOLVED`:

- identidad general de contribución;
- distinción participante/contribuyente;
- sujeto o referente de la afirmación derivada;
- ámbito de la afirmación derivada;
- beneficiario de una consecuencia posterior;
- ubicación de `bookingRef` y otras relaciones contextuales;
- identidad de Group y membership;
- participación, Evidence, suficiencia y outcome colectivos;
- acreditación, revocación y conflicto de autoridad;
- cardinalidad authority-premise/evaluation context;
- interacción o concurrencia de varios premises;
- asistencia/influencia de actores externos frente a contribución evidenciaria;
- reconocimiento de solución;
- elegibilidad de incentivo;
- pistas ordenadas/habilitantes;
- latencia, ambigüedad, confusión de identidad y conflicto;
- reconocimiento de Evento TES;
- contratos de API reales.

Se preservan como fronteras distintas:

```text
sujeto/referente de la afirmación
!=
ámbito de la afirmación
!=
beneficiario de una consecuencia posterior
```

`Beneficiario` queda reservado para consecuencias posteriores y no nombra la próxima frontera.

## K. Candidatas a siguiente frontera

Quedan candidatas, sin selección ni diseño:

| ID | Frontera candidata | Pregunta todavía abierta |
|---|---|---|
| A | Sujeto/referente de la afirmación derivada | ¿De qué o de quién habla el claim producido con A@P1 y B@P2? |
| B | Ámbito de la afirmación derivada | ¿Dentro de qué scope puede sostenerse el claim sin confundirlo con sus contributors? |
| C | Distinción participante/contribuyente | ¿La atribución evidenciaria exige roles semánticos distintos? |
| D | Asistencia de actores externos | ¿Cómo distinguir influencia/ayuda de contribución de Evidence? |
| E | Acreditación de autoridad | ¿Qué demuestra competencia para emitir el premise? |
| F | Conflicto o múltiples premises | ¿Cómo preservar indeterminación ante premises incompatibles o concurrentes? |

Esta consolidación no elige Session 18. La selección debe realizarse después de revisar PSC-P01 frente al contrato y comparar qué variable reduce mayor incertidumbre sin resolver simultáneamente las demás.

## L. Veredicto final

```text
H17
→ SUPPORTED WITH QUALIFICATION

ADR-005
→ ACCEPTED / unchanged

Architecture v0.5
→ ACTIVE / unchanged

new ADR
→ NOT NEEDED

architecture revision
→ NOT NEEDED

Product Semantic Contract
→ REVIEWED / OBSERVED PRESSURE / unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE

Group
→ NOT REQUIRED BY H17 / UNRESOLVED

bookingRef placement
→ EXPERIMENTAL / NOT PROMOTED / UNRESOLVED

same-subject control interpretation
→ REGRESSION CONTROL ONLY

AuthoritativePremise shape
→ EXPERIMENTAL / NOT PROMOTED

Recommended immediate next action
→ review PSC-P01 and the current Product Semantic Contract
  against candidate frontiers A–F before selecting Session 18
```

### Método preservado

```text
hallazgo != promoción
presión != refinamiento
refinamiento semántico != arquitectura nueva
```

Session 17 aporta un hallazgo y una presión semántica real. No aporta todavía la solución conceptual ni la necesidad de nueva arquitectura.
