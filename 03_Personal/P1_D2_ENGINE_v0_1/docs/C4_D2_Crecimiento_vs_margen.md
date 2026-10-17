---
content_id: criterio-c4-d2-crecimiento-vs-margen
title: "C4.D2 — Crecimiento vs margen"
short_title: "D2 Crecimiento vs margen"
version: 0.1
document_type: screening_subspecification
status: proposed
language: es
effective_date: 2026-10-04
canonical_project: "Investigando mercados"
parent_specification: "[[C4_Dislocacion_fundamental]]"
taxonomy_ref: "[[02_Taxonomia_cribado#C4 — Cribado de dislocación fundamental]]"
depends_on:
  - "[[C4_Dislocacion_fundamental]]"
  - "[[05_P1_Definicion_universo_C4]]"
validation_ref: "[[05_Pruebas_estres_cribado]]"
purpose:
  - "detectar crecimiento de ingresos acompañado por contracción material del margen operativo"
  - "generar hipótesis causales y candidatos de investigación"
---

# C4.D2 — Crecimiento vs margen v0.1

> [!important]
> Los umbrales de esta versión son **semillas de calibración**.
>
> No son reglas canónicas ni criterios de inversión.

# 1. Pregunta

> **¿Qué compañías están aumentando ingresos mientras su rentabilidad operativa se deteriora de forma material?**

La señal conceptual es:

$$
Revenue\ Growth > 0
$$

simultáneamente con:

$$
\Delta Operating\ Margin < 0
$$

La señal no determina si el fenómeno es favorable o adverso.

# 2. Hipótesis rivales

## H1 — Reinversión deliberada
La empresa sacrifica margen presente para capturar crecimiento futuro.

## H2 — Mix adverso
El crecimiento procede de productos, clientes o geografías menos rentables.

## H3 — Presión competitiva
El crecimiento se obtiene mediante menor precio, promociones o mayor gasto comercial.

## H4 — Coste transitorio
El margen se contrae por inflación, ramp-up, capacidad, integración o lanzamiento.

## H5 — Deterioro estructural
El modelo no presenta el apalancamiento operativo esperado.

# 3. Señal primaria de descubrimiento

Para P1 se propone:

$$
Revenue\ Growth_{TTM\ YoY}
\ge
10\%
$$

y:

$$
Operating\ Margin_{TTM}
-
Operating\ Margin_{FY}
\le
-2\ puntos\ porcentuales
$$

Interpretación:

- crecimiento suficientemente visible;
- margen TTM materialmente inferior al último FY;
- sólo señal de descubrimiento.

# 4. Señal fuerte provisional

Marcar como `high_magnitude` si:

$$
Revenue\ Growth_{TTM\ YoY}
\ge
20\%
$$

y:

$$
Operating\ Margin_{TTM}
-
Operating\ Margin_{FY}
\le
-3\ puntos\ porcentuales
$$

# 5. Razón de los umbrales

No se afirma que 10 %, 20 %, 2 pp o 3 pp tengan validez económica universal.

Se utilizan porque:

- excluyen variaciones pequeñas;
- permiten obtener un conjunto manejable;
- son fáciles de reproducir;
- pueden falsarse rápidamente.

$$
\text{umbral inicial}
\rightarrow
\text{prueba}
\rightarrow
\text{calibración}
$$

# 6. Limitación temporal

Comparar TTM con FY tiene solapamiento temporal.

Por tanto:

$$
Operating\ Margin_{TTM}
<
Operating\ Margin_{FY}
$$

es una **preseñal**, no evidencia suficiente de deterioro.

Toda compañía detectada debe confirmarse mediante períodos comparables.

# 7. Confirmación mínima

La señal D2 sólo pasa a `confirmed_screening_signal` si una segunda revisión muestra uno de estos patrones:

## Patrón A — trimestral interanual

$$
Revenue\ Growth_{FQ\ YoY}
>0
$$

y:

$$
Operating\ Margin_{FQ,t}
<
Operating\ Margin_{FQ,t-4}
$$

## Patrón B — TTM interanual reconstruido

$$
Revenue_{TTM,t}
>
Revenue_{TTM,t-4}
$$

y:

$$
Operating\ Margin_{TTM,t}
<
Operating\ Margin_{TTM,t-4}
$$

## Patrón C — tendencia multianual

Crecimiento de ingresos persistente con contracción de margen durante dos o más ejercicios.

# 8. Criterio de descarte rápido

Clasificar como `discard` si la aparente dislocación se explica claramente por:

- adquisición;
- desinversión;
- cambio de perímetro;
- reestructuración puntual;
- deterioro contable no operativo;
- cambio relevante de reconocimiento;
- estacionalidad evidente;
- comparación temporal no homogénea.

# 9. Variables auxiliares

Para explicar D2:

- Gross Margin;
- SG&A / Revenue;
- R&D / Revenue;
- EBITDA Margin;
- price / volume / mix;
- headcount;
- utilization;
- acquisition contribution;
- restructuring charges.

# 10. Salida mínima

```yaml
d2_signal:
  revenue_growth_ttm_yoy:
  operating_margin_ttm:
  operating_margin_fy:
  preliminary_margin_delta_pp:
  preliminary_signal:
  comparable_period_confirmed:
  confirmed_margin_delta_pp:
  magnitude:
  persistence:
  primary_hypothesis:
  alternative_hypothesis:
  evidence_needed: []
  triage_state:
```

# 11. Estados

```text
no_signal
preliminary_signal
confirmed_screening_signal
discard
```

# 12. Éxito metodológico

D2 funciona si:

- reduce el universo;
- genera casos causalmente interesantes;
- la mayoría de preseñales pueden confirmarse o descartarse con rapidez;
- no depende de una única plataforma;
- distingue reinversión de deterioro en la fase de investigación.

D2 falla si:

- produce demasiado ruido;
- FY vs TTM genera falsos positivos masivos;
- selecciona sistemáticamente sólo empresas estacionales;
- requiere tanto trabajo manual que deja de ser cribado.

# Addendum v0.1.8 — implementación inicial anual

P1.D2 se restringe inicialmente a dos ejercicios fiscales completos consecutivos.

$$
Revenue\ Growth_{FY}
=
\frac{Revenue_t}{Revenue_{t-1}}-1
$$

$$
\Delta OM_{pp}
=
100
\left(
\frac{OI_t}{Revenue_t}
-
\frac{OI_{t-1}}{Revenue_{t-1}}
\right)
$$

La comparación TTM vs FY queda retirada de P1.

La versión trimestral se pospone hasta validar el contrato SEC anual.
