# SESIÓN 33 — OPERATIONAL SUPERVISION SUBJECT REPRESENTATION PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 32 — Explicit Composition Introductory Framing
```

No reconstruir decisiones anteriores.

# 1. BASELINE CONSOLIDADA

```text
SESSION 32 → CLOSED

H32
→ SUPPORTED WITH QUALIFICATION

INTRODUCTORY FRAMING RELATION
→ EXPLICIT / EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

HOST
→ DemoScript / experimental

APP BRAND AUTHORITY
→ existing resolved BrandArtifact
→ CURRENT APP DOM-INTEGRATION EXECUTION-VERIFIED

BRAND / INTRO AUTHORITY SEPARATION
→ SUPPORTED within A/B

APP CONSUMER BOUNDARY
→ PRESERVED

A/B COMPOSITION FRAMING
→ CURRENT APP DOM-INTEGRATION EXECUTION-VERIFIED

VIEWER RELATION
→ NOT INTRODUCED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 INTRODUCTORY FRAMING
→ EXPERIMENTALLY ADDRESSED within A/B / NOT PROMOTED

L4 TITLE / BRAND
→ EXISTING-SOURCE / LOCAL TRANSPORT / DOM-INTEGRATION VERIFIED

L4 SUPERVISION
→ PRESERVED / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ STRENGTHENED / NOT PROMOTED
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

No promover ningún artefacto H25–H32.

---

# 2. PRESSURE SELECTED

Seleccionar exclusivamente dentro de L4 / Supervision:

```text
Supervision subject presentation
```

El síntoma conocido en App es equivalente a:

```text
subject.id === "subject-p1"
  ? "P1 · Lucía"
  : "P2 · Huésped 2"
```

Esta expresión mezcla potencialmente:

```text
operational subject identification
+
local P1/P2 alias
+
human situated presentation
+
A-specific copy
```

H33 debe averiguar qué parte está autorizada por las fuentes operacionales existentes.

NO seleccionar todavía:

```text
"Cuenta/sesión operativa"
huntName
fixed navigation link to A
supervision criterion labels
other diagnostic copy
```

No corregirlos incidentalmente.

---

# 3. H33 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de SupervisionPerspective,
las referencias y propiedades operacionales
ya existentes de los sujetos
pueden proporcionar una representación
diagnóstica neutral suficiente

sin reutilizar subjectPresentations H27,
sin introducir nombres humanos,
sin crear una nueva relación presentacional,
sin inferir P1/P2 mediante parsing,
y sin modificar sujetos, sesión operacional,
Evidence, estados, evaluación, K o claim.
```

La relación ensayada es:

```text
existing operational subject representation
→ neutral supervision display
```

NO:

```text
subjectRef
→ human identity
```

NO:

```text
GuestPerspective subject label
→ Supervision subject label
```

NO:

```text
account
→ supervised subject
```

Condición:

```text
NO-NEW-RELATION
```

---

# 4. WHY NO NEW RELATION IS AUTHORIZED YET

S31/S32 demostraron una relación ausente para framing y posteriormente autorizaron H32.

Supervisión se encuentra en una situación distinta.

Actualmente sabemos que `SupervisionPerspective` ya transporta información operacional sobre sujetos, incluyendo al menos los identificadores usados por App para aplicar el branch A-specific.

Por tanto primero debe probarse:

```text
existing operational authority
→ sufficient neutral diagnostic representation?
```

antes de autorizar:

```text
new supervision presentation relation
```

Preservar:

```text
existing human-looking hardcode
!=
evidence that human presentation is required
```

y:

```text
less narrative display
may be more epistemically correct
```

---

# 5. VARIABLE UNDER TEST

Exclusivamente el encabezado/label de cada sujeto dentro de la superficie Supervision.

No modificar los datos diagnósticos asociados:

```text
subject id
exists
operational state
Evidence count
```

ni otros campos actualmente renderizados.

No modificar:

```text
GuestPerspective subjects[].label
GuestPerspective subjects[].status
sessionLabel
message
Activity
introductory framing
branding
```

---

# 6. FIRST REQUIRED STEP — SOURCE INSPECTION

Antes del delta, inspeccionar exactamente:

```text
SupervisionPerspective contract
projectSupervisionPerspective()
Scenario subject definition
subjectStates
operationalSessionSubjectRef
Evidence attribution
App SystemPage consumer
```

Construir una matriz por sujeto:

```text
source field
semantic responsibility
current rendered representation
whether current copy adds information
whether added information is authorized
```

Documentar expresamente qué conoce `SupervisionPerspective` de:

```text
subject reference
subject existence
operational state
Evidence attribution/count
session reference
```

y qué NO conoce legítimamente de:

```text
human name
account ownership
viewer identity
GuestPerspective presentation
```

---

# 7. CURRENT COPY DECOMPOSITION

Analizar por separado:

```text
P1
Lucía

P2
Huésped 2
```

No asumir que ninguna parte está legitimada.

Preguntar:

```text
"P1"
→ explicit declared value?
→ abbreviation?
→ parsing/transformation of subject-p1?
→ local UI alias?

"Lucía"
→ what declared supervision source authorizes this?

"Huésped 2"
→ what declared supervision source authorizes this?
```

Si P1/P2 sólo pueden obtenerse mediante parsing o branch local:

```text
not legitimate operational authority
```

para H33.

---

# 8. H27 GUARDRAIL

H27 demostró:

```text
DemoScript.subjectPresentations
→ GuestPerspective.subjects[].label
```

dentro de A/B.

H27 NO demostró:

```text
subjectPresentations
→ universal subject display
```

ni:

```text
GuestPerspective display
→ SupervisionPerspective display
```

Por tanto H33 NO debe reutilizar:

```text
Lucía
Huésped 2
Inés
Mateo
Participante Alfa
```

desde H27.

Preservar:

```text
same subjectRef
across two read models
!=
same presentation authority
```

---

# 9. OPERATIONAL IDENTIFIER CANDIDATE

Analizar si el identificador/ref operacional ya transportado puede representarse directamente en Supervisión.

Por ejemplo, si la fuente declara:

```text
subject.id = "subject-p1"
```

puede ensayarse su representación literal como identificador diagnóstico.

NO exigir este output de antemano.

Códex debe determinar primero qué campo representa realmente la identidad/referencia operacional.

Si se utiliza:

```text
render exact declared identifier
```

NO:

```text
parse identifier
→ P1
```

NO:

```text
map identifier
→ Lucía
```

Preservar:

```text
displaying an identifier
!=
declaring human identity
```

---

# 10. ROLE / TYPE CANDIDATES

Si Scenario o SupervisionPerspective contienen explícitamente:

```text
role
type
```

analizar su semántica real antes de utilizarlos.

No convertir automáticamente:

```text
role
→ human label
```

ni:

```text
type
→ display name
```

Si no llegan actualmente a SupervisionPerspective, distinguir:

```text
missing transport
```

de:

```text
missing presentation relationship
```

pero no añadir transporte salvo que sea imprescindible y la semántica del campo autorice exactamente el output seleccionado.

Preferir la fuente mínima ya presente en SP.

---

# 11. NEUTRALITY REQUIREMENT

La representación resultante debe ser:

```text
operational
diagnostic
neutral
non-human
non-perspectival
```

No debe afirmar:

```text
Lucía
Inés
Mateo
Huésped 2
Tú
Tu sujeto
Tu cuenta
Titular
Participante
Operador
Representante
```

salvo que una relación existente inspeccionada autorice literalmente alguno de esos significados.

No introducir género.

---

# 12. A CONTROL

Sobre A, ejecutar la App actual y navegar a Supervisión.

Debe observarse una representación neutral procedente de la fuente seleccionada.

No prescribir:

```text
P1 / P2
```

si esos valores no están declarados.

Debe conservarse:

```text
exists
operationalState
Evidence count
sessionSubjectRef
evaluation
K
claim
```

según sus fuentes actuales.

---

# 13. B CONTROL

Sobre B, ejecutar la misma App actual.

La representación supervisora de los mismos sujetos operacionales debe proceder de la misma regla/fuente.

No debe aparecer por dependencia H33:

```text
Lucía
Huésped 2
```

ni tampoco introducir automáticamente:

```text
Inés
Mateo
```

El objetivo NO es sustituir nombres A por nombres B.

El objetivo es:

```text
remove unsupported human presentation
while preserving operational identification
```

---

# 14. CROSS-COMPOSITION CONTROL

Si A/B utilizan las mismas referencias operacionales:

```text
same operational subject reference
→ same supervision representation
```

aunque difieran:

```text
account
subjectPresentations
brand
introductory framing
journey narrative
Activity presentation
context
```

Esto es deliberado.

Supervisión puede legítimamente ser menos situada que GuestPerspective.

Preservar:

```text
same operational structure
→ same diagnostic representation
```

si la fuente lo justifica.

---

# 15. SUBJECT PRESENTATION INDEPENDENCE CONTROL

Perturbar únicamente:

```text
DemoScript.subjectPresentations
```

Debe resultar:

```text
GuestPerspective subject labels change

Supervision subject representation
→ unchanged
```

Esto es un control central.

Demuestra:

```text
GuestPerspective presentation authority
!=
Supervision operational authority
```

---

# 16. ACCOUNT INDEPENDENCE CONTROL

Perturbar:

```text
member.name
```

Debe cambiar únicamente las superficies cuya autoridad deriva legítimamente de member/branding correspondiente.

La representación del sujeto en Supervisión debe permanecer igual.

Preservar:

```text
account presentation
!=
supervision subject identification
```

---

# 17. BRAND / INTRO / JOURNEY INDEPENDENCE

Perturbar independientemente:

```text
brand.name
experimentalIntroductoryFraming
experimentalJourneyPresentations
activityPresentation
```

La representación supervisora del sujeto debe permanecer idéntica.

Esto debe evitar que la recurrencia presentacional de Script se filtre accidentalmente en Supervisión.

---

# 18. STATE INDEPENDENCE OF IDENTIFIER

Cambiar legítimamente:

```text
subject operational state
```

sin cambiar la referencia del sujeto.

Debe resultar:

```text
supervision operationalState changes

supervision subject identifier/presentation
→ unchanged
```

La identificación del sujeto no puede depender de su estado actual.

---

# 19. EVIDENCE INDEPENDENCE OF IDENTIFIER

Añadir Evidence mediante el recorrido legítimo.

Debe resultar:

```text
Evidence count changes

supervision subject identifier/presentation
→ unchanged
```

Preservar:

```text
Evidence attribution
!=
subject presentation
```

---

# 20. ORDER CONTROL

Si técnicamente puede realizarse en harness sin cambiar semántica, alterar el orden de la colección de sujetos manteniendo sus referencias.

La presentación debe permanecer asociada al sujeto correcto.

No utilizar:

```text
array index
```

como autoridad equivalente a P1/P2.

Preservar:

```text
first subject
!=
P1
```

salvo contrato explícito.

Si el orden forma parte de una relación autoritativa existente, documentarlo antes de usarlo.

---

# 21. UNKNOWN / ADDITIONAL SUBJECT OBSERVATION

Sólo mediante control aislado de projector/read model, si es seguro y no exige ampliar Scenario productivo, observar qué ocurre con una referencia de sujeto distinta de los dos IDs conocidos.

El objetivo es comprobar que App no aplica:

```text
if p1
  P1/Lucía
else
  P2/Huésped 2
```

a cualquier referencia desconocida.

No crear P3 como concepto de producto.

Si el experimento requiere cambiar semántica del Scenario:

```text
DO NOT RUN
```

y documentar que el control no es aplicable.

---

# 22. NO PARSING CONTROL

La implementación no puede utilizar:

```text
split
replace
regex
substring
suffix extraction
```

sobre subjectRef para producir P1/P2 u otro alias humano.

Si la representación neutral seleccionada es el identificador:

```text
render identifier as declared
```

La apariencia técnica no constituye falsificación.

H33 estudia autoridad, no estética.

---

# 23. "CUENTA/SESIÓN OPERATIVA" FREEZE

Conservar exactamente la superficie equivalente a:

```text
Cuenta/sesión operativa
```

durante H33.

Aunque sea semánticamente sospechosa.

No corregirla junto con subject labels.

Ese texto mezcla potencialmente:

```text
account
session
operationalSessionSubjectRef
```

y constituye otra presión.

Mantenerla visible.

---

# 24. OTHER SUPERVISION FREEZE

No modificar:

```text
Evaluación compartida
Criterio K
Evidence recibida
Admisibilidad conjunta
Suficiencia K
Afirmación derivada
Evidence y atribución
```

salvo instrumentación de test.

H33 no reevalúa la terminología de esas superficies.

---

# 25. APP CONSUMER BOUNDARY

La dirección debe continuar:

```text
SupervisionPerspective
→ App
→ render
```

No:

```text
App
→ Scenario lookup
```

No:

```text
App
→ DemoScript lookup
```

para resolver labels de Supervisión.

Especialmente NO:

```text
App
→ subjectPresentations
```

App no debe reconstruir relaciones que el read model no declara.

Si la fuente legítima ya forma parte de SupervisionPerspective, consumirla directamente.

---

# 26. NO-NEW-RELATION CONDITION

H33 queda SUPPORTED sólo si una fuente operacional ya existente resulta suficiente para una representación supervisora neutral.

Si para conservar una representación humana o amigable hace falta:

```text
subjectRef
→ supervision display label
```

como relación declarada nueva:

```text
STOP
```

Registrar:

```text
operational identification available
human supervision presentation missing
```

No introducir esa relación en S33.

Una sesión posterior podrá decidir si realmente se necesita.

---

# 27. CURRENT APP EXECUTION REQUIRED

Si H33 modifica App, ejecutar obligatoriamente la aplicación vigente con:

```text
A
B
```

y navegar a Supervisión.

Verificar DOM/integration del resultado.

También comprobar las páginas relevantes para asegurar que:

```text
GuestPerspective
Activity
framing
```

no han cambiado.

Registrar:

```text
DOM/integration
→ EXECUTED / NOT EXECUTED

browser visual validation
→ EXECUTED / NOT EXECUTED
```

No equipararlos.

---

# 28. NEGATIVE CONTROLS

Retail y Arrival deben permanecer intactos.

No deben recibir estructuras o labels de Supervision Family Adventure por hacer genérico el cambio.

Si no poseen la rama Supervision:

```text
absence remains absence
```

No crear defaults.

---

# 29. CURRENT CUMULATIVE REGRESSION

Sobre código actual preservar:

```text
H25 Activity
H27 GuestPerspective subject labels
H28 account presentation
H29 status
H30 journey message
H32 brand + introductory framing
```

La única diferencia autorizada debe estar en:

```text
Supervision subject heading/presentation
```

No utilizar exclusivamente replay histórico para acreditar App vigente.

---

# 30. RECURRING PRESENTATION PRESSURE — OBSERVATION ONLY

H33 debe registrar qué aporta su resultado a:

```text
RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
```

Especialmente distinguir:

```text
situated experiential/editorial presentation
```

de:

```text
operational diagnostic representation
```

Si H33 puede resolverse desde autoridad operacional existente, registrar:

```text
counter-evidence against
"all presentation belongs in Script"
```

sin convertirlo todavía en principio arquitectónico.

No crear ADR.

No promover DemoScript.

No crear PresentationBoundary.

---

# 31. FALSIFIERS

H33 queda FALSIFIED bajo NO-NEW-RELATION si:

```text
Supervision cannot identify its subjects
adequately from existing operational fields
```

sin introducir una nueva relación,

o si eliminar los hardcodes requiere:

```text
H27 subjectPresentations
member.name
DemoScript presentation
ID parsing
array position
A/B branching
```

o si el cambio modifica:

```text
subjectRef
operational state
Evidence attribution
operationalSessionSubjectRef
evaluation
K
claim
```

o si obliga a resolver simultáneamente:

```text
Cuenta/sesión operativa
viewer
account→subject
```

Ante falsador:

```text
STOP
→ document missing relation
→ preserve hardcode if necessary
→ do not create next abstraction
```

---

# 32. OUTPUT

Producir:

```text
session-33-operational-supervision-subject-representation-provenance.md
```

con al menos:

```text
H32 CONSOLIDATED INPUT

H33 HYPOTHESIS

VARIABLE UNDER TEST

WHY NO NEW RELATION IS AUTHORIZED YET

SUPERVISION SOURCE INSPECTION

CURRENT COPY DECOMPOSITION

OPERATIONAL SUBJECT AUTHORITY

H27 / SUPERVISION SEPARATION

CANDIDATE EXISTING REPRESENTATIONS

NO-PARSING ANALYSIS

NO-NEW-RELATION ANALYSIS

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

CROSS-COMPOSITION CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

ACCOUNT INDEPENDENCE CONTROL

BRAND / INTRO / JOURNEY INDEPENDENCE CONTROL

STATE INDEPENDENCE CONTROL

EVIDENCE INDEPENDENCE CONTROL

ORDER CONTROL

UNKNOWN SUBJECT OBSERVATION

CUENTA/SESIÓN OPERATIVA FREEZE

OTHER SUPERVISION FREEZE

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

L4 SUPERVISION SUBJECT RESULT

L4 REMAINING SUPERVISION PRESSURE

L5 STATUS

RECURRING PRESENTATION PRESSURE

FALSIFICATION ANALYSIS

H33 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H33 DOES NOT PROVE

REMAINING PRESSURES
```

---

# 33. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H33
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

SUPERVISION SUBJECT AUTHORITY
→ existing operational source
  / missing relation

HUMAN SUBJECT PRESENTATION
→ NOT REQUIRED
  / MISSING
  / introduced-invalidly

GP / SP PRESENTATION SEPARATION
→ supported / unsupported

APP CONSUMER BOUNDARY
→ preserved / violated

A/B SUPERVISION SUBJECT REPRESENTATION
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
→ status

L4 SUPERVISION SESSION
→ preserved / open

L5
→ preserved / experimentally addressed H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ observed / qualified by H33 / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H34 automáticamente.

---

# 34. METHODOLOGICAL GUARDRAIL

Preservar:

```text
operational identification
!=
human identity

operational identification
!=
situated human presentation

GuestPerspective
!=
SupervisionPerspective

same subjectRef
!=
same presentation authority

human-readable
!=
more epistemically correct

diagnostic surface
!=
experiential surface

subject array position
!=
subject identity

subjectRef syntax
!=
declared alias

rendering an existing identifier
!=
creating a new identity relation

reducing unsupported copy
!=
losing demonstrated semantics

Script presentation recurrence
!=
universal presentation ownership
```

El objetivo de H33 no es hacer Supervisión más agradable.

El objetivo es determinar **qué sabe legítimamente Supervisión sobre el sujeto que está mostrando** y reducir su representación exactamente a ese nivel si las fuentes existentes son suficientes.
