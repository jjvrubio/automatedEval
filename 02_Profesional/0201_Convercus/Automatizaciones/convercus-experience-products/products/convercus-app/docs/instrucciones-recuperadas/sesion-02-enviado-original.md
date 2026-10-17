# Convercus Demo Factory — Session 2: Repository Anatomy and Semantic Architecture

## Purpose of this session

Using the repository assessment already produced, perform a second, deeper architectural analysis of the current Convercus repository.

Do **not** modify any files, generate implementation code, perform a refactor, install dependencies, or redesign the application.

The purpose of this session is to progress through the following cognitive sequence:

**REMEMBER → UNDERSTAND → APPLY → ANALYZE → EVALUATE → CREATE**

The final output should therefore not merely describe the repository. It should reconstruct the current architecture, understand the TES-governed semantic model, test architectural hypotheses against representative commercial scenarios, compare alternatives, and create an evidence-based target architecture hypothesis for the future Demo Factory.

Treat all architectural statements below as **hypotheses to test**, not conclusions to force onto the repository.

---

# 0. Epistemic rules

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

# BLOOM LEVEL 1 — REMEMBER

## Reconstruct the current system

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

# BLOOM LEVEL 2 — UNDERSTAND

## Reconstruct the semantic model

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

# BLOOM LEVEL 2B — UNDERSTAND THE ACTIVITY HYPOTHESIS

## Distinguish current Activity from a possible interaction model

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

# BLOOM LEVEL 3 — APPLY

## Apply the semantic model to representative commercial scenarios

Without implementing anything, test the reconstructed domain model against four representative sectors:

### A. Airline loyalty

Possible interactions may include, only as test examples:

* booking;
* flight;
* ancillary purchase;
* status progression;
* redemption;
* campaign participation.

### B. Retail loyalty

Possible interactions may include:

* purchase;
* product/category behaviour;
* coupon use;
* referral;
* promotion participation;
* redemption.

### C. Public transport / sustainable mobility

Possible interactions may include:

* trip;
* route usage;
* mobility challenge;
* participation;
* badge/reward-related effects;
* repeated behavioural patterns.

### D. Hospitality

Model one hotel chain containing at least two distinct commercial scenarios:

#### Business Hotel Scenario

Examples may include:

* booking;
* stay;
* check-in;
* breakfast;
* repeated stays;
* upgrades;
* meeting-related services;
* late checkout.

#### Vacation Resort Scenario

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

# BLOOM LEVEL 3B — APPLY THE EXPERIENCE / INTERACTION RELATIONSHIP

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

# BLOOM LEVEL 4 — ANALYZE

## Analyze the architecture as a composition system

Treat the following as a working hypothesis:

> `DemoPackage` may evolve into the authoritative composition contract for a demo, while TES remains the semantic authority for domain concepts such as `Experience`.

Analyze whether this separation is coherent with the existing repository.

In particular distinguish:

### Semantic authority

What defines what an Experience **means**?

### Composition authority

What defines which Experiences, capabilities, data, brand and scenarios belong to a specific demo?

### Runtime authority

What decides which adapter, modules and state are active?

### Presentation authority

What decides how underlying state is displayed?

---

## Analyze these candidate responsibilities

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

# Scenario vs Experience vs Demo Script

Explicitly test whether these concepts should remain separate.

## Scenario

Working definition:

A commercial/demo context describing:

* prospect context;
* actors;
* initial conditions;
* use case;
* business hypothesis;
* relevant configuration.

## Experience

Must use TES-derived meaning.

Do not redefine it from the working definition of Scenario.

## Demo Script

Working definition:

An optional presenter-facing sequence used to demonstrate a Scenario.

A Demo Script is necessarily ordered because a presentation occurs through time.

Its ordering must **not imply that the underlying Experience itself is sequential**.

Determine whether this distinction is architecturally useful and semantically safe.

---

# Interaction Trace vs Experience

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

# DemoPackage vs AppSnapshot

Analyze the current disconnect between `DemoPackage` and `AppSnapshot`.

Explain:

* what each represents today;
* whether one should contain the other;
* whether both should instead depend on a third runtime/domain model;
* whether `AppSnapshot` should remain adapter-facing;
* how Experience-derived state might become visible to the UI without coupling TES directly to React.

Do not redesign either interface prematurely.

---

# BLOOM LEVEL 5 — EVALUATE

## Evaluate architectural alternatives

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

### Semantic fidelity

Does it preserve TES as semantic authority?

### Reusability

Can new prospects be created mainly through configuration?

### Sector scalability

Can airline, retail, mobility and hospitality coexist?

### Scenario flexibility

Can one hotel brand support both business-hotel and resort scenarios?

### Experience flexibility

Can scenarios use different Experience combinations without redefining Experience?

### Interaction flexibility

Can the same interaction model support sector-specific interaction types without requiring sector-specific application forks?

### API evolution

Can mock, simulation and future Convercus API adapters coexist?

### Complexity

What technical complexity does the model introduce?

### Marginal Demo Code Cost

Would each additional demo tend to require less new code?

### Risk

What are the likely failure modes?

---

# Explicitly evaluate the following working principles

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

# BLOOM LEVEL 6 — CREATE

## Create an evidence-based target architecture hypothesis

Without generating implementation code, create a proposed **Demo Factory Architecture v0.1**.

This is not yet an implementation specification.

It should contain:

### 1. Architecture map

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

### 2. Authority map

Explicitly state which layer is authoritative for:

* semantic meaning;
* demo composition;
* data acquisition;
* Experience evaluation;
* runtime state;
* presentation;
* branding;
* scenario configuration.

### 3. Core invariants

Propose a small set of architectural invariants that future implementation should not violate.

Example form:

> “Adding a new prospect must not require redefining TES domain concepts.”

Do not simply copy this example; derive the invariants from the evidence.

### 4. Minimum viable architectural transition

Identify the **minimum architectural changes** required to make a second prospect demo possible without copying or forking the application.

Do not implement them.

Order them by dependency, not by coding convenience.

### 5. Explicit non-goals

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

### 6. Open semantic questions

List all remaining TES/domain questions that must be resolved before implementation.

Do not hide unresolved semantic uncertainty behind architectural abstractions.

### 7. Architecture Decision candidates

Identify the decisions that are now mature enough to become future ADRs.

Do not write the ADRs yet.

---

# Final architectural stress test

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

# Output structure

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
