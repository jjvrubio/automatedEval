Abre la Sesión 22 a partir de los resultados consolidados de H21.

No intentes todavía completar Composition B ni reparar todos los leaks observados.

## 1. Línea de base

Mantener:

```text
SESSION 20
→ CLOSED
→ FIRST VERTICAL DEMO
→ EXECUTABLE WITH PRESENTATION GAPS

H21
→ FALSIFIED

H21 LAST SUCCESSFUL FACTORY BOUNDARY
→ manifest/artifacts
→ resolveDemo()
→ distinct ResolvedDemoRuntime
→ distinct provider instances
→ generic initial snapshots

H21 FIRST MATERIAL FALSIFIER
→ L2a:
   Family Adventure projections
   selected by Scenario A identity
```

Distinguir desde ahora:

```text
L2a
scenario.id → projection selection
→ EXECUTION-CONFIRMED

L2b
scenario.id → evaluation selection
→ SOURCE-INSPECTION FINDING
→ NOT YET EXECUTION-CONFIRMED
```

Mantener:

```text
L1 / L3 / L4 / L5
→ SOURCE-INSPECTION FINDINGS
```

salvo que Sesión 22 produzca evidencia ejecutable directa sobre alguno de ellos.

No reescribir H21 después de una eventual reparación.

H21 queda falsificada para su baseline congelada.

## 2. Hallazgo de H21 que gobierna esta sesión

La evidencia permite sostener, únicamente dentro del ámbito probado:

```text
Scenario-specific identity
!=
composition-stable selector
for shared Family Adventure behavior
```

No promover esta formulación a regla universal de dominio.

No crear ADR.

Architecture v0.5 permanece ACTIVE / unchanged.

## 3. Hipótesis H22

```text
H22 — Experience-Stable Behavior Selection
```

Hipótesis falsable:

```text
Dentro del alcance de Family Adventure,
dos composiciones que resuelven la misma
Experience pueden seleccionar el mismo
comportamiento ejecutable específico de
esa Experience mediante su relación
resuelta con la Experience,

sin utilizar la identidad particular
del Scenario como proxy de selección
y sin conceder ese comportamiento
a composiciones de otras Experiences.
```

La Experience compartida:

```text
experience:family-adventure@1
```

es un discriminante experimental candidato.

No asumir que:

```text
Experience = Behavior
```

ni que:

```text
one Experience → exactly one behavior
```

H22 no establece una arquitectura general de selección.

## 4. Inspección previa mínima

Antes de cambiar código, identifica exactamente qué referencia a Experience ya está disponible en:

```text
ResolvedDemoRuntime
Scenario / resolved artifacts
provider construction
MockDataAdapter construction
```

Determina cuál es la ruta mínima para que el punto donde hoy se utiliza:

```text
scenario.id === "family-adventure"
```

pueda discriminar Family Adventure mediante una referencia existente a su Experience.

Prioriza relaciones explícitas ya existentes.

No utilices heurísticas como:

```text
number of subjects
presence of P1/P2
presence of enlist
action IDs
checkpoint names
script shape
```

para inferir la Experience.

No inventes un concepto Behavior/Capability para hacer pasar la prueba.

## 5. Delta permitido

Esta sesión autoriza únicamente el cambio mínimo necesario para experimentar con la selección de comportamiento.

Puedes modificar:

```text
mock-adapter.ts
```

en los puntos que utilizan `scenario.id` como selector del comportamiento Family Adventure.

Si la referencia de Experience ya existe aguas arriba pero no llega al adaptador, puedes realizar el threading técnico mínimo de esa referencia existente hasta el adaptador.

Ese threading:

```text
must use an existing Experience reference
```

y no puede introducir:

```text
BehaviorRef
CapabilityRef
BehaviorProfile
ExperienceEngine
CapabilityRegistry
BehaviorRegistry
Strategy registry
plugin architecture
```

No modifiques el contrato semántico de Experience.

No modifiques `DemoProvider` salvo que resulte estrictamente inevitable para transportar una referencia ya existente; si exige cambiar su significado o introducir una nueva responsabilidad pública:

```text
STOP
```

y registra la falsación.

## 6. Componentes que permanecen congelados

No corrijas:

```text
vertical-evaluation.ts context constants
guest projection situated copy
App.tsx situated literals
Runtime Activity narrative
K
joint admissibility
authority premise semantics
Scenario/Script semantics
Evidence attribution
```

En particular:

```text
L1
L3
L4
L5
```

permanecen fuera de alcance.

No aproveches H22 para limpiar hardcoding.

## 7. Controles positivos

Conserva A y B con identidades distintas:

```text
A scenario.id
→ family-adventure

B scenario.id
→ family-adventure-costa
```

No igualarlas.

Comprueba:

```text
A Experience
==
B Experience
==
experience:family-adventure@1
```

Después verifica:

```text
A initial snapshot
→ Family Adventure guest perspective present
→ supervision perspective present

B initial snapshot
→ Family Adventure guest perspective present
→ supervision perspective present
```

Ambas deben utilizar la misma implementación compartida.

## 8. Controles negativos obligatorios

Utiliza al menos las demos existentes de otras Experiences, por ejemplo Retail y Hospitality Arrival cuando sean aplicables.

Comprueba que la modificación no produzca:

```text
unrelated Experience
→ Family Adventure guestPerspective
```

ni:

```text
unrelated Experience
→ Family Adventure supervisionPerspective
```

La ausencia de falsos positivos es condición necesaria.

No construyas una demo artificial exclusivamente para que el control negativo pase si las demos existentes permiten discriminarlo.

## 9. Comprueba también L2b

Si L2a queda superado, ejecuta B a través de las acciones existentes hasta disponer al menos de A@P1.

Verifica:

```text
B enlist
→ enabled
→ no Evidence
```

```text
B action A
→ A@P1 accepted
→ Family Adventure evaluation path invoked
```

El objetivo es comprobar que la selección del comportamiento no vuelve a depender de:

```text
scenario.id === "family-adventure"
```

en `executeAction()`.

Si es necesario sustituir el segundo gate L2b por el mismo discriminante experimental basado en Experience, hazlo dentro del delta autorizado.

No modifiques el evaluador.

No modifiques su contexto.

## 10. Si es observable, continúa únicamente para verificar selección

Puedes continuar:

```text
activate P2
→ B@P2
→ evaluation
```

si ello ayuda a demostrar que el comportamiento seleccionado continúa siendo el mismo.

Pero no interpretes:

```text
correct K result
```

como evidencia de integridad contextual.

L1 permanece una frontera separada.

## 11. Tratamiento de L1/L3/L4/L5 si aparecen

Si después de seleccionar correctamente el comportamiento B observas directamente:

```text
Aurora context in B evaluation
```

registra:

```text
L1
→ EXECUTION-CONFIRMED
```

solo si la ejecución proporciona evidencia directa de ello.

Si observas directamente:

```text
Lucía
jardín
fuente
Aurora
```

dentro de una perspectiva B:

registra el leak correspondiente como ejecución confirmada.

Pero:

```text
L1/L3/L4/L5
!=
falsification of H22
```

salvo que impidan observar la variable de selección.

No los repares.

No abstraigas.

## 12. STOP de H22

Detente ante el primer falsador material de H22, por ejemplo:

```text
Experience reference cannot discriminate
A/B from unrelated Experiences
```

o:

```text
using Experience selection
causes unrelated demos to receive
Family Adventure behavior
```

o:

```text
the existing Experience relationship
cannot reach the selection boundary
without introducing a new architectural/
semantic contract
```

o:

```text
A regression appears
```

No introduzcas una abstracción adicional para salvar la hipótesis.

## 13. Veredicto H22

Clasifica:

```text
H22 → SUPPORTED WITH QUALIFICATION
```

solo si:

```text
A and B
→ same Family Adventure behavior selected

Scenario IDs
→ remain different

unrelated Experiences
→ do not receive that behavior

A
→ no regression

projection selection
→ no longer requires Scenario A identity

evaluation selection
→ no longer requires Scenario A identity
```

La cualificación debe indicar expresamente que H22:

```text
does not prove general Experience→Behavior mapping
does not prove correct contextual binding
does not prove content transport
does not repair H21 historically
does not prove full Factory reuse
```

Clasifica:

```text
H22 → FALSIFIED
```

si el discriminante de Experience no puede sostener la selección dentro de estas condiciones.

Usa:

```text
H22 → INCONCLUSIVE
```

solo para un impedimento externo al experimento.

## 14. Verificación

Ejecuta:

```text
tests focalizados H22
regresión de H21
suite completa
typecheck
lint
build
```

Comprueba que A permanece aceptada.

No es necesaria aceptación manual del navegador para establecer esta hipótesis si la frontera puede verificarse íntegramente a través del provider/snapshot/evaluation públicos.

Si navegas B para observar contenido, clasifica esa evidencia aparte; no conviertas presentación en criterio principal de H22.

## 15. Documentación

Crear:

`session-22-experience-stable-behavior-selection.md`

Documentar explícitamente:

```text
H21 CONSOLIDATED INPUT

H22 HYPOTHESIS

VARIABLE UNDER TEST

CONTROLLED VARIABLES

EXPERIMENTAL SELECTOR CANDIDATE

WHY EXPERIENCE IS TESTED

WHAT EXPERIENCE DOES NOT MEAN

BASELINE

CODE DELTA

POSITIVE CONTROLS

NEGATIVE CONTROLS

L2a RESULT

L2b RESULT

EXECUTION TRACE

REGRESSIONS

OUT-OF-SCOPE LEAKS OBSERVED

H22 FALSIFICATION ANALYSIS

H22 VERDICT

ARCHITECTURAL CONSEQUENCE

WHAT H22 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H23.

## 16. Guardas finales

Preservar:

```text
Composition
!=
Runtime State
!=
Derived Evaluation
!=
Read Model
!=
UI Local State
```

```text
Scenario identity
!=
semantic authority
```

```text
Experience reference
!=
Behavior ontology
```

```text
selector experimental
!=
arquitectura promovida
```

```text
successful reuse
!=
general Factory architecture
```

Mantener:

```text
TES → unchanged
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED
Product Semantic Contract → unchanged
PSC-P01 → unchanged
PSC-P02 → NOT CREATED
Group → NOT INTRODUCED
```

Al final entrega:

```text
H22
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L2a
→ status

L2b
→ status

EXPERIENCE AS LOCAL SELECTOR
→ supported / unsupported
   within tested scope

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
