# CODEX_TASK_05A Report

status: READY_FOR_SIGNAL_TRIAGE
engine_version: 0.5A
d2_engine_version: 0.3 (frozen)
task: CODEX_TASK_05A
input_universe_sha256: 01c760346139648c9f63624c516f94db4c3a4fe9fc0bf2ad33171dd557323f57

## Respuestas

1. Revenue comparable quedó resuelto automáticamente en 7 de 13 unknown.
2. 3 siguen unknown (EMAT, PXED, RRC); 3 quedaron definitivamente ineligible por ausencia explícita de Revenue comercial.
3. Causas: 5 tags estándar alternativos, 1 conflicto componente/total, 2 conceptos totales semánticamente distintos, 2 mismatches de contexto y 3 casos sin Revenue/pre-revenue.
4. Nuevo tag estándar aceptado condicionalmente: RevenueFromContractWithCustomerIncludingAssessedTax. La aceptación requiere conciliación al estado primario.
5. Custom tags validados: ninguno.
6. Permanecen EMAT y PXED por contexto anual/registrante no reconciliable y RRC por diferencias entre ingresos por contratos, ganancias de derivados y otros ingresos.
7. UniverseResolutionRate: 94.0%.
8. EligibleFreshCoverage: 95.0%.
9. Señales D2 elegibles: 2, sin cambio frente a v0.4; CXT y FUN permanecen candidates.
10. Se confirmó que una partida de derivados puede formar parte de operating revenues; el contrato ahora requiere validación del estado/notas del filing y no se apoya sólo en labels XBRL.
11. La expansión a 100 está técnicamente justificada para pasar a triage de señales: tests PASS, gates >=70% y objetivo experimental >=90% cumplidos; los tres unknown restantes siguen explícitos y no se rellenan por heurística.

No hay ramas de resolución específicas por ticker. El input congelado coincide y los outputs v0.4 no fueron sobrescritos.

## SHA-256 de artefactos v05A

- `88d77e411c39ff3f8cd5bc4e3ea58172771a2d221982721a1272a60782cce3f8`  `output/Revenue_unknown_diagnostics_v05A.csv`
- `10b68e5c5c8172eb1d95e361a061964319b7c56e3800a29bcc31172a74f539ad`  `output/Revenue_tag_decisions_v05A.csv`
- `59dd2d7d9dffc5c382432a2dff80dfe351433c9e4fef61b6d841096cb2750aaa`  `output/P1_universe_v05A.csv`
- `69d86beaf341115e654bf11a23fc2e942b32a37b74e4116c4904d70ffa54a153`  `output/D2_results_v05A.csv`
- `3ff29e6c7d2a4f5a60a8e6f27ff71b4a4cfe6c541fe3f88abf8eb17aa52bec92`  `output/D2_provenance_v05A.csv`
- `ff62534b791ec34fc95c0bbdae07a9b66346a0be6d6e2d182cd365837aa514c8`  `output/D2_diagnostics_v05A.md`

## Metrics

# P1.D2 diagnostics v0.5A

engine_version: 0.5A
d2_engine_version: 0.3 (frozen)
task: CODEX_TASK_05A

- N_input: 50
- N_universe_eligible: 40
- N_universe_ineligible: 7
- N_universe_unknown: 3
- UniverseResolutionRate: 94.0%
- N_fresh_eligible_processable: 38
- EligibleFreshCoverage: 95.0%
- N_definitively_ineligible: 7
- EndToEndTerminalResolution: 90.0%
- N_raw_D2_signals: 2
- N_eligible_D2_signals: 2
- fresh_coverage (legacy descriptive): 76.0%

## Revenue diagnostic causes

| Cause | Count |
|---|---:|
| A_alternative_standard_total_revenue_tag | 5 |
| C_component_vs_total_conflict | 1 |
| D_multiple_total_concepts_semantically_different | 2 |
| E_latest_period_context_mismatch | 2 |
| F_true_no_revenue_or_pre_revenue | 3 |

## Unknown resolution changes

| Ticker | v04_status | v05A_status | cause | resolution_method | revenue_value | source_filing_url |
|---|---|---|---|---|---:|---|
| AAON | unresolved | resolved_standard_total | A_alternative_standard_total_revenue_tag | standard_total | 1442076000.0 | https://www.sec.gov/Archives/edgar/data/824142/000082414226000005/ |
| BV | unresolved | resolved_standard_total | A_alternative_standard_total_revenue_tag | standard_total | 2672800000.0 | https://www.sec.gov/Archives/edgar/data/1734713/000119312525288109/ |
| EMAT | unresolved | context_mismatch | E_latest_period_context_mismatch |  |  | https://www.sec.gov/Archives/edgar/data/1866226/000121390026018858/ |
| EVRG | ambiguous | resolved_semantic_reconciliation | D_multiple_total_concepts_semantically_different | semantic_reconciliation | 5961600000.0 | https://www.sec.gov/Archives/edgar/data/1711269/000171126926000017/ |
| FRNM | unresolved | no_revenue | F_true_no_revenue_or_pre_revenue |  | 0.0 | https://www.sec.gov/Archives/edgar/data/2017526/000114036126009262/ |
| HYMC | unresolved | no_revenue | F_true_no_revenue_or_pre_revenue |  | 0.0 | https://www.sec.gov/Archives/edgar/data/1718405/000171840526000009/ |
| IDT | unresolved | resolved_standard_total | A_alternative_standard_total_revenue_tag | standard_total | 1297960000.0 | https://www.sec.gov/Archives/edgar/data/1005731/000143774926031469/ |
| IMVT | unresolved | no_revenue | F_true_no_revenue_or_pre_revenue |  | 0.0 | https://www.sec.gov/Archives/edgar/data/1764013/000176401326000064/ |
| LFUS | unresolved | resolved_standard_total | A_alternative_standard_total_revenue_tag | standard_total | 2386294000.0 | https://www.sec.gov/Archives/edgar/data/889331/000162828026009585/ |
| MATW | unresolved | resolved_standard_total | A_alternative_standard_total_revenue_tag | standard_total | 1497689000.0 | https://www.sec.gov/Archives/edgar/data/63296/000006329625000070/ |
| PXED | unresolved | context_mismatch | E_latest_period_context_mismatch |  |  | https://www.sec.gov/Archives/edgar/data/1600222/000119312525289786/ |
| RRC | ambiguous | ambiguous_components | D_multiple_total_concepts_semantically_different |  |  | https://www.sec.gov/Archives/edgar/data/315852/000119312526067292/ |
| WEX | ambiguous | resolved_semantic_reconciliation | C_component_vs_total_conflict | semantic_reconciliation | 2660800000.0 | https://www.sec.gov/Archives/edgar/data/1309108/000130910826000010/ |

## Gates

EligibleFreshCoverage >= 70%: PASS
UniverseResolutionRate >= 90% experimental objective: PASS

Revenue ambiguity is not treated as terminal. `fresh_coverage` is descriptive only; D2 is gated on eligible companies.
The annual D2 evaluator and thresholds (Revenue growth >= 10%, operating-margin delta <= -2 pp) remain v0.3 unchanged.

D2 thresholds and `OperatingIncomeLoss` selection were not changed. CXT/FUN signal classification is preserved from the v0.4 frozen results. This pilot is a technical coverage experiment, not an investment recommendation.
