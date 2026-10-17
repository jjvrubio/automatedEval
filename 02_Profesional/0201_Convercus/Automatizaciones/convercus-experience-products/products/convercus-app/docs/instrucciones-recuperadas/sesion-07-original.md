# Convercus Demo Factory — Session 7: Public Presenter Action and Deterministic Checkpoint Experiment

## Purpose

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

# Hypothesis under test

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

# Experiment scope

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

# Required behaviour

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

# Public action boundary

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

# Ownership rules

## Demo Script may own

* presenter-facing ordering;
* explanation;
* expected checkpoint;
* public action reference;
* optional preconditions for demonstration;
* recovery guidance where useful.

## Demo Script must not own

* hidden mutable state;
* Experience rules;
* progression logic;
* reward logic;
* direct fixture mutation;
* internal reducer/state implementation;
* provider internals.

---

## Scenario may own or reference

Only what the current experiment needs, such as:

* contextual actors;
* booking/stay context;
* current checkpoint or initial conditions;
* allowed public action relevant to this Scenario.

Do not expand Scenario into a generic workflow definition.

---

## Runtime owns

The actual mutable state controlled by the demo.

It must determine whether the public action can be applied and produce the resulting state.

The Script must not assign the resulting state directly.

---

# Experience boundary

Do not implement an Experience engine.

If the Hospitality Scenario currently references an Experience, preserve that reference.

The public action must not claim to produce TES Progression, Pattern, Result or Completion unless the current repository already has validated semantics and executable support for that claim.

A checkpoint transition in this experiment is a **demo/runtime transition**, not automatically a TES Experience transition.

This distinction must be explicit in code comments or experiment documentation if ambiguity could arise.

---

# Checkpoint semantics

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

# Presenter control

Expose the action through the smallest useful presenter-facing mechanism.

This may be:

* an existing demo control surface;
* a minimal test/debug control;
* another lightweight UI affordance.

Do not build a presenter console.

The experiment must demonstrate the boundary operationally, but presentation polish is not part of the objective.

If a visible control would cause disproportionate UI work, use the smallest rendered mechanism capable of demonstrating the action.

---

# Activity / projection interaction

If the action produces a visible Activity/read-model change, that is acceptable.

However:

* Activity remains a projection;
* the Script must not insert `ActivityItem` directly;
* runtime/domain input must not be represented primarily through icon/tone/copy fields;
* presentation fields should be derived where practical.

Do not broaden Session 7 into H3 architecture work.

---

# Determinism

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

# Tests required

Add only tests necessary to evaluate H2 operationally.

At minimum test:

## 1. Initial checkpoint

Hospitality starts at the expected deterministic state.

## 2. Public action

The action can be invoked through the public boundary.

## 3. Transition

The expected checkpoint/state transition occurs.

## 4. No direct Script mutation

Demonstrate structurally or through tests that the Demo Script invokes the public action rather than mutating runtime state directly.

## 5. Projection

The read model/UI reflects the resulting state.

## 6. Deterministic reset

Reset returns Hospitality to the original checkpoint.

## 7. Isolation

The action cannot mutate Retail state.

## 8. Invalid action/state

If the action is invoked from an invalid state, fail explicitly or return a controlled no-op/result according to the smallest coherent design.

Do not silently produce an impossible checkpoint.

---

# Regression requirements

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

# Experiment questions

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

# H2 verdict

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

# Stop conditions

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

# Explicit non-goals

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

# Change discipline

Prefer the smallest possible number of shared-core modifications.

Hospitality-specific artefacts should remain Hospitality-specific.

Shared changes must be justified by reuse or architectural boundary, not convenience.

Do not refactor unrelated Session-5 experimental code.

---

# Required final report

## A. Change inventory

List:

* files added;
* files modified;
* intentionally untouched areas.

## B. Implementation flow

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

## C. Test evidence

Provide:

* baseline before changes;
* incremental relevant tests;
* final full check.

## D. H2 verdict

Give evidence for the classification.

## E. Architecture impact

State whether Session 7:

* confirms Architecture v0.3;
* requires qualification;
* contradicts an accepted ADR.

## F. Technical debt

List all experimental shortcuts.

## G. Reversibility

Explain exactly how to remove the Session-7 experiment.

## H. Next architectural decision

State only what decision is now mature enough to consider.

Do not automatically recommend another feature implementation.

---

# Final falsification questions

Before concluding answer:

1. Could the same result have been achieved by removing Demo Script entirely?
2. If yes, what value does Demo Script add?
3. Did Scenario remain contextual or start absorbing executable workflow semantics?
4. Did the public action remain narrow or start becoming a generic command architecture?
5. Is the checkpoint a demo concept or accidentally becoming a TES Experience state?
6. Would a second Script for the same Scenario still fit the model without redesign?
7. What evidence would falsify the Scenario / Experience / Demo Script separation in a future experiment?

---

# Success criterion

Session 7 succeeds only if it demonstrates that:

> **A presenter-facing Demo Script can trigger one deterministic demo behaviour through a public Scenario/runtime boundary, producing a visible checkpoint/read-model transition without directly mutating hidden state, redefining Experience semantics or requiring a generic workflow architecture.**

Do not optimize beyond this criterion.
