---
title: "Session 11 — Experimento de relevancia contextual de evidencia"
aliases:
- "Contextual Evidence Relevance Experiment"
language: es
version: "v1.0"
status: "experiment completed"
date: "2026-09-04"
project: "Convercus App"
document_type: "informe de experimento"
scope: "evaluación contextual y determinista de evidencia neutral frente a dos Experience contexts"
repository_role: "evidencia ejecutable de H3 y entrada para una decisión arquitectónica estrecha"
semantic_authority: "experimento técnico de producto subordinado; no reconoce TES Events ni modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 11 — Experimento de relevancia contextual de evidencia

## Conclusión ejecutiva

Session 11 demuestra el criterio de éxito dentro de su alcance: **la misma evidencia neutral de Cooking Class es relevante para Aventura Familiar y no relevante para Desafío Activo debido a criterios de Experience Definition y Scenario, sin ramas por Experience ID, mutación, estado oculto, Progression ni Activity autoritativa**.

Se añadió una sola frontera pura, `evaluateEvidenceRelevance(evidence, context)`, y un test focalizado con dos contextos basados en las Product Experience Definitions de Session 10. La definición aporta las clasificaciones de actividad relevantes; el Scenario aporta stay, property y el catálogo local que identifica/clasifica la actividad. La evaluación necesita ambas partes.

Los 7 tests incrementales pasan. El check final supera typecheck, lint, **10 test files y 38 tests**, y build PWA. Las regresiones de presenter action/checkpoint y Retail permanecen verdes.

H3a, H3b, H3c y H3d quedan **SUPPORTED** para el caso mínimo. El veredicto H3 global es **SUPPORTED WITH QUALIFICATION**: se ha demostrado relevancia contextual previa a reconocimiento, no TES Event recognition, Pattern, Sequence, Progression, Result, Measurement, Learning, persistencia, participación o integración con API real.

## A. Base semántica

Cooking Class es un discriminante defendible por tres motivos independientes:

1. La fuente comercial y la Product Experience Definition de Aventura Familiar incluyen expresamente una clase de cocina entre las actividades del hotel que pueden sostener participación familiar compartida.
2. Desafío Activo limita su candidato semántico a participación deportiva/bienestar; Cooking Class no pertenece a esa clase con el material gobernado disponible.
3. La realización de una actividad puede existir como hecho verificable —quién, qué actividad, cuándo, en qué stay/property y por qué fuente— sin conocer ninguna Experience.

La evaluación no declara que completar Cooking Class sea un TES Event. Solo devuelve si la evidencia es relevante para el contexto de producto proporcionado.

### Hecho, interpretación de producto y simplificación

| Capa | Contenido utilizado |
|---|---|
| Fuente comercial no normativa | Aventura Familiar enumera clase de cocina; Desafío Activo se refiere a actividades deportivas/bienestar. |
| Product Experience Definitions subordinadas | Aventura Familiar trata participación compartida en actividades del hotel; Desafío Activo trata participación deportiva/bienestar reiterada. |
| Simplificación de experimento | Dos clasificaciones técnicas: `shared-hotel-activity` y `sport-wellness`; un catálogo local con Cooking Class y yoga. No son conceptos TES ni taxonomía final. |

No se modificaron las definiciones de Session 10 para producir el contraste.

## B. Responsabilidad de `ExperienceContext`

El experimento encuentra que la relevancia no reside por completo en Definition ni en Scenario:

```text
Product Experience Definition responsibility
  clases de actividad que pueden ser relevantes al núcleo candidato
                         +
Scenario responsibility
  stay + property + catálogo local + clasificación situada de actividad
                         ↓
              contextual relevance
```

### Product Experience Definition

`experience.relevantActivityClassifications` expresa el criterio de núcleo utilizado en este test:

- Aventura Familiar acepta `shared-hotel-activity`;
- Desafío Activo acepta `sport-wellness`.

No describe recompensas, estados ni reglas de Progression.

### Scenario

`scenario` aporta:

- la estancia y propiedad contra las que debe coincidir la evidencia;
- un catálogo local de actividades;
- la clasificación situada de cada actividad disponible.

Cooking Class figura como `shared-hotel-activity`; yoga figura como `sport-wellness`. El Scenario no decide qué clasificación acepta cada Experience ni redefine sus propósitos.

### Combinación

Una evidencia es relevante únicamente cuando:

1. coincide el contexto stay/property;
2. la actividad existe en el catálogo del Scenario;
3. alguna clasificación local de la actividad intersecta las clasificaciones relevantes de la Definition.

Los tests falsifican cada contribución por separado. Cambiar stay, retirar Cooking Class o cambiar el criterio semántico vuelve el resultado no relevante por razones distintas.

Esta división es experimental: no promueve un modelo general de catálogos ni una taxonomía de actividades.

## C. Inventario de cambios

### Archivos añadidos

- `prototype/src/demo-factory/evidence-relevance.ts`: tipos mínimos y evaluator puro.
- `prototype/src/demo-factory/evidence-relevance.test.ts`: evidencia, contextos y 7 tests focalizados.
- `docs/session-11-contextual-evidence-relevance-experiment.md`: este informe.

### Archivos modificados

- Ninguno.

### Áreas intencionadamente intactas

- Product Experience Definitions de Session 10.
- `EvidenceInput`, `EvidenceInput.interpretation` y `SignificantEvent`.
- Scenario, Demo Script, bootstrap, provider y presenter action.
- Checkpoints, fixtures, AppSnapshot, Activity projection y React UI.
- Retail, persistencia, APIs, providers y todo el corpus TES.

## D. Flujo real de evaluación

```text
ActivityCompletionEvidence
  cooking-class + participant + stay/property + provenance
                         │
                         ▼
            evaluateEvidenceRelevance
                 /                 \
                /                   \
Family Adventure Context      Active Challenge Context
Definition: shared activity   Definition: sport/wellness
Scenario: cooking class       Scenario: cooking class
         classified shared             classified shared
                │                   │
                ▼                   ▼
 relevant / explicit reason   not relevant / explicit reason

Activity: not invoked; remains a possible downstream projection
```

El evaluator devuelve `evidenceRef`, `experienceRef`, `relevant` y un reason code. No escribe runtime, checkpoint, Activity ni participación.

## E. Evidencia de tests

### Baseline

Antes del cambio, `npm run check` pasó con:

- typecheck correcto;
- lint correcto;
- 9 test files y 31 tests;
- build Vite/PWA correcto.

### Tests incrementales

Un nuevo archivo aporta 7 pruebas:

1. el input carece de Experience, interpretación, relevancia, Progression, reward y campos de Activity;
2. el mismo objeto produce `relevant` para Aventura Familiar y `not relevant` para Desafío Activo;
3. cambiar `definitionRef` preservando criterios no altera el resultado semántico;
4. Definition y Scenario contribuyen de forma observable e independiente;
5. input y contextos permanecen iguales y A→B equivale a B→A;
6. repetir input+context devuelve el mismo outcome;
7. el evaluator no importa ni produce Activity/read-model fields.

El test focalizado pasa: **1 file, 7 tests**.

### Check final

`npm run check` pasa con:

- typecheck correcto;
- lint correcto;
- **10 test files, 38 tests, todos superados**;
- build Vite/PWA correcto.

La suite completa incluye el presenter action de Session 7, rechazo de repetición, reset, proyección de Activity e aislamiento Retail.

## F. Veredictos de subhipótesis H3

| Subhipótesis | Veredicto | Evidencia y límite |
|---|---|---|
| H3a — Input independence | **SUPPORTED** | `ActivityCompletionEvidence` no contiene Experience, interpretación, relevancia ni presentación y existe antes de ambos contextos. Probado solo para una evidencia controlada. |
| H3b — Contextual relevance | **SUPPORTED** | El mismo input es relevante en A y no en B; ID renombrado con criterios idénticos conserva el resultado. Probado con dos clasificaciones y un catálogo local. |
| H3c — Evaluation independence | **SUPPORTED** | Evaluator puro, outcomes explícitos, objetos inmutados, orden y repetición deterministas. No cubre evaluaciones stateful reales. |
| H3d — Projection separation | **SUPPORTED** | Activity no es input, dependencia ni output del evaluator; la suite anterior conserva la proyección downstream. No se añadió una nueva Activity desde outcomes. |

## G. Veredicto H3 global

**SUPPORTED WITH QUALIFICATION.**

La evidencia ejecutable respalda:

```text
neutral factual evidence
        ≠
Experience-relative relevance outcome
        ≠
Activity projection
```

También respalda cardinalidad potencial sin tabla de pertenencia: un input puede producir outcomes independientes por contexto y puede no ser relevante. No respalda todavía:

- que `relevant` equivalga a TES Event;
- reconocimiento o confirmación de un Evento;
- Pattern, Sequence o cualquier estado de participación;
- Progression, Result, Measurement o Learning;
- evaluación contra definiciones plenamente validadas;
- reglas configurables, múltiples evidencias o agregación;
- comportamiento de una API o provider real.

Por ello, H3 completa su subhipótesis de **relevancia contextual**, pero no está listo para un ADR que gobierne toda la frontera Evidence/Occurrence/TES Event.

## H. Evaluación de `SignificantEvent`

Session 11 opera coherentemente antes de `SignificantEvent` y refuerza, sin formalizar todavía, esta separación conceptual:

```text
EvidenceInput / factual input
        ↓
Contextual relevance evaluation
        ↓
[future unresolved recognition boundary]
        ↓
SignificantEvent
```

El experimento muestra que `SignificantEvent` no es un nombre adecuado para el input factual neutral. Podría ser apropiado después de un reconocimiento contextual gobernado, pero esa frontera no se implementó. El contrato existente no se renombró, migró ni reutilizó porque incorpora semántica de participation/effects que excede el test.

No debe inferirse que toda evidencia relevante se convierta en SignificantEvent. Relevancia es condición de producto observada en el test, no reconocimiento TES completo.

## I. Evaluación de `EvidenceInput.interpretation`

El riesgo de conflación se vuelve **más visible**, no mayor por cambio de código: el campo opcional ya existía y Session 11 demuestra que la evaluación puede ocurrir sin él.

Si se conserva, `EvidenceInput.interpretation` solo puede leerse con seguridad como interpretación externa o previamente resuelta cuya procedencia debe ser explícita. Embutirla en el mismo objeto facilita que consumidores traten input e interpretación como una sola autoridad y que omitan evaluación contextual.

El campo queda provisional. La evidencia sugiere considerar en una decisión futura separar payload factual y interpretación asociada, pero Session 11 no rediseña el contrato ni prueba la forma final de esa relación.

## J. Impacto arquitectónico

**Architecture v0.4 sobrevive sin contradicción.**

- Experience Definition conserva responsabilidad distinta de Scenario.
- Scenario aporta situación sin convertirse en engine ni redefinir el núcleo.
- El evaluator puro queda fuera de React y del provider mutable.
- Runtime, checkpoints y presenter action no cambian.
- Read models/Activity permanecen downstream.

La arquitectura solo requiere una cualificación analítica, no una actualización formal: entre evidencia factual y proyección puede existir una frontera de relevancia contextual. Esta costura aún es experimental y no se añade como bloque aceptado de v0.4.

## K. Deuda técnica y atajos experimentales

- Solo se usan dos clasificaciones string locales.
- Las clasificaciones no forman una taxonomía gobernada ni versionada.
- Definition y Scenario contexts existen como fixtures de test, no se resuelven desde documentos.
- Los Product Experience Definition documents no son machine-readable contracts.
- El evaluator solo entiende `ActivityCompletionEvidence`.
- Hay coincidencia exacta de strings para stay, property y activity.
- No se modelan aliases, jerarquía, incertidumbre o múltiples clasificaciones provenientes de fuentes.
- Los reason codes son provisionales.
- No existe una política para distinguir unknown de not relevant.
- `participantRef` no se valida contra subjects del Scenario.
- Se reutiliza el union de `EvidenceInput.reliability`, creando un acoplamiento técnico pequeño con el contrato anterior.
- No hay evaluación de elegibilidad, participación, concurrencia ni tiempo válido.
- No se evalúan varias evidencias ni resultados agregados.
- No se integra el outcome en runtime o Activity.
- No se prueba una API real ni procedencia heterogénea.
- `definitionRef` identifica documentos candidate, no definiciones TES plenamente validadas.

## L. Reversibilidad

Session 11 se elimina por completo borrando:

```text
prototype/src/demo-factory/evidence-relevance.ts
prototype/src/demo-factory/evidence-relevance.test.ts
docs/session-11-contextual-evidence-relevance-experiment.md
```

No hay imports desde producción, migraciones, estado persistido, cambios de manifests, fixtures, runtime, UI ni dependencias. Tras retirar los dos archivos TypeScript, la suite vuelve a su baseline de 9 archivos/31 tests.

## M. Experimento reservado Treasure Hunt

**No se implementó ningún comportamiento de Treasure Hunt / Búsqueda del Tesoro.** No existen clues, agregadores, estados parciales, subjects colectivos nuevos ni reglas de suficiencia.

Permanecen abiertas para un experimento futuro y separado:

- participación cooperativa;
- sujeto individual frente a grupo;
- evidencia parcial por actor;
- agregación sin convertir Activity en fuente;
- solución parcial frente a resolución observada;
- pistas ordenadas o no ordenadas;
- suficiencia de evidencia y contradicciones;
- reconstrucción de outcome grupal sin inferir TES Progression o Completion.

Treasure Hunt no debe incorporarse como “segundo ejemplo” del evaluator actual: su valor reside precisamente en falsificar supuestos de evidencia individual y atómica.

## N. Siguiente decisión madura

Ha madurado una única decisión estrecha para consideración arquitectónica:

> **La relevancia respecto de una Experience es un outcome explícito y contextual derivado de evidencia factual + Product Experience Definition + Scenario; no es una propiedad universal intrínseca del input, no autoriza por sí misma un TES Event y no pertenece a Activity.**

Esta decisión puede considerarse para un ADR acotado de **neutral evidence and contextual relevance**. No debe ampliarse a reconocimiento de Eventos, modelo de persistencia, reglas engine, cardinalidad universal ni migración de `SignificantEvent`.

## Revisión adversarial final

1. **¿Dependió la relevancia de criterios y no del Experience ID?** Sí. El evaluator no contiene IDs; un test cambia `definitionRef` y conserva relevant/reason.
2. **¿Podría existir EvidenceInput sin ambas Experiences?** Sí. El input solo contiene hecho, participante, stay/property, actividad, tiempo, fuente y fiabilidad.
3. **¿Scenario aportó información situada real?** Sí: stay/property, existencia local y clasificación de Cooking Class.
4. **¿Scenario absorbió reglas semánticas generales?** No decide qué clase acepta una Experience. Sí contiene una clasificación local experimental; su frontera deberá revisarse antes de generalizar.
5. **¿Alguna evaluación mutó el input?** No; input y ambos contextos se comparan antes/después.
6. **¿Afectó el orden?** No; A→B y B→A producen outcomes individuales idénticos.
7. **¿`relevant` se convirtió en TES Event?** No; el outcome y el informe lo prohíben expresamente.
8. **¿Apareció Progression oculta?** No hay estados, contadores, checkpoints, efectos ni mutaciones.
9. **¿Activity sigue completamente downstream?** Sí; no interviene en el evaluator ni recibe nuevos datos en este experimento.
10. **¿Puede operar el evaluator sobre otra actividad sin special cases?** Sí, si el Scenario aporta la actividad y clasificaciones; no existen branches por Cooking Class o Experience ID. Esto no prueba generalidad taxonómica.
11. **¿Qué sigue débil en las definiciones?** Pattern, Result participante, Progression no contable, Measurement, Learning y validación de participación.
12. **¿Qué podría invalidar una API real?** Eventos ya interpretados sin payload neutral, taxonomías incompatibles, IDs no estables, evaluación stateful, contextos implícitos, distinta unidad de sujeto o ausencia de procedencia común.
13. **¿Qué no debe generalizarse?** Las dos clasificaciones, la forma de context, los reason codes, evaluación puramente síncrona, coincidencia por strings, independencia universal de orden o que todo input deba evaluarse contra N Experiences.
14. **¿Treasure Hunt quedó intacto?** Sí; continúa reservado como stress test cooperativo más rico.
