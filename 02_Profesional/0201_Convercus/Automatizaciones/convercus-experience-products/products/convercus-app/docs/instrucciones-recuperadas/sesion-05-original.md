# Convercus Demo Factory — Session 5: Minimum Reversible Experiment Implementation

## Purpose

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

# Governing principle

Implement:

**Two demos. One core. No forks.**

The two demos are:

1. the existing retail-like baseline;
2. a new hospitality demo designed to stress configuration boundaries.

Do not create a separate React application for hospitality.

Do not duplicate the application core.

Do not redesign the repository globally.

---

# Existing architecture decisions

Respect the accepted ADRs.

## ADR-001

TES governs semantic meaning and invariants.

Do not modify:

* TES source excerpts;
* TES Ontology;
* Experience Ledger;
* Lexicon;
* Protocol;

unless the experiment discovers a genuine semantic contradiction.

No such modification is expected in Session 5.

## ADR-002

Maintain logical separation between:

* composition/configuration;
* mutable runtime state where needed;
* read models/projections.

This does NOT require three physical stores.

Use the smallest realization appropriate for the experiment.

---

# Hypotheses under test

## H1 — Demo Manifest + Effective Bootstrap Composition

Test whether a small declarative demo configuration can describe desired composition while bootstrap resolves the effective composition.

The experiment must show:

* more than one demo can exist;
* a prospect is not hard-coded to one demo;
* requested configuration and resolved runtime are distinguishable;
* invalid references fail explicitly;
* secrets or environment implementation details do not live in the demo manifest.

Do not create a large universal configuration schema.

---

## H2 — Scenario / Experience / Demo Script Separation

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

## H3 — Evidence / Occurrence / TES Event / Activity Projection

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

## H4 — Provider Resolution

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

# Demo A — Retail baseline

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

# Demo B — Hospitality stress demo

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

# Subject and context constraint

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

# Brand resolution

The hospitality demo must use a different brand configuration.

Remove only the hard-coded Convercus-brand assumptions necessary for the experiment.

Brand selection must originate from demo configuration/resolution rather than requiring source-code edits to switch demos.

Validate at minimum:

* brand identifier;
* required assets/tokens;
* fallback/error behaviour.

Do not build a complete design system.

---

# Fixture separation

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

# Demo selection

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

# Capability provenance

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

# Activity

Activity must continue to work in both demos.

But:

* Activity is a read model;
* hospitality input should not have to become an `ActivityItem` merely to exist;
* visual fields belong to projection/presentation where reasonably possible.

Do not perform a broad Activity refactor.

Only introduce the minimum separation required by the experiment.

---

# Reset

Retail and hospitality locally controlled mock state must reset deterministically.

Reset applies only to state controlled by the demo.

Do not generalize this to future live providers.

Prove that resetting Demo A cannot mutate Demo B state and vice versa.

---

# Validation and failure behaviour

Bootstrap/configuration must fail explicitly for materially invalid configuration.

At minimum test:

* unknown demo id;
* missing referenced brand;
* missing required fixture;
* incompatible or unresolved configuration where applicable.

Avoid silent fallback that could accidentally display another prospect's data.

---

# Isolation requirements

The experiment must verify that:

* retail assets/content do not appear in hospitality;
* hospitality assets/content do not appear in retail;
* fixture state is isolated;
* reset is isolated;
* demo selection is explicit;
* no implicit "default prospect leakage" occurs.

---

# Testing strategy

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

# Incremental implementation discipline

Work in small dependency-ordered increments.

After each increment:

1. run the relevant tests;
2. report what hypothesis the increment tests;
3. inspect for accidental cross-demo coupling;
4. do not proceed if the increment invalidates an accepted ADR.

Preferred sequence:

### Step 1 — Characterize baseline

Run the current relevant test suite before modifying code.

Record baseline status.

### Step 2 — Define minimal demo configuration boundary

Introduce only the minimum structures required for two demos.

Test H1.

### Step 3 — Externalize retail fixtures

Move prospect-specific fixture data out of `MockDataAdapter`.

Preserve behaviour.

Test H4.

### Step 4 — Resolve demo during bootstrap

Remove direct prospect/data choice from `App.tsx`.

Use the smallest resolver seam.

Test H1 + H4.

### Step 5 — Resolve branding

Allow retail and hospitality brands/configuration to differ.

Test isolation.

### Step 6 — Add hospitality configuration and fixtures

Introduce the hospitality Scenario/context/actors.

Test H2.

### Step 7 — Preserve Activity as projection

Make only the minimum changes required to prevent factual fixture input from being defined solely in UI terms.

Test H3.

### Step 8 — Reset/isolation

Verify deterministic isolated reset.

### Step 9 — Cross-demo validation

Run both demos and the full relevant test suite.

---

# Stop conditions

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

# Prohibited premature work

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

# Required evidence after implementation

At completion provide:

## A. Change inventory

List:

* files added;
* files modified;
* files intentionally untouched.

## B. Test evidence

Report:

* baseline tests before changes;
* tests after each relevant stage;
* final complete relevant test run.

## C. Hypothesis verdict

For H1–H4 assign:

* SUPPORTED BY EXPERIMENT
* PARTIALLY SUPPORTED
* FALSIFIED
* INCONCLUSIVE

Give evidence.

## D. Architecture deviations

Report every place implementation required deviation from:

* ADR-001;
* ADR-002;
* Session-4 experiment specification.

## E. Technical debt introduced

Explicitly list temporary compromises.

Do not hide experimental shortcuts.

## F. Reversibility

Explain exactly how the experiment could be removed.

## G. Next-decision recommendation

State what architectural decision is now mature enough for Session 6.

Do not automatically propose implementing more features.

---

# Final evaluation questions

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

# Success criterion

The experiment succeeds if:

**the same application core can demonstrably run two materially different prospect demos through explicit configuration/composition, without forks and without prospect-specific leakage, while preserving accepted semantic and architectural boundaries.**

Do not optimize beyond this criterion.
