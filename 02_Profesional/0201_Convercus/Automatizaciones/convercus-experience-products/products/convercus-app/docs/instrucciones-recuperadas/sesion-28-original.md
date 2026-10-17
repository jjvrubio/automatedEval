# SESIÓN 28 — ACCOUNT-SOURCED GUEST PRESENTATION

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 27 — Explicit Situated Subject Representation
```

S27 queda consolidada como:

```text
SESSION 27 → CLOSED

H27 → SUPPORTED WITH QUALIFICATION

L3b SUBJECT DISPLAY
→ EXPLICIT SCRIPT-BOUND SUBJECT LABELS
→ EXECUTION-VERIFIED within A/B

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ SUPPORTED within tested scope

DemoScript.subjectPresentations
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

Preservar íntegramente:

```text
H26 → FALSIFIED / historical baseline unchanged

L3a → OPEN
L3c → OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN
L5 → experimentally addressed H25

Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

No promover ninguno de los artefactos experimentales H25/H27.

---

# H28 — PRESSURE SELECTED

Seleccionar exclusivamente:

```text
L3a
```

No resolver L3c.

No resolver L4.

La presión procede de H26 y permanece visible después de H27.

Existe una fuente legítima para presentación aislada de cuenta:

```text
fixture.member.name
→ snapshot.member
→ account display
```

pero el actual:

```text
GuestPerspective.sessionLabel
```

mezcla todavía varias afirmaciones:

```text
account
+
subject relationship
+
second person
+
capability / journey narrative
```

Por ejemplo, copy histórico del tipo:

```text
Usas la cuenta de Lucía, huésped 1...
```

no queda autorizado simplemente porque conozcamos:

```text
member.name
```

ni porque H27 haya introducido:

```text
subjectRef
→ subject presentation
```

Preservar:

```text
account presentation
!=
subject presentation

account/member
!=
Experience subject

subject presentation
!=
subject identity

operationalSessionSubjectRef
!=
authentication identity

represented subject
!=
authenticated user
```

H27 NO creó:

```text
member → subject
viewer → subject
account → subject
session → subject
```

---

# H28 HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
la fuente de cuenta ya existente puede proporcionar
una presentación situada exclusivamente de cuenta
para GuestPerspective.sessionLabel,

y esa presentación puede variar
independientemente de DemoScript.subjectPresentations,

sin introducir relaciones account→subject,
viewer→subject o session→subject,

y sin modificar subjectRef,
operationalSessionSubjectRef,
Evidence attribution,
subjectStates,
Activity,
context,
evaluation,
K o claim.
```

H28 investiga:

```text
account source
→ account-only presentation
```

NO:

```text
account
→ represented subject
```

NO:

```text
account
→ viewer identity
```

NO:

```text
operational session
→ authenticated user
```

---

# VARIABLE UNDER TEST

Exclusivamente:

```text
GuestPerspective.sessionLabel
```

No modificar:

```text
GuestPerspective.subjects[].label
GuestPerspective.subjects[].status
GuestPerspective.message
GuestPerspective.supervision
Activity
App
```

salvo instrumentación estrictamente necesaria para observar el experimento.

Los labels H27 deben permanecer procedentes exclusivamente de:

```text
DemoScript.subjectPresentations
```

No utilizar dichos labels para construir sessionLabel.

---

# FIRST REQUIRED STEP — SOURCE / HOST ANALYSIS

Antes del delta, inspeccionar y documentar la procedencia y threading actuales de:

```text
fixture.member
snapshot.member
GuestPerspective.sessionLabel
projectGuestPerspective()
MockDataAdapter
App consumer
```

Comparar dónde debe ocurrir la transformación presentacional sin introducir una nueva relación semántica.

No asumir de antemano que debe pasarse todo `member` al projector.

Preferir el transporte mínimo que preserve explícitamente que la única autoridad ensayada es:

```text
existing account presentation source
```

Si el experimento exige utilizar `operationalSessionSubjectRef`, `subjectPresentations`, Evidence o Scenario role para construir la presentación de cuenta:

```text
STOP
→ document dependency
→ H28 FALSIFIED or INCONCLUSIVE
```

según corresponda.

---

# ACCOUNT-ONLY COPY

El resultado de sessionLabel debe afirmar exclusivamente la presentación de la cuenta.

Puede ensayarse una forma equivalente a:

```text
Cuenta de Lucía
Cuenta de Inés
```

La forma textual concreta puede adaptarse si el contrato/read model existente lo requiere, pero NO debe incluir:

```text
tú
usas
tu cuenta
huésped 1
P1
subject-p1
has habilitado
puedes activar
Mateo
Huésped 2
```

ni ninguna afirmación equivalente que requiera relacionar cuenta, viewer, sujeto o capability.

---

# A CONTROL

Con composición A:

```text
member.name → Lucía

subject-p1 presentation → Lucía
subject-p2 presentation → Huésped 2
```

debe observarse:

```text
sessionLabel
→ account-source presentation of Lucía

subject-p1 label
→ Lucía

subject-p2 label
→ Huésped 2
```

La coincidencia Lucía/Lucía NO constituye evidencia de relación.

Debe proceder de dos fuentes independientes.

---

# B CONTROL

Con composición B:

```text
member.name → Inés

subject-p1 presentation → Inés
subject-p2 presentation → Mateo
```

debe observarse:

```text
sessionLabel
→ account-source presentation of Inés

subject-p1 label
→ Inés

subject-p2 label
→ Mateo
```

De nuevo:

```text
display equality
!=
identity relation
```

---

# PRIMARY DECOUPLING CONTROL

Sobre B:

```text
member.name → Cuenta Demo

subject-p1 presentation → Inés
subject-p2 presentation → Mateo
```

Debe resultar simultáneamente:

```text
sessionLabel
→ account presentation derived from Cuenta Demo

subject-p1 label
→ Inés

subject-p2 label
→ Mateo
```

y mantenerse:

```text
operationalSessionSubjectRef → subject-p1

Evidence A → subject-p1
Evidence B → subject-p2

Activity unchanged
context unchanged
evaluation unchanged
K unchanged
claim unchanged
```

No introducir mapping para explicar la diferencia.

---

# INVERSE DECOUPLING CONTROL

Mantener:

```text
member.name → Inés
```

y cambiar únicamente:

```text
subject-p1 presentation
→ Participante Alfa
```

Debe resultar:

```text
sessionLabel
→ account presentation of Inés

subject-p1 label
→ Participante Alfa
```

sin ningún otro cambio.

Esto debe demostrar:

```text
subject presentation changes
!=
account presentation changes
```

---

# REPRESENTATION INDEPENDENCE CONTROL

Construir variantes X/Y con:

```text
same Scenario
same member
same Evidence
same session
same Activity
same evaluation

different subjectPresentations
```

Debe cumplirse:

```text
sessionLabel X == sessionLabel Y
subject labels X != subject labels Y
facts X == facts Y
evaluation X == evaluation Y
Activity X == Activity Y
```

Y el control complementario:

```text
same subjectPresentations
different member.name
```

debe producir:

```text
sessionLabel X != sessionLabel Y
subject labels X == subject labels Y
facts X == facts Y
evaluation X == evaluation Y
Activity X == Activity Y
```

---

# NO SECOND PERSON

H28 no debe introducir ni conservar por necesidad experimental afirmaciones perspectivales como:

```text
tú
tu
usas
por ti
```

dentro de la variable estudiada.

Conocer:

```text
member.name = Inés
```

NO autoriza:

```text
Tú eres Inés
```

Conocer:

```text
subject-p1 presentation = Inés
```

tampoco autoriza esa inferencia.

La eventual relación:

```text
viewer/account/session
→ represented subject
```

permanece AUSENTE.

---

# FALSIFIERS

H28 queda FALSIFIED si para producir account presentation en sessionLabel se necesita:

```text
member → subject mapping
```

o:

```text
subject presentation
```

o:

```text
operationalSessionSubjectRef
```

como fundamento de identidad/perspectiva,

o si cambiar la cuenta modifica:

```text
subject labels
subject refs
Evidence attribution
Activity
context
evaluation
K
claim
```

o si cambiar subjectPresentations modifica sessionLabel,

o si debe ampliarse la semántica de:

```text
SubjectReference
member
operationalSessionSubjectRef
```

para hacer pasar el experimento.

También STOP si es necesario introducir:

```text
Actor
Operator
Participant
Representative
AccountSubject
ViewerSubject
AuthenticatedSubject
```

o equivalentes.

No crear la abstracción siguiente dentro de una baseline falsificada.

---

# PRESERVE OPEN PRESSURES

H28 NO resolverá:

```text
L3c
```

Por tanto deben permanecer visibles los textos históricos relacionados con:

```text
journey state
locations
gender
has habilitado
por ti
sigue explorando
```

fuera de `sessionLabel`.

Tampoco modificar:

```text
L4 / App
```

para hacer parecer completa la composición B.

H25/H27 permanecen en cuarentena.

---

# ARTIFACT STATUS

Preservar:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

DemoScript.subjectPresentations
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
```

H28 no constituye evidencia suficiente para promover DemoScript como modelo universal de presentación.

No crear:

```text
PresentationModel
PresentationRegistry
ContentRegistry
PerspectiveEngine
```

ni abstracción equivalente.

---

# OUTPUT

Producir:

```text
session-28-account-sourced-guest-presentation.md
```

documentando al menos:

```text
H27 CONSOLIDATED INPUT
H28 HYPOTHESIS
VARIABLE UNDER TEST
EXISTING ACCOUNT SOURCE
ACCOUNT / SUBJECT / SESSION SEPARATION
SOURCE AND HOST ANALYSIS
THREADING PATH
BASELINE
CODE DELTA
A CONTROL
B CONTROL
ACCOUNT DECOUPLING CONTROL
INVERSE DECOUPLING CONTROL
REPRESENTATION INDEPENDENCE CONTROL
EXECUTION TRACE
L3a RESULT
L3b STATUS
L3c STATUS
L4 STATUS
L5 STATUS
FALSIFICATION ANALYSIS
H28 VERDICT
ARCHITECTURAL CONSEQUENCE
SEMANTIC CONSEQUENCE
ARTIFACT QUARANTINE
WHAT H28 DOES NOT PROVE
REMAINING PRESSURES
```

Concluir exclusivamente con una matriz equivalente a:

```text
H28
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3a ACCOUNT DISPLAY
→ status

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ preserved / unsupported

L3b
→ preserved / experimentally addressed

L3c
→ preserved / open

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H29 automáticamente.

El objetivo sigue siendo:

```text
hypothesis
→ falsification
→ reversible experiment
→ evidence
→ evaluation
→ consolidation
→ eventual promotion
```

y no diseñar retrospectivamente la arquitectura necesaria para que la demo parezca correcta.
