Create one new product-interpretation document in:

`01-semantic-contract/product-interpretations/observed-occurrence-trace-event.md`

Do not modify TES source excerpts, the TES baseline, Ontology, Ledger, Lexicon, Protocol, TypeScript, tests, configuration or application code.

The document must record the product interpretation resulting from the TES review concerning Activity, observable occurrences, traces and TES Events.

Use the following governing status:

**Product interpretation subordinate to TES — not a TES extension.**

The document must make explicit that:

1. Demo Factory must **adapt the product layer** to a distinction already contained in TES; it is not correcting or extending TES.
2. TES establishes that not every observable fact is a significant Event.
3. For product purposes, Demo Factory may provisionally represent an observable fact as an `Observed Occurrence`, but this is a product/technical construct and not a new TES entity.
4. A `Trace` belongs to the instrumentation/reconstruction plane and provides evidence that an occurrence, condition or transition occurred. Trace and TES Event are not equivalent.
5. TES Event significance is contextual to an Experience and must not be treated as an unconditional intrinsic property of an observed occurrence.
6. A product architecture may need to support one observed occurrence being evaluated relative to zero, one or multiple Experiences. Mark this explicitly as a product interpretation strongly compatible with TES, not an explicit TES cardinality rule.
7. Preserve two different planes:

   Instrumentation / reconstruction:\
   `Observed Occurrence → Trace → contextual recognition / confirmation`

   TES experiential plane:\
   `Event → Pattern → Sequence → Progression → Result → Measurement → Learning`

   The first may feed the second but must not be inserted into the TES Experience Ledger as additional ontological stages.
8. `Pattern` must remain the TES concept for regularity emerging from relations between Events. A collection or trace of occurrences is not automatically a Pattern.
9. `Activity` must be treated as a read model / presentation projection rather than a sovereign semantic or factual source.
10. Do not equate occurrence accumulation, Pattern, Sequence, Progression, Completion, Result, Incentive or Reward.

Add a separate section titled:

`Analytical hypothesis — coverage`

This section must state that `coverage` is inspired by set-covering theory and is NOT a TES concept.

Record two distinct analytical questions:

A. **Observed-field coverage**

Given an observed occurrence universe `U` and subsets `S_E` associated with Experiences, unions/intersections/uncovered elements may be useful for analyzing Experience overlap, redundancy and portions of observable behaviour not related to any Experience.

B. **Experience evidence/requirement coverage**

The degree to which evidence or structural requirements of one Experience have been satisfied is a different problem and must not be conflated with observed-field set coverage.

Do not define either as TES Progression and do not assume percentage representation is valid.

Mark the usefulness of both coverage notions as **subject to adversarial falsification in Demo Factory Session 3**.

Finally include a reopening condition:

TES should only be reconsidered if a concrete case cannot be coherently represented using the existing distinction:

`observable occurrence / trace → contextual recognition as TES Event`

and therefore provides actual evidence of a semantic gap.

After creating the document, report only:

- the path created;
- the headings created;
- whether any other files were modified.

Do not make any other repository change.
