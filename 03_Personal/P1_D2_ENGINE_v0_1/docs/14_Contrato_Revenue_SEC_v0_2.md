# P1.D2 — Contrato de Revenue SEC v0.2

## Alcance

Este contrato cambia únicamente la identificación del numerador anual Revenue y el diagnóstico de cobertura previa a D2. Conserva US-GAAP, USD, `10-K`/`10-K/A`, `fp=FY`, latest-FY, dos ejercicios consecutivos y el cálculo D2 v0.3. No usa 10-Q, TTM ni reconstrucciones trimestrales.

## Tags estándar candidatos

| Tag | Decisión | Semántica y condición |
|---|---|---|
| `RevenueFromContractWithCustomerExcludingAssessedTax` | Aceptado condicionalmente | Total consolidado de contratos con clientes sólo cuando no haya ingresos materiales fuera de Topic 606. Si existen, es subtotal. |
| `RevenueFromContractWithCustomerIncludingAssessedTax` | Aceptado condicionalmente | Total consolidado de contratos con clientes con impuestos incluidos; validar con ventas/ingresos del estado primario. |
| `Revenues` | Aceptado condicionalmente | Puede ser total de ingresos operativos, pero se rechaza o deja ambiguo si agrega partidas no operativas materiales o “other income”. |
| `SalesRevenueNet` | Aceptado condicionalmente | Ventas netas consolidadas; validar que no sea solo una clase de producto/segmento. |
| `RevenueNotFromContractWithCustomer` | Rechazado como total | Componente fuera de contratos Topic 606; puede reconciliarse con el total, nunca sustituirlo por sí solo. |
| Conceptos de segmento/producto/geografía | Rechazados | No son consolidados aunque contengan “revenue” o “sales”. |
| Conceptos de derivative gain/loss, fair value u other income | Rechazados como Revenue | Partidas no operativas o económicamente distintas no se incorporan al numerador. |
| Tags custom | Rechazados por defecto | Sólo se aceptan por filing si taxonomy, definición, accession y valor del estado consolidado se validan exactamente. Registrar `resolved_validated_custom_total` / `validated_custom_total`. |

## Regla de total y componentes

1. Sólo se consideran observaciones de duración anual aceptada, `10-K`/`10-K/A`, `fp=FY`, con unidad y período preservados.
2. El concepto seleccionado debe ser consolidado y reconciliar con el estado de resultados primario del mismo filing.
3. Un subtotal Topic 606 no sustituye ingresos consolidados cuando hay ingresos materiales no-Topic-606.
4. Si un total estándar y un concepto de contratos difieren, sólo se reconcilian automáticamente cuando CompanyFacts identifica el componente no-Topic-606 y la suma iguala el total dentro de 0,5%.
5. Utilities: el ingreso operativo total puede incluir tarifas/regulación u otros ingresos operativos además de contratos con clientes. Se conserva el total del estado si las diferencias no son partidas no operativas materiales; si no se prueba, no se elige por orden fijo.
6. Extractivas: ventas de producción, marketing/brokered sales, derivative gains y “other income” no son intercambiables. Si el renglón agregado incluye partidas no operativas materiales y no hay total operativo reconciliable, usar `ambiguous_components`.
7. Si dos conceptos totales del mismo período difieren y la semántica no determina su relación, usar `ambiguous_components` o `unresolved`; no priorizar por nombre.

## Estados y provenance

Estados: `resolved_standard_total`, `resolved_validated_custom_total`, `resolved_semantic_reconciliation`, `ambiguous_components`, `no_revenue`, `context_mismatch`, `unresolved`.

Cada observación usada conserva taxonomy, tag, unidad, inicio/fin, valor, form, fecha de presentación, accession, FY y FP. Cada diagnóstico enlaza el filing SEC y registra etiqueta/valor primario cuando se pudo reconciliar. No se sintetizan valores ni se reparan manualmente facts dentro de D2.

## Fallback prohibidos

- No escoger automáticamente `RevenueFromContract...` frente a `Revenues` ni viceversa.
- No sumar ingresos de segmentos, ni inventar un total a partir de etiquetas no relacionadas.
- No usar un valor de un FY anterior si falta Revenue en latest FY.
- No aceptar un custom tag por su nombre o por una allowlist global.
- No sustituir ausencia de evidencia por cero; `no_revenue` requiere evidencia primaria explícita.
- No ampliar tags para alcanzar una métrica de cobertura objetivo.

## Decisiones revisadas para el piloto v0.4

Los casos y referencias por filing quedan en `input/revenue_evidence_v05A.csv` y `output/Revenue_unknown_diagnostics_v05A.csv`. AAON, BV, IDT, LFUS y MATW validan un total estándar alternativo con impuestos incluidos. EVRG requiere el total de ingresos operativos y RRC conserva ambigüedad al diferir el total de “revenues and other income” del revenue por contratos con componentes materiales ajenos a éste. WEX reconcilia Revenue de contratos más Revenue no procedente de contratos con el total `Revenues`. Los casos pre-revenue y de contexto/filling no se resuelven por similitud de etiqueta.