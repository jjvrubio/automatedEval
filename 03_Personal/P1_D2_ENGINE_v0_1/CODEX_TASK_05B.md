# CODEX_TASK_05B — Reconciliación de flags D2 tras Revenue v0.5A

> El nombre `CODEX_TASK` se conserva por continuidad.
> Puede ejecutarse con GitHub Copilot.

## Contexto

v0.5A mejoró la resolución de Revenue sin modificar el motor D2 v0.3.

Métricas documentadas:

```text
N_input = 50
N_universe_eligible = 40
N_universe_ineligible = 7
N_universe_unknown = 3
UniverseResolutionRate = 94.0%
N_fresh_eligible_processable = 38
EligibleFreshCoverage = 95.0%
```

Sin embargo, existe una inconsistencia derivada.

AAON contiene simultáneamente:

```text
candidate_d2 = true
d2_signal = true
freshness_status = fresh
latest_fy_resolution_status = resolved
universe_eligible = true
revenue_eligibility = true

raw_d2_signal = false
eligible_d2_signal = false
```

Sus métricas D2 son:

```text
Revenue growth FY YoY ≈ +20.1094%
OM FY t-1 ≈ 17.4173%
OM FY t ≈ 10.1415%
ΔOM ≈ -7.2758 pp
```

La procedencia contiene los dos hechos Revenue y los dos `OperatingIncomeLoss` usados para el cálculo.

Por definición vigente:

```text
raw_d2_signal = d2_signal
```

para una fila con D2 técnicamente evaluado.

Y:

```text
eligible_d2_signal =
raw_d2_signal == true
AND
universe_eligible == true
AND
freshness_status == fresh
```

La tarea consiste únicamente en restaurar consistencia.

---

# 1. Invariantes

NO modificar:

```text
Revenue Growth >= 10%
ΔOM <= -2 pp
```

NO modificar:

- universo de 50;
- Revenue facts seleccionados;
- contrato Revenue v0.5A;
- decisiones semánticas de tags;
- OperatingIncomeLoss;
- latest-FY logic;
- freshness logic;
- market-cap filters;
- entity exclusions;
- 10-K/10-K/A;
- US-GAAP scope.

NO introducir:

- 10-Q;
- TTM;
- triage económico;
- impairment adjustments;
- M&A adjustments;
- valoración;
- precio;
- inversión.

---

# 2. Input congelado

Usar los outputs v0.5A existentes como caso de regresión:

```text
D2_results_v05A.csv
D2_provenance_v05A.csv
P1_universe_v05A.csv
Revenue_tag_decisions_v05A.csv
Revenue_unknown_diagnostics_v05A.csv
```

No editar estos archivos.

---

# 3. Diagnóstico causal obligatorio

Identificar en código por qué:

```text
AAON.d2_signal = true
```

pero:

```text
AAON.raw_d2_signal = false
```

Determinar si el error proviene de:

```text
ordering of pipeline stages
stale copied flag
pre-reconciliation snapshot
failure to recompute derived field
join/merge overwrite
boolean coercion
other
```

Documentar la causa exacta.

No aplicar un parche específico para AAON.

---

# 4. Fuente única de verdad

Establecer una única derivación explícita.

Para filas donde D2 fue evaluado:

```text
raw_d2_signal = bool(d2_signal)
```

Para filas donde D2 NO fue evaluado:

```text
raw_d2_signal = false
```

y debe existir un `status/reason` que explique por qué no se evaluó.

Después:

```text
eligible_d2_signal =
raw_d2_signal
AND
universe_eligible == true
AND
freshness_status == fresh
```

No mantener una segunda lógica independiente que vuelva a calcular los umbrales.

---

# 5. Invariantes de consistencia

Añadir checks automáticos.

## Invariante A

Si:

```text
status == candidate
```

entonces:

```text
d2_signal == true
raw_d2_signal == true
```

## Invariante B

Si:

```text
eligible_d2_signal == true
```

entonces necesariamente:

```text
raw_d2_signal == true
universe_eligible == true
freshness_status == fresh
```

## Invariante C

Si:

```text
raw_d2_signal == true
AND
universe_eligible == true
AND
freshness_status == fresh
```

entonces:

```text
eligible_d2_signal == true
```

## Invariante D

No puede existir:

```text
d2_signal != raw_d2_signal
```

cuando D2 haya sido evaluado.

---

# 6. Revisión completa de las 50 filas

No comprobar sólo AAON.

Buscar automáticamente inconsistencias entre:

```text
candidate_d2
status
d2_signal
raw_d2_signal
eligible_d2_signal
universe_eligible
freshness_status
latest_fy_resolution_status
```

Generar un audit:

```text
output/D2_flag_consistency_audit_v05B.csv
```

con una fila por ticker y:

```text
ticker
status
candidate_d2
d2_signal
raw_d2_signal
eligible_d2_signal
universe_eligible
freshness_status
latest_fy_resolution_status
consistency_status
consistency_reason
```

---

# 7. Tests obligatorios

Mantener todos los tests previos.

Añadir al menos:

1. D2 true + eligible true + fresh → eligible signal true;
2. D2 true + eligible unknown → eligible signal false;
3. D2 true + fresh false → eligible signal false;
4. D2 false + eligible true + fresh → eligible signal false;
5. candidate status cannot coexist with raw false;
6. AAON-like transition from Revenue unknown to Revenue resolved recomputes derived flags;
7. merge/update of Revenue eligibility cannot preserve a stale raw flag;
8. all 50 v0.5A rows pass the new consistency audit after regeneration.

Ejecutar:

```bash
pytest -q
```

---

# 8. Outputs v0.5B

No sobrescribir v0.5A.

Generar:

```text
output/P1_universe_v05B.csv
output/D2_results_v05B.csv
output/D2_provenance_v05B.csv
output/D2_flag_consistency_audit_v05B.csv
output/D2_diagnostics_v05B.md
CODEX_TASK_05B_REPORT.md
```

Usar:

```text
engine_version = 0.5B
d2_engine_version = 0.3
task = CODEX_TASK_05B
```

Revenue contract version remains v0.5A-equivalent unless a purely technical version label is required.

---

# 9. Diagnóstico v0.5B

Informar:

```text
N_input
N_universe_eligible
N_universe_ineligible
N_universe_unknown
UniverseResolutionRate
N_fresh_eligible_processable
EligibleFreshCoverage
N_raw_D2_signals
N_eligible_D2_signals
N_flag_inconsistencies
```

Añadir:

```text
## Eligible D2 signals
```

con todas las señales que emerjan después de corregir los flags.

No hardcodear:

```text
AAON
CXT
FUN
```

---

# 10. No triage todavía

No explicar aún por qué las señales existen.

No clasificar:

```text
M&A
impairment
restructuring
organic deterioration
```

Eso pertenece a la siguiente etapa.

Esta tarea termina al estabilizar el estado lógico.

---

# 11. Criterio de cierre

Éxito sólo si:

```text
pytest PASS
N_flag_inconsistencies = 0
derived flags recomputed from one source of truth
no methodology drift
v0.5A preserved
```

El informe debe responder:

1. causa exacta del bug;
2. cuántas filas estaban afectadas;
3. si el recuento de señales cambió;
4. qué tickers son señales elegibles después de la corrección;
5. confirmación de que Revenue y D2 no fueron metodológicamente alterados.

Terminar con:

```text
READY_FOR_SIGNAL_TRIAGE
```

si todo lo anterior se cumple.
