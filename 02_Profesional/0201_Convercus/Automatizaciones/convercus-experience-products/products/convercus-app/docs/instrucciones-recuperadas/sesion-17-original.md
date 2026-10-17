# Session 17 — Authority-Bounded Cross-Subject Evidence Composition Experiment

Continue the existing project:

`Convercus Demo Factory / Convercus Experience Products`

Repository:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

Do not start from scratch.

This session begins after the consolidation of Session 16.

The objective is to run the **first cooperative / multi-subject experiment** while preserving the existing epistemic method and without introducing a Group model.

---

# 1. Baseline

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

# 2. Existing semantic constraints

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

# 3. ADR-005 remains the governing invariant

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

# 4. Experimental frontier

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

# 5. Experimental question

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

# 6. H17

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

# 7. One new unresolved variable

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

# 8. Critical semantic separation

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

# 9. Authoritative premise vs evaluation

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

# 10. Do not encode cardinality assumptions

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

# 11. Shared context is not semantic authority

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

# 12. Minimum experimental cases

Implement the smallest reversible experiment that can test H17.

At minimum, include the following cases.

## Case A — Same-subject control

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

## Case B — Cross-subject with applicable authoritative premise

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

## Case C — Cross-subject without applicable authority

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

## Case D — Wrong scope

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

## Case E — Wrong subjects

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

## Case F — Shared context without semantic authority

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

# 13. Optional adversarial checks

Only add these if they remain trivial and do not expand the variable under investigation.

Potential checks:

### Premise exists but does not cover this evaluation context

```text
authority exists
scope appears superficially related
but applicability is not established
```

Expected:

```text
undetermined / cannot establish
```

### Extra Evidence does not strengthen authority

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

# 14. Do not use Group

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

# 15. Do not resolve participant vs contributor

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

# 16. External actors are explicitly out of scope

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

# 17. Sufficiency criterion remains unchanged

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

# 18. Outcome representation remains experimental

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

# 19. No semantic-product-contract redesign yet

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

# 20. Architectural guardrails

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

# 21. Repository work

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

# 22. Falsification criteria

H17 is not automatically considered supported because the positive case works.

The experiment should be considered challenged or falsified if evidence shows, for example:

### F1

Cross-subject Evidence can legitimately enter the same evaluation with no authoritative premise or equivalent basis whatsoever.

If this occurs, determine whether hidden authority is already embedded elsewhere before concluding H17 is false.

### F2

Shared contextual facts alone necessarily produce joint admissibility.

Again inspect for hidden rules or authority laundering before interpreting this as evidence.

### F3

Joint admissibility cannot be represented or evaluated without introducing a persistent collective identity.

If genuinely unavoidable:

```text
STOP
```

and document the reason.

Do not manufacture Group semantics.

### F4

The sufficiency evaluator necessarily determines admissibility itself and cannot be separated without contradicting existing accepted architecture.

Document the contradiction.

Do not force an artificial separation solely to satisfy H17.

### F5

Cross-subject Evidence requires a fundamentally new architectural responsibility not covered by ADR-005.

If supported by concrete evidence, document it as a candidate architectural finding.

Do not automatically create ADR-006.

---

# 23. Expected epistemic verdict

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

# 24. Required report

Create:

`docs/experiments/session-17-authority-bounded-cross-subject-evidence-composition.md`

or use the repository's established Session documentation location if different.

The report must contain at least:

## A. Repository inspection

What existing code, tests and documents were reused.

## B. Hypothesis

Exact H17 tested.

## C. Constants

What was held constant from Session 15.

## D. New variable

```text
authority-bounded cross-subject evidence composition
```

and operational observation:

```text
joint admissibility
```

## E. Minimal implementation

Explain what was added and, importantly, what was deliberately not added.

## F. Test matrix

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

## G. Adversarial findings

Report any hidden coupling between:

* authority and K;
* subject attribution and participation;
* situated context and semantic authority;
* fixtures and architecture.

## H. Falsification analysis

State explicitly whether any falsification criterion occurred.

## I. Semantic findings

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

## J. Product Semantic Contract pressure

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

## K. Architecture impact

Evaluate:

```text
ADR-005
Architecture v0.5
need for new ADR
need for architecture revision
```

Do not presume modification.

## L. Unresolved items

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

## M. Final verdict

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

# 25. Important interpretation rules

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

# 26. STOP / NO-GO conditions

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

# 27. Desired experimental character

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
