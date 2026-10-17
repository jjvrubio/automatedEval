# CODEX_TASK_02 — Corregir selección temporal y gate de frescura

## Contexto

El primer run real de P1.D2 devolvió:

- N0 = 20
- N4 = 18 procesables
- N5 = 1 candidato
- cobertura nominal = 90%

Pero la inspección de `D2_results.csv` y `D2_provenance.csv` muestra que el gate actual es demasiado permisivo.

Casos problemáticos:

```text
NVDA → FY t = 2022-01-30
DE   → FY t = 2024-10-27
LMT  → FY t = 2019-12-31
```

Estos casos fueron tratados como `processable`, aunque el período seleccionado no es el último ejercicio anual razonablemente disponible.

Por tanto:

```text
nominal_coverage != useful_fresh_coverage
```

No cambies los umbrales D2.

## Objetivo

Corregir exclusivamente:

1. selección del último par FY comparable;
2. detección de series obsoletas;
3. gate técnico;
4. diagnóstico de tags.

No ampliar universo.
No añadir market cap.
No tocar 10% / -2 pp.
No introducir 10-Q ni TTM.

---

# 1. Invariante nueva: latest common comparable FY

La compañía sólo puede ser `processable` si el motor encuentra el par más reciente:

```text
FY t
FY t-1
```

que sea simultáneamente utilizable para:

```text
revenue
OperatingIncomeLoss
```

No selecciones primero un tag de Revenue y después sus dos últimos años.

Debes:

1. construir todas las series candidatas de revenue;
2. construir la serie de OperatingIncomeLoss;
3. encontrar períodos anuales comparables;
4. seleccionar el par común más reciente;
5. sólo entonces elegir el revenue tag que soporta ese par.

---

# 2. Cambios de tag de Revenue

Los tags candidatos siguen siendo:

```text
RevenueFromContractWithCustomerExcludingAssessedTax
Revenues
SalesRevenueNet
```

Un cambio histórico de tag NO debe forzar al motor a quedarse con una serie vieja.

Implementa:

```text
tag transition detection
```

Si un tag deja de utilizarse y otro continúa en años posteriores:

- intenta identificar el par FY más reciente con el tag actual;
- conserva el tag realmente utilizado para cada hecho;
- no concatene dos tags automáticamente dentro del mismo par si su equivalencia no está demostrada.

Si dos tags distintos reportan el mismo período y valores incompatibles:

```text
ambiguous_revenue_tag
```

como hasta ahora.

---

# 3. Freshness guard

Añade una comprobación independiente de frescura.

Para cada compañía estima:

```text
latest_annual_period_end_observed
```

a partir del conjunto de hechos anuales US-GAAP disponibles, no sólo del tag finalmente seleccionado.

Después compara:

```text
selected_fy_t_end
vs
latest_annual_period_end_observed
```

Si la diferencia supera un ciclo fiscal razonable:

```text
stale_selected_period
```

Para v0.2 usa como guard provisional:

```text
selected_fy_t_end < latest_annual_period_end_observed - 450 days
```

No lo conviertas en regla metodológica canónica.
Es un control técnico provisional.

Además calcula:

```text
selected_period_age_days
```

contra `as_of`.

---

# 4. Gate técnico

Sustituye:

```text
processable coverage
```

por dos métricas:

```text
nominal_coverage
fresh_coverage
```

Definiciones:

```text
nominal_coverage =
processable_before_freshness / N0
```

```text
fresh_coverage =
processable_after_freshness / N0
```

El PASS debe depender de:

```text
fresh_coverage >= 70%
```

No del nominal.

---

# 5. Diagnóstico esperado para el run actual

Con los outputs existentes, el nuevo código debería como mínimo dejar de considerar como frescos:

```text
NVDA
DE
LMT
```

No codifiques estos tickers como excepciones.

La lógica debe detectarlos por datos.

---

# 6. NKE

Mantén:

```text
missing_operating_income
```

por ahora.

No reconstruyas EBIT sintéticamente.

Añade al diagnóstico:

```text
available_operating_income_tags
```

o una lista de conceptos cercanos si es fácil extraerla, pero sin utilizarlos automáticamente.

---

# 7. GM

Mantén:

```text
ambiguous_revenue_tag
```

Pero mejora el diagnóstico para registrar:

```text
tag A
value A
tag B
value B
period
```

No resuelvas la ambigüedad por heurística todavía.

---

# 8. Candidate handling

ABNB puede seguir apareciendo como `candidate_D2` en términos puramente fundamentales.

Pero el output debe distinguir:

```text
d2_signal = True/False
universe_eligible = unknown/True/False
```

En esta tarea:

```text
universe_eligible = unknown
```

porque todavía no estamos aplicando el rango completo de market cap.

No llames a ABNB `P1 candidate` todavía.

---

# 9. Tests obligatorios

Añade tests para:

1. un tag revenue viejo deja de usarse y otro tag continúa;
2. el motor selecciona el par FY común más reciente;
3. una serie 5 años obsoleta produce `stale_selected_period`;
4. `fresh_coverage` excluye stale;
5. GM-like ambiguous tags siguen siendo ambiguos;
6. NKE-like missing OperatingIncomeLoss no se reconstruye;
7. ABNB-like signal puede ser D2=True con `universe_eligible=unknown`.

Todos los tests deben quedar verdes.

---

# 10. Salidas nuevas

Actualizar `D2_results.csv` con:

```text
selected_fy_t_end
latest_annual_period_end_observed
selected_period_age_days
freshness_status
d2_signal
universe_eligible
```

Actualizar `D2_diagnostics.md` con:

```text
N0
nominal_processable
fresh_processable
nominal_coverage
fresh_coverage
D2_signals
stale_selected_period count
```

Añadir una sección:

```text
## Freshness failures
```

con ticker + selected FY + latest annual period observed.

---

# 11. No hacer

No:

- cambiar 10% / -2 pp;
- introducir market cap todavía;
- introducir 10-Q;
- introducir TTM;
- ampliar a 50 tickers;
- resolver manualmente LMT/NVDA/DE;
- usar excepciones por ticker;
- silenciar ambigüedades;
- cambiar la ontología o taxonomía.

---

# 12. Criterio de cierre

La tarea termina cuando:

```text
pytest
```

está verde y el mismo lote de 20 tickers produce un diagnóstico donde:

- la frescura se mide explícitamente;
- los períodos obsoletos ya no cuentan como cobertura útil;
- ninguna señal D2 depende de un FY obsoleto;
- no se ha modificado la metodología.

Después entrega:

```text
D2_results_v02.csv
D2_provenance_v02.csv
D2_diagnostics_v02.md
CODEX_TASK_02_REPORT.md
```
