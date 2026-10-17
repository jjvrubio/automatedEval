Continúa la Sesión 21 a partir de:

`session-21-composition-boundary-factory-reusability-audit.md`

La auditoría y el protocolo H21 están aprobados como baseline de trabajo.

No abras Sesión 22.

El estado actual es:

```text id="ketc3s"
SESSION 20 → CLOSED
FIRST VERTICAL A → ACCEPTED REFERENCE

SESSION 21 AUDIT → COMPLETED

H21 → FORMULATED
      NOT TESTED
      NOT CONSOLIDATED

COMPOSITION B → NOT IMPLEMENTED
```

Ahora debes **ejecutar H21 contra la baseline congelada**.

La segunda composición B es un instrumento de falsación arquitectónica, no un objetivo de producto.

## 1. Preserva la baseline congelada

No modifiques antes del ensayo:

```text id="a0w6wb"
prototype/src/demo/mock-adapter.ts
prototype/src/demo-factory/contracts.ts
prototype/src/demo-factory/vertical-evaluation.ts
prototype/src/demo-factory/cross-subject-evidence-admissibility.ts
prototype/src/demo-factory/evidence-sufficiency.ts
prototype/src/app/App.tsx
prototype/src/styles/global.css
prototype/src/main.tsx
```

ni el comportamiento compartido de bootstrap/resolution.

No extraigas literales de estos archivos para hacer pasar B antes del experimento.

No refactorices previamente L1–L5.

Las fugas L1–L5 son hallazgos de inspección, todavía no reparaciones autorizadas.

## 2. Construye Composition B únicamente mediante las superficies permitidas en el protocolo

Puedes añadir:

```text id="o79gvo"
manifest B
brand artifact B
fixture B
ScenarioDefinition B
DemoScript B
registro de B en los catálogos existentes
activo local necesario de branding
test/harness experimental H21
```

Utiliza los valores documentados en el protocolo, o equivalentes estrictamente situados:

```text id="nejo3f"
Costa Clara Resort
Inés
Mateo
property B
booking/stay B
mirador
patio
```

Mantén:

```text id="oltx8h"
Experience → same
P1/P2 → individual subjects
operational session → P1
enlist semantics → same
activate P2 semantics → same
Evidence A/B/C → same criterion role
A@P1 → same attribution
B@P2 → same attribution
K = A AND (B OR C)
authority requirement → same
evaluators → same
perspectives → same
actionIds/checkpoints → same
```

No utilices el `scenario.id` de A para evitar el gate detectado en L2.

B debe conservar una identidad situada distinta, como:

```text id="a44icv"
family-adventure-costa
```

Si esto revela una dependencia compartida, esa dependencia es evidencia del experimento.

## 3. Ejecuta el ensayo incrementalmente

Primero verifica únicamente:

```text id="z0j6eq"
Composition A resolves
Composition B resolves
ResolvedDemoRuntime A != B
brand/context/fixture refs A != B
Experience A == Experience B
```

Después intenta instanciar los providers y obtener sus snapshots iniciales.

Después intenta recorrer B con la misma secuencia funcional de A:

```text id="gtnhlx"
initial
→ enlist P1
→ A@P1
→ activate P2
→ B@P2
→ joint admissibility
→ K
→ claim
→ guest/supervision projections
```

Si llega suficientemente lejos, ejecuta también los controles de aislamiento A/B documentados:

```text id="t0lb32"
action A does not mutate B
action B does not mutate A
Evidence A does not appear in B
Evidence B does not appear in A
reset A does not reset B
reset B does not reset A
```

y verifica ausencia de contaminación de contenido/contexto.

## 4. STOP en el primer falsador arquitectónico material

Si para conseguir que B continúe necesitas modificar cualquiera de los componentes compartidos congelados:

```text id="46kuxe"
STOP
```

No hagas la modificación.

No abstraigas.

No crees una solución.

Conserva el estado del experimento exactamente en el punto de fallo.

Registra:

```text id="q22z2n"
input/action
expected behavior
observed behavior

last successful boundary

first failing boundary

file / responsibility
that would require modification

why the modification
would be necessary

which audit finding
L1–L5 it confirms,
if applicable
```

Especialmente, si el primer bloqueo es:

```text id="dh6mp5"
scenario.id B
→ shared runtime does not select
   Family Adventure evaluation/projections
```

no reutilices el `scenario.id` de A y no cambies el gate.

Regístralo como evidencia de L2.

## 5. No intentes demostrar todos L1–L5 en una sola ejecución

H21 necesita un primer falsador material para quedar refutada.

Si L2 impide llegar a L1/L3/L4/L5:

```text id="fzq5ye"
L2
→ EXECUTION-CONFIRMED
```

pero:

```text id="p19n9i"
L1/L3/L4/L5
→ SOURCE-INSPECTION FINDINGS
→ NOT EXECUTION-CONFIRMED BY H21
```

salvo que hayan sido efectivamente observados antes del STOP.

No repares L2 para continuar buscando el siguiente fallo dentro de la misma baseline.

Una reparación produciría una nueva baseline y requeriría otro experimento.

## 6. Clasifica H21

Usa únicamente:

```text id="wnr0bz"
SUPPORTED WITH QUALIFICATION
```

si B completa el pipeline congelado, utiliza su propio contexto y contenido, mantiene aislamiento A/B y no exige cambios compartidos.

Usa:

```text id="tjvteg"
FALSIFIED
```

si una diferencia legítimamente situada de B exige modificar runtime, integración de evaluación, proyección o pantallas compartidas.

Usa:

```text id="fhw75p"
INCONCLUSIVE
```

solo si un problema externo al objeto experimental impide ejecutar el ensayo.

No utilices resolución correcta del manifest, compilación o branding correcto como `PARTIAL PASS` de H21. Pueden registrarse como evidencia de fronteras que sí funcionaron, pero H21 pregunta por el pipeline completo.

## 7. Preserva las distinciones arquitectónicas

Durante todo el ensayo:

```text id="cfhwpm"
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

No conviertas:

```text id="1qnd2d"
Evidence
K
claim
admissibility
subject enablement actual
```

en configuración.

No introduzcas:

```text id="zxuz9w"
DemoTemplate
DemoTenant
ClientConfiguration
CapabilityRegistry
BehaviorRegistry
UniversalRenderer
VerticalEngine
ExperienceEngine
PerspectiveRegistry
FactoryEngine
plugin architecture
```

ni equivalentes.

No modifiques TES, Product Semantic Contract, PSC-P01, Architecture v0.5 ni ADR-001–005.

No crees PSC-P02 ni un nuevo ADR.

## 8. Actualiza el informe de Sesión 21

Actualiza:

`session-21-composition-boundary-factory-reusability-audit.md`

o crea su consolidación de ejecución siguiendo la convención documental existente.

Añade explícitamente:

```text id="t4y4ke"
EXPERIMENT EXECUTION

BASELINE HASH / SHARED FILES FROZEN

COMPOSITION B CREATED

RESOLUTION RESULT A/B

LAST SUCCESSFUL BOUNDARY

FIRST FAILING BOUNDARY

OBSERVED EXECUTION TRACE

A/B ISOLATION RESULT
(si se alcanzó)

CONTEXT INTEGRITY RESULT
(si se alcanzó)

CONTENT LEAKAGE RESULT
(si se alcanzó)

AUDIT FINDINGS CONFIRMED BY EXECUTION

AUDIT FINDINGS STILL INSPECTION-ONLY

FALSIFICATION ANALYSIS

H21 VERDICT

ARCHITECTURAL CONSEQUENCE

WHAT H21 DOES NOT PROVE

REMAINING PRESSURES
```

Si H21 es falsificada, no revises Architecture v0.5 automáticamente.

Registra únicamente la responsabilidad observada que impide la reutilización.

## 9. No selecciones ni implementes H22

Al final puedes enumerar las incertidumbres residuales que la evidencia deja abiertas, pero no elijas automáticamente una solución ni una nueva arquitectura.

En particular, si L2 es el primer falsador, registra la posible frontera:

```text id="vrw4xv"
Scenario identity
!=
execution behavior selection
```

como **candidata a revisión**, no como hallazgo consolidado hasta evaluar el resultado completo.

El objetivo de esta ejecución es obtener evidencia sobre H21, no arreglar la Demo Factory.

Entrega al final:

```text id="un75ik"
H21
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

FIRST MATERIAL FALSIFIER
→ ...

LAST SUCCESSFUL FACTORY BOUNDARY
→ ...

ARCHITECTURE v0.5
→ ACTIVE / unchanged pending review

NEXT FRONTIER
→ NOT SELECTED
```
