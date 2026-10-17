# CODEX_TASK_03 — Exigir el último FY disponible para D2

## Contexto

`CODEX_TASK_02_RETRY` fue ejecutado correctamente:

```text
pytest = PASS
nominal_coverage = 90%
fresh_coverage = 90%
D2_signals = 2
```

Sin embargo, la ejecución ha revelado un defecto en la especificación de frescura.

Caso observado:

```text
DE
selected_fy_t_end = 2024-10-27
latest_annual_period_end_observed = 2025-11-02
selected_period_age_days = 709
freshness_status = fresh
```

El resultado cumple el guard provisional anterior porque:

```text
2025-11-02 - 2024-10-27 = 371 días
371 < 450
```

Pero metodológicamente no es aceptable llamar `fresh` a un cálculo D2 que omite el último ejercicio anual disponible.

El problema no es de implementación de Codex.
El problema es la regla de frescura definida en la tarea anterior.

No cambies los umbrales D2.
No amplíes universo.
No añadas market cap.
No introduzcas 10-Q ni TTM.

---

# 1. Nueva definición de frescura

Retirar como criterio de aceptación:

```text
selected_fy_t_end >= latest_annual_period_end_observed - 450 days
```

La frescura de D2 anual debe exigir que el período seleccionado corresponda al **último ejercicio anual observado**.

Regla:

```text
selected_fy_t_end == latest_annual_period_end_observed
```

Si existe una razón técnica documentada para permitir pequeñas diferencias de fecha dentro del mismo FY, impleméntala sólo si aparece un caso real en fixtures y documenta la tolerancia.

No introduzcas una tolerancia arbitraria de cientos de días.

---

# 2. Nuevo estado

Si:

```text
selected_fy_t_end < latest_annual_period_end_observed
```

el estado debe ser:

```text
latest_fy_unresolved
```

No:

```text
fresh
discard
```

Ese ticker:

- no cuenta como `fresh_processable`;
- no participa en D2;
- no se considera descarte fundamental;
- queda como incidencia de cobertura.

---

# 3. Diferenciar dos conceptos

Mantener:

```text
selected_period_age_days
```

como información descriptiva.

Pero NO usar la antigüedad absoluta como criterio principal de frescura.

Ejemplo:

Una compañía con FY terminado hace 370 días puede seguir estar usando su último FY disponible si todavía no ha cerrado/reportado el siguiente.

Por tanto:

```text
absolute age
!=
staleness
```

La pregunta correcta es:

```text
¿el FY usado es el último FY anual observado?
```

---

# 4. Deere como prueba de regresión

No codifiques `DE` como excepción.

Construye un fixture equivalente:

```text
latest annual facts exist for FY2025
Revenue exists for FY2025
OperatingIncomeLoss only resolves through FY2024
```

Resultado esperado:

```text
status = latest_fy_unresolved
freshness_status = latest_fy_unresolved
d2_signal = false
```

El motor no debe retroceder silenciosamente a FY2024 y clasificar la compañía.

---

# 5. Gate técnico

Actualizar:

```text
fresh_processable
```

para excluir:

```text
latest_fy_unresolved
```

El PASS sigue siendo:

```text
fresh_coverage >= 70%
```

Con el lote actual esperamos aproximadamente:

```text
fresh_processable = 17
fresh_coverage = 85%
```

No hardcodear estas cifras; deben emerger del run.

---

# 6. Diagnóstico

`D2_diagnostics_v03.md` debe añadir:

```text
latest_fy_unresolved count
```

y:

```text
## Latest FY unresolved
```

con columnas:

```text
ticker
selected_fy_t_end
latest_annual_period_end_observed
missing_metric
```

Para DE, `missing_metric` debería explicar qué impide resolver el último FY, por ejemplo:

```text
OperatingIncomeLoss
```

si ése es realmente el caso.

---

# 7. NKE y GM

Mantener:

```text
NKE → missing_operating_income
GM  → ambiguous_revenue_tag
```

No reconstruir EBIT.
No resolver tags ambiguos automáticamente.

---

# 8. Señales D2

NVDA y ABNB pueden seguir siendo:

```text
d2_signal = true
```

si la lógica y los hechos frescos lo sostienen.

No investigues todavía el universo de market cap.

Mantener:

```text
universe_eligible = unknown
```

---

# 9. Tests obligatorios

Añadir tests para:

1. último FY resoluble → `fresh`;
2. FY anterior resoluble pero último FY no → `latest_fy_unresolved`;
3. `latest_fy_unresolved` no cuenta en `fresh_processable`;
4. absolute age > 365 días puede seguir ser `fresh` si es el último FY observado;
5. DE-like fixture;
6. NVDA-like latest FY continues as fresh;
7. existing GM/NKE regressions remain green.

Ejecutar:

```bash
pytest -q
```

---

# 10. Salidas nuevas

No sobrescribir v02.

Generar:

```text
D2_results_v03.csv
D2_provenance_v03.csv
D2_diagnostics_v03.md
CODEX_TASK_03_REPORT.md
```

Añadir:

```text
engine_version = 0.3
task = CODEX_TASK_03
```

---

# 11. Resultados mínimos en `D2_results_v03.csv`

Conservar:

```text
engine_version
ticker
status
selected_fy_t_end
latest_annual_period_end_observed
selected_period_age_days
freshness_status
revenue_growth_fy_yoy
operating_margin_fy_t
operating_margin_fy_t_minus_1
om_delta_pp
d2_signal
universe_eligible
```

Añadir:

```text
latest_fy_resolution_status
missing_latest_fy_metric
```

---

# 12. No hacer

No:

- cambiar Revenue Growth >= 10%;
- cambiar ΔOM <= -2 pp;
- introducir market cap;
- ampliar a 50 tickers;
- introducir 10-Q;
- introducir TTM;
- reconstruir OperatingIncomeLoss;
- usar excepciones por ticker;
- modificar ontología;
- clasificar `latest_fy_unresolved` como `discard`.

---

# 13. Criterio de cierre

La tarea termina cuando:

```text
pytest = PASS
DE-like case = latest_fy_unresolved
fresh gate uses latest FY requirement
v03 artifacts generated
```

y el informe explica:

1. qué cambió respecto de v02;
2. nueva fresh_coverage;
3. qué tickers quedaron `latest_fy_unresolved`;
4. si NVDA y ABNB siguen siendo señales D2;
5. hashes SHA-256 de los artefactos v03.
