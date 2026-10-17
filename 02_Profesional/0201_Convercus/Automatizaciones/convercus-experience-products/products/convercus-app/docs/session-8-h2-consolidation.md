---
title: "Session 8 — Consolidación de H2 y promoción de ADR"
aliases:
- "H2 Consolidation and ADR Promotion"
- "Demo Factory Architecture v0.4"
language: es
version: "v1.0"
status: "consolidado"
date: "2026-09-04"
project: "Convercus App"
document_type: "informe de consolidación de arquitectura"
scope: "verificación de Session 7, consolidación de H2 y selección del siguiente experimento"
repository_role: "evaluación posterior al experimento y entrada de decisión para Session 9"
semantic_authority: "análisis de producto y arquitectura subordinado; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 8 — Consolidación de H2 y promoción de ADR

## 1. Conclusión ejecutiva

Session 7 confirma la hipótesis H2 dentro del alcance mínimo ensayado: **Experience Definition, Scenario y Demo Script pueden permanecer lógicamente separados mientras el Script provoca comportamiento determinista exclusivamente mediante una acción pública validada por el runtime**.

La verificación independiente inspeccionó contratos, artefactos, bootstrap, adapter, UI y pruebas. También ejecutó `npm run check` el 4 de septiembre de 2026: typecheck y lint correctos, **9 archivos de test y 31 tests superados**, y build PWA correcto. Hospitality ofrece exactamente una acción de presentador; el runtime valida y posee la transición; el snapshot y Activity proyectan el resultado; reset recupera el estado inicial; Retail permanece aislado; repetir la acción falla explícitamente. No se añadieron semánticas TES de Progression, Result o Completion.

Se acepta [ADR-004 — Separación de Experience Definition, Scenario y Demo Script](../../../00-governance/decisions/ADR-004-experience-scenario-demo-script-separation.md). La promoción se limita a la separación de responsabilidades y a la frontera pública. La forma de transición singular, los strings, el control `/system` y la ejecución de `steps[0]` continúan experimentales.

H2 queda **SUPPORTED — READY FOR ADR**, ahora formalizado. H3 y H4 continúan parciales. H3 pasa a ser la incertidumbre arquitectónica de mayor valor: Session 7 añade procedencia y una proyección derivada, pero no evaluación contextual ni reconocimiento de TES Event. Se recomienda exactamente **Candidate A — experimento H3 de evaluación contextual multi-Experience** para Session 9, estrictamente in-memory y sin construir un motor de Experience.

## 2. Verificación independiente de Session 7

### 2.1 Resultado ejecutable

| Verificación | Resultado |
|---|---|
| TypeScript | Correcto. |
| ESLint | Correcto. |
| Vitest | 9 archivos, 31 tests, todos superados. |
| Build | Vite/PWA correcto. |

### 2.2 Matriz de evidencia

Cada afirmación distingue el hecho observable en el repositorio, la cobertura de test y la inferencia arquitectónica permitida.

| Afirmación | Repository fact | Test evidence | Architectural inference | Veredicto |
|---|---|---|---|---|
| Hospitality expone exactamente la acción prevista | `hospitalityScenario.presenterAction` declara solo `confirm-arrival`; `hospitalityScript.steps` contiene un único paso con esa acción. `/system` deriva su control de `runtime.script?.steps[0]`. | `presenter-action.test.tsx` renderiza el botón «Confirmar llegada» y comprueba el cambio. | El recorrido actual ofrece una sola acción operacional de presentador. No prueba cardinalidad futura. | Confirmada con alcance singular. |
| Demo Script identifica la acción sin mutar estado | El paso contiene copy, checkpoint esperado y `DemoAction`; no recibe provider ni callback interno. La acción no contiene `fromCheckpoint` ni `toCheckpoint`. | La prueba estructural exige que la acción del Script no posea ambos campos. | Script solicita y describe; Scenario declara el límite permitido; runtime ejecuta. | Confirmada. |
| La frontera pública está fuera de React | `DemoProvider` publica `executeAction(action)`; `App.tsx` solo la invoca desde un handler genérico. No importa el adapter concreto. | La prueba de UI ejecuta el camino público; las pruebas de proyección impiden el acoplamiento de App al provider concreto. | React no es autoridad sobre la acción ni sobre la transición. | Confirmada. |
| Runtime valida la legalidad | `MockDataAdapter.executeAction()` compara identificador y checkpoint efectivo con la acción permitida del Scenario y lanza errores explícitos. | Se prueba la acción válida y la repetición desde el estado resultante. | La mera presencia de un paso de Script no autoriza una mutación. | Confirmada para la única transición. |
| Runtime posee la transición | El adapter mantiene `checkpoint` privado y lo actualiza a `toCheckpoint` solo después de validar. Scenario aporta la transición permitida; Script no escribe el estado. | El test pasa de `pre-arrival-confirmed` a `checked-in` y obtiene el mismo resultado desde dos instancias equivalentes. | La autoridad operacional reside en runtime; Scenario aporta configuración contextual, no ejecución. | Confirmada. |
| AppSnapshot/read model refleja el resultado | `getSnapshot()` publica `scenario.checkpoint` y `availableActionId`; App renderiza checkpoint actual y esperado. | El test DOM observa `checked-in` y el botón queda deshabilitado. | La UI observa un read model en lugar de inspeccionar estado interno. | Confirmada. |
| Activity se actualiza como proyección | La acción añade un `ActivitySourceRecord`; `projectSnapshot()` produce los campos visuales de `ActivityItem`. | El test navega a Activity y encuentra `booking.checked_in`; las pruebas de proyección verifican que icono y tono no están en el source. | Activity representa el cambio, pero no se convierte en fuente de verdad. | Confirmada. |
| Reset restaura el checkpoint inicial | El adapter clona el fixture y conserva `initialCheckpoint`; `reset()` restaura ambos. | Tras la acción, el test verifica recuperación de `pre-arrival-confirmed` y desaparición de la entrada añadida. | La sesión demo puede volver a un estado reproducible. | Confirmada. |
| Retail permanece aislado | Cada resolución crea un adapter con clones propios; Retail no posee Scenario ni Script. | La suite comprueba que actuar/resetear Hospitality no altera el snapshot Retail. | No hay estado mutable compartido entre ambas composiciones resueltas. | Confirmada para providers locales por instancia. |
| Repetir la acción tiene resultado controlado | Desde `checked-in`, la precondición de checkpoint ya no se cumple y el adapter lanza error. | Test dedicado espera rechazo explícito en la segunda ejecución. | El runtime evita una segunda mutación silenciosa. No demuestra idempotencia general. | Confirmada como fallo explícito. |
| No se introdujo Progression, Result o Completion TES | Contratos, artefactos y adapter llaman `checkpoint` al estado local; un comentario lo separa explícitamente de TES. No existen reglas ni tipos nuevos de esos conceptos. | Ningún test afirma progreso, resultado o completion; solo checkpoint y Activity. | Los nombres de llegada describen la demo, no un estado semántico de Experience. | Confirmada por inspección, con obligación de conservar la cualificación. |

### 2.3 Discrepancias y cualificaciones previas al ADR

No se encontró una afirmación de Session 7 que impida aceptar la separación. Sí se acotan cuatro afirmaciones que podrían leerse con más fuerza de la respaldada:

1. La UI consume únicamente `steps[0]`; no ejecuta un Script multi-step.
2. `ScenarioDefinition` contiene un solo `presenterAction`; no modela varias transiciones, branching ni un grafo.
3. `expectedCheckpoint` del Script se valida en bootstrap contra la transición del Scenario, pero no gobierna la transición en runtime.
4. La acción recibe una `EvidenceInput` simulada con interpretación TES opcional ya adjunta. Esto no demuestra reconocimiento de Event, evaluación contextual ni ocurrencia factual externa.

Además, `ExperienceDefinition` es hoy un header resoluble mínimo, no una definición semántica completa de TES, y la reutilización entre varios Scenarios o Scripts no se ha ensayado. ADR-004 acepta la frontera conceptual, no eleva esas formas experimentales a contratos universales.

## 3. ADR-004

Se crea y acepta ADR-004 con esta decisión central:

```text
Experience Definition
        ↑ referenced/instantiated by
Scenario
        ↑ demonstrated through
Demo Script
```

Toda interacción operacional debe atravesar:

```text
Demo Script → Public Action → Runtime Boundary
            → Controlled Runtime Transition → Read Model / UI
```

El ADR asigna significado a Experience Definition, situación a Scenario, orquestación de presentación a Demo Script y estado mutable/validación al runtime. Establece además la desigualdad obligatoria:

```text
Demo checkpoint != TES Experience Progression / Result / Completion
```

No decide motores, grafos, branching, ejecución multi-step, concurrencia de scripts, participación colectiva, evaluación de Experience ni workflow reutilizable.

## 4. Matriz de promoción de elementos de Session 7

Cada elemento recibe exactamente una clasificación.

| Elemento | Clasificación | Decisión y límite |
|---|---|---|
| Frontera pública de acción de presentador | **PROMOTE** | Se promueve que UI/Script soliciten acciones mediante una frontera pública y que runtime valide y posea la mutación. No implica command bus ni provider universal. |
| Representación de Demo Script | **PROMOTE WITH QUALIFICATION** | Se promueve el artefacto separado y su referencia a acciones/expectativas públicas. La forma del contrato, cardinalidad y semántica de pasos siguen abiertas. |
| Representación de transición en Scenario | **PROMOTE WITH QUALIFICATION** | Se promueve que Scenario pueda declarar un límite de interacción situado sin ejecutar reglas. El único `from/to` y su ubicación exacta no son normativos. |
| Checkpoint de runtime | **PROMOTE WITH QUALIFICATION** | Se promueve estado local mínimo, observable y reseteable cuando una demo lo necesita. Su modelo y nombres son provisionales y no expresan TES. |
| Control de presentador en `/system` | **RETAIN AS EXPERIMENTAL** | Prueba el recorrido end-to-end; ruta, ubicación, copy y disabled state no son una arquitectura de presenter console. |
| Proyección de Activity tras la acción | **PROMOTE** | El runtime añade un registro fuente y Activity deriva la representación. Extiende con acción la costura ya aceptada en ADR-002. |
| Identificadores de acción string | **RETAIN AS EXPERIMENTAL** | `confirm-arrival` basta para el test; no demuestra namespace, versionado, compatibilidad ni tipado final. |
| Checkpoints string | **RETAIN AS EXPERIMENTAL** | Son valores locales legibles, no un contrato general ni estados TES. |
| Scenario de una sola acción | **RETAIN AS EXPERIMENTAL** | Es el mínimo falsable del experimento, no una restricción arquitectónica. |
| Ejecución exclusiva del primer paso del Script | **RETAIN AS EXPERIMENTAL** | `steps[0]` evita generalización prematura; no define semántica de ejecución del Script. |

No se clasifica ningún elemento como DEPRECATE o REMOVE: nada del alcance nuevo compite con la decisión aceptada ni debe eliminarse para consolidarla.

## 5. Madurez final de H2

**Clasificación: SUPPORTED — READY FOR ADR, formalizada en ADR-004.**

La evidencia cumple el umbral porque demuestra simultáneamente:

- separación estructural de Experience Definition, Scenario y Demo Script;
- composición y validación de referencias antes del render;
- solicitud de una acción real desde el Script;
- frontera operacional ajena a React;
- validación y transición deterministas en runtime;
- read model y Activity derivados;
- recuperación mediante reset, fallo controlado e aislamiento cruzado;
- ausencia de reglas TES inventadas.

La madurez corresponde a la **separación de responsabilidades**, no a la generalidad de las representaciones. Reutilización, múltiples pasos, múltiples acciones, condiciones, branching y cardinalidades permanecen hipótesis. Estas limitaciones no bloquean el ADR porque el ADR las excluye expresamente.

## 6. Demo Factory Architecture v0.4

Architecture v0.4 añade solamente la separación respaldada por H2 a v0.3:

```text
┌──────────────────────────────────────────────────────┐
│ TES semantic authority                              │
│ Significado e invariantes                           │
└──────────────────────────┬───────────────────────────┘
                           │ trazabilidad
┌──────────────────────────▼───────────────────────────┐
│ Experience Definition                 ACCEPTED      │
│ Definición semántica; forma actual mínima/cualificada│
└──────────────────────────┬───────────────────────────┘
                           │ referenced/instantiated by
┌──────────────────────────▼───────────────────────────┐
│ Scenario Context                     ACCEPTED SEAM  │
│ Contexto situado y límite permitido                 │
│ Transición singular/from-to: PROVISIONAL            │
└──────────────────────────┬───────────────────────────┘
                           │ referencia desde
┌──────────────────────────▼───────────────────────────┐
│ Demo Manifest / Desired Composition    ACCEPTED      │
│ Referencias, intención y capability requests        │
└──────────────────────────┬───────────────────────────┘
                           │ validar y resolver
┌──────────────────────────▼───────────────────────────┐
│ Bootstrap / Effective Composition      ACCEPTED SEAM │
│ Catálogos y selector concretos: PROVISIONAL         │
└──────────────────────────┬───────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────┐
│ Runtime                               ACCEPTED SEAM  │
│ Valida acción, posee transición y estado mutable     │
│ Checkpoint/string/single transition: PROVISIONAL     │
└───────────────┬───────────────────────────▲──────────┘
                │ projection                │ Public Action
┌───────────────▼──────────────────┐  ┌─────┴───────────────┐
│ Read Models / UI       ACCEPTED  │  │ Demo Script         │
│ AppSnapshot + Activity           │  │ Separate: ACCEPTED  │
└──────────────────────────────────┘  │ steps[0]: PROVISIONAL│
                                      └─────────────────────┘
```

La dirección hacia Runtime desde Demo Script representa una solicitud pública, no acceso interno. Scenario llega al runtime como parte de la composición efectiva; no es un motor ejecutándose. H3 (evaluación contextual) y H4 (multi-provider) permanecen fuera de la parte aceptada.

## 7. Actualización de evidencia H3

**Clasificación: parcial; no promover.**

Session 7 aporta evidencia nueva pero estrecha:

| Dimensión | Evidencia añadida | Lo que no demuestra |
|---|---|---|
| Factual occurrence | Una acción controlada produce un registro fuente de Activity. | El hecho no procede de una fuente independiente: el presentador aporta evidencia simulada al ejecutar la acción. No prueba ocurrencia externa, deduplicación ni corrección. |
| Provenance | `EvidenceInput` conserva procedencia y el registro resultante mantiene su carácter simulado. | No atraviesa providers heterogéneos, persistencia ni transformaciones múltiples. |
| Event interpretation | La evidencia admite una interpretación TES opcional separada de los campos visuales. | La interpretación ya viene adjunta; no se reconoce ni evalúa respecto a una Experience. No prueba cero/una/múltiples interpretaciones. |
| Activity projection | El nuevo registro se transforma en `ActivityItem` y se vuelve visible en la UI. | Activity no prueba por sí misma significado TES ni autoridad factual. |

H3 se convierte en la incertidumbre de mayor valor porque H1 dispone de dos demos y una costura compositiva aceptada, H2 ya alcanza ADR y H4 puede recibir más valor cuando haya requisitos o contratos de API reales. La cuestión que sigue abierta en el centro del producto es si **el mismo input evidenciario puede adquirir significación distinta según la Experience sin contaminar la evidencia ni construir un motor general**.

## 8. Actualización de evidencia H4

**Clasificación: parcial; no promover arquitectura multi-provider.**

La acción pública demuestra que la aplicación puede invocar comportamiento a través de `DemoProvider` sin importar el adapter concreto. También demuestra que una composición efectiva puede entregar una frontera con lectura, acción y reset, y que la validación queda fuera de React.

No demuestra:

- resolución de un provider por capability;
- dos providers simultáneos;
- contratos separados de lectura y comando;
- overlays, precedencia o reconciliación;
- degradación parcial;
- compatibilidad con una API real;
- distribución de secretos o políticas de deployment;
- que `DemoProvider` agregado sea el puerto final.

La evidencia mejora la confianza en **inyección de una frontera runtime**, no en multi-provider. H4 continúa parcial y no preparada para ADR.

## 9. Candidatos para el siguiente experimento

| Candidato | Información ganada | Incertidumbre reducida | Coste | Reversibilidad | Riesgo de abstracción prematura | Dependencias TES/API |
|---|---|---|---|---|---|---|
| **A — H3 contextual multi-Experience evaluation** | Observa si un mismo input puede producir significación/efectos distintos por Experience y Activity derivada. | Alta: ataca la separación aún no probada entre evidencia, interpretación contextual y proyección. | Medio-bajo si es puro e in-memory. | Alta: tipos, funciones y fixtures locales eliminables. | Medio-alto; se controla prohibiendo un engine, reglas universales y estado persistente. | TES alta en vocabulario y límites; API baja. |
| **B — H4 multi-provider composition** | Prueba provider por capability, coexistencia y quizá fallo parcial. | Alta para H4 local, pero limitada respecto a integración real. | Medio. | Alta con dos providers locales. | Medio-alto: puede cristalizar puertos sin conocer contratos reales. | TES baja; API real alta para obtener validez externa. |
| **C — Third-demo marginal-cost test** | Repite la medición de coste y revela especificidad oculta en H1. | Media: fortalece una hipótesis ya bien respaldada. | Medio: marca, fixture, manifiesto y regresión completa. | Alta. | Medio: una tercera vertical puede forzar un pseudo-esquema prematuro. | Baja o media según el dominio. |
| **D — Second Scenario / Script reuse test** | Prueba reutilización y cardinalidad más allá del camino singular. | Media: reduce límites residuales de una separación ya aceptada. | Bajo-medio. | Muy alta. | Medio: tentación de generalizar listas, grafos o runners tras solo dos casos. | TES media-baja; API baja. |

Aplicando el criterio «máxima incertidumbre arquitectónica reducida por unidad de complejidad irreversible», A supera a B porque aborda una incertidumbre semántica central con un experimento local menor; supera a C y D porque ambas profundizan hipótesis que ya cruzaron su umbral de decisión.

## 10. Recomendación para Session 9

**Recomendar exactamente Candidate A — H3 contextual multi-Experience evaluation.**

El experimento mínimo conceptual debe contener:

```text
un único factual/evidentiary input inmutable
                   │
          ┌────────┴────────┐
          │                 │
 evaluación relativa   evaluación relativa
 a Experience A        a Experience B
          │                 │
 significant / effect A     no effect o effect B
          └────────┬────────┘
                   │
          Activity derivada
```

### Alcance mínimo propuesto

1. Un input evidenciario inmutable, con identidad y procedencia, sin icono/tono de Activity y sin significación universal preasignada.
2. Dos referencias versionadas a Experiences y dos contextos controlados.
3. Una evaluación pura por par input–Experience que produzca resultados separados: A significativo con un efecto demo; B no significativo o con un efecto diferente.
4. Registros de evaluación separados y trazables que no muten ni dupliquen la evidencia.
5. Activity proyectada desde los resultados de evaluación, no directamente desde el input bruto.
6. Tests de independencia, determinismo, procedencia y cardinalidad cero/una/múltiples Experiences evaluadas.

### Guardrails

- No llamar TES Event al resultado salvo que la baseline autorice exactamente esa interpretación.
- No introducir Pattern, Sequence, Progression, Result o Completion.
- No añadir persistence, replay, store, reglas configurables, DSL ni motor genérico.
- No diseñar participación colectiva ni efectos productivos.
- No ampliar la UI salvo lo estrictamente necesario para observar la diferencia; una prueba de proyección puede ser suficiente.
- Detener el experimento si exige inventar semántica TES que no esté validada.

La pregunta falsable es: **¿puede conservarse un hecho/evidencia común e independiente mientras su significación y proyección varían por Experience de forma explícita, trazable y no mutante?**

## 11. Riesgos restantes

- `ExperienceDefinition` de Demo Factory sigue siendo un header mínimo y comparte nombre con representaciones de dominio más ricas.
- Solo existe un Scenario con una acción y un Script con un paso ejecutable.
- `presenterAction`, `actionId`, checkpoints y `expectedCheckpoint` carecen de versionado y política de compatibilidad.
- Los checkpoints podrían adquirir semántica implícita por sus nombres si no se conserva la cualificación ADR-004.
- El Script y Scenario duplican una expectativa de destino validada en bootstrap; el crecimiento podría convertirla en reglas repetidas.
- `EvidenceInput` llega desde una acción simulada y con interpretación opcional preconstruida; H3 sigue sin resolver.
- Activity conserva copy descriptivo en el registro fuente aunque deriva sus campos visuales.
- `DemoProvider` agrupa lectura, acción y reset; no hay prueba de que esa granularidad sobreviva a proveedores reales.
- Todas las capabilities siguen resueltas al mismo adapter local.
- Manifiesto, artifacts y catálogos TypeScript aún carecen de una estrategia final de registry y versionado de instancia.
- `DemoPackage`, `canonical-demo-package.ts` y `app.yaml` continúan como fuentes legacy competidoras.
- El selector por query parameter y el control `/system` son mecanismos de laboratorio.
- `visibleModules` sigue declarado sin gobernar la UI.
- No hay evidencia de participación colectiva, evaluación contextual, estados tardíos, corrección, privacidad o persistencia.

## 12. Recomendación Go / No-Go

**GO para aceptar ADR-004 y declarar H2 SUPPORTED — READY FOR ADR.** La baseline de Session 7 puede conservarse como evidencia ejecutable cualificada.

**GO condicionado para Session 9 exclusivamente con Candidate A.** Debe limitarse a una evaluación contextual in-memory, inmutable y observable entre dos Experience references. Es **NO-GO** para un motor de Experience, workflow, Pattern/Sequence/Progression/Result, persistencia general, integración API o ampliación multi-provider dentro de esa sesión.

Si no puede formularse el resultado sin inventar significado TES, Session 9 debe detenerse y registrar el bloqueo semántico en lugar de sustituirlo por semántica de producto no gobernada.
