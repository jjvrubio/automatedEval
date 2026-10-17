Abre la Sesión 23 a partir del resultado consolidado de H22.

No corrijas todavía L3, L4 ni L5.

## 1. Línea de base

Mantener:

```text
SESSION 20
→ CLOSED

H21
→ FALSIFIED for historical baseline

H22
→ SUPPORTED WITH QUALIFICATION

L2a
→ Experience-based selection
→ EXECUTION-VERIFIED

L2b
→ Experience-based selection
→ EXECUTION-VERIFIED

L1
→ EXECUTION-CONFIRMED

L3
→ EXECUTION-CONFIRMED

L5
→ EXECUTION-CONFIRMED

L4
→ SOURCE-INSPECTION FINDING
```

No modificar retrospectivamente H21 ni H22.

Mantener el selector experimental de H22:

```text
scenario.experienceRef
===
"experience:family-adventure@1"
```

sin promoverlo a arquitectura general.

---

## 2. Presión seleccionada

La siguiente frontera es exclusivamente:

```text
L1 — situated evaluation context binding
```

La ejecución H22 demuestra:

```text
Composition B
→ Costa Clara context

Evidence payload B
→ Costa Clara context

vertical evaluation receives B Evidence

BUT

nested joint evaluation
→ Aurora context
```

Por tanto:

```text
situated runtime context
!=
evaluation context currently applied
```

No selecciones todavía problemas de copy/presentation.

---

## 3. Guarda epistemológica obligatoria

Preservar especialmente:

```text
Evidence factual context
!=
evaluation authority
```

```text
subjectRef
!=
evaluation scope
```

```text
shared booking/stay/property
!=
authority by itself
```

```text
context equality
!=
semantic authority
```

PSC-P01 permanece:

```text
OPEN / EVIDENCE-BACKED PRESSURE
```

sin modificación.

No crear PSC-P02.

No promover:

```text
EvaluationScope
ContextScope
ParticipationScope
ContextAuthority
```

o equivalentes.

---

## 4. H23

```text
H23 — Situated Evaluation Context Binding
```

Hipótesis falsable:

```text
Dentro del recorrido Family Adventure,
la maquinaria compartida de evaluación puede
recibir el contexto situado correspondiente
a la composición que está siendo ejecutada,

preservando las referencias factuales
de la Evidence y la premisa autoritativa
experimental existente,

sin sustituirlas por constantes
de otra composición y sin inferir
autoridad de evaluación únicamente
a partir de la Evidence.
```

No asumir todavía cuál debe ser la forma productiva de este binding.

---

## 5. Inspección previa

Antes de modificar código, identifica exactamente:

```text
qué contexto declara Scenario A/B

qué contexto lleva EvidenceInput A/B

qué contexto recibe evaluateVerticalEvidence()

qué contexto construye toCrossSubjectEvidence()

qué contexto recibe evaluateJointAdmissibility()

qué contexto utiliza la premisa experimental

qué contexto llega a
evaluateCrossSubjectEvidenceSufficiency()
```

Construye una tabla:

```text
SOURCE
VALUE A
VALUE B
AUTHORITY / ROLE
CURRENT CONSUMER
CURRENT TRANSFORMATION
```

Distinguir:

```text
declared situated context
runtime factual context
evaluation input context
authoritative premise applicability
derived result
```

No refactorices durante esta inspección.

---

## 6. Selección de la fuente experimental

Después de inspeccionar las relaciones existentes, utiliza la ruta mínima explícita que permita transportar el contexto situado aplicable.

Prioriza información ya disponible en:

```text
ScenarioDefinition
EvidenceInput.contexts
ResolvedDemoRuntime
existing experimental evaluation context
```

No añadas automáticamente un nuevo contrato.

Si ninguna relación existente permite distinguir legítimamente:

```text
factual context
from
evaluation-applicable context
```

sin inventar autoridad:

```text
STOP
H23 → FALSIFIED or INCONCLUSIVE
```

según la causa.

Documenta la carencia.

No inventes `EvaluationContextBinding` para salvar la hipótesis.

---

## 7. Delta permitido

Puede modificarse:

```text
vertical-evaluation.ts
```

y únicamente el threading técnico mínimo estrictamente necesario desde una relación existente para eliminar las constantes situadas de Aurora.

Puede modificarse la llamada desde:

```text
mock-adapter.ts
```

solo si es necesario proporcionar a la integración una referencia situada ya existente.

No modificar:

```text
evaluateJointAdmissibility()
evaluateCrossSubjectEvidenceSufficiency()
K
AuthoritativePremise semantics
coveredSubjectRefs semantics
guest projection copy
App.tsx
Activity narrative
Scenario/Script semantics
Experience selector H22
```

No limpiar L3/L4/L5.

---

## 8. Control positivo A

Ejecutar A:

```text
A@P1
→ evaluation
```

y verificar que el input factual/contextual utilizado corresponde exclusivamente a:

```text
Aurora
AS-8842
stay-AS-8842
aurora-resort
```

Después:

```text
A@P1 + B@P2
→ joint admissibility
→ K established
```

sin regresión respecto de Sesión 20/H22.

---

## 9. Control positivo B

Ejecutar B:

```text
Costa Clara
CC-205
stay-CC-205
costa-clara-resort
```

hasta:

```text
A@P1
```

y después:

```text
A@P1 + B@P2
```

Verificar que las llamadas reales de evaluación contienen el contexto B aplicable y:

```text
NO:
aurora-resort
AS-8842
stay-AS-8842
```

dentro de la evaluación de B.

No basta con comprobar el payload original.

Debe observarse la entrada efectiva al evaluador conjunto.

---

## 10. Control de separación A/B

Comprobar:

```text
Evaluation A
→ no Costa Clara refs
```

```text
Evaluation B
→ no Aurora refs
```

La maquinaria sigue siendo compartida.

No duplicar evaluator ni crear wrapper específico B.

---

## 11. Control adversarial de incoherencia

Añade un fixture/harness experimental adversarial, sin convertirlo en demo comercial, donde exista deliberadamente una discrepancia entre:

```text
Scenario situated context
```

y:

```text
EvidenceInput.contexts
```

por ejemplo:

```text
Scenario
→ CC-205

Evidence
→ AS-8842
```

o discrepancia equivalente suficientemente discriminante.

El objetivo NO es decidir todavía cuál gana.

El objetivo es falsar:

```text
Evidence context
→ automatic evaluation authority
```

No debe ocurrir una normalización silenciosa como:

```text
mismatch
→ arbitrarily choose Evidence
→ evaluate as established
```

ni:

```text
mismatch
→ arbitrarily choose Scenario
→ silently rewrite Evidence
```

El resultado aceptable puede ser un rechazo controlado o:

```text
cannot-currently-establish
```

según la forma actual de los contratos.

No introduzcas nueva semántica únicamente para producir ese outcome.

Si el sistema actual no puede expresar la discrepancia sin inventar una autoridad nueva:

```text
STOP
```

y regístralo como evidencia.

---

## 12. Premisa autoritativa

La premisa experimental de H17 debe permanecer condición separada.

Preservar:

```text
correct contextual binding
+
no applicable authoritative premise
!=
joint admissibility established
```

Si es viable dentro del harness actual, añade un control donde el contexto factual sea correcto pero la premisa no cubra los sujetos/contexto requerido.

Debe permanecer:

```text
cannot-currently-establish
```

No conviertas la correspondencia contextual en sustituto de autoridad.

---

## 13. H23 no estudia copy

Durante la ejecución pueden seguir apareciendo:

```text
Lucía
jardín
fuente
Aurora
```

en guest projection, Activity o App.

Registrar esos resultados bajo:

```text
L3/L4/L5
→ preserved / out of scope
```

No corregirlos.

No son falsadores de H23 salvo que impidan observar la integridad contextual de evaluación.

---

## 14. Falsadores H23

H23 queda falsificada si:

```text
B cannot reach evaluation with B context
without introducing a new semantic/
architectural concept
```

o:

```text
evaluation still silently substitutes
Aurora context
```

o:

```text
context mismatch is accepted by treating
Evidence context as automatic authority
```

o:

```text
A regression appears
```

o:

```text
fix requires modifying H17 evaluators
or K
```

Usar:

```text
INCONCLUSIVE
```

solo ante impedimento externo al objeto experimental.

---

## 15. Resultado esperado si H23 se sostiene

Para A:

```text
A runtime Evidence
→ A situated evaluation input
→ existing premise check
→ existing K
```

Para B:

```text
B runtime Evidence
→ B situated evaluation input
→ existing premise check
→ existing K
```

Y:

```text
A context != B context
```

sin duplicar maquinaria.

Esto no implica:

```text
context
→ authority
```

---

## 16. Verificación

Ejecutar:

```text
H23 focalized tests
H22 regression
H21 historical reproduction
Session 20 vertical regression
full suite
typecheck
lint
build
```

Registrar resultados exactos.

No es necesaria aceptación manual de navegador para H23 si las entradas efectivas de evaluación pueden observarse mediante el harness y los snapshots públicos.

---

## 17. Informe

Crear:

`session-23-situated-evaluation-context-binding.md`

con:

```text
H22 CONSOLIDATED INPUT

H23 HYPOTHESIS

VARIABLE UNDER TEST

CONTEXT PROVENANCE MAP

FACTUAL CONTEXT

EVALUATION CONTEXT

AUTHORITATIVE PREMISE

BASELINE

CODE DELTA

A CONTROL

B CONTROL

A/B CONTEXT SEPARATION

ADVERSARIAL MISMATCH CONTROL

AUTHORITY-SEPARATION CONTROL

EXECUTION TRACE

L1 RESULT

REGRESSIONS

OUT-OF-SCOPE LEAKS

FALSIFICATION ANALYSIS

H23 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

WHAT H23 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H24.

---

## 18. Guardas

Mantener:

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
Evidence factual context
!=
evaluation authority
```

```text
context correspondence
!=
admissibility
```

```text
admissibility
!=
sufficiency
```

```text
binding mechanism
!=
new semantic ontology
```

```text
experimental context transport
!=
Product Semantic Contract refinement
```

No modificar:

```text
TES
Architecture v0.5
ADR-001–005
Product Semantic Contract
PSC-P01
```

No crear:

```text
PSC-P02
Group
EvaluationScope
ContextAuthority
ContextBinding service
ScopeResolver
```

o equivalentes.

Al terminar:

```text
H23
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L1
→ status

CONTEXT BINDING
→ supported / unsupported
   within tested scope

AUTHORITY SEPARATION
→ preserved / violated / unresolved

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
