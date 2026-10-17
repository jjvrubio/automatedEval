---
content_id: contrato-datos-sec-d2
title: "P1.D2 — Contrato de datos SEC EDGAR"
version: 0.1
document_type: data_contract
status: proposed
language: es
effective_date: 2026-10-05
canonical_project: "Investigando mercados"
---

# P1.D2 — Contrato de datos SEC EDGAR v0.1

# 1. Fuente

```text
https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
```

Ticker ↔ CIK:

```text
https://www.sec.gov/files/company_tickers.json
```

La API SEC no requiere API key.

# 2. Alcance inicial

```text
taxonomy: us-gaap
forms:
  - 10-K
  - 10-K/A
period: FY
unit: USD
```

Se excluyen inicialmente:

```text
20-F
40-F
IFRS
custom-only concepts
```

La exclusión busca reducir heterogeneidad durante la primera prueba.

# 3. Ingresos

Tags candidatos:

```text
RevenueFromContractWithCustomerExcludingAssessedTax
Revenues
SalesRevenueNet
```

Regla:

1. identificar el tag consolidado usado de forma consistente;
2. conservar el tag elegido;
3. si dos tags plausibles arrojan valores diferentes para el mismo período:

```text
ambiguous_revenue_tag
```

y excluir hasta reconciliación.

# 4. Resultado operativo

Tag preferido:

```text
OperatingIncomeLoss
```

Si no existe un hecho US-GAAP comparable:

```text
missing_operating_income
```

No reconstruir EBIT sintéticamente en P1.D2 v0.1.

# 5. Selección de período

Exigir:

```text
form ∈ {10-K, 10-K/A}
fp = FY
unit = USD
```

Los dos ejercicios deben ser consecutivos.

# 6. Duplicados

`companyfacts` puede contener varias observaciones del mismo período.

Para un mismo:

```text
concept
start
end
unit
```

se conserva la observación más recientemente presentada que represente el mismo período, preservando:

```text
filed
accession
form
```

# 7. Comparabilidad

No comparar si:

- la duración de los ejercicios difiere materialmente;
- existe cambio de moneda;
- cambia el tag con semántica no reconciliada;
- una cifra es consolidada y otra no;
- existe ambigüedad de período.

# 8. Duración

Control inicial:

```text
330–400 días
```

Un ejercicio de 52/53 semanas puede aceptarse si queda documentado.

# 9. Regla epistemológica

$$
\text{dato primario}
\neq
\text{explicación causal}
$$
