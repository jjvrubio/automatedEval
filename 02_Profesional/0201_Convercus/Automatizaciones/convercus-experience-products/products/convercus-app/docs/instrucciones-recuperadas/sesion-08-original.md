# Convercus Demo Factory — Session 8: H2 Consolidation and ADR Promotion

## Purpose

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

# Part A — Verify Session-7 evidence

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

# Part B — Create ADR-004

Create one ADR using the existing governance conventions.

Suggested title:

**ADR-004 — Separation of Experience Definition, Scenario and Demo Script**

## Context

Demo Factory must distinguish:

### Experience Definition

A semantically governed definition of an Experience, traceable to TES.

### Scenario

The situated demo context that may provide:

* actors;
* roles;
* subject/context references;
* initial conditions;
* relevant Experience references;
* fixture/checkpoint context;
* permitted demo-level interaction boundaries where required.

### Demo Script

Presenter-facing demonstration orchestration that may provide:

* ordered demonstration steps;
* presenter copy/instructions;
* references to public actions;
* expected demo checkpoints/results;
* recovery guidance where useful.

---

# Decision

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

# Mandatory boundaries

The ADR must explicitly establish:

## Experience Definition must not own

* presenter instructions;
* prospect-specific narrative unless semantically intrinsic;
* UI state;
* demo checkpoints;
* presenter actions.

## Scenario must not

* redefine TES Experience semantics;
* become a generic workflow engine;
* implement TES Progression or Result;
* absorb presenter narration merely for convenience.

## Demo Script must not

* directly mutate hidden runtime state;
* implement Experience rules;
* implement reward/progression logic;
* bypass runtime validation;
* become a second application controller.

## Runtime must

* validate public actions;
* own mutable state transitions;
* expose resulting state through read models/projections.

---

# Checkpoint qualification

State explicitly that:

**Demo checkpoint != TES Experience Progression/Result/Completion**

unless future validated semantic and executable evidence explicitly establishes such a relationship.

Current Hospitality checkpoints are demo/runtime constructs only.

---

# Scope limitation

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

# Reconsideration triggers

The ADR must be reconsidered if future implementation shows that:

1. Scenario needs to encode substantial workflow/rule semantics;
2. Demo Script needs direct internal-state access;
3. multiple Scripts for one Scenario cannot coexist without redefining Scenario;
4. Experience-specific execution logic migrates into Script;
5. checkpoints begin to function as implicit Experience states;
6. the same useful behaviour can be represented more simply without the three-way separation.

---

# Part C — Promotion review of Session-7 elements

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

# Part D — Architecture v0.4

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

# Part E — Reassess H3 and H4 after Session 7

Do not promote H3 or H4.

Review whether Session 7 changed the evidence available for either.

## H3

Evidence / Occurrence / TES Event / Activity Projection.

Determine whether the new presenter action teaches anything useful about:

* factual occurrence;
* provenance;
* Event interpretation;
* Activity projection.

Do not infer more than the implementation demonstrates.

## H4

Provider resolution.

Determine whether the public action boundary adds evidence for provider architecture.

Do not infer multi-provider support merely because runtime exposes an action.

---

# Part F — Select the next empirical question

Compare the following candidates.

## Candidate A — H3 contextual multi-Experience evaluation

Construct the smallest in-memory experiment where one factual/evidentiary input is evaluated differently relative to two Experience references.

The purpose is to test:

* contextual significance;
* zero/one/multiple Experience evaluation;
* Activity as derived projection;
* separation between evidence and TES Event interpretation.

Do NOT build a general Experience engine.

## Candidate B — H4 multi-provider composition

Use two controlled local providers for separate capabilities.

Test whether provider-per-capability resolution adds genuine value.

## Candidate C — Third-demo marginal-cost test

Introduce a third materially different demo and measure Marginal Demo Code Cost.

## Candidate D — Second Scenario / Script reuse test

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

# Part G — Special attention to H3

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

# Required output

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
