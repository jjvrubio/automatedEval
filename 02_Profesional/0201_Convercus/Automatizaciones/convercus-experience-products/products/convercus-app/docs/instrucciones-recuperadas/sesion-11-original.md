# Convercus Demo Factory — Session 11: Contextual Evidence Relevance Experiment

## Purpose

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

# Core hypothesis

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

# Important conceptual distinction

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

# Governed Experience material

Use the actual Product Experience Definition candidates created in Session 10.

## Experience A

**Aventura Familiar / Family Adventure**

Its semantic candidate core concerns continuity of shared family/group participation in hotel activities during a stay.

Scenario-specific material may include:

* booking/stay;
* property;
* family/group context;
* locally available activity catalogue.

## Experience B

**Desafío Activo / Active Challenge**

Its semantic candidate core concerns repeated sport/wellness participation during a stay.

Scenario-specific material may include:

* booking/stay;
* property;
* participant;
* locally available sport/wellness activity catalogue.

Do not modify either Product Experience Definition primarily to make the experiment pass.

---

# Primary evidence discriminant

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

# Why Cooking Class is used

Cooking Class is intentionally selected as the primary discriminant because it provides a narrow test of contextual relevance:

* it is supported as an activity in Aventura Familiar;
* it is not part of the sport/wellness activity class represented by Desafío Activo.

The purpose is experimental isolation, not architectural richness.

Do not broaden this experiment into cooperative participation, partial completion or group evidence.

---

# Reserved future experiment — Treasure Hunt

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

# Factual input requirements

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

# ExperienceContext

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

# Evaluation boundary

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

# Evaluation outcome

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

# Tests required

At minimum prove:

## 1. Input independence

Cooking-class evidence exists without Experience or interpretation fields.

## 2. Family Adventure relevance

The evidence is relevant under the Family Adventure ExperienceContext.

## 3. Active Challenge non-relevance

The same evidence is not relevant under the Active Challenge ExperienceContext.

## 4. Criterion-based evaluation

Demonstrate that evaluation depends on ExperienceContext criteria rather than Experience ID.

Changing an ID while preserving criteria must not change the semantic result.

## 5. Scenario contribution

Identify whether the activity admissibility comes from:

* Product Experience Definition;
* Scenario;
* or their combination.

Test the actual implemented responsibility boundary.

## 6. Immutability

Neither evaluation mutates the original EvidenceInput.

## 7. Order independence

A → B and B → A produce the same individual results.

## 8. Repeatability

Same input + same ExperienceContext produces the same outcome.

## 9. Activity separation

Activity is not an evaluation input or source of truth.

## 10. Session-7 regression

Presenter action/checkpoint behaviour remains green.

## 11. Retail regression

Retail remains unaffected.

---

# Optional second discriminant

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

# H3 decomposition

Evaluate four sub-hypotheses separately.

## H3a — Input independence

A factual/evidentiary input can exist independently of Experience interpretation.

## H3b — Contextual relevance

Relevance can differ according to ExperienceContext.

## H3c — Evaluation independence

Evaluation does not mutate input and does not depend on evaluation order.

## H3d — Projection separation

Activity remains downstream from evidence and interpretation.

---

# SignificantEvent assessment

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

# EvidenceInput.interpretation assessment

Inspect the existing optional `EvidenceInput.interpretation`.

Determine whether Session 11 suggests that:

* it represents externally supplied/pre-resolved interpretation;
* it risks conflating factual input and contextual interpretation;
* it should remain provisional;
* a future separation may be required.

Do not redesign the contract broadly.

---

# Stop conditions

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

# Explicit non-goals

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

# Required final report

## A. Semantic basis

Explain why Cooking Class provides a defensible contextual discriminant.

## B. ExperienceContext responsibility

State explicitly what relevance information came from:

* Product Experience Definition;
* Scenario;
* their combination.

## C. Change inventory

List files added and modified.

## D. Actual evaluation flow

Show the implemented path.

## E. Test evidence

Baseline, incremental tests and final full check.

## F. H3 sub-hypothesis verdicts

For H3a–H3d use:

* SUPPORTED
* PARTIALLY SUPPORTED
* FALSIFIED
* INCONCLUSIVE

## G. Overall H3 verdict

Use:

* SUPPORTED — READY FOR ADR
* SUPPORTED WITH QUALIFICATION
* PARTIALLY SUPPORTED
* FALSIFIED
* INCONCLUSIVE

## H. SignificantEvent assessment

State what the experiment teaches about its semantic position.

## I. EvidenceInput.interpretation assessment

State whether conflation risk has increased or decreased.

## J. Architecture impact

State whether Architecture v0.4 survives or requires qualification.

## K. Technical debt

List experimental shortcuts.

## L. Reversibility

Explain exact rollback.

## M. Reserved Treasure Hunt experiment

Confirm that no Treasure Hunt behaviour was implemented.

Record the still-open future questions:

* cooperative participation;
* group vs individual subject;
* partial evidence;
* aggregation;
* partial solution;
* ordered/unordered clues;
* evidence sufficiency.

## N. Next mature decision

Identify only what has actually become mature.

---

# Final adversarial questions

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

# Success criterion

Session 11 succeeds if:

> The same neutral Cooking Class evidence is deterministically relevant to Family Adventure and not relevant to Active Challenge because of independently meaningful Product Experience Definition + Scenario criteria, without mutating the input, hard-coding Experience IDs, invoking TES Progression or making Activity authoritative.

Do not optimize beyond this criterion.
