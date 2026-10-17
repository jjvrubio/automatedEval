# Decisions

## 2026-10-05 — Prototype baseline

- Historical source: SEC EDGAR `companyfacts`.
- Comparison: two consecutive full fiscal years.
- Revenue candidate tags: `RevenueFromContractWithCustomerExcludingAssessedTax`, `Revenues`, `SalesRevenueNet`.
- Operating income tag: `OperatingIncomeLoss`.
- D2 seed: revenue growth >= 10% and operating-margin delta <= -2 pp.
- Technical gate: useful coverage >= 70% before threshold calibration.

## 2026-10-05 — Data-contract review findings

- The annual-duration filter validates each fiscal period independently (330–400 days), but does not compare the durations of the two selected periods. A 330-day period and a 370-day period can pass as consecutive; define and test a maximum duration difference before treating such periods as comparable.
- Revenue-tag ambiguity is checked only when candidate tags select identical latest period pairs. Conflicting values on an overlapping period can therefore be missed when tags have different latest pairs; compare all overlapping selected annual periods before resolving a tag.
- These are extraction/comparability defects, not changes to the D2 hypothesis or thresholds. No live SEC coverage was measured in this review.
