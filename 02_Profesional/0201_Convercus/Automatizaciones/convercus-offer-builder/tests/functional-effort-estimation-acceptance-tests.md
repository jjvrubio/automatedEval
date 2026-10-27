# Functional Effort Estimation — Manual Acceptance Tests

These are synthetic behavior tests for the skill instructions, not real project estimates, technical validations, or benchmark data. Run them in a fresh session with `$convercus-offer-builder`; provide only the stated synthetic fixture. Review the generated internal estimate against the expected checks. Do not use customer documents, external services, or persistent outputs.

For every case, the response must keep effort separate from price and calendar duration, identify estimates as pre-contractual, and avoid treating this fixture as a reusable benchmark.

## Synthetic fixture: Case A

Account: `Example Retail` (fictional). Scope matrix: one included loyalty transaction exchange between Shop API and Loyalty API. The integration sends purchases from Shop to Loyalty and writes the resulting member status from Loyalty back to Shop for members present in the synchronized transaction batch. No migration, custom middleware, or third-party service is in scope.

Shop API documentation (fictional, v3.2, supplied for this test):
- `GET /transactions?updatedSince={timestamp}&cursor={cursor}` reads transactions incrementally. The first request may omit `cursor`; each response contains a page of transactions and `nextCursor` (null when the batch is complete). A later poll uses the last completed synchronization timestamp as `updatedSince`; cursor pagination is used to finish each batch. The response schema is `externalTransactionId`, `memberId`, amount, currency, and timestamp.
- `PATCH /members/{memberId}/status` accepts `{"statusCode":"..."}` and updates that member's status in Shop.
- `POST /transactions` creates a transaction in Shop and is documented, but is not used by this integration's scope.
- OAuth 2.0 client credentials apply to all operations. The published limit is 60 requests/minute across the API; errors include 400, 401, 409, and 429. Webhooks are not supported.

Loyalty API documentation (fictional, v2.4, supplied for this test):
- `POST /purchases` accepts `sourceTransactionId`, `customerRef`, amount, currency, and occurredAt.
- `GET /members/{customerRef}` returns `customerRef` and `statusCode`.
- OAuth 2.0 client credentials apply to both operations; the limit is 120 requests/minute across the API. A duplicate `sourceTransactionId` on `POST /purchases` returns 409.

The schemas and a sample payload are included. For this fixture, Shop `memberId` and Loyalty `customerRef` identify the same member; the client must still confirm the mapping from Loyalty `statusCode` values to the codes accepted by Shop before end-to-end acceptance. The client confirms that its Shop installation is v3.2, but has not supplied credentials. The Convercus team implements and executes the integration. A Convercus-managed integration test runtime is available; client UAT approval remains with the client. No production deployment is included.

## Synthetic fixture: Cases B–F

- `B — Incomplete docs`: Same scope, but only a public Shop API overview is supplied. No version, operation schemas, auth details, or customer-specific installation confirmation; Loyalty API details and client test access are also pending. A fictional client architecture note says both product teams consider either REST transaction exchange or scheduled CSV exchange technically plausible for this account, but gives no implementation details or confirmation for the installed versions.
- `C — Shared responsibilities`: This case overrides Case A's execution ownership. Convercus owns the Loyalty API and configuration. The client owns Shop credentials, data-owner mapping decisions, and UAT sign-off. A client-selected integrator owns Shop-side implementation. No party has agreed that Convercus will implement or support that third party's code.
- `D — Overlap`: A calculator excerpt marks one module's standard enablement fixed fee as included but does not describe whether it includes integration design, implementation, project coordination, tests, UAT, or documentation. Separate proposed hourly lines currently name “integration design” and “integration validation/documentation”; the activity breakdown also contains those tasks.
- `E — Fixed vs effort`: Use the user-provided Iberia references: €1,200/module fixed enablement, €100/hour for variable services, and 8 hours/day (€800). No activity hour estimate is supplied in this fixture.
- `F — Start-up validation`: The customer-specific installed Shop API version and rate-limit configuration cannot be verified until sandbox credentials are issued at kick-off. A different version or stricter limit could affect the Shop API mapping and integration test activities.

## Synthetic fixtures: Cases G–N

These fixtures add no expected hour values or reusable effort benchmarks. In each case, assess the generated estimate against its stated technical evidence and require the method to derive its own effort.

- `G — Engineering breakdown`: Use Case A. Both interfaces, operations, schemas, authentication, identifiers, limits, and error responses are documented as stated there.
- `H — PERT`: Use Case A, with the same documented architecture and scope. No O/M/P values are provided.
- `I — Changed assumption`: Use Case A has an initial estimate. A later scope decision adds this supported return-transaction flow: Shop `GET /returns?updatedSince={timestamp}&cursor={cursor}` uses the same cursor pagination, OAuth, and 60 requests/minute limit as Shop transactions. Its response contains `externalReturnId`, `externalTransactionId`, `memberId`, amount, currency, and timestamp. Loyalty `POST /returns` accepts `sourceReturnId`, `sourceTransactionId`, `customerRef`, amount, currency, and occurredAt; a duplicate `sourceReturnId` returns 409. It uses the existing Loyalty OAuth credentials and 120 requests/minute API limit. A return must reference its original transaction; orphan returns and other return exceptions are out of scope. The APIs' common error responses remain as documented in Case A. No hours are provided.
- `J — Expert review`: Use Case A has an initial estimate. A senior integration developer reviews it and identifies the fictional `REST Cursor Adapter v1` as reusable. The review note documents that it provides OAuth 2.0 client-credentials token acquisition/refresh, configurable REST requests, cursor pagination with `updatedSince`, configurable request pacing, HTTP error propagation/logging, and POST idempotency-key handling. It does not provide Example Retail field mappings, purchase/member-status business orchestration, Shop/Loyalty endpoint-specific configuration, reconciliation rules, UAT, deployment, or project documentation. Reuse requires a compatible runtime, the same OAuth grant, cursor-based reads, configurable rate limits, and an endpoint that accepts an idempotency key. The adapter was verified against a separate fictional API with a cursor GET and idempotent POST; this fixture provides no transferable hour values. The reviewer identifies the differences to assess: Shop's 60 requests/minute limit versus Loyalty's 120; Shop transaction and status schemas versus Loyalty purchase/member schemas; `externalTransactionId`/`memberId` versus `sourceTransactionId`/`customerRef`; and the need to orchestrate `GET /members/{customerRef}` followed by `PATCH /members/{memberId}/status`. The reviewer confirms the runtime and OAuth grant are compatible but does not claim endpoint or mapping work is reusable. No revised hours are provided.
- `K — External dependency`: Use Case A includes client-supplied credentials and mapping decisions required before authenticated end-to-end testing. Their delivery date is uncertain; the estimate does not state that the Convercus team must perform productive work while waiting.
- `L — Partial uncertainty`: This case overrides Case A's Shop interface evidence: the Convercus target contract and a bounded review of the target documentation (the Loyalty API details from Case A) are available, but the customer-specific Shop source interface, source event schema, and identity-matching rules are unavailable. Extraction and matching implementation cannot yet be bounded.
- `M — Alternative architectures`: Use Case B. REST transaction exchange and scheduled CSV exchange are both considered plausible by the fictional product teams, but implementation details and installed-version confirmation are absent.
- `N — Progressive capture`: Use Case A has an initial estimate and a separately recorded expert revision. No actual delivery results have yet been supplied.

## Acceptance checks

### A — Sufficient technical documentation

Pass if the estimate:

- Analyses both API ends using the supplied versions, operations, schemas, authentication, identifiers, limits, errors, and lack of webhooks.
- Produces bounded activity rows with numerical hour estimates, deliverables, evidence references, responsibilities, and included tasks.
- For each activity, explains specifically why its estimated magnitude is reasonable, identifying the relevant technical drivers from this fixture (such as the two API contracts, opposing data flows, field/identifier mapping, authentication, rate limits, duplicate/error handling, and test/validation needs). A generic task list without a quantitative rationale fails.
- Makes the estimate reviewable by naming the technical assumptions that drive its magnitude and explaining which activity hours should be reconsidered if a factor changes.
- Explicitly identifies affected activities and revises their estimate or conditional status if a relevant technical factor changes, rather than preserving the original hours without reassessment.
- Does not claim the client has issued credentials or that authentication has been tested.
- Does not require particular universal hour values; reviewers assess the specificity and coherence of each justification against the synthetic evidence and scope. Arbitrary hours supported only by generic task descriptions fail.

### B — Incomplete documentation

Pass only if the response avoids both invented certainty and unjustified blocking:

- Labels the missing version, contracts, authentication, installation confirmation, and access as pending; records material hypotheses as conditional risks.
- Estimates the activities that can still be reasonably dimensioned from available evidence, while keeping independent known work moving.
- Where more than one technically plausible solution can be reasonably bounded, presents conditional scenarios and explains the assumptions and activities that differ.
- For this fixture's REST and CSV alternatives, presents separate conditional scenarios if the available high-level evidence is enough to bound them; otherwise identifies exactly which missing detail prevents bounding a scenario and leaves that activity conditional rather than inventing hours.
- Leaves an essential activity without a closed hours figure when the missing evidence prevents identifying a plausible solution or bounding its effort; states exactly what evidence is missing and what check will make it estimable.
- Does not block the entire estimate merely because one activity is uncertain, and does not invent API operations, technical capabilities, certainty, or generic reserve hours.

### C — Shared responsibilities

Pass if the estimate assigns Shop-side work, credentials, data decisions, Loyalty-side work, and UAT approval to the stated owners; separates third-party effort from Convercus effort; and does not price or count third-party implementation as Convercus services.

### D — Double-counting and fixed coverage

Pass if the response flags unclear fixed-fee coverage, does not assume the enablement fee covers integration work, reconciles each shared task against fixed and hourly lines, and counts each activity once. It identifies the calculator descriptions or approval needed to resolve ambiguous coverage.

### E — Fixed fee versus estimated effort

Pass if the response keeps €1,200/module separate from service hours, applies €100/hour or 8h/day only as pricing references, never derives or changes hours from those amounts, and keeps any module enablement distinct from specific engineering effort.

### F — Start-up validation

Pass if the output records the version/rate-limit hypothesis, missing evidence, trigger (credentials and sandbox access at kick-off), affected activities, planned verification, and possible scope/effort consequences. It must not automatically add reserve hours or imply that validating the hypothesis automatically changes price.

### G — Engineering-based bottom-up estimate

Pass if the estimate:

- Defines the candidate architecture and decomposes its scope into implementable units with verifiable results.
- Identifies the actual operations needed for each unit and derives hours from those operations and the case-specific interface, data, testing, and dependency evidence.
- Aggregates operations without double-counting shared work and separates the effort of Convercus from other owners.
- Provides quantitative, assumption-linked rationales; a generic WBS, hours-per-endpoint catalog, uncalibrated coefficient, or arbitrary total fails.

### H — PERT calculation and rationale

Pass if the estimate:

- Provides O, M, and P for each sufficiently bounded activity where PERT is pertinent, and computes `E = (O + 4M + P) / 6` correctly for each.
- Explains the technical conditions behind all three values; P is a plausible upper effort within the same architecture, not a generic contingency or an alternative solution.
- Shows productive effort in hours and does not present E as a confidence interval, delivery promise, or empirically validated result.
- Uses a justified point/range or explicitly leaves work non-dimensionable when PERT is not meaningful. No universal reference values are required.

### I — Changed technical assumption or scope

Pass if the response compares the initial and revised estimates, identifies the new operations and activities affected by the added return flow, updates their O/M/P/E or conditional status with case-specific rationale, and leaves unaffected activities unchanged unless a technical dependency explains a change. It must not silently preserve stale values or apply a blanket uplift.

### J — Traceable expert review

Pass if the estimate:

- Preserves the initial activity breakdown and initial O/M/P/E values.
- Records revised values separately and identifies additions, removals, splits, merges, or other corrections to activities/operations.
- Explains the technical basis of each material revision and whether/how the adapter reuse evidence applies, including differences from this case.
- Records conditional risks, reviewer identity or role when available, review status, and a recalculated E wherever O/M/P changed.
- Describes review as increased expert confidence only; it must not overwrite the baseline or claim empirical validation from review alone.
- Does not block a sufficiently grounded estimate merely because a review has not occurred.

### K — External effort, calendar time, and waiting

Pass if the output separates Convercus productive effort, client/integrator effort, and calendar duration/waiting. It must not convert delayed credentials or decisions into implementation hours or billable effort. Any additional work caused by a delay is a separately described conditional rework risk with a trigger, owner, and affected estimate.

### L — Partial uncertainty and continuation

Pass if the response estimates independent, sufficiently bounded work (such as the documented Convercus target-contract analysis) and keeps the source extraction and identity-matching implementation conditional and without closed hours. It must state exactly what evidence is missing and what check will make those activities estimable; uncertainty in those activities must not block the rest.

### M — Separate architecture scenarios

Pass if REST and scheduled CSV are represented as separate conditional scenarios whenever their work can be reasonably bounded. Each scenario must state its own assumptions, operations, responsibilities, and estimate; the response must not blend them into one PERT range or average. If either scenario cannot be bounded from the fixture, it must identify the missing evidence and leave that scenario conditional rather than inventing effort.

### N — Progressive estimate and outcome capture

Pass if the internal output can preserve the original estimate, expert revisions, and later actual activity results as separate records when those results become available, with relevant scope/assumption context. Because no actuals are supplied in this fixture, it must not invent them or claim calibration. It must not create or require a parametric database, universal coefficient, or persistent artifact for this test.
