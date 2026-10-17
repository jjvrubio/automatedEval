He revisado tu informe `session-20-first-family-adventure-vertical.md` v1.2 y tu propuesta posterior de crear una segunda demo.

La dirección de utilizar una segunda demo es válida, pero antes quiero cerrar formalmente Sesión 20 y después utilizar esa segunda composición como un **experimento arquitectónico**, no simplemente como white-labeling.

## 1. Cierre de Sesión 20

La checklist original de 22 transiciones que indicabas como no disponible es esta:

```text
1. abrir la demo;

2. P1 existe como sujeto/huésped;

3. P2 existe como segundo sujeto disponible
   en el contexto, aunque todavía no esté
   habilitado en la Experience;

4. P1 todavía no está alistado;

5. P1 pulsa “Alistarme”;

6. se observa un cambio perceptible;

7. no existe todavía Evidence A;

8. aparece una acción comprensible
   de Experience para P1;

9. P1 ejecuta esa acción;

10. aparece Evidence A@P1;

11. desde la misma cuenta/sesión aparece
    la posibilidad de activar P2;

12. P1 activa P2;

13. P2 queda habilitado;

14. activar P2 no produce Evidence;

15. aparece una acción atribuible a P2;

16. se ejecuta esa acción;

17. aparece Evidence B@P2;

18. se evalúa la admisibilidad conjunta;

19. se aplica K;

20. se produce la afirmación derivada;

21. perspectiva del huésped y perspectiva
    de supervisión se actualizan coherentemente;

22. el reset devuelve la demo al estado inicial.
```

Coteja explícitamente el recorrido ya implementado contra esta lista exacta.

Si la evidencia de navegador existente es suficiente, puedes reutilizarla; si algún punto no está demostrado inequívocamente, vuelve a recorrerlo.

Actualiza el informe de Sesión 20 con el resultado exacto.

No abras Sesión 21 hasta completar este cierre.

---

## 2. Después, no implementes inmediatamente la segunda demo

Quiero primero un **architecture/configuration audit** de Aventura Familiar.

La pregunta que queremos estudiar ya no es:

```text
¿podemos cambiar Aurora Stay por otro resort?
```

sino:

```text
¿dónde termina una Demo Definition /
Composition y dónde empieza la maquinaria
compartida capaz de ejecutarla?
```

Analiza todas las dependencias específicas de Aventura Familiar, incluyendo:

```text
Aurora Stay
Lucía
nombres visibles P1/P2
property/stay/booking refs
Aventura Familiar
pistas y copy
labels de acciones
operationalSessionSubjectRef
DemoEnableAction
DemoSubjectState
guest projection
supervision projection
UI específica
styles específicos
```

Para cada una indica:

```text
CURRENT LOCATION
CURRENT RESPONSIBILITY
EXPECTED RESPONSIBILITY
IS SITUATED DATA?
IS RUNTIME STATE?
IS DERIVED RESULT?
IS PRESENTATION?
IS REAL ARCHITECTURAL LEAK?
```

No confundas:

```text
dato específico visible
!=
hardcoded architectural dependency
```

Que “Lucía” llegue a una proyección puede ser correcto si procede del Scenario/fixture.

Lo que queremos detectar son dependencias como:

```text
App.tsx → conoce directamente Aurora Stay
MockDataAdapter → conoce directamente un cliente
projection logic → contiene decisiones exclusivas del resort
shared contract → contiene accidentalmente una necesidad
               exclusiva de Aventura Familiar
```

---

## 3. Conserva especialmente esta separación

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

No conviertas todo lo específico en configuration.

Ejemplo:

```text
nombre/imagen/copy de una pista
→ puede ser composition/content
```

pero:

```text
A@P1 existe
→ Runtime factual Evidence
```

y:

```text
K established
→ derived evaluation
```

No pueden convertirse en configuration para facilitar una segunda demo.

---

## 4. Después del audit, formula H21

Quiero utilizar provisionalmente esta frontera:

```text
H21 — Composition Boundary / Factory Reusability
```

Hipótesis provisional:

```text
Una segunda composición de demostración
que reutiliza la misma Experience y las
mismas invariantes de interacción puede
resolverse y ejecutarse mediante el mismo
pipeline compartido,

sin modificar runtime compartido,
evaluadores, lógica compartida de
proyección ni componentes compartidos
de pantalla,

cuando las diferencias pertenecen
legítimamente a Composition,
ScenarioDefinition,
DemoScript,
fixtures,
branding
o contenido situado.
```

No consolides H21 antes de experimentar.

---

## 5. La segunda demo será el falsador de H21

Mantén constantes:

```text
Experience
semántica de interacción
P1/P2 individuales
alistamiento P1
activación P2 desde sesión P1
Evidence A/B/C
K = A AND (B OR C)
evaluadores
runtime semantics
guest/supervision perspectives
```

Varía únicamente elementos legítimamente situados:

```text
brand
resort/property
display names
fixture refs
situated copy
presentation de pistas
```

El objetivo NO es construir dos demos.

El objetivo es comprobar:

```text
Composition A ─┐
               │
               ▼
       SAME SHARED PIPELINE
               │
               ├→ Runtime
               ├→ Evaluation
               ├→ Read Models
               └→ Presentation
               │
Composition B ─┘
```

---

## 6. Condición experimental fuerte

Intenta incorporar B sin modificar comportamiento compartido en:

```text
MockDataAdapter
DemoProvider
evaluateJointAdmissibility()
evaluateCrossSubjectEvidenceSufficiency()
shared projection machinery
shared screen components
```

Naturalmente puedes añadir o modificar:

```text
manifest
brand artifact
fixture
ScenarioDefinition
DemoScript
situated presentation data
registration
```

cuando pertenezcan legítimamente a la nueva composición.

Si la demo B exige cambiar un componente compartido:

```text
STOP BEFORE ABSTRACTING
```

No soluciones inmediatamente el problema.

Documenta:

```text
qué necesita cambiar
por qué
qué responsabilidad específica se filtró
qué frontera arquitectónica queda presionada
```

Eso será evidencia de H21.

No crees automáticamente:

```text
DemoTemplate
DemoTenant
ClientConfiguration
UniversalRenderer
VerticalEngine
ExperienceEngine
PerspectiveRegistry
FactoryEngine
plugin architecture
```

ni equivalentes.

---

## 7. Todavía no construyas el catálogo/selector

Primero prueba A y B mediante el mecanismo actual de resolución, por ejemplo sus IDs/query parameter si es suficiente.

Comprueba:

```text
composition A != composition B

runtime state A != runtime state B

state A does not leak into B

content A does not leak into B

reset A does not mutate B

both use the same execution machinery
```

El catálogo será una superficie posterior, no evidencia de arquitectura.

---

## 8. Salida que quiero antes de una refactorización

Devuélveme:

```text
SESSION 20 FINAL STATUS

EXACT 22-STEP ACCEPTANCE RESULT

CURRENT FACTORY PIPELINE

DEPENDENCY MAP

CONFIGURATION / RESPONSIBILITY MATRIX

LEGITIMATE SITUATED DATA

RUNTIME-SPECIFIC DATA

DERIVED DATA

ARCHITECTURAL LEAKS FOUND

LOCAL EXPERIMENTAL SHAPES
that recur or do not recur

H21 FINAL FORMULATION

CONTROLLED VARIABLES

VARIABLES CHANGED FOR COMPOSITION B

FILES EXPECTED TO CHANGE

FILES EXPECTED NOT TO CHANGE

FALSIFICATION CONDITIONS

STOP CONDITIONS
```

No hagas una refactorización arquitectónica amplia antes de devolver este análisis.

Preserva:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED
TES → unchanged
Product Semantic Contract → unchanged
PSC-P01 → unchanged
Group → NOT INTRODUCED
PSC-P02 → NOT CREATED
```
