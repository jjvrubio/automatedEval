# SESIÓN 34 — OPERATIONAL SESSION SUBJECT REPRESENTATION PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 33 — Operational Supervision Subject Representation Provenance
```

No reconstruir decisiones anteriores.

---

# 1. BASELINE CONSOLIDADA

```text
SESSION 33 → CLOSED

H33
→ SUPPORTED WITH QUALIFICATION

NO-NEW-RELATION
→ SUFFICIENT

SUPERVISION SUBJECT AUTHORITY
→ EXISTING OPERATIONAL SOURCE
→ SupervisionPerspective.subjects[].id

HUMAN SUBJECT PRESENTATION
→ NOT REQUIRED for tested diagnostic purpose

GP / SP PRESENTATION SEPARATION
→ SUPPORTED within A/B

APP CONSUMER BOUNDARY
→ PRESERVED

A/B SUPERVISION SUBJECT REPRESENTATION
→ CURRENT APP DOM-INTEGRATION VERIFIED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 FRAMING
→ PRESERVED / EXPERIMENTALLY ADDRESSED H32

L4 SUPERVISION SUBJECT
→ EXISTING-SOURCE / LOCALLY RENDERED
→ EXPERIMENTALLY ADDRESSED H33

L4 SUPERVISION SESSION
→ PRESERVED / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ OBSERVED
→ QUALIFIED BY H33
→ NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

No promover relaciones H25–H33.

---

# 2. PRESSURE SELECTED

Seleccionar exclusivamente en Supervision:

```text
"Cuenta/sesión operativa"
+
sessionSubjectRef
```

La presión es la **procedencia semántica de la representación de `sessionSubjectRef`**.

No seleccionar todavía:

```text
huntName
fixed Family Adventure navigation link
other supervision terminology
human-friendly supervision labels
viewer identity
authentication
```

---

# 3. H34 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de SupervisionPerspective,
la relación operacional existente
que produce sessionSubjectRef
puede proporcionar una representación
diagnóstica neutral de esa referencia,

sin atribuir cuenta,
autenticación,
viewer,
ownership,
representación humana
ni relación account→subject,

sin crear una nueva relación
y sin modificar runtime,
subjects,
Evidence,
evaluation,
K o claim.
```

Condición:

```text
NO-NEW-RELATION
```

La relación investigada es:

```text
existing operational session subject reference
→ neutral diagnostic representation
```

NO:

```text
session subject
→ account owner
```

NO:

```text
session subject
→ authenticated user
```

NO:

```text
session subject
→ viewer
```

NO:

```text
session subject
→ human identity
```

---

# 4. WHY NO NEW RELATION IS AUTHORIZED

S33 demostró que Supervision puede identificar sujetos mediante datos operacionales ya presentes.

El campo:

```text
sessionSubjectRef
```

también existe ya en SupervisionPerspective.

Por tanto debe investigarse primero si el problema actual es:

```text
existing operational data
+
overstated UI label
```

y no:

```text
missing presentation relation
```

Preservar:

```text
overclaim in copy
!=
missing data
```

y:

```text
reducing copy to existing authority
!=
creating semantics
```

---

# 5. VARIABLE UNDER TEST

Exclusivamente la representación compuesta actualmente por:

```text
"Cuenta/sesión operativa"
+
sessionSubjectRef
```

No modificar:

```text
Supervision subject headings H33
subjects[].exists
subjects[].operationalState
subjects[].evidenceCount
Evidence attribution
jointAdmissibility
sufficiency
derivedClaim
criterion K
```

Ni:

```text
GuestPerspective
Activity
branding
introductory framing
huntName
navigation
```

---

# 6. FIRST REQUIRED STEP — SEMANTIC SOURCE INSPECTION

Antes de cambiar App, inspeccionar:

```text
ScenarioDefinition.operationalSessionSubjectRef

SupervisionPerspectiveReadModel.sessionSubjectRef

projectSupervisionPerspective()

MockDataAdapter / provider usage

action admission checks

App SystemPage consumer
```

Buscar todos los usos de:

```text
operationalSessionSubjectRef
sessionSubjectRef
```

y construir una matriz:

```text
field
declaring layer
producer
consumers
operational effect
semantic claim explicitly supported
claims NOT supported
```

No inferir significado exclusivamente del nombre de la propiedad.

---

# 7. QUESTIONS THE INSPECTION MUST ANSWER

Determinar exactamente si la fuente acredita:

```text
A. una referencia a un sujeto

B. una referencia al sujeto asociado
   al mecanismo operacional de sesión

C. el sujeto que puede ejecutar
   ciertas acciones

D. identidad de cuenta

E. identidad autenticada

F. viewer

G. titularidad/ownership
```

No agruparlas.

La inspección debe documentar para cada una:

```text
SUPPORTED
NOT SUPPORTED
NOT DETERMINED
```

H34 sólo puede representar las afirmaciones SUPPORTED.

---

# 8. ACCOUNT NEGATIVE AUTHORITY

Preservar explícitamente la evidencia acumulada:

```text
fixture.member
→ account presentation H28

operationalSessionSubjectRef
→ operational responsibility
```

Hasta ahora no existe:

```text
member
→ operationalSessionSubjectRef
```

ni:

```text
account
→ Experience subject
```

Por tanto, salvo evidencia nueva ya existente en contratos:

```text
"Cuenta"
```

no puede formar parte de la representación H34.

No introducir mapping para conservar esa palabra.

---

# 9. H33 SUBJECT REPRESENTATION SEPARATION

S33 establece:

```text
Supervision.subjects[].id
→ operational diagnostic subject identification
```

H34 debe estudiar si:

```text
sessionSubjectRef
```

puede correlacionarse legítimamente con esas referencias.

Si ambos contienen el mismo valor:

```text
subject-p1
```

preservar:

```text
value equality
!=
new identity relation
```

La relación sólo puede ser la ya declarada en el modelo operacional.

No utilizar la igualdad para inferir cuenta/viewer.

---

# 10. CANDIDATE NEUTRAL REPRESENTATIONS

Después de inspeccionar semántica, comparar posibles representaciones diagnósticas mínimas.

Ejemplos conceptuales, NO copy obligatorio:

```text
Referencia de sesión operativa · subject-p1

Sujeto de sesión operativa · subject-p1

Referencia operacional de sujeto · subject-p1
```

Cada opción hace afirmaciones ligeramente distintas.

Seleccionar únicamente la que esté respaldada por la semántica inspeccionada.

Si ninguna formulación amigable puede expresarse sin añadir significado:

```text
render raw field/value in diagnostic form
```

puede ser suficiente.

H34 estudia autoridad, no estética.

---

# 11. FORBIDDEN REPRESENTATIONS

No usar:

```text
Cuenta
Cuenta activa
Cuenta operativa
Usuario
Usuario activo
Usuario autenticado
Viewer
Persona
Participante
Operador
Representante
Titular
Lucía
Inés
P1
```

salvo que un significado concreto esté explícitamente declarado por la fuente inspeccionada.

No utilizar H27, member.name ni parsing para humanizar.

---

# 12. NO-PARSING CONDITION

La presentación del valor debe conservar:

```text
sessionSubjectRef
```

literalmente si se presenta.

No:

```text
subject-p1
→ P1
```

mediante:

```text
split
replace
regex
substring
index
branch
```

No mapear:

```text
subject-p1 → Lucía/Inés
```

El valor técnico es admisible en una superficie diagnóstica.

---

# 13. A CONTROL

Ejecutar A con App actual y recorrer Family Adventure.

Navegar a Supervisión en las fases necesarias.

Comprobar:

```text
sessionSubjectRef
→ unchanged
```

y que la nueva representación:

```text
does not contain unsupported account/viewer language
```

Preservar todos los demás valores SP.

---

# 14. B CONTROL

Ejecutar B mediante la misma App.

Debe aplicarse exactamente la misma regla diagnóstica.

Si:

```text
sessionSubjectRef A == sessionSubjectRef B
```

la representación deberá ser equivalente.

No utilizar:

```text
Lucía
Inés
brand
intro
subjectPresentations
context
```

para distinguirla.

---

# 15. ACCOUNT INDEPENDENCE CONTROL

Perturbar únicamente:

```text
member.name
```

Debe observarse:

```text
account presentation changes

Supervision session representation
→ unchanged
```

Esto es central para falsar cualquier dependencia implícita:

```text
account
→ sessionSubjectRef
```

---

# 16. SUBJECT PRESENTATION INDEPENDENCE

Perturbar:

```text
DemoScript.subjectPresentations
```

Debe cambiar GP y conservar completamente la representación H34.

Preservar:

```text
human subject presentation
!=
operational session reference
```

---

# 17. BRAND / INTRO / JOURNEY / ACTIVITY INDEPENDENCE

Perturbar independientemente:

```text
brand.name
experimentalIntroductoryFraming
experimentalJourneyPresentations
activityPresentation
```

La representación de sesión supervisora debe permanecer idéntica.

No permitir que Script-bound presentation se convierta en fuente de semántica operacional.

---

# 18. STATE / EVIDENCE INDEPENDENCE

Durante el recorrido:

```text
subjectStates change
Evidence grows
evaluation changes
claim changes
```

mientras:

```text
operationalSessionSubjectRef
```

permanezca igual.

Debe resultar:

```text
session representation unchanged
```

si su fuente no ha cambiado.

No reconstruirla desde estado o Evidence.

---

# 19. SESSION SUBJECT VARIATION CONTROL

Investigar si el repositorio ofrece una forma legítima, local y reversible de variar:

```text
operationalSessionSubjectRef
```

sin inventar una nueva relación ni declarar esa variante como composición productiva.

Si es posible mediante una copia de Scenario exclusivamente de harness:

```text
subjectRef X
→ session representation X

subjectRef Y
→ session representation Y
```

manteniendo el label/formatting constante.

Pero NO ejecutar acciones si la variante vuelve incoherentes las guards del Scenario.

El objetivo es observar transporte/proyección/render, no demostrar una nueva ruta operacional.

Clasificar como:

```text
isolated read-model / composition observation
```

si no constituye recorrido alcanzable.

Si cambiar la referencia exige alterar semántica operacional material:

```text
DO NOT RUN
```

y documentar la limitación.

---

# 20. UNKNOWN OPAQUE REF CONTROL

Si puede hacerse de forma aislada sin modificar Scenario productivo, usar una referencia opaca:

```text
opaque:session-subject/X
```

como entrada de proyección.

Debe renderizarse sin:

```text
P1
Lucía
Huésped 2
account
```

ni parsing.

No ejecutar acciones.

No afirmar que la referencia sea válida para una composición productiva.

Este control prueba el consumidor, no la semántica de un nuevo sujeto.

---

# 21. APP CONSUMER BOUNDARY

Mantener:

```text
Scenario
→ SupervisionPerspective
→ App
→ render
```

App no debe consultar:

```text
Scenario directly
member
DemoScript
subjectPresentations
fixtures
```

para explicar `sessionSubjectRef`.

No branch:

```text
if subject-p1 ...
```

No lookup A/B.

---

# 22. NO-NEW-RELATION ANALYSIS

H34 queda SUPPORTED si:

```text
existing sessionSubjectRef semantics
are sufficient
for a neutral diagnostic representation
```

sin otra relación.

Si la superficie necesita realmente representar:

```text
account
viewer
authenticated user
human operator
```

y esas relaciones no existen:

```text
H34
→ FALSIFIED under NO-NEW-RELATION

STOP
```

Documentar exactamente qué relación falta.

No crearla en H34.

---

# 23. "CUENTA" REMOVAL IS NOT ACCOUNT DENIAL

Si la inspección confirma que `sessionSubjectRef` no acredita cuenta y el nuevo copy elimina esa palabra, registrar:

```text
removing unsupported account language
!=
proving that no account exists operationally
```

H34 sólo establece:

```text
current source
does not authorize that claim
```

No formula una teoría negativa universal sobre autenticación/cuentas.

---

# 24. OTHER SUPERVISION FREEZE

Preservar:

```text
subject headings H33
Evaluación compartida
Criterio K
Evidence recibida
Admisibilidad conjunta
Suficiencia K
Afirmación derivada
Evidence y atribución
```

No corregir terminología colateral.

---

# 25. HUNTNAME FREEZE

Preservar:

```text
GuestPerspective.huntName
```

y su h1 actual.

No aprovechar H34 para conectarlo con Experience.name.

---

# 26. NAVIGATION FREEZE

Preservar el acceso fijo detectado:

```text
/?demo=hospitality-family-adventure
```

No resolver composición/navegación en esta sesión.

---

# 27. CURRENT APP EXECUTION

Si existe delta de App:

```text
A DOM/integration → REQUIRED
B DOM/integration → REQUIRED
```

Navegar a Supervisión y comprobar el campo H34.

Además verificar Home / Activity para preservar:

```text
H25
H27
H28
H29
H30
H32
H33
```

Registrar por separado:

```text
DOM/integration verification
browser visual validation
```

No equipararlos.

---

# 28. NEGATIVE CONTROLS

Retail y Arrival deben permanecer sin Supervision Family Adventure.

No añadir campos/fallbacks de sesión para hacer genérico el cambio.

```text
absence remains absence
```

---

# 29. CURRENT CUMULATIVE REGRESSION

Sobre aplicación actual verificar:

```text
H25 Activity
H27 GP labels
H28 account display
H29 status
H30 message
H32 brand + intro
H33 SP subject IDs
```

La única diferencia autorizada debe ser:

```text
Supervision session label / representation
```

No sustituir esta verificación por replay histórico.

---

# 30. RECURRING PRESENTATION PRESSURE

Registrar qué aporta H34 a la distinción emergente:

```text
situated/editorial presentation
vs
operational/diagnostic representation
```

Si H34 se resuelve desde autoridad operacional existente, se acumula más contraevidencia a:

```text
all presentation belongs in Script
```

pero NO promover todavía:

```text
derive operational presentation
declare experiential presentation
```

a principio arquitectónico.

Sigue siendo hipótesis emergente.

No ADR.

No PresentationBoundary.

---

# 31. FALSIFIERS

H34 queda FALSIFIED si:

```text
sessionSubjectRef existing semantics
are insufficient to describe the surface
without account/viewer/authentication claims
```

o si eliminar la mezcla requiere:

```text
member.name
subjectPresentations
DemoScript
ID parsing
A/B branching
new account→subject relation
viewer→subject
authentication identity
```

o si el cambio altera:

```text
operationalSessionSubjectRef
subject refs
Evidence attribution
states
evaluation
K
claim
```

o exige solucionar simultáneamente:

```text
huntName
navigation
other supervision terminology
```

Ante falsador:

```text
STOP
→ preserve evidence
→ do not introduce missing relation
```

---

# 32. OUTPUT

Producir:

```text
session-34-operational-session-subject-representation-provenance.md
```

con al menos:

```text
H33 CONSOLIDATED INPUT

H34 HYPOTHESIS

VARIABLE UNDER TEST

WHY NO NEW RELATION IS AUTHORIZED

SESSION SUBJECT SOURCE INSPECTION

SEMANTIC SUPPORT MATRIX

CURRENT COPY DECOMPOSITION

ACCOUNT NEGATIVE AUTHORITY

H33 / SESSION REPRESENTATION SEPARATION

CANDIDATE NEUTRAL REPRESENTATIONS

REPRESENTATION DECISION

NO-PARSING ANALYSIS

NO-NEW-RELATION ANALYSIS

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

ACCOUNT INDEPENDENCE CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

BRAND / INTRO / JOURNEY / ACTIVITY INDEPENDENCE CONTROL

STATE / EVIDENCE INDEPENDENCE CONTROL

SESSION SUBJECT VARIATION CONTROL

OPAQUE REF OBSERVATION

OTHER SUPERVISION FREEZE

HUNTNAME FREEZE

NAVIGATION FREEZE

CURRENT APP DOM / INTEGRATION EXECUTION

BROWSER VISUAL VALIDATION STATUS

NEGATIVE CONTROLS

CURRENT CUMULATIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c STATUS

L4 FRAMING STATUS

L4 SUPERVISION SUBJECT STATUS

L4 SUPERVISION SESSION RESULT

L4 REMAINING PRESSURES

L5 STATUS

RECURRING PRESENTATION PRESSURE

FALSIFICATION ANALYSIS

H34 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H34 DOES NOT PROVE

REMAINING PRESSURES
```

---

# 33. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H34
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

SESSION SUBJECT AUTHORITY
→ existing operational source
  / missing relation

ACCOUNT CLAIM
→ REMOVED AS UNSUPPORTED
  / supported
  / unresolved

VIEWER / AUTHENTICATION RELATION
→ NOT INTRODUCED / introduced-invalidly

APP CONSUMER BOUNDARY
→ preserved / violated

A/B SESSION REPRESENTATION
→ DOM-INTEGRATION VERIFIED
  / not established

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c
→ preserved / experimentally addressed H29–H30

L4 FRAMING
→ preserved / experimentally addressed H32

L4 SUPERVISION SUBJECT
→ preserved / experimentally addressed H33

L4 SUPERVISION SESSION
→ status

L5
→ preserved / experimentally addressed H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ observed / further qualified / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H35 automáticamente.

---

# 34. METHODOLOGICAL GUARDRAIL

Preservar:

```text
session subject reference
!=
account

session subject reference
!=
authenticated user

session subject reference
!=
viewer

session subject reference
!=
human identity

value equality
!=
identity equivalence

operational authority
!=
experiential presentation authority

diagnostic representation
!=
human-friendly presentation

removing unsupported wording
!=
proving the opposite proposition

existing source + overstated copy
!=
missing semantic relation

rendering a declared reference
!=
creating a new identity relation
```

El objetivo de H34 es averiguar **qué significa realmente `operationalSessionSubjectRef` dentro de la arquitectura existente** y hacer que Supervisión no afirme más de lo que esa relación acredita.
