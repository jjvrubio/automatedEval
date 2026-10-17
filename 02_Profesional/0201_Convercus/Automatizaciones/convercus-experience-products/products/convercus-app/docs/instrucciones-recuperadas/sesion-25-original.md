Abre la Sesión 25 a partir del resultado consolidado de H24.

H24 queda falsificada. No intentes reescribirla después de introducir una relación nueva.

## 1. Baseline

Mantener:

```text
SESSION 20
→ CLOSED

H21
→ FALSIFIED for historical baseline

H22
→ SUPPORTED WITH QUALIFICATION

H23
→ SUPPORTED WITH QUALIFICATION

H24
→ FALSIFIED

L1
→ SITUATED BINDING EXECUTION-VERIFIED

L2a/L2b
→ EXPERIENCE-BASED SELECTION EXECUTION-VERIFIED

L5
→ EXECUTION-CONFIRMED / OPEN

L3
→ EXECUTION-CONFIRMED / OPEN

L4
→ SOURCE-INSPECTION FINDING / OPEN
```

Preservar las reproducciones históricas.

H24 demostró:

```text
NO LEGITIMATE EXISTING SOURCE
```

para representar posteriormente una acción aceptada de manera situada.

No reutilizar `presenterLabel`.

---

## 2. Consecuencia que autoriza esta sesión

H24 demuestra una relación ausente:

```text
accepted action
        ↓
?
        ↓
situated Activity representation
```

S25 puede probar una relación nueva mínima, local y reversible.

Esto NO autoriza:

```text
ContentRegistry
NarrativeEngine
LocalizationService
PresentationEngine
ActivityTemplateRegistry
```

o arquitectura equivalente.

---

## 3. H25

```text
H25 — Script-Bound Situated Activity Representation
```

Hipótesis falsable:

```text
Una DemoScript Step puede declarar
una representación situada de Activity
distinta de su affordance previa,

de forma que esa representación solo
se materializa después de que el runtime
acepte la acción correspondiente,

y puede variar o estar ausente
sin modificar Evidence, atribución,
contexto, estado operacional,
admisibilidad, K o claim.
```

La relación propuesta es experimental.

No constituye un contrato productivo.

---

## 4. Distinción obligatoria dentro de DemoScript

Preservar:

```text
presenterLabel
→ affordance BEFORE action
```

y experimentar separadamente con algo equivalente a:

```text
activityPresentation
→ representation AFTER accepted action
```

No derives uno del otro.

No hagas parsing, transformación verbal o sustitución textual de `presenterLabel`.

Evita nomenclatura `completion*` para no confundir esta representación con Experience Completion o TES Result.

---

## 5. Shape experimental mínima

Puede añadirse a `DemoScriptStep` una shape local y opcional equivalente a:

```text
activityPresentation:
    title
    description
```

El nombre concreto puede ajustarse si el contrato existente lo requiere, pero debe conservar este significado limitado.

Preferir, si es técnicamente razonable, una shape inline/local antes que promover un nuevo concepto nominal amplio.

Clasificar explícitamente:

```text
EXPERIMENTAL
LOCAL
REVERSIBLE
NOT PROMOTED
```

No modificar Product Semantic Contract.

---

## 6. Fuente de autoridad

`activityPresentation` es únicamente:

```text
presentation input
```

No es:

```text
fact
Evidence
runtime state
evaluation input
semantic authority
```

Preservar:

```text
declared representation
!=
occurred activity
```

La mera existencia del campo en Script no puede crear Activity.

---

## 7. Threading técnico

Inspecciona primero cuál es el threading mínimo para que la composición resuelta pueda poner esa representación a disposición del lugar que materializa Activity.

Prioriza:

```text
resolved DemoScript
→ mock provider/adapter
```

como dependencia presentacional de la demo resuelta.

No introduzcas el texto dentro de `EvidenceInput`.

No uses Evidence como contenedor de narrativa.

No conviertas `subjectRef`, markerRef, context o source en mecanismo de inferencia.

Evita añadir representación a la Public Action si existe una ruta más limpia desde la composición resuelta.

Si transportar la relación requiere alterar el significado de `DemoProvider` o introducir una nueva arquitectura pública:

```text
STOP
```

y registra el falsador.

---

## 8. Runtime semantics

El runtime continúa teniendo autoridad únicamente sobre si la acción es aceptada.

Secuencia requerida:

```text
DemoScript declares representation
        ↓
NO Activity yet

Public Action
        ↓
runtime validates

if rejected:
    NO Evidence
    NO Activity representation

if accepted:
    Evidence / operational consequence
        ↓
    optional situated Activity representation
```

DemoScript no controla checkpoint, habilitación, atribución ni evaluación.

---

## 9. A control

A debe declarar explícitamente representaciones adecuadas para sus dos acciones de Evidence:

```text
marker A
→ jardín representation

marker B
→ fuente representation
```

Ejecutar:

```text
enlist
→ action A
→ activate P2
→ action B
```

Activity efectiva debe conservar el comportamiento visual aceptado de A.

No modificar sus Evidence, contexto o evaluación.

---

## 10. B control

B debe declarar representaciones propias:

```text
marker A
→ mirador representation

marker B
→ patio representation
```

Ejecutar la misma secuencia.

Activity efectiva debe contener exclusivamente la representación B correspondiente a esas acciones y no:

```text
jardín
fuente
```

Los hechos B deben seguir siendo:

```text
evidence-costa-a-p1
→ subject-p1
→ marker-a

evidence-costa-b-p2
→ subject-p2
→ marker-b
```

con contexto Costa y evaluación H23 intacta.

---

## 11. Control crítico: declaration != occurrence

Antes de ejecutar ninguna acción de Evidence:

```text
Script contains activityPresentation
```

pero debe mantenerse:

```text
no new clue Activity
no Evidence
K not-attempted
claim not-produced
```

La representación declarada no puede aparecer en Activity por existir en Composition.

---

## 12. Control crítico: representation independence

Crea dos variantes experimentales del mismo Script manteniendo exactamente constantes:

```text
Scenario
actionIds
Public Actions
Evidence payload
Evidence IDs
Evidence type
subjectRefs
marker refs
contexts
operational state
premise
K
```

y variando únicamente:

```text
activityPresentation
```

Por ejemplo:

```text
variant X
→ representation X

variant Y
→ representation Y
```

Después de ejecutar la misma acción debe observarse:

```text
facts X == facts Y

operational state X == Y

evaluation X == Y

claim X == Y

Activity representation X != Y
```

Este es el control discriminante principal de H25.

No editar directamente el snapshot/read model.

---

## 13. Control inverso: representation cannot force fact

Crea un caso donde la representación está declarada pero la acción es rechazada por una guarda preexistente, por ejemplo sujeto no habilitado o checkpoint incorrecto, sin alterar esas guardas.

Debe resultar:

```text
declared representation
+
rejected action
→
no Evidence
no new Activity representation
```

No debilitar runtime para hacer pasar este control.

---

## 14. Absence control

Construye una variante experimental donde una acción factual válida carezca de `activityPresentation`.

No reintroducir:

```text
jardín/fuente
```

como fallback.

La acción factual debe poder seguir produciendo:

```text
Evidence
context
evaluation
```

sin inventar representación situada.

Para este experimento puede observarse:

```text
accepted fact
+
no activityPresentation
→
no new situated Activity record
```

Clasificar expresamente este comportamiento como:

```text
LOCAL EXPERIMENTAL ABSENCE BEHAVIOR
NOT PRODUCT FALLBACK POLICY
```

Si expresar esta ausencia exige otra semántica o contrato adicional:

```text
STOP
```

No diseñar política de fallback.

---

## 15. No inferir representación

Después del delta, `MockDataAdapter` no debe contener decisiones equivalentes a:

```text
subject-p1
→ jardín

else
→ fuente
```

ni:

```text
marker-a
→ jardín

marker-b
→ fuente
```

ni:

```text
scenario A
→ jardín
scenario B
→ mirador
```

La maquinaria puede materializar una representación ya suministrada legítimamente, pero no decidir el contenido situado.

---

## 16. No amplíes todavía el problema a dónde debe vivir Activity finalmente

H25 no pregunta todavía si:

```text
Activity representation materialization
```

debería residir finalmente en:

```text
runtime
projection layer
read-model projector
other component
```

El objetivo inmediato es probar:

```text
runtime does not DECIDE situated narrative
```

y:

```text
representation can vary independently
from factual/evaluation semantics
```

No hagas una refactorización mayor de Activity para lograr una pureza arquitectónica no exigida por H25.

---

## 17. Arrival / generic Activity regression

Hospitality Arrival y cualquier otro consumidor existente de Activity deben conservar su comportamiento.

No obligar a otras Experiences a adoptar `activityPresentation` para hacer pasar H25.

La recurrencia fuera de Family Adventure no se presupone.

Si el cambio obliga a reformular Activity globalmente:

```text
STOP
```

y registra la presión.

---

## 18. L3 permanece congelado

GuestPerspective B puede seguir mostrando:

```text
Lucía
jardín
fuente
```

Clasificar:

```text
L3
→ PRESERVED / OUT OF SCOPE
```

No reutilices automáticamente `activityPresentation` para arreglar GuestPerspective.

Que dos superficies necesiten contenido parecido:

```text
!=
same representational responsibility
```

---

## 19. L4 permanece congelado

No modificar `App.tsx` para adaptar B.

Mantener:

```text
L4
→ SOURCE-INSPECTION FINDING
→ OUT OF SCOPE
```

Activity puede verificarse mediante snapshot público.

---

## 20. Falsadores H25

H25 → FALSIFIED si:

```text
DemoScript cannot transport
the relation without taking
operational/factual authority
```

o:

```text
activityPresentation existence
can create Activity without
accepted action
```

o:

```text
changing representation changes
Evidence, context, attribution,
evaluation, K or claim
```

o:

```text
runtime must still infer situated
content from subject/marker/
scenario/client identity
```

o:

```text
threading requires a new general
architecture or changes the public
semantic responsibility of DemoProvider
```

o:

```text
A regression appears
```

Usa INCONCLUSIVE únicamente para impedimento externo.

---

## 21. Veredicto positivo

H25 → SUPPORTED WITH QUALIFICATION únicamente si:

```text
declared representation
!=
occurred Activity

accepted action
→ factual consequence
→ situated representation

same fact + different representation
→ same fact/evaluation
→ different Activity representation

no representation
→ fact can still occur
→ no invented situated narrative

rejected action
→ no Activity representation
```

y A/B siguen usando la misma maquinaria.

La cualificación debe conservar:

```text
DemoScript activityPresentation
→ experimental local shape
```

No demostraría todavía:

```text
general content architecture
general Activity architecture
localization
GuestPerspective provenance
UI correctness
cross-Experience recurrence
```

---

## 22. Verificación

Ejecutar:

```text
H25 focalized harness
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

Preservar baselines históricas.

No se necesita navegador si Activity efectiva puede observarse en snapshots.

---

## 23. Informe

Crear:

`session-25-script-bound-situated-activity-representation.md`

con:

```text
H24 CONSOLIDATED INPUT

H25 HYPOTHESIS

VARIABLE UNDER TEST

WHY A NEW RELATION IS NOW PERMITTED

CANDIDATE HOST ANALYSIS

EXPERIMENTAL SCRIPT SHAPE

REPRESENTATION AUTHORITY

THREADING PATH

BASELINE

CODE DELTA

A CONTROL

B CONTROL

DECLARATION / OCCURRENCE CONTROL

FACT / REPRESENTATION INDEPENDENCE CONTROL

REJECTED ACTION CONTROL

ABSENCE CONTROL

GENERIC ACTIVITY REGRESSION

EXECUTION TRACE

L5 RESULT

L3 STATUS

L4 STATUS

FALSIFICATION ANALYSIS

H25 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H25 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H26.

---

## 24. Artifact quarantine

Si H25 pasa, clasificar la nueva shape:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

No convertirla automáticamente en:

```text
product contract
Experience contract
TES concept
general presentation architecture
```

Recurrencia futura:

```text
!=
automatic promotion
```

---

## 25. Guardas finales

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
Evidence
!=
Activity
```

```text
DemoScript declaration
!=
runtime occurrence
```

```text
presenterLabel
!=
activityPresentation
```

```text
action affordance
!=
post-action representation
```

```text
representation input
!=
factual authority
```

```text
Activity representation
!=
evaluation input
```

```text
representation provenance
!=
semantic authority
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
H25
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L5
→ status

SCRIPT-BOUND REPRESENTATION
→ supported / unsupported
   within tested scope

FACT / REPRESENTATION INDEPENDENCE
→ supported / unsupported

L3
→ preserved / out of scope

L4
→ preserved / source-inspection

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
