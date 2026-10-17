Abre la Sesión 26 a partir del resultado consolidado de H25.

No corrijas todavía App.tsx/L4.

## 1. Baseline

Mantener:

```text
SESSION 20 → CLOSED

H21 → FALSIFIED
       historical baseline

H22 → SUPPORTED WITH QUALIFICATION
       Experience-based behavior selection

H23 → SUPPORTED WITH QUALIFICATION
       situated evaluation context binding

H24 → FALSIFIED
       no legitimate existing Activity
       representation source

H25 → SUPPORTED WITH QUALIFICATION
       script-bound Activity representation

L1 → experimentally addressed
L2a/L2b → experimentally addressed
L5 → SCRIPT-BOUND SITUATED REPRESENTATION
     EXECUTION-VERIFIED within A/B

L3 → EXECUTION-CONFIRMED / OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN
```

Mantener:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

No reescribir H24 después del resultado positivo de H25.

---

## 2. Presión seleccionada

Seleccionar únicamente:

```text
L3 — GuestPerspective situated content provenance
```

No tratar L3 como un simple problema de copy.

Descomponer durante la inspección, como mínimo:

```text
L3a
→ session/account display provenance

L3b
→ subject display provenance

L3c
→ situated journey/status narrative provenance
```

Esta división es diagnóstica y experimental.

No promover todavía L3a/L3b/L3c a arquitectura.

---

## 3. H26

```text
H26 — Situated Guest Perspective Provenance
```

Hipótesis falsable:

```text
Dentro del recorrido Family Adventure,
la Guest Perspective puede producir una
representación situada coherente para
las composiciones A y B combinando
estado/hechos/evaluación derivados con
datos presentacionales ya disponibles
en la composición resuelta,

sin hardcodes específicos de A,
sin inferir identidad de sujeto a partir
de la cuenta/sesión y sin reutilizar
Activity representation como autoridad
narrativa general.
```

H26 exige inicialmente utilizar sólo relaciones ya existentes.

No introducir una nueva shape para salvar la hipótesis.

---

## 4. Provenance audit previo obligatorio

Antes de cambiar código, inventariar todos los campos y textos de:

```text
GuestPerspectiveReadModel
projectGuestPerspective()
App consumption of guestPerspective
```

Para cada salida indicar:

```text
OUTPUT FIELD / TEXT

CURRENT SOURCE

CURRENT TRANSFORMATION

CURRENT HARDCODE

EXPECTED RESPONSIBILITY

CANDIDATE EXISTING SOURCE

FACTUAL?
OPERATIONAL?
DERIVED?
ACCOUNT PRESENTATION?
SUBJECT PRESENTATION?
SITUATED NARRATIVE?
```

Inspeccionar como candidatos existentes:

```text
BrandArtifact
ExperienceDefinition
DemoFixture.member
ScenarioDefinition.subjects
ScenarioDefinition.contexts
operationalSessionSubjectRef
DemoScript.presenterLabel
DemoScript.activityPresentation
runtime subjectStates
runtime Evidence
vertical evaluation
resolved DemoRuntime
```

No asumir que todos son fuentes legítimas.

---

## 5. Guarda account/session vs subject

Preservar:

```text
fixture member/account
!=
Experience subject
```

```text
operational session
!=
Evidence subjectRef
```

```text
displaying "Cuenta de Inés"
!=
asserting subject-p1 = account member
```

```text
represented subject
!=
authentication identity
```

No añadir automáticamente una relación:

```text
memberId → subjectRef
```

para hacer pasar H26.

No introducir:

```text
Actor
Operator
Representative
Participant
Contributor
AccountSubject
```

o equivalentes.

Si una representación requerida exige conocer una relación entre cuenta y sujeto que hoy no existe explícitamente:

```text
STOP
```

y documentar la relación ausente.

No inferirla por coincidencia narrativa.

---

## 6. Guarda Activity vs Guest Perspective

Preservar:

```text
activityPresentation
!=
GuestPerspective narrative
```

No reutilizar automáticamente:

```text
"Pista del mirador encontrada"
```

para generar:

```text
"Has encontrado la pista del mirador.
Sigue hacia..."
```

`activityPresentation` representa una ocurrencia histórica después de aceptar una acción.

GuestPerspective expresa estado/perspectiva presente.

Contenido parecido:

```text
!=
same representational responsibility
```

Puede utilizarse como evidencia de vocabulario común durante el audit, pero no como autoridad narrativa para H26.

---

## 7. DemoScript.presenterLabel

`presenterLabel` conserva su significado:

```text
affordance before action
```

Puede ser fuente legítima únicamente para representar la acción disponible como affordance.

No analizar sintácticamente el texto para extraer:

```text
mirador
patio
Inés
Mateo
```

y construir otras frases.

No transformar verbos ni hacer parsing de copy.

---

## 8. Estado y evaluación

GuestPerspective puede derivar estado únicamente de fuentes operativas/derivadas existentes:

```text
subjectStates
Evidence
evaluation
claim
available action
```

No mover estado al Script.

No utilizar contenido presentacional para decidir:

```text
enabled
Evidence count
joint admissibility
K
claim
```

Preservar:

```text
presentation
!=
factual authority
```

---

## 9. Fase experimental inicial

Sin añadir relaciones nuevas, intenta construir A y B usando exclusivamente fuentes legítimas identificadas por el audit.

El objetivo mínimo para B es que GuestPerspective no contenga indebidamente:

```text
Lucía
jardín
fuente
Aurora Stay
```

cuando esos valores son específicos de A.

Pero eliminar hardcodes mediante textos genéricos no basta si destruye información situada que ya existe legítimamente.

No considerar:

```text
"huésped"
"pista"
"lugar"
```

como PASS automático si el sistema dispone de datos situados que debería poder representar.

---

## 10. Controles A/B

Ejecutar ambas composiciones en:

```text
initial
enlisted
A@P1
P2 enabled
A@P1 + B@P2
reset
```

Comparar GuestPerspective completa.

Verificar separadamente:

```text
operational state
Evidence
evaluation
```

para demostrar que cualquier diferencia presentacional no cambia esos planos.

---

## 11. Control de account presentation

Si `fixture.member.name` puede utilizarse legítimamente como nombre de la cuenta/sesión visible sin afirmar identidad con `subject-p1`, prueba:

```text
A account presentation
→ Lucía

B account presentation
→ Inés
```

manteniendo:

```text
Evidence A/P1
Evidence B/P2
```

sin cambios.

Si el read model actual obliga a denominar ese campo como identidad del sujeto y no puede expresar únicamente account/session presentation:

```text
STOP
```

No cambies el significado del campo silenciosamente.

---

## 12. Control de subject display

Inspecciona si existe una fuente legítima y explícita para mostrar los dos sujetos de Experience.

Si existe, utilizarla.

Si únicamente existen:

```text
subject-p1
subject-p2
```

más nombres narrativos dispersos en copy:

```text
STOP
```

antes de afirmar:

```text
P1 = Inés
P2 = Mateo
```

La ausencia de una representación situada del sujeto sería evidencia, no permiso para inventar mapping.

---

## 13. Control de next-action affordance

La acción actualmente disponible debe poder representarse mediante:

```text
DemoScript.presenterLabel
```

cuando exista el paso correspondiente.

Verifica A y B.

La UI/GuestPerspective no debe decidir:

```text
garden vs mirador
fountain vs patio
```

por subjectRef, markerRef o Scenario ID.

El Script continúa sin controlar la disponibilidad: sólo representa una acción que runtime ya ha determinado como disponible.

---

## 14. Status narrative

Para mensajes como:

```text
alistado
pista aportada
P2 habilitado
sigue explorando
resultado alcanzado
```

identifica qué parte procede legítimamente de:

```text
runtime state
evaluation
```

y qué parte requiere contenido situado adicional.

No construyas narrativa situada mediante parsing de:

```text
presenterLabel
activityPresentation
Evidence type
subjectRef
```

Si no existe una fuente legítima para una parte necesaria:

```text
STOP
```

y registra el punto exacto.

---

## 15. Falsificadores H26

H26 → FALSIFIED si para producir una GuestPerspective correctamente situada es necesario:

```text
inventar account→subject mapping
```

o:

```text
reutilizar activityPresentation
como narrativa general
```

o:

```text
parsear presenterLabel
para obtener semántica situada
```

o:

```text
añadir una nueva shape/registry/
content architecture
```

o:

```text
hardcodear A/B en projection logic
```

o si:

```text
correct presentation
modifies facts/evaluation
```

o aparece regresión de A.

Detenerse en el primer falsador material.

No crear la solución ausente en esta sesión.

---

## 16. Si las fuentes existentes bastan

H26 → SUPPORTED WITH QUALIFICATION únicamente si A/B producen una GuestPerspective situada coherente empleando relaciones existentes con responsabilidades legítimas y:

```text
facts unchanged
evaluation unchanged
Activity unchanged
```

Además:

```text
A presentation
→ no B leakage

B presentation
→ no A leakage
```

sin ampliar contratos.

---

## 17. Si no bastan

Si se alcanza:

```text
NO LEGITIMATE EXISTING SOURCE
```

o una relación ausente concreta:

```text
STOP
```

y documentar:

```text
what representation is required
which existing candidates were rejected
why they are semantically inappropriate
what exact relation is absent
```

No seleccionar todavía la forma de esa relación.

Ese resultado debe clasificarse:

```text
H26 → FALSIFIED
```

dentro de la baseline actual, igual que H24.

Una sesión posterior podrá probar una relación mínima nueva si la evidencia lo justifica.

---

## 18. L4 permanece congelado

No modificar `App.tsx`.

Mantener:

```text
L4
→ SOURCE-INSPECTION FINDING
→ OUT OF SCOPE
```

No usar renderizado B para reparar App.

Si el audit descubre que App añade contenido específico después de recibir GuestPerspective:

```text
record as L4 evidence
```

pero no corregirlo.

---

## 19. L5 permanece consolidado experimentalmente

No modificar:

```text
activityPresentation
```

salvo lo necesario para ejecutar regresiones.

Mantener:

```text
L5
→ SCRIPT-BOUND SITUATED REPRESENTATION
→ EXECUTION-VERIFIED within A/B
```

No utilizar H26 para promover la shape.

---

## 20. Verificación

Ejecutar:

```text
H26 focused harness

H25 regression

H24 historical reproduction

H23 regression

H22 regression

H21 historical reproduction

Session 20 vertical regression

full suite
typecheck
lint
build
```

Si H26 se detiene en inspección por ausencia inequívoca de relación, construir solamente el harness diagnóstico necesario para reproducir el problema.

No se necesita navegador para el read model si el snapshot público permite observar L3.

---

## 21. Informe

Crear:

`session-26-situated-guest-perspective-provenance.md`

con:

```text
H25 CONSOLIDATED INPUT

H26 HYPOTHESIS

VARIABLE UNDER TEST

GUEST PERSPECTIVE OUTPUT MAP

L3 DECOMPOSITION

EXISTING SOURCE CANDIDATES

ACCOUNT / SESSION PROVENANCE

SUBJECT DISPLAY PROVENANCE

NEXT-ACTION AFFORDANCE PROVENANCE

STATUS NARRATIVE PROVENANCE

REJECTED SOURCE CANDIDATES

NO-NEW-RELATION TEST

BASELINE

CODE DELTA

A CONTROL

B CONTROL

FACT / PRESENTATION SEPARATION

L3 RESULT

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H26 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

WHAT H26 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H27.

---

## 22. Guardas

Preservar:

```text
DEMO COMPOSITION
!=
RUNTIME FACT
!=
DERIVED EVALUATION
!=
READ MODEL
!=
UI LOCAL STATE
```

```text
account/session
!=
subject identity
```

```text
operationalSessionSubjectRef
!=
authentication identity
```

```text
GuestPerspective
!=
Activity history
```

```text
presenterLabel
!=
activityPresentation
```

```text
state-derived message
!=
situated content source
```

```text
display name
!=
semantic identity
```

```text
content similarity
!=
shared responsibility
```

Mantener:

```text
TES → unchanged
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED
Product Semantic Contract → unchanged
PSC-P01 → OPEN / unchanged
PSC-P02 → NOT CREATED
Group → NOT INTRODUCED
```

No crear ADR.

Al terminar:

```text
H26
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3a ACCOUNT DISPLAY
→ status

L3b SUBJECT DISPLAY
→ status

L3c JOURNEY NARRATIVE
→ status

NO-NEW-RELATION
→ sufficient / insufficient

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
