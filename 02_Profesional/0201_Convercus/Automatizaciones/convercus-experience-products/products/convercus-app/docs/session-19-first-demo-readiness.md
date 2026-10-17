---
title: "Sesión 19 — Comprobación de preparación para la primera demostración vertical"
aliases:
- "Session 19 — First Vertical Demo Readiness"
language: es
version: "v1.0"
status: "assessment completed"
date: "2026-09-07"
project: "Convercus App"
document_type: "informe de preparación arquitectónica y epistemológica"
scope: "capacidad actual para construir la primera demostración vertical completa"
repository_role: "evaluación documental; no implementa la demostración ni abre una nueva frontera semántica"
semantic_authority: "análisis subordinado a TES, ADR-001–005 y al Contrato semántico de producto"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Sesión 19 — Comprobación de preparación para la primera demostración vertical

## 1. Conclusión ejecutiva

```text
FIRST DEMO READINESS → READY WITH GAPS
```

El repositorio ya puede ejecutar una sección vertical mínima de composición, configuración, Scenario, Demo Script, acción pública, transición controlada, modelo de lectura y UI. Esa ruta está demostrada para la Hospitality existente de llegada/check-in.

No existe todavía una sección vertical completa que conecte la Evidence recibida por la acción con `evaluateCrossSubjectEvidenceSufficiency()`, una afirmación derivada, la aplicabilidad contextual de H18 y un read model/UI de esa evaluación. Por tanto, la primera demostración Resort / Aventura Familiar puede construirse sobre bases existentes, pero todavía no está implementada extremo a extremo.

La preparación es `READY WITH GAPS` porque el hueco es local y reversible, no exige una nueva arquitectura, una API real ni resolver las fronteras semánticas excluidas.

## 2. Línea de base preservada

Se mantienen sin modificación:

```text
H17 → SUPPORTED WITH QUALIFICATION
H18 → SUPPORTED WITH QUALIFICATION
ADR-001–005 → ACCEPTED
Architecture v0.5 → ACTIVE / unchanged
Product Semantic Contract → OBSERVED PRESSURE / unchanged
PSC-P01 → OPEN / EVIDENCE-BACKED PRESSURE
PSC-P01 → STRENGTHENED BY ADDITIONAL EVIDENCE
```

Esta sesión no abre una nueva frontera semántica y no modifica código, TES, pruebas ni contratos.

## 3. Inspección del estado actual

### 3.1 Matriz de capacidades

| Capacidad | Estado actual | Evidencia concreta | Bloqueo para la primera demo | Trabajo mínimo pendiente | Riesgo semántico |
|---|---|---|---|---|---|
| Core / frontera de runtime | `AVAILABLE` | `DemoProvider` en `prototype/src/demo-factory/contracts.ts`; `App` recibe `ResolvedDemoRuntime` | No | Mantener la frontera | Bajo; no convertirla en arquitectura general prematura |
| Configuration / composición | `AVAILABLE` | `DemoManifest`, catálogos y `resolveDemo()` en `manifests.ts`, `artifacts.ts` y `bootstrap.ts` | No | Añadir referencias del fixture vertical si procediera | Promover manifest a autoridad semántica, evitando esa lectura |
| Scenario | `AVAILABLE` para un caso singular | `ScenarioDefinition` con subjects, contexts, checkpoints y `presenterAction` en `artifacts.ts` | No para el camino mínimo | Definir el fixture Resort sin inventar ontología | Confundir checkpoint con TES Progression |
| Demo Script | `AVAILABLE` para un paso | `DemoScript` y `hospitalityScript` en `artifacts.ts`; el runtime usa `steps[0]` | No para un primer paso | Declarar una acción vertical mínima | Hacer que Script controle estado o semántica |
| Runtime State | `AVAILABLE` local | `MockDataAdapter` conserva `checkpoint`, valida la acción y ejecuta transición en `mock-adapter.ts` | No | Añadir estado local de evaluación solo si el recorrido lo exige | Introducir estados TES no respaldados |
| Public Action | `AVAILABLE` | `DemoProvider.executeAction(action)` y `App` invocando el handler genérico | No | Reutilizar la frontera existente | Permitir que la UI escriba transición directamente |
| Data / fixtures | `AVAILABLE` local y mock | `DemoFixture`, `hospitalityFixture` y `retailFixture` en `contracts.ts` y `fixtures.ts` | No | Crear datos A/B/C, contexto y dos subjects para la demo candidata | Convertir fixture en modelo productivo |
| Neutral factual Evidence | `EXPERIMENTAL ONLY` | `EvidenceInput` en `contracts.ts`; la acción de Hospitality contiene una Evidence simulada en `artifacts.ts` | No para la shell actual; sí para la vertical completa | Conservar y pasar Evidence al evaluador, sin añadir interpretación automática | Confundir Evidence con Evento TES o Activity |
| Admisibilidad conjunta | `EXPERIMENTAL ONLY` | `evaluateJointAdmissibility()` y tests de Sesión 17 | Sí para demostrar A@P1+B@P2 legítimamente | Invocar la evaluación antes de K dentro del flujo local | Saltarse la premisa autoritativa o promoverla a autoridad productiva |
| Suficiencia K | `EXPERIMENTAL ONLY` | `evaluateCrossSubjectEvidenceSufficiency()` y `evidence-sufficiency.ts` | Sí para el claim vertical | Conectar el evaluador con la acción y conservar K sin cambios | Alterar K o asignar el claim a un sujeto/Group |
| Aplicabilidad contextual H18 | `EXPERIMENTAL ONLY` | `evaluateDerivedClaimContextualApplicability()` y tests de Sesión 18 | Solo si se quiere demostrar explícitamente reutilización en S2 | Mantenerla como evaluación local posterior, no como servicio | Promover `scopeRef` o exigir igualdad de ámbitos |
| Derived claim | `PARTIAL` | El tipo `AdmittedEvidenceSufficiencyClaim` existe; no se publica en runtime/UI | Sí para una vertical epistemicamente completa | Incorporar el resultado como estado/read model local | Inventar sujeto, propietario o beneficiario |
| Read Model | `AVAILABLE` parcial | `AppSnapshot` y `projectSnapshot()` en `mock-adapter.ts` | No para mostrar transición simple; sí para mostrar claim/evaluación | Añadir una proyección mínima si la demo debe mostrar el claim | Hacer de `AppSnapshot` fuente canónica o de autoridad |
| UI | `AVAILABLE` parcial | Rutas y pantallas en `App.tsx`; `/system` muestra checkpoint y acción | No para la shell; sí para visualizar evaluación | Añadir una superficie mínima de estado derivado | Hacer que la UI infiera validez por su cuenta |
| Branding | `AVAILABLE` para el fixture Hospitality | `brand:aurora-stay@1`, tokens y logo en `artifacts.ts` | No | Reutilizar Aurora Stay o confirmar marca de demo | Confundir marca con autoridad del escenario |
| Contexto situado | `AVAILABLE` experimental | booking/stay/property en `ScenarioDefinition` y Evidence | No | Mantenerlo explícito y separado | Resolver prematuramente dónde pertenece `bookingRef` |
| Real Convercus API | `MISSING` | No hay cliente API, auth, proxy ni endpoints verificados | No | Ninguno ahora | Inventar contrato o arquitectura API |

### 3.2 Lo que Architecture v0.5 no prueba por sí sola

Architecture v0.5 y los documentos de gobierno describen separaciones deseadas, pero la evidencia ejecutable actual solo demuestra el camino singular ya implementado. En particular, no se debe asumir que la existencia documental de Experience, evaluación o claims implique integración runtime.

## 4. Recorrido extremo a extremo actual

### Tramo ejecutable demostrado

```text
manifest/configuración
        ↓
resolveDemo()
        ↓
Scenario + Demo Script + MockDataAdapter
        ↓
App obtiene AppSnapshot
        ↓
usuario pulsa acción pública
        ↓
DemoProvider.executeAction()
        ↓
MockDataAdapter valida checkpoint
        ↓
actualiza checkpoint
        ↓
añade ActivitySourceRecord
        ↓
projectSnapshot()
        ↓
AppSnapshot
        ↓
Activity / System UI refleja el cambio
```

Este tramo está respaldado por los tests de bootstrap, presenter action y projection, y por la consolidación de H2.

### Primer corte real

```text
EvidenceInput recibida por executeAction()
        ↓
[CORTE]
contextual evaluation de Sesión 17
        ↓
claim de suficiencia K
        ↓
aplicabilidad contextual H18
        ↓
read model del claim
        ↓
UI del resultado
```

`MockDataAdapter.executeAction()` conserva la Evidence en la acción y crea una fila `ActivitySourceRecord`, pero no invoca `evaluateCrossSubjectEvidenceSufficiency()` ni `evaluateDerivedClaimContextualApplicability()`. Los evaluadores aparecen en módulos y tests experimentales aislados. No existe todavía un read model de esos resultados ni una pantalla que los presente.

```text
First missing link → Runtime Evidence → contextual evaluation
```

## 5. Candidata inicial de demostración

La preferencia inicial Resort / Aventura Familiar es viable como alcance, pero no se adopta como decisión irreversible de producto.

```text
vertical → Hospitality / Resort
property type → un resort
scenario → Aventura Familiar / Treasure Hunt
subjects → P1 y P2, ambos sujetos individuales
stay → una estancia
Evidence → A, B y C
criterion → K = A AND (B OR C)
clues → no ordenadas
```

La participación de A@P1 y B@P2 debe usar la premisa autoritativa experimental ya probada por H17. C puede conservarse como alternativa factual del criterio sin convertirlo en una pista ordenada ni en un Evento TES.

### Secuencia mínima propuesta

1. Resolver el paquete de demo, marca, fixture y Scenario.
2. Iniciar un estado runtime determinista para una estancia y un Treasure Hunt.
3. Presentar una acción pública que produzca o reciba una Evidence factual.
4. Repetir la acción mínima necesaria para disponer de A, B y, si se usa, C.
5. Ejecutar admisibilidad conjunta antes de K.
6. Producir el claim de suficiencia sin asignarle sujeto, propietario, beneficiario o Group.
7. Proyectar el resultado a un read model con procedencia y estado open-world.
8. Mostrar en UI el estado derivado y la Evidence atribuida, sin llamar a la afirmación colectiva ni a una entidad TES no reconocida.

Esto es una propuesta de alcance para una futura implementación, no una implementación de esta sesión.

## 6. UI y datos mínimos

La primera UI puede reutilizar la shell existente y añadir únicamente una superficie de demostración controlada:

- estado de la estancia y del Treasure Hunt;
- subjects P1 y P2 como atribuciones factuales, no como Group;
- Evidence A, B y C con procedencia;
- resultado de admisibilidad conjunta;
- resultado de K;
- claim establecido o `cannot-currently-establish`;
- indicador de provenance mock/simulated;
- acción de reset determinista.

No necesita mostrar beneficiario, owner, participación colectiva, Progression, Result TES, Completion TES ni incentivo.

## 7. Elementos fuera de alcance: bloqueo real

| Elemento | Clasificación para la primera sección vertical | Justificación |
|---|---|---|
| Group identity | `NON-BLOCKING` | H17 y H18 funcionan sin Group; la UI puede mostrar sujetos separados. |
| membership | `NON-BLOCKING` | No se necesita para A/B atribuidas ni para el claim sin referente resuelto. |
| collective participation | `NON-BLOCKING` | No se probará un outcome colectivo. |
| participant/contributor distinction | `NON-BLOCKING` | `subjectRef` factual basta dentro del fixture. |
| claim subject/referent | `NON-BLOCKING` | H18 ya se completó manteniéndolo `UNRESOLVED`. |
| external assistance | `NON-BLOCKING` | No forma parte de la acción mínima. |
| ordered clues | `NON-BLOCKING` | K usa contribuciones no ordenadas. |
| solution recognition | `NON-BLOCKING` | No se modela resolución de solución. |
| partial incentive eligibility | `NON-BLOCKING` | No se muestra incentivo. |
| authority accreditation | `NON-BLOCKING` para el fixture; `UNKNOWN` para producción | La competencia del premise está asumida experimentalmente, pero no es un bloqueador de la demo local. |
| authority conflict | `NON-BLOCKING` | Solo se usa una premisa controlada. |
| multiple authority premises | `NON-BLOCKING` | El alcance usa el fixture de una premisa ya probado. |
| scope hierarchy | `NON-BLOCKING` | H18 no requiere jerarquía. |
| scope equivalence | `NON-BLOCKING` | S1/S2 pueden permanecer opacos. |
| scope transitivity | `NON-BLOCKING` | No se infiere transitividad. |
| TES Event recognition | `NON-BLOCKING` | La Evidence puede permanecer factual con interpretación opcional no promovida. |
| TES Progression | `NON-BLOCKING` | No se afirma progreso TES; un checkpoint local basta. |
| TES Result | `NON-BLOCKING` | No se afirma Result TES. |
| real Convercus API | `NON-BLOCKING` | Mock/simulation local es admisible para una primera demostración. |
| bookingRef placement | `UNKNOWN` | El fixture puede conservarlo sin decidir su semántica productiva. |
| new derivation in S2 | `NON-BLOCKING` | La primera vertical puede demostrar una derivación en un contexto, no su nueva derivación en otro. |

`UNKNOWN` no significa bloqueo: indica una dependencia semántica que debe quedar explícitamente fuera del alcance.

## 8. PSC-P01 desde la perspectiva de bloqueo

```text
PSC-P01 → NON-BLOCKING FOR FIRST DEMO
```

La presión registrada no impide una demostración local con Evidence atribuida a P1 y P2, siempre que la admisibilidad conjunta esté respaldada por la premisa experimental de H17 y que no se confunda atribución con Group, ownership o claim subject.

PSC-P01 sí es un bloqueo para cualquier afirmación más amplia que pretenda tratar la atribución de Evidence como identidad automática de contribución, participación o referente del claim. Esa ampliación queda fuera de la primera vertical.

## 9. Evaluación de incertidumbres específicas

| Incertidumbre | Clasificación | Razón |
|---|---|---|
| `subjectRef` sin ontología Participant/Contributor | `NON-BLOCKING` | Se conserva como atribución factual experimental. |
| Falta de claim subject/referent | `NON-BLOCKING` | El claim puede permanecer sin asignación. |
| Falta de Group | `NON-BLOCKING` | No se necesita una entidad colectiva. |
| Authority accreditation unresolved | `NON-BLOCKING` para demo local, `UNKNOWN` para producto | Se asume solo en el fixture y no se promueve. |
| Nueva derivación en otro scope unresolved | `NON-BLOCKING` | No forma parte del primer recorrido. |
| Ubicación de `bookingRef` unresolved | `UNKNOWN` | Puede preservarse como dato experimental sin decidir su significado productivo. |

## 10. Deuda aceptable

### Deuda técnica reversible

- estado en memoria;
- fixture local;
- una transición pública controlada;
- catálogo estático;
- una proyección local adicional;
- UI de demostración concentrada.

### Deuda semántica no aceptable

- llamar Group a los dos sujetos;
- presentar checkpoint como Progression TES;
- convertir Activity en Evidence canónica;
- asignar el claim a P1, P2, P1+P2 o un beneficiario sin evidencia;
- tratar `scopeRef` como autoridad por existir;
- convertir la premisa experimental en acreditación productiva;
- afirmar validez universal o `false` cuando el resultado es `cannot-currently-establish`.

### Capacidad fuera de alcance

La API real, la acreditación de autoridad, los conflictos entre premisas, la persistencia, la jerarquía de ámbitos y la nueva derivación en S2 pueden quedar fuera sin constituir deuda de la primera demostración.

## 11. Criterios de preparación aplicados

| Criterio | Resultado |
|---|---|
| Usar semántica respaldada | `Sí`, si se limita a H17/H18 y no se promueven fixtures |
| No inventar API real | `Sí` |
| Separar Composition, Runtime State y Read Models | `Sí`, la separación ya existe; falta conectarla a evaluación |
| Demo Script no controla directamente estado/semántica | `Sí`, demostrado en la acción existente |
| Mostrar cambio observable por acción | `Sí`, demostrado por checkpoint y Activity |
| No resolver fronteras excluidas | `Sí` |
| Recorrido vertical completo disponible hoy | `No` |

El último criterio impide clasificar como `READY` pleno, pero el hueco no justifica `NOT READY`.

## 12. Veredicto final

```text
FIRST DEMO READINESS → READY WITH GAPS

First demo candidate → Hospitality / Resort / Aventura Familiar / Treasure Hunt

First executable path → manifest → resolveDemo() → Scenario → Demo Script
  → public action → MockDataAdapter → checkpoint → ActivitySourceRecord
  → projectSnapshot() → AppSnapshot → UI

First missing link → Runtime Evidence → contextual evaluation

PSC-P01 → NON-BLOCKING FOR FIRST DEMO

Group → NON-BLOCKING

Participant/Contributor distinction → NON-BLOCKING

Claim subject/referent → NON-BLOCKING

Real API → NOT REQUIRED NOW

Architecture v0.5 → ACTIVE / unchanged

Product Semantic Contract → OBSERVED PRESSURE / unchanged

Recommended next action → preparar una implementación vertical mínima que
  conecte una acción controlada con A/B/C, admisibilidad conjunta, K y un
  read model visible, manteniendo todos los artefactos experimentales bajo
  cuarentena; no introducir arquitectura general ni abrir otra frontera.
```

La recomendación identifica el trabajo técnico mínimo pendiente, pero esta sesión no lo implementa ni selecciona una nueva frontera semántica.
