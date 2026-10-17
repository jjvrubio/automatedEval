# CODEX_TASK_05A — Diagnóstico y ampliación controlada del contrato Revenue SEC

> Nota operativa: el nombre `CODEX_TASK` se conserva por continuidad documental.
> Puede ejecutarse con GitHub Copilot u otro agente local compatible.

## Contexto

`CODEX_TASK_04` ejecutó el piloto P1 de 50 compañías con el motor D2 v0.3 congelado.

Resultado observado:

```text
N_input = 50
N_universe_eligible = 33
N_universe_unknown = 13
N_fresh_eligible_processable = 31
eligible_fresh_coverage = 93.9%
raw_D2_signals = 2
eligible_D2_signals = 2
```

La capa D2 funciona con alta cobertura una vez que la compañía queda elegible.

El principal problema está antes:

```text
13 / 50 = 26%
```

del piloto quedan con `universe_eligible=unknown` por resolución de Revenue.

Distribución de los 13 casos:

```text
10 → No allowed annual Revenue fact at the latest observed annual period
3  → Conflicting allowed annual Revenue tags at the latest period
```

No ampliar a 100 compañías todavía.

No cambiar D2.

---

# 1. Objetivo

Diagnosticar los 13 `universe_eligible=unknown` del piloto v0.4 y mejorar, sólo cuando exista evidencia semántica suficiente, el contrato de resolución de Revenue.

La pregunta es:

> ¿Qué parte del 26% desconocido es causada por un diccionario de conceptos Revenue demasiado estrecho, qué parte por ambigüedad real, qué parte por compañías sin Revenue comparable y qué parte por defectos de período/contexto?

---

# 2. Invariantes

NO modificar:

```text
Revenue Growth FY YoY >= 10%
Δ Operating Margin <= -2 pp
```

NO modificar:

- `OperatingIncomeLoss`;
- definición de FY;
- latest-FY requirement;
- universo P1;
- selección de 50;
- market-cap buckets;
- exclusiones jurídicas;
- 10-K / 10-K/A;
- US-GAAP only;
- no 10-Q;
- no TTM.

NO introducir:

- valoración;
- precio;
- momentum;
- analistas;
- recomendación;
- decisión de inversión.

---

# 3. Input congelado

Usar exactamente:

```text
input/universe_p1_50.csv
```

producido por R2.

Verificar SHA-256:

```text
01c760346139648c9f63624c516f94db4c3a4fe9fc0bf2ad33171dd557323f57
```

Si cambia:

```text
BLOCKED_UNIVERSE_INPUT_CHANGED
```

No reseleccionar compañías.

---

# 4. Los 13 casos unknown

El diagnóstico debe partir exactamente de:

```text
AAON
BV
EMAT
EVRG
FRNM
HYMC
IDT
IMVT
LFUS
MATW
PXED
RRC
WEX
```

No hardcodear su solución.

La lista sólo sirve como conjunto de regresión del piloto v0.4.

---

# 5. Separar diagnóstico de resolución

Para cada ticker unknown crear primero un inventario de TODOS los hechos anuales candidatos relacionados con ingresos en el último FY observado.

No limitar esta fase a los tres tags permitidos actualmente.

Inventariar, como mínimo:

```text
taxonomy
tag
label / description if available
unit
start
end
value
form
filed
accession
fy
fp
```

y si el dato es:

```text
consolidated_total
segment_or_component
topic606_subset
non_topic606_component
other_income_component
unknown_semantics
```

No usar todavía el dato para cerrar elegibilidad.

---

# 6. Taxonomía de causas

Cada unknown debe quedar clasificado en UNA causa principal:

```text
A_alternative_standard_total_revenue_tag
B_custom_total_revenue_tag
C_component_vs_total_conflict
D_multiple_total_concepts_semantically_different
E_latest_period_context_mismatch
F_true_no_revenue_or_pre_revenue
G_filing_or_taxonomy_anomaly
H_unresolved_other
```

Añadir:

```text
diagnostic_confidence = low/moderate/high
```

---

# 7. Regla de ampliación del diccionario

Un nuevo tag sólo puede incorporarse al resolver automático si cumple:

1. pertenece a `us-gaap`;
2. representa ingresos consolidados totales o ventas netas consolidadas;
3. es económicamente equivalente al numerador Revenue usado en D2;
4. no representa sólo un segmento;
5. no representa sólo una subcategoría Topic 606 cuando existen ingresos materiales fuera de Topic 606;
6. no incorpora de forma material partidas no operativas que hagan inconsistente D2;
7. puede validarse contra el estado de resultados primario del 10-K.

Documentar para cada tag propuesto:

```text
tag
semantic_definition
accepted/rejected
reason
example_tickers
```

---

# 8. No resolver ambigüedad por preferencia ciega

Para los casos actuales:

```text
EVRG
RRC
WEX
```

no elegir simplemente:

```text
RevenueFromContract...
```

o:

```text
Revenues
```

por prioridad estática.

Comparar la semántica con el estado de resultados.

Ejemplos de riesgo:

```text
WEX:
Topic 606 revenue != total revenue
```

```text
RRC:
product sales != total revenues and other income
```

```text
EVRG:
revenue from contracts with customers != operating revenues
```

El objetivo es identificar el concepto económico compatible con D2, no maximizar cobertura.

---

# 9. Evidencia primaria obligatoria

Para cada uno de los 13 casos, conservar una referencia al 10-K que permita validar el importe económico del Revenue total relevante.

Crear:

```text
source_filing_url
source_statement_label
source_statement_value
```

Si no se puede reconciliar Companyfacts con el estado de resultados:

```text
unresolved
```

No reparar a mano el valor dentro del resultado final.

---

# 10. Nuevo contrato Revenue v0.2

Crear documento:

```text
docs/14_Contrato_Revenue_SEC_v0_2.md
```

Debe contener:

- tags aceptados;
- tags rechazados;
- reglas de total vs componente;
- reglas para utilities;
- reglas para empresas con Topic 606 + non-Topic 606;
- reglas para extractivas si aplica;
- custom tags: política explícita;
- ambigüedad;
- provenance;
- fallback prohibidos.

No convertir reglas específicas de un ticker en reglas generales sin justificación semántica.

---

# 11. Custom tags

Por defecto:

```text
custom_tag != automatically accepted
```

Un custom tag puede utilizarse sólo si:

1. el filing XBRL lo define claramente;
2. corresponde al total consolidado del estado de resultados;
3. se puede reconciliar exactamente con el statement;
4. el uso queda registrado como:

```text
resolution_method = validated_custom_total
```

No añadir custom tags a una allowlist global por nombre.

La validación debe ser por filing/contexto.

---

# 12. Estados de resolución nuevos

Usar:

```text
resolved_standard_total
resolved_validated_custom_total
resolved_semantic_reconciliation
ambiguous_components
no_revenue
context_mismatch
unresolved
```

No colapsarlos en `resolved/ambiguous` solamente.

---

# 13. Métricas de cobertura

Corregir la semántica de los gates.

La métrica v0.4:

```text
fresh_coverage = fresh eligible D2 / N_input
```

NO debe utilizarse como gate técnico principal, porque las compañías correctamente ineligibles no deben ejecutar D2.

Calcular explícitamente:

$$
UniverseResolutionRate =
\frac{
N_{eligible}+N_{ineligible}
}{
N_{input}
}
$$

$$
EligibleFreshCoverage =
\frac{
N_{fresh\ eligible\ processable}
}{
N_{eligible}
}
$$

$$
EndToEndTerminalResolution =
\frac{
N_{fresh\ eligible\ processable}+N_{definitively\ ineligible}
}{
N_{input}
}
$$

Conservar `fresh_coverage` sólo como métrica descriptiva legacy.

No borrar historia v0.4.

---

# 14. Gate experimental

Para esta tarea:

```text
EligibleFreshCoverage >= 70%
```

sigue siendo gate del motor D2.

Añadir:

```text
UniverseResolutionRate
```

como métrica diagnóstica prioritaria.

Objetivo experimental, NO canónico:

```text
UniverseResolutionRate >= 90%
```

antes de ampliar a 100.

Si no se alcanza, no forzar nuevos tags para alcanzar el objetivo.

Calidad semántica > cobertura.

---

# 15. Señales D2 existentes

No modificar la clasificación D2 de:

```text
CXT
FUN
```

en esta tarea.

No normalizar impairments, M&A o restructuring aquí.

Eso pertenece a una tarea posterior de triage de señales.

---

# 16. Tests obligatorios

Mantener todos los tests previos y añadir:

1. standard total revenue alternativo válido;
2. Topic 606 subset no sustituye total si existe non-Topic 606 material;
3. utility operating revenue total vs customer-contract subset;
4. extractive product sales vs total revenue/other-income ambiguity;
5. validated custom total reconciles exactly to statement;
6. custom tag without semantic validation remains unresolved;
7. component tag cannot be selected as consolidated total;
8. same-period conflicting total concepts remain ambiguous;
9. latest FY remains mandatory;
10. all 13 v0.4 unknowns receive a diagnostic-cause code;
11. no ticker-specific exception branch;
12. previous v0.3/v0.4 regressions remain green.

Ejecutar:

```bash
pytest -q
```

---

# 17. Outputs

No sobrescribir v0.4.

Generar:

```text
output/Revenue_unknown_diagnostics_v05A.csv
output/Revenue_tag_decisions_v05A.csv
output/P1_universe_v05A.csv
output/D2_results_v05A.csv
output/D2_provenance_v05A.csv
output/D2_diagnostics_v05A.md
CODEX_TASK_05A_REPORT.md
```

Usar:

```text
engine_version = 0.5A
d2_engine_version = 0.3
task = CODEX_TASK_05A
```

---

# 18. Diagnóstico final

`D2_diagnostics_v05A.md` debe informar:

```text
N_input
N_universe_eligible
N_universe_ineligible
N_universe_unknown
UniverseResolutionRate
N_fresh_eligible_processable
EligibleFreshCoverage
EndToEndTerminalResolution
N_raw_D2_signals
N_eligible_D2_signals
```

y:

```text
## Unknown resolution changes
```

con:

```text
ticker
v04_status
v05A_status
cause
resolution_method
revenue_value
source_filing_url
```

---

# 19. Informe

`CODEX_TASK_05A_REPORT.md` debe responder:

1. ¿Cuántos de los 13 unknown fueron resueltos?
2. ¿Cuántos siguen unknown?
3. ¿Qué causas explicaban los 13?
4. ¿Qué nuevos tags estándar se aceptaron?
5. ¿Se usó algún custom tag validado?
6. ¿Qué ambigüedades permanecen?
7. ¿Cuál es el nuevo UniverseResolutionRate?
8. ¿Cuál es el EligibleFreshCoverage?
9. ¿Cambió el número de señales D2?
10. ¿Apareció algún defecto nuevo en el contrato SEC?
11. ¿Está justificado ampliar a 100 o hace falta otra reparación?

Añadir SHA-256 de todos los artefactos v05A.

---

# 20. Criterio de cierre

Éxito metodológico NO significa resolver los 13.

Significa:

```text
pytest PASS
all 13 diagnosed
every new automatic resolution semantically justified
primary-source reconciliation preserved
no D2 threshold drift
no ticker-specific hacks
```

Terminar con uno de:

```text
READY_FOR_SIGNAL_TRIAGE
```

o:

```text
REVENUE_CONTRACT_REQUIRES_MORE_WORK
```

---

# 21. Principio epistemológico

$$
\text{más cobertura}
\neq
\text{mejor evidencia}
$$

y:

$$
\text{XBRL tag coincidente}
\neq
\text{concepto económico equivalente}
$$

La ampliación del contrato debe reducir falsos desconocidos sin crear falsos Revenue.
