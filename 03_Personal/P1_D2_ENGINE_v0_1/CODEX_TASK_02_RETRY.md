# CODEX_TASK_02_RETRY — Aplicar realmente la corrección de frescura

## Motivo

La ejecución posterior a `CODEX_TASK_02.md` devolvió artefactos **idénticos byte por byte** a los del run anterior.

Por tanto, NO asumir que `CODEX_TASK_02` fue aplicado.

No cambies metodología.
No cambies umbrales.
No amplíes universo.

---

# 0. Verificación obligatoria antes de tocar código

Desde la raíz del repo:

```bash
pwd
git status --short
find . -maxdepth 3 -type f | sort
```

Confirma que estás trabajando sobre el repo correcto.

Busca si existen ya los cambios pedidos:

```bash
grep -R "fresh_coverage" -n src tests . || true
grep -R "stale_selected_period" -n src tests . || true
grep -R "universe_eligible" -n src tests . || true
grep -R "latest_annual_period_end_observed" -n src tests . || true
```

## Regla

Si ninguno aparece, `CODEX_TASK_02` NO fue implementado.

Si aparecen sólo en documentación pero no en código/tests, tampoco fue implementado.

---

# 1. Leer primero

Lee:

```text
AGENTS.md
CODEX_TASK_02.md
```

y conserva todas sus restricciones.

La tarea sigue siendo exclusivamente:

- seleccionar el par FY común más reciente;
- detectar períodos obsoletos;
- separar cobertura nominal y fresca;
- mejorar diagnóstico de tags;
- distinguir `d2_signal` de `universe_eligible`.

---

# 2. Cambios mínimos obligatorios en código

El código final debe contener de forma explícita:

```text
latest_annual_period_end_observed
selected_period_age_days
freshness_status
stale_selected_period
d2_signal
universe_eligible
nominal_coverage
fresh_coverage
```

No basta con calcularlos internamente.

Deben aparecer en las salidas correspondientes.

---

# 3. Selección temporal

Implementa el flujo:

```text
todos los revenue tags candidatos
+
OperatingIncomeLoss
        ↓
períodos FY comparables comunes
        ↓
par común más reciente
        ↓
validación de frescura
        ↓
cálculo D2
```

No:

```text
elegir primero un revenue tag
→ quedarse con dos años viejos
```

---

# 4. Freshness guard

Calcular:

```text
latest_annual_period_end_observed
```

a partir de hechos anuales US-GAAP razonablemente utilizables.

Luego:

```text
selected_fy_t_end
```

debe compararse con ese máximo.

Control provisional:

```text
selected_fy_t_end < latest_annual_period_end_observed - 450 days
→ stale_selected_period
```

Además:

```text
selected_period_age_days
```

contra la fecha `as_of` del run.

---

# 5. Gate

Calcular:

```text
nominal_coverage
fresh_coverage
```

y usar sólo:

```text
fresh_coverage >= 70%
```

para PASS.

El diagnóstico debe mostrar ambas.

---

# 6. Casos que deben corregirse por lógica, no por ticker

El run anterior seleccionó:

```text
NVDA → FY 2022
DE   → FY 2024
LMT  → FY 2019
```

No introduzcas excepciones por ticker.

La nueva lógica debe detectar automáticamente que el período seleccionado no es suficientemente reciente respecto del histórico anual observado.

---

# 7. Casos que deben conservar comportamiento

## GM

Debe seguir como:

```text
ambiguous_revenue_tag
```

si persiste incompatibilidad real.

El diagnóstico debe registrar:

```text
period
tag_a
value_a
tag_b
value_b
```

## NKE

Debe seguir como:

```text
missing_operating_income
```

si falta `OperatingIncomeLoss`.

No reconstruir EBIT.

## ABNB

Puede seguir como:

```text
d2_signal = true
```

si los datos frescos lo sostienen.

Pero:

```text
universe_eligible = unknown
```

porque todavía no aplicamos universo completo.

---

# 8. Tests obligatorios

Añadir y ejecutar tests para:

1. cambio histórico de revenue tag;
2. selección del FY común más reciente;
3. serie obsoleta → `stale_selected_period`;
4. stale excluido de `fresh_coverage`;
5. ambiguous revenue tags;
6. missing OperatingIncomeLoss;
7. `d2_signal=True` con `universe_eligible=unknown`.

Ejecutar:

```bash
pytest -q
```

No continuar si no está verde.

---

# 9. Prueba de que el código nuevo está activo

Antes del run real:

```bash
grep -R "fresh_coverage" -n src tests
grep -R "stale_selected_period" -n src tests
grep -R "universe_eligible" -n src tests
```

Incluye la salida relevante en el informe.

---

# 10. Salidas: NO sobrescribir v0.1

Genera obligatoriamente nombres nuevos:

```text
D2_results_v02.csv
D2_provenance_v02.csv
D2_diagnostics_v02.md
CODEX_TASK_02_REPORT.md
```

No escribas:

```text
D2_results.csv
D2_provenance.csv
D2_diagnostics.md
```

---

# 11. Versionado dentro de los artefactos

Añade en `D2_diagnostics_v02.md`:

```text
engine_version: 0.2
task: CODEX_TASK_02_RETRY
as_of: <timestamp ISO>
```

Y en `D2_results_v02.csv` añade:

```text
engine_version
```

con valor:

```text
0.2
```

en todas las filas.

---

# 12. Columnas obligatorias en results v02

Como mínimo:

```text
engine_version
ticker
status
selected_fy_t_end
selected_fy_t_minus_1_end
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

Si estas columnas no existen, la tarea no está terminada.

---

# 13. Diagnóstico obligatorio

`D2_diagnostics_v02.md` debe contener:

```text
N0
nominal_processable
fresh_processable
nominal_coverage
fresh_coverage
D2_signals
stale_selected_period count
```

y:

```text
## Freshness failures
```

con:

```text
ticker
selected FY
latest annual period observed
```

---

# 14. Verificación final de que no devolvemos archivos viejos

Al terminar, ejecutar:

```bash
sha256sum \
  output/D2_results_v02.csv \
  output/D2_provenance_v02.csv \
  output/D2_diagnostics_v02.md
```

Incluye esos hashes en:

```text
CODEX_TASK_02_REPORT.md
```

También confirma explícitamente:

```text
The v02 artifacts are newly generated and are not copies of the v01 artifacts.
```

---

# 15. No hacer

No:

- tocar 10% / -2 pp;
- añadir market cap;
- ampliar a 50 tickers;
- introducir 10-Q;
- introducir TTM;
- modificar ontología;
- introducir excepciones por ticker;
- sobrescribir v0.1;
- devolver archivos con nombres antiguos.

---

# 16. Criterio de cierre

Sólo termina cuando:

```text
pytest = PASS
freshness fields = presentes
v02 outputs = generados
hashes = registrados
```

Entrega exactamente:

```text
D2_results_v02.csv
D2_provenance_v02.csv
D2_diagnostics_v02.md
CODEX_TASK_02_REPORT.md
```
