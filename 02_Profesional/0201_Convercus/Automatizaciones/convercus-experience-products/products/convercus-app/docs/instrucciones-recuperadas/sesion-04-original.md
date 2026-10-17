# Convercus Demo Factory — Session 4: ADR Formalization and Minimum Reversible Experiment Specification

## Purpose

Session 3 completed the adversarial falsification of Architecture v0.1 and produced Architecture v0.2.

Do not perform another broad architecture redesign.

Do not implement the experiment yet.

Session 4 has two objectives:

1. formalize only the architectural decisions that are sufficiently mature;
2. transform the remaining provisional decisions into explicit hypotheses to be tested by a minimum reversible implementation experiment.

The cognitive emphasis is:

**CREATE → prepare for APPLY**

---

# Part A — Formalize mature ADRs

Create exactly two ADRs.

Before creating them, inspect the repository's existing governance/decision conventions and follow them where applicable.

Do not invent a new ADR format if the repository already defines one.

## ADR-001 — Bounded TES Semantic Authority

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

## ADR-002 — Logical Separation of Composition, Runtime State and Read Models

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

# Part B — Record provisional architecture hypotheses

Do NOT convert the following into accepted ADRs yet.

Create a Session-4 experiment hypothesis document recording four provisional decisions.

## H1 — Demo Manifest + Effective Bootstrap Composition

Hypothesis:

A small versioned demo manifest should declare desired logical composition, while bootstrap/deployment policy resolves the effective composition.

Test:

* multiple demos per prospect;
* versioned references;
* no secrets in manifest;
* requested vs resolved capabilities;
* failure of invalid references.

---

## H2 — Scenario / Experience / Demo Script Separation

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

## H3 — Evidence / Occurrence / TES Event / Activity Projection

Hypothesis:

The product must preserve the semantic distinction between factual/evidentiary input and TES Event interpretation without requiring every concept to exist as a separate persisted object.

Test only what is needed for the two-demo experiment.

Do NOT build a general occurrence/evidence event store.

Activity must remain a projection/read model.

---

## H4 — Provider Resolution by Capability

Hypothesis:

Providers should be resolved outside `App.tsx`, potentially at capability/port level, rather than assuming one universal adapter per demo.

For the experiment, do not design the future provider architecture.

Use the existing mock implementation where possible while introducing only the smallest seam required to test external resolution.

---

# Part C — Preserve coverage as experimental analytics only

Do not create an ADR for coverage.

Record two separate experimental analytical ideas:

### Observation overlap

Provisional term:

**Experience-portfolio observation overlap**

Purpose:

Explore overlap/unrelated observed occurrences across Experience evaluations.

### Evidence sufficiency

Provisional term:

**Experience evidence sufficiency profile**

Purpose:

Represent sufficient / insufficient / contradictory / pending evidence without claiming TES Progression.

Neither should be implemented in the minimum experiment.

---

# Part D — Specify the Minimum Reversible Experiment

Design, but do not implement, the smallest experiment that tests H1–H4.

## Experimental principle

**Two demos. One core. No forks.**

### Demo A — Retail baseline

Remain close to the current prototype.

Use the current general application behaviour where possible.

### Demo B — Hospitality

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

# Experiment acceptance criteria

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

# Reversibility requirement

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

# Explicit non-goals

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

# Implementation sequence proposal

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

# Final pre-implementation review

Before concluding Session 4 answer:

1. identify whether either of the two ADRs still contains an unresolved assumption that should prevent acceptance;
2. identify whether the proposed experiment is testing architecture or merely implementing it;
3. remove any experimental feature that is not needed to falsify H1–H4;
4. identify the single most informative failure the experiment could produce;
5. state what result would cause each hypothesis H1–H4 to be rejected.

---

# Required output

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
