---
content_id: transferencia-p1-d2-v05b
title: "P1.D2 — Transferencia de continuidad después del cierre técnico v0.5B"
version: "0.5B"
document_type: operational_transfer
status: validated_for_next_stage
language: es
canonical_project: "Investigando mercados"
as_of: 2026-10-08
supersedes:
  - "TRANSFERENCIA_HILO_P1_D2_v05A.md"
source_release: "0.5B"
d2_engine_version: "0.3"
next_phase: "triage_economico_de_senales"
next_phase_status: authorized_not_executed
ready_for_signal_triage: true
---

# TRANSFERENCIA DE HILO — P1.D2 tras el cierre técnico de v0.5B

> [!important] Dictamen de continuidad
> **La condición de consistencia que bloqueaba el triage económico en v0.5A se ha satisfecho con v0.5B.** Se ha comprobado independientemente la identidad de los 50 registros, la coherencia de los cuatro indicadores D2, los 38 cálculos anuales procesables, la conservación de los datos contables y la procedencia. El siguiente paso *autorizado*, pero **no ejecutado en esta transferencia**, es el triage económico explicativo de AAON, CXT y FUN. La ejecución de `pytest` sobre el repositorio sólo está acreditada por el informe de Codex, no reproducida aquí.

## 1. Identidad y frontera del proyecto

**Proyecto:** `Investigando mercados`.

**Objeto operativo:** `P1.D2 / C4.D2 — Crecimiento de ingresos frente a margen operativo`.

Regla ontológica obligatoria:

```text
Investigando mercados = CONOCER
Inversiones crecimiento = DECIDIR
```

El detector D2 identifica una divergencia de indicadores, no un valor interesante para comprar, una oportunidad, una expectativa de revalorización o una propiedad de convexidad.

```text
Observación financiera
→ divergencia reproducible
→ hipótesis explicativas alternativas
→ contraste y falsación
→ pregunta de investigación
```

No se permiten recomendaciones `buy/sell`, tamaño de posición, señales de valoración o selección de cartera dentro de esta transferencia.

## 2. Regla D2 congelada

La lógica del evaluador anual US-GAAP permanece en `d2_engine_version = 0.3`.

Sean $R_t$ los ingresos del ejercicio anual más reciente seleccionado, $R_{t-1}$ los del ejercicio anterior y $OI$ el resultado operativo de cada período. La condición de divergencia es:

$$
g_{FY}=\frac{R_t}{R_{t-1}}-1\geq 0.10
$$

junto con:

$$
\Delta OM_{pp}=100\left(\frac{OI_t}{R_t}-\frac{OI_{t-1}}{R_{t-1}}\right)\leq -2
$$

Los umbrales del **10 %** y **−2 puntos porcentuales** siguen siendo hipótesis instrumentales experimentales, no criterios metodológicos canónicos ni condiciones suficientes de calidad empresarial.

No se modificaron `Revenue`, `OperatingIncomeLoss`, reglas de selección de ejercicios fiscales, criterios de frescura, universo ni contrato Revenue.

## 3. Universo piloto y limitación inferencial

El piloto conserva **50 compañías estadounidenses**, acciones ordinarias de negocios operativos no financieros, excluyendo REIT, BDC, fideicomisos de regalías y determinadas sociedades limitadas de socios, con capitalización seleccionada entre 500 millones y 20.000 millones de dólares.

El diseño se distribuye intencionalmente en cinco estratos de diez empresas cada uno:

| Estrato de capitalización | Número |
|---|---:|
| 0,5–1 millardo USD | 10 |
| 1–2 millardos USD | 10 |
| 2–5 millardos USD | 10 |
| 5–10 millardos USD | 10 |
| 10–20 millardos USD | 10 |

Esta selección es una **muestra de estrés**; la frecuencia de señales observada no estima de manera representativa la frecuencia de divergencias en toda la población de cotizadas.

## 4. Inventario de archivos vigentes

### 4.1. Salidas operativas de v0.5B

| Archivo | Función |
|---|---|
| `CODEX_TASK_05B_REPORT.md` | Causa raíz, ejecución y declaración de cierre de Codex |
| `D2_diagnostics_v05B.md` | Conteos, cobertura y lista técnica de señales |
| `D2_results_v05B.csv` | Resultado principal del cribador con cuatro indicadores y dos nuevos campos de evaluación |
| `D2_provenance_v05B.csv` | Hechos SEC utilizados, preservados desde v0.5A, más metadatos de versión |
| `P1_universe_v05B.csv` | Universo piloto, conservado salvo metadatos de versión |
| `D2_flag_consistency_audit_v05B.csv` | Auditoría de coherencia, fila por fila, para las 50 compañías |

### 4.2. Artefactos anteriores que se conservan

| Archivo | Estado |
|---|---|
| `D2_results_v05A.csv`, `D2_provenance_v05A.csv`, `P1_universe_v05A.csv`, `D2_diagnostics_v05A.md` | Instantánea histórica para comparación y trazabilidad; **no** resultado operativo vigente |
| `Revenue_tag_decisions_v05A.csv` | Decisiones del contrato Revenue **vigentes**, sin reapertura |
| `Revenue_unknown_diagnostics_v05A.csv` | Diagnóstico y justificación histórica de la resolución de Revenue; se conserva |
| `TRANSFERENCIA_HILO_P1_D2_v05A.md` | Historial de transferencia, sustituido funcionalmente por este documento |
| `P1_D2_AUDITORIA_TRANSFERENCIA_v05A.md` | Auditoría pre-reparación, válida como registro histórico del fallo |
| `P1_D2_v05B_acceptance_test.py` | Verificador previo ligado al esquema v0.5A; no usar sin adaptar a nuevos campos y a la reducción del diagnóstico |
| `P1_D2_v05B_verificacion_independiente.py` | Verificador independiente **adaptado** al formato entregado de v0.5B |

No sustituir los archivos históricos por una versión reconstruida, no modificar manualmente filas para ajustar conteos y no trasladar un indicador derivado a categoría de evidencia fundamental.

## 5. Hallazgo de v0.5A y causa raíz establecida en v0.5B

En v0.5A, `AAON` tenía:

```yaml
candidate_d2: true
d2_signal: true
universe_eligible: true
freshness_status: fresh
latest_fy_resolution_status: resolved
raw_d2_signal: false
eligible_d2_signal: false
```

Esto violaba la coherencia del resultado D2. `CODEX_TASK_05B_REPORT.md` identifica la causa raíz en un paso de **combinación posterior a la reconciliación Revenue**: se fusionó una salida nueva del evaluador v0.3 (`D2Result`) con filas anteriores v0.4, sin recalcular después las columnas derivadas `raw_d2_signal` y `eligible_d2_signal`, que no pertenecían al objeto `D2Result`.

La explicación documentada es, por tanto, **indicadores copiados que quedaron desactualizados**, no un defecto en la comparación contra los umbrales ni en la interpretación de valores booleanos.

En v0.5B:

```yaml
AAON:
  candidate_d2: true
  d2_signal: true
  raw_d2_signal: true
  eligible_d2_signal: true
  universe_eligible: true
  freshness_status: fresh
```

Al comparar los dos `D2_results`, **los únicos campos funcionales históricos modificados son exactamente esos dos indicadores de AAON, ambos de `False` a `True`**. Cambian además los metadatos de tarea y versión; se añaden dos campos de diagnóstico de evaluación. No cambia ninguna magnitud económica.

El informe de Codex menciona **dos filas afectadas, AAON y CNX**. No significa dos señales añadidas. CNX sigue sin resultado D2 evaluable: `status=missing_operating_income` y `missing_latest_fy_metric=OperatingIncomeLoss`. Ahora consta expresamente `d2_evaluation_status=not_evaluated` y una razón. Su `eligible_d2_signal=false` **no** debe leerse como evaluación técnica negativa.

Este contraste es importante: las salidas D2 sólo permiten inferir resultados para compañías **evaluadas**, no para las que permanecen fuera del universo o no tienen datos comparables.

## 6. Semántica consolidada de estados derivados

Para filas evaluadas, `d2_signal` es la **única fuente de verdad técnica**; los demás indicadores son proyecciones del estado.

```python
candidate_d2 == d2_signal
raw_d2_signal == d2_signal
eligible_d2_signal == (
    d2_signal
    and universe_eligible is True
    and freshness_status == "fresh"
)
```

Se exige consistencia con `latest_fy_resolution_status` y con los estados explícitos de evaluación. Para una fila que no pudo evaluarse, el booleano `false` no informa por sí solo de un resultado negativo; debe consultarse `d2_evaluation_status` y `d2_evaluation_reason`.

El archivo `D2_flag_consistency_audit_v05B.csv` consigna **50 filas `consistent` de 50**, sin razones de discrepancia.

## 7. Resultados definitivos de salida v0.5B

| Métrica | Resultado |
|---|---:|
| `N_input` | 50 |
| `N_universe_eligible` | 40 |
| `N_universe_ineligible` | 7 |
| `N_universe_unknown` | 3 |
| `UniverseResolutionRate` | 94,0 % |
| `N_fresh_eligible_processable` | 38 |
| `EligibleFreshCoverage` | 95,0 % |
| `N_raw_D2_signals` | 3 |
| `N_eligible_D2_signals` | 3 |
| `N_flag_inconsistencies` | 0 |

Métricas de continuidad de v0.5A, **recalculables pero omitidas del diagnóstico resumido v0.5B**: `N_definitively_ineligible=7`, `EndToEndTerminalResolution=90,0 %`, cobertura descriptiva legacy = 76,0 %. Ninguna entra en contradicción con v0.5B. Se recomienda mantenerlas en futuros informes para evitar pérdida de continuidad documental.

De las 40 elegibles, 38 están procesadas; **CNX** no es procesable por falta de `OperatingIncomeLoss` anual y **IP** presenta `latest_fy_unresolved`. Los otros 10 casos fuera de la evaluación se componen de siete inelegibles y tres de elegibilidad desconocida.

Las tres compañías con señal técnica elegible son:

| Ticker | Compañía | Crecimiento anual ingresos | Margen operativo FY anterior | Margen operativo FY actual | Variación pp |
|---|---|---:|---:|---:|---:|
| AAON | AAON, INC. | +20,1094 % | 17,4173 % | 10,1415 % | −7,2758 |
| CXT | Crane NXT, Co. | +11,4272 % | 18,0791 % | 14,8910 % | −3,1880 |
| FUN | Six Flags Entertainment Corporation/NEW | +14,4472 % | 11,4623 % | −44,3509 % | −55,8133 |

Son **observaciones del motor**, no explicaciones económicas. No atribuir todavía el margen de FUN a operaciones recurrentes ni inferir causas en AAON o CXT.

## 8. Auditoría independiente de consistencia e integridad

Se ejecutó `P1_D2_v05B_verificacion_independiente.py` directamente sobre los archivos cargados, con **ocho bloques `PASS`, cero fallos y `READY_FOR_SIGNAL_TRIAGE: PASS`**.

Alcance verificado:

1. Las cinco sumas de comprobación SHA-256 del informe Codex coinciden exactamente con los archivos v0.5B recibidos.
2. Las 50 compañías del universo y todos sus campos sustantivos permanecen iguales a v0.5A.
3. Las 50 filas de `D2_results` conservan todos los campos económicos y técnicos preexistentes, salvo los dos indicadores de AAON antes descritos.
4. Los **189 registros de procedencia** conservan sus 16 campos históricos y sus valores, incluida multiplicidad; v0.5B sólo añade `engine_version`, `d2_engine_version` y `task`.
5. Las relaciones entre los cuatro indicadores, elegibilidad y frescura son consistentes en 50 filas y reproducen el archivo de auditoría.
6. Los 38 cálculos D2 procesables reconcilian contra sus **152 hechos de procedencia** utilizados para Revenue y OperatingIncomeLoss en los dos ejercicios comparados.
7. Los contadores principales y las tres señales coinciden con `D2_diagnostics_v05B.md`.
8. Se conserva la distinción entre 38 filas `evaluated` y 12 `not_evaluated` (incluyendo CNX, IP y el universo no elegible/desconocido).

**Ejecución del repositorio:** `CODEX_TASK_05B_REPORT.md` declara `pytest -q`: **88 pruebas superadas (80 previas + 8 nuevas)**. Este resultado se atribuye a Codex. Como no se ha entregado el repositorio ni su registro completo de pruebas, la auditoría independiente **no afirma haber reproducido las 88 pruebas** ni haber inspeccionado las líneas exactas de la reparación.

**Compatibilidad documental:** el antiguo verificador `P1_D2_v05B_acceptance_test.py` da un falso bloqueo formal con los nuevos archivos porque comparaba todos los campos de procedencia sin tolerar tres columnas nuevas y exigía en el informe resumido métricas de diagnóstico v0.5A que dejaron de imprimirse. Esa incompatibilidad del instrumento antiguo **no constituye una violación de los cálculos D2**. Se ha preparado y probado el verificador adaptado; no es preciso modificar las salidas certificadas para acomodar un test obsoleto.

## 9. Casos pendientes de Revenue

Permanecen abiertos, sin forzar una interpretación por aumentar cobertura:

| Ticker | Estado | Motivo |
|---|---|---|
| EMAT | `context_mismatch` | Desajuste de contexto del período más reciente |
| PXED | `context_mismatch` | Desajuste de contexto del período más reciente |
| RRC | `ambiguous_components` | Ambigüedad entre conceptos/componentes de ingresos |

La clasificación proviene de v0.5A y se preserva en v0.5B. No reabrir `Revenue_tag_decisions_v05A.csv` sin evidencia nueva y una tarea específica.

## 10. Sumas SHA-256 de la instantánea v0.5B

```text
P1_universe_v05B.csv
c1a680434d5c60c62c3b18d0f4ce68ace8810a283fdc4c502721c74f4899890f

D2_results_v05B.csv
f9c14e087103536a2b2e0a40ecc4b0b05febd9c8a988d7f1e7fe6cf9820c4725

D2_provenance_v05B.csv
0b86767b9b898fe569cbeafb531f257b8bbbdbfac0544ad3d3ce41ff8d88f4c6

D2_flag_consistency_audit_v05B.csv
8fabb599ced4fd282cba181a974e518aa0031a85b81eb390793851415c592969

D2_diagnostics_v05B.md
770bbdf44e029f74b0ded495d1b553040a3528e17279a9ed08718b6273601513
```

## 11. Criterio de cierre y autorización de la próxima fase

La condición que impedía continuar era **la coherencia de los indicadores técnicos D2**. Está satisfecha para los archivos v0.5B: tres señales elegibles, cero incoherencias, hechos SEC y métricas inalterados, umbrales y motor v0.3 congelados.

```yaml
project: "Investigando mercados"
object: "C4.D2 — Crecimiento vs margen operativo"
engine_version: "0.5B"
d2_engine_version: "0.3"
status: "validated_for_next_stage"
ready_for_signal_triage: true
n_input: 50
n_universe_eligible: 40
n_fresh_eligible_processable: 38
n_raw_d2_signals: 3
n_eligible_d2_signals: 3
n_flag_inconsistencies: 0
signal_tickers: [AAON, CXT, FUN]
open_revenue_cases: [EMAT, PXED, RRC]
next_phase: "triage_economico_de_senales"
next_phase_status: "authorized_not_executed"
```

### 11.1. Alcance autorizado del triage (siguiente tarea, aún no realizada)

Para **AAON, CXT y FUN**, y sólo sobre la base técnica validada:

1. Recuperar los registros SEC relevantes y cualquier otra fuente primaria necesaria para interpretar los ejercicios FY empleados por el motor.
2. Separar **crecimiento orgánico**, adquisiciones o cambio de perímetro, efecto base, precio, volumen, mezcla, y variaciones de presentación contable.
3. Reconstruir las causas potenciales de margen: costes transitorios, reestructuración, deterioros de activos, amortizaciones de intangibles, escala, integración, inversión o deterioro recurrente.
4. Distinguir hechos observados de declaraciones de la dirección y de inferencias propias.
5. Formular **al menos dos hipótesis rivales** por señal y precisar la evidencia discriminante capaz de favorecer o debilitar cada una.
6. Producir una **pregunta de investigación falsable** y una clasificación del tipo de divergencia, indicando incertidumbre y trazabilidad.
7. No convertir automáticamente ninguna divergencia en ventaja competitiva, oportunidad de inversión, valoración o señal de compra.

El triage comienza en una fase analítica posterior a esta transferencia; **no ha sido efectuado aquí**. Debe recibir las versiones v0.5B, nunca los contadores incorrectos de v0.5A.

### 11.2. Deuda documental menor, no bloqueante

Conviene conservar en futuras versiones, además de los contadores mínimos actuales, la tasa de resolución terminal, la cobertura descriptiva legacy, el detalle de causas de Revenue y el estado de las puertas experimentales. Su ausencia en la versión abreviada del diagnóstico v0.5B no invalida las invariantes ni requiere reabrir el núcleo D2.

---

**Dictamen:** `v0.5B VALIDADA; TRANSFERENCIA ACTUALIZADA; TRIAGE ECONÓMICO AUTORIZADO, TODAVÍA NO EJECUTADO`.
