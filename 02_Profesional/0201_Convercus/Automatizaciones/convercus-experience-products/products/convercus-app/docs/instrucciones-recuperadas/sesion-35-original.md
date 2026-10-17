# SESIÓN 35 — EXPERIENCE-SOURCED GUEST EXPERIENCE NAME PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 34 — Operational Session Subject Representation Provenance
```

No reconstruir decisiones anteriores.

---

# 1. BASELINE CONSOLIDADA

```text
SESSION 34 → CLOSED

H34
→ SUPPORTED WITH QUALIFICATION

NO-NEW-RELATION
→ SUFFICIENT

SESSION SUBJECT AUTHORITY
→ EXISTING OPERATIONAL SOURCE

ACCOUNT CLAIM
→ REMOVED AS UNSUPPORTED

VIEWER / AUTHENTICATION RELATION
→ NOT INTRODUCED

APP CONSUMER BOUNDARY
→ PRESERVED

A/B SESSION REPRESENTATION
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
→ PRESERVED / EXPERIMENTALLY ADDRESSED H33

L4 SUPERVISION SESSION
→ PRESERVED / EXPERIMENTALLY ADDRESSED H34

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ OBSERVED / FURTHER QUALIFIED / NOT PROMOTED
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

No promover artefactos H25–H34.

---

# 2. PRESSURE SELECTED

Seleccionar exclusivamente:

```text
GuestPerspective.huntName
```

y su representación actual como h1 en HomePage.

Síntoma actual:

```text
GuestPerspective.huntName
→ hardcoded "Aventura Familiar"
```

mientras existe:

```text
ExperienceDefinition.name
→ "Aventura Familiar"
```

La igualdad actual de strings NO constituye procedencia.

H35 debe determinar si:

```text
ExperienceDefinition.name
```

posee autoridad semántica suficiente para proporcionar el nombre presentado de la Experience dentro de GuestPerspective.

---

# 3. DO NOT SELECT

No modificar:

```text
brand / eyebrow H32
introductory framing H32
sessionLabel H28
subject labels H27
subject status H29
journey message H30
Activity H25
Supervision H33/H34
fixed navigation link
generic App navigation labels
document title
```

No seleccionar todavía la navegación fija a A.

---

# 4. H35 — HYPOTHESIS

Hipótesis falsable:

```text
La ExperienceDefinition ya existente
contiene una relación semántica de nombre
suficiente para proporcionar
GuestPerspective.huntName,

de modo que el nombre presentado
pueda proceder de Experience.name

sin hardcode local,
sin una nueva relación editorial,
sin utilizar DemoScript,
sin inferir desde Scenario,
brand o manifest identity,

y sin modificar runtime state,
Evidence,
evaluation,
K o claim.
```

Condición:

```text
NO-NEW-RELATION
```

La relación candidata es:

```text
Experience
→ declared semantic name
→ GuestPerspective experience-name presentation
```

NO:

```text
DemoScript
→ huntName
```

NO:

```text
brand
→ huntName
```

NO:

```text
Scenario
→ huntName
```

NO:

```text
composition intro
→ huntName
```

---

# 5. FIRST REQUIRED STEP — NAME SEMANTICS INSPECTION

Antes del delta, inspeccionar:

```text
ExperienceDefinition contract
ExperienceDefinition.name usages
resolveDemo()
ResolvedDemoRuntime
projectSnapshot()
projectGuestPerspective()
GuestPerspectiveReadModel.huntName
App HomePage h1 consumer
```

Buscar todos los usos actuales de:

```text
experience.name
huntName
```

y documentar:

```text
declaring layer
producer
consumers
current semantic role
current transport path
whether the two concepts are already related
```

No asumir que un campo denominado `name` es automáticamente el nombre que GuestPerspective debe mostrar.

---

# 6. SEMANTIC QUESTIONS

Responder expresamente:

```text
A. Experience.name identifies
   the Experience as a semantic artifact?

B. Is it intended as a human-readable name?

C. Is it stable across Scenario/compositions
   sharing the Experience?

D. Does huntName mean
   the presented name of that Experience?

E. Does huntName instead mean
   a composition-specific title,
   journey title,
   campaign title,
   or another responsibility?
```

Para cada pregunta:

```text
SUPPORTED
NOT SUPPORTED
NOT DETERMINED
```

H35 sólo puede conectar ambos campos si la semántica inspeccionada sostiene la correspondencia.

---

# 7. STRING EQUALITY IS NOT EVIDENCE

Preservar:

```text
Experience.name == "Aventura Familiar"

GuestPerspective.huntName == "Aventura Familiar"
```

actualmente.

Pero:

```text
same string
!=
same semantic authority
```

El experimento NO puede justificarse únicamente por esa coincidencia.

Debe demostrarse:

```text
name semantics
→ compatible with huntName responsibility
```

---

# 8. CANDIDATE SOURCE ANALYSIS

Comparar al menos:

```text
ExperienceDefinition.name
DemoScript
Scenario
BrandArtifact.name
Manifest/demoId
current projector literal
```

### ExperienceDefinition.name

Candidato principal.

Analizar si representa el nombre de la Experience compartida.

### DemoScript

Ya aloja varias presentaciones situadas.

Pero H35 NO debe usar recurrencia como permiso.

Si `huntName` es el nombre de la Experience, Script sería una autoridad más débil o incorrecta.

### Scenario

No utilizar Scenario sólo porque A/B lo transporten.

Scenario describe situación/operación, no necesariamente nombre de Experience.

### BrandArtifact.name

Ya tiene autoridad de branding H32.

Preservar:

```text
brand name
!=
Experience name
```

### Manifest/demoId

Identifican/configuran composición.

No parsear ni utilizar IDs como nombre.

### Projector literal

Es el síntoma histórico.

No constituye fuente.

---

# 9. TRANSPORT / RELATION DISTINCTION

Si la inspección concluye:

```text
Experience.name
has the required semantic authority
```

pero no llega actualmente al projector, clasificar:

```text
relationship semantics → existing

transport → missing
```

Un transporte mínimo puede ensayarse.

Si, en cambio:

```text
Experience.name
does not authorize huntName
```

entonces:

```text
NO-NEW-RELATION
→ INSUFFICIENT
→ STOP
```

No crear una relación nueva en H35.

---

# 10. MINIMAL TRANSPORT REQUIREMENT

Si la relación es suficiente, transportar únicamente lo necesario.

Preferir:

```text
Experience.name
→ existing runtime/projectSnapshot path
→ projectGuestPerspective
→ huntName
```

sin pasar objetos completos si sólo se necesita el nombre.

Pero no forzar un escalar si la arquitectura existente ya transporta Experience legítimamente hasta la frontera apropiada.

Documentar la elección.

Preservar:

```text
minimal transport
!=
new semantic relation
```

---

# 11. APP CONSUMER BOUNDARY

App debe continuar:

```text
GuestPerspective.huntName
→ h1
```

No cambiar App para leer directamente:

```text
runtime.experience.name
```

si eso evita la procedencia del read model.

H35 investiga la fuente de:

```text
GuestPerspective.huntName
```

No sustituye esa responsabilidad por un acceso paralelo desde App.

Preservar:

```text
App
→ consumer of GuestPerspective
```

para esta superficie.

---

# 12. A CONTROL

A utiliza:

```text
experience:family-adventure@1
```

y debe presentar exactamente el nombre declarado por esa Experience si la hipótesis se sostiene.

Verificar:

```text
h1
→ GuestPerspective.huntName
→ Experience.name
```

y preservar:

```text
brand
intro
message
subjects
status
Activity
Supervision
facts
evaluation
```

---

# 13. B CONTROL

B comparte la misma Experience.

Por tanto, si:

```text
A.experienceRef == B.experienceRef
```

debe resultar:

```text
huntName A == huntName B
```

aunque difieran:

```text
brand
Scenario
Fixture
DemoScript
subject presentations
journey narrative
intro framing
Activity presentation
context
```

Esto es un control central.

Preservar:

```text
same Experience
→ same Experience name
```

si ésa es realmente la responsabilidad demostrada.

---

# 14. EXPERIENCE NAME VARIATION CONTROL

Crear una variante exclusivamente de harness donde cambie:

```text
Experience.name
```

manteniendo:

```text
Experience.id
Scenario
DemoScript
Fixture
brand
runtime actions
evaluation
```

idénticos cuando sea técnicamente posible.

Debe resultar:

```text
GuestPerspective.huntName changes

facts unchanged
runtime unchanged
evaluation unchanged
Activity unchanged
intro unchanged
brand unchanged
```

Este control debe demostrar que:

```text
huntName depends on Experience.name
```

y no en el string histórico hardcoded.

---

# 15. EXPERIENCE ID INDEPENDENCE

Cuando sea técnicamente seguro en harness, comprobar que renombrar exclusivamente la identidad técnica de Experience manteniendo su `name` y las referencias coherentes no altera la presentación.

No hacerlo si exige una modificación extensa de la composición que introduzca ruido.

Si se ejecuta:

```text
Experience.id X/Y
same Experience.name
→ same huntName
```

El objetivo es preservar:

```text
Experience identity
!=
presented name
```

No parsear IDs.

---

# 16. BRAND INDEPENDENCE

Cambiar exclusivamente:

```text
BrandArtifact.name
```

Debe cambiar las superficies H32 de branding y conservar:

```text
huntName
```

Preservar:

```text
Brand name
!=
Experience name
```

---

# 17. SCRIPT PRESENTATION INDEPENDENCE

Perturbar por separado:

```text
subjectPresentations
experimentalJourneyPresentations
experimentalIntroductoryFraming
activityPresentation
presenterLabel
```

Ninguna debe cambiar:

```text
huntName
```

si Experience.name resulta la autoridad.

Este control es especialmente importante para la presión Script-bound.

---

# 18. SCENARIO INDEPENDENCE

Usar A/B como control principal:

```text
different Scenario
same Experience
→ same huntName
```

No crear un Scenario artificial sólo para demostrarlo salvo necesidad.

Preservar:

```text
Scenario situated behavior
!=
Experience naming authority
```

---

# 19. ACCOUNT / SUBJECT / STATE INDEPENDENCE

Perturbar o recorrer legítimamente:

```text
member.name
subjectPresentations
subjectStates
Evidence
```

Debe conservarse:

```text
huntName
```

El nombre de la Experience no depende del sujeto, cuenta o estado actual.

---

# 20. NO DEMOSCRIPT FALLBACK

Si `Experience.name` no está disponible o no es semánticamente suficiente:

```text
do not fallback to DemoScript
```

en H35.

No crear:

```text
experimentalHuntName
presentation.title
experienceTitle
```

dentro de Script.

Eso sería una nueva relación y requeriría una sesión posterior.

---

# 21. ABSENCE OBSERVATION

Si técnicamente puede ensayarse una Experience con nombre vacío/ausente sin violar el contrato, observar el comportamiento.

Pero NO debilitar el tipo o contrato sólo para crear el control.

Si `name` es obligatorio:

```text
document contract requirement
```

y no inventar ausencia.

No crear fallback al literal:

```text
"Aventura Familiar"
```

para preservar la apariencia.

---

# 22. NEGATIVE CONTROLS

Retail y Arrival deben conservar comportamiento actual.

Analizar si poseen ExperienceDefinition.name y si ésta llega a superficies distintas.

No hacer obligatorio:

```text
GuestPerspective
```

para verticales que no lo tienen.

No introducir huntName o Family Adventure UI en otros recorridos.

---

# 23. CURRENT APP EXECUTION

Si H35 modifica runtime/projector:

Ejecutar App actual para:

```text
A
B
Retail
Arrival
```

En A/B comprobar:

```text
h1
eyebrow
intro
message
subjects
status
Supervision
Activity
```

y preservar todos salvo `huntName` cuando una variante de Experience.name lo modifique.

Registrar:

```text
DOM/integration → EXECUTED / NOT EXECUTED

browser visual validation
→ EXECUTED / NOT EXECUTED
```

No equipararlos.

---

# 24. CURRENT CUMULATIVE REGRESSION

Preservar sobre código actual:

```text
H25 Activity
H27 subject labels
H28 account
H29 status
H30 message
H32 brand + intro
H33 supervision subject IDs
H34 supervision session representation
```

La única nueva dependencia autorizada:

```text
Experience.name
→ GuestPerspective.huntName
```

si H35 la sostiene.

---

# 25. RECURRING PRESENTATION PRESSURE

H35 debe registrar qué aporta el resultado a la presión emergente.

Si Experience.name resulta suficiente, tenemos evidencia de una tercera clase:

```text
semantic definition metadata
→ semantic presentation
```

junto a:

```text
operational/diagnostic authority
→ derived representation

composition-specific editorial content
→ explicit declaration
```

Registrar como:

```text
PRESENTATION AUTHORITY STRATIFICATION
→ EVIDENCE STRENGTHENED
→ NOT PROMOTED
```

No crear ADR.

No crear PresentationBoundary.

No crear PresentationModel.

No convertir esta observación en regla universal.

---

# 26. FALSIFIERS

H35 queda FALSIFIED bajo NO-NEW-RELATION si:

```text
Experience.name
does not semantically authorize huntName
```

o si GuestPerspective.huntName representa algo distinto que exige una relación nueva,

o si la conexión requiere:

```text
DemoScript
Scenario-specific copy
BrandArtifact
manifest/demoId parsing
App branching
```

o si cambiar Experience.name altera indebidamente:

```text
runtime state
Evidence
evaluation
K
claim
```

o si App debe abandonar GuestPerspective como fuente del h1.

Ante falsador:

```text
STOP
→ preserve hardcode/source evidence
→ document missing relationship
→ do not create experimental huntName relation
```

---

# 27. HISTORICAL VS CURRENT VERIFICATION

Preservar:

```text
historical replay
!=
current cumulative verification
```

Adaptar únicamente la instrumentación histórica necesaria para conservar verdictos H21–H34.

El nuevo harness H35 debe ejecutar fuentes actuales.

No usar replay para afirmar comportamiento vigente.

---

# 28. OUTPUT

Producir:

```text
session-35-experience-sourced-guest-experience-name-provenance.md
```

con al menos:

```text
H34 CONSOLIDATED INPUT

H35 HYPOTHESIS

VARIABLE UNDER TEST

WHY NO NEW RELATION IS AUTHORIZED

EXPERIENCE NAME SOURCE INSPECTION

HUNTNAME SEMANTIC ANALYSIS

SEMANTIC SUPPORT MATRIX

CANDIDATE SOURCE ANALYSIS

STRING EQUALITY / AUTHORITY DISTINCTION

TRANSPORT / RELATION DISTINCTION

SOURCE DECISION

THREADING PATH

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

SHARED EXPERIENCE CONTROL

EXPERIENCE NAME VARIATION CONTROL

EXPERIENCE ID INDEPENDENCE CONTROL

BRAND INDEPENDENCE CONTROL

SCRIPT PRESENTATION INDEPENDENCE CONTROL

SCENARIO INDEPENDENCE CONTROL

ACCOUNT / SUBJECT / STATE INDEPENDENCE

ABSENCE OBSERVATION

NEGATIVE CONTROLS

CURRENT APP DOM / INTEGRATION EXECUTION

BROWSER VISUAL VALIDATION STATUS

CURRENT CUMULATIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c STATUS

L4 FRAMING STATUS

L4 SUPERVISION SUBJECT STATUS

L4 SUPERVISION SESSION STATUS

L4 HUNTNAME RESULT

L5 STATUS

PRESENTATION AUTHORITY STRATIFICATION

FALSIFICATION ANALYSIS

H35 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H35 DOES NOT PROVE

REMAINING PRESSURES
```

---

# 29. FINAL VERDICT FORMAT

Concluir únicamente con:

```text
H35
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

HUNTNAME AUTHORITY
→ Experience.name
  / missing relation
  / other existing source

EXPERIENCE / HUNTNAME SEMANTIC CORRESPONDENCE
→ supported / unsupported / unresolved

APP CONSUMER BOUNDARY
→ preserved / violated

A/B HUNTNAME
→ CURRENT APP DOM-INTEGRATION VERIFIED
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
→ preserved / experimentally addressed H34

L4 HUNTNAME
→ status

L5
→ preserved / experimentally addressed H25

PRESENTATION AUTHORITY STRATIFICATION
→ evidence strengthened / unsupported
→ NOT PROMOTED

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H36 automáticamente.

---

# 30. METHODOLOGICAL GUARDRAIL

Preservar:

```text
same text
!=
same authority

semantic name
!=
brand name

semantic name
!=
composition-specific title

Experience
!=
Scenario

Experience
!=
DemoScript

stable Experience identity
+
different situated compositions
→
may legitimately share semantic name

semantic metadata presentation
!=
editorial situated presentation

operational derivation
!=
semantic metadata derivation

existing semantic authority
+
missing transport
!=
missing relation

recurring Script presentation
!=
universal presentation ownership
```

El objetivo de H35 es determinar si el hardcode `huntName` está ocultando una autoridad semántica ya existente o si la coincidencia con `Experience.name` es sólo accidental.

No diseñar una nueva relación si las fuentes actuales no sostienen esa correspondencia.
