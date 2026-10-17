# P1.D2 Engine v0.1

Prototype for the first empirical test of **C4.D2 — Crecimiento vs margen**.

The repository deliberately separates:

```text
SEC client / facts
        ↓
normalization + provenance
        ↓
D2 calculation
        ↓
diagnostics
```

It does **not** make investment decisions.

## 1. Open in VS Code

```bash
code P1_D2_ENGINE_v0_1
```

## 2. Create environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -e '.[dev]'
```

## 3. Run tests first

```bash
pytest
```

## 4. Configure SEC identification

SEC automated access requires an identifiable `User-Agent` with contact information.

```bash
export SEC_USER_AGENT="Your Name your.email@example.com"
```

Do not put the real value in `.env.example`, Git, `AGENTS.md` or source code.

## 5. Run technical sample

The 20 tickers in `input/tickers_technical.csv` are deliberately heterogeneous and **are not a market-cap-qualified P1 universe**. They are for extraction testing.

```bash
p1-d2 run \
  --input input/tickers_technical.csv \
  --output output \
  --limit 20
```

Outputs:

- `output/D2_results.csv` — company-level result/status;
- `output/D2_provenance.csv` — the four facts used for each processed company;
- `output/D2_diagnostics.md` — coverage and failure distribution.

## 6. Interpret diagnostics before candidates

The prototype uses:

```text
useful coverage = processable companies / input tickers
```

Initial technical gate:

```text
>= 70%
```

If it fails, do **not** tune 10% / -2 pp. Fix fact selection first.

## 7. Current D2 seed

For two consecutive full fiscal years:

$$
Revenue\ Growth_{FY}=\frac{Revenue_t}{Revenue_{t-1}}-1
$$

$$
OM_t=\frac{Operating\ Income_t}{Revenue_t}
$$

$$
\Delta OM_{pp}=100(OM_t-OM_{t-1})
$$

Candidate:

```text
Revenue growth >= 10%
AND
Operating-margin delta <= -2 pp
```

## 8. Codex

Start Codex with this repository open and give it:

```text
Read AGENTS.md and execute CODEX_TASK_01.md exactly. Do not change methodology or thresholds unless you first identify a methodological defect and document it separately from code defects.
```

## 9. SEC policy

The SEC states that `data.sec.gov` APIs need no API key, but automated access must identify the requester and remain within fair-access limits. This client defaults to 4 requests/second and caches every JSON response.
