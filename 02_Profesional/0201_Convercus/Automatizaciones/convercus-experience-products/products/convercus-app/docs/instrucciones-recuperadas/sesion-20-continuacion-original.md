Continúa el proyecto existente `Convercus Demo Factory / Convercus Experience Products` en el repositorio:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

Trabaja sobre el estado actual del repositorio. No empieces desde cero y no abras la Sesión 21.

La instrucción de continuidad que te he proporcionado es la especificación autoritativa para esta corrección.

Tu tarea ahora es ejecutar la corrección de la Sesión 20.

Debes proceder en este orden:

1. Inspecciona el código actual y diagnostica por qué la demo representa actualmente algo equivalente a:

```text
inicio
→ active
→ pista ya disponible
```

y por qué la operación sobre P2 se presenta o implementa como si fuera alta/creación de un segundo huésped.

Determina concretamente si el problema está en:

```text
ScenarioDefinition
DemoScript
Public Action
Runtime transition
MockDataAdapter
GuestPerspectiveReadModel
SupervisionPerspectiveReadModel
UI
fixtures
action availability
```

o en una combinación de ellos.

No corrijas únicamente el copy si el flujo subyacente es incorrecto.

2. Implementa la corrección mínima necesaria para que el recorrido sea:

```text
P1 ya existe
        ↓
P1 se alista en la Experience
        ↓
P1 queda habilitado
        ↓
todavía no existe Evidence
        ↓
P1 realiza una acción de Experience
        ↓
Evidence A@P1
        ↓
P1 activa P2 desde la misma cuenta/sesión
        ↓
P2, que ya existía, queda habilitado
        ↓
activar P2 no produce Evidence
        ↓
P2 realiza una acción de Experience
        ↓
Evidence B@P2
        ↓
evaluateJointAdmissibility()
        ↓
K = A AND (B OR C)
        ↓
afirmación derivada
        ↓
guest projection + supervision projection
```

3. Preserva obligatoriamente estas invariantes:

```text
P1 activa P2
!=
P1 crea P2
```

```text
P1 + P2
!=
Group
```

```text
alistamiento P1
!=
Evidence
```

```text
activación P2
!=
Evidence
```

```text
cuenta/sesión operativa
!=
subjectRef de Evidence
```

```text
estado operativo
!=
modelo de lectura
!=
estado local de interfaz
```

```text
distintas perspectivas
!=
distintas fuentes de verdad
```

No introduzcas:

```text
Group
FamilyGroup
GroupMembership
CollectiveParticipation
Participant
Contributor
Membership
Enrollment como contrato productivo
Actor
Operator
Representative
TES Event
TES Progression
TES Result
PerspectiveRegistry
RoleBasedProjectionEngine
```

ni arquitectura equivalente.

4. P1 y P2 deben existir desde el estado inicial.

La diferencia inicial debe ser aproximadamente:

```text
P1
→ exists
→ not enlisted

P2
→ exists
→ not enabled

Evidence
→ none
```

P2 no debe ser creado durante el recorrido.

5. El alistamiento de P1 debe atravesar:

```text
UI
→ Public Action
→ Runtime
```

React no debe modificar directamente el estado.

Después del alistamiento debe poder existir explícitamente este estado:

```text
P1 enlisted/enabled
P2 not enabled
Evidence = []
```

6. La activación de P2 debe realizarse desde la cuenta/sesión de P1.

Después de esa acción debe poder existir explícitamente este estado:

```text
P1 enabled
P2 enabled
Evidence = []
```

o, si A ya se produjo:

```text
P1 enabled
P2 enabled
Evidence = [A@P1]
```

En ningún caso la activación debe crear automáticamente B@P2.

7. Las acciones de Experience deben estar separadas de Evidence.

La interfaz del huésped debe utilizar acciones situadas y comprensibles, no términos técnicos como:

```text
Evidence A
markerRef
subjectRef
```

Una acción de P1 produce A@P1.

Una acción representada como atribuible a P2 produce B@P2.

Aunque ambas acciones se operen desde la misma sesión de P1:

```text
acción operada desde cuenta P1
!=
subjectRef de Evidence
```

8. Conserva sin modificar la lógica ya validada de Sesión 17:

```text
evaluateJointAdmissibility()
evaluateCrossSubjectEvidenceSufficiency()
K = A AND (B OR C)
```

Mantén también el control negativo:

```text
B + C
→ not-established
```

Dos sujetos habilitados no deben contar como dos Evidence ni producir suficiencia.

9. Actualiza las dos proyecciones desde el mismo Runtime State.

La perspectiva de huésped debe mostrar de forma comprensible:

```text
Experience disponible
→ Alistarme
→ alistado
→ acción de P1
→ pista encontrada/aportada
→ activar P2
→ P2 habilitado
→ acción atribuida a P2
→ resultado
```

La perspectiva de supervisión debe permitir observar al menos:

```text
P1 exists
P1 enlisted/enabled
Evidence de P1

P2 exists
P2 enabled/not enabled
Evidence de P2

joint admissibility
K
derived claim
```

Ninguna UI debe recalcular K, admisibilidad o suficiencia.

10. Añade o adapta pruebas para verificar expresamente:

```text
P1 not enlisted
→ no Evidence
```

```text
P1 enlist
→ enabled
→ no Evidence
```

```text
P1 action
→ A@P1
```

```text
P2 not enabled
→ no B@P2
```

```text
P1 activates P2
→ P2 enabled
→ no nueva Evidence
```

```text
P2 action
→ B@P2
```

```text
A@P1 + B@P2
→ joint admissibility established
→ K established
```

```text
B + C
→ K not established
```

```text
same Runtime State
→ guest projection
→ supervision projection
```

y reset:

```text
P1 → not enlisted
P2 → not enabled
Evidence → none
sufficiency → not produced
```

11. Ejecuta después:

```text
tests focalizados
suite completa
typecheck
lint
build
```

Indica resultados concretos.

12. Después realiza obligatoriamente la aceptación manual en navegador desde estado limpio.

No des por aceptada la demo solo porque los tests sean verdes.

Verifica de forma manual las 22 transiciones indicadas en la instrucción de continuidad, prestando especial atención a estos tres estados:

```text
P1 alistado
+
0 Evidence
```

```text
P2 habilitado
+
0 Evidence atribuida a P2
```

y:

```text
misma cuenta/sesión
+
Evidence A@P1
+
Evidence B@P2
```

Si alguno de ellos no puede observarse o comprenderse desde la demo, clasifica:

```text
MANUAL BROWSER ACCEPTANCE → FAIL
```

y corrígelo antes de cerrar.

13. Actualiza:

`session-20-first-family-adventure-vertical.md`

con las secciones solicitadas en la instrucción:

* Specification misunderstanding found
* Subject existence
* Enlistment
* P2 activation
* Evidence contribution
* Attribution
* Multiple perspectives
* Semantic observations
* Manual browser acceptance
* Revised verdict

El informe anterior que declara `MANUAL BROWSER ACCEPTANCE → PASS` y `FIRST VERTICAL DEMO → EXECUTABLE WITH PRESENTATION GAPS` debe considerarse superado por la observación manual posterior hasta que esta corrección sea realmente aceptada.

14. Al final entrégame un informe breve pero concreto con:

```text
ROOT CAUSE

FILES CHANGED

BEHAVIOR BEFORE

BEHAVIOR AFTER

TEST RESULTS

MANUAL BROWSER ACCEPTANCE

SEMANTIC OBSERVATIONS

ARCHITECTURAL IMPACT

SESSION 20 REVISED VERDICT
```

No abras Sesión 21.

No modifiques TES.

No modifiques Architecture v0.5.

No crees ADR.

No modifiques el Product Semantic Contract.

No crees PSC-P02.

No promociones los artefactos experimentales.

Si la corrección y la aceptación manual pasan, el máximo veredicto permitido por ahora es:

```text
FIRST VERTICAL DEMO
→ EXECUTABLE WITH PRESENTATION GAPS
```
