# Convercus Demo Factory — Session 3: Adversarial Architecture Review and ADR Falsification

## Purpose

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

# Epistemic discipline

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

# New product interpretation to test

A product-level interpretation has now been adopted provisionally:

## Observed Occurrence / Trace / TES Event

TES is not being extended.

The working product interpretation is:

* observable reality may produce an **Observed Occurrence**;
* instrumentation may preserve a **Trace** allowing occurrence reconstruction/confirmation;
* an occurrence becomes a TES Event only through relevant contextual recognition within an Experience;
* Activity is a read model/presentation projection and not a semantic source of truth.

Do not assume this realization is architecturally correct merely because it is semantically compatible with TES.

Attempt to falsify the way Demo Factory proposes to materialize this distinction.

---

# Coverage analytical hypothesis

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

# ADR candidates under review

Attempt to falsify the following six candidate decisions.

---

# ADR-001 — TES Semantic Authority

## Candidate proposition

TES remains the authoritative source for the meaning of Experience and its core experiential categories.

Product contracts, runtime models and DemoPackage composition must remain subordinate to TES and traceable to it.

### Attempted falsification

Search for cases where:

* TES is too abstract to govern an executable demo;
* product semantics necessarily diverge;
* different technical implementations require contradictory interpretations;
* versioning TES could make runtime packages unstable;
* Demo Factory would need concepts TES explicitly excludes;
* strict subordination to TES could prevent legitimate product extensions.

Determine what authority TES should possess and where that authority must stop.

---

# ADR-002 — DemoPackage as Composition Root

## Candidate proposition

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

### Attempted falsification

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

# ADR-003 — Separation of Scenario / Experience / Demo Script

## Candidate proposition

Keep three concepts distinct:

### Scenario

Commercial/demo context, actors, initial conditions, relevant configuration and use case.

### Experience

TES-governed situated transformation.

### Demo Script

Optional presenter-facing sequence used to demonstrate a Scenario.

### Attempted falsification

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

# ADR-004 — Observed Occurrence / Trace / TES Event / Projection

## Candidate proposition

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

### Attempted falsification

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

# Coverage falsification experiment

Treat coverage separately from ADR-004.

Test the set-cover adaptation critically.

## Model A — Observed-field coverage

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

## Model B — Experience requirement/evidence coverage

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

## Required decision

For each model classify coverage as:

* useful analytical construct;
* useful only under strict constraints;
* misleading abstraction;
* redundant with existing TES/product concepts;
* insufficient evidence.

If retained, propose terminology that explicitly prevents confusion with TES Progression.

---

# ADR-005 — Runtime State / Read Models

## Candidate proposition

Separate:

1. immutable/versioned demo composition;
2. canonical mutable runtime state;
3. read models/UI projections.

`AppSnapshot` may survive as a read model but should not simultaneously represent backend response, canonical truth and presentation.

### Attempted falsification

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

# ADR-006 — Data Adapter Resolution

## Candidate proposition

The runtime should resolve data adapters during demo bootstrap/composition rather than instantiate `MockDataAdapter` directly inside the application.

Adapters should provide the boundary between external/simulated data and domain/runtime processing.

### Attempted falsification

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

# Cross-ADR falsification

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

# Sector stress tests

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

# BLOOM LEVEL 4 — ANALYZE

For each ADR:

1. decompose its assumptions;
2. identify dependencies;
3. identify what evidence supports it;
4. identify what evidence is merely inferred;
5. identify potential counterexamples;
6. identify interaction with the other ADRs.

Do not approve or reject yet.

---

# BLOOM LEVEL 5 — EVALUATE

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

# BLOOM LEVEL 6 — CREATE

After adversarial evaluation, create:

## A. Revised architecture decision set

Only include decisions that survived or were successfully revised.

## B. Rejected assumptions

List ideas from Sessions 1–2 that should no longer guide implementation.

## C. Deferred questions

Identify decisions requiring:

* API evidence;
* TES clarification;
* product validation;
* real prospect use;
* implementation experiment.

## D. Revised Demo Factory Architecture v0.2

Produce an architecture map reflecting only surviving decisions.

Do not preserve Architecture v0.1 merely for continuity.

## E. ADR readiness

For each surviving decision classify it as:

* ready to write as ADR;
* provisional ADR;
* not ready for ADR.

## F. Minimum reversible experiment

Propose the smallest implementation experiment that could test the architecture after the ADRs are approved.

The experiment must be reversible and must not require:

* full API integration;
* Experience Builder;
* multi-tenant backend;
* full UI refactor.

Prefer a test involving two prospect configurations on the same shared core.

Do not implement it.

---

# Final meta-review

Before concluding, answer:

1. Which architecture assumption from Session 2 was easiest to falsify?
2. Which survived the strongest attack?
3. Which assumption remains most dangerous despite appearing reasonable?
4. What are we most likely to be over-engineering?
5. What are we most likely to be under-modeling?
6. Did the set-cover-inspired `coverage` hypothesis add analytical value or merely new terminology?
7. What evidence would most likely cause Architecture v0.2 to be revised again?

---

# Required output structure

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
