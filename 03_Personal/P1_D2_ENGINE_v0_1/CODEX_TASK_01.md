# Codex Task 01 — Validate the P1.D2 SEC prototype

Work inside this repository only.

## Objective
Validate the **data contract and extraction logic**, not the investment usefulness of D2.

## Required sequence
1. Read `AGENTS.md` and the three methodology docs in `docs/`.
2. Run `pytest` and do not modify code until you understand any failure.
3. Review `fact_resolver.py` specifically for:
   - duplicate/restated annual facts;
   - revenue-tag ambiguity;
   - period alignment between revenue and operating income;
   - 52/53-week fiscal years.
4. Review `sec_client.py` for SEC fair-access compliance and caching.
5. Do **not** change D2 thresholds or add TTM/quarterly logic.
6. After the user has set a real `SEC_USER_AGENT`, run:
   ```bash
   p1-d2 run --input input/tickers_technical.csv --output output --limit 20
   ```
7. Inspect `output/D2_diagnostics.md` first. If useful coverage is <70%, diagnose extraction failures before discussing candidates.
8. Record any methodological/data-contract issue in `docs/DECISIONS.md`; do not silently patch the method.

## Deliverable
Return:
- test status;
- coverage status;
- error/status distribution;
- any data-contract defects;
- proposed code fixes separated from proposed methodology changes.
