# Convercus Demo Factory — Session 12: Authority Frontiers and Open-World Evaluation Semantics

## Purpose

Session 11 successfully demonstrated a narrow product-level proposition:

> contextual relevance can be derived from neutral factual evidence + Product Experience Definition + Scenario without storing relevance inside the factual input, making Activity authoritative, or recognizing a TES Event.

Before promoting this into ADR-005 or moving to the reserved Treasure Hunt experiment, Session 12 must examine three architectural tensions revealed by the accumulated evidence:

1. **authority frontiers** — which artefact or layer has authority to make which claims;
2. **open-world relevance semantics** — `not relevant` must not silently mean `unknown`, `insufficient` or `not evaluable`;
3. **ExperienceDefinition authority ambiguity** — multiple artefacts currently use the name `ExperienceDefinition` despite representing different semantic maturity and runtime responsibilities.

Do NOT modify application code.

Do NOT create ADR-005 before completing the analysis.

Do NOT rename contracts.

Do NOT modify TES.

The cognitive progression is:

**ANALYZE → EVALUATE → CONSOLIDATE → CREATE**

---

# Part A — Verify the current ADR foundation

Inspect ADR-001 through ADR-004 and Session-11 implementation/evidence.

Do not assume the ADRs need modification.

Determine:

* what each ADR already says about authority;
* where authority is explicit;
* where it is only implied;
* whether Session 11 contradicts any accepted decision;
* whether new findings fit as subordinate architectural decisions.

Pay special attention to:

* ADR-001 semantic authority;
* ADR-002 factual/runtime/read-model authority;
* ADR-003 desired/effective composition authority;
* ADR-004 Experience/Scenario/Script/runtime authority.

Report any genuine contradiction separately from an unresolved boundary.

---

# Part B — Define the concept of Authority Frontier

Use **Authority Frontier** as a product/architecture analytical term, not a TES concept.

Working definition to test:

> An Authority Frontier identifies the scope within which an artefact, component or source is entitled to make a claim, and the point beyond which a new interpretation, validation or authority is required.

Determine whether this concept genuinely adds explanatory power beyond ordinary layering.

Test it against existing examples:

```text
TES
→ semantic meaning/invariants

Product Experience Definition
→ governed product interpretation

Scenario
→ situated context

Source/provider
→ factual observation within its contract

Contextual evaluator
→ relational evaluation outcome

Runtime
→ operational mutable state

Read model / Activity
→ presentation
```

Do not assume these boundaries are final.

---

# Part C — Build an Authority Frontier Matrix

Create a matrix with at minimum these columns:

| Artefact / layer | Authoritative claims | Inputs it may trust | Claims it may derive | Claims it must NOT make | Required provenance / version | Open questions |

Include at minimum:

* TES corpus;
* Product Interpretation;
* commercial/product source material;
* candidate Product Experience Definition;
* validated Product Experience Definition if conceptually distinct;
* runtime Experience descriptor/reference;
* Scenario;
* activity/product catalogue or classification source;
* provider/source;
* neutral EvidenceInput;
* contextual relevance evaluator;
* `SignificantEvent`;
* runtime state;
* Demo Script;
* Demo Manifest;
* bootstrap/resolution;
* AppSnapshot;
* Activity/read model.

If an artefact does not yet exist concretely, mark it **conceptual/provisional**.

---

# Part D — Classification authority from Session 11

Session 11 currently uses:

```text
Scenario:
Cooking Class → shared-hotel-activity
```

while the Experience context declares which activity classifications are relevant.

This worked experimentally but does not establish Scenario as the final taxonomy authority.

Analyse alternative authority locations, without implementing them:

* Scenario;
* Product Experience Definition;
* reusable activity/product catalogue;
* provider/source;
* property configuration;
* shared taxonomy;
* externally supplied classification;
* composed authority across more than one source.

For each, evaluate:

* semantic appropriateness;
* reuse;
* versioning;
* local variation;
* risk of Scenario becoming semantic authority;
* risk of provider data becoming product meaning;
* compatibility with ADR-004.

Do NOT choose a final taxonomy architecture unless evidence supports it.

The key question is:

> Who has authority to assert that an observed activity belongs to a classification that an Experience can evaluate?

---

# Part E — Open-world relevance semantics

Session 11 used a deliberately minimal binary:

```text
relevant
not_relevant
```

Do NOT promote that binary into architecture.

Analyse the distinction between at least these conceptual situations:

### Positive determination

Enough authoritative information exists to conclude that the evidence is relevant.

### Negative determination

Enough authoritative information exists to conclude that it is not relevant.

### Undetermined

The available evidence/context/authority is insufficient to make either conclusion.

Also analyse whether other conditions may need future distinction, such as:

* unknown classification;
* missing context;
* unsupported evaluator;
* contradictory evidence;
* unreliable source;
* not evaluable under current version.

Do NOT define a final enum.

Do NOT create a universal state machine.

The architectural question is:

> What minimum semantic invariant prevents absence of knowledge from collapsing into a negative claim?

---

# Part F — Relation between authority and evaluation outcome

Test the proposition:

```text
EvaluationOutcome =
f(
  Evidence,
  ExperienceContext,
  AvailableAuthority
)
```

rather than merely:

```text
EvaluationOutcome =
f(Evidence, ExperienceContext)
```

Analyse concrete examples.

## Example 1 — Known negative

Cooking Class is authoritatively classified as non-sport/wellness in the relevant Scenario/catalogue context.

Can `not relevant` be justified?

## Example 2 — Unknown activity

The input identifies an activity not present in the local catalogue.

Is that:

* not relevant;
* unknown;
* unevaluable?

What authority is missing?

## Example 3 — Missing property/stay context

The evidence exists but cannot be situated against the Scenario.

What may the evaluator claim?

## Example 4 — Conflicting classifications

Two sources classify the same activity differently.

Which layer has authority to resolve that conflict, if any?

Do not solve conflicts by arbitrary precedence.

---

# Part G — `ExperienceDefinition` authority ambiguity

There is now a deliberate tension to analyse.

ADR-001 states that an `ExperienceDefinition` must identify the TES baseline against which it was validated.

However, the repository currently contains or references conceptually different artefacts using the same or similar `ExperienceDefinition` name.

Inspect at minimum:

## 1. Product Experience Definition candidates from Session 10

Examples:

* Aventura Familiar;
* Desafío Activo;
* Circuito Sostenible.

They are explicitly:

**READY WITH EXPLICIT GAPS — non-executable candidate**

and therefore must not be mistaken for fully validated TES-governed definitions.

## 2. `prototype/src/domain/contracts.ts::ExperienceDefinition`

This is a richer functional candidate but does not yet demonstrate full TES semantic completeness or runtime authority.

## 3. `prototype/src/demo-factory/contracts.ts::ExperienceDefinition`

This contains only identity/baseline-level information and acts operationally as a runtime descriptor/reference.

---

# Part H — Distinguish authority, maturity and representation

For each Experience-related artefact, determine separately:

### Semantic authority

What meaning is it entitled to assert?

### Validation maturity

Candidate / validated / experimental / legacy / runtime-only / other.

### Representation role

Definition / reference / descriptor / projection / configuration.

### Executability

Non-executable / runtime reference / executable contract / unresolved.

### TES relationship

Which baseline is referenced, and does the reference mean:

* interpreted against;
* validated against;
* merely associated with?

Do not assume those are equivalent.

---

# Part I — Test the naming problem

Evaluate whether the current shared use of `ExperienceDefinition` creates a material risk of false authority.

Specifically test the misleading inference:

```text
object named ExperienceDefinition
+
tesBaseline
=
TES-validated semantic definition
```

which must NOT be assumed.

Determine whether a future conceptual distinction may be necessary, potentially along lines such as:

```text
CandidateProductExperienceDefinition
ValidatedProductExperienceDefinition
RuntimeExperienceReference
RuntimeExperienceDescriptor
```

These are examples only.

Do NOT rename files, types or contracts.

Recommend terminology only if it materially reduces authority ambiguity.

---

# Part J — ADR-001 compatibility review

Determine whether ADR-001 requires:

* no change;
* clarification;
* future amendment;
* reconsideration.

Pay special attention to the phrase requiring every `ExperienceDefinition` to identify the TES baseline against which it was validated.

Ask:

1. Should the obligation apply only to semantically validated definitions?
2. Can a candidate definition reference a baseline without claiming validation?
3. Should runtime references carry `tesBaseline` indirectly through the definition they reference?
4. Does the current wording risk treating candidate or descriptor artefacts as validated?
5. Can this be resolved by terminology/governance rather than reopening ADR-001?

Prefer no ADR modification unless a genuine contradiction exists.

---

# Part K — Authority provenance

Analyse whether future derived claims should carry information about:

* source authority;
* source version;
* Experience Definition version/status;
* Scenario version;
* evaluator version;
* classification authority;
* reason/rationale.

Do NOT design a full provenance schema.

Determine only which dimensions appear necessary to prevent a derived claim from appearing more authoritative than its inputs.

---

# Part L — Proposed narrow ADR-005 scope

Only after completing the authority and open-world analysis, draft the intended scope of a future ADR.

Do NOT create it yet unless the evidence is unequivocally sufficient.

Candidate scope:

**Neutral Evidence and Authority-Bounded Contextual Evaluation**

Potential invariant:

> Factual evidence remains distinct from Experience-relative evaluation. Any derived relevance claim must be scoped to an Experience context and to the authority available for that evaluation. Absence of sufficient authority or context must not silently collapse into a negative relevance claim. A relevance outcome does not by itself recognize a TES Event and does not belong to Activity.

Evaluate whether this is now mature.

List explicitly what such an ADR must NOT decide:

* final relevance enum;
* classification taxonomy;
* classification-authority implementation;
* Event recognition;
* SignificantEvent migration;
* persistence;
* generic rule engine;
* participation;
* Pattern/Sequence/Progression;
* provider/API topology.

---

# Part M — Architecture v0.5 candidate

Do not automatically publish Architecture v0.5.

First determine whether the new concept changes accepted architecture or only adds an analytical annotation.

If useful, propose a candidate shape:

```text
Source / Evidence Authority
        ↓
Neutral factual evidence
        ↓
Experience Definition + Scenario + classification authority
        ↓
Authority-bounded contextual evaluation
        ↓
[future unresolved recognition boundary]
        ↓
Runtime / projections as applicable
```

Mark all non-accepted boundaries clearly.

---

# Part N — Reserved Treasure Hunt experiment

Treasure Hunt remains explicitly reserved.

Do NOT implement it.

Use Session-12 analysis to refine what that future experiment should attack.

At minimum preserve:

* multiple participants;
* individual and group subject;
* partial evidence;
* evidence aggregation;
* cooperative contribution;
* partial resolution;
* ordered/unordered clues;
* contradictory or missing evidence;
* evidence sufficiency;
* reconstruction of a group-level outcome.

Now add two explicit stress dimensions:

## Authority

Who may assert:

* clue observed;
* clue solved;
* contribution belongs to participant;
* contributions belong to one group;
* partial solution is valid;
* whole hunt is resolved?

## Open-world semantics

Distinguish:

```text
false / negative
```

from:

```text
unknown / unresolved / insufficient
```

without defining final terminology yet.

The future Treasure Hunt experiment should be designed specifically to falsify the current assumptions of:

* atomic evidence;
* individual subject;
* binary relevance;
* single authoritative classification.

---

# Part O — Decide the next step

At the end recommend exactly one:

### Option A

Create ADR-005 in a subsequent documentation-only session.

### Option B

Perform one more focused experiment before ADR-005 because authority/open-world behaviour remains under-evidenced.

### Option C

Reopen an existing ADR because a genuine contradiction has appeared.

### Option D

Proceed to Treasure Hunt design because authority boundaries are sufficiently understood.

Explain why.

---

# Required output

1. Session-12 executive conclusion
2. ADR-001–004 compatibility review
3. Authority Frontier concept assessment
4. Authority Frontier Matrix
5. Classification-authority analysis
6. Open-world relevance analysis
7. Authority × evaluation-outcome analysis
8. `ExperienceDefinition` ambiguity analysis
9. Experience artefact maturity/authority matrix
10. ADR-001 wording compatibility assessment
11. Authority provenance requirements
12. ADR-005 readiness and proposed scope
13. Candidate Architecture v0.5 implications
14. Treasure Hunt authority/open-world preparation
15. Remaining risks
16. Recommended next step

---

# File creation

Create only:

* one Session-12 analysis/consolidation report.

Do not create ADR-005 yet.

Do not modify ADR-001–004.

Do not modify application code.

Do not rename `ExperienceDefinition`.

---

# Final adversarial questions

1. Does Authority Frontier add explanatory power beyond ordinary architecture layers?
2. Which current artefact is most likely to overstate its authority?
3. Who currently has de facto classification authority in Session 11?
4. Is that authority legitimate or merely experimental convenience?
5. Under what conditions can `not relevant` be asserted confidently?
6. What situations currently collapse incorrectly into the same binary result?
7. Can an evaluator make a negative claim when classification authority is missing?
8. Does `tesBaseline` mean the same thing for candidate, validated and runtime artefacts?
9. Does the name `ExperienceDefinition` currently transfer false semantic authority?
10. Can the ambiguity be solved without modifying ADR-001?
11. What minimum provenance prevents derived claims from exceeding their sources?
12. Is ADR-005 now mature?
13. What would Treasure Hunt falsify that Cooking Class could not?
14. Have we accidentally designed an ontology of relevance instead of identifying an architectural invariant?

---

# Success criterion

Session 12 succeeds if it can establish:

> which system actors are authoritative for which claims, why contextual evaluation cannot safely be assumed binary in an open-world setting, and whether the current `ExperienceDefinition` naming/maturity model risks transferring semantic authority that its artefacts do not possess.

The session must improve governance without inventing a final taxonomy, relevance ontology or Experience runtime.
