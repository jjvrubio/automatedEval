# Convercus Demo Factory — Session 6: Experiment Consolidation and Architecture Promotion

## Purpose

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

# Part A — Verify Session-5 evidence

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

# Part B — ADR-003: Desired vs Effective Demo Composition

Create one new ADR following the existing repository ADR conventions.

Suggested title:

**ADR-003 — Desired and Effective Demo Composition**

The decision should formalize the following distinction:

## Desired composition

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

## Effective composition

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

## Authority boundaries

The ADR must establish that:

* the manifest declares intent;
* bootstrap/resolution validates and resolves;
* deployment/environment provides implementation constraints and secrets;
* runtime session owns mutable execution state when required;
* read models represent presentation;
* TES remains authoritative only for governed semantic meaning.

---

## Important constraints

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

# Part C — Promotion review of Session-5 implementation

Review every architectural element introduced by Session 5 and classify it into exactly one category:

### PROMOTE

The concept and current implementation are sufficiently supported to become part of the working Demo Factory baseline.

### PROMOTE WITH QUALIFICATION

The seam/concept should remain, but part of the current implementation is experimental or temporary.

### RETAIN AS EXPERIMENTAL

Keep temporarily because further experiments depend on it, but do not treat it as architecture.

### DEPRECATE

It is no longer conceptually authoritative and should eventually be removed or migrated.

### REMOVE

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

# Part D — Competing source-of-truth analysis

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

# Part E — Do not over-promote H2–H4

## H2 — Scenario / Experience / Demo Script

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

## H3 — Evidence / Occurrence / TES Event / Activity

Do not create an ADR.

Session 5 established that Activity can remain a projection and factual inputs need not contain UI concerns.

It did NOT establish a general evidence/event architecture.

State exactly what remains untested.

---

## H4 — Provider Resolution

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

# Part F — Architecture v0.3

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

# Part G — Select the next empirical question

Do NOT automatically choose the most sophisticated next feature.

Compare at least these candidate experiments:

### Candidate A — Third-demo marginal-cost test

Add a third materially different demo to test whether Session-5 abstractions genuinely reduce Marginal Demo Code Cost.

### Candidate B — H3 contextual Experience evaluation

Use the smallest possible in-memory example where one factual input/evidence can be evaluated differently in relation to two Experiences.

Do not build an event store or full Experience engine.

### Candidate C — H4 hybrid provider experiment

Use two controlled local/mock providers for different capabilities to test whether provider-by-capability resolution is actually required.

Do not use the real Convercus API.

### Candidate D — Scenario / Demo Script operational test

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

# Part H — Marginal Demo Code Cost

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

# Required output

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
