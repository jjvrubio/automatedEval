---
titulo: TES_KPI_Dictionary
aliases:
  - Diccionario KPI del TES
  - Diccionario operativo de medición TES
idioma: es
fecha: '2026-04-16'
version: v3.0
estado: activo
estado_edicion: revisado
tipo: diccionario_operativo_de_kpi
capa: externalizacion_funcional_critica
alcance: medicion_trazabilidad_validacion_operativa_y_especializacion_sectorial
funcion: normalizar la medición del TES como extensión analítica crítica, fijar un vocabulario operativo de KPI y sostener el contacto, el contraste y el aprendizaje sin reocupar el núcleo irreducible
canonico: false
rige:
  - arquitectura_operativa_de_medicion
  - nomenclatura_estable_de_kpi
  - trazabilidad_de_fuente_formula_y_responsable
  - distincion_entre_core_transversal_y_modulos_sectoriales
  - control_de_colisiones_y_alias
  - compatibilidad_con_validacion_y_bucle_de_aprendizaje
dominio_precedencia: extension_analitica_critica_y_gobernanza_metrica
depende_de:
  - TES_Ontologia_Accion_Situada
  - TES_Experience_Ledger
  - TES_Protocolo_Validacion
  - TES_Lexico
  - TES_Gobernanza_Documental
  - LEEME
documentos_relacionados:
  - KPI Dictionary VERTICALS v1_6
  - Explicación semántica de los KPI
  - Archetype_Map_v1_0
  - Glosario_Convercus_ES
tags:
  - TES
  - KPI
  - medicion
  - extension-operativa-critica
  - validacion
  - trazabilidad
  - metricas
---

# TES_KPI_Dictionary

## Naturaleza de esta pieza

Este documento desarrolla la **capa analítica** del TES fuera del núcleo irreducible.

Su función no es redefinir la ontología ni desplazar el centro del sistema hacia la métrica. Su tarea es fijar una infraestructura estable para nombrar, medir, comparar y gobernar resultados sin deriva semántica ni colisión metodológica.

## 1. Principio rector

La medición sigue al resultado y precede al aprendizaje.

El KPI no sustituye la acción, la secuencia ni la validación. Mide una consecuencia reconstruible de ellas.

## 2. Estatuto dentro del sistema

`TES_KPI_Dictionary` pertenece a `/medicion/` como **extensión analítica crítica**.

Eso implica:

- no forma parte del núcleo irreducible;
- no actúa como fundamento del TES;
- no redefine ontología, ledger, telar, política ni validación;
- pero sí conserva relevancia alta para contacto, contraste, gobernanza métrica, aprendizaje y especialización sectorial.

La externalización no lo convierte en pieza accesoria. Lo sitúa fuera del núcleo irreducible sin degradar su peso operativo dentro del sistema.

## 3. Qué resuelve

Este diccionario corrige cuatro fallos recurrentes:

1. ambigüedad de definición;
2. ambigüedad de medición;
3. ambigüedad de causalidad;
4. ambigüedad de arquitectura entre core, sector y campaña.

## 4. Reglas estructurales

1. Ningún KPI vale por su nombre.
2. Todo KPI debe poder reconstruirse por definición, fórmula, fuente, nivel de cálculo, frecuencia, responsable y criterio de interpretación.
3. El core transversal prevalece sobre proliferaciones locales.
4. Toda afirmación causal debe declarar su método de contraste.
5. Las métricas de campaña o pieza específica viven como derivación, no como núcleo.

## 5. Plantilla canónica de ficha KPI

```yaml
KPI ID:
Nombre canónico:
Familia:
Definición:
Cadena TES principal afectada:
Fórmula:
Unidad:
Fuente de datos:
Nivel de cálculo:
Frecuencia de medición:
Responsable:
Umbral / objetivo:
Notas operativas:
Sesgos comunes / riesgos de interpretación:
Relación con palancas o mecanismos del sistema:
Compuerta de decisión:
Estado de calidad de dato:
Alias / equivalencias:
```

## 6. Escala de calidad del dato

- **A**: definición y fórmula estables; fuente única o reconciliada; latencia conocida; histórico suficiente.
- **B**: definición estable, pero con múltiples fuentes, histórico parcial o latencia variable.
- **C**: definición no consolidada, no instrumentada o todavía no comparable.

## 7. Arquitectura general

### Core transversal

- KPI-001–009 — economía y valor agregado
- KPI-010–019 — identificación, activación, recurrencia y valor de actor
- KPI-020–029 — secuencia, progresión, resultado y validación
- KPI-030–039 — conversión, ruta, coste de servicio y resolución operativa
- KPI-040–049 — cobertura de medición, contraste causal y cierre de aprendizaje

### Módulos sectoriales de referencia

- **KPI-050–099 — Viajes / Travel**: agencias, mayoristas/turoperación y programas de destino (turismo), incluyendo pagos/refunds/chargebacks y cost-to-serve por reserva.
- **KPI-100–149 — Distribución de moda, zapatos y complementos**: descuentos, inventario, devoluciones, tallas y disciplina promocional.
- **KPI-150–199 — Supermercados de alimentación y hogar**: frescos, disponibilidad, merma, ejecución operativa y cadencias cortas.
- **KPI-200–249 — Hoteles, alojamientos y hospitality**: ocupación, ADR/RevPAR, canal directo, estancias, revenue management y satisfacción.
- **KPI-250–299 — Parafarmacias**: mix y margen por categoría, recurrencia, caducidades, compliance promocional y servicios de consejo.
- **KPI-300–349 — Atención sanitaria y hospitalaria (privada)**: acceso de pacientes, utilización clínica, margen por episodio, revenue-cycle y experiencia.
- **KPI-350–399 — Reservado**: futuros verticales y sub-rangos.

Este diccionario debe utilizarse:

- para normalizar nombres y fórmulas de KPI;
- para reconstruir trazabilidad métrica en piezas y casos;
- para sostener lectura de pilotos, diagnósticos y gobernanza;
- y para preservar una capa de medición compatible con ontología, ledger, validación y aprendizaje.

No debe utilizarse:

- para sustituir la ontología;
- para convertir cifras de campaña en doctrina de sistema;
- ni para reclamar centralidad nuclear que ya no le corresponde en el estado comprimido.

### Reglas de mantenimiento

1) **No reutilizar IDs**: si un KPI se elimina, su ID no se reasigna.
2) **Fuente + fórmula obligatorias**: si no existe trazabilidad aún, se permite un KPI en estado *C* (pendiente de instrumentación), pero nunca sin definir fuente y fórmula objetivo.
3) **Referencias internas**: cualquier “Paquete mínimo”, mapa de palancas o checklist debe referenciar **KPI-IDs**, no nombres sueltos.
4) **Compatibilidad core↔sector**: cuando un KPI del core aplica al sector sin cambios materiales, se referencia el **KPI core**. Solo se crea KPI sectorial si hay diferencias inevitables (unidad de análisis, fuente o fórmula) que impidan comparabilidad.



## 9. Nota de cierre

La medición no desaparece del TES.

Se vuelve más rigurosa cuando deja de fingir que es el centro del sistema.
