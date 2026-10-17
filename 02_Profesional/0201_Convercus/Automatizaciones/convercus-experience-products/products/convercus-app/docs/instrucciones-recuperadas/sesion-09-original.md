# Convercus Demo Factory — Session 9: Contextual Multi-Experience Evaluation Experiment

## Purpose

Session 8 promoted H2 into ADR-004 and confirmed Architecture v0.4.

The highest-value unresolved architectural hypothesis is now H3:

**Evidence / occurrence and TES Event interpretation must remain semantically distinct, while Activity remains a derived projection.**

Session 9 must test only one narrow proposition:

> The same factual/evidentiary input can be evaluated differently in relation to two Experience references without storing its significance as an intrinsic universal property and without building a general Experience engine.

The cognitive cycle is:

**APPLY → TEST → EVALUATE**

Implementation is evidence generation.

---

# Governing semantic constraints

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

# H3 hypothesis under test

The product interpretation currently states:

1. not every observable occurrence is automatically a TES Event;
2. evidence/trace and experiential interpretation are distinct responsibilities;
3. significance may depend on the Experience context;
4. one evidentiary input may potentially be evaluated relative to zero, one or multiple Experiences;
5. Activity is a presentation/read-model projection rather than the semantic source of truth.

Session 9 must generate executable evidence for or against points 2–5.

---

# Critical limitation

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

# Experiment shape

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

# Experience selection

Before implementation, inspect the existing Experience definitions/references and semantic documentation.

Prefer existing definitions or references where possible.

Do not invent two rich new TES Experiences solely to satisfy the test.

If the repository does not contain two semantically defensible Experience references for the chosen evidence:

STOP.

Report that the experiment lacks sufficient semantic material rather than fabricating Experience semantics.

A stop condition is a valid result.

---

# Factual/evidentiary input

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

# Contextual evaluation boundary

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

# Required evaluation properties

The experiment must demonstrate that:

## 1. Same factual input

The underlying evidentiary input is identical when evaluated against both Experiences.

## 2. Experience-relative interpretation

The resulting evaluation may differ according to Experience context.

## 3. Input immutability

Evaluating Experience A must not overwrite the factual input with A-specific meaning before Experience B evaluates it.

## 4. Independent evaluation

Evaluation order must not change the result unless existing semantics explicitly require stateful dependence.

For this experiment prefer deterministic independent evaluation.

## 5. Explicit outcome

Each Experience evaluation must return an explicit result rather than mutate hidden state as a side effect.

---

# Many-to-many qualification

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

# Activity projection

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

# No forced persistence model

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

# No progression semantics

A successful evaluation must not automatically change:

* Experience Progression;
* Completion;
* Result.

If an existing demo-level/read-model indicator changes for demonstration purposes, label it explicitly as demo/runtime state rather than TES Progression.

---

# Tests required

Add only the smallest tests necessary.

At minimum prove:

## 1. Identical input

Both Experience evaluations receive the same factual input.

## 2. Different contextual result

Experience A and Experience B produce meaningfully different evaluation results.

## 3. Input remains unchanged

Evaluation does not mutate the factual input.

## 4. Evaluation isolation

Evaluating A then B produces the same per-Experience outcomes as evaluating B then A.

## 5. Zero-match possibility

Where practical, show that an input can produce no relevant evaluation for an unrelated Experience/context.

Do not invent a third Experience solely for this if an existing valid case is unavailable.

## 6. Activity remains projection

The read model may represent the resulting behaviour without becoming an evaluation input.

## 7. Existing presenter action regression

Session-7 Hospitality behaviour continues to pass.

## 8. Retail regression

Retail remains unaffected.

---

# Falsification cases

Actively attempt to falsify H3 during implementation.

Ask:

### F1

Does the input actually need to know the target Experience in order to exist?

If yes, the claim of a neutral evidentiary input may be too strong.

### F2

Do both Experience evaluations always produce the same result?

If yes, the experiment provides no evidence for contextual significance.

### F3

Does evaluation require TES Pattern/Sequence/Progression semantics?

If yes, STOP rather than implementing them.

### F4

Does Activity need to contain hidden semantic state for the experiment to work?

If yes, H3 or the current projection boundary may be wrong.

### F5

Does the existing `SignificantEvent` abstraction already encode significance too early?

If yes, document whether it should be:

* retained;
* qualified;
* renamed later;
* replaced in a future experiment.

Do not perform broad renaming during Session 9.

---

# Coverage exclusion

Do NOT implement:

* Experience-portfolio observation overlap;
* Experience evidence sufficiency profile;
* generic coverage;
* set-cover calculations.

Session 9 may generate data relevant to future overlap analysis, but coverage remains experimental analytics.

---

# Stop conditions

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

# Implementation discipline

Prefer:

* one input;
* two Experience references;
* one evaluation seam;
* deterministic in-memory behaviour;
* focused tests.

Avoid adding abstractions for future possibilities.

Use the smallest number of shared-core modifications possible.

---

# Required final report

## A. Semantic basis

State exactly why the selected factual input and two Experience contexts are semantically defensible.

Distinguish:

* TES fact;
* Product Interpretation;
* experiment-specific simplification.

## B. Change inventory

List:

* files added;
* files modified;
* intentionally untouched areas.

## C. Evaluation flow

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

## D. Test evidence

Report:

* baseline;
* incremental tests;
* final full project check.

## E. H3 verdict

Classify:

* **SUPPORTED — READY FOR ADR**
* **SUPPORTED WITH QUALIFICATION**
* **PARTIALLY SUPPORTED**
* **FALSIFIED**
* **INCONCLUSIVE**

## F. SignificantEvent assessment

Explicitly assess whether the existing `SignificantEvent` name/contract remains semantically appropriate after the experiment.

Do not automatically change it.

## G. Architecture impact

State whether Architecture v0.4:

* survives;
* requires qualification;
* is contradicted.

## H. Technical debt

List every experimental shortcut.

## I. Reversibility

Explain exactly how to remove Session-9 changes.

## J. Next decision

Identify only the architectural decision that has become mature enough to consider.

Do not automatically recommend more implementation.

---

# Final adversarial questions

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

# Success criterion

Session 9 succeeds if:

> **One semantically defensible factual/evidentiary input can be evaluated independently and differently relative to two Experience contexts, without mutating the input, making Activity authoritative, implementing TES Progression or introducing a general Experience engine.**

Do not optimize beyond this criterion.
