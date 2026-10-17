Abre la Sesión 27 a partir del resultado consolidado de H26.

H26 permanece FALSIFIED.

No corrijas todavía L3a, L3c ni L4.

## 1. Baseline

Mantener:

```text
SESSION 20 → CLOSED

H21 → FALSIFIED / historical baseline

H22 → SUPPORTED WITH QUALIFICATION
       Experience-based behavior selection

H23 → SUPPORTED WITH QUALIFICATION
       situated evaluation context binding

H24 → FALSIFIED
       no legitimate existing Activity
       representation source

H25 → SUPPORTED WITH QUALIFICATION
       script-bound Activity representation

H26 → FALSIFIED
       existing sources insufficient
       for complete GuestPerspective

L3a ACCOUNT DISPLAY
→ legitimate account source available
→ GuestPerspective sessionLabel OPEN

L3b SUBJECT DISPLAY
→ NO LEGITIMATE EXISTING SOURCE
→ FIRST H26 FALSIFIER
→ OPEN

L3c JOURNEY NARRATIVE
→ operational/derived inputs available
→ situated narrative source absent
→ OPEN

L4
→ SOURCE-INSPECTION FINDING / OPEN

L5
→ SCRIPT-BOUND SITUATED REPRESENTATION
→ EXECUTION-VERIFIED within A/B
```

Preservar:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

No reinterpretar H26 después de esta nueva sesión.

---

## 2. Hallazgo que autoriza S27

H26 demuestra que falta la relación:

```text
Experience subject reference
        ↓
?
        ↓
situated human representation
```

Los datos narrativos existentes no establecen esa relación.

Preservar:

```text
co-located data
!=
declared relationship
```

```text
same human name across artifacts
!=
subject identity relation
```

---

## 3. H27

```text
H27 — Explicit Situated Subject Representation
```

Hipótesis falsable:

```text
Dentro del recorrido Family Adventure,
una relación presentacional explícita
puede asociar cada subjectRef de Experience
con una representación humana situada,

de modo que esa representación pueda variar
independientemente de la cuenta/sesión,
sin modificar identidad factual,
operationalSessionSubjectRef,
atribución de Evidence,
contexto, evaluación, K o claim.
```

La relación:

```text
subjectRef → situated presentation
```

es exclusivamente representacional.

No constituye una relación de identidad de dominio.

---

## 4. Guarda central

Preservar obligatoriamente:

```text
subject presentation
!=
subject identity
```

```text
account/member
!=
Experience subject
```

```text
operational session
!=
authentication identity
```

```text
display-name equality
!=
identity equality
```

```text
represented subject
!=
authenticated user
```

No introducir:

```text
memberId → subjectRef
```

ni:

```text
accountSubjectRef
viewerSubjectRef
actorRef
operatorRef
representativeRef
```

para hacer pasar H27.

---

## 5. Candidate host

Antes del delta, compara explícitamente al menos:

```text
ScenarioDefinition
DemoScript
GuestPerspectiveReadModel
Fixture
```

como posibles hosts.

La candidata experimental preferida es `DemoScript`, porque:

```text
Scenario
→ operational/semantic subject references
```

mientras:

```text
DemoScript
→ situated demo presentation
```

Pero no asumas esta decisión sin documentar el análisis.

No añadas `displayName` directamente a `ScenarioDefinition.subjects` salvo que el experimento demuestre que Script no puede alojar legítimamente la relación dentro del alcance autorizado.

Si para resolver H27 es necesario modificar la semántica del SubjectReference compartido:

```text
STOP
```

---

## 6. Shape experimental mínima

Si el análisis del host confirma DemoScript, puede ensayarse una forma local equivalente a:

```text
subjectPresentations?: [
    {
        subjectRef: "subject-p1",
        label: "Inés"
    },
    {
        subjectRef: "subject-p2",
        label: "Mateo"
    }
]
```

La forma concreta puede ajustarse al contrato local.

Debe clasificarse:

```text
EXPERIMENTAL
LOCAL
REVERSIBLE
NOT PROMOTED
```

Evitar nombres como:

```text
SubjectProfile
SubjectIdentity
Participant
AccountSubject
Persona
```

que implicarían semántica no demostrada.

---

## 7. No usar la cuenta como fuente

Para A puede declararse explícitamente, por ejemplo:

```text
subject-p1 → "Lucía"
subject-p2 → "Huésped 2"
```

Para B:

```text
subject-p1 → "Inés"
subject-p2 → "Mateo"
```

Pero estas declaraciones deben existir por sí mismas.

No generarlas mediante:

```text
fixture.member.name
→ subject-p1 label
```

La coincidencia Lucía/Lucía o Inés/Inés es un dato narrativo intencionado de la composición, no una relación de identidad inferida.

---

## 8. Threading mínimo

Transporta la representación hasta `projectGuestPerspective()` mediante la ruta técnica mínima desde la composición resuelta.

No introducir la representación en:

```text
EvidenceInput
Public Action
subjectStates
evaluation
```

No utilizar el label para buscar, filtrar o identificar Evidence.

La asociación debe continuar utilizando:

```text
subjectRef
```

como referencia.

La representación sólo determina:

```text
GuestPerspective.subjects[].label
```

dentro de H27.

No reutilizarla todavía en App, supervision, sessionLabel o journey message.

---

## 9. Alcance preciso de H27

Modificar exclusivamente la procedencia de:

```text
GuestPerspective.subjects[].label
```

para Family Adventure A/B.

No corregir todavía:

```text
GuestPerspective.sessionLabel
GuestPerspective.message
GuestPerspective.subjects[].status
```

cuando contengan segunda persona, género o narrativa situada.

Esos elementos pertenecen a L3a/L3c o a una relación perspectival todavía no demostrada.

No eliminar esos síntomas mediante copy genérico.

---

## 10. A control

A debe producir subject labels a partir de la nueva relación explícita:

```text
subject-p1
→ Lucía

subject-p2
→ Huésped 2
```

o labels equivalentes declarados explícitamente.

Verificar que los IDs siguen siendo:

```text
subject-p1
subject-p2
```

y Evidence permanece:

```text
A@subject-p1
B@subject-p2
```

No inferir labels desde member.

---

## 11. B control

B debe declarar y mostrar:

```text
subject-p1
→ Inés

subject-p2
→ Mateo
```

GuestPerspective.subjects debe exponer esos labels en todas las fases.

No debe contener:

```text
"Tú · huésped 1"
"Huésped 2 · ya existe..."
```

como labels derivados por ID.

El resto de L3 puede permanecer incorrecto y debe registrarse separadamente.

---

## 12. Control crítico account ≠ subject presentation

Crea una variante exclusivamente de harness:

```text
fixture.member.name
→ Inés

subject-p1 presentation
→ Participante Alfa
```

Mantener:

```text
operationalSessionSubjectRef
→ subject-p1

Evidence A
→ subject-p1

Evidence B
→ subject-p2
```

Debe observarse simultáneamente:

```text
account presentation
→ Inés

GuestPerspective subject-p1 label
→ Participante Alfa
```

sin cambios en hechos, estado o evaluación.

Esto es condición discriminante principal de H27.

---

## 13. Control inverso

Crear otra variante donde:

```text
fixture.member.name
→ Cuenta Demo
```

pero:

```text
subject-p1 presentation
→ Inés
```

Debe observarse:

```text
account presentation
→ Cuenta Demo

subject-p1 label
→ Inés
```

mientras permanecen idénticos:

```text
subjectRefs
operationalSessionSubjectRef
Evidence
context
evaluation
K
claim
```

No cambiar Scenario para conseguirlo.

---

## 14. Representation independence

Crear variantes X/Y que cambien exclusivamente:

```text
subjectPresentations[].label
```

Manteniendo:

```text
Scenario subjects
member
session
actions
Evidence
contexts
evaluation
Activity
```

Después:

```text
facts X == facts Y
evaluation X == evaluation Y
Activity X == Activity Y
subject labels X != subject labels Y
```

No editar directamente el snapshot.

---

## 15. No introducir «Tú»

La nueva representación no autoriza automáticamente:

```text
subject-p1 → Tú
```

porque eso exigiría una relación perspectival distinta:

```text
viewer/account/session
→ represented subject
```

H27 no estudia esa relación.

Por tanto, utilizar labels nominales o descriptivos explícitos.

No derivar segunda persona de:

```text
operationalSessionSubjectRef
```

---

## 16. Ausencia / mismatch

No diseñar todavía una política productiva general.

Pero verificar al menos que una representación no puede:

```text
create a subject
change subjectRef
change Evidence attribution
```

Si el Script contiene una referencia de presentación para un subjectRef inexistente, no debe materializar un nuevo sujeto.

Si expresar de manera segura la ausencia de presentación exige cambiar contratos adicionales o inventar un fallback general:

```text
STOP
```

Documentar la presión sin resolverla.

---

## 17. L3a fuera de alcance

Mantener:

```text
GuestPerspective.sessionLabel
→ OPEN
```

aunque siga diciendo Lucía en B.

No sustituirlo simplemente por:

```text
member.name
```

porque la frase actual mezcla:

```text
account presentation
subject relation
second-person perspective
capability narrative
```

La presentación de cuenta aislada ya dispone de fuente legítima:

```text
fixture.member.name
```

pero la composición de sessionLabel pertenece a otra presión.

---

## 18. L3c fuera de alcance

Mantener:

```text
GuestPerspective.message
GuestPerspective.subjects[].status
```

sin corrección situada si hacerlo exige:

```text
second-person perspective
gender
journey narrative
situated locations
```

Registrar los síntomas restantes.

No reutilizar:

```text
presenterLabel
activityPresentation
subjectPresentations
```

como narrativa general por mera conveniencia.

---

## 19. L4 congelado

No modificar `App.tsx`.

Mantener:

```text
L4
→ SOURCE-INSPECTION FINDING
→ OUT OF SCOPE
```

No reutilizar subjectPresentations directamente desde App para saltarse GuestPerspective.

---

## 20. L5 congelado

Mantener:

```text
activityPresentation
```

sin promoción ni reutilización automática.

Verificar regresión H25:

```text
A Activity → jardín/fuente
B Activity → mirador/patio
```

Subject presentation no debe modificar Activity.

---

## 21. Falsadores H27

H27 → FALSIFIED si:

```text
subject label cannot vary independently
from account/member
```

o:

```text
representation changes subjectRef,
Evidence attribution, session,
context or evaluation
```

o:

```text
a member→subject mapping is required
to make the relation work
```

o:

```text
subject presentation must be embedded
in SubjectReference semantics
```

o:

```text
new relation requires Actor/Participant/
Representative/etc.
```

o:

```text
App must be modified to make
GuestPerspective carry the relation
```

o aparece regresión A.

Usar INCONCLUSIVE sólo para impedimento externo.

---

## 22. Veredicto positivo

H27 → SUPPORTED WITH QUALIFICATION únicamente si:

```text
subjectRef
→ explicit situated presentation
```

puede variar independientemente de:

```text
account display
operational session
factual identity
Evidence attribution
evaluation
Activity representation
```

y GuestPerspective B obtiene labels situados sin hardcodes A.

La cualificación debe indicar que H27 NO demuestra:

```text
subject identity model
account→subject relation
viewer/perspective relation
authentication
general participant model
journey narrative provenance
general presentation architecture
```

---

## 23. Artifact quarantine

Si la nueva relación funciona:

```text
DemoScript.subjectPresentations
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

No convertirla automáticamente en:

```text
Experience contract
Subject contract
Product Semantic Contract
TES concept
general identity model
```

Recurrencia futura no implica promoción.

---

## 24. Verificación

Ejecutar:

```text
H27 focused harness
H26 historical reproduction
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

No se necesita navegador para `GuestPerspective.subjects[].label` si el snapshot público lo demuestra.

---

## 25. Informe

Crear:

`session-27-explicit-situated-subject-representation.md`

con:

```text
H26 CONSOLIDATED INPUT

H27 HYPOTHESIS

VARIABLE UNDER TEST

WHY A NEW RELATION IS NOW PERMITTED

SUBJECT / ACCOUNT / SESSION SEPARATION

CANDIDATE HOST ANALYSIS

EXPERIMENTAL REPRESENTATION SHAPE

REPRESENTATION AUTHORITY

THREADING PATH

BASELINE

CODE DELTA

A CONTROL

B CONTROL

ACCOUNT / SUBJECT DECOUPLING CONTROL

INVERSE DECOUPLING CONTROL

REPRESENTATION INDEPENDENCE CONTROL

ABSENCE / MISMATCH OBSERVATION

EXECUTION TRACE

L3b RESULT

L3a STATUS

L3c STATUS

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H27 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H27 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H28.

---

## 26. Guardas finales

Preservar:

```text
subject presentation
!=
subject identity
```

```text
account presentation
!=
subject presentation
```

```text
account/member
!=
Experience subject
```

```text
operationalSessionSubjectRef
!=
authentication identity
```

```text
same display name
!=
same identity
```

```text
co-located data
!=
declared relationship
```

```text
display relation
!=
factual authority
```

```text
GuestPerspective
!=
Activity history
```

```text
subjectPresentations
!=
journey narrative
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
H27
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3b SUBJECT DISPLAY
→ status

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ supported / unsupported

L3a
→ preserved / open

L3c
→ preserved / open

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
