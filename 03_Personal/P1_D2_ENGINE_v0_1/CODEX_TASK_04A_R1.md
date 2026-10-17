# CODEX_TASK_04A_R1 — Rebalanceo del piloto P1 por capitalización

## Motivo

`CODEX_TASK_04A` fue ejecutado correctamente y produjo:

```text
READY_FOR_CODEX_TASK_04
preeligible_true = 1338
selected_50 = 50
sector_count = 11
largest_sector_count = 5
```

Sin embargo, la auditoría posterior ha identificado un sesgo de diseño en la selección de las 50 compañías.

La regla original:

```text
dentro de sector → market cap descendente
→ round-robin sectorial
```

favorece sistemáticamente compañías cercanas al límite superior de:

```text
500 M – 20 B USD
```

Esto es una fricción metodológica de la especificación original, no un defecto de Codex.

Para un primer piloto de robustez del motor D2 necesitamos cubrir deliberadamente el rango completo de capitalización.

Esta tarea modifica SOLO la selección de las 50 compañías.

NO modifica:

- fuente Nasdaq;
- normalización;
- criterios de pre-elegibilidad;
- SEC;
- D2;
- umbrales;
- ontología.

---

# 1. Invariante de fuente

Usar exactamente el mismo archivo fuente ya validado:

```text
nasdaq_screener_1791296955512.csv
```

y verificar que su SHA-256 sigue siendo:

```text
8e4dc6139f7dd7cdb6f9a326f6a9927c1d80529953b3ac35530f8cf5387a2c35
```

Si el hash cambia:

```text
BLOCKED_SOURCE_CHANGED
```

No sustituir la fuente.

---

# 2. Conservar la clasificación 04A

No recalcular con reglas distintas:

```text
security_type
operating_business
financial_sector
reit
bdc
pre_revenue
universe_preeligible
universe_exclusion_reason
```

La población de partida debe seguir siendo:

```text
universe_preeligible = true
```

según la lógica 04A ya probada.

Si al ejecutar el código actual la cifra deja de ser:

```text
1338
```

detenerse y explicar por qué.

---

# 3. Objetivo del rebalanceo

Construir un piloto de:

```text
50 compañías
```

con cobertura deliberada de todo el intervalo:

```text
500 M <= market cap <= 20 B USD
```

El piloto NO pretende reproducir la distribución poblacional.

Pretende ser un:

```text
stress-test sample
```

del motor anual SEC/D2 a través de distintos tamaños empresariales.

Por tanto:

```text
pilot signal rate
!=
population signal rate
```

Esta distinción debe aparecer en el diagnóstico.

---

# 4. Bandas de capitalización

Crear:

```text
market_cap_bucket
```

con estas cinco bandas:

```text
B1_0_5_1B   : 500 M <= cap < 1 B
B2_1_2B     : 1 B <= cap < 2 B
B3_2_5B     : 2 B <= cap < 5 B
B4_5_10B    : 5 B <= cap < 10 B
B5_10_20B   : 10 B <= cap <= 20 B
```

Objetivo:

```text
10 compañías por banda
```

para un total de:

```text
50
```

---

# 5. Si una banda no tiene 10 pre-elegibles

No fabricar compañías.

Registrar:

```text
bucket_shortfall
```

Redistribuir el déficit de forma determinista entre las bandas con exceso de candidatos, priorizando las bandas adyacentes.

Documentar cualquier redistribución.

Si ni siquiera así pueden obtenerse 50:

```text
BLOCKED_INSUFFICIENT_PREELIGIBLE_ROWS
```

---

# 6. Diversidad sectorial dentro de cada banda

Dentro de cada `market_cap_bucket`:

1. agrupar por `sector_normalized`;
2. aplicar round-robin entre sectores;
3. evitar que un solo sector domine la banda.

Objetivo global, si la población lo permite:

```text
minimum represented sectors = 8
maximum selected from one sector = 8
```

No son criterios económicos ni de inversión.

Son controles de diversidad del experimento.

---

# 7. No ordenar por market cap dentro del sector

Eliminar el criterio:

```text
market_cap descending
```

como selector interno.

Para evitar sesgo económico y mantener reproducibilidad, crear:

```text
selection_key
```

como:

```text
SHA256(source_sha256 + ":" + ticker)
```

Dentro de cada combinación:

```text
market_cap_bucket + sector_normalized
```

ordenar por:

```text
selection_key ascending
```

Después aplicar el round-robin.

Así:

```text
same source
→ same selection
```

sin favorecer empresas grandes, pequeñas, de mayor crecimiento o de mejor valoración.

---

# 8. Campo explícito de selección

El audit generado en 04A permite reconstruir la selección, pero no contiene un indicador explícito de pertenencia al piloto.

Añadir:

```text
selected_for_pilot
```

a TODAS las filas del audit.

Valores:

```text
true
false
```

Añadir también:

```text
selection_revision = 1
market_cap_bucket
selection_key
```

Esto debe permitir identificar directamente las 50 filas sin reconstruir el algoritmo.

---

# 9. Preservar la selección anterior

No borrar el piloto anterior.

Antes de escribir un nuevo archivo canónico:

1. conservar una copia del anterior como:

```text
input/universe_p1_50_v04A_topcap.csv
```

si todavía no existe;

2. verificar que coincide con el hash previo documentado:

```text
befc0cc06086662d9afab53cc3e2e9ddf9bb9be0308c3fd6a4123d607b352a94
```

Si no coincide, no sobrescribir nada y reportar:

```text
BLOCKED_PREVIOUS_SELECTION_MISMATCH
```

---

# 10. Nuevo output de selección

Generar:

```text
input/universe_p1_50.csv
```

como nueva selección balanceada.

Además guardar copia versionada:

```text
input/universe_p1_50_v04A_r1.csv
```

Ambos deben ser byte-identical.

---

# 11. Audit revisado

Generar:

```text
output/P1_universe_audit_v04A_r1.csv
```

con las 7017 filas y, además de los campos anteriores:

```text
market_cap_bucket
selection_key
selected_for_pilot
selection_revision
```

Debe cumplirse:

```text
selected_for_pilot = true
```

exactamente 50 veces.

---

# 12. Diagnóstico revisado

Generar:

```text
output/P1_universe_diagnostics_v04A_r1.md
```

Debe incluir:

```text
source_rows
preeligible_true
selected_50
selection_revision
```

## Market-cap distribution of selected 50

Informar:

```text
min
p10
p25
median
p75
p90
max
mean
```

## Market-cap bucket distribution

Tabla:

```text
bucket | selected count | preeligible population
```

## Sector distribution

Tabla:

```text
sector | count
```

## Cross-distribution

Tabla:

```text
market_cap_bucket x sector
```

---

# 13. Comparación con selección anterior

Añadir:

```text
## Previous vs rebalanced pilot
```

con:

```text
metric
old_selection
new_selection
```

Como mínimo:

```text
min market cap
median market cap
p75 market cap
max market cap
number of sectors
largest sector count
```

No calcular rendimiento, crecimiento o calidad.

---

# 14. Controles de límites

El nuevo piloto debe contener, si existe población suficiente:

```text
10 compañías B1
10 compañías B2
10 compañías B3
10 compañías B4
10 compañías B5
```

Debe verificar:

```text
min market cap >= 500 M
max market cap <= 20 B
```

y ninguna seleccionada:

```text
universe_preeligible != true
```

---

# 15. Tests obligatorios

Mantener todos los tests anteriores y añadir:

1. clasificación correcta de 500 M;
2. clasificación correcta de 999,999,999;
3. clasificación correcta de 1 B;
4. clasificación correcta de 2 B;
5. clasificación correcta de 5 B;
6. clasificación correcta de 10 B;
7. clasificación correcta de 20 B;
8. 10 seleccionadas por banda cuando existe oferta suficiente;
9. exactamente 50 `selected_for_pilot=true`;
10. mismo input → mismos 50 tickers;
11. cambio de orden de filas del input → mismos 50 tickers;
12. ninguna seleccionada fuera de rango;
13. ninguna seleccionada con preeligible != true;
14. hash-based selection no depende de market-cap ordering;
15. todos los tests 04A y v0.3 siguen verdes.

Ejecutar:

```bash
pytest -q
```

---

# 16. No ejecutar SEC ni D2

NO ejecutar:

```text
companyfacts
run_d2
CODEX_TASK_04
```

La tarea termina antes.

---

# 17. Informe

Generar:

```text
CODEX_TASK_04A_R1_REPORT.md
```

Debe responder:

1. ¿Se preservó exactamente la fuente original?
2. ¿Se preservó la clasificación preeligible de 1338 filas?
3. ¿Se conservaron las 50 anteriores?
4. ¿Se generaron 50 nuevas compañías?
5. ¿Cuántas quedaron en cada banda de market cap?
6. ¿Cuál es la mediana de market cap de la nueva selección?
7. ¿Cuántos sectores están representados?
8. ¿Cuál es el mayor peso sectorial?
9. ¿Hubo que redistribuir déficit entre bandas?
10. ¿Todos los tests pasaron?
11. ¿Está el piloto listo para CODEX_TASK_04?

Añadir SHA-256 de:

```text
input/universe_p1_50.csv
input/universe_p1_50_v04A_r1.csv
output/P1_universe_audit_v04A_r1.csv
output/P1_universe_diagnostics_v04A_r1.md
```

---

# 18. Criterio de cierre

Éxito sólo si:

```text
pytest = PASS
source hash unchanged
preeligible population unchanged
50 selected
full market-cap range represented
selected_for_pilot explicit
old pilot preserved
new artifacts hashed
```

Terminar con:

```text
READY_FOR_CODEX_TASK_04
```

---

# 19. Interpretación epistemológica

El objetivo de este piloto es testar infraestructura.

No estimar todavía la prevalencia poblacional real de D2.

Por tanto:

$$
\text{D2 Signal Rate}_{pilot}
\neq
\text{D2 Signal Rate}_{universe}
$$

La tasa obtenida en TASK_04 deberá denominarse explícitamente:

```text
pilot_d2_signal_rate
```

hasta que diseñemos una muestra representativa o ejecutemos el universo completo.
