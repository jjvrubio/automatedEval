# Prototype status — v0.1

## Completed

- repository structure for VS Code / Codex;
- SEC client with cache and conservative 4 req/s default;
- ticker → CIK mapping;
- annual XBRL fact filtering;
- latest filing / amendment precedence for identical periods;
- explicit revenue-tag ambiguity status;
- alignment of revenue and `OperatingIncomeLoss` periods;
- D2 annual calculation;
- provenance output;
- diagnostics and 70% technical gate;
- synthetic end-to-end demo;
- pytest suite.

## Test status

```text
5 passed
```

## Not yet executed

A live SEC run has **not** been executed in this packaged prototype because SEC fair-access guidance requires an identifiable `User-Agent` with real contact information. The repository deliberately does not embed or invent one.

Once `SEC_USER_AGENT` is set locally, the next empirical step is:

```bash
p1-d2 run --input input/tickers_technical.csv --output output --limit 20
```

The first object to inspect is `output/D2_diagnostics.md`, not the candidate list.
