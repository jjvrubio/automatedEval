# Convercus Demo Factory — BUILD 01  
## Primer corte situado: Sports Season / Carrera / Captación

## 0. Propósito

Ha concluido el `SAFE-TO-BUILD review`.

El veredicto aceptado es:

```text
FIRST DEMO CUT
→ SAFE TO BUILD WITH QUALIFICATIONS
```

Esta instrucción autoriza por primera vez la construcción del **primer corte real de la nueva demo deportiva**.

No abre automáticamente H40.

No inicia una nueva campaña de hardening arquitectónico.

No pretende construir toda la narrativa de Sports Season.

El objetivo es implementar el menor corte reversible que permita llegar a:

```text
BUILD
→ HUMAN USE
→ UX CHALLENGE
→ OBSERVATION
```

---

# 1. Fuentes de autoridad

Utilizar, en este orden:

```text
1. Demo definition v_0_2.md
2. sports-season-safe-to-build-review.md
3. sports-season-smallest-buildable-slice.md
4. Architecture v0.5 + ADR-001–005
5. evidencia y cierres históricos S01–S39
```

`Demo definition v_0_2.md` gobierna **qué demo queremos construir**.

El SAFE-TO-BUILD review gobierna **qué capacidades existen, cuáles faltan y qué límites deben preservarse**.

`Sports Season — smallest buildable slice` define **el corte técnico mínimo autorizado**, subordinado a la Demo Definition.

No reinterpretar la narrativa para ajustarla a las capacidades existentes.

No modificar `Demo definition v_0_2.md` durante esta construcción.

---

# 2. Regla principal

Aplicar:

```text
BUILD THE SITUATED CUT
NOT THE GENERAL PLATFORM
```

y:

```text
new local capability
!=
generalized architecture
```

Toda construcción nueva debe estar justificada por una necesidad observable del corte.

No construir preventivamente:

```text
generic season engine
generic event engine
generic Experience engine
generic rewards engine
generic rules engine
generic CRM
generic participant platform
generic provider architecture
generic navigation framework
no-code demo editor
```

---

# 3. PRE-BUILD EXECUTION GATE — OBLIGATORIO

Antes de modificar cualquier archivo productivo, resolver o aislar el problema ambiental que impidió ejecutar Vitest durante el SAFE-TO-BUILD review.

El fallo observado fue:

```text
ERR_DLOPEN_FAILED
Rolldown native binding
macOS Team ID mismatch
```

## Requisito

Debe existir un entorno en el que pueda ejecutarse la baseline relevante antes de comenzar el delta productivo.

Intentar primero soluciones ambientales mínimas y reversibles.

No utilizar como primer recurso:

```text
delete lockfile
rewrite package configuration
change dependencies
change test framework
disable tests
skip suites
change expected hashes
```

No modificar producto para corregir un problema de entorno.

Registrar:

```text
Node version
architecture
command
working directory
exit code
environmental intervention if any
```

---

## PRE-BUILD STOP

Si no es posible disponer de un entorno verificable sin una modificación material no autorizada:

```text
STOP BEFORE PRODUCT DELTA
```

Documentar el bloqueo operacional.

No empezar a construir la demo sin capacidad razonable de comprobar posteriormente el cambio.

Este STOP no convierte automáticamente el problema ambiental en H40.

---

# 4. Baseline antes del delta

Una vez disponible el entorno:

1. preservar el working tree recibido;
2. registrar hashes/material inventory relevante;
3. ejecutar la baseline actual que resulte legítimamente ejecutable;
4. distinguir explícitamente:

```text
historical replay
!=
current-product verification
```

No exigir que un hash histórico describa el producto después de un delta intencional.

No actualizar baselines históricas para hacerlas coincidir con el nuevo producto.

---

# 5. Regla para evidencia histórica

Las evidencias S01–S39 son históricas.

Preservar:

```text
historical evidence
historical traces
historical reports
historical verdicts
historical hashes
```

Un cambio intencional de:

```text
App.tsx
contracts.ts
bootstrap.ts
```

puede hacer que una comprobación histórica de bytes ya no describa el producto actual.

Esto debe registrarse como:

```text
current product changed intentionally
```

y no como:

```text
historical evidence rewritten
```

Nunca:

```text
update old expected hash
→ make historical replay green
```

Si fuera necesaria una adaptación futura de la infraestructura para separar replay histórico de verificación actual, registrarla como presión observada.

No resolverla aquí salvo que impida materialmente verificar este BUILD.

---

# 6. Corte autorizado

Construir únicamente el recorrido primario:

```text
TEMPORADA DEPORTIVA
↓
Carrera
↓
participante externo
↓
elige Social o Bienestar
↓
confirma inscripción
↓
QR / check-in simulado
↓
Evidencia de presencia
↓
declara esfuerzo:
suave / medio / intenso
↓
Evidencia de esfuerzo
↓
regla situada
↓
insignia individual
↓
motivo visible
↓
invitación a conocer / incorporarse al club
↓
cambio de perspectiva
↓
Marketing / CRM
```

La persona debe seguir siendo:

```text
EXTERNAL
```

al terminar el recorrido.

La invitación:

```text
!= membership
!= consent
!= conversion
!= lead sent
```

---

# 7. Temporada y disciplinas

La demo debe hacer visible una temporada con:

```text
Carrera
Vela
Vóley playa
```

Sólo Carrera es ejecutable en este corte.

Vela y Vóley playa deben presentarse de manera que no induzcan a creer que sus recorridos están implementados.

Mantener:

```text
season
!=
event
```

No implementar lógica transversal entre disciplinas.

---

# 8. Persona y membresía

Introducir la mínima representación explícita necesaria para que exista:

```text
person
+
membershipStatus
```

El recorrido ejecutado utiliza:

```text
membershipStatus = external
```

No satisfacer contratos existentes inventando un miembro ficticio.

No inferir:

```text
person
=
member
```

ni:

```text
participant
=
customer
```

La relación comercial con el club permanece explícita y diferenciada.

---

# 9. Inscripción

Implementar una inscripción deportiva situada que conserve al menos:

```text
registrationId
personRef
eventRef
selectedModality
status
```

La modalidad elegida pertenece a:

```text
esta inscripción
+
este evento
```

No al perfil permanente de la persona.

Debe ser posible elegir realmente:

```text
Social
Bienestar
```

No fijar silenciosamente la elección desde Demo Script o fixture.

---

# 10. Evidencia de presencia

Implementar:

```text
QR / CHECK-IN SIMULADO
→ Evidencia de presencia
```

Debe conservar como mínimo:

```text
evidenceId
personRef
registrationRef
eventRef
occurredAt
source = simulated-check-in
```

La interfaz debe dejar claro que el check-in es simulado.

No afirmar:

```text
physical attendance verified
real QR scanned
external system confirmed attendance
```

---

# 11. Evidencia de esfuerzo

Implementar una Evidencia independiente para:

```text
suave
medio
intenso
```

Debe quedar explícitamente registrada como:

```text
participant self-report
```

No derivarla desde:

```text
presence
copy
modality
person profile
```

Mantener:

```text
presence
!=
effort
```

Los tres niveles satisfacen el mismo requisito del corte.

No utilizar intensidad para valorar a la persona, segmentarla permanentemente o inferir intención de compra.

---

# 12. Regla situada de insignia

Implementar únicamente esta regla local:

```text
accepted registration
+
simulated presence Evidence
+
valid self-reported effort Evidence
+
same person
+
same event
→
individual badge
```

La regla debe residir en runtime / lógica de producto situada.

No en:

```text
App copy
Demo Script wording
Activity
UI routing
```

No reutilizar:

```text
K
Family Adventure evaluator
hospitality premise
TES Progression
TES Completion
TES Result
```

La regla es:

```text
LOCAL
SPORTS-SEASON-SPECIFIC
EXPERIMENTAL
NOT PROMOTED
```

---

# 13. Insignia

La insignia debe conservar al menos:

```text
badgeId
personRef
registrationRef
rule/version reference
supporting Evidence refs
reason
```

Debe resultar perceptible para la persona:

```text
qué ha obtenido
por qué lo ha obtenido
qué puede hacer después
```

No convertir la insignia en:

```text
cupón
trofeo
nivel
beneficio económico
```

---

# 14. Oportunidad de captación

Después de obtener la insignia:

```text
external participant
→ club invitation / capture opportunity
```

Debe permanecer separada del reconocimiento.

No modificar:

```text
membershipStatus = external
```

Mostrar oportunidad.

No ejecutar conversión.

No afirmar intención de compra.

No crear lead real.

No producir consentimiento ficticio.

---

# 15. Perspectiva Marketing / CRM

Implementar una segunda superficie que utilice **el mismo runtime y el mismo estado**.

Debe poder mostrar, como mínimo:

```text
persona
membership status
temporada
evento
disciplina
modalidad elegida
inscripción
Evidencia de presencia + origen
Evidencia de esfuerzo + origen
insignia
motivo / criterio
oportunidad de captación
```

Distinguir claramente:

```text
fixture data
observed / entered facts
derived local recognition
commercial opportunity
```

No mostrar como hechos:

```text
converted
interested in buying
high-value customer
verified athlete
real attendee
```

---

# 16. Cambio de perspectiva

El cambio:

```text
PARTICIPANTE
↔
MARKETING / CRM
```

debe conservar:

```text
composition identity
runtime
provider/state where applicable
person
registration
Evidence
badge
opportunity
```

No debe:

```text
reset
change composition
create new business action
change participant
```

No crear una nueva abstracción general de navegación salvo necesidad demostrada durante la construcción.

---

# 17. Reset

Implementar reset determinista.

Debe devolver Sports Season a su estado inicial y eliminar únicamente el estado mutable de esta ejecución:

```text
registration
presence Evidence
effort Evidence
badge
capture opportunity
```

No modificar:

```text
Retail
Arrival
Family Adventure A
Family Adventure B / Costa
historical evidence
```

---

# 18. Representación de equipos

Vóley playa puede mostrar que existen eventos por equipos.

En este corte:

```text
team
→ informative / organizational concept only
```

No ejecutar:

```text
Group TES
collective outcome
collective Evidence
team-owned badge
team-owned reward
collective claim
```

Si para mostrar Vóley resulta necesario inventar esas relaciones:

```text
DO NOT DO IT
```

Reducir su representación a contenido informativo honesto.

---

# 19. Experience

No inventar una Experience deportiva validada para satisfacer un contrato.

No reutilizar:

```text
Family Adventure
Active Challenge
hospitality Experience
```

mediante simple cambio de nombre.

Si Scenario exige actualmente una `experienceRef`, resolverlo mediante el mínimo ajuste técnico que permita representar responsablemente el corte sin afirmar semántica que no existe.

Mantener abierta:

```text
modality
↔
Experience
```

No resolver cardinalidad en este BUILD.

---

# 20. App y responsabilidades

App debe seguir siendo consumidor.

No trasladar a React:

```text
factual validation
badge eligibility
membership transition
Evidence authority
business rules
```

La UI:

```text
captures input
requests public action
renders read model
```

El runtime:

```text
validates
accepts/rejects
mutates controlled state
applies situated rule
projects observable result
```

---

# 21. Código local nuevo

El SAFE-TO-BUILD review autoriza código situado donde sea necesario.

Puede incluir, si la implementación concreta lo justifica:

```text
sports-season-artifacts.ts
sports-season-runtime.ts
local sports contracts/types
new manifest/composition
bootstrap resolution
sports UI components
sports read model/projection
tests
styles/assets
```

Los nombres son orientativos, no obligatorios.

No crear archivos sólo para ajustarse a esta lista.

No duplicar:

```text
App
MockDataAdapter
K evaluator
Family Adventure
```

como método de implementación.

---

# 22. Demo-Author UX — REGISTRO OBLIGATORIO

Esta construcción constituye nuestra primera observación real de la UX del creador de demos.

Crear un registro separado durante BUILD.

Para cada elemento necesario de la Demo Definition, registrar si pudo resolverse mediante:

```text
existing configuration
new situated configuration
small reusable code extension
new situated product code
duplication required
manual workaround
blocked
```

Registrar especialmente:

```text
marca
temporada
eventos
fechas
modalidades
persona
membership status
copy
Evidencia
regla
insignia
oportunidad
perspectiva CRM
```

No mejorar preventivamente la UX del creador durante esta misma construcción sólo para obtener mejores resultados.

Primero observar la fricción.

---

# 23. No construir editor sin código

Aunque el objetivo futuro sea permitir que un creador cambie la demo sin programar:

```text
DO NOT BUILD NO-CODE AUTHORING
```

en esta sesión.

La programación necesaria es precisamente evidencia de la baseline actual de Demo-Author UX.

---

# 24. Pruebas mínimas obligatorias

Añadir comprobaciones del nuevo corte que cubran al menos:

```text
external participant remains external
registration stores selected modality
registration != presence
presence != effort
check-in source remains simulated
effort source remains self-reported
badge unavailable before complete rule
badge granted after valid complete rule
badge references correct person/event/Evidence
repeat action does not duplicate facts/badge
invalid order rejected without mutation
invalid effort rejected without mutation
wrong person/event rejected
perspective change preserves state
reset restores initial state
sports composition isolated from R/H/A/B
```

Cambiar:

```text
label
copy
display name
```

no debe cambiar:

```text
facts
attribution
eligibility
```

---

# 25. Browser gate

Una vez construido y con pruebas ejecutables:

realizar inspección en navegador si la herramienta está disponible.

Comprobar al menos:

```text
initial participant surface
event selection
modality choice
registration
simulated check-in
effort input
badge
reason
club invitation
Marketing/CRM view
reset
error path
```

Separar:

```text
DOM test
browser execution
human UX observation
```

No llamar «human UX validated» a una inspección del agente.

---

# 26. Human-use readiness

El objetivo de BUILD no es aceptar la UX.

El objetivo es llegar al estado:

```text
READY FOR HUMAN UX CHALLENGE
```

Esto requiere como mínimo:

```text
functional path works
no known semantic shortcut invalidates it
state survives perspective change
errors are legible
reset works
simulated provenance is visible
browser path is usable
```

No requiere que la UX sea buena.

De hecho, necesitamos conservar fricciones reales para poder observarlas.

---

# 27. STOP DURING BUILD

Detener el delta si aparece evidencia de que continuar exige:

```text
fabricating membership
fabricating Experience authority
merging presence and effort
reusing hospitality contexts falsely
making Activity factual authority
calling checkpoint TES Progression
introducing unsupported collective semantics
rewriting historical evidence
weakening tests to obtain green
```

En ese caso:

```text
STOP
→ identify blocker
→ preserve partial evidence
→ do not architect around it
```

---

# 28. También STOP si el corte crece materialmente

Si la implementación empieza a exigir:

```text
generic engine
generic provider architecture
large App redesign
general reward system
general participant identity system
general event platform
```

detenerse.

Explicar qué requisito concreto del corte produjo esa necesidad.

No asumir que la abstracción es necesaria porque parezca elegante.

---

# 29. Evidencia de ejecución

Registrar por separado:

```text
PRE-BUILD BASELINE
PRODUCT DELTA
NEW TESTS
CURRENT VERIFICATION
HISTORICAL PRESERVATION
BROWSER INSPECTION
DEMO-AUTHOR UX OBSERVATIONS
NOT EXECUTED
```

No mezclar resultados antiguos S39 con resultados de este BUILD.

Un test S39 PASS es evidencia S39.

Un test nuevo PASS es evidencia de este BUILD.

---

# 30. Resultado esperado

El observable central debe ser:

```text
persona externa
+
inscripción Carrera
+
modalidad elegida
+
Evidencia de presencia simulada
+
Evidencia de esfuerzo autodeclarada
+
insignia individual explicada
+
oportunidad de captación
```

y posteriormente:

```text
Marketing / CRM
→ ve los mismos hechos y su procedencia
→ sin cambio de persona
→ sin cambio de composición
→ sin reset
```

La persona debe seguir siendo externa.

---

# 31. Lo que este BUILD no demostrará

Incluso si todo funciona:

```text
NOT PROVEN
```

seguirán siendo:

```text
competición ejecutada
resultado + posición ejecutados
trofeo concedido
ranking
segunda participación
booster
TES Progression
TES Completion
TES Result
beneficio por recurrencia
acceso anticipado real
cross-sport progression
team semantics
Group TES
collective recognition
real QR
real attendance
real authentication
real membership conversion
CRM integration
ecommerce integration
sports API integration
no-code demo authoring
commercial acceptance
participant UX acceptance
general demo-definition protocol
```

---

# 32. Informe final obligatorio

Entregar al menos:

## A. Pre-build gate

```text
environment
baseline
tests executable?
```

## B. Delta implementado

Archivo por archivo:

```text
what changed
why required by Demo Definition
whether situated or reused
```

## C. Recorrido ejecutado

Reconstrucción factual:

```text
input
action
state
Evidencia
rule
result
projection
```

## D. Pruebas

Separar:

```text
PASS
FAIL
NOT EXECUTED
```

## E. Preservación histórica

Explicar cómo se mantuvo:

```text
historical replay
!=
current verification
```

## F. Demo-Author UX

Tabla de:

```text
wanted variation
configuration available
code required
duplication required
friction observed
```

## G. Browser inspection

Ejecutada o NOT EXECUTED.

## H. Límites

Qué sigue sin estar demostrado.

## I. Veredicto

Utilizar uno de:

```text
BUILD COMPLETED
→ READY FOR HUMAN UX CHALLENGE
```

o:

```text
BUILD STOPPED
→ MATERIAL BLOCKER OBSERVED
```

con las cualificaciones necesarias.

---

# 33. No seleccionar automáticamente el trabajo posterior

Si el BUILD termina correctamente:

no implementar el siguiente corte.

No añadir competición.

No implementar booster.

No implementar editor.

No arreglar UX observada.

No abrir H40.

Cerrar primero esta construcción y preservar la evidencia.

El siguiente paso será que una persona utilice y desafíe la demo, o que evaluemos juntos las fricciones de autoría observadas.

---

# 34. Finalidad

Estamos construyendo deliberadamente algo que todavía puede resultar incómodo, confuso o imperfecto.

Eso no es un defecto del experimento.

Necesitamos llegar a una demo:

```text
semantically responsible
functionally coherent
reversible
observable
human-usable
```

para poder descubrir mediante uso aquello que ya no podemos aprender únicamente leyendo arquitectura.

El cambio de régimen es:

```text
PREVENTIVE HARDENING
↓
SITUATED BUILD
↓
HUMAN UX CHALLENGE
↓
OBSERVED PRESSURE
↓
BOUNDED EXPERIMENT
↓
REFINEMENT
```

Construir sólo lo suficiente para alcanzar de forma segura el siguiente nivel de evidencia.