# CODEX_TASK_04A_R2 — Corrección de estructuras jurídicas antes de TASK_04

## Motivo

`CODEX_TASK_04A_R1` fue ejecutado correctamente:

```text
source hash unchanged
50 selected
10 companies per market-cap bucket
11 sectors represented
pytest PASS
```

Sin embargo, la auditoría de las 50 seleccionadas ha detectado falsos positivos estructurales que incumplen el universo P1 antes de SEC/D2.

Casos observados en la selección R1:

```text
PDM → Piedmont Realty Trust Inc. Class A Common Stock
SBR → Sabine Royalty Trust Common Stock
```

Verificación externa/primaria posterior confirma:

```text
PDM = REIT
SBR = royalty trust, not an operating common-stock company
```

Además, dentro de la población `preeligible=true` aparecen otros casos equivalentes:

```text
PBT → Permian Basin Royalty Trust
IEP → Icahn Enterprises L.P.
SPH → Suburban Propane Partners L.P.
```

El defecto no está en el balanceo R1.

Está en la clasificación estructural previa.

Esta tarea corrige SOLO esa capa.

NO ejecutar SEC.
NO ejecutar D2.
NO modificar el rango de market cap.
NO modificar las bandas R1.
NO cambiar el método de selección hash + round-robin.

---

# 1. Fuente inmutable

Usar exactamente:

```text
nasdaq_screener_1791296955512.csv
```

y exigir:

```text
SHA-256 =
8e4dc6139f7dd7cdb6f9a326f6a9927c1d80529953b3ac35530f8cf5387a2c35
```

Si cambia:

```text
BLOCKED_SOURCE_CHANGED
```

---

# 2. Preservar R1

No sobrescribir:

```text
input/universe_p1_50_v04A_r1.csv
output/P1_universe_audit_v04A_r1.csv
output/P1_universe_diagnostics_v04A_r1.md
CODEX_TASK_04A_R1_REPORT.md
```

Verificar que:

```text
input/universe_p1_50_v04A_r1.csv
```

mantiene SHA-256:

```text
fd876e7e54a91d74ffdf866e8317e9991b2c95c17f170a1a37ad2b6596a4ed90
```

Si no:

```text
BLOCKED_PREVIOUS_SELECTION_MISMATCH
```

---

# 3. Objetivo

Mejorar la clasificación de estructuras jurídicas usando exclusivamente evidencia explícita y de alta confianza disponible en:

```text
Name
Sector
Industry
```

No inferir modelos de negocio complejos.

No investigar compañías individualmente salvo para tests/fixtures locales.

La regla debe ser general y reproducible.

---

# 4. Nuevo campo

Añadir:

```text
entity_structure
```

Valores iniciales:

```text
corporation
limited_partnership
royalty_trust
reit
other_trust
unknown
```

No convertir `unknown` en `corporation` por defecto.

---

# 5. Royalty trusts

Si `Name` contiene explícitamente:

```text
Royalty Trust
```

clasificar:

```text
entity_structure = royalty_trust
security_type = non_common_stock
operating_business = false
universe_preeligible = false
```

Razones:

```text
not_common_stock;not_operating_business
```

No confiar en que Nasdaq escriba `Common Stock` al final del nombre.

Casos de regresión obligatorios:

```text
SBR
PBT
```

Ambos deben quedar fuera.

---

# 6. REIT

Clasificar:

```text
entity_structure = reit
reit = true
universe_preeligible = false
```

cuando exista evidencia explícita de alta confianza.

Regla mínima obligatoria:

```text
Name contains "Realty Trust"
AND
Sector == Real Estate
```

También admitir:

```text
Name contains "Real Estate Investment Trust"
```

si aparece.

No marcar `reit=true` sólo porque:

```text
Sector == Real Estate
```

Casos de regresión:

```text
PDM → reit=true → preeligible=false
```

No excluir automáticamente:

```text
LAUR
PXED
```

sólo por aparecer bajo `Real Estate`.

---

# 7. Limited partnerships

Si el nombre legal contiene como entidad:

```text
L.P.
LP
Limited Partnership
```

mediante una expresión con límites robustos que no capture letras dentro de palabras:

```text
entity_structure = limited_partnership
security_type = non_common_stock
universe_preeligible = false
```

Razón:

```text
not_common_stock
```

El hecho de que Nasdaq añada `Common Stock` no prevalece sobre una forma jurídica explícita de partnership.

Casos de regresión:

```text
IEP → false
SPH → false
```

Evitar falsos positivos como palabras que simplemente contienen las letras `lp`.

---

# 8. Corporations

Sólo usar:

```text
entity_structure = corporation
```

cuando el nombre y la clasificación vigente sean compatibles con:

```text
security_type = common_stock
```

y no haya evidencia explícita de:

```text
trust
limited partnership
fund
SPAC/shell
```

No es necesario perfeccionar toda la ontología societaria en esta tarea.

---

# 9. Recalcular población pre-elegible

Aplicar primero toda la lógica 04A existente.

Después aplicar las nuevas reglas de estructura.

Registrar:

```text
preeligible_before_entity_fix
preeligible_after_entity_fix
entity_structure_exclusions
```

No asumir ni hardcodear el nuevo total.

Pero el informe debe explicar expresamente qué ocurrió con:

```text
PDM
SBR
PBT
IEP
SPH
```

---

# 10. Reselección del piloto

Después de corregir la población:

mantener EXACTAMENTE el método R1:

```text
B1 0.5–1B  → target 10
B2 1–2B    → target 10
B3 2–5B    → target 10
B4 5–10B   → target 10
B5 10–20B  → target 10
```

Dentro de cada bucket:

```text
sector round-robin
```

y:

```text
selection_key =
SHA256(source_sha256 + ":" + ticker)
```

No introducir nuevos criterios.

---

# 11. Nueva selección

Generar:

```text
input/universe_p1_50_v04A_r2.csv
```

y actualizar:

```text
input/universe_p1_50.csv
```

para que sea byte-identical al R2.

No borrar R1.

---

# 12. Audit R2

Generar:

```text
output/P1_universe_audit_v04A_r2.csv
```

con todas las filas y, como mínimo:

```text
entity_structure
market_cap_bucket
selection_key
selected_for_pilot
selection_revision = 2
```

---

# 13. Diagnóstico R2

Generar:

```text
output/P1_universe_diagnostics_v04A_r2.md
```

Debe incluir:

```text
source_rows
preeligible_before_entity_fix
entity_structure_exclusions
preeligible_after_entity_fix
selected_50
bucket_shortfall
sector_max_relaxed
```

## Entity structure exclusions

Tabla:

```text
entity_structure | count
```

## Known regression cases

Tabla:

```text
ticker
company
entity_structure
security_type
reit
operating_business
universe_preeligible
exclusion_reason
```

para:

```text
PDM
SBR
PBT
IEP
SPH
```

## Selected legal-structure check

Confirmar que ninguna de las 50 contiene:

```text
entity_structure in:
- limited_partnership
- royalty_trust
- reit
- other_trust
```

---

# 14. Revisión de la nueva muestra

Mantener las métricas R1:

```text
market-cap distribution
bucket distribution
sector distribution
cross-distribution
```

Añadir comparación:

```text
R1 vs R2
```

con:

```text
number of replaced tickers
R1-only tickers
R2-only tickers
```

---

# 15. Tests obligatorios

Mantener todos los tests anteriores.

Añadir:

1. `Sabine Royalty Trust Common Stock` → royalty_trust;
2. `Permian Basin Royalty Trust Common Stock` → royalty_trust;
3. `Piedmont Realty Trust Inc. ...` + Real Estate → reit;
4. empresa ordinaria en Real Estate sin `Realty Trust` → no REIT por esta regla;
5. `Icahn Enterprises L.P. Common Stock` → limited_partnership;
6. `Suburban Propane Partners L.P. Common Stock` → limited_partnership;
7. texto con letras `lp` dentro de una palabra → no limited_partnership;
8. ninguna de PDM/SBR/PBT/IEP/SPH queda preeligible;
9. exactamente 50 seleccionadas;
10. 10 por bucket si sigue existiendo oferta suficiente;
11. ninguna seleccionada tiene estructura jurídica excluida;
12. selección determinista;
13. todos los tests v0.3, 04A y R1 siguen verdes.

Ejecutar:

```bash
pytest -q
```

---

# 16. No ejecutar SEC/D2

No ejecutar:

```text
companyfacts
run_d2
CODEX_TASK_04
```

Esta tarea sigue siendo únicamente de construcción del universo.

---

# 17. Informe final

Generar:

```text
CODEX_TASK_04A_R2_REPORT.md
```

Debe responder:

1. ¿Se preservó la fuente original?
2. ¿Se preservó R1?
3. ¿Cuántos falsos positivos estructurales fueron eliminados?
4. ¿Qué pasó con PDM, SBR, PBT, IEP y SPH?
5. ¿Cuántas filas quedaron pre-elegibles después de la corrección?
6. ¿Se obtuvieron de nuevo 50 compañías?
7. ¿Se mantienen 10 por banda?
8. ¿Cuántos tickers cambiaron respecto de R1?
9. ¿Todos los tests pasaron?
10. ¿Existe algún bloqueo real antes de `CODEX_TASK_04`?

Añadir SHA-256 de:

```text
input/universe_p1_50.csv
input/universe_p1_50_v04A_r2.csv
output/P1_universe_audit_v04A_r2.csv
output/P1_universe_diagnostics_v04A_r2.md
```

---

# 18. Criterio de cierre

Éxito sólo si:

```text
source unchanged
R1 preserved
known structural false positives excluded
pytest PASS
50 selected
10 per market-cap bucket
no excluded entity structures in selected 50
artifacts hashed
```

Terminar con:

```text
READY_FOR_CODEX_TASK_04
```

---

# 19. Límite metodológico

Esta corrección no pretende construir un clasificador jurídico universal.

Sólo formaliza exclusiones de alta confianza observadas empíricamente.

El principio sigue siendo:

```text
unknown
!=
eligible
```

y:

```text
Nasdaq label
!=
legal/economic entity type
```
