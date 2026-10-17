# SESIÓN 31 — APPLICATION COMPOSITION FRAMING PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 30 — Script-bound Situated Journey Narrative
```

No reconstruir decisiones anteriores.

## BASELINE CONSOLIDADA

```text
SESSION 30 → CLOSED

H30
→ SUPPORTED WITH QUALIFICATION

JOURNEY POSITION SELECTOR
→ existing availableActionId
→ EXECUTION-VERIFIED within Family Adventure A/B
→ NOT UNIVERSALIZED

checkpoint
→ REJECTED AS H30 SELECTOR
→ semantics unchanged

L3c JOURNEY NARRATIVE
→ EXPERIMENTALLY ADDRESSED
→ EXECUTION-VERIFIED within A/B

NARRATIVE / FACT AUTHORITY SEPARATION
→ SUPPORTED within tested scope

VIEWER RELATION
→ NOT INTRODUCED

L3c OVERALL
→ EXPERIMENTALLY ADDRESSED within A/B
→ NOT PROMOTED

L4
→ PRESERVED / SOURCE-INSPECTION / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING PRESENTATION PRESSURE
→ OBSERVED
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

Artefactos experimentales H25–H30 permanecen en cuarentena.

No promocionar DemoScript.

---

# 1. PRESSURE SELECTED

Seleccionar exclusivamente dentro de L4:

```text
APPLICATION COMPOSITION FRAMING
```

Los síntomas conocidos incluyen:

```text
"Mi aventura · Aurora Stay"

"Busca las pistas del jardín y de la fuente durante tu estancia."
```

o sus equivalentes actuales en App.

NO seleccionar todavía los residuos de Supervision:

```text
"P1 · Lucía"
"P2 · Huésped 2"
"Cuenta/sesión operativa"
```

Deben permanecer visibles.

Esta separación de L4 es diagnóstica, no contractual.

No crear L4a/L4b como taxonomía estable salvo necesidad posterior demostrada.

---

# 2. H31 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
las relaciones y artefactos ya existentes
pueden proporcionar a App
una presentación situada de framing
para la composición seleccionada,

de modo que A y B puedan mostrar
su framing correspondiente

sin hardcodes específicos de A en App,

sin crear una nueva relación semántica,
sin derivar framing desde GuestPerspective.message,
sin agregar o parsear presentation copy,
sin modificar runtime, Evidence, evaluación,
K o claim,

y manteniendo App como consumidor,
no como autoridad de composición.
```

H31 prueba inicialmente:

```text
EXISTING RELATIONS ONLY
```

No está autorizada todavía una nueva relación declarativa de framing.

---

# 3. VARIABLE UNDER TEST

Exclusivamente la procedencia de los elementos de App equivalentes a:

```text
application adventure title
application adventure introductory / framing text
```

Actualmente materializados mediante literales equivalentes a:

```text
Mi aventura · Aurora Stay
Busca las pistas del jardín y de la fuente durante tu estancia.
```

No modificar en H31:

```text
GuestPerspective.sessionLabel
GuestPerspective.subjects[].label
GuestPerspective.subjects[].status
GuestPerspective.message
Activity
SupervisionPerspective
Evidence
evaluation
runtime
```

No resolver otros literales App incidentalmente.

---

# 4. FIRST REQUIRED STEP — COMPLETE APP LITERAL INVENTORY

Antes de modificar código, inspeccionar App y producir un inventario de todo literal o composición de copy que pueda ser:

```text
generic application UI
composition-specific presentation
GuestPerspective rendering
Supervision rendering
Activity rendering
debug / diagnostic presentation
```

La inspección debe identificar al menos:

```text
source file / component
literal or expression
rendering surface
whether A-specific
existing source candidates
```

Pero H31 sólo seleccionará para experimento:

```text
application composition framing
```

El resto queda como evidencia L4.

No corregirlo.

---

# 5. FRAMING DECOMPOSITION

Descomponer semánticamente el framing actual.

Para el título, distinguir si contiene:

```text
generic shell label
+
property / brand / composition-specific label
```

Por ejemplo, no asumir que:

```text
"Mi aventura"
```

y:

```text
"Aurora Stay"
```

poseen la misma procedencia.

Para el texto introductorio distinguir:

```text
generic Experience framing
+
composition-specific situated content
```

Por ejemplo:

```text
jardín
fuente
```

puede ser contenido situado aunque:

```text
Busca las pistas...
```

sea framing genérico.

Esta descomposición es diagnóstica.

No convertirla automáticamente en campos o contratos.

---

# 6. EXISTING SOURCE INSPECTION

Inspeccionar todos los candidatos existentes relevantes, incluidos cuando existan:

```text
resolved demo / manifest metadata
Experience definition
Scenario
DemoScript metadata
Fixture
brand / property data
snapshot/read models
resolved runtime
composition artifacts
```

Para cada componente de framing preguntar:

```text
¿existe una relación DECLARADA
que autorice exactamente
esta presentación?
```

Preservar:

```text
having Aurora Stay somewhere
!=
having application-title authority

having jardín/fuente somewhere
!=
having adventure-summary authority

having situated messages
!=
having composition framing

having Activity presentations
!=
having static itinerary summary
```

---

# 7. FORBIDDEN SOURCE REUSE

NO construir framing mediante:

```text
parsing presenterLabel
parsing activityPresentation
aggregating experimentalJourneyPresentations
extracting place names from message
extracting labels from Activity
parsing markerRef
parsing IDs
scenario.id branching
demoId branching
brand.id branching
subject labels
Evidence payload parsing
news copy reuse
```

salvo que la inspección demuestre una relación ya declarada cuya semántica sea exactamente la requerida.

Coexistencia de texto no equivale a autoridad.

Especialmente:

```text
H30 journey narrative
!=
application static framing
```

y:

```text
H25 Activity presentation
!=
Experience itinerary description
```

---

# 8. TITLE SOURCE ANALYSIS

Analizar de forma independiente:

```text
generic title component
composition-specific title component
```

Si existe actualmente una fuente legítima, documentar:

```text
source
→ threading
→ App consumer
```

Si, por ejemplo, existe un nombre explícito de propiedad/composición, verificar qué semántica declara realmente antes de usarlo.

No asumir:

```text
brand == property
member == property
context ID == display name
scenario identity == title
```

Si sólo existe el dato pero no la relación:

```text
STOP for that component
```

---

# 9. INTRODUCTORY FRAMING SOURCE ANALYSIS

Investigar separadamente el texto equivalente a:

```text
Busca las pistas del jardín y de la fuente durante tu estancia.
```

Preguntar si existe una fuente legítima para:

```text
Experience-level situated framing
```

No inferirla de la suma de las posiciones H30.

Preservar:

```text
three position-specific messages
!=
declared itinerary summary
```

También:

```text
two Activity presentations
!=
declared Experience description
```

y:

```text
two clue locations
!=
authority to state
"Busca las pistas X e Y..."
```

Si no existe una relación declarada:

```text
STOP
→ record missing relationship
→ do not create it in S31
```

---

# 10. ALL-OR-STOP APPLICATION DELTA RULE

H31 debe completar primero la inspección de:

```text
title
+
introductory framing
```

ANTES de modificar App.

Si cualquiera de los componentes necesarios para eliminar el framing específico de A carece de fuente legítima:

```text
H31 NO-NEW-RELATION
→ INSUFFICIENT
→ STOP
```

En ese caso:

```text
NO partial App correction
NO new framing field
NO fallback to A
NO aggregation from H25/H30
```

Conservar App intacta para mantener visible la presión.

Registrar por separado las fuentes legítimas que sí se hayan encontrado.

No reparar sólo el título si el framing seleccionado sigue dependiendo de una relación ausente.

---

# 11. IF EXISTING SOURCES ARE SUFFICIENT

Sólo si title + introductory framing tienen fuentes legítimas existentes, está autorizado un delta mínimo.

La dirección debe ser:

```text
existing authoritative composition source
→ existing/minimal transport
→ App presentation
```

App no puede importar directamente artefactos concretos A/B para resolver copy.

No:

```text
App
→ artifacts.ts
```

No:

```text
App
→ costa-artifacts.ts
```

No branching:

```text
if demo === A ...
if scenario.id === ...
```

App debe seguir siendo consumidor.

---

# 12. TRANSPORT VS RELATION

Distinguir explícitamente:

```text
missing transport
!=
missing semantic/presentational relation
```

Puede existir una fuente legítima cuyo dato todavía no alcance App.

Si la relación ya está declarada pero falta transporte, documentarlo.

Un transporte mínimo local puede ensayarse únicamente si:

```text
source semantics already authorize the output
```

Clasificar ese transporte como:

```text
EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
```

No crear arquitectura general para transportar dos strings.

Si transportar el dato requiere inventar primero qué significa:

```text
STOP
```

---

# 13. A CONTROL

Si H31 supera la condición no-new-relation:

A debe presentar framing A desde las fuentes identificadas.

Verificar que no depende de hardcodes App equivalentes a:

```text
Aurora Stay
jardín
fuente
```

excepto si alguno de esos textos forma parte legítima de un artefacto presentado a App desde la composición.

Mantener intactos:

```text
account presentation H28
subject presentation H27
subject status H29
journey narrative H30
Activity H25
Evidence
evaluation
K
claim
```

---

# 14. B CONTROL

B debe presentar framing correspondiente a sus fuentes existentes.

NO prescribir de antemano el literal B.

Códex debe registrar exactamente:

```text
declared source
→ observed B framing
```

No inventar:

```text
Costa Clara
mirador
patio
```

en una capa nueva simplemente porque esos valores ya sean conocidos en otros artefactos.

Si las fuentes existentes no pueden producir framing B legítimamente:

```text
H31 FALSIFIED / INSUFFICIENT
```

No hardcodear B.

---

# 15. COMPOSITION SWITCH CONTROL

Si el harness actual permite instanciar A/B con la misma App:

```text
same application code
+
different resolved composition
→
different framing where declared
```

Debe demostrarse sin cambiar:

```text
App source
projection behavior
runtime rules
```

La diferencia debe proceder exclusivamente de fuentes de composición legítimas.

Si App no dispone actualmente de una frontera mediante la cual recibir esa información, distinguir:

```text
missing transport boundary
```

de:

```text
missing semantic relation
```

No fusionar ambos problemas.

---

# 16. READ-MODEL PRESERVATION

H31 NO debe mover hacia App autoridad que actualmente pertenece al read model.

Preservar:

```text
sessionLabel
→ H28 authority

subject labels
→ H27 authority

subject status
→ H29 authority

journey message
→ H30 mixed authority

Activity representation
→ H25 authority
```

App sólo renderiza esos outputs.

No reconstruirlos localmente.

---

# 17. RECURRING SCRIPT PRESENTATION PRESSURE

S30 consolidó:

```text
H25 → Script-bound Activity presentation
H27 → Script-bound subject presentation
H30 → Script-bound situated journey narrative
```

H31 debe observar esta recurrencia pero NO utilizarla como permiso para:

```text
put framing in DemoScript
```

sin evidencia.

Preservar:

```text
recurring host
!=
authority for new presentation relation
```

H31 puede aportar nueva evidencia a esa presión.

No debe resolverla arquitectónicamente.

---

# 18. SUPERVISION FREEZE

Conservar intactos en esta sesión los outputs/literales equivalentes a:

```text
P1 · Lucía
P2 · Huésped 2
Cuenta/sesión operativa
```

No usar H27 subjectPresentations automáticamente para corregirlos.

Preservar:

```text
GuestPerspective subject representation
!=
SupervisionPerspective representation
```

hasta que se estudie su autoridad.

---

# 19. NEGATIVE CONTROLS

Retail y Arrival deben permanecer sin cambios.

H31 no debe obligarles a adoptar:

```text
Family Adventure framing
DemoScript situated framing
journey presentations
```

Si el transporte nuevo provoca requerimientos artificiales en verticales no relacionadas:

```text
STOP
```

No crear defaults semánticos para hacer pasar controles negativos.

---

# 20. APP EXECUTION REQUIREMENT

A diferencia de H25–H30, L4 pertenece explícitamente a App.

Por tanto, si existe delta de aplicación en H31, no basta con probar projector/provider.

Debe verificarse la aplicación actual.

Usar la capacidad de render/integration test disponible en el repositorio.

Si existe navegador o infraestructura equivalente disponible, ejecutar A y B a través de App.

Si sólo existe jsdom/integration rendering:

```text
record as DOM/integration verification
```

y NO llamarlo validación visual.

Registrar claramente:

```text
browser visual validation
→ executed / not executed
```

No inferirla.

Si H31 termina por STOP antes de modificar App, la inspección de fuente basta para el veredicto no-new-relation.

---

# 21. HISTORICAL VS CURRENT TESTS

Preservar:

```text
historical replay
!=
current cumulative behavior verification
```

Los harness H21–H30 pueden continuar verificando sus baselines históricas.

Pero cualquier afirmación sobre App actual debe proceder de:

```text
current source inspection
+
current live/integration execution
```

no de projectors históricos archivados.

---

# 22. FALSIFIERS

H31 queda FALSIFIED para la condición NO-NEW-RELATION si:

```text
App composition title
requires a presentation relationship
that does not exist
```

o si:

```text
introductory framing
requires a presentation relationship
that does not exist
```

o si sólo puede construirse mediante:

```text
parsing
aggregation
ID branching
copy reuse
hardcodes A/B
```

o si requiere convertir:

```text
H30 messages
→ Experience summary
```

o:

```text
H25 Activity
→ itinerary definition
```

o si App debe convertirse en autoridad para decidir qué significa la composición.

También STOP si eliminar los hardcodes exige simultáneamente resolver:

```text
SupervisionPerspective
viewer identity
account→subject
```

Esas son presiones distintas.

---

# 23. POSSIBLE POSITIVE VERDICT

Sólo si las relaciones existentes bastan:

```text
H31
→ SUPPORTED WITH QUALIFICATION
```

y:

```text
L4 APPLICATION COMPOSITION FRAMING
→ EXISTING-SOURCE / EXECUTION-VERIFIED
```

con los límites concretos encontrados.

---

# 24. POSSIBLE FALSIFICATION VERDICT

Si falta una relación legítima:

```text
H31
→ FALSIFIED

NO-NEW-RELATION
→ INSUFFICIENT
```

Registrar exactamente:

```text
which framing component lacks authority
what data exists
what relationship is missing
why existing presentation artifacts cannot substitute it
```

No crear el artefacto nuevo en S31.

Una sesión posterior podrá autorizar un experimento mínimo.

---

# 25. OUTPUT

Producir:

```text
session-31-application-composition-framing-provenance.md
```

con al menos:

```text
H30 CONSOLIDATED INPUT

H31 HYPOTHESIS

VARIABLE UNDER TEST

WHY L4 IS DIAGNOSTICALLY SPLIT

CURRENT APP LITERAL INVENTORY

FRAMING DECOMPOSITION

EXISTING SOURCE INVENTORY

TITLE SOURCE ANALYSIS

INTRODUCTORY FRAMING SOURCE ANALYSIS

DATA / RELATION DISTINCTION

TRANSPORT / RELATION DISTINCTION

NO-NEW-RELATION ANALYSIS

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

COMPOSITION SWITCH CONTROL

READ-MODEL PRESERVATION

NEGATIVE CONTROLS

CURRENT APP EXECUTION

BROWSER / DOM VERIFICATION STATUS

SUPERVISION FREEZE

RECURRING PRESENTATION PRESSURE

FALSIFICATION ANALYSIS

H31 VERDICT

L4 FRAMING RESULT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H31 DOES NOT PROVE

REMAINING PRESSURES
```

---

# 26. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H31
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

APP TITLE AUTHORITY
→ status

APP INTRODUCTORY FRAMING AUTHORITY
→ status

APP CONSUMER BOUNDARY
→ preserved / violated / unresolved

A/B COMPOSITION FRAMING
→ execution-verified / not established

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c
→ preserved / experimentally addressed H29–H30

L4 APPLICATION FRAMING
→ status

L4 SUPERVISION
→ preserved / open

L5
→ preserved / experimentally addressed H25

RECURRING PRESENTATION PRESSURE
→ observed / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H32 automáticamente.

---

# 27. METHODOLOGICAL GUARDRAIL

Preservar:

```text
having a value
!=
having framing authority

having situated journey copy
!=
having Experience summary

having Activity location copy
!=
having itinerary definition

App rendering
!=
App semantic authority

missing transport
!=
missing relationship

same App
+
different legitimate composition source
→
may produce different framing

different hardcoded App copy
→
is not composition

recurrence
!=
promotion
```

S31 debe responder primero:

```text
¿la Factoría ya sabe legítimamente
qué debe presentar App
como framing de esta composición?
```

antes de responder:

```text
¿cómo hacemos que App lo muestre?
```

Si la primera respuesta es negativa:

```text
STOP
```

No diseñar el artefacto que falta dentro de la baseline falsificada.
