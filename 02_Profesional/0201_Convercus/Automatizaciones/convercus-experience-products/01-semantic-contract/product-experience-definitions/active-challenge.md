---
id: "product-experience:active-challenge@candidate-1"
name: "Desafío Activo"
sector: "Hospitality"
status: "READY WITH EXPLICIT GAPS — non-executable candidate"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
source_material: "Convercus New Generation Loyalty ES, slide 7"
source_sha256: "53c9e7db3116f13f38d13da34f146aa913a5cef4707616ffc9f4f317ceefce1e"
semantic_authority: "Product Experience Definition candidate subordinate to TES; commercial source is non-normative"
language: es
version: "candidate-1"
date: "2026-09-04"
document_type: "definición candidata de Product Experience"
---

# Desafío Activo

> [!important] Candidata no ejecutable y subordinada a TES
> Esta definición conserva los límites de una fuente comercial breve. No modifica TES ni constituye una configuración runtime. Todo elemento no respaldado permanece como gap.

## Propósito y transformación pretendida

Favorecer una participación deportiva o de bienestar sostenida durante una estancia, en lugar de una interacción aislada con una actividad. La fuente declara como objetivos aumentar la participación y mejorar el uso de spa y áreas activas. No demuestra mejora de bienestar ni define todavía el cambio participante observado que cerraría la transformación.

## Participante o sujeto

- Huésped durante una estancia hotelera.
- La fuente dice “cada huésped”, pero no precisa elegibilidad, edad, unidad de participación ni relación con grupos.

## Dependencias de Scenario

- estancia vigente en una propiedad con oferta deportiva/bienestar;
- actividades disponibles, por ejemplo yoga, spinning, pádel o crossfit;
- reto comunicado al huésped;
- QR, TPV o app capaces de aportar validaciones;
- disponibilidad de los beneficios anunciados.

Hotel, stay, horarios, catálogo local, canales y beneficio concreto son dependencias situadas, no semántica universal de la Experience.

## Evidencia y eventos relevantes respaldados por la fuente

- reto recibido o activado, si el canal lo registra;
- participación/completitud de una actividad deportiva o de bienestar;
- validación de esa actividad mediante QR, TPV o app;
- concesión del beneficio automático tras la condición.

La validación es evidencia técnica. Solo una evaluación contextual puede reconocer su papel dentro de esta candidata.

## Hipótesis de Pattern

Varias participaciones verificadas en actividades deportivas o de bienestar dentro de una estancia podrían expresar una regularidad de implicación activa. La fuente exige tres actividades, pero no explica si diversidad, repetición, intensidad o continuidad son semánticamente relevantes. El Pattern no queda validado por el contador 3/3.

## Sequence

```text
reto durante la estancia
→ actividad deportiva/bienestar validada
→ nuevas actividades hasta la condición comercial
→ beneficio concedido
```

Existe orden entre activación, participaciones y concesión. No se prescribe orden entre las tres actividades ni se afirma que el flujo comercial sea ya una TES Sequence completa.

## Interpretación de Progression

La candidata apunta a un desplazamiento desde disponibilidad/invitación hacia participación reiterada durante la estancia. El progreso visual 0/3–3/3 y las insignias son representaciones o mecánicas. Falta demostrar qué cambio de estado hace que ese desplazamiento sea TES Progression y no mero recuento.

## Result pretendido

El source permite observar que el huésped ha realizado varias actividades. No permite inferir que haya mejorado su bienestar ni que el uso del spa sea un Result participante. “Mejorar el uso” es un objetivo comercial. El Result participante queda explícitamente sin resolver.

## Medición y evidencia

- validaciones QR/TPV/app correlacionadas con huésped, actividad y estancia;
- número y tipo de actividades verificadas;
- beneficio emitido o utilizado;
- uso agregado de spa/áreas activas como KPI de negocio separado.

No se especifican evidencia suficiente, prevención de duplicados, comparabilidad de canales, ventanas temporales, medición de transformación ni Learning.

## Incentivos

- comunicación del reto;
- progreso visual e insignias;
- promesa de spa, smoothie o upgrade wellness.

## Recompensas

- spa, smoothie o upgrade wellness concedido automáticamente tras la condición.

La recompensa no constituye el Result de la Experience.

## Gaps semánticos no resueltos

- Result participante y Measurement asociado;
- Pattern más allá de tres registros;
- estados y Progression no reducidos al contador;
- elegibilidad y unidad de participación;
- equivalencia, diversidad y repetición de actividades;
- definición operativa de actividad “completada”;
- corrección, duplicidad y fiabilidad entre QR/TPV/app;
- abandono, expiración y reentrada;
- Learning reutilizable;
- relación entre bienestar pretendido y evidencia disponible.

## Interpretaciones prohibidas

- Tres validaciones no son automáticamente Pattern, Sequence, Progression o Completion.
- El contador y las insignias no son estados TES.
- Una lectura QR/TPV/app no es automáticamente un Evento TES.
- El beneficio automático no es Result.
- Uso de spa o áreas activas no demuestra bienestar del participante.
- “Desafío” es una forma comercial; no concede por sí misma estatuto de Experience.
