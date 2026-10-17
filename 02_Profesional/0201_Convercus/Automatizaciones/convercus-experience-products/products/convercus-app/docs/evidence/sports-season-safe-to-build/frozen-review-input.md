# Convercus Demo Factory — SAFE-TO-BUILD REVIEW

## Purpose

S39 está cerrada.

No abras automáticamente H40.

No selecciones una presión histórica simplemente porque S39 haya terminado.

Entramos ahora en una fase diferente de Convercus Demo Factory:

```text
narrative
→ situated demo definition
→ SAFE-TO-BUILD review
→ build if safe
→ human interaction
→ observed pressure
→ bounded experiment if necessary
```

La especificación situada que sigue constituye el input congelado de este análisis.

Tu tarea **NO es implementar todavía la demo completa**.

Tu tarea es determinar si la Demo Factory existente puede comenzar de forma metodológicamente segura la construcción de su primer slice y, si no puede, identificar exactamente el bloqueo material que lo impide.

---

# 1. GOVERNING PRINCIPLE

Aplicar:

```text
SAFE TO BUILD
!=
EVERYTHING SOLVED
```

y:

```text
OPEN PRESSURE
!=
BLOCKING PRESSURE
```

Una cuestión pendiente sólo puede impedir la construcción si compromete materialmente alguna garantía necesaria para el recorrido que realmente queremos ejecutar.

No utilizar desconocidos, capacidades todavía no generalizadas o futuras necesidades posibles como argumento automático para ampliar arquitectura.

Preferir siempre:

```text
reuse demonstrated capability
→ build minimum situated slice
→ observe actual pressure
```

frente a:

```text
anticipate general problem
→ design abstraction
→ implement infrastructure
```

---

# 2. FROZEN HISTORICAL STATE

Preservar todos los veredictos y estados históricos S01–S39.

En particular:

```text
S39
→ CLOSED / STOP PRE-DELTA

P39
→ FALSIFIED / NOT REPRODUCED

H39
→ SUPPORTED WITH QUALIFICATION

NO-NEW-NAVIGATION-RELATION
→ LOCALLY SUFFICIENT
→ NOT PROMOTED

H21 / H36
→ HISTORICALLY FALSIFIED / PRESERVED

H37
→ SUPPORTED WITH QUALIFICATION
→ CURRENT CUMULATIVE VERIFICATION

S38 evidence-integrity rule
→ LOCAL / EXPERIMENTAL / NOT PROMOTED

Costa B
→ EXPERIMENTAL COMPOSITION
→ NOT COMMERCIAL DEMO ACCEPTANCE
```

No reescribir baselines, tests, reports, traces o verdicts históricos.

---

# 3. SITUATED DEMO DEFINITION v0.1

Esta definición es:

```text
SITUATED
EXPERIMENTAL
LOCAL
NOT A GENERAL DEMO PROTOCOL
NOT PROMOTED
```

No generalizarla a todas las futuras demos.

---

# 4. BUSINESS CONTEXT

Crear posteriormente una demo para una **cadena ficticia de distribución de moda y equipamiento deportivo**.

La empresa:

```text
ya dispone de club de fidelización
+
organiza eventos deportivos
```

La oportunidad consiste en vincular:

```text
fidelización
participación deportiva
captación
reconocimiento
activación comercial
```

---

# 5. DEMO AUDIENCE

Un único interlocutor inicial.

Debe resultar:

```text
comprensible para Marketing
+
operacionalmente creíble para CRM / Loyalty
```

No crear todavía experiencias separadas de demostración para Marketing y CRM.

---

# 6. COMMERCIAL THESIS

La demo debe hacer visible que los eventos deportivos pueden constituir:

```text
una superficie de fidelización
+
una superficie de captación
+
una fuente de contexto para activación comercial relevante
```

Especialmente:

```text
participante externo
→ oportunidad de captación
```

y para miembros existentes:

```text
participación continuada
→ reconocimiento
→ contexto para renovación / categoría superior / beneficio relevante
```

No inferir intención de compra automáticamente desde la participación.

---

# 7. SEASON AND EVENTS

La demo representa una:

```text
TEMPORADA DEPORTIVA
```

que contiene varios eventos.

Debe distinguir:

```text
season
!=
event
```

Tres disciplinas serán visibles inicialmente:

```text
Carrera
Vela
Vóley playa
```

Sólo una debe ejecutarse extremo a extremo en el primer slice:

```text
Carrera
```

No implementar todavía lógica transversal entre deportes.

---

# 8. PARTICIPANT TYPES

Deben distinguirse al menos:

```text
existing club member
external participant
```

No asumir:

```text
participant
=
customer
=
club member
```

Un participante externo puede inscribirse y participar.

Su participación constituye una oportunidad de alta/captación.

No convertirlo automáticamente en miembro.

---

# 9. REGISTRATION

La inscripción debe formar parte del recorrido visible.

El participante elige:

```text
event
+
participation modality
```

En el primer slice, la modalidad la elige el participante.

No desarrollar todavía un motor genérico de modalidades.

---

# 10. SITUATED PARTICIPATION MODALITY

Una persona no posee una identidad permanente:

```text
casual
social
competitor
```

La misma persona puede comportarse de forma diferente según evento y contexto.

Mantener:

```text
person
!=
permanent participation modality
```

Las orientaciones pueden incluir:

```text
competition
social
wellness
casual
```

La relación exacta entre:

```text
modality
motivation
event
discipline
Experience
```

permanece OPEN.

No resolverla preventivamente.

---

# 11. EXPERIENCE RELATION

Pueden existir varias Experiences Convercus.

Pero esta especificación NO autoriza todavía:

```text
1 modality = 1 Experience
```

ni ninguna cardinalidad general.

La primera construcción debe reutilizar las capacidades existentes y revelar si la relación realmente necesita una nueva representación.

---

# 12. EVIDENCE — FIRST SLICE

Mantener explícitamente separadas tres clases de hecho:

```text
presence
effort
competitive result
```

## Presence

Para v0.1 queda fijado:

```text
SIMULATED QR / CHECK-IN
→ presence Evidence
```

No constituye integración real de QR.

No crear infraestructura general de check-in.

## Effort

Para participación no competitiva:

```text
suave
medio
intenso
```

Puede ser autodeclarado por el participante.

Mantener:

```text
presence
!=
effort
```

## Competitive result

El participante puede introducir:

```text
result
+
position
```

En v0.1 se acepta esa entrada sin validación externa.

No implementar todavía:

```text
organizer verification
federation verification
wearable verification
external sports API
```

---

# 13. RECOGNITION

Distinguir:

```text
badge
trophy
benefit
```

El primer recorrido utilizará principalmente:

```text
BADGE
```

Debe resultar visible:

```text
what was obtained
why it was obtained
what changes afterwards
```

No reducirlo a un contador silencioso.

Trofeos pueden estar presentes conceptualmente para competición pero no necesitan gobernar el primer slice.

---

# 14. COMMERCIAL BENEFITS

El modelo narrativo admite beneficios como:

```text
acceso anticipado a colecciones
sesiones de mejora
encuentros con figuras públicas
cupones asociados a nivel
```

No es necesario implementar todos.

Para la primera demo puede utilizarse una única consecuencia comercial situada.

Candidato:

```text
participación recurrente en running
→ acceso anticipado a colección performance running
```

Mantener:

```text
recognition
!=
commercial benefit
```

---

# 15. ACCUMULATION

La lógica pretendida es dual:

```text
first participation
→ immediate recognition
```

y:

```text
second participation
→ booster / meaningful continuity
→ possible entry or advancement in an Experience journey
```

Puede utilizarse un estado inicial donde ya exista una participación previa.

No inventar TES Progression, Completion o Result si la autoridad semántica existente no lo permite.

Si expresar el “booster” exige semántica no autorizada, clasificarlo y determinar si bloquea realmente el primer slice.

---

# 16. TEAM EVENTS

Vóley playa hace visible que existen deportes colectivos.

Para v0.1:

```text
team
→ organizational mechanism for participants
```

Los reconocimientos siguen siendo individuales.

No inferir:

```text
sports team
=
TES Group
```

No implementar todavía:

```text
collective result
collective recognition
team-owned reward
collective claim
```

La presión existe, pero no debería bloquear el recorrido inicial de Carrera salvo evidencia contraria.

---

# 17. RANKING

No implementar leaderboard.

Para competición basta:

```text
personal result
+
personal position
+
individual recognition
```

---

# 18. PRIMARY EXECUTABLE PATH

El primer slice debe estudiar la posibilidad de construir:

```text
SPORT SEASON
↓
Carrera event
↓
registration
↓
participant chooses modality
↓
participation
↓
appropriate Evidence
↓
badge
↓
visible consequence
```

El recorrido preferido para el primer slice es:

```text
EXTERNAL PARTICIPANT
↓
CARRERA EVENT
↓
SOCIAL / WELLNESS PARTICIPATION
↓
SIMULATED QR CHECK-IN
↓
SELF-REPORTED EFFORT
↓
BADGE
↓
CAPTURE / CLUB JOIN OPPORTUNITY
```

Razón:

permite ensayar directamente la tesis comercial prioritaria de captación sin exigir todavía ranking, validación competitiva o semántica colectiva.

---

# 19. SECONDARY CONTRAST

Debe comprobarse que el diseño no impida posteriormente:

```text
EXISTING CLUB MEMBER
↓
Carrera
↓
competition
↓
result + position
↓
individual recognition
↓
commercial activation / continuity
```

Pero no es obligatorio implementar ambos recorridos en el primer slice.

El segundo sirve inicialmente como contraste de diseño.

---

# 20. PERSPECTIVE CHANGE

La demo futura debe permitir:

```text
PARTICIPANT VIEW
↓
PERSPECTIVE CHANGE
↓
MARKETING / CRM VIEW
```

La vista Marketing/CRM debería poder comprender, como mínimo:

```text
person
membership status
season
event
discipline
selected modality
participation
Evidence
recognition
relevant continuity
capture / activation opportunity
```

No convertir inferencias comerciales en hechos observados.

---

# 21. DEMO-AUTHOR UX

Objetivo futuro:

el creador debería poder variar sin programar, progresivamente:

```text
brand
season
disciplines
events
dates
modalities
participants
member/external status
Experience references
participation criteria
Evidence
badges
trophies
benefits
copy
images
narrative path
```

No asumir que Demo Factory ya permite hacerlo.

En este SAFE-TO-BUILD review debes descubrir:

```text
what is already configurable
what is structurally reusable
what requires new situated data
what requires product code
what requires duplicated code
what relation is actually missing
```

No corregir esas fricciones todavía.

Clasificarlas.

---

# 22. PARTICIPANT UX

La futura demo debe permitir observar, no resolver preventivamente:

```text
¿entiende la temporada?
¿entiende el evento?
¿entiende las modalidades?
¿entiende qué debe hacer?
¿entiende qué Evidence está aportando?
¿entiende que el check-in acredita presencia?
¿entiende qué significa el esfuerzo declarado?
¿entiende por qué recibe la insignia?
¿entiende qué cambia después?
¿entiende la relación con el club?
¿entiende la oportunidad de alta?
¿percibe continuidad?
```

No diseñar una UX “perfecta” preventivamente.

Necesitamos una UX suficientemente coherente para que pueda ser desafiada por una persona.

---

# 23. REQUIRED SAFE-TO-BUILD GUARANTEES

Para el primer slice, evaluar explícitamente si el estado actual puede conservar:

```text
composition identity
state integrity
participant != automatic customer/member
modality != permanent person classification
presence != effort != competitive result
Evidence provenance
recognition != commercial benefit
individual attribution
no unsupported collective semantics
historical evidence integrity
experimental capability != promoted product capability
```

Sólo una amenaza material a estas garantías puede constituir BLOCKER.

---

# 24. REQUIRED REVIEW

Construye una matriz de capacidades contra la Demo Definition.

Para cada necesidad relevante clasifica exclusivamente como:

```text
AVAILABLE / DEMONSTRATED
AVAILABLE WITH QUALIFICATION
REUSABLE WITH SITUATED CONFIGURATION
MISSING BUT NON-BLOCKING
MATERIAL BLOCKER
UNKNOWN — INSUFFICIENT EVIDENCE
```

Para cada fila indicar:

1. necesidad de la demo;
2. evidencia existente;
3. autoridad / origen;
4. capacidad actual;
5. gap exacto;
6. si requiere cambio;
7. si bloquea realmente el first slice;
8. por qué.

No convertir:

```text
MISSING
```

automáticamente en:

```text
BLOCKER
```

---

# 25. TRACE THE FIRST SLICE THROUGH THE EXISTING SYSTEM

Reconstruye, sin modificar todavía el producto, cómo podría fluir el primer slice usando las capacidades actuales.

Como mínimo:

```text
composition / manifest
→ Scenario
→ Demo Script if applicable
→ participant representation
→ registration
→ simulated QR / presence Evidence
→ effort input
→ public action
→ runtime
→ evaluation where applicable
→ state / read model
→ badge / visible consequence
→ capture opportunity
→ Marketing/CRM perspective
```

Para cada transición indicar:

```text
already exists
can be represented with existing capability
requires situated configuration
missing but can be deferred
materially blocked
```

No rellenar huecos por analogía.

---

# 26. CHECK AGAINST HISTORICAL PRESSURES

Revisar las presiones abiertas heredadas S01–S39 únicamente contra este first slice.

Ejemplos:

```text
viewer/actor
account
second person
PSC-P01
team / collective semantics
navigation
browser validation
historical replay maintenance
diagnostic terminology
K duplication
```

Para cada una preguntar:

```text
Does this pressure invalidate the first slice?
```

Si no:

```text
NOT BLOCKING FOR THIS DEMO SLICE
```

No abrir experimento.

---

# 27. STRICT STOP CONDITIONS

STOP el SAFE-TO-BUILD review si descubres un MATERIAL BLOCKER.

Un blocker debe cumplir las dos condiciones:

```text
the required first-slice behavior cannot be represented responsibly
AND
working around it would falsify, blur or violate an existing semantic / architectural guarantee
```

No basta:

```text
the ideal architecture does not exist
```

ni:

```text
this might be useful later
```

ni:

```text
the current model is not general
```

---

# 28. IF A MATERIAL BLOCKER EXISTS

No implementarlo.

No diseñar varios arreglos.

No seleccionar otra presión adicional.

Identificar exactamente:

```text
BLOCKER
→ violated required behavior
→ existing evidence
→ conflicting guarantee
→ smallest falsifiable question
```

Sólo ese blocker podrá convertirse después, con autorización, en una hipótesis experimental acotada.

No abrirla automáticamente como H40.

---

# 29. IF NO MATERIAL BLOCKER EXISTS

Declarar:

```text
FIRST DEMO SLICE
→ SAFE TO BUILD WITH QUALIFICATIONS
```

No significa:

```text
commercially ready
production ready
UX accepted
architecture complete
general demo protocol proven
```

A continuación definir, pero NO implementar todavía, el **smallest buildable slice**.

Debe especificar:

```text
files / artifacts likely involved
existing capabilities reused
new situated configuration required
minimum UI surfaces
minimum data
minimum actions
minimum Evidence
minimum state changes
expected observable result
explicit exclusions
UX questions that must remain observable
```

El objetivo será que la instrucción posterior pueda ordenar una construcción pequeña y reversible.

---

# 30. NO PRODUCT DELTA IN THIS REVIEW

Esta instrucción es de inspección y readiness.

No modificar todavía:

```text
App
bootstrap
providers
adapters
contracts
manifests
fixtures
Scenario
DemoScript
ExperienceDefinitions
Evidence model
evaluators
TES
PSC
navigation
CSS
assets
historical harnesses
```

salvo artefactos exclusivamente documentales/evidenciales necesarios para el informe si el entorno de trabajo lo requiere.

No implementar la demo durante este review.

---

# 31. REQUIRED FINAL VERDICT

Finalizar con exactamente una de estas dos conclusiones:

```text
A.
FIRST DEMO SLICE
→ SAFE TO BUILD WITH QUALIFICATIONS
```

o:

```text
B.
FIRST DEMO SLICE
→ STOP
→ MATERIAL BLOCKER IDENTIFIED
```

Si A:

no seleccionar H40.

Preparar únicamente la especificación del smallest buildable slice.

Si B:

no arreglarlo.

Preparar únicamente la evidencia que demuestra que ese blocker merece un experimento posterior.

---

# 32. FINAL PURPOSE

El propósito de esta revisión no es demostrar que Demo Factory está terminada.

Es responder una pregunta mucho más pequeña:

```text
Can we responsibly start building
the first situated Sports Season demo slice
with what has already been demonstrated?
```

El objetivo del proyecto a partir de aquí es llegar cuanto antes, de forma segura, a:

```text
BUILD
→ HUMAN USE
→ UX CHALLENGE
→ OBSERVATION
→ FALSIFICATION
→ REFINEMENT
```

No regresar a hardening preventivo salvo que la propia demo demuestre que es necesario.