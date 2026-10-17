---
title: "Session 10 — Interpretación de fuentes comerciales y readiness semántico"
aliases:
- "Commercial Experience Source Interpretation and Semantic Readiness"
language: es
version: "v1.0"
status: "evaluado"
date: "2026-09-04"
project: "Convercus Experience Products"
document_type: "informe de readiness semántico"
scope: "interpretación gobernada del deck Convercus New Generation Loyalty ES y prerrequisitos de H3"
repository_role: "evaluación de fuente comercial previa a Product Experience Definitions y reapertura de H3"
semantic_authority: "análisis de producto subordinado a TES; la fuente comercial es no normativa"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 10 — Interpretación de fuentes comerciales y readiness semántico

## 1. Conclusión ejecutiva

La presentación **Convercus New Generation Loyalty ES** contiene material suficiente para redactar tres Product Experience Definitions no ejecutables y subordinadas a TES, todas con gaps explícitos:

- Aventura Familiar;
- Desafío Activo;
- Circuito Sostenible.

Ninguna diapositiva constituye por sí misma una definición. **Embajadores de Estilo** permanece como concepto comercial insuficiente; **Maratón de Temporada** es, con el material actual, una campaña/reto gamificado sin Result participante ni Pattern defendibles; y **Antes–Durante–Después** es un marco de lifecycle/orquestación que puede contener varias Experiences, campañas y tácticas.

Tras retirar puntos, estrellas, insignias, cupones y recompensas, los tres candidatos promovidos conservan una transformación candidata: participación familiar compartida, implicación deportiva/bienestar reiterada y práctica circular continuada. Aun así, los criterios de Pattern, el Result participante observado, Measurement y Learning requieren validación adicional. Por eso reciben exactamente **READY WITH EXPLICIT GAPS** y no una aprobación semántica completa.

H3 obtiene una base independiente de su experimento: una validación factual de participación en una actividad deportiva durante una estancia puede evaluarse respecto de Aventura Familiar y Desafío Activo. En la primera aporta evidencia de participación compartida en actividades del hotel; en la segunda, evidencia de implicación deportiva/bienestar. Ambas candidatas existían en la fuente por razones comerciales propias, no fueron diseñadas para H3.

Veredicto: **GO — H3 SEMANTIC PREREQUISITES SATISFIED.** Este GO autoriza reconsiderar el experimento estrecho de Session 9; no autoriza runtime, evaluator, Pattern, Progression, engine ni conversión de los documentos en TypeScript.

## 2. Clasificación de autoridad de la fuente

### Fuente inspeccionada

| Propiedad | Valor |
|---|---|
| Título | `Convercus New Generation Loyalty ES` |
| Formato inspeccionado | PPTX completo: 20 slides y 19 speaker-note parts. El PDF equivalente se localizó, pero la extracción se realizó desde el PPTX local. |
| Ubicación de origen | OneDrive Convercus, `Branding & Narratives/Narratives/` |
| Modificación del PPTX | 2026-08-31T10:49:25+0100 |
| SHA-256 | `53c9e7db3116f13f38d13da34f146aa913a5cef4707616ffc9f4f317ceefce1e` |
| Audiencia declarada | Marketing; inversores cualificados, clientes profesionales y contrapartes apropiadas. |
| Clasificación | **Product source material — non-normative.** |

La presentación describe intención comercial, ejemplos, canales, mecánicas y claims. No gobierna TES ni puede pasar directamente a runtime.

```text
TES semantic authority
        ↓
Product Interpretations subordinate to TES
        ↓
Commercial / product source material
        ↓
Candidate Experience interpretation
        ↓
TES semantic validation
        ↓
Validated Product Experience Definition
        ↓
Demo Factory runtime reference
```

Los documentos creados en esta sesión se encuentran todavía entre **Candidate Experience interpretation** y una validación de producto subordinada con gaps. No son referencias runtime ni una implementación del TES Experience Ledger.

## 3. Extracción de semántica comercial

Solo se recoge contenido presente en slides o notas. “No especificado” significa que no se completó desde conocimiento sectorial.

### Hospitality — macro-marco Antes–Durante–Después

| Dimensión | Evidencia respaldada por la fuente |
|---|---|
| Commercial name | Lealtad Dinámica: Antes–Durante–Después. |
| Sector | Hospitality. |
| Stated objective | Acompañar al huésped/viajero en todo el recorrido con experiencias personalizadas que incrementen gasto y fortalezcan la relación de marca. |
| Actors / participants | Huésped/viajero; no se especifican roles adicionales. |
| Context | Antes/reserva, durante/acomodación-servicios-tours, después/agradecimiento-próxima visita. |
| Observed actions | Reserva directa; consumo durante estancia; futura visita/recomendación implícitas como outcomes, no eventos definidos. |
| Validation / evidence sources | Notas: integración en tiempo real con TPV y PMS; análisis de comportamiento. No hay esquema evidenciario. |
| Conditions / thresholds | Reserva por web/app; upgrade según consumo; no se detallan reglas. |
| Sequence indications | Orden lifecycle explícito antes → durante → después. |
| Progress indications | Ninguna progresión participante explícita. |
| Incentives | Incentivo por reserva directa; ofertas personalizadas; upgrade. |
| Rewards | Mensaje de agradecimiento y recompensa para próxima visita. |
| Intended participant outcome | Ahorro/exclusividad, experiencia mejorada, reconocimiento y continuidad emocional, expresados como promesas comerciales. |
| Intended business outcome | Más reserva directa, menos comisión OTA, mayor ticket, repetición y recomendación. |
| Channels / systems | Web, app, TPV, PMS; notas añaden email y SMS. |
| Ambiguities | Mezcla lifecycle, campañas, ofertas, canales, claims humanos y KPI; no identifica una transformación unitaria. |

### Hospitality H-A — Aventura Familiar

| Dimensión | Evidencia respaldada por la fuente |
|---|---|
| Commercial name | Lealtad Social: Aventura Familiar, búsqueda del tesoro. |
| Sector | Hospitality. |
| Stated objective | Incrementar participación de familias en actividades y consumo de servicios complementarios. |
| Actors / participants | Familia/grupo; niños/participantes; recepcionista/staff como mediadores. |
| Context | Reserva familiar identificada, llegada/check-in, estancia y checkout. |
| Observed actions | Registro en app/programa; actividades como búsqueda del tesoro, cocina, fútbol o arte; escaneo QR o marca del staff; compartir foto; reserva futura condicionada. |
| Validation / evidence sources | QR, staff desde app e integración TPV. |
| Conditions / thresholds | “Cierto número” de estrellas; reserva futura antes de 30 días para descuento. Umbral exacto ausente. |
| Sequence indications | Check-in → registro/Mi Aventura → actividades diarias → mensajes → recompensa → checkout/continuidad. |
| Progress indications | Estrellas digitales y mensaje sobre actividad restante. |
| Incentives | Bienvenida, sorpresas, mensajes de proximidad y descuento futuro. |
| Rewards | Snacks, prioridad en cenas, foto familiar y otros cupones automáticos. |
| Intended participant outcome | Participación compartida y reconocimiento; el cambio experiencial final no se explicita. |
| Intended business outcome | Mayor participación, F&B, souvenirs, experiencias locales, futura reserva y recomendación. |
| Channels / systems | App, QR, staff, TPV; notas añaden email/SMS/displays y reporting. |
| Ambiguities | Unidad individual/grupal; Pattern; Result participante; medición del cambio; umbral; Learning. |

### Hospitality H-B — Desafío Activo

| Dimensión | Evidencia respaldada por la fuente |
|---|---|
| Commercial name | Lealtad Gamificada: Desafío Activo. |
| Sector | Hospitality. |
| Stated objective | Aumentar participación deportiva/bienestar y mejorar uso de spa/áreas activas. |
| Actors / participants | Cada huésped; no se precisa elegibilidad. |
| Context | Durante la estancia, con actividades deportivas y de bienestar disponibles. |
| Observed actions | Completar tres actividades; ejemplos: yoga, spinning, pádel y crossfit. |
| Validation / evidence sources | QR, TPV o app en cada evento, según la slide. |
| Conditions / thresholds | Tres actividades durante la estancia. |
| Sequence indications | Reto → actividades verificadas → condición alcanzada → premio. No hay orden entre actividades. |
| Progress indications | Progreso visual e insignias digitales. |
| Incentives | Reto, visualización, insignias y promesa de beneficio. |
| Rewards | Spa, smoothie o upgrade wellness automático. |
| Intended participant outcome | Participación deportiva/bienestar; mejora de bienestar no afirmada ni medida. |
| Intended business outcome | Uso de spa y áreas activas. |
| Channels / systems | QR, TPV y app. |
| Ambiguities | Pattern, Result, medición, significado de “completar”, elegibilidad y Learning. |

### Fashion & Retail R-A — Embajadores de Estilo

| Dimensión | Evidencia respaldada por la fuente |
|---|---|
| Commercial name | Lealtad Dinámica: Embajadores de Estilo. |
| Sector | Fashion & Retail. |
| Stated objective | Interacción social, recomendación orgánica y comunidad de marca. |
| Actors / participants | No especificado; se infiere comercialmente “cliente”, pero la slide no define sujeto. |
| Context | Tienda y actividad social no detallada. |
| Observed actions | Visita a tienda, posting y valoración. |
| Validation / evidence sources | No especificado. |
| Conditions / thresholds | No especificado. |
| Sequence indications | No especificado. |
| Progress indications | Etiquetas “Cazador de Colecciones”, “Creador de Tendencias” y “Líder de Estilo”, sin reglas. |
| Incentives | No especificado. |
| Rewards | No especificado. |
| Intended participant outcome | Sentido de comunidad, como intención comercial no operacionalizada. |
| Intended business outcome | Interacción social y recomendación orgánica. |
| Channels / systems | Tienda y posting; plataforma no especificada. |
| Ambiguities | Casi toda la estructura semántica y operacional. |

### Fashion & Retail R-B — Circuito Sostenible

| Dimensión | Evidencia respaldada por la fuente |
|---|---|
| Commercial name | Lealtad Social: “Cicuito” Sostenible; se normaliza la errata como Circuito Sostenible. |
| Sector | Fashion & Retail. |
| Stated objective | Reforzar posicionamiento sostenible y retorno de clientes mediante retos verdes. |
| Actors / participants | Cliente consciente; referido; cohortes de empresa/gimnasio/barrio; no se define estatuto grupal. |
| Context | Programa, tienda, causa local, reparación, compra reciclada, retorno textil y fin de temporada. |
| Observed actions | Registro/primera compra/login; seleccionar causa, recordatorio y reto; reparar denim, comprar reciclado, retornar textil; compartir/referir; reentrada. |
| Validation / evidence sources | TPV/QR; tarjetas de impacto; referral; reporting y scoring propuestos. |
| Conditions / thresholds | Regla 2-de-3; alta referida en plazo; cupones por categorías/condiciones. |
| Sequence indications | Descubrir → onboarding → reto 3R → compartir → reentrada → reconocimiento. Las tres acciones 3R son alternativas combinables. |
| Progress indications | Puntos/primer nivel, 2-de-3, scoring y ascenso a Embajador Circular. |
| Incentives | Causa local, retos, recordatorios, puntos, niveles, storytelling y acceso anticipado. |
| Rewards | Bono/recompensa instantánea, acceso, fast-lane e invitación a co-diseñar. |
| Intended participant outcome | Práctica circular y reconocimiento; adopción o cambio efectivo no están definidos. |
| Intended business outcome | Posicionamiento sostenible, retorno, referral y agregados por cohorte. |
| Channels / systems | Noticias/feed geolocalizado, app implícita, TPV/QR y activos compartibles. |
| Ambiguities | Impacto real, unidad de Experience, Pattern/Result, metodología 2,3 kg/scoring, privacidad, Learning. |

### Fashion & Retail R-C — Maratón de Temporada

| Dimensión | Evidencia respaldada por la fuente |
|---|---|
| Commercial name | Lealtad Gamificada: Maratón de Temporada. |
| Sector | Fashion & Retail. |
| Stated objective | Aumentar visitas recurrentes y ticket medio mediante retos por colección/categoría. |
| Actors / participants | Shopper/cliente; no se precisa elegibilidad. |
| Context | Tiendas, temporada, colecciones o categorías: zapatos, accesorios y abrigo. |
| Observed actions | Visitar tiendas, comprar en categorías y escanear QR/registrar compra. |
| Validation / evidence sources | QR o registro de compra. |
| Conditions / thresholds | Completar categorías; número y reglas exactas no especificados. |
| Sequence indications | Visitas/compras → marcador → “completar la maratón”. No hay orden significativo explícito. |
| Progress indications | Marcador actualizado al instante. |
| Incentives | Reto, marcador y promesa de premio. |
| Rewards | Cupón o beneficio experiencial de estilismo. |
| Intended participant outcome | No especificado más allá de completar compras/visitas y recibir premio. |
| Intended business outcome | Recurrencia y ticket medio. |
| Channels / systems | Tienda, QR y registro de compra; sistema concreto no indicado. |
| Ambiguities | Transformación participante, Pattern, Sequence, Progression no reducible a contador, Result, Measurement y Learning. |

## 4. Matriz de clasificación de constructos

| Constructo | Clasificación | Razón |
|---|---|---|
| Antes–Durante–Después | **Lifecycle / orchestration frame**, Scenario context, campañas/tácticas | Ordena momentos y acciones comerciales distintas; no muestra una transformación unitaria ni una participación continua gobernada. |
| Aventura Familiar | **Candidate Experience** + Scenario-specific instantiation + campaña/mecánicas | Conserva una candidata de participación compartida al quitar estrellas/recompensas, pero mezcla reserva, propiedad, UI, canales y promoción futura. |
| Desafío Activo | **Candidate Experience** + campaña/reto + tácticas gamificadas | Conserva participación deportiva reiterada sin badges/premio, aunque su Result y Pattern siguen incompletos. |
| Embajadores de Estilo | **Campaign / tactic / status mechanic / insufficiently specified** | Tres acciones y nombres de niveles no establecen transformación, secuencia, reglas ni evidencia. |
| Circuito Sostenible | **Candidate Experience** + lifecycle/orchestration + varias mecánicas/capabilities | Existe continuidad candidata entre descubrimiento, acciones circulares y reentrada; sus seis fases podrían ocultar varias Experiences. |
| Maratón de Temporada | **Campaign / tactic / loyalty mechanic / commercial concept only** | Sin cupón y marcador quedan visitas/compras orientadas a KPI; no aparece un Result participante o Pattern suficientemente defendible. |
| Estrellas, puntos, marcadores, insignias y niveles | **Tactic / mechanic / UI behaviour** | Representan motivación o estado comercial, no Progression por sí solos. |
| Spa, smoothie, cupones, styling y accesos | **Incentive y/o Reward** | Su función depende del momento de promesa/concesión; no son Result. |
| QR, TPV, PMS, app, feed, email/SMS | **Capability / UI / channel behaviour** | Aportan observación, entrega o comunicación; no definen Experience. |
| Repetición, ticket, F&B, retorno y recomendación | **Business outcome** | Son objetivos/KPI comerciales y no sustituyen el Result participante. |

## 5. Análisis de candidatos Hospitality

### Aventura Familiar

La diapositiva mezcla al menos cuatro planos:

```text
Experience semantic core
  participación familiar compartida y continuada en actividades
+
Scenario
  familia/grupo + reserva + propiedad + estancia + oferta local
+
Mechanics
  estrellas + mensajes + umbral + cupones
+
Channels/capabilities
  Mi Aventura + QR + staff + app + TPV
```

No es necesario decidir ahora si checkout/retorno futuro pertenece a la misma Experience o a una reactivación relacionada. La candidata permanece coherente sin puntos y recompensas, pero falta saber qué diferencia produce la participación en la familia/grupo y cómo observarla.

### Desafío Activo

```text
Experience semantic core
  participación deportiva/bienestar reiterada durante una estancia
+
Scenario
  huésped elegible + hotel + stay + oferta activa
+
Mechanics
  reto de tres + contador + badges + premio
+
Channels/capabilities
  QR + TPV + app
```

La coherencia no depende del spa o smoothie: sigue existiendo una candidata de implicación activa. Sin embargo, completar tres actividades no prueba bienestar ni TES Progression; su Result continúa abierto.

### Marco Hospitality

Booking, stay, property, familia/grupo, huésped y catálogo de servicios son ante todo elementos de Scenario. “Antes–Durante–Después” puede ordenar varias composiciones y campañas, pero sería una sobreextensión declararlo una única Experience.

## 6. Análisis de candidatos Retail

### Embajadores de Estilo

Es el ejemplo que más se presenta comercialmente como identidad/progresión y menos estructura semántica aporta. Visita, posting y valoración pueden ser ocurrencias; tres nombres de nivel son mecánicas. Faltan relación entre acciones, condiciones, participante Result, medición y evidencia. Promoverlo exigiría escribir prácticamente toda la Experience desde imaginación.

### Circuito Sostenible

```text
Experience semantic core
  pasar de descubrimiento a práctica circular verificable y reentrada
+
Scenario
  cliente + retailer + tienda/temporada + servicios/categorías locales
+
Mechanics
  2-de-3 + puntos + nivel + cupón + referral + scoring
+
Channels/capabilities
  feed + TPV/QR + recordatorios + social sharing + reporting
```

Es el candidato comercialmente más rico y el que mejor conserva continuidad al retirar mecánicas. La principal precaución es no comprimir seis fases y varios objetivos en una Experience monolítica. Referral, reconocimiento social y reentrada podrían acabar siendo Experiences relacionadas o intervenciones; el documento candidato no fija esa cardinalidad.

### Maratón de Temporada

Retirar marcador y recompensa deja una estrategia de visitas/compras entre categorías cuyo propósito explícito es elevar recurrencia y ticket. La fuente no explica el cambio participante ni una relación cualitativa entre categorías. Pluralidad de compras no basta para Pattern o Sequence; por tanto, no se redacta Product Experience Definition.

## 7. Validación TES de candidatos promovibles

| Cadena | Aventura Familiar | Desafío Activo | Circuito Sostenible |
|---|---|---|---|
| Event | Actividad verificada puede adquirir significación en la participación familiar. Check-in/registro solo son señales hasta evaluación. | Actividad deportiva/bienestar verificada es candidata clara; QR/TPV/app son evidencia. | Reparación, compra reciclada o retorno pueden adquirir significación; ninguna es Evento TES automáticamente. |
| Pattern | Hipótesis de participación compartida repetida en actividades diversas. Criterio ausente. | Hipótesis de implicación activa reiterada. “Tres” no basta como Pattern. | Hipótesis de práctica circular relacionada/repetida. 2-de-3 es regla comercial, no Pattern. |
| Sequence | Hay orden estancia: invitación/registro, actividades, cierre. Obligatoriedad y ramas ausentes. | Activación precede actividades y concesión; actividades carecen de orden significativo explícito. | Hay arco descubrimiento–onboarding–acción–reentrada; el reto interno admite acciones alternativas. Puede contener varias secuencias. |
| Progression | Participación situada creciente es plausible; estrellas/contador no la demuestran. | Paso de invitación a reiteración es plausible; 0/3–3/3 no la demuestra. | Paso hacia práctica circular y reentrada es plausible; puntos/niveles/scoring no la demuestran. |
| Result | Participación familiar realizada es observable, pero el cambio experiencial no está definido. KPI de consumo no vale. | Varias actividades son observables, pero bienestar no está demostrado. Uso de spa no vale. | Adopción/repetición circular es candidata, pero no hay umbral/evidencia de adopción. Posicionamiento/retorno no valen. |
| Measurement | QR/staff, app, estancia, recompensa y posible retorno permiten reconstrucción parcial. | Validaciones por actividad y beneficio permiten reconstrucción; falta medida del cambio. | TPV/QR, referral, recurrencia e impacto estimado aportan trazas; metodología y autoridad están ausentes. |
| Learning | Notas hablan de reporting y ajustar journeys según resultados, pero no existe Learning específico verificable. | Ausente. | Reporting/scoring aparecen, pero no se explica cómo se convierte Measurement en Learning reutilizable. |

### Mecánica frente a semántica

| Candidato | ¿Permanece coherente sin loyalty mechanics? | Conclusión |
|---|---|---|
| Aventura Familiar | Sí: persiste la continuidad de participación familiar en actividades durante la estancia. | Las mecánicas apoyan motivación y reconocimiento; no definen el núcleo. |
| Desafío Activo | Sí: persiste la implicación deportiva/bienestar reiterada. | El “tres”, los badges y premio operacionalizan un reto, no prueban transformación. |
| Circuito Sostenible | Sí: persiste el arco hacia prácticas circulares y reentrada. | 2-de-3, puntos, niveles y couponing son instrumentación comercial. |
| Embajadores de Estilo | No con la evidencia actual: quedan acciones sociales desconectadas y un objetivo de marca. | Principalmente concepto/campaña. |
| Maratón de Temporada | No de forma suficientemente semántica: quedan visitas/compras entre categorías orientadas a KPI. | Principalmente campaña/reto de cross-sell. |

## 8. Matriz de readiness de Experience Definition

| Candidato | Readiness | Evidencia más fuerte | Ambigüedad más fuerte | Qué se inventaría si se promoviera demasiado pronto | Confianza |
|---|---|---|---|---|---|
| Aventura Familiar | **READY WITH EXPLICIT GAPS** | Contexto, participantes, actividades, evidencia, continuidad de estancia y cierre están descritos. | Result participante, Pattern y unidad grupal. | Transformación familiar, estados, umbral, participación colectiva y Learning. | Media-alta. |
| Desafío Activo | **READY WITH EXPLICIT GAPS** | Un participante situado, clase de acciones, validación, condición y objetivo de participación claros. | Completar 3/3 puede ser solo campaña; Result/bienestar no medido. | Pattern, Progression, Result, elegibilidad y equivalencia de actividades. | Media. |
| Embajadores de Estilo | **COMMERCIAL CONCEPT ONLY** | Objetivo social y tres acciones/labels. | Falta toda continuidad y resultado participante. | Casi toda la Experience, incluidas reglas y evidencias. | Alta sobre el rechazo. |
| Circuito Sostenible | **READY WITH EXPLICIT GAPS** | Acciones circulares heterogéneas, validación, reentrada y arco temporal explícitos. | Puede contener varias Experiences; impacto y Result no definidos. | Unidad, Pattern, impacto, Measurement, Learning y estados. | Alta para definición candidata; media para su unidad. |
| Maratón de Temporada | **COMMERCIAL CONCEPT ONLY** | Acciones, fuente de validación, marcador y condición comercial. | No existe transformación participante tras retirar mecánicas. | Pattern, Sequence significativa, Progression, Result y Learning. | Media-alta. |
| Antes–Durante–Después | **NOT AN EXPERIENCE** | Marco temporal y múltiples intervenciones/canales bien descritos. | No hay núcleo transformacional unitario. | Una Experience artificial que fusionaría reserva, upsell y reactivación. | Alta. |

No hay candidatos **READY FOR PRODUCT EXPERIENCE DEFINITION** sin cualificación. Tres superan el umbral inferior y reciben documentos con gaps; los otros no generan placeholders.

## 9. Responsabilidad de los dos `ExperienceDefinition`

| Tipo actual | Campos | Consumidores | Responsabilidad semántica | Responsabilidad runtime | Estatuto real | Riesgo |
|---|---|---|---|---|---|---|
| `prototype/src/domain/contracts.ts::ExperienceDefinition` | `id`, `name`, `purpose`, `transformationHypothesis`, `mediationField`, `archetype`, `sectorPropensity`, `initialState`, `intendedOutcome`, `tesBaseline` | `DemoPackage`; validator solo comprueba IDs duplicados y presencia cuando TES es required. El paquete canónico contiene `experiences: []`. | Intenta una traducción funcional rica, pero no cubre explícitamente toda la cadena TES y el contrato compartido sigue “en preparación”. | Se empaqueta en el contrato legacy; no lo consume el runtime Demo Factory. | Candidato de definición funcional, no definición aprobada ni activa. | Puede parecer completo y autoritativo pese a campos provisionales y falta de validación semántica. |
| `prototype/src/demo-factory/contracts.ts::ExperienceDefinition` | `id`, `name`, `tesBaseline` | Registry `artifacts.ts`, resolución en `bootstrap.ts` y `ResolvedDemoRuntime`. | No puede expresar semántica; solo conserva identidad nominal y baseline. | Descriptor/header resoluble para composición efectiva. | Runtime Experience descriptor/reference, no definición completa. | El mismo nombre oculta una reducción radical y puede hacer que un header parezca autoridad semántica. |

Conceptualmente conviene distinguir:

```text
ProductExperienceDefinition
        ↓ referenced by
RuntimeExperienceDescriptor / RuntimeExperienceReference
```

La terminología es una recomendación, no un rename. Los nuevos documentos tampoco legitiman automáticamente el tipo de dominio existente: purpose, estado inicial e intended outcome necesitan alinearse con Pattern, Sequence, Progression, Result, Measurement y Learning antes de declararlo contrato compartido.

## 10. Product Experience Definitions candidatas

Se crean únicamente las tres candidatas que alcanzan **READY WITH EXPLICIT GAPS**:

1. [Aventura Familiar](../../../01-semantic-contract/product-experience-definitions/family-adventure.md)
2. [Desafío Activo](../../../01-semantic-contract/product-experience-definitions/active-challenge.md)
3. [Circuito Sostenible](../../../01-semantic-contract/product-experience-definitions/sustainable-circuit.md)

Son documentos no ejecutables. No se incorporan a `artifacts.ts`, manifests, runtime contracts ni UI. Embajadores de Estilo y Maratón de Temporada no reciben definición para evitar que un placeholder adquiera falsa autoridad.

## 11. Matriz Evidence-to-Experience

| Evidence/Input candidato | Aventura Familiar | Desafío Activo | Circuito Sostenible | Relación respaldada por la fuente |
|---|---|---|---|---|
| Validación de participación en actividad deportiva durante una estancia | **Relevante candidata:** actividad diaria compartida; la slide incluye torneo de fútbol y QR/staff. | **Relevante candidata distinta:** actividad deportiva/bienestar; QR/TPV/app. | No relevante con el material actual. | Sí para ambos candidatos Hospitality por motivos declarados independientemente. |
| Check-in/llegada | Señal de contexto/entrada explícita. | Estancia es contexto, pero check-in no se declara condición. | No relevante. | Solo Aventura Familiar de forma directa. |
| Registro en app/programa | Paso explícito de onboarding. | No especificado. | Onboarding sostenible explícito, pero la semántica de registro no es idéntica entre sectores. | No es buen input H3 compartido sin más cualificación. |
| Validación QR genérica | Canal de evidencia, no hecho suficiente sin payload. | Canal de evidencia, no hecho suficiente sin payload. | Canal de evidencia, no hecho suficiente sin payload. | La coincidencia de canal no crea una ocurrencia semánticamente común. |
| Compra con fibras recicladas | No relevante. | No relevante. | Acción 3R explícita. | Solo Circuito Sostenible. |
| Retorno textil | No relevante. | No relevante. | Acción 3R explícita. | Solo Circuito Sostenible. |

### Input recomendado para reabrir H3

```text
X = validación factual de que un huésped/participante
    completó una actividad deportiva identificada
    durante una estancia concreta
```

El input debería conservar identidad, tipo de actividad, instante, sujeto, stay/property y procedencia de validación. No debería contener estrellas, contador 1/3, insignia, copy, `significant`, `experienceRef` ni outcome.

```text
X
├── Aventura Familiar
│   └── posible outcome neutral: evidencia aceptada como participación
│       en actividad compartida de la aventura familiar
└── Desafío Activo
    └── posible outcome neutral: evidencia aceptada como participación
        deportiva/bienestar del desafío activo
```

La evaluación futura deberá demostrar que los outcomes no son strings distintos hard-coded por ID: sus criterios deben derivarse del contexto independiente de cada definición. Tampoco debe afirmar Progression, estrella, 1/3 o Event TES.

## 12. Veredicto de readiness H3

**GO — H3 SEMANTIC PREREQUISITES SATISFIED.**

Se cumplen las precondiciones porque:

1. existen dos candidatas Hospitality defendibles y documentadas por razones independientes de H3;
2. ambas conservan coherencia al retirar las mecánicas;
3. una clase de input concreta —actividad deportiva validada durante estancia— aparece naturalmente en ambas;
4. la relación contextual es distinta y expresable sin Progression, Result o reward;
5. el input puede existir como hecho/evidencia antes de ambas interpretaciones;
6. no fue necesario mezclar sectores ni alterar las definiciones para fabricar overlap.

El GO está limitado a reabrir el experimento mínimo. No convierte las candidatas en definiciones TES plenamente validadas ni resuelve si una persona participa simultáneamente en ambas en producción. El test puede evaluar el mismo input de forma independiente contra dos contextos controlados sin afirmar membresía universal.

## 13. Recomendación de gobierno de source material

Se recomienda, en una sesión de gobernanza separada, distinguir:

```text
01-semantic-contract/
├── source-material/
│   ├── commercial/
│   └── product/
├── product-interpretations/
└── product-experience-definitions/
```

- `source-material/commercial/`: collateral de marketing/ventas, con título, propietario, fecha, versión/hash, audiencia, localizador de páginas/slides y restricciones de uso.
- `source-material/product/`: especificaciones, discovery y decisiones de producto no ontológicas, con la misma procedencia.
- `product-interpretations/`: derivaciones razonadas, subordinadas a TES, que citan fuentes pero no las sustituyen.
- `product-experience-definitions/`: definiciones versionadas que han cruzado un umbral explícito de validación y enumeran gaps/prohibiciones.

La presentación no debe copiarse ni etiquetarse como Product Interpretation. Si se incorpora al repositorio, debe respetarse su confidencialidad, licencia y política documental; alternativamente puede registrarse solo un manifiesto de procedencia y hash. Session 10 no reorganiza ni copia la fuente.

## 14. Reglas de advertencia para lenguaje comercial

1. `Journey` no es automáticamente una entidad TES.
2. `Experience` en marketing no es automáticamente una TES Experience.
3. Puntos, estrellas, contadores, insignias y niveles no significan automáticamente TES Progression.
4. Una reward no es automáticamente Result.
5. Una acción del cliente o una lectura técnica no es automáticamente Event.
6. Varias acciones no constituyen automáticamente Pattern ni Sequence.
7. Un KPI de negocio no es automáticamente Result participante.
8. Mecánicas de campaña pueden apoyar, pero no definir, una Experience.
9. Fases de una presentación pueden describir Scenario, lifecycle u orchestration y no una Experience.
10. Los huecos de simplificación comercial no deben repararse silenciosamente con semántica inventada.
11. Un QR, TPV, PMS o app identifica canal/evidencia, no significación.
12. “Completion” comercial de un reto no implica Experience Completion.
13. Cohorte, familia o grupo comercial no define por sí solo participación colectiva TES.
14. Reporting, scoring o dashboard no equivalen automáticamente a Measurement o Learning.

## 15. Gaps semánticos restantes

- Ninguna candidata define de forma suficiente un Result participante observado.
- Pattern sigue siendo hipótesis en las tres definiciones.
- Las secuencias comerciales no han sido validadas como TES Sequence.
- Progression no está operacionalizada fuera de contadores/mecánicas.
- Learning específico está ausente; reporting y optimización declarados son insuficientes.
- Measurement no dispone de métodos, ventanas, atribución ni evidencia suficiente.
- La participación colectiva familiar requiere validar sujetos, roles y cardinalidad.
- No está decidido si Circuito Sostenible contiene una o varias Experiences relacionadas.
- Elegibilidad, abandono, reentrada y concurrencia carecen de reglas gobernadas.
- Fiabilidad, deduplicación, corrección y privacidad de QR/TPV/app no están especificadas.
- Las claims de bienestar, impacto sostenible y continuidad emocional no están demostradas.
- La cifra de residuo evitado y los scorings carecen de metodología/procedencia.
- El contrato rico `ExperienceDefinition` no representa explícitamente la cadena TES completa.
- El descriptor Demo Factory puede seguir confundiéndose con una definición semántica.
- Una API real podría entregar eventos ya interpretados o ligar evaluación a participación/estado de un modo incompatible con el futuro experimento puro.

## 16. Recomendación GO / CONDITIONAL GO / NO-GO

**GO — H3 SEMANTIC PREREQUISITES SATISFIED para volver a plantear Session 9 como experimento nuevo y acotado.**

El experimento debe usar una única evidencia de actividad deportiva validada y las dos definiciones Hospitality sin mutarlas. Debe devolver outcomes explícitos y neutrales, probar independencia/orden/immutability y mantener Activity como proyección. Debe ser NO-GO si para diferenciar resultados necesita introducir 1/3, estrellas, Progression, Result, participación colectiva completa o reglas inventadas.

Este informe no recomienda implementar nada más: la única pregunta madura es si la frontera `input neutral → evaluación relativa a Experience` sobrevive ejecutablemente con el nuevo fundamento semántico.

## Revisión adversarial final

1. **¿Qué candidato parecía más una Experience comercialmente y menos semánticamente?** Embajadores de Estilo: usa identidad y niveles, pero casi no ofrece estructura. Maratón es más operable como campaña, no más completa como Experience.
2. **¿Cuál siguió coherente sin points/rewards/gamification?** Circuito Sostenible con mayor claridad; también Aventura Familiar y, con más gaps, Desafío Activo.
3. **¿Qué campos exigieron más inferencia?** Pattern, Result participante, Progression no contable, Measurement del cambio y Learning.
4. **¿Algún Candidate Experience terminó siendo Scenario o campaign?** Antes–Durante–Después es lifecycle/orchestration; Maratón y Embajadores quedan como campañas/conceptos. Los candidatos aceptados contienen componentes de Scenario que se separaron.
5. **¿Se crearon definiciones principalmente para desbloquear H3?** No. Se validaron los cinco ejemplos primero y Circuito Sostenible se documentó aunque no participa en el overlap H3. Las definiciones conservan utilidad independiente.
6. **¿H3 tiene ahora base semántica independiente?** Sí: dos candidatos Hospitality preexistentes comparten naturalmente evidencia de actividad deportiva, con relaciones distintas.
7. **¿Serían útiles las definiciones si H3 se abandonara?** Sí: registran límites entre transformación, Scenario, mecánicas, canales y KPI para Demo Factory y futuro Builder.
8. **¿Qué fuente mejoraría la definición más débil?** Para Desafío Activo: evidencia de cambio participante, criterio de Pattern, diversidad/repetición requerida, medición de bienestar y aprendizaje. Para Embajadores, una especificación completa de participantes, secuencia y resultado antes de reconsiderarla.
9. **¿La superficie comercial distorsiona categorías TES?** Sí: llama progresión a contadores, resultado a beneficios/KPI, evento a cada validación y journey/Experience a conjuntos de fases y mecánicas. El informe no conserva esas equivalencias.
10. **¿Se preservó utilidad comercial frente a autoridad semántica?** Sí: objetivos, canales y mecánicas se conservan como evidencia de intención, mientras los gaps y prohibiciones impiden tratarlos como semántica gobernada.
