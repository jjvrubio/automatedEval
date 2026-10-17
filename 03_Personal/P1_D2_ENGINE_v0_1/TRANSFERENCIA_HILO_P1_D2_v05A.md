# TRANSFERENCIA DE HILO — P1.D2 tras v0.5A

## Proyecto

**Investigando mercados**

## Objeto

Continuación del desarrollo metodológico y técnico del cribado:

```text
C4.D2 — Crecimiento vs margen operativo
```

La frontera ontológica sigue siendo obligatoria:

```text
Investigando mercados = CONOCER
Inversiones crecimiento = DECIDIR
```

Este hilo NO debe convertir señales D2 en recomendaciones de inversión.

---

# 1. Estado alcanzado

Se ha construido y probado un motor anual SEC/US-GAAP para detectar:

$$
Revenue\ Growth_{FY}\ge 10\%
$$

y:

$$
\Delta OM_{pp}\le -2pp
$$

Los umbrales siguen siendo semillas experimentales.

No son reglas canónicas ni criterios de compra.

La lógica anual D2 permanece congelada desde v0.3.

---

# 2. Universo piloto

Se construyó un universo P1 piloto de 50 compañías estadounidenses mediante Nasdaq Stock Screener.

Criterios previos:

```text
common stock
US
operating business
non-financial
not REIT
not BDC
not royalty trust
not limited partnership
500 M <= market cap <= 20 B USD
```

El piloto es una muestra de estrés deliberadamente balanceada:

```text
B1: 0.5–1 B     → 10
B2: 1–2 B       → 10
B3: 2–5 B       → 10
B4: 5–10 B      → 10
B5: 10–20 B     → 10
```

Por tanto:

$$
Pilot\ Signal\ Rate
\neq
Population\ Signal\ Rate
$$

---

# 3. Resultado de v0.5A

Archivos que deben utilizarse como estado actual:

```text
D2_diagnostics_v05A.md
D2_results_v05A.csv
D2_provenance_v05A.csv
P1_universe_v05A.csv
Revenue_tag_decisions_v05A.csv
Revenue_unknown_diagnostics_v05A.csv
```

Métricas documentadas:

```text
N_input = 50
N_universe_eligible = 40
N_universe_ineligible = 7
N_universe_unknown = 3
UniverseResolutionRate = 94.0%

N_fresh_eligible_processable = 38
EligibleFreshCoverage = 95.0%
EndToEndTerminalResolution = 90.0%
```

La expansión controlada del contrato Revenue resolvió o cerró terminalmente 10 de los 13 casos desconocidos de v0.4.

Persisten:

```text
EMAT → context_mismatch
PXED → context_mismatch
RRC  → ambiguous_components
```

No intentar forzar su resolución para maximizar cobertura.

El objetivo experimental de:

```text
UniverseResolutionRate >= 90%
```

ya se ha superado.

---

# 4. Hallazgo crítico al auditar v0.5A

Existe una inconsistencia material en los flags derivados de AAON.

`D2_results_v05A.csv` contiene:

```text
ticker = AAON

revenue_growth_fy_yoy ≈ +20.1094%
operating_margin_fy_t_minus_1 ≈ 17.4173%
operating_margin_fy_t ≈ 10.1415%
om_delta_pp ≈ -7.2758 pp

candidate_d2 = true
d2_signal = true
freshness_status = fresh
latest_fy_resolution_status = resolved
universe_eligible = true
revenue_eligibility = true

raw_d2_signal = false
eligible_d2_signal = false
```

La procedencia SEC v0.5A incluye para AAON los dos Revenue anuales y los dos `OperatingIncomeLoss` utilizados en D2.

Por tanto, según la especificación vigente:

```text
raw_d2_signal
```

debería coincidir con el resultado técnico D2, y:

```text
eligible_d2_signal =
d2_signal == true
AND
universe_eligible == true
AND
freshness_status == fresh
```

AAON debería previsiblemente contar como señal elegible.

La v0.5A diagnostica sólo:

```text
N_raw_D2_signals = 2
N_eligible_D2_signals = 2
```

pero el CSV contiene tres filas `candidate_d2=true`:

```text
AAON
CXT
FUN
```

No iniciar todavía el triage económico usando el recuento de v0.5A.

---

# 5. Próxima etapa obligatoria: v0.5B

La siguiente tarea es una **reparación de consistencia de estados derivados**, no una modificación metodológica.

Debe:

1. identificar la causa exacta por la que AAON conserva `raw_d2_signal=false`;
2. comprobar si el problema aparece cuando una compañía pasa de `universe_eligible=unknown` a `true` después de la reconciliación Revenue;
3. definir una única fuente de verdad para `d2_signal`;
4. recomputar `raw_d2_signal` y `eligible_d2_signal`;
5. añadir invariantes automáticos;
6. regenerar diagnóstico y outputs v0.5B;
7. no cambiar datos, tags, Revenue, OperatingIncomeLoss, FY, umbrales ni universo.

Archivo de ejecución preparado:

```text
CODEX_TASK_05B.md
```

Aunque conserve el nombre `CODEX_TASK`, puede ejecutarlo GitHub Copilot.

---

# 6. Condición para pasar a triage

Sólo pasar a triage de señales cuando v0.5B demuestre:

```text
candidate_d2
d2_signal
raw_d2_signal
eligible_d2_signal
```

coherentes según sus definiciones.

Si AAON sigue cumpliendo los datos actuales, el conjunto esperado para triage será:

```text
AAON
CXT
FUN
```

No hardcodear esta expectativa.

Debe emerger del motor corregido.

---

# 7. Etapa posterior: triage D2

Una vez cerrada v0.5B, la siguiente etapa será estudiar qué explica cada señal:

```text
observación D2
→ causas contables/económicas
→ hipótesis rivales
→ pregunta de investigación
```

El triage debe distinguir, entre otros:

```text
crecimiento orgánico
M&A / cambio de perímetro
impairments
reestructuración
amortización de intangibles adquiridos
mix
pricing
costes transitorios
deterioro operativo recurrente
base effects
```

No debe convertir D2 en:

```text
buy/sell
valuation signal
convexity
investment opportunity
```

---

# 8. Principio metodológico

D2 sigue siendo detector de divergencia:

$$
\text{Observaciones}
\rightarrow
\text{Divergencia}
\rightarrow
\text{Hipótesis rivales}
\rightarrow
\text{Pregunta de investigación}
$$

No:

$$
\text{Divergencia}
\rightarrow
\text{Conclusión de inversión}
$$

---

# 9. Primera acción del nuevo hilo

1. Revisar los seis archivos v0.5A.
2. Verificar de forma independiente la inconsistencia de AAON.
3. Ejecutar o revisar el resultado de `CODEX_TASK_05B.md`.
4. Sólo después preparar la tarea de triage D2.

No reabrir decisiones ya validadas salvo nueva evidencia.
