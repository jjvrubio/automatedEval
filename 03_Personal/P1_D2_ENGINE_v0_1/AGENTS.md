# AGENTS.md — P1.D2 Engine

## Purpose
This repository is an empirical prototype for **C4.D2 — Crecimiento vs margen** within the `Investigando mercados` methodology.

## Invariants
1. **Conocer != Decidir.** This repo detects research candidates; it never issues buy/sell/hold decisions.
2. **Source != screening logic.** SEC access code and D2 logic must remain separate modules.
3. **Do not silently repair data.** Missing or ambiguous facts must become explicit statuses.
4. **No threshold drift.** Do not change `10% revenue growth` or `-2 pp operating-margin delta` without documenting the experiment in `docs/DECISIONS.md` and updating tests.
5. **Annual first.** P1.D2 v0.1 uses two comparable full fiscal years. Do not add TTM or quarterly reconstruction until the annual prototype passes its technical gate.
6. **Provenance is mandatory.** Every fact used in a D2 calculation must preserve tag, period, form, filing date and accession.
7. **SEC fair access.** Never raise request rate above SEC policy limits. Keep caching enabled. Do not commit contact details or raw cache files.
8. **No market-cap logic inside SEC fact resolution.** Universe selection and historical fact resolution are separate concerns.

## Before editing
Read:
- `docs/C4_D2_Crecimiento_vs_margen.md`
- `docs/12_Contrato_datos_SEC_D2.md`
- `docs/13_Algoritmo_P1_D2_anual.md`

Then run:
```bash
pytest
```

## Definition of done for prototype changes
- tests pass;
- diagnostics remain explicit;
- provenance remains reproducible;
- no methodological rule is changed silently.
