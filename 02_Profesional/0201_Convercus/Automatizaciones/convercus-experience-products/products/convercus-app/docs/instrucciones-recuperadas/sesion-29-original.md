# SESIÓN 29 — OPERATIONAL SUBJECT STATUS PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 28 — Account-Sourced Guest Presentation
```

No reconstruir decisiones anteriores.

La baseline consolidada de entrada es:

```text
SESSION 28 → CLOSED

H28 → SUPPORTED WITH QUALIFICATION

L3a ACCOUNT DISPLAY
→ ACCOUNT-SOURCED
→ ACCOUNT-ONLY
→ EXECUTION-VERIFIED within A/B

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ EXECUTION-VERIFIED within tested scope

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / OPEN

L4
→ PRESERVED / SOURCE-INSPECTION / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged

ADR-001–005
→ ACCEPTED / unchanged

TES → unchanged

Product Semantic Contract
→ unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Artefactos en cuarentena:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

DemoScript.subjectPresentations
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

H28 account-name transport / formatting
→ LOCAL PROTOTYPE EXPERIMENT
→ NOT PROMOTED
```

---

# 1. PRESSURE SELECTED

Seleccionar exclusivamente, dentro de L3c:

```text
GuestPerspective.subjects[].status
```

NO seleccionar todavía:

```text
GuestPerspective.message
```

La separación:

```text
subjects[].status
vs
message
```

es una descomposición diagnóstica de L3c para permitir falsación independiente.

NO constituye:

```text
nuevo contrato
nueva arquitectura
nueva taxonomía TES
PSC extension
```

L3c permanece como presión consolidada hasta que exista evidencia suficiente para reconsiderarla.

---

# 2. MOTIVACIÓN

S28 confirma que siguen presentes expresiones históricas como:

```text
Habilitado por ti
```

mientras la fuente operacional:

```text
subjectStates
```

ya proporciona información sobre el estado presente de los sujetos.

La cuestión de S29 NO es todavía:

```text
¿cómo construimos una narrativa situada
sobre el estado del huésped?
```

La cuestión es anterior:

```text
¿qué parte de subjects[].status
puede estar autorizada únicamente
por el estado operacional existente?
```

Preservar:

```text
operational state
!=
causal attribution

operational state
!=
actor attribution

operational state
!=
viewer perspective

operational state
!=
journey narrative

operational state
!=
gender information
```

Especialmente:

```text
P2 is enabled
```

NO implica:

```text
P1 enabled P2
```

y aunque una acción anterior haya producido la transición:

```text
P1 enabled P2
```

NO implica:

```text
you enabled P2
```

porque no existe todavía una relación legitimada:

```text
viewer
→ P1
```

ni:

```text
account
→ P1
```

ni:

```text
authenticated user
→ P1
```

---

# 3. H29 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
GuestPerspective.subjects[].status
puede representar exclusivamente
el estado operacional presente
de cada sujeto utilizando
la fuente existente subjectStates,

sin introducir causalidad,
actor attribution,
segunda persona,
género del sujeto,
localización
ni journey narrative,

y sin modificar
subject identity/reference,
account presentation,
subject presentation,
Activity,
Evidence attribution,
operationalSessionSubjectRef,
context,
evaluation,
K o claim.
```

La relación bajo estudio es estrictamente:

```text
existing subject operational state
→ neutral present-state representation
```

NO:

```text
state
→ cause of state
```

NO:

```text
state
→ actor who caused state
```

NO:

```text
state
→ viewer relation
```

NO:

```text
state
→ journey interpretation
```

---

# 4. NO-NEW-COMPOSITION-RELATION CONDITION

S29 debe intentar resolver esta presión utilizando exclusivamente las relaciones operacionales existentes.

No añadir en esta sesión:

```text
DemoScript.subjectStatusPresentations

Scenario.subjectStatusPresentation

Fixture.subjectStatusPresentation

StatusPresentationRegistry

PresentationModel

PerspectiveModel
```

o equivalentes.

Si la inspección demuestra que `subjectStates` no puede acreditar una representación de estado suficientemente precisa sin añadir una nueva relación declarativa:

```text
STOP
→ document missing relation
→ preserve evidence
→ H29 FALSIFIED or INCONCLUSIVE
```

No crear la solución siguiente dentro de esa misma baseline.

Una sesión posterior podría autorizar una relación mínima si la falsación la justificase.

---

# 5. VARIABLE UNDER TEST

Modificar exclusivamente la procedencia/construcción de:

```text
GuestPerspective.subjects[].status
```

Preservar:

```text
GuestPerspective.sessionLabel
GuestPerspective.subjects[].label
GuestPerspective.message
GuestPerspective.supervision
Activity
App
```

H28 debe seguir gobernando:

```text
sessionLabel
→ account-only presentation
```

H27 debe seguir gobernando:

```text
subjects[].label
→ DemoScript.subjectPresentations
```

H25 debe seguir gobernando la representación situada posterior de Activity.

No reutilizar ninguno de esos campos como fuente de `subjects[].status`.

---

# 6. FIRST REQUIRED STEP — SOURCE INSPECTION

Antes de modificar código, documentar el recorrido exacto actual de:

```text
Scenario subjects
subjectStates
operationalSessionSubjectRef
Evidence
GuestPerspective.subjects[].status
projectGuestPerspective()
```

Identificar todos los valores reales que puede adoptar `subjectStates` dentro de Family Adventure y en qué transición aparecen.

Construir antes del delta una matriz:

```text
subjectRef
operational state
phase/action
current status copy
information justified by state
information NOT justified by state
```

No diseñar primero los nuevos textos y después buscar una justificación.

La fuente debe preceder a la representación.

---

# 7. REPRESENTATION RULE

Si la inspección confirma que los estados existentes contienen información suficiente, puede realizarse una representación local y reversible del significado operacional existente.

La representación debe ser:

```text
state-only
neutral
non-perspectival
non-causal
non-locational
non-narrative
```

No debe contener:

```text
tú
tu
por ti
contigo
gracias a ti
por Lucía
por Inés
por P1
por la cuenta
```

ni formulaciones semánticamente equivalentes.

Tampoco debe afirmar género del sujeto si éste no forma parte de la fuente.

Si el castellano exige concordancia gramatical, formular el texto alrededor de un sustantivo cuyo género sea conocido por el propio copy, por ejemplo conceptualmente:

```text
Estado: ...
Habilitación: ...
```

en lugar de atribuir género a la persona representada.

NO asumir esos ejemplos como el copy obligatorio.

Códex debe derivar el vocabulario final del estado real encontrado en la baseline y documentar explícitamente el mapping:

```text
operational state
→ displayed state
```

No introducir significado adicional para conseguir copy más natural.

---

# 8. AUTHORITY DIRECTION

La dirección obligatoria es:

```text
Scenario subject
→ corresponding existing subjectState
→ status representation
```

No:

```text
status presentation
→ subject existence
```

No:

```text
subjectPresentations
→ state
```

No:

```text
member
→ state
```

No:

```text
Activity presentation
→ state
```

No:

```text
Evidence count
→ invented state
```

`subjects[].status` debe describir un estado existente, no crearlo ni inferirlo de copy coexistente.

---

# 9. TEMPORAL / TRANSITION CONTROL

Aprovechar la secuencia operacional ya existente para comprobar discriminación temporal.

Como mínimo estudiar:

```text
initial
enlist-p1
discover-clue-a
activate-p2
discover-clue-b
reset
```

Para cada sujeto identificar cuándo cambia realmente `subjectStates`.

Debe cumplirse:

```text
same subjectState
→ same status representation
```

aunque cambien otros elementos como Evidence o Activity.

Y cuando una acción produzca legítimamente una transición:

```text
subjectState X → subjectState Y
```

debe observarse:

```text
status X → status Y
```

sólo en correspondencia con esa transición.

No afirmar que la transición fue causada por un actor concreto salvo que esa causalidad ya esté representada explícitamente en una fuente autoritativa; si esto fuese necesario para el status:

```text
STOP
```

---

# 10. A / B CONTROL

Ejecutar A y B a través de sus secuencias completas.

Cuando:

```text
subjectRef A == subjectRef B
operational state A == operational state B
```

la representación de status debe ser equivalente aunque difieran:

```text
member.name
subjectPresentations
context
Activity presentation
situated locations
```

Este control es importante.

S29 NO busca status situados por composición.

Busca comprobar si el estado operacional ya disponible constituye autoridad suficiente para una representación neutral del presente.

Si A y B necesitan status distintos pese a tener el mismo operational state:

```text
H29 NO-NEW-COMPOSITION-RELATION
→ falsification pressure
```

No introducir automáticamente una nueva relación para resolverlo.

---

# 11. ACCOUNT INDEPENDENCE CONTROL

Perturbar exclusivamente:

```text
member.name
```

manteniendo iguales:

```text
Scenario
subjectStates
subjectPresentations
actions
Evidence
context
evaluation
Activity
```

Debe cumplirse:

```text
sessionLabel changes
subjects[].status unchanged
```

La presentación de cuenta H28 no puede convertirse en autoridad del estado.

---

# 12. SUBJECT PRESENTATION INDEPENDENCE CONTROL

Perturbar exclusivamente:

```text
DemoScript.subjectPresentations
```

manteniendo todo el estado operacional igual.

Debe cumplirse:

```text
subjects[].label changes
subjects[].status unchanged
```

Especialmente:

```text
subject-p1 label = Participante Alfa
```

no debe alterar ninguna representación de estado.

Esto preserva:

```text
subject presentation
!=
subject operational state
```

---

# 13. ACTIVITY REPRESENTATION INDEPENDENCE CONTROL

Perturbar únicamente representación H25 cuando sea técnicamente posible dentro del harness, sin cambiar la acción/hecho ocurrido.

Debe cumplirse:

```text
Activity representation changes
subjects[].status unchanged
```

No reutilizar:

```text
activityPresentation
```

para explicar el estado presente.

Preservar:

```text
Activity
→ representation of occurred Activity

subjectStates
→ present operational state
```

---

# 14. EVIDENCE DISCRIMINATION CONTROL

Usar las fases del recorrido en las que aumenta Evidence pero no cambia el `subjectState` relevante.

Debe comprobarse:

```text
Evidence changes
+
subjectState unchanged
→
status unchanged
```

Esto debe impedir que el projector reconstruya estado desde:

```text
Evidence count
marker presence
K
claim
```

si ya existe `subjectStates` como fuente autoritativa.

Preservar:

```text
Evidence
!=
subject state
```

y:

```text
evaluation
!=
subject state
```

---

# 15. CAUSALITY NEGATIVE CONTROL

Prestar especial atención a la transición que habilita P2.

Si el estado resultante sólo acredita:

```text
subject-p2
→ enabled
```

la representación puede afirmar únicamente ese estado.

No puede afirmar:

```text
enabled by you
enabled by P1
enabled by Inés
enabled by Lucía
```

sin una fuente autoritativa adicional.

Incluso si la secuencia del Demo Script contiene una acción anterior de activación, no convertir automáticamente:

```text
temporal precedence
```

en:

```text
actor attribution
```

ni:

```text
viewer attribution
```

Preservar:

```text
transition occurrence
!=
viewer identity
```

y:

```text
action chronology
!=
perspective authority
```

---

# 16. MESSAGE FREEZE

`GuestPerspective.message` debe permanecer sin resolver y, cuando sea posible, byte-for-byte idéntico en su construcción.

Los síntomas existentes deben permanecer visibles:

```text
jardín
fuente
mirador/patio mismatch where applicable
segunda persona
sigue explorando
journey narrative
```

No corregirlos incidentalmente.

La existencia de esos síntomas NO falsifica H29 porque no forman parte de la variable bajo prueba.

Conservarlos permite que la siguiente presión continúe siendo observable.

---

# 17. L3c STATUS AFTER H29

No declarar automáticamente:

```text
L3c → RESOLVED
```

aunque H29 sea positiva.

En caso de éxito, registrar algo equivalente a:

```text
L3c subject-status component
→ experimentally addressed
```

mientras:

```text
L3c journey/present-state narrative
→ OPEN
```

Esta formulación es diagnóstica.

No crear nuevos identificadores normativos L3c1/L3c2 salvo que exista una necesidad demostrada de gobierno posterior.

---

# 18. FALSIFIERS

H29 queda FALSIFIED si:

```text
subjects[].status
cannot be derived
from existing subjectStates
without another relationship
```

o si:

```text
changing account presentation
changes status
```

o:

```text
changing subject presentation
changes status
```

o:

```text
changing Activity representation
changes status
```

sin cambio operacional correspondiente,

o si:

```text
Evidence/K/claim
must be used to reconstruct
a state already represented in subjectStates
```

o si se requiere introducir:

```text
viewer
actor
operator
participant
representative
accountSubject
viewerSubject
```

o equivalente.

También falsifica la versión no-new-relation de H29 si una representación correcta exige:

```text
DemoScript.subjectStatusPresentations
```

o cualquier nueva relación declarativa de composición.

Ante cualquiera de esos casos:

```text
STOP
→ preserve evidence
→ document missing relation
→ do not solve it in S29
```

---

# 19. REGRESSION REQUIREMENTS

Preservar las baselines históricas H21–H28.

Comprobar al menos:

```text
S20 vertical
H21
H22
H23
H24
H25
H26
H27
H28
```

según el esquema histórico ya utilizado.

A/B deben mantener:

```text
subjectRefs
operationalSessionSubjectRef
Evidence attribution
context
evaluation
K
claim
Activity
account presentation
subject presentation
```

excepto exclusivamente el cambio autorizado en:

```text
subjects[].status
```

---

# 20. OUTPUT

Producir:

```text
session-29-operational-subject-status-provenance.md
```

con al menos:

```text
H28 CONSOLIDATED INPUT

H29 HYPOTHESIS

VARIABLE UNDER TEST

WHY L3c IS DIAGNOSTICALLY SPLIT

EXISTING OPERATIONAL STATE SOURCE

PRE-DELTA STATE / COPY MATRIX

SOURCE AUTHORITY

NO-NEW-COMPOSITION-RELATION CONDITION

HOST / PROJECTION ANALYSIS

THREADING PATH

BASELINE

CODE DELTA

A CONTROL

B CONTROL

TEMPORAL / TRANSITION CONTROL

ACCOUNT INDEPENDENCE CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

ACTIVITY REPRESENTATION INDEPENDENCE CONTROL

EVIDENCE DISCRIMINATION CONTROL

CAUSALITY NEGATIVE CONTROL

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c SUBJECT STATUS RESULT

L3c REMAINING NARRATIVE PRESSURE

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H29 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H29 DOES NOT PROVE

REMAINING PRESSURES
```

Concluir únicamente con una matriz equivalente a:

```text
H29
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3c SUBJECT STATUS
→ status

STATE / PRESENTATION AUTHORITY
→ supported / unsupported

CAUSAL / VIEWER ATTRIBUTION
→ NOT INTRODUCED / introduced-invalidly

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c JOURNEY NARRATIVE
→ preserved / open

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed H25

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H30 automáticamente.

---

# 21. METHODOLOGICAL GUARDRAIL

Mantener:

```text
having a state
!=
knowing why that state exists

knowing a transition occurred
!=
knowing who should be credited for it

knowing the operational subject
!=
knowing the viewer

knowing P1 operates in the session
!=
viewer is P1

state representation
!=
journey narrative
```

S29 debe intentar **reducir la afirmación al nivel de la evidencia disponible**, no aumentar la semántica del modelo para conservar el copy histórico.

El objetivo sigue siendo:

```text
hipótesis
→ falsación
→ experimento reversible
→ evidencia
→ evaluación
→ consolidación
→ eventual promoción
```

La arquitectura debe continuar emergiendo de relaciones demostradas, no de los textos que la demo históricamente necesitaba mostrar.
