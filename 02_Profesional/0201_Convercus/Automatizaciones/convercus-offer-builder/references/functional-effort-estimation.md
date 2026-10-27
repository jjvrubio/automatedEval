# Functional and Technical Effort Estimation

Use this reference for an internal, pre-contractual estimate when the agreed scope includes implementation, functional configuration, migration, custom work, or integrations. The estimate supports later Pricing Calculator inputs; it is not a quote, delivery commitment, or commercial approval.

## Evidence and integration analysis

Start from the agreed scope matrix and the opportunity source inventory. For each integration, identify both ends and examine the available interface evidence for each. Prefer versioned, customer-specific documentation and examples. Public vendor documentation can inform an analysis, but does not prove that the documented operation, version, permissions, or configuration is available in the customer's installation.

Record:

- Product/system, installation, version, owner, and relevant environment on each end.
- Relevant operations, API/interface version, contracts and schemas, authentication and permissions.
- Entities, identifiers, mappings, direction and frequency of synchronization.
- Limits, compatibility, errors, duplicate handling, retries, reconciliation, and third-party constraints.
- Source and date for each verified fact; label assumptions, inferences, and pending confirmation separately.

Do not claim undocumented capabilities. If a necessary interface document, version, access, or behavior is unavailable, state what is missing and bound only the work that can still be reasonably estimated.

## Work breakdown and estimates

Use an engineering-based, bottom-up method for each technically plausible solution candidate:

1. Examine the relevant interfaces, versions, operations, contracts, data, and constraints at both ends.
2. Describe a technically plausible architecture and its boundaries, owners, and dependencies.
3. Decompose the included scope into implementable units with verifiable results.
4. Identify the actual technical and delivery operations needed for each unit.
5. Estimate the operations from the work evidenced in this case, then aggregate them into activities without counting any operation twice.

Derive the units and operations from the case; do not impose a standard WBS or universal activity catalog. Do not use a table of hours per endpoint, an uncalibrated coefficient, a qualitative label, price, or historical customer figure to produce hours. For materially different architectures, make separate estimates rather than combining their work into one range.

For each estimate, explain why its magnitude is reasonable in light of the case-specific operations, interfaces, data flows and transformations, identifier rules, API availability and maturity, adapters or custom work, authentication, error/duplicate/reconciliation handling, environments, test scenarios, validation, and team dependencies as applicable. Explain which technical assumption drives each material part of the estimate and which operations and hours must be reconsidered if that assumption changes. A task list without this quantitative rationale is insufficient.

### Activity estimate and PERT

Use activity-level PERT when the activity and its technical scenario are sufficiently defined for meaningful bounds. State productive effort in hours for:

- **O — Optimistic:** the low but technically plausible effort if the documented path works as expected and stated dependencies are met.
- **M — Most likely:** the effort expected under the adopted technical assumptions and ordinary execution conditions.
- **P — Pessimistic:** the high but still plausible effort within the same architecture, accounting for identified technical friction or bounded rework. It is not a generic contingency or an alternative architecture.

Explain the case-specific technical conditions behind each value; do not select O, M, or P by applying standard percentages or multipliers. Calculate the weighted activity effort as `E = (O + 4M + P) / 6`. Show the inputs and calculated E, and round only the displayed result after calculation. E is a reasoned estimate, not a confidence interval, delivery promise, or empirically validated outcome. Sum E only within the same architecture, scope, and responsible party.

If PERT is not meaningful for a sufficiently bounded activity, use a reasoned point estimate or range and explain why. If the work cannot be bounded without decisive unsupported assumptions, leave it conditional and non-dimensionable; do not manufacture PERT values. When an assumption changes, revisit the affected operations and their O/M/P/E, not unrelated activities. Never use PERT to conceal uncertainty about which architecture will be selected.

For every activity, record:

| Field | Required content |
|---|---|
| Activity and expected result | A bounded work item and its deliverable or acceptance result |
| System and responsibility | Systems touched and owner: Convercus, client, or named third party |
| Engineering units and operations | Implementable units, their observable results, and the actual operations included; identify shared operations once |
| Evidence | Source/version and case facts supporting the architecture, operations, and complexity |
| Estimated effort | O/M/P and calculated E in hours when PERT is pertinent, or a justified point/range; otherwise explicitly “conditional — not dimensionable” with the missing evidence |
| Quantitative rationale | Why the operations and technical factors make the proposed O/M/P or point/range reasonable; assumptions whose change would affect the estimate |
| Included tasks | Relevant analysis, design, coordination, documentation, implementation, testing, UAT support, and reasonable adjustments |
| Effort, ownership, and timing | Convercus productive effort; client/integrator effort separately; external waiting time/calendar duration separately; conditional rework separately |
| Assumptions and conditional risks | Hypothesis, evidence and pending fact, trigger/condition, affected operations and activities, and project-start check |
| Scope status | Included, conditional, optional, or excluded |

Estimate productive effort from the described operations, not from a fee, rate, elapsed calendar time, or external waiting period. Keep Convercus effort separate from client and integrator effort. Record those parties' effort separately only when it can be reasoned about; do not include it in Convercus totals. Record calendar duration and dependencies/waiting time separately. Client response delays or missing documentation are not implementation hours. If a delay creates actual additional work, identify the specific conditional rework operation, its trigger, owner, and affected estimate; do not add it automatically as reserve.

Include cross-functional work in the activity it supports or in one explicit shared activity, not both. Before totaling, reconcile each analysis, coordination, documentation, test, UAT, adjustment, and management task against all fixed, hourly, client, and third-party work lines. Assign a single owner and one effort entry to each task; distinguish effort by party rather than counting another party's hours as Convercus delivery effort.

### Expert review and estimate history

An experienced developer with relevant, comparable technical experience may review an estimate. Expert review is non-blocking: absence of a reviewer does not prevent a sufficiently grounded estimate from being used in offer preparation. A review can increase confidence in the reasoning, but it does not validate accuracy against actual delivery effort. Prior work may inform identified reuse only when its technical and scope comparability is demonstrated; record the reusable component or operation and its differences from this case rather than importing another project's hours or prices.

Preserve the initial estimate as a baseline. Record the review as a separate, traceable revision with:

- Initial activity breakdown and initial O/M/P/E or point/range.
- Revised activity breakdown and revised values, retaining the original values.
- Activities or operations added, removed, split, merged, or otherwise corrected.
- Technical rationale for every material correction and any reuse identified, with its relevance to this scope.
- Conditional risks affected by the review.
- Reviewer identity or role when available, review date when available, and status (for example, not reviewed, reviewed, or review pending).

Recalculate E whenever reviewed O/M/P values change. Do not overwrite the baseline or describe review alone as empirical validation. Where real delivery results later become available, record them separately against the corresponding activity and scope, alongside material scope or assumption changes. Do not build a parametric database, infer universal coefficients, or promote Brownie, Compactor, or other customer estimates into default parameters.

## Estimation under uncertainty

Uncertainty is inherent in pre-contractual estimation and is not, by itself, a reason to block the estimate or commercial preparation. Proceed with the best available evidence and classify each affected activity:

- **Sufficiently grounded estimate:** Evidence supports a technically plausible solution and a reasonable effort range or figure, although some uncertainty remains. Estimate the hours and record material conditional risks.
- **Plausible alternatives:** More than one technically viable solution exists and the effort may differ. Present separate conditional scenarios or alternatives when each can be reasonably bounded, explaining the assumptions and activities that distinguish them.
- **Essential activity not dimensionable:** Missing information prevents identifying a technically plausible solution or reasonably bounding essential work. Keep that activity conditional without a closed hours figure; state exactly what evidence is missing and which check will make it estimable.

Do not let an unbounded activity block estimates for independent work that is sufficiently known. Do not invent certainty or force a closed total across unestimated conditional activities. Keep estimates for different plausible architectures in separate scenarios, including their assumptions, activity breakdowns, and totals; do not average or merge them into one PERT range. For each material conditional risk, record the adopted hypothesis, evidence and pending fact, condition that would make it materialize, affected operations and activities, and project-start check. Do not add generic contingency hours, percentages, or automatic commercial surcharges. Checking a hypothesis during project start does not automatically change the price; any scope or commercial consequence requires separate review and approval.

## Pricing Calculator handoff

Keep the internal estimate distinct from calculator prices. Reconcile activities into the applicable categories without changing calculator formulas or rates:

- Fixed standard module enablement.
- Specific professional services estimated in hours.
- Shared/transversal services, counted once.
- Third-party work or charges, separated by provider and responsibility.
- Optional and conditional work, shown separately from the included base.

For Iberia, use the user-provided commercial references only for pricing classification: €1,200 fixed enablement per module; €100/hour for variable services; 8 hours per day (€800). These amounts do not determine or validate the effort. Inspect the actual calculator line descriptions and current included scope before deciding a task is covered by a fixed fee. If coverage is unclear or a current approved opportunity input conflicts with these references, flag it for confirmation; do not infer coverage or edit the calculator.

The handoff should map each estimate activity to a calculator category and identify its scope status, owner, effort hours, any applicable validated price input, source, and any overlap/coverage check. Do not expose internal hours, costs, or estimate rationale in client-facing material by default.

## Required internal output

Deliver an internal estimate with:

1. Case summary and scope estimated.
2. Sources and API/interface documents examined, including version and evidence status.
3. Integration architecture and viable alternatives, distinguishing verified facts from hypotheses.
4. Interface correspondence matrix (system/end, operation/data, direction/sync, auth, constraints, owner, evidence/pending checks).
5. Activity breakdown by architecture/scenario, with implementable units and operations, expected results, responsibilities, evidence, O/M/P/E (or justified point/range), quantitative rationale, included tasks, estimate assumptions, and status. Separate Convercus effort, client/integrator effort, calendar duration/waiting, and conditional rework. Preserve initial values, expert review revisions and rationale, and actual results when available; identify review and validation status.
6. Conditional risks in the form: hypothesis; evidence and pending fact; materialization condition; affected activities; start-up check.
7. Exclusions and optional/conditional components.
8. Checks planned for project start.
9. Mapping to Pricing Calculator categories and any fixed-line coverage review.
10. QA reconciliation confirming scope coverage, owner separation, and no duplicate effort or price coverage.

Keep this internal working output separate from the commercial proposal. A customer-facing summary may state only scope and planning information appropriate to the approved proposal; it must not inherit the internal breakdown automatically.

## QA before handoff

- Every included scope item maps to one or more bounded activities or is explicitly identified as unestimated/conditional.
- Every estimate has evidence and a task-based explanation; unknowns are not stated as facts.
- Hours are derived bottom-up from case-specific implementable units and operations; PERT values have technical rationales, and E is calculated correctly where PERT is pertinent.
- Material architecture alternatives have separate estimates; changes in assumptions trigger reassessment of affected operations and values only.
- Expert review, if present, preserves the original estimate and records corrections, rationale, reuse, reviewer/status, and affected risks; review is not presented as empirical validation.
- Convercus, client/integrator effort, calendar waiting, and conditional rework are separate; waiting is not counted as productive hours.
- Both interfaces are examined for integrations where evidence is available; installation-specific availability remains unverified until confirmed.
- Responsibilities distinguish Convercus, client, and third parties.
- Hours are not derived from price, and previous-account figures are not used as default benchmarks.
- Shared work and fixed-price coverage are checked for overlap; each task is counted once.
- Fixed enablement, hourly services, third-party work, and optional/conditional work are separated in the calculator mapping.
- Conditional risks identify their start-up check and affected activities; no automatic reserve or price change is added.
- Internal effort detail is not copied into client-facing content without explicit approval.
