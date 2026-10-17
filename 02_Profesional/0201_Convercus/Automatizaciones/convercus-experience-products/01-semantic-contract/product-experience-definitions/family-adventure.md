---
id: "product-experience:family-adventure@candidate-1"
name: "Aventura Familiar"
sector: "Hospitality"
status: "READY WITH EXPLICIT GAPS — non-executable candidate"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
source_material: "Convercus New Generation Loyalty ES, slide 6 and speaker notes"
source_sha256: "53c9e7db3116f13f38d13da34f146aa913a5cef4707616ffc9f4f317ceefce1e"
semantic_authority: "Product Experience Definition candidate subordinate to TES; commercial source is non-normative"
language: es
version: "candidate-1"
date: "2026-09-04"
document_type: "definición candidata de Product Experience"
---

# Aventura Familiar

> [!important] Candidata no ejecutable y subordinada a TES
> Esta definición interpreta material comercial; no modifica TES, no valida afirmaciones comerciales y no constituye todavía un contrato runtime. Los gaps declarados no pueden completarse desde la conveniencia de Demo Factory.

## Propósito y transformación pretendida

Crear continuidad entre la llegada de una familia o grupo y su participación compartida en actividades del hotel durante la estancia. La fuente pretende aumentar la participación familiar y el consumo complementario; solo la primera parte puede formularse como orientación participante. El cambio experiencial exacto —más allá de haber realizado actividades— permanece por validar.

## Participante o sujeto

- Familia o grupo asociado a una reserva.
- Niños u otros participantes que realizan actividades.
- La relación entre titular de reserva, individuos y grupo requiere modelado y validación posteriores; no se presume una única participación colectiva TES.

## Dependencias de Scenario

- reserva identificada como familiar o grupal;
- llegada/check-in en una propiedad concreta;
- estancia vigente y catálogo local de actividades;
- disponibilidad de app/programa y asistencia de recepción;
- canales QR, personal y posible integración TPV para registrar actividad.

Propiedad, booking, stay, oferta local, copy de bienvenida y prospecto pertenecen al Scenario o a la composición, no al núcleo semántico de esta candidata.

## Evidencia y eventos relevantes respaldados por la fuente

La fuente respalda como ocurrencias observables candidatas:

- identificación de una reserva familiar/grupal;
- llegada o check-in;
- registro en app/programa;
- participación completada en una actividad diaria;
- validación por QR o personal;
- checkout;
- compartición de una foto o reserva futura, si llegan a observarse.

Estas ocurrencias no son automáticamente Eventos TES. Su significación debe reconocerse en contexto. La validación de una actividad es el candidato más claro a evidencia de participación dentro de esta definición.

## Hipótesis de Pattern

La repetición de participaciones verificadas en actividades diversas durante una misma estancia podría indicar una regularidad de exploración y participación familiar compartida. La fuente aporta multiplicidad y continuidad diaria, pero no define el criterio que distingue Pattern de simple acumulación. La hipótesis queda abierta.

## Sequence

La fuente presenta este orden comercial:

```text
reserva familiar identificada / check-in
→ registro y “Mi Aventura”
→ actividades diarias verificadas
→ mensajes de continuidad
→ umbral y recompensa
→ checkout e invitación futura
```

Este orden apoya una secuencia candidata. No se afirma que todos los pasos sean obligatorios, que cada actividad tenga orden interno ni que la secuencia comercial sea ya una TES Sequence validada.

## Interpretación de Progression

La transformación candidata sería el desplazamiento desde invitación/registro hacia participación compartida sostenida durante la estancia. Estrellas, número de actividades y mensajes de “falta una” son indicadores comerciales o mecánicas; no constituyen por sí mismos TES Progression. Estados, umbrales y relación con la transformación requieren validación.

## Result pretendido

La fuente permite afirmar operativamente que una familia puede terminar habiendo participado en varias actividades y recibiendo reconocimiento o beneficios. No permite afirmar todavía qué cambio participante observado constituye el Result de la Experience. Incremento de consumo, repetición y recomendación son objetivos de negocio, no sustitutos de ese Result.

## Medición y evidencia

Material disponible para reconstrucción o medición:

- registros de programa/app;
- validaciones QR o de personal por actividad;
- actividad, momento, participante y estancia correlacionados;
- recompensa emitida o utilizada;
- compartición y reserva posterior, cuando se observen.

La fuente no define deduplicación, fiabilidad comparada de canales, atribución, privacidad, ventana de medición ni evidencia suficiente para validar el Result.

## Incentivos

- promesa de estrellas y sorpresas;
- mensajes personalizados de proximidad al umbral;
- anticipación de snacks, acceso prioritario, foto u otros beneficios;
- descuento condicionado a una reserva futura.

## Recompensas

- cupones automáticos al alcanzar un umbral;
- snacks, acceso prioritario a cenas temáticas o foto familiar impresa;
- el descuento futuro solo es recompensa si se concede tras la condición especificada.

Las estrellas, mensajes y recompensas apoyan la Experience; no la definen.

## Gaps semánticos no resueltos

- patrón relevante y criterio de reconocimiento;
- Result participante distinguible de actividad completada y KPI comercial;
- estados y Progression compatibles con la transformación;
- unidad de participación individual, grupal o relacionada;
- reglas de elegibilidad, reentrada, abandono y simultaneidad;
- umbral y equivalencia entre actividades;
- evidencia suficiente y tratamiento de validaciones contradictorias;
- Measurement del cambio participante;
- Learning reutilizable y mecanismo de validación;
- relación entre invitación de próxima visita y la Experience actual.

## Interpretaciones prohibidas

- `check-in` no implica inicio automático de una Experience.
- Una validación QR no es automáticamente un Evento TES.
- Estrellas o conteo de actividades no son automáticamente Progression.
- Alcanzar el umbral no demuestra Experience Completion ni Result.
- Cupón, snack, prioridad, foto o descuento no son el Result experiencial.
- El aumento de F&B, repetición o recomendación no sustituye al Result participante.
- La familia no se modela automáticamente como una sola participación TES.
- “Mi Aventura” es UI/canal, no Experience Definition.
