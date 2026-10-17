---
content_id: algoritmo-p1-d2-anual
title: "P1.D2 — Algoritmo anual"
version: 0.1
document_type: algorithm_specification
status: proposed
language: es
effective_date: 2026-10-05
canonical_project: "Investigando mercados"
---

# P1.D2 — Algoritmo anual v0.1

# 1. Secuencia

```text
ticker
→ resolver CIK
→ descargar companyfacts
→ localizar revenue
→ localizar OperatingIncomeLoss
→ seleccionar FY t y FY t-1
→ validar comparabilidad
→ calcular crecimiento
→ calcular márgenes
→ aplicar reglas
→ producir estado
```

# 2. Cálculos

$$
g_R=\frac{R_t}{R_{t-1}}-1
$$

$$
OM_t=\frac{OI_t}{R_t}
$$

$$
OM_{t-1}=\frac{OI_{t-1}}{R_{t-1}}
$$

$$
\Delta OM_{pp}=100(OM_t-OM_{t-1})
$$

# 3. Condición D2

```text
g_R >= 0.10
AND
delta_om_pp <= -2.0
```

# 4. Señal fuerte provisional

```text
revenue_growth >= 20%
delta_om_pp <= -3
```

# 5. Exclusiones automáticas

```text
missing_data
ambiguous_revenue_tag
non_consecutive_fy
duration_mismatch
non_us_gaap
excluded_form
```

# 6. Métrica técnica

$$
Cobertura\ útil
=
\frac{compañías\ procesables}{compañías\ de\ entrada}
$$

Antes de juzgar D2:

```text
cobertura útil >= 70%
```

# 7. Primer lote

```text
50 compañías
```

No ampliar hasta conocer:

- resolución de ingresos;
- resolución de `OperatingIncomeLoss`;
- comparabilidad de FY;
- señales D2.
