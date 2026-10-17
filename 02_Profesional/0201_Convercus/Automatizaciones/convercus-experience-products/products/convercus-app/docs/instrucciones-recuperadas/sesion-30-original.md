# SESIÓN 30 — SCRIPT-BOUND SITUATED JOURNEY NARRATIVE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 29 — Operational Subject Status Provenance
```

No reconstruir decisiones anteriores.

Baseline consolidada:

```text
SESSION 29 → CLOSED

H29
→ SUPPORTED WITH QUALIFICATION

L3c SUBJECT STATUS
→ EXPERIMENTALLY ADDRESSED
→ STATE-ONLY
→ EXECUTION-VERIFIED within A/B

STATE / PRESENTATION AUTHORITY
→ SUPPORTED from existing subjectStates within tested scope

CAUSAL / VIEWER ATTRIBUTION
→ NOT INTRODUCED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c JOURNEY NARRATIVE
→ PRESERVED / OPEN

L4
→ PRESERVED / SOURCE-INSPECTION / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25
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

Artefactos en cuarentena:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

DemoScript.subjectPresentations
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

H28 account presentation transport/format
→ LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED

H29 state-to-status mapping
→ LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED
```

---

# 1. PRESSURE SELECTED

Seleccionar exclusivamente:

```text
GuestPerspective.message
```

dentro de la presión narrativa restante de L3c.

No seleccionar todavía L4.

No modificar:

```text
sessionLabel
subjects[].label
subjects[].status
supervision
Activity
App
```

excepto instrumentación estrictamente necesaria para observar H30.

---

# 2. WHY A NEW RELATION IS NOW PERMITTED

H26 ya falsificó explícitamente la condición:

```text
NO-NEW-RELATION
```

para la narrativa situada de GuestPerspective.

El diagnóstico consolidado fue:

```text
operational/derived inputs
→ AVAILABLE

situated present-state narrative source
→ ABSENT
```

y observó exactamente la relación ausente:

```text
current situated journey position
→ appropriate situated narrative content
```

H26 además rechazó como fuentes:

```text
member
presenterLabel parsing
activityPresentation
news
brand
context IDs
subject IDs
Evidence type
markerRef
generic copy substitution as complete solution
```

Por tanto S30 NO debe repetir una búsqueda general de fuente existente como si esta ausencia no hubiera sido ya demostrada.

S30 autoriza estudiar una relación presentacional mínima nueva.

Preservar:

```text
previous falsification
→ permits new experiment

previous falsification
!=
preselects architectural shape
```

La forma y host de la relación siguen sin estar decididos.

---

# 3. H30 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
una relación presentacional explícita
puede asociar una posición operacional
ya existente y legítimamente distinguible
del recorrido

con contenido narrativo situado
de GuestPerspective.message,

de forma que A y B puedan presentar
narrativas distintas
manteniendo la misma estructura operacional,

sin convertir la representación narrativa
en autoridad sobre runtime, Evidence,
subjectStates, evaluación, K o claim,

y sin introducir viewer,
account→subject,
session→subject,
identidad humana,
TES Progression
ni una nueva máquina de estados.
```

La relación estudiada es conceptualmente:

```text
existing runtime position
→ situated message presentation
```

NO:

```text
message
→ runtime state
```

NO:

```text
message
→ Evidence
```

NO:

```text
message
→ evaluation
```

NO:

```text
message
→ viewer identity
```

---

# 4. FIRST REQUIRED STEP — RUNTIME POSITION ANALYSIS

ANTES de modificar contratos o aplicación, construir una matriz de las seis observaciones:

```text
initial
enlist-p1
discover-clue-a
activate-p2
discover-clue-b
reset
```

para A y B.

Registrar, como mínimo:

```text
runtime checkpoint
availableActionId
GuestPerspective.state
P1 subjectState
P2 subjectState
Evidence count
P1 Evidence count
P2 Evidence count
evaluation sufficiency
claim status
current message
next presenterLabel
```

La pregunta es:

```text
¿qué relación EXISTENTE identifica
de forma mínima, estable y no semánticamente abusiva
la posición operacional desde la que
debe seleccionarse presentación narrativa?
```

Comparar expresamente como candidatos:

```text
checkpoint

availableActionId

GuestPerspective.state

subjectStates combination

Evidence/evaluation combination
```

y cualquier discriminante ya existente que la inspección encuentre material.

No inventar un selector antes de completar esta comparación.

---

# 5. SELECTOR REQUIREMENTS

El selector candidato debe cumplir:

```text
A and B
→ same operational position
→ same selector identity
```

y debe distinguir todos los momentos que requieran narrativa diferente.

Especialmente comprobar que:

```text
exploring before P2 enabled
!=
exploring after P2 enabled
```

puede distinguirse sin:

```text
scenario.id
demoId
brandRef
member.name
subject presentation label
location literal
Evidence ID
markerRef parsing
```

`GuestPerspective.state` por sí solo NO debe seleccionarse si colapsa dos posiciones narrativamente distintas.

No ampliar sus valores para hacer pasar H30.

---

# 6. CHECKPOINT GUARDRAIL

`checkpoint` es un candidato importante porque ya pertenece al runtime local y participa en disponibilidad/transición.

Pero NO asumir su selección.

Si se selecciona, demostrar previamente:

```text
checkpoint A == checkpoint B
```

en posiciones operacionalmente equivalentes y:

```text
distinct required narrative position
→ distinct checkpoint
```

dentro del recorrido probado.

Preservar estrictamente:

```text
checkpoint
!=
TES Progression
```

```text
checkpoint
!=
Experience semantic phase
```

```text
checkpoint sequence
!=
TES Sequence
```

```text
checkpoint transition
!=
TES Event
```

Usarlo como discriminante técnico local no autoriza ninguna promoción semántica.

Si checkpoint no cumple los requisitos:

```text
REJECT AS SELECTOR
```

y continuar el análisis con los candidatos existentes.

No modificar checkpoint para hacerlo adecuado al experimento.

---

# 7. AVAILABLE ACTION GUARDRAIL

`availableActionId` también debe analizarse porque actualmente distingue las affordances disponibles.

Pero:

```text
available action
!=
journey state
```

y:

```text
presenterLabel
!=
journey narrative
```

No utilizar `presenterLabel` como message.

No parsearlo.

No transformar sus nombres o lugares.

Si `availableActionId` se usa como discriminante, debe añadirse una relación presentacional explícita; la coincidencia con un Script step no autoriza reutilizar el copy de affordance.

Debe estudiarse además qué sucede cuando:

```text
availableActionId = none
```

tras el resultado final.

No introducir un sentinel artificial sólo para completar una tabla.

---

# 8. CANDIDATE HOST ANALYSIS

Después de seleccionar —si es posible— un discriminante operacional legítimo, comparar como host al menos:

```text
ScenarioDefinition
DemoScript
GuestPerspectiveReadModel
Fixture
```

Criterios:

### ScenarioDefinition

Ya contiene semántica operacional:

```text
subjects
contexts
checkpoints
actions
guards/transitions
```

Añadir copy situado puede mezclar presentación con definición operacional.

No descartarlo por convención; documentar la razón.

### DemoScript

Ya contiene presentación situada de la demo y transporta experimentalmente:

```text
presenterLabel
activityPresentation
subjectPresentations
```

Por ello es candidato plausible para contenido narrativo situado.

Pero preservar:

```text
recurrent host usage
!=
universal presentation architecture
```

y:

```text
DemoScript
!=
PresentationModel
```

### GuestPerspectiveReadModel

Es salida proyectada.

No convertir output en autoridad de su propia narrativa.

### Fixture

Contiene datos simulados y account presentation, pero no declara actualmente relación entre posición operacional y narrativa.

No usar proximidad de contenido como autoridad.

---

# 9. PROVISIONAL EXPERIMENTAL SHAPE

NO implementar esta forma hasta completar el análisis anterior.

Si:

```text
DemoScript
```

resulta host legítimo y:

```text
checkpoint
```

resulta discriminante suficiente, puede ensayarse una forma mínima equivalente a:

```text
journeyPresentations?: [
  {
    checkpoint: "...",
    message: "..."
  }
]
```

Los nombres definitivos deben reflejar estrictamente el alcance experimental.

Si otro discriminante existente resulta más preciso y semánticamente más limpio, utilizarlo y documentar la razón.

NO crear:

```text
JourneyEngine
NarrativeEngine
PerspectiveEngine
PresentationRegistry
ContentRegistry
PhaseRegistry
MessageResolver
```

o equivalentes.

No crear una nueva entidad `JourneyPhase` sólo para H30.

---

# 10. NARRATIVE CONTENT CONSTRAINT

Los messages H30 deben ser:

```text
situated
presentational
non-authoritative
non-perspectival
```

Deben permitir distinguir A/B, especialmente:

```text
A → jardín / fuente
B → mirador / patio
```

cuando corresponda.

Pero NO introducir:

```text
tú
tu
te
por ti
has habilitado
estás
eres
contigo
```

ni formulaciones equivalentes que identifiquen al viewer.

Tampoco inferir género personal.

El experimento debe demostrar narrativa situada SIN resolver todavía:

```text
viewer/account/session
→ represented subject
```

---

# 11. COPY CONTENT SHOULD NOT CLAIM MORE THAN ITS POSITION

El nuevo message puede describir o presentar:

```text
situated exploration availability
situated clue already recorded
next operational opportunity
completion presentation where legitimately bound
```

pero no debe convertirse en autoridad factual.

Ejemplos conceptuales admisibles:

```text
Exploración disponible en el jardín.

Pista del jardín registrada.
La siguiente acción está disponible.

Nueva exploración disponible en la fuente.
```

Para B:

```text
Exploración disponible en el mirador.

Pista del mirador registrada.
La siguiente acción está disponible.

Nueva exploración disponible en el patio.
```

Son ejemplos semánticos, NO copy obligatorio.

Evitar expresiones que atribuyan el hecho a una persona o al viewer.

---

# 12. COMPLETION AUTHORITY

Prestar especial atención al message final.

Actualmente:

```text
evaluation.sufficiency == established
```

constituye fuente legítima para afirmar que la condición está establecida.

No sustituir automáticamente esa autoridad por:

```text
checkpoint
availableAction absence
Script presentation
```

Si el message final puede mantenerse como representación neutral del resultado derivado existente:

```text
evaluation
→ completion representation
```

preservar esa relación.

La nueva relación situada H30 no debe degradar una autoridad ya legítima.

Esto puede conducir a una construcción mixta:

```text
operational/derived authority
+
situated presentation where required
```

sin convertir ninguno de los dos planos en autoridad del otro.

Documentarlo si ocurre.

---

# 13. INITIAL / READY AUTHORITY

Aplicar el mismo análisis al estado inicial.

Si los datos operacionales existentes bastan para una representación neutral del tipo:

```text
adventure available
enlistment pending
```

no trasladarla automáticamente al nuevo artefacto sólo por uniformidad.

Preservar:

```text
new relation
→ only where evidence demonstrated it is needed
```

No maximizar el nuevo artefacto.

---

# 14. A CONTROL

Ejecutar A completo.

La narrativa situada debe corresponder con la presentación A cuando la nueva relación resulte aplicable:

```text
jardín
fuente
```

sin modificar:

```text
account presentation
subject labels
subject status
subject refs
operationalSessionSubjectRef
Evidence
Activity
context
evaluation
K
claim
available actions
checkpoint transitions
```

---

# 15. B CONTROL

Ejecutar B completo.

En las posiciones equivalentes debe aparecer narrativa B:

```text
mirador
patio
```

sin residuos narrativos A dentro de:

```text
GuestPerspective.message
```

cuando la posición dependa de la nueva relación situada.

Mantener:

```text
same operational selector
+
different declared presentation
→
different situated message
```

---

# 16. REPRESENTATION INDEPENDENCE CONTROL

Crear variantes X/Y que mantengan:

```text
same Scenario
same checkpoint/runtime position
same subjectStates
same account
same subjectPresentations
same Evidence
same Activity
same context
same evaluation
same K
same claim
```

y cambien únicamente la nueva presentación narrativa.

Debe resultar:

```text
message X != message Y

facts X == facts Y
runtime position X == runtime position Y
subject states X == subject states Y
evaluation X == evaluation Y
Activity X == Activity Y
```

El copy no puede modificar la posición desde la que se selecciona.

---

# 17. CROSS-COMPOSITION SELECTOR CONTROL

A y B deben demostrar:

```text
same semantic/operational journey position
→ same selector
```

pero:

```text
A declared narrative != B declared narrative
```

Debe resultar:

```text
A message != B message
```

sin usar:

```text
scenario.id
script.id
demoId
brand identity
```

como selector de comportamiento.

La diferencia debe proceder de la presentación declarada, no de una rama A/B en el projector.

---

# 18. SUBJECT PRESENTATION INDEPENDENCE

Cambiar únicamente:

```text
DemoScript.subjectPresentations
```

manteniendo la nueva presentación narrativa fija.

Debe resultar:

```text
subjects[].label changes
message unchanged
```

No interpolar labels dentro de message durante H30.

Esto evita que la nueva narrativa cree accidentalmente una segunda dependencia sobre la representación humana del sujeto.

---

# 19. ACCOUNT INDEPENDENCE

Cambiar únicamente:

```text
member.name
```

Debe resultar:

```text
sessionLabel changes
message unchanged
```

La narrativa situada no puede inferirse de cuenta ni utilizar la coincidencia cuenta/subject presentation.

---

# 20. ACTIVITY PRESENTATION INDEPENDENCE

Cambiar exclusivamente:

```text
activityPresentation
```

cuando el harness lo permita sin cambiar la acción factual.

Debe resultar:

```text
Activity representation changes
GuestPerspective.message unchanged
```

Preservar:

```text
occurred Activity representation
!=
present journey narrative
```

---

# 21. STATUS INDEPENDENCE / AUTHORITY

No utilizar los strings producidos por H29 para construir message.

Puede utilizarse el estado operacional subyacente como discriminante sólo si el análisis de selector lo justifica.

Preservar:

```text
status presentation
!=
message authority
```

y:

```text
subjectStates
!=
situated narrative content
```

El resultado positivo H29 no debe convertirse indirectamente en una fuente narrativa que H26 ya demostró insuficiente.

---

# 22. ABSENCE CONTROL

Si para una posición que requiere narrativa situada no existe una declaración presentacional aplicable:

```text
do not invent situated narrative
```

No utilizar como fallback:

```text
A hardcode
presenterLabel
activityPresentation
member
subject label
markerRef
news
brand copy
```

Observar qué representación mínima segura puede producirse sin sobreafirmación.

Si no existe ninguna:

```text
message → ""
```

es admisible experimentalmente antes que inventar contenido.

Esto NO constituye todavía una política productiva de UX.

Documentar claramente:

```text
absence behavior
→ local experiment
→ not promoted
```

---

# 23. MISMATCH CONTROL

Introducir una presentación declarada para un selector inexistente o no actual.

Debe observarse:

```text
no runtime position created
no checkpoint created
no action made available
no Evidence created
no evaluation change
no message selected from unrelated position
```

La presentación no puede crear el estado al que dice pertenecer.

---

# 24. NO VIEWER CONTROL

Comprobar explícitamente que los nuevos messages seleccionados no requieren una relación:

```text
viewer → subject
```

H30 queda fuera de cualquier justificación de:

```text
Tú eres P1
La cuenta representa P1
La sesión operacional identifica al viewer
P1 == authenticated user
```

Aunque el contenido anterior utilizase segunda persona, preservar:

```text
historical copy
!=
semantic authority
```

---

# 25. FACT / PRESENTATION CONTRADICTION CONTROL

Cuando sea posible en harness, declarar deliberadamente una variante narrativa que no coincida con la presentación comercial A/B, manteniendo el runtime igual.

El objetivo NO es aceptar UX falsa.

El objetivo es demostrar:

```text
presentation text
cannot change factual truth
```

Debe resultar:

```text
message changes
facts unchanged
evaluation unchanged
K unchanged
claim unchanged
```

Registrar la contradicción como:

```text
representational inconsistency
```

NO como cambio de hechos.

No diseñar en H30 un validador editorial para impedirla.

---

# 26. FALSIFIERS

H30 queda FALSIFIED si:

```text
no existing runtime discriminant
can distinguish the required narrative positions
without creating a new phase/state model
```

o si:

```text
situated narrative
must be parsed from presenterLabel
or activityPresentation
```

o si:

```text
message presentation
changes runtime checkpoint/state
```

o:

```text
changes Evidence attribution
```

o:

```text
changes evaluation/K/claim
```

o si requiere:

```text
viewer→subject
account→subject
session→subject
```

para funcionar.

También falsifica H30 si debe promover:

```text
checkpoint → TES Progression
```

o introducir:

```text
JourneyPhase
NarrativeEngine
PresentationEngine
Registry
Actor
Operator
Participant
Representative
```

o equivalentes.

También:

```text
App modification required
to make the GuestPerspective relation work
→ STOP
```

No resolver L4 para salvar H30.

---

# 27. DO NOT REUSE H25/H27 BY ANALOGY

Aunque H25, H27 y eventualmente H30 puedan terminar alojando relaciones presentacionales en DemoScript:

```text
multiple experimental presentation relations
!=
universal Script presentation contract
```

Si H30 resulta positiva registrar únicamente:

```text
recurring architectural pressure observed
```

No promover.

No crear ADR.

No crear PSC-P02.

No modificar TES.

---

# 28. HISTORICAL REGRESSION AND LIVE REGRESSION

Preservar las reproducciones históricas H21–H29.

Pero distinguir expresamente:

```text
historical replay
!=
current cumulative behavior verification
```

Además de los replay históricos, H30 debe ejecutar controles vivos del código actual sobre:

```text
A
B
Retail negative control
Arrival negative control
```

y verificar que la implementación actual conserva los resultados acumulados H25–H29 salvo exclusivamente:

```text
GuestPerspective.message
```

donde H30 autorice cambios.

No afirmar validación visual de App si no se ejecuta navegador.

---

# 29. L4 FREEZE

App permanece fuera de alcance.

Preservar visibles sus literales conocidos:

```text
Mi aventura · Aurora Stay
Busca las pistas del jardín y de la fuente durante tu estancia.
```

y los textos situados de supervisión detectados en H26.

No corregirlos durante H30.

Esos residuos deben seguir constituyendo evidencia para L4.

---

# 30. OUTPUT

Producir:

```text
session-30-script-bound-situated-journey-narrative.md
```

con al menos:

```text
H29 CONSOLIDATED INPUT

H30 HYPOTHESIS

VARIABLE UNDER TEST

WHY A NEW RELATION IS NOW PERMITTED

H26 NARRATIVE ABSENCE CONSOLIDATION

PRE-DELTA RUNTIME POSITION MATRIX

SELECTOR CANDIDATE ANALYSIS

SELECTOR DECISION

CHECKPOINT / TES SEPARATION

CANDIDATE HOST ANALYSIS

EXPERIMENTAL REPRESENTATION SHAPE

REPRESENTATION AUTHORITY

THREADING PATH

BASELINE

CODE DELTA

A CONTROL

B CONTROL

CROSS-COMPOSITION SELECTOR CONTROL

REPRESENTATION INDEPENDENCE CONTROL

ACCOUNT INDEPENDENCE CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

STATUS INDEPENDENCE CONTROL

ACTIVITY PRESENTATION INDEPENDENCE CONTROL

ABSENCE CONTROL

MISMATCH CONTROL

NO-VIEWER CONTROL

FACT / PRESENTATION CONTRADICTION CONTROL

CURRENT-LIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c SUBJECT STATUS STATUS

L3c JOURNEY NARRATIVE RESULT

L3c OVERALL STATUS

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H30 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H30 DOES NOT PROVE

REMAINING PRESSURES
```

---

# 31. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H30
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

JOURNEY POSITION SELECTOR
→ selected existing discriminant
  / insufficient

L3c JOURNEY NARRATIVE
→ status

NARRATIVE / FACT AUTHORITY SEPARATION
→ supported / unsupported

VIEWER RELATION
→ NOT INTRODUCED / introduced-invalidly

CHECKPOINT / TES PROGRESSION SEPARATION
→ preserved / violated / not applicable

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c SUBJECT STATUS
→ preserved / experimentally addressed H29

L3c OVERALL
→ status

L4
→ preserved / source-inspection / open

L5
→ preserved / experimentally addressed H25

RECURRING PRESENTATION PRESSURE
→ observed / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H31 automáticamente.

---

# 32. METHODOLOGICAL GUARDRAIL

Preservar:

```text
knowing runtime position
!=
having situated narrative

having situated narrative
!=
creating runtime position

checkpoint
!=
TES Progression

available action
!=
journey state

presenterLabel
!=
journey message

Activity history
!=
present journey narrative

message presentation
!=
factual authority

same operational route
+
different situated composition
→
may legitimately produce different presentation

different presentation
→
must not produce different facts
```

El objetivo de S30 no es conseguir copy bonito.

El objetivo es determinar si la Factoría puede declarar explícitamente narrativa situada vinculada a una posición operacional ya existente sin convertir presentación en semántica, estado o autoridad factual.
