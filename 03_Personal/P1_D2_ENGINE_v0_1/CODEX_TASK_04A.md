# CODEX_TASK_04A — Construcción verificable del universo P1 de 50 compañías

## Contexto

`CODEX_TASK_04` se detuvo correctamente porque no existía todavía un universo verificable de 50 compañías con datos actuales suficientes.

El usuario ha guardado en la misma carpeta donde están los `CODEX_TASK_*` un archivo cuyo nombre comienza por:

```text
nasdaq_screener_1791296955512
```

Puede tener extensión `.csv` u otra extensión reconocible.

Esta tarea NO ejecuta todavía D2.

Su única función es construir:

```text
input/universe_p1_50.csv
```

de forma reproducible, trazable y sin inventar datos.

---

# 1. Objetivo

Transformar el archivo bruto Nasdaq en un universo P1 de:

```text
50 compañías
```

que cumplan, hasta donde permitan los datos disponibles:

```text
country = US
security_type = common_stock
operating_business = true
financial_sector = false
reit = false
bdc = false
pre_revenue = false
500 M <= market_cap_current <= 20 B USD
```

El criterio:

```text
Revenue latest FY > 100 M
```

NO se cierra en esta tarea.

Ese criterio se validará después con SEC dentro de `CODEX_TASK_04`.

Por tanto:

```text
TASK_04A = elegibilidad previa por datos actuales
TASK_04  = elegibilidad final + SEC + D2
```

---

# 2. Localizar el archivo fuente

Desde la raíz del repo, localizar:

```bash
find .. -maxdepth 2 -type f -name 'nasdaq_screener_1791296955512*' -print
```

Debe existir exactamente un archivo fuente plausible.

Si aparecen varios, no elegir arbitrariamente.

Registrar todos y detenerse con:

```text
BLOCKED_AMBIGUOUS_SOURCE_FILE
```

Si no aparece ninguno:

```text
BLOCKED_SOURCE_FILE_NOT_FOUND
```

No descargar otro screener ni sustituir la fuente.

---

# 3. No modificar el archivo fuente

El archivo Nasdaq es input bruto e inmutable.

No:

- sobrescribirlo;
- renombrarlo destructivamente;
- editar filas;
- cambiar valores.

Si hace falta una copia normalizada:

```text
input/nasdaq_screener_raw.csv
```

crear una copia, preservando el original.

Registrar:

```text
source_filename
source_sha256
source_modified_at
```

---

# 4. Inspección inicial obligatoria

Antes de filtrar:

1. detectar delimitador;
2. detectar encoding;
3. listar columnas;
4. contar filas;
5. mostrar 5 filas de ejemplo;
6. identificar columnas candidatas para:

```text
symbol / ticker
company name
market cap
country
sector
industry
exchange
```

No asumir nombres de columnas.

Generar:

```text
output/NASDAQ_SOURCE_PROFILE.md
```

con:

```text
source file
sha256
row count
column names
detected mapping
missing required fields
```

---

# 5. Mapping de columnas

Crear una capa explícita de mapping.

Como mínimo intentar resolver:

```text
ticker
company
market_cap_current
sector
industry
country
exchange
```

Si el archivo no contiene `country`, no inventarlo.

Puede derivarse `country = US` sólo si la propia fuente/documentación del archivo demuestra que el universo descargado está restringido a acciones estadounidenses.

Si no puede demostrarse:

```text
country = unknown
```

y documentarlo.

Si `industry` falta:

```text
industry = unknown
```

No inferirla desde el nombre de la compañía.

---

# 6. Normalización de market cap

La columna de capitalización puede venir como:

```text
1234567890
1.23B
850M
$1.2B
```

Normalizar a:

```text
market_cap_current
```

numérico USD.

Conservar también:

```text
market_cap_raw
```

No aceptar valores no parseables silenciosamente.

Estado:

```text
invalid_market_cap
```

---

# 7. Fecha y procedencia de market cap

Añadir:

```text
market_cap_source = Nasdaq Stock Screener
market_cap_as_of
```

## `market_cap_as_of`

No inventar la fecha exacta si el archivo no la contiene.

Usar por prioridad:

1. fecha explícita del archivo;
2. timestamp verificable asociado al archivo o descarga;
3. fecha de modificación del archivo como proxy técnico, marcada como tal.

Si sólo existe proxy:

```text
market_cap_as_of_basis = file_modified_at_proxy
```

---

# 8. Tipo de instrumento

Intentar clasificar:

```text
security_type
```

Valores permitidos:

```text
common_stock
non_common_stock
unknown
```

Excluir si existe evidencia clara de:

- ETF;
- fund;
- preferred;
- warrant;
- right;
- unit;
- SPAC sin negocio operativo;
- shell.

No inferir por heurísticas frágiles del ticker sin documentarlo.

Si no existe información suficiente:

```text
security_type = unknown
```

y no considerar la fila elegible automáticamente.

---

# 9. Exclusiones sectoriales

## Financials

Si `sector` permite identificar claramente:

```text
Financials
Financial Services
Banks
Insurance
Capital Markets
```

marcar:

```text
financial_sector = true
```

Excluir.

No excluir únicamente porque una empresa tenga deuda o palabra "capital" en su nombre.

## REIT

Marcar `reit = true` sólo si la fuente ofrece sector/industria/denominación suficientemente clara para identificar REIT.

## BDC

Marcar `bdc = true` sólo con evidencia explícita suficiente.

## Pre-revenue

No intentar inferir `pre_revenue` a partir del precio o nombre.

Si el archivo contiene revenue u otra columna que permita identificar claramente revenue = 0:

```text
pre_revenue = true
```

Si no:

```text
pre_revenue = unknown
```

La ausencia de dato no equivale a `false`.

---

# 10. Operating business

Usar:

```text
operating_business = true/false/unknown
```

Marcar `false` sólo para:

- shell;
- SPAC no operativa;
- fondo;
- vehículo sin negocio operativo.

Si no hay evidencia:

```text
unknown
```

No convertir automáticamente todas las acciones en `true`.

---

# 11. Pre-elegibilidad

Definir:

```text
universe_preeligible
```

como:

```text
true
false
unknown
```

## true

Sólo si:

```text
market cap válido
500 M <= market cap <= 20 B
financial_sector != true
reit != true
bdc != true
pre_revenue != true
security_type == common_stock
operating_business == true
country == US
```

## false

Si incumple explícitamente al menos un criterio.

## unknown

Si no incumple ningún criterio pero falta información necesaria.

---

# 12. Razones de exclusión

Crear:

```text
universe_exclusion_reason
```

Puede contener múltiples razones separadas por `;`.

Valores normalizados:

```text
market_cap_below_min
market_cap_above_max
invalid_market_cap
financial
reit
bdc
pre_revenue
not_common_stock
security_type_unknown
not_operating_business
operating_business_unknown
non_us
country_unknown
```

No usar texto libre cuando exista código normalizado.

---

# 13. Objetivo: 50 compañías verdaderamente pre-elegibles

Construir el lote de 50 únicamente desde:

```text
universe_preeligible = true
```

No rellenar huecos con `unknown`.

Si existen menos de 50:

```text
BLOCKED_INSUFFICIENT_PREELIGIBLE_ROWS
```

y reportar cuántas existen.

---

# 14. Diversidad sectorial

Entre las compañías pre-elegibles, seleccionar 50 buscando diversidad razonable.

Sectores deseables, cuando existan:

```text
Technology
Industrials
Consumer Cyclical / Consumer Discretionary
Consumer Defensive / Staples
Health Care
Energy
Basic Materials / Materials
Communication Services
Transportation
Business Services
Defense / Aerospace
```

No imponer cuotas rígidas.

Pero aplicar estas reglas:

```text
max 12 compañías de un mismo sector
min 5 sectores representados si la fuente lo permite
```

Si la taxonomía Nasdaq usa otros nombres, mapear sólo lo necesario para medir concentración y conservar también el sector original.

---

# 15. Selección reproducible

No elegir "las que parezcan mejores".

La selección debe ser determinista.

Método recomendado:

1. ordenar pre-elegibles por `sector_normalized`;
2. dentro de sector ordenar por `market_cap_current` descendente;
3. seleccionar mediante round-robin sectorial hasta llegar a 50;
4. respetar máximo de 12 por sector.

Si el round-robin no permite 50:

- relajar sólo el máximo sectorial;
- documentar la relajación;
- no introducir criterio de calidad/inversión.

No usar:

- crecimiento;
- margen;
- valoración;
- precio;
- momentum;
- recomendación;
- popularidad.

---

# 16. Controles de continuidad

Comprobar si aparecen en el archivo fuente:

```text
NVDA
ABNB
DE
GM
NKE
```

Registrar para cada una:

```text
present_in_source
preeligible_status
exclusion_reason
market_cap_current
```

No forzar su entrada.

Es perfectamente válido que NVDA quede fuera por:

```text
market_cap_above_max
```

No cambiar el rango para conservar controles.

---

# 17. Output principal

Generar:

```text
input/universe_p1_50.csv
```

con exactamente 50 filas si es posible.

Columnas mínimas:

```text
ticker
company
country
security_type
sector
sector_normalized
industry
exchange
market_cap_raw
market_cap_current
market_cap_currency
market_cap_as_of
market_cap_as_of_basis
market_cap_source
operating_business
financial_sector
reit
bdc
pre_revenue
universe_preeligible
universe_exclusion_reason
source_filename
source_sha256
```

Para las 50 filas:

```text
universe_preeligible = true
```

---

# 18. Output de auditoría completo

Generar además:

```text
output/P1_universe_audit_v04A.csv
```

con TODAS las filas del archivo Nasdaq y su clasificación.

Debe permitir reconstruir:

```text
source
→ normalización
→ exclusión
→ selección
```

---

# 19. Diagnóstico

Generar:

```text
output/P1_universe_diagnostics_v04A.md
```

con:

```text
source_filename
source_sha256
source_rows
valid_market_cap_rows
preeligible_true
preeligible_false
preeligible_unknown
selected_50
sector_count
largest_sector_count
```

y:

```text
## Exclusion counts
```

por razón.

Añadir:

```text
## Sector distribution of selected 50
```

Añadir:

```text
## Continuity controls
```

para:

```text
NVDA
ABNB
DE
GM
NKE
```

---

# 20. Validaciones automáticas

Crear tests para:

1. 499,999,999 → below min;
2. 500,000,000 → pasa límite inferior;
3. 20,000,000,000 → pasa límite superior;
4. 20,000,000,001 → above max;
5. financial → false;
6. REIT → false;
7. BDC → false;
8. ETF/fund → not common stock;
9. unknown security type → unknown;
10. unknown country → unknown;
11. selección final contiene 50 filas;
12. ninguna fila seleccionada tiene `universe_preeligible != true`;
13. ningún sector supera 12 mientras exista alternativa válida;
14. selección determinista: mismo input → mismos 50 tickers.

Ejecutar:

```bash
pytest -q
```

---

# 21. No ejecutar D2

Esta tarea termina ANTES de SEC/D2.

No ejecutar:

```text
run_d2
companyfacts
D2 thresholds
```

No generar:

```text
D2_results_v04.csv
```

Eso pertenece a `CODEX_TASK_04`.

---

# 22. Versionado

Usar:

```text
task = CODEX_TASK_04A
universe_builder_version = 0.1
```

No cambiar `engine_version=0.3` del motor D2 porque no se toca aquí.

---

# 23. Informe

Generar:

```text
CODEX_TASK_04A_REPORT.md
```

Debe responder:

1. ¿Se encontró exactamente un archivo `nasdaq_screener_1791296955512*`?
2. ¿Cuántas filas contenía?
3. ¿Qué columnas reales contenía?
4. ¿Qué mappings se utilizaron?
5. ¿Cuántas filas quedaron `true / false / unknown`?
6. ¿Fue posible obtener 50 pre-elegibles?
7. ¿Qué distribución sectorial tienen?
8. ¿Qué pasó con NVDA, ABNB, DE, GM y NKE?
9. ¿Qué supuestos o proxies se utilizaron?
10. ¿Queda algún bloqueo antes de ejecutar `CODEX_TASK_04`?

Añadir SHA-256 de:

```text
input/universe_p1_50.csv
output/P1_universe_audit_v04A.csv
output/P1_universe_diagnostics_v04A.md
```

---

# 24. Criterio de cierre

## Éxito

```text
pytest = PASS
source profile generated
audit generated
50 preeligible companies selected
universe_p1_50.csv generated
diagnostics generated
report generated
```

Terminar con:

```text
READY_FOR_CODEX_TASK_04
```

## Bloqueo

Si no se pueden obtener 50 filas `universe_preeligible=true` sin inventar datos:

```text
BLOCKED_INSUFFICIENT_PREELIGIBLE_ROWS
```

Si faltan campos estructurales esenciales para determinar `true`:

```text
BLOCKED_SOURCE_SCHEMA_INSUFFICIENT
```

No rellenar manualmente para evitar el bloqueo.

---

# 25. Principio epistemológico

Esta tarea sólo construye el universo de investigación.

$$
\text{inclusión en universo}
\neq
\text{calidad de compañía}
\neq
\text{oportunidad de inversión}
$$

La selección de los 50 debe ser mecánica y reproducible, no una recomendación.
