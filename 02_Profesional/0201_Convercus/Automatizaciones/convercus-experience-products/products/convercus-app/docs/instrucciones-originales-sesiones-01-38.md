---
title: "Convercus Demo Factory — Textos originales de las instrucciones 01–38"
language: es
date: "2026-09-22"
status: "COMPILACIÓN PARCIAL — 35 de 38 instrucciones principales recuperadas; sesión 20 parcial; 18 y 19 pendientes"
---

# Convercus Demo Factory — Instrucciones originales por capítulos

Este documento recopila el texto íntegro de las instrucciones originales recuperadas, no resúmenes ni informes de ejecución.

**Estado: 35 de 38 sesiones con su instrucción principal recuperada — sesiones 01–17 y 21–38. La sesión 20 está parcialmente recuperada: se conserva una corrección posterior, pero falta su apertura y una especificación de continuidad previa. Las instrucciones originales de las sesiones 18 y 19 siguen pendientes.** El ZIP del M3 contiene 18 registros JSONL, sin errores de descompresión ni de lectura JSON. De ellos se recuperan 30 instrucciones principales adicionales y varias instrucciones complementarias; las referencias a informes no se contabilizan como originales.

Se conserva el idioma, redacción, listas, tablas y bloques de código de cada original. Únicamente se desplazan dos niveles los encabezados Markdown fuera de bloques de código para subordinarlos a su capítulo. No se corrigen erratas ni se sustituyen instrucciones por conclusiones posteriores. Las notas de procedencia y los marcadores que delimitan cada transcripción son editoriales.

La sesión 02 corresponde al bloque final rotulado «INSTRUCCIÓN SESION 2» en el documento histórico; no se mezclan las versiones propuestas anteriormente en ese mismo archivo. Los separadores y espacios del bloque extraído se conservan.

La [guía resumida anterior](guia-maestra-sesiones-01-38.md) permanece disponible como material distinto. No reemplaza los textos originales que faltan. Para completar este volumen siguen haciendo falta las instrucciones de las sesiones 18 y 19 y la apertura/especificación previa de la sesión 20.

La recuperación desde `2026.zip` utiliza los mensajes originales y las lecturas de adjuntos registradas por las herramientas. No se ejecutan aquellas órdenes, no se importan hilos en Codex y no se modifican los archivos aportados. Los adjuntos originales del M3 no están incluidos en el ZIP: se recupera su texto desde las salidas conservadas, se cotejan los rangos, recuentos y repeticiones disponibles, y se guardan [copias literales con un manifiesto de procedencia](instrucciones-recuperadas/manifest-recuperacion-2026.json).

Se preservan por separado las correcciones y consolidaciones de las sesiones 02, 14, 17 y 21. Los reenvíos idénticos de las sesiones 04, 20, 32 y 33 no se cuentan como nuevas sesiones. Las transcripciones ya incorporadas de las sesiones 01, 02, 30, 37 y 38 permanecen intactas.

## Índice y disponibilidad

| Capítulo | Tema orientativo | Texto original |
| --- | --- | --- |
| [Sesión 01](#sesion-01) | Inspección arquitectónica del repositorio | ÍNTEGRO RECUPERADO |
| [Sesión 02](#sesion-02) | Anatomía semántica y Architecture v0.1 | ÍNTEGRO RECUPERADO |
| [Sesión 03](#sesion-03) | Revisión adversarial de Architecture v0.1 | ÍNTEGRO RECUPERADO |
| [Sesión 04](#sesion-04) | ADR mínimos y experimento reversible | ÍNTEGRO RECUPERADO |
| [Sesión 05](#sesion-05) | Implementar el experimento mínimo de dos demos | ÍNTEGRO RECUPERADO |
| [Sesión 06](#sesion-06) | Consolidar la composición deseada y efectiva | ÍNTEGRO RECUPERADO |
| [Sesión 07](#sesion-07) | Acción pública de presentador y transición controlada | ÍNTEGRO RECUPERADO |
| [Sesión 08](#sesion-08) | Consolidar H2 y aceptar ADR-004 | ÍNTEGRO RECUPERADO |
| [Sesión 09](#sesion-09) | Comprobar prerrequisitos de evaluación multi-Experience | ÍNTEGRO RECUPERADO |
| [Sesión 10](#sesion-10) | Readiness de fuentes comerciales | ÍNTEGRO RECUPERADO |
| [Sesión 11](#sesion-11) | Relevancia contextual de evidencia neutral | ÍNTEGRO RECUPERADO |
| [Sesión 12](#sesion-12) | Fronteras de autoridad y mundo abierto | ÍNTEGRO RECUPERADO |
| [Sesión 13](#sesion-13) | Evaluación open-world acotada por autoridad | ÍNTEGRO RECUPERADO |
| [Sesión 14](#sesion-14) | Promoción limitada de ADR-005 | ÍNTEGRO RECUPERADO |
| [Sesión 15](#sesion-15) | Evidencia distribuida y suficiencia | ÍNTEGRO RECUPERADO |
| [Sesión 16](#sesion-16) | Preparar la frontera entre atribución y admisibilidad | ÍNTEGRO RECUPERADO |
| [Sesión 17](#sesion-17) | Composición entre sujetos acotada por autoridad | ÍNTEGRO RECUPERADO |
| [Sesión 18](#sesion-18) | Validez contextual del claim derivado | PENDIENTE |
| [Sesión 19](#sesion-19) | Preparación para la primera demo vertical | PENDIENTE |
| [Sesión 20](#sesion-20) | Construir y corregir Aventura Familiar | PARCIAL — corrección posterior recuperada |
| [Sesión 21](#sesion-21) | Falsar la reutilización de composición | ÍNTEGRO RECUPERADO |
| [Sesión 22](#sesion-22) | Selección estable por Experience | ÍNTEGRO RECUPERADO |
| [Sesión 23](#sesion-23) | Transporte del contexto situado a evaluación | ÍNTEGRO RECUPERADO |
| [Sesión 24](#sesion-24) | Buscar una fuente existente para Activity situada | ÍNTEGRO RECUPERADO |
| [Sesión 25](#sesion-25) | Declaración explícita de Activity por paso | ÍNTEGRO RECUPERADO |
| [Sesión 26](#sesion-26) | Auditar GuestPerspective sin relaciones nuevas | ÍNTEGRO RECUPERADO |
| [Sesión 27](#sesion-27) | Labels situados de sujetos | ÍNTEGRO RECUPERADO |
| [Sesión 28](#sesion-28) | Presentación exclusivamente de cuenta | ÍNTEGRO RECUPERADO |
| [Sesión 29](#sesion-29) | Estado operacional neutral del sujeto | ÍNTEGRO RECUPERADO |
| [Sesión 30](#sesion-30) | Narrativa situada por posición operacional | ÍNTEGRO RECUPERADO |
| [Sesión 31](#sesion-31) | Auditoría del framing introductorio de App | ÍNTEGRO RECUPERADO |
| [Sesión 32](#sesion-32) | Introducción explícita de composición | ÍNTEGRO RECUPERADO |
| [Sesión 33](#sesion-33) | Identificación neutral en Supervisión | ÍNTEGRO RECUPERADO |
| [Sesión 34](#sesion-34) | Rótulo neutral de sujeto de sesión | ÍNTEGRO RECUPERADO |
| [Sesión 35](#sesion-35) | Nombre procedente de Experience | ÍNTEGRO RECUPERADO |
| [Sesión 36](#sesion-36) | Auditoría de autoridad por afirmación | ÍNTEGRO RECUPERADO |
| [Sesión 37](#sesion-37) | Reducir atribuciones no acreditadas en Activity | ÍNTEGRO RECUPERADO |
| [Sesión 38](#sesion-38) | Portabilidad del replay e integridad de evidencia | ÍNTEGRO RECUPERADO |

Los temas del índice sirven para localizar sesiones; no certifican que se haya recuperado su prompt. Ningún capítulo pendiente contiene una reconstrucción presentada como original.

---

<a id="sesion-01"></a>

## Capítulo 01 — Inspección arquitectónica del repositorio

**Estado:** instrucción original íntegra.

**Procedencia:** [Architectural assessment — current Convercus](../../../Architectural%20assessment%20-%20current%20Conv.md), líneas 1–20.

SHA-256 del texto fuente extraído: ec4d402ac707f4ea4660ff400a817d299c10d53566ea7d2b0b532315091e2a3f.

<!-- INICIO-TEXTO-ORIGINAL-S01 -->
### INSTRUCCIÓN SESION 1   
Inspect the entire current repository without modifying any files. I am turning this project into a reusable “Convercus Demo Factory” whose purpose is to generate prospect-specific demos on top of the Convercus API.

Produce an architectural assessment containing:

1. current repository structure and technology stack;
2. application entry points;
3. where Convercus API access is implemented;
4. where demo-specific data, branding and configuration currently live;
5. reusable components already present;
6. hard-coded prospect-specific logic;
7. duplicated patterns;
8. current testing and validation mechanisms;
9. environment/configuration dependencies;
10. architectural obstacles to supporting multiple customized demos from a common core.

Do not propose a large refactor yet. First describe the system as it actually exists, distinguish facts from inference, and identify the five most important architectural questions we need to resolve before designing the Demo Factory.

---
---

<!-- FIN-TEXTO-ORIGINAL-S01 -->

**Nota de contraste con el historial:** la versión documental anterior comienza con `Inspect`; el mensaje efectivamente enviado empieza con la errata `nspect`. Se conservan ambos sin corregirlos ni confundir sus procedencias.

**Mensaje original enviado desde VS Code:**

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-01-enviado-original.md) de `2026.zip`, registro `2026/08/03/rollout-2026-08-03T00-01-30-019fc4b6-02f1-7211-8aaa-81c05f4b4129.jsonl`. Mensaje de usuario en la línea 462; texto del propio mensaje. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 0e4221814f9243cbb6efbdf17c68fe7757fc0f515d9ae70786ad96dca0fc57bb.

<!-- INICIO-TEXTO-ORIGINAL-S01-ENVIADO -->
nspect the entire current repository without modifying any files. I am turning this project into a reusable “Convercus Demo Factory” whose purpose is to generate prospect-specific demos on top of the Convercus API.

Produce an architectural assessment containing:

1. current repository structure and technology stack;
2. application entry points;
3. where Convercus API access is implemented;
4. where demo-specific data, branding and configuration currently live;
5. reusable components already present;
6. hard-coded prospect-specific logic;
7. duplicated patterns;
8. current testing and validation mechanisms;
9. environment/configuration dependencies;
10. architectural obstacles to supporting multiple customized demos from a common core.

Do not propose a large refactor yet. First describe the system as it actually exists, distinguish facts from inference, and identify the five most important architectural questions we need to resolve before designing the Demo Factory.
<!-- FIN-TEXTO-ORIGINAL-S01-ENVIADO -->

---

<a id="sesion-02"></a>

## Capítulo 02 — Anatomía semántica y Architecture v0.1

**Estado:** instrucción original íntegra.

**Procedencia:** [Architectural assessment — current Convercus](../../../Architectural%20assessment%20-%20current%20Conv.md), líneas 2698–3343.

SHA-256 del texto fuente extraído: 61770b92853cd7a3790c1689ddf4aa42551f4275394a10a8f58b8820cdd18394.

<!-- INICIO-TEXTO-ORIGINAL-S02 -->
### INSTRUCCIÓN SESION 2

### Convercus Demo Factory — Session 2: Repository Anatomy and Semantic Architecture

#### Purpose of this session

Using the repository assessment already produced, perform a second, deeper architectural analysis of the current Convercus repository.

Do **not** modify any files, generate implementation code, perform a refactor, install dependencies, or redesign the application.

The purpose of this session is to progress through the following cognitive sequence:

**REMEMBER → UNDERSTAND → APPLY → ANALYZE → EVALUATE → CREATE**

The final output should therefore not merely describe the repository. It should reconstruct the current architecture, understand the TES-governed semantic model, test architectural hypotheses against representative commercial scenarios, compare alternatives, and create an evidence-based target architecture hypothesis for the future Demo Factory.

Treat all architectural statements below as **hypotheses to test**, not conclusions to force onto the repository.

---

### 0. Epistemic rules

For every material conclusion, explicitly distinguish between:

* **Repository Fact**
* **TES / Semantic Contract Fact**
* **Architectural Inference**
* **Recommendation**
* **Unresolved / Insufficient Evidence**

Never convert an inference into a fact.

Never invent TES semantics.

When describing `Experience`, participation, events, rules, effects, completion, temporal behaviour, coverage, incentives or related concepts, inspect the actual TES baseline, semantic contracts, product interpretations and shared contracts available in the repository.

Cite the repository files or TES-derived artifacts that support each important semantic conclusion.

If a concept discussed in this instruction is not supported by the repository or TES material, state that explicitly.

---

### BLOOM LEVEL 1 — REMEMBER

#### Reconstruct the current system

Using the previous repository assessment as a starting point, identify the existing artifacts that currently represent or participate in:

* `DemoPackage`
* `AppSnapshot`
* `DataAdapter`
* `MockDataAdapter`
* `ExperienceDefinition`
* participation
* events
* rules
* effects
* capability status
* scenarios
* brand configuration
* application configuration
* demo fixtures/data
* routes
* UI projections
* TES semantic governance
* product interpretations
* shared contracts

For each item provide:

1. current file(s);
2. current responsibility;
3. whether it is executable, declarative, semantic/governance, or test-only;
4. whether it currently participates in runtime composition.

Do not propose changes yet.

The objective of this section is factual reconstruction.

---

### BLOOM LEVEL 2 — UNDERSTAND

#### Reconstruct the semantic model

Study the TES baseline, semantic contracts, product interpretations and shared contracts relevant to `Experience`.

Explain, using the terminology actually present in those sources, how the repository currently understands:

* Experience;
* participation;
* event;
* rule;
* effect;
* state, where applicable;
* completion versus non-completion;
* temporal or sequential behaviour;
* non-sequential behaviour;
* coverage or progress;
* reward;
* incentive;
* consequences/effects of participation or coverage.

Do not assume that all Experiences:

* must be completed;
* must be sequential;
* must produce a reward;
* have identical coverage semantics.

Explicitly determine whether TES supports, rejects, or leaves undefined those possibilities.

Also explain the existing `evaluateEventAcrossExperiences` logic and what it actually establishes semantically versus what remains outside its current implementation.

---

### BLOOM LEVEL 2B — UNDERSTAND THE ACTIVITY HYPOTHESIS

#### Distinguish current Activity from a possible interaction model

The current application contains `ActivityItem` and an Activity Feed.

Do not assume that this current implementation represents a valid universal domain abstraction.

First reconstruct what the existing `Activity`, `ActivityItem`, transactions, events and related concepts actually represent.

Then evaluate the following architectural hypothesis:

> A useful domain-level concept may exist corresponding to the observable interaction trace of a consumer: a set or temporally ordered stream of interactions/events generated through the consumer's relationship with the ecosystem.

For the purposes of analysis, refer to this provisionally as:

**Consumer Interaction Trace**

Do not rename repository entities or assume this term belongs in the final implementation.

Determine whether the repository and TES material support a conceptual separation between:

1. underlying consumer interactions/events;
2. Experience evaluation against those interactions;
3. resulting Experience state/coverage/effects;
4. presentation projections such as an Activity Feed, history or timeline.

Specifically analyze whether the current `ActivityItem` model is:

* a domain object;
* a capability-specific object;
* a UI projection;
* a mixture of these;
* or something else.

Pay particular attention to the current coupling between data and UI concepts such as icons, visual tone and presentation strings.

---

### BLOOM LEVEL 3 — APPLY

#### Apply the semantic model to representative commercial scenarios

Without implementing anything, test the reconstructed domain model against four representative sectors:

##### A. Airline loyalty

Possible interactions may include, only as test examples:

* booking;
* flight;
* ancillary purchase;
* status progression;
* redemption;
* campaign participation.

##### B. Retail loyalty

Possible interactions may include:

* purchase;
* product/category behaviour;
* coupon use;
* referral;
* promotion participation;
* redemption.

##### C. Public transport / sustainable mobility

Possible interactions may include:

* trip;
* route usage;
* mobility challenge;
* participation;
* badge/reward-related effects;
* repeated behavioural patterns.

##### D. Hospitality

Model one hotel chain containing at least two distinct commercial scenarios:

###### Business Hotel Scenario

Examples may include:

* booking;
* stay;
* check-in;
* breakfast;
* repeated stays;
* upgrades;
* meeting-related services;
* late checkout.

###### Vacation Resort Scenario

Examples may include:

* booking;
* stay;
* restaurant consumption;
* spa;
* activities;
* family services;
* excursions;
* engagement with resort experiences.

These interaction examples are analytical probes, not assumed Convercus entities.

For each sector determine whether the same underlying architecture can represent:

* different interaction types;
* different combinations of Experiences;
* different presentation views;
* different incentives;
* different scenario configurations;

without requiring a sector-specific fork of the application.

---

### BLOOM LEVEL 3B — APPLY THE EXPERIENCE / INTERACTION RELATIONSHIP

Test the following hypothesis against TES:

> Consumer interactions may provide the observable factual substrate against which one or more Experiences are evaluated.

Investigate whether a single interaction/event may legitimately contribute to:

* no Experience;
* one Experience;
* multiple Experiences;

according to the existing semantic model.

Also determine whether different Experiences may overlap in the interactions relevant to them.

Do not assume simple set intersection is sufficient.

Explicitly consider whether Experience evaluation may depend on properties such as:

* presence of events;
* ordering;
* timing;
* frequency/count;
* conditions;
* accumulated state;
* coverage;
* other TES-defined rules.

If TES does not support any of these dimensions, state so.

---

### BLOOM LEVEL 4 — ANALYZE

#### Analyze the architecture as a composition system

Treat the following as a working hypothesis:

> `DemoPackage` may evolve into the authoritative composition contract for a demo, while TES remains the semantic authority for domain concepts such as `Experience`.

Analyze whether this separation is coherent with the existing repository.

In particular distinguish:

##### Semantic authority

What defines what an Experience **means**?

##### Composition authority

What defines which Experiences, capabilities, data, brand and scenarios belong to a specific demo?

##### Runtime authority

What decides which adapter, modules and state are active?

##### Presentation authority

What decides how underlying state is displayed?

---

#### Analyze these candidate responsibilities

Produce a responsibility map for:

* DemoPackage
* Demo Runtime
* DataAdapter
* Data source / adapter resolver
* Brand
* Scenario
* Experience
* Consumer Interaction Trace
* Demo Script
* Capabilities / Modules
* Fixtures / Content
* Domain State
* AppSnapshot
* UI projections
* TES / semantic governance

For each responsibility identify:

1. what it should conceptually own;
2. what it should not own;
3. which current repository artifacts could participate;
4. overlaps with existing abstractions;
5. missing boundaries;
6. semantic risks.

---

### Scenario vs Experience vs Demo Script

Explicitly test whether these concepts should remain separate.

#### Scenario

Working definition:

A commercial/demo context describing:

* prospect context;
* actors;
* initial conditions;
* use case;
* business hypothesis;
* relevant configuration.

#### Experience

Must use TES-derived meaning.

Do not redefine it from the working definition of Scenario.

#### Demo Script

Working definition:

An optional presenter-facing sequence used to demonstrate a Scenario.

A Demo Script is necessarily ordered because a presentation occurs through time.

Its ordering must **not imply that the underlying Experience itself is sequential**.

Determine whether this distinction is architecturally useful and semantically safe.

---

### Interaction Trace vs Experience

Analyze the possible relationship:

Consumer Interaction Trace
→ Experience evaluation
→ participation / coverage / state
→ rules / effects
→ incentives or other consequences
→ UI projections

Do not assume this exact pipeline exists in TES.

Determine which parts are:

* supported;
* partially supported;
* inferred;
* unsupported.

---

### DemoPackage vs AppSnapshot

Analyze the current disconnect between `DemoPackage` and `AppSnapshot`.

Explain:

* what each represents today;
* whether one should contain the other;
* whether both should instead depend on a third runtime/domain model;
* whether `AppSnapshot` should remain adapter-facing;
* how Experience-derived state might become visible to the UI without coupling TES directly to React.

Do not redesign either interface prematurely.

---

### BLOOM LEVEL 5 — EVALUATE

#### Evaluate architectural alternatives

Propose **no more than three** alternative composition architectures.

Each alternative must preserve, as far as possible:

* TES semantic authority;
* a shared application core;
* prospect isolation;
* configurable branding;
* multiple scenarios per prospect;
* multiple Experiences per scenario;
* potential reuse of an Experience across scenarios;
* configurable sector-specific interaction content;
* mock/simulation/future API data modes;
* deterministic demo behaviour where required;
* future secure Convercus API integration.

For each architecture evaluate:

##### Semantic fidelity

Does it preserve TES as semantic authority?

##### Reusability

Can new prospects be created mainly through configuration?

##### Sector scalability

Can airline, retail, mobility and hospitality coexist?

##### Scenario flexibility

Can one hotel brand support both business-hotel and resort scenarios?

##### Experience flexibility

Can scenarios use different Experience combinations without redefining Experience?

##### Interaction flexibility

Can the same interaction model support sector-specific interaction types without requiring sector-specific application forks?

##### API evolution

Can mock, simulation and future Convercus API adapters coexist?

##### Complexity

What technical complexity does the model introduce?

##### Marginal Demo Code Cost

Would each additional demo tend to require less new code?

##### Risk

What are the likely failure modes?

---

### Explicitly evaluate the following working principles

Assess whether the evidence supports these principles:

1. **A demo should be an instance of a shared core rather than a fork.**

2. **DemoPackage should be a composition root, not a competing semantic ontology.**

3. **TES should remain the semantic authority for Experience.**

4. **Prospect-specific variation should become configuration unless it represents a genuinely reusable capability.**

5. **Consumer Interaction Trace may be a useful factual substrate from which Experience state can be derived.**

6. **Activity Feed should likely be treated as a presentation projection rather than assumed to be the universal interaction model.**

7. **Scenario, Experience and Demo Script should remain distinct concepts.**

8. **Completion, coverage and incentivization must not be assumed to be equivalent concepts.**

For each principle classify it as:

* strongly supported;
* provisionally supported;
* unsupported;
* contradicted;
* requires further TES clarification.

---

### BLOOM LEVEL 6 — CREATE

#### Create an evidence-based target architecture hypothesis

Without generating implementation code, create a proposed **Demo Factory Architecture v0.1**.

This is not yet an implementation specification.

It should contain:

##### 1. Architecture map

Show the proposed relationships between:

* TES;
* semantic/product contracts;
* DemoPackage;
* Scenario;
* Experience;
* interaction/event state;
* DataAdapter;
* runtime;
* capabilities/modules;
* domain/application state;
* UI projections.

##### 2. Authority map

Explicitly state which layer is authoritative for:

* semantic meaning;
* demo composition;
* data acquisition;
* Experience evaluation;
* runtime state;
* presentation;
* branding;
* scenario configuration.

##### 3. Core invariants

Propose a small set of architectural invariants that future implementation should not violate.

Example form:

> “Adding a new prospect must not require redefining TES domain concepts.”

Do not simply copy this example; derive the invariants from the evidence.

##### 4. Minimum viable architectural transition

Identify the **minimum architectural changes** required to make a second prospect demo possible without copying or forking the application.

Do not implement them.

Order them by dependency, not by coding convenience.

##### 5. Explicit non-goals

Identify what should **not** be refactored or built yet.

Include consideration of:

* large-scale UI decomposition;
* CSS redesign;
* backend implementation;
* API integration;
* multi-tenancy;
* production connectivity;
* unnecessary state-management frameworks;
* Experience Builder implementation.

##### 6. Open semantic questions

List all remaining TES/domain questions that must be resolved before implementation.

Do not hide unresolved semantic uncertainty behind architectural abstractions.

##### 7. Architecture Decision candidates

Identify the decisions that are now mature enough to become future ADRs.

Do not write the ADRs yet.

---

### Final architectural stress test

Before concluding, use the Hospitality case as the hardest current test.

Assume:

One hotel company
→ one brand or brand family
→ Business Hotels + Vacation Resorts
→ multiple Scenarios
→ potentially overlapping Experiences
→ different interaction patterns
→ potentially different incentives
→ potentially different UI projections.

Determine whether Demo Factory Architecture v0.1 can represent this without:

* creating two separate applications;
* redefining Experience;
* introducing business-hotel-specific or resort-specific core domain types unnecessarily;
* forcing all interaction events into a single generic UI-oriented `ActivityItem`;
* assuming all Experience progress is sequential;
* assuming completion necessarily produces a reward.

If the architecture fails this test, explain where and revise the architecture hypothesis before completing the report.

---

### Output structure

Use exactly this top-level structure:

1. Executive conclusion
2. Bloom 1 — Repository reconstruction
3. Bloom 2 — Semantic understanding
4. Bloom 2B — Activity / Consumer Interaction Trace
5. Bloom 3 — Sector application
6. Bloom 3B — Interaction-to-Experience evaluation
7. Bloom 4 — Architectural analysis
8. Bloom 5 — Alternative evaluation
9. Bloom 6 — Demo Factory Architecture v0.1
10. Minimum transition path
11. Explicit non-goals
12. Open TES / semantic questions
13. Candidate ADRs
14. Final hospitality stress test
15. Confidence and evidence gaps

Do not modify repository files.

Do not generate implementation code.

Do not begin the refactor.

The purpose of Session 2 is to move from **repository knowledge** to **semantic understanding**, then to **architectural analysis**, **evaluation**, and finally a defensible **architecture hypothesis**.

---
---


<!-- FIN-TEXTO-ORIGINAL-S02 -->

**Contraste con el historial:** el [adjunto realmente enviado](instrucciones-recuperadas/sesion-02-enviado-original.md) coincide íntegramente con el texto de la instrucción anterior, sin la cabecera «INSTRUCCIÓN SESION 2» ni los separadores añadidos en el documento histórico. Sus lecturas registradas abarcan las 640 líneas indicadas por `wc -l`. No se duplica aquí ese mismo cuerpo.

**Instrucción complementaria posterior — interpretación de ocurrencia, traza y evento:**

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-02-interpretacion-original.md) de `2026.zip`, registro `2026/08/03/rollout-2026-08-03T00-01-30-019fc4b6-02f1-7211-8aaa-81c05f4b4129.jsonl`. Mensaje de usuario en la línea 559; texto del propio mensaje. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 5fe21d3b35586baff78da71ceb1e72977837a0dd95ae609b46b8db6805f672a0.

<!-- INICIO-TEXTO-ORIGINAL-S02-INTERPRETACION -->
Create one new product-interpretation document in:

`01-semantic-contract/product-interpretations/observed-occurrence-trace-event.md`

Do not modify TES source excerpts, the TES baseline, Ontology, Ledger, Lexicon, Protocol, TypeScript, tests, configuration or application code.

The document must record the product interpretation resulting from the TES review concerning Activity, observable occurrences, traces and TES Events.

Use the following governing status:

**Product interpretation subordinate to TES — not a TES extension.**

The document must make explicit that:

1. Demo Factory must **adapt the product layer** to a distinction already contained in TES; it is not correcting or extending TES.
2. TES establishes that not every observable fact is a significant Event.
3. For product purposes, Demo Factory may provisionally represent an observable fact as an `Observed Occurrence`, but this is a product/technical construct and not a new TES entity.
4. A `Trace` belongs to the instrumentation/reconstruction plane and provides evidence that an occurrence, condition or transition occurred. Trace and TES Event are not equivalent.
5. TES Event significance is contextual to an Experience and must not be treated as an unconditional intrinsic property of an observed occurrence.
6. A product architecture may need to support one observed occurrence being evaluated relative to zero, one or multiple Experiences. Mark this explicitly as a product interpretation strongly compatible with TES, not an explicit TES cardinality rule.
7. Preserve two different planes:

   Instrumentation / reconstruction:\
   `Observed Occurrence → Trace → contextual recognition / confirmation`

   TES experiential plane:\
   `Event → Pattern → Sequence → Progression → Result → Measurement → Learning`

   The first may feed the second but must not be inserted into the TES Experience Ledger as additional ontological stages.
8. `Pattern` must remain the TES concept for regularity emerging from relations between Events. A collection or trace of occurrences is not automatically a Pattern.
9. `Activity` must be treated as a read model / presentation projection rather than a sovereign semantic or factual source.
10. Do not equate occurrence accumulation, Pattern, Sequence, Progression, Completion, Result, Incentive or Reward.

Add a separate section titled:

`Analytical hypothesis — coverage`

This section must state that `coverage` is inspired by set-covering theory and is NOT a TES concept.

Record two distinct analytical questions:

A. **Observed-field coverage**

Given an observed occurrence universe `U` and subsets `S_E` associated with Experiences, unions/intersections/uncovered elements may be useful for analyzing Experience overlap, redundancy and portions of observable behaviour not related to any Experience.

B. **Experience evidence/requirement coverage**

The degree to which evidence or structural requirements of one Experience have been satisfied is a different problem and must not be conflated with observed-field set coverage.

Do not define either as TES Progression and do not assume percentage representation is valid.

Mark the usefulness of both coverage notions as **subject to adversarial falsification in Demo Factory Session 3**.

Finally include a reopening condition:

TES should only be reconsidered if a concrete case cannot be coherently represented using the existing distinction:

`observable occurrence / trace → contextual recognition as TES Event`

and therefore provides actual evidence of a semantic gap.

After creating the document, report only:

- the path created;
- the headings created;
- whether any other files were modified.

Do not make any other repository change.
<!-- FIN-TEXTO-ORIGINAL-S02-INTERPRETACION -->

---

<a id="sesion-03"></a>

## Capítulo 03 — Revisión adversarial de Architecture v0.1

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-03-original.md) de `2026.zip`, registro `2026/08/03/rollout-2026-08-03T00-01-30-019fc4b6-02f1-7211-8aaa-81c05f4b4129.jsonl`. Mensaje de usuario en la línea 587; salida(s) de lectura en la(s) línea(s) 593, 597, 600. Cotejado con el recuento histórico de 552 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 0317d377caccf83fdec7866d1353cb667f3a37f76b2ea2a2c083fc4e95a93edf.

<!-- INICIO-TEXTO-ORIGINAL-S03 -->
### Convercus Demo Factory — Session 3: Adversarial Architecture Review and ADR Falsification

#### Purpose

Session 2 produced an evidence-based Demo Factory Architecture v0.1.

Session 3 must NOT defend that architecture.

Your role in this session is to act as an **adversarial architecture reviewer** whose objective is to falsify, weaken or qualify the proposed architectural conclusions wherever the repository, TES corpus, product requirements or realistic commercial scenarios provide sufficient counter-evidence.

Do not modify application code.

Do not begin the refactor.

Do not implement the ADRs.

Do not assume that a conclusion is correct merely because you proposed it in Session 2.

The cognitive progression for this session is:

**ANALYZE → EVALUATE → CREATE**

The required outcome is a set of architectural decisions that have survived explicit attempted falsification.

---

### Epistemic discipline

For every material claim distinguish:

* Repository Fact
* TES / Semantic Contract Fact
* Product Interpretation
* Architectural Inference
* Analytical Construct
* Recommendation
* Counterexample
* Unresolved / Insufficient Evidence

A previous recommendation is not evidence.

A previous architecture diagram is not evidence.

Prefer primary repository/TES evidence over conclusions from the Session 2 report.

Where necessary, return to the underlying repository files and TES-derived sources.

---

### New product interpretation to test

A product-level interpretation has now been adopted provisionally:

#### Observed Occurrence / Trace / TES Event

TES is not being extended.

The working product interpretation is:

* observable reality may produce an **Observed Occurrence**;
* instrumentation may preserve a **Trace** allowing occurrence reconstruction/confirmation;
* an occurrence becomes a TES Event only through relevant contextual recognition within an Experience;
* Activity is a read model/presentation projection and not a semantic source of truth.

Do not assume this realization is architecturally correct merely because it is semantically compatible with TES.

Attempt to falsify the way Demo Factory proposes to materialize this distinction.

---

### Coverage analytical hypothesis

`Coverage` is NOT a TES term in this architecture.

It is a candidate analytical construct inspired by set-covering theory.

One possible analytical model is:

* `U`: set of observed occurrences inside a defined scenario/time/context;
* `S_E ⊆ U`: subset of occurrences recognized as relevant in relation to Experience `E`;
* a family of Experiences produces a family of subsets `{S_E}` whose union and intersections may be analytically useful.

This may allow questions such as:

* what parts of the observed behavioural field are related to no Experience?
* which occurrences are related to several Experiences?
* how much overlap exists between Experiences?
* what observable field is addressed by a portfolio of Experiences?

This construct must NOT be assumed to measure:

* TES Progression;
* Completion;
* Result;
* Experience state.

A second possible meaning —the extent to which evidence or structural requirements of one Experience have been satisfied— is analytically different and must not be conflated with set coverage of observed occurrences.

Your task is to determine whether either notion of coverage adds genuine analytical value or merely introduces misleading mathematical language.

---

### ADR candidates under review

Attempt to falsify the following six candidate decisions.

---

### ADR-001 — TES Semantic Authority

#### Candidate proposition

TES remains the authoritative source for the meaning of Experience and its core experiential categories.

Product contracts, runtime models and DemoPackage composition must remain subordinate to TES and traceable to it.

##### Attempted falsification

Search for cases where:

* TES is too abstract to govern an executable demo;
* product semantics necessarily diverge;
* different technical implementations require contradictory interpretations;
* versioning TES could make runtime packages unstable;
* Demo Factory would need concepts TES explicitly excludes;
* strict subordination to TES could prevent legitimate product extensions.

Determine what authority TES should possess and where that authority must stop.

---

### ADR-002 — DemoPackage as Composition Root

#### Candidate proposition

`DemoPackage` should become the authoritative composition root of a demo.

It may reference rather than embed:

* prospect identity;
* brand;
* scenarios;
* Experiences;
* capabilities;
* fixtures;
* content;
* adapter policy;
* modules;
* Demo Scripts;
* reset policy.

It must not redefine TES semantic concepts.

##### Attempted falsification

Search for cases where:

* DemoPackage becomes an oversized “god configuration”;
* runtime concerns leak into configuration;
* Experience versions and Scenario versions conflict;
* one prospect requires several packages rather than one;
* live API state cannot be reconciled with immutable package composition;
* package references make reproducibility worse;
* deployment concerns should be authoritative instead.

Determine whether DemoPackage truly deserves composition-root authority or whether another boundary is needed.

---

### ADR-003 — Separation of Scenario / Experience / Demo Script

#### Candidate proposition

Keep three concepts distinct:

##### Scenario

Commercial/demo context, actors, initial conditions, relevant configuration and use case.

##### Experience

TES-governed situated transformation.

##### Demo Script

Optional presenter-facing sequence used to demonstrate a Scenario.

##### Attempted falsification

Search for:

* cases where Scenario and Experience cannot be separated cleanly;
* Experiences that only make sense inside one prospect context;
* multiple Scripts requiring different runtime states;
* Scripts that must cause domain actions and therefore are not merely presentation;
* hospitality cases with group participation;
* scenario reuse across brands or Experiences;
* cases where separation creates excessive indirection.

Determine whether all three abstractions are necessary and which dependencies between them are legitimate.

---

### ADR-004 — Observed Occurrence / Trace / TES Event / Projection

#### Candidate proposition

Demo Factory should preserve observed occurrences and traces independently from their contextual recognition as TES Events.

Activity and other UI views are derived projections.

Candidate invariants:

1. Observed Occurrence is a product/technical concept, not a new TES entity.
2. Occurrence does not automatically imply TES Event.
3. Trace supports reconstruction/confirmation but does not replace the Event.
4. Significance is contextual to an Experience.
5. One occurrence may potentially relate to zero, one or multiple Experiences.
6. Interpretation must not overwrite the original factual occurrence.
7. UI projections cannot become canonical factual records.
8. Pattern cannot be reduced to a collection of occurrences.
9. Progression cannot be inferred from accumulation alone.

##### Attempted falsification

Look for counterexamples involving:

* occurrences that are inherently Experience-specific;
* system-generated events that already arrive semantically classified;
* corrections or retractions;
* duplicate occurrences;
* late-arriving events;
* unreliable traces;
* inferred rather than observed events;
* multiple sources describing the same occurrence;
* aggregated events;
* privacy constraints preventing preservation of raw occurrences;
* an API that exposes only already-interpreted events;
* Experiences whose event cannot be mapped to one discrete occurrence;
* patterns that are recognized without storing all constituent occurrences.

Also challenge the proposed many-to-many relationship between occurrence and Experience.

Determine whether it is:

* structurally necessary;
* merely convenient;
* contradicted by TES;
* or dependent on product use case.

---

### Coverage falsification experiment

Treat coverage separately from ADR-004.

Test the set-cover adaptation critically.

#### Model A — Observed-field coverage

Given:

`U = observed occurrences`

and:

`S_E = occurrences related to Experience E`

evaluate whether:

* unions;
* intersections;
* uncovered occurrences;
* overlap density;
* minimal covering Experience sets;

could produce useful product, commercial or analytical information.

Potential questions include:

* Are there meaningful customer behaviours that no Experience currently addresses?
* Are several Experiences responding to substantially the same observable behaviour?
* Does the Experience portfolio contain redundancy?
* Which Experiences collectively relate to the largest relevant behavioural field?

#### Model B — Experience requirement/evidence coverage

Separately evaluate whether it is legitimate or useful to represent how much of an Experience's required evidence/structure has been satisfied.

Do NOT assume that a percentage is appropriate.

Take into account:

* Pattern;
* Sequence;
* Progression;
* ordinal constraints;
* state transitions;
* qualitative evidence;
* TES reconstructibility.

#### Required decision

For each model classify coverage as:

* useful analytical construct;
* useful only under strict constraints;
* misleading abstraction;
* redundant with existing TES/product concepts;
* insufficient evidence.

If retained, propose terminology that explicitly prevents confusion with TES Progression.

---

### ADR-005 — Runtime State / Read Models

#### Candidate proposition

Separate:

1. immutable/versioned demo composition;
2. canonical mutable runtime state;
3. read models/UI projections.

`AppSnapshot` may survive as a read model but should not simultaneously represent backend response, canonical truth and presentation.

##### Attempted falsification

Search for:

* unnecessary state duplication;
* synchronization problems;
* simple demos where canonical runtime state adds no value;
* adapters capable of supplying read models directly;
* offline/reset constraints;
* simulation vs live state conflicts;
* Experience state that cannot be reconstructed deterministically;
* excessive projection complexity.

Determine the minimum state architecture required for Demo Factory rather than designing an enterprise event platform prematurely.

---

### ADR-006 — Data Adapter Resolution

#### Candidate proposition

The runtime should resolve data adapters during demo bootstrap/composition rather than instantiate `MockDataAdapter` directly inside the application.

Adapters should provide the boundary between external/simulated data and domain/runtime processing.

##### Attempted falsification

Test:

* whether one adapter per demo is sufficient;
* whether adapters should instead be capability-specific;
* whether one demo needs multiple concurrent adapters;
* whether an adapter should expose occurrences, canonical state, read models, or all three;
* whether a Convercus API could invalidate the current generic `DataAdapter<TSnapshot,TEvent>` abstraction;
* whether hybrid real/simulated demonstrations require adapter orchestration;
* whether adapter resolution belongs in DemoPackage or another policy layer.

Do not design the production Convercus adapter before verifying the real API.

---

### Cross-ADR falsification

Do not review each ADR only in isolation.

Search for contradictions between them.

Examples:

* Does DemoPackage composition conflict with runtime adapter discovery?
* Can an immutable package coexist with live mutable capabilities?
* Does Scenario need to own fixtures that Runtime also considers canonical?
* Does the occurrence model duplicate adapter data?
* Could TES authority make product contracts impossible to version independently?
* Can one Activity projection combine real and simulated sources without misleading users?
* Does deterministic reset conflict with live data?
* Does one prospect with multiple hotel scenarios require separate packages?

Identify hidden coupling across ADRs.

---

### Sector stress tests

Use the same architecture against:

* airline loyalty;
* retail loyalty;
* public transport / sustainable mobility;
* hospitality.

Hospitality remains the hardest current stress test.

Assume one hotel group contains:

* business hotels;
* vacation resorts;
* potentially different sub-brands;
* individual and group actors;
* booking/stay/group contexts;
* Experiences potentially reused across scenarios;
* shared occurrences relevant to multiple Experiences;
* different incentives and UI projections.

Attempt to construct cases that break each ADR.

Do not protect the architecture from the scenario.

Allow the scenario to falsify it.

---

### BLOOM LEVEL 4 — ANALYZE

For each ADR:

1. decompose its assumptions;
2. identify dependencies;
3. identify what evidence supports it;
4. identify what evidence is merely inferred;
5. identify potential counterexamples;
6. identify interaction with the other ADRs.

Do not approve or reject yet.

---

### BLOOM LEVEL 5 — EVALUATE

For every ADR assign one of:

* **SURVIVES**
* **SURVIVES WITH QUALIFICATION**
* **REVISE**
* **DEFER**
* **REJECT**

For every verdict provide:

* strongest supporting evidence;
* strongest falsifying evidence;
* unresolved assumptions;
* consequences of being wrong;
* confidence level.

A decision may only be classified as `SURVIVES` if you attempted to find material counterexamples first.

---

### BLOOM LEVEL 6 — CREATE

After adversarial evaluation, create:

#### A. Revised architecture decision set

Only include decisions that survived or were successfully revised.

#### B. Rejected assumptions

List ideas from Sessions 1–2 that should no longer guide implementation.

#### C. Deferred questions

Identify decisions requiring:

* API evidence;
* TES clarification;
* product validation;
* real prospect use;
* implementation experiment.

#### D. Revised Demo Factory Architecture v0.2

Produce an architecture map reflecting only surviving decisions.

Do not preserve Architecture v0.1 merely for continuity.

#### E. ADR readiness

For each surviving decision classify it as:

* ready to write as ADR;
* provisional ADR;
* not ready for ADR.

#### F. Minimum reversible experiment

Propose the smallest implementation experiment that could test the architecture after the ADRs are approved.

The experiment must be reversible and must not require:

* full API integration;
* Experience Builder;
* multi-tenant backend;
* full UI refactor.

Prefer a test involving two prospect configurations on the same shared core.

Do not implement it.

---

### Final meta-review

Before concluding, answer:

1. Which architecture assumption from Session 2 was easiest to falsify?
2. Which survived the strongest attack?
3. Which assumption remains most dangerous despite appearing reasonable?
4. What are we most likely to be over-engineering?
5. What are we most likely to be under-modeling?
6. Did the set-cover-inspired `coverage` hypothesis add analytical value or merely new terminology?
7. What evidence would most likely cause Architecture v0.2 to be revised again?

---

### Required output structure

1. Executive adversarial verdict
2. Evidence hierarchy
3. ADR-001 falsification
4. ADR-002 falsification
5. ADR-003 falsification
6. ADR-004 falsification
7. Coverage falsification experiment
8. ADR-005 falsification
9. ADR-006 falsification
10. Cross-ADR contradictions
11. Sector stress tests
12. Revised decision matrix
13. Rejected assumptions
14. Deferred questions
15. Demo Factory Architecture v0.2
16. ADR readiness
17. Minimum reversible experiment
18. Meta-review
19. Confidence and evidence gaps

Do not modify application code.

Do not implement the proposed experiment.

The purpose of Session 3 is not to produce more architecture.

The purpose is to determine which parts of the architecture remain defensible **after an explicit attempt to prove them wrong**.
<!-- FIN-TEXTO-ORIGINAL-S03 -->

---

<a id="sesion-04"></a>

## Capítulo 04 — ADR mínimos y experimento reversible

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-04-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 9; salida(s) de lectura en la(s) línea(s) 17, 21. Cotejo adicional: adjunto repetido con hashes históricos. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 2074812206902e385128d90cfa3c86f018850a41fa52007be4e37420330ae795.

<!-- INICIO-TEXTO-ORIGINAL-S04 -->
### Convercus Demo Factory — Session 4: ADR Formalization and Minimum Reversible Experiment Specification

#### Purpose

Session 3 completed the adversarial falsification of Architecture v0.1 and produced Architecture v0.2.

Do not perform another broad architecture redesign.

Do not implement the experiment yet.

Session 4 has two objectives:

1. formalize only the architectural decisions that are sufficiently mature;
2. transform the remaining provisional decisions into explicit hypotheses to be tested by a minimum reversible implementation experiment.

The cognitive emphasis is:

**CREATE → prepare for APPLY**

---

### Part A — Formalize mature ADRs

Create exactly two ADRs.

Before creating them, inspect the repository's existing governance/decision conventions and follow them where applicable.

Do not invent a new ADR format if the repository already defines one.

#### ADR-001 — Bounded TES Semantic Authority

Formalize the surviving decision that:

* TES is authoritative for the semantic meaning, relations and invariants of Experience and its governed concepts;
* TES is not authoritative for software architecture, persistence, APIs, deployment, privacy, caches or provider implementation;
* product and technical extensions are permitted where they:

  * are explicitly classified as non-TES;
  * do not silently redefine TES concepts;
  * preserve semantic traceability where they operationalize Experience;
* Experience definitions must identify the TES baseline/version against which they were validated;
* TES baseline changes must not silently reinterpret existing versioned Experience definitions.

Include:

* context;
* decision;
* scope of authority;
* consequences;
* prohibited interpretations;
* versioning implications;
* conditions that could force reconsideration.

---

#### ADR-002 — Logical Separation of Composition, Runtime State and Read Models

This ADR corresponds to the revised Session-3 decision previously associated with ADR-005.

Formalize the decision that Demo Factory must distinguish logically between:

1. **composition/configuration** — what demo is intended;
2. **runtime state** — mutable state controlled or referenced during execution when required;
3. **read models / projections** — structures prepared for UI/presentation.

Important qualification:

This decision does NOT require three physical stores or copies of all data.

Different demo modes may use different minimal realizations:

* static/mock → direct read model may be sufficient;
* simulation → local state + projections;
* hybrid → external state reference + local overlay;
* live → external source may remain authoritative.

Include explicit consequences for:

* `AppSnapshot`;
* Activity;
* reset semantics;
* external sources;
* avoiding unnecessary event-platform architecture.

---

### Part B — Record provisional architecture hypotheses

Do NOT convert the following into accepted ADRs yet.

Create a Session-4 experiment hypothesis document recording four provisional decisions.

#### H1 — Demo Manifest + Effective Bootstrap Composition

Hypothesis:

A small versioned demo manifest should declare desired logical composition, while bootstrap/deployment policy resolves the effective composition.

Test:

* multiple demos per prospect;
* versioned references;
* no secrets in manifest;
* requested vs resolved capabilities;
* failure of invalid references.

---

#### H2 — Scenario / Experience / Demo Script Separation

Hypothesis:

These concepts remain distinct but can depend on one another:

`Experience Definition ← Scenario ← Demo Script`

Test:

* optional Scenario;
* optional Demo Script;
* hospitality context;
* multiple actors;
* different initial checkpoints;
* Script invoking public actions without implementing domain rules.

Do not attempt to solve the complete Experience participation model.

---

#### H3 — Evidence / Occurrence / TES Event / Activity Projection

Hypothesis:

The product must preserve the semantic distinction between factual/evidentiary input and TES Event interpretation without requiring every concept to exist as a separate persisted object.

Test only what is needed for the two-demo experiment.

Do NOT build a general occurrence/evidence event store.

Activity must remain a projection/read model.

---

#### H4 — Provider Resolution by Capability

Hypothesis:

Providers should be resolved outside `App.tsx`, potentially at capability/port level, rather than assuming one universal adapter per demo.

For the experiment, do not design the future provider architecture.

Use the existing mock implementation where possible while introducing only the smallest seam required to test external resolution.

---

### Part C — Preserve coverage as experimental analytics only

Do not create an ADR for coverage.

Record two separate experimental analytical ideas:

##### Observation overlap

Provisional term:

**Experience-portfolio observation overlap**

Purpose:

Explore overlap/unrelated observed occurrences across Experience evaluations.

##### Evidence sufficiency

Provisional term:

**Experience evidence sufficiency profile**

Purpose:

Represent sufficient / insufficient / contradictory / pending evidence without claiming TES Progression.

Neither should be implemented in the minimum experiment.

---

### Part D — Specify the Minimum Reversible Experiment

Design, but do not implement, the smallest experiment that tests H1–H4.

#### Experimental principle

**Two demos. One core. No forks.**

##### Demo A — Retail baseline

Remain close to the current prototype.

Use the current general application behaviour where possible.

##### Demo B — Hospitality

Create a genuinely different prospect configuration that stresses the architecture.

It must support at minimum:

* different brand;
* different content;
* different fixture data;
* hospitality-specific Scenario;
* booking/stay context;
* more than one actor or subject reference;
* different visible module/configuration choices where useful.

It does not need a full hotel Experience engine.

---

### Experiment acceptance criteria

The specification must include tests proving that:

1. the same application core can start both demos;
2. switching demo does not require editing application code;
3. no prospect brand/content/fixture leaks into the other demo;
4. one prospect can conceptually own multiple demos;
5. manifest/configuration declares desired composition;
6. bootstrap resolves effective composition;
7. invalid or missing references fail explicitly;
8. brand is resolved from configuration rather than hard-coded Convercus identity;
9. fixtures are external to the mock provider implementation;
10. provider resolution happens outside `App.tsx`;
11. Activity remains a read model;
12. capability provenance can be represented;
13. reset remains deterministic for locally controlled mock state;
14. hospitality can represent booking/stay context and multiple actors without making `memberId` universal;
15. Demo Script, if included, invokes a public action boundary rather than directly mutating internal state.

---

### Reversibility requirement

The experiment must be removable without:

* database migration;
* backend cleanup;
* API cleanup;
* TES modification;
* Experience Builder modification;
* widespread UI rollback.

Identify precisely which files would be added or minimally changed.

Do not modify them yet.

---

### Explicit non-goals

The experiment must not include:

* live Convercus API integration;
* production authentication;
* backend implementation;
* generic event sourcing;
* general occurrence/evidence store;
* complete Experience engine;
* complete participation lifecycle;
* coverage calculation;
* Experience Builder;
* production multi-tenancy;
* broad React component refactor;
* design-system rewrite;
* global state-management framework unless absolutely required by the experiment.

---

### Implementation sequence proposal

Produce a dependency-ordered implementation plan for the future Session 5.

Prefer very small steps with verification after each one.

For each future step state:

* purpose;
* expected files affected;
* test/validation;
* rollback path;
* architectural hypothesis being tested.

Do not execute the steps.

---

### Final pre-implementation review

Before concluding Session 4 answer:

1. identify whether either of the two ADRs still contains an unresolved assumption that should prevent acceptance;
2. identify whether the proposed experiment is testing architecture or merely implementing it;
3. remove any experimental feature that is not needed to falsify H1–H4;
4. identify the single most informative failure the experiment could produce;
5. state what result would cause each hypothesis H1–H4 to be rejected.

---

### Required output

1. Session 4 executive conclusion
2. ADR-001
3. ADR-002
4. Provisional hypotheses H1–H4
5. Experimental analytics status
6. Minimum reversible experiment specification
7. Acceptance criteria
8. Files expected to change
9. Dependency-ordered Session-5 implementation plan
10. Rejection criteria for H1–H4
11. Remaining uncertainties
12. Go / No-Go recommendation for implementation

Only create the two approved ADR documents and the Session-4 hypothesis/experiment specification document.

Do not modify application code.

Do not implement the experiment.
<!-- FIN-TEXTO-ORIGINAL-S04 -->

---

<a id="sesion-05"></a>

## Capítulo 05 — Implementar el experimento mínimo de dos demos

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-05-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 209; salida(s) de lectura en la(s) línea(s) 217, 221. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 0a581e9054c3e9fec389855ae93b503856f4f7d06047e979e1ba2542ba90d8cf.

<!-- INICIO-TEXTO-ORIGINAL-S05 -->
### Convercus Demo Factory — Session 5: Minimum Reversible Experiment Implementation

#### Purpose

Session 4 produced:

* ADR-001 — Bounded TES Semantic Authority
* ADR-002 — Logical Separation of Composition, Runtime and Read Models
* H1–H4 provisional architecture hypotheses
* a Minimum Reversible Experiment specification

Session 5 is the first implementation session.

Do NOT implement Demo Factory as a complete platform.

Do NOT generalize beyond what the experiment requires.

Your goal is to implement the smallest reversible change capable of testing H1–H4.

The cognitive cycle for this session is:

**APPLY → TEST → EVALUATE**

Implementation is evidence generation.

---

### Governing principle

Implement:

**Two demos. One core. No forks.**

The two demos are:

1. the existing retail-like baseline;
2. a new hospitality demo designed to stress configuration boundaries.

Do not create a separate React application for hospitality.

Do not duplicate the application core.

Do not redesign the repository globally.

---

### Existing architecture decisions

Respect the accepted ADRs.

#### ADR-001

TES governs semantic meaning and invariants.

Do not modify:

* TES source excerpts;
* TES Ontology;
* Experience Ledger;
* Lexicon;
* Protocol;

unless the experiment discovers a genuine semantic contradiction.

No such modification is expected in Session 5.

#### ADR-002

Maintain logical separation between:

* composition/configuration;
* mutable runtime state where needed;
* read models/projections.

This does NOT require three physical stores.

Use the smallest realization appropriate for the experiment.

---

### Hypotheses under test

#### H1 — Demo Manifest + Effective Bootstrap Composition

Test whether a small declarative demo configuration can describe desired composition while bootstrap resolves the effective composition.

The experiment must show:

* more than one demo can exist;
* a prospect is not hard-coded to one demo;
* requested configuration and resolved runtime are distinguishable;
* invalid references fail explicitly;
* secrets or environment implementation details do not live in the demo manifest.

Do not create a large universal configuration schema.

---

#### H2 — Scenario / Experience / Demo Script Separation

Test only the minimum needed to preserve the distinction.

Hospitality should be able to declare:

* a Scenario;
* booking/stay context;
* multiple actors or subject references;
* initial fixture state.

A Demo Script may exist if useful.

If implemented, it may invoke a public application/demo action.

It must not:

* implement Experience rules;
* directly mutate hidden internal state;
* become a second application controller.

Do not implement a complete Experience participation model.

---

#### H3 — Evidence / Occurrence / TES Event / Activity Projection

Do NOT build a general occurrence/evidence/event store.

For this experiment:

* preserve Activity as a read model / presentation projection;
* ensure fixture/domain input is not defined as Activity UI objects where avoidable;
* avoid adding visual concerns such as icon/tone to factual input solely because the Activity screen needs them.

Only introduce the smallest additional representation necessary if the hospitality scenario genuinely requires it.

Do not force separate persisted objects for:

* occurrence;
* trace;
* TES Event;
* evaluation.

Conceptual distinction does not require universal storage separation.

---

#### H4 — Provider Resolution

Remove the requirement that `App.tsx` directly decides the demo's data implementation.

Introduce the smallest external resolution seam necessary.

For this experiment:

* reuse the current mock behaviour where possible;
* make the mock provider receive demo-specific fixtures/configuration;
* resolve the appropriate demo/provider before or during application bootstrap;
* do not design the final provider architecture;
* do not create a universal provider framework.

The experiment should make future provider-by-capability architecture possible without implementing it now.

---

### Demo A — Retail baseline

Preserve current behaviour as closely as reasonably possible.

The purpose of Demo A is regression control.

Where possible retain:

* current member concept;
* benefits;
* news/content;
* Activity presentation;
* current mock interactions.

Move only the data/configuration that must move in order to prove separation from the core.

Do not rewrite the retail demo for architectural purity.

---

### Demo B — Hospitality stress demo

Create a clearly distinct hospitality demo configuration.

It must differ materially from the retail demo in at least:

* brand identity;
* visible content;
* fixture data;
* Scenario;
* actor/context structure.

Use a realistic but minimal hospitality scenario.

Example structure:

Hotel group / property context

Primary actor:
business traveller or resort guest

Additional actor/context:
booking, stay or related guest

Possible fixture information:

* guest identity;
* booking reference;
* property;
* arrival/departure;
* stay context;
* one or more hotel services;
* one or two Activity/read-model items.

Do not create a complete hotel loyalty model.

Do not create hospitality-specific core domain classes unless the experiment proves a generic representation cannot support the case.

---

### Subject and context constraint

The hospitality demo must prove that the core does not require:

`memberId`

to be the universal identifier of all contextual state.

Do not solve the complete subject ontology.

A minimal extensible reference may be enough.

Prefer the smallest representation that permits the experiment to express:

* individual;
* booking/stay context;
* more than one actor/reference.

Document any compromise.

---

### Brand resolution

The hospitality demo must use a different brand configuration.

Remove only the hard-coded Convercus-brand assumptions necessary for the experiment.

Brand selection must originate from demo configuration/resolution rather than requiring source-code edits to switch demos.

Validate at minimum:

* brand identifier;
* required assets/tokens;
* fallback/error behaviour.

Do not build a complete design system.

---

### Fixture separation

Move prospect-specific fixture content out of `MockDataAdapter`.

The provider should simulate behaviour using supplied fixture/configuration.

It should not own:

* Alex Martín;
* retail-specific benefits;
* retail-specific news;
* hospitality guest data;
* prospect-specific narrative.

Prefer explicit fixture inputs.

Avoid premature universal fixture schemas.

---

### Demo selection

Use the smallest explicit mechanism suitable for testing two demos.

Possible mechanisms may include:

* query parameter;
* path;
* build/runtime config;
* another existing lightweight mechanism.

Choose the least invasive option.

Document why it was selected.

Do not interpret this experiment as a final decision between:

* runtime demo registry;
* separate builds;
* production multi-tenancy.

That remains unresolved.

---

### Capability provenance

Preserve the ability to declare the provenance/reality status of visible capabilities.

At minimum support the existing vocabulary where applicable:

* real;
* simulated;
* mocked;
* proposed;
* unsupported.

The experiment may use only a subset.

Do not build a full disclosure UI unless needed.

The important requirement is that provenance is representable and does not depend on one global `dataMode`.

---

### Activity

Activity must continue to work in both demos.

But:

* Activity is a read model;
* hospitality input should not have to become an `ActivityItem` merely to exist;
* visual fields belong to projection/presentation where reasonably possible.

Do not perform a broad Activity refactor.

Only introduce the minimum separation required by the experiment.

---

### Reset

Retail and hospitality locally controlled mock state must reset deterministically.

Reset applies only to state controlled by the demo.

Do not generalize this to future live providers.

Prove that resetting Demo A cannot mutate Demo B state and vice versa.

---

### Validation and failure behaviour

Bootstrap/configuration must fail explicitly for materially invalid configuration.

At minimum test:

* unknown demo id;
* missing referenced brand;
* missing required fixture;
* incompatible or unresolved configuration where applicable.

Avoid silent fallback that could accidentally display another prospect's data.

---

### Isolation requirements

The experiment must verify that:

* retail assets/content do not appear in hospitality;
* hospitality assets/content do not appear in retail;
* fixture state is isolated;
* reset is isolated;
* demo selection is explicit;
* no implicit "default prospect leakage" occurs.

---

### Testing strategy

Add only the tests necessary to demonstrate the experiment.

Prefer focused unit/integration tests over broad test-framework expansion.

At minimum test:

1. both demo configurations validate;
2. bootstrap resolves Demo A;
3. bootstrap resolves Demo B;
4. invalid demo fails;
5. resolved brand differs correctly;
6. resolved fixtures differ correctly;
7. provider receives fixtures externally;
8. reset is deterministic and isolated;
9. capability provenance is preserved;
10. hospitality supports booking/stay context and multiple actor/reference data;
11. Activity remains correctly rendered/derived for both demos where practical.

If a rendered test is necessary to prove cross-demo leakage does not occur, add the smallest useful rendered test.

Do not introduce E2E infrastructure unless genuinely necessary.

---

### Incremental implementation discipline

Work in small dependency-ordered increments.

After each increment:

1. run the relevant tests;
2. report what hypothesis the increment tests;
3. inspect for accidental cross-demo coupling;
4. do not proceed if the increment invalidates an accepted ADR.

Preferred sequence:

##### Step 1 — Characterize baseline

Run the current relevant test suite before modifying code.

Record baseline status.

##### Step 2 — Define minimal demo configuration boundary

Introduce only the minimum structures required for two demos.

Test H1.

##### Step 3 — Externalize retail fixtures

Move prospect-specific fixture data out of `MockDataAdapter`.

Preserve behaviour.

Test H4.

##### Step 4 — Resolve demo during bootstrap

Remove direct prospect/data choice from `App.tsx`.

Use the smallest resolver seam.

Test H1 + H4.

##### Step 5 — Resolve branding

Allow retail and hospitality brands/configuration to differ.

Test isolation.

##### Step 6 — Add hospitality configuration and fixtures

Introduce the hospitality Scenario/context/actors.

Test H2.

##### Step 7 — Preserve Activity as projection

Make only the minimum changes required to prevent factual fixture input from being defined solely in UI terms.

Test H3.

##### Step 8 — Reset/isolation

Verify deterministic isolated reset.

##### Step 9 — Cross-demo validation

Run both demos and the full relevant test suite.

---

### Stop conditions

STOP implementation and report instead of generalizing if any of the following occurs:

1. the experiment requires modifying TES semantics;
2. hospitality requires a fundamentally different application core;
3. provider separation requires knowledge of the real Convercus API;
4. a proposed change requires a backend;
5. supporting multiple actors forces creation of a complete participation ontology;
6. Activity separation requires building a general event platform;
7. demo selection requires production multi-tenancy;
8. an accepted ADR appears contradicted.

A stop condition is a valid experimental result.

Do not work around it silently.

---

### Prohibited premature work

Do not implement:

* Convercus real API;
* authentication;
* backend;
* database;
* event sourcing;
* general Evidence store;
* complete Experience engine;
* Experience Builder;
* production multi-tenancy;
* coverage analytics;
* generic provider framework;
* global state library;
* broad UI refactor;
* component library redesign;
* speculative abstractions for future verticals.

---

### Required evidence after implementation

At completion provide:

#### A. Change inventory

List:

* files added;
* files modified;
* files intentionally untouched.

#### B. Test evidence

Report:

* baseline tests before changes;
* tests after each relevant stage;
* final complete relevant test run.

#### C. Hypothesis verdict

For H1–H4 assign:

* SUPPORTED BY EXPERIMENT
* PARTIALLY SUPPORTED
* FALSIFIED
* INCONCLUSIVE

Give evidence.

#### D. Architecture deviations

Report every place implementation required deviation from:

* ADR-001;
* ADR-002;
* Session-4 experiment specification.

#### E. Technical debt introduced

Explicitly list temporary compromises.

Do not hide experimental shortcuts.

#### F. Reversibility

Explain exactly how the experiment could be removed.

#### G. Next-decision recommendation

State what architectural decision is now mature enough for Session 6.

Do not automatically propose implementing more features.

---

### Final evaluation questions

Answer:

1. Did a second demo require application-core edits beyond creating the generic configuration seam?
2. What new code was genuinely reusable?
3. What code was hospitality-specific?
4. Did any prospect-specific knowledge remain inside shared core?
5. Did the experiment reduce expected marginal code for a third demo?
6. Which hypothesis H1–H4 received the strongest evidence?
7. Which received the weakest?
8. What did implementation teach that architecture analysis did not?
9. What should NOT be generalized from this two-demo experiment?

---

### Success criterion

The experiment succeeds if:

**the same application core can demonstrably run two materially different prospect demos through explicit configuration/composition, without forks and without prospect-specific leakage, while preserving accepted semantic and architectural boundaries.**

Do not optimize beyond this criterion.
<!-- FIN-TEXTO-ORIGINAL-S05 -->

---

<a id="sesion-06"></a>

## Capítulo 06 — Consolidar la composición deseada y efectiva

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-06-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 472; salida(s) de lectura en la(s) línea(s) 480, 484. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 5ef674d204b96d4f69a162cbbe30f77ef68aaada15d1f108093a7e8c58fecce6.

<!-- INICIO-TEXTO-ORIGINAL-S06 -->
### Convercus Demo Factory — Session 6: Experiment Consolidation and Architecture Promotion

#### Purpose

Session 5 successfully implemented the Minimum Reversible Experiment.

The experiment produced executable evidence for H1–H4.

Do NOT add new application functionality in this session.

Do NOT generalize the provider architecture.

Do NOT implement Experience evaluation.

Do NOT implement coverage analytics.

Session 6 has three purposes:

1. convert the now sufficiently supported desired/effective composition decision into a formal ADR;
2. decide which parts of the Session-5 experiment are promoted into the Demo Factory baseline and which remain explicitly experimental;
3. detect duplicate or competing sources of architectural authority before further implementation.

The cognitive progression is:

**EVALUATE → CONSOLIDATE → CREATE**

---

### Part A — Verify Session-5 evidence

Before creating any new governance artifact, inspect the actual implementation and tests produced by Session 5.

Verify independently that:

* Retail and Hospitality use the same application core;
* neither requires prospect-specific logic inside `App.tsx`;
* manifests exist separately from runtime state;
* bootstrap performs explicit demo resolution;
* unknown demo IDs fail explicitly;
* fixtures are external to `MockDataAdapter`;
* branding is resolved through the new composition seam;
* Activity remains a read model;
* Hospitality represents booking/stay and multiple subject/context references;
* reset state is isolated;
* capability provenance is representable.

Do not rely solely on the Session-5 written summary.

Distinguish:

* repository fact;
* test evidence;
* architectural inference.

If the implementation does not support one of the Session-5 claims, report the discrepancy before proceeding.

---

### Part B — ADR-003: Desired vs Effective Demo Composition

Create one new ADR following the existing repository ADR conventions.

Suggested title:

**ADR-003 — Desired and Effective Demo Composition**

The decision should formalize the following distinction:

#### Desired composition

A versioned demo manifest declares what a demo intends to assemble.

This may include logical references to:

* demo/prospect identity;
* brand;
* locale;
* Scenario;
* Experience references;
* modules;
* fixtures;
* capability requirements;
* provenance expectations;
* optional Demo Script;
* reset scope.

The ADR must NOT require that every possible field above already exists or is implemented.

---

#### Effective composition

A bootstrap/resolution boundary determines what can actually be instantiated in the current environment.

Therefore:

`desired composition != effective composition`

The effective composition depends on:

* valid referenced artifacts;
* available providers/implementations;
* deployment/environment constraints;
* capability availability;
* validation results.

---

#### Authority boundaries

The ADR must establish that:

* the manifest declares intent;
* bootstrap/resolution validates and resolves;
* deployment/environment provides implementation constraints and secrets;
* runtime session owns mutable execution state when required;
* read models represent presentation;
* TES remains authoritative only for governed semantic meaning.

---

#### Important constraints

The ADR must explicitly state:

1. one prospect may own zero, one or multiple demos;
2. one demo manifest must not be assumed to represent an entire prospect;
3. the manifest must not contain runtime secrets;
4. runtime state must not be stored in the manifest;
5. unresolved required references must fail explicitly;
6. requested capability and resolved capability are different concepts;
7. references requiring reproducibility should be versioned or otherwise fixed;
8. the manifest should remain small enough to avoid becoming a god configuration;
9. deployment/bootstrap may reject or qualify desired composition;
10. query-parameter demo selection is NOT part of the architectural decision;
11. static local catalogues used by the current experiment are NOT declared as the final registry architecture;
12. the current single mock provider is NOT declared as the final provider architecture.

---

### Part C — Promotion review of Session-5 implementation

Review every architectural element introduced by Session 5 and classify it into exactly one category:

##### PROMOTE

The concept and current implementation are sufficiently supported to become part of the working Demo Factory baseline.

##### PROMOTE WITH QUALIFICATION

The seam/concept should remain, but part of the current implementation is experimental or temporary.

##### RETAIN AS EXPERIMENTAL

Keep temporarily because further experiments depend on it, but do not treat it as architecture.

##### DEPRECATE

It is no longer conceptually authoritative and should eventually be removed or migrated.

##### REMOVE

It is unnecessary even for the next experiment.

At minimum classify:

* `src/demo-factory/contracts.ts`
* `manifests.ts`
* `fixtures.ts`
* `artifacts.ts`
* `bootstrap.ts`
* Hospitality demo artifacts
* Retail demo artifacts
* demo selection by query parameter
* static catalogues
* single mock provider
* Activity projection seam
* capability provenance representation
* subject/context references
* neutral PWA identity
* `canonical-demo-package.ts`
* `app.yaml`

Do not delete or modify application code during this session.

---

### Part D — Competing source-of-truth analysis

The repository now contains older and newer representations of demo configuration.

Specifically inspect:

* `DemoPackage`;
* `canonical-demo-package.ts`;
* `app.yaml`;
* Session-5 manifests;
* fixtures;
* artifact catalogues;
* bootstrap.

For each one determine:

1. what it represents today;
2. whether runtime uses it;
3. whether tests use it;
4. whether another artifact represents overlapping information;
5. whether it is:

   * authoritative;
   * subordinate;
   * legacy;
   * experimental;
   * candidate for future migration.

Identify every case where two artifacts could reasonably be interpreted by a future contributor or Codex session as competing sources of truth.

---

### Part E — Do not over-promote H2–H4

#### H2 — Scenario / Experience / Demo Script

Session 5 supports the separation, but do not create its ADR yet.

Explain what evidence remains missing.

Pay particular attention to:

* Demo Script being exercised only in tests;
* commands and checkpoints;
* collective participation;
* reuse across a second materially different Scenario.

Classify H2 as:

* ready;
* nearly ready;
* still provisional.

Provide reasoning.

---

#### H3 — Evidence / Occurrence / TES Event / Activity

Do not create an ADR.

Session 5 established that Activity can remain a projection and factual inputs need not contain UI concerns.

It did NOT establish a general evidence/event architecture.

State exactly what remains untested.

---

#### H4 — Provider Resolution

Do not create an ADR for multi-provider architecture.

Session 5 proves resolution outside `App.tsx`.

It does not prove:

* provider-per-capability;
* multiple simultaneous providers;
* reconciliation;
* real/simulated overlays;
* real API compatibility.

Preserve this distinction.

---

### Part F — Architecture v0.3

Produce a small architecture map reflecting only decisions now supported by evidence.

Do not create a more elaborate architecture than v0.2.

Expected conceptual shape:

TES
↓
Versioned product contracts
↓
Desired demo composition / manifest
↓
Bootstrap + environment resolution
↓
Effective composition
↓
Runtime as required
↓
Read models / UI

Include Scenario, Experience, providers and evidence only where their current maturity justifies them.

Mark provisional boundaries explicitly.

---

### Part G — Select the next empirical question

Do NOT automatically choose the most sophisticated next feature.

Compare at least these candidate experiments:

##### Candidate A — Third-demo marginal-cost test

Add a third materially different demo to test whether Session-5 abstractions genuinely reduce Marginal Demo Code Cost.

##### Candidate B — H3 contextual Experience evaluation

Use the smallest possible in-memory example where one factual input/evidence can be evaluated differently in relation to two Experiences.

Do not build an event store or full Experience engine.

##### Candidate C — H4 hybrid provider experiment

Use two controlled local/mock providers for different capabilities to test whether provider-by-capability resolution is actually required.

Do not use the real Convercus API.

##### Candidate D — Scenario / Demo Script operational test

Expose a minimal presenter action that invokes a public Scenario command and reaches a deterministic checkpoint without directly mutating internal state.

For each candidate evaluate:

* information gained;
* architectural hypothesis tested;
* implementation cost;
* reversibility;
* risk of premature generalization;
* dependency on unknown API/TES semantics.

Recommend exactly ONE as Session 7.

The selection criterion is:

**maximum architectural information gained per unit of irreversible complexity introduced.**

---

### Part H — Marginal Demo Code Cost

Session 5 claims that a third compatible demo should mainly require manifest and artifacts.

Do not present this as proven.

Define a minimal way of measuring this in future experiments.

Possible dimensions may include:

* new shared-core lines changed;
* new generic abstractions required;
* prospect-specific files added;
* tests added;
* existing files touched;
* cross-demo regression risk.

Do not reduce the metric to raw line count alone.

The goal is to determine whether Demo Factory is actually reducing the marginal engineering cost of each additional demo.

---

### Required output

1. Session-6 executive conclusion
2. Verification of Session-5 claims
3. ADR-003
4. Session-5 promotion matrix
5. Competing source-of-truth analysis
6. H2 maturity review
7. H3 maturity review
8. H4 maturity review
9. Demo Factory Architecture v0.3
10. Candidate Session-7 experiments
11. Recommended Session-7 experiment
12. Marginal Demo Code Cost measurement proposal
13. Remaining risks
14. Go / No-Go recommendation

Create only:

* ADR-003;
* one Session-6 consolidation report.

Do not modify application code during Session 6.
<!-- FIN-TEXTO-ORIGINAL-S06 -->

---

<a id="sesion-07"></a>

## Capítulo 07 — Acción pública de presentador y transición controlada

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-07-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 580; salida(s) de lectura en la(s) línea(s) 588, 592. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 500bf0eeeab9a3450e9b0fa9c6cb22b04561fb8264d053bb8f9830169553462c.

<!-- INICIO-TEXTO-ORIGINAL-S07 -->
### Convercus Demo Factory — Session 7: Public Presenter Action and Deterministic Checkpoint Experiment

#### Purpose

Session 6 consolidated Architecture v0.3 and recommended one next empirical experiment:

**Expose one minimal presenter action that invokes a public Scenario command and produces a deterministic checkpoint transition without directly mutating hidden runtime state or implementing Experience rules.**

Session 7 must test the operational boundary between:

* Demo Script;
* Scenario;
* runtime state;
* public commands/actions;
* read models / UI projections.

Do NOT implement a generic command framework.

Do NOT implement a complete checkpoint engine.

Do NOT implement Experience evaluation.

Do NOT modify TES semantics.

The cognitive cycle for this session is:

**APPLY → TEST → EVALUATE**

Implementation is evidence generation.

---

### Hypothesis under test

The current H2 hypothesis is:

**Scenario, Experience and Demo Script are distinct concepts that can depend on one another without collapsing into a single abstraction.**

Session 7 tests a narrower operational consequence of H2:

> A Demo Script may trigger a public Scenario/runtime action and observe its result, while domain state transitions remain owned by the Scenario/runtime boundary rather than by the Script itself.

The intended dependency remains:

```text
Experience Definition
        ↑
     Scenario
        ↑
   Demo Script
```

But operational interaction should follow:

```text
Demo Script
     ↓
Public Action / Command
     ↓
Scenario / Runtime Boundary
     ↓
State Transition
     ↓
Read Model / UI Projection
```

The following must NOT occur:

```text
Demo Script
     ↓
direct hidden state mutation
```

or:

```text
Demo Script
     ↓
implementation of Experience rules
```

---

### Experiment scope

Use only the existing Hospitality demo.

Do not modify Retail except where shared generic code requires regression-safe changes.

Implement exactly one meaningful presenter action.

Prefer an action naturally supported by the current Hospitality Scenario and fixture.

A suitable example would be:

**confirm arrival**

but use the current repository Scenario/fixture terminology if another existing action fits better.

The experiment should begin from a deterministic initial checkpoint such as:

```text
arrival_pending
```

The public action produces a deterministic transition to something equivalent to:

```text
arrival_confirmed
```

Do not introduce these literal names if the current model already uses better terminology.

---

### Required behaviour

The Hospitality demo should be able to demonstrate this flow:

```text
Initial Scenario state
        ↓
Presenter triggers public action
        ↓
Runtime validates/applies allowed transition
        ↓
Scenario checkpoint changes
        ↓
Read model changes
        ↓
Visible UI reflects the new state
```

The same initial fixture + same action must produce the same result.

---

### Public action boundary

Introduce the smallest possible public action boundary.

Examples of acceptable shapes include:

* a small action object;
* an explicit runtime method;
* a narrowly scoped command;
* another simple existing pattern.

Do not generalize it into:

* command bus;
* CQRS architecture;
* event sourcing;
* generic workflow engine;
* plugin command registry;
* global action framework.

The action boundary exists only to test whether Demo Script can interact with runtime without owning runtime internals.

---

### Ownership rules

#### Demo Script may own

* presenter-facing ordering;
* explanation;
* expected checkpoint;
* public action reference;
* optional preconditions for demonstration;
* recovery guidance where useful.

#### Demo Script must not own

* hidden mutable state;
* Experience rules;
* progression logic;
* reward logic;
* direct fixture mutation;
* internal reducer/state implementation;
* provider internals.

---

#### Scenario may own or reference

Only what the current experiment needs, such as:

* contextual actors;
* booking/stay context;
* current checkpoint or initial conditions;
* allowed public action relevant to this Scenario.

Do not expand Scenario into a generic workflow definition.

---

#### Runtime owns

The actual mutable state controlled by the demo.

It must determine whether the public action can be applied and produce the resulting state.

The Script must not assign the resulting state directly.

---

### Experience boundary

Do not implement an Experience engine.

If the Hospitality Scenario currently references an Experience, preserve that reference.

The public action must not claim to produce TES Progression, Pattern, Result or Completion unless the current repository already has validated semantics and executable support for that claim.

A checkpoint transition in this experiment is a **demo/runtime transition**, not automatically a TES Experience transition.

This distinction must be explicit in code comments or experiment documentation if ambiguity could arise.

---

### Checkpoint semantics

Use the smallest checkpoint representation that can answer:

1. what state did the Scenario start in?
2. what public action occurred?
3. what state should it reach?
4. can the resulting state be displayed and tested?

Do not design:

* arbitrary checkpoint graphs;
* branching;
* rollback graphs;
* state-machine DSL;
* persistence;
* cross-session recovery.

A simple deterministic transition is sufficient.

---

### Presenter control

Expose the action through the smallest useful presenter-facing mechanism.

This may be:

* an existing demo control surface;
* a minimal test/debug control;
* another lightweight UI affordance.

Do not build a presenter console.

The experiment must demonstrate the boundary operationally, but presentation polish is not part of the objective.

If a visible control would cause disproportionate UI work, use the smallest rendered mechanism capable of demonstrating the action.

---

### Activity / projection interaction

If the action produces a visible Activity/read-model change, that is acceptable.

However:

* Activity remains a projection;
* the Script must not insert `ActivityItem` directly;
* runtime/domain input must not be represented primarily through icon/tone/copy fields;
* presentation fields should be derived where practical.

Do not broaden Session 7 into H3 architecture work.

---

### Determinism

The experiment must prove:

```text
same initial fixture
+
same action
=
same resulting checkpoint/read model
```

Reset must return the Hospitality demo to the original checkpoint.

Retail reset behaviour must remain unchanged.

---

### Tests required

Add only tests necessary to evaluate H2 operationally.

At minimum test:

#### 1. Initial checkpoint

Hospitality starts at the expected deterministic state.

#### 2. Public action

The action can be invoked through the public boundary.

#### 3. Transition

The expected checkpoint/state transition occurs.

#### 4. No direct Script mutation

Demonstrate structurally or through tests that the Demo Script invokes the public action rather than mutating runtime state directly.

#### 5. Projection

The read model/UI reflects the resulting state.

#### 6. Deterministic reset

Reset returns Hospitality to the original checkpoint.

#### 7. Isolation

The action cannot mutate Retail state.

#### 8. Invalid action/state

If the action is invoked from an invalid state, fail explicitly or return a controlled no-op/result according to the smallest coherent design.

Do not silently produce an impossible checkpoint.

---

### Regression requirements

Run:

* relevant unit tests;
* relevant rendered tests;
* typecheck;
* lint;
* build;
* full existing project check.

Retail behaviour must remain intact.

The current 25-test Session-5/6 baseline should not regress without explicit explanation.

---

### Experiment questions

After implementation answer:

1. Can Demo Script trigger behaviour without knowing hidden runtime implementation?
2. Does Scenario provide useful context without becoming a workflow engine?
3. Is a separate Demo Script abstraction still justified after executable use?
4. Did the public-action boundary require generic infrastructure?
5. Did Hospitality-specific behaviour leak into shared core?
6. Did the action require Experience semantics that are currently unresolved?
7. Does the experiment support promotion of H2 to ADR?
8. What part of H2 remains untested?

---

### H2 verdict

At completion classify H2 as:

* **SUPPORTED — READY FOR ADR**
* **SUPPORTED WITH QUALIFICATION**
* **PARTIALLY SUPPORTED**
* **FALSIFIED**
* **INCONCLUSIVE**

A `READY FOR ADR` verdict requires evidence that:

* Experience, Scenario and Demo Script remain meaningfully distinct;
* Script can cause demo behaviour through a public boundary;
* Script does not implement runtime/domain rules;
* Scenario does not become a duplicate runtime engine;
* the separation adds operational value rather than indirection only.

---

### Stop conditions

STOP and report rather than generalize if:

1. the action requires a generic workflow engine;
2. checkpoint transition requires unresolved TES Progression semantics;
3. public action design requires knowledge of the real Convercus API;
4. multiple actors require a complete participation ontology;
5. Activity must become source of truth;
6. Script requires direct access to hidden state to work;
7. Scenario must absorb Experience semantics;
8. the same feature could be implemented more simply without Demo Script and the abstraction provides no demonstrable value.

A stop condition is a valid experimental result.

---

### Explicit non-goals

Do not implement:

* generic command bus;
* CQRS;
* event sourcing;
* workflow engine;
* general state-machine framework;
* full Experience runtime;
* Experience progression;
* reward logic;
* multi-provider architecture;
* real Convercus API;
* backend;
* persistence;
* authentication;
* coverage analytics;
* generic presenter console;
* broad UI refactor;
* third demo.

---

### Change discipline

Prefer the smallest possible number of shared-core modifications.

Hospitality-specific artefacts should remain Hospitality-specific.

Shared changes must be justified by reuse or architectural boundary, not convenience.

Do not refactor unrelated Session-5 experimental code.

---

### Required final report

#### A. Change inventory

List:

* files added;
* files modified;
* intentionally untouched areas.

#### B. Implementation flow

Show the actual resulting path:

```text
Demo Script
→ Public Action
→ Scenario/Runtime
→ State Transition
→ Read Model
→ UI
```

State clearly where each responsibility lives.

#### C. Test evidence

Provide:

* baseline before changes;
* incremental relevant tests;
* final full check.

#### D. H2 verdict

Give evidence for the classification.

#### E. Architecture impact

State whether Session 7:

* confirms Architecture v0.3;
* requires qualification;
* contradicts an accepted ADR.

#### F. Technical debt

List all experimental shortcuts.

#### G. Reversibility

Explain exactly how to remove the Session-7 experiment.

#### H. Next architectural decision

State only what decision is now mature enough to consider.

Do not automatically recommend another feature implementation.

---

### Final falsification questions

Before concluding answer:

1. Could the same result have been achieved by removing Demo Script entirely?
2. If yes, what value does Demo Script add?
3. Did Scenario remain contextual or start absorbing executable workflow semantics?
4. Did the public action remain narrow or start becoming a generic command architecture?
5. Is the checkpoint a demo concept or accidentally becoming a TES Experience state?
6. Would a second Script for the same Scenario still fit the model without redesign?
7. What evidence would falsify the Scenario / Experience / Demo Script separation in a future experiment?

---

### Success criterion

Session 7 succeeds only if it demonstrates that:

> **A presenter-facing Demo Script can trigger one deterministic demo behaviour through a public Scenario/runtime boundary, producing a visible checkpoint/read-model transition without directly mutating hidden state, redefining Experience semantics or requiring a generic workflow architecture.**

Do not optimize beyond this criterion.
<!-- FIN-TEXTO-ORIGINAL-S07 -->

---

<a id="sesion-08"></a>

## Capítulo 08 — Consolidar H2 y aceptar ADR-004

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-08-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 736; salida(s) de lectura en la(s) línea(s) 744, 748. Cotejo adicional: lectura repetida completa. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 5b2c5a2dc2b83dc1c7645f869079164b21af6e91471f65261b4a460165f0d615.

<!-- INICIO-TEXTO-ORIGINAL-S08 -->
### Convercus Demo Factory — Session 8: H2 Consolidation and ADR Promotion

#### Purpose

Session 7 produced executable evidence for H2:

**Experience Definition, Scenario and Demo Script can remain logically distinct while Demo Script triggers deterministic demo behaviour exclusively through a public runtime boundary.**

Session 8 must consolidate that evidence.

Do NOT modify application code.

Do NOT add new presenter actions.

Do NOT generalize scripts, checkpoints, commands or Scenario behaviour.

The cognitive progression is:

**EVALUATE → CONSOLIDATE → CREATE**

The objectives are:

1. independently verify the Session-7 implementation evidence;
2. formalize the surviving H2 decision as an ADR;
3. distinguish what has actually been proven from what remains experimental;
4. define the next empirical question without implementing it.

---

### Part A — Verify Session-7 evidence

Inspect the actual implementation and tests rather than relying only on the Session-7 report.

Verify that:

* Hospitality exposes exactly the intended presenter action;
* Demo Script identifies the presenter-facing action without directly mutating runtime state;
* the public action boundary exists outside React presentation logic;
* runtime validates whether the action is legal;
* runtime owns the checkpoint transition;
* AppSnapshot/read model reflects the resulting state;
* Activity is updated as projection rather than source of truth;
* reset restores the initial checkpoint;
* Retail state remains isolated;
* repeating the action from the resulting state fails explicitly or produces the documented controlled result;
* no TES Progression, Result or Completion semantics were introduced.

For each claim classify evidence as:

* repository fact;
* test evidence;
* architectural inference.

If Session-7 claims are stronger than the implementation supports, report the discrepancy before creating the ADR.

---

### Part B — Create ADR-004

Create one ADR using the existing governance conventions.

Suggested title:

**ADR-004 — Separation of Experience Definition, Scenario and Demo Script**

#### Context

Demo Factory must distinguish:

##### Experience Definition

A semantically governed definition of an Experience, traceable to TES.

##### Scenario

The situated demo context that may provide:

* actors;
* roles;
* subject/context references;
* initial conditions;
* relevant Experience references;
* fixture/checkpoint context;
* permitted demo-level interaction boundaries where required.

##### Demo Script

Presenter-facing demonstration orchestration that may provide:

* ordered demonstration steps;
* presenter copy/instructions;
* references to public actions;
* expected demo checkpoints/results;
* recovery guidance where useful.

---

### Decision

Formalize the following dependency:

```text
Experience Definition
        ↑ referenced/instantiated by
Scenario
        ↑ demonstrated through
Demo Script
```

Operational interaction must occur through:

```text
Demo Script
      ↓
Public Action
      ↓
Runtime Boundary
      ↓
Controlled Runtime Transition
      ↓
Read Model / UI
```

---

### Mandatory boundaries

The ADR must explicitly establish:

#### Experience Definition must not own

* presenter instructions;
* prospect-specific narrative unless semantically intrinsic;
* UI state;
* demo checkpoints;
* presenter actions.

#### Scenario must not

* redefine TES Experience semantics;
* become a generic workflow engine;
* implement TES Progression or Result;
* absorb presenter narration merely for convenience.

#### Demo Script must not

* directly mutate hidden runtime state;
* implement Experience rules;
* implement reward/progression logic;
* bypass runtime validation;
* become a second application controller.

#### Runtime must

* validate public actions;
* own mutable state transitions;
* expose resulting state through read models/projections.

---

### Checkpoint qualification

State explicitly that:

**Demo checkpoint != TES Experience Progression/Result/Completion**

unless future validated semantic and executable evidence explicitly establishes such a relationship.

Current Hospitality checkpoints are demo/runtime constructs only.

---

### Scope limitation

The ADR must explicitly state that Session 7 does NOT establish:

* generic script engines;
* multi-step script execution;
* arbitrary state machines;
* branching;
* generic checkpoint graphs;
* multiple concurrent scripts;
* collective Experience participation;
* Experience evaluation;
* TES Progression;
* reusable workflow semantics.

These remain outside the decision.

---

### Reconsideration triggers

The ADR must be reconsidered if future implementation shows that:

1. Scenario needs to encode substantial workflow/rule semantics;
2. Demo Script needs direct internal-state access;
3. multiple Scripts for one Scenario cannot coexist without redefining Scenario;
4. Experience-specific execution logic migrates into Script;
5. checkpoints begin to function as implicit Experience states;
6. the same useful behaviour can be represented more simply without the three-way separation.

---

### Part C — Promotion review of Session-7 elements

Classify each as:

* PROMOTE
* PROMOTE WITH QUALIFICATION
* RETAIN AS EXPERIMENTAL
* DEPRECATE
* REMOVE

At minimum classify:

* public presenter-action boundary;
* Demo Script representation;
* Scenario transition representation;
* runtime checkpoint;
* presenter control in `/system`;
* Activity projection following action;
* string action identifiers;
* string checkpoints;
* single-action Scenario;
* first-step-only Script execution.

Expected discipline:

Promote the architectural seam where supported.

Do not promote experimental limitations into architecture.

---

### Part D — Architecture v0.4

Update the architecture map only enough to include the now-supported separation.

Do not redesign Architecture v0.3.

Conceptually include:

```text
TES semantic authority
        ↓
Experience Definition
        ↓
Scenario Context
        ↓
Demo Manifest / Desired Composition
        ↓
Bootstrap / Effective Composition
        ↓
Runtime
   ↑ Public Action
Demo Script
        ↓
Read Models / UI
```

Adjust this shape if the verified implementation supports a more precise representation.

Clearly distinguish:

* accepted architecture;
* provisional boundaries.

---

### Part E — Reassess H3 and H4 after Session 7

Do not promote H3 or H4.

Review whether Session 7 changed the evidence available for either.

#### H3

Evidence / Occurrence / TES Event / Activity Projection.

Determine whether the new presenter action teaches anything useful about:

* factual occurrence;
* provenance;
* Event interpretation;
* Activity projection.

Do not infer more than the implementation demonstrates.

#### H4

Provider resolution.

Determine whether the public action boundary adds evidence for provider architecture.

Do not infer multi-provider support merely because runtime exposes an action.

---

### Part F — Select the next empirical question

Compare the following candidates.

#### Candidate A — H3 contextual multi-Experience evaluation

Construct the smallest in-memory experiment where one factual/evidentiary input is evaluated differently relative to two Experience references.

The purpose is to test:

* contextual significance;
* zero/one/multiple Experience evaluation;
* Activity as derived projection;
* separation between evidence and TES Event interpretation.

Do NOT build a general Experience engine.

#### Candidate B — H4 multi-provider composition

Use two controlled local providers for separate capabilities.

Test whether provider-per-capability resolution adds genuine value.

#### Candidate C — Third-demo marginal-cost test

Introduce a third materially different demo and measure Marginal Demo Code Cost.

#### Candidate D — Second Scenario / Script reuse test

Add a second materially distinct Scenario or Script configuration to test whether the H2 separation scales one step beyond the current single path.

For each evaluate:

* information gain;
* architecture uncertainty reduced;
* implementation cost;
* reversibility;
* risk of premature abstraction;
* TES/API dependencies.

Recommend exactly one.

Use the criterion:

**maximum architectural uncertainty reduced per unit of irreversible complexity introduced.**

---

### Part G — Special attention to H3

Because H3 has remained partially supported through several sessions, explicitly determine whether it has now become the highest-value uncertainty.

If recommending H3, define the smallest possible experiment conceptually.

It should ideally test something equivalent to:

```text
one factual/evidentiary input
        ↓
evaluation relative to Experience A
        → significant / effect A

same input
        ↓
evaluation relative to Experience B
        → different significance / no effect / effect B
```

Do not implement it.

Do not introduce Pattern, Sequence, Progression or Result unless necessary and semantically supported.

The experiment should test contextual interpretation, not build an Experience engine.

---

### Required output

1. Session-8 executive conclusion
2. Verification of Session-7 evidence
3. ADR-004
4. Session-7 promotion matrix
5. H2 final maturity status
6. Architecture v0.4
7. H3 evidence update
8. H4 evidence update
9. Candidate next experiments
10. Recommended Session-9 experiment
11. Remaining risks
12. Go / No-Go recommendation

Create only:

* ADR-004;
* one Session-8 consolidation report.

Do not modify application code.
<!-- FIN-TEXTO-ORIGINAL-S08 -->

---

<a id="sesion-09"></a>

## Capítulo 09 — Comprobar prerrequisitos de evaluación multi-Experience

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-09-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 841; salida(s) de lectura en la(s) línea(s) 848, 852. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 6afcc1d0c03c8af7b13fc0639c884f375d8f2daa826c63be58571eeb2c854886.

<!-- INICIO-TEXTO-ORIGINAL-S09 -->
### Convercus Demo Factory — Session 9: Contextual Multi-Experience Evaluation Experiment

#### Purpose

Session 8 promoted H2 into ADR-004 and confirmed Architecture v0.4.

The highest-value unresolved architectural hypothesis is now H3:

**Evidence / occurrence and TES Event interpretation must remain semantically distinct, while Activity remains a derived projection.**

Session 9 must test only one narrow proposition:

> The same factual/evidentiary input can be evaluated differently in relation to two Experience references without storing its significance as an intrinsic universal property and without building a general Experience engine.

The cognitive cycle is:

**APPLY → TEST → EVALUATE**

Implementation is evidence generation.

---

### Governing semantic constraints

Respect:

* ADR-001 — bounded TES semantic authority;
* ADR-002 — logical separation of composition/runtime/read models;
* ADR-003 — desired vs effective composition;
* ADR-004 — Experience / Scenario / Demo Script separation;
* `observed-occurrence-trace-event.md`.

Do not modify TES.

Do not introduce a new TES concept.

Do not treat this experiment as implementation of the complete TES Experience Ledger.

---

### H3 hypothesis under test

The product interpretation currently states:

1. not every observable occurrence is automatically a TES Event;
2. evidence/trace and experiential interpretation are distinct responsibilities;
3. significance may depend on the Experience context;
4. one evidentiary input may potentially be evaluated relative to zero, one or multiple Experiences;
5. Activity is a presentation/read-model projection rather than the semantic source of truth.

Session 9 must generate executable evidence for or against points 2–5.

---

### Critical limitation

Do NOT attempt to implement:

`Event → Pattern → Sequence → Progression → Result → Measurement → Learning`

Session 9 tests only the boundary around contextual recognition/evaluation.

Any output of the experiment must therefore avoid claiming:

* TES Progression;
* TES Pattern;
* TES Sequence completion;
* TES Result;
* Experience Completion;
* reward entitlement;

unless such meaning is already explicitly supported by existing validated repository semantics.

Prefer neutral experiment terminology such as:

* relevant;
* not relevant;
* evidence accepted;
* evidence ignored;
* demo effect;
* evaluation outcome.

Do not invent new TES vocabulary.

---

### Experiment shape

Use one controlled factual/evidentiary input.

Prefer an input naturally connected to the existing Hospitality demo so that Session 7 infrastructure can be reused.

A candidate may be the existing **arrival confirmation** action/evidence, if repository semantics permit.

Do not force this example if another existing input provides cleaner evidence.

The same input must be presented to two distinct Experience references.

Conceptually:

```text
Factual / evidentiary input X
          │
          ├──────── evaluation relative to Experience A
          │                  ↓
          │            outcome A
          │
          └──────── evaluation relative to Experience B
                             ↓
                       outcome B
```

At least one of the following must occur:

* relevant for A / irrelevant for B;
* different accepted effects for A and B;
* accepted under different contextual conditions.

If both Experiences always produce identical output, the experiment has not adequately tested contextual significance.

---

### Experience selection

Before implementation, inspect the existing Experience definitions/references and semantic documentation.

Prefer existing definitions or references where possible.

Do not invent two rich new TES Experiences solely to satisfy the test.

If the repository does not contain two semantically defensible Experience references for the chosen evidence:

STOP.

Report that the experiment lacks sufficient semantic material rather than fabricating Experience semantics.

A stop condition is a valid result.

---

### Factual/evidentiary input

Introduce only the smallest representation needed for the experiment.

Do NOT assume that the final architecture requires an `ObservedOccurrence` class or persisted occurrence store.

The experiment may use:

* an existing event/evidence structure;
* a minimal neutral input record;
* another existing domain representation.

The representation must not contain:

* UI icon;
* visual tone;
* editorial Activity copy;
* universal `significant: true/false`;
* Experience-specific interpretation embedded as an intrinsic property of the input.

Preserve provenance or source identity only to the degree necessary for the experiment.

---

### Contextual evaluation boundary

Create or reuse the smallest evaluation seam capable of expressing:

```text
evaluate(input, experienceContext)
    -> evaluation outcome
```

Do not generalize this into a complete engine.

Before adding new abstractions, inspect whether existing:

`evaluateEventAcrossExperiences`

or related routing/domain code can be reused or minimally adapted.

Do not preserve an existing abstraction merely because it exists if it semantically contradicts the current Product Interpretation.

---

### Required evaluation properties

The experiment must demonstrate that:

#### 1. Same factual input

The underlying evidentiary input is identical when evaluated against both Experiences.

#### 2. Experience-relative interpretation

The resulting evaluation may differ according to Experience context.

#### 3. Input immutability

Evaluating Experience A must not overwrite the factual input with A-specific meaning before Experience B evaluates it.

#### 4. Independent evaluation

Evaluation order must not change the result unless existing semantics explicitly require stateful dependence.

For this experiment prefer deterministic independent evaluation.

#### 5. Explicit outcome

Each Experience evaluation must return an explicit result rather than mutate hidden state as a side effect.

---

### Many-to-many qualification

Do not implement a static occurrence-to-Experience membership table.

The experiment should establish only this capability:

> one input can be considered independently in relation to multiple Experiences.

It must NOT establish as a universal rule that every occurrence participates in many Experiences.

Possible cardinalities remain:

```text
input → 0 Experiences
input → 1 Experience
input → N Experiences
```

according to context.

---

### Activity projection

Use the evaluation results to test the presentation boundary minimally.

Activity may display a representation of:

* the factual input;
* one or more evaluation consequences;

if useful.

However:

* Activity must not become the evaluation engine;
* Activity must not be the factual source of truth;
* `ActivityItem` must not be required as input to Experience evaluation;
* UI-specific fields must remain projection concerns.

A single Activity representation may summarize several underlying relationships if provenance remains sufficiently clear.

Do not redesign the Activity UI.

---

### No forced persistence model

Do not create:

* occurrence database;
* event store;
* evidence ledger;
* evaluation persistence layer;
* event sourcing;
* generic audit framework.

Use in-memory deterministic state if sufficient.

The semantic distinction:

`input ≠ interpretation`

does not imply:

`input table + interpretation table`

in this experiment.

---

### No progression semantics

A successful evaluation must not automatically change:

* Experience Progression;
* Completion;
* Result.

If an existing demo-level/read-model indicator changes for demonstration purposes, label it explicitly as demo/runtime state rather than TES Progression.

---

### Tests required

Add only the smallest tests necessary.

At minimum prove:

#### 1. Identical input

Both Experience evaluations receive the same factual input.

#### 2. Different contextual result

Experience A and Experience B produce meaningfully different evaluation results.

#### 3. Input remains unchanged

Evaluation does not mutate the factual input.

#### 4. Evaluation isolation

Evaluating A then B produces the same per-Experience outcomes as evaluating B then A.

#### 5. Zero-match possibility

Where practical, show that an input can produce no relevant evaluation for an unrelated Experience/context.

Do not invent a third Experience solely for this if an existing valid case is unavailable.

#### 6. Activity remains projection

The read model may represent the resulting behaviour without becoming an evaluation input.

#### 7. Existing presenter action regression

Session-7 Hospitality behaviour continues to pass.

#### 8. Retail regression

Retail remains unaffected.

---

### Falsification cases

Actively attempt to falsify H3 during implementation.

Ask:

##### F1

Does the input actually need to know the target Experience in order to exist?

If yes, the claim of a neutral evidentiary input may be too strong.

##### F2

Do both Experience evaluations always produce the same result?

If yes, the experiment provides no evidence for contextual significance.

##### F3

Does evaluation require TES Pattern/Sequence/Progression semantics?

If yes, STOP rather than implementing them.

##### F4

Does Activity need to contain hidden semantic state for the experiment to work?

If yes, H3 or the current projection boundary may be wrong.

##### F5

Does the existing `SignificantEvent` abstraction already encode significance too early?

If yes, document whether it should be:

* retained;
* qualified;
* renamed later;
* replaced in a future experiment.

Do not perform broad renaming during Session 9.

---

### Coverage exclusion

Do NOT implement:

* Experience-portfolio observation overlap;
* Experience evidence sufficiency profile;
* generic coverage;
* set-cover calculations.

Session 9 may generate data relevant to future overlap analysis, but coverage remains experimental analytics.

---

### Stop conditions

STOP implementation and report if:

1. two defensible Experience contexts cannot be found;
2. evaluating the input requires inventing TES semantics;
3. Pattern or Progression must be implemented;
4. a general Experience engine becomes necessary;
5. persistence becomes necessary solely to satisfy the experiment;
6. Activity must become source of truth;
7. factual input cannot be separated coherently from presentation;
8. the same semantic claim can only be demonstrated by hard-coding arbitrary Experience-specific results with no repository-supported rationale.

Do not work around a stop condition.

---

### Implementation discipline

Prefer:

* one input;
* two Experience references;
* one evaluation seam;
* deterministic in-memory behaviour;
* focused tests.

Avoid adding abstractions for future possibilities.

Use the smallest number of shared-core modifications possible.

---

### Required final report

#### A. Semantic basis

State exactly why the selected factual input and two Experience contexts are semantically defensible.

Distinguish:

* TES fact;
* Product Interpretation;
* experiment-specific simplification.

#### B. Change inventory

List:

* files added;
* files modified;
* intentionally untouched areas.

#### C. Evaluation flow

Show the actual implemented flow, for example:

```text
Evidence/Input
      ↓
Contextual Evaluation
     / \
    /   \
Exp A   Exp B
 ↓       ↓
Outcome Outcome
   \     /
    Read Model
       ↓
    Activity/UI
```

Adjust to actual implementation.

#### D. Test evidence

Report:

* baseline;
* incremental tests;
* final full project check.

#### E. H3 verdict

Classify:

* **SUPPORTED — READY FOR ADR**
* **SUPPORTED WITH QUALIFICATION**
* **PARTIALLY SUPPORTED**
* **FALSIFIED**
* **INCONCLUSIVE**

#### F. SignificantEvent assessment

Explicitly assess whether the existing `SignificantEvent` name/contract remains semantically appropriate after the experiment.

Do not automatically change it.

#### G. Architecture impact

State whether Architecture v0.4:

* survives;
* requires qualification;
* is contradicted.

#### H. Technical debt

List every experimental shortcut.

#### I. Reversibility

Explain exactly how to remove Session-9 changes.

#### J. Next decision

Identify only the architectural decision that has become mature enough to consider.

Do not automatically recommend more implementation.

---

### Final adversarial questions

Before concluding:

1. Did we genuinely demonstrate contextual significance or merely hard-code two different outputs?
2. Could the input exist independently of both Experiences?
3. Did either Experience need to mutate the input?
4. Did evaluation order matter?
5. Did we accidentally implement part of Progression?
6. Is `SignificantEvent` currently named at the correct semantic layer?
7. Did Activity remain only a projection?
8. What evidence still prevents H3 from becoming an ADR?
9. What future real-API behaviour could invalidate this experiment?
10. What should explicitly NOT be generalized from this test?

---

### Success criterion

Session 9 succeeds if:

> **One semantically defensible factual/evidentiary input can be evaluated independently and differently relative to two Experience contexts, without mutating the input, making Activity authoritative, implementing TES Progression or introducing a general Experience engine.**

Do not optimize beyond this criterion.
<!-- FIN-TEXTO-ORIGINAL-S09 -->

---

<a id="sesion-10"></a>

## Capítulo 10 — Readiness de fuentes comerciales

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-10-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 927; salida(s) de lectura en la(s) línea(s) 934, 938. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 18568fb456e40fe446f8da5002d79029e0f12a5a97484dac764ab9ba8031910c.

<!-- INICIO-TEXTO-ORIGINAL-S10 -->
### Convercus Demo Factory — Session 10: Commercial Experience Source Interpretation and Semantic Readiness

#### Purpose

Session 9 stopped correctly because Demo Factory did not contain two semantically defensible Experience references for the same evidentiary input.

New source material is now available:

**Convercus New Generation Loyalty ES**

This presentation contains commercial/product examples for Hospitality and Fashion & Retail.

The presentation was created for a marketing/product-facing communication surface.

Therefore:

> It is valid source material for identifying product intentions and candidate Experiences, but it is NOT TES semantic authority and must NOT be translated directly into executable Experience Definitions.

Session 10 must establish whether this commercial source contains enough independent semantic material to create one or more TES-governed Product Experience Definitions without inventing meaning for the purpose of passing H3.

Do NOT implement application code.

Do NOT modify TES.

Do NOT rerun H3 yet.

The cognitive progression is:

**UNDERSTAND → ANALYZE → EVALUATE → CREATE**

---

### Source authority hierarchy

Use the following hierarchy strictly:

```text
TES semantic authority
        ↓
Product Interpretations subordinate to TES
        ↓
Commercial / product source material
        ↓
Candidate Experience interpretation
        ↓
TES semantic validation
        ↓
Validated Product Experience Definition
        ↓
Demo Factory runtime reference
```

Never use:

```text
commercial slide
      ↓
executable Experience
```

without semantic validation.

---

### Commercial-source qualification

Treat the presentation as:

**Product source material — non-normative**

It may validly describe:

* intended customer behaviour;
* product use cases;
* marketing goals;
* engagement tactics;
* participant actions;
* triggers;
* incentives;
* rewards;
* channels;
* commercial outcomes;
* candidate Experience structures.

It may also use terminology loosely.

In particular, do NOT assume that the following commercial expressions correspond directly to TES entities:

* Customer Journey;
* experience;
* phase;
* activity;
* engagement;
* challenge;
* campaign;
* gamification;
* reward;
* loyalty mechanic;
* customer lifecycle.

The communication target is primarily marketing/product users, not ontology or software architecture.

Commercial phrasing must therefore be interpreted rather than copied into the semantic model.

---

### Primary source examples to inspect

Inspect the entire presentation, but pay particular attention to the following candidates.

#### Hospitality

##### Candidate H-A — Family Adventure / Aventura Familiar

Source material includes approximately:

* family/group reservation identification;
* check-in;
* programme/app registration;
* personalised "Mi Aventura";
* daily activities;
* QR/staff validation;
* digital stars;
* gamified progression messaging;
* threshold reward;
* checkout/future-visit activation.

Do NOT assume the complete slide equals one Experience.

Determine whether it represents:

* one Experience;
* several nested/related Experiences;
* Scenario + Experience;
* campaign;
* loyalty mechanic;
* or a combination.

---

##### Candidate H-B — Active Challenge / Desafío Activo

Source material includes approximately:

* challenge during hotel stay;
* completion of three sport/wellness activities;
* QR/POS/App validation;
* progress visibility;
* digital badges;
* automatic benefit/reward.

Evaluate whether this forms a coherent TES-compatible Experience candidate.

---

##### Hospitality macro-frame — Before / During / After

The presentation also contains a broader guest lifecycle:

* before booking;
* during stay;
* after stay.

Do NOT automatically classify this as one Experience.

Test whether it is better interpreted as:

* Scenario;
* lifecycle framing;
* Experience portfolio;
* orchestration context;
* commercial narrative.

---

#### Fashion & Retail

##### Candidate R-A — Style Ambassadors / Embajadores de Estilo

Evaluate whether the available material is semantically sufficient or merely a product concept.

Do not fill missing semantic structure from imagination.

---

##### Candidate R-B — Sustainable Circuit / Circuito Sostenible

Source material includes:

* sustainable onboarding;
* local cause selection;
* first challenge;
* repair;
* recycled-material purchase;
* textile return;
* 2-of-3 rule;
* immediate reward;
* referral/sharing;
* re-entry;
* social recognition / levels.

This candidate appears structurally rich, but validate rather than assume.

---

##### Candidate R-C — Seasonal Marathon / Maratón de Temporada

Source material includes:

* visits or purchases across categories;
* QR/purchase validation;
* progress update;
* completion;
* coupon or styling experience.

Evaluate its semantic completeness.

---

### Part A — Extract the commercial semantics

For each relevant example, extract only what the presentation actually supports.

Use the following table:

| Dimension                     | Source-supported evidence |
| ----------------------------- | ------------------------- |
| Commercial name               |                           |
| Sector                        |                           |
| Stated objective              |                           |
| Actors / participants         |                           |
| Context                       |                           |
| Observed actions              |                           |
| Validation / evidence sources |                           |
| Conditions / thresholds       |                           |
| Sequence indications          |                           |
| Progress indications          |                           |
| Incentives                    |                           |
| Rewards                       |                           |
| Intended participant outcome  |                           |
| Intended business outcome     |                           |
| Channels / systems            |                           |
| Ambiguities                   |                           |

Do not fill unsupported cells using general domain knowledge.

Mark missing information explicitly.

---

### Part B — Classify before calling anything an Experience

Every extracted commercial construct must first be classified into one or more of:

* **Candidate Experience**
* **Scenario**
* **Lifecycle / orchestration frame**
* **Campaign**
* **Tactic / mechanic**
* **Incentive**
* **Reward**
* **Capability**
* **UI / channel behaviour**
* **Business outcome**
* **Insufficiently specified**

A commercial label containing "Experience", "Challenge", "Journey" or "Loyalty" is not evidence of its semantic class.

Explain the classification.

---

### Part C — TES semantic validation

For every **Candidate Experience**, evaluate whether the source material is sufficiently compatible with the TES semantic chain:

```text
Event
→ Pattern
→ Sequence
→ Progression
→ Result
→ Measurement
→ Learning
```

Do not require the commercial slide to use TES terminology.

Instead ask whether the underlying structure is supportable.

For each candidate analyse:

#### Event

What occurrences could become significant events relative to this Experience?

Do not equate raw observations automatically with Events.

#### Pattern

Is there evidence of meaningful regularity/relations among events, or would Pattern have to be invented?

#### Sequence

Is there a meaningful sequence or ordering?

Remember:

plural actions != TES Sequence

#### Progression

Is there evidence of situated displacement/transformation?

Do not equate points, stars or counters automatically with TES Progression.

#### Result

What resulting transformation is implied?

Distinguish participant/customer result from business KPI.

#### Measurement

What evidence could support reconstruction or measurement?

#### Learning

Is learning represented, inferable as product operation, or absent from the commercial material?

Missing Learning detail does not automatically invalidate the candidate, but must be recorded accurately.

---

### Part D — Separate commercial mechanics from Experience semantics

For each candidate explicitly distinguish:

```text
Experience semantic structure
```

from:

```text
loyalty mechanics
```

such as:

* points;
* stars;
* coupon;
* badge;
* status;
* reward;
* push notification;
* gamification copy;
* QR scan;
* app registration.

A loyalty mechanic may support an Experience without defining it.

Example analytical question:

> If points, coupon and badges were removed, would a coherent participant transformation still remain?

If the answer is no, the candidate may be primarily a mechanic/campaign rather than a robust Experience.

---

### Part E — Scenario vs Experience analysis

Pay special attention to constructs that mix context and transformation.

For Hospitality determine whether:

* booking;
* stay;
* property;
* family/group;
* business traveller;
* resort guest;

belong primarily to Scenario/context rather than to the Experience definition itself.

For each Experience candidate propose:

```text
Experience semantic core
+
Scenario-specific instantiation
```

if that distinction is supported.

Do not force cross-sector reuse.

---

### Part F — Experience Definition readiness

For every candidate classify its readiness as exactly one of:

##### READY FOR PRODUCT EXPERIENCE DEFINITION

Enough source-supported semantic material exists to create a Product Experience Definition subordinate to TES.

##### READY WITH EXPLICIT GAPS

A definition can be created, but unresolved fields must remain explicitly unresolved rather than invented.

##### COMMERCIAL CONCEPT ONLY

Useful source material exists, but the structure is insufficient for a governed Experience Definition.

##### NOT AN EXPERIENCE

The construct is better classified as Scenario, campaign, mechanic, capability or outcome.

For each verdict give:

* strongest supporting evidence;
* strongest ambiguity;
* what would be invented if promoted too early;
* confidence.

---

### Part G — Experience Definition responsibility model

Inspect the two existing constructs currently called `ExperienceDefinition` in the repository.

Do not rename or modify them.

Determine whether they actually represent different responsibilities such as:

```text
Semantic/Product Experience Definition
        ↓
Runtime Experience Reference / Descriptor
```

or whether they are competing definitions.

For each current type report:

* current fields;
* current consumers;
* semantic responsibility;
* runtime responsibility;
* whether it is a full definition or reference/header;
* risk of future confusion.

Recommend terminology conceptually, but do NOT perform renaming.

---

### Part H — Author candidate Product Experience Definitions

Only for candidates classified:

* READY FOR PRODUCT EXPERIENCE DEFINITION
  or
* READY WITH EXPLICIT GAPS

draft non-executable Product Experience Definitions.

These definitions must be subordinate to TES.

They must contain at minimum:

```yaml
id:
name:
sector:
status:
tes_baseline:
source_material:
semantic_authority:
```

Then describe:

* purpose / intended transformation;
* participant or subject;
* Scenario dependencies;
* relevant evidence/events supported by source;
* Pattern hypothesis;
* Sequence;
* Progression interpretation;
* intended Result;
* measurement/evidence;
* incentives;
* rewards;
* unresolved semantic gaps;
* prohibited interpretations.

Do NOT introduce implementation fields merely because Demo Factory may need them later.

Do NOT create TypeScript.

---

### Part I — H3 readiness analysis

Only AFTER Product Experience candidate validation, reassess H3.

Session 9 required:

> one factual/evidentiary input evaluated independently relative to two semantically defensible Experiences.

Do not force `arrival confirmation` to remain the input.

Search the validated candidate definitions for naturally shared evidence.

Construct an evidence-to-Experience matrix such as:

| Evidence/Input candidate | Experience A | Experience B | Relationship supported by source? |
| ------------------------ | ------------ | ------------ | --------------------------------- |

Possible Hospitality evidence may include, only if semantically supported:

* reservation identified;
* arrival/check-in;
* activity participation;
* QR validation;
* restaurant/service consumption;
* checkout;
* subsequent booking.

Possible Retail evidence may include:

* store visit;
* purchase;
* repair;
* textile return;
* QR validation;
* referral.

Do not mix sectors solely to obtain two Experiences unless the same evidentiary semantics genuinely apply.

---

### Critical H3 question

Determine whether there exists:

```text
one evidence/input X
        ↓
Experience A — semantically relevant
        ↓
outcome A

same X
        ↓
Experience B — semantically different relationship
        ↓
outcome B / irrelevant
```

where BOTH Experience Definitions exist independently of H3.

This is essential.

The Experiences must not have been shaped to manufacture the experiment.

---

### Possible H3 outcomes

Classify Session-10 readiness as:

##### GO — H3 SEMANTIC PREREQUISITES SATISFIED

At least two defensible Product Experience Definitions exist and one shared evidentiary input can test contextual interpretation without invented semantics.

##### CONDITIONAL GO

Two Experience Definitions exist, but the shared input or evaluation relation requires one clearly identified product clarification.

##### NO-GO — EXPERIENCE MATERIAL STILL INSUFFICIENT

The presentation improves product knowledge but does not provide sufficient Experience semantics.

##### NO-GO — NO NATURAL SHARED EVIDENCE

Multiple valid Experiences exist, but none provide an honest H3 multi-Experience test with current evidence.

The last outcome is valid and must not be worked around.

---

### Part J — Source-material governance recommendation

Recommend how this presentation and future commercial documents should enter repository knowledge.

Evaluate whether the repository needs a distinction such as:

```text
source-material/
    commercial/
    product/
```

versus:

```text
product-interpretations/
```

The presentation must NOT be stored or treated as a Product Interpretation itself.

Its role is evidence/source material from which interpretations can be derived.

Recommend only.

Do not reorganise repository files in Session 10 unless an existing governance rule already mandates it.

---

### Part K — Commercial-language warnings

Create a short reusable set of warnings for future Codex sessions using commercial collateral.

At minimum include:

1. `Journey` is not automatically a TES entity.
2. `Experience` in marketing copy is not automatically a TES Experience.
3. points/stars/badges do not automatically mean TES Progression.
4. reward is not automatically Result.
5. customer action is not automatically Event.
6. several actions do not automatically constitute Pattern or Sequence.
7. business KPI is not automatically participant Result.
8. campaign mechanics may support but do not define an Experience.
9. presentation phases may describe Scenario/lifecycle rather than Experience.
10. commercial simplification must not be repaired silently by invented semantics.

---

### Stop conditions

STOP semantic promotion if:

1. a candidate only becomes coherent by inventing missing behaviours;
2. business outcome is being substituted for participant Result;
3. points or count are being substituted automatically for Progression;
4. commercial phase order is being assumed to be TES Sequence without support;
5. a Scenario is being forced into an Experience;
6. two Experiences are being constructed solely to unblock H3;
7. the shared H3 evidence exists only because definitions were modified for the experiment;
8. TES itself would need modification to make the candidate work.

A stop condition is a successful analytical result.

---

### Explicit non-goals

Do not:

* modify TES;
* modify application code;
* modify runtime contracts;
* rename `ExperienceDefinition`;
* rename `SignificantEvent`;
* create the H3 evaluator;
* rerun Session 9;
* implement Pattern;
* implement Sequence;
* implement Progression;
* build an Experience Engine;
* create Builder functionality;
* implement coverage analytics;
* transform all presentation examples into Experiences;
* validate marketing claims or business metrics externally.

---

### Required output

1. Session-10 executive conclusion
2. Source authority classification
3. Commercial semantics extraction
4. Construct classification matrix
5. Hospitality candidate analysis
6. Retail candidate analysis
7. TES semantic validation per candidate
8. Experience readiness matrix
9. Experience Definition responsibility analysis
10. Draft Product Experience Definitions
11. Evidence-to-Experience matrix
12. H3 semantic readiness verdict
13. Source-material governance recommendation
14. Commercial-language warning rules
15. Remaining semantic gaps
16. GO / CONDITIONAL GO / NO-GO recommendation for re-running H3

---

### File creation

Create only:

1. one Session-10 semantic-readiness report;
2. Product Experience Definition documents only for candidates that pass the readiness threshold.

Do not create placeholder Experience Definitions for rejected or insufficient candidates.

Do not modify application code.

---

### Final adversarial review

Before concluding answer:

1. Which candidate looked most like an Experience commercially but least like one semantically?
2. Which candidate remained coherent after removing points/rewards/gamification?
3. Which semantic fields required the greatest inference?
4. Did any Candidate Experience actually turn out to be a Scenario or campaign?
5. Are any Product Experience Definitions being created mainly to unblock H3?
6. Does H3 now have an independent semantic basis?
7. Would the definitions still be useful if H3 were permanently abandoned?
8. What source information would most improve the weakest definition?
9. Did the marketing/product communication surface materially distort any TES category?
10. Has Session 10 preserved the distinction between commercial usefulness and semantic authority?

---

### Success criterion

Session 10 succeeds if it can determine, without inventing semantics, which commercial Experience examples can become governed Product Experience Definitions and whether those independently valid definitions provide enough material to reopen H3.

A valid outcome may still be NO-GO.
<!-- FIN-TEXTO-ORIGINAL-S10 -->

---

<a id="sesion-11"></a>

## Capítulo 11 — Relevancia contextual de evidencia neutral

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-11-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1152; salida(s) de lectura en la(s) línea(s) 1165, 1169. Cotejado con el recuento histórico de 636 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 69295fa6cab01690f3019caab18caee98b255527116969c308cf18ba2c25d74e.

<!-- INICIO-TEXTO-ORIGINAL-S11 -->
### Convercus Demo Factory — Session 11: Contextual Evidence Relevance Experiment

#### Purpose

Session 9 stopped correctly because Demo Factory lacked two semantically defensible Experience contexts.

Session 10 resolved that prerequisite by creating independent Product Experience Definition candidates for:

* Aventura Familiar / Family Adventure
* Desafío Activo / Active Challenge
* Circuito Sostenible / Sustainable Circuit

Session 11 reopens H3 with a narrower proposition:

> The relevance of a neutral factual/evidentiary input can be derived from the situated relationship between that input and an Experience context, rather than being stored as an intrinsic universal property of the input.

The cognitive cycle is:

**APPLY → TEST → EVALUATE**

Do not implement TES Event recognition.

Do not implement Pattern, Sequence, Progression, Result, Measurement or Learning.

Do not build an Experience Engine.

---

### Core hypothesis

The experiment should test:

```text
relevance = f(EvidenceInput, ExperienceContext)
```

where:

```text
ExperienceContext =
    Product Experience Definition
    +
    Scenario instantiation
```

and therefore:

```text
f(X, ExperienceContext A)
!=
f(X, ExperienceContext B)
```

while:

* the factual input X remains unchanged;
* both Product Experience Definitions exist independently of H3;
* Scenario provides situated configuration rather than redefining the Experience;
* evaluation order does not alter the result;
* Activity remains a downstream projection.

---

### Important conceptual distinction

Do not assume that relevance belongs entirely to:

```text
ProductExperienceDefinition
```

or entirely to:

```text
Scenario
```

Session 11 should explicitly investigate whether the relevance criterion comes from:

1. the Experience semantic core;
2. Scenario-specific instantiation;
3. the combination of both.

This distinction is part of the experiment.

---

### Governed Experience material

Use the actual Product Experience Definition candidates created in Session 10.

#### Experience A

**Aventura Familiar / Family Adventure**

Its semantic candidate core concerns continuity of shared family/group participation in hotel activities during a stay.

Scenario-specific material may include:

* booking/stay;
* property;
* family/group context;
* locally available activity catalogue.

#### Experience B

**Desafío Activo / Active Challenge**

Its semantic candidate core concerns repeated sport/wellness participation during a stay.

Scenario-specific material may include:

* booking/stay;
* property;
* participant;
* locally available sport/wellness activity catalogue.

Do not modify either Product Experience Definition primarily to make the experiment pass.

---

### Primary evidence discriminant

Use one neutral factual input representing:

> a participant completed a cooking activity/class during a specific hotel stay.

The factual input should be able to exist independently of either Experience.

Conceptually:

```text
Evidence X
participant completed cooking class
during stay S
```

Evaluate the same X against both Experience contexts.

Expected hypothesis:

```text
Family Adventure Context
    → relevant

Active Challenge Context
    → not relevant
```

The difference must arise from independently meaningful Experience + Scenario criteria.

Do NOT implement:

```text
if experienceId == family-adventure:
    return relevant

if experienceId == active-challenge:
    return not_relevant
```

That would invalidate the experiment.

---

### Why Cooking Class is used

Cooking Class is intentionally selected as the primary discriminant because it provides a narrow test of contextual relevance:

* it is supported as an activity in Aventura Familiar;
* it is not part of the sport/wellness activity class represented by Desafío Activo.

The purpose is experimental isolation, not architectural richness.

Do not broaden this experiment into cooperative participation, partial completion or group evidence.

---

### Reserved future experiment — Treasure Hunt

Explicitly record the following future experimental candidate:

**Treasure Hunt / Búsqueda del Tesoro**

It must NOT be implemented in Session 11.

Its future purpose is to stress-test architecture around:

* cooperative resolution;
* multiple actors;
* individual versus group subject;
* partial evidence;
* distributed contribution;
* evidence aggregation;
* ordered and unordered clue resolution;
* partial sufficiency;
* group-level outcome reconstruction;
* possible tension between Scenario, participation and Experience semantics.

Conceptual example:

```text
Treasure Hunt
    ├── Participant A → clue/evidence A
    ├── Participant B → clue/evidence B
    ├── Participant C → clue/evidence C
    └── Group → partial / complete resolution
```

Do not infer TES Progression or Completion from this example.

This is a reserved future stress test, not part of H3.

---

### Factual input requirements

The Session-11 EvidenceInput should contain only the minimum factual information needed.

Possible fields:

* stable evidence/input ID;
* subject or participant reference;
* stay/property context;
* activity identifier;
* activity type/category;
* timestamp;
* source/provenance;
* reliability if already supported.

Do not add speculative fields.

The input must NOT contain:

* `experienceRef`;
* `significant`;
* `relevant`;
* evaluation outcome;
* stars;
* badges;
* progress count;
* reward;
* Activity icon/tone;
* editorial Activity copy.

---

### ExperienceContext

Introduce only the minimum representation required to evaluate the input against a situated Experience.

Do NOT create a generic ExperienceContext framework.

For the experiment, it may conceptually contain:

```text
ExperienceContext
    ProductExperienceDefinition reference
    Scenario-specific relevant configuration
```

For example:

```text
Family Adventure Context
    activity catalogue:
        treasure hunt
        cooking class
        football
        art workshop

Active Challenge Context
    activity class:
        sport/wellness
    examples:
        yoga
        spinning
        padel
        crossfit
```

Only represent what is supported by the Product Experience Definitions and source material.

Do not invent richer catalogues, eligibility or taxonomy unless required by the experiment.

---

### Evaluation boundary

Introduce the smallest possible boundary equivalent to:

```text
evaluateEvidenceRelevance(
    evidenceInput,
    experienceContext
) -> EvaluationOutcome
```

The exact naming and shape should follow repository conventions.

The evaluator must not:

* mutate EvidenceInput;
* mutate Product Experience Definition;
* mutate Scenario;
* mutate runtime participation state;
* write Activity;
* change checkpoint;
* grant reward;
* update Progression.

Prefer an explicit returned outcome.

---

### Evaluation outcome

Use neutral product-level semantics.

The minimum useful result may contain:

* relevant / not relevant;
* reason;
* Experience reference;
* Evidence reference.

Do not describe the result as a TES Event.

Do not use:

* Progression;
* Completion;
* Result;
* Pattern;
* reward state.

---

### Tests required

At minimum prove:

#### 1. Input independence

Cooking-class evidence exists without Experience or interpretation fields.

#### 2. Family Adventure relevance

The evidence is relevant under the Family Adventure ExperienceContext.

#### 3. Active Challenge non-relevance

The same evidence is not relevant under the Active Challenge ExperienceContext.

#### 4. Criterion-based evaluation

Demonstrate that evaluation depends on ExperienceContext criteria rather than Experience ID.

Changing an ID while preserving criteria must not change the semantic result.

#### 5. Scenario contribution

Identify whether the activity admissibility comes from:

* Product Experience Definition;
* Scenario;
* or their combination.

Test the actual implemented responsibility boundary.

#### 6. Immutability

Neither evaluation mutates the original EvidenceInput.

#### 7. Order independence

A → B and B → A produce the same individual results.

#### 8. Repeatability

Same input + same ExperienceContext produces the same outcome.

#### 9. Activity separation

Activity is not an evaluation input or source of truth.

#### 10. Session-7 regression

Presenter action/checkpoint behaviour remains green.

#### 11. Retail regression

Retail remains unaffected.

---

### Optional second discriminant

Only if it requires no new abstraction, evaluate a sport activity such as football.

This may produce:

```text
Family Adventure → relevant
Active Challenge → potentially relevant
```

for independently different reasons.

This is optional and must not broaden the implementation.

The primary discriminator remains Cooking Class.

---

### H3 decomposition

Evaluate four sub-hypotheses separately.

#### H3a — Input independence

A factual/evidentiary input can exist independently of Experience interpretation.

#### H3b — Contextual relevance

Relevance can differ according to ExperienceContext.

#### H3c — Evaluation independence

Evaluation does not mutate input and does not depend on evaluation order.

#### H3d — Projection separation

Activity remains downstream from evidence and interpretation.

---

### SignificantEvent assessment

Do not rename or modify `SignificantEvent` unless implementation becomes impossible otherwise.

Prefer Session 11 to operate before that contract.

After the experiment assess whether evidence now supports a conceptual boundary such as:

```text
EvidenceInput
      ↓
Contextual relevance evaluation
      ↓
[future unresolved recognition boundary]
      ↓
SignificantEvent
```

Do not promote this diagram to architecture automatically.

---

### EvidenceInput.interpretation assessment

Inspect the existing optional `EvidenceInput.interpretation`.

Determine whether Session 11 suggests that:

* it represents externally supplied/pre-resolved interpretation;
* it risks conflating factual input and contextual interpretation;
* it should remain provisional;
* a future separation may be required.

Do not redesign the contract broadly.

---

### Stop conditions

STOP and report rather than work around the issue if:

1. Cooking Class is not actually supported by Aventura Familiar;
2. Desafío Activo cannot defensibly exclude it from sport/wellness relevance;
3. relevance can only differ by Experience ID;
4. relevance requires Pattern, Progression or Result;
5. evaluation requires a participation engine;
6. EvidenceInput must contain the desired interpretation;
7. Activity must become source of truth;
8. a generic rules engine becomes necessary;
9. Product Experience Definitions must be changed primarily to satisfy H3;
10. Scenario begins absorbing general Experience semantics.

A stop condition is valid evidence.

---

### Explicit non-goals

Do not implement:

* Treasure Hunt;
* cooperative participation;
* partial clue resolution;
* group participation engine;
* TES Event recognition;
* SignificantEvent migration;
* Experience Engine;
* rules DSL;
* Pattern;
* Sequence;
* Progression;
* Result;
* Measurement;
* Learning;
* rewards;
* points;
* coverage;
* persistence;
* backend;
* real API;
* multi-provider architecture;
* generic eligibility;
* workflow engine;
* Builder;
* broad UI changes.

---

### Required final report

#### A. Semantic basis

Explain why Cooking Class provides a defensible contextual discriminant.

#### B. ExperienceContext responsibility

State explicitly what relevance information came from:

* Product Experience Definition;
* Scenario;
* their combination.

#### C. Change inventory

List files added and modified.

#### D. Actual evaluation flow

Show the implemented path.

#### E. Test evidence

Baseline, incremental tests and final full check.

#### F. H3 sub-hypothesis verdicts

For H3a–H3d use:

* SUPPORTED
* PARTIALLY SUPPORTED
* FALSIFIED
* INCONCLUSIVE

#### G. Overall H3 verdict

Use:

* SUPPORTED — READY FOR ADR
* SUPPORTED WITH QUALIFICATION
* PARTIALLY SUPPORTED
* FALSIFIED
* INCONCLUSIVE

#### H. SignificantEvent assessment

State what the experiment teaches about its semantic position.

#### I. EvidenceInput.interpretation assessment

State whether conflation risk has increased or decreased.

#### J. Architecture impact

State whether Architecture v0.4 survives or requires qualification.

#### K. Technical debt

List experimental shortcuts.

#### L. Reversibility

Explain exact rollback.

#### M. Reserved Treasure Hunt experiment

Confirm that no Treasure Hunt behaviour was implemented.

Record the still-open future questions:

* cooperative participation;
* group vs individual subject;
* partial evidence;
* aggregation;
* partial solution;
* ordered/unordered clues;
* evidence sufficiency.

#### N. Next mature decision

Identify only what has actually become mature.

---

### Final adversarial questions

1. Did relevance depend on ExperienceContext criteria rather than Experience ID?
2. Could EvidenceInput exist if neither Experience existed?
3. Did Scenario contribute meaningful situated information?
4. Did Scenario start absorbing semantic rules that belong elsewhere?
5. Did either evaluation mutate the input?
6. Did order affect the result?
7. Did `relevant` accidentally become equivalent to TES Event?
8. Did hidden Progression appear?
9. Does Activity remain entirely downstream?
10. Could the same evaluator operate on another activity without special-case code?
11. What remains too weak in the Product Experience Definitions?
12. What would a real API potentially invalidate?
13. What should not be generalized from Session 11?
14. Has Treasure Hunt remained untouched and available for a richer future experiment?

---

### Success criterion

Session 11 succeeds if:

> The same neutral Cooking Class evidence is deterministically relevant to Family Adventure and not relevant to Active Challenge because of independently meaningful Product Experience Definition + Scenario criteria, without mutating the input, hard-coding Experience IDs, invoking TES Progression or making Activity authoritative.

Do not optimize beyond this criterion.
<!-- FIN-TEXTO-ORIGINAL-S11 -->

---

<a id="sesion-12"></a>

## Capítulo 12 — Fronteras de autoridad y mundo abierto

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-12-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1316; salida(s) de lectura en la(s) línea(s) 1324, 1328. Cotejado con el recuento histórico de 608 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 2fb55be881ca6eab32f27cb1df8de54ccb507bc15a3d02b4b301e1230450acc7.

<!-- INICIO-TEXTO-ORIGINAL-S12 -->
### Convercus Demo Factory — Session 12: Authority Frontiers and Open-World Evaluation Semantics

#### Purpose

Session 11 successfully demonstrated a narrow product-level proposition:

> contextual relevance can be derived from neutral factual evidence + Product Experience Definition + Scenario without storing relevance inside the factual input, making Activity authoritative, or recognizing a TES Event.

Before promoting this into ADR-005 or moving to the reserved Treasure Hunt experiment, Session 12 must examine three architectural tensions revealed by the accumulated evidence:

1. **authority frontiers** — which artefact or layer has authority to make which claims;
2. **open-world relevance semantics** — `not relevant` must not silently mean `unknown`, `insufficient` or `not evaluable`;
3. **ExperienceDefinition authority ambiguity** — multiple artefacts currently use the name `ExperienceDefinition` despite representing different semantic maturity and runtime responsibilities.

Do NOT modify application code.

Do NOT create ADR-005 before completing the analysis.

Do NOT rename contracts.

Do NOT modify TES.

The cognitive progression is:

**ANALYZE → EVALUATE → CONSOLIDATE → CREATE**

---

### Part A — Verify the current ADR foundation

Inspect ADR-001 through ADR-004 and Session-11 implementation/evidence.

Do not assume the ADRs need modification.

Determine:

* what each ADR already says about authority;
* where authority is explicit;
* where it is only implied;
* whether Session 11 contradicts any accepted decision;
* whether new findings fit as subordinate architectural decisions.

Pay special attention to:

* ADR-001 semantic authority;
* ADR-002 factual/runtime/read-model authority;
* ADR-003 desired/effective composition authority;
* ADR-004 Experience/Scenario/Script/runtime authority.

Report any genuine contradiction separately from an unresolved boundary.

---

### Part B — Define the concept of Authority Frontier

Use **Authority Frontier** as a product/architecture analytical term, not a TES concept.

Working definition to test:

> An Authority Frontier identifies the scope within which an artefact, component or source is entitled to make a claim, and the point beyond which a new interpretation, validation or authority is required.

Determine whether this concept genuinely adds explanatory power beyond ordinary layering.

Test it against existing examples:

```text
TES
→ semantic meaning/invariants

Product Experience Definition
→ governed product interpretation

Scenario
→ situated context

Source/provider
→ factual observation within its contract

Contextual evaluator
→ relational evaluation outcome

Runtime
→ operational mutable state

Read model / Activity
→ presentation
```

Do not assume these boundaries are final.

---

### Part C — Build an Authority Frontier Matrix

Create a matrix with at minimum these columns:

| Artefact / layer | Authoritative claims | Inputs it may trust | Claims it may derive | Claims it must NOT make | Required provenance / version | Open questions |

Include at minimum:

* TES corpus;
* Product Interpretation;
* commercial/product source material;
* candidate Product Experience Definition;
* validated Product Experience Definition if conceptually distinct;
* runtime Experience descriptor/reference;
* Scenario;
* activity/product catalogue or classification source;
* provider/source;
* neutral EvidenceInput;
* contextual relevance evaluator;
* `SignificantEvent`;
* runtime state;
* Demo Script;
* Demo Manifest;
* bootstrap/resolution;
* AppSnapshot;
* Activity/read model.

If an artefact does not yet exist concretely, mark it **conceptual/provisional**.

---

### Part D — Classification authority from Session 11

Session 11 currently uses:

```text
Scenario:
Cooking Class → shared-hotel-activity
```

while the Experience context declares which activity classifications are relevant.

This worked experimentally but does not establish Scenario as the final taxonomy authority.

Analyse alternative authority locations, without implementing them:

* Scenario;
* Product Experience Definition;
* reusable activity/product catalogue;
* provider/source;
* property configuration;
* shared taxonomy;
* externally supplied classification;
* composed authority across more than one source.

For each, evaluate:

* semantic appropriateness;
* reuse;
* versioning;
* local variation;
* risk of Scenario becoming semantic authority;
* risk of provider data becoming product meaning;
* compatibility with ADR-004.

Do NOT choose a final taxonomy architecture unless evidence supports it.

The key question is:

> Who has authority to assert that an observed activity belongs to a classification that an Experience can evaluate?

---

### Part E — Open-world relevance semantics

Session 11 used a deliberately minimal binary:

```text
relevant
not_relevant
```

Do NOT promote that binary into architecture.

Analyse the distinction between at least these conceptual situations:

##### Positive determination

Enough authoritative information exists to conclude that the evidence is relevant.

##### Negative determination

Enough authoritative information exists to conclude that it is not relevant.

##### Undetermined

The available evidence/context/authority is insufficient to make either conclusion.

Also analyse whether other conditions may need future distinction, such as:

* unknown classification;
* missing context;
* unsupported evaluator;
* contradictory evidence;
* unreliable source;
* not evaluable under current version.

Do NOT define a final enum.

Do NOT create a universal state machine.

The architectural question is:

> What minimum semantic invariant prevents absence of knowledge from collapsing into a negative claim?

---

### Part F — Relation between authority and evaluation outcome

Test the proposition:

```text
EvaluationOutcome =
f(
  Evidence,
  ExperienceContext,
  AvailableAuthority
)
```

rather than merely:

```text
EvaluationOutcome =
f(Evidence, ExperienceContext)
```

Analyse concrete examples.

#### Example 1 — Known negative

Cooking Class is authoritatively classified as non-sport/wellness in the relevant Scenario/catalogue context.

Can `not relevant` be justified?

#### Example 2 — Unknown activity

The input identifies an activity not present in the local catalogue.

Is that:

* not relevant;
* unknown;
* unevaluable?

What authority is missing?

#### Example 3 — Missing property/stay context

The evidence exists but cannot be situated against the Scenario.

What may the evaluator claim?

#### Example 4 — Conflicting classifications

Two sources classify the same activity differently.

Which layer has authority to resolve that conflict, if any?

Do not solve conflicts by arbitrary precedence.

---

### Part G — `ExperienceDefinition` authority ambiguity

There is now a deliberate tension to analyse.

ADR-001 states that an `ExperienceDefinition` must identify the TES baseline against which it was validated.

However, the repository currently contains or references conceptually different artefacts using the same or similar `ExperienceDefinition` name.

Inspect at minimum:

#### 1. Product Experience Definition candidates from Session 10

Examples:

* Aventura Familiar;
* Desafío Activo;
* Circuito Sostenible.

They are explicitly:

**READY WITH EXPLICIT GAPS — non-executable candidate**

and therefore must not be mistaken for fully validated TES-governed definitions.

#### 2. `prototype/src/domain/contracts.ts::ExperienceDefinition`

This is a richer functional candidate but does not yet demonstrate full TES semantic completeness or runtime authority.

#### 3. `prototype/src/demo-factory/contracts.ts::ExperienceDefinition`

This contains only identity/baseline-level information and acts operationally as a runtime descriptor/reference.

---

### Part H — Distinguish authority, maturity and representation

For each Experience-related artefact, determine separately:

##### Semantic authority

What meaning is it entitled to assert?

##### Validation maturity

Candidate / validated / experimental / legacy / runtime-only / other.

##### Representation role

Definition / reference / descriptor / projection / configuration.

##### Executability

Non-executable / runtime reference / executable contract / unresolved.

##### TES relationship

Which baseline is referenced, and does the reference mean:

* interpreted against;
* validated against;
* merely associated with?

Do not assume those are equivalent.

---

### Part I — Test the naming problem

Evaluate whether the current shared use of `ExperienceDefinition` creates a material risk of false authority.

Specifically test the misleading inference:

```text
object named ExperienceDefinition
+
tesBaseline
=
TES-validated semantic definition
```

which must NOT be assumed.

Determine whether a future conceptual distinction may be necessary, potentially along lines such as:

```text
CandidateProductExperienceDefinition
ValidatedProductExperienceDefinition
RuntimeExperienceReference
RuntimeExperienceDescriptor
```

These are examples only.

Do NOT rename files, types or contracts.

Recommend terminology only if it materially reduces authority ambiguity.

---

### Part J — ADR-001 compatibility review

Determine whether ADR-001 requires:

* no change;
* clarification;
* future amendment;
* reconsideration.

Pay special attention to the phrase requiring every `ExperienceDefinition` to identify the TES baseline against which it was validated.

Ask:

1. Should the obligation apply only to semantically validated definitions?
2. Can a candidate definition reference a baseline without claiming validation?
3. Should runtime references carry `tesBaseline` indirectly through the definition they reference?
4. Does the current wording risk treating candidate or descriptor artefacts as validated?
5. Can this be resolved by terminology/governance rather than reopening ADR-001?

Prefer no ADR modification unless a genuine contradiction exists.

---

### Part K — Authority provenance

Analyse whether future derived claims should carry information about:

* source authority;
* source version;
* Experience Definition version/status;
* Scenario version;
* evaluator version;
* classification authority;
* reason/rationale.

Do NOT design a full provenance schema.

Determine only which dimensions appear necessary to prevent a derived claim from appearing more authoritative than its inputs.

---

### Part L — Proposed narrow ADR-005 scope

Only after completing the authority and open-world analysis, draft the intended scope of a future ADR.

Do NOT create it yet unless the evidence is unequivocally sufficient.

Candidate scope:

**Neutral Evidence and Authority-Bounded Contextual Evaluation**

Potential invariant:

> Factual evidence remains distinct from Experience-relative evaluation. Any derived relevance claim must be scoped to an Experience context and to the authority available for that evaluation. Absence of sufficient authority or context must not silently collapse into a negative relevance claim. A relevance outcome does not by itself recognize a TES Event and does not belong to Activity.

Evaluate whether this is now mature.

List explicitly what such an ADR must NOT decide:

* final relevance enum;
* classification taxonomy;
* classification-authority implementation;
* Event recognition;
* SignificantEvent migration;
* persistence;
* generic rule engine;
* participation;
* Pattern/Sequence/Progression;
* provider/API topology.

---

### Part M — Architecture v0.5 candidate

Do not automatically publish Architecture v0.5.

First determine whether the new concept changes accepted architecture or only adds an analytical annotation.

If useful, propose a candidate shape:

```text
Source / Evidence Authority
        ↓
Neutral factual evidence
        ↓
Experience Definition + Scenario + classification authority
        ↓
Authority-bounded contextual evaluation
        ↓
[future unresolved recognition boundary]
        ↓
Runtime / projections as applicable
```

Mark all non-accepted boundaries clearly.

---

### Part N — Reserved Treasure Hunt experiment

Treasure Hunt remains explicitly reserved.

Do NOT implement it.

Use Session-12 analysis to refine what that future experiment should attack.

At minimum preserve:

* multiple participants;
* individual and group subject;
* partial evidence;
* evidence aggregation;
* cooperative contribution;
* partial resolution;
* ordered/unordered clues;
* contradictory or missing evidence;
* evidence sufficiency;
* reconstruction of a group-level outcome.

Now add two explicit stress dimensions:

#### Authority

Who may assert:

* clue observed;
* clue solved;
* contribution belongs to participant;
* contributions belong to one group;
* partial solution is valid;
* whole hunt is resolved?

#### Open-world semantics

Distinguish:

```text
false / negative
```

from:

```text
unknown / unresolved / insufficient
```

without defining final terminology yet.

The future Treasure Hunt experiment should be designed specifically to falsify the current assumptions of:

* atomic evidence;
* individual subject;
* binary relevance;
* single authoritative classification.

---

### Part O — Decide the next step

At the end recommend exactly one:

##### Option A

Create ADR-005 in a subsequent documentation-only session.

##### Option B

Perform one more focused experiment before ADR-005 because authority/open-world behaviour remains under-evidenced.

##### Option C

Reopen an existing ADR because a genuine contradiction has appeared.

##### Option D

Proceed to Treasure Hunt design because authority boundaries are sufficiently understood.

Explain why.

---

### Required output

1. Session-12 executive conclusion
2. ADR-001–004 compatibility review
3. Authority Frontier concept assessment
4. Authority Frontier Matrix
5. Classification-authority analysis
6. Open-world relevance analysis
7. Authority × evaluation-outcome analysis
8. `ExperienceDefinition` ambiguity analysis
9. Experience artefact maturity/authority matrix
10. ADR-001 wording compatibility assessment
11. Authority provenance requirements
12. ADR-005 readiness and proposed scope
13. Candidate Architecture v0.5 implications
14. Treasure Hunt authority/open-world preparation
15. Remaining risks
16. Recommended next step

---

### File creation

Create only:

* one Session-12 analysis/consolidation report.

Do not create ADR-005 yet.

Do not modify ADR-001–004.

Do not modify application code.

Do not rename `ExperienceDefinition`.

---

### Final adversarial questions

1. Does Authority Frontier add explanatory power beyond ordinary architecture layers?
2. Which current artefact is most likely to overstate its authority?
3. Who currently has de facto classification authority in Session 11?
4. Is that authority legitimate or merely experimental convenience?
5. Under what conditions can `not relevant` be asserted confidently?
6. What situations currently collapse incorrectly into the same binary result?
7. Can an evaluator make a negative claim when classification authority is missing?
8. Does `tesBaseline` mean the same thing for candidate, validated and runtime artefacts?
9. Does the name `ExperienceDefinition` currently transfer false semantic authority?
10. Can the ambiguity be solved without modifying ADR-001?
11. What minimum provenance prevents derived claims from exceeding their sources?
12. Is ADR-005 now mature?
13. What would Treasure Hunt falsify that Cooking Class could not?
14. Have we accidentally designed an ontology of relevance instead of identifying an architectural invariant?

---

### Success criterion

Session 12 succeeds if it can establish:

> which system actors are authoritative for which claims, why contextual evaluation cannot safely be assumed binary in an open-world setting, and whether the current `ExperienceDefinition` naming/maturity model risks transferring semantic authority that its artefacts do not possess.

The session must improve governance without inventing a final taxonomy, relevance ontology or Experience runtime.
<!-- FIN-TEXTO-ORIGINAL-S12 -->

---

<a id="sesion-13"></a>

## Capítulo 13 — Evaluación open-world acotada por autoridad

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-13-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1371; salida(s) de lectura en la(s) línea(s) 1379, 1385, 1389. Cotejado con el recuento histórico de 1340 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: b2d1c94fea1d1dd44e8dbd62fe63618c5995acb78f09436a06ed83994cf47470.

<!-- INICIO-TEXTO-ORIGINAL-S13 -->
### Session 13 — Authority-Bounded Open-World Evaluation Experiment

Trabaja sobre el repositorio existente:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

No empieces desde cero.

No rediseñes la arquitectura.

No conviertas esta sesión en una implementación de plataforma.

La arquitectura vigente está definida por ADR-001, ADR-002, ADR-003 y ADR-004. Session 12 ya está consolidada y NO debe repetirse.

ADR-005 todavía NO existe como decisión aceptada y NO debe crearse durante esta sesión.

Architecture v0.5 NO debe publicarse durante esta sesión.

Treasure Hunt / Búsqueda del Tesoro permanece reservado para un experimento posterior.

El método obligatorio es:

```text
hypothesis
→ falsification
→ reversible experiment
→ evidence
→ evaluation
```

Un resultado:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NO-GO
STOP
```

es legítimo.

Nunca introduzcas semántica, tipos, taxonomías, engines o arquitectura únicamente para obtener tests verdes.

---

### 1. Objetivo de Session 13

Session 11 demostró, con cualificación:

```text
neutral factual evidence
        ≠
Experience-relative relevance
        ≠
Activity projection
```

Session 12 identificó una limitación material del experimento:

```text
relevant / not_relevant
```

no es una semántica promovible en un mundo abierto porque:

```text
absence of knowledge
≠
negative claim
```

Session 13 debe producir evidencia ejecutable mínima sobre una cuestión más precisa:

> ¿Puede cambiar el tipo de claim legítimo al cambiar la autoridad disponible, manteniendo constantes la Evidence y el ExperienceContext?

La sesión debe investigar únicamente la diferencia entre:

```text
known positive
known negative
undetermined
```

sin convertir esos términos en una ontología universal ni en un enum arquitectónico definitivo.

---

### 2. Hipótesis experimental

#### H13 — Authority-bounded evaluation

> Para Evidence y ExperienceContext constantes, el tipo de claim que puede emitir una evaluación contextual está limitado por la competencia, scope y cobertura de la autoridad disponible. La ausencia de autoridad suficiente no autoriza un claim negativo.

Formulación analítica provisional:

```text
EvaluationOutcome =
f(
    Evidence,
    ExperienceContext,
    AvailableAuthority
)
```

`AvailableAuthority` es una variable experimental/conceptual.

NO debes asumir que necesita convertirse en:

* objeto universal;
* service;
* registry;
* provider;
* interface arquitectónica;
* catálogo global;
* authority engine.

La forma exacta deberá ser únicamente la mínima necesaria para falsificar la hipótesis.

---

### 3. Subhipótesis a intentar falsificar

#### H13a — Positive authority

Una clasificación positiva explícita emitida por una autoridad competente puede sostener un positive determination dentro de su scope.

#### H13b — Explicit negative authority

Una exclusión explícita emitida por una autoridad competente puede sostener un negative determination dentro de su scope.

#### H13c — Incomplete knowledge

La ausencia de una clasificación en una fuente o catálogo que NO declara cobertura exhaustiva no puede sostener un negative determination.

Debe permanecer:

```text
undetermined
```

o equivalente experimental.

#### H13d — Scoped exhaustive coverage

La ausencia de una clasificación puede sostener un negative determination únicamente cuando una autoridad competente declara cobertura suficientemente exhaustiva para el scope/version evaluados.

#### H13e — Missing authority

La ausencia de classification authority competente debe permanecer indeterminada.

#### H13f — Conflicting authority

Claims competentes en conflicto, sin una policy de precedence ya demostrada, deben permanecer indeterminados/conflicting.

El evaluator NO debe inventar precedence.

#### H13g — Evaluator non-authority

El evaluator puede derivar un claim relacional a partir de inputs y autoridad disponible.

NO puede convertirse él mismo en fuente de:

* clasificación;
* semántica TES;
* factual truth;
* Experience validation;
* Event recognition.

#### H13h — Activity non-escalation

Activity puede proyectar downstream un EvaluationOutcome, pero no puede:

* originarlo;
* reforzar su autoridad;
* reinterpretarlo;
* convertir `undetermined` en `negative`;
* eliminar qualifiers de conflicto o insuficiencia;
* convertir relevance en TES Event, Progression, Result o Completion.

---

### 4. Inspección obligatoria antes de modificar código

Antes de implementar nada, inspecciona el repositorio real.

Localiza como mínimo:

* el evaluator introducido en Session 11, probablemente `evaluateEvidenceRelevance`;
* sus tipos de Evidence;
* sus tipos/contextos de Experience;
* los fixtures de Cooking Class;
* Family Adventure;
* Active Challenge;
* Scenario utilizado en Session 11;
* `activityCatalogue`;
* `ActivityClassification` o forma equivalente;
* tests actuales del evaluator;
* cualquier consumidor runtime del evaluator;
* cualquier consumidor UI/read model;
* Activity;
* AppSnapshot;
* `domain/contracts.ts::ExperienceDefinition`;
* `demo-factory/contracts.ts::ExperienceDefinition`;
* cualquier campo `tesBaseline`;
* documentación de Session 11;
* documentación de Session 12;
* ADR-001–004.

Primero informa brevemente de la topología real encontrada.

No adaptes silenciosamente la arquitectura a esta instrucción.

Si encuentras una contradicción material entre el repositorio y el baseline descrito aquí:

```text
STOP
```

y documenta la contradicción.

Una diferencia de naming o localización de archivo no es por sí misma contradicción material.

---

### 5. Baseline arquitectónico que debes preservar

Arquitectura aceptada aproximada v0.4:

```text
TES semantic authority
        ↓
Product contracts / interpretations
        ↓
Experience Definition
        ↓
Scenario
        ↓
Demo Manifest / desired composition
        ↓
Bootstrap / effective composition
        ↓
Runtime
        ↓
Read Models / UI
```

Separación Experience / Scenario / Demo Script:

```text
Experience Definition
        ↑ instantiated/referenced by
Scenario
        ↑ demonstrated through
Demo Script
```

Frontera operacional:

```text
Demo Script
→ Public Action
→ Runtime Boundary
→ Controlled Runtime Transition
→ Read Model / UI
```

Separación lógica aceptada:

```text
Composition
Runtime State
Read Models
```

No implica tres stores físicos.

Activity permanece:

```text
read model / projection
```

y nunca:

```text
factual authority
evidence ledger
TES Event ledger
```

---

### 6. Guardrail upstream — tensión de ADR-001 y Experience authority

Session 12 confirmó una ambigüedad real:

no todos los artefactos llamados `ExperienceDefinition` poseen la misma autoridad.

Actualmente deben distinguirse conceptualmente, aunque NO deben renombrarse necesariamente en esta sesión:

```text
Candidate Product Experience Definition
→ interpreted against TES
→ non-executable candidate
→ explicit gaps

domain/contracts.ts::ExperienceDefinition
→ functional/product translation candidate
→ richer contract
→ not demonstrated as TES-complete

demo-factory/contracts.ts::ExperienceDefinition
→ runtime Experience descriptor/reference
→ minimal runtime representation
```

No debes asumir:

```text
object named ExperienceDefinition
+
tesBaseline
=
TES-validated Experience Definition
```

Tampoco debes asumir:

```text
bootstrap resolved Experience reference
=
semantic validation
```

Ni:

```text
tesBaseline
=
validation certificate
```

Para esta sesión:

```text
runtime Experience descriptor
≠
validated Product Experience Definition
≠
classification authority
```

El evaluator NO puede utilizar:

* el nombre `ExperienceDefinition`;
* presencia de `tesBaseline`;
* resolución bootstrap;
* presencia runtime;

como evidencia de autoridad semántica o clasificadora.

Si el experimento necesita hacerlo para alcanzar los resultados esperados:

```text
STOP
```

No reabras ADR-001.

No renombres todavía las interfaces salvo que exista una necesidad estrictamente local y reversible, y en tal caso documenta por qué.

No conviertas esta sesión en una migración de `ExperienceDefinition`.

---

### 7. Guardrail downstream — Authority Frontier de Activity

Activity permanece downstream.

La dirección legítima es:

```text
Evidence
   ↓
Authority-bounded contextual evaluation
   ↓
EvaluationOutcome
   ↓
Projection
   ↓
Activity / UI
```

La dirección inversa está prohibida:

```text
Activity
   ↓
Evaluation
```

Activity puede eventualmente presentar o resumir un EvaluationOutcome.

Pero Activity NO puede:

* convertirse en input autoritativo del evaluator;
* demostrar que la actividad ocurrió;
* clasificar la actividad;
* resolver incertidumbre;
* escoger entre fuentes en conflicto;
* convertir un `undetermined` en `negative`;
* convertir una evaluación relativa a Experience en TES Event;
* inferir Progression, Result o Completion;
* adquirir mayor autoridad por ser visible en UI.

Invariant experimental:

> Activity may project or summarize an EvaluationOutcome but may not strengthen, resolve or reinterpret its epistemic status.

Expresado provisionalmente:

```text
Authority(Activity representation)
<=
Authority(projected source claim)
```

No promociones esta fórmula como axioma arquitectónico general durante esta sesión.

Úsala únicamente como guardrail experimental.

Cuando inspecciones el repositorio, comprueba si Activity participa actualmente en el evaluator.

Si no existe dependencia:

* documenta la separación;
* no construyas un test artificial de UI solo para demostrar lo evidente.

Si existe dependencia:

* identifícala como riesgo material;
* aplica el cambio mínimo necesario para restaurar la dirección correcta;
* documenta el delta.

Una modificación o eliminación de la proyección Activity no debe alterar el outcome del evaluator.

---

### 8. Qué NO cuenta como AvailableAuthority

Para este experimento:

```text
AvailableAuthority
≠
runtime resolution
≠
artifact naming
≠
tesBaseline field
≠
Activity/read-model presentation
≠
evaluator implementation itself
≠
provider label by mere presence
```

La autoridad debe proceder de un input explícitamente tratado como competente para el claim que emite, dentro de un scope declarado o experimentalmente controlado.

No conviertas esa afirmación en una arquitectura final de authority management.

---

### 9. Evidence constante

Reutiliza el mismo caso factual de Session 11.

Conceptualmente:

```text
participant completed Cooking Class
during stay S
at property P
```

El input debe permanecer neutral respecto a Experience.

No añadas al Evidence campos que afirmen:

```text
relevant
significant
TES Event
progress
result
reward
```

Si `EvidenceInput.interpretation` existe actualmente, no lo uses como atajo para introducir la conclusión que el evaluator debería derivar.

Si participa materialmente, documenta cómo se trata y preserva su carácter provisional.

---

### 10. ExperienceContext constante en los tests críticos

Para aislar la variable autoridad, los tests centrales deben mantener constantes:

```text
Evidence
+
ExperienceContext
```

y cambiar únicamente la autoridad/cobertura disponible.

El caso recomendado para los tests críticos es:

```text
Evidence:
Cooking Class completed

ExperienceContext:
Active Challenge
+
same stay
+
same property
```

Active Challenge requiere experimentalmente una clasificación relacionada con:

```text
sport-wellness
```

No branches por Experience ID.

Los criterios deben proceder de la representación existente de la Product Experience Definition/contexto experimental.

---

### 11. Casos obligatorios

#### Caso A — Positive control

Usa Family Adventure como control positivo ya defendible desde Session 11.

Una autoridad competente afirma explícitamente:

```text
Cooking Class
→ shared-hotel-activity
```

Family Adventure acepta esa clase.

Resultado permitido:

```text
positive determination
```

No interpretes el resultado como TES Event.

---

#### Caso B — Explicit known negative

Mantén:

```text
Evidence = Cooking Class
ExperienceContext = Active Challenge + same stay/property
```

Una autoridad competente afirma explícitamente:

```text
Cooking Class
NOT sport-wellness
```

Active Challenge requiere `sport-wellness`.

Resultado permitido:

```text
negative determination
```

El negativo queda limitado al scope/version de la autoridad.

No extrapoles universalmente:

```text
Cooking Class is never sport/wellness
```

---

#### Caso C — Incomplete authority

Mantén EXACTAMENTE:

```text
same Evidence
same Active Challenge ExperienceContext
```

La autoridad afirma:

```text
Cooking Class
→ shared-hotel-activity
```

pero NO declara que el conocimiento de clasificaciones de Cooking Class sea completo.

La ausencia de:

```text
sport-wellness
```

NO autoriza un negativo.

Resultado esperado:

```text
undetermined
```

Este es un falsificador central de Session 13.

Si devuelve negative:

```text
H13c FAILED
```

No modifiques semántica para evitarlo.

---

#### Caso D — Scoped exhaustive authority

Mantén:

```text
same Evidence
same ExperienceContext
```

Ahora la autoridad declara que el conjunto conocido de clasificaciones es exhaustivo para un scope/version concretos.

Por ejemplo conceptualmente:

```text
known classifications:
- shared-hotel-activity

coverage:
complete for activity classification
within property P / catalogue version V
```

Si:

```text
sport-wellness
```

no pertenece al conjunto exhaustivo conocido, puede sostenerse:

```text
negative determination
```

únicamente dentro de ese scope.

No conviertas `complete` en propiedad universal.

---

#### Caso E — Missing classification authority

Mismos:

```text
Evidence
ExperienceContext
```

No existe classification authority competente disponible.

Resultado esperado:

```text
undetermined
```

Nunca:

```text
negative
```

---

#### Caso F — Conflicting authority

Mismos:

```text
Evidence
ExperienceContext
```

Dos claims competentes disponibles entran en conflicto.

Conceptualmente:

```text
Authority A:
Cooking Class → sport-wellness

Authority B:
Cooking Class NOT sport-wellness
```

No existe una precedence policy aceptada.

Resultado esperado:

```text
undetermined / conflicting
```

No:

```text
choose A
```

ni:

```text
choose B
```

NO implementes source precedence.

---

### 12. Representación experimental del outcome

El booleano de Session 11:

```text
relevant: boolean
```

es sospechoso porque puede colapsar:

```text
known negative
undetermined
```

en:

```text
false
```

Inspecciona primero sus consumidores.

Si no existen consumidores que exijan compatibilidad, puedes sustituir o cualificar el contrato mediante la forma local mínima que preserve los tres tipos de claim.

Puede utilizarse, por ejemplo:

* discriminated union;
* literal union;
* test-local representation;
* objeto experimental mínimo.

Pero NO promociones la forma elegida a:

* ontology;
* universal `EvaluationOutcome`;
* API contract;
* TES concept;
* cross-domain rules language.

La representación utilizada es:

```text
experimental mechanism
```

hasta evaluación posterior.

No elijas nombres pensando en arquitectura final.

El objetivo es preservar la diferencia epistemológica, no diseñar vocabulario definitivo.

---

### 13. Representación experimental de authority/completeness

Puedes introducir únicamente lo mínimo necesario para expresar experimentalmente:

```text
positive classification assertion
explicit exclusion
incomplete coverage
scoped exhaustive coverage
missing authority
conflicting claims
```

No construyas:

```text
ClassificationAuthorityRegistry
AuthorityService
TaxonomyService
AuthorityProvider
PrecedencePolicyEngine
GenericCataloguePlatform
```

Una función pura + fixtures explícitos es preferible si basta.

Los fixtures NO se promocionan a arquitectura.

---

### 14. Falsificadores explícitos

Considera H13 total o parcialmente falsificada/no soportada si ocurre cualquiera de estos casos:

1. ausencia en un catálogo incompleto produce negative;
2. missing classification authority produce negative;
3. conflicto entre claims competentes se resuelve mediante precedence inventada;
4. el evaluator necesita branch por Experience ID;
5. el evaluator inventa clasificaciones;
6. el evaluator usa Activity como input autoritativo;
7. Activity transforma `undetermined` en `negative` como parte de la lógica;
8. el evaluator usa `tesBaseline` como certificado de validación;
9. el evaluator usa el nombre `ExperienceDefinition` como prueba de autoridad;
10. bootstrap resolution se interpreta como semantic validation;
11. el evaluator necesita reconocer TES Event para calcular relevance;
12. hace falta construir taxonomy/authority/rules engine para ejecutar el experimento;
13. cambiar authority/coverage no puede cambiar el claim legítimo manteniendo constantes Evidence y ExperienceContext;
14. el experimento solo funciona añadiendo semántica no respaldada por las Product Experience Definition candidates existentes.

Si ocurre una de estas situaciones, no amplíes el sistema para obtener el resultado esperado.

Documenta:

```text
FAILED
INCONCLUSIVE
NO-GO
STOP
```

según corresponda.

---

### 15. Restricciones permanentes de Session 13

NO debes:

* crear ADR-005;
* publicar Architecture v0.5;
* reabrir ADR-001–004 salvo contradicción genuina;
* declarar `ExperienceDefinition` semánticamente validada por nombre;
* asumir `tesBaseline = validated`;
* resolver la nomenclatura final de Experience artifacts;
* fijar classification authority final;
* asumir Scenario como classification authority final;
* asumir provider como semantic authority;
* construir shared taxonomy;
* diseñar taxonomy final;
* implementar precedence de fuentes;
* crear Experience engine;
* crear participation engine;
* crear generic rules DSL;
* introducir persistencia;
* introducir event sourcing;
* crear evidence ledger;
* crear audit platform;
* reconocer TES Event;
* promover `RelevantEvidence = SignificantEvent`;
* modificar `SignificantEvent` salvo necesidad estricta e incidental;
* diseñar TES Pattern;
* diseñar TES Sequence;
* diseñar TES Progression;
* diseñar TES Result;
* diseñar Measurement;
* diseñar Learning;
* diseñar Treasure Hunt;
* inventar arquitectura API sin API real verificada.

---

### 16. Preference for minimum reversible delta

Preferencia:

```text
existing evaluator
+
minimal authority representation
+
open-world outcome distinction
+
focused tests
+
session documentation
```

No:

```text
new architectural subsystem
```

El experimento debe poder retirarse con un delta pequeño si H13 no sobrevive.

No conviertas implementaciones experimentales en contratos públicos salvo que ya sean necesarios por la topología real existente.

---

### 17. Tests mínimos esperados

La matriz experimental mínima debe demostrar:

| Evidence      | ExperienceContext | Authority                                   | Coverage                       | Expected claim           |
| ------------- | ----------------- | ------------------------------------------- | ------------------------------ | ------------------------ |
| Cooking Class | Family Adventure  | positive membership → shared-hotel-activity | sufficient for positive        | positive                 |
| Cooking Class | Active Challenge  | explicit exclusion from sport-wellness      | scoped competent               | negative                 |
| Cooking Class | Active Challenge  | shared-hotel-activity only                  | incomplete                     | undetermined             |
| Cooking Class | Active Challenge  | classification set without sport-wellness   | explicitly exhaustive in scope | negative                 |
| Cooking Class | Active Challenge  | none                                        | none                           | undetermined             |
| Cooking Class | Active Challenge  | conflicting competent claims                | unresolved                     | undetermined/conflicting |

Añade únicamente tests adicionales si una condición real del repositorio los exige.

Comprueba también:

```text
no Experience-ID branching
```

y:

```text
Activity not required for evaluator outcome
```

Si Activity solo es downstream y no participa en el evaluator, no construyas una gran batería UI.

---

### 18. Verificación del repositorio

Ejecuta todas las verificaciones reales que ya utilice el proyecto.

Como mínimo, si existen:

```text
tests
typecheck
lint
build
```

No sustituyas la suite completa por tests aislados.

Informa:

* test files totales;
* tests totales;
* tests passing/failing;
* typecheck;
* lint;
* build;
* archivos modificados;
* archivos nuevos;
* archivos eliminados;
* branches específicos por Experience ID encontrados o no encontrados.

Si alguna verificación no existe en el repositorio, indícalo.

---

### 19. Documento de Session 13

Crea un documento de sesión siguiendo el estilo real de las sesiones anteriores.

Título:

```text
Session 13 — Authority-Bounded Open-World Evaluation Experiment
```

Debe contener como mínimo:

#### Hypothesis

H13 y subhipótesis.

#### Falsifiers

Lista explícita.

#### Repository state before experiment

Qué existía antes y qué autoridad tenía cada artefacto relevante.

#### Authority guardrails

Documenta expresamente:

```text
tesBaseline ≠ validation certificate
runtime Experience descriptor ≠ semantic authority
Activity ≠ factual/evaluation authority
evaluator ≠ classification authority
```

#### Experimental design

Qué variable permanece constante y cuál cambia.

#### Implementation delta

Delta exacto y por qué es el mínimo.

#### Test matrix

Expected vs observed.

#### Evidence

Qué demuestra realmente la ejecución.

#### Unexpected findings

Incluye dependencias, consumers, authority laundering o incompatibilidades inesperadas.

#### Limitations

Qué NO se ha demostrado.

#### Architectural evaluation

Sin promoción automática.

#### Verdict

Uno de:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NO-GO
STOP
```

---

### 20. Claims que una ejecución positiva podría soportar

Incluso con todos los tests verdes, Session 13 podría como máximo aportar evidencia para claims del tipo:

```text
neutral Evidence can remain independent
from Experience-relative evaluation

same Evidence + same ExperienceContext
can legitimately yield different claim types
when authority/coverage changes

absence in incomplete knowledge
does not justify a negative determination

a scoped negative requires sufficient authority
to exclude the relation

missing or conflicting authority
can remain undetermined

the evaluator need not become classification authority

Activity can remain downstream
without influencing the evaluation
```

No conviertas automáticamente estos claims en arquitectura aceptada.

La promoción corresponde a una evaluación posterior.

---

### 21. Claims que Session 13 NO puede soportar

No puede demostrar:

* cuál debe ser la classification authority final;
* que Scenario sea classification authority;
* que un provider sea classification authority;
* que exista una universal taxonomy;
* que un catálogo de propiedad sea suficiente en todos los casos;
* precedence entre fuentes;
* schema definitivo de authority;
* enum definitivo de EvaluationOutcome;
* TES Event recognition;
* Pattern;
* Sequence;
* Progression;
* Result;
* Measurement;
* Learning;
* participation semantics;
* group semantics;
* Treasure Hunt;
* persistencia;
* event sourcing;
* provider architecture;
* API architecture;
* Activity UX final;
* semantic completeness de `ExperienceDefinition`;
* necesidad de modificar ADR-001.

---

### 22. Criterio de éxito epistemológico

El éxito de Session 13 NO es:

```text
all tests green
```

El éxito es obtener evidencia capaz de discriminar esta diferencia:

```text
we cannot establish X
≠
we have established NOT X
```

y demostrar que esa diferencia puede mantenerse a través del evaluator sin:

* autoridad inventada upstream;
* authority laundering en `ExperienceDefinition`;
* authority laundering downstream en Activity;
* taxonomía universal;
* Event recognition;
* rules engine.

El patrón crítico esperado es:

```text
same Evidence
+
same ExperienceContext
+
different available authority / coverage
        ↓
different legitimate evaluation claims
```

---

### 23. Condición de STOP por sobrearquitectura

Si para distinguir:

```text
positive
negative
undetermined
```

resulta necesario introducir una infraestructura sustancial de:

* taxonomy;
* providers;
* registries;
* precedence;
* persistence;
* workflow;
* rules;
* participation;

detente.

El resultado correcto será:

```text
INCONCLUSIVE
```

o:

```text
NO-GO
```

para la forma propuesta.

No construyas la infraestructura.

---

### 24. No promoción al terminar

Aunque H13 resulte SUPPORTED:

```text
Experiment
→ Evidence
→ Evaluation
→ Promotion
```

Por tanto, al terminar Session 13:

```text
NO ADR-005
NO Architecture v0.5
NO Treasure Hunt
```

La siguiente fase, si la evidencia lo justifica, será una sesión posterior de consolidación/evaluación arquitectónica.

---

### 25. Respuesta final esperada de Codex

Devuélveme exactamente una evaluación estructurada que incluya:

1. **Repository inspection**

   * topología encontrada;
   * evaluator actual;
   * consumers;
   * ExperienceDefinition variants;
   * Activity dependencies.

2. **Baseline compatibility**

   * contradicciones materiales, si existen;
   * diferencias no materiales.

3. **Experimental delta**

   * cambios realizados;
   * por qué constituyen el delta mínimo.

4. **Authority representation**

   * cómo representaste positive/exclusion/coverage/missing/conflict;
   * por qué NO debe interpretarse como arquitectura final.

5. **Evaluation outcome representation**

   * cómo evitaste colapsar negative y undetermined;
   * impacto sobre el booleano previo.

6. **ADR-001 guardrail**

   * confirmación de que `tesBaseline`, naming y bootstrap no se utilizaron como autoridad semántica.

7. **Activity Authority Frontier**

   * confirmación de que Activity sigue downstream;
   * cualquier riesgo detectado de strengthening/reinterpretation.

8. **Test matrix**

   * expected;
   * observed;
   * verdict por caso.

9. **Verification**

   * tests;
   * test files;
   * typecheck;
   * lint;
   * build.

10. **Files changed**

    * nuevos;
    * modificados;
    * eliminados.

11. **Authority laundering review**

    * upstream;
    * evaluator;
    * downstream.

12. **Claims supported by evidence**

13. **Claims NOT supported by evidence**

14. **Limitations**

15. **Session 13 verdict**

    * SUPPORTED;
    * SUPPORTED WITH QUALIFICATION;
    * INCONCLUSIVE;
    * NO-GO;
    * STOP.

16. **Recommended next step**

    * sin crear ADR-005;
    * sin publicar Architecture v0.5;
    * sin avanzar a Treasure Hunt.

Sé adversarial.

Si la hipótesis no sobrevive al experimento, dilo.

No cambies la arquitectura para protegerla.
<!-- FIN-TEXTO-ORIGINAL-S13 -->

---

<a id="sesion-14"></a>

## Capítulo 14 — Promoción limitada de ADR-005

**Estado:** instrucción principal íntegra recuperada del historial.

**Nota de numeración:** el mensaje de envío llamó a este adjunto «sesión 15», pero su título y contenido corresponden a la sesión 14. Se mantiene esa numeración y se incorpora también la corrección documental posterior, sin ejecutarla ahora.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-14-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1535; salida(s) de lectura en la(s) línea(s) 1543, 1549, 1553. Cotejado con el recuento histórico de 1406 saltos de línea. Cotejo adicional: lectura repetida completa. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 080208b4422e8d57a6b36fb3389db084e046e64760efb4dad1dd19e2564500d0.

<!-- INICIO-TEXTO-ORIGINAL-S14 -->
### Session 14 — Consolidation and Architectural Promotion Decision

Trabaja sobre el repositorio existente:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

No empieces desde cero.

No rediseñes la arquitectura.

No realices un nuevo experimento salvo que durante la evaluación descubras una contradicción material que haga imposible decidir con la evidencia existente. En ese caso, no improvises una implementación: devuelve **DEFER / INCONCLUSIVE** e identifica exactamente qué evidencia falta.

Session 11, Session 12 y Session 13 ya están completadas.

ADR-001, ADR-002, ADR-003 y ADR-004 permanecen aceptados.

Session 13 terminó:

```text
SUPPORTED WITH QUALIFICATION
```

y produjo evidencia ejecutable open-world.

Esta sesión corresponde a la fase:

```text
Experiment
→ Evidence
→ Evaluation
→ Promotion
```

Session 14 debe realizar:

```text
Evaluation
→ Promotion decision
```

No debe convertirse en:

```text
new experiment
→ new platform
→ new architecture
```

Treasure Hunt / Búsqueda del Tesoro sigue reservado.

---

### 1. Objetivo de Session 14

Evaluar adversarialmente la evidencia acumulada de Sessions 11–13 y decidir:

1. si existe base suficiente para aceptar un ADR-005;
2. cuál es el alcance máximo legítimo de esa decisión;
3. qué elementos deben permanecer explícitamente experimentales o unresolved;
4. si Architecture v0.4 debe permanecer vigente o existe base suficiente para publicar una Architecture v0.5 estrechamente acotada;
5. qué tensiones deben conservarse abiertas para experimentos posteriores.

La sesión NO debe asumir de antemano que:

```text
Session 13 green
=
ADR-005 accepted
```

ni:

```text
ADR-005 accepted
=
Architecture v0.5 required
```

Las dos promociones deben evaluarse separadamente.

---

### 2. Material que debes revisar antes de decidir

Inspecciona y utiliza como evidencia, como mínimo:

* ADR-001;
* ADR-002;
* ADR-003;
* ADR-004;
* Session 10 Product Experience Definition candidates relevantes;
* Session 11 — Contextual Evidence Relevance Experiment;
* Session 12 — Authority Frontiers and Open-World Evaluation Semantics;
* Session 13 — Authority-Bounded Open-World Evaluation Experiment;
* implementación actual de `evidence-relevance.ts`;
* tests actuales de `evidence-relevance.test.ts`;
* contratos actuales relacionados con:

  * Evidence;
  * ExperienceContext;
  * Scenario;
  * Activity;
  * AppSnapshot;
  * `domain/contracts.ts::ExperienceDefinition`;
  * `demo-factory/contracts.ts::ExperienceDefinition`.

No asumas que el informe de Session 13 es suficiente por sí solo.

Comprueba que sus afirmaciones corresponden al código y tests existentes.

No necesitas repetir toda la suite si no modificas código, pero sí debes verificar la evidencia documental y ejecutable que sustenta cualquier decisión de promoción.

Si encuentras divergencia material entre documentación y repositorio:

```text
STOP / DEFER
```

y documenta la divergencia.

---

### 3. Baseline metodológico

Aplica estrictamente:

```text
hypothesis
→ falsification
→ experiment
→ evidence
→ evaluation
→ promotion
```

La promoción debe recaer sobre el **invariant demostrado**, no automáticamente sobre:

* nombres de tipos;
* fixtures;
* unions TypeScript;
* reason codes;
* nombres de interfaces;
* representation shapes;
* scopes particulares del experimento.

Distingue siempre:

```text
demonstrated invariant
≠
experimental mechanism used to demonstrate it
```

Y:

```text
architectural decision
≠
current implementation shape
```

---

### 4. Evidencia acumulada que debes someter a revisión adversarial

#### Session 11

Session 11 respaldó, con cualificación:

```text
neutral factual evidence
        ≠
Experience-relative evaluation
        ≠
Activity projection
```

También respaldó que la evaluación contextual podía producirse sin branches por Experience ID.

Pero utilizó semántica binaria:

```text
relevant / not_relevant
```

bajo una asunción closed-world experimental.

No promociones esa semántica binaria.

---

#### Session 12

Session 12 consolidó conceptualmente:

```text
Authority Frontier
```

como término analítico para identificar:

* qué claims puede emitir un artefacto;
* dentro de qué scope;
* con qué provenance;
* qué no puede afirmar;
* cuándo hace falta nueva autoridad.

También identificó:

```text
absence of knowledge
≠
negative claim
```

y dejó ADR-005 conceptualmente maduro pero experimentalmente infraevidenciado.

Session 12 NO aceptó ADR-005.

---

#### Session 13

Session 13 produjo evidencia ejecutable de:

```text
same Evidence
+
same ExperienceContext
+
different classification authority / coverage
        ↓
different legitimate claim type
```

Respaldó:

```text
explicit membership
→ positive

explicit exclusion
→ negative

absence + incomplete knowledge
→ undetermined

absence + sufficiently exhaustive scoped knowledge
→ negative

missing authority
→ undetermined

out-of-scope authority
→ undetermined

conflicting authority without precedence
→ undetermined/conflicting
```

También mostró que el evaluator:

* no necesita branches por Experience ID;
* no necesita Activity;
* no necesita TES Event recognition;
* no necesita taxonomy engine;
* no necesita registry;
* no necesita precedence engine;
* no necesita provider architecture.

Session 13 terminó:

```text
SUPPORTED WITH QUALIFICATION
```

No olvides las cualificaciones.

---

### 5. Cualificación central que Session 14 debe incorporar

Session 13 manipuló experimentalmente **classification authority**.

Esto NO demuestra que classification authority sea la única Authority Frontier del EvaluationOutcome.

Un claim contextual depende de varias premisas potencialmente autoritativas:

```text
factual Evidence
+
Experience interpretation
+
Scenario / situated context
+
classification claims
+
evaluation transformation
```

Por tanto, evita convertir:

```text
AvailableAuthority
```

en una caja arquitectónica única o un tercer DTO soberano.

La formulación a evaluar es más general:

> Todo claim derivado está limitado por la autoridad, alcance y madurez de las premisas utilizadas para derivarlo.

Session 13 aporta evidencia directa principalmente sobre una dimensión:

```text
classification authority / coverage
```

No aporta evidencia ejecutable equivalente sobre todas las demás.

---

### 6. Product Experience Definition authority — cualificación obligatoria

Las Product Experience Definitions utilizadas siguen siendo candidatas:

```text
READY WITH EXPLICIT GAPS
non-executable
interpreted against TES
```

No son:

```text
TES-validated Product Experience Definitions
```

Por tanto, si un criterio experimental dice:

```text
Active Challenge accepts sport-wellness
```

la autoridad del claim resultante no puede exceder la madurez de esa interpretación de Experience.

Incluso si la clasificación factual fuese perfecta:

```text
Cooking Class → sport-wellness
```

no debes inferir automáticamente:

```text
fully TES-validated relevance claim
```

La relación correcta permanece acotada por las premisas.

Evalúa expresamente esta desigualdad:

```text
classification certainty
≠
semantic validation of Experience
```

Y:

```text
strong authority on one premise
cannot repair weak authority on another premise
```

No utilices esta observación para reabrir ADR-001 salvo contradicción genuina.

---

### 7. Tensión ADR-001 — decisión esperada

ADR-001 permanece aceptado salvo evidencia contradictoria.

La tensión existente es:

```text
ExperienceDefinition
+
tesBaseline
```

puede parecer más autoritativa de lo que realmente es.

Distingue conceptualmente:

```text
Candidate Product Experience Definition
→ interpreted against TES

Validated Product Experience Definition
→ validated against TES

Runtime Experience Descriptor / Reference
→ runtime identity/binding
```

No renombres los tipos durante Session 14 salvo que exista una razón documental absolutamente necesaria.

No conviertas la consolidación en una migración.

Session 14 debe decidir únicamente si esta tensión:

```text
A. contradice ADR-001
B. requiere amendment inmediato
C. requiere aclaración futura
D. permanece correctamente como open issue
```

La hipótesis de partida es:

```text
clarification/open issue
```

pero debes evaluarla adversarialmente.

---

### 8. Activity Authority Frontier — evaluación esperada

ADR-002 ya establece:

```text
Activity = read model / projection
```

y nunca:

```text
factual authority
evidence ledger
TES Event ledger
```

Session 13 comprobó que Activity no participa en el evaluator.

Pero no existe todavía una integración real:

```text
EvaluationOutcome
→ production projector
→ Activity
```

Por tanto, distingue:

##### Evidencia respaldada

```text
Activity need not participate in evaluation
```

y:

```text
Activity can remain downstream
```

##### Evidencia NO respaldada plenamente

```text
all future Activity projections
will preserve epistemic qualifiers correctly
```

Si ADR-005 incluye Activity, su decisión debe ser mínima:

> Activity/read models cannot originate or strengthen the authority of an evaluation claim.

No decidas todavía:

* wording UI;
* icons;
* labels;
* conflict presentation;
* confidence visualization;
* `unknown` copy;
* UX definitiva de undetermined.

---

### 9. Taxonomy alignment — open issue obligatorio

Session 13 funcionó porque Experience criteria y classification authority utilizaban el mismo vocabulario experimental:

```text
shared-hotel-activity
sport-wellness
```

No se probó:

```text
taxonomy A
→ mapping
→ taxonomy B
```

Ejemplo futuro posible:

```text
provider:
culinary_experience

property catalogue:
recreation

Product Experience Definition:
shared-hotel-activity
```

El mapping:

```text
culinary_experience
→ shared-hotel-activity
```

constituiría otra Authority Frontier.

Session 14 debe registrar explícitamente:

```text
taxonomy alignment / semantic mapping authority
→ UNRESOLVED
```

No construyas shared taxonomy.

No diseñes mappings.

No resuelvas authority de mappings.

---

### 10. Exhaustiveness — no promover el mecanismo experimental

Session 13 utilizó:

```text
coverage = incomplete | exhaustive
```

como mecanismo de falsificación.

No promociones este shape.

Lo respaldado por evidencia es:

> Una ausencia solo puede contribuir a un claim negativo cuando existe autoridad suficiente para excluir la relación dentro del scope evaluado.

NO:

```text
coverage: exhaustive
→ architecture rule
```

No se ha demostrado:

* cómo se acredita exhaustividad;
* quién la declara;
* cómo cambia en el tiempo;
* si es binaria;
* si puede ser parcial;
* si varía por dimensión;
* si depende del provider.

En cualquier ADR, utiliza lenguaje de:

```text
sufficient authority to exclude
within declared scope
```

no una propiedad TypeScript concreta.

---

### 11. EvaluationOutcome — no promover el vocabulario experimental

Session 13 utilizó:

```text
positive
negative
undetermined
```

y reason codes como:

```text
authoritative-membership
explicit-exclusion
scoped-exhaustive-absence
incomplete-classification-knowledge
missing-classification-authority
conflicting-classification-authority
```

La evidencia respalda la **distinción epistemológica**, no este vocabulario exacto.

Por tanto:

```text
positive / negative / undetermined
→ experimental representation
```

El ADR puede exigir que:

```text
negative determination
```

se distinga de:

```text
insufficient / unresolved determination
```

pero NO debe congelar el enum.

---

### 12. SignificantEvent — mantener frontera sin resolver

No promociones:

```text
RelevantEvidence
=
SignificantEvent
```

ni:

```text
positive contextual evaluation
=
TES Event recognition
```

La posición sigue siendo:

```text
EvidenceInput
        ↓
Contextual evaluation
        ↓
[future recognition boundary unresolved]
        ↓
SignificantEvent
```

Esta representación sigue siendo provisional.

Session 14 puede registrar que existe una futura recognition boundary, pero no debe:

* definirla;
* implementarla;
* nombrar su authority final;
* migrar `SignificantEvent`;
* diseñar Event recognition.

---

### 13. Candidate ADR-005 — pregunta de decisión

Evalúa si la evidencia ya soporta aceptar una decisión del tipo:

#### Candidate title

**ADR-005 — Neutral Evidence and Authority-Bounded Contextual Evaluation**

Título sujeto a evaluación; no lo aceptes solo porque fue propuesto anteriormente.

#### Candidate invariant

Evalúa críticamente una formulación como:

> La evidencia factual permanece separada de la evaluación relativa a Experience. Todo claim contextual derivado queda limitado por la autoridad, alcance y madurez de las premisas utilizadas para derivarlo. La ausencia de información, clasificación, contexto o autoridad suficientes no se convierte silenciosamente en un claim negativo. Un claim negativo requiere base suficiente para excluir la relación dentro del scope evaluado. La relevancia contextual no reconoce por sí misma un TES Event y no pertenece a Activity.

No copies necesariamente esta redacción.

Debes:

1. comprobar cada cláusula contra evidencia;
2. separar evidencia directa de inferencia razonable;
3. eliminar cualquier cláusula que exceda lo demostrado;
4. cualificar cualquier parte que todavía dependa de candidatos no validados.

---

### 14. ADR-005 — decisiones que PODRÍA legítimamente contener

Evalúa como máximo decisiones de este orden:

##### Neutral Evidence

```text
factual evidence
≠
Experience-relative evaluation
```

##### Open-world evaluation

```text
insufficient knowledge
≠
negative determination
```

##### Authority-bounded negative claims

```text
negative claim
requires sufficient authority
to exclude within scope
```

##### Derived-claim authority

```text
derived claim
cannot exceed the authority/maturity
of its premises
```

Esta última cláusula debe evaluarse con especial cuidado porque Session 13 solo falsificó directamente una parte de ella.

Puede aceptarse como principio arquitectónico si la combinación de Sessions 11–13 y ADR-001–004 la sustenta suficientemente; si no, mantenerla como implication/candidate principle y no invariant.

##### TES Event separation

```text
contextual relevance
≠
TES Event recognition
```

##### Activity separation

```text
Activity/read model
does not originate or strengthen evaluation authority
```

---

### 15. ADR-005 — decisiones que NO debe contener

Aunque ADR-005 sea aceptado, NO debe decidir:

* enum definitivo de evaluation outcomes;
* reason codes;
* `ActivityClassificationAuthority`;
* `authorityRef`;
* `coverage`;
* `scope` schema;
* property/catalogue version shape;
* classification taxonomy;
* shared taxonomy;
* taxonomy mappings;
* mapping authority;
* provider topology;
* provider interfaces;
* registries;
* trust framework;
* authority accreditation;
* signatures;
* reliability model;
* confidence model;
* precedence;
* conflict resolution policy;
* persistence;
* audit log;
* event sourcing;
* recognition boundary;
* `SignificantEvent` migration;
* `ExperienceDefinition` rename;
* runtime composition of authorities;
* bootstrap resolution of authorities;
* Activity UI representation.

Si alguno aparece como decisión normativa, el ADR está sobrearquitecturado.

---

### 16. Resultado permitido para ADR-005

Session 14 debe terminar con exactamente una de estas decisiones:

```text
ADR-005 → ACCEPT
```

si el invariant mínimo está suficientemente respaldado;

o:

```text
ADR-005 → DEFER
```

si todavía existe una laguna experimental material;

o:

```text
ADR-005 → REJECT
```

si la evidencia contradice el invariant o demuestra que el framing es incorrecto.

No uses:

```text
READY TO PROPOSE LATER
```

como salida evasiva si la evidencia actual permite decidir.

Esta sesión es precisamente la promoción decision.

---

### 17. Si ADR-005 es ACCEPT

Si concluyes:

```text
ADR-005 → ACCEPT
```

crea el ADR real siguiendo el formato de ADR-001–004.

Debe incluir al menos:

* Estado;
* Contexto;
* Decisión;
* Alcance de autoridad;
* consecuencias positivas;
* costes y obligaciones;
* interpretaciones prohibidas;
* evidencia de aceptación;
* implicaciones de versionado si aplican;
* condiciones de reconsideración;
* revisión de aceptación.

Debe declarar explícitamente que:

```text
Authority Frontier
```

es un concepto analítico de producto/arquitectura, no TES.

El ADR no debe reclamar que TES prescribe la evaluación open-world técnica.

La decisión debe permanecer subordinada a ADR-001.

---

### 18. Si ADR-005 es DEFER o REJECT

No crees un ADR aceptado.

Crea únicamente el documento de Session 14 y explica:

```text
exact missing evidence
```

o:

```text
exact contradiction
```

No propongas un gran experimento genérico.

Si hace falta nueva evidencia, formula únicamente la siguiente hipótesis mínima falsable.

---

### 19. Architecture v0.5 — decisión separada

Solo después de decidir ADR-005, evalúa Architecture v0.5.

No asumas:

```text
ADR-005 accepted
→ Architecture v0.5
```

Architecture v0.5 tiene un riesgo adicional:

```text
diagram
→ reification
```

Un diagrama puede hacer parecer arquitectónicamente reales conceptos todavía experimentales.

En particular, evita introducir una caja normativa llamada:

```text
Classification Authority Layer
```

o:

```text
AvailableAuthority Service
```

o equivalente.

No existe evidencia para una topología de ese tipo.

---

### 20. Arquitectura v0.5 — criterio de aceptación

Una Architecture v0.5 solo puede publicarse si puede expresar la nueva frontera sin convertir mecanismos experimentales en componentes.

Una representación candidata podría ser de este orden:

```text
TES semantic authority
        ↓
Product interpretations / definitions
        ↓
Scenario / situated context
        ↓
Neutral factual evidence
        +
authoritative premises within declared scope
        ↓
Contextual evaluation boundary
        ↓
Derived evaluation claim
        ↓
[future TES Event recognition boundary — unresolved]
        ↓
Runtime / Read Models / UI
```

Pero NO uses este diagrama como especificación.

Evalúa si encaja realmente con ADR-003 y ADR-004, porque Evidence no debe forzarse artificialmente dentro de la cadena lineal de composición:

```text
Experience Definition
→ Scenario
→ Manifest
→ Bootstrap
→ Runtime
```

Es posible que la nueva realidad sea mejor representada mediante **dos flujos que convergen**:

```text
Product semantic/contextual inputs
                ↘
                 contextual evaluation
                ↗
Factual evidence inputs
```

Si v0.5 no puede representarse sin distorsionar esa distinción, NO la publiques.

---

### 21. Resultados permitidos para Architecture v0.5

Después de la decisión de ADR-005, devuelve exactamente uno:

```text
Architecture v0.5 → PUBLISH
```

o:

```text
Architecture v0.5 → DEFER
```

No hay obligación de publicar.

Es perfectamente válido:

```text
ADR-005 → ACCEPT
Architecture v0.5 → DEFER
```

si el invariant es estable pero su representación topológica todavía podría cosificar elementos experimentales.

---

### 22. Si Architecture v0.5 se publica

Debe distinguir con claridad:

##### ACCEPTED

Fronteras ya promovidas por ADR-001–005.

##### PROVISIONAL

Elementos respaldados parcialmente pero sin topología final.

##### UNRESOLVED

Como mínimo:

```text
classification authority topology
taxonomy
taxonomy mapping authority
authority accreditation
source precedence
Event recognition
ExperienceDefinition naming/maturity representation
Activity UX for unresolved evaluations
```

No mezcles esos estados visualmente.

No hagas parecer `PROVISIONAL` o `UNRESOLVED` como componentes productivos.

---

### 23. Treasure Hunt

Treasure Hunt permanece reservado.

Session 14 debe decidir si, después de la consolidación:

```text
Treasure Hunt
```

es ya el siguiente experimento adecuado o si antes existe otra frontera mínima que requiera falsificación.

No diseñes Treasure Hunt.

No crees schemas de:

* participant groups;
* clues;
* group evidence;
* aggregation;
* sufficiency;
* partial resolution.

Solo evalúa readiness.

---

### 24. Criterios adversariales para aceptar ADR-005

Antes de ACCEPT, responde explícitamente:

1. ¿Existe evidencia ejecutable de separación Evidence/evaluation?
2. ¿Existe evidencia ejecutable de unknown ≠ negative?
3. ¿Existe evidencia ejecutable de que un negativo por ausencia requiere authority/coverage suficiente?
4. ¿La decisión puede formularse sin fijar `coverage = exhaustive`?
5. ¿Puede formularse sin congelar `positive/negative/undetermined`?
6. ¿Puede formularse sin inventar classification authority final?
7. ¿Puede formularse sin asumir Scenario como taxonomy authority?
8. ¿Puede formularse sin elevar Product Experience Definition candidata a TES-validada?
9. ¿Puede formularse sin introducir Event recognition?
10. ¿Puede formularse sin convertir Activity en evaluator?
11. ¿Es compatible con ADR-001?
12. ¿Es compatible con ADR-002?
13. ¿Es compatible con ADR-003?
14. ¿Es compatible con ADR-004?
15. ¿Puede ser reconsiderado cuando exista una API real?
16. ¿Distingue invariant de implementation mechanism?

Si alguna respuesta crítica es NO, evalúa DEFER.

---

### 25. Criterios adversariales para publicar Architecture v0.5

Antes de PUBLISH, responde:

1. ¿El diagrama expresa autoridad sin inventar un Authority Service?
2. ¿Distingue Evidence flow de composition flow?
3. ¿Preserva Experience → Scenario → Demo Script?
4. ¿Preserva Desired ≠ Effective Composition?
5. ¿Preserva Activity downstream?
6. ¿Deja Event recognition unresolved?
7. ¿No presenta taxonomy como decidida?
8. ¿No presenta `AvailableAuthority` como nuevo aggregate?
9. ¿Distingue accepted/provisional/unresolved?
10. ¿Añade comprensión arquitectónica real frente a v0.4?

Si el décimo punto es débil o cualquiera de los anteriores falla:

```text
Architecture v0.5 → DEFER
```

No publiques una versión nueva solo porque el número siguiente esté disponible.

---

### 26. No implementar durante Session 14

No modifiques runtime/product code salvo que descubras una contradicción documental menor cuya corrección sea imprescindible para consistencia y no cambie comportamiento.

Preferencia:

```text
documentation-only consolidation
```

No implementes:

* new evaluator behavior;
* authority services;
* taxonomy;
* provider;
* mappings;
* Activity integration;
* UI;
* Event recognition;
* Treasure Hunt.

Si para aceptar ADR-005 necesitas código nuevo:

```text
ADR-005 → DEFER
```

y explica qué hipótesis falta probar.

---

### 27. Documento de Session 14

Crea:

```text
Session 14 — Consolidation and Architectural Promotion Decision
```

siguiendo el estilo documental existente.

Debe incluir:

#### 1. Executive conclusion

* ADR-005 verdict;
* Architecture v0.5 verdict;
* Treasure Hunt readiness.

#### 2. Evidence chain

```text
Session 11
→ Session 12
→ Session 13
→ Session 14 evaluation
```

#### 3. Claims promoted

Solo invariants realmente promovidos.

#### 4. Experimental mechanisms NOT promoted

Incluye como mínimo:

```text
positive/negative/undetermined literals
reason codes
ActivityClassificationAuthority
coverage enum
scope shape
authorityRef
fixture taxonomy
```

#### 5. Authority Frontier consolidation

Distingue:

* factual authority;
* Experience interpretation authority;
* situated context authority;
* classification/mapping authority;
* evaluation transformation;
* runtime;
* projection.

No es necesario inventar un artefacto para cada una.

#### 6. ADR-001 tension

Estado después de Session 14.

#### 7. Activity frontier

Estado después de Session 14.

#### 8. Classification authority

Qué se ha demostrado y qué sigue abierto.

#### 9. Taxonomy alignment

Explícitamente unresolved.

#### 10. Event recognition boundary

Explícitamente unresolved.

#### 11. ADR-005 decision

Razonamiento adversarial.

#### 12. Architecture v0.5 decision

Razonamiento separado.

#### 13. Remaining risks

#### 14. Treasure Hunt readiness

Sin diseñarlo.

#### 15. Final project state

Tabla accepted / supported / provisional / unresolved.

---

### 28. Si se acepta ADR-005

Además del informe de Session 14:

crea el ADR real:

```text
ADR-005 — Neutral Evidence and Authority-Bounded Contextual Evaluation
```

o un título mejor si el análisis demuestra que existe una formulación más precisa.

No uses el título para ampliar el scope.

El contenido manda sobre el nombre.

---

### 29. Si se publica Architecture v0.5

Actualiza únicamente el artefacto arquitectónico correspondiente.

No reescribas ADR-001–004.

No conviertas Session documents en arquitectura normativa.

Deja trazabilidad explícita:

```text
Architecture v0.5
derived from
ADR-001–005
+
evidence Sessions 5/7/11/13 as applicable
```

No mezcles Evidence con norma.

---

### 30. Estado epistemológico esperado

Distingue en la conclusión:

##### ACCEPTED

Decisiones arquitectónicas aprobadas.

##### SUPPORTED

Claims experimentales respaldados pero que no necesitan ser arquitectura independiente.

##### PROVISIONAL

Representaciones o conceptos útiles aún no consolidados.

##### UNRESOLVED

Preguntas cuya autoridad o implementación todavía no está demostrada.

##### REJECTED / NOT PROMOTED

Artefactos o interpretaciones explícitamente descartados.

No utilices únicamente:

```text
done / pending
```

porque pierde la naturaleza epistemológica del proyecto.

---

### 31. Resultado final esperado de Codex

Devuelve una respuesta estructurada con:

1. **Repository/document inspection**
2. **Evidence chain validation**
3. **Session 11–13 compatibility**
4. **Authority-frontier synthesis**
5. **Product Experience Definition authority qualification**
6. **ADR-001 tension assessment**
7. **Activity frontier assessment**
8. **Classification authority assessment**
9. **Taxonomy alignment assessment**
10. **EvaluationOutcome mechanism vs invariant**
11. **ADR-005 candidate clause-by-clause evaluation**
12. **ADR-005 verdict: ACCEPT / DEFER / REJECT**
13. **ADR-005 file created or not**
14. **Architecture v0.5 independent evaluation**
15. **Architecture v0.5 verdict: PUBLISH / DEFER**
16. **Architecture files changed, if any**
17. **Claims promoted**
18. **Mechanisms explicitly NOT promoted**
19. **Remaining unresolved frontiers**
20. **Treasure Hunt readiness**
21. **Files created/modified/deleted**
22. **Final project epistemic state**
23. **Recommended next session**

---

### 32. Final adversarial check

Antes de terminar, responde internamente y documenta:

```text
Did we promote an invariant
or merely our latest implementation?
```

```text
Did classification authority become
a hidden new sovereign layer?
```

```text
Did strong classification evidence
silently upgrade a candidate Experience Definition?
```

```text
Did an experimental enum
become domain ontology by convenience?
```

```text
Did Activity gain authority
because it is downstream and visible?
```

```text
Did Architecture v0.5 add explanatory power
or only additional boxes?
```

```text
Would the decision still make sense
if a real Convercus API exposes
different shapes and taxonomies?
```

Si la respuesta a cualquiera revela sobrepromoción, reduce el alcance antes de aceptar.

El objetivo de Session 14 no es ampliar la arquitectura.

Es decidir exactamente **qué mínima frontera ha sobrevivido a la falsificación suficiente para merecer autoridad arquitectónica**.
<!-- FIN-TEXTO-ORIGINAL-S14 -->

**Corrección documental posterior a la sesión 14:**

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-14-correccion-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1656; salida(s) de lectura en la(s) línea(s) 1664, 1670. Cotejado con el recuento histórico de 925 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 633083d2c63c7856eb09a04a03a4cdce4c7a04396fe3407e3b998334a6ebfb4c.

<!-- INICIO-TEXTO-ORIGINAL-S14-CORRECCION -->
### Post-Session 14 — Documentation Consistency Patch

Trabaja sobre el repositorio existente:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

Esta tarea NO es una nueva sesión experimental.

No la numeres como Session 15.

No diseñes Treasure Hunt.

No ejecutes un nuevo experimento.

No reabras las decisiones de Session 14.

El objetivo es realizar una **corrección documental estrictamente acotada** después de la revisión de los artefactos producidos en Session 14.

Las decisiones ya alcanzadas permanecen:

```text
Session 13
→ SUPPORTED WITH QUALIFICATION

Session 14
→ consolidation completed

ADR-005
→ ACCEPT

Architecture v0.5
→ PUBLISH

Treasure Hunt
→ READY FOR A BOUNDED NEXT EXPERIMENT
```

No reconsideres esas decisiones salvo que al editar encuentres una contradicción genuina que haga imposible mantenerlas. Si eso ocurre, STOP y documenta exactamente la contradicción en vez de modificar arquitectura silenciosamente.

---

### 1. Archivos objeto de revisión

Revisa y corrige únicamente cuando sea necesario:

```text
00-governance/decisions/
ADR-005-neutral-evidence-authority-bounded-contextual-evaluation.md

00-governance/
program-architecture.md

products/convercus-app/docs/
session-14-consolidation-architectural-promotion-decision.md
```

Puedes consultar ADR-001–004, Sessions 10–13 y demás documentación para verificar consistencia, pero no los modifiques.

No modifiques código productivo.

No modifiques tests.

No modifiques fixtures.

No modifiques contracts TypeScript.

---

### 2. Naturaleza de la tarea

Esta tarea corrige una forma de riesgo documental detectada después de Session 14:

```text
historical / prospective product vision
        ↓
included inside an active governing architecture document
        ↓
may appear as accepted architecture
```

El objetivo es impedir:

```text
document status
→ authority laundering
```

No todo contenido históricamente presente en `program-architecture.md` posee el mismo grado de validación.

Architecture v0.5 debe distinguir claramente:

```text
ACCEPTED
SUPPORTED
PROVISIONAL
UNRESOLVED
NON-NORMATIVE / FUTURE DIRECTION
```

cuando corresponda.

La regla rectora es:

> El hecho de que una idea aparezca dentro de un documento arquitectónico activo no debe otorgarle una autoridad mayor que la evidencia que la sostiene.

---

### 3. Corrección 1 — Session 14 identification note

En:

```text
session-14-consolidation-architectural-promotion-decision.md
```

elimina la nota inicial que indica que la petición acompañante denominaba la sesión como “Session 15”.

La referencia a Session 15 se debió a un error humano al trasladar la instrucción y no necesita conservarse en el documento consolidado.

No la sustituyas por una explicación adicional.

El documento debe comenzar directamente como:

```text
Session 14 — Consolidation and Architectural Promotion Decision
```

seguido de su contenido normal.

No cambies el resto del verdict por este motivo.

---

### 4. Corrección 2 — Event recognition NO debe aparecer como gate serial obligatorio

Revisa el bloque:

```text
FLUJO DE EVALUACIÓN CONTEXTUAL — ACCEPTED BOUNDARY
```

de:

```text
program-architecture.md
```

La representación actual puede interpretarse como:

```text
Derived evaluation claim
        ↓
TES Event recognition
        ↓
Runtime/read-model use
```

Esto es demasiado fuerte.

La evidencia aceptada establece:

```text
contextual relevance
≠
TES Event recognition
```

y NO ha demostrado que todo EvaluationOutcome que llegue a runtime, AppSnapshot, Activity o UI deba atravesar antes una frontera de reconocimiento de Evento TES.

Por tanto, modifica el diagrama para que:

```text
Derived evaluation claim
```

pueda alimentar:

```text
Runtime / read-model use when applicable
```

sin pasar necesariamente por Event recognition.

La futura relación con Event recognition debe quedar como relación lateral, opcional, hipotética o explícitamente unresolved.

Una forma conceptual aceptable sería:

```text
Product semantic premises + situated context
                         ↘
                          Contextual evaluation
                         ↗
Neutral factual evidence + authoritative premises in scope
                                      ↓
                         Derived evaluation claim
                                      ↓
                   Runtime / read-model use
                        when applicable


Possible future relation:

Derived evaluation claim
        - - ? - ->
[TES Event recognition boundary — UNRESOLVED]
```

No copies necesariamente este diagrama si una representación más limpia encaja mejor con el documento.

Pero debe quedar inequívoco:

```text
Evaluation
≠
Event recognition
```

y:

```text
Runtime/read-model use
does not require TES Event recognition by default
```

No definas ahora qué inputs necesitará una futura recognition boundary.

No afirmes tampoco que `Derived evaluation claim` será necesariamente su input único.

---

### 5. Corrección 3 — Shared contracts prospectivos no pueden aparecer como arquitectura aceptada

Revisa la sección de `program-architecture.md` que actualmente propone contratos compartidos como:

```text
ExperienceDefinition
ExperienceParticipation
SignificantEvent
PatternHypothesis
Sequence
ProgressionState
Intervention
Incentive
Reward
ObservedOutcome
Measurement
ReusableLearning
WorkflowReference
```

Esta lista procede de una visión anterior del programa y no debe adquirir estatuto normativo por encontrarse ahora dentro de Architecture v0.5.

La evidencia actual NO demuestra todavía como contratos arquitectónicos compartidos:

```text
ExperienceParticipation
SignificantEvent
PatternHypothesis
ProgressionState
ObservedOutcome
ReusableLearning
```

ni demuestra que los conceptos TES:

```text
Sequence
Progression
Result
Measurement
Learning
```

deban materializarse como interfaces, DTOs, stores o contratos software separados.

`SignificantEvent` sigue además situado detrás de una future recognition boundary unresolved.

Por tanto, aplica una de estas soluciones, prefiriendo la más pequeña y clara:

##### Opción preferida

Retira la lista concreta de contratos prospectivos del documento rector.

Sustitúyela por una formulación como:

> Los contratos compartidos solo se incorporarán cuando una responsabilidad reutilizable entre App y Builder haya sido demostrada. La existencia de un concepto TES no implica por sí misma que deba materializarse como contrato técnico independiente.

Puedes añadir:

```text
Current shared contracts
→ only those actually demonstrated and present

Future shared contracts
→ evidence-driven
```

##### Opción alternativa

Si existe una razón documental fuerte para conservar la lista histórica, clasifícala explícitamente como:

```text
NON-NORMATIVE HISTORICAL / PROSPECTIVE DIRECTION
```

y deja claro que ninguno de esos nombres constituye arquitectura aceptada por aparecer allí.

No crees nuevas interfaces.

No reorganices carpetas para materializar la lista.

---

### 6. Corrección 4 — eliminar la implicación de un generic Experience simulation engine

En `program-architecture.md`, revisa el roadmap App donde aparece una formulación equivalente a:

```text
A3. Incorporar motor de simulación de Experiences/Workflows.
```

Esta frase puede interpretarse como promoción de:

```text
Experience engine
generic simulation engine
generic workflow rules engine
```

y entra en tensión con las restricciones metodológicas ya consolidadas.

Sustitúyela por una formulación que preserve la intención de simulación, pero mantenga el enfoque evidence-driven.

Por ejemplo:

> A3. Incorporar comportamientos de simulación acotados a escenarios demostrados, mediante runtime boundaries reversibles y sin asumir un Experience engine o rules engine general.

La idea debe ser:

```text
scenario-specific demonstrated simulation
→ allowed

generic Experience engine
→ NOT promoted
```

No cambies el roadmap más allá de lo necesario.

---

### 7. Corrección 5 — preservar el estatuto semántico de los escenarios/conceptos comerciales

Revisa cualquier sección de `program-architecture.md` que agrupe como equivalentes:

```text
Aventura Familiar
Desafío Activo
Maratón de Temporada
Circuito de decisión
```

No todos poseen el mismo estatuto semántico.

El baseline consolidado establece al menos:

```text
Aventura Familiar
→ Product Experience Definition candidate
→ READY WITH EXPLICIT GAPS
→ non-executable
→ interpreted against TES

Desafío Activo
→ Product Experience Definition candidate
→ READY WITH EXPLICIT GAPS
→ non-executable
→ interpreted against TES

Maratón de Temporada
→ commercial / campaign / loyalty mechanic concept
→ NOT a validated Product Experience Definition
```

No transformes Maratón de Temporada en Experience por aparecer dentro de una demo.

La inclusión de un concepto en:

```text
demo
scenario
commercial story
```

no modifica su autoridad semántica.

Reformula la sección para que pueda, por ejemplo, hablar de:

```text
Potential demo scenarios / commercial concepts
```

y anotar explícitamente su estatuto.

Una formulación aceptable:

```text
Aventura Familiar
→ Product Experience Definition candidate

Desafío Activo
→ Product Experience Definition candidate

Maratón de Temporada
→ commercial/campaign concept; do not assume Experience

Circuito de decisión
→ preserve its currently documented semantic classification
```

No inventes una clasificación nueva de Circuito de decisión si la documentación disponible no la establece de forma suficiente.

Añade, si encaja naturalmente:

> La inclusión en una demo no modifica el estatuto semántico del artefacto.

---

### 8. Corrección 6 — usar la cadena TES de referencia sin introducir variantes como equivalentes normativos

Revisa `program-architecture.md` para detectar cadenas como:

```text
evento significativo
→ patrón
→ secuencia
→ progresión
→ resultado observado
→ medición
→ aprendizaje reutilizable
```

La cadena TES de referencia vigente es:

```text
Event
→ Pattern
→ Sequence
→ Progression
→ Result
→ Measurement
→ Learning
```

No utilices:

```text
Significant Event
Observed Result
Reusable Learning
```

como si fueran términos TES equivalentes salvo que el corpus TES los defina expresamente así.

En particular:

```text
SignificantEvent
```

continúa provisional y situado detrás de una recognition boundary unresolved.

Sustituye las variantes por la cadena TES exacta:

```text
Event
→ Pattern
→ Sequence
→ Progression
→ Result
→ Measurement
→ Learning
```

o por la traducción oficial que ya exista en el corpus TES si el repositorio la utiliza normativamente.

No inventes traducciones nuevas.

No conviertas la cadena TES en una lista de contratos técnicos.

---

### 9. Corrección 7 — precisión de ADR-005 respecto a mapping authority

En:

```text
ADR-005-neutral-evidence-authority-bounded-contextual-evaluation.md
```

revisa la fila de `Alcance de autoridad` que agrupa actualmente:

```text
Clasificación o mapping
```

Session 13 probó directamente una frontera de clasificación.

Session 14 dejó:

```text
taxonomy alignment / semantic mapping authority
→ UNRESOLVED
```

Para evitar que `mapping` parezca promovido al mismo nivel, ajusta la formulación.

Preferencia:

```text
Clasificación
```

y en el límite o explicación:

> Los mappings entre vocabularios permanecen unresolved y requerirían una Authority Frontier propia.

También puedes utilizar una formulación equivalente si encaja mejor.

No cambies el verdict:

```text
ADR-005 → ACCEPTED
```

No reescribas el ADR más allá de esta precisión salvo que detectes una inconsistencia directa.

---

### 10. Corrección 8 — evitar recombinar Product Interpretation y Experience Definition

Revisa en Architecture v0.5 expresiones como:

```text
Product interpretation / Experience Definition
```

La barra `/` puede recombinar responsabilidades cuya diferencia hemos protegido expresamente.

Actualmente debemos mantener conceptualmente diferenciados:

```text
Candidate Product Experience Definition
→ interpreted against TES

Validated Product Experience Definition
→ validated against TES

Runtime Experience Descriptor / Reference
→ technical/runtime identity or binding
```

No es necesario resolver ahora la nomenclatura final.

Pero el diagrama tampoco debe sugerir que:

```text
Product Interpretation
=
Experience Definition
```

Usa una formulación neutral que preserve la tensión abierta.

Por ejemplo:

```text
Product interpretations / governed Experience references
```

o una redacción equivalente, siempre acompañada si es necesario por la cualificación:

```text
maturity may differ
```

No introduzcas una nueva clase arquitectónica solo para resolver el wording.

No renombres interfaces TypeScript.

---

### 11. Discipline of architectural status

Revisa `program-architecture.md` completo y detecta cualquier otro lugar donde una frase prospectiva utilice lenguaje excesivamente normativo como:

```text
must
will
should contain
must implement
will provide
```

cuando realmente representa:

```text
future direction
roadmap
product hypothesis
possible structure
```

No hagas una reescritura global del documento.

Corrige únicamente los casos donde el wording pueda convertir una hipótesis prospectiva en arquitectura aceptada.

Usa explícitamente, cuando sea necesario:

```text
ACCEPTED
SUPPORTED
PROVISIONAL
UNRESOLVED
NON-NORMATIVE PRODUCT DIRECTION
```

El objetivo no es burocratizar el documento.

El objetivo es preservar epistemic status.

---

### 12. Qué NO debes cambiar

NO cambies:

```text
ADR-005 → ACCEPT
Architecture v0.5 → PUBLISH
Session 14 → consolidated
Treasure Hunt → READY FOR A BOUNDED NEXT EXPERIMENT
```

salvo contradicción genuina.

NO modifiques:

* ADR-001;
* ADR-002;
* ADR-003;
* ADR-004;
* Session 11;
* Session 12;
* Session 13;
* Product Experience Definition candidates;
* TypeScript contracts;
* evaluator;
* tests;
* runtime;
* manifests;
* bootstrap;
* Activity;
* AppSnapshot;
* UI.

NO crees:

* ADR-006;
* Architecture v0.6;
* Session 15;
* Treasure Hunt schema;
* Experience engine;
* taxonomy;
* taxonomy mapping;
* authority service;
* new shared contracts;
* provider architecture.

---

### 13. No convertir esta corrección en una refactorización documental

No reorganices ahora todo el repositorio.

No separes `program-architecture.md` en múltiples documentos salvo que sea absolutamente imprescindible para corregir una contradicción.

La recomendación de separar en el futuro:

```text
program architecture
product vision
roadmaps
```

puede registrarse como mejora futura si resulta útil, pero NO es objetivo de este patch.

Preferimos:

```text
small explicit correction
```

a:

```text
large documentation refactor
```

---

### 14. Verification after patch

Como esta tarea debe ser documentation-only:

* no es necesario ejecutar la suite completa de tests;
* no modifiques package files;
* no generes build nuevo salvo que el repositorio tenga una validación documental automática que ya forme parte del flujo normal.

Comprueba al menos:

1. que los enlaces internos siguen resolviendo;
2. que ADR-005 sigue marcado `accepted`;
3. que program architecture sigue marcado `v0.5` y `active`;
4. que Session 14 sigue marcada `consolidated`;
5. que no se ha creado Session 15;
6. que no se ha creado ADR-006;
7. que no se han modificado archivos de código;
8. que no se ha convertido ningún elemento `UNRESOLVED` en componente arquitectónico.

Si Git está disponible, usa el diff para demostrar que el delta se limita a documentación.

---

### 15. Expected final state

Después de la corrección:

```text
ADR-001–004
→ ACCEPTED / unchanged

ADR-005
→ ACCEPTED
→ classification boundary promoted
→ mapping authority explicitly unresolved

Session 14
→ CONSOLIDATED
→ erroneous Session 15 note removed

Architecture v0.5
→ PUBLISHED / ACTIVE
→ composition flow preserved
→ contextual evaluation flow preserved
→ Event recognition lateral/unresolved
→ no generic authority layer
→ no generic Experience simulation engine
→ no speculative shared-contract architecture
→ commercial concepts retain semantic status
→ exact TES chain preserved

ExperienceDefinition tension
→ OPEN / no rename

Taxonomy alignment
→ UNRESOLVED

Mapping authority
→ UNRESOLVED

TES Event recognition
→ UNRESOLVED

Activity unresolved-outcome UX
→ UNRESOLVED

Treasure Hunt
→ READY, NOT STARTED
```

---

### 16. Final adversarial review

Antes de terminar, comprueba específicamente:

##### A. Event recognition

```text
Does the diagram imply that runtime/read models
must pass through TES Event recognition?
```

La respuesta debe ser:

```text
NO
```

##### B. Shared contracts

```text
Does the active architecture imply that
TES concepts must exist as software contracts?
```

Respuesta:

```text
NO
```

##### C. Simulation

```text
Does the roadmap imply a generic Experience engine?
```

Respuesta:

```text
NO
```

##### D. Commercial concepts

```text
Does appearing in a demo upgrade
Maratón de Temporada into an Experience?
```

Respuesta:

```text
NO
```

##### E. TES terminology

```text
Does the architecture use SignificantEvent,
ObservedOutcome or ReusableLearning
as if they were the canonical TES chain?
```

Respuesta:

```text
NO
```

##### F. Mapping

```text
Does ADR-005 imply that semantic mapping authority
has already been demonstrated?
```

Respuesta:

```text
NO
```

##### G. ExperienceDefinition

```text
Does Architecture v0.5 collapse
Product Interpretation,
validated Product Experience Definition,
and runtime Experience descriptor
into the same authority?
```

Respuesta:

```text
NO
```

##### H. Document authority

```text
Does any historical/product-direction wording
gain architectural authority merely because
program-architecture.md is active?
```

Respuesta:

```text
NO
```

---

### 17. Response expected from Codex

Devuélveme:

1. **Files inspected**
2. **Exact corrections made**
3. **For each correction, why it was necessary**
4. **Sections intentionally left unchanged**
5. **Confirmation that Session 14 verdicts remain unchanged**
6. **Confirmation that no code/tests/contracts were modified**
7. **ADR-005 mapping wording after correction**
8. **Architecture v0.5 contextual-evaluation diagram after correction**
9. **How speculative shared contracts were handled**
10. **How the simulation-engine wording was corrected**
11. **How demo concepts preserve their semantic status**
12. **How the TES chain was normalized**
13. **How the ExperienceDefinition wording was kept non-authoritative**
14. **Files modified / created / deleted**
15. **Git diff summary if available**
16. **Final adversarial checklist**
17. **Final project state**
18. **Whether the repository is now cleanly ready for the bounded Treasure Hunt experiment**

No avances a Treasure Hunt.

No propongas todavía su implementation design.

Esta tarea termina cuando la documentación de Session 14, ADR-005 y Architecture v0.5 expresan exactamente la autoridad que la evidencia permite, y nada más.
<!-- FIN-TEXTO-ORIGINAL-S14-CORRECCION -->

---

<a id="sesion-15"></a>

## Capítulo 15 — Evidencia distribuida y suficiencia

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-15-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1743; salida(s) de lectura en la(s) línea(s) 1751, 1757. Cotejado con el recuento histórico de 1519 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: e068f63fa47d5c6ace414395ca624172b1bc65f9023fa766aeb98b5c10fea642.

<!-- INICIO-TEXTO-ORIGINAL-S15 -->
### Session 15 — Treasure Hunt: Distributed Evidence and Sufficiency Experiment

Trabaja sobre el repositorio existente:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

No empieces desde cero.

No rediseñes Architecture v0.5.

No reabras ADR-001–005 salvo contradicción genuina.

No conviertas Treasure Hunt en una nueva Experience Definition validada.

No diseñes todavía Treasure Hunt completo.

Esta sesión inicia un nuevo ciclo experimental:

```text
hypothesis
→ falsification
→ reversible experiment
→ evidence
→ evaluation
```

Un resultado:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NO-GO
STOP
```

es legítimo.

Nunca amplíes semántica o infraestructura solo para conseguir tests verdes.

---

### 1. Estado arquitectónico vigente

El baseline actual es:

```text
ADR-001 → ACCEPTED
ADR-002 → ACCEPTED
ADR-003 → ACCEPTED
ADR-004 → ACCEPTED
ADR-005 → ACCEPTED

Architecture v0.5 → ACTIVE
```

Architecture v0.5 distingue:

```text
Composition flow
```

de:

```text
Contextual evaluation flow
```

y deja explícitamente unresolved:

* TES Event recognition;
* taxonomy alignment;
* semantic mapping authority;
* authority accreditation;
* conflict precedence;
* naming/maturity de `ExperienceDefinition`;
* Activity UX para evaluaciones no resueltas;
* APIs reales.

Treasure Hunt fue declarado:

```text
READY FOR A BOUNDED NEXT EXPERIMENT
```

No significa que Treasure Hunt sea ya una Experience validada ni que posea un domain model aprobado.

---

### 2. Qué simplificación de los experimentos anteriores vamos a tensionar

Cooking Class utilizó esencialmente:

```text
one participant
+
one factual Evidence
+
one ExperienceContext
+
one contextual evaluation
```

Session 13 corrigió la simplificación closed-world:

```text
unknown
≠
negative
```

Treasure Hunt permite ahora tensionar una simplificación diferente:

```text
one atomic Evidence
```

Session 15 debe investigar:

```text
multiple independent factual evidences
        ↓
sufficiency evaluation
```

sin introducir todavía:

```text
group participation
TES Sequence
TES Progression
TES Result
TES Completion
generic Experience engine
```

---

### 3. Product scenario mínimo

Utiliza un único participante.

Narrativamente puede ser:

```text
Business Guest
```

durante una estancia en un hotel orientado a negocios.

El contexto comercial puede formularse como una pequeña búsqueda distribuida por distintos espacios del hotel.

Por ejemplo:

```text
Participant P
Stay S
Property H
Treasure Hunt scenario T
```

No es necesario fijar qué sistema identifica finalmente a `P`.

No decidas todavía si representa:

* loyalty member;
* booking owner;
* account;
* device holder;
* TES participant;
* ExperienceParticipation.

Para este experimento basta una referencia estable y controlada.

---

### 4. No refinar todavía el Contrato semántico de producto

El escenario actual mantiene:

```text
one participant
```

y un dominio experimental controlado de validación/suficiencia.

Por tanto, Session 15 NO debe refinar el actual:

```text
Contrato semántico de producto
```

ni modificar la tesis general App/Builder para introducir semántica colectiva.

Registra únicamente este trigger futuro:

> El Contrato semántico de producto deberá reconsiderarse cuando un experimento cooperativo requiera distinguir de forma material participante individual, contribuyente, grupo, pertenencia, atribución de evidencia o resultado colectivo.

En forma abreviada:

```text
single-participant Treasure Hunt
→ no semantic-contract refinement required

cooperative / multi-participant Treasure Hunt
→ semantic-contract review trigger
```

No anticipes esa revisión.

---

### 5. Evidence factual

Utiliza tres evidencias independientes:

```text
Evidence A
Evidence B
Evidence C
```

Narrativamente pueden corresponder a tres pistas o marcadores situados en espacios diferentes del hotel.

Ejemplo no normativo:

```text
A → marker observed/validated in lobby
B → marker observed/validated in business lounge
C → marker observed/validated in another eligible hotel area
```

No fijes QR, NFC, staff validation, provider o API.

La evidencia debe conservarse factual y neutral.

Puede contener únicamente aquello necesario para identificar:

```text
evidenceRef
subjectRef
scenario/huntRef
observed clue/marker identity
situated context needed by the experiment
```

No añadas como facts:

```text
progress
percentage
cluesFound
sufficient
solved
completed
reward
Result
TES Event
```

En particular:

```text
Evidence
≠
its evaluation
```

según ADR-005.

---

### 6. Criterio experimental de suficiencia

Para evitar que suficiencia se reduzca a un contador, utiliza el siguiente criterio experimental:

```text
A AND (B OR C)
```

Por tanto:

```text
A + B
→ sufficient evidence

A + C
→ sufficient evidence

A
→ sufficiency not established

B
→ sufficiency not established

C
→ sufficiency not established

B + C
→ sufficiency not established

A + A
→ sufficiency not established
```

El criterio existe únicamente para falsificar:

```text
quantity
≠
sufficiency
```

y:

```text
aggregation
≠
sufficiency
```

No promociones:

```text
A AND (B OR C)
```

como regla general de Treasure Hunt.

No construyas un generic expression engine.

No construyas rules DSL.

No construyas un `TreasureHuntRulesEngine`.

Una función pura y fixtures explícitos son preferibles.

---

### 7. Hipótesis principal

#### H15 — Distributed Evidence Sufficiency

> Varias Evidence factual e independientemente válidas pueden contribuir conjuntamente a un claim derivado de suficiencia, pero su pluralidad, cantidad u orden no establecen por sí solos esa suficiencia. El claim requiere un criterio scoped y autoritativo distinto del contenido factual de cada Evidence.

Formulación analítica provisional:

```text
SufficiencyClaim =
f(
    EvidenceSet,
    SituatedContext,
    SufficiencyCriterion
)
```

No conviertas esta fórmula en arquitectura.

`EvidenceSet` no debe convertirse automáticamente en aggregate persistente.

`SufficiencyCriterion` no debe convertirse automáticamente en service, engine o TES concept.

---

### 8. Subhipótesis

#### H15a — Evidence independence

Cada Evidence conserva identidad factual independiente de las demás y de la evaluación de suficiencia.

```text
Evidence A
≠
"Sufficient"
```

#### H15b — Quantity is not sufficiency

Dos registros no son suficientes simplemente porque:

```text
count = 2
```

Debe cumplirse el criterio cualitativo experimental.

Por tanto:

```text
A + B → sufficient
B + C → not established
```

aunque ambos conjuntos tengan cardinalidad 2.

#### H15c — Duplicate evidence does not create sufficiency

```text
A + A
```

no debe satisfacer:

```text
A AND (B OR C)
```

La duplicación de records no equivale a contribuciones semánticamente distintas.

No diseñes una plataforma genérica de deduplicación.

Representa únicamente el caso mínimo necesario para falsificar el contador ingenuo.

#### H15d — Order independence

Para Session 15, las pistas son deliberadamente unordered.

Por tanto:

```text
A then B
```

y:

```text
B then A
```

deben sostener el mismo claim.

Esto debe preservar:

```text
multiple evidence
≠
TES Sequence
```

No modeles pistas habilitantes, encadenadas u ordenadas todavía.

Registra:

```text
ordered / enabling clues
→ future experiment
```

#### H15e — Open-world insufficiency

Cuando el criterio no se satisface con Evidence disponible:

```text
sufficiency not established
```

NO significa necesariamente:

```text
hunt failed
solution false
participant failed
impossible to satisfy
```

La Evidence puede:

* no haber llegado todavía;
* estar retrasada;
* estar pendiente de validación;
* ser ambigua;
* proceder después de otra fuente;
* entrar posteriormente en conflicto.

Session 15 no debe construir latency/conflict infrastructure.

Solo debe conservar la diferencia:

```text
not established
≠
established false
```

#### H15f — Sufficiency is not solution recognition

Incluso cuando:

```text
A + B
```

establece evidencia suficiente, el claim máximo de este experimento es equivalente a:

```text
sufficient evidence established
under criterion K
within scenario T
```

No implica automáticamente:

```text
solution recognized
Treasure Hunt solved
Treasure Hunt completed
TES Result
TES Completion
TES Event
```

La posible frontera:

```text
Sufficient Evidence
        ↓ ?
Solution Recognition
```

permanece:

```text
UNRESOLVED
```

#### H15g — Sufficiency is not TES Progression

No inferir:

```text
A = 33%
A+B = 66%
A+B+C = 100%
```

como TES Progression.

Tampoco:

```text
number of clues
=
Progression
```

Un contador UI podría existir en el futuro como read model, pero no adquiere semántica TES por ello.

#### H15h — Partial incentive remains downstream

Cuando existe:

```text
sufficient evidence established
```

el huésped **puede quedar en condiciones de recibir un incentivo parcial**.

La relación experimental permitida es:

```text
SufficiencyClaim
        ↓
possible eligibility / authorization
for partial incentive
```

Pero:

```text
partial incentive
≠
proof of sufficiency
```

y:

```text
partial incentive
≠
TES Result
```

y:

```text
partial incentive
≠
Treasure Hunt completion
```

La dirección es únicamente:

```text
sufficiency evaluation
        ↓
downstream incentive eligibility/use
```

Nunca:

```text
incentive exists
        ↓
therefore evidence was sufficient
```

No construyas reward engine.

No construyas incentive engine.

Si el repositorio ya posee una representación mínima compatible, puede utilizarse de forma experimental.

Si no existe, usa únicamente una derivación test-local o documenta la posibilidad downstream.

No crees infraestructura para demostrarla.

#### H15i — Activity remains downstream

Activity no participa en:

```text
evidence aggregation
sufficiency evaluation
criterion satisfaction
```

Puede eventualmente presentar:

```text
clue observed
sufficient evidence established
partial incentive available
```

pero no originar dichos claims.

---

### 9. Authority Frontier candidata

Session 15 investiga provisionalmente una nueva pregunta:

> ¿Quién tiene autoridad para afirmar que un conjunto de Evidence es suficiente para sostener un claim concreto dentro de un scope?

Denomina analíticamente, si ayuda:

```text
Evidence Sufficiency Authority
```

pero NO promociones el término a componente arquitectónico.

No crees:

```text
EvidenceSufficiencyAuthorityService
SufficiencyRegistry
RuleProvider
CriteriaEngine
```

La pregunta es sobre autoridad del claim, no sobre topología de software.

---

### 10. Distinción entre aggregation y sufficiency

Esta distinción es central.

```text
Aggregation
```

puede significar únicamente:

```text
these Evidence records are being considered together
```

No significa:

```text
they are sufficient
```

Por tanto:

```text
aggregation
≠
sufficiency
```

Y tampoco:

```text
sufficiency
≠
solution recognition
```

Conserva las tres posibles fronteras:

```text
Independent factual Evidence
        ↓
considered together / aggregation
        ↓
Sufficiency evaluation
        ↓
Sufficiency claim
        ↓ ?
Future solution-recognition boundary
```

No promociones `aggregation` como nuevo aggregate/domain entity salvo que la implementación mínima lo exija de forma demostrada.

---

### 11. Diseño experimental mínimo obligatorio

Mantén constantes:

```text
Participant P
Stay S
Property H
Treasure Hunt scenario T
Sufficiency criterion K = A AND (B OR C)
```

Cambia únicamente la Evidence disponible.

#### Caso A — no evidence

```text
{}
```

Expected:

```text
sufficiency not established
```

No failure.

#### Caso B — A only

```text
{A}
```

Expected:

```text
sufficiency not established
```

#### Caso C — B + C

```text
{B, C}
```

Expected:

```text
sufficiency not established
```

Crítico porque:

```text
count = 2
```

pero el criterio no se satisface.

#### Caso D — A + B

```text
{A, B}
```

Expected:

```text
sufficiency established
```

#### Caso E — A + C

```text
{A, C}
```

Expected:

```text
sufficiency established
```

#### Caso F — A + A

Dos records que representan la misma contribución factual relevante.

Expected:

```text
sufficiency not established
```

No:

```text
count 2 → sufficient
```

#### Caso G — order independence

```text
[A, B]
```

vs.

```text
[B, A]
```

Expected:

```text
same sufficiency claim
```

#### Caso H — extra evidence

```text
{A, B, C}
```

Expected:

```text
sufficiency established
```

pero NO stronger claim que A+B o A+C.

En particular, NO:

```text
more evidence
→ more Progression
→ stronger Result
```

#### Caso I — downstream partial incentive

Para un outcome de suficiencia establecido:

```text
possible partial-incentive eligibility
```

puede derivarse downstream.

Para un outcome no establecido:

```text
no eligibility may be inferred from sufficiency
```

Esto NO debe convertir el incentive en autoridad retroactiva.

Si implementar este caso exige infraestructura nueva, déjalo como documented downstream implication y NO lo fuerces al código.

---

### 12. Latency, ambiguity and confusing evidence

La observación siguiente debe quedar registrada:

> En escenarios reales, una aparente insuficiencia puede provenir no solo de ausencia factual sino también de latencia, evidencia todavía no validada, ambigüedad, confusión de identidad, duplicación o conflicto.

Session 15 NO debe resolver esos casos.

No diseñes:

* pending evidence state machine;
* latency model;
* conflict engine;
* confidence model;
* identity-resolution system.

Solo preserva el invariant:

```text
insufficiency under currently available evidence
does not prove failure
```

Registra esos factores como futuras Authority Frontiers/cualificaciones candidatas.

---

### 13. No convertir Treasure Hunt en TES semantics

Está expresamente prohibido inferir:

```text
Clue
=
TES Event
```

```text
multiple clues
=
Pattern
```

```text
ordered clues
=
Sequence
```

```text
clue count
=
Progression
```

```text
sufficient evidence
=
Result
```

```text
all clues
=
Completion
```

```text
partial incentive
=
Result
```

La cadena TES sigue siendo:

```text
Event
→ Pattern
→ Sequence
→ Progression
→ Result
→ Measurement
→ Learning
```

Session 15 no operacionaliza ninguno de estos conceptos.

---

### 14. No convertir Treasure Hunt en Experience Definition

Treasure Hunt en esta sesión es:

```text
experimental situated scenario
```

No:

```text
Validated Product Experience Definition
```

No crees un Product Experience Definition completo para Treasure Hunt.

No añadas artificialmente:

* Pattern;
* Sequence;
* Progression;
* Result;
* Measurement;
* Learning;

para hacerlo parecer semánticamente completo.

Si el experimento requiere esas construcciones:

```text
STOP
```

porque el diseño ha excedido el scope.

---

### 15. Inspección del repositorio antes de implementar

Localiza como mínimo:

* `evidence-relevance.ts`;
* `evidence-relevance.test.ts`;
* cualquier tipo factual de Evidence existente;
* cualquier representación de authority;
* Activity/AppSnapshot;
* incentive/reward contracts existentes;
* runtime/public-action boundary;
* ADR-005;
* Architecture v0.5;
* Session 13;
* Session 14.

Determina si la nueva evaluación de suficiencia debe:

```text
A. extender experimentalmente una frontera existente
```

o:

```text
B. usar una función pura separada
```

No decidas por simetría.

La preferencia semántica es **no mezclar relevance con sufficiency** si representan claims diferentes.

Por tanto, no sobrecargues:

```text
evaluateEvidenceRelevance()
```

solo porque ya existe.

Si una función experimental separada es más honesta:

```text
evaluateEvidenceSufficiency(...)
```

o nombre equivalente puede ser preferible.

Pero el nombre NO se promociona a arquitectura.

---

### 16. Preferencia de implementation delta

Preferencia:

```text
existing factual Evidence concepts
+
minimal experimental sufficiency boundary
+
explicit fixtures
+
focused tests
+
Session 15 document
```

No:

```text
Treasure Hunt module hierarchy
generic rules engine
new domain platform
```

La implementación debe ser fácilmente eliminable si H15 falla.

---

### 17. Falsifiers

Considera H15 total o parcialmente falsificada/no soportada si ocurre cualquiera de estos casos:

1. `B + C` produce sufficiency simplemente porque hay dos evidencias;
2. `A + A` produce sufficiency por count;
3. cambiar el orden A/B cambia el claim en un experimento declarado unordered;
4. Evidence individual necesita contener `sufficient`;
5. Activity count se utiliza como input autoritativo;
6. sufficiency requiere TES Progression;
7. sufficiency se implementa como TES Result;
8. sufficiency requiere Event recognition;
9. incentive concedido se utiliza para inferir retroactivamente suficiencia;
10. para implementar `A AND (B OR C)` hace falta un generic DSL/rules engine;
11. Treasure Hunt debe convertirse en Experience Definition completa;
12. se necesita group semantics para ejecutar este caso unipersonal;
13. la ausencia de una Evidence produce `failed` en vez de preservar no-determinación;
14. más Evidence produce un claim semánticamente “más completo” sin criterio adicional;
15. el experimento obliga a refinar el Contrato semántico de producto pese a mantener un solo participante.

Si ocurre:

```text
do not expand architecture
```

Documenta el resultado.

---

### 18. Contrato semántico de producto — trigger futuro obligatorio

Session 15 debe terminar registrando explícitamente:

```text
Semantic Product Contract review trigger:
first cooperative / multi-participant Treasure Hunt experiment
```

Esa futura revisión deberá cuestionar, como mínimo:

```text
individual participant
contributor
group
membership
evidence attribution
shared evidence
group sufficiency
group outcome
```

No respondas ahora esas preguntas.

Solo registra el trigger.

---

### 19. Pistas habilitantes / ordenadas — trigger futuro

Session 15 utiliza:

```text
unordered clues
```

No presupone que Treasure Hunt general sea unordered.

Registra:

```text
ordered or enabling clues
→ separate future experiment
```

Ese experimento deberá distinguir, llegado el momento:

```text
temporal order
causal enablement
narrative order
TES Sequence
```

No los mezcles ahora.

---

### 20. Incentivo parcial — límites

La observación de producto a preservar es:

> Cuando existe evidencia suficiente bajo el criterio experimental, el huésped puede recibir un incentivo parcial.

No convertir esta frase en:

```text
sufficiency automatically grants incentive
```

sin pasar por la autoridad operacional apropiada.

Distingue:

```text
SufficiencyClaim
        ↓
possible incentive eligibility
        ↓
runtime/public action or product policy
        ↓
incentive presentation/use
```

si el repositorio real permite representar esa separación mínimamente.

No diseñes esta cadena si no existe infraestructura suficiente.

En ese caso documenta únicamente:

```text
partial incentive
→ downstream implication
→ not tested operationally
```

---

### 21. Tests y verificaciones

Añade únicamente los tests necesarios para falsificar H15.

Después ejecuta la suite real del repositorio:

```text
tests
typecheck
lint
build
```

si existen.

Informa:

* test files;
* total tests;
* nuevos tests;
* typecheck;
* lint;
* build;
* archivos modificados;
* archivos nuevos;
* archivos eliminados.

Comprueba especialmente:

```text
no generic rule engine
no Experience-ID branching
no TES terminology introduced as runtime semantics
no Activity dependency
no Product Semantic Contract changes
```

---

### 22. Documento Session 15

Crea:

```text
Session 15 — Treasure Hunt: Distributed Evidence and Sufficiency Experiment
```

Debe incluir:

#### 1. Hypothesis

H15 y subhipótesis.

#### 2. Why Treasure Hunt

Qué simplificación de Cooking Class tensiona.

#### 3. Scope

```text
one participant
unordered clues
distributed Evidence
sufficiency
partial incentive downstream
```

#### 4. Explicit exclusions

Group semantics, TES semantics, ordered clues, engines, APIs.

#### 5. Repository inspection

Estado real previo.

#### 6. Experimental model

A, B, C y K = A AND (B OR C).

#### 7. Authority Frontier

Qué autoridad experimental sostiene el criterio de suficiencia.

#### 8. Test matrix

Expected vs observed.

#### 9. Aggregation vs sufficiency

Conclusión explícita.

#### 10. Sufficiency vs solution recognition

Conclusión explícita.

#### 11. Sufficiency vs incentive

Conclusión explícita.

#### 12. Open-world implications

Latency, ambiguity, missing evidence y conflict como límites no resueltos.

#### 13. Activity frontier

Confirmación de downstream.

#### 14. Semantic Product Contract

Confirmación de que NO se refinó y trigger para cooperative scenario.

#### 15. Evidence

Qué quedó realmente demostrado.

#### 16. Claims supported

#### 17. Claims not supported

#### 18. Limitations

#### 19. Architectural evaluation

No promotion automática.

#### 20. Verdict

Uno de:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NO-GO
STOP
```

---

### 23. Claims que una Session 15 positiva podría soportar

Como máximo:

```text
multiple independent Evidence
can participate in one derived evaluation
```

```text
evidence count
does not establish sufficiency
```

```text
evidence aggregation
does not establish sufficiency
```

```text
sufficiency can be derived
without TES Progression / Result
```

```text
unordered Evidence
need not imply TES Sequence
```

```text
missing qualifying Evidence
does not prove failure
```

```text
sufficiency may support
a downstream partial-incentive decision
without becoming the incentive or Result
```

```text
Activity can remain downstream
```

---

### 24. Claims que Session 15 NO puede soportar

No puede demostrar:

* Treasure Hunt como TES-validada Experience;
* Treasure Hunt Completion;
* TES Event;
* TES Pattern;
* TES Sequence;
* TES Progression;
* TES Result;
* Measurement;
* Learning;
* solution-recognition semantics;
* group participation;
* group evidence;
* family semantics;
* contributor membership;
* shared evidence attribution;
* group sufficiency;
* ordered/enabling clue semantics;
* generic rules engine;
* generic sufficiency engine;
* incentive/reward engine;
* real provider architecture;
* persistence;
* latency infrastructure;
* confidence;
* conflict resolution;
* API contracts;
* semantic-contract changes.

---

### 25. Promotion prohibition

Aunque H15 resulte SUPPORTED:

```text
NO ADR-006
NO Architecture v0.6
NO Product Semantic Contract refinement
NO Treasure Hunt Experience Definition
NO group model
```

Session 15 produce:

```text
Experiment
→ Evidence
```

La evaluación/promoción posterior deberá ser una sesión separada si la evidencia lo merece.

---

### 26. Final adversarial questions

Antes del verdict, responde:

1. ¿`A+B` es suficiente porque son dos evidencias o porque satisface K?
2. ¿`B+C` demuestra que count y sufficiency son distintos?
3. ¿`A+A` demuestra que record count no equivale a evidence contribution?
4. ¿El orden alteró accidentalmente el resultado?
5. ¿Se introdujo una TES Sequence implícita?
6. ¿Se introdujo Progression mediante counts?
7. ¿Se convirtió sufficiency en Result o Completion?
8. ¿Se convirtió el incentive en prueba retroactiva?
9. ¿La ausencia se interpretó como fracaso?
10. ¿El evaluator adquirió autoridad que pertenecía al criterio?
11. ¿Treasure Hunt se convirtió accidentalmente en Experience Definition?
12. ¿Se refinó innecesariamente el Contrato semántico de producto?
13. ¿Latency/ambiguity/conflict se mantuvieron abiertos?
14. ¿Group semantics siguen completamente fuera?
15. ¿Ordered/enabling clues siguen fuera?
16. ¿La implementación podría retirarse sin alterar ADR-001–005?

Si alguna respuesta revela sobrepromoción, reduce el verdict.

---

### 27. Respuesta final esperada de Codex

Devuelve:

1. Repository inspection.
2. Baseline compatibility.
3. Experimental model actually implemented.
4. Why the delta is minimal.
5. Evidence representation.
6. Sufficiency criterion representation.
7. Whether relevance evaluator was reused or a separate boundary was created, and why.
8. Full test matrix.
9. Aggregation vs sufficiency result.
10. Duplicate-evidence result.
11. Order-independence result.
12. Open-world insufficiency result.
13. Sufficiency vs solution-recognition assessment.
14. Partial-incentive downstream assessment.
15. Activity frontier assessment.
16. Confirmation that Product Semantic Contract was not changed.
17. Future semantic-contract review trigger.
18. Ordered/enabling-clue future trigger.
19. Latency/ambiguity/conflict unresolved findings.
20. Test/typecheck/lint/build results.
21. Files created/modified/deleted.
22. Claims supported.
23. Claims NOT supported.
24. Limitations.
25. Authority-laundering review.
26. Session 15 verdict.
27. Recommended next step.

Sé adversarial.

No construyas Treasure Hunt para demostrar que Treasure Hunt funciona.

Utilízalo únicamente para falsificar si varias evidencias independientes pueden sostener un claim de suficiencia sin convertir cantidad, orden, incentivo o presentación en semántica que todavía no hemos demostrado.
<!-- FIN-TEXTO-ORIGINAL-S15 -->

---

<a id="sesion-16"></a>

## Capítulo 16 — Preparar la frontera entre atribución y admisibilidad

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-16-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1861; salida(s) de lectura en la(s) línea(s) 1869, 1875. Cotejado con el recuento histórico de 869 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: a5f6c5faec462a148b14b67e3f13d2a26d2c3733ac0c496afcc7c403588318a2.

<!-- INICIO-TEXTO-ORIGINAL-S16 -->
### Session 16 — Consolidation of Distributed Evidence and Sufficiency

Trabaja sobre el repositorio existente:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

Esta sesión es de **evaluación y consolidación documental**.

NO es un nuevo experimento.

NO implementes nueva funcionalidad.

NO diseñes todavía el Treasure Hunt cooperativo.

NO modifiques el Contrato semántico de producto.

NO crees ADR-006 salvo que la evidencia existente demuestre inequívocamente que ADR-005 es insuficiente como decisión arquitectónica.

NO publiques Architecture v0.6 salvo que exista una modificación arquitectónica genuina que no pueda expresarse correctamente dentro de v0.5.

La hipótesis inicial de esta sesión, que debes intentar refutar, es:

```text
H16:

Session 15 no requiere una nueva decisión arquitectónica.

Sus resultados son una especialización y evidencia adicional
del invariant ya aceptado en ADR-005:

la evidencia factual permanece separada de los claims derivados,
y la consideración conjunta de varias evidencias no concede
por sí sola semántica de suficiencia, progresión, resultado
o completion.
```

No protejas esta hipótesis.

Si la evidencia exige ADR-006, dilo.

---

### 1. Baseline vigente

Estado aceptado antes de Session 16:

```text
ADR-001 → ACCEPTED
ADR-002 → ACCEPTED
ADR-003 → ACCEPTED
ADR-004 → ACCEPTED
ADR-005 → ACCEPTED

Architecture v0.5 → ACTIVE

Session 15
→ H15 SUPPORTED WITH QUALIFICATION
```

Architecture v0.5 distingue:

```text
composition flow
```

de:

```text
contextual evaluation flow
```

y no contiene:

* Evidence Aggregator;
* Sufficiency Service;
* Treasure Hunt engine;
* Authority Service;
* TES Event recognizer;
* generic rules engine.

No introduzcas ninguno durante esta sesión.

---

### 2. Evidencia que debes evaluar

Revisa, como mínimo:

* ADR-005;
* Architecture v0.5;
* Session 13;
* Session 14;
* Session 15;
* implementación de `evaluateEvidenceSufficiency()` y sus tests;
* implementación de `evaluateEvidenceRelevance()` únicamente para comparar fronteras, no para fusionarlas.

Comprueba que Session 15 realmente sostiene:

```text
multiple factual Evidence
can be considered jointly
```

sin sostener:

```text
multiple Evidence
=
sufficiency
```

y que sostiene:

```text
count
≠
sufficiency
```

```text
aggregation
≠
sufficiency
```

```text
duplicate records
≠
distinct qualifying contributions
```

dentro del alcance experimental.

---

### 3. Pregunta principal de promoción

Decide:

> ¿Session 15 introduce un nuevo invariant arquitectónico independiente o únicamente aporta evidencia adicional/especializada para ADR-005?

Evalúa explícitamente las dos alternativas.

#### Alternativa A — Absorción por ADR-005

Sería correcta si lo demostrado puede derivarse de:

```text
Evidence
≠
derived contextual claim
```

y:

```text
derived claim authority
is bounded by its premises
```

sin necesidad de una nueva responsabilidad arquitectónica.

En ese caso:

```text
ADR-005
→ remains sufficient

Session 15
→ supporting evidence

ADR-006
→ NOT NEEDED
```

#### Alternativa B — Nueva decisión arquitectónica

Solo sería correcta si Session 15 demuestra una frontera independiente que:

* no esté ya gobernada por ADR-005;
* tenga consecuencias arquitectónicas propias;
* no pueda tratarse simplemente como otro tipo de evaluación derivada;
* requiera una decisión estable más allá del fixture experimental.

No crees ADR-006 únicamente porque exista el término:

```text
Evidence Sufficiency Authority
```

Ese término sigue siendo analítico y provisional.

---

### 4. No promover `EvidenceSet`

Session 15 utilizó varias Evidence simultáneamente.

Esto NO demuestra:

```text
EvidenceSet
```

como:

* aggregate;
* entity;
* store;
* value object obligatorio;
* persistence boundary;
* API contract.

La consideración conjunta puede seguir siendo:

```text
in-memory evaluation concern
```

hasta nueva evidencia.

Evalúa explícitamente:

```text
multiple inputs
≠
domain aggregate
```

---

### 5. No promover `Evidence Sufficiency Authority`

Session 15 mostró que un claim de suficiencia necesita un criterio competente/scoped.

Pero el experimento solo usó un fixture controlado.

Por tanto distingue:

```text
need for an authoritative sufficiency premise
```

de:

```text
Evidence Sufficiency Authority
as architectural component
```

La primera puede estar soportada.

La segunda permanece:

```text
NOT DEMONSTRATED
```

salvo evidencia contraria.

No crees:

* SufficiencyAuthorityService;
* SufficiencyRegistry;
* RuleProvider;
* CriterionRepository;
* Authority aggregate.

---

### 6. Contribution identity — límite importante

Session 15 deduplicó por:

```text
markerRef
```

solo para falsificar:

```text
A + A
→ count 2
→ sufficient
```

No promociones:

```text
markerRef
=
semantic contribution identity
```

como invariant general.

Registra:

```text
duplicate-record handling
→ SUPPORTED LOCALLY

general contribution identity
→ UNRESOLVED
```

Esto será especialmente importante en escenarios cooperativos.

---

### 7. `not-established` no es vocabulario normativo

Session 15 utilizó:

```text
established
not-established
```

como representación experimental.

No promociones esos literales.

Lo demostrado es únicamente la distinción:

```text
sufficiency established
```

frente a:

```text
sufficiency cannot currently be established
```

sin colapsar este último estado en:

```text
failure
false
impossible
```

Mantén abiertos:

* missing evidence;
* delayed evidence;
* ambiguous evidence;
* conflicting evidence;
* criterion not applicable;
* authority unavailable.

No diseñes un outcome model nuevo.

---

### 8. Aggregation vs sufficiency

Evalúa si debe consolidarse como principio explícito:

```text
aggregation
≠
sufficiency
```

Pero no asumas que necesita ADR independiente.

Pregúntate:

> ¿Es simplemente una instancia de ADR-005, donde los inputs factuales no contienen el claim derivado?

Si sí, regístralo como evidencia/consecuencia de ADR-005.

Si no, explica exactamente qué responsabilidad arquitectónica adicional introduce.

---

### 9. Sufficiency vs TES semantics

Session 15 mostró que puede evaluarse suficiencia sin:

* TES Event;
* Pattern;
* Sequence;
* Progression;
* Result;
* Measurement;
* Learning;
* Completion.

Consolida únicamente la separación:

```text
SufficiencyClaim
≠
TES Progression
≠
TES Result
≠
Treasure Hunt Completion
```

No conviertas esa evidencia negativa en un nuevo modelo TES.

No actualices el Contrato semántico de producto por este motivo.

---

### 10. Sufficiency vs solution recognition

Session 15 soporta:

```text
sufficiency evaluation
does not require solution recognition
```

pero NO demuestra:

```text
SolutionRecognition
```

como componente o boundary final.

Mantén:

```text
possible future solution-recognition relation
→ UNRESOLVED
```

No crees una nueva caja arquitectónica.

---

### 11. Incentivo parcial

Session 15 NO probó operacionalmente la relación con incentivo.

Por tanto:

```text
SufficiencyClaim
→ possible partial-incentive eligibility
```

permanece una implicación de producto downstream.

No promover:

```text
sufficiency automatically grants incentive
```

ni:

```text
incentive existence proves sufficiency
```

Mantén incentive eligibility como:

```text
NOT OPERATIONALLY TESTED
```

No implementes nada.

---

### 12. Architecture v0.5

Evalúa expresamente si Session 15 exige cambiar Architecture v0.5.

La hipótesis inicial es:

```text
NO
```

porque v0.5 ya permite:

```text
Neutral factual evidence + authoritative premises
        ↓
Contextual evaluation
        ↓
Derived claim
```

y no limita `Neutral factual evidence` a cardinalidad uno.

Si esto es suficiente:

```text
Architecture v0.5
→ survives unchanged

Architecture v0.6
→ NOT NEEDED
```

Solo propone v0.6 si existe una diferencia topológica genuina.

No introduzcas:

```text
Evidence Aggregation Layer
Sufficiency Layer
EvidenceSet Aggregate
```

para representar Session 15.

---

### 13. ADR-005

Evalúa si ADR-005 necesita:

```text
A. no change
B. clarification/amendment
C. replacement
D. new ADR
```

La hipótesis inicial es:

```text
A. no change
```

porque ADR-005 ya dice que:

* Evidence permanece factual;
* los claims derivados dependen de premisas;
* la transformación no crea autoridad;
* insuficiencia no debe convertirse silenciosamente en negativo.

No modifiques ADR-005 salvo necesidad demostrada.

Si Session 15 únicamente aporta evidencia adicional, referencia esa evidencia desde Session 16, no alteres el ADR.

---

### 14. Trigger cooperativo

Session 15 registró:

```text
Semantic Product Contract review trigger:
first cooperative / multi-participant Treasure Hunt experiment
```

Session 16 debe confirmar si ese trigger sigue siendo válido.

NO realices todavía esa revisión.

NO modifiques el contrato.

La siguiente sesión experimental, en otro hilo, podrá introducir múltiples sujetos.

La cuestión candidata será:

> ¿Bajo qué condiciones Evidence producida por sujetos distintos puede considerarse conjuntamente para evaluar suficiencia sin asumir automáticamente que esos sujetos constituyen un grupo ni inventar semántica colectiva?

Session 16 solo debe dejar preparada esa frontera.

---

### 15. Fronteras que deben llegar abiertas al experimento cooperativo

Registra explícitamente como `UNRESOLVED`:

```text
participant identity
contributor identity
group identity
group membership
shared participation
cross-participant evidence attribution
contribution identity
group evidence
group sufficiency
group outcome
```

También permanecen abiertos:

```text
ordered/enabling clues
solution recognition
incentive eligibility
latency
ambiguity
conflict
identity confusion
authority accreditation
```

No resuelvas ninguno.

---

### 16. Criterios para NO crear ADR-006

No crear ADR-006 si:

1. `aggregation ≠ sufficiency` es una consecuencia de ADR-005;
2. múltiples Evidence solo amplían el número de premisas de una evaluación;
3. no se necesita un componente nuevo;
4. no se necesita una nueva topología;
5. no existe contrato reusable demostrado;
6. `Evidence Sufficiency Authority` sigue siendo concepto analítico;
7. la implementación es todavía local/removible;
8. no existen consumers productivos.

Si se cumplen estos puntos, el resultado esperado es:

```text
ADR-006 → NOT NEEDED
```

---

### 17. Criterios que podrían justificar ADR-006

Solo considera ADR-006 si puedes demostrar que existe un invariant independiente como:

```text
X
```

que:

* no esté contenido en ADR-005;
* sobreviva a cambiar Treasure Hunt;
* no dependa de A/B/C;
* no dependa del shape actual;
* introduzca una responsabilidad arquitectónica estable;
* tenga consecuencias normativas propias.

Si no puedes formular ese `X` sin hablar del fixture:

```text
ADR-006 → NOT JUSTIFIED
```

---

### 18. No nuevo experimento

No modifiques:

* `evidence-sufficiency.ts`;
* sus tests;
* relevance evaluator;
* Activity;
* Runtime;
* Product Semantic Contract;
* manifests;
* bootstrap;
* APIs.

No añadas tests salvo que sea estrictamente necesario para verificar una contradicción documental/material ya existente.

Esta sesión debe ser:

```text
documentation + evaluation
```

---

### 19. Documento Session 16

Crea:

```text
Session 16 — Consolidation of Distributed Evidence and Sufficiency
```

Debe incluir:

#### 1. Executive conclusion

```text
ADR-006 verdict
Architecture v0.6 verdict
ADR-005 status
Architecture v0.5 status
Cooperative experiment readiness
```

#### 2. Evidence reviewed

Session 15 + código/test relevante.

#### 3. What H15 actually demonstrated

Sin ampliarlo.

#### 4. What H15 did not demonstrate

#### 5. ADR-005 compatibility

#### 6. Aggregation vs sufficiency

#### 7. Multiple Evidence vs aggregate

#### 8. Contribution identity

#### 9. Sufficiency authority

#### 10. Outcome representation

#### 11. TES separation

#### 12. Solution recognition

#### 13. Partial incentive

#### 14. Architecture v0.5 compatibility

#### 15. ADR-006 decision

#### 16. Architecture v0.6 decision

#### 17. Semantic Product Contract trigger

#### 18. Cooperative-scenario unresolved frontiers

#### 19. Final epistemic state

#### 20. Recommended next experiment

---

### 20. Permitted verdicts

#### ADR-006

Exactamente uno:

```text
ADR-006 → NOT NEEDED
ADR-006 → DEFER
ADR-006 → REQUIRED
```

Si `REQUIRED`, NO lo crees todavía.

Explica qué invariant independiente lo exigiría.

#### Architecture v0.6

Exactamente uno:

```text
Architecture v0.6 → NOT NEEDED
Architecture v0.6 → DEFER
Architecture v0.6 → REQUIRED
```

Si `REQUIRED`, no la publiques durante esta sesión.

---

### 21. Estado esperado si la hipótesis sobrevive

La expectativa, no la conclusión impuesta, es:

```text
ADR-005
→ ACCEPTED / unchanged

Session 15
→ supporting evidence for ADR-005
→ specialized evidence on multiple factual premises

ADR-006
→ NOT NEEDED

Architecture v0.5
→ ACTIVE / unchanged

Architecture v0.6
→ NOT NEEDED

Evidence Sufficiency Authority
→ analytical candidate only

Contribution identity
→ UNRESOLVED

Solution recognition
→ UNRESOLVED

Partial incentive
→ NOT OPERATIONALLY TESTED

Semantic Product Contract
→ unchanged
→ review trigger reached for next cooperative experiment
```

---

### 22. Final adversarial questions

Antes del verdict responde:

1. ¿Session 15 demuestra una nueva responsabilidad o una nueva instancia de evaluación?
2. ¿`aggregation ≠ sufficiency` ya está implicado por ADR-005?
3. ¿Existe alguna razón para materializar `EvidenceSet`?
4. ¿Existe evidencia para una Sufficiency Authority productiva?
5. ¿`markerRef` puede promocionarse como identidad general de contribución?
6. ¿`not-established` debe convertirse en vocabulario de dominio?
7. ¿Existe una topología nueva que v0.5 no pueda representar?
8. ¿ADR-005 necesita modificación para aceptar múltiples premisas factuales?
9. ¿Se está intentando crear ADR-006 por simetría con sesiones anteriores?
10. ¿El incentivo parcial añade actualmente arquitectura?
11. ¿Solution Recognition existe realmente o solo una pregunta?
12. ¿El primer escenario cooperativo activa legítimamente la revisión del Contrato semántico de producto?
13. ¿Podemos llegar al experimento cooperativo manteniendo todos los conceptos colectivos unresolved?

Si una nueva decisión no supera estas preguntas:

```text
do not promote it
```

---

### 23. Respuesta final esperada de Codex

Devuelve:

1. Repository/document inspection.
2. Session 15 evidence validation.
3. H15 scope assessment.
4. ADR-005 compatibility.
5. Whether Session 15 adds a new invariant.
6. Aggregation vs sufficiency assessment.
7. EvidenceSet/aggregate assessment.
8. Contribution-identity assessment.
9. Evidence Sufficiency Authority assessment.
10. Outcome-vocabulary assessment.
11. TES separation assessment.
12. Solution-recognition assessment.
13. Partial-incentive assessment.
14. ADR-006 verdict.
15. Architecture v0.6 verdict.
16. Files changed/created/deleted.
17. Confirmation of no product-code changes.
18. Semantic Product Contract status.
19. Cooperative review trigger.
20. Unresolved frontiers entering the cooperative experiment.
21. Final epistemic state.
22. Recommended next experiment.

Sé adversarial.

No crees una decisión nueva para premiar un experimento exitoso.

El objetivo de Session 16 es determinar si hemos aprendido algo arquitectónicamente nuevo o si hemos obtenido evidencia más rica para una frontera que ADR-005 ya gobierna.
<!-- FIN-TEXTO-ORIGINAL-S16 -->

---

<a id="sesion-17"></a>

## Capítulo 17 — Composición entre sujetos acotada por autoridad

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-17-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 1927; salida(s) de lectura en la(s) línea(s) 1935, 1941. Cotejado con el recuento histórico de 1434 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 277a6eb5f9808c2d8b5ab04961fd52e678dc0e0b09bb6d537758424393bc9a87.

<!-- INICIO-TEXTO-ORIGINAL-S17 -->
### Session 17 — Authority-Bounded Cross-Subject Evidence Composition Experiment

Continue the existing project:

`Convercus Demo Factory / Convercus Experience Products`

Repository:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

Do not start from scratch.

This session begins after the consolidation of Session 16.

The objective is to run the **first cooperative / multi-subject experiment** while preserving the existing epistemic method and without introducing a Group model.

---

### 1. Baseline

Treat the following as established baseline and do not reopen them unless the experiment discovers a genuine contradiction.

```text
ADR-001–005
→ ACCEPTED

Architecture v0.5
→ ACTIVE / unchanged

ADR-006
→ NOT NEEDED

Architecture v0.6
→ NOT NEEDED
```

Session 15 demonstrated, with one subject:

```text
A + B → sufficiency established
A + C → sufficiency established

A → not established
B + C → not established
A + A → not established

[A,B] = [B,A]

A+B+C
→ no stronger claim than A+B
```

under the experimental sufficiency criterion:

```text
K = A AND (B OR C)
```

Session 15 supported:

```text
count ≠ sufficiency
aggregation ≠ sufficiency
duplicate record ≠ distinct qualifying contribution
multiple Evidence ≠ TES Sequence
sufficiency ≠ TES Progression / Result / Completion
```

Session 16 consolidated Session 15 as supporting evidence for ADR-005.

Do not create a new ADR merely because this session introduces more than one subject.

---

### 2. Existing semantic constraints

Preserve TES bounded semantic authority.

TES governs:

* meaning;
* semantic relationships;
* invariants of governed concepts.

TES does not automatically prescribe:

* persistence;
* APIs;
* providers;
* repositories;
* stores;
* services;
* runtime topology;
* UI;
* technical architecture.

Reference TES chain:

```text
Event
→ Pattern
→ Sequence
→ Progression
→ Result
→ Measurement
→ Learning
```

Do not reinterpret ordinary runtime concepts as TES concepts.

In particular:

```text
observed fact ≠ TES Event
multiple Evidence ≠ TES Pattern
multiple actions ≠ TES Sequence
counter ≠ TES Progression
reward ≠ TES Result
```

TES Event recognition remains:

```text
UNRESOLVED
```

and is not required for this experiment.

---

### 3. ADR-005 remains the governing invariant

ADR-005 — Neutral Evidence and Authority-Bounded Contextual Evaluation — remains accepted.

Preserve:

```text
factual Evidence
≠
Experience-relative evaluation
```

and:

```text
derived claim authority
≤
authority + scope + maturity
of its premises
```

Also preserve:

```text
insufficient knowledge
≠
negative determination
```

A negative determination requires sufficient authoritative basis within the evaluated scope.

Activity/read models may project claims but may not originate or strengthen factual or semantic authority.

---

### 4. Experimental frontier

The new experimental frontier is:

```text
authority-bounded cross-subject evidence composition
```

This exact expression may be used as the name of the experimental variable.

Important terminology rule:

`composition` already has an architectural meaning in:

```text
Desired Demo Composition
Effective Demo Composition
Composition Flow
```

Therefore:

* do not use the bare term `composition` to describe the new evidence operation;
* use the full expression `authority-bounded cross-subject evidence composition` when referring to the experimental frontier;
* use `joint admissibility` for the operational decision being tested.

Preserve:

```text
Demo Composition
≠
authority-bounded cross-subject evidence composition
```

Do not introduce an API or function called `composeEvidence()` merely because the experimental variable uses the word composition.

---

### 5. Experimental question

Start from:

```text
Evidence A
subjectRef = P1

Evidence B
subjectRef = P2

P1 != P2
```

Session 15 already established that:

```text
A + B
```

may satisfy K when the Evidence may legitimately be considered together.

The new question is:

```text
What authorizes Evidence attributed
to distinct subjects to be treated
as jointly admissible premises
of the same contextual evaluation?
```

Do not begin with:

```text
What is a Group?
```

The experiment is specifically intended to determine whether `Group` is needed at all for this frontier.

---

### 6. H17

Test the following hypothesis:

```text
H17 — Authority-bounded cross-subject evidence composition

Evidence attributed to distinct subjects
may be treated as jointly admissible premises
of the same contextual sufficiency evaluation
only to the extent supported by an authoritative,
scoped premise applicable to that evaluation context.

Shared factual or situated context alone
does not establish such authority.

Joint admissibility does not by itself imply
Group identity, membership, collective participation,
group Evidence, group sufficiency or group outcome.
```

H17 is falsifiable.

Do not implement architecture to make H17 true.

---

### 7. One new unresolved variable

Preserve the method:

```text
one new unresolved variable
per experiment
```

The new variable is:

```text
authority-bounded cross-subject evidence composition
```

Operationally observed through:

```text
joint admissibility
```

Keep constant, as far as possible, the Session 15 semantics:

```text
Evidence A
Evidence B
criterion K
unordered clues
neutral Evidence
same sufficiency semantics
same distinction between factual Evidence and derived claim
```

The primary new factual condition is:

```text
subjectRef(A) != subjectRef(B)
```

Do not simultaneously attempt to resolve:

* Group;
* membership;
* collective participation;
* participant/contributor ontology;
* ordered clues;
* solution recognition;
* incentive eligibility;
* TES Event recognition;
* TES Progression;
* TES Result;
* latency;
* ambiguity;
* conflict;
* actor assistance;
* validator semantics.

---

### 8. Critical semantic separation

The experiment must preserve three distinct stages:

```text
1. Evidence attribution
2. Joint admissibility
3. Sufficiency evaluation
```

Formally:

```text
Evidence attribution
≠
joint admissibility

joint admissibility
≠
sufficiency
```

Example:

```text
A@P1
B@P2
```

means only:

```text
Evidence A is attributed to P1
Evidence B is attributed to P2
```

It does not mean:

```text
P1 and P2 are a Group
```

It does not mean:

```text
A and B may be evaluated together
```

It does not mean:

```text
A+B satisfies K
```

These must remain separate claims.

---

### 9. Authoritative premise vs evaluation

Introduce, only as an experimental fixture, an explicit authoritative premise that may support joint admissibility.

Use a neutral term such as:

```text
Authoritative Premise
```

or another equally non-architectural fixture name if repository conventions require it.

Do not introduce:

```text
EvidenceCompositionAuthority
EvidenceAuthorityService
EvidenceSufficiencyAuthority
AuthorityRegistry
AuthorityProvider
AuthorityRepository
CollaborationService
```

The conceptual flow should remain:

```text
A@P1
B@P2

+
authoritative scoped premise

        ↓

joint admissibility

        ↓

K(A,B)

        ↓

possible SufficiencyClaim
```

Preserve:

```text
authority for joint admissibility
≠
sufficiency criterion
```

The authoritative premise must not be hidden inside K.

A test becoming green because K itself implicitly decides who may cooperate would be a failed experiment through authority laundering.

---

### 10. Do not encode cardinality assumptions

There is a future design pressure concerning the relationship between:

```text
authoritative admissibility premises
↔
evaluation contexts
```

Potential cardinality is:

```text
UNRESOLVED
```

Do not encode a semantic invariant such as:

```text
one authority premise
=
one evaluation
```

or:

```text
one evaluation
=
one authority premise
```

A fixture may necessarily use one concrete premise for one test case, but this must remain a fixture convenience.

Document explicitly:

```text
Session 17 does not establish
1:1, 1:N, N:1 or N:N cardinality
between authority premises
and evaluation contexts.
```

Do not create mappings, registries or generalized relationship schemas to solve this future problem.

---

### 11. Shared context is not semantic authority

The experiment must test explicitly that contextual facts do not acquire semantic authority merely because they are authoritative facts.

Candidate contextual relations include:

```text
same booking
same stay
same room
same property
same Treasure Hunt
shared objective
```

Treat them only as contextual facts.

For example:

```text
P1 and P2 belong to booking B17
```

may be an authoritative booking fact.

But:

```text
authoritative booking fact
≠
authority to establish joint Evidence admissibility
```

The semantic distinction is:

```text
authority over a fact
≠
authority over the consequence inferred from that fact
```

Do not call `same booking`, `same stay`, `same Hunt`, etc. "authorities".

They may later become factual conditions referenced by an authoritative product premise, but Session 17 must not assume such a rule.

---

### 12. Minimum experimental cases

Implement the smallest reversible experiment that can test H17.

At minimum, include the following cases.

#### Case A — Same-subject control

```text
A@P1
B@P1
```

Same relevant scope.

Expected:

```text
Session 15 behaviour remains reproducible.
```

This verifies that introducing subject distinction machinery has not broken the previous experiment.

Do not make cross-subject authority a requirement for same-subject Session 15 behaviour unless the repository structure forces a neutral equivalent and you can justify it.

---

#### Case B — Cross-subject with applicable authoritative premise

```text
A@P1
B@P2
P1 != P2
```

Applicable authoritative scoped premise allows these Evidence records to be jointly considered in the evaluation context.

Expected:

```text
joint admissibility
→ established
```

Then:

```text
K(A,B)
```

may be evaluated.

Given the unchanged Session 15 criterion:

```text
A AND (B OR C)
```

A+B should establish the same sufficiency level demonstrated in Session 15.

Important:

The experiment must demonstrate that sufficiency follows **after** admissibility.

Do not collapse the two.

---

#### Case C — Cross-subject without applicable authority

```text
A@P1
B@P2
P1 != P2
```

No applicable authoritative premise supports joint admissibility.

Expected:

```text
joint admissibility
→ cannot currently be established
```

Do not return a semantic equivalent of:

```text
forbidden
invalid collaboration
failure
subjects cannot cooperate
```

unless such a negative claim has an explicit authoritative basis, which is outside the current experiment.

Preserve:

```text
absence of authority
≠
prohibition
```

---

#### Case D — Wrong scope

```text
A@P1
B@P2
```

There is an authoritative premise, but it is valid for scope S2.

The evaluation is occurring in scope S1.

Expected:

```text
joint admissibility
→ cannot currently be established
```

This should demonstrate that presence of an authoritative premise is insufficient unless its scope applies.

---

#### Case E — Wrong subjects

```text
A@P1
B@P3
```

The fixture premise supports the relevant relation only for P1/P2 within the controlled experiment.

Expected:

```text
joint admissibility
→ cannot currently be established
```

Do not infer generalized membership or Group semantics from the fixture.

---

#### Case F — Shared context without semantic authority

Use:

```text
A@P1
B@P2
```

and at least one strong common contextual fact such as:

```text
same booking
```

Optionally, if technically trivial and without adding architecture:

```text
same stay
same property
same Hunt
```

But no applicable authoritative premise supports joint admissibility.

Expected:

```text
shared situated context
→ present

joint admissibility
→ cannot currently be established
```

This case is epistemically important.

It should falsify the shortcut:

```text
same booking
→ cooperative Evidence admissibility
```

without asserting the universal opposite:

```text
same booking
→ never relevant
```

---

### 13. Optional adversarial checks

Only add these if they remain trivial and do not expand the variable under investigation.

Potential checks:

##### Premise exists but does not cover this evaluation context

```text
authority exists
scope appears superficially related
but applicability is not established
```

Expected:

```text
undetermined / cannot establish
```

##### Extra Evidence does not strengthen authority

If:

```text
A@P1
B@P2
C@P2
```

but cross-subject joint admissibility is not established, the additional Evidence must not manufacture authority.

Preserve:

```text
more Evidence
≠
more semantic authority
```

Do not add this case if it requires a generalized aggregation engine.

---

### 14. Do not use Group

Do not introduce:

```text
Group
GroupId
GroupMembership
GroupParticipation
CollectiveParticipation
GroupEvidence
GroupEvidenceSet
GroupSufficiency
GroupOutcome
SharedParticipation
```

Do not introduce equivalent concepts under different names.

Preserve:

```text
multiple subjects
≠
Group
```

and:

```text
cross-subject joint admissibility
≠
Group
```

The experiment should succeed or fail without Group identity.

If implementation appears genuinely impossible without some persistent collective identity, STOP and document why rather than silently inventing a Group model.

That result would be important evidence.

---

### 15. Do not resolve participant vs contributor

For Session 17, use the smallest factual representation already available or minimally required:

```text
subjectRef
```

Do not determine whether `subjectRef` means:

* loyalty member;
* participant;
* contributor;
* account;
* device owner;
* booking owner;
* TES participant;
* ExperienceParticipation.

Preserve:

```text
participant identity
contributor identity
participant/contributor distinction

→ UNRESOLVED
```

Do not create `Participant` or `Contributor` entities solely for this experiment.

---

### 16. External actors are explicitly out of scope

Do not introduce:

* hotel employees;
* helpers;
* advisors;
* observers;
* validators;
* attestors;
* operators;
* external assistance.

A hotel employee giving a clue could causally influence participant behaviour without becoming an Evidence contributor.

That is a distinct future frontier.

Preserve:

```text
external assistance
≠
Evidence contribution
```

but do not attempt to operationally prove it in Session 17.

Record:

```text
external actor assistance / influence
→ UNRESOLVED
```

if useful in the report.

---

### 17. Sufficiency criterion remains unchanged

Reuse the smallest existing Session 15 criterion if possible:

```text
K = A AND (B OR C)
```

Do not generalize it into:

* rules engine;
* sufficiency DSL;
* policy engine;
* generic evaluator framework.

The purpose is not to improve the sufficiency model.

The purpose is to hold sufficiency semantics constant while changing the subject relationship.

---

### 18. Outcome representation remains experimental

Existing literals such as:

```text
established
not-established
```

or current equivalents remain experimental mechanisms.

Do not promote them to product-wide enums.

Preserve the semantic invariant:

```text
cannot currently establish
≠
failure
≠
false
≠
impossible
```

If current code forces an overly closed-world boolean result, document this as experimental friction rather than redesigning the whole architecture unless the minimum experiment genuinely requires a local reversible adjustment.

---

### 19. No semantic-product-contract redesign yet

The first cooperative experiment activates the review trigger for the Product Semantic Contract.

However:

```text
review trigger activated
≠
contract redesign required before experiment
```

Do not modify the Product Semantic Contract merely to encode:

* Group;
* participant;
* contributor;
* membership;
* collective participation.

Instead use the experiment to discover whether the contract actually requires a new distinction.

Candidate tension under observation:

```text
Evidence subject attribution
≠
scope in which Evidence may contribute
```

Do not promote this to an accepted invariant before evaluating the experiment.

---

### 20. Architectural guardrails

Do not build:

* Group domain model;
* GroupParticipation aggregate;
* ExperienceParticipation aggregate;
* EvidenceSet aggregate;
* membership service;
* participant registry;
* contribution registry;
* group evidence store;
* evidence aggregation engine;
* evidence composition engine;
* evidence sufficiency engine;
* generic rules engine;
* authority registry;
* authority provider;
* authority repository;
* Treasure Hunt Experience Definition;
* taxonomy;
* TES Event recognition;
* TES Sequence;
* TES Progression;
* TES Result;
* ordered clue model;
* partial incentive implementation;
* solution recognition component;
* provider/API architecture.

Do not add persistence unless the existing experiment already requires it.

Do not create architecture simply to obtain green tests.

---

### 21. Repository work

First inspect the repository and locate:

* Session 15 experiment;
* Session 16 consolidation;
* ADR-005;
* Architecture v0.5;
* relevant Evidence and contextual-evaluation code;
* existing tests and fixtures used by Session 15.

Prefer extension of the smallest existing experimental seam.

Do not refactor unrelated code.

Do not rename established architectural concepts unnecessarily.

Keep changes reversible and localized.

---

### 22. Falsification criteria

H17 is not automatically considered supported because the positive case works.

The experiment should be considered challenged or falsified if evidence shows, for example:

##### F1

Cross-subject Evidence can legitimately enter the same evaluation with no authoritative premise or equivalent basis whatsoever.

If this occurs, determine whether hidden authority is already embedded elsewhere before concluding H17 is false.

##### F2

Shared contextual facts alone necessarily produce joint admissibility.

Again inspect for hidden rules or authority laundering before interpreting this as evidence.

##### F3

Joint admissibility cannot be represented or evaluated without introducing a persistent collective identity.

If genuinely unavoidable:

```text
STOP
```

and document the reason.

Do not manufacture Group semantics.

##### F4

The sufficiency evaluator necessarily determines admissibility itself and cannot be separated without contradicting existing accepted architecture.

Document the contradiction.

Do not force an artificial separation solely to satisfy H17.

##### F5

Cross-subject Evidence requires a fundamentally new architectural responsibility not covered by ADR-005.

If supported by concrete evidence, document it as a candidate architectural finding.

Do not automatically create ADR-006.

---

### 23. Expected epistemic verdict

At the end, classify H17 as one of:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NOT SUPPORTED
FALSIFIED
```

Use the weakest classification justified by the evidence.

Do not promote experimental fixture shape into architecture.

---

### 24. Required report

Create:

`docs/experiments/session-17-authority-bounded-cross-subject-evidence-composition.md`

or use the repository's established Session documentation location if different.

The report must contain at least:

#### A. Repository inspection

What existing code, tests and documents were reused.

#### B. Hypothesis

Exact H17 tested.

#### C. Constants

What was held constant from Session 15.

#### D. New variable

```text
authority-bounded cross-subject evidence composition
```

and operational observation:

```text
joint admissibility
```

#### E. Minimal implementation

Explain what was added and, importantly, what was deliberately not added.

#### F. Test matrix

Include:

* same-subject control;
* authorized cross-subject;
* no-authority;
* wrong scope;
* wrong subjects;
* shared-context-without-authority.

For every case include:

```text
Evidence
subject attribution
situated context
applicable authoritative premise
joint-admissibility result
sufficiency evaluation attempted?
sufficiency result if attempted
```

#### G. Adversarial findings

Report any hidden coupling between:

* authority and K;
* subject attribution and participation;
* situated context and semantic authority;
* fixtures and architecture.

#### H. Falsification analysis

State explicitly whether any falsification criterion occurred.

#### I. Semantic findings

Evaluate whether evidence supports, challenges or leaves unresolved:

```text
evidence attribution
≠
joint admissibility

joint admissibility
≠
sufficiency

shared situated context
≠
semantic authority over joint admissibility

multiple subjects
≠
Group
```

Do not automatically label these architectural invariants.

#### J. Product Semantic Contract pressure

Evaluate whether Session 17 provides actual evidence that the Product Semantic Contract must distinguish any of:

```text
subject attribution
participation scope
participant
contributor
collective participation
Group
```

Classification options:

```text
NO CHANGE NEEDED
REVIEW WARRANTED
REFINEMENT CANDIDATE
INSUFFICIENT EVIDENCE
```

Do not edit the contract during Session 17 unless a genuine contradiction makes completion impossible.

#### K. Architecture impact

Evaluate:

```text
ADR-005
Architecture v0.5
need for new ADR
need for architecture revision
```

Do not presume modification.

#### L. Unresolved items

At minimum reassess:

```text
contribution identity
participant/contributor distinction
Group identity
membership
collective participation
group sufficiency
group outcome
authority accreditation
authority-premise/evaluation cardinality
external actor assistance
solution recognition
incentive eligibility
ordered clues
latency
ambiguity
conflict
TES Event recognition
```

#### M. Final verdict

Provide:

```text
H17 → ?

ADR-005 → ?

Architecture v0.5 → ?

Product Semantic Contract → ?

Group concept → ?

Recommended next experimental frontier → ?
```

---

### 25. Important interpretation rules

Do not interpret:

```text
no applicable authority
```

as:

```text
forbidden
```

Do not interpret:

```text
same booking
```

as:

```text
cooperative participation
```

Do not interpret:

```text
joint admissibility
```

as:

```text
Group
```

Do not interpret:

```text
A@P1 + B@P2 satisfies K
```

as:

```text
P1 and P2 jointly own the SufficiencyClaim
```

Beneficiary / subject / ownership of the eventual claim remains outside this experiment.

Do not interpret:

```text
subjectRef
```

as:

```text
participant ontology
```

Do not interpret:

```text
fixture authority premise
```

as:

```text
architectural authority component
```

---

### 26. STOP / NO-GO conditions

STOP rather than expand scope if:

* a Group model seems required;
* participant/contributor semantics must be resolved;
* external helpers become necessary;
* a generic policy engine appears necessary;
* TES Event recognition becomes necessary;
* the real API must be invented;
* the experiment requires broad architectural refactoring;
* existing accepted semantics genuinely contradict H17.

A valid result may be:

```text
INCONCLUSIVE
```

or:

```text
NO-GO
```

Those are preferable to architecture invented to preserve the hypothesis.

---

### 27. Desired experimental character

Keep the experiment:

```text
small
reversible
local
falsifiable
authority-aware
open-world
non-normative beyond its evidence
```

The goal is not to implement cooperative Treasure Hunt.

The goal is to discover whether:

```text
Evidence attributed to different subjects
can legitimately become premises
of the same derived sufficiency evaluation
without first constructing a collective actor.
```

Only after evidence exists should we decide whether concepts such as:

```text
participant
contributor
membership
collective participation
Group
```

belong in the Product Semantic Contract or architecture.

Proceed with repository inspection, minimal experiment, tests and report.
<!-- FIN-TEXTO-ORIGINAL-S17 -->

**Instrucción posterior de consolidación de la sesión 17:**

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-17-consolidacion-original.md) de `2026.zip`, registro `2026/09/03/rollout-2026-09-03T18-13-56-01a06843-4d71-7a32-bb84-9b332893cf6a.jsonl`. Mensaje de usuario en la línea 2033; salida(s) de lectura en la(s) línea(s) 2041, 2047. Cotejado con el recuento histórico de 1425 saltos de línea. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: e09d19b7f13d1841ea1449602890831b4b39f03879f60b24b25624b30358e024.

<!-- INICIO-TEXTO-ORIGINAL-S17-CONSOLIDACION -->
### Consolidación de la Sesión 17 — Composición de evidencia entre sujetos acotada por autoridad

Continúa el proyecto existente:

`Convercus Demo Factory / Convercus Experience Products`

Repositorio:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

No empieces desde cero.

Esta sesión es exclusivamente de **consolidación epistemológica y documental** de la Sesión 17.

No diseñes todavía la Sesión 18.

No añadas nueva arquitectura de producto.

No modifiques todavía el Contrato semántico de producto.

---

### 1. Propósito de la consolidación

La Sesión 17 experimentó la primera frontera cooperativa:

```text
authority-bounded cross-subject evidence composition
```

La operación observada fue:

```text
joint admissibility
```

A efectos de documentación en español, interpretar estos términos como:

```text
composición de evidencia entre sujetos acotada por autoridad

admisibilidad conjunta
```

La Sesión 17 produjo evidencia de que:

```text
atribución de Evidence
≠
admisibilidad conjunta

admisibilidad conjunta
≠
evaluación de suficiencia

contexto situado compartido
≠
autoridad para establecer admisibilidad conjunta

pluralidad de sujetos
≠
necesidad de Group
```

La consolidación debe determinar:

1. qué parte de esos resultados queda respaldada;
2. qué parte permanece local al experimento;
3. qué mecanismos experimentales no deben convertirse en semántica de producto;
4. qué presión real aparece sobre el Contrato semántico de producto;
5. cómo registrar futuras presiones semánticas sin resolverlas prematuramente;
6. qué preguntas deben permanecer abiertas antes de seleccionar la variable de la Sesión 18.

---

### 2. Línea de base vinculante

Mantener:

```text
ADR-001–005
→ ACCEPTED

Architecture v0.5
→ ACTIVE / unchanged
```

La Sesión 16 concluyó:

```text
ADR-006
→ NOT NEEDED

Architecture v0.6
→ NOT NEEDED
```

La Sesión 17 concluyó:

```text
H17
→ SUPPORTED WITH QUALIFICATION

ADR-005
→ ACCEPTED / unchanged

Architecture v0.5
→ ACTIVE / unchanged

new ADR
→ NOT NEEDED

architecture revision
→ NOT NEEDED

Product Semantic Contract
→ REVIEW WARRANTED / unchanged

Group
→ NOT REQUIRED BY THIS EXPERIMENT / UNRESOLVED
```

No reabras estas conclusiones salvo que la consolidación encuentre una contradicción material en la evidencia de la Sesión 17.

---

### 3. Alcance de la evidencia que debe consolidarse

La Sesión 17 mantuvo constante:

```text
K = A AND (B OR C)
```

y demostró experimentalmente:

```text
A@P1
B@P2
+
premisa autoritativa aplicable
        ↓
admisibilidad conjunta establecida
        ↓
K(A,B)
        ↓
suficiencia establecida
```

También demostró:

```text
A@P1
B@P2
+
contexto compartido
-
premisa autoritativa aplicable
        ↓
admisibilidad conjunta
no puede establecerse actualmente
```

Los controles incluyeron:

* ausencia de autoridad aplicable;
* ámbito incorrecto;
* sujetos incorrectos;
* misma reserva sin autoridad semántica;
* evidencia adicional sin autoridad suficiente.

Preservar:

```text
ausencia de autoridad suficiente
≠
prohibición

no puede establecerse actualmente
≠
falso
≠
imposible
≠
fracaso
```

---

### 4. Resultado central que debe consolidarse

Consolidar H17 como:

```text
SUPPORTED WITH QUALIFICATION
```

La cualificación principal es:

> La competencia de la premisa autoritativa se asumió por construcción dentro del artefacto experimental.

Por tanto, la Sesión 17 demuestra:

```text
una premisa autoritativa y aplicable
puede acotar legítimamente
la admisibilidad conjunta
de Evidence atribuida
a sujetos distintos
```

pero NO demuestra:

```text
cómo se origina esa autoridad
cómo se acredita
cómo se revoca
cómo se resuelven conflictos entre autoridades
cuántas evaluaciones puede gobernar
cuántas premisas puede requerir una evaluación
qué forma productiva debe adoptar
```

No promover:

```text
AuthoritativePremise
```

como componente de arquitectura.

---

### 5. Separación epistemológica consolidable

Evaluar y, si la evidencia lo permite, consolidar con alcance explícitamente experimental:

```text
atribución de Evidence
≠
admisibilidad conjunta
```

```text
admisibilidad conjunta
≠
suficiencia
```

```text
hecho contextual autoritativo
≠
autoridad sobre la consecuencia semántica inferida
```

Ejemplo:

```text
P1 y P2 pertenecen a la misma reserva
```

puede ser un hecho acreditado por una fuente competente.

Pero:

```text
sus Evidence pueden entrar juntas
en una evaluación de suficiencia
```

es una afirmación distinta que requiere autoridad adecuada para esa consecuencia.

Consolidar, por tanto:

```text
autoridad sobre un hecho
≠
autoridad sobre toda inferencia
derivada de ese hecho
```

Tratar esta formulación como consecuencia analítica de ADR-005, no como nuevo ADR.

---

### 6. Pluralidad de sujetos y Group

La Sesión 17 logró ejecutar la frontera cooperativa sin:

* identidad colectiva;
* membership;
* persistencia colectiva;
* Evidence colectiva;
* suficiencia colectiva;
* outcome colectivo.

Consolidar únicamente:

```text
Group
→ NOT REQUIRED BY H17
```

Mantener:

```text
Group
→ UNRESOLVED
```

No concluir:

```text
Group is unnecessary
```

en términos generales.

La evidencia solo permite afirmar:

> La identidad colectiva no es necesaria para resolver el problema específico de admisibilidad conjunta estudiado en la Sesión 17.

No promover:

* Group;
* GroupParticipation;
* collective participation;
* membership;
* collective Evidence;
* collective outcome.

---

### 7. Vigilancia crítica 1 — ubicación de `bookingRef`

Prestar especial atención a este punto.

La implementación experimental añadió:

```text
bookingRef
```

dentro de:

```text
CrossSubjectMarkerEvidence
```

Esto NO debe consolidarse como semántica de Evidence.

La cuestión permanece abierta:

```text
¿la relación con una reserva
es un hecho intrínseco
sobre la propia Evidence?

o

¿es una relación contextual
utilizada cuando esa Evidence
se evalúa en un ámbito determinado?
```

La Sesión 17 no resolvió esta cuestión.

Clasificar:

```text
bookingRef placement
→ EXPERIMENTAL
→ NOT PROMOTED
→ UNRESOLVED
```

La consolidación debe impedir explícitamente que futuras sesiones interpreten:

```text
CrossSubjectMarkerEvidence.bookingRef
```

como contrato semántico de producto.

Preservar conceptualmente:

```text
Evidence A@P1
Evidence B@P2

+

relaciones contextuales situadas

+

premisas autoritativas aplicables
```

sin decidir todavía dónde debe residir estructuralmente la relación con reserva, estancia, propiedad o escenario.

No refactorizar código durante esta consolidación salvo que exista una contradicción material.

---

### 8. Vigilancia crítica 2 — control de sujeto único

La Sesión 17 utilizó:

```text
A@P1
B@P1
```

como control de regresión para demostrar que la extracción de la evaluación K no rompía el comportamiento de la Sesión 15.

Este control NO demuestra:

```text
mismo sujeto
→ Evidence siempre conjuntamente admisible
```

La ausencia de una premisa de admisibilidad entre sujetos en ese control significa únicamente:

> La Sesión 17 no introduce retroactivamente un nuevo requisito de cooperación en el experimento de sujeto único de la Sesión 15.

Consolidar expresamente:

```text
same-subject control
→ regression control only
```

No promover:

```text
same subject
→ automatic admissibility
```

como regla de producto.

La admisibilidad general de Evidence perteneciente al mismo sujeto NO fue la variable estudiada.

Mantener esa cuestión fuera del alcance de la consolidación.

---

### 9. Vigilancia crítica 3 — forma de `AuthoritativePremise`

La implementación utilizó experimentalmente:

```text
AuthoritativePremise
```

con elementos como:

```text
identity
provenance
scope
covered subjects
```

Todo ello permanece como:

```text
PROVISIONAL EXPERIMENTAL SHAPE
NOT PROMOTED
```

En particular:

```text
coveredSubjects
```

no debe convertirse en:

```text
general semantic model
for cooperative authority
```

La autorización futura podría depender de relaciones, condiciones, delegación, invitación, pertenencia contextual u otros mecanismos todavía desconocidos.

No asumir:

```text
premisa autoritativa
=
lista explícita de sujetos autorizados
```

Preservar:

```text
authority accreditation
→ UNRESOLVED

authority revocation
→ UNRESOLVED

authority conflict
→ UNRESOLVED

authority-premise/evaluation cardinality
→ UNRESOLVED
```

---

### 10. Cardinalidad entre premisas y evaluaciones

La Sesión 17 utilizó una única premisa opcional por conveniencia experimental.

Esto no demuestra:

```text
1:1
1:N
N:1
N:N
```

entre:

```text
premisas autoritativas
↔
contextos de evaluación
```

Consolidar explícitamente:

```text
cardinality
→ UNRESOLVED
```

No permitir que la forma de la función experimental sea citada posteriormente como evidencia de cardinalidad semántica.

---

### 11. Presión sobre el Contrato semántico de producto

La Sesión 16 activó el disparador de revisión:

```text
primer experimento cooperativo
→ revisión del Contrato semántico de producto
```

La Sesión 17 ya constituye ese primer experimento.

Por tanto:

```text
trigger
→ REACHED
```

y:

```text
Product Semantic Contract
→ REVIEW NOW
```

La consolidación NO debe modificar todavía el contrato.

Debe identificar formalmente la presión observada.

La presión actualmente respaldada es:

```text
atribución del sujeto de Evidence
≠
ámbito en el que esa Evidence
puede participar en una evaluación
```

La Sesión 17 demostró que:

```text
A@P1
B@P2
```

pueden conservar sus atribuciones individuales y, bajo autoridad competente, participar en una misma evaluación.

Por tanto, queda tensionada cualquier simplificación equivalente a:

```text
un sujeto
=
un ámbito de participación
=
un ámbito de evaluación
```

No concluir todavía cuál debe ser la solución.

---

### 12. No elegir aún la solución semántica

La consolidación NO debe promover:

```text
ParticipationScope
EvaluationScope
ContributionScope
CollectiveParticipation
Collaboration
Group
Membership
```

ni equivalentes.

El hecho observado es anterior a la solución conceptual.

La consolidación debe distinguir:

```text
presión observada
```

de:

```text
concepto que eventualmente
podría resolver esa presión
```

Preservar el método:

```text
evidencia
→ presión semántica
→ revisión
→ hipótesis
→ experimento
→ eventual promoción
```

No:

```text
evidencia
→ nuevo concepto
→ arquitectura
```

---

### 13. Crear un registro de presiones semánticas

A partir de esta consolidación, crear o introducir en la documentación un mecanismo ligero de seguimiento denominado:

```text
Registro de presiones sobre el Contrato semántico de producto
```

No convertirlo en componente de software.

No crear repositorio técnico, servicio, esquema de persistencia ni API.

Debe ser únicamente una disciplina documental.

Cada presión registrada debe contener como mínimo:

```text
Identificador
Fuente experimental
Distinción observada
Evidencia disponible
Autoridad afectada
Estado epistemológico
Qué NO demuestra
Preguntas abiertas
Riesgo de promoción prematura
Condición para nueva experimentación
Condición para posible refinamiento del contrato
```

Para la presión surgida en Sesión 17, registrar algo equivalente a:

```text
PSC-P01
```

con:

```text
Fuente:
Session 17

Presión:
atribución del sujeto de Evidence
≠
ámbito de contribución/evaluación

Evidencia:
Evidence atribuida a P1 y P2
puede entrar en una misma evaluación
sin borrar las atribuciones individuales
y sin crear Group.

Estado:
SUPPORTED WITH QUALIFICATION
como presión observada.

No demuestra:
qué es ParticipationScope;
qué es EvaluationScope;
que deba existir Group;
que deba existir CollectiveParticipation;
que participant y contributor sean entidades distintas;
quién es el sujeto del claim;
quién es beneficiario de consecuencias posteriores.

Condición de futura promoción:
evidencia adicional que demuestre
que el contrato actual no puede expresar
correctamente un comportamiento necesario
sin introducir una nueva distinción semántica.
```

---

### 14. El registro debe prepararse para nuevas presiones

No asumir que PSC-P01 será la única tensión.

El registro debe poder recibir futuras presiones provenientes de:

* cooperación;
* ayuda externa;
* contributor frente a participant;
* identidad de contribución;
* claim derivado;
* ámbito del claim;
* solución reconocida;
* incentivos;
* orden y dependencia entre pistas;
* latencia;
* ambigüedad;
* conflicto;
* autoridad;
* posible participación colectiva;
* futuras diferencias entre Experience Definition y realización de producto.

Pero no registrar como presión confirmada una cuestión que todavía solo sea una posibilidad.

Distinguir:

```text
presión observada
```

de:

```text
frontera potencial futura
```

---

### 15. Evitar acumulación silenciosa de presión semántica

La finalidad del registro es impedir este patrón:

```text
experimento n
→ pequeña excepción local

experimento n+1
→ otra excepción local

experimento n+2
→ otra excepción local

        ↓

contrato semántico implícitamente obsoleto
sin decisión explícita
```

En su lugar:

```text
nueva evidencia
        ↓
¿presiona al contrato?
        ↓
sí
        ↓
registrar presión
        ↓
acumular evidencia
        ↓
revisión explícita
        ↓
mantener / refinar / rechazar
```

La consolidación debe indicar que una presión acumulada no modifica por sí sola el contrato.

---

### 16. Umbral para modificar el Contrato semántico de producto

No establecer un umbral numérico.

Definir un criterio epistemológico.

Una modificación del contrato debería considerarse cuando exista evidencia suficiente de que:

```text
1. una distinción semántica es necesaria
para representar correctamente
comportamientos de producto legítimos;

2. la distinción no puede permanecer
como simple detalle de Scenario;

3. no es únicamente consecuencia
de un artefacto experimental;

4. su ausencia produce ambigüedad,
contradicción o pérdida semántica recurrente;

5. existe suficiente evidencia
para definir la distinción
sin inventar ontología adicional.
```

No modificar el contrato simplemente porque:

```text
un experimento utiliza una nueva propiedad
```

o:

```text
dos sesiones encuentran la misma palabra útil
```

---

### 17. Diferenciar presión semántica y presión arquitectónica

La consolidación debe preservar:

```text
presión sobre el Contrato semántico de producto
≠
necesidad de nueva arquitectura
```

La Sesión 17 es ejemplo de ello:

```text
presión semántica
→ sí

nueva responsabilidad arquitectónica
→ no demostrada
```

Por tanto:

```text
ADR-005
→ ACCEPTED / unchanged

Architecture v0.5
→ ACTIVE / unchanged
```

La revisión del contrato no debe provocar automáticamente:

* nuevo ADR;
* nueva capa;
* nuevo agregado;
* nuevo servicio;
* nueva persistencia.

---

### 18. No promover aún una entidad colectiva

Mantener:

```text
Group identity
→ UNRESOLVED

membership
→ UNRESOLVED

collective participation
→ UNRESOLVED

group Evidence
→ UNRESOLVED

group sufficiency
→ UNRESOLVED

group outcome
→ UNRESOLVED
```

La presión sobre el contrato NO debe resolverse mediante Group por defecto.

Preservar:

```text
evaluación compartida
≠
sujeto colectivo demostrado
```

---

### 19. No resolver aún el sujeto del claim

La Sesión 17 produjo una nueva cuestión:

```text
cuando A@P1 y B@P2
son conjuntamente admisibles
y K establece suficiencia,

¿de qué o de quién habla
la afirmación derivada?
```

No resolverla en esta consolidación.

Registrar separadamente:

```text
claim subject / referent
→ UNRESOLVED
```

En español:

```text
sujeto o referente
de la afirmación derivada
→ NO RESUELTO
```

No identificar automáticamente:

```text
sujeto del claim
=
P1
```

ni:

```text
=
P2
```

ni:

```text
=
P1 + P2
```

ni:

```text
=
Group
```

ni:

```text
=
beneficiary
```

---

### 20. Separar sujeto del claim, ámbito y beneficiario

Registrar como fronteras distintas:

```text
sujeto/referente de la afirmación
≠
ámbito de la afirmación
≠
beneficiario de una consecuencia posterior
```

No usar `beneficiary` como nombre de la siguiente frontera experimental.

En español:

```text
beneficiario
```

debe reservarse para consecuencias posteriores, potencialmente relacionadas con:

* incentivo;
* recompensa;
* elegibilidad;
* derecho;
* resultado comercial.

Estas materias permanecen fuera de la consolidación.

---

### 21. No seleccionar todavía la Sesión 18

La consolidación debe terminar sin diseñar la Sesión 18.

Debe dejar candidatas separadas, como mínimo:

```text
A. sujeto/referente de la afirmación derivada

B. ámbito de la afirmación derivada

C. participant/contributor distinction

D. external actor assistance

E. authority accreditation

F. authority conflict / multiple premises
```

No decidir todavía cuál será la siguiente.

La decisión debe tomarse después de revisar:

```text
PSC-P01
```

y el Contrato semántico de producto actual.

---

### 22. Revisión del Contrato semántico de producto

Durante esta consolidación:

1. localizar el Contrato semántico de producto vigente;
2. identificar exactamente qué formulaciones presuponen o favorecen una perspectiva individual;
3. comparar esas formulaciones con la evidencia de Sesión 17;
4. NO editar el contrato;
5. documentar la tensión con referencias concretas;
6. indicar si la evidencia actual produce:

```text
NO PRESSURE

OBSERVED PRESSURE

REFINEMENT CANDIDATE

CONTRADICTION
```

La clasificación esperable, salvo evidencia contraria, es:

```text
OBSERVED PRESSURE
```

No elevar a:

```text
REFINEMENT CANDIDATE
```

solo porque se haya activado la revisión.

---

### 23. Criterio para `REFINEMENT CANDIDATE`

Solo clasificar una presión como:

```text
REFINEMENT CANDIDATE
```

cuando exista evidencia suficiente para sostener:

> El contrato necesita una nueva distinción semántica concreta y existe evidencia suficiente para expresar esa distinción sin inventar significado adicional.

Actualmente Sesión 17 demuestra una tensión, pero no determina todavía si la solución es:

* nuevo concepto;
* nueva relación;
* nuevo ámbito;
* nueva cualificación de participación;
* o ninguna nueva entidad.

Por tanto, evitar promoción prematura.

---

### 24. Documento de consolidación requerido

Crear:

`docs/experiments/session-17-consolidation-authority-bounded-cross-subject-evidence-composition.md`

o la ubicación equivalente establecida por el repositorio.

El documento debe incluir:

#### A. Veredicto sobre H17

```text
H17
→ SUPPORTED WITH QUALIFICATION
```

con explicación de la cualificación.

#### B. Evidencia consolidada

Qué separaciones quedan respaldadas y con qué alcance.

#### C. Qué NO demuestra Sesión 17

Enumerar explícitamente las inferencias no autorizadas.

#### D. Cuarentena de artefactos experimentales

Como mínimo:

```text
AuthoritativePremise
coveredSubjects
bookingRef placement
single optional premise
outcome literals
cross-subject fixture shapes
```

Clasificarlos como:

```text
NOT PROMOTED
```

o:

```text
UNRESOLVED
```

según corresponda.

#### E. Control de sujeto único

Explicar que:

```text
A@P1 + B@P1
```

fue un control de regresión y no evidencia de admisibilidad universal intra-sujeto.

#### F. Relación con ADR-005

Determinar si la Sesión 17:

* contradice;
* extiende evidencia;
* requiere nueva responsabilidad.

Resultado esperado si no surge contradicción:

```text
supporting evidence for ADR-005
```

#### G. Impacto arquitectónico

Evaluar:

```text
ADR-005
Architecture v0.5
nuevo ADR
nueva versión arquitectónica
```

#### H. Revisión del Contrato semántico de producto

Citar las formulaciones actuales relevantes y describir la presión observada.

No modificar el contrato.

#### I. Registro de presiones semánticas

Crear o actualizar el registro e introducir:

```text
PSC-P01
```

#### J. Fronteras que permanecen abiertas

Incluir:

```text
contribution identity
participant/contributor distinction
claim subject/referent
claim scope
Group identity
membership
collective participation
authority accreditation
authority revocation
authority conflict
authority-premise/evaluation cardinality
external actor assistance
solution recognition
incentive eligibility
ordered/enabling clues
latency
ambiguity
identity confusion
TES Event recognition
real API contracts
```

Cuando el término disponga de equivalente español estable en el documento, utilizarlo.

Los nombres de tipos o identificadores de código pueden conservarse literalmente.

#### K. Candidatas a siguiente frontera

Enumerarlas sin seleccionar una.

#### L. Veredicto final

Incluir:

```text
H17 → ?

ADR-005 → ?

Architecture v0.5 → ?

new ADR → ?

architecture revision → ?

Product Semantic Contract → ?

PSC-P01 → ?

Group → ?

bookingRef placement → ?

same-subject control interpretation → ?

Recommended immediate next action → ?
```

---

### 25. Veredicto esperado salvo contradicción

Si la inspección no descubre evidencia nueva que contradiga el informe de Sesión 17, la consolidación debería aproximarse a:

```text
H17
→ SUPPORTED WITH QUALIFICATION

ADR-005
→ ACCEPTED / unchanged

Architecture v0.5
→ ACTIVE / unchanged

new ADR
→ NOT NEEDED

architecture revision
→ NOT NEEDED

Product Semantic Contract
→ REVIEWED / OBSERVED PRESSURE / unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE

Group
→ NOT REQUIRED BY H17 / UNRESOLVED

bookingRef placement
→ EXPERIMENTAL / NOT PROMOTED / UNRESOLVED

same-subject control
→ REGRESSION CONTROL ONLY

AuthoritativePremise shape
→ EXPERIMENTAL / NOT PROMOTED
```

No fuerces estos resultados si la evidencia contradice alguno.

---

### 26. Prohibiciones

No construir:

* Group;
* ParticipationScope;
* EvaluationScope;
* CollectiveParticipation;
* Contributor;
* Participant;
* authority service;
* authority registry;
* semantic-pressure registry como software;
* new aggregate;
* persistence;
* API;
* TES Event recognition;
* incentive model;
* solution recognition.

No modificar:

* ADR-005;
* Architecture v0.5;
* Product Semantic Contract;

salvo contradicción explícita y documentada.

Si aparece una contradicción:

```text
STOP
```

y documentarla.

---

### 27. Resultado metodológico buscado

La consolidación debe dejar el proyecto preparado para que futuras sesiones puedan distinguir:

```text
nuevo hallazgo experimental
```

de:

```text
nueva presión semántica
```

de:

```text
necesidad de refinar
el Contrato semántico de producto
```

de:

```text
necesidad de nueva arquitectura
```

Preservar siempre:

```text
hallazgo
≠
promoción
```

```text
presión
≠
refinamiento
```

```text
refinamiento semántico
≠
arquitectura nueva
```

La finalidad de la consolidación no es cerrar las preguntas cooperativas.

Es evitar que las próximas respuestas locales degraden silenciosamente la coherencia semántica global del producto.

Procede con inspección, consolidación documental y registro de la primera presión semántica observada.
<!-- FIN-TEXTO-ORIGINAL-S17-CONSOLIDACION -->

---

<a id="sesion-18"></a>

## Capítulo 18 — Validez contextual del claim derivado

**Texto original pendiente de recuperación.**

No se ha localizado la instrucción principal de esta sesión entre los mensajes y las lecturas de adjuntos de los 18 registros aportados en `2026.zip`. Las referencias a esta sesión y sus informes de ejecución no sustituyen el prompt original. No se reconstruye ni se presenta como recuperado.

---

<a id="sesion-19"></a>

## Capítulo 19 — Preparación para la primera demo vertical

**Texto original pendiente de recuperación.**

No se ha localizado la instrucción principal de esta sesión entre los mensajes y las lecturas de adjuntos de los 18 registros aportados en `2026.zip`. Las referencias a esta sesión y sus informes de ejecución no sustituyen el prompt original. No se reconstruye ni se presenta como recuperado.

---

<a id="sesion-20"></a>

## Capítulo 20 — Construir y corregir Aventura Familiar

**Estado: recuperación parcial de la sesión.** Se conserva íntegra una instrucción posterior de corrección, no el prompt de apertura. Tampoco se ha recuperado la especificación de continuidad previa a la que esta corrección remite. La checklist exacta de 22 transiciones sí aparece en la [instrucción de cierre y apertura de la sesión 21](#sesion-21).

El mismo adjunto de corrección se envió dos veces con idéntico contenido; se transcribe una sola vez. Esta sesión no se contabiliza entre las 35 instrucciones principales recuperadas.

**Corrección posterior recuperada:**

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-20-continuacion-original.md) de `2026.zip`, registro `2026/09/08/rollout-2026-09-08T09-46-18-01a08032-5aa5-7063-ac04-0df7be912ee5.jsonl`. Mensaje de usuario en la línea 58; salida(s) de lectura en la(s) línea(s) 64. Cotejo adicional: adjunto repetido. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 949718de8780a13e01693736eb2b721a98ea0e16c6bf51923e9750484f07932b.

<!-- INICIO-TEXTO-ORIGINAL-S20-CONTINUACION -->
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
<!-- FIN-TEXTO-ORIGINAL-S20-CONTINUACION -->

---

<a id="sesion-21"></a>

## Capítulo 21 — Falsar la reutilización de composición

**Estado:** instrucción principal íntegra recuperada del historial.

Esta instrucción incluye el cierre de la sesión 20 y la formulación/auditoría de H21. A continuación se conserva también la instrucción posterior de ejecución de H21.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-21-original.md) de `2026.zip`, registro `2026/09/08/rollout-2026-09-08T09-46-18-01a08032-5aa5-7063-ac04-0df7be912ee5.jsonl`. Mensaje de usuario en la línea 406; salida(s) de lectura en la(s) línea(s) 413. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 306cad76c3652ce00f72de47d9e3eacfc3da08bd4653394a79c81e2d047c7fd8.

<!-- INICIO-TEXTO-ORIGINAL-S21 -->
He revisado tu informe `session-20-first-family-adventure-vertical.md` v1.2 y tu propuesta posterior de crear una segunda demo.

La dirección de utilizar una segunda demo es válida, pero antes quiero cerrar formalmente Sesión 20 y después utilizar esa segunda composición como un **experimento arquitectónico**, no simplemente como white-labeling.

#### 1. Cierre de Sesión 20

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

#### 2. Después, no implementes inmediatamente la segunda demo

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

#### 3. Conserva especialmente esta separación

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

#### 4. Después del audit, formula H21

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

#### 5. La segunda demo será el falsador de H21

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

#### 6. Condición experimental fuerte

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

#### 7. Todavía no construyas el catálogo/selector

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

#### 8. Salida que quiero antes de una refactorización

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
<!-- FIN-TEXTO-ORIGINAL-S21 -->

**Instrucción posterior de ejecución de H21:**

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-21-continuacion-original.md) de `2026.zip`, registro `2026/09/08/rollout-2026-09-08T09-46-18-01a08032-5aa5-7063-ac04-0df7be912ee5.jsonl`. Mensaje de usuario en la línea 489; salida(s) de lectura en la(s) línea(s) 496. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: de0d8276e297a59f2b8029080a853ef4d2e9da1fb8ee73dbe7f1b346b0ef8f85.

<!-- INICIO-TEXTO-ORIGINAL-S21-CONTINUACION -->
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

#### 1. Preserva la baseline congelada

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

#### 2. Construye Composition B únicamente mediante las superficies permitidas en el protocolo

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

#### 3. Ejecuta el ensayo incrementalmente

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

#### 4. STOP en el primer falsador arquitectónico material

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

#### 5. No intentes demostrar todos L1–L5 en una sola ejecución

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

#### 6. Clasifica H21

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

#### 7. Preserva las distinciones arquitectónicas

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

#### 8. Actualiza el informe de Sesión 21

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

#### 9. No selecciones ni implementes H22

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
<!-- FIN-TEXTO-ORIGINAL-S21-CONTINUACION -->

---

<a id="sesion-22"></a>

## Capítulo 22 — Selección estable por Experience

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-22-original.md) de `2026.zip`, registro `2026/09/08/rollout-2026-09-08T09-46-18-01a08032-5aa5-7063-ac04-0df7be912ee5.jsonl`. Mensaje de usuario en la línea 599; salida(s) de lectura en la(s) línea(s) 606. Cotejo adicional: lectura cat frente a lectura segmentada. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 04c5fb0fbfde8e5e01b5893031cd059d65a5e437ae176af10ef607552191e29d.

<!-- INICIO-TEXTO-ORIGINAL-S22 -->
Abre la Sesión 22 a partir de los resultados consolidados de H21.

No intentes todavía completar Composition B ni reparar todos los leaks observados.

#### 1. Línea de base

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

#### 2. Hallazgo de H21 que gobierna esta sesión

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

#### 3. Hipótesis H22

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

#### 4. Inspección previa mínima

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

#### 5. Delta permitido

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

#### 6. Componentes que permanecen congelados

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

#### 7. Controles positivos

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

#### 8. Controles negativos obligatorios

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

#### 9. Comprueba también L2b

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

#### 10. Si es observable, continúa únicamente para verificar selección

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

#### 11. Tratamiento de L1/L3/L4/L5 si aparecen

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

#### 12. STOP de H22

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

#### 13. Veredicto H22

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

#### 14. Verificación

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

#### 15. Documentación

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

#### 16. Guardas finales

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
<!-- FIN-TEXTO-ORIGINAL-S22 -->

---

<a id="sesion-23"></a>

## Capítulo 23 — Transporte del contexto situado a evaluación

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-23-original.md) de `2026.zip`, registro `2026/09/08/rollout-2026-09-08T09-46-18-01a08032-5aa5-7063-ac04-0df7be912ee5.jsonl`. Mensaje de usuario en la línea 718; salida(s) de lectura en la(s) línea(s) 725. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: b075a06a141f69f34626d858c7bbdc554b32b46ccca1156e461952d16b17a951.

<!-- INICIO-TEXTO-ORIGINAL-S23 -->
Abre la Sesión 23 a partir del resultado consolidado de H22.

No corrijas todavía L3, L4 ni L5.

#### 1. Línea de base

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

#### 2. Presión seleccionada

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

#### 3. Guarda epistemológica obligatoria

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

#### 4. H23

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

#### 5. Inspección previa

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

#### 6. Selección de la fuente experimental

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

#### 7. Delta permitido

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

#### 8. Control positivo A

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

#### 9. Control positivo B

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

#### 10. Control de separación A/B

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

#### 11. Control adversarial de incoherencia

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

#### 12. Premisa autoritativa

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

#### 13. H23 no estudia copy

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

#### 14. Falsadores H23

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

#### 15. Resultado esperado si H23 se sostiene

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

#### 16. Verificación

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

#### 17. Informe

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

#### 18. Guardas

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
<!-- FIN-TEXTO-ORIGINAL-S23 -->

---

<a id="sesion-24"></a>

## Capítulo 24 — Buscar una fuente existente para Activity situada

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-24-original.md) de `2026.zip`, registro `2026/09/14/rollout-2026-09-14T13-17-09-01a09fd9-8978-7280-9a36-812ea094c412.jsonl`. Mensaje de usuario en la línea 9; salida(s) de lectura en la(s) línea(s) 15. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: c396e0b646f33cc45102e06faefa52849ae7ef9a1c60f1ba66c21b308988f9c9.

<!-- INICIO-TEXTO-ORIGINAL-S24 -->
Abre la Sesión 24 a partir del resultado consolidado de H23.

La presión seleccionada es exclusivamente **L5 — procedencia de la representación situada de Activity**.

No corrijas L3 ni L4.

#### 1. Línea de base

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

#### 2. Presión seleccionada

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

#### 3. H24

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

#### 4. Inspección previa obligatoria

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

#### 5. Guarda semántica

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

#### 6. Fuente candidata

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

#### 7. Delta permitido

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

#### 8. Controles A y B

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

#### 9. Invariantes factuales

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

#### 10. Control adversarial de independencia representación/hecho

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

#### 11. Control de ausencia

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

#### 12. L3 y L4 permanecen fuera de alcance

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

#### 13. Falsadores H24

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

#### 14. Veredicto positivo

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

#### 15. Verificación

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

#### 16. Informe

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

#### 17. Guardas finales

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
<!-- FIN-TEXTO-ORIGINAL-S24 -->

---

<a id="sesion-25"></a>

## Capítulo 25 — Declaración explícita de Activity por paso

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-25-original.md) de `2026.zip`, registro `2026/09/14/rollout-2026-09-14T13-17-09-01a09fd9-8978-7280-9a36-812ea094c412.jsonl`. Mensaje de usuario en la línea 101; salida(s) de lectura en la(s) línea(s) 107. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: a281b05665effa84ce9661856b348780d618283b2b1319d685508212138cc0ec.

<!-- INICIO-TEXTO-ORIGINAL-S25 -->
Abre la Sesión 25 a partir del resultado consolidado de H24.

H24 queda falsificada. No intentes reescribirla después de introducir una relación nueva.

#### 1. Baseline

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

#### 2. Consecuencia que autoriza esta sesión

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

#### 3. H25

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

#### 4. Distinción obligatoria dentro de DemoScript

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

#### 5. Shape experimental mínima

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

#### 6. Fuente de autoridad

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

#### 7. Threading técnico

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

#### 8. Runtime semantics

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

#### 9. A control

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

#### 10. B control

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

#### 11. Control crítico: declaration != occurrence

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

#### 12. Control crítico: representation independence

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

#### 13. Control inverso: representation cannot force fact

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

#### 14. Absence control

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

#### 15. No inferir representación

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

#### 16. No amplíes todavía el problema a dónde debe vivir Activity finalmente

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

#### 17. Arrival / generic Activity regression

Hospitality Arrival y cualquier otro consumidor existente de Activity deben conservar su comportamiento.

No obligar a otras Experiences a adoptar `activityPresentation` para hacer pasar H25.

La recurrencia fuera de Family Adventure no se presupone.

Si el cambio obliga a reformular Activity globalmente:

```text
STOP
```

y registra la presión.

---

#### 18. L3 permanece congelado

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

#### 19. L4 permanece congelado

No modificar `App.tsx` para adaptar B.

Mantener:

```text
L4
→ SOURCE-INSPECTION FINDING
→ OUT OF SCOPE
```

Activity puede verificarse mediante snapshot público.

---

#### 20. Falsadores H25

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

#### 21. Veredicto positivo

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

#### 22. Verificación

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

#### 23. Informe

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

#### 24. Artifact quarantine

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

#### 25. Guardas finales

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
<!-- FIN-TEXTO-ORIGINAL-S25 -->

---

<a id="sesion-26"></a>

## Capítulo 26 — Auditar GuestPerspective sin relaciones nuevas

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-26-original.md) de `2026.zip`, registro `2026/09/14/rollout-2026-09-14T13-17-09-01a09fd9-8978-7280-9a36-812ea094c412.jsonl`. Mensaje de usuario en la línea 193; salida(s) de lectura en la(s) línea(s) 199. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: d4458858033c162bf111f4eb70b560858596ee21b8856ef9e517f5db770ed1f0.

<!-- INICIO-TEXTO-ORIGINAL-S26 -->
Abre la Sesión 26 a partir del resultado consolidado de H25.

No corrijas todavía App.tsx/L4.

#### 1. Baseline

Mantener:

```text
SESSION 20 → CLOSED

H21 → FALSIFIED
       historical baseline

H22 → SUPPORTED WITH QUALIFICATION
       Experience-based behavior selection

H23 → SUPPORTED WITH QUALIFICATION
       situated evaluation context binding

H24 → FALSIFIED
       no legitimate existing Activity
       representation source

H25 → SUPPORTED WITH QUALIFICATION
       script-bound Activity representation

L1 → experimentally addressed
L2a/L2b → experimentally addressed
L5 → SCRIPT-BOUND SITUATED REPRESENTATION
     EXECUTION-VERIFIED within A/B

L3 → EXECUTION-CONFIRMED / OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN
```

Mantener:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

No reescribir H24 después del resultado positivo de H25.

---

#### 2. Presión seleccionada

Seleccionar únicamente:

```text
L3 — GuestPerspective situated content provenance
```

No tratar L3 como un simple problema de copy.

Descomponer durante la inspección, como mínimo:

```text
L3a
→ session/account display provenance

L3b
→ subject display provenance

L3c
→ situated journey/status narrative provenance
```

Esta división es diagnóstica y experimental.

No promover todavía L3a/L3b/L3c a arquitectura.

---

#### 3. H26

```text
H26 — Situated Guest Perspective Provenance
```

Hipótesis falsable:

```text
Dentro del recorrido Family Adventure,
la Guest Perspective puede producir una
representación situada coherente para
las composiciones A y B combinando
estado/hechos/evaluación derivados con
datos presentacionales ya disponibles
en la composición resuelta,

sin hardcodes específicos de A,
sin inferir identidad de sujeto a partir
de la cuenta/sesión y sin reutilizar
Activity representation como autoridad
narrativa general.
```

H26 exige inicialmente utilizar sólo relaciones ya existentes.

No introducir una nueva shape para salvar la hipótesis.

---

#### 4. Provenance audit previo obligatorio

Antes de cambiar código, inventariar todos los campos y textos de:

```text
GuestPerspectiveReadModel
projectGuestPerspective()
App consumption of guestPerspective
```

Para cada salida indicar:

```text
OUTPUT FIELD / TEXT

CURRENT SOURCE

CURRENT TRANSFORMATION

CURRENT HARDCODE

EXPECTED RESPONSIBILITY

CANDIDATE EXISTING SOURCE

FACTUAL?
OPERATIONAL?
DERIVED?
ACCOUNT PRESENTATION?
SUBJECT PRESENTATION?
SITUATED NARRATIVE?
```

Inspeccionar como candidatos existentes:

```text
BrandArtifact
ExperienceDefinition
DemoFixture.member
ScenarioDefinition.subjects
ScenarioDefinition.contexts
operationalSessionSubjectRef
DemoScript.presenterLabel
DemoScript.activityPresentation
runtime subjectStates
runtime Evidence
vertical evaluation
resolved DemoRuntime
```

No asumir que todos son fuentes legítimas.

---

#### 5. Guarda account/session vs subject

Preservar:

```text
fixture member/account
!=
Experience subject
```

```text
operational session
!=
Evidence subjectRef
```

```text
displaying "Cuenta de Inés"
!=
asserting subject-p1 = account member
```

```text
represented subject
!=
authentication identity
```

No añadir automáticamente una relación:

```text
memberId → subjectRef
```

para hacer pasar H26.

No introducir:

```text
Actor
Operator
Representative
Participant
Contributor
AccountSubject
```

o equivalentes.

Si una representación requerida exige conocer una relación entre cuenta y sujeto que hoy no existe explícitamente:

```text
STOP
```

y documentar la relación ausente.

No inferirla por coincidencia narrativa.

---

#### 6. Guarda Activity vs Guest Perspective

Preservar:

```text
activityPresentation
!=
GuestPerspective narrative
```

No reutilizar automáticamente:

```text
"Pista del mirador encontrada"
```

para generar:

```text
"Has encontrado la pista del mirador.
Sigue hacia..."
```

`activityPresentation` representa una ocurrencia histórica después de aceptar una acción.

GuestPerspective expresa estado/perspectiva presente.

Contenido parecido:

```text
!=
same representational responsibility
```

Puede utilizarse como evidencia de vocabulario común durante el audit, pero no como autoridad narrativa para H26.

---

#### 7. DemoScript.presenterLabel

`presenterLabel` conserva su significado:

```text
affordance before action
```

Puede ser fuente legítima únicamente para representar la acción disponible como affordance.

No analizar sintácticamente el texto para extraer:

```text
mirador
patio
Inés
Mateo
```

y construir otras frases.

No transformar verbos ni hacer parsing de copy.

---

#### 8. Estado y evaluación

GuestPerspective puede derivar estado únicamente de fuentes operativas/derivadas existentes:

```text
subjectStates
Evidence
evaluation
claim
available action
```

No mover estado al Script.

No utilizar contenido presentacional para decidir:

```text
enabled
Evidence count
joint admissibility
K
claim
```

Preservar:

```text
presentation
!=
factual authority
```

---

#### 9. Fase experimental inicial

Sin añadir relaciones nuevas, intenta construir A y B usando exclusivamente fuentes legítimas identificadas por el audit.

El objetivo mínimo para B es que GuestPerspective no contenga indebidamente:

```text
Lucía
jardín
fuente
Aurora Stay
```

cuando esos valores son específicos de A.

Pero eliminar hardcodes mediante textos genéricos no basta si destruye información situada que ya existe legítimamente.

No considerar:

```text
"huésped"
"pista"
"lugar"
```

como PASS automático si el sistema dispone de datos situados que debería poder representar.

---

#### 10. Controles A/B

Ejecutar ambas composiciones en:

```text
initial
enlisted
A@P1
P2 enabled
A@P1 + B@P2
reset
```

Comparar GuestPerspective completa.

Verificar separadamente:

```text
operational state
Evidence
evaluation
```

para demostrar que cualquier diferencia presentacional no cambia esos planos.

---

#### 11. Control de account presentation

Si `fixture.member.name` puede utilizarse legítimamente como nombre de la cuenta/sesión visible sin afirmar identidad con `subject-p1`, prueba:

```text
A account presentation
→ Lucía

B account presentation
→ Inés
```

manteniendo:

```text
Evidence A/P1
Evidence B/P2
```

sin cambios.

Si el read model actual obliga a denominar ese campo como identidad del sujeto y no puede expresar únicamente account/session presentation:

```text
STOP
```

No cambies el significado del campo silenciosamente.

---

#### 12. Control de subject display

Inspecciona si existe una fuente legítima y explícita para mostrar los dos sujetos de Experience.

Si existe, utilizarla.

Si únicamente existen:

```text
subject-p1
subject-p2
```

más nombres narrativos dispersos en copy:

```text
STOP
```

antes de afirmar:

```text
P1 = Inés
P2 = Mateo
```

La ausencia de una representación situada del sujeto sería evidencia, no permiso para inventar mapping.

---

#### 13. Control de next-action affordance

La acción actualmente disponible debe poder representarse mediante:

```text
DemoScript.presenterLabel
```

cuando exista el paso correspondiente.

Verifica A y B.

La UI/GuestPerspective no debe decidir:

```text
garden vs mirador
fountain vs patio
```

por subjectRef, markerRef o Scenario ID.

El Script continúa sin controlar la disponibilidad: sólo representa una acción que runtime ya ha determinado como disponible.

---

#### 14. Status narrative

Para mensajes como:

```text
alistado
pista aportada
P2 habilitado
sigue explorando
resultado alcanzado
```

identifica qué parte procede legítimamente de:

```text
runtime state
evaluation
```

y qué parte requiere contenido situado adicional.

No construyas narrativa situada mediante parsing de:

```text
presenterLabel
activityPresentation
Evidence type
subjectRef
```

Si no existe una fuente legítima para una parte necesaria:

```text
STOP
```

y registra el punto exacto.

---

#### 15. Falsificadores H26

H26 → FALSIFIED si para producir una GuestPerspective correctamente situada es necesario:

```text
inventar account→subject mapping
```

o:

```text
reutilizar activityPresentation
como narrativa general
```

o:

```text
parsear presenterLabel
para obtener semántica situada
```

o:

```text
añadir una nueva shape/registry/
content architecture
```

o:

```text
hardcodear A/B en projection logic
```

o si:

```text
correct presentation
modifies facts/evaluation
```

o aparece regresión de A.

Detenerse en el primer falsador material.

No crear la solución ausente en esta sesión.

---

#### 16. Si las fuentes existentes bastan

H26 → SUPPORTED WITH QUALIFICATION únicamente si A/B producen una GuestPerspective situada coherente empleando relaciones existentes con responsabilidades legítimas y:

```text
facts unchanged
evaluation unchanged
Activity unchanged
```

Además:

```text
A presentation
→ no B leakage

B presentation
→ no A leakage
```

sin ampliar contratos.

---

#### 17. Si no bastan

Si se alcanza:

```text
NO LEGITIMATE EXISTING SOURCE
```

o una relación ausente concreta:

```text
STOP
```

y documentar:

```text
what representation is required
which existing candidates were rejected
why they are semantically inappropriate
what exact relation is absent
```

No seleccionar todavía la forma de esa relación.

Ese resultado debe clasificarse:

```text
H26 → FALSIFIED
```

dentro de la baseline actual, igual que H24.

Una sesión posterior podrá probar una relación mínima nueva si la evidencia lo justifica.

---

#### 18. L4 permanece congelado

No modificar `App.tsx`.

Mantener:

```text
L4
→ SOURCE-INSPECTION FINDING
→ OUT OF SCOPE
```

No usar renderizado B para reparar App.

Si el audit descubre que App añade contenido específico después de recibir GuestPerspective:

```text
record as L4 evidence
```

pero no corregirlo.

---

#### 19. L5 permanece consolidado experimentalmente

No modificar:

```text
activityPresentation
```

salvo lo necesario para ejecutar regresiones.

Mantener:

```text
L5
→ SCRIPT-BOUND SITUATED REPRESENTATION
→ EXECUTION-VERIFIED within A/B
```

No utilizar H26 para promover la shape.

---

#### 20. Verificación

Ejecutar:

```text
H26 focused harness

H25 regression

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

Si H26 se detiene en inspección por ausencia inequívoca de relación, construir solamente el harness diagnóstico necesario para reproducir el problema.

No se necesita navegador para el read model si el snapshot público permite observar L3.

---

#### 21. Informe

Crear:

`session-26-situated-guest-perspective-provenance.md`

con:

```text
H25 CONSOLIDATED INPUT

H26 HYPOTHESIS

VARIABLE UNDER TEST

GUEST PERSPECTIVE OUTPUT MAP

L3 DECOMPOSITION

EXISTING SOURCE CANDIDATES

ACCOUNT / SESSION PROVENANCE

SUBJECT DISPLAY PROVENANCE

NEXT-ACTION AFFORDANCE PROVENANCE

STATUS NARRATIVE PROVENANCE

REJECTED SOURCE CANDIDATES

NO-NEW-RELATION TEST

BASELINE

CODE DELTA

A CONTROL

B CONTROL

FACT / PRESENTATION SEPARATION

L3 RESULT

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H26 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

WHAT H26 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H27.

---

#### 22. Guardas

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
account/session
!=
subject identity
```

```text
operationalSessionSubjectRef
!=
authentication identity
```

```text
GuestPerspective
!=
Activity history
```

```text
presenterLabel
!=
activityPresentation
```

```text
state-derived message
!=
situated content source
```

```text
display name
!=
semantic identity
```

```text
content similarity
!=
shared responsibility
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
H26
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3a ACCOUNT DISPLAY
→ status

L3b SUBJECT DISPLAY
→ status

L3c JOURNEY NARRATIVE
→ status

NO-NEW-RELATION
→ sufficient / insufficient

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
<!-- FIN-TEXTO-ORIGINAL-S26 -->

---

<a id="sesion-27"></a>

## Capítulo 27 — Labels situados de sujetos

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-27-original.md) de `2026.zip`, registro `2026/09/14/rollout-2026-09-14T13-17-09-01a09fd9-8978-7280-9a36-812ea094c412.jsonl`. Mensaje de usuario en la línea 262; salida(s) de lectura en la(s) línea(s) 268. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: f7194bcf34f1c2e68ab4d417de3627710c91f692ac94fc3e9700d74c2f6c0816.

<!-- INICIO-TEXTO-ORIGINAL-S27 -->
Abre la Sesión 27 a partir del resultado consolidado de H26.

H26 permanece FALSIFIED.

No corrijas todavía L3a, L3c ni L4.

#### 1. Baseline

Mantener:

```text
SESSION 20 → CLOSED

H21 → FALSIFIED / historical baseline

H22 → SUPPORTED WITH QUALIFICATION
       Experience-based behavior selection

H23 → SUPPORTED WITH QUALIFICATION
       situated evaluation context binding

H24 → FALSIFIED
       no legitimate existing Activity
       representation source

H25 → SUPPORTED WITH QUALIFICATION
       script-bound Activity representation

H26 → FALSIFIED
       existing sources insufficient
       for complete GuestPerspective

L3a ACCOUNT DISPLAY
→ legitimate account source available
→ GuestPerspective sessionLabel OPEN

L3b SUBJECT DISPLAY
→ NO LEGITIMATE EXISTING SOURCE
→ FIRST H26 FALSIFIER
→ OPEN

L3c JOURNEY NARRATIVE
→ operational/derived inputs available
→ situated narrative source absent
→ OPEN

L4
→ SOURCE-INSPECTION FINDING / OPEN

L5
→ SCRIPT-BOUND SITUATED REPRESENTATION
→ EXECUTION-VERIFIED within A/B
```

Preservar:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

No reinterpretar H26 después de esta nueva sesión.

---

#### 2. Hallazgo que autoriza S27

H26 demuestra que falta la relación:

```text
Experience subject reference
        ↓
?
        ↓
situated human representation
```

Los datos narrativos existentes no establecen esa relación.

Preservar:

```text
co-located data
!=
declared relationship
```

```text
same human name across artifacts
!=
subject identity relation
```

---

#### 3. H27

```text
H27 — Explicit Situated Subject Representation
```

Hipótesis falsable:

```text
Dentro del recorrido Family Adventure,
una relación presentacional explícita
puede asociar cada subjectRef de Experience
con una representación humana situada,

de modo que esa representación pueda variar
independientemente de la cuenta/sesión,
sin modificar identidad factual,
operationalSessionSubjectRef,
atribución de Evidence,
contexto, evaluación, K o claim.
```

La relación:

```text
subjectRef → situated presentation
```

es exclusivamente representacional.

No constituye una relación de identidad de dominio.

---

#### 4. Guarda central

Preservar obligatoriamente:

```text
subject presentation
!=
subject identity
```

```text
account/member
!=
Experience subject
```

```text
operational session
!=
authentication identity
```

```text
display-name equality
!=
identity equality
```

```text
represented subject
!=
authenticated user
```

No introducir:

```text
memberId → subjectRef
```

ni:

```text
accountSubjectRef
viewerSubjectRef
actorRef
operatorRef
representativeRef
```

para hacer pasar H27.

---

#### 5. Candidate host

Antes del delta, compara explícitamente al menos:

```text
ScenarioDefinition
DemoScript
GuestPerspectiveReadModel
Fixture
```

como posibles hosts.

La candidata experimental preferida es `DemoScript`, porque:

```text
Scenario
→ operational/semantic subject references
```

mientras:

```text
DemoScript
→ situated demo presentation
```

Pero no asumas esta decisión sin documentar el análisis.

No añadas `displayName` directamente a `ScenarioDefinition.subjects` salvo que el experimento demuestre que Script no puede alojar legítimamente la relación dentro del alcance autorizado.

Si para resolver H27 es necesario modificar la semántica del SubjectReference compartido:

```text
STOP
```

---

#### 6. Shape experimental mínima

Si el análisis del host confirma DemoScript, puede ensayarse una forma local equivalente a:

```text
subjectPresentations?: [
    {
        subjectRef: "subject-p1",
        label: "Inés"
    },
    {
        subjectRef: "subject-p2",
        label: "Mateo"
    }
]
```

La forma concreta puede ajustarse al contrato local.

Debe clasificarse:

```text
EXPERIMENTAL
LOCAL
REVERSIBLE
NOT PROMOTED
```

Evitar nombres como:

```text
SubjectProfile
SubjectIdentity
Participant
AccountSubject
Persona
```

que implicarían semántica no demostrada.

---

#### 7. No usar la cuenta como fuente

Para A puede declararse explícitamente, por ejemplo:

```text
subject-p1 → "Lucía"
subject-p2 → "Huésped 2"
```

Para B:

```text
subject-p1 → "Inés"
subject-p2 → "Mateo"
```

Pero estas declaraciones deben existir por sí mismas.

No generarlas mediante:

```text
fixture.member.name
→ subject-p1 label
```

La coincidencia Lucía/Lucía o Inés/Inés es un dato narrativo intencionado de la composición, no una relación de identidad inferida.

---

#### 8. Threading mínimo

Transporta la representación hasta `projectGuestPerspective()` mediante la ruta técnica mínima desde la composición resuelta.

No introducir la representación en:

```text
EvidenceInput
Public Action
subjectStates
evaluation
```

No utilizar el label para buscar, filtrar o identificar Evidence.

La asociación debe continuar utilizando:

```text
subjectRef
```

como referencia.

La representación sólo determina:

```text
GuestPerspective.subjects[].label
```

dentro de H27.

No reutilizarla todavía en App, supervision, sessionLabel o journey message.

---

#### 9. Alcance preciso de H27

Modificar exclusivamente la procedencia de:

```text
GuestPerspective.subjects[].label
```

para Family Adventure A/B.

No corregir todavía:

```text
GuestPerspective.sessionLabel
GuestPerspective.message
GuestPerspective.subjects[].status
```

cuando contengan segunda persona, género o narrativa situada.

Esos elementos pertenecen a L3a/L3c o a una relación perspectival todavía no demostrada.

No eliminar esos síntomas mediante copy genérico.

---

#### 10. A control

A debe producir subject labels a partir de la nueva relación explícita:

```text
subject-p1
→ Lucía

subject-p2
→ Huésped 2
```

o labels equivalentes declarados explícitamente.

Verificar que los IDs siguen siendo:

```text
subject-p1
subject-p2
```

y Evidence permanece:

```text
A@subject-p1
B@subject-p2
```

No inferir labels desde member.

---

#### 11. B control

B debe declarar y mostrar:

```text
subject-p1
→ Inés

subject-p2
→ Mateo
```

GuestPerspective.subjects debe exponer esos labels en todas las fases.

No debe contener:

```text
"Tú · huésped 1"
"Huésped 2 · ya existe..."
```

como labels derivados por ID.

El resto de L3 puede permanecer incorrecto y debe registrarse separadamente.

---

#### 12. Control crítico account ≠ subject presentation

Crea una variante exclusivamente de harness:

```text
fixture.member.name
→ Inés

subject-p1 presentation
→ Participante Alfa
```

Mantener:

```text
operationalSessionSubjectRef
→ subject-p1

Evidence A
→ subject-p1

Evidence B
→ subject-p2
```

Debe observarse simultáneamente:

```text
account presentation
→ Inés

GuestPerspective subject-p1 label
→ Participante Alfa
```

sin cambios en hechos, estado o evaluación.

Esto es condición discriminante principal de H27.

---

#### 13. Control inverso

Crear otra variante donde:

```text
fixture.member.name
→ Cuenta Demo
```

pero:

```text
subject-p1 presentation
→ Inés
```

Debe observarse:

```text
account presentation
→ Cuenta Demo

subject-p1 label
→ Inés
```

mientras permanecen idénticos:

```text
subjectRefs
operationalSessionSubjectRef
Evidence
context
evaluation
K
claim
```

No cambiar Scenario para conseguirlo.

---

#### 14. Representation independence

Crear variantes X/Y que cambien exclusivamente:

```text
subjectPresentations[].label
```

Manteniendo:

```text
Scenario subjects
member
session
actions
Evidence
contexts
evaluation
Activity
```

Después:

```text
facts X == facts Y
evaluation X == evaluation Y
Activity X == Activity Y
subject labels X != subject labels Y
```

No editar directamente el snapshot.

---

#### 15. No introducir «Tú»

La nueva representación no autoriza automáticamente:

```text
subject-p1 → Tú
```

porque eso exigiría una relación perspectival distinta:

```text
viewer/account/session
→ represented subject
```

H27 no estudia esa relación.

Por tanto, utilizar labels nominales o descriptivos explícitos.

No derivar segunda persona de:

```text
operationalSessionSubjectRef
```

---

#### 16. Ausencia / mismatch

No diseñar todavía una política productiva general.

Pero verificar al menos que una representación no puede:

```text
create a subject
change subjectRef
change Evidence attribution
```

Si el Script contiene una referencia de presentación para un subjectRef inexistente, no debe materializar un nuevo sujeto.

Si expresar de manera segura la ausencia de presentación exige cambiar contratos adicionales o inventar un fallback general:

```text
STOP
```

Documentar la presión sin resolverla.

---

#### 17. L3a fuera de alcance

Mantener:

```text
GuestPerspective.sessionLabel
→ OPEN
```

aunque siga diciendo Lucía en B.

No sustituirlo simplemente por:

```text
member.name
```

porque la frase actual mezcla:

```text
account presentation
subject relation
second-person perspective
capability narrative
```

La presentación de cuenta aislada ya dispone de fuente legítima:

```text
fixture.member.name
```

pero la composición de sessionLabel pertenece a otra presión.

---

#### 18. L3c fuera de alcance

Mantener:

```text
GuestPerspective.message
GuestPerspective.subjects[].status
```

sin corrección situada si hacerlo exige:

```text
second-person perspective
gender
journey narrative
situated locations
```

Registrar los síntomas restantes.

No reutilizar:

```text
presenterLabel
activityPresentation
subjectPresentations
```

como narrativa general por mera conveniencia.

---

#### 19. L4 congelado

No modificar `App.tsx`.

Mantener:

```text
L4
→ SOURCE-INSPECTION FINDING
→ OUT OF SCOPE
```

No reutilizar subjectPresentations directamente desde App para saltarse GuestPerspective.

---

#### 20. L5 congelado

Mantener:

```text
activityPresentation
```

sin promoción ni reutilización automática.

Verificar regresión H25:

```text
A Activity → jardín/fuente
B Activity → mirador/patio
```

Subject presentation no debe modificar Activity.

---

#### 21. Falsadores H27

H27 → FALSIFIED si:

```text
subject label cannot vary independently
from account/member
```

o:

```text
representation changes subjectRef,
Evidence attribution, session,
context or evaluation
```

o:

```text
a member→subject mapping is required
to make the relation work
```

o:

```text
subject presentation must be embedded
in SubjectReference semantics
```

o:

```text
new relation requires Actor/Participant/
Representative/etc.
```

o:

```text
App must be modified to make
GuestPerspective carry the relation
```

o aparece regresión A.

Usar INCONCLUSIVE sólo para impedimento externo.

---

#### 22. Veredicto positivo

H27 → SUPPORTED WITH QUALIFICATION únicamente si:

```text
subjectRef
→ explicit situated presentation
```

puede variar independientemente de:

```text
account display
operational session
factual identity
Evidence attribution
evaluation
Activity representation
```

y GuestPerspective B obtiene labels situados sin hardcodes A.

La cualificación debe indicar que H27 NO demuestra:

```text
subject identity model
account→subject relation
viewer/perspective relation
authentication
general participant model
journey narrative provenance
general presentation architecture
```

---

#### 23. Artifact quarantine

Si la nueva relación funciona:

```text
DemoScript.subjectPresentations
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

No convertirla automáticamente en:

```text
Experience contract
Subject contract
Product Semantic Contract
TES concept
general identity model
```

Recurrencia futura no implica promoción.

---

#### 24. Verificación

Ejecutar:

```text
H27 focused harness
H26 historical reproduction
H25 regression
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

No se necesita navegador para `GuestPerspective.subjects[].label` si el snapshot público lo demuestra.

---

#### 25. Informe

Crear:

`session-27-explicit-situated-subject-representation.md`

con:

```text
H26 CONSOLIDATED INPUT

H27 HYPOTHESIS

VARIABLE UNDER TEST

WHY A NEW RELATION IS NOW PERMITTED

SUBJECT / ACCOUNT / SESSION SEPARATION

CANDIDATE HOST ANALYSIS

EXPERIMENTAL REPRESENTATION SHAPE

REPRESENTATION AUTHORITY

THREADING PATH

BASELINE

CODE DELTA

A CONTROL

B CONTROL

ACCOUNT / SUBJECT DECOUPLING CONTROL

INVERSE DECOUPLING CONTROL

REPRESENTATION INDEPENDENCE CONTROL

ABSENCE / MISMATCH OBSERVATION

EXECUTION TRACE

L3b RESULT

L3a STATUS

L3c STATUS

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H27 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H27 DOES NOT PROVE

REMAINING PRESSURES
```

No selecciones automáticamente H28.

---

#### 26. Guardas finales

Preservar:

```text
subject presentation
!=
subject identity
```

```text
account presentation
!=
subject presentation
```

```text
account/member
!=
Experience subject
```

```text
operationalSessionSubjectRef
!=
authentication identity
```

```text
same display name
!=
same identity
```

```text
co-located data
!=
declared relationship
```

```text
display relation
!=
factual authority
```

```text
GuestPerspective
!=
Activity history
```

```text
subjectPresentations
!=
journey narrative
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
H27
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3b SUBJECT DISPLAY
→ status

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ supported / unsupported

L3a
→ preserved / open

L3c
→ preserved / open

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```
<!-- FIN-TEXTO-ORIGINAL-S27 -->

---

<a id="sesion-28"></a>

## Capítulo 28 — Presentación exclusivamente de cuenta

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-28-original.md) de `2026.zip`, registro `2026/09/14/rollout-2026-09-14T13-17-09-01a09fd9-8978-7280-9a36-812ea094c412.jsonl`. Mensaje de usuario en la línea 364; salida(s) de lectura en la(s) línea(s) 371. Cotejo adicional: lectura repetida completa. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 4ebe42dcec8b8875a1c763d3d102f72c06957b70b5e9da08d818a33af4038127.

<!-- INICIO-TEXTO-ORIGINAL-S28 -->
### SESIÓN 28 — ACCOUNT-SOURCED GUEST PRESENTATION

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 27 — Explicit Situated Subject Representation
```

S27 queda consolidada como:

```text
SESSION 27 → CLOSED

H27 → SUPPORTED WITH QUALIFICATION

L3b SUBJECT DISPLAY
→ EXPLICIT SCRIPT-BOUND SUBJECT LABELS
→ EXECUTION-VERIFIED within A/B

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ SUPPORTED within tested scope

DemoScript.subjectPresentations
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

Preservar íntegramente:

```text
H26 → FALSIFIED / historical baseline unchanged

L3a → OPEN
L3c → OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN
L5 → experimentally addressed H25

Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

No promover ninguno de los artefactos experimentales H25/H27.

---

### H28 — PRESSURE SELECTED

Seleccionar exclusivamente:

```text
L3a
```

No resolver L3c.

No resolver L4.

La presión procede de H26 y permanece visible después de H27.

Existe una fuente legítima para presentación aislada de cuenta:

```text
fixture.member.name
→ snapshot.member
→ account display
```

pero el actual:

```text
GuestPerspective.sessionLabel
```

mezcla todavía varias afirmaciones:

```text
account
+
subject relationship
+
second person
+
capability / journey narrative
```

Por ejemplo, copy histórico del tipo:

```text
Usas la cuenta de Lucía, huésped 1...
```

no queda autorizado simplemente porque conozcamos:

```text
member.name
```

ni porque H27 haya introducido:

```text
subjectRef
→ subject presentation
```

Preservar:

```text
account presentation
!=
subject presentation

account/member
!=
Experience subject

subject presentation
!=
subject identity

operationalSessionSubjectRef
!=
authentication identity

represented subject
!=
authenticated user
```

H27 NO creó:

```text
member → subject
viewer → subject
account → subject
session → subject
```

---

### H28 HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
la fuente de cuenta ya existente puede proporcionar
una presentación situada exclusivamente de cuenta
para GuestPerspective.sessionLabel,

y esa presentación puede variar
independientemente de DemoScript.subjectPresentations,

sin introducir relaciones account→subject,
viewer→subject o session→subject,

y sin modificar subjectRef,
operationalSessionSubjectRef,
Evidence attribution,
subjectStates,
Activity,
context,
evaluation,
K o claim.
```

H28 investiga:

```text
account source
→ account-only presentation
```

NO:

```text
account
→ represented subject
```

NO:

```text
account
→ viewer identity
```

NO:

```text
operational session
→ authenticated user
```

---

### VARIABLE UNDER TEST

Exclusivamente:

```text
GuestPerspective.sessionLabel
```

No modificar:

```text
GuestPerspective.subjects[].label
GuestPerspective.subjects[].status
GuestPerspective.message
GuestPerspective.supervision
Activity
App
```

salvo instrumentación estrictamente necesaria para observar el experimento.

Los labels H27 deben permanecer procedentes exclusivamente de:

```text
DemoScript.subjectPresentations
```

No utilizar dichos labels para construir sessionLabel.

---

### FIRST REQUIRED STEP — SOURCE / HOST ANALYSIS

Antes del delta, inspeccionar y documentar la procedencia y threading actuales de:

```text
fixture.member
snapshot.member
GuestPerspective.sessionLabel
projectGuestPerspective()
MockDataAdapter
App consumer
```

Comparar dónde debe ocurrir la transformación presentacional sin introducir una nueva relación semántica.

No asumir de antemano que debe pasarse todo `member` al projector.

Preferir el transporte mínimo que preserve explícitamente que la única autoridad ensayada es:

```text
existing account presentation source
```

Si el experimento exige utilizar `operationalSessionSubjectRef`, `subjectPresentations`, Evidence o Scenario role para construir la presentación de cuenta:

```text
STOP
→ document dependency
→ H28 FALSIFIED or INCONCLUSIVE
```

según corresponda.

---

### ACCOUNT-ONLY COPY

El resultado de sessionLabel debe afirmar exclusivamente la presentación de la cuenta.

Puede ensayarse una forma equivalente a:

```text
Cuenta de Lucía
Cuenta de Inés
```

La forma textual concreta puede adaptarse si el contrato/read model existente lo requiere, pero NO debe incluir:

```text
tú
usas
tu cuenta
huésped 1
P1
subject-p1
has habilitado
puedes activar
Mateo
Huésped 2
```

ni ninguna afirmación equivalente que requiera relacionar cuenta, viewer, sujeto o capability.

---

### A CONTROL

Con composición A:

```text
member.name → Lucía

subject-p1 presentation → Lucía
subject-p2 presentation → Huésped 2
```

debe observarse:

```text
sessionLabel
→ account-source presentation of Lucía

subject-p1 label
→ Lucía

subject-p2 label
→ Huésped 2
```

La coincidencia Lucía/Lucía NO constituye evidencia de relación.

Debe proceder de dos fuentes independientes.

---

### B CONTROL

Con composición B:

```text
member.name → Inés

subject-p1 presentation → Inés
subject-p2 presentation → Mateo
```

debe observarse:

```text
sessionLabel
→ account-source presentation of Inés

subject-p1 label
→ Inés

subject-p2 label
→ Mateo
```

De nuevo:

```text
display equality
!=
identity relation
```

---

### PRIMARY DECOUPLING CONTROL

Sobre B:

```text
member.name → Cuenta Demo

subject-p1 presentation → Inés
subject-p2 presentation → Mateo
```

Debe resultar simultáneamente:

```text
sessionLabel
→ account presentation derived from Cuenta Demo

subject-p1 label
→ Inés

subject-p2 label
→ Mateo
```

y mantenerse:

```text
operationalSessionSubjectRef → subject-p1

Evidence A → subject-p1
Evidence B → subject-p2

Activity unchanged
context unchanged
evaluation unchanged
K unchanged
claim unchanged
```

No introducir mapping para explicar la diferencia.

---

### INVERSE DECOUPLING CONTROL

Mantener:

```text
member.name → Inés
```

y cambiar únicamente:

```text
subject-p1 presentation
→ Participante Alfa
```

Debe resultar:

```text
sessionLabel
→ account presentation of Inés

subject-p1 label
→ Participante Alfa
```

sin ningún otro cambio.

Esto debe demostrar:

```text
subject presentation changes
!=
account presentation changes
```

---

### REPRESENTATION INDEPENDENCE CONTROL

Construir variantes X/Y con:

```text
same Scenario
same member
same Evidence
same session
same Activity
same evaluation

different subjectPresentations
```

Debe cumplirse:

```text
sessionLabel X == sessionLabel Y
subject labels X != subject labels Y
facts X == facts Y
evaluation X == evaluation Y
Activity X == Activity Y
```

Y el control complementario:

```text
same subjectPresentations
different member.name
```

debe producir:

```text
sessionLabel X != sessionLabel Y
subject labels X == subject labels Y
facts X == facts Y
evaluation X == evaluation Y
Activity X == Activity Y
```

---

### NO SECOND PERSON

H28 no debe introducir ni conservar por necesidad experimental afirmaciones perspectivales como:

```text
tú
tu
usas
por ti
```

dentro de la variable estudiada.

Conocer:

```text
member.name = Inés
```

NO autoriza:

```text
Tú eres Inés
```

Conocer:

```text
subject-p1 presentation = Inés
```

tampoco autoriza esa inferencia.

La eventual relación:

```text
viewer/account/session
→ represented subject
```

permanece AUSENTE.

---

### FALSIFIERS

H28 queda FALSIFIED si para producir account presentation en sessionLabel se necesita:

```text
member → subject mapping
```

o:

```text
subject presentation
```

o:

```text
operationalSessionSubjectRef
```

como fundamento de identidad/perspectiva,

o si cambiar la cuenta modifica:

```text
subject labels
subject refs
Evidence attribution
Activity
context
evaluation
K
claim
```

o si cambiar subjectPresentations modifica sessionLabel,

o si debe ampliarse la semántica de:

```text
SubjectReference
member
operationalSessionSubjectRef
```

para hacer pasar el experimento.

También STOP si es necesario introducir:

```text
Actor
Operator
Participant
Representative
AccountSubject
ViewerSubject
AuthenticatedSubject
```

o equivalentes.

No crear la abstracción siguiente dentro de una baseline falsificada.

---

### PRESERVE OPEN PRESSURES

H28 NO resolverá:

```text
L3c
```

Por tanto deben permanecer visibles los textos históricos relacionados con:

```text
journey state
locations
gender
has habilitado
por ti
sigue explorando
```

fuera de `sessionLabel`.

Tampoco modificar:

```text
L4 / App
```

para hacer parecer completa la composición B.

H25/H27 permanecen en cuarentena.

---

### ARTIFACT STATUS

Preservar:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

DemoScript.subjectPresentations
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
```

H28 no constituye evidencia suficiente para promover DemoScript como modelo universal de presentación.

No crear:

```text
PresentationModel
PresentationRegistry
ContentRegistry
PerspectiveEngine
```

ni abstracción equivalente.

---

### OUTPUT

Producir:

```text
session-28-account-sourced-guest-presentation.md
```

documentando al menos:

```text
H27 CONSOLIDATED INPUT
H28 HYPOTHESIS
VARIABLE UNDER TEST
EXISTING ACCOUNT SOURCE
ACCOUNT / SUBJECT / SESSION SEPARATION
SOURCE AND HOST ANALYSIS
THREADING PATH
BASELINE
CODE DELTA
A CONTROL
B CONTROL
ACCOUNT DECOUPLING CONTROL
INVERSE DECOUPLING CONTROL
REPRESENTATION INDEPENDENCE CONTROL
EXECUTION TRACE
L3a RESULT
L3b STATUS
L3c STATUS
L4 STATUS
L5 STATUS
FALSIFICATION ANALYSIS
H28 VERDICT
ARCHITECTURAL CONSEQUENCE
SEMANTIC CONSEQUENCE
ARTIFACT QUARANTINE
WHAT H28 DOES NOT PROVE
REMAINING PRESSURES
```

Concluir exclusivamente con una matriz equivalente a:

```text
H28
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3a ACCOUNT DISPLAY
→ status

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ preserved / unsupported

L3b
→ preserved / experimentally addressed

L3c
→ preserved / open

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H29 automáticamente.

El objetivo sigue siendo:

```text
hypothesis
→ falsification
→ reversible experiment
→ evidence
→ evaluation
→ consolidation
→ eventual promotion
```

y no diseñar retrospectivamente la arquitectura necesaria para que la demo parezca correcta.
<!-- FIN-TEXTO-ORIGINAL-S28 -->

---

<a id="sesion-29"></a>

## Capítulo 29 — Estado operacional neutral del sujeto

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-29-original.md) de `2026.zip`, registro `2026/09/14/rollout-2026-09-14T13-17-09-01a09fd9-8978-7280-9a36-812ea094c412.jsonl`. Mensaje de usuario en la línea 490; salida(s) de lectura en la(s) línea(s) 498. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: c5671f06ce73fffc02d0bcc1b192c9459c4bbc9219d05f1642a31a61a2e25c9f.

<!-- INICIO-TEXTO-ORIGINAL-S29 -->
### SESIÓN 29 — OPERATIONAL SUBJECT STATUS PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 28 — Account-Sourced Guest Presentation
```

No reconstruir decisiones anteriores.

La baseline consolidada de entrada es:

```text
SESSION 28 → CLOSED

H28 → SUPPORTED WITH QUALIFICATION

L3a ACCOUNT DISPLAY
→ ACCOUNT-SOURCED
→ ACCOUNT-ONLY
→ EXECUTION-VERIFIED within A/B

ACCOUNT / SUBJECT PRESENTATION SEPARATION
→ EXECUTION-VERIFIED within tested scope

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / OPEN

L4
→ PRESERVED / SOURCE-INSPECTION / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged

ADR-001–005
→ ACCEPTED / unchanged

TES → unchanged

Product Semantic Contract
→ unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Artefactos en cuarentena:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

DemoScript.subjectPresentations
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

H28 account-name transport / formatting
→ LOCAL PROTOTYPE EXPERIMENT
→ NOT PROMOTED
```

---

### 1. PRESSURE SELECTED

Seleccionar exclusivamente, dentro de L3c:

```text
GuestPerspective.subjects[].status
```

NO seleccionar todavía:

```text
GuestPerspective.message
```

La separación:

```text
subjects[].status
vs
message
```

es una descomposición diagnóstica de L3c para permitir falsación independiente.

NO constituye:

```text
nuevo contrato
nueva arquitectura
nueva taxonomía TES
PSC extension
```

L3c permanece como presión consolidada hasta que exista evidencia suficiente para reconsiderarla.

---

### 2. MOTIVACIÓN

S28 confirma que siguen presentes expresiones históricas como:

```text
Habilitado por ti
```

mientras la fuente operacional:

```text
subjectStates
```

ya proporciona información sobre el estado presente de los sujetos.

La cuestión de S29 NO es todavía:

```text
¿cómo construimos una narrativa situada
sobre el estado del huésped?
```

La cuestión es anterior:

```text
¿qué parte de subjects[].status
puede estar autorizada únicamente
por el estado operacional existente?
```

Preservar:

```text
operational state
!=
causal attribution

operational state
!=
actor attribution

operational state
!=
viewer perspective

operational state
!=
journey narrative

operational state
!=
gender information
```

Especialmente:

```text
P2 is enabled
```

NO implica:

```text
P1 enabled P2
```

y aunque una acción anterior haya producido la transición:

```text
P1 enabled P2
```

NO implica:

```text
you enabled P2
```

porque no existe todavía una relación legitimada:

```text
viewer
→ P1
```

ni:

```text
account
→ P1
```

ni:

```text
authenticated user
→ P1
```

---

### 3. H29 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
GuestPerspective.subjects[].status
puede representar exclusivamente
el estado operacional presente
de cada sujeto utilizando
la fuente existente subjectStates,

sin introducir causalidad,
actor attribution,
segunda persona,
género del sujeto,
localización
ni journey narrative,

y sin modificar
subject identity/reference,
account presentation,
subject presentation,
Activity,
Evidence attribution,
operationalSessionSubjectRef,
context,
evaluation,
K o claim.
```

La relación bajo estudio es estrictamente:

```text
existing subject operational state
→ neutral present-state representation
```

NO:

```text
state
→ cause of state
```

NO:

```text
state
→ actor who caused state
```

NO:

```text
state
→ viewer relation
```

NO:

```text
state
→ journey interpretation
```

---

### 4. NO-NEW-COMPOSITION-RELATION CONDITION

S29 debe intentar resolver esta presión utilizando exclusivamente las relaciones operacionales existentes.

No añadir en esta sesión:

```text
DemoScript.subjectStatusPresentations

Scenario.subjectStatusPresentation

Fixture.subjectStatusPresentation

StatusPresentationRegistry

PresentationModel

PerspectiveModel
```

o equivalentes.

Si la inspección demuestra que `subjectStates` no puede acreditar una representación de estado suficientemente precisa sin añadir una nueva relación declarativa:

```text
STOP
→ document missing relation
→ preserve evidence
→ H29 FALSIFIED or INCONCLUSIVE
```

No crear la solución siguiente dentro de esa misma baseline.

Una sesión posterior podría autorizar una relación mínima si la falsación la justificase.

---

### 5. VARIABLE UNDER TEST

Modificar exclusivamente la procedencia/construcción de:

```text
GuestPerspective.subjects[].status
```

Preservar:

```text
GuestPerspective.sessionLabel
GuestPerspective.subjects[].label
GuestPerspective.message
GuestPerspective.supervision
Activity
App
```

H28 debe seguir gobernando:

```text
sessionLabel
→ account-only presentation
```

H27 debe seguir gobernando:

```text
subjects[].label
→ DemoScript.subjectPresentations
```

H25 debe seguir gobernando la representación situada posterior de Activity.

No reutilizar ninguno de esos campos como fuente de `subjects[].status`.

---

### 6. FIRST REQUIRED STEP — SOURCE INSPECTION

Antes de modificar código, documentar el recorrido exacto actual de:

```text
Scenario subjects
subjectStates
operationalSessionSubjectRef
Evidence
GuestPerspective.subjects[].status
projectGuestPerspective()
```

Identificar todos los valores reales que puede adoptar `subjectStates` dentro de Family Adventure y en qué transición aparecen.

Construir antes del delta una matriz:

```text
subjectRef
operational state
phase/action
current status copy
information justified by state
information NOT justified by state
```

No diseñar primero los nuevos textos y después buscar una justificación.

La fuente debe preceder a la representación.

---

### 7. REPRESENTATION RULE

Si la inspección confirma que los estados existentes contienen información suficiente, puede realizarse una representación local y reversible del significado operacional existente.

La representación debe ser:

```text
state-only
neutral
non-perspectival
non-causal
non-locational
non-narrative
```

No debe contener:

```text
tú
tu
por ti
contigo
gracias a ti
por Lucía
por Inés
por P1
por la cuenta
```

ni formulaciones semánticamente equivalentes.

Tampoco debe afirmar género del sujeto si éste no forma parte de la fuente.

Si el castellano exige concordancia gramatical, formular el texto alrededor de un sustantivo cuyo género sea conocido por el propio copy, por ejemplo conceptualmente:

```text
Estado: ...
Habilitación: ...
```

en lugar de atribuir género a la persona representada.

NO asumir esos ejemplos como el copy obligatorio.

Códex debe derivar el vocabulario final del estado real encontrado en la baseline y documentar explícitamente el mapping:

```text
operational state
→ displayed state
```

No introducir significado adicional para conseguir copy más natural.

---

### 8. AUTHORITY DIRECTION

La dirección obligatoria es:

```text
Scenario subject
→ corresponding existing subjectState
→ status representation
```

No:

```text
status presentation
→ subject existence
```

No:

```text
subjectPresentations
→ state
```

No:

```text
member
→ state
```

No:

```text
Activity presentation
→ state
```

No:

```text
Evidence count
→ invented state
```

`subjects[].status` debe describir un estado existente, no crearlo ni inferirlo de copy coexistente.

---

### 9. TEMPORAL / TRANSITION CONTROL

Aprovechar la secuencia operacional ya existente para comprobar discriminación temporal.

Como mínimo estudiar:

```text
initial
enlist-p1
discover-clue-a
activate-p2
discover-clue-b
reset
```

Para cada sujeto identificar cuándo cambia realmente `subjectStates`.

Debe cumplirse:

```text
same subjectState
→ same status representation
```

aunque cambien otros elementos como Evidence o Activity.

Y cuando una acción produzca legítimamente una transición:

```text
subjectState X → subjectState Y
```

debe observarse:

```text
status X → status Y
```

sólo en correspondencia con esa transición.

No afirmar que la transición fue causada por un actor concreto salvo que esa causalidad ya esté representada explícitamente en una fuente autoritativa; si esto fuese necesario para el status:

```text
STOP
```

---

### 10. A / B CONTROL

Ejecutar A y B a través de sus secuencias completas.

Cuando:

```text
subjectRef A == subjectRef B
operational state A == operational state B
```

la representación de status debe ser equivalente aunque difieran:

```text
member.name
subjectPresentations
context
Activity presentation
situated locations
```

Este control es importante.

S29 NO busca status situados por composición.

Busca comprobar si el estado operacional ya disponible constituye autoridad suficiente para una representación neutral del presente.

Si A y B necesitan status distintos pese a tener el mismo operational state:

```text
H29 NO-NEW-COMPOSITION-RELATION
→ falsification pressure
```

No introducir automáticamente una nueva relación para resolverlo.

---

### 11. ACCOUNT INDEPENDENCE CONTROL

Perturbar exclusivamente:

```text
member.name
```

manteniendo iguales:

```text
Scenario
subjectStates
subjectPresentations
actions
Evidence
context
evaluation
Activity
```

Debe cumplirse:

```text
sessionLabel changes
subjects[].status unchanged
```

La presentación de cuenta H28 no puede convertirse en autoridad del estado.

---

### 12. SUBJECT PRESENTATION INDEPENDENCE CONTROL

Perturbar exclusivamente:

```text
DemoScript.subjectPresentations
```

manteniendo todo el estado operacional igual.

Debe cumplirse:

```text
subjects[].label changes
subjects[].status unchanged
```

Especialmente:

```text
subject-p1 label = Participante Alfa
```

no debe alterar ninguna representación de estado.

Esto preserva:

```text
subject presentation
!=
subject operational state
```

---

### 13. ACTIVITY REPRESENTATION INDEPENDENCE CONTROL

Perturbar únicamente representación H25 cuando sea técnicamente posible dentro del harness, sin cambiar la acción/hecho ocurrido.

Debe cumplirse:

```text
Activity representation changes
subjects[].status unchanged
```

No reutilizar:

```text
activityPresentation
```

para explicar el estado presente.

Preservar:

```text
Activity
→ representation of occurred Activity

subjectStates
→ present operational state
```

---

### 14. EVIDENCE DISCRIMINATION CONTROL

Usar las fases del recorrido en las que aumenta Evidence pero no cambia el `subjectState` relevante.

Debe comprobarse:

```text
Evidence changes
+
subjectState unchanged
→
status unchanged
```

Esto debe impedir que el projector reconstruya estado desde:

```text
Evidence count
marker presence
K
claim
```

si ya existe `subjectStates` como fuente autoritativa.

Preservar:

```text
Evidence
!=
subject state
```

y:

```text
evaluation
!=
subject state
```

---

### 15. CAUSALITY NEGATIVE CONTROL

Prestar especial atención a la transición que habilita P2.

Si el estado resultante sólo acredita:

```text
subject-p2
→ enabled
```

la representación puede afirmar únicamente ese estado.

No puede afirmar:

```text
enabled by you
enabled by P1
enabled by Inés
enabled by Lucía
```

sin una fuente autoritativa adicional.

Incluso si la secuencia del Demo Script contiene una acción anterior de activación, no convertir automáticamente:

```text
temporal precedence
```

en:

```text
actor attribution
```

ni:

```text
viewer attribution
```

Preservar:

```text
transition occurrence
!=
viewer identity
```

y:

```text
action chronology
!=
perspective authority
```

---

### 16. MESSAGE FREEZE

`GuestPerspective.message` debe permanecer sin resolver y, cuando sea posible, byte-for-byte idéntico en su construcción.

Los síntomas existentes deben permanecer visibles:

```text
jardín
fuente
mirador/patio mismatch where applicable
segunda persona
sigue explorando
journey narrative
```

No corregirlos incidentalmente.

La existencia de esos síntomas NO falsifica H29 porque no forman parte de la variable bajo prueba.

Conservarlos permite que la siguiente presión continúe siendo observable.

---

### 17. L3c STATUS AFTER H29

No declarar automáticamente:

```text
L3c → RESOLVED
```

aunque H29 sea positiva.

En caso de éxito, registrar algo equivalente a:

```text
L3c subject-status component
→ experimentally addressed
```

mientras:

```text
L3c journey/present-state narrative
→ OPEN
```

Esta formulación es diagnóstica.

No crear nuevos identificadores normativos L3c1/L3c2 salvo que exista una necesidad demostrada de gobierno posterior.

---

### 18. FALSIFIERS

H29 queda FALSIFIED si:

```text
subjects[].status
cannot be derived
from existing subjectStates
without another relationship
```

o si:

```text
changing account presentation
changes status
```

o:

```text
changing subject presentation
changes status
```

o:

```text
changing Activity representation
changes status
```

sin cambio operacional correspondiente,

o si:

```text
Evidence/K/claim
must be used to reconstruct
a state already represented in subjectStates
```

o si se requiere introducir:

```text
viewer
actor
operator
participant
representative
accountSubject
viewerSubject
```

o equivalente.

También falsifica la versión no-new-relation de H29 si una representación correcta exige:

```text
DemoScript.subjectStatusPresentations
```

o cualquier nueva relación declarativa de composición.

Ante cualquiera de esos casos:

```text
STOP
→ preserve evidence
→ document missing relation
→ do not solve it in S29
```

---

### 19. REGRESSION REQUIREMENTS

Preservar las baselines históricas H21–H28.

Comprobar al menos:

```text
S20 vertical
H21
H22
H23
H24
H25
H26
H27
H28
```

según el esquema histórico ya utilizado.

A/B deben mantener:

```text
subjectRefs
operationalSessionSubjectRef
Evidence attribution
context
evaluation
K
claim
Activity
account presentation
subject presentation
```

excepto exclusivamente el cambio autorizado en:

```text
subjects[].status
```

---

### 20. OUTPUT

Producir:

```text
session-29-operational-subject-status-provenance.md
```

con al menos:

```text
H28 CONSOLIDATED INPUT

H29 HYPOTHESIS

VARIABLE UNDER TEST

WHY L3c IS DIAGNOSTICALLY SPLIT

EXISTING OPERATIONAL STATE SOURCE

PRE-DELTA STATE / COPY MATRIX

SOURCE AUTHORITY

NO-NEW-COMPOSITION-RELATION CONDITION

HOST / PROJECTION ANALYSIS

THREADING PATH

BASELINE

CODE DELTA

A CONTROL

B CONTROL

TEMPORAL / TRANSITION CONTROL

ACCOUNT INDEPENDENCE CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

ACTIVITY REPRESENTATION INDEPENDENCE CONTROL

EVIDENCE DISCRIMINATION CONTROL

CAUSALITY NEGATIVE CONTROL

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c SUBJECT STATUS RESULT

L3c REMAINING NARRATIVE PRESSURE

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H29 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H29 DOES NOT PROVE

REMAINING PRESSURES
```

Concluir únicamente con una matriz equivalente a:

```text
H29
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

L3c SUBJECT STATUS
→ status

STATE / PRESENTATION AUTHORITY
→ supported / unsupported

CAUSAL / VIEWER ATTRIBUTION
→ NOT INTRODUCED / introduced-invalidly

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c JOURNEY NARRATIVE
→ preserved / open

L4
→ preserved / source-inspection

L5
→ preserved / experimentally addressed H25

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H30 automáticamente.

---

### 21. METHODOLOGICAL GUARDRAIL

Mantener:

```text
having a state
!=
knowing why that state exists

knowing a transition occurred
!=
knowing who should be credited for it

knowing the operational subject
!=
knowing the viewer

knowing P1 operates in the session
!=
viewer is P1

state representation
!=
journey narrative
```

S29 debe intentar **reducir la afirmación al nivel de la evidencia disponible**, no aumentar la semántica del modelo para conservar el copy histórico.

El objetivo sigue siendo:

```text
hipótesis
→ falsación
→ experimento reversible
→ evidencia
→ evaluación
→ consolidación
→ eventual promoción
```

La arquitectura debe continuar emergiendo de relaciones demostradas, no de los textos que la demo históricamente necesitaba mostrar.
<!-- FIN-TEXTO-ORIGINAL-S29 -->

---

<a id="sesion-30"></a>

## Capítulo 30 — Narrativa situada por posición operacional

**Estado:** instrucción original íntegra recuperada del registro de la sesión.

**Procedencia:** [copia literal del texto recuperado](instrucciones-recuperadas/sesion-30-original.md). El usuario aportó el archivo `rollout-2026-09-17T11-54-23-01a0af00-d87f-7163-a410-d83e0ffaeec4.jsonl copia`, correspondiente al hilo `01a0af00-d87f-7163-a410-d83e0ffaeec4` de VS Code, iniciado el 17 de septiembre de 2026.

La línea 9 del JSONL identifica el adjunto original `/Users/juanjo/.codex/attachments/0a54c091-3225-4498-97cf-6bff6438830b/pasted-text.txt`. La línea 13 registra su lectura con `cat`; la línea 15 conserva el resultado completo de esa lectura (salida 0, sin indicadores de truncación). El texto se ha extraído decodificando los contenedores JSON, sin ejecutar las instrucciones ni las llamadas históricas. No se ha comparado con el adjunto original del M3, que no está disponible aquí.

SHA-256 del archivo JSONL aportado: 1c0de40ac2d546d391e64131eaa3252967a6f073420fdb2110c38c861fc21860.

SHA-256 del texto fuente recuperado: 0b57a9861f5eabc174324f66fdcfd9c4807417b9b19ff4800a9366756cca9987.

<!-- INICIO-TEXTO-ORIGINAL-S30 -->
### SESIÓN 30 — SCRIPT-BOUND SITUATED JOURNEY NARRATIVE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 29 — Operational Subject Status Provenance
```

No reconstruir decisiones anteriores.

Baseline consolidada:

```text
SESSION 29 → CLOSED

H29
→ SUPPORTED WITH QUALIFICATION

L3c SUBJECT STATUS
→ EXPERIMENTALLY ADDRESSED
→ STATE-ONLY
→ EXECUTION-VERIFIED within A/B

STATE / PRESENTATION AUTHORITY
→ SUPPORTED from existing subjectStates within tested scope

CAUSAL / VIEWER ATTRIBUTION
→ NOT INTRODUCED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c JOURNEY NARRATIVE
→ PRESERVED / OPEN

L4
→ PRESERVED / SOURCE-INSPECTION / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Artefactos en cuarentena:

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

DemoScript.subjectPresentations
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

H28 account presentation transport/format
→ LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED

H29 state-to-status mapping
→ LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED
```

---

### 1. PRESSURE SELECTED

Seleccionar exclusivamente:

```text
GuestPerspective.message
```

dentro de la presión narrativa restante de L3c.

No seleccionar todavía L4.

No modificar:

```text
sessionLabel
subjects[].label
subjects[].status
supervision
Activity
App
```

excepto instrumentación estrictamente necesaria para observar H30.

---

### 2. WHY A NEW RELATION IS NOW PERMITTED

H26 ya falsificó explícitamente la condición:

```text
NO-NEW-RELATION
```

para la narrativa situada de GuestPerspective.

El diagnóstico consolidado fue:

```text
operational/derived inputs
→ AVAILABLE

situated present-state narrative source
→ ABSENT
```

y observó exactamente la relación ausente:

```text
current situated journey position
→ appropriate situated narrative content
```

H26 además rechazó como fuentes:

```text
member
presenterLabel parsing
activityPresentation
news
brand
context IDs
subject IDs
Evidence type
markerRef
generic copy substitution as complete solution
```

Por tanto S30 NO debe repetir una búsqueda general de fuente existente como si esta ausencia no hubiera sido ya demostrada.

S30 autoriza estudiar una relación presentacional mínima nueva.

Preservar:

```text
previous falsification
→ permits new experiment

previous falsification
!=
preselects architectural shape
```

La forma y host de la relación siguen sin estar decididos.

---

### 3. H30 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
una relación presentacional explícita
puede asociar una posición operacional
ya existente y legítimamente distinguible
del recorrido

con contenido narrativo situado
de GuestPerspective.message,

de forma que A y B puedan presentar
narrativas distintas
manteniendo la misma estructura operacional,

sin convertir la representación narrativa
en autoridad sobre runtime, Evidence,
subjectStates, evaluación, K o claim,

y sin introducir viewer,
account→subject,
session→subject,
identidad humana,
TES Progression
ni una nueva máquina de estados.
```

La relación estudiada es conceptualmente:

```text
existing runtime position
→ situated message presentation
```

NO:

```text
message
→ runtime state
```

NO:

```text
message
→ Evidence
```

NO:

```text
message
→ evaluation
```

NO:

```text
message
→ viewer identity
```

---

### 4. FIRST REQUIRED STEP — RUNTIME POSITION ANALYSIS

ANTES de modificar contratos o aplicación, construir una matriz de las seis observaciones:

```text
initial
enlist-p1
discover-clue-a
activate-p2
discover-clue-b
reset
```

para A y B.

Registrar, como mínimo:

```text
runtime checkpoint
availableActionId
GuestPerspective.state
P1 subjectState
P2 subjectState
Evidence count
P1 Evidence count
P2 Evidence count
evaluation sufficiency
claim status
current message
next presenterLabel
```

La pregunta es:

```text
¿qué relación EXISTENTE identifica
de forma mínima, estable y no semánticamente abusiva
la posición operacional desde la que
debe seleccionarse presentación narrativa?
```

Comparar expresamente como candidatos:

```text
checkpoint

availableActionId

GuestPerspective.state

subjectStates combination

Evidence/evaluation combination
```

y cualquier discriminante ya existente que la inspección encuentre material.

No inventar un selector antes de completar esta comparación.

---

### 5. SELECTOR REQUIREMENTS

El selector candidato debe cumplir:

```text
A and B
→ same operational position
→ same selector identity
```

y debe distinguir todos los momentos que requieran narrativa diferente.

Especialmente comprobar que:

```text
exploring before P2 enabled
!=
exploring after P2 enabled
```

puede distinguirse sin:

```text
scenario.id
demoId
brandRef
member.name
subject presentation label
location literal
Evidence ID
markerRef parsing
```

`GuestPerspective.state` por sí solo NO debe seleccionarse si colapsa dos posiciones narrativamente distintas.

No ampliar sus valores para hacer pasar H30.

---

### 6. CHECKPOINT GUARDRAIL

`checkpoint` es un candidato importante porque ya pertenece al runtime local y participa en disponibilidad/transición.

Pero NO asumir su selección.

Si se selecciona, demostrar previamente:

```text
checkpoint A == checkpoint B
```

en posiciones operacionalmente equivalentes y:

```text
distinct required narrative position
→ distinct checkpoint
```

dentro del recorrido probado.

Preservar estrictamente:

```text
checkpoint
!=
TES Progression
```

```text
checkpoint
!=
Experience semantic phase
```

```text
checkpoint sequence
!=
TES Sequence
```

```text
checkpoint transition
!=
TES Event
```

Usarlo como discriminante técnico local no autoriza ninguna promoción semántica.

Si checkpoint no cumple los requisitos:

```text
REJECT AS SELECTOR
```

y continuar el análisis con los candidatos existentes.

No modificar checkpoint para hacerlo adecuado al experimento.

---

### 7. AVAILABLE ACTION GUARDRAIL

`availableActionId` también debe analizarse porque actualmente distingue las affordances disponibles.

Pero:

```text
available action
!=
journey state
```

y:

```text
presenterLabel
!=
journey narrative
```

No utilizar `presenterLabel` como message.

No parsearlo.

No transformar sus nombres o lugares.

Si `availableActionId` se usa como discriminante, debe añadirse una relación presentacional explícita; la coincidencia con un Script step no autoriza reutilizar el copy de affordance.

Debe estudiarse además qué sucede cuando:

```text
availableActionId = none
```

tras el resultado final.

No introducir un sentinel artificial sólo para completar una tabla.

---

### 8. CANDIDATE HOST ANALYSIS

Después de seleccionar —si es posible— un discriminante operacional legítimo, comparar como host al menos:

```text
ScenarioDefinition
DemoScript
GuestPerspectiveReadModel
Fixture
```

Criterios:

##### ScenarioDefinition

Ya contiene semántica operacional:

```text
subjects
contexts
checkpoints
actions
guards/transitions
```

Añadir copy situado puede mezclar presentación con definición operacional.

No descartarlo por convención; documentar la razón.

##### DemoScript

Ya contiene presentación situada de la demo y transporta experimentalmente:

```text
presenterLabel
activityPresentation
subjectPresentations
```

Por ello es candidato plausible para contenido narrativo situado.

Pero preservar:

```text
recurrent host usage
!=
universal presentation architecture
```

y:

```text
DemoScript
!=
PresentationModel
```

##### GuestPerspectiveReadModel

Es salida proyectada.

No convertir output en autoridad de su propia narrativa.

##### Fixture

Contiene datos simulados y account presentation, pero no declara actualmente relación entre posición operacional y narrativa.

No usar proximidad de contenido como autoridad.

---

### 9. PROVISIONAL EXPERIMENTAL SHAPE

NO implementar esta forma hasta completar el análisis anterior.

Si:

```text
DemoScript
```

resulta host legítimo y:

```text
checkpoint
```

resulta discriminante suficiente, puede ensayarse una forma mínima equivalente a:

```text
journeyPresentations?: [
  {
    checkpoint: "...",
    message: "..."
  }
]
```

Los nombres definitivos deben reflejar estrictamente el alcance experimental.

Si otro discriminante existente resulta más preciso y semánticamente más limpio, utilizarlo y documentar la razón.

NO crear:

```text
JourneyEngine
NarrativeEngine
PerspectiveEngine
PresentationRegistry
ContentRegistry
PhaseRegistry
MessageResolver
```

o equivalentes.

No crear una nueva entidad `JourneyPhase` sólo para H30.

---

### 10. NARRATIVE CONTENT CONSTRAINT

Los messages H30 deben ser:

```text
situated
presentational
non-authoritative
non-perspectival
```

Deben permitir distinguir A/B, especialmente:

```text
A → jardín / fuente
B → mirador / patio
```

cuando corresponda.

Pero NO introducir:

```text
tú
tu
te
por ti
has habilitado
estás
eres
contigo
```

ni formulaciones equivalentes que identifiquen al viewer.

Tampoco inferir género personal.

El experimento debe demostrar narrativa situada SIN resolver todavía:

```text
viewer/account/session
→ represented subject
```

---

### 11. COPY CONTENT SHOULD NOT CLAIM MORE THAN ITS POSITION

El nuevo message puede describir o presentar:

```text
situated exploration availability
situated clue already recorded
next operational opportunity
completion presentation where legitimately bound
```

pero no debe convertirse en autoridad factual.

Ejemplos conceptuales admisibles:

```text
Exploración disponible en el jardín.

Pista del jardín registrada.
La siguiente acción está disponible.

Nueva exploración disponible en la fuente.
```

Para B:

```text
Exploración disponible en el mirador.

Pista del mirador registrada.
La siguiente acción está disponible.

Nueva exploración disponible en el patio.
```

Son ejemplos semánticos, NO copy obligatorio.

Evitar expresiones que atribuyan el hecho a una persona o al viewer.

---

### 12. COMPLETION AUTHORITY

Prestar especial atención al message final.

Actualmente:

```text
evaluation.sufficiency == established
```

constituye fuente legítima para afirmar que la condición está establecida.

No sustituir automáticamente esa autoridad por:

```text
checkpoint
availableAction absence
Script presentation
```

Si el message final puede mantenerse como representación neutral del resultado derivado existente:

```text
evaluation
→ completion representation
```

preservar esa relación.

La nueva relación situada H30 no debe degradar una autoridad ya legítima.

Esto puede conducir a una construcción mixta:

```text
operational/derived authority
+
situated presentation where required
```

sin convertir ninguno de los dos planos en autoridad del otro.

Documentarlo si ocurre.

---

### 13. INITIAL / READY AUTHORITY

Aplicar el mismo análisis al estado inicial.

Si los datos operacionales existentes bastan para una representación neutral del tipo:

```text
adventure available
enlistment pending
```

no trasladarla automáticamente al nuevo artefacto sólo por uniformidad.

Preservar:

```text
new relation
→ only where evidence demonstrated it is needed
```

No maximizar el nuevo artefacto.

---

### 14. A CONTROL

Ejecutar A completo.

La narrativa situada debe corresponder con la presentación A cuando la nueva relación resulte aplicable:

```text
jardín
fuente
```

sin modificar:

```text
account presentation
subject labels
subject status
subject refs
operationalSessionSubjectRef
Evidence
Activity
context
evaluation
K
claim
available actions
checkpoint transitions
```

---

### 15. B CONTROL

Ejecutar B completo.

En las posiciones equivalentes debe aparecer narrativa B:

```text
mirador
patio
```

sin residuos narrativos A dentro de:

```text
GuestPerspective.message
```

cuando la posición dependa de la nueva relación situada.

Mantener:

```text
same operational selector
+
different declared presentation
→
different situated message
```

---

### 16. REPRESENTATION INDEPENDENCE CONTROL

Crear variantes X/Y que mantengan:

```text
same Scenario
same checkpoint/runtime position
same subjectStates
same account
same subjectPresentations
same Evidence
same Activity
same context
same evaluation
same K
same claim
```

y cambien únicamente la nueva presentación narrativa.

Debe resultar:

```text
message X != message Y

facts X == facts Y
runtime position X == runtime position Y
subject states X == subject states Y
evaluation X == evaluation Y
Activity X == Activity Y
```

El copy no puede modificar la posición desde la que se selecciona.

---

### 17. CROSS-COMPOSITION SELECTOR CONTROL

A y B deben demostrar:

```text
same semantic/operational journey position
→ same selector
```

pero:

```text
A declared narrative != B declared narrative
```

Debe resultar:

```text
A message != B message
```

sin usar:

```text
scenario.id
script.id
demoId
brand identity
```

como selector de comportamiento.

La diferencia debe proceder de la presentación declarada, no de una rama A/B en el projector.

---

### 18. SUBJECT PRESENTATION INDEPENDENCE

Cambiar únicamente:

```text
DemoScript.subjectPresentations
```

manteniendo la nueva presentación narrativa fija.

Debe resultar:

```text
subjects[].label changes
message unchanged
```

No interpolar labels dentro de message durante H30.

Esto evita que la nueva narrativa cree accidentalmente una segunda dependencia sobre la representación humana del sujeto.

---

### 19. ACCOUNT INDEPENDENCE

Cambiar únicamente:

```text
member.name
```

Debe resultar:

```text
sessionLabel changes
message unchanged
```

La narrativa situada no puede inferirse de cuenta ni utilizar la coincidencia cuenta/subject presentation.

---

### 20. ACTIVITY PRESENTATION INDEPENDENCE

Cambiar exclusivamente:

```text
activityPresentation
```

cuando el harness lo permita sin cambiar la acción factual.

Debe resultar:

```text
Activity representation changes
GuestPerspective.message unchanged
```

Preservar:

```text
occurred Activity representation
!=
present journey narrative
```

---

### 21. STATUS INDEPENDENCE / AUTHORITY

No utilizar los strings producidos por H29 para construir message.

Puede utilizarse el estado operacional subyacente como discriminante sólo si el análisis de selector lo justifica.

Preservar:

```text
status presentation
!=
message authority
```

y:

```text
subjectStates
!=
situated narrative content
```

El resultado positivo H29 no debe convertirse indirectamente en una fuente narrativa que H26 ya demostró insuficiente.

---

### 22. ABSENCE CONTROL

Si para una posición que requiere narrativa situada no existe una declaración presentacional aplicable:

```text
do not invent situated narrative
```

No utilizar como fallback:

```text
A hardcode
presenterLabel
activityPresentation
member
subject label
markerRef
news
brand copy
```

Observar qué representación mínima segura puede producirse sin sobreafirmación.

Si no existe ninguna:

```text
message → ""
```

es admisible experimentalmente antes que inventar contenido.

Esto NO constituye todavía una política productiva de UX.

Documentar claramente:

```text
absence behavior
→ local experiment
→ not promoted
```

---

### 23. MISMATCH CONTROL

Introducir una presentación declarada para un selector inexistente o no actual.

Debe observarse:

```text
no runtime position created
no checkpoint created
no action made available
no Evidence created
no evaluation change
no message selected from unrelated position
```

La presentación no puede crear el estado al que dice pertenecer.

---

### 24. NO VIEWER CONTROL

Comprobar explícitamente que los nuevos messages seleccionados no requieren una relación:

```text
viewer → subject
```

H30 queda fuera de cualquier justificación de:

```text
Tú eres P1
La cuenta representa P1
La sesión operacional identifica al viewer
P1 == authenticated user
```

Aunque el contenido anterior utilizase segunda persona, preservar:

```text
historical copy
!=
semantic authority
```

---

### 25. FACT / PRESENTATION CONTRADICTION CONTROL

Cuando sea posible en harness, declarar deliberadamente una variante narrativa que no coincida con la presentación comercial A/B, manteniendo el runtime igual.

El objetivo NO es aceptar UX falsa.

El objetivo es demostrar:

```text
presentation text
cannot change factual truth
```

Debe resultar:

```text
message changes
facts unchanged
evaluation unchanged
K unchanged
claim unchanged
```

Registrar la contradicción como:

```text
representational inconsistency
```

NO como cambio de hechos.

No diseñar en H30 un validador editorial para impedirla.

---

### 26. FALSIFIERS

H30 queda FALSIFIED si:

```text
no existing runtime discriminant
can distinguish the required narrative positions
without creating a new phase/state model
```

o si:

```text
situated narrative
must be parsed from presenterLabel
or activityPresentation
```

o si:

```text
message presentation
changes runtime checkpoint/state
```

o:

```text
changes Evidence attribution
```

o:

```text
changes evaluation/K/claim
```

o si requiere:

```text
viewer→subject
account→subject
session→subject
```

para funcionar.

También falsifica H30 si debe promover:

```text
checkpoint → TES Progression
```

o introducir:

```text
JourneyPhase
NarrativeEngine
PresentationEngine
Registry
Actor
Operator
Participant
Representative
```

o equivalentes.

También:

```text
App modification required
to make the GuestPerspective relation work
→ STOP
```

No resolver L4 para salvar H30.

---

### 27. DO NOT REUSE H25/H27 BY ANALOGY

Aunque H25, H27 y eventualmente H30 puedan terminar alojando relaciones presentacionales en DemoScript:

```text
multiple experimental presentation relations
!=
universal Script presentation contract
```

Si H30 resulta positiva registrar únicamente:

```text
recurring architectural pressure observed
```

No promover.

No crear ADR.

No crear PSC-P02.

No modificar TES.

---

### 28. HISTORICAL REGRESSION AND LIVE REGRESSION

Preservar las reproducciones históricas H21–H29.

Pero distinguir expresamente:

```text
historical replay
!=
current cumulative behavior verification
```

Además de los replay históricos, H30 debe ejecutar controles vivos del código actual sobre:

```text
A
B
Retail negative control
Arrival negative control
```

y verificar que la implementación actual conserva los resultados acumulados H25–H29 salvo exclusivamente:

```text
GuestPerspective.message
```

donde H30 autorice cambios.

No afirmar validación visual de App si no se ejecuta navegador.

---

### 29. L4 FREEZE

App permanece fuera de alcance.

Preservar visibles sus literales conocidos:

```text
Mi aventura · Aurora Stay
Busca las pistas del jardín y de la fuente durante tu estancia.
```

y los textos situados de supervisión detectados en H26.

No corregirlos durante H30.

Esos residuos deben seguir constituyendo evidencia para L4.

---

### 30. OUTPUT

Producir:

```text
session-30-script-bound-situated-journey-narrative.md
```

con al menos:

```text
H29 CONSOLIDATED INPUT

H30 HYPOTHESIS

VARIABLE UNDER TEST

WHY A NEW RELATION IS NOW PERMITTED

H26 NARRATIVE ABSENCE CONSOLIDATION

PRE-DELTA RUNTIME POSITION MATRIX

SELECTOR CANDIDATE ANALYSIS

SELECTOR DECISION

CHECKPOINT / TES SEPARATION

CANDIDATE HOST ANALYSIS

EXPERIMENTAL REPRESENTATION SHAPE

REPRESENTATION AUTHORITY

THREADING PATH

BASELINE

CODE DELTA

A CONTROL

B CONTROL

CROSS-COMPOSITION SELECTOR CONTROL

REPRESENTATION INDEPENDENCE CONTROL

ACCOUNT INDEPENDENCE CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

STATUS INDEPENDENCE CONTROL

ACTIVITY PRESENTATION INDEPENDENCE CONTROL

ABSENCE CONTROL

MISMATCH CONTROL

NO-VIEWER CONTROL

FACT / PRESENTATION CONTRADICTION CONTROL

CURRENT-LIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c SUBJECT STATUS STATUS

L3c JOURNEY NARRATIVE RESULT

L3c OVERALL STATUS

L4 STATUS

L5 STATUS

FALSIFICATION ANALYSIS

H30 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H30 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 31. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H30
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

JOURNEY POSITION SELECTOR
→ selected existing discriminant
  / insufficient

L3c JOURNEY NARRATIVE
→ status

NARRATIVE / FACT AUTHORITY SEPARATION
→ supported / unsupported

VIEWER RELATION
→ NOT INTRODUCED / introduced-invalidly

CHECKPOINT / TES PROGRESSION SEPARATION
→ preserved / violated / not applicable

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c SUBJECT STATUS
→ preserved / experimentally addressed H29

L3c OVERALL
→ status

L4
→ preserved / source-inspection / open

L5
→ preserved / experimentally addressed H25

RECURRING PRESENTATION PRESSURE
→ observed / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H31 automáticamente.

---

### 32. METHODOLOGICAL GUARDRAIL

Preservar:

```text
knowing runtime position
!=
having situated narrative

having situated narrative
!=
creating runtime position

checkpoint
!=
TES Progression

available action
!=
journey state

presenterLabel
!=
journey message

Activity history
!=
present journey narrative

message presentation
!=
factual authority

same operational route
+
different situated composition
→
may legitimately produce different presentation

different presentation
→
must not produce different facts
```

El objetivo de S30 no es conseguir copy bonito.

El objetivo es determinar si la Factoría puede declarar explícitamente narrativa situada vinculada a una posición operacional ya existente sin convertir presentación en semántica, estado o autoridad factual.
<!-- FIN-TEXTO-ORIGINAL-S30 -->

---

<a id="sesion-31"></a>

## Capítulo 31 — Auditoría del framing introductorio de App

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-31-original.md) de `2026.zip`, registro `2026/09/17/rollout-2026-09-17T22-18-33-01a0b13c-4a03-7702-8be0-e7dcf49af57e.jsonl`. Mensaje de usuario en la línea 129; salida(s) de lectura en la(s) línea(s) 135. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 3a885cf11f6f38b003f8c048d7a9394c38834e94603cf2a78b8acfaa6e3b60d8.

<!-- INICIO-TEXTO-ORIGINAL-S31 -->
### SESIÓN 31 — APPLICATION COMPOSITION FRAMING PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 30 — Script-bound Situated Journey Narrative
```

No reconstruir decisiones anteriores.

#### BASELINE CONSOLIDADA

```text
SESSION 30 → CLOSED

H30
→ SUPPORTED WITH QUALIFICATION

JOURNEY POSITION SELECTOR
→ existing availableActionId
→ EXECUTION-VERIFIED within Family Adventure A/B
→ NOT UNIVERSALIZED

checkpoint
→ REJECTED AS H30 SELECTOR
→ semantics unchanged

L3c JOURNEY NARRATIVE
→ EXPERIMENTALLY ADDRESSED
→ EXECUTION-VERIFIED within A/B

NARRATIVE / FACT AUTHORITY SEPARATION
→ SUPPORTED within tested scope

VIEWER RELATION
→ NOT INTRODUCED

L3c OVERALL
→ EXPERIMENTALLY ADDRESSED within A/B
→ NOT PROMOTED

L4
→ PRESERVED / SOURCE-INSPECTION / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING PRESENTATION PRESSURE
→ OBSERVED
→ NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Artefactos experimentales H25–H30 permanecen en cuarentena.

No promocionar DemoScript.

---

### 1. PRESSURE SELECTED

Seleccionar exclusivamente dentro de L4:

```text
APPLICATION COMPOSITION FRAMING
```

Los síntomas conocidos incluyen:

```text
"Mi aventura · Aurora Stay"

"Busca las pistas del jardín y de la fuente durante tu estancia."
```

o sus equivalentes actuales en App.

NO seleccionar todavía los residuos de Supervision:

```text
"P1 · Lucía"
"P2 · Huésped 2"
"Cuenta/sesión operativa"
```

Deben permanecer visibles.

Esta separación de L4 es diagnóstica, no contractual.

No crear L4a/L4b como taxonomía estable salvo necesidad posterior demostrada.

---

### 2. H31 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
las relaciones y artefactos ya existentes
pueden proporcionar a App
una presentación situada de framing
para la composición seleccionada,

de modo que A y B puedan mostrar
su framing correspondiente

sin hardcodes específicos de A en App,

sin crear una nueva relación semántica,
sin derivar framing desde GuestPerspective.message,
sin agregar o parsear presentation copy,
sin modificar runtime, Evidence, evaluación,
K o claim,

y manteniendo App como consumidor,
no como autoridad de composición.
```

H31 prueba inicialmente:

```text
EXISTING RELATIONS ONLY
```

No está autorizada todavía una nueva relación declarativa de framing.

---

### 3. VARIABLE UNDER TEST

Exclusivamente la procedencia de los elementos de App equivalentes a:

```text
application adventure title
application adventure introductory / framing text
```

Actualmente materializados mediante literales equivalentes a:

```text
Mi aventura · Aurora Stay
Busca las pistas del jardín y de la fuente durante tu estancia.
```

No modificar en H31:

```text
GuestPerspective.sessionLabel
GuestPerspective.subjects[].label
GuestPerspective.subjects[].status
GuestPerspective.message
Activity
SupervisionPerspective
Evidence
evaluation
runtime
```

No resolver otros literales App incidentalmente.

---

### 4. FIRST REQUIRED STEP — COMPLETE APP LITERAL INVENTORY

Antes de modificar código, inspeccionar App y producir un inventario de todo literal o composición de copy que pueda ser:

```text
generic application UI
composition-specific presentation
GuestPerspective rendering
Supervision rendering
Activity rendering
debug / diagnostic presentation
```

La inspección debe identificar al menos:

```text
source file / component
literal or expression
rendering surface
whether A-specific
existing source candidates
```

Pero H31 sólo seleccionará para experimento:

```text
application composition framing
```

El resto queda como evidencia L4.

No corregirlo.

---

### 5. FRAMING DECOMPOSITION

Descomponer semánticamente el framing actual.

Para el título, distinguir si contiene:

```text
generic shell label
+
property / brand / composition-specific label
```

Por ejemplo, no asumir que:

```text
"Mi aventura"
```

y:

```text
"Aurora Stay"
```

poseen la misma procedencia.

Para el texto introductorio distinguir:

```text
generic Experience framing
+
composition-specific situated content
```

Por ejemplo:

```text
jardín
fuente
```

puede ser contenido situado aunque:

```text
Busca las pistas...
```

sea framing genérico.

Esta descomposición es diagnóstica.

No convertirla automáticamente en campos o contratos.

---

### 6. EXISTING SOURCE INSPECTION

Inspeccionar todos los candidatos existentes relevantes, incluidos cuando existan:

```text
resolved demo / manifest metadata
Experience definition
Scenario
DemoScript metadata
Fixture
brand / property data
snapshot/read models
resolved runtime
composition artifacts
```

Para cada componente de framing preguntar:

```text
¿existe una relación DECLARADA
que autorice exactamente
esta presentación?
```

Preservar:

```text
having Aurora Stay somewhere
!=
having application-title authority

having jardín/fuente somewhere
!=
having adventure-summary authority

having situated messages
!=
having composition framing

having Activity presentations
!=
having static itinerary summary
```

---

### 7. FORBIDDEN SOURCE REUSE

NO construir framing mediante:

```text
parsing presenterLabel
parsing activityPresentation
aggregating experimentalJourneyPresentations
extracting place names from message
extracting labels from Activity
parsing markerRef
parsing IDs
scenario.id branching
demoId branching
brand.id branching
subject labels
Evidence payload parsing
news copy reuse
```

salvo que la inspección demuestre una relación ya declarada cuya semántica sea exactamente la requerida.

Coexistencia de texto no equivale a autoridad.

Especialmente:

```text
H30 journey narrative
!=
application static framing
```

y:

```text
H25 Activity presentation
!=
Experience itinerary description
```

---

### 8. TITLE SOURCE ANALYSIS

Analizar de forma independiente:

```text
generic title component
composition-specific title component
```

Si existe actualmente una fuente legítima, documentar:

```text
source
→ threading
→ App consumer
```

Si, por ejemplo, existe un nombre explícito de propiedad/composición, verificar qué semántica declara realmente antes de usarlo.

No asumir:

```text
brand == property
member == property
context ID == display name
scenario identity == title
```

Si sólo existe el dato pero no la relación:

```text
STOP for that component
```

---

### 9. INTRODUCTORY FRAMING SOURCE ANALYSIS

Investigar separadamente el texto equivalente a:

```text
Busca las pistas del jardín y de la fuente durante tu estancia.
```

Preguntar si existe una fuente legítima para:

```text
Experience-level situated framing
```

No inferirla de la suma de las posiciones H30.

Preservar:

```text
three position-specific messages
!=
declared itinerary summary
```

También:

```text
two Activity presentations
!=
declared Experience description
```

y:

```text
two clue locations
!=
authority to state
"Busca las pistas X e Y..."
```

Si no existe una relación declarada:

```text
STOP
→ record missing relationship
→ do not create it in S31
```

---

### 10. ALL-OR-STOP APPLICATION DELTA RULE

H31 debe completar primero la inspección de:

```text
title
+
introductory framing
```

ANTES de modificar App.

Si cualquiera de los componentes necesarios para eliminar el framing específico de A carece de fuente legítima:

```text
H31 NO-NEW-RELATION
→ INSUFFICIENT
→ STOP
```

En ese caso:

```text
NO partial App correction
NO new framing field
NO fallback to A
NO aggregation from H25/H30
```

Conservar App intacta para mantener visible la presión.

Registrar por separado las fuentes legítimas que sí se hayan encontrado.

No reparar sólo el título si el framing seleccionado sigue dependiendo de una relación ausente.

---

### 11. IF EXISTING SOURCES ARE SUFFICIENT

Sólo si title + introductory framing tienen fuentes legítimas existentes, está autorizado un delta mínimo.

La dirección debe ser:

```text
existing authoritative composition source
→ existing/minimal transport
→ App presentation
```

App no puede importar directamente artefactos concretos A/B para resolver copy.

No:

```text
App
→ artifacts.ts
```

No:

```text
App
→ costa-artifacts.ts
```

No branching:

```text
if demo === A ...
if scenario.id === ...
```

App debe seguir siendo consumidor.

---

### 12. TRANSPORT VS RELATION

Distinguir explícitamente:

```text
missing transport
!=
missing semantic/presentational relation
```

Puede existir una fuente legítima cuyo dato todavía no alcance App.

Si la relación ya está declarada pero falta transporte, documentarlo.

Un transporte mínimo local puede ensayarse únicamente si:

```text
source semantics already authorize the output
```

Clasificar ese transporte como:

```text
EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
```

No crear arquitectura general para transportar dos strings.

Si transportar el dato requiere inventar primero qué significa:

```text
STOP
```

---

### 13. A CONTROL

Si H31 supera la condición no-new-relation:

A debe presentar framing A desde las fuentes identificadas.

Verificar que no depende de hardcodes App equivalentes a:

```text
Aurora Stay
jardín
fuente
```

excepto si alguno de esos textos forma parte legítima de un artefacto presentado a App desde la composición.

Mantener intactos:

```text
account presentation H28
subject presentation H27
subject status H29
journey narrative H30
Activity H25
Evidence
evaluation
K
claim
```

---

### 14. B CONTROL

B debe presentar framing correspondiente a sus fuentes existentes.

NO prescribir de antemano el literal B.

Códex debe registrar exactamente:

```text
declared source
→ observed B framing
```

No inventar:

```text
Costa Clara
mirador
patio
```

en una capa nueva simplemente porque esos valores ya sean conocidos en otros artefactos.

Si las fuentes existentes no pueden producir framing B legítimamente:

```text
H31 FALSIFIED / INSUFFICIENT
```

No hardcodear B.

---

### 15. COMPOSITION SWITCH CONTROL

Si el harness actual permite instanciar A/B con la misma App:

```text
same application code
+
different resolved composition
→
different framing where declared
```

Debe demostrarse sin cambiar:

```text
App source
projection behavior
runtime rules
```

La diferencia debe proceder exclusivamente de fuentes de composición legítimas.

Si App no dispone actualmente de una frontera mediante la cual recibir esa información, distinguir:

```text
missing transport boundary
```

de:

```text
missing semantic relation
```

No fusionar ambos problemas.

---

### 16. READ-MODEL PRESERVATION

H31 NO debe mover hacia App autoridad que actualmente pertenece al read model.

Preservar:

```text
sessionLabel
→ H28 authority

subject labels
→ H27 authority

subject status
→ H29 authority

journey message
→ H30 mixed authority

Activity representation
→ H25 authority
```

App sólo renderiza esos outputs.

No reconstruirlos localmente.

---

### 17. RECURRING SCRIPT PRESENTATION PRESSURE

S30 consolidó:

```text
H25 → Script-bound Activity presentation
H27 → Script-bound subject presentation
H30 → Script-bound situated journey narrative
```

H31 debe observar esta recurrencia pero NO utilizarla como permiso para:

```text
put framing in DemoScript
```

sin evidencia.

Preservar:

```text
recurring host
!=
authority for new presentation relation
```

H31 puede aportar nueva evidencia a esa presión.

No debe resolverla arquitectónicamente.

---

### 18. SUPERVISION FREEZE

Conservar intactos en esta sesión los outputs/literales equivalentes a:

```text
P1 · Lucía
P2 · Huésped 2
Cuenta/sesión operativa
```

No usar H27 subjectPresentations automáticamente para corregirlos.

Preservar:

```text
GuestPerspective subject representation
!=
SupervisionPerspective representation
```

hasta que se estudie su autoridad.

---

### 19. NEGATIVE CONTROLS

Retail y Arrival deben permanecer sin cambios.

H31 no debe obligarles a adoptar:

```text
Family Adventure framing
DemoScript situated framing
journey presentations
```

Si el transporte nuevo provoca requerimientos artificiales en verticales no relacionadas:

```text
STOP
```

No crear defaults semánticos para hacer pasar controles negativos.

---

### 20. APP EXECUTION REQUIREMENT

A diferencia de H25–H30, L4 pertenece explícitamente a App.

Por tanto, si existe delta de aplicación en H31, no basta con probar projector/provider.

Debe verificarse la aplicación actual.

Usar la capacidad de render/integration test disponible en el repositorio.

Si existe navegador o infraestructura equivalente disponible, ejecutar A y B a través de App.

Si sólo existe jsdom/integration rendering:

```text
record as DOM/integration verification
```

y NO llamarlo validación visual.

Registrar claramente:

```text
browser visual validation
→ executed / not executed
```

No inferirla.

Si H31 termina por STOP antes de modificar App, la inspección de fuente basta para el veredicto no-new-relation.

---

### 21. HISTORICAL VS CURRENT TESTS

Preservar:

```text
historical replay
!=
current cumulative behavior verification
```

Los harness H21–H30 pueden continuar verificando sus baselines históricas.

Pero cualquier afirmación sobre App actual debe proceder de:

```text
current source inspection
+
current live/integration execution
```

no de projectors históricos archivados.

---

### 22. FALSIFIERS

H31 queda FALSIFIED para la condición NO-NEW-RELATION si:

```text
App composition title
requires a presentation relationship
that does not exist
```

o si:

```text
introductory framing
requires a presentation relationship
that does not exist
```

o si sólo puede construirse mediante:

```text
parsing
aggregation
ID branching
copy reuse
hardcodes A/B
```

o si requiere convertir:

```text
H30 messages
→ Experience summary
```

o:

```text
H25 Activity
→ itinerary definition
```

o si App debe convertirse en autoridad para decidir qué significa la composición.

También STOP si eliminar los hardcodes exige simultáneamente resolver:

```text
SupervisionPerspective
viewer identity
account→subject
```

Esas son presiones distintas.

---

### 23. POSSIBLE POSITIVE VERDICT

Sólo si las relaciones existentes bastan:

```text
H31
→ SUPPORTED WITH QUALIFICATION
```

y:

```text
L4 APPLICATION COMPOSITION FRAMING
→ EXISTING-SOURCE / EXECUTION-VERIFIED
```

con los límites concretos encontrados.

---

### 24. POSSIBLE FALSIFICATION VERDICT

Si falta una relación legítima:

```text
H31
→ FALSIFIED

NO-NEW-RELATION
→ INSUFFICIENT
```

Registrar exactamente:

```text
which framing component lacks authority
what data exists
what relationship is missing
why existing presentation artifacts cannot substitute it
```

No crear el artefacto nuevo en S31.

Una sesión posterior podrá autorizar un experimento mínimo.

---

### 25. OUTPUT

Producir:

```text
session-31-application-composition-framing-provenance.md
```

con al menos:

```text
H30 CONSOLIDATED INPUT

H31 HYPOTHESIS

VARIABLE UNDER TEST

WHY L4 IS DIAGNOSTICALLY SPLIT

CURRENT APP LITERAL INVENTORY

FRAMING DECOMPOSITION

EXISTING SOURCE INVENTORY

TITLE SOURCE ANALYSIS

INTRODUCTORY FRAMING SOURCE ANALYSIS

DATA / RELATION DISTINCTION

TRANSPORT / RELATION DISTINCTION

NO-NEW-RELATION ANALYSIS

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

COMPOSITION SWITCH CONTROL

READ-MODEL PRESERVATION

NEGATIVE CONTROLS

CURRENT APP EXECUTION

BROWSER / DOM VERIFICATION STATUS

SUPERVISION FREEZE

RECURRING PRESENTATION PRESSURE

FALSIFICATION ANALYSIS

H31 VERDICT

L4 FRAMING RESULT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H31 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 26. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H31
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

APP TITLE AUTHORITY
→ status

APP INTRODUCTORY FRAMING AUTHORITY
→ status

APP CONSUMER BOUNDARY
→ preserved / violated / unresolved

A/B COMPOSITION FRAMING
→ execution-verified / not established

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c
→ preserved / experimentally addressed H29–H30

L4 APPLICATION FRAMING
→ status

L4 SUPERVISION
→ preserved / open

L5
→ preserved / experimentally addressed H25

RECURRING PRESENTATION PRESSURE
→ observed / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H32 automáticamente.

---

### 27. METHODOLOGICAL GUARDRAIL

Preservar:

```text
having a value
!=
having framing authority

having situated journey copy
!=
having Experience summary

having Activity location copy
!=
having itinerary definition

App rendering
!=
App semantic authority

missing transport
!=
missing relationship

same App
+
different legitimate composition source
→
may produce different framing

different hardcoded App copy
→
is not composition

recurrence
!=
promotion
```

S31 debe responder primero:

```text
¿la Factoría ya sabe legítimamente
qué debe presentar App
como framing de esta composición?
```

antes de responder:

```text
¿cómo hacemos que App lo muestre?
```

Si la primera respuesta es negativa:

```text
STOP
```

No diseñar el artefacto que falta dentro de la baseline falsificada.
<!-- FIN-TEXTO-ORIGINAL-S31 -->

---

<a id="sesion-32"></a>

## Capítulo 32 — Introducción explícita de composición

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-32-original.md) de `2026.zip`, registro `2026/09/17/rollout-2026-09-17T22-18-33-01a0b13c-4a03-7702-8be0-e7dcf49af57e.jsonl`. Mensaje de usuario en la línea 210; salida(s) de lectura en la(s) línea(s) 216. Cotejo adicional: adjunto repetido. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 75244f7bb7e2e1fa0a3ea1a150f003ae0ef8818884a47f19af6fa827b91152d2.

<!-- INICIO-TEXTO-ORIGINAL-S32 -->
### SESIÓN 32 — EXPLICIT COMPOSITION INTRODUCTORY FRAMING

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 31 — Application Composition Framing Provenance
```

No reconstruir decisiones anteriores.

---

### 1. BASELINE CONSOLIDADA

```text
SESSION 31 → CLOSED

H31
→ FALSIFIED

NO-NEW-RELATION
→ INSUFFICIENT

APP TITLE / EYEBROW AUTHORITY
→ UI shell + resolved brand name AVAILABLE
→ branding interpretation only
→ local transport to HomePage missing

APP INTRODUCTORY FRAMING AUTHORITY
→ MISSING DECLARED RELATION

APP CONSUMER BOUNDARY
→ PRESERVED

A/B COMPOSITION FRAMING
→ NOT ESTABLISHED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 APPLICATION FRAMING
→ SOURCE-INSPECTED / STOP / OPEN

L4 SUPERVISION
→ PRESERVED / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING PRESENTATION PRESSURE
→ OBSERVED / NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Todos los artefactos experimentales H25–H30 permanecen en cuarentena.

---

### 2. WHY A NEW RELATION IS NOW PERMITTED

H31 ha demostrado:

```text
relevant composition data exists
!=
declared introductory framing relation
```

Concretamente:

```text
H25 Activity presentations
H30 situated journey presentations
News content
Scenario contexts
Script affordances
```

contienen datos que podrían parecer utilizables para construir un resumen, pero ninguna relación existente declara:

```text
selected composition
→ authorized static introductory framing
```

Por tanto:

```text
H31 NO-NEW-RELATION
→ FALSIFIED
```

y una sesión posterior puede ahora autorizar un experimento mínimo sobre esa relación.

H32 es esa sesión.

Preservar:

```text
previous falsification
→ permission to test missing relation

previous falsification
!=
permission to design general presentation architecture
```

---

### 3. PRESSURE SELECTED

Seleccionar exclusivamente:

```text
COMPOSITION-SPECIFIC STATIC INTRODUCTORY FRAMING
```

para la rama Family Adventure de App.

NO seleccionar:

```text
huntName provenance
SupervisionPerspective labels
Cuenta/sesión operativa
fixed generic link to Family Adventure
document title
generic Activity copy
loading/error copy
viewer identity
```

No resolver incidentalmente otros hallazgos del inventario S31.

---

### 4. H32 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de Family Adventure,
una relación presentacional explícita y mínima
puede asociar la composición situada seleccionada
con una presentación introductoria estática,

de modo que A y B puedan declarar
introducciones diferentes

sin derivarlas mediante parsing,
agregación de otras presentaciones,
IDs, Evidence, Activity o journey message,

sin modificar Experience semantics,
Scenario semantics,
runtime state,
Evidence,
evaluation,
K o claim,

y manteniendo App como consumidor.
```

Además, la fuente de branding ya existente puede transportarse de forma independiente para completar el eyebrow:

```text
UI shell label
+
resolved brand.name
```

sin incorporarla a la nueva relación introductoria.

---

### 5. TWO-AUTHORITY COMPOSITION TEST

H32 debe probar explícitamente que el framing de App puede construirse mediante dos autoridades independientes:

```text
"Mi aventura"
→ generic UI shell authority

runtime.brand.name
→ existing resolved branding authority

NEW introductory framing relation
→ static situated introductory presentation
```

No crear una estructura única sólo para agruparlas.

Preservar:

```text
co-rendered presentation
!=
single semantic authority
```

y:

```text
same visual header
!=
same source responsibility
```

---

### 6. VARIABLE UNDER TEST

La relación nueva afecta exclusivamente al texto introductorio equivalente al actual:

```text
Busca las pistas del jardín y de la fuente durante tu estancia.
```

La corrección del eyebrow:

```text
Mi aventura · Aurora Stay
```

puede ejecutarse en H32 únicamente mediante transporte de:

```text
runtime.brand.name
```

porque H31 ya acreditó esa relación como branding.

NO crear un nuevo campo para el nombre de marca.

NO crear:

```text
compositionTitle
propertyName
experiencePropertyName
```

para resolver el eyebrow.

El verdadero:

```text
h1 = adventure.huntName
```

permanece congelado.

---

### 7. FIRST REQUIRED STEP — CANDIDATE HOST ANALYSIS

Antes del delta, comparar como mínimo:

```text
Manifest
ExperienceDefinition
ScenarioDefinition
DemoScript
Fixture
new dedicated artifact
```

Para cada candidato documentar:

```text
current responsibility
A/B variability
semantic coupling introduced
transport path
reversibility
whether it changes an existing authority
```

No seleccionar host únicamente porque pueda almacenar un string.

---

### 8. EXPERIENCE CANDIDATE

Family Adventure Experience es compartida entre A/B.

Comprobar si introducir framing situado ahí exigiría:

```text
duplicating Experience
composition override
situated semantics inside shared Experience
```

Si es así, rechazar como host para este experimento.

Preservar:

```text
Experience identity
!=
composition-specific presentation
```

salvo evidencia contraria.

No modificar Experience sólo para conseguir variación A/B.

---

### 9. SCENARIO CANDIDATE

Scenario distingue A/B y contiene:

```text
subjects
contexts
actions
guards
checkpoints
transitions
```

Analizar si añadir framing estático supondría mezclar:

```text
operational definition
+
editorial presentation
```

No descartarlo por convención.

Pero no ampliar semántica de Scenario sin necesidad demostrada.

Preservar:

```text
Scenario
!=
automatic presentation authority
```

---

### 10. MANIFEST CANDIDATE

Manifest define la composición deseada mediante referencias explícitas.

Analizar si alojar copy directamente allí mezclaría:

```text
composition selection/configuration
+
editorial content
```

Preservar:

```text
composition root
!=
automatic content host
```

No convertir manifest en un contenedor de strings sólo porque selecciona A/B.

---

### 11. FIXTURE CANDIDATE

Fixture contiene:

```text
member
coupons
news
activity records
```

H31 ya demostró que:

```text
news content
!=
introductory framing authority
```

No reutilizar ni promover una NewsReadModel.

Sólo seleccionar Fixture si aparece una relación declarada compatible, no por proximidad de contenido.

---

### 12. DEMOSCRIPT CANDIDATE

DemoScript ya transporta experimentalmente:

```text
presenterLabel
activityPresentation
subjectPresentations
experimentalJourneyPresentations
```

y varía entre A/B.

Por ello es candidato material.

Pero preservar:

```text
previous recurring use
!=
automatic authority
```

La decisión debe responder específicamente:

```text
¿el framing introductorio es presentación situada
de esta composición/demostración
sin autoridad operacional?
```

Si la respuesta queda respaldada por responsabilidades existentes y por los controles, DemoScript puede seleccionarse experimentalmente.

No convertirlo en:

```text
PresentationModel
CompositionPresentationModel
ContentRegistry
```

---

### 13. NEW DEDICATED ARTIFACT CANDIDATE

Analizar brevemente si una entidad nueva sería necesaria para expresar la relación.

Aplicar principio de minimalidad:

```text
if existing bounded host
can express the tested relation
without semantic corruption
→ do not create a new architectural entity
```

Crear un artefacto nuevo únicamente si los hosts existentes falsifican el experimento.

No hacerlo por anticipación arquitectónica.

---

### 14. EXPERIMENTAL SHAPE

No implementar antes de seleccionar host.

Si DemoScript resulta el host mínimo legítimo, puede ensayarse algo estrictamente equivalente a:

```ts
// EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
experimentalIntroductoryFraming?: string;
```

El nombre final puede variar si existe otro que describa mejor el alcance.

NO utilizar todavía:

```ts
presentation: {
  title,
  intro,
  subjects,
  journey,
  activity
}
```

NO consolidar H25/H27/H30/H32 dentro de una estructura común.

Eso sería una hipótesis arquitectónica distinta.

---

### 15. CONTENT CONSTRAINT

Las declaraciones canónicas A/B deben ser:

```text
composition-specific
static
introductory
non-authoritative
non-perspectival
```

Pueden declarar lugares o encuadre editorial porque precisamente ésa es la relación explícita bajo ensayo.

Pero no deben introducir:

```text
tú
tu
te
eres
estás
tu estancia
has encontrado
has habilitado
```

ni formulaciones equivalentes.

H32 NO introduce:

```text
viewer → subject
viewer → stay
account → stay owner
```

La desaparición del histórico:

```text
durante tu estancia
```

debe considerarse reducción de una afirmación no acreditada, no pérdida semántica demostrada.

---

### 16. A CANONICAL CONTROL

La composición A debe declarar explícitamente su introducción situada.

El copy exacto debe documentarse como declaración, no derivación.

Conceptualmente puede expresar:

```text
jardín
fuente
```

sin perspectiva personal.

No prescribir literalmente una frase concreta si el vocabulario actual del proyecto ofrece una formulación mejor.

Debe comprobarse:

```text
A declared introductory presentation
→ A intro rendered
```

sin consultar:

```text
H25 activityPresentation
H30 journeyPresentations
News
markerRef
scenario.id
demoId
```

---

### 17. B CANONICAL CONTROL

B debe declarar explícitamente una introducción distinta.

Conceptualmente:

```text
mirador
patio
```

pero el contenido concreto debe proceder de la declaración H32, no inferirse de otros artefactos.

Debe cumplirse:

```text
same App code
+
different resolved composition
+
different declared intro
→
different rendered introduction
```

---

### 18. BRAND TRANSPORT CONTROL

El eyebrow debe pasar de hardcode:

```text
Mi aventura · Aurora Stay
```

a una composición equivalente a:

```text
generic UI label
+
runtime.brand.name
```

Debe observarse:

```text
A → Aurora Stay
B → Costa Clara Resort
```

estrictamente como branding.

No afirmar:

```text
Aurora Stay = property
Costa Clara Resort = property
```

No utilizar context property ID para mostrar esos nombres.

---

### 19. BRAND / INTRO INDEPENDENCE CONTROL

Cambiar únicamente el nombre de BrandArtifact en una variante de harness:

```text
brand.name X → brand.name Y
```

manteniendo idéntica la declaración introductoria.

Debe resultar:

```text
eyebrow X != eyebrow Y
intro X == intro Y

facts X == facts Y
runtime behavior X == Y
evaluation X == Y
```

Y el control inverso:

```text
same brand
different introductory declaration
```

debe resultar:

```text
eyebrow X == eyebrow Y
intro X != intro Y
```

Esto debe demostrar:

```text
brand presentation
!=
composition introductory presentation
```

---

### 20. REPRESENTATION INDEPENDENCE CONTROL

Variantes X/Y:

```text
same manifest references
same brand
same Experience
same Scenario
same fixture
same subjectPresentations
same journeyPresentations
same Activity presentations
same runtime
same Evidence
same evaluation

different introductory framing
```

Debe resultar:

```text
rendered introduction X != Y

all factual/runtime/evaluation outputs X == Y
```

La presentación no puede modificar la composición factual.

---

### 21. FACT / PRESENTATION CONTRADICTION CONTROL

Declarar intencionadamente un framing editorial contradictorio en una variante exclusiva del harness.

Por ejemplo, una introducción que nombre otro lugar.

Debe observarse:

```text
rendered intro changes

Scenario unchanged
Activity unchanged
journey message unchanged
Evidence unchanged
context unchanged
evaluation unchanged
K unchanged
claim unchanged
```

Clasificar:

```text
representational inconsistency
```

NO:

```text
factual mutation
```

No crear en H32 un sistema de validación editorial.

---

### 22. ABSENCE CONTROL

Cuando Family Adventure carezca de nueva declaración introductoria:

```text
do not reconstruct it
```

No fallback desde:

```text
A hardcode
H25
H30
News
Scenario contexts
Evidence
markerRef
brand
```

La representación segura puede ser:

```text
intro absent / not rendered
```

o string vacío según la forma mínima de App.

Documentar la decisión.

Esto es:

```text
LOCAL EXPERIMENTAL ABSENCE BEHAVIOR
```

no política UX productiva.

---

### 23. ACCOUNT / SUBJECT / STATUS / JOURNEY INDEPENDENCE

Perturbar independientemente, reutilizando cuando sea razonable los patrones de harness existentes:

```text
member.name
subjectPresentations
subjectStates
experimentalJourneyPresentations
activityPresentation
```

Ninguno debe modificar la introducción H32.

Y cambiar la introducción H32 no debe modificar:

```text
sessionLabel
subjects[].label
subjects[].status
GuestPerspective.message
Activity
```

Preservar las autoridades H25/H27/H28/H29/H30.

---

### 24. APP CONSUMER BOUNDARY

La dirección debe ser:

```text
resolved composition
→ selected explicit presentation source
→ minimal transport
→ App
```

No:

```text
App
→ infer composition meaning
```

App no debe importar:

```text
artifacts.ts
costa-artifacts.ts
fixtures.ts
```

para resolver el copy.

No branching:

```text
if demoId ...
if scenario.id ...
if brand.id ...
```

para seleccionar introducción.

App sólo consume.

---

### 25. NO READ-MODEL REUSE

No introducir la nueva intro dentro de GuestPerspective sólo para transportarla si su responsabilidad no es GuestPerspective.

Analizar expresamente si:

```text
composition introductory framing
```

pertenece al snapshot/read model existente o si puede llegar a App desde resolved runtime/composition.

Preservar:

```text
transport convenience
!=
semantic ownership
```

No ensanchar GuestPerspective por conveniencia de props.

---

### 26. CURRENT APP EXECUTION REQUIRED

H32 sí modifica App si la hipótesis se sostiene.

Por tanto debe ejecutar código actual.

Como mínimo:

```text
A current App integration/DOM
B current App integration/DOM
```

y verificar:

```text
A eyebrow
A introduction

B eyebrow
B introduction
```

sobre la aplicación vigente.

Si existe sólo jsdom:

```text
DOM / integration verification
```

No llamarlo browser visual validation.

Si existe navegador real disponible y es razonable utilizarlo, registrar por separado:

```text
browser visual validation
→ EXECUTED / NOT EXECUTED
```

No confundir ambos.

---

### 27. COMPOSITION SWITCH CONTROL

Comprobar mediante instancias A/B:

```text
same App source
same rendering path
different resolved composition
→ different brand + intro where declared
```

No exigir necesariamente hot-switch sin remount si la arquitectura actual selecciona composición en bootstrap.

Documentar exactamente el mecanismo probado.

---

### 28. NEGATIVE CONTROLS

Retail y Arrival no deben adquirir framing Family Adventure por default.

La nueva relación debe ser opcional o acotada de modo compatible con esos controles.

No introducir:

```text
fake generic introductory framing
```

para hacer pasar tipos o UI.

Si esos productos no declaran framing H32:

```text
absence remains absence
```

salvo copy genérico que ya sea legítimamente UI local.

---

### 29. HUNTNAME FREEZE

Preservar:

```text
adventure.huntName
```

exactamente como está durante H32.

S31 detectó:

```text
Experience.name exists
GuestPerspective.huntName exists
```

pero no una relación de threading entre ambos.

No resolverla incidentalmente.

Registrar como presión observada si sigue siendo material.

---

### 30. SUPERVISION FREEZE

Preservar:

```text
P1 · Lucía
P2 · Huésped 2
Cuenta/sesión operativa
```

No reutilizar H27 automáticamente.

GuestPerspective y SupervisionPerspective continúan separados.

No resolver viewer/account/session→subject.

---

### 31. FIXED NAVIGATION LINK FREEZE

Preservar el acceso fijo:

```text
/?demo=hospitality-family-adventure
```

detectado en S31.

No corregirlo incidentalmente.

Es una presión de composición/navegación distinta de introductory framing.

---

### 32. RECURRING PRESENTATION PRESSURE

Si DemoScript vuelve a resultar host legítimo, registrar:

```text
H25 → activity presentation
H27 → subject presentation
H30 → journey narrative
H32 → composition introductory framing
```

como:

```text
RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ STRENGTHENED
→ NOT PROMOTED
```

No concluir todavía:

```text
DemoScript = PresentationModel
```

No crear:

```text
PresentationBoundary
PresentationRegistry
PresentationEngine
CompositionPresentation
```

sólo por recurrencia.

Una eventual sesión posterior deberá formular y falsar esa hipótesis de forma independiente.

---

### 33. FALSIFIERS

H32 queda FALSIFIED si:

```text
no candidate host
can express the relation locally
without corrupting existing responsibility
```

o si requiere:

```text
duplicating Experience
changing Scenario semantics
turning Manifest into arbitrary copy storage
reinterpreting Fixture/News
```

o si:

```text
App must parse or aggregate
H25/H30 content
```

o si:

```text
new framing changes runtime,
Evidence,
evaluation,
K,
claim
```

o si requiere:

```text
viewer→subject
viewer→stay
account→subject
```

para producir la intro canónica.

También falsifica si la nueva relación sólo funciona mediante:

```text
demoId branching
scenario.id branching
brand.id branching
```

o si exige resolver simultáneamente Supervision, huntName o navegación fija.

Ante falsador:

```text
STOP
→ preserve evidence
→ do not create next abstraction in same baseline
```

---

### 34. HISTORICAL AND CURRENT REGRESSION

Preservar:

```text
historical replay
!=
current cumulative verification
```

Los replay H21–H31 mantienen sus verdictos históricos.

Además ejecutar sobre código actual:

```text
A
B
Retail
Arrival
```

y verificar preservación acumulada de:

```text
H25 Activity
H27 subject labels
H28 account display
H29 status
H30 journey message
```

salvo exclusivamente:

```text
App eyebrow
App introductory framing
```

autorizados por H32.

---

### 35. OUTPUT

Producir:

```text
session-32-explicit-composition-introductory-framing.md
```

con al menos:

```text
H31 CONSOLIDATED INPUT

H32 HYPOTHESIS

VARIABLE UNDER TEST

WHY A NEW RELATION IS NOW PERMITTED

TITLE / INTRO AUTHORITY SEPARATION

TWO-AUTHORITY COMPOSITION TEST

CANDIDATE HOST ANALYSIS

HOST DECISION

EXPERIMENTAL REPRESENTATION SHAPE

CONTENT AUTHORITY

VIEWER GUARDRAIL

THREADING PATH

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA

A CONTROL

B CONTROL

BRAND TRANSPORT CONTROL

BRAND / INTRO INDEPENDENCE CONTROL

REPRESENTATION INDEPENDENCE CONTROL

FACT / PRESENTATION CONTRADICTION CONTROL

ABSENCE CONTROL

ACCOUNT / SUBJECT / STATUS / JOURNEY INDEPENDENCE

COMPOSITION SWITCH CONTROL

NEGATIVE CONTROLS

CURRENT APP DOM / INTEGRATION EXECUTION

BROWSER VISUAL VALIDATION STATUS

HUNTNAME FREEZE

SUPERVISION FREEZE

FIXED NAVIGATION LINK FREEZE

CURRENT CUMULATIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c STATUS

L4 INTRODUCTORY FRAMING RESULT

L4 TITLE / BRAND RESULT

L4 SUPERVISION STATUS

L5 STATUS

RECURRING PRESENTATION PRESSURE

FALSIFICATION ANALYSIS

H32 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H32 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 36. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H32
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

INTRODUCTORY FRAMING RELATION
→ status

HOST
→ selected experimental host
  / insufficient

APP BRAND AUTHORITY
→ existing resolved BrandArtifact
→ preserved / unsupported

BRAND / INTRO AUTHORITY SEPARATION
→ supported / unsupported

APP CONSUMER BOUNDARY
→ preserved / violated

A/B COMPOSITION FRAMING
→ execution-verified / not established

VIEWER RELATION
→ NOT INTRODUCED / introduced-invalidly

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c
→ preserved / experimentally addressed H29–H30

L4 INTRODUCTORY FRAMING
→ status

L4 TITLE / BRAND
→ status

L4 SUPERVISION
→ preserved / open

L5
→ preserved / experimentally addressed H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ observed / strengthened / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H33 automáticamente.

---

### 37. METHODOLOGICAL GUARDRAIL

Preservar:

```text
having brand authority
!=
having introductory framing authority

having intro authority
!=
having brand authority

sharing one visual surface
!=
sharing one semantic source

static composition framing
!=
journey narrative

static composition framing
!=
Activity history

composition presentation
!=
runtime truth

declared presentation
!=
factual validation

DemoScript recurrence
!=
PresentationModel

viewer-oriented grammar
!=
viewer relationship

missing transport
!=
missing relation

new relation
!=
new architecture
```

El objetivo de H32 es comprobar únicamente si la relación ausente demostrada por H31 puede declararse de forma mínima, situada y reversible.

No utilizar H32 para ordenar retrospectivamente todas las relaciones de presentación descubiertas hasta ahora.
<!-- FIN-TEXTO-ORIGINAL-S32 -->

---

<a id="sesion-33"></a>

## Capítulo 33 — Identificación neutral en Supervisión

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-33-original.md) de `2026.zip`, registro `2026/09/17/rollout-2026-09-17T22-18-33-01a0b13c-4a03-7702-8be0-e7dcf49af57e.jsonl`. Mensaje de usuario en la línea 356; salida(s) de lectura en la(s) línea(s) 363. Cotejo adicional: adjunto repetido en otro hilo. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: b32c260cc587a9a8a3f3eb7775965062d717b6c858c4b0af343b0fe8e6ba3e48.

<!-- INICIO-TEXTO-ORIGINAL-S33 -->
### SESIÓN 33 — OPERATIONAL SUPERVISION SUBJECT REPRESENTATION PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 32 — Explicit Composition Introductory Framing
```

No reconstruir decisiones anteriores.

### 1. BASELINE CONSOLIDADA

```text
SESSION 32 → CLOSED

H32
→ SUPPORTED WITH QUALIFICATION

INTRODUCTORY FRAMING RELATION
→ EXPLICIT / EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED

HOST
→ DemoScript / experimental

APP BRAND AUTHORITY
→ existing resolved BrandArtifact
→ CURRENT APP DOM-INTEGRATION EXECUTION-VERIFIED

BRAND / INTRO AUTHORITY SEPARATION
→ SUPPORTED within A/B

APP CONSUMER BOUNDARY
→ PRESERVED

A/B COMPOSITION FRAMING
→ CURRENT APP DOM-INTEGRATION EXECUTION-VERIFIED

VIEWER RELATION
→ NOT INTRODUCED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 INTRODUCTORY FRAMING
→ EXPERIMENTALLY ADDRESSED within A/B / NOT PROMOTED

L4 TITLE / BRAND
→ EXISTING-SOURCE / LOCAL TRANSPORT / DOM-INTEGRATION VERIFIED

L4 SUPERVISION
→ PRESERVED / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ STRENGTHENED / NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

No promover ningún artefacto H25–H32.

---

### 2. PRESSURE SELECTED

Seleccionar exclusivamente dentro de L4 / Supervision:

```text
Supervision subject presentation
```

El síntoma conocido en App es equivalente a:

```text
subject.id === "subject-p1"
  ? "P1 · Lucía"
  : "P2 · Huésped 2"
```

Esta expresión mezcla potencialmente:

```text
operational subject identification
+
local P1/P2 alias
+
human situated presentation
+
A-specific copy
```

H33 debe averiguar qué parte está autorizada por las fuentes operacionales existentes.

NO seleccionar todavía:

```text
"Cuenta/sesión operativa"
huntName
fixed navigation link to A
supervision criterion labels
other diagnostic copy
```

No corregirlos incidentalmente.

---

### 3. H33 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de SupervisionPerspective,
las referencias y propiedades operacionales
ya existentes de los sujetos
pueden proporcionar una representación
diagnóstica neutral suficiente

sin reutilizar subjectPresentations H27,
sin introducir nombres humanos,
sin crear una nueva relación presentacional,
sin inferir P1/P2 mediante parsing,
y sin modificar sujetos, sesión operacional,
Evidence, estados, evaluación, K o claim.
```

La relación ensayada es:

```text
existing operational subject representation
→ neutral supervision display
```

NO:

```text
subjectRef
→ human identity
```

NO:

```text
GuestPerspective subject label
→ Supervision subject label
```

NO:

```text
account
→ supervised subject
```

Condición:

```text
NO-NEW-RELATION
```

---

### 4. WHY NO NEW RELATION IS AUTHORIZED YET

S31/S32 demostraron una relación ausente para framing y posteriormente autorizaron H32.

Supervisión se encuentra en una situación distinta.

Actualmente sabemos que `SupervisionPerspective` ya transporta información operacional sobre sujetos, incluyendo al menos los identificadores usados por App para aplicar el branch A-specific.

Por tanto primero debe probarse:

```text
existing operational authority
→ sufficient neutral diagnostic representation?
```

antes de autorizar:

```text
new supervision presentation relation
```

Preservar:

```text
existing human-looking hardcode
!=
evidence that human presentation is required
```

y:

```text
less narrative display
may be more epistemically correct
```

---

### 5. VARIABLE UNDER TEST

Exclusivamente el encabezado/label de cada sujeto dentro de la superficie Supervision.

No modificar los datos diagnósticos asociados:

```text
subject id
exists
operational state
Evidence count
```

ni otros campos actualmente renderizados.

No modificar:

```text
GuestPerspective subjects[].label
GuestPerspective subjects[].status
sessionLabel
message
Activity
introductory framing
branding
```

---

### 6. FIRST REQUIRED STEP — SOURCE INSPECTION

Antes del delta, inspeccionar exactamente:

```text
SupervisionPerspective contract
projectSupervisionPerspective()
Scenario subject definition
subjectStates
operationalSessionSubjectRef
Evidence attribution
App SystemPage consumer
```

Construir una matriz por sujeto:

```text
source field
semantic responsibility
current rendered representation
whether current copy adds information
whether added information is authorized
```

Documentar expresamente qué conoce `SupervisionPerspective` de:

```text
subject reference
subject existence
operational state
Evidence attribution/count
session reference
```

y qué NO conoce legítimamente de:

```text
human name
account ownership
viewer identity
GuestPerspective presentation
```

---

### 7. CURRENT COPY DECOMPOSITION

Analizar por separado:

```text
P1
Lucía

P2
Huésped 2
```

No asumir que ninguna parte está legitimada.

Preguntar:

```text
"P1"
→ explicit declared value?
→ abbreviation?
→ parsing/transformation of subject-p1?
→ local UI alias?

"Lucía"
→ what declared supervision source authorizes this?

"Huésped 2"
→ what declared supervision source authorizes this?
```

Si P1/P2 sólo pueden obtenerse mediante parsing o branch local:

```text
not legitimate operational authority
```

para H33.

---

### 8. H27 GUARDRAIL

H27 demostró:

```text
DemoScript.subjectPresentations
→ GuestPerspective.subjects[].label
```

dentro de A/B.

H27 NO demostró:

```text
subjectPresentations
→ universal subject display
```

ni:

```text
GuestPerspective display
→ SupervisionPerspective display
```

Por tanto H33 NO debe reutilizar:

```text
Lucía
Huésped 2
Inés
Mateo
Participante Alfa
```

desde H27.

Preservar:

```text
same subjectRef
across two read models
!=
same presentation authority
```

---

### 9. OPERATIONAL IDENTIFIER CANDIDATE

Analizar si el identificador/ref operacional ya transportado puede representarse directamente en Supervisión.

Por ejemplo, si la fuente declara:

```text
subject.id = "subject-p1"
```

puede ensayarse su representación literal como identificador diagnóstico.

NO exigir este output de antemano.

Códex debe determinar primero qué campo representa realmente la identidad/referencia operacional.

Si se utiliza:

```text
render exact declared identifier
```

NO:

```text
parse identifier
→ P1
```

NO:

```text
map identifier
→ Lucía
```

Preservar:

```text
displaying an identifier
!=
declaring human identity
```

---

### 10. ROLE / TYPE CANDIDATES

Si Scenario o SupervisionPerspective contienen explícitamente:

```text
role
type
```

analizar su semántica real antes de utilizarlos.

No convertir automáticamente:

```text
role
→ human label
```

ni:

```text
type
→ display name
```

Si no llegan actualmente a SupervisionPerspective, distinguir:

```text
missing transport
```

de:

```text
missing presentation relationship
```

pero no añadir transporte salvo que sea imprescindible y la semántica del campo autorice exactamente el output seleccionado.

Preferir la fuente mínima ya presente en SP.

---

### 11. NEUTRALITY REQUIREMENT

La representación resultante debe ser:

```text
operational
diagnostic
neutral
non-human
non-perspectival
```

No debe afirmar:

```text
Lucía
Inés
Mateo
Huésped 2
Tú
Tu sujeto
Tu cuenta
Titular
Participante
Operador
Representante
```

salvo que una relación existente inspeccionada autorice literalmente alguno de esos significados.

No introducir género.

---

### 12. A CONTROL

Sobre A, ejecutar la App actual y navegar a Supervisión.

Debe observarse una representación neutral procedente de la fuente seleccionada.

No prescribir:

```text
P1 / P2
```

si esos valores no están declarados.

Debe conservarse:

```text
exists
operationalState
Evidence count
sessionSubjectRef
evaluation
K
claim
```

según sus fuentes actuales.

---

### 13. B CONTROL

Sobre B, ejecutar la misma App actual.

La representación supervisora de los mismos sujetos operacionales debe proceder de la misma regla/fuente.

No debe aparecer por dependencia H33:

```text
Lucía
Huésped 2
```

ni tampoco introducir automáticamente:

```text
Inés
Mateo
```

El objetivo NO es sustituir nombres A por nombres B.

El objetivo es:

```text
remove unsupported human presentation
while preserving operational identification
```

---

### 14. CROSS-COMPOSITION CONTROL

Si A/B utilizan las mismas referencias operacionales:

```text
same operational subject reference
→ same supervision representation
```

aunque difieran:

```text
account
subjectPresentations
brand
introductory framing
journey narrative
Activity presentation
context
```

Esto es deliberado.

Supervisión puede legítimamente ser menos situada que GuestPerspective.

Preservar:

```text
same operational structure
→ same diagnostic representation
```

si la fuente lo justifica.

---

### 15. SUBJECT PRESENTATION INDEPENDENCE CONTROL

Perturbar únicamente:

```text
DemoScript.subjectPresentations
```

Debe resultar:

```text
GuestPerspective subject labels change

Supervision subject representation
→ unchanged
```

Esto es un control central.

Demuestra:

```text
GuestPerspective presentation authority
!=
Supervision operational authority
```

---

### 16. ACCOUNT INDEPENDENCE CONTROL

Perturbar:

```text
member.name
```

Debe cambiar únicamente las superficies cuya autoridad deriva legítimamente de member/branding correspondiente.

La representación del sujeto en Supervisión debe permanecer igual.

Preservar:

```text
account presentation
!=
supervision subject identification
```

---

### 17. BRAND / INTRO / JOURNEY INDEPENDENCE

Perturbar independientemente:

```text
brand.name
experimentalIntroductoryFraming
experimentalJourneyPresentations
activityPresentation
```

La representación supervisora del sujeto debe permanecer idéntica.

Esto debe evitar que la recurrencia presentacional de Script se filtre accidentalmente en Supervisión.

---

### 18. STATE INDEPENDENCE OF IDENTIFIER

Cambiar legítimamente:

```text
subject operational state
```

sin cambiar la referencia del sujeto.

Debe resultar:

```text
supervision operationalState changes

supervision subject identifier/presentation
→ unchanged
```

La identificación del sujeto no puede depender de su estado actual.

---

### 19. EVIDENCE INDEPENDENCE OF IDENTIFIER

Añadir Evidence mediante el recorrido legítimo.

Debe resultar:

```text
Evidence count changes

supervision subject identifier/presentation
→ unchanged
```

Preservar:

```text
Evidence attribution
!=
subject presentation
```

---

### 20. ORDER CONTROL

Si técnicamente puede realizarse en harness sin cambiar semántica, alterar el orden de la colección de sujetos manteniendo sus referencias.

La presentación debe permanecer asociada al sujeto correcto.

No utilizar:

```text
array index
```

como autoridad equivalente a P1/P2.

Preservar:

```text
first subject
!=
P1
```

salvo contrato explícito.

Si el orden forma parte de una relación autoritativa existente, documentarlo antes de usarlo.

---

### 21. UNKNOWN / ADDITIONAL SUBJECT OBSERVATION

Sólo mediante control aislado de projector/read model, si es seguro y no exige ampliar Scenario productivo, observar qué ocurre con una referencia de sujeto distinta de los dos IDs conocidos.

El objetivo es comprobar que App no aplica:

```text
if p1
  P1/Lucía
else
  P2/Huésped 2
```

a cualquier referencia desconocida.

No crear P3 como concepto de producto.

Si el experimento requiere cambiar semántica del Scenario:

```text
DO NOT RUN
```

y documentar que el control no es aplicable.

---

### 22. NO PARSING CONTROL

La implementación no puede utilizar:

```text
split
replace
regex
substring
suffix extraction
```

sobre subjectRef para producir P1/P2 u otro alias humano.

Si la representación neutral seleccionada es el identificador:

```text
render identifier as declared
```

La apariencia técnica no constituye falsificación.

H33 estudia autoridad, no estética.

---

### 23. "CUENTA/SESIÓN OPERATIVA" FREEZE

Conservar exactamente la superficie equivalente a:

```text
Cuenta/sesión operativa
```

durante H33.

Aunque sea semánticamente sospechosa.

No corregirla junto con subject labels.

Ese texto mezcla potencialmente:

```text
account
session
operationalSessionSubjectRef
```

y constituye otra presión.

Mantenerla visible.

---

### 24. OTHER SUPERVISION FREEZE

No modificar:

```text
Evaluación compartida
Criterio K
Evidence recibida
Admisibilidad conjunta
Suficiencia K
Afirmación derivada
Evidence y atribución
```

salvo instrumentación de test.

H33 no reevalúa la terminología de esas superficies.

---

### 25. APP CONSUMER BOUNDARY

La dirección debe continuar:

```text
SupervisionPerspective
→ App
→ render
```

No:

```text
App
→ Scenario lookup
```

No:

```text
App
→ DemoScript lookup
```

para resolver labels de Supervisión.

Especialmente NO:

```text
App
→ subjectPresentations
```

App no debe reconstruir relaciones que el read model no declara.

Si la fuente legítima ya forma parte de SupervisionPerspective, consumirla directamente.

---

### 26. NO-NEW-RELATION CONDITION

H33 queda SUPPORTED sólo si una fuente operacional ya existente resulta suficiente para una representación supervisora neutral.

Si para conservar una representación humana o amigable hace falta:

```text
subjectRef
→ supervision display label
```

como relación declarada nueva:

```text
STOP
```

Registrar:

```text
operational identification available
human supervision presentation missing
```

No introducir esa relación en S33.

Una sesión posterior podrá decidir si realmente se necesita.

---

### 27. CURRENT APP EXECUTION REQUIRED

Si H33 modifica App, ejecutar obligatoriamente la aplicación vigente con:

```text
A
B
```

y navegar a Supervisión.

Verificar DOM/integration del resultado.

También comprobar las páginas relevantes para asegurar que:

```text
GuestPerspective
Activity
framing
```

no han cambiado.

Registrar:

```text
DOM/integration
→ EXECUTED / NOT EXECUTED

browser visual validation
→ EXECUTED / NOT EXECUTED
```

No equipararlos.

---

### 28. NEGATIVE CONTROLS

Retail y Arrival deben permanecer intactos.

No deben recibir estructuras o labels de Supervision Family Adventure por hacer genérico el cambio.

Si no poseen la rama Supervision:

```text
absence remains absence
```

No crear defaults.

---

### 29. CURRENT CUMULATIVE REGRESSION

Sobre código actual preservar:

```text
H25 Activity
H27 GuestPerspective subject labels
H28 account presentation
H29 status
H30 journey message
H32 brand + introductory framing
```

La única diferencia autorizada debe estar en:

```text
Supervision subject heading/presentation
```

No utilizar exclusivamente replay histórico para acreditar App vigente.

---

### 30. RECURRING PRESENTATION PRESSURE — OBSERVATION ONLY

H33 debe registrar qué aporta su resultado a:

```text
RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
```

Especialmente distinguir:

```text
situated experiential/editorial presentation
```

de:

```text
operational diagnostic representation
```

Si H33 puede resolverse desde autoridad operacional existente, registrar:

```text
counter-evidence against
"all presentation belongs in Script"
```

sin convertirlo todavía en principio arquitectónico.

No crear ADR.

No promover DemoScript.

No crear PresentationBoundary.

---

### 31. FALSIFIERS

H33 queda FALSIFIED bajo NO-NEW-RELATION si:

```text
Supervision cannot identify its subjects
adequately from existing operational fields
```

sin introducir una nueva relación,

o si eliminar los hardcodes requiere:

```text
H27 subjectPresentations
member.name
DemoScript presentation
ID parsing
array position
A/B branching
```

o si el cambio modifica:

```text
subjectRef
operational state
Evidence attribution
operationalSessionSubjectRef
evaluation
K
claim
```

o si obliga a resolver simultáneamente:

```text
Cuenta/sesión operativa
viewer
account→subject
```

Ante falsador:

```text
STOP
→ document missing relation
→ preserve hardcode if necessary
→ do not create next abstraction
```

---

### 32. OUTPUT

Producir:

```text
session-33-operational-supervision-subject-representation-provenance.md
```

con al menos:

```text
H32 CONSOLIDATED INPUT

H33 HYPOTHESIS

VARIABLE UNDER TEST

WHY NO NEW RELATION IS AUTHORIZED YET

SUPERVISION SOURCE INSPECTION

CURRENT COPY DECOMPOSITION

OPERATIONAL SUBJECT AUTHORITY

H27 / SUPERVISION SEPARATION

CANDIDATE EXISTING REPRESENTATIONS

NO-PARSING ANALYSIS

NO-NEW-RELATION ANALYSIS

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

CROSS-COMPOSITION CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

ACCOUNT INDEPENDENCE CONTROL

BRAND / INTRO / JOURNEY INDEPENDENCE CONTROL

STATE INDEPENDENCE CONTROL

EVIDENCE INDEPENDENCE CONTROL

ORDER CONTROL

UNKNOWN SUBJECT OBSERVATION

CUENTA/SESIÓN OPERATIVA FREEZE

OTHER SUPERVISION FREEZE

CURRENT APP DOM / INTEGRATION EXECUTION

BROWSER VISUAL VALIDATION STATUS

NEGATIVE CONTROLS

CURRENT CUMULATIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c STATUS

L4 FRAMING STATUS

L4 SUPERVISION SUBJECT RESULT

L4 REMAINING SUPERVISION PRESSURE

L5 STATUS

RECURRING PRESENTATION PRESSURE

FALSIFICATION ANALYSIS

H33 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H33 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 33. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H33
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

SUPERVISION SUBJECT AUTHORITY
→ existing operational source
  / missing relation

HUMAN SUBJECT PRESENTATION
→ NOT REQUIRED
  / MISSING
  / introduced-invalidly

GP / SP PRESENTATION SEPARATION
→ supported / unsupported

APP CONSUMER BOUNDARY
→ preserved / violated

A/B SUPERVISION SUBJECT REPRESENTATION
→ DOM-INTEGRATION VERIFIED
  / not established

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c
→ preserved / experimentally addressed H29–H30

L4 FRAMING
→ preserved / experimentally addressed H32

L4 SUPERVISION SUBJECT
→ status

L4 SUPERVISION SESSION
→ preserved / open

L5
→ preserved / experimentally addressed H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ observed / qualified by H33 / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H34 automáticamente.

---

### 34. METHODOLOGICAL GUARDRAIL

Preservar:

```text
operational identification
!=
human identity

operational identification
!=
situated human presentation

GuestPerspective
!=
SupervisionPerspective

same subjectRef
!=
same presentation authority

human-readable
!=
more epistemically correct

diagnostic surface
!=
experiential surface

subject array position
!=
subject identity

subjectRef syntax
!=
declared alias

rendering an existing identifier
!=
creating a new identity relation

reducing unsupported copy
!=
losing demonstrated semantics

Script presentation recurrence
!=
universal presentation ownership
```

El objetivo de H33 no es hacer Supervisión más agradable.

El objetivo es determinar **qué sabe legítimamente Supervisión sobre el sujeto que está mostrando** y reducir su representación exactamente a ese nivel si las fuentes existentes son suficientes.
<!-- FIN-TEXTO-ORIGINAL-S33 -->

---

<a id="sesion-34"></a>

## Capítulo 34 — Rótulo neutral de sujeto de sesión

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-34-original.md) de `2026.zip`, registro `2026/09/18/rollout-2026-09-18T14-34-19-01a0b4b9-9faf-7ac2-a5b7-d7b3ac53a0cb.jsonl`. Mensaje de usuario en la línea 54; salida(s) de lectura en la(s) línea(s) 60. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 38891f57a6f888dacfeadf8561cfb830da142fc1d4c12500a698e8e987138f7c.

<!-- INICIO-TEXTO-ORIGINAL-S34 -->
### SESIÓN 34 — OPERATIONAL SESSION SUBJECT REPRESENTATION PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 33 — Operational Supervision Subject Representation Provenance
```

No reconstruir decisiones anteriores.

---

### 1. BASELINE CONSOLIDADA

```text
SESSION 33 → CLOSED

H33
→ SUPPORTED WITH QUALIFICATION

NO-NEW-RELATION
→ SUFFICIENT

SUPERVISION SUBJECT AUTHORITY
→ EXISTING OPERATIONAL SOURCE
→ SupervisionPerspective.subjects[].id

HUMAN SUBJECT PRESENTATION
→ NOT REQUIRED for tested diagnostic purpose

GP / SP PRESENTATION SEPARATION
→ SUPPORTED within A/B

APP CONSUMER BOUNDARY
→ PRESERVED

A/B SUPERVISION SUBJECT REPRESENTATION
→ CURRENT APP DOM-INTEGRATION VERIFIED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 FRAMING
→ PRESERVED / EXPERIMENTALLY ADDRESSED H32

L4 SUPERVISION SUBJECT
→ EXISTING-SOURCE / LOCALLY RENDERED
→ EXPERIMENTALLY ADDRESSED H33

L4 SUPERVISION SESSION
→ PRESERVED / OPEN

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ OBSERVED
→ QUALIFIED BY H33
→ NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

No promover relaciones H25–H33.

---

### 2. PRESSURE SELECTED

Seleccionar exclusivamente en Supervision:

```text
"Cuenta/sesión operativa"
+
sessionSubjectRef
```

La presión es la **procedencia semántica de la representación de `sessionSubjectRef`**.

No seleccionar todavía:

```text
huntName
fixed Family Adventure navigation link
other supervision terminology
human-friendly supervision labels
viewer identity
authentication
```

---

### 3. H34 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro de SupervisionPerspective,
la relación operacional existente
que produce sessionSubjectRef
puede proporcionar una representación
diagnóstica neutral de esa referencia,

sin atribuir cuenta,
autenticación,
viewer,
ownership,
representación humana
ni relación account→subject,

sin crear una nueva relación
y sin modificar runtime,
subjects,
Evidence,
evaluation,
K o claim.
```

Condición:

```text
NO-NEW-RELATION
```

La relación investigada es:

```text
existing operational session subject reference
→ neutral diagnostic representation
```

NO:

```text
session subject
→ account owner
```

NO:

```text
session subject
→ authenticated user
```

NO:

```text
session subject
→ viewer
```

NO:

```text
session subject
→ human identity
```

---

### 4. WHY NO NEW RELATION IS AUTHORIZED

S33 demostró que Supervision puede identificar sujetos mediante datos operacionales ya presentes.

El campo:

```text
sessionSubjectRef
```

también existe ya en SupervisionPerspective.

Por tanto debe investigarse primero si el problema actual es:

```text
existing operational data
+
overstated UI label
```

y no:

```text
missing presentation relation
```

Preservar:

```text
overclaim in copy
!=
missing data
```

y:

```text
reducing copy to existing authority
!=
creating semantics
```

---

### 5. VARIABLE UNDER TEST

Exclusivamente la representación compuesta actualmente por:

```text
"Cuenta/sesión operativa"
+
sessionSubjectRef
```

No modificar:

```text
Supervision subject headings H33
subjects[].exists
subjects[].operationalState
subjects[].evidenceCount
Evidence attribution
jointAdmissibility
sufficiency
derivedClaim
criterion K
```

Ni:

```text
GuestPerspective
Activity
branding
introductory framing
huntName
navigation
```

---

### 6. FIRST REQUIRED STEP — SEMANTIC SOURCE INSPECTION

Antes de cambiar App, inspeccionar:

```text
ScenarioDefinition.operationalSessionSubjectRef

SupervisionPerspectiveReadModel.sessionSubjectRef

projectSupervisionPerspective()

MockDataAdapter / provider usage

action admission checks

App SystemPage consumer
```

Buscar todos los usos de:

```text
operationalSessionSubjectRef
sessionSubjectRef
```

y construir una matriz:

```text
field
declaring layer
producer
consumers
operational effect
semantic claim explicitly supported
claims NOT supported
```

No inferir significado exclusivamente del nombre de la propiedad.

---

### 7. QUESTIONS THE INSPECTION MUST ANSWER

Determinar exactamente si la fuente acredita:

```text
A. una referencia a un sujeto

B. una referencia al sujeto asociado
   al mecanismo operacional de sesión

C. el sujeto que puede ejecutar
   ciertas acciones

D. identidad de cuenta

E. identidad autenticada

F. viewer

G. titularidad/ownership
```

No agruparlas.

La inspección debe documentar para cada una:

```text
SUPPORTED
NOT SUPPORTED
NOT DETERMINED
```

H34 sólo puede representar las afirmaciones SUPPORTED.

---

### 8. ACCOUNT NEGATIVE AUTHORITY

Preservar explícitamente la evidencia acumulada:

```text
fixture.member
→ account presentation H28

operationalSessionSubjectRef
→ operational responsibility
```

Hasta ahora no existe:

```text
member
→ operationalSessionSubjectRef
```

ni:

```text
account
→ Experience subject
```

Por tanto, salvo evidencia nueva ya existente en contratos:

```text
"Cuenta"
```

no puede formar parte de la representación H34.

No introducir mapping para conservar esa palabra.

---

### 9. H33 SUBJECT REPRESENTATION SEPARATION

S33 establece:

```text
Supervision.subjects[].id
→ operational diagnostic subject identification
```

H34 debe estudiar si:

```text
sessionSubjectRef
```

puede correlacionarse legítimamente con esas referencias.

Si ambos contienen el mismo valor:

```text
subject-p1
```

preservar:

```text
value equality
!=
new identity relation
```

La relación sólo puede ser la ya declarada en el modelo operacional.

No utilizar la igualdad para inferir cuenta/viewer.

---

### 10. CANDIDATE NEUTRAL REPRESENTATIONS

Después de inspeccionar semántica, comparar posibles representaciones diagnósticas mínimas.

Ejemplos conceptuales, NO copy obligatorio:

```text
Referencia de sesión operativa · subject-p1

Sujeto de sesión operativa · subject-p1

Referencia operacional de sujeto · subject-p1
```

Cada opción hace afirmaciones ligeramente distintas.

Seleccionar únicamente la que esté respaldada por la semántica inspeccionada.

Si ninguna formulación amigable puede expresarse sin añadir significado:

```text
render raw field/value in diagnostic form
```

puede ser suficiente.

H34 estudia autoridad, no estética.

---

### 11. FORBIDDEN REPRESENTATIONS

No usar:

```text
Cuenta
Cuenta activa
Cuenta operativa
Usuario
Usuario activo
Usuario autenticado
Viewer
Persona
Participante
Operador
Representante
Titular
Lucía
Inés
P1
```

salvo que un significado concreto esté explícitamente declarado por la fuente inspeccionada.

No utilizar H27, member.name ni parsing para humanizar.

---

### 12. NO-PARSING CONDITION

La presentación del valor debe conservar:

```text
sessionSubjectRef
```

literalmente si se presenta.

No:

```text
subject-p1
→ P1
```

mediante:

```text
split
replace
regex
substring
index
branch
```

No mapear:

```text
subject-p1 → Lucía/Inés
```

El valor técnico es admisible en una superficie diagnóstica.

---

### 13. A CONTROL

Ejecutar A con App actual y recorrer Family Adventure.

Navegar a Supervisión en las fases necesarias.

Comprobar:

```text
sessionSubjectRef
→ unchanged
```

y que la nueva representación:

```text
does not contain unsupported account/viewer language
```

Preservar todos los demás valores SP.

---

### 14. B CONTROL

Ejecutar B mediante la misma App.

Debe aplicarse exactamente la misma regla diagnóstica.

Si:

```text
sessionSubjectRef A == sessionSubjectRef B
```

la representación deberá ser equivalente.

No utilizar:

```text
Lucía
Inés
brand
intro
subjectPresentations
context
```

para distinguirla.

---

### 15. ACCOUNT INDEPENDENCE CONTROL

Perturbar únicamente:

```text
member.name
```

Debe observarse:

```text
account presentation changes

Supervision session representation
→ unchanged
```

Esto es central para falsar cualquier dependencia implícita:

```text
account
→ sessionSubjectRef
```

---

### 16. SUBJECT PRESENTATION INDEPENDENCE

Perturbar:

```text
DemoScript.subjectPresentations
```

Debe cambiar GP y conservar completamente la representación H34.

Preservar:

```text
human subject presentation
!=
operational session reference
```

---

### 17. BRAND / INTRO / JOURNEY / ACTIVITY INDEPENDENCE

Perturbar independientemente:

```text
brand.name
experimentalIntroductoryFraming
experimentalJourneyPresentations
activityPresentation
```

La representación de sesión supervisora debe permanecer idéntica.

No permitir que Script-bound presentation se convierta en fuente de semántica operacional.

---

### 18. STATE / EVIDENCE INDEPENDENCE

Durante el recorrido:

```text
subjectStates change
Evidence grows
evaluation changes
claim changes
```

mientras:

```text
operationalSessionSubjectRef
```

permanezca igual.

Debe resultar:

```text
session representation unchanged
```

si su fuente no ha cambiado.

No reconstruirla desde estado o Evidence.

---

### 19. SESSION SUBJECT VARIATION CONTROL

Investigar si el repositorio ofrece una forma legítima, local y reversible de variar:

```text
operationalSessionSubjectRef
```

sin inventar una nueva relación ni declarar esa variante como composición productiva.

Si es posible mediante una copia de Scenario exclusivamente de harness:

```text
subjectRef X
→ session representation X

subjectRef Y
→ session representation Y
```

manteniendo el label/formatting constante.

Pero NO ejecutar acciones si la variante vuelve incoherentes las guards del Scenario.

El objetivo es observar transporte/proyección/render, no demostrar una nueva ruta operacional.

Clasificar como:

```text
isolated read-model / composition observation
```

si no constituye recorrido alcanzable.

Si cambiar la referencia exige alterar semántica operacional material:

```text
DO NOT RUN
```

y documentar la limitación.

---

### 20. UNKNOWN OPAQUE REF CONTROL

Si puede hacerse de forma aislada sin modificar Scenario productivo, usar una referencia opaca:

```text
opaque:session-subject/X
```

como entrada de proyección.

Debe renderizarse sin:

```text
P1
Lucía
Huésped 2
account
```

ni parsing.

No ejecutar acciones.

No afirmar que la referencia sea válida para una composición productiva.

Este control prueba el consumidor, no la semántica de un nuevo sujeto.

---

### 21. APP CONSUMER BOUNDARY

Mantener:

```text
Scenario
→ SupervisionPerspective
→ App
→ render
```

App no debe consultar:

```text
Scenario directly
member
DemoScript
subjectPresentations
fixtures
```

para explicar `sessionSubjectRef`.

No branch:

```text
if subject-p1 ...
```

No lookup A/B.

---

### 22. NO-NEW-RELATION ANALYSIS

H34 queda SUPPORTED si:

```text
existing sessionSubjectRef semantics
are sufficient
for a neutral diagnostic representation
```

sin otra relación.

Si la superficie necesita realmente representar:

```text
account
viewer
authenticated user
human operator
```

y esas relaciones no existen:

```text
H34
→ FALSIFIED under NO-NEW-RELATION

STOP
```

Documentar exactamente qué relación falta.

No crearla en H34.

---

### 23. "CUENTA" REMOVAL IS NOT ACCOUNT DENIAL

Si la inspección confirma que `sessionSubjectRef` no acredita cuenta y el nuevo copy elimina esa palabra, registrar:

```text
removing unsupported account language
!=
proving that no account exists operationally
```

H34 sólo establece:

```text
current source
does not authorize that claim
```

No formula una teoría negativa universal sobre autenticación/cuentas.

---

### 24. OTHER SUPERVISION FREEZE

Preservar:

```text
subject headings H33
Evaluación compartida
Criterio K
Evidence recibida
Admisibilidad conjunta
Suficiencia K
Afirmación derivada
Evidence y atribución
```

No corregir terminología colateral.

---

### 25. HUNTNAME FREEZE

Preservar:

```text
GuestPerspective.huntName
```

y su h1 actual.

No aprovechar H34 para conectarlo con Experience.name.

---

### 26. NAVIGATION FREEZE

Preservar el acceso fijo detectado:

```text
/?demo=hospitality-family-adventure
```

No resolver composición/navegación en esta sesión.

---

### 27. CURRENT APP EXECUTION

Si existe delta de App:

```text
A DOM/integration → REQUIRED
B DOM/integration → REQUIRED
```

Navegar a Supervisión y comprobar el campo H34.

Además verificar Home / Activity para preservar:

```text
H25
H27
H28
H29
H30
H32
H33
```

Registrar por separado:

```text
DOM/integration verification
browser visual validation
```

No equipararlos.

---

### 28. NEGATIVE CONTROLS

Retail y Arrival deben permanecer sin Supervision Family Adventure.

No añadir campos/fallbacks de sesión para hacer genérico el cambio.

```text
absence remains absence
```

---

### 29. CURRENT CUMULATIVE REGRESSION

Sobre aplicación actual verificar:

```text
H25 Activity
H27 GP labels
H28 account display
H29 status
H30 message
H32 brand + intro
H33 SP subject IDs
```

La única diferencia autorizada debe ser:

```text
Supervision session label / representation
```

No sustituir esta verificación por replay histórico.

---

### 30. RECURRING PRESENTATION PRESSURE

Registrar qué aporta H34 a la distinción emergente:

```text
situated/editorial presentation
vs
operational/diagnostic representation
```

Si H34 se resuelve desde autoridad operacional existente, se acumula más contraevidencia a:

```text
all presentation belongs in Script
```

pero NO promover todavía:

```text
derive operational presentation
declare experiential presentation
```

a principio arquitectónico.

Sigue siendo hipótesis emergente.

No ADR.

No PresentationBoundary.

---

### 31. FALSIFIERS

H34 queda FALSIFIED si:

```text
sessionSubjectRef existing semantics
are insufficient to describe the surface
without account/viewer/authentication claims
```

o si eliminar la mezcla requiere:

```text
member.name
subjectPresentations
DemoScript
ID parsing
A/B branching
new account→subject relation
viewer→subject
authentication identity
```

o si el cambio altera:

```text
operationalSessionSubjectRef
subject refs
Evidence attribution
states
evaluation
K
claim
```

o exige solucionar simultáneamente:

```text
huntName
navigation
other supervision terminology
```

Ante falsador:

```text
STOP
→ preserve evidence
→ do not introduce missing relation
```

---

### 32. OUTPUT

Producir:

```text
session-34-operational-session-subject-representation-provenance.md
```

con al menos:

```text
H33 CONSOLIDATED INPUT

H34 HYPOTHESIS

VARIABLE UNDER TEST

WHY NO NEW RELATION IS AUTHORIZED

SESSION SUBJECT SOURCE INSPECTION

SEMANTIC SUPPORT MATRIX

CURRENT COPY DECOMPOSITION

ACCOUNT NEGATIVE AUTHORITY

H33 / SESSION REPRESENTATION SEPARATION

CANDIDATE NEUTRAL REPRESENTATIONS

REPRESENTATION DECISION

NO-PARSING ANALYSIS

NO-NEW-RELATION ANALYSIS

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

ACCOUNT INDEPENDENCE CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

BRAND / INTRO / JOURNEY / ACTIVITY INDEPENDENCE CONTROL

STATE / EVIDENCE INDEPENDENCE CONTROL

SESSION SUBJECT VARIATION CONTROL

OPAQUE REF OBSERVATION

OTHER SUPERVISION FREEZE

HUNTNAME FREEZE

NAVIGATION FREEZE

CURRENT APP DOM / INTEGRATION EXECUTION

BROWSER VISUAL VALIDATION STATUS

NEGATIVE CONTROLS

CURRENT CUMULATIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c STATUS

L4 FRAMING STATUS

L4 SUPERVISION SUBJECT STATUS

L4 SUPERVISION SESSION RESULT

L4 REMAINING PRESSURES

L5 STATUS

RECURRING PRESENTATION PRESSURE

FALSIFICATION ANALYSIS

H34 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H34 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 33. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H34
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

SESSION SUBJECT AUTHORITY
→ existing operational source
  / missing relation

ACCOUNT CLAIM
→ REMOVED AS UNSUPPORTED
  / supported
  / unresolved

VIEWER / AUTHENTICATION RELATION
→ NOT INTRODUCED / introduced-invalidly

APP CONSUMER BOUNDARY
→ preserved / violated

A/B SESSION REPRESENTATION
→ DOM-INTEGRATION VERIFIED
  / not established

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c
→ preserved / experimentally addressed H29–H30

L4 FRAMING
→ preserved / experimentally addressed H32

L4 SUPERVISION SUBJECT
→ preserved / experimentally addressed H33

L4 SUPERVISION SESSION
→ status

L5
→ preserved / experimentally addressed H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ observed / further qualified / not promoted

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H35 automáticamente.

---

### 34. METHODOLOGICAL GUARDRAIL

Preservar:

```text
session subject reference
!=
account

session subject reference
!=
authenticated user

session subject reference
!=
viewer

session subject reference
!=
human identity

value equality
!=
identity equivalence

operational authority
!=
experiential presentation authority

diagnostic representation
!=
human-friendly presentation

removing unsupported wording
!=
proving the opposite proposition

existing source + overstated copy
!=
missing semantic relation

rendering a declared reference
!=
creating a new identity relation
```

El objetivo de H34 es averiguar **qué significa realmente `operationalSessionSubjectRef` dentro de la arquitectura existente** y hacer que Supervisión no afirme más de lo que esa relación acredita.
<!-- FIN-TEXTO-ORIGINAL-S34 -->

---

<a id="sesion-35"></a>

## Capítulo 35 — Nombre procedente de Experience

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-35-original.md) de `2026.zip`, registro `2026/09/18/rollout-2026-09-18T14-34-19-01a0b4b9-9faf-7ac2-a5b7-d7b3ac53a0cb.jsonl`. Mensaje de usuario en la línea 157; salida(s) de lectura en la(s) línea(s) 163. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: 8e4d4b1d6b0b505e69fa125bf56e04e151bbe13e909f60586f2b382a52b5d755.

<!-- INICIO-TEXTO-ORIGINAL-S35 -->
### SESIÓN 35 — EXPERIENCE-SOURCED GUEST EXPERIENCE NAME PROVENANCE

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 34 — Operational Session Subject Representation Provenance
```

No reconstruir decisiones anteriores.

---

### 1. BASELINE CONSOLIDADA

```text
SESSION 34 → CLOSED

H34
→ SUPPORTED WITH QUALIFICATION

NO-NEW-RELATION
→ SUFFICIENT

SESSION SUBJECT AUTHORITY
→ EXISTING OPERATIONAL SOURCE

ACCOUNT CLAIM
→ REMOVED AS UNSUPPORTED

VIEWER / AUTHENTICATION RELATION
→ NOT INTRODUCED

APP CONSUMER BOUNDARY
→ PRESERVED

A/B SESSION REPRESENTATION
→ CURRENT APP DOM-INTEGRATION VERIFIED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 FRAMING
→ PRESERVED / EXPERIMENTALLY ADDRESSED H32

L4 SUPERVISION SUBJECT
→ PRESERVED / EXPERIMENTALLY ADDRESSED H33

L4 SUPERVISION SESSION
→ PRESERVED / EXPERIMENTALLY ADDRESSED H34

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

RECURRING SCRIPT-BOUND PRESENTATION PRESSURE
→ OBSERVED / FURTHER QUALIFIED / NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

No promover artefactos H25–H34.

---

### 2. PRESSURE SELECTED

Seleccionar exclusivamente:

```text
GuestPerspective.huntName
```

y su representación actual como h1 en HomePage.

Síntoma actual:

```text
GuestPerspective.huntName
→ hardcoded "Aventura Familiar"
```

mientras existe:

```text
ExperienceDefinition.name
→ "Aventura Familiar"
```

La igualdad actual de strings NO constituye procedencia.

H35 debe determinar si:

```text
ExperienceDefinition.name
```

posee autoridad semántica suficiente para proporcionar el nombre presentado de la Experience dentro de GuestPerspective.

---

### 3. DO NOT SELECT

No modificar:

```text
brand / eyebrow H32
introductory framing H32
sessionLabel H28
subject labels H27
subject status H29
journey message H30
Activity H25
Supervision H33/H34
fixed navigation link
generic App navigation labels
document title
```

No seleccionar todavía la navegación fija a A.

---

### 4. H35 — HYPOTHESIS

Hipótesis falsable:

```text
La ExperienceDefinition ya existente
contiene una relación semántica de nombre
suficiente para proporcionar
GuestPerspective.huntName,

de modo que el nombre presentado
pueda proceder de Experience.name

sin hardcode local,
sin una nueva relación editorial,
sin utilizar DemoScript,
sin inferir desde Scenario,
brand o manifest identity,

y sin modificar runtime state,
Evidence,
evaluation,
K o claim.
```

Condición:

```text
NO-NEW-RELATION
```

La relación candidata es:

```text
Experience
→ declared semantic name
→ GuestPerspective experience-name presentation
```

NO:

```text
DemoScript
→ huntName
```

NO:

```text
brand
→ huntName
```

NO:

```text
Scenario
→ huntName
```

NO:

```text
composition intro
→ huntName
```

---

### 5. FIRST REQUIRED STEP — NAME SEMANTICS INSPECTION

Antes del delta, inspeccionar:

```text
ExperienceDefinition contract
ExperienceDefinition.name usages
resolveDemo()
ResolvedDemoRuntime
projectSnapshot()
projectGuestPerspective()
GuestPerspectiveReadModel.huntName
App HomePage h1 consumer
```

Buscar todos los usos actuales de:

```text
experience.name
huntName
```

y documentar:

```text
declaring layer
producer
consumers
current semantic role
current transport path
whether the two concepts are already related
```

No asumir que un campo denominado `name` es automáticamente el nombre que GuestPerspective debe mostrar.

---

### 6. SEMANTIC QUESTIONS

Responder expresamente:

```text
A. Experience.name identifies
   the Experience as a semantic artifact?

B. Is it intended as a human-readable name?

C. Is it stable across Scenario/compositions
   sharing the Experience?

D. Does huntName mean
   the presented name of that Experience?

E. Does huntName instead mean
   a composition-specific title,
   journey title,
   campaign title,
   or another responsibility?
```

Para cada pregunta:

```text
SUPPORTED
NOT SUPPORTED
NOT DETERMINED
```

H35 sólo puede conectar ambos campos si la semántica inspeccionada sostiene la correspondencia.

---

### 7. STRING EQUALITY IS NOT EVIDENCE

Preservar:

```text
Experience.name == "Aventura Familiar"

GuestPerspective.huntName == "Aventura Familiar"
```

actualmente.

Pero:

```text
same string
!=
same semantic authority
```

El experimento NO puede justificarse únicamente por esa coincidencia.

Debe demostrarse:

```text
name semantics
→ compatible with huntName responsibility
```

---

### 8. CANDIDATE SOURCE ANALYSIS

Comparar al menos:

```text
ExperienceDefinition.name
DemoScript
Scenario
BrandArtifact.name
Manifest/demoId
current projector literal
```

##### ExperienceDefinition.name

Candidato principal.

Analizar si representa el nombre de la Experience compartida.

##### DemoScript

Ya aloja varias presentaciones situadas.

Pero H35 NO debe usar recurrencia como permiso.

Si `huntName` es el nombre de la Experience, Script sería una autoridad más débil o incorrecta.

##### Scenario

No utilizar Scenario sólo porque A/B lo transporten.

Scenario describe situación/operación, no necesariamente nombre de Experience.

##### BrandArtifact.name

Ya tiene autoridad de branding H32.

Preservar:

```text
brand name
!=
Experience name
```

##### Manifest/demoId

Identifican/configuran composición.

No parsear ni utilizar IDs como nombre.

##### Projector literal

Es el síntoma histórico.

No constituye fuente.

---

### 9. TRANSPORT / RELATION DISTINCTION

Si la inspección concluye:

```text
Experience.name
has the required semantic authority
```

pero no llega actualmente al projector, clasificar:

```text
relationship semantics → existing

transport → missing
```

Un transporte mínimo puede ensayarse.

Si, en cambio:

```text
Experience.name
does not authorize huntName
```

entonces:

```text
NO-NEW-RELATION
→ INSUFFICIENT
→ STOP
```

No crear una relación nueva en H35.

---

### 10. MINIMAL TRANSPORT REQUIREMENT

Si la relación es suficiente, transportar únicamente lo necesario.

Preferir:

```text
Experience.name
→ existing runtime/projectSnapshot path
→ projectGuestPerspective
→ huntName
```

sin pasar objetos completos si sólo se necesita el nombre.

Pero no forzar un escalar si la arquitectura existente ya transporta Experience legítimamente hasta la frontera apropiada.

Documentar la elección.

Preservar:

```text
minimal transport
!=
new semantic relation
```

---

### 11. APP CONSUMER BOUNDARY

App debe continuar:

```text
GuestPerspective.huntName
→ h1
```

No cambiar App para leer directamente:

```text
runtime.experience.name
```

si eso evita la procedencia del read model.

H35 investiga la fuente de:

```text
GuestPerspective.huntName
```

No sustituye esa responsabilidad por un acceso paralelo desde App.

Preservar:

```text
App
→ consumer of GuestPerspective
```

para esta superficie.

---

### 12. A CONTROL

A utiliza:

```text
experience:family-adventure@1
```

y debe presentar exactamente el nombre declarado por esa Experience si la hipótesis se sostiene.

Verificar:

```text
h1
→ GuestPerspective.huntName
→ Experience.name
```

y preservar:

```text
brand
intro
message
subjects
status
Activity
Supervision
facts
evaluation
```

---

### 13. B CONTROL

B comparte la misma Experience.

Por tanto, si:

```text
A.experienceRef == B.experienceRef
```

debe resultar:

```text
huntName A == huntName B
```

aunque difieran:

```text
brand
Scenario
Fixture
DemoScript
subject presentations
journey narrative
intro framing
Activity presentation
context
```

Esto es un control central.

Preservar:

```text
same Experience
→ same Experience name
```

si ésa es realmente la responsabilidad demostrada.

---

### 14. EXPERIENCE NAME VARIATION CONTROL

Crear una variante exclusivamente de harness donde cambie:

```text
Experience.name
```

manteniendo:

```text
Experience.id
Scenario
DemoScript
Fixture
brand
runtime actions
evaluation
```

idénticos cuando sea técnicamente posible.

Debe resultar:

```text
GuestPerspective.huntName changes

facts unchanged
runtime unchanged
evaluation unchanged
Activity unchanged
intro unchanged
brand unchanged
```

Este control debe demostrar que:

```text
huntName depends on Experience.name
```

y no en el string histórico hardcoded.

---

### 15. EXPERIENCE ID INDEPENDENCE

Cuando sea técnicamente seguro en harness, comprobar que renombrar exclusivamente la identidad técnica de Experience manteniendo su `name` y las referencias coherentes no altera la presentación.

No hacerlo si exige una modificación extensa de la composición que introduzca ruido.

Si se ejecuta:

```text
Experience.id X/Y
same Experience.name
→ same huntName
```

El objetivo es preservar:

```text
Experience identity
!=
presented name
```

No parsear IDs.

---

### 16. BRAND INDEPENDENCE

Cambiar exclusivamente:

```text
BrandArtifact.name
```

Debe cambiar las superficies H32 de branding y conservar:

```text
huntName
```

Preservar:

```text
Brand name
!=
Experience name
```

---

### 17. SCRIPT PRESENTATION INDEPENDENCE

Perturbar por separado:

```text
subjectPresentations
experimentalJourneyPresentations
experimentalIntroductoryFraming
activityPresentation
presenterLabel
```

Ninguna debe cambiar:

```text
huntName
```

si Experience.name resulta la autoridad.

Este control es especialmente importante para la presión Script-bound.

---

### 18. SCENARIO INDEPENDENCE

Usar A/B como control principal:

```text
different Scenario
same Experience
→ same huntName
```

No crear un Scenario artificial sólo para demostrarlo salvo necesidad.

Preservar:

```text
Scenario situated behavior
!=
Experience naming authority
```

---

### 19. ACCOUNT / SUBJECT / STATE INDEPENDENCE

Perturbar o recorrer legítimamente:

```text
member.name
subjectPresentations
subjectStates
Evidence
```

Debe conservarse:

```text
huntName
```

El nombre de la Experience no depende del sujeto, cuenta o estado actual.

---

### 20. NO DEMOSCRIPT FALLBACK

Si `Experience.name` no está disponible o no es semánticamente suficiente:

```text
do not fallback to DemoScript
```

en H35.

No crear:

```text
experimentalHuntName
presentation.title
experienceTitle
```

dentro de Script.

Eso sería una nueva relación y requeriría una sesión posterior.

---

### 21. ABSENCE OBSERVATION

Si técnicamente puede ensayarse una Experience con nombre vacío/ausente sin violar el contrato, observar el comportamiento.

Pero NO debilitar el tipo o contrato sólo para crear el control.

Si `name` es obligatorio:

```text
document contract requirement
```

y no inventar ausencia.

No crear fallback al literal:

```text
"Aventura Familiar"
```

para preservar la apariencia.

---

### 22. NEGATIVE CONTROLS

Retail y Arrival deben conservar comportamiento actual.

Analizar si poseen ExperienceDefinition.name y si ésta llega a superficies distintas.

No hacer obligatorio:

```text
GuestPerspective
```

para verticales que no lo tienen.

No introducir huntName o Family Adventure UI en otros recorridos.

---

### 23. CURRENT APP EXECUTION

Si H35 modifica runtime/projector:

Ejecutar App actual para:

```text
A
B
Retail
Arrival
```

En A/B comprobar:

```text
h1
eyebrow
intro
message
subjects
status
Supervision
Activity
```

y preservar todos salvo `huntName` cuando una variante de Experience.name lo modifique.

Registrar:

```text
DOM/integration → EXECUTED / NOT EXECUTED

browser visual validation
→ EXECUTED / NOT EXECUTED
```

No equipararlos.

---

### 24. CURRENT CUMULATIVE REGRESSION

Preservar sobre código actual:

```text
H25 Activity
H27 subject labels
H28 account
H29 status
H30 message
H32 brand + intro
H33 supervision subject IDs
H34 supervision session representation
```

La única nueva dependencia autorizada:

```text
Experience.name
→ GuestPerspective.huntName
```

si H35 la sostiene.

---

### 25. RECURRING PRESENTATION PRESSURE

H35 debe registrar qué aporta el resultado a la presión emergente.

Si Experience.name resulta suficiente, tenemos evidencia de una tercera clase:

```text
semantic definition metadata
→ semantic presentation
```

junto a:

```text
operational/diagnostic authority
→ derived representation

composition-specific editorial content
→ explicit declaration
```

Registrar como:

```text
PRESENTATION AUTHORITY STRATIFICATION
→ EVIDENCE STRENGTHENED
→ NOT PROMOTED
```

No crear ADR.

No crear PresentationBoundary.

No crear PresentationModel.

No convertir esta observación en regla universal.

---

### 26. FALSIFIERS

H35 queda FALSIFIED bajo NO-NEW-RELATION si:

```text
Experience.name
does not semantically authorize huntName
```

o si GuestPerspective.huntName representa algo distinto que exige una relación nueva,

o si la conexión requiere:

```text
DemoScript
Scenario-specific copy
BrandArtifact
manifest/demoId parsing
App branching
```

o si cambiar Experience.name altera indebidamente:

```text
runtime state
Evidence
evaluation
K
claim
```

o si App debe abandonar GuestPerspective como fuente del h1.

Ante falsador:

```text
STOP
→ preserve hardcode/source evidence
→ document missing relationship
→ do not create experimental huntName relation
```

---

### 27. HISTORICAL VS CURRENT VERIFICATION

Preservar:

```text
historical replay
!=
current cumulative verification
```

Adaptar únicamente la instrumentación histórica necesaria para conservar verdictos H21–H34.

El nuevo harness H35 debe ejecutar fuentes actuales.

No usar replay para afirmar comportamiento vigente.

---

### 28. OUTPUT

Producir:

```text
session-35-experience-sourced-guest-experience-name-provenance.md
```

con al menos:

```text
H34 CONSOLIDATED INPUT

H35 HYPOTHESIS

VARIABLE UNDER TEST

WHY NO NEW RELATION IS AUTHORIZED

EXPERIENCE NAME SOURCE INSPECTION

HUNTNAME SEMANTIC ANALYSIS

SEMANTIC SUPPORT MATRIX

CANDIDATE SOURCE ANALYSIS

STRING EQUALITY / AUTHORITY DISTINCTION

TRANSPORT / RELATION DISTINCTION

SOURCE DECISION

THREADING PATH

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

SHARED EXPERIENCE CONTROL

EXPERIENCE NAME VARIATION CONTROL

EXPERIENCE ID INDEPENDENCE CONTROL

BRAND INDEPENDENCE CONTROL

SCRIPT PRESENTATION INDEPENDENCE CONTROL

SCENARIO INDEPENDENCE CONTROL

ACCOUNT / SUBJECT / STATE INDEPENDENCE

ABSENCE OBSERVATION

NEGATIVE CONTROLS

CURRENT APP DOM / INTEGRATION EXECUTION

BROWSER VISUAL VALIDATION STATUS

CURRENT CUMULATIVE REGRESSION

HISTORICAL REPLAY STATUS

EXECUTION TRACE

L3a STATUS

L3b STATUS

L3c STATUS

L4 FRAMING STATUS

L4 SUPERVISION SUBJECT STATUS

L4 SUPERVISION SESSION STATUS

L4 HUNTNAME RESULT

L5 STATUS

PRESENTATION AUTHORITY STRATIFICATION

FALSIFICATION ANALYSIS

H35 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H35 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 29. FINAL VERDICT FORMAT

Concluir únicamente con:

```text
H35
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

HUNTNAME AUTHORITY
→ Experience.name
  / missing relation
  / other existing source

EXPERIENCE / HUNTNAME SEMANTIC CORRESPONDENCE
→ supported / unsupported / unresolved

APP CONSUMER BOUNDARY
→ preserved / violated

A/B HUNTNAME
→ CURRENT APP DOM-INTEGRATION VERIFIED
  / not established

L3a
→ preserved / experimentally addressed H28

L3b
→ preserved / experimentally addressed H27

L3c
→ preserved / experimentally addressed H29–H30

L4 FRAMING
→ preserved / experimentally addressed H32

L4 SUPERVISION SUBJECT
→ preserved / experimentally addressed H33

L4 SUPERVISION SESSION
→ preserved / experimentally addressed H34

L4 HUNTNAME
→ status

L5
→ preserved / experimentally addressed H25

PRESENTATION AUTHORITY STRATIFICATION
→ evidence strengthened / unsupported
→ NOT PROMOTED

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H36 automáticamente.

---

### 30. METHODOLOGICAL GUARDRAIL

Preservar:

```text
same text
!=
same authority

semantic name
!=
brand name

semantic name
!=
composition-specific title

Experience
!=
Scenario

Experience
!=
DemoScript

stable Experience identity
+
different situated compositions
→
may legitimately share semantic name

semantic metadata presentation
!=
editorial situated presentation

operational derivation
!=
semantic metadata derivation

existing semantic authority
+
missing transport
!=
missing relation

recurring Script presentation
!=
universal presentation ownership
```

El objetivo de H35 es determinar si el hardcode `huntName` está ocultando una autoridad semántica ya existente o si la coincidencia con `Experience.name` es sólo accidental.

No diseñar una nueva relación si las fuentes actuales no sostienen esa correspondencia.
<!-- FIN-TEXTO-ORIGINAL-S35 -->

---

<a id="sesion-36"></a>

## Capítulo 36 — Auditoría de autoridad por afirmación

**Estado:** instrucción principal íntegra recuperada del historial.

**Procedencia:** [texto literal recuperado](instrucciones-recuperadas/sesion-36-original.md) de `2026.zip`, registro `2026/09/17/rollout-2026-09-17T22-18-33-01a0b13c-4a03-7702-8be0-e7dcf49af57e.jsonl`. Mensaje de usuario en la línea 497; salida(s) de lectura en la(s) línea(s) 504. La procedencia detallada figura en el [manifiesto](instrucciones-recuperadas/manifest-recuperacion-2026.json).

SHA-256 del texto fuente recuperado: dd5fc838ee61293e71d7fa778b32e0a416d71f9b099e438e4ee4384fbc6f7aca.

<!-- INICIO-TEXTO-ORIGINAL-S36 -->
### SESIÓN 36 — PRESENTATION AUTHORITY PROVENANCE STRATIFICATION AUDIT

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 35 — Experience-Sourced Guest Experience Name Provenance
```

No reconstruir decisiones anteriores.

---

### 1. BASELINE CONSOLIDADA

```text
SESSION 35 → CLOSED

H35
→ SUPPORTED WITH QUALIFICATION

NO-NEW-RELATION
→ SUFFICIENT

HUNTNAME AUTHORITY
→ ExperienceDefinition.name

EXPERIENCE / HUNTNAME SEMANTIC CORRESPONDENCE
→ SUPPORTED within tested scope

APP CONSUMER BOUNDARY
→ PRESERVED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 FRAMING
→ PRESERVED / EXPERIMENTALLY ADDRESSED H32

L4 SUPERVISION SUBJECT
→ PRESERVED / EXPERIMENTALLY ADDRESSED H33

L4 SUPERVISION SESSION
→ PRESERVED / EXPERIMENTALLY ADDRESSED H34

L4 HUNTNAME
→ EXPERIENCE-SOURCED / EXPERIMENTALLY ADDRESSED H35

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

PRESENTATION AUTHORITY STRATIFICATION
→ EVIDENCE STRENGTHENED
→ NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Todos los artefactos experimentales H25–H35 permanecen en cuarentena.

---

### 2. CHARACTER OF SESSION 36

S36 es una sesión de:

```text
CROSS-EXPERIMENTAL AUDIT
+
FALSIFICATION
+
CONSOLIDATION
```

No es, por defecto, una sesión de implementación.

Objetivo:

```text
test whether the accumulated presentation evidence
admits a coherent provenance model
without inventing a universal presentation owner
```

No crear arquitectura para hacer que la hipótesis pase.

---

### 3. H36 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro del alcance experimental H25–H35,
cada afirmación presentacional significativa
puede rastrearse hasta una autoridad explícita
compatible con su significado,

y las relaciones observadas pueden distinguirse
en modos de procedencia diferentes

sin necesitar un PresentationModel universal,
sin convertir DemoScript en propietario
de toda presentación,
y sin convertir App en autoridad semántica.
```

La hipótesis NO exige:

```text
one UI surface
→ one authority
```

Al contrario, debe admitir:

```text
one visual surface
→ multiple independent authorities
```

cuando cada fragmento tenga procedencia separada.

---

### 4. PROVISIONAL AUTHORITY MODES

Utilizar exclusivamente como hipótesis de clasificación inicial:

#### MODE U — UI-LOCAL CONVENTION

Copy o transformación puramente presentacional que no introduce una afirmación nueva de dominio.

Ejemplos candidatos:

```text
"Mi aventura"
separadores
pluralización
"Estado:"
generic headings
```

Preservar:

```text
UI-local copy
must not manufacture domain meaning
```

---

#### MODE D — DECLARED DOMAIN / ARTIFACT DATA

Valores ya declarados por una fuente cuya responsabilidad incluye ese significado.

Ejemplos candidatos:

```text
Experience.name
BrandArtifact.name
member.name
```

No asumir que cualquier campo descriptivo entra aquí.

La responsabilidad debe estar demostrada.

---

#### MODE O — OPERATIONAL / DERIVED AUTHORITY

Representaciones derivadas de estado, referencias, Evidence o evaluación cuyo significado ya está determinado por el runtime/read model.

Ejemplos candidatos:

```text
subjectStates
Supervision.subjects[].id
sessionSubjectRef
Evidence counts
evaluation.sufficiency
derivedClaim
```

Preservar:

```text
derived presentation
must not claim more than the operational/derived source proves
```

---

#### MODE E — EXPLICIT SITUATED EDITORIAL DECLARATION

Contenido situado que no puede derivarse legítimamente de hechos/metadata existentes y que necesita declaración explícita para la composición/demostración.

Ejemplos experimentales:

```text
H25 activityPresentation
H27 subjectPresentations
H30 experimentalJourneyPresentations
H32 experimentalIntroductoryFraming
```

Preservar:

```text
declared presentation
!=
factual authority
```

---

### 5. THESE MODES ARE NOT ARCHITECTURE

Los cuatro modos anteriores son:

```text
AUDIT CATEGORIES
```

NO:

```text
layers
services
interfaces
modules
contracts
ownership boundaries
ADR decisions
TES concepts
```

No renombrar clases o mover código para reflejarlos.

Si la clasificación falla:

```text
H36 must fail or qualify
```

No modificar categorías ad hoc sólo para obtener cobertura perfecta.

---

### 6. UNIT OF ANALYSIS

La unidad de análisis NO será:

```text
field
component
page
read model
```

por defecto.

Será:

```text
presentation claim / meaningful fragment
```

porque una sola superficie puede contener múltiples autoridades.

Ejemplo obligatorio:

```text
Mi aventura · Aurora Stay
```

debe analizarse al menos como:

```text
"Mi aventura"
→ U candidate

"Aurora Stay"
→ D candidate
```

No asignar automáticamente la cabecera completa a un solo modo.

---

### 7. H30 MIXED-AUTHORITY CONTROL

`GuestPerspective.message` debe utilizarse como falsador principal contra:

```text
one field → one authority
```

Clasificar separadamente:

```text
initial representation
intermediate situated representations
completion representation
```

y sus fuentes.

Debe quedar visible que:

```text
same output field
can legitimately use different authorities
depending on runtime condition
```

Si esta afirmación no puede sostenerse con las fuentes H30:

```text
H36 → FALSIFIED / QUALIFIED
```

No diseñar un owner común para resolverlo.

---

### 8. H32 COMPOSED-SURFACE CONTROL

Analizar la cabecera de Family Adventure actual:

```text
eyebrow
h1
introductory paragraph
```

como una superficie visual compuesta.

Registrar autoridad de:

```text
generic UI shell
BrandArtifact.name
Experience.name
experimentalIntroductoryFraming
```

Comprobar:

```text
co-location in DOM
!=
shared semantic authority
```

---

### 9. H25 ACTIVITY CONTROL

Analizar H25 cuidadosamente porque combina:

```text
occurred factual Activity / Evidence acceptance
+
declared situated representation
```

Determinar qué autoridad decide:

```text
that an Activity exists
```

y qué autoridad decide:

```text
how that Activity is presented
```

No clasificar toda Activity como MODE E.

Preservar:

```text
factual occurrence authority
!=
presentation-content authority
```

Esta distinción es obligatoria.

---

### 10. H27 SUBJECT PRESENTATION CONTROL

Analizar:

```text
Scenario subject existence/reference
+
DemoScript.subjectPresentations
```

Distinguir:

```text
subject exists
→ non-editorial authority

subject human/situated label
→ explicit editorial declaration
```

Preservar:

```text
presentation cannot create subject
```

---

### 11. H28 ACCOUNT PRESENTATION CONTROL

Descomponer:

```text
Cuenta de Inés
```

como mínimo en:

```text
"Cuenta de"
→ candidate UI convention

"Inés"
→ member.name authority
```

Comprobar que la composición textual no crea:

```text
member → subject
account → viewer
```

Si el prefijo introduce más significado que la fuente acredita:

registrarlo como contraejemplo.

No asumir que H28 prueba automáticamente MODE U + MODE D.

---

### 12. H29 STATUS CONTROL

Analizar:

```text
Estado: habilitado
```

como:

```text
"Estado:"
→ UI/local representation candidate

enabled
→ operational authority

mapping enabled → "habilitado"
→ presentation transformation
```

Determinar si ese mapping cabe legítimamente como presentación derivada o revela una categoría adicional.

No alterar las categorías para salvar el resultado.

---

### 13. H33 / H34 DIAGNOSTIC CONTROLS

Analizar:

```text
subject-p1

Sujeto de sesión operativa
subject-p1
```

Distinguir:

```text
raw operational value
UI diagnostic label
operational relationship
```

Comprobar que App no añade significado no soportado.

H33/H34 deben constituir contraevidencia explícita a:

```text
all human-readable presentation
requires explicit Script declaration
```

---

### 14. H35 SEMANTIC NAME CONTROL

Analizar:

```text
Experience.name
→ GuestPerspective.huntName
```

como posible MODE D.

Compararlo con:

```text
BrandArtifact.name
member.name
```

y determinar si realmente comparten una clase útil de autoridad o si agruparlos oculta diferencias materiales.

Si:

```text
semantic metadata
account factual data
branding configuration
```

resultan demasiado distintos para una misma categoría:

registrar la falsación o cualificación.

No crear subtipos ilimitados sólo para preservar la hipótesis.

---

### 15. COMPLETE ADDRESSED-SURFACE MATRIX

Construir una matriz exhaustiva de todas las superficies modificadas o estudiadas desde H25 hasta H35.

Como mínimo:

```text
Activity existence
Activity title
Activity description

GP huntName
GP sessionLabel
GP subjects[].label
GP subjects[].status
GP message

App eyebrow generic part
App eyebrow brand part
App introductory framing

SP subject heading
SP subject detail ID
SP session label
SP sessionSubjectRef

completion message
initial message
intermediate messages
```

Para cada fragmento registrar:

```text
surface
claim
source
relationship
authority mode candidate
transport
consumer
factual/editorial
composition-specific?
runtime-varying?
experiment proving it
qualification
```

---

### 16. DO NOT LIMIT THE AUDIT TO SUCCESSFUL PATCHES

Incluir también falsaciones y STOP relevantes:

```text
H24
H26
H31
```

porque proporcionan evidencia sobre:

```text
what was NOT authorized
```

Especialmente registrar:

```text
H24
activity situated representation missing

H26
GuestPerspective situated narrative/human representation gaps

H31
composition introductory relation missing
```

y cómo sesiones posteriores pudieron experimentar sólo después de esas falsaciones.

La arquitectura emergente debe explicar también los STOP.

---

### 17. COUNTEREXAMPLE SEARCH

Buscar deliberadamente en las superficies auditadas ejemplos que contradigan cualquiera de estas proposiciones:

```text
P1:
existing authoritative meaning
→ should always be derived

P2:
composition-specific editorial meaning
→ always belongs in DemoScript

P3:
operational presentation
→ never needs explicit declaration

P4:
semantic/artifact metadata
→ can always be presented directly

P5:
UI-local convention
→ never introduces domain meaning

P6:
one claim
→ one authority source
```

No intentar demostrar las seis.

Intentar falsarlas.

Registrar cada una como:

```text
SUPPORTED WITHIN OBSERVED SET
FALSIFIED
INCONCLUSIVE
```

---

### 18. PARTICULARLY IMPORTANT FALSIFIERS

H36 debe considerarse materialmente cualificada o falsificada si encuentra:

```text
a supposedly generic UI string
that actually adds domain meaning
```

o:

```text
an operational output
that legitimately requires composition-specific declaration
```

o:

```text
a DemoScript presentation
that actually functions as factual/runtime authority
```

o:

```text
semantic metadata
whose display needs a separate editorial relationship
```

o:

```text
a presentation claim
whose authority cannot be assigned
without circular reasoning
```

o:

```text
a surface where transport convenience
has been mistaken for semantic ownership
```

---

### 19. NO PRODUCT DELTA BY DEFAULT

S36 should begin with:

```text
CODE DELTA → NONE
```

No cambiar producto para conseguir una clasificación más limpia.

Si durante la auditoría aparece un bug/overclaim nuevo:

```text
record pressure
do not repair it
```

salvo que la ausencia de una corrección impida materialmente observar las fuentes.

En ese caso:

```text
STOP
```

y documentar.

---

### 20. CURRENT SOURCE VERIFICATION

Aunque no haya delta, comprobar que las relaciones actuales siguen presentes en fuentes vigentes.

No depender únicamente de informes históricos.

Inspeccionar directamente al menos:

```text
contracts
artifacts A/B
bootstrap
MockDataAdapter
vertical-evaluation/projectors
App
```

y contrastar con los verdictos H25–H35.

No es necesario repetir todos los recorridos si no hay cambio de código, pero cualquier afirmación sobre fuentes actuales debe proceder del working tree vigente.

---

### 21. HISTORICAL EVIDENCE USE

Los informes/trazas H25–H35 pueden utilizarse como evidencia experimental de:

```text
causality
independence
falsification
```

pero preservar:

```text
historical experiment
!=
current runtime execution
```

No reejecutar toda la historia sólo para producir una tabla si las fuentes están intactas y las trazas son suficientes.

Si se ejecuta suite actual:

registrar el resultado separadamente.

---

### 22. UI-LOCAL COPY GUARDRAIL

No clasificar automáticamente como legítimo todo copy que permanezca en App.

Para cada fragmento UI-local seleccionado preguntar:

```text
does this string merely organize/present?
```

o:

```text
does it assert something about
Experience,
subject,
account,
session,
state,
journey,
facts,
evaluation,
ownership,
viewer?
```

Si hace lo segundo:

```text
UI-local authority alone is insufficient
```

salvo evidencia específica.

Este control debe explicar por qué:

```text
"Mi aventura"
```

puede ser distinto de:

```text
"Cuenta/sesión operativa"
```

históricamente.

---

### 23. PRESENTATION TRANSFORMATION QUESTION

Investigar explícitamente el estatus de mappings como:

```text
enabled → "habilitado"
not-enabled → "sin habilitar"
not-enlisted → "sin alistar"
```

y:

```text
evaluation.sufficiency = established
→ completion sentence
```

Preguntar si son:

```text
derived representation
```

o:

```text
editorial declaration hidden in code
```

No decidir por su ubicación en el projector.

Esta cuestión puede falsar una clasificación demasiado simple.

---

### 24. AUTHORITY VS CONTENT DISTINCTION

Para cada caso distinguir:

```text
authority to say something
```

de:

```text
exact wording used to say it
```

Ejemplo conceptual:

```text
subjectState=enabled
may authorize the claim that it is enabled

but may not uniquely determine
the Spanish wording "Estado: habilitado"
```

Registrar esta diferencia.

No crear localización/content architecture en S36.

---

### 25. AUTHORITY COMPOSITION

Cuando una frase combine fuentes distintas, representar explícitamente la composición.

Ejemplo:

```text
"Cuenta de " + member.name
```

No esconderla bajo una única categoría.

Registrar:

```text
fragment A authority
fragment B authority
combined claim
whether combination introduces extra semantics
```

La combinación misma puede necesitar autoridad.

---

### 26. OUTPUT — PROVENANCE GRAPH

Además de la matriz, producir un grafo textual o Mermaid equivalente:

```text
source authority
→ transformation/declaration
→ read model/runtime
→ App surface
```

para las principales relaciones H25–H35.

El grafo debe mostrar múltiples fuentes convergiendo en una superficie cuando ocurra.

No crear una nueva arquitectura de runtime a partir del grafo.

Es documentación de evidencia.

---

### 27. OUTPUT — PROVISIONAL MODEL

Sólo después del análisis, producir un modelo provisional de autoridad.

Puede resultar:

```text
four modes supported
```

o:

```text
three modes + exceptions
```

o:

```text
proposed stratification falsified
```

No prescribir de antemano el resultado.

Si se conserva una clasificación, cada modo debe incluir:

```text
definition
positive examples
counterexamples
boundary conditions
what it must NOT be used to infer
```

---

### 28. PROMOTION GATE

S36 NO puede:

```text
create ADR
modify Architecture v0.5
modify TES
modify PSC
create PSC-P02
promote DemoScript
create PresentationBoundary
create PresentationModel
create PresentationRegistry
```

aunque H36 resulte positiva.

Como máximo puede concluir:

```text
CANDIDATE ARCHITECTURAL PRINCIPLE
→ EVIDENCE-BACKED
→ NOT PROMOTED
```

Una sesión posterior deberá decidir expresamente si hay materia suficiente para promoción.

---

### 29. KNOWN UNRESOLVED PRESSURES

Mantener visibles y NO resolver:

```text
fixed navigation link to A

remaining supervision terminology
if any

other App literals from S31 inventory
```

No utilizar su existencia automáticamente para falsar H36 si están fuera del conjunto experimental auditado.

Pero pueden utilizarse como:

```text
challenge probes
```

si ayudan a probar los límites de la clasificación.

---

### 30. TEST-INFRASTRUCTURE OBSERVATION

Registrar separadamente la presión observada en la infraestructura experimental:

```text
historical replay count
archived-source routing
test concurrency/timeouts
instrumentation maintenance
```

S35 observó timeouts bajo concurrencia y PASS serial sin cambio de producto.

No modificar infraestructura en S36.

Clasificar únicamente:

```text
NO MATERIAL PRESSURE
OBSERVED PRESSURE
MATERIAL PRESSURE
```

con evidencia.

No mezclarla con el veredicto semántico de H36.

---

### 31. H36 FALSIFIERS

H36 queda FALSIFIED si:

```text
no coherent provenance classification
can account for the addressed presentation claims
without circular or ad hoc categories
```

o si:

```text
DemoScript must be treated
as factual authority
for any demonstrated case
```

o si:

```text
operational/runtime sources
cannot explain representations
previously classified as derived
```

o si:

```text
semantic metadata / UI-local / operational / editorial
boundaries collapse under existing counterexamples
```

o si:

```text
the same relationship
must be classified differently
only to make the model pass
```

H36 queda SUPPORTED WITH QUALIFICATION si:

```text
a useful, bounded classification survives
the counterexample search
```

aunque existan:

```text
mixed-authority surfaces
transformations
unresolved pressures
```

si están explícitamente explicadas.

---

### 32. OUTPUT

Producir:

```text
session-36-presentation-authority-provenance-stratification-audit.md
```

con al menos:

```text
H35 CONSOLIDATED INPUT

H36 HYPOTHESIS

AUDIT SCOPE

PROVISIONAL AUTHORITY MODES

UNIT OF ANALYSIS

CURRENT SOURCE VERIFICATION

ADDRESSED SURFACE MATRIX

H24 / H26 / H31 FALSIFICATION INPUT

H25 ACTIVITY AUTHORITY ANALYSIS

H27 SUBJECT PRESENTATION ANALYSIS

H28 ACCOUNT PRESENTATION ANALYSIS

H29 STATUS PRESENTATION ANALYSIS

H30 MIXED MESSAGE AUTHORITY ANALYSIS

H32 COMPOSED HEADER AUTHORITY ANALYSIS

H33 SUPERVISION SUBJECT ANALYSIS

H34 SUPERVISION SESSION ANALYSIS

H35 EXPERIENCE NAME ANALYSIS

UI-LOCAL COPY ANALYSIS

PRESENTATION TRANSFORMATION ANALYSIS

AUTHORITY / WORDING DISTINCTION

AUTHORITY COMPOSITION ANALYSIS

COUNTEREXAMPLE SEARCH

PROPOSITION P1–P6 RESULTS

PROVENANCE GRAPH

PROVISIONAL AUTHORITY MODEL

CURRENT UNRESOLVED PRESSURES

TEST-INFRASTRUCTURE OBSERVATION

FALSIFICATION ANALYSIS

H36 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

PROMOTION GATE STATUS

WHAT H36 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 33. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H36
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

PRESENTATION AUTHORITY CLASSIFICATION
→ supported / qualified / falsified

UI-LOCAL CONVENTION
→ status

DECLARED DOMAIN / ARTIFACT DATA
→ status

OPERATIONAL / DERIVED AUTHORITY
→ status

EXPLICIT SITUATED EDITORIAL DECLARATION
→ status

MIXED-AUTHORITY SURFACES
→ supported / problematic

DEMO SCRIPT UNIVERSAL OWNERSHIP
→ NOT SUPPORTED / supported-invalidly

APP SEMANTIC AUTHORITY
→ NOT SUPPORTED / supported-invalidly

CANDIDATE ARCHITECTURAL PRINCIPLE
→ evidence-backed / insufficient
→ NOT PROMOTED

TEST-INFRASTRUCTURE PRESSURE
→ status

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H37 automáticamente.

---

### 34. METHODOLOGICAL GUARDRAIL

Preservar:

```text
where text lives
!=
where authority comes from

where authority comes from
!=
where wording must live

authority to make a claim
!=
exact wording of the claim

one field
!=
one authority

one component
!=
one authority

one visual surface
!=
one authority

presentation
!=
editorial declaration

presentation
!=
factual authority

derivation
!=
inference without authority

declaration
!=
truth

UI-local copy
!=
permission to assert domain meaning

recurrence
!=
ownership

classification
!=
architecture

evidence-backed principle
!=
promoted principle
```

El objetivo de S36 es intentar destruir nuestra explicación actual de la procedencia presentacional antes de convertirla en arquitectura.

Si sobrevive, habremos ganado una base de promoción.

Si falla, habremos descubierto qué categoría o relación todavía no comprendemos.
<!-- FIN-TEXTO-ORIGINAL-S36 -->

---

<a id="sesion-37"></a>

## Capítulo 37 — Reducir atribuciones no acreditadas en Activity

**Estado:** instrucción original íntegra.

**Procedencia:** adjunto original aportado por el usuario, identificado como 69936bfc-f066-440f-8eb8-386305e398fe/pasted-text.txt.

SHA-256 del texto fuente extraído: 8221298b478c8d85ae0354cd0894070893e70e8670c20fbd870573386f281f42.

<!-- INICIO-TEXTO-ORIGINAL-S37 -->
### SESIÓN 37 — ACTIVITY ATTRIBUTION CLAIM PROVENANCE AND REDUCTION

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 36 — Presentation Authority Provenance Stratification Audit
```

No reconstruir decisiones anteriores.

---

### 1. BASELINE CONSOLIDADA

```text
SESSION 36 → CLOSED

H36
→ FALSIFIED
  as exhaustive compatible-meaning claim

U / D / O / E
→ PARTIALLY USEFUL
→ QUALIFIED
→ NOT PROMOTED

DEMO SCRIPT UNIVERSAL OWNERSHIP
→ NOT SUPPORTED

APP SEMANTIC AUTHORITY
→ NOT SUPPORTED

CANDIDATE ARCHITECTURAL PRINCIPLE
→ evidence-backed only as review discipline
→ NOT PROMOTED

PROMOTION GATE
→ CLOSED
```

H36 localiza dos contraejemplos materiales dentro de H25:

```text
C1 / M05
Activity.description:
"por ti"

→ textual source exists
→ viewer/actor relation absent
```

y:

```text
C2 / M06
Activity.description:
"desde tu cuenta"
"registrado desde la cuenta de Inés"

→ textual source exists
→ account→execution relation absent
```

Preservar asimismo:

```text
H25 → Activity representation
H27 → subject presentation
H28 → account presentation
H29 → subject status
H30 → journey narrative
H32 → composition framing
H33 → supervision subject
H34 → supervision session
H35 → Experience name
```

dentro de sus respectivos alcances y cualificaciones.

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Todos los artefactos H25–H36 permanecen sin promoción.

---

### 2. PRESSURE SELECTED

Seleccionar exclusivamente las afirmaciones de atribución perspectival y de cuenta presentes en:

```text
DemoScriptStep.activityPresentation.description
```

para Family Adventure.

En particular, las expresiones equivalentes a:

```text
"por ti"

"desde tu cuenta"

"registrado desde la cuenta de Inés"
```

cuando afirman alguna de estas relaciones:

```text
viewer → actor/contributor

viewer → subject

account → execution

account holder → contributor

member → execution source
```

No seleccionar el resto de Activity.

---

### 3. H37 — HYPOTHESIS

Hipótesis falsable:

```text
La representación situada de Activity
demostrada por H25

puede conservarse
reduciendo únicamente las afirmaciones
viewer/account/actor no acreditadas

a contenido compatible con
la ocurrencia aceptada,
la atribución operacional existente
y la declaración editorial situada H25,

sin introducir viewer,
actor,
operator,
accountSubject,
executedBy,
account→subject
ni account→execution.
```

Condición:

```text
NO-NEW-RELATION
```

H37 prueba:

```text
unsupported relational claim
→ can be removed/reduced
while preserving demonstrated Activity semantics
```

NO:

```text
missing relation
→ must be modelled
```

---

### 4. WHY NO NEW RELATION IS AUTHORIZED

H36 demuestra:

```text
text provenance
!=
semantic authority for every claim in the text
```

Pero H36 NO demuestra que las relaciones ausentes sean necesarias para el producto.

Por tanto:

```text
missing viewer/account authority
→ first test semantic reduction
```

antes de:

```text
create viewer/account/actor model
```

Preservar:

```text
historical wording
!=
product requirement
```

y:

```text
removing an unsupported assertion
!=
losing demonstrated semantics
```

---

### 5. VARIABLE UNDER TEST

Únicamente:

```text
activityPresentation.description
```

en las entradas Family Adventure afectadas.

Congelar:

```text
activityPresentation.title

Activity existence/materialization
Activity.id
Activity.occurredAt
Activity.provenance

Evidence
Evidence.subjectRefs

Scenario
actions
guards
checkpoints

evaluation
K
claim
```

No modificar H25 `activityPresentation` como relación.

No cambiar su host.

No consolidar su estructura con otras presentaciones.

---

### 6. FIRST REQUIRED STEP — PRE-DELTA CLAIM MATRIX

Antes de modificar las declaraciones, inspeccionar todas las instancias canónicas A/B de:

```text
activityPresentation.title
activityPresentation.description
```

y producir una matriz por fragmento significativo:

```text
composition
step/actionId
current title
current description
fragment
claim asserted
existing factual/editorial source
relation required
authority status
KEEP / REDUCE / REMOVE
```

Distinguir explícitamente como mínimo:

```text
occurred/accepted Evidence
subjectRef attribution
situated location/content
human narrative label
viewer attribution
account attribution
execution attribution
```

No tratar una frase completa como una única unidad.

---

### 7. SOURCE AUTHORITY TO PRESERVE

Conservar la separación S36:

#### Ocurrencia

```text
guards + action + runtime
→ Evidence accepted
```

Esto acredita la ocurrencia simulada aceptada.

#### Atribución operacional

```text
Evidence.subjectRefs
→ subject attribution
```

No acredita nombre humano, viewer ni cuenta.

#### Representación situada H25

```text
accepted occurrence
+
matching activityPresentation declaration
→ situated Activity row
```

La declaración puede proporcionar:

```text
title
situated editorial wording
```

pero:

```text
declaration
!=
proof of actor/viewer/account relation
```

---

### 8. CLAIMS THAT MUST NOT SURVIVE WITHOUT AUTHORITY

Una descripción canónica H37 no puede afirmar, directa o indirectamente:

```text
tú aportaste el hallazgo

tú registraste el hallazgo

tu cuenta registró el hallazgo

la cuenta de Inés registró el hallazgo

Inés ejecutó la acción
```

salvo que la inspección encuentre una relación existente que H36 no contempló.

Si apareciese tal relación:

```text
STOP
→ document contradictory evidence
→ do not silently reuse it
```

porque modificaría el diagnóstico de S36.

---

### 9. NO VIEWER MODEL

No crear:

```text
viewerRef
viewerSubjectRef
currentViewer
authenticatedViewer
```

No inferir:

```text
operationalSessionSubjectRef
→ viewer
```

Preservar:

```text
session subject
!=
viewer
```

---

### 10. NO ACTOR / OPERATOR MODEL

No crear:

```text
actorRef
operatorRef
performedBy
executedBy
representativeRef
participantRef
```

Public Action y Evidence actuales no acreditan identidad humana del ejecutor.

Preservar:

```text
action target subject
!=
human executor
```

y:

```text
Evidence attributed subject
!=
actor who performed the UI interaction
```

---

### 11. NO ACCOUNT EXECUTION MODEL

No crear:

```text
accountRef on Activity
performedFromAccount
registeredFromAccount
memberRef on Evidence
```

No usar:

```text
fixture.member.name
```

para reconstruir la cuenta desde la que se ejecutó una acción.

Preservar:

```text
account presentation H28
!=
execution provenance
```

---

### 12. H27 GUARDRAIL

No reutilizar:

```text
DemoScript.subjectPresentations
```

para reparar Activity.

H27 acredita:

```text
subjectRef → GuestPerspective human/situated label
```

en GP.

No acredita:

```text
subjectRef → universal human identity
```

ni:

```text
subjectRef → Activity actor name
```

Si los nombres editoriales existentes de H25 permanecen en algún texto:

registrar expresamente que continúan siendo:

```text
Activity-local editorial declaration
```

y no identidad operacional universal.

---

### 13. CONTENT REDUCTION RULE

Para cada descripción problemática:

```text
remove only unsupported relational predicates
```

Preservar, cuando sea posible:

```text
accepted occurrence
situated editorial content
subject-neutral description
```

Preferir:

```text
less assertion
```

sobre:

```text
new inferred relationship
```

Ejemplos conceptuales admisibles:

```text
Hallazgo registrado.

Pista registrada.

Hallazgo situado registrado.
```

o formulaciones similares compatibles con las fuentes.

Estos son ejemplos conceptuales, NO copy obligatorio.

Códex debe obtener el wording final después de la matriz de claims.

---

### 14. DO NOT SOLVE BY DELETING ACTIVITY

H37 no puede hacer pasar la hipótesis mediante:

```text
remove Activity row

remove activityPresentation

remove description field globally

stop materializing accepted occurrences
```

La Activity situada H25 debe permanecer.

Preservar:

```text
accepted occurrence
+
H25 situated presentation
→ visible Activity
```

La pregunta es cuánto puede afirmar esa presentación, no si debe existir.

---

### 15. TITLE FREEZE

Conservar los títulos H25 actuales durante H37 salvo que la matriz pre-delta descubra dentro de ellos exactamente la misma clase de atribución no acreditada.

Si aparece ese caso:

```text
document
→ STOP before expanding variable
```

No ampliar silenciosamente H37 de description a toda Activity.

Según S36, el falsador seleccionado está en description.

---

### 16. A CONTROL

Ejecutar A completo:

```text
initial
enlist-p1
discover-clue-a
activate-p2
discover-clue-b
reset
```

Verificar:

```text
Activity rows
→ same occurrence count

Activity IDs
→ preserved

occurredAt
→ preserved

provenance
→ preserved

titles
→ preserved

descriptions
→ only authorized semantic reduction
```

Snapshots factuales, Evidence y evaluación deben coincidir con S36/S35 baseline salvo el wording autorizado.

---

### 17. B CONTROL

Ejecutar B completo con la misma App y reglas.

Debe mantenerse:

```text
mirador / patio situated representation
```

donde H25 lo declaraba legítimamente.

Pero la descripción no puede necesitar:

```text
cuenta de Inés
```

para diferenciar B.

Preservar:

```text
different situated editorial presentation
!=
different factual authority
```

---

### 18. ACCOUNT INDEPENDENCE CONTROL

Perturbar únicamente:

```text
member.name
```

en A/B.

Debe cambiar:

```text
account presentation H28
```

y no Activity description H37.

Además, tras H37 no debe existir inconsistencia equivalente a:

```text
GP → Cuenta de Cuenta X

Activity → registrado desde la cuenta de Inés
```

porque Activity ya no debe formular account execution.

Este control demuestra eliminación de la dependencia semántica no acreditada, no una nueva relación entre ambos campos.

---

### 19. SUBJECT PRESENTATION INDEPENDENCE

Perturbar:

```text
DemoScript.subjectPresentations
```

Debe cambiar GP labels y conservar Activity H37.

No utilizar H27 como fuente dinámica de nombres.

Preservar:

```text
GP human presentation
!=
Activity execution attribution
```

---

### 20. SESSION SUBJECT INDEPENDENCE

Cuando resulte técnicamente seguro reutilizar un control aislado equivalente a H34:

```text
operationalSessionSubjectRef X/Y
```

la representación Activity H37 no debe cambiar por esa referencia.

No ejecutar un recorrido si las guards quedan incoherentes.

Clasificarlo como:

```text
isolated transport/composition observation
```

si procede.

El objetivo es demostrar:

```text
sessionSubjectRef
!=
Activity viewer/account provenance
```

---

### 21. EVIDENCE ATTRIBUTION PRESERVATION

Después de cada hallazgo:

```text
Evidence.subjectRefs
```

debe permanecer exactamente igual.

H37 NO reduce la atribución factual existente.

Preservar:

```text
removing "por ti"
!=
removing subject attribution
```

La atribución sigue estando donde ya estaba: Evidence/read models.

---

### 22. OCCURRENCE NEGATIVE CONTROL

Preservar el resultado H25:

```text
rejected / non-admitted occurrence
→ no corresponding accepted Evidence
→ no H25 materialized Activity row
```

El nuevo wording no puede hacer aparecer una Activity antes de la aceptación operacional.

Preservar:

```text
description declaration
!=
occurrence authority
```

---

### 23. EDITORIAL INDEPENDENCE CONTROL

Crear X/Y de harness que varíen únicamente la nueva descripción neutral manteniendo idéntico:

```text
action
Evidence
subjectRefs
state
context
evaluation
K
claim
title
```

Debe resultar:

```text
Activity.description X != Y

facts X == facts Y
evaluation X == evaluation Y
```

Esto conserva el límite H25/H36:

```text
editorial wording
!=
factual truth
```

---

### 24. CONTRADICTION CONTROL

Puede conservarse un control deliberadamente contradictorio de description, si el harness lo permite, para demostrar que una declaración editorial todavía puede mentir sin cambiar hechos.

Pero:

```text
contradictory harness text
```

NO debe introducir viewer/account como si eso acreditase la relación ausente.

El objetivo es preservar:

```text
declared wording
!=
truth
```

---

### 25. SEMANTIC NEGATIVE CHECK

Además de comprobar strings exactos canónicos, inspeccionar las nuevas descripciones para asegurar ausencia de relaciones equivalentes a:

```text
por ti
tu cuenta
desde tu cuenta
cuenta de <nombre>
registrado por <persona>
aportado por <viewer>
```

No limitar este control a una lista lexical.

Documentar semánticamente qué predicados siguen afirmándose.

---

### 26. CURRENT APP EXECUTION REQUIRED

H37 modifica contenido visible de Activity.

Por tanto ejecutar App actual:

```text
A
B
Retail
Arrival
```

En A/B navegar expresamente a:

```text
Activity
```

después de cada Evidence aceptada.

Verificar también Home/Supervisión para regresión acumulada.

Registrar:

```text
DOM/integration verification
→ EXECUTED / NOT EXECUTED

browser visual validation
→ EXECUTED / NOT EXECUTED
```

No equipararlos.

---

### 27. NEGATIVE CONTROLS

Retail y Arrival deben permanecer iguales.

H37 no debe modificar:

```text
generic Activity branch
fixture Activity records
Arrival activity behavior
```

No introducir copy neutral Family Adventure como default global.

---

### 28. CURRENT CUMULATIVE REGRESSION

Sobre fuentes actuales preservar:

```text
H27 GP labels
H28 account
H29 status
H30 journey message
H32 branding + intro
H33 supervision subject
H34 supervision session
H35 Experience name
```

Y, dentro de H25, preservar:

```text
Activity occurrence
Activity title
id
occurredAt
provenance
subject attribution
```

La única diferencia autorizada:

```text
selected Activity.description wording
```

---

### 29. H36 MODEL IMPACT

H37 NO debe intentar convertir H36 en SUPPORTED.

Registrar únicamente qué sucede con el contraejemplo:

```text
C1 viewer/actor claim
C2 account execution claim
```

Si H37 funciona:

```text
unsupported claims
→ eliminated from canonical Activity presentation
```

pero:

```text
H36 historical verdict
→ remains FALSIFIED
```

porque H36 evaluó correctamente la baseline que recibió.

No reescribir S36.

---

### 30. AUTHORITY MODEL OBSERVATION

Si H37 resulta positiva, registrar:

```text
semantic reduction can restore compatibility
without adding missing relation
```

Eso reforzaría una regla metodológica ya observada en:

```text
H29
H33
H34
H37
```

pero NO promoverla todavía como arquitectura.

Posible formulación observacional:

```text
when presentation overstates available authority,
first reduce the claim before expanding the model
```

Estado:

```text
EVIDENCE-BACKED REVIEW HEURISTIC
→ NOT PROMOTED
```

---

### 31. TEST-INFRASTRUCTURE PRESSURE FREEZE

S36 identifica:

```text
TEST-INFRASTRUCTURE PRESSURE
→ MATERIAL
```

H37 NO debe intentar resolverla.

Pero tampoco debe ocultar su coste.

Registrar:

```text
number of historical harnesses modified
number of archived-source routes added
parallel test result
serial test result if needed
```

No cambiar:

```text
timeouts
test runner configuration
worker defaults
historical replay architecture
```

para conseguir H37.

Si H37 sólo pudiera ejecutarse modificando sustancialmente esa infraestructura:

```text
STOP
→ classify infrastructure pressure as blocker
```

Una adaptación mínima al mecanismo histórico ya existente puede documentarse separadamente, como en sesiones previas.

---

### 32. BASELINE / HISTORICAL REPLAY

Preservar:

```text
historical replay
!=
current cumulative verification
```

Los tests históricos H25–H36 deben seguir acreditando sus baselines respectivas.

Si necesitan fuentes archivadas para conservar el wording antiguo:

```text
archive previous source
→ explicit historical routing
```

sin cambiar expectativas históricas.

No hacer que H25 histórico espere retrospectivamente el wording H37.

---

### 33. FALSIFIERS

H37 queda FALSIFIED si:

```text
Activity situated representation
cannot remain meaningful
without viewer/account attribution
```

o si eliminar esos claims requiere:

```text
viewer relation
actor relation
account→execution relation
member→subject relation
H27 labels as universal identity
```

o si el delta cambia:

```text
Evidence
subjectRefs
runtime state
evaluation
K
claim
Activity occurrence
```

o si sólo puede resolverse eliminando Activity o activityPresentation.

También:

```text
if existing sources unexpectedly contain
a legitimate viewer/account execution relation
contradicting H36
→ STOP / INCONCLUSIVE
```

No absorber ese descubrimiento silenciosamente.

---

### 34. OUTPUT

Producir:

```text
session-37-activity-attribution-claim-provenance-and-reduction.md
```

con al menos:

```text
H36 CONSOLIDATED INPUT

H37 HYPOTHESIS

VARIABLE UNDER TEST

WHY NO NEW RELATION IS AUTHORIZED

PRE-DELTA ACTIVITY CLAIM MATRIX

ACTIVITY OCCURRENCE AUTHORITY

EVIDENCE SUBJECT ATTRIBUTION AUTHORITY

H25 EDITORIAL AUTHORITY

VIEWER CLAIM ANALYSIS

ACCOUNT EXECUTION CLAIM ANALYSIS

H27 / ACTIVITY SEPARATION

SESSION SUBJECT / ACTIVITY SEPARATION

REDUCTION DECISION

CANONICAL DESCRIPTION DELTA

NO-NEW-RELATION ANALYSIS

APP CONSUMER BOUNDARY

BASELINE

CODE DELTA OR STOP

A CONTROL

B CONTROL

ACCOUNT INDEPENDENCE CONTROL

SUBJECT PRESENTATION INDEPENDENCE CONTROL

SESSION SUBJECT INDEPENDENCE CONTROL

EVIDENCE ATTRIBUTION PRESERVATION

OCCURRENCE NEGATIVE CONTROL

EDITORIAL INDEPENDENCE CONTROL

CONTRADICTION CONTROL

SEMANTIC NEGATIVE CHECK

CURRENT APP DOM / INTEGRATION EXECUTION

BROWSER VISUAL VALIDATION STATUS

NEGATIVE CONTROLS

CURRENT CUMULATIVE REGRESSION

HISTORICAL REPLAY STATUS

TEST-INFRASTRUCTURE PRESSURE OBSERVATION

EXECUTION TRACE

H25 STATUS

H36 HISTORICAL VERDICT STATUS

ACTIVITY ATTRIBUTION RESULT

AUTHORITY MODEL OBSERVATION

FALSIFICATION ANALYSIS

H37 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

ARTIFACT QUARANTINE

WHAT H37 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 35. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H37
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

NO-NEW-RELATION
→ SUFFICIENT / INSUFFICIENT

VIEWER / ACTOR CLAIM
→ REMOVED AS UNSUPPORTED
  / supported
  / unresolved

ACCOUNT EXECUTION CLAIM
→ REMOVED AS UNSUPPORTED
  / supported
  / unresolved

ACTIVITY OCCURRENCE AUTHORITY
→ PRESERVED / violated

EVIDENCE SUBJECT ATTRIBUTION
→ PRESERVED / violated

H25 SITUATED ACTIVITY PRESENTATION
→ PRESERVED / degraded / falsified

APP CONSUMER BOUNDARY
→ preserved / violated

A/B ACTIVITY REPRESENTATION
→ CURRENT APP DOM-INTEGRATION VERIFIED
  / not established

H36 HISTORICAL VERDICT
→ PRESERVED / improperly rewritten

SEMANTIC REDUCTION HEURISTIC
→ evidence strengthened / unsupported
→ NOT PROMOTED

TEST-INFRASTRUCTURE PRESSURE
→ material / blocking / unchanged

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H38 automáticamente.

---

### 36. METHODOLOGICAL GUARDRAIL

Preservar:

```text
text provenance
!=
claim authority

editorial declaration
!=
truth

Evidence subject attribution
!=
human actor identity

action target
!=
executor

session subject
!=
viewer

member/account
!=
execution source

human-readable narrative
!=
requirement for human identity model

removing unsupported relation
!=
removing factual attribution

situated presentation
!=
perspectival attribution

missing relation
!=
automatic permission to create relation

historical wording
!=
semantic requirement
```

El objetivo de H37 es determinar si los dos contraejemplos materiales que falsificaron H36 pueden resolverse **reduciendo la afirmación al nivel de autoridad existente**, sin expandir el modelo.

Si no pueden, entonces tendremos evidencia real de que una futura relación viewer/actor/account puede ser necesaria.

Si pueden, la ausencia de esa relación deja de ser una necesidad del producto actual y permanece simplemente como una capacidad no modelada.
<!-- FIN-TEXTO-ORIGINAL-S37 -->

---

<a id="sesion-38"></a>

## Capítulo 38 — Portabilidad del replay e integridad de evidencia

**Estado:** instrucción original íntegra.

**Procedencia:** adjunto original aportado por el usuario, identificado como c956bf6f-d232-4bf3-9604-20023f8e238e/pasted-text.txt.

SHA-256 del texto fuente extraído: 8832691f0c88df9a782cc9e15124f80d1d1e493d4b71ce338dd2b5dc0008c2fc.

<!-- INICIO-TEXTO-ORIGINAL-S38 -->
### SESIÓN 38 — HISTORICAL REPLAY PORTABILITY AND EVIDENCE INTEGRITY

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 37 — Activity Attribution Claim Provenance and Reduction
```

No reconstruir decisiones semánticas anteriores.

Esta sesión estudia exclusivamente la **infraestructura de evidencia y replay histórico**.

NO es una sesión de producto.

---

### 1. BASELINE CONSOLIDADA

```text
SESSION 37 → CLOSED

H37
→ SUPPORTED WITH QUALIFICATION

NO-NEW-RELATION
→ SUFFICIENT

VIEWER / ACTOR CLAIM
→ REMOVED AS UNSUPPORTED

ACCOUNT EXECUTION CLAIM
→ REMOVED AS UNSUPPORTED

ACTIVITY OCCURRENCE AUTHORITY
→ PRESERVED

EVIDENCE SUBJECT ATTRIBUTION
→ PRESERVED

H25 SITUATED ACTIVITY PRESENTATION
→ PRESERVED

H36 HISTORICAL VERDICT
→ PRESERVED / FALSIFIED

SEMANTIC REDUCTION HEURISTIC
→ EVIDENCE STRENGTHENED
→ NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Todos los artefactos H21–H37 mantienen su estatuto histórico y sus verdictos originales.

No reinterpretarlos para hacer pasar S38.

---

### 2. INFRASTRUCTURE PRESSURE RECEIVED

S36 clasificó:

```text
TEST-INFRASTRUCTURE PRESSURE
→ MATERIAL
```

S37 aporta evidencia adicional:

```text
95 PASS
3 FAIL
```

Los tres fallos corresponden a:

```text
H21
H22
H23
```

y se producen por lectura/dependencia de:

```text
00-governance/.DS_Store
```

ausente en el entorno actual.

Además, el mantenimiento acumulado incluye ya:

```text
historical harness adaptations
archived-source routing
historical readers
relocated imports
baseline copies
machine/environment sensitivity
```

S38 debe determinar si esta presión puede resolverse **sin degradar la integridad de la evidencia histórica**.

---

### 3. CHARACTER OF SESSION 38

S38 es:

```text
INFRASTRUCTURE FALSIFICATION
+
EVIDENCE INTEGRITY AUDIT
+
PORTABILITY EXPERIMENT
```

Por defecto:

```text
PRODUCT DELTA → NONE
SEMANTIC DELTA → NONE
ARCHITECTURE DELTA → NONE
```

Puede existir un delta de infraestructura de test/replay **sólo después** de demostrar que conserva las propiedades históricas relevantes.

No modificar producto para conseguir una suite verde.

---

### 4. H38 — HYPOTHESIS

Hipótesis falsable:

```text
La evidencia histórica H21–H37
puede reproducirse de forma portable

sin depender de metadata incidental
del sistema operativo o del equipo,

sin reescribir verdictos históricos,
sin relajar assertions materiales,
sin fabricar archivos ambientales faltantes,
sin ocultar cambios de producto,

y conservando la capacidad de distinguir:

historical replay
!=
current cumulative verification.
```

Más concretamente:

```text
material historical evidence
can be separated from
incidental environmental metadata
```

mediante una frontera reproducible y explícita.

---

### 5. WHAT H38 DOES NOT ASSUME

No asumir de antemano que:

```text
.DS_Store
→ incidental
```

aunque ésa sea la hipótesis principal.

No asumir que:

```text
failing historical test
→ obsolete test
```

No asumir que:

```text
green suite
→ evidence preserved
```

No asumir que:

```text
archived byte equality
→ semantic replay integrity
```

La clasificación debe salir de la inspección.

---

### 6. FIRST REQUIRED STEP — FAILURE REPRODUCTION

Antes de modificar infraestructura:

reproducir exactamente los tres fallos actuales:

```text
H21
H22
H23
```

Registrar:

```text
test file
failing assertion
call stack
file/path requested
why that path is requested
which historical invariant
the assertion intended to protect
```

No limitarse al mensaje:

```text
ENOENT .DS_Store
```

Hay que identificar por qué un replay histórico intenta leer ese archivo.

---

### 7. MATERIALITY ANALYSIS OF .DS_STORE

Para cada dependencia de `.DS_Store`, responder:

```text
Was this file intentionally created
as experimental evidence?

Was its content ever inspected
or interpreted by H21/H22/H23?

Was its hash used only because
a directory-wide inventory captured it?

Would changing its bytes
have changed the historical semantic verdict?

Would its absence have changed
runtime behavior or experimental facts?

Was it produced by product code,
test code,
Codex,
or Finder/macOS?
```

Clasificar:

```text
MATERIAL EVIDENCE

INCIDENTAL ENVIRONMENT METADATA

INDETERMINATE
```

con evidencia.

No clasificar por extensión únicamente.

---

### 8. MATERIAL EVIDENCE DEFINITION

S38 debe proponer y aplicar una definición operativa mínima.

Una fuente histórica será MATERIAL si su contenido o identidad fue necesario para acreditar alguno de estos aspectos:

```text
product source under experiment

test/harness logic

fixture / manifest / Scenario / Script / Experience / contract

expected factual or representational output

evaluation input/result

runtime trace

declared experimental relation

baseline source whose preservation
was part of the experiment
```

Ésta es una definición de auditoría S38, no un nuevo contrato de producto.

---

### 9. INCIDENTAL METADATA CANDIDATES

Inspeccionar al menos:

```text
.DS_Store
Thumbs.db
desktop.ini
AppleDouble ._*
temporary editor files
swap files
tsbuildinfo
build artifacts
dependency directories
```

No añadir exclusiones porque “suelen ser basura”.

Para cada familia que realmente aparezca o pueda afectar al mecanismo actual, justificar:

```text
why it is or is not material
```

No crear una blacklist infinita de nombres sin relación con el repositorio.

---

### 10. H21–H23 HISTORICAL INTENT RECONSTRUCTION

Inspeccionar informes, harnesses y evidencia H21/H22/H23.

Para cada sesión identificar:

```text
original hypothesis
variable under test
material source set
baseline mechanism
historical assertions
verdict
```

y responder:

```text
Would removal of .DS_Store from
the preservation inventory
have altered the historical conclusion?
```

Si la respuesta no puede justificarse:

```text
STOP / INCONCLUSIVE
```

No modificar esos replays.

---

### 11. CURRENT REPLAY ARCHITECTURE INVENTORY

Inventariar el mecanismo actual de replay histórico.

Como mínimo:

```text
historical harness files
test-fixtures directories
archived App/source copies
archive-path maps
historical-read helpers
import relocation mechanisms
routing precedence
environment variables for trace recording
baseline manifests
preservation checks
```

Registrar:

```text
component
purpose
sessions depending on it
how many routes/copies
whether portable
whether deterministic
whether machine-specific
```

---

### 12. ROUTING CHAIN ANALYSIS

Documentar explícitamente cómo una lectura histórica decide entre:

```text
current working-tree source

S37 archive
S36 archive
S35 archive
...
older archive
```

Analizar:

```text
precedence
fallthrough
cycles
shadowing
ambiguity
path normalization
Unicode normalization
absolute vs relative paths
```

S37 ya observó normalización Unicode NFC.

Registrar si ésta constituye:

```text
PORTABILITY PRESSURE
```

o sólo normalización segura.

No cambiarla incidentalmente salvo que sea necesaria para H38.

---

### 13. HISTORICAL SOURCE VS ENVIRONMENT SEPARATION

Determinar si el sistema actual mezcla en una misma baseline:

```text
intentional experiment sources

and

whatever happened to exist
in the filesystem at capture time
```

Si ocurre, documentarlo como problema.

La hipótesis candidata es:

```text
historical baseline
should preserve intentional material sources

not arbitrary ambient filesystem state
```

Pero NO promoverla todavía.

Primero falsarla con H21–H37.

---

### 14. CANDIDATE PORTABILITY STRATEGIES

Antes del delta comparar al menos estas estrategias conceptuales:

```text
A. Explicit material-file allowlist

B. Explicit incidental-metadata exclusion policy

C. Material-source manifest generated
   from experiment-owned roots/types

D. Hermetic archived replay package

E. Keep current byte-complete filesystem capture
```

Puede haber otra estrategia si el código actual la sugiere.

Para cada una evaluar:

```text
historical fidelity
risk of hiding changes
portability
maintenance cost
reversibility
complexity
compatibility with existing evidence
```

No seleccionar simplemente la que produzca PASS.

---

### 15. PREFERRED PROPERTY — POSITIVE DEFINITION

Preferir, si es viable, una frontera basada en:

```text
what must be preserved
```

antes que sólo:

```text
what must be ignored
```

Por ejemplo:

```text
material experiment source set
```

es conceptualmente más fuerte que:

```text
ignore .DS_Store
```

pero no imponer esta solución si el repositorio demuestra que sería excesiva.

---

### 16. FORBIDDEN SHORTCUTS

No resolver S38 mediante:

```text
touch .DS_Store

copy .DS_Store from another Mac

create dummy .DS_Store

skip H21/H22/H23

test.skip

catch ENOENT and return success

remove preservation assertions

update historical expected hashes
to current filesystem

increase timeouts

force serial mode
as the semantic fix
```

Tampoco:

```text
delete historical harnesses
```

para reducir coste.

---

### 17. HISTORICAL EXPECTATION FREEZE

Los verdictos y expectativas semánticas históricas permanecen congelados.

S38 puede cambiar:

```text
how historical source material is selected/read
```

sólo si demuestra que:

```text
what is asserted
```

no cambia.

No modificar expected:

```text
actions
Evidence
states
read models
evaluation
K
claim
presentation
composition
```

de ninguna sesión histórica.

---

### 18. BYTE-PRESERVATION QUESTION

Analizar expresamente:

```text
byte preservation
```

frente a:

```text
evidence preservation
```

No son automáticamente equivalentes.

Preguntar:

```text
Which historical files require byte equality?

Which require semantic/executable equality?

Which require only existence?

Which should never have entered
the preservation set?
```

No sustituir hashes por comparaciones laxas de contenido sin justificación.

---

### 19. TEST-FIXTURE PORTABILITY CONTROL

Una vez seleccionado el mecanismo candidato, ejecutar controles en al menos dos condiciones lógicas:

```text
ENVIRONMENT A
→ incidental metadata absent

ENVIRONMENT B
→ equivalent incidental metadata present
```

No es necesario utilizar dos máquinas si puede reproducirse herméticamente mediante fixtures temporales.

El resultado material debe ser idéntico:

```text
historical verdicts
historical assertions
source selection
runtime outputs
```

La metadata incidental no debe afectar.

---

### 20. CONTENT MUTATION CONTROL

Introducir exclusivamente en harness temporal una modificación de un archivo **material** archivado.

Por ejemplo:

```text
change a relevant historical Script declaration
or expected source byte
```

sin tocar el test expected.

El replay/preservation mechanism debe detectar la alteración.

Esto es obligatorio para evitar una falsa solución:

```text
portable
because nothing is actually checked
```

Debe cumplirse:

```text
incidental metadata variation
→ ignored / neutral

material source variation
→ detected
```

---

### 21. MATERIAL FILE REMOVAL CONTROL

Eliminar o esconder temporalmente del harness un archivo material requerido.

Debe producir fallo.

Preservar:

```text
portable
!=
permissive
```

---

### 22. UNKNOWN FILE CONTROL

Añadir al entorno temporal un archivo desconocido no material.

Determinar qué debe ocurrir según el mecanismo seleccionado.

La decisión debe ser explícita.

Opciones legítimas podrían ser:

```text
ignored because outside material source set
```

o:

```text
reported but not evidence-failing
```

No hacer que cualquier archivo nuevo del sistema operativo invalide un replay salvo justificación.

---

### 23. CURRENT PRODUCT SOURCE CONTROL

Modificar sólo una fuente actual —no archivada— en un control temporal.

El replay histórico debe continuar utilizando su fuente archivada cuando corresponda.

A la inversa, la verificación actual debe usar la fuente actual.

Demostrar:

```text
historical replay
!=
current verification
```

operacionalmente, no sólo documentalmente.

---

### 24. ROUTING SHADOW CONTROL

Crear una situación temporal donde exista:

```text
current source
newer archive
older archive
```

para la misma ruta lógica.

Comprobar que la precedencia seleccionada es:

```text
deterministic
documented
appropriate to the historical session
```

No aceptar:

```text
first filesystem match wins
```

si eso depende del entorno.

---

### 25. UNICODE / PATH NORMALIZATION CONTROL

Dado que S37 observó una necesidad de NFC:

comprobar al menos:

```text
NFC / NFD path equivalence
```

en el mecanismo de inventario/routing cuando sea relevante en macOS.

Preservar bytes del archivo.

Normalizar ruta lógica:

```text
!=
normalize file content
```

No introducir case-folding universal sin necesidad.

---

### 26. NODE ENVIRONMENT OBSERVATION

S37 observó:

```text
Codex bundled Node
→ native dependency signature error

official Node 24.14.0 arm64
→ execution possible
```

Clasificar esta presión como:

```text
environment/toolchain

not semantic replay
```

Determinar si el repositorio ya declara una versión de Node.

No modificar versión de Node/package.json/lockfile salvo que sea imprescindible para reproducibilidad y esté explícitamente justificado.

Por defecto:

```text
NODE TOOLCHAIN DELTA → NONE
```

Registrar el entorno usado para S38.

---

### 27. CONCURRENCY / TIMEOUT OBSERVATION

S35 observó timeouts concurrentes.

S37 no reprodujo timeouts, pero sí tres fallos deterministas.

S38 debe distinguir:

```text
resource sensitivity

from

replay correctness
```

No utilizar ejecución serial para ocultar un fallo lógico.

Si se ejecutan ambos modos:

```text
parallel
serial
```

registrar por separado.

No cambiar timeouts.

---

### 28. MINIMAL INFRASTRUCTURE DELTA GATE

Sólo se permite delta si, tras la inspección, se demuestra:

```text
historical invariant preserved
+
environmental dependency incidental
+
candidate mechanism falsifiable
+
material mutation remains detectable
```

Entonces implementar el cambio mínimo.

NO aprovechar S38 para:

```text
refactor all historical tests
deduplicate all fixtures
redesign test architecture
create new framework
rename sessions
clean all archived files
```

---

### 29. TARGETED H21–H23 RECOVERY

Si el mecanismo candidato es válido, H21/H22/H23 deben volver a ejecutar sus **assertions originales materiales** sin necesidad de `.DS_Store`.

Registrar explícitamente:

```text
before H38
→ failure cause

after H38
→ same historical semantic assertions
→ PASS / FAIL
```

No afirmar que sus verdictos sean “más correctos” ahora.

Sólo que el replay vuelve a ser portable.

---

### 30. FULL HISTORICAL REPLAY CONTROL

Después del delta —si existe— ejecutar la suite histórica completa disponible.

Registrar:

```text
PASS
FAIL
TIMEOUT
NOT EXECUTED
```

por sesión/harness relevante.

No resumir una suite parcialmente ejecutada como PASS.

---

### 31. CURRENT CUMULATIVE VERIFICATION

Ejecutar también la verificación de código actual disponible.

No basta con que los replays históricos sean verdes.

Preservar:

```text
historical replay
→ historical sources

current cumulative verification
→ current sources
```

No hacer que el nuevo routing intercepte accidentalmente los tests actuales.

---

### 32. PRODUCT FREEZE

Verificar byte-identidad frente a S37 de al menos:

```text
App
contracts
bootstrap
adapter
projectors/evaluation
artifacts A/B
fixtures
manifests
Scenario/Script/Experience definitions
```

Producto:

```text
MUST REMAIN UNCHANGED
```

Si una corrección de infraestructura exige cambiar producto:

```text
STOP
```

---

### 33. SEMANTIC FREEZE

H38 no puede modificar:

```text
Activity wording H37
GuestPerspective
SupervisionPerspective
Evidence semantics
subject semantics
session semantics
Experience semantics
evaluation
K
claim
```

No usar S38 para corregir otras presiones.

---

### 34. EVIDENCE-INTEGRITY MANIFEST

Si el experimento se sostiene, producir un artefacto documental que describa la frontera de evidencia histórica.

NO necesariamente un nuevo contrato runtime.

Debe indicar al menos:

```text
material-source inclusion rule

incidental-environment exclusion rule

path normalization rule

archive routing precedence

historical/current separation

mutation detection behavior
```

Estado:

```text
TEST INFRASTRUCTURE EVIDENCE RULE
→ LOCAL / EXPERIMENTAL
```

No ADR por defecto.

---

### 35. REPLAY MAINTENANCE COST MEASUREMENT

Comparar antes/después:

```text
number of archive routes

number of historical readers

number of archived source copies

number of historical harnesses requiring adaptation

amount of source-specific routing
```

S38 no necesita reducir todos esos números.

La pregunta es si el mecanismo seleccionado:

```text
prevents incidental-environment growth
```

y evita que futuras sesiones tengan que preservar metadata irrelevante.

No declarar resuelto el coste general si sólo desaparece `.DS_Store`.

---

### 36. FALSIFIERS

H38 queda FALSIFIED si:

```text
.DS_Store or equivalent metadata
was materially required
for the historical verdict
```

o si:

```text
removing incidental metadata from replay
also hides mutation of material sources
```

o si:

```text
historical expectations must be weakened
to obtain portability
```

o si:

```text
current tests begin consuming archived sources
```

o si:

```text
historical replay starts consuming current sources
```

o si la solución requiere:

```text
fabricating environmental files
changing product
changing historical semantics
deleting failing tests
```

H38 queda INCONCLUSIVE si no puede distinguir materialidad con evidencia suficiente.

Ante falsador:

```text
STOP
→ preserve failing replay
→ document exact portability dependency
```

No continuar refactorizando.

---

### 37. POSSIBLE POSITIVE VERDICT

H38 puede resultar:

```text
SUPPORTED WITH QUALIFICATION
```

si demuestra:

```text
incidental metadata excluded safely

material files still protected

H21–H23 replay restored

historical/current separation preserved

product unchanged

historical expectations unchanged
```

La cualificación debe registrar:

```text
platforms/environments actually tested
remaining routing complexity
remaining concurrency/toolchain pressure
```

No afirmar portabilidad universal.

---

### 38. TEST-INFRASTRUCTURE PRESSURE RESULT

Distinguir al final:

```text
METADATA PORTABILITY PRESSURE

ARCHIVE ROUTING COMPLEXITY

TOOLCHAIN PRESSURE

CONCURRENCY PRESSURE
```

No reducirlas todas a una sola variable.

Posibles estados:

```text
EXPERIMENTALLY ADDRESSED

PRESERVED / OPEN

MATERIAL / NON-BLOCKING

BLOCKING
```

---

### 39. PROMOTION GATE

S38 NO puede:

```text
create product ADR
modify Architecture v0.5
modify TES
modify PSC
create PSC-P02
```

Si emerge una regla estable de infraestructura:

```text
candidate test/evidence governance rule
→ evidence-backed
→ NOT PROMOTED
```

Una sesión posterior decidirá si merece consolidación formal.

---

### 40. OUTPUT

Producir:

```text
session-38-historical-replay-portability-evidence-integrity.md
```

con al menos:

```text
H37 CONSOLIDATED INPUT

H38 HYPOTHESIS

INFRASTRUCTURE PRESSURE RECEIVED

FAILURE REPRODUCTION

H21–H23 HISTORICAL INTENT

.DS_STORE MATERIALITY ANALYSIS

MATERIAL EVIDENCE DEFINITION

INCIDENTAL METADATA ANALYSIS

CURRENT REPLAY ARCHITECTURE INVENTORY

ROUTING CHAIN ANALYSIS

HISTORICAL SOURCE / ENVIRONMENT SEPARATION

CANDIDATE PORTABILITY STRATEGIES

STRATEGY DECISION

MINIMAL INFRASTRUCTURE DELTA GATE

BASELINE

INFRASTRUCTURE DELTA OR STOP

PRODUCT FREEZE

SEMANTIC FREEZE

H21 CONTROL

H22 CONTROL

H23 CONTROL

INCIDENTAL METADATA ABSENCE CONTROL

INCIDENTAL METADATA PRESENCE CONTROL

MATERIAL CONTENT MUTATION CONTROL

MATERIAL FILE REMOVAL CONTROL

UNKNOWN FILE CONTROL

CURRENT / HISTORICAL SOURCE SEPARATION CONTROL

ROUTING SHADOW CONTROL

UNICODE / PATH NORMALIZATION CONTROL

NODE ENVIRONMENT OBSERVATION

CONCURRENCY / TIMEOUT OBSERVATION

FULL HISTORICAL REPLAY RESULT

CURRENT CUMULATIVE VERIFICATION

EVIDENCE-INTEGRITY MANIFEST

REPLAY MAINTENANCE COST

TEST-INFRASTRUCTURE PRESSURE RESULT

FALSIFICATION ANALYSIS

H38 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

PROMOTION GATE STATUS

WHAT H38 DOES NOT PROVE

REMAINING PRESSURES
```

---

### 41. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H38
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

HISTORICAL REPLAY PORTABILITY
→ experimentally supported
  / unsupported
  / unresolved

.DS_STORE MATERIALITY
→ INCIDENTAL
  / MATERIAL
  / INDETERMINATE

H21 REPLAY
→ PASS / FAIL / NOT EXECUTED

H22 REPLAY
→ PASS / FAIL / NOT EXECUTED

H23 REPLAY
→ PASS / FAIL / NOT EXECUTED

MATERIAL MUTATION DETECTION
→ PRESERVED / DEGRADED

HISTORICAL EXPECTATIONS
→ UNCHANGED / MODIFIED-INVALIDLY

PRODUCT SOURCES
→ UNCHANGED / MODIFIED-INVALIDLY

HISTORICAL / CURRENT SEPARATION
→ PRESERVED / VIOLATED

METADATA PORTABILITY PRESSURE
→ experimentally addressed / open / blocking

ARCHIVE ROUTING COMPLEXITY
→ open / reduced / blocking

TOOLCHAIN PRESSURE
→ open / non-blocking / blocking

CONCURRENCY PRESSURE
→ open / non-blocking / blocking

TEST-INFRASTRUCTURE PRESSURE
→ status

CANDIDATE EVIDENCE GOVERNANCE RULE
→ evidence-backed / insufficient
→ NOT PROMOTED

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H39 automáticamente.

---

### 42. METHODOLOGICAL GUARDRAIL

Preservar:

```text
green test
!=
valid evidence

byte capture
!=
material evidence

filesystem presence
!=
experimental relevance

incidental metadata
!=
historical source

portable replay
!=
weakened replay

ignoring irrelevant files
!=
ignoring relevant mutations

historical replay
!=
current verification

historical source
!=
current source

archive routing
!=
semantic authority

environmental failure
!=
semantic falsification

semantic PASS
!=
infrastructure PASS

infrastructure repair
!=
historical rewrite
```

El objetivo de S38 es hacer que el instrumento de falsación sea nuevamente confiable y portable.

No se trata de conseguir una suite verde.

Se trata de demostrar que:

```text
the same material historical evidence
produces the same historical verdict
independently of incidental machine metadata
```

sin perder sensibilidad frente a cambios materiales.
<!-- FIN-TEXTO-ORIGINAL-S38 -->
