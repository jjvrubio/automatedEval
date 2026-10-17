Abre la Sesión 24 a partir del resultado consolidado de H23.

La presión seleccionada es exclusivamente **L5 — procedencia de la representación situada de Activity**.

No corrijas L3 ni L4.

## 1. Línea de base

Mantener:

```text
SESSION 20
→ CLOSED

H21
→ FALSIFIED for historical baseline

H22
→ SUPPORTED WITH QUALIFICATION
→ Experience-based behavior selection
   execution-verified

H23
→ SUPPORTED WITH QUALIFICATION

L1
→ SITUATED BINDING EXECUTION-VERIFIED

AUTHORITY SEPARATION
→ PRESERVED under experimental premise

L3
→ EXECUTION-CONFIRMED / OPEN

L5
→ EXECUTION-CONFIRMED / OPEN

L4
→ SOURCE-INSPECTION FINDING / OPEN
```

No reescribir los resultados históricos.

Preservar las baselines y harness históricos.

## 2. Presión seleccionada

La ejecución B demuestra que Activity continúa produciendo:

```text
"Pista del jardín encontrada"
"Pista de la fuente encontrada"
```

aunque Composition B declara mirador/patio.

El problema no se formula como:

```text
wrong copy
```

sino como:

```text
factual/operational acceptance
and
situated human-readable representation
are currently coupled inside runtime machinery
```

La frontera que queremos estudiar es:

```text
accepted Experience action / factual consequence
!=
situated Activity representation
```

## 3. H24

```text
H24 — Situated Activity Representation Provenance
```

Hipótesis falsable:

```text
Una acción de Experience aceptada puede
mantener su consecuencia factual y operacional
independiente de la representación humana
situada que se proyecta en Activity,

de forma que dos composiciones que comparten
la misma semántica de acción puedan conservar
Evidence, atribución, contexto y evaluación
correctos y producir representaciones de
Activity distintas,

sin que el runtime tenga que inferir la
narrativa situada desde subjectRef,
markerRef o una identidad concreta de Scenario,
cliente o composición.
```

H24 no establece todavía una arquitectura general de contenido.

## 4. Inspección previa obligatoria

Antes de modificar código, traza la procedencia actual de:

```text
actionId
presenterLabel
subjectRef
markerRef
Evidence source/type
ActivitySourceRecord title
ActivitySourceRecord description
Activity projection visible to the user
```

para A y B.

Construye un mapa:

```text
SOURCE
→ CARRIED VALUE
→ CONSUMER
→ TRANSFORMATION
→ FACTUAL / OPERATIONAL / REPRESENTATIONAL
```

Inspecciona al menos:

```text
ScenarioDefinition
DemoScript
Public Action shape
EvidenceInput
MockDataAdapter.executeAction()
ActivitySourceRecord
projectSnapshot()
Activity read model / UI consumer
```

No refactorices durante esta inspección.

## 5. Guarda semántica

Preservar:

```text
Evidence
!=
Activity
```

```text
Activity
→ projection / representation
→ never factual authority
```

```text
action accepted
!=
human-readable description
```

```text
action affordance copy
!=
completed-action representation
```

No asumir que `presenterLabel` constituye automáticamente la narrativa correcta de Activity.

No utilizar Activity para reconstruir Evidence o K.

## 6. Fuente candidata

Después de la inspección, identifica si **alguna relación existente** transporta legítimamente suficiente contenido situado para construir la representación posterior de Activity.

Prioriza relaciones existentes.

No introduzcas previamente:

```text
ActivityPresentation
ActivityTemplate
NarrativeDescriptor
ContentRegistry
CopyRegistry
LocalizationEngine
PresentationEngine
```

o equivalentes.

Si ninguna relación existente puede transportar legítimamente la representación sin confundir:

```text
action affordance
factual Evidence
completed-action representation
```

detente antes de inventar una nueva.

Registra esa ausencia como evidencia de H24.

## 7. Delta permitido

Puede modificarse el recorrido mínimo entre la fuente situada existente que el experimento identifique y la materialización/proyección de Activity.

`MockDataAdapter` puede cambiar únicamente para dejar de decidir la narrativa específica jardín/fuente si existe una fuente legítima que ya la proporcione.

No modificar:

```text
H22 Experience selector

H23 situated context binding

evaluateJointAdmissibility()

evaluateCrossSubjectEvidenceSufficiency()

K

AuthoritativePremise semantics

Evidence attribution

GuestPerspective projection copy

App.tsx situated literals

Scenario/Experience semantics
```

No limpiar L3 ni L4.

## 8. Controles A y B

Ejecuta A y B con la misma secuencia:

```text
enlist P1
→ action A
→ activate P2
→ action B
```

Verifica que A conserva su representación situada esperada:

```text
jardín
fuente
```

y B produce la suya:

```text
mirador
patio
```

sin referencias cruzadas indebidas.

La comparación debe realizarse sobre la representación efectiva de Activity, no únicamente sobre los datos declarados del Script.

## 9. Invariantes factuales

Antes y después del cambio deben permanecer equivalentes para cada composición:

```text
Evidence IDs
subjectRefs
marker refs/types
booking/stay/property context
operational session
subject enablement
joint admissibility
K
claim
```

Una modificación de contenido situado no puede modificar ninguno de ellos.

## 10. Control adversarial de independencia representación/hecho

Crea un control exclusivamente de harness donde, manteniendo constantes:

```text
action semantics
subjectRef
markerRef
Evidence payload
context
evaluation
```

varíe únicamente la representación humana situada disponible para Activity, si la forma existente permite hacerlo legítimamente.

Debe observarse:

```text
factual/operational state
→ unchanged

evaluation
→ unchanged

Activity representation
→ changed
```

Este control debe falsar:

```text
representation text
=
factual identity
```

No registres el fixture adversarial como demo comercial.

Si la forma existente no permite variar representación sin variar la acción factual, documenta esa limitación y no inventes un nuevo contrato para conseguir el control.

## 11. Control de ausencia

Si la fuente situada elegida puede carecer de representación, comprueba qué hace el sistema.

No debe:

```text
inventar jardín/fuente por defecto
```

ni:

```text
cambiar Evidence
```

ni:

```text
cambiar K
```

No inventes una política productiva de fallback.

Si el sistema necesita una política nueva para expresar la ausencia:

```text
STOP
```

y registra la presión.

## 12. L3 y L4 permanecen fuera de alcance

Durante H24 esperamos que B pueda continuar mostrando en GuestPerspective:

```text
Lucía
jardín
fuente
```

Eso debe registrarse como:

```text
L3
→ PRESERVED / OUT OF SCOPE
```

No es falsador de H24.

`App.tsx` permanece sin cambios:

```text
L4
→ SOURCE-INSPECTION FINDING
→ OUT OF SCOPE
```

No renderices B con el propósito de arreglar App.

## 13. Falsadores H24

Clasifica H24 como FALSIFIED si:

```text
no existe una procedencia legítima
para la representación situada
sin introducir un nuevo contrato
```

o si:

```text
cambiar Activity representation
modifica Evidence, contexto,
atribución o evaluación
```

o si:

```text
runtime sigue necesitando inferir
jardín/fuente/mirador/patio
desde subjectRef, markerRef
o identidad concreta de Scenario
```

o si:

```text
A regression appears
```

No introduzcas una abstracción nueva para salvar la hipótesis.

Usa INCONCLUSIVE solo ante un impedimento externo al experimento.

## 14. Veredicto positivo

H24 puede clasificarse:

```text
SUPPORTED WITH QUALIFICATION
```

únicamente si se demuestra:

```text
A fact/action
→ A factual consequence
→ A situated Activity representation

B fact/action
→ B factual consequence
→ B situated Activity representation
```

usando la misma maquinaria y manteniendo:

```text
A/B Evidence
A/B context
A/B evaluation
```

independientes de su representación humana.

La cualificación debe indicar que esto no demuestra todavía:

```text
general content architecture
localization architecture
GuestPerspective content provenance
App rendering correctness
universal Activity representation
```

## 15. Verificación

Ejecuta:

```text
H24 focalized harness
H23 regression
H22 regression
H21 historical reproduction
Session 20 vertical regression
full suite
typecheck
lint
build
```

No necesitas navegador si Activity efectiva puede verificarse mediante snapshot público.

No modifiques la aceptación histórica de A.

## 16. Informe

Crear:

`session-24-situated-activity-representation-provenance.md`

con:

```text
H23 CONSOLIDATED INPUT

H24 HYPOTHESIS

VARIABLE UNDER TEST

ACTIVITY PROVENANCE MAP

FACTUAL / OPERATIONAL INPUT

REPRESENTATIONAL INPUT

CURRENT COUPLING

EXISTING SOURCE CANDIDATES

SELECTED EXPERIMENTAL SOURCE
or
NO LEGITIMATE EXISTING SOURCE

BASELINE

CODE DELTA

A CONTROL

B CONTROL

FACT / REPRESENTATION INDEPENDENCE CONTROL

ABSENCE CONTROL

EXECUTION TRACE

L5 RESULT

REGRESSIONS

L3 STATUS

L4 STATUS

FALSIFICATION ANALYSIS

H24 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

WHAT H24 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H25.

## 17. Guardas finales

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
accepted action
!=
situated representation
```

```text
action affordance
!=
completed-action representation
```

```text
representation provenance
!=
semantic authority
```

```text
copy reuse
!=
architectural reuse
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

No crear ADR ni arquitectura general de contenido.

Al terminar:

```text
H24
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L5
→ status

FACT / REPRESENTATION SEPARATION
→ supported / unsupported
   within tested scope

L3
→ preserved / out of scope

L4
→ preserved / source-inspection

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
