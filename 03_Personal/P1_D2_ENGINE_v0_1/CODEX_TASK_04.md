# CODEX_TASK_04 — Primer lote de universo real P1.D2

## Contexto

La infraestructura anual SEC del motor P1.D2 ha superado la prueba técnica v0.3.

Último estado validado:

```text
engine_version = 0.3
N0 = 20
nominal_processable = 18
fresh_processable = 17
fresh_coverage = 85%
D2_signals = 2
latest_fy_unresolved = 1
technical_gate = PASS
```

Comportamientos ya validados:

```text
DE   → latest_fy_unresolved
GM   → ambiguous_revenue_tag
NKE  → missing_operating_income
NVDA → d2_signal = true
ABNB → d2_signal = true
```

La selección temporal, el contrato SEC y los umbrales D2 quedan **congelados** para esta tarea.

No estamos reparando el extractor.

Estamos cambiando de fase:

```text
prueba técnica del motor
→
prueba sobre universo P1 real
```

---

# 1. Objetivo

Añadir una capa explícita de:

```text
universe_eligibility
```

y ejecutar el motor anual D2 sobre un lote piloto de:

```text
50 compañías
```

que pertenezcan realmente al universo P1.

La pregunta de esta tarea es:

> ¿Mantiene el motor una cobertura fresca suficiente y produce una tasa de señales razonable cuando se aplica a compañías elegibles del universo P1?

---

# 2. Invariantes

NO modificar:

```text
Revenue Growth FY YoY >= 10%
Δ Operating Margin <= -2 pp
```

NO modificar:

- lógica de selección FY;
- contrato SEC;
- resolución de tags;
- definición de `latest_fy_unresolved`;
- tratamiento de GM/NKE-like cases;
- exclusión de datos ambiguos;
- ontología;
- taxonomía.

NO introducir todavía:

- 10-Q;
- TTM;
- scoring agregado;
- valoración;
- precio como señal;
- momentum;
- analistas;
- dividendos;
- convexidad;
- decisión de inversión.

---

# 3. Definición del universo P1

Una compañía es elegible si cumple simultáneamente:

```text
country = US
security_type = common_stock
operating_business = true
financial_sector = false
reit = false
bdc = false
pre_revenue = false
market_cap_current >= 500,000,000
market_cap_current <= 20,000,000,000
revenue_latest_fy > 100,000,000
SEC reporting = 10-K / US-GAAP
```

La elegibilidad es un filtro de investigación.

No es un criterio de inversión.

---

# 4. Separar datos actuales de datos SEC

Mantener esta arquitectura:

```text
CURRENT UNIVERSE DATA
→ market cap
→ sector / industry
→ security type
→ entity flags

SEC EDGAR
→ historical Revenue
→ historical OperatingIncomeLoss
→ D2 annual engine
```

No utilizar SEC `companyfacts` como fuente principal de market cap.

No usar el market cap implícito de fechas históricas SEC.

---

# 5. Fuente de datos actuales

La lógica de universo debe aceptar un fichero de entrada independiente:

```text
input/universe_p1_50.csv
```

Esquema obligatorio:

```text
ticker
company
country
security_type
sector
industry
market_cap_current
market_cap_currency
market_cap_as_of
market_cap_source
operating_business
reit
bdc
pre_revenue
```

## Regla crítica

No inventar valores de market cap.

No estimar market cap con conocimiento del modelo.

No codificar cifras actuales directamente en el código.

No añadir scraping opaco o una dependencia de datos de mercado sin documentarla.

Si `input/universe_p1_50.csv` no existe o no contiene datos verificables para 50 compañías, crear:

```text
input/universe_p1_50_TEMPLATE.csv
```

y devolver:

```text
BLOCKED_INPUT_REQUIRED
```

sin fingir que el experimento de universo se ha ejecutado.

El motor debe quedar preparado para ejecutarse en cuanto el archivo esté disponible.

---

# 6. Validación del archivo de universo

Antes de consultar SEC validar:

```text
ticker non-empty
country == US
security_type == common_stock
market_cap_current numeric
market_cap_currency == USD
market_cap_as_of non-empty
market_cap_source non-empty
boolean flags valid
```

Registrar errores de input como:

```text
invalid_universe_input
missing_market_cap
unsupported_currency
invalid_security_type
```

No corregir silenciosamente.

---

# 7. Elegibilidad previa SEC

Aplicar primero:

$$
500M
\le
Market\ Cap
\le
20B
$$

y exclusiones estructurales.

Crear:

```text
universe_preeligible = true/false
```

con:

```text
universe_exclusion_reason
```

Valores iniciales permitidos:

```text
market_cap_below_min
market_cap_above_max
not_common_stock
non_us
financial
reit
bdc
pre_revenue
not_operating_business
invalid_universe_input
```

No enviar a SEC compañías claramente no elegibles.

---

# 8. Ingresos > 100 M

Este criterio debe calcularse con SEC sobre el último FY fresco resuelto:

$$
Revenue_{latest\ FY}>100M
$$

No usar un ingreso actual de agregador para cerrar la elegibilidad.

Añadir:

```text
revenue_eligibility = true/false/unknown
```

Si SEC no permite resolver el último Revenue:

```text
revenue_eligibility = unknown
```

y:

```text
universe_eligible = unknown
```

No convertirlo en `false`.

---

# 9. Estado final de elegibilidad

Usar:

```text
universe_eligible = true
universe_eligible = false
universe_eligible = unknown
```

## true

Sólo si:

```text
preeligible = true
AND
latest FY Revenue > 100 M
AND
SEC reporting contract compatible
```

## false

Sólo cuando existe evidencia suficiente de incumplimiento de un criterio.

## unknown

Cuando falta información suficiente para decidir.

---

# 10. D2 sólo sobre elegibles

La tasa de señales principal se calcula únicamente sobre:

```text
fresh
AND
universe_eligible = true
```

Definir:

$$
Eligible\ Fresh\ Coverage
=
\frac{
Fresh\ Eligible\ Processable
}{
Universe\ Eligible
}
$$

y:

$$
D2\ Signal\ Rate
=
\frac{
D2\ Signals
}{
Fresh\ Eligible\ Processable
}
$$

No mezclar `unknown` con `false`.

---

# 11. Lote piloto

Objetivo:

```text
50 compañías
```

El lote debe buscar diversidad razonable entre:

```text
Technology
Industrials
Consumer
Health Care commercial
Energy
Materials
Communication Services
Transportation
Business Services
Defense
```

No es necesario imponer cuotas sectoriales exactas.

Pero evita un lote dominado por un único sector.

No incluir deliberadamente financieros, REIT o BDC como controles positivos salvo que estén marcados expresamente como control y fuera del denominador principal.

---

# 12. Controles

Incluir, si están presentes en el universo real y cumplen market cap:

```text
NVDA
ABNB
DE
GM
NKE
```

sólo como continuidad diagnóstica.

No forzar su inclusión si incumplen el rango de capitalización actual.

No modificar reglas para conservarlos.

---

# 13. Nueva versión

Incrementar:

```text
engine_version = 0.4
task = CODEX_TASK_04
```

No sobrescribir:

```text
v01
v02
v03
```

---

# 14. Salidas

Generar:

```text
P1_universe_v04.csv
D2_results_v04.csv
D2_provenance_v04.csv
D2_diagnostics_v04.md
CODEX_TASK_04_REPORT.md
```

---

# 15. `P1_universe_v04.csv`

Columnas mínimas:

```text
ticker
company
country
security_type
sector
industry
market_cap_current
market_cap_as_of
market_cap_source
operating_business
reit
bdc
pre_revenue
universe_preeligible
universe_exclusion_reason
revenue_latest_fy
revenue_eligibility
universe_eligible
```

---

# 16. `D2_results_v04.csv`

Conservar las columnas v0.3 y añadir o garantizar:

```text
engine_version
ticker
universe_preeligible
universe_exclusion_reason
revenue_eligibility
universe_eligible
status
latest_fy_resolution_status
freshness_status
revenue_growth_fy_yoy
operating_margin_fy_t
operating_margin_fy_t_minus_1
om_delta_pp
d2_signal
```

Regla:

```text
d2_signal
```

puede calcularse técnicamente sobre datos válidos, pero el reporte principal debe distinguir:

```text
raw_d2_signal
eligible_d2_signal
```

donde:

```text
eligible_d2_signal =
d2_signal == true
AND
universe_eligible == true
AND
freshness_status == fresh
```

---

# 17. Diagnóstico obligatorio

`D2_diagnostics_v04.md` debe informar:

```text
engine_version
task
as_of
N_input
N_valid_universe_rows
N_preeligible
N_universe_eligible
N_universe_unknown
N_fresh_eligible_processable
N_latest_fy_unresolved
N_ambiguous_revenue_tag
N_missing_operating_income
N_raw_D2_signals
N_eligible_D2_signals
```

y:

$$
Eligible\ Fresh\ Coverage
$$

$$
D2\ Signal\ Rate
$$

---

# 18. Gate técnico

Mantener el gate del extractor:

```text
fresh coverage >= 70%
```

y añadir un gate de universo:

```text
eligible_fresh_coverage >= 70%
```

No usar `D2 Signal Rate` como gate.

La tasa de señales es un resultado que estamos observando, no un criterio de aprobación.

---

# 19. Tabla de exclusiones

Añadir al diagnóstico:

```text
## Universe exclusions
```

con conteos por:

```text
market_cap_below_min
market_cap_above_max
not_common_stock
non_us
financial
reit
bdc
pre_revenue
not_operating_business
revenue_below_min
unknown
```

---

# 20. Tabla de señales

Añadir:

```text
## Eligible D2 signals
```

con:

```text
ticker
company
sector
market_cap_current
revenue_growth_fy_yoy
operating_margin_fy_t_minus_1
operating_margin_fy_t
om_delta_pp
```

No añadir:

- precio;
- múltiplos;
- target;
- recomendación;
- oportunidad de inversión.

---

# 21. Tests obligatorios

Añadir tests para:

1. market cap 499 M → false;
2. market cap 500 M → eligible por límite inferior;
3. market cap 20 B → eligible por límite superior;
4. market cap >20 B → false;
5. financial → false;
6. REIT → false;
7. BDC → false;
8. pre-revenue → false;
9. latest FY revenue <=100 M → false;
10. missing latest FY revenue → unknown;
11. fresh D2 signal + universe true → eligible_d2_signal true;
12. fresh D2 signal + universe unknown → eligible_d2_signal false;
13. stale/latest_fy_unresolved → eligible_d2_signal false;
14. previous v0.3 regression tests remain green.

Ejecutar:

```bash
pytest -q
```

antes del run.

---

# 22. No ajustar D2 todavía

Aunque la tasa de señales parezca alta o baja:

NO cambiar:

```text
10%
-2 pp
```

Esta tarea sólo mide:

- cobertura;
- elegibilidad;
- tasa de señal;
- incidencias.

La calibración de umbrales será una tarea posterior.

---

# 23. Criterio de cierre

## Caso A — input disponible

La tarea termina cuando:

```text
pytest = PASS
50 universe rows validated
universe eligibility computed
SEC run completed
eligible fresh coverage computed
D2 signal rate computed
v04 artifacts generated
```

## Caso B — input actual verificable no disponible

La tarea termina en:

```text
BLOCKED_INPUT_REQUIRED
```

después de:

- implementar toda la capa de universo;
- dejar tests verdes;
- generar `universe_p1_50_TEMPLATE.csv`;
- explicar exactamente qué columnas necesita el usuario;
- NO fabricar 50 compañías o market caps.

---

# 24. Informe final

`CODEX_TASK_04_REPORT.md` debe responder:

1. ¿Se pudo ejecutar el lote real de 50?
2. ¿Cuál fue la fuente del universo y fecha `as_of`?
3. ¿Cuántas compañías resultaron elegibles?
4. ¿Cuál fue `eligible_fresh_coverage`?
5. ¿Cuántas señales D2 elegibles aparecieron?
6. ¿Cuál fue `D2 Signal Rate`?
7. ¿Cuáles fueron las principales causas de exclusión o `unknown`?
8. ¿Se mantuvieron verdes todos los tests v0.3?
9. ¿Apareció algún defecto nuevo del contrato SEC?
10. ¿Debemos ampliar a 100 o corregir infraestructura antes?

Añadir SHA-256 de todos los artefactos v04.

---

# 25. Interpretación epistemológica

No concluir:

```text
D2 funciona
```

sólo porque existan señales.

El resultado de esta tarea debe formularse como:

```text
P1.D2 sobre un lote elegible de 50
→ cobertura observada
→ tasa de señal observada
→ incidencias
→ decisión sobre siguiente experimento
```

No convertir cribado en decisión de inversión.
