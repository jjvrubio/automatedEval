---
titulo: TES_KPI_Sectores
aliases:
  - KPI sectores TES
  - Sectores KPI TES
  - Especializacion sectorial KPI TES
idioma: es
fecha: '2026-04-21'
version: v1.0
estado: activo
estado_edicion: integrado
tipo: especializacion_sectorial_de_medicion
capa: zona_externalizada_medicion
alcance: despliegue_sectorial_de_kpis_normas_de_ids_mapeo_core_sector_y_paquetes_minimos_de_piloto
funcion: concentrar en un unico nodo la especializacion sectorial de la medicion del TES, absorbiendo la riqueza descriptiva y operativa del archivo excepcional de verticales sin duplicar funciones ni abrir un segundo documento paralelo
canonico: false
rige:
  - especializacion_sectorial_de_kpis
  - rangos_de_ids_y_reglas_de_mantenimiento
  - compatibilidad_core_sector
  - paquetes_minimos_sectoriales
  - mapa_kpi_palanca_convercus
  - collision_ledger_de_metricas
  - terminologia_sectorial_de_medicion
dominio_precedencia: especializacion_sectorial_de_medicion_en_la_zona_externalizada_medicion
depende_de:
  - LEEME
  - TES_Gobernanza_Documental
  - TES_Experience_Ledger
  - TES_Lexico
documentos_relacionados:
  - léeme_medición
  - TES_KPI_Dictionary
  - TES_KPI_Dictionary_VERTICALS v1_6
  - léeme_registro_validación
tags:
  - TES
  - medicion
  - KPI
  - sectores
  - verticales
  - externalizacion
---

# TES_KPI_Sectores

## Naturaleza de esta pieza

`TES_KPI_Sectores` concentra la especializacion sectorial de la medicion del TES dentro de `medicion/`.

No redefine la ontologia primaria, no sustituye al [[TES Núcleo/TES_Experience_Ledger|TES_Experience_Ledger]], no ocupa el lugar del `TES_Lexico` y no desplaza la gobernanza documental. Su tarea es otra: ordenar en un unico nodo vigente los desarrollos sectoriales de KPIs, sus rangos de identificacion, sus reglas de mantenimiento, sus instanciaciones por vertical y sus paquetes minimos de uso.

Esta pieza existe para evitar una duplicacion funcional entre un diccionario KPI general y un archivo sectorial rico tratado como fuente paralela de trabajo. Por ello, absorbe la riqueza descriptiva y operativa del archivo excepcional [[KPI Dictionary VERTICALS v1_6|TES_KPI_Dictionary_VERTICALS v1_6]] y lo deja relegado a función de trazabilidad de construcción, no de nodo vigente adicional.

## Principio rector

> En `medicion/`, la especializacion sectorial de los KPIs debe vivir en un solo nodo vigente.
>
> La riqueza sectorial se integra; no se reparte entre documentos paralelos de la misma funcion.

## Estatuto documental

Esta pieza pertenece a la zona externalizada `medicion/`.

Su estatuto es el de **especializacion sectorial de la medicion**. Esto implica simultaneamente que:

- la **entrada de medicion** sigue dependiendo de la cadena fijada por `TES_Experience_Ledger`;
- la **gobernanza del mapa visible** sigue dependiendo de `LEEME` y `TES_Gobernanza_Documental`;
- la **normalizacion terminologica** sigue remitiendo a `TES_Lexico`;
- y la **especializacion por sectores** se desarrolla aqui sin reclamar soberania de nucleo.

Relación con `TES_KPI_Dictionary`:

- [[TES_KPI_Dictionary]] fija la gramática KPI, la definición matriz y la trazabilidad mínima de la capa analítica.
- [[TES_KPI_Sectores]] desarrolla esa gramática por sectores y concentra los módulos verticales vigentes.

Cuando exista conflicto entre definición matriz y especialización sectorial, prevalecerá `TES_KPI_Dictionary` en la definición general y `TES_KPI_Sectores` en la adaptación sectorial compatible.

## Regla de uso

Esta pieza debe utilizarse:

- para desplegar KPIs por sector;
- para conservar la compatibilidad entre KPIs core y KPIs sectoriales;
- para fijar rangos de IDs, owners, formulas, fuentes y gates por vertical;
- y para vincular medicion sectorial y palancas operativas de Convercus.

No debe utilizarse:

- para redefinir la arquitectura general del TES;
- para sustituir el futuro o vigente `TES_KPI_Dictionary` como nodo matriz de medicion;
- ni para justificar la coexistencia de otro documento vivo con la misma riqueza sectorial y la misma funcion.

## Contenido integrado

Lo que sigue constituye ya el cuerpo operativo del nodo sectorial vigente.

Se conserva la riqueza estructural del archivo de verticales: norma de IDs, ficha reusable, modulos por sector, paquetes minimos, indice por owner, mapa KPI → palanca y registro de colisiones. La absorcion no resume ese contenido; lo incorpora.

---


Este documento funciona como “diccionario” para estandarizar KPIs en diagnósticos, pilotos y gobernanza. La idea es simple: **cada KPI debe poder auditarse** (fuente + fórmula), **operarse** (cadencia + owner) y **vincularse** (cómo lo mueve Convercus y bajo qué condiciones).

---

## Convención de IDs KPI y rangos por módulo (norma)

Para preservar **auditabilidad**, evitar colisiones y permitir escalado por vertical, este diccionario usa IDs estables con rangos reservados. Un KPI mantiene su ID a lo largo del tiempo; si cambia la fórmula o el alcance de forma material, se crea un **nuevo KPI-ID** y el anterior se marca como *deprecated* (con nota de migración).

### Rangos reservados (versión actual)

- **KPI-001–049 — Core transversal**: economía/rentabilidad, cliente/lealtad, omnicanalidad y eficiencia comercial (aplica a todos los verticales).
- **KPI-050–099 — Viajes / Travel**: agencias, mayoristas/turoperación y programas de destino (turismo), incluyendo pagos/refunds/chargebacks y cost-to-serve por reserva.
- **KPI-100–149 — Distribución de moda, zapatos y complementos**: descuentos, inventario, devoluciones, tallas y disciplina promocional.
- **KPI-150–199 — Supermercados de alimentación y hogar**: frescos, disponibilidad, merma, ejecución operativa y cadencias cortas.
- **KPI-200–249 — Hoteles, alojamientos y hospitality**: ocupación, ADR/RevPAR, canal directo, estancias, revenue management y satisfacción.
- **KPI-250–299 — Parafarmacias**: mix y margen por categoría, recurrencia, caducidades, compliance promocional y servicios de consejo.
- **KPI-300–349 — Atención sanitaria y hospitalaria (privada)**: acceso de pacientes, utilización clínica, margen por episodio, revenue-cycle y experiencia.
- **KPI-350–399 — Reservado**: futuros verticales y sub-rangos.

### Reglas de mantenimiento

1) **No reutilizar IDs**: si un KPI se elimina, su ID no se reasigna.
2) **Fuente + fórmula obligatorias**: si no existe trazabilidad aún, se permite un KPI en estado *C* (pendiente de instrumentación), pero nunca sin definir fuente y fórmula objetivo.
3) **Referencias internas**: cualquier “Paquete mínimo”, mapa de palancas o checklist debe referenciar **KPI-IDs**, no nombres sueltos.
4) **Compatibilidad core↔sector**: cuando un KPI del core aplica al sector sin cambios materiales, se referencia el **KPI core**. Solo se crea KPI sectorial si hay diferencias inevitables (unidad de análisis, fuente o fórmula) que impidan comparabilidad.


## 0) Plantilla — Ficha KPI (copiar/pegar)

> **KPI ID:** KPI-XXX  
> **Nombre:**  
> **Definición:**  
> **Fórmula:**  
> **Unidad:**  
> **Fuente de datos (sistemas):**  
> **Nivel de cálculo:** (cliente | pedido | ticket | SKU | tienda | canal | cohorte)  
> **Frecuencia de medición:** (diario | semanal | mensual | trimestral)  
> **Owner (responsable):** (Finanzas | Marketing/eComm | Operaciones | Data/BI | Supply | TI)  
> **Umbral/Objetivo:** (baseline + target + horizonte)  
> **Notas operativas:** (supuestos, filtros, exclusiones, estacionalidad, segmentación)  
> **Sesgos comunes / Riesgos de interpretación:**  
> **Relación con Convercus:** (capacidad → palanca → mecanismo → cómo se valida incrementalidad)  
> **Compuerta de piloto (Gate):** (sí/no; regla de decisión)  
> **Estado de calidad de dato:** (A/B/C; definida abajo)

### Escala de calidad de dato (recomendada)
- **A:** definición y fórmula estables; fuente única; trazabilidad completa; latencia conocida; histórico ≥12 meses.
- **B:** definición estable pero múltiples fuentes o latencia variable; histórico parcial.
- **C:** definición no consolidada o no medible hoy; requiere instrumentación.

---

## 1) Economía y rentabilidad (core)

### KPI-001 — Net Revenue (Net Sales / Net Revenue)
- **Definición:** Ingreso neto atribuible al negocio en el periodo, neto de devoluciones/refunds, descuentos e incobrables/ajustes; en retail suele mapear a **Net Sales**, y en viajes a **Net Revenue** (comisiones/fees/mark-ups) según modelo.
- **Fórmula:** *Retail (Net Sales):* ventas brutas − devoluciones − descuentos (según política). *Viajes (Net Revenue):* comisiones + fees + mark-ups + otros − contraingresos/ajustes (refunds, chargebacks, incentivos, etc.).
- **Unidad:** €.
- **Fuente de datos (sistemas):** ERP/Finance; POS; eCommerce; Data Warehouse.
- **Nivel de cálculo:** canal, tienda, cohorte.
- **Frecuencia de medición:** semanal/mensual.
- **Owner (responsable):** Finanzas.
- **Umbral/Objetivo:** crecimiento vs LY y vs plan.
- **Notas operativas:** Declarar el **modelo de negocio** (retail; viajes agency vs merchant), la política de neteo (descuentos/bonos), el tratamiento de devoluciones/refunds y el momento de reconocimiento (accrual vs cash). *Equivalencias sectoriales:* ver **KPI-051** (instanciación Viajes).
- **Sesgos comunes:** confundir revenue con contribución (ignorar COGS, devoluciones, fulfillment).
- **Relación con Convercus:** incremento por repetición identificada y AOV en cohortes expuestas; debe medirse como *uplift* vs control.
- **Compuerta de piloto (Gate):** no (KPI de resultado; se usa para validar).
- **Estado de calidad de dato:** A/B.

### KPI-002 — Gross Margin % (GM%)
- **Definición:** Margen bruto como % de ventas.
- **Fórmula:** (Ventas − COGS) / Ventas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** ERP/Finance; costing; Data Warehouse.
- **Nivel de cálculo:** SKU/categoría/canal/cohorte.
- **Frecuencia de medición:** mensual.
- **Owner:** Finanzas (con Merchandising).
- **Umbral/Objetivo:** mantener/mejorar vs baseline, especialmente en cohortes tratadas.
- **Notas:** definir COGS (incluye o no logística inbound); separar efecto precio vs mix.
- **Sesgos comunes:** atribuir mejora a fidelización cuando viene de mix/compra; ignorar devoluciones.
- **Relación con Convercus:** promo governance (cupones con guardarraíles) + experiencias para sustituir descuento; medir GM por pedido/cohorte.
- **Gate:** sí (si GM% cae en cohortes tratadas sin explicación, ajustar mecánicas).
- **Calidad:** A/B.

### KPI-003 — Contribution Margin per Transaction (CM/txn)
- **Definición:** Margen de contribución por **transacción** (pedido/ticket/reserva): ingreso neto menos costes variables atribuibles (pagos, picking/fulfillment, atención, incentivos, devoluciones/refunds, etc.).
- **Fórmula:** (Ventas − COGS − fulfilment − comisiones − devoluciones − pagos − atención) / nº pedidos.
- **Unidad:** €/pedido.
- **Fuente:** ERP; OMS/WMS; logística; PSP; CRM soporte; BI.
- **Nivel:** pedido, canal, cohorte.
- **Frecuencia:** semanal/mensual.
- **Owner:** Finanzas + Operaciones.
- **Umbral:** ≥ baseline en cohortes tratadas.
- **Notas:** requiere modelo de cost-to-serve por ruta (envío, BOPIS, BORIS).
- **Sesgos comunes:** subestimar devoluciones o costos indirectos; comparar rutas no equivalentes.
- **Relación con Convercus:** misiones que desplazan a rutas rentables (BOPIS, cambios vs reembolso); medición incremental por cohorte.
- **Gate:** sí (KPI clave de “no comprar ventas”).
- **Calidad:** B/C (suele requerir instrumentación).

### KPI-004 — EBITDA (or EBITDA proxy)
- **Definición:** Beneficio operativo antes de D&A (o proxy si no se dispone semanalmente).
- **Fórmula:** estándar contable; proxy: GM − Opex variables clave.
- **Unidad:** € y %.
- **Fuente:** Finance; ERP.
- **Nivel:** empresa/canal (no suele estar a cohorte).
- **Frecuencia:** mensual/trimestral.
- **Owner:** Finanzas.
- **Umbral:** mejorar vs plan o proteger durante expansión.
- **Sesgos:** atribución errónea (muchos drivers simultáneos).
- **Relación Convercus:** se usa como “norte”; el piloto debe demostrar drivers (repeat, devoluciones, dilución) que lo mueven.
- **Gate:** no (demasiado rezagado para piloto corto).
- **Calidad:** A.

### KPI-005 — Payback Period (Program ROI)
- **Definición:** tiempo para recuperar el coste total del programa mediante margen incremental.
- **Fórmula:** Coste total (SaaS + incentivos + operación) / margen incremental mensual.
- **Unidad:** meses.
- **Fuente:** Finance + BI (uplift).
- **Nivel:** programa/piloto.
- **Frecuencia:** mensual.
- **Owner:** CFO/Finanzas.
- **Umbral:** < 12–24 meses (según política).
- **Sesgos:** usar revenue uplift sin netear incentivos y canibalización.
- **Relación Convercus:** diseño de guardarraíles + medición incremental; escalado condicionado a payback.
- **Gate:** sí (decisión de escalar).
- **Calidad:** B (depende de diseño experimental).

---

## 2) Cliente, lealtad y fidelización (behavioural core)

### KPI-010 — Customer Identification Rate (POS + Online)
- **Definición:** % de transacciones con cliente identificado y consentido.
- **Fórmula:** nº transacciones con customer_id / nº transacciones totales.
- **Unidad:** %.
- **Fuente:** POS; eCommerce; CRM/CDP; consent logs.
- **Nivel:** tienda/canal/día.
- **Frecuencia:** diario/semanal.
- **Owner:** Marketing/CRM + Operaciones.
- **Umbral:** +X pp en piloto (ej. +5–15 pp según baseline).
- **Notas:** separar “identificado” de “miembro activo”; validar consentimiento.
- **Sesgos:** inflar por duplicados; identificar sin activar (base muerta).
- **Relación Convercus:** journeys + QR/flows de alta + incentivos no monetarios (experiencias) para capturar ID.
- **Gate:** sí (si no sube, no hay motor de personalización ni medición robusta).
- **Calidad:** A/B.

### KPI-011 — Member Penetration (Transactions by Members)
- **Definición:** % de transacciones realizadas por miembros del programa.
- **Fórmula:** transacciones de miembros / transacciones totales.
- **Unidad:** %.
- **Fuente:** POS/eCommerce + CRM.
- **Nivel:** tienda/canal/cohorte.
- **Frecuencia:** semanal.
- **Owner:** Marketing/CRM.
- **Umbral:** +X pp en 12 semanas piloto.
- **Sesgos:** miembros inactivos; miembros que compran igual (no incremental).
- **Relación Convercus:** aceleración de adopción vía journeys y gamificación; medir uplift vs control.
- **Gate:** sí (escala mínima para ROI).
- **Calidad:** A/B.

### KPI-012 — Repeat Rate (60/90-day repurchase)
- **Definición:** % clientes que recompran en 60/90 días.
- **Fórmula:** clientes con ≥2 compras en ventana / clientes elegibles.
- **Unidad:** %.
- **Fuente:** CRM/CDP; POS/eComm.
- **Nivel:** cohorte (alta/primera compra/campaña).
- **Frecuencia:** semanal (rolling) / mensual.
- **Owner:** Marketing/CRM + BI.
- **Umbral:** +0.5–2.0 pp (base) según baseline.
- **Sesgos:** estacionalidad; promociones externas; cohortes no equivalentes.
- **Relación Convercus:** misiones de repetición, niveles, reactivación; A/B o holdout para incrementalidad.
- **Gate:** sí (KPI “resultado temprano” de fidelización).
- **Calidad:** B (requiere cohortes bien definidas).

### KPI-013 — Purchase Frequency (per identified customer)
- **Definición:** compras promedio por cliente identificado en periodo.
- **Fórmula:** nº compras / nº clientes (identificados) en periodo.
- **Unidad:** compras/cliente/periodo.
- **Fuente:** CRM/CDP; POS/eComm.
- **Nivel:** cliente/cohorte.
- **Frecuencia:** mensual/trimestral.
- **Owner:** Marketing/CRM.
- **Umbral:** +2–5% anualizado (según baseline).
- **Sesgos:** mezcla de clientes (heavy buyers) y efecto supervivencia.
- **Relación Convercus:** tiering + experiencias + misiones para aumentar hábito.
- **Gate:** opcional (depende del piloto).
- **Calidad:** B.

### KPI-014 — LTV (Cohort LTV, contribution-based)
- **Definición:** margen de contribución acumulado por cliente en horizonte (cohorte).
- **Fórmula:** Σ contribución neta por cliente (incluye devoluciones y cost-to-serve).
- **Unidad:** €/cliente.
- **Fuente:** BI (modelado) + Finance.
- **Nivel:** cohorte.
- **Frecuencia:** trimestral.
- **Owner:** Finanzas + BI.
- **Umbral:** uplift vs control (no “nivel absoluto”).
- **Sesgos:** horizonte insuficiente; no descontar devoluciones; atribución débil.
- **Relación Convercus:** objetivo final; el piloto usa leading indicators (repeat, devoluciones) como proxies.
- **Gate:** no en 12 semanas; sí para escalado anual.
- **Calidad:** C→B (se madura).

### KPI-015 — Redemption Rate (Rewards)
- **Definición:** % recompensas emitidas que se canjean.
- **Fórmula:** canjes / recompensas emitidas.
- **Unidad:** %.
- **Fuente:** motor loyalty/cuponing; POS/eComm.
- **Nivel:** campaña/recompensa.
- **Frecuencia:** semanal.
- **Owner:** Marketing/CRM.
- **Umbral:** rango saludable (depende de diseño; evitar extremos).
- **Sesgos:** canje alto puede ser “subsidio” no incremental; canje bajo puede ser irrelevancia.
- **Relación Convercus:** optimización de journeys y ofertas; debe conectarse a margen incremental.
- **Gate:** sí si se dispara coste por canje.
- **Calidad:** A.

### KPI-016 — Effective Rebate Rate (Incentive Cost %)
- **Definición:** coste efectivo del incentivo como % de ventas afectadas.
- **Fórmula:** coste incentivos / ventas donde aplican.
- **Unidad:** %.
- **Fuente:** loyalty engine + Finance.
- **Nivel:** campaña/programa.
- **Frecuencia:** mensual.
- **Owner:** Finanzas + Marketing.
- **Umbral:** límite (ej. 0.5–2.0% según estrategia y margen).
- **Sesgos:** no netear canibalización; no separar categorías.
- **Relación Convercus:** reglas y guardarraíles por margen/categoría; experiencias para reducir necesidad de cupón.
- **Gate:** sí (control del “discount creep”).
- **Calidad:** B.

---

## 3) Omnicanalidad y eficiencia comercial

### KPI-030 — BOPIS Share (Click & Collect)
- **Definición:** % pedidos online recogidos en tienda.
- **Fórmula:** pedidos BOPIS / pedidos online totales.
- **Unidad:** %.
- **Fuente:** OMS/eComm; POS.
- **Nivel:** tienda/canal.
- **Frecuencia:** semanal.
- **Owner:** Omnichannel Ops.
- **Umbral:** +X pp si BOPIS es más rentable.
- **Sesgos:** comparar tiendas con distinta densidad; efecto campaña.
- **Relación Convercus:** misiones y recompensas para desplazar a rutas rentables; experiencias al recoger.
- **Gate:** sí si el objetivo es cost-to-serve.
- **Calidad:** A/B.

### KPI-031 — BORIS Share
- **Definición:** % devoluciones de online realizadas en tienda.
- **Fórmula:** devoluciones BORIS / devoluciones online totales.
- **Unidad:** %.
- **Fuente:** OMS + POS.
- **Nivel:** tienda/canal.
- **Frecuencia:** semanal/mensual.
- **Owner:** Operaciones + CX.
- **Umbral:** +X pp para reducir coste y aumentar exchanges.
- **Sesgos:** devoluciones registradas fuera de tienda.
- **Relación Convercus:** journeys postcompra y recompensas por devolución en tienda + cambio.
- **Gate:** sí si el coste por devolución es crítico.
- **Calidad:** B.

### KPI-032 — Cost-to-Serve per Transaction (by route)
- **Definición:** Coste variable de servicio/operación por **transacción** (pedido/ticket/reserva), desagregado por ruta (p. ej., envío, recogida, devoluciones, atención).
- **Fórmula:** Σ costes ruta / nº pedidos ruta.
- **Unidad:** €/pedido.
- **Fuente:** logística; WMS; OMS; Finance.
- **Nivel:** ruta/canal.
- **Frecuencia:** mensual.
- **Owner:** Operaciones + Finanzas.
- **Umbral:** reducir y/o desplazar mix hacia rutas mejores.
- **Sesgos:** costos indirectos mal asignados; latencias.
- **Relación Convercus:** gamificación conductual para dirigir elecciones del cliente.
- **Gate:** sí.
- **Calidad:** C→B.

### KPI-033 — Conversion Rate (Digital Checkout)
- **Definición:** Tasa de conversión digital en el **último tramo** (p. ej., sesión→compra o checkout-start→compra) según definición acordada. Complementa métricas de conversión por etapas.
- **Fórmula:** nº pedidos online / nº sesiones.
- **Unidad:** %.
- **Fuente:** analytics (GA/Adobe) + eComm.
- **Nivel:** canal/campaña.
- **Frecuencia:** diario/semanal.
- **Owner:** eCommerce.
- **Umbral:** subir sin aumentar devoluciones ni bajar margen.
- **Sesgos:** bots, cambios de tracking, atribución last-click.
- **Relación Convercus:** personalización, experiencias, journeys; medir lift en cohortes expuestas.
- **Gate:** no (siempre condicionada por margen).
- **Calidad:** B.

---

## 4) Distribución de moda, zapatos y complementos — Módulo sectorial (KPI-100–149)

Este módulo extiende el core con métricas de **temporada, descuentos, devoluciones y disponibilidad por talla**. Cuando aplique un KPI core (margen, identificación, repeat), se referencia el KPI core; aquí se añaden los *drivers* específicos.

### KPI-100 — Sell-Through (tasa de venta por campaña/temporada)
- **Definición:** Porcentaje del inventario recibido que se vende en una ventana definida (por colección/temporada).
- **Fórmula:** Unidades vendidas ÷ unidades recibidas (por campaña/temporada).
- **Unidad:** % (reportar también unidades y €).
- **Fuente de datos (sistemas):** ERP/Inventario + POS/eCommerce + BI merchandising.
- **Nivel de cálculo:** SKU | talla | tienda | canal | colección | semana
- **Frecuencia de medición:** semanal (operación) | mensual (dirección)
- **Owner (responsable):** Merchandising / Planning
- **Umbral/Objetivo:** ↑ vs baseline y plan; guardarraíl: no crecer por descuentos extremos (ver KPI-101/102).
- **Notas operativas:** Definir ventana (4/8/12 semanas) y separar full-price vs markdown. Normalizar por devoluciones.
- **Sesgos comunes / Riesgos de interpretación:** Comparaciones inválidas si cambia mix de colecciones o se ignoran devoluciones/cambios.
- **Relación con Convercus:** Capacidad: journeys + gamificación + segmentación → palanca: acelerar adopción de novedad y reducir necesidad de markdown → validación: test por cohortes/tiendas con control (uplift en full-price sell-through).
- **Compuerta de piloto (Gate):** sí (si no hay mejora en sell-through, el programa no está corrigiendo rotación).
- **Estado de calidad de dato:** B

### KPI-101 — % ventas en markdown (Markdown Rate)
- **Definición:** Proporción de ventas realizadas con descuento frente al total.
- **Fórmula:** € ventas con descuento ÷ € ventas totales.
- **Unidad:** %.
- **Fuente de datos (sistemas):** POS/eCommerce + motor de promociones + BI.
- **Nivel de cálculo:** ticket | SKU | tienda | canal | semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Retail Director / Pricing
- **Umbral/Objetivo:** ↓ pp vs baseline sin caer conversión; fijar límites por categoría/temporada.
- **Notas operativas:** Separar descuento explícito vs cupones/beneficios del programa (earn & burn) para evitar doble conteo.
- **Sesgos comunes / Riesgos de interpretación:** Reducir markdown puede bajar volumen si no se acompaña de valor percibido (experiencias/estatus).
- **Relación con Convercus:** Convercus permite sustituir descuento plano por recompensas/estatus (no precio), segmentar elegibilidad y aplicar caps por margen.
- **Compuerta de piloto (Gate):** sí (guardarraíl económico).
- **Estado de calidad de dato:** A/B

### KPI-102 — Dilución de margen por descuento (Discount Dilution)
- **Definición:** Pérdida de margen atribuible a descuentos vs un escenario de referencia sin descuento.
- **Fórmula:** (Margen sin descuento − margen real) ÷ margen sin descuento.
- **Unidad:** % (+ €).
- **Fuente de datos (sistemas):** Finance + BI merchandising + pricing.
- **Nivel de cálculo:** SKU | categoría | canal | semana
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** Finance BP + Merchandising
- **Umbral/Objetivo:** ≤ baseline; umbral máximo por categoría (política de rentabilidad).
- **Notas operativas:** Definir baseline y controlar por mix. Incluir efectos de devoluciones y costes variables.
- **Sesgos comunes / Riesgos de interpretación:** Si baseline está mal definido, la dilución se subestima y se “compra” sell-through.
- **Relación con Convercus:** Convercus: gobernanza de incentivos (caps) + reglas por margen + personalización → medir CM neta por cohorte.
- **Compuerta de piloto (Gate):** sí.
- **Estado de calidad de dato:** B

### KPI-103 — Tasa de devoluciones (Return Rate) — moda
- **Definición:** Porcentaje de unidades (y €) devueltas respecto a ventas en una ventana.
- **Fórmula:** Unidades devueltas ÷ unidades vendidas (reportar también €).
- **Unidad:** %.
- **Fuente de datos (sistemas):** OMS/returns + POS/eCommerce + logística inversa.
- **Nivel de cálculo:** pedido | SKU | talla | canal | cohorte
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** eCommerce Ops / Operaciones
- **Umbral/Objetivo:** ↓ pp vs baseline sin deteriorar conversión; target por categoría (calzado suele diferir).
- **Notas operativas:** Separar devoluciones por talla, calidad, daño y logística. Medir impacto en margen (reacondicionado).
- **Sesgos comunes / Riesgos de interpretación:** Bajar devoluciones puede subir fricción si se endurecen políticas; medir junto a NPS.
- **Relación con Convercus:** Convercus: journeys post-compra (guía talla/cuidado), incentivos por cambios vs devoluciones, comunicación y soporte.
- **Compuerta de piloto (Gate):** sí (si devoluciones suben, el piloto puede destruir margen).
- **Estado de calidad de dato:** B

### KPI-104 — Cobertura de inventario (Weeks of Supply / Stock Cover)
- **Definición:** Semanas de venta cubiertas por el inventario disponible al ritmo actual.
- **Fórmula:** Inventario disponible ÷ ventas semanales (promedio móvil).
- **Unidad:** semanas.
- **Fuente de datos (sistemas):** ERP/Inventario + POS/eCommerce + BI.
- **Nivel de cálculo:** SKU | tienda | canal | semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Planning / Supply Chain
- **Umbral/Objetivo:** Mantener en rango objetivo por categoría (evitar sobrestock y roturas).
- **Notas operativas:** Separar inventario “vendible” vs bloqueado (daños, tránsito). Normalizar por estacionalidad.
- **Sesgos comunes / Riesgos de interpretación:** Cover alto puede ocultar sobrecompra; cover bajo puede ocultar roturas de talla.
- **Relación con Convercus:** Convercus: mejora señal de demanda (identificación + preferencias) y activa reequilibrio por reglas/campañas.
- **Compuerta de piloto (Gate):** no (operativo; se usa con sell-through y OOS).
- **Estado de calidad de dato:** B

### KPI-105 — GMROI (retorno de margen sobre inventario)
- **Definición:** Margen bruto generado por euro invertido en inventario en una ventana.
- **Fórmula:** Margen bruto ÷ inventario medio a coste.
- **Unidad:** ratio.
- **Fuente de datos (sistemas):** Finance + ERP inventario + BI.
- **Nivel de cálculo:** categoría | tienda | canal | temporada
- **Frecuencia de medición:** mensual
- **Owner (responsable):** CFO + Merchandising
- **Umbral/Objetivo:** ↑ vs baseline; priorizar categorías con GMROI alto en surtido/campañas.
- **Notas operativas:** Acordar coste (FIFO/avg) y ventana. Ajustar por devoluciones y markdown.
- **Sesgos comunes / Riesgos de interpretación:** Interpretación errónea si no se ajusta por devoluciones o si el inventario medio está mal calculado.
- **Relación con Convercus:** Convercus: incentivos y journeys para mover categorías rentables sin acudir a markdown masivo.
- **Compuerta de piloto (Gate):** sí (en decisiones de escalado por categoría).
- **Estado de calidad de dato:** C→B

### KPI-106 — Índice de disponibilidad de tallas (Size Availability Index)
- **Definición:** Disponibilidad de tallas clave por SKU/categoría frente a la curva objetivo.
- **Fórmula:** Tallas clave disponibles ÷ tallas clave objetivo (ponderado por demanda).
- **Unidad:** índice (0–1) o %.
- **Fuente de datos (sistemas):** ERP/Inventario + planogramas + BI merchandising.
- **Nivel de cálculo:** SKU | talla | tienda | semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Merchandising / Store Ops
- **Umbral/Objetivo:** ↑ vs baseline; minimizar “huecos” en tallas top.
- **Notas operativas:** Definir tallas clave por categoría/mercado. Usar ponderación por ventas históricas.
- **Sesgos comunes / Riesgos de interpretación:** Sin ponderación, el índice es engañoso; tallas raras distorsionan.
- **Relación con Convercus:** Convercus: usa preferencias y compras previas para ajustar surtido y campañas por tienda/segmento.
- **Compuerta de piloto (Gate):** no.
- **Estado de calidad de dato:** C

### KPI-107 — Rotura de stock (OOS) — moda
- **Definición:** Porcentaje de oportunidades de venta perdidas por falta de stock (SKU/talla).
- **Fórmula:** Eventos OOS ÷ eventos de demanda (o lost sales estimadas).
- **Unidad:** % (o € lost sales).
- **Fuente de datos (sistemas):** POS/eCommerce + inventario + analítica de demanda.
- **Nivel de cálculo:** SKU | talla | tienda | canal | día/semana
- **Frecuencia de medición:** diario/semanal
- **Owner (responsable):** Store Ops + Supply Chain
- **Umbral/Objetivo:** ↓ vs baseline; objetivo por tienda y categoría.
- **Notas operativas:** Distinguir OOS real vs visibilidad (inventario no sincronizado).
- **Sesgos comunes / Riesgos de interpretación:** Medir OOS sin lost sales puede infravalorar el impacto; riesgo de subregistro.
- **Relación con Convercus:** Convercus: omnicanalidad (ship-from-store/BOPIS) + journeys de sustitución/recomendación.
- **Compuerta de piloto (Gate):** sí (guardarraíl de experiencia y revenue).
- **Estado de calidad de dato:** B


## 5) Supermercados de alimentación y hogar — Módulo sectorial (KPI-150–199)

Este módulo incorpora métricas de **ejecución en tienda** (OSA), **frescos** (merma) y disciplina promocional propia de supermercados.

### KPI-150 — Disponibilidad en lineal (On-Shelf Availability, OSA)
- **Definición:** Porcentaje de tiempo/SKU en el que el producto está disponible en estantería (no solo en inventario).
- **Fórmula:** SKU-horas disponibles ÷ SKU-horas planificadas (o % planogram cumplido).
- **Unidad:** %.
- **Fuente de datos (sistemas):** ERP + sistemas tienda (inventario) + auditorías/vision (si existe) + POS.
- **Nivel de cálculo:** SKU | tienda | día | franja
- **Frecuencia de medición:** diario/semanal
- **Owner (responsable):** Store Ops / Operaciones
- **Umbral/Objetivo:** ≥ umbral (p. ej., 95%) en categorías críticas; prioridad frescos y top sellers.
- **Notas operativas:** Separar “stock en trastienda” vs “en lineal”. Definir catálogo objetivo por tienda.
- **Sesgos comunes / Riesgos de interpretación:** Medir solo inventario oculta roturas en estantería; sesgo por auditoría parcial.
- **Relación con Convercus:** Convercus: triggers y misiones para personal/tienda (gobernanza), y para clientes (sustitución) si aplica.
- **Compuerta de piloto (Gate):** sí (si OSA cae, el piloto no puede demostrar uplift sostenible).
- **Estado de calidad de dato:** B

### KPI-151 — Merma en frescos (Fresh Waste Rate)
- **Definición:** Pérdida por caducidad/deterioro en categorías frescas respecto a ventas o recepción.
- **Fórmula:** € merma ÷ € ventas (o unidades mermadas ÷ unidades recibidas).
- **Unidad:** % (+ €).
- **Fuente de datos (sistemas):** ERP inventario + mermas + POS; registros de caducidad/temperatura si existen.
- **Nivel de cálculo:** categoría | tienda | día/semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Category Manager (Frescos) + Store Ops
- **Umbral/Objetivo:** ↓ vs baseline; umbrales por categoría (pan, fruta, lácteos, etc.).
- **Notas operativas:** Definir merma “evitable” vs “inevitable”. Ajustar por promociones y temperatura.
- **Sesgos comunes / Riesgos de interpretación:** Reducir merma puede subir roturas si se recorta demasiado; leer junto a OSA.
- **Relación con Convercus:** Convercus: campañas antiestacionalidad y bundles para mover inventario cercano a caducidad sin descuento agresivo; reglas por margen.
- **Compuerta de piloto (Gate):** sí (guardarraíl de rentabilidad).
- **Estado de calidad de dato:** B

### KPI-152 — Shrinkage (pérdidas desconocidas / hurto)
- **Definición:** Pérdidas por diferencias inventario teórico vs físico (hurto, errores, mermas no registradas).
- **Fórmula:** (Inventario teórico − inventario físico) ÷ ventas (o ÷ inventario).
- **Unidad:** % (+ €).
- **Fuente de datos (sistemas):** ERP + inventarios físicos + POS + seguridad.
- **Nivel de cálculo:** tienda | categoría | mes
- **Frecuencia de medición:** mensual (con señales semanales)
- **Owner (responsable):** Loss Prevention / Operaciones
- **Umbral/Objetivo:** ≤ umbral interno; objetivo por tienda y categoría de riesgo.
- **Notas operativas:** Alinear calendarios de inventario físico. Separar pérdidas conocidas (merma) de desconocidas.
- **Sesgos comunes / Riesgos de interpretación:** Cambios en metodología de conteo distorsionan; riesgo de atribución incorrecta.
- **Relación con Convercus:** Convercus: apoyo indirecto (segmentación de campañas reduce incentivos a fraude en redenciones; trazabilidad).
- **Compuerta de piloto (Gate):** no (no es KPI primario de piloto, pero sí de gobernanza).
- **Estado de calidad de dato:** C

### KPI-153 — Índice de precio de cesta (Price Index)
- **Definición:** Comparativo de precio relativo frente a competidores para una cesta representativa.
- **Fórmula:** Σ precio cesta propia ÷ Σ precio cesta competidor (ponderado).
- **Unidad:** índice.
- **Fuente de datos (sistemas):** Pricing + scraping/benchmarks + BI.
- **Nivel de cálculo:** cesta | tienda | zona | semana
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** Pricing / Comercial
- **Umbral/Objetivo:** Mantener dentro de banda objetivo por zona; evitar erosión de margen.
- **Notas operativas:** Definir cesta por misión (reposición, conveniencia, hogar). Mantener ponderaciones estables.
- **Sesgos comunes / Riesgos de interpretación:** Cambios de cesta o competencia distorsionan; comparar sin mix comparable es inválido.
- **Relación con Convercus:** Convercus: permite competir con valor (recompensas/beneficios) sin bajar precio linealmente; segmentación por sensibilidad.
- **Compuerta de piloto (Gate):** sí (si price index se degrada y margen cae, ajustar estrategia).
- **Estado de calidad de dato:** B

### KPI-154 — Efectividad promocional incremental (Promo Uplift)
- **Definición:** Incremento neto atribuible a una promoción/campaña frente a baseline/control (unidades y margen).
- **Fórmula:** (Ventas tratadas − ventas control) ÷ ventas control (y CM incremental).
- **Unidad:** % (+ € CM).
- **Fuente de datos (sistemas):** POS + BI + segmentación/cohortes; catálogo de promos.
- **Nivel de cálculo:** campaña | tienda | cohorte | semana
- **Frecuencia de medición:** semanal por campaña
- **Owner (responsable):** CRM/Trade Marketing + Finance BP
- **Umbral/Objetivo:** CM incremental ≥ 0 y uplift significativo; evitar canibalización.
- **Notas operativas:** Usar holdout o geo-test. Reportar canibalización y stockouts.
- **Sesgos comunes / Riesgos de interpretación:** Uplift aparente por estacionalidad o por rotura de stock en control.
- **Relación con Convercus:** Convercus: habilita A/B por cohortes, reglas de elegibilidad y caps por margen.
- **Compuerta de piloto (Gate):** sí (gate de escalado de campaña).
- **Estado de calidad de dato:** B

### KPI-155 — Share de marca propia (Private Label Share)
- **Definición:** Proporción de ventas atribuible a marca propia.
- **Fórmula:** € ventas marca propia ÷ € ventas totales.
- **Unidad:** %.
- **Fuente de datos (sistemas):** POS + BI categoría.
- **Nivel de cálculo:** categoría | tienda | semana
- **Frecuencia de medición:** mensual
- **Owner (responsable):** Category Management
- **Umbral/Objetivo:** ↑ vs baseline en categorías objetivo, sin degradar satisfacción.
- **Notas operativas:** Separar categorías donde la marca propia es estratégica vs no. Controlar precio relativo.
- **Sesgos comunes / Riesgos de interpretación:** Subir share puede bajar tráfico si se sacrifica surtido; medir junto a NPS y OSA.
- **Relación con Convercus:** Convercus: misiones y beneficios por descubrimiento de marca propia; personalización por sensibilidad al precio.
- **Compuerta de piloto (Gate):** no.
- **Estado de calidad de dato:** A/B


## 6) Viajes (Agencias, Mayoristas y Destinos) — Módulo sectorial normalizado

Este módulo incorpora el diccionario sectorial de **Viajes** dentro de la ontología del KPI Dictionary: cada KPI conserva los campos de **auditabilidad** (fuente + fórmula), **operabilidad** (cadencia + owner) y **vinculación** (capacidad → palanca → mecanismo → validación incremental).

Convención crítica sectorial: en viajes, **Volumen bruto de reservas (Gross Bookings/TTV)** no equivale a **Ingresos netos (Net Revenue)**; por ello se separan explícitamente volumen, ingreso y margen en las fichas. 


### Propósito

Este documento unifica y normaliza dos anexos sectoriales de Viajes bajo la ontología operativa del **KPI Dictionary**: cada KPI debe poder **auditarse** (fuente + fórmula), **operarse** (cadencia + owner) y **vincularse** (cómo lo mueve Convercus y bajo qué condiciones).

> Convención crítica (viajes): **Gross Bookings/TTV ≠ Ingresos**. El volumen transaccionado no es ingreso contable; por ello el diccionario separa **volumen**, **ingreso** y **margen**.

---

---

### Fuentes de datos (taxonomía mínima)

1. **Motor de reservas / eCommerce / App**: sesiones, búsquedas, cotizaciones, conversiones, atribución.
2. **Backoffice (mid-office)**: expedientes, PNR, confirmaciones, modificaciones, cancelaciones.
3. **Pagos (PSP) y conciliación**: cobros, devoluciones, contracargos, fraude, comisiones.
4. **CRM/CDP**: identidad cliente, cohortes, CLV, segmentación.
5. **Contact center / Helpdesk**: tickets, AHT, FCR, SLAs, motivos.
6. **Revenue/Yield** (mayoristas): cupos, ocupación, spoilage, pricing, forecasting.
7. **Convercus**: journeys, eventos, incentivos, “ganar y canjear”, socios, gamificación, trazabilidad omnicanal.

---

### KPI norte recomendado por subsector

#### Agencias (B2C / B2B2C)
- **Norte:** Margen de contribución por cliente + Tasa de repetición.
- **Control:** Cancelación, Refund cycle time, Cost-to-serve por reserva.

#### Mayoristas / Turoperadores
- **Norte:** Margen neto por salida/paquete + Utilización de cupos (sin dilución).
- **Control:** Spoilage, Dilución por descuentos, Cancelaciones.

#### Destinos (DMO/NTO/RTO/LTO)
- **Norte:** Gasto diario por visitante + Estancia media + Dispersión territorial (si se gestiona presión de flujos).
- **Control:** Estacionalidad, Activación de socios, Capacidad de carga (cuando aplique).

---

### Diccionario de KPIs — Normalizado (v1.1)

#### A) Economía del negocio (P&L / unidad económica)

##### KPI-050 — Volumen bruto de reservas (Gross Bookings / TTV)
- **Definición:** valor total de viajes vendidos en un periodo (no ingreso).
- **Fórmula:** Σ importe bruto de reservas confirmadas.
- **Unidad:** € (segmentar por canal, producto, mercado, tienda/agente).
- **Fuente de datos (sistemas):** Backoffice/mid-office (expedientes, PNR, confirmaciones) + BI comercial; (opcional) motor de reservas para conciliación.
- **Nivel de cálculo:** reserva | producto | canal | mercado | tienda/agente | cohorte (si cliente identificado)
- **Frecuencia de medición:** diario (operación) | mensual (dirección)
- **Owner (responsable):** Dirección Comercial / BI Comercial.
- **Umbral/Objetivo:** ↑ vs baseline y vs plan; condicionado a que no se deteriore el margen (ver KPI-053 y KPI-070).
- **Notas operativas:** Aclarar: (i) moneda y tipo de cambio; (ii) incluye/excluye impuestos; (iii) incluye ancillaries o se reporta separado; (iv) criterio de “confirmación” (pago capturado, billete emitido, etc.).
- **Sesgos comunes / Riesgos de interpretación:** crecer en volumen con caída de margen.
- **Relación con Convercus:** Capacidad: *Journeys + omnicanalidad + venta social* → palanca: captación/reactivación y conversión asistida → mecanismo: segmentación, misiones, incentivos no monetarios y trazabilidad de canal → validación: cohortes tratadas vs holdout (o matching) separando canal directo/intermediado.
- **Compuerta de piloto (Gate):** no (KPI de contexto; se usa para lectura de escala, no como prueba de ROI por sí solo).
- **Estado de calidad de dato:** A/B

##### KPI-051 — Ingresos netos (Net Revenue)
- **Definición:** ingresos atribuibles tras comisiones/fees/mark-ups y ajustes (cancelaciones, devoluciones, incentivos).
- **Fórmula:** comisiones + fees + mark-ups + otros − contraingresos/ajustes.
- **Unidad:** €.
- **Fuente de datos (sistemas):** ERP/Finance + conciliación PSP; (puente) backoffice para estado de reserva y ajustes.
- **Nivel de cálculo:** reserva | cliente | canal | línea de negocio (agency vs merchant) | cohorte
- **Frecuencia de medición:** semanal (control) | mensual (cierre)
- **Owner (responsable):** CFO / Controller.
- **Umbral/Objetivo:** ↑ vs baseline en cohortes tratadas; *guardarraíl*: no aceptar uplift si KPI-053 (margen de contribución) cae.
- **Notas operativas:** Normalizar por modelo: *agency* (comisión) vs *merchant* (ingreso bruto). Definir tratamiento de incentivos (rebates/canje) y momento de reconocimiento (accrual vs cash).  
  **Equivalencia (core):** KPI-001.
- **Sesgos comunes / Riesgos de interpretación:** modelos contables distintos por línea (agency vs merchant).
- **Relación con Convercus:** Capacidad: *programa (ganar y canjear) + journeys + personalización* → palanca: sustituir descuento plano por recompensas/experiencias y elevar attach rate → mecanismo: incentivos con guardarraíles por margen y reglas de elegibilidad → validación: uplift en net revenue por cohorte vs control, neteando coste de incentivos y canibalización.
- **Compuerta de piloto (Gate):** sí (si net revenue no crece o crece “a costa” de margen, se ajustan mecánicas).
- **Estado de calidad de dato:** B

##### KPI-052 — Tasa de captura (Take Rate / Revenue Margin)
- **Definición:** % del volumen bruto capturado como ingreso.
- **Fórmula:** ingresos (según definición interna) ÷ gross bookings.
- **Unidad:** %.
- **Fuente de datos (sistemas):** ERP/Finance (ingresos) + backoffice/BI comercial (gross bookings).
- **Nivel de cálculo:** canal | producto | mercado | línea (agency/merchant) | cohorte
- **Frecuencia de medición:** mensual.
- **Owner (responsable):** CFO + Pricing/Comercial.
- **Umbral/Objetivo:** ↑ pp vs baseline en categorías objetivo; evitar degradación de conversión (ver KPI-056) y aumento de incidencias (ver KPI-060–114).
- **Notas operativas:** No comparar take rate entre modelos sin normalizar. Definir si el numerador usa *net revenue* contable o una aproximación operativa.
- **Sesgos comunes / Riesgos de interpretación:** comparar take rate entre modelos sin normalizar (grave en M&A).
- **Relación con Convercus:** Capacidad: *personalización + gestión de incentivos + programa de socios* → palanca: reducir fugas de margen y mejorar mix → mecanismo: reglas por producto/canal, incentivos por comportamiento (no por precio) → validación: análisis por cohortes con control de mix (antes/después + control) y reconciliación contable.
- **Compuerta de piloto (Gate):** sí (especialmente en consolidación/M&A y en escalado de programa).
- **Estado de calidad de dato:** B

##### KPI-053 — Margen de contribución (por reserva / por cliente / por canal)
- **Definición:** margen tras costes variables atribuibles (pagos, marketing variable, servicio variable, incentivos).
- **Fórmula:** net revenue − costes variables atribuibles.
- **Unidad:** € y %.
- **Fuente de datos (sistemas):** Finance (P&L) + modelo de asignación de costes; PSP; contact center/helpdesk; (si aplica) logística de documentos/ticketing.
- **Nivel de cálculo:** reserva | cliente | canal | cohorte | producto
- **Frecuencia de medición:** mensual.
- **Owner (responsable):** Finance Business Partner / Controller.
- **Umbral/Objetivo:** ≥ baseline en cohortes tratadas; en piloto, priorizar *CM por reserva* y *CM por cliente* para evitar “comprar ventas”.
- **Notas operativas:** Definir coste variable por ruta/canal (web vs tienda vs call center). Incluir posventa, refunds y contracargos en el modelo; separar costes fijos (no atribuirlos como variable).  
  **Equivalencia (core):** KPI-003.
- **Sesgos comunes / Riesgos de interpretación:** margen “inflado” si no se imputa posventa y reembolsos.
- **Relación con Convercus:** Capacidad: *journeys (pre/durante/post) + omnicanalidad + gobernanza de incentivos* → palanca: menos cancelación/refund, más autoservicio, más attach rate → mecanismo: nudges, misiones, recompensas y reglas de elegibilidad por margen → validación: uplift de CM por cohorte vs holdout, neteando coste de incentivos y cambios de mix.
- **Compuerta de piloto (Gate):** sí (KPI central de decisión: si CM cae, se rediseña el programa).
- **Estado de calidad de dato:** B/C

##### KPI-054 — CAC (Coste de adquisición de cliente)
- **Definición:** coste total de adquisición de un nuevo cliente activado.
- **Fórmula:** gasto de adquisición atribuible ÷ # nuevos clientes activados (con reserva o criterio acordado).
- **Unidad:** €/cliente.
- **Fuente de datos (sistemas):** Marketing spend (ad platforms) + atribución (analytics) + CRM/CDP; (si hay tienda/call center) sistema de leads y conversión asistida.
- **Nivel de cálculo:** cohorte (alta/primer contacto) | canal | campaña | mercado
- **Frecuencia de medición:** semanal (canales), mensual (dirección).
- **Owner (responsable):** CMO / Growth Lead.
- **Umbral/Objetivo:** ↓ vs baseline sin degradar calidad (ver cancelación, refund, chargebacks). En pilot, fijar rango objetivo por canal.
- **Notas operativas:** Definir “activación” (p. ej., 1ª reserva confirmada) y ventana de atribución. Separar nuevos clientes vs reactivados.
- **Sesgos comunes / Riesgos de interpretación:** medir leads en lugar de clientes activados.
- **Relación con Convercus:** Capacidad: *venta social + journeys de registro/opt-in + referrals* → palanca: captar con menor coste y mayor intención → mecanismo: rutas de captación con incentivo no monetario, trazabilidad de agente y campaña → validación: comparación por cohortes/canales con holdout de incentivo (o geo-test) y control de estacionalidad.
- **Compuerta de piloto (Gate):** sí (si CAC se dispara o baja a costa de peor calidad, se corrige).
- **Estado de calidad de dato:** B

##### KPI-055 — CLV/LTV (Valor de vida del cliente)
- **Definición:** valor económico esperado del cliente en el tiempo.
- **Fórmula:** Σ margen cohorte − Σ coste de servicio cohorte (con retención).
- **Unidad:** €/cliente.
- **Fuente de datos (sistemas):** CRM/CDP (cohortes + retención) + Finance (margen) + Helpdesk/PSP (cost-to-serve, refunds, contracargos).
- **Nivel de cálculo:** cohorte | cliente | segmento
- **Frecuencia de medición:** mensual (cohortes), trimestral (modelo).
- **Owner (responsable):** CMO + CFO.
- **Umbral/Objetivo:** Uplift vs control por cohorte; en piloto 12 semanas usar *proxies* (repeat, attach, cancelación, cost-to-serve).
- **Notas operativas:** Evitar LTV “solo ingresos”: incorporar refunds, incidencias y coste de servicio. Definir horizonte (6/12/24m) y, si aplica, tasa de descuento.  
  **Equivalencia (core):** KPI-014.
- **Sesgos comunes / Riesgos de interpretación:** sobreestimar si se ignoran incidencias, reembolsos y contracargos.
- **Relación con Convercus:** Capacidad: *journeys post-viaje + estatus/niveles + canje* → palanca: más repetición rentable y menor coste de servicio → mecanismo: misiones post-trip, recompensas por comportamiento y programa de socios → validación: modelado por cohortes con holdout (o test por mercado) y reconciliación con CM incremental.
- **Compuerta de piloto (Gate):** no en piloto corto (se usa para escalado; en 12 semanas se priorizan leading indicators).
- **Estado de calidad de dato:** C→B


#### B) Embudo de demanda y distribución

##### KPI-056 — Conversión por etapa (y conversión total)
- **Definición:** % que avanza en el embudo (visita→búsqueda→cotización→reserva).
- **Fórmula:** etapa(t+1) ÷ etapa(t).
- **Unidad:** %.
- **Fuente de datos (sistemas):** Analítica web/app (GA/Adobe), motor de reservas, logs de búsqueda/cotización; para tienda/call center: CRM y sistema de ventas asistidas.
- **Nivel de cálculo:** etapa | canal | campaña | dispositivo | cohorte
- **Frecuencia de medición:** diaria/semanal.
- **Owner (responsable):** Head of Digital / eCommerce.
- **Umbral/Objetivo:** ↑ vs baseline; *guardarraíles*: no elevar conversión si aumenta cancelación/refund/chargeback (KPI-060–114).
- **Notas operativas:** Alinear definición de eventos entre canales (online, tienda, call center). Tratar bots, cambios de tracking y ventanas de atribución.  
  **Equivalencia (core):** KPI-033.
- **Sesgos comunes / Riesgos de interpretación:** medir solo online (ignorar tienda/call center).
- **Relación con Convercus:** Capacidad: *omnicanalidad + journeys de recuperación + venta social* → palanca: reducir fricción y recuperar intención → mecanismo: reminders, re-contacto asistido, ofertas personalizadas y trazabilidad de agente → validación: A/B de journeys (expuesto vs control) y análisis por canal con matching.
- **Compuerta de piloto (Gate):** sí (si el embudo no mejora, no hay base para uplift económico).
- **Estado de calidad de dato:** A/B

##### KPI-057 — Look-to-Book (L2B)
- **Definición:** búsquedas (“looks”) por cada reserva (“book”); proxy de eficiencia de shopping/coste infra.
- **Fórmula:** # looks ÷ # books.
- **Unidad:** ratio.
- **Fuente de datos (sistemas):** Logs del motor de reservas; integraciones GDS/NDC (cuando aplique); analítica digital.
- **Nivel de cálculo:** búsqueda | reserva | canal | proveedor | mercado
- **Frecuencia de medición:** diaria/semanal.
- **Owner (responsable):** Digital + Tecnología.
- **Umbral/Objetivo:** ↓ vs baseline manteniendo conversión y margen (evitar “bajar looks” a costa de menos intención).
- **Notas operativas:** Normalizar por mix de producto (vuelo vs paquete) y por proveedor. Tener en cuenta que iniciativas de inspiración pueden aumentar “looks” legítimamente.
- **Sesgos comunes / Riesgos de interpretación:** iniciativas de inspiración/IA pueden inflar “looks” sin elevar reservas.
- **Relación con Convercus:** Capacidad: *segmentación + personalización + journeys por intención* → palanca: filtrar tráfico no productivo y acelerar decisión → mecanismo: recomendaciones, bundles, triggers por intención → validación: test A/B de personalización (impacto en conversión y CM), controlando mix.
- **Compuerta de piloto (Gate):** no (métrica operativa; se usa como señal de eficiencia).
- **Estado de calidad de dato:** B

##### KPI-058 — Mix de canal (directo vs intermediado)
- **Definición:** distribución de volumen e ingresos por canal (web, tienda, call center, afiliación, OTA, B2B).
- **Fórmula:** % del total por canal (volumen e ingresos).
- **Unidad:** % + €.
- **Fuente de datos (sistemas):** BI consolidado (DWH) + atribución omnicanal; backoffice (ventas); ERP (ingresos).
- **Nivel de cálculo:** canal | tienda/agente | mercado | cohorte
- **Frecuencia de medición:** semanal/mensual.
- **Owner (responsable):** Dirección Comercial / Growth.
- **Umbral/Objetivo:** ↑ canal directo (si es objetivo) sin deteriorar conversión total ni aumentar cost-to-serve.
- **Notas operativas:** Definir claramente “directo” (incluye call center, tiendas y mensajería) y “intermediado”. Alinear incentivos internos para evitar conflicto de canal.
- **Sesgos comunes / Riesgos de interpretación:** conflicto interno si incentivos no están alineados.
- **Relación con Convercus:** Capacidad: *omnicanalidad + venta social + journeys coherentes* → palanca: capturar demanda en canal más rentable → mecanismo: incentivos diferenciales por canal, trazabilidad y continuidad de experiencia → validación: pilotos por segmento/canal con holdout y análisis de CM por canal.
- **Compuerta de piloto (Gate):** sí (si el programa genera desplazamientos no deseados de canal, se corrige).
- **Estado de calidad de dato:** B

##### KPI-059 — Attach Rate (servicios complementarios)
- **Definición:** % de reservas con servicios complementarios (seguro, equipaje, actividades, upgrades).
- **Fórmula:** # reservas con ancillary ÷ # reservas totales.
- **Unidad:** % + margen incremental.
- **Fuente de datos (sistemas):** Backoffice/mid-office + partners (seguro/actividades) + BI; ERP para margen.
- **Nivel de cálculo:** reserva | producto | canal | cohorte
- **Frecuencia de medición:** semanal.
- **Owner (responsable):** Product / Partnerships.
- **Umbral/Objetivo:** ↑ pp vs baseline en segmentos objetivo; *guardarraíl*: no aumentar incidencias/refunds por mala recomendación.
- **Notas operativas:** Separar attach rate por tipo de ancillary y por momento (pre-trip vs checkout). Medir elasticidad por segmento.
- **Sesgos comunes / Riesgos de interpretación:** subir attach rate con producto incorrecto aumenta incidencias y devoluciones.
- **Relación con Convercus:** Capacidad: *journeys pre-viaje + personalización + gamificación “viaje completo”* → palanca: upsell/cross-sell relevante → mecanismo: triggers por intención, bundles, recompensas por completar servicios → validación: A/B de oferta/trigger y medición de margen incremental neto (incl. refunds/chargebacks).
- **Compuerta de piloto (Gate):** sí (métrica de monetización incremental, pero sujeta a guardarraíles operativos).
- **Estado de calidad de dato:** B


#### C) Cancelaciones, cambios, reembolsos y contracargos

##### KPI-060 — Tasa de cancelación
- **Definición:** Porcentaje de reservas confirmadas que se cancelan en una ventana definida.
- **Fórmula:** # cancelaciones ÷ # reservas confirmadas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** Backoffice/mid-office (estado de reserva) + BI; (opcional) motor de reservas para eventos.
- **Nivel de cálculo:** reserva | producto | canal | tarifa | cohorte
- **Frecuencia de medición:** diaria/semanal.
- **Owner (responsable):** Operaciones + Comercial (políticas).
- **Umbral/Objetivo:** ↓ pp vs baseline en cohortes tratadas; o “cambiar cancelación por modificación” cuando sea preferible (ver KPI-061).
- **Notas operativas:** Normalizar por reglas tarifarias y por ventana (24h/7d/30d). Separar cancelaciones voluntarias vs por disrupción del proveedor.
- **Sesgos comunes / Riesgos de interpretación:** comparar sin normalizar condiciones tarifarias.
- **Relación con Convercus:** Capacidad: *journeys proactivos + autoservicio + comunicación omnicanal* → palanca: reducir cancelación evitable → mecanismo: recordatorios, opciones de cambio, transparencia de políticas → validación: test en cohortes con holdout y control por tipo de tarifa.
- **Compuerta de piloto (Gate):** sí (si sube, el piloto puede estar generando fricción o mala expectativa).
- **Estado de calidad de dato:** A/B

##### KPI-061 — Tasa de cambios/modificaciones
- **Definición:** Porcentaje de reservas confirmadas que se modifican (fechas, nombres, servicios, itinerario) en una ventana definida.
- **Fórmula:** # reservas modificadas ÷ # reservas confirmadas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** Backoffice + contact center/helpdesk; motor de reservas (si registra cambios).
- **Nivel de cálculo:** reserva | producto | canal | cohorte
- **Frecuencia de medición:** semanal.
- **Owner (responsable):** Operaciones.
- **Umbral/Objetivo:** Interpretación contextual: puede ↑ si se incentiva “cambiar vs cancelar” (positivo) siempre que CM y cost-to-serve no empeoren.
- **Notas operativas:** Definir qué cuenta como cambio (menor vs mayor) y si se originó en autoservicio o agente. Medir impacto en coste de servicio.
- **Sesgos comunes / Riesgos de interpretación:** autoservicio débil sube carga del contact center.
- **Relación con Convercus:** Capacidad: *autoservicio guiado + journeys pre-viaje* → palanca: permitir cambios rápidos y reducir cancelación → mecanismo: flows de modificación, checklists, comunicación → validación: análisis causal (cohortes expuestas) cruzando con KPI-064/116 (cost-to-serve/contact rate).
- **Compuerta de piloto (Gate):** sí (pero como KPI de control: si cambios ↑ y coste ↑, rediseñar).
- **Estado de calidad de dato:** B

##### KPI-062 — Tiempo de ciclo de reembolso (Refund Cycle Time)
- **Definición:** Tiempo medio/mediano desde que se inicia un reembolso hasta que se completa (en PSP y conciliación).
- **Fórmula:** avg(fecha refund_completed − fecha refund_initiated).
- **Unidad:** días.
- **Fuente de datos (sistemas):** PSP + conciliación + backoffice (estado de reserva) + ERP (asientos).
- **Nivel de cálculo:** transacción | reserva | canal | proveedor
- **Frecuencia de medición:** semanal.
- **Owner (responsable):** Payments / Finanzas operativas.
- **Umbral/Objetivo:** ↓ días vs baseline; *guardarraíl*: no aumentar contracargos por retrasos (ver KPI-063).
- **Notas operativas:** Separar por método de pago y por proveedor. Alinear SLA interno y comunicar estado al cliente (tracking).
- **Sesgos comunes / Riesgos de interpretación:** reembolso lento dispara tickets y deteriora reputación.
- **Relación con Convercus:** Capacidad: *journeys de transparencia + reglas automatizadas + mensajería omnicanal* → palanca: reducir ansiedad y contactos → mecanismo: notificaciones, tracking, autoservicio → validación: descenso de contact rate y chargeback en cohortes expuestas, con control temporal.
- **Compuerta de piloto (Gate):** sí (KPI crítico de operación y reputación).
- **Estado de calidad de dato:** A/B

##### KPI-063 — Tasa de contracargos (Chargeback Rate)
- **Definición:** Porcentaje (o proporción en €) de contracargos sobre transacciones en una ventana definida; incluye fraude y disputas.
- **Fórmula:** # contracargos ÷ # transacciones (o € contracargos ÷ € transaccionado).
- **Unidad:** % + €.
- **Fuente de datos (sistemas):** PSP + antifraude + conciliación; (contexto) CRM/helpdesk para motivo de disputa.
- **Nivel de cálculo:** transacción | canal | método de pago | mercado | cohorte
- **Frecuencia de medición:** semanal/mensual.
- **Owner (responsable):** Risk / Payments.
- **Umbral/Objetivo:** ≤ baseline; fijar umbral máximo por políticas del adquirente (y por riesgo reputacional).
- **Notas operativas:** Separar fraude real vs disputa por comunicación/servicio. En modelos con reembolso lento, monitorizar conjuntamente con KPI-062.
- **Sesgos comunes / Riesgos de interpretación:** separar fraude real de disputa por mala comunicación.
- **Relación con Convercus:** Capacidad: *trazabilidad omnicanal + soporte guiado + comunicación proactiva* → palanca: reducir disputas evitables → mecanismo: pruebas de servicio, confirmaciones claras, journeys de incidencia → validación: reducción de chargebacks por motivo en cohortes expuestas (y control por PSP/región).
- **Compuerta de piloto (Gate):** sí (riesgo financiero y de continuidad con PSP).
- **Estado de calidad de dato:** A/B


#### D) Operaciones y coste de servicio

##### KPI-064 — Cost-to-Serve por reserva
- **Definición:** Coste variable de operaciones/posventa por reserva (incluye atención, reemisiones, gestiones, costes PSP variables).
- **Fórmula:** coste variable operaciones/posventa ÷ # reservas.
- **Unidad:** €/reserva.
- **Fuente de datos (sistemas):** Finance + helpdesk/contact center (tiempos) + backoffice (tipos de gestión) + PSP (fees).
- **Nivel de cálculo:** reserva | canal | producto | cohorte
- **Frecuencia de medición:** mensual (con señales semanales).
- **Owner (responsable):** COO / Operaciones.
- **Umbral/Objetivo:** ↓ vs baseline (o mantener) mientras se incrementa Net Revenue/CM; fijar target por canal (tienda/call).
- **Notas operativas:** Requiere modelo de costes por tipo de interacción y por complejidad. Separar coste “evitable” (falta de info) vs “inevitable” (disrupción proveedor).  
  **Equivalencia (core):** KPI-032.
- **Sesgos comunes / Riesgos de interpretación:** sin imputación correcta, se toman decisiones a ciegas.
- **Relación con Convercus:** Capacidad: *journeys preventivos + omnicanalidad (contexto único) + autoservicio* → palanca: menos contactos y menos reprocesos → mecanismo: checklists, notificaciones, FAQ dinámica → validación: reducción de contact rate/AHT manteniendo CSAT, y mejora de CM neta en cohortes expuestas.
- **Compuerta de piloto (Gate):** sí (guardarraíl económico-operativo).
- **Estado de calidad de dato:** C→B

##### KPI-065 — Tasa de contacto del cliente por reserva (Contact Rate)
- **Definición:** Número medio de contactos/interacciones de atención por cada reserva (incluye canales digitales y voz).
- **Fórmula:** # contactos ÷ # reservas.
- **Unidad:** ratio.
- **Fuente de datos (sistemas):** CRM/helpdesk + contact center; backoffice para denominador (# reservas).
- **Nivel de cálculo:** reserva | canal | motivo | cohorte
- **Frecuencia de medición:** semanal.
- **Owner (responsable):** Contact Center Manager.
- **Umbral/Objetivo:** ↓ vs baseline sin deteriorar FCR/CSAT; fijar umbrales por motivo (refunds, cambios, incidencias).
- **Notas operativas:** Definir qué cuenta como “contacto” (mensaje, llamada, ticket) y deduplicación (múltiples canales por el mismo caso).
- **Sesgos comunes / Riesgos de interpretación:** bajar contactos a costa de CSAT/NPS.
- **Relación con Convercus:** Capacidad: *mensajería + autoservicio + journeys proactivos* → palanca: resolver antes de que el cliente contacte → mecanismo: notificaciones, tracking, resolución guiada → validación: A/B de journeys proactivos midiendo caída de contactos y mejora de CM neta.
- **Compuerta de piloto (Gate):** sí (guardarraíl de eficiencia; siempre junto a FCR/CSAT).
- **Estado de calidad de dato:** B

##### KPI-066 — Tiempo medio de gestión (AHT)
- **Definición:** Duración media por interacción (talk + hold + after-call work) en contact center.
- **Fórmula:** (talk + hold + after-call work) ÷ # interacciones.
- **Unidad:** minutos.
- **Fuente de datos (sistemas):** Plataforma de contact center (ACD) + helpdesk.
- **Nivel de cálculo:** interacción | motivo | agente | canal
- **Frecuencia de medición:** diaria/semanal.
- **Owner (responsable):** Contact Center Manager.
- **Umbral/Objetivo:** ↓ vs baseline sin caer FCR; objetivos por motivo (refund vs cambio) y por canal (voz vs mensajería).
- **Notas operativas:** AHT es métrica de eficiencia, no de calidad. Interpretar junto a FCR y CSAT.
- **Sesgos comunes / Riesgos de interpretación:** bajar AHT puede empeorar FCR.
- **Relación con Convercus:** Capacidad: *orquestación omnicanal + contexto único* → palanca: reducir tiempo de búsqueda y reprocesos → mecanismo: perfiles unificados, historial de journey, macros → validación: análisis antes/después en equipos adoptantes vs control.
- **Compuerta de piloto (Gate):** no (no debe ser gate único; se usa en balance).
- **Estado de calidad de dato:** A

##### KPI-067 — Resolución en primer contacto (FCR)
- **Definición:** % de casos/tickets resueltos en una única interacción (sin recontacto).
- **Fórmula:** tickets resueltos en 1 interacción ÷ tickets totales.
- **Unidad:** %.
- **Fuente de datos (sistemas):** Helpdesk/CRM + contact center; (si aplica) omnicanal event log para recontactos.
- **Nivel de cálculo:** ticket/caso | motivo | canal | cohorte
- **Frecuencia de medición:** semanal.
- **Owner (responsable):** Operaciones/Soporte.
- **Umbral/Objetivo:** ↑ pp vs baseline; objetivo diferencial por motivo (refunds, cambios, incidencias).
- **Notas operativas:** Normalizar definición entre canales (ticket vs chat). Definir ventana de “recontacto” (p. ej., 7 días).
- **Sesgos comunes / Riesgos de interpretación:** definiciones inconsistentes entre canales; normalizar.
- **Relación con Convercus:** Capacidad: *omnicanalidad (contexto único) + journeys de autoservicio* → palanca: resolver con menos fricción → mecanismo: guía paso a paso, tracking y contenido contextual → validación: pilotos por motivo con holdout midiendo FCR y caída de cost-to-serve.
- **Compuerta de piloto (Gate):** sí (si FCR no mejora, no hay eficiencia sostenible).
- **Estado de calidad de dato:** B


#### E) Mayoristas / Turoperadores (inventario, yield, estacionalidad)

##### KPI-068 — Utilización de cupos (Allotment Utilization)
- **Definición:** % de unidades asignadas/contratadas que se venden en un periodo/salida.
- **Fórmula:** unidades vendidas ÷ unidades asignadas (por salida/periodo).
- **Unidad:** %.
- **Fuente de datos (sistemas):** Sistemas de contracting + RM/yield + backoffice (ventas por salida).
- **Nivel de cálculo:** salida/paquete | periodo | canal/agencia | mercado
- **Frecuencia de medición:** semanal (temporada), mensual (dirección).
- **Owner (responsable):** Revenue/Yield.
- **Umbral/Objetivo:** ↑ vs baseline en salidas objetivo; *guardarraíl*: no aceptar ocupación si la dilución por descuentos aumenta (ver KPI-070).
- **Notas operativas:** Separar cupos garantizados vs bajo demanda. Cruzar siempre con margen por salida/paquete.
- **Sesgos comunes / Riesgos de interpretación:** ocupar “barato” no es éxito; cruzar con margen.
- **Relación con Convercus:** Capacidad: *gamificación early booking + activación de socios (agencias) + segmentación* → palanca: desplazar demanda a preventa → mecanismo: misiones/incentivos por anticipación y calidad → validación: test por agencia/mercado con control, midiendo margen neto por salida.
- **Compuerta de piloto (Gate):** sí (clave en mayoristas).
- **Estado de calidad de dato:** B

##### KPI-069 — Spoilage (pérdida por no venta)
- **Definición:** Proporción de unidades comprometidas que expiran sin vender (impacto directo en margen).
- **Fórmula:** unidades expiran sin vender ÷ unidades comprometidas.
- **Unidad:** % + € impacto.
- **Fuente de datos (sistemas):** RM/yield + contracting; BI para valoración del impacto.
- **Nivel de cálculo:** salida/paquete | periodo | canal/agencia
- **Frecuencia de medición:** semanal.
- **Owner (responsable):** Revenue + Contratación.
- **Umbral/Objetivo:** ↓ vs baseline en salidas objetivo; evitar compensarlo con descuentos agresivos que destruyen margen.
- **Notas operativas:** Valorar el impacto económico por unidad/paquete. Separar spoilage estructural (sobrecontratación) vs coyuntural (shock demanda).
- **Sesgos comunes / Riesgos de interpretación:** “esconder” spoilage vía descuentos agresivos.
- **Relación con Convercus:** Capacidad: *segmentación + journeys de reactivación + programa para agencias asociadas* → palanca: llenar valles sin discount creep → mecanismo: incentivos por ventana (early booking), bundles y recompensas no monetarias → validación: comparación por salidas y agencias con control, midiendo CM neta.
- **Compuerta de piloto (Gate):** sí.
- **Estado de calidad de dato:** B

##### KPI-070 — Dilución por descuentos (Discount Dilution)
- **Definición:** Pérdida relativa de margen atribuible a descuentos frente a un escenario sin descuento (baseline).
- **Fórmula:** (margen sin descuento − margen real) ÷ margen sin descuento.
- **Unidad:** % + €.
- **Fuente de datos (sistemas):** Pricing + BI + Finance; (si aplica) contracting/RM.
- **Nivel de cálculo:** salida/paquete | producto | canal | agencia | cohorte
- **Frecuencia de medición:** semanal en picos; mensual consolidado.
- **Owner (responsable):** Comercial + Revenue.
- **Umbral/Objetivo:** ↓ vs baseline; fijar límites por producto/temporada (guardarraíl de rentabilidad).
- **Notas operativas:** Definir baseline “sin descuento” y controlar por mix. Diferenciar descuento explícito vs rebates/incentivos indirectos.
- **Sesgos comunes / Riesgos de interpretación:** optimizar ocupación sacrificando rentabilidad.
- **Relación con Convercus:** Capacidad: *ganar y canjear + experiencias + gobernanza de incentivos* → palanca: sustituir rebaja por recompensas y segmentación → mecanismo: reglas por margen, elegibilidad y caps de coste → validación: comparación de CM neta en cohortes tratadas vs control manteniendo conversión.
- **Compuerta de piloto (Gate):** sí (métrica de disciplina).
- **Estado de calidad de dato:** B

##### KPI-071 — Precisión de previsión (Forecast Accuracy)
- **Definición:** Exactitud del forecast de demanda/ventas vs realización (por salida/periodo).
- **Fórmula:** MAPE u otra métrica estándar (definir en gobernanza).
- **Unidad:** % (o MAPE).
- **Fuente de datos (sistemas):** RM/yield + BI; (si aplica) señales digitales (motor de reservas) y CRM.
- **Nivel de cálculo:** salida/periodo | mercado | canal
- **Frecuencia de medición:** semanal/mensual.
- **Owner (responsable):** Revenue.
- **Umbral/Objetivo:** ↑ precisión vs baseline; en shocks, priorizar estabilidad metodológica y explicabilidad.
- **Notas operativas:** Documentar método (MAPE/WMAPE), horizonte (1/4/12 semanas) y tratamiento de outliers/shocks.
- **Sesgos comunes / Riesgos de interpretación:** previsión sin señales de intención falla en shocks.
- **Relación con Convercus:** Capacidad: *señales de intención (registro, interacción, wishlists) + journeys* → palanca: enriquecer modelos de demanda → mecanismo: captura de eventos y segmentación → validación: backtesting con y sin señales Convercus; pilotos por mercado.
- **Compuerta de piloto (Gate):** no (útil para madurez; no suele ser gate de piloto 12 semanas).
- **Estado de calidad de dato:** B


#### F) Destinos (economía del visitante y socios)

##### KPI-072 — Estancia media (Length of Stay, LoS)
- **Definición:** Número medio de noches/días por visitante o por estancia (según fuente).
- **Fórmula:** Σ noches ÷ # visitantes (o # estancias).
- **Unidad:** noches/días.
- **Fuente de datos (sistemas):** Observatorios/estadística alojamientos; (opcional) partners y datos agregados según acuerdos.
- **Nivel de cálculo:** visitante/estancia | mercado | temporada | zona
- **Frecuencia de medición:** mensual/trimestral.
- **Owner (responsable):** Observatorio / Dirección de análisis.
- **Umbral/Objetivo:** ↑ vs baseline (si es objetivo de destino) sin aumentar presión en zonas saturadas (ver KPI-075).
- **Notas operativas:** Aclarar fuente y sesgo (encuestas vs registros). Definir unidad (visitante vs estancia) y excluir day-trippers si aplica.
- **Sesgos comunes / Riesgos de interpretación:** Cambios de metodología estadística; sesgos por muestra; atribución débil.
- **Relación con Convercus:** Capacidad: *pasaporte de destino + journeys de itinerarios extendidos* → palanca: incentivar extensión de estancia → mecanismo: recompensas por hitos (2ª/3ª noche, rutas temáticas) → validación: tests geográficos o por cohortes (residentes vs visitantes) con control estacional.
- **Compuerta de piloto (Gate):** no (KPI de resultado macro; se usa en escalado y planificación).
- **Estado de calidad de dato:** C

##### KPI-073 — Gasto diario por visitante
- **Definición:** Gasto estimado por visitante y día (unidad típica para economía del visitante).
- **Fórmula:** gasto total estimado ÷ (visitantes × días).
- **Unidad:** €/día.
- **Fuente de datos (sistemas):** Encuestas de gasto; partners; (opcional) pagos agregados con gobernanza y privacidad.
- **Nivel de cálculo:** visitante | día | zona | segmento
- **Frecuencia de medición:** trimestral (realista) con proxies mensuales.
- **Owner (responsable):** Economía del destino.
- **Umbral/Objetivo:** ↑ vs baseline en segmentos objetivo; siempre declarar supuestos (correlación vs causalidad).
- **Notas operativas:** Separar gasto atribuible por categoría (alojamiento, restauración, ocio). Documentar supuestos y cobertura.
- **Sesgos comunes / Riesgos de interpretación:** atribución: correlación ≠ causalidad (declarar supuestos).
- **Relación con Convercus:** Capacidad: *activación de socios + recompensas por consumo distribuido* → palanca: elevar gasto en red de socios → mecanismo: earn & burn, misiones por rutas y cross-partner → validación: holdout geográfico o por cohortes, midiendo uplift en transacciones de socios (no solo estimaciones).
- **Compuerta de piloto (Gate):** no (requiere diseño causal robusto para ser KPI de decisión).
- **Estado de calidad de dato:** C

##### KPI-074 — Índice de estacionalidad
- **Definición:** Índice de concentración de actividad por meses vs media anual (mide presión de picos).
- **Fórmula:** índice de concentración mensual vs media anual (definir método).
- **Unidad:** índice.
- **Fuente de datos (sistemas):** Llegadas/pernoctaciones; tráfico; reservas; BI del destino.
- **Nivel de cálculo:** mes | mercado | zona
- **Frecuencia de medición:** mensual.
- **Owner (responsable):** Marketing del destino.
- **Umbral/Objetivo:** ↓ concentración en picos y ↑ en valle (si es objetivo) sin deteriorar KPI-072/124.
- **Notas operativas:** Definir método (p. ej., Gini/coeficiente de variación o ratio pico/medio) y mantenerlo estable.
- **Sesgos comunes / Riesgos de interpretación:** Cambios metodológicos; confundir redistribución con crecimiento neto.
- **Relación con Convercus:** Capacidad: *campañas + gamificación + pasaporte de destino* → palanca: mover demanda a temporada baja → mecanismo: misiones por fechas/zonas, incentivos por consumo en valle → validación: geo-tests (zonas/mercados) y análisis contrafactual con control estacional.
- **Compuerta de piloto (Gate):** sí (en programas de destino con objetivo antiestacional).
- **Estado de calidad de dato:** B

##### KPI-075 — Dispersión territorial
- **Definición:** Medida de redistribución de la actividad (visitas/consumo) fuera de zonas saturadas hacia zonas objetivo, preservando privacidad.
- **Fórmula:** % actividad fuera de zonas saturadas + índice de concentración.
- **Unidad:** % / índice.
- **Fuente de datos (sistemas):** Partners + (opcional) movilidad y datos agregados; gobernanza legal (DPO) y acuerdos de tratamiento.
- **Nivel de cálculo:** zona | barrio | punto de interés | periodo | segmento (agregado)
- **Frecuencia de medición:** mensual.
- **Owner (responsable):** Gestión de destino + sostenibilidad.
- **Umbral/Objetivo:** ↑ % fuera de zonas saturadas (vs baseline) con umbrales por capacidad de carga si aplica.
- **Notas operativas:** Acordar nivel de agregación y reglas de privacidad. Definir “zona saturada” y “zona objetivo”. Evitar tracking individual.
- **Sesgos comunes / Riesgos de interpretación:** privacidad y gobernanza de datos; involucrar DPO.
- **Relación con Convercus:** Capacidad: *pasaporte con rutas alternativas + incentivos por zonas* → palanca: dirigir flujos → mecanismo: misiones geolocalizadas (agregadas), recompensas en socios por zona → validación: tests por zona/periodo con control, midiendo uplift en transacciones de socios y proxies de movilidad agregada.
- **Compuerta de piloto (Gate):** sí (si hay riesgo de privacidad o backlash, se detiene/ajusta el diseño).
- **Estado de calidad de dato:** C

##### KPI-076 — Activación de socios (Partners Active Rate)
- **Definición:** Porcentaje de socios estratégicos que registran actividad real (eventos, redenciones, transacciones o campañas) en una ventana definida.
- **Fórmula:** # socios con actividad real (redenciones/eventos) ÷ # socios totales.
- **Unidad:** %.
- **Fuente de datos (sistemas):** Convercus (eventos, redenciones, campañas) + reporting de socios; (opcional) POS/eComm de socios para verificación.
- **Nivel de cálculo:** socio | vertical | zona | periodo
- **Frecuencia de medición:** mensual.
- **Owner (responsable):** Ecosystem/Partnerships Manager.
- **Umbral/Objetivo:** ↑ pp vs baseline; fijar meta de “socios activos” mínima para efectos de red (y para justificar inversión).
- **Notas operativas:** Definir “actividad real” (no solo alta en catálogo). Requerir al menos 1 evento/mes (o umbral) y validar calidad (transacción/redención).
- **Sesgos comunes / Riesgos de interpretación:** “socios en el PDF” ≠ socios activos; medir actividad.
- **Relación con Convercus:** Capacidad: *programa de socios + liquidación transparente + gamificación* → palanca: activar red y mejorar propuesta → mecanismo: incentivos a socio, reglas de earn & burn, reporting y settlement → validación: aumento de socios activos y del attach rate/gasto en socios vs control.
- **Compuerta de piloto (Gate):** sí (sin socios activos, el modelo de ecosistema no escala).
- **Estado de calidad de dato:** A/B


---

#### Paquete mínimo recomendado para un piloto Convercus en Viajes (12 semanas)

> Selección mínima para que el piloto sea defendible en comité (CFO + Operaciones + Comercial/Marketing).

1) **KPI-053 Margen de contribución** (gate económico: “no comprar ventas”)  
2) **KPI-062 Refund Cycle Time** + **KPI-065 Contact Rate** (cost-to-serve y fricción operativa)  
3) **KPI-060 Tasa de cancelación** (guardarraíl de calidad y expectativas)  
4) **KPI-059 Attach Rate** (monetización incremental)  
5) **KPI-051 Ingresos netos** (resultado de negocio, siempre neteado de incentivos)



---

#### Índice rápido por owner (asignación inmediata)

- **Finanzas / CFO / Controller:** KPI-051, KPI-052, KPI-053, KPI-064  
- **Comercial / Pricing / Growth:** KPI-050, KPI-054, KPI-058, KPI-059, KPI-070  
- **Digital / eCommerce / Tecnología:** KPI-056, KPI-057  
- **Operaciones / Contact Center / Payments:** KPI-060, KPI-061, KPI-062, KPI-063, KPI-065, KPI-066, KPI-067  
- **Revenue/Yield (Mayoristas):** KPI-068, KPI-069, KPI-071  
- **Destinos (Análisis/Marketing/Sostenibilidad):** KPI-072, KPI-073, KPI-074, KPI-075  
- **Ecosistema / Partnerships:** KPI-076



---

### Mapa KPI → Palanca Convercus (resumen normalizado)

- **Journeys:** KPI-055, KPI-059, KPI-060, KPI-061, KPI-062, KPI-067  
- **Omnicanalidad:** KPI-056, KPI-058, KPI-064, KPI-065  
- **Venta social:** KPI-054, KPI-056, KPI-058  
- **Gamificación:** KPI-068, KPI-070, KPI-059, KPI-076  
- **Programa de socios:** KPI-059, KPI-073, KPI-075, KPI-076



---

### Apéndice: eventos mínimos del journey

`search_performed`, `quote_created`, `booking_confirmed`, `payment_captured`, `booking_modified`, `booking_cancelled`,  
`refund_initiated`, `refund_completed`, `trip_start`, `trip_end`, `incident_opened`, `incident_resolved`,  
`review_submitted`, `referral_shared`, `referral_converted`, `ancillary_added`.

---

### Anexo — Terminología recomendada (Viajes) y reglas de estilo

Este anexo se incorpora para asegurar consistencia semántica en presentaciones, diagnósticos y gobernanza.
En particular: (i) separar **volumen** (Gross Bookings/TTV) de **ingreso** (Net Revenue), (ii) usar **reserva** en lugar de “booking” como sustantivo,
y (iii) preferir **vinculación** frente a “engagement” en la narrativa.

### Anexo sectorial: Viajes (agencias, mayoristas y destinos) — Terminología recomendada

Este anexo amplía el glosario general con términos recurrentes del **sector viajes** y sugiere equivalencias en español coherentes con la narrativa de Convercus. El objetivo es doble:

1) **Precisión económica**: evitar confusiones habituales (p. ej., *Gross Bookings* vs *Net Revenue*, comisiones vs márgenes, cancelación vs reembolso).  
2) **Claridad operativa**: nombrar de forma consistente procesos y métricas de servicio (posventa, incidencias, chargebacks).  

> Nota: cuando el término inglés sea prácticamente un “estándar de facto” en travel-tech (p. ej., *GDS*, *PNR*, *NDC*), se mantiene entre paréntesis según la **Regla de estilo 1** del glosario general.

---

#### 1) Actores, canales y roles comerciales

- **Travel Agency** → **Agencia de viajes**  
- **Retail Travel Agency** → **Agencia minorista (red de tiendas / retail)**  
- **Online Travel Agency (OTA)** → **Agencia de viajes online (OTA)**  
- **Tour Operator** → **Turoperador**  
- **Wholesaler** → **Mayorista (turoperación mayorista)**  
- **DMC (Destination Management Company)** → **Agencia receptiva (DMC)**  
- **DMO (Destination Marketing/Management Organization)** → **Organismo/Entidad de gestión de destino (DMO)**  
- **NTO / RTO / LTO** → **Organismo nacional / regional / local de turismo (NTO/RTO/LTO)**  
- **Supplier** → **Proveedor** (hotel, aerolínea, rent-a-car, actividades, cruceros, etc.)  
- **Partner** → **Socio estratégico** (evitar “partner” como único término; ver sección de “Términos a evitar”)  
- **Affiliate** → **Afiliado (programa de afiliación)**  
- **B2B Channel** → **Canal B2B**  
- **B2C Channel** → **Canal B2C**  
- **B2B2C** → **B2B2C** (mantener; es un patrón de go-to-market más que un anglicismo)  
- **Agent / Travel Advisor** → **Agente / Asesor de viajes**  
- **Sales Enablement** → **Habilitación comercial** (en Convercus, se conecta con *Social Selling*)  
- **Social Selling** → **Venta social (Social Selling)**  

**Uso recomendado (viajes):**  
- En contenidos de negocio, preferir “agencia de viajes online” antes que “OTA” salvo cuando el público sea técnico o muy sectorial.  
- Para redes físicas o mixtas, “red de agencias” o “grupo de agencias” suele ser más natural que “retail”.

---

#### 2) Distribución, tecnología y operación de reserva

- **Booking Engine** → **Motor de reservas**  
- **Search-to-Book Funnel** → **Embudo de búsqueda a reserva**  
- **Metasearch** → **Metabuscador**  
- **Rate Shopping** → **Comparador de tarifas (rate shopping)**  
- **Channel Manager** → **Gestor de canales (channel manager)**  
- **Inventory / Availability** → **Inventario / disponibilidad**  
- **Allotment** → **Cupo (allotment)**  
- **Release Period** → **Plazo de liberación (release period)**  
- **GDS (Global Distribution System)** → **Sistema global de distribución (GDS)**  
- **IATA** → **IATA** (sigla estándar; no traducir)  
- **NDC (New Distribution Capability)** → **NDC (New Distribution Capability)**  
- **PNR (Passenger Name Record)** → **PNR (registro del pasajero)**  
- **Ticketing / Issuance** → **Emisión de billetes (ticketing/issuance)**  
- **Fare Rules** → **Reglas tarifarias**  
- **Ancillaries** → **Servicios complementarios (ancillaries)**  
- **Dynamic Packaging** → **Paquetización dinámica (dynamic packaging)**  
- **Self-service** → **Autoservicio (self-service)**  
- **Customer Support** → **Atención al cliente**  
- **Call Center / Contact Center** → **Centro de atención / Contact center**  
- **WhatsApp Commerce / Messaging Commerce** → **Comercio conversacional (mensajería)**  

**Regla sectorial 3 (viajes):**  
En textos comerciales, evitar “booking” como sustantivo (“un booking”) y usar **reserva**. “Booking window” sí puede traducirse como **ventana de reserva** (ver métricas), manteniendo el inglés entre paréntesis solo si aporta claridad para audiencias travel-tech.

---

#### 3) Economía de la reserva y métricas de ingresos (P&L)

La industria de viajes usa vocabulario financiero específico que conviene normalizar porque la “venta” no siempre es “ingreso” en sentido contable.

- **Gross Bookings / TTV (Total Transaction Value)** → **Volumen bruto de reservas (Gross Bookings/TTV)**  
  - *Nota:* refleja valor transaccionado, no necesariamente ingreso neto.
- **Net Revenue** → **Ingresos netos** (tras comisiones, anulaciones y ajustes según modelo)  
- **Take Rate** → **Tasa de captura (take rate)** (ingreso neto / volumen bruto)  
- **Commission** → **Comisión**  
- **Service Fee** → **Cargo de servicio** (p. ej., gestión, asistencia, cambios)  
- **Mark-up** → **Margen aplicado (mark-up)**  
- **Override** → **Comisión incremental / rappel (override)**  
- **Contribution Margin** → **Margen de contribución**  
- **CAC (Customer Acquisition Cost)** → **Coste de adquisición (CAC)**  
- **CLV/LTV (Customer Lifetime Value)** → **Valor de vida del cliente (CLV/LTV)**  
- **Share of Wallet** → **Cuota en el gasto del cliente**  
- **Attach Rate** → **Tasa de incorporación (attach rate)** (p. ej., seguros, experiencias, equipaje)  
- **Upsell / Cross-sell** → **Venta incremental / venta cruzada**  
- **Refund** → **Reembolso**  
- **Chargeback** → **Contracargo (chargeback)**  
- **Fraud Rate** → **Tasa de fraude**  
- **Cost-to-Serve** → **Coste de servicio (cost-to-serve)**  

**Traducción sugerida (para dirección financiera):**  
- “Optimizar el *take rate*” → “**aumentar la tasa de captura** sin deteriorar conversión ni aumentar incidencias”.  
- “Reducir *leakage*” → “**reducir fugas de margen** (descuentos no controlados, comisiones mal aplicadas, errores de tarifa)”.

---

#### 4) Métricas operativas del journey de viaje (antes/durante/después)

Para Convercus, este bloque es crítico porque conecta “fidelización” con hechos observables del recorrido del cliente (journey).

- **Pre-trip / In-trip / Post-trip** → **Antes del viaje / Durante el viaje / Después del viaje**  
- **Booking Window** → **Ventana de reserva (booking window)**  
- **Lead Time** → **Anticipación de compra (lead time)**  
- **Cancellation Rate** → **Tasa de cancelación**  
- **Change Rate** → **Tasa de cambios/modificaciones**  
- **No-show** → **No presentación (no-show)**  
- **Refund Cycle Time** → **Tiempo de ciclo de reembolso**  
- **Disruption** → **Incidencia / disrupción** (p. ej., retraso, overbooking, cambio de itinerario)  
- **Customer Contact Rate** → **Tasa de contacto del cliente** (contactos por reserva)  
- **AHT (Average Handle Time)** → **Tiempo medio de gestión (AHT)**  
- **FCR (First Contact Resolution)** → **Resolución en primer contacto (FCR)**  
- **SLA (Service Level Agreement)** → **Acuerdo de nivel de servicio (SLA)**  
- **CSAT / NPS** → **Satisfacción (CSAT) / NPS**  
- **Review / Rating** → **Reseña / valoración**  
- **Rebooking** → **Nueva reserva tras incidencia (rebooking)**  

**Uso recomendado (viajes):**  
Cuando se hable de experiencia, aterrizarla siempre a un evento: “confirmación”, “check-in”, “llegada”, “uso de servicio”, “incidencia resuelta”, “reseña verificada”. Ese es el puente entre narrativa y medición.

---

#### 5) Revenue management, inventario y estacionalidad (especialmente mayoristas)

- **Revenue Management** → **Gestión de ingresos (revenue management)**  
- **Yield Management** → **Gestión de rendimiento (yield)**  
- **Load Factor** → **Factor de ocupación** (muy usado en aéreo; en paquetes puede adaptarse)  
- **Spoilage** → **Pérdida por no venta (spoilage)**  
- **Forecast Accuracy** → **Precisión de previsión**  
- **Seasonality** → **Estacionalidad**  
- **Peak / Off-peak** → **Temporada alta / baja**  
- **Early Booking** → **Reserva anticipada (early booking)**  
- **Last-minute** → **Última hora (last-minute)**  
- **Price Elasticity** → **Elasticidad precio-demanda**  

**Regla sectorial 4 (viajes):**  
Evitar traducir “yield” por “rentabilidad” (es demasiado amplio). Cuando se use “yield”, acompañar con “gestión de rendimiento (yield)” o “gestión de ingresos”.

---

#### 6) Destinos y economía del visitante (DMO/NTO/RTO/LTO)

- **Visitor Economy** → **Economía del visitante**  
- **Length of Stay (LoS)** → **Estancia media (LoS)**  
- **Spend per Visitor / per Day** → **Gasto por visitante / gasto diario**  
- **Geographic Dispersion** → **Dispersión territorial**  
- **Seasonality Index** → **Índice de estacionalidad**  
- **Carrying Capacity** → **Capacidad de carga**  
- **Overtourism** → **Sobreturismo (overtourism)**  
- **Sustainable Tourism** → **Turismo sostenible**  
- **Destination Pass / City Card** → **Pase de destino / tarjeta turística**  
- **Attribution / Incrementality** → **Atribución / incrementalidad** (en campañas de destino)  

**Uso recomendado (destinos):**  
Hablar de “retorno” con rigor: si no hay medición causal, usar “contribución estimada” o “impacto correlacional”. Cuando sí exista diseño de medición (p. ej., tests geográficos o por cohortes), entonces “incrementalidad” es un término útil.

---

#### 7) M&A y consolidación en redes de viajes (cuando aplique)

- **Roll-up** → **Consolidación por adquisiciones (roll-up)**  
- **Synergies** → **Sinergias**  
- **Commercial Synergies** → **Sinergias comerciales**  
- **Integration / Day-1** → **Integración / Día 1 (Day-1)**  
- **Earn-out** → **Pago variable por resultados (earn-out)**  
- **Governance Model** → **Modelo de gobernanza**  
- **Commission Harmonization** → **Armonización de comisiones**  
- **Partner Incentives** → **Incentivos a socios estratégicos**  

---

#### 8) Claims y frases recomendadas (viajes)

Estas propuestas están pensadas para comunicar valor sin “promesas vagas”; cada una sugiere un ángulo medible.

- **“Más repetición, sin destruir margen.”**  
- **“Del postventa reactivo al journey orquestado.”**  
- **“Omnicanal real: tienda, web, call center y mensajería con una sola lógica de fidelización.”**  
- **“Habilite a su red de agentes con venta social y trazabilidad.”**  
- **“Incentivos medibles para socios estratégicos: más calidad, menos cancelaciones.”**  
- **“Gamificación útil: acelere reservas anticipadas y reduzca descuentos de última hora.”**  

---

#### 9) Términos a evitar en viajes (y alternativas)

- **Booking (como sustantivo)** → Evitar “un booking”; usar **reserva**.  
- **Ancillaries (sin traducir)** → Usar **servicios complementarios (ancillaries)**.  
- **Partner (como único término)** → Usar **socio estratégico** (y especificar tipo: proveedor, afiliado, franquiciado, receptivo).  
- **Engagement** → Evitar, usar **vinculación**.  
- **Insights** → Evitar, usar **información accionable** (reservar “inteligencia” para IA/ML).  
- **Leakage** (sin contexto) → Usar **fugas de margen** y describir el mecanismo (descuentos, comisiones, errores).  

---

#### 10) Mini-diccionario de KPIs (nombres recomendados)

> No sustituye a un diccionario de fórmulas, pero fija el “nombre canónico” para presentaciones y propuestas.

- **Volumen bruto de reservas (Gross Bookings/TTV)**  
- **Ingresos netos (Net Revenue)**  
- **Tasa de captura (Take Rate)**  
- **Tasa de incorporación (Attach Rate)**  
- **Coste de adquisición (CAC)**  
- **Valor de vida del cliente (CLV/LTV)**  
- **Coste de servicio (Cost-to-Serve)**  
- **Tiempo de ciclo de reembolso (Refund Cycle Time)**  
- **Tasa de cancelación (Cancellation Rate)**  
- **Tiempo medio de gestión (AHT)**  
- **Resolución en primer contacto (FCR)**  
- **Satisfacción (CSAT) / NPS**  
- **Estancia media (LoS)** (destinos)  
- **Gasto diario por visitante** (destinos)  
- **Índice de estacionalidad** (destinos)

---

Fin del KPI Dictionary.
## 7) Hoteles, alojamientos y hospitality — Módulo sectorial (KPI-200–249)

Este módulo cubre indicadores estándar hoteleros (Occupancy, ADR, RevPAR, GOPPAR) y su **vinculación** con Convercus (canal directo, repetición, ancillaries). 

> **Nota sobre destinos:** para economía del visitante y programas de destino (LoS, gasto, estacionalidad, dispersión, socios) usar los KPIs **KPI-072–KPI-076** del módulo de Viajes.

### KPI-200 — Ocupación (Occupancy Rate)
- **Definición:** Porcentaje de habitaciones disponibles que están ocupadas en un periodo.
- **Fórmula:** Noches ocupadas ÷ noches disponibles.
- **Unidad:** %.
- **Fuente de datos (sistemas):** PMS + channel manager + BI revenue.
- **Nivel de cálculo:** hotel | fecha | segmento | canal
- **Frecuencia de medición:** diario/semanal
- **Owner (responsable):** Revenue Manager
- **Umbral/Objetivo:** ↑ vs baseline/forecast manteniendo ADR/RevPAR (evitar ocupar “barato”).
- **Notas operativas:** Separar por segmento (corporate, leisure), por canal (directo/OTA) y por tipo de habitación.
- **Sesgos comunes / Riesgos de interpretación:** Ocupación alta puede ocultar caída de tarifa; leer con ADR y GOPPAR.
- **Relación con Convercus:** Convercus: fidelización + journeys pre-estancia + incentivos no monetarios para ocupación en valle.
- **Compuerta de piloto (Gate):** sí (si ocupación sube con caída de ADR/margen, ajustar).
- **Estado de calidad de dato:** A/B

### KPI-201 — ADR (Average Daily Rate)
- **Definición:** Tarifa media diaria por habitación vendida.
- **Fórmula:** Ingresos de habitaciones ÷ noches ocupadas.
- **Unidad:** €.
- **Fuente de datos (sistemas):** PMS/ERP + BI revenue.
- **Nivel de cálculo:** hotel | fecha | segmento | canal
- **Frecuencia de medición:** diario/semanal
- **Owner (responsable):** Revenue Manager
- **Umbral/Objetivo:** ↑ vs baseline en segmentos objetivo; mantener competitividad (price index hotelero si aplica).
- **Notas operativas:** Definir ingresos de habitaciones (sin impuestos) y excluir paquetes si se reportan aparte (o desagregar).
- **Sesgos comunes / Riesgos de interpretación:** ADR puede subir por mix (habitaciones premium) sin mejora real; controlar mix.
- **Relación con Convercus:** Convercus: segmentación por sensibilidad y beneficios (upgrade/late checkout) en lugar de descuento directo.
- **Compuerta de piloto (Gate):** sí (si ADR cae por incentivos, revisar).
- **Estado de calidad de dato:** B

### KPI-202 — RevPAR
- **Definición:** Ingresos por habitación disponible (mide rendimiento combinado de ocupación y tarifa).
- **Fórmula:** Ingresos de habitaciones ÷ habitaciones disponibles (o ADR × Ocupación).
- **Unidad:** €.
- **Fuente de datos (sistemas):** PMS + BI revenue.
- **Nivel de cálculo:** hotel | fecha | segmento
- **Frecuencia de medición:** diario/semanal
- **Owner (responsable):** Revenue Manager + GM
- **Umbral/Objetivo:** ↑ vs baseline; objetivo por temporada y plaza.
- **Notas operativas:** Separar RevPAR neto de comisiones OTA si se quiere lectura de rentabilidad real.
- **Sesgos comunes / Riesgos de interpretación:** RevPAR bruto puede ocultar coste de distribución; leer con % canal directo.
- **Relación con Convercus:** Convercus: impulsa canal directo y repetición con experiencias/estatus, mejorando net RevPAR.
- **Compuerta de piloto (Gate):** sí (KPI de resultado de RM).
- **Estado de calidad de dato:** A/B

### KPI-203 — GOPPAR (Gross Operating Profit per Available Room)
- **Definición:** Beneficio operativo bruto por habitación disponible (métrica de rentabilidad hotelera).
- **Fórmula:** GOP ÷ habitaciones disponibles (en periodo).
- **Unidad:** €.
- **Fuente de datos (sistemas):** P&L hotelero + BI + PMS para denominador.
- **Nivel de cálculo:** hotel | mes | segmento
- **Frecuencia de medición:** mensual
- **Owner (responsable):** CFO/Controller + GM
- **Umbral/Objetivo:** ↑ vs baseline; gate económico para escalado de programa.
- **Notas operativas:** Definir GOP (incluir/excluir costes) y mantener consistencia. Ajustar por estacionalidad.
- **Sesgos comunes / Riesgos de interpretación:** Comparar sin normalizar por temporada o cambios de costes fijos distorsiona.
- **Relación con Convercus:** Convercus: reduce dependencia OTA (comisiones) y eleva consumo ancillary; medir uplift vs control.
- **Compuerta de piloto (Gate):** sí (gate de negocio).
- **Estado de calidad de dato:** C→B

### KPI-204 — Share de canal directo (Direct Booking Share)
- **Definición:** Proporción de reservas/ingresos capturados por canal directo vs intermediado.
- **Fórmula:** Reservas (o ingresos) directos ÷ total.
- **Unidad:** %.
- **Fuente de datos (sistemas):** PMS + channel manager + analytics web/app.
- **Nivel de cálculo:** hotel | canal | semana/mes
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** Marketing Digital + Revenue
- **Umbral/Objetivo:** ↑ pp vs baseline; objetivo por mercado.
- **Notas operativas:** Definir “directo” (web, app, call center, walk-in). Separar metabuscadores.
- **Sesgos comunes / Riesgos de interpretación:** Atribución confusa si se mezclan canales; riesgo de conflicto interno.
- **Relación con Convercus:** Convercus: journeys omnicanal + beneficios para miembros en directo (sin descuento plano) + trazabilidad de canal.
- **Compuerta de piloto (Gate):** sí.
- **Estado de calidad de dato:** B

### KPI-205 — Tasa de cancelación hotelera
- **Definición:** Porcentaje de reservas que se cancelan antes del check-in.
- **Fórmula:** # cancelaciones ÷ # reservas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** PMS + channel manager.
- **Nivel de cálculo:** reserva | canal | tarifa | ventana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Revenue + Front Office
- **Umbral/Objetivo:** ↓ pp vs baseline; en tarifas flex, fijar umbrales por canal.
- **Notas operativas:** Separar cancelaciones por política tarifaria y por canal (OTA tiende a diferir).
- **Sesgos comunes / Riesgos de interpretación:** Reducir cancelación endureciendo políticas puede bajar conversión; medir junto a ocupación.
- **Relación con Convercus:** Convercus: comunicación proactiva pre-estancia, opciones de cambio, beneficios por mantener reserva.
- **Compuerta de piloto (Gate):** sí (guardarraíl).
- **Estado de calidad de dato:** A/B

### KPI-206 — Booking Window (anticipación de reserva)
- **Definición:** Días promedio entre la fecha de reserva y la fecha de llegada.
- **Fórmula:** avg(fecha llegada − fecha reserva).
- **Unidad:** días.
- **Fuente de datos (sistemas):** PMS + analytics.
- **Nivel de cálculo:** reserva | canal | segmento
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** Revenue Manager
- **Umbral/Objetivo:** ↑ en segmentos objetivo (si se busca predecibilidad) y ↓ volatilidad en picos.
- **Notas operativas:** Controlar por mercado y temporada. Ventana puede ser deseable distinta por producto.
- **Sesgos comunes / Riesgos de interpretación:** Cambios en mix distorsionan; no interpretar sin segmentación.
- **Relación con Convercus:** Convercus: misiones early-booking, beneficios por anticipación y campañas antiestacionalidad.
- **Compuerta de piloto (Gate):** no.
- **Estado de calidad de dato:** B

### KPI-207 — Estancia media hotelera (LoS hotel)
- **Definición:** Número medio de noches por estancia (hotel).
- **Fórmula:** Σ noches ÷ # estancias.
- **Unidad:** noches.
- **Fuente de datos (sistemas):** PMS.
- **Nivel de cálculo:** estancia | segmento | canal
- **Frecuencia de medición:** mensual
- **Owner (responsable):** Revenue + Marketing
- **Umbral/Objetivo:** ↑ vs baseline en temporadas objetivo sin deteriorar ADR.
- **Notas operativas:** Separar leisure vs corporate; controlar por fines de semana y eventos.
- **Sesgos comunes / Riesgos de interpretación:** Puede subir por mix, no por efecto del programa; requerir control.
- **Relación con Convercus:** Convercus: recompensas por hitos (2ª/3ª noche), bundles con ancillaries, journeys de itinerario.
- **Compuerta de piloto (Gate):** no (resultado medio plazo).
- **Estado de calidad de dato:** B

### KPI-208 — Ingreso ancillary por huésped (Ancillary Rev per Guest)
- **Definición:** Ingresos complementarios (F&B, spa, parking, actividades) por huésped/estancia.
- **Fórmula:** Ingresos ancillary ÷ # huéspedes (o # estancias).
- **Unidad:** €.
- **Fuente de datos (sistemas):** PMS + POS F&B/spa + BI.
- **Nivel de cálculo:** huésped | estancia | categoría
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** Hotel Ops + Revenue
- **Umbral/Objetivo:** ↑ vs baseline; objetivo por segmento.
- **Notas operativas:** Definir qué entra en ancillary y evitar doble conteo con paquetes.
- **Sesgos comunes / Riesgos de interpretación:** Subir ancillary puede aumentar quejas si se fuerza upsell; medir con NPS.
- **Relación con Convercus:** Convercus: gamificación y misiones durante la estancia, beneficios por consumo en socios internos.
- **Compuerta de piloto (Gate):** sí (si es KPI de monetización del piloto).
- **Estado de calidad de dato:** B

### KPI-209 — Penetración de miembros en reservas (Member Share)
- **Definición:** Proporción de reservas realizadas por miembros identificados del programa.
- **Fórmula:** # reservas miembro ÷ # reservas totales.
- **Unidad:** %.
- **Fuente de datos (sistemas):** CRM/loyalty + PMS (linking) + canal directo.
- **Nivel de cálculo:** reserva | canal | segmento
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** CRM/Loyalty Manager
- **Umbral/Objetivo:** ↑ pp vs baseline; target mínimo para poder atribuir uplift.
- **Notas operativas:** Requiere matching fiable entre PMS y CRM. Separar miembros nuevos vs recurrentes.
- **Sesgos comunes / Riesgos de interpretación:** Sin identificación, no hay atribución; riesgo de sesgo si se identifica solo en directo.
- **Relación con Convercus:** Convercus: onboarding, identidad, beneficios para registro y journeys de activación.
- **Compuerta de piloto (Gate):** sí (habilitador de medición).
- **Estado de calidad de dato:** B

### KPI-210 — Satisfacción del huésped (CSAT/NPS)
- **Definición:** Medida de satisfacción/experiencia (post-stay) capturada de forma consistente.
- **Fórmula:** CSAT promedio (1–5) y/o NPS (%promotores − %detractores).
- **Unidad:** score.
- **Fuente de datos (sistemas):** Encuestas + reviews + CRM.
- **Nivel de cálculo:** estancia | hotel | segmento
- **Frecuencia de medición:** mensual (con alertas semanales)
- **Owner (responsable):** GM + Guest Experience
- **Umbral/Objetivo:** ≥ baseline; umbral mínimo (si cae, se revisa el programa).
- **Notas operativas:** Separar por canal y segmento; controlar sesgos de respuesta.
- **Sesgos comunes / Riesgos de interpretación:** Optimizar revenue puede degradar experiencia si se recortan servicios; CSAT es guardarraíl.
- **Relación con Convercus:** Convercus: journeys durante estancia, resolución proactiva, recompensas por feedback.
- **Compuerta de piloto (Gate):** sí (guardarraíl reputacional).
- **Estado de calidad de dato:** B

## 8) Parafarmacias — Módulo sectorial (KPI-250–299)

Este módulo prioriza **recurrencia, mix de categoría, caducidades y compliance** (sin entrar en consejo médico). La trazabilidad de consentimiento y el uso prudente de datos son críticos.

### KPI-250 — Mix de margen por categoría (Category Margin Mix)
- **Definición:** Distribución del margen y ventas por categoría (dermo, suplementos, infantil, higiene, etc.).
- **Fórmula:** Margen por categoría ÷ margen total (y ventas por categoría ÷ ventas totales).
- **Unidad:** % (+ €).
- **Fuente de datos (sistemas):** ERP/POS + BI categoría.
- **Nivel de cálculo:** categoría | tienda | canal | mes
- **Frecuencia de medición:** mensual
- **Owner (responsable):** Category Manager / Dirección Comercial
- **Umbral/Objetivo:** Optimizar mix hacia categorías objetivo (rentabilidad y estrategia) sin deteriorar satisfacción.
- **Notas operativas:** Definir margen (bruto o contribución) y normalizar promociones. Controlar por estacionalidad (alergias, gripe).
- **Sesgos comunes / Riesgos de interpretación:** Cambios estacionales pueden parecer mejoras; interpretar por cohorte y temporada.
- **Relación con Convercus:** Convercus: personalización por necesidades y misiones de salud/bienestar (no médicas), bundles y socios.
- **Compuerta de piloto (Gate):** no.
- **Estado de calidad de dato:** A/B

### KPI-251 — Repeat Purchase Rate (30/90d) — parafarmacia
- **Definición:** Porcentaje de clientes que repiten compra en 30/90 días (por categoría y total).
- **Fórmula:** # clientes con ≥2 compras en ventana ÷ # clientes activos.
- **Unidad:** %.
- **Fuente de datos (sistemas):** POS/eComm + CRM (identificación).
- **Nivel de cálculo:** cliente | cohorte | categoría | ventana
- **Frecuencia de medición:** mensual
- **Owner (responsable):** CRM/Loyalty + Comercial
- **Umbral/Objetivo:** ↑ pp vs baseline; objetivo por categorías de recurrencia (dermo, suplementos).
- **Notas operativas:** Definir cliente único e identificación. Separar consumo recurrente vs ocasional.
- **Sesgos comunes / Riesgos de interpretación:** Sesgo si solo se mide canal con identificación alta (eComm) y no tienda.
- **Relación con Convercus:** Convercus: journeys de reabastecimiento (recordatorios), niveles y recompensas por adherencia (no sanitaria).
- **Compuerta de piloto (Gate):** sí (KPI de efecto temprano).
- **Estado de calidad de dato:** B

### KPI-252 — Caducidad/merma por expiración (Expiry Waste Rate)
- **Definición:** Pérdida por productos caducados o próximos a caducar.
- **Fórmula:** € caducidad ÷ € inventario (o ÷ ventas).
- **Unidad:** % (+ €).
- **Fuente de datos (sistemas):** ERP inventario + mermas + control caducidades.
- **Nivel de cálculo:** SKU | tienda | categoría | mes
- **Frecuencia de medición:** mensual (con alertas semanales)
- **Owner (responsable):** Store Ops + Supply Chain
- **Umbral/Objetivo:** ↓ vs baseline; umbrales por categoría (cosmética/suplementos).
- **Notas operativas:** Definir ventana “near-expiry” y políticas de liquidación. Controlar por rotación.
- **Sesgos comunes / Riesgos de interpretación:** Reducir merma puede aumentar OOS si se recorta demasiado inventario.
- **Relación con Convercus:** Convercus: campañas segmentadas para mover near-expiry con valor (packs, puntos) respetando márgenes.
- **Compuerta de piloto (Gate):** sí (guardarraíl económico).
- **Estado de calidad de dato:** C→B

### KPI-253 — Disponibilidad SKU críticos (Critical SKU OSA)
- **Definición:** Disponibilidad de SKUs críticos/estacionales (p. ej., SPF, antialérgicos) en tienda y online.
- **Fórmula:** SKU críticos disponibles ÷ SKU críticos planificados (por periodo).
- **Unidad:** %.
- **Fuente de datos (sistemas):** ERP + POS/eComm + auditoría tienda.
- **Nivel de cálculo:** SKU | tienda | semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Store Ops / Category
- **Umbral/Objetivo:** ≥ umbral (p. ej., 97%) en top SKUs.
- **Notas operativas:** Definir lista de SKUs críticos por temporada. Controlar por proveedores.
- **Sesgos comunes / Riesgos de interpretación:** Si se mide solo inventario, no refleja disponibilidad real en lineal.
- **Relación con Convercus:** Convercus: triggers para sustitución y avisos “back in stock” a miembros identificados.
- **Compuerta de piloto (Gate):** sí (guardarraíl de experiencia y ventas).
- **Estado de calidad de dato:** B

### KPI-254 — Tasa de consejo/servicio (Consultation Rate)
- **Definición:** Proporción de tickets/ventas donde existe interacción de consejo (asesoría) registrada (cuando aplique).
- **Fórmula:** # interacciones consejo ÷ # tickets (o # clientes).
- **Unidad:** %.
- **Fuente de datos (sistemas):** POS con códigos de servicio + CRM (si existe) + app/turnos.
- **Nivel de cálculo:** ticket | tienda | franja | motivo
- **Frecuencia de medición:** semanal/mensual
- **Owner (responsable):** Store Manager / Customer Experience
- **Umbral/Objetivo:** ↑ en categorías donde el consejo aumenta conversión y valor; mantener eficiencia (AHT si aplica).
- **Notas operativas:** Definir qué cuenta como consejo (registro mínimo). Evitar sesgos por subregistro.
- **Sesgos comunes / Riesgos de interpretación:** Más consejo puede subir coste de servicio; medir junto a margen y satisfacción.
- **Relación con Convercus:** Convercus: journeys de recomendación (no médica), contenido y misiones; derivación a servicios en tienda.
- **Compuerta de piloto (Gate):** no.
- **Estado de calidad de dato:** C

### KPI-255 — Cumplimiento promocional (Promo Compliance Rate)
- **Definición:** Cumplimiento de reglas promocionales y regulatorias (etiquetado, claims, descuentos permitidos) en campañas.
- **Fórmula:** # campañas conformes ÷ # campañas auditadas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** Sistema de promos + QA/Compliance + auditorías.
- **Nivel de cálculo:** campaña | canal | categoría
- **Frecuencia de medición:** mensual
- **Owner (responsable):** Compliance / Legal + Marketing
- **Umbral/Objetivo:** ≥ 99% (tolerancia mínima).
- **Notas operativas:** Definir checklist por categoría y canal. Registrar evidencias.
- **Sesgos comunes / Riesgos de interpretación:** Riesgo legal y reputacional si se incumple; alta severidad aunque baja frecuencia.
- **Relación con Convercus:** Convercus: aplica reglas de elegibilidad y copy/claims controlado; trazabilidad de campañas.
- **Compuerta de piloto (Gate):** sí (gate de despliegue).
- **Estado de calidad de dato:** B

## 9) Atención sanitaria y hospitalaria (privada) — Módulo sectorial (KPI-300–349)

Este módulo se incorpora para **entornos regulados** y de alta criticidad. Convercus actúa principalmente como capa de **journeys, comunicación y adherencia**; la medición debe respetar consentimiento y normativa aplicable (DPO/Compliance).

### KPI-300 — PAC (Patient Acquisition Cost)
- **Definición:** Coste de adquisición de un paciente nuevo activado (definición acordada por servicio).
- **Fórmula:** Gasto de captación atribuible ÷ # pacientes nuevos con 1ª cita/episodio.
- **Unidad:** €/paciente.
- **Fuente de datos (sistemas):** Marketing + CRM + sistema de citas (HIS/EMR scheduling).
- **Nivel de cálculo:** cohorte | especialidad | canal | mes
- **Frecuencia de medición:** mensual
- **Owner (responsable):** CMO / Patient Access
- **Umbral/Objetivo:** ↓ vs baseline sin degradar calidad (no-show, readmisión).
- **Notas operativas:** Definir “nuevo” y ventana de atribución. Separar urgencias vs programadas.
- **Sesgos comunes / Riesgos de interpretación:** Sesgo por atribución last-click; comparar sin case-mix es inválido.
- **Relación con Convercus:** Convercus: journeys de captación y activación (registro, recordatorios), segmentación por intención; siempre bajo consentimiento.
- **Compuerta de piloto (Gate):** sí (si PAC sube, ajustar).
- **Estado de calidad de dato:** C→B

### KPI-301 — Conversión consulta→cita (Inquiry-to-Appointment Conversion)
- **Definición:** Porcentaje de interesados que agenda una cita (por especialidad/canal).
- **Fórmula:** # citas agendadas ÷ # consultas/inquiries.
- **Unidad:** %.
- **Fuente de datos (sistemas):** CRM/call center + sistema de citas.
- **Nivel de cálculo:** inquiry | canal | especialidad | semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Patient Access / Call Center
- **Umbral/Objetivo:** ↑ vs baseline; objetivo por especialidad.
- **Notas operativas:** Normalizar definición de inquiry (web, teléfono, referidos) y deduplicación.
- **Sesgos comunes / Riesgos de interpretación:** Si el tracking es incompleto, la conversión queda inflada o subestimada.
- **Relación con Convercus:** Convercus: omnicanalidad y journeys de seguimiento; mensajería y recordatorios para completar agenda.
- **Compuerta de piloto (Gate):** sí (habilitador de volumen).
- **Estado de calidad de dato:** B

### KPI-302 — Lead Time de cita (Appointment Lead Time)
- **Definición:** Tiempo desde solicitud hasta fecha de cita (acceso).
- **Fórmula:** avg(fecha cita − fecha solicitud).
- **Unidad:** días.
- **Fuente de datos (sistemas):** Sistema de citas (HIS/EMR) + CRM.
- **Nivel de cálculo:** especialidad | centro | semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** COO / Patient Access
- **Umbral/Objetivo:** ≤ umbral por especialidad; priorizar reducción en servicios estratégicos.
- **Notas operativas:** Separar primera visita vs revisiones. Controlar por capacidad instalada.
- **Sesgos comunes / Riesgos de interpretación:** Reducir lead time sin capacidad puede degradar calidad o saturar equipos.
- **Relación con Convercus:** Convercus: gestión de journeys y listas de espera (comunicación), reasignación y confirmaciones.
- **Compuerta de piloto (Gate):** sí (guardarraíl de experiencia).
- **Estado de calidad de dato:** B

### KPI-303 — No-show Rate (ausencias a cita)
- **Definición:** Porcentaje de citas no asistidas sin cancelación efectiva.
- **Fórmula:** # no-shows ÷ # citas programadas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** Sistema de citas + check-in.
- **Nivel de cálculo:** especialidad | centro | semana
- **Frecuencia de medición:** semanal
- **Owner (responsable):** Patient Access / Operaciones
- **Umbral/Objetivo:** ↓ pp vs baseline; umbral crítico por especialidad.
- **Notas operativas:** Definir no-show vs cancelación tardía. Medir impacto económico (slot perdido).
- **Sesgos comunes / Riesgos de interpretación:** Políticas agresivas pueden dañar experiencia; equilibrar con CSAT.
- **Relación con Convercus:** Convercus: recordatorios, confirmaciones, incentivos no monetarios, journeys de reprogramación.
- **Compuerta de piloto (Gate):** sí (KPI de eficiencia).
- **Estado de calidad de dato:** A/B

### KPI-304 — Ocupación de camas (Bed Occupancy Rate)
- **Definición:** Porcentaje de camas disponibles ocupadas (hospitalización privada).
- **Fórmula:** Camas ocupadas ÷ camas disponibles.
- **Unidad:** %.
- **Fuente de datos (sistemas):** HIS/bed management + BI.
- **Nivel de cálculo:** centro | unidad | día
- **Frecuencia de medición:** diario/semanal
- **Owner (responsable):** COO / Dirección hospitalaria
- **Umbral/Objetivo:** Mantener en rango óptimo (evitar infrautilización y saturación).
- **Notas operativas:** Separar unidades (UCI, quirófano, planta). Ajustar por cierres/obras.
- **Sesgos comunes / Riesgos de interpretación:** Ocupación alta puede elevar tiempos de espera y deteriorar calidad.
- **Relación con Convercus:** Convercus: efecto indirecto (mejor programación y adherencia reduce picos); no es palanca principal.
- **Compuerta de piloto (Gate):** no (resultado estructural).
- **Estado de calidad de dato:** B

### KPI-305 — Estancia media (ALOS)
- **Definición:** Promedio de días de estancia por episodio de hospitalización.
- **Fórmula:** Σ días estancia ÷ # altas.
- **Unidad:** días.
- **Fuente de datos (sistemas):** HIS/EMR + BI clínico.
- **Nivel de cálculo:** episodio | diagnóstico | unidad
- **Frecuencia de medición:** mensual
- **Owner (responsable):** Dirección médica + Operaciones
- **Umbral/Objetivo:** ↓ vs baseline donde aplique sin subir readmisiones; objetivo por case-mix.
- **Notas operativas:** Controlar por complejidad y protocolos clínicos; ALOS no es solo eficiencia.
- **Sesgos comunes / Riesgos de interpretación:** Reducir ALOS sin control puede aumentar readmisiones; usar junto a KPI-306.
- **Relación con Convercus:** Convercus: journeys post-alta y seguimiento (si existe consentimiento) para mejorar adherencia y reducir reingresos evitables.
- **Compuerta de piloto (Gate):** sí (si se usa en programas post-alta).
- **Estado de calidad de dato:** B

### KPI-306 — Readmission Rate (30 días)
- **Definición:** Porcentaje de pacientes reingresados en 30 días tras alta (indicador de calidad).
- **Fórmula:** # reingresos 30d ÷ # altas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** HIS/EMR + BI clínico.
- **Nivel de cálculo:** paciente | diagnóstico | unidad | cohorte
- **Frecuencia de medición:** mensual
- **Owner (responsable):** Dirección médica / Calidad
- **Umbral/Objetivo:** ≤ baseline; umbrales por patología.
- **Notas operativas:** Definir readmisión evitable vs no evitable. Ajustar por case-mix.
- **Sesgos comunes / Riesgos de interpretación:** Sesgo si falta integración entre centros o si el paciente reingresa fuera de red.
- **Relación con Convercus:** Convercus: seguimiento y comunicación post-alta (bajo consentimiento), recordatorios y educación.
- **Compuerta de piloto (Gate):** sí (guardarraíl de calidad).
- **Estado de calidad de dato:** C→B

### KPI-307 — Margen de contribución por episodio (CM per Episode)
- **Definición:** Margen tras costes variables atribuibles por episodio/procedimiento.
- **Fórmula:** Ingresos episodio − costes variables atribuibles.
- **Unidad:** € (+ %).
- **Fuente de datos (sistemas):** Finance + cost accounting + HIS (codificación).
- **Nivel de cálculo:** episodio | DRG/código | centro
- **Frecuencia de medición:** mensual/trimestral
- **Owner (responsable):** CFO / Controller + Dirección de servicio
- **Umbral/Objetivo:** ↑ vs baseline; usar para priorizar servicios y eficiencia.
- **Notas operativas:** Requiere costeo por actividad o asignación consistente. Separar reingresos/complicaciones.
- **Sesgos comunes / Riesgos de interpretación:** Costeo incompleto distorsiona; riesgo alto en decisiones estratégicas.
- **Relación con Convercus:** Convercus: palanca indirecta (reducción de no-shows, mejor adherencia y satisfacción) que impacta costes variables.
- **Compuerta de piloto (Gate):** sí (para escalado).
- **Estado de calidad de dato:** C

### KPI-308 — Claim Denial Rate (rechazo de aseguradora)
- **Definición:** Porcentaje de reclamaciones rechazadas por pagadores/aseguradoras.
- **Fórmula:** # reclamaciones rechazadas ÷ # reclamaciones presentadas.
- **Unidad:** %.
- **Fuente de datos (sistemas):** Revenue Cycle Management (RCM) + billing.
- **Nivel de cálculo:** pagador | código | mes
- **Frecuencia de medición:** mensual
- **Owner (responsable):** Revenue Cycle / Billing
- **Umbral/Objetivo:** ↓ vs baseline; umbral crítico por pagador.
- **Notas operativas:** Clasificar motivos (codificación, documentación, elegibilidad).
- **Sesgos comunes / Riesgos de interpretación:** Si se oculta denegación con write-offs, no se ve el problema real.
- **Relación con Convercus:** Convercus: puede apoyar comunicación y documentación al paciente; palanca principal está en RCM.
- **Compuerta de piloto (Gate):** sí (riesgo financiero).
- **Estado de calidad de dato:** B

### KPI-309 — DSO / Días en cuentas por cobrar (A/R Days)
- **Definición:** Tiempo promedio de cobro (ciclo de caja) para ingresos facturados.
- **Fórmula:** Cuentas por cobrar ÷ (ingresos diarios promedio).
- **Unidad:** días.
- **Fuente de datos (sistemas):** Finance/RCM.
- **Nivel de cálculo:** centro | pagador | mes
- **Frecuencia de medición:** mensual
- **Owner (responsable):** CFO / Revenue Cycle
- **Umbral/Objetivo:** ↓ vs baseline; objetivo por pagador.
- **Notas operativas:** Ajustar por mix de pagadores. Separar facturas en disputa.
- **Sesgos comunes / Riesgos de interpretación:** Cambios contables pueden distorsionar; requiere gobernanza financiera.
- **Relación con Convercus:** Convercus: impacto indirecto (menos disputas por comunicación); palanca principal está en RCM.
- **Compuerta de piloto (Gate):** no.
- **Estado de calidad de dato:** A/B

### KPI-310 — Satisfacción del paciente (CSAT/NPS/Patient Experience)
- **Definición:** Medición de experiencia del paciente pre/durante/post atención.
- **Fórmula:** CSAT promedio y/o NPS; incluir también quejas por 1.000 episodios.
- **Unidad:** score.
- **Fuente de datos (sistemas):** Encuestas + CRM + sistema de quejas.
- **Nivel de cálculo:** episodio | centro | servicio
- **Frecuencia de medición:** mensual (alertas semanales)
- **Owner (responsable):** Calidad / Experiencia paciente
- **Umbral/Objetivo:** ≥ baseline; umbral mínimo (si cae, ajustar journeys).
- **Notas operativas:** Separar por servicio y canal; controlar sesgo de respuesta.
- **Sesgos comunes / Riesgos de interpretación:** Mejorar eficiencia puede empeorar experiencia si se reduce contacto humano; usar como guardarraíl.
- **Relación con Convercus:** Convercus: journeys omnicanal, recordatorios, seguimiento, resolución proactiva (con consentimiento).
- **Compuerta de piloto (Gate):** sí (guardarraíl).
- **Estado de calidad de dato:** B

## 10) “Paquete mínimo” recomendado para cualquier piloto Convercus (12 semanas)

> Selección de KPIs para que el piloto sea defendible en comité (Marketing + Ops + CFO).

1) **KPI-010 Identification Rate** (leading, habilitador)  
2) **KPI-012 Repeat Rate 60/90d** (resultado temprano)  
3) **KPI-024 Return Rate** + **KPI-025 Exchange over Refund** (cost-to-serve + margen)  
4) **KPI-020 Full-Price Sell-Through** y/o **KPI-021 % Sales on Discount** (disciplina de margen)  
5) **KPI-003 Contribution Margin per Order** (control del “no comprar ventas”)  

---

## 11) Índice rápido por “owner” (para asignación inmediata)

- **Finanzas/CFO:** KPI-001, KPI-002, KPI-003, KPI-004, KPI-005, KPI-023, KPI-032  
- **Marketing/CRM:** KPI-010, KPI-011, KPI-012, KPI-013, KPI-015, KPI-016, KPI-033  
- **Operaciones/Omnichannel:** KPI-024, KPI-025, KPI-026, KPI-030, KPI-031, KPI-032  
- **Merchandising/Supply:** KPI-020, KPI-021, KPI-022, KPI-023, KPI-041, KPI-042  

---

---

- **Moda / Merchandising / Planning / Store Ops:** KPI-100, KPI-101, KPI-102, KPI-103, KPI-104, KPI-105, KPI-106, KPI-107  
- **Supermercados / Store Ops / Frescos / Pricing:** KPI-150, KPI-151, KPI-152, KPI-153, KPI-154, KPI-155  
- **Hoteles / Revenue Management / Guest Experience:** KPI-200, KPI-201, KPI-202, KPI-203, KPI-204, KPI-205, KPI-206, KPI-207, KPI-208, KPI-209, KPI-210  
- **Parafarmacias / Category / Compliance / Store Ops:** KPI-250, KPI-251, KPI-252, KPI-253, KPI-254, KPI-255  
- **Sanidad privada / Patient Access / RCM / Calidad:** KPI-300, KPI-301, KPI-302, KPI-303, KPI-304, KPI-305, KPI-306, KPI-307, KPI-308, KPI-309, KPI-310  

## 12) Registro de colisiones y resoluciones (Collision Ledger)

Este registro documenta, de forma auditable, las colisiones detectadas entre el **core transversal** y los **módulos sectoriales**, y la resolución aplicada. El objetivo es evitar deriva semántica y duplicidad de gobierno (dos métricas “parecidas” compitiendo por el mismo espacio decisional).

| Collision-ID | KPI(s) implicados | Tipo | Diagnóstico (qué colisiona) | Decisión | Cambio aplicado (v1.5) |
|---|---|---|---|---|---|
| COL-001 | KPI-001 ↔ KPI-051 | Semántica / ontológica | “Net Sales” (retail) y “Net Revenue” (viajes) usan el mismo significante de “ingreso neto”, pero cambian modelo (agency/merchant) y tratamiento de refunds/contraingresos. | **Generalizar core + instanciación sectorial** | KPI-001 renombrado a **Net Revenue (Net Sales / Net Revenue)** con fórmula bifurcada; KPI-051 mantiene detalle travel y se declara equivalencia a KPI-001. |
| COL-002 | KPI-003 ↔ KPI-053 | Formal (unidad) | Margen de contribución “por order” vs “por reserva”; mismo concepto, distinta unidad de análisis. | **Generalizar core + alias sectorial** | KPI-003 generalizado a **CM por transacción (CM/txn)**; KPI-053 mantiene contexto travel y se declara equivalencia a KPI-003. |
| COL-003 | KPI-014 ↔ KPI-055 | Semántica | LTV/CLV contribution-based es transversal; el módulo de Viajes replicaba el concepto con distinto rótulo. | **Alias sectorial** | KPI-014 incorpora nota de instanciación travel; KPI-055 se mantiene como entrada travel pero se declara equivalencia a KPI-014 (y se refuerza uso de proxies en piloto corto). |
| COL-004 | KPI-032 ↔ KPI-064 | Formal (unidad) | Cost-to-Serve por order vs por reserva; mismo constructo, distinta unidad. | **Generalizar core + instanciación sectorial** | KPI-032 pasa a “Cost-to-Serve per Transaction”; KPI-064 se declara equivalencia a KPI-032. |
| COL-005 | KPI-033 ↔ KPI-056 | Causal / alcance | Conversión digital en último tramo (checkout) vs conversión por etapas (embudo completo). | **Split controlado (complementarios)** | KPI-033 se renombra como “Digital Checkout”; KPI-056 conserva embudo por etapas en Viajes; se añaden referencias cruzadas. |
| COL-006 | KPI-016 ↔ KPI-021 ↔ KPI-070 | Causal (doble conteo de “incentivo/discount”) | Incentivos pueden aparecer como descuento (pricing), rebate (programa) o dilución de margen; riesgo de doble conteo y de “comprar ventas”. | **Marco de disciplina (sin merge)** | Se mantiene cada KPI por su naturaleza, pero se recomienda en gobernanza reportarlos juntos: coste incentivo (KPI-016), share descuento (KPI-021) y dilución (KPI-070). |


## 13) Índice de alias y equivalencias (canónicos ↔ instanciaciones)

Este índice define qué KPI actúa como **canónico** (core) y qué entradas sectoriales funcionan como **instanciación** (mismo constructo con unidad/fuente/modelo específico). El canónico es el que se usa para gobernanza transversal; la instanciación aporta el detalle operativo sectorial.

- **KPI-001 (Canónico): Net Revenue (Net Sales / Net Revenue)**  
  - *Retail:* “Revenue (Net Sales)” (terminología histórica)  
  - *Viajes (instanciación):* **KPI-051** (Net Revenue con agency/merchant y tratamiento de refunds/chargebacks)

- **KPI-003 (Canónico): Contribution Margin per Transaction (CM/txn)**  
  - *Retail:* CM per order/ticket  
  - *Viajes (instanciación):* **KPI-053** (CM por reserva / cliente / canal)

- **KPI-014 (Canónico): LTV (cohort, contribution-based)**  
  - *Viajes (instanciación):* **KPI-055** (CLV/LTV, con proxies para pilotos de 12 semanas)

- **KPI-032 (Canónico): Cost-to-Serve per Transaction (by route)**  
  - *Viajes (instanciación):* **KPI-064** (Cost-to-Serve por reserva)

- **KPI-033 (Canónico): Conversion Rate (Digital Checkout)**  
  - *Viajes (complemento embudo):* **KPI-056** (Conversión por etapas; KPI-033 suele ser la última etapa o un “macro” de conversión)

