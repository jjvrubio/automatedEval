# Sports Season — SAFE-TO-BUILD review

Fecha: 2026-09-23. Estatuto: SITUATED / EXPERIMENTAL / LOCAL / NOT A GENERAL DEMO PROTOCOL / NOT PROMOTED. Inspección del working tree recibido; no sesión S40, experimento H40 ni delta de producto.

La construcción del primer slice es metodológicamente viable **con código situado pendiente**. La Factory actual no ejecuta la demo deportiva mediante configuración únicamente. No se ha encontrado una conducta requerida que obligue a falsificar una garantía semántica o arquitectónica: ADR-001 permite construcciones funcionales locales; ADR-002–005 permiten estado controlado, acciones públicas y proyecciones sin declarar Progression, Result ni reconocimiento de Evento TES.

Las cualificaciones esenciales son: representar explícitamente al participante externo; conservar inscripción y modalidad por evento; registrar presencia simulada y esfuerzo autodeclarado por separado; conceder una insignia individual mediante una regla local explícita; presentar una oportunidad de alta sin producir membresía. Estas piezas **se construirían**, no están demostradas por los tests de Aventura Familiar. La especificación concreta está en [smallest buildable slice](sports-season-smallest-buildable-slice.md).

## Input, autoridad y alcance de la evidencia

El input rector es la [copia exacta de la instrucción recibida](evidence/sports-season-safe-to-build/frozen-review-input.md). Su SHA-256 y los hashes de fuentes constan en [source-inspection.json](evidence/sports-season-safe-to-build/source-inspection.json). La definición anterior en la raíz mantiene la fuente de presencia abierta; la instrucción recibida la fija en **QR/check-in simulado** y prevalece. No se modifica ese documento anterior.

Distinguimos cuatro cosas: capacidad existente inspeccionada, comportamiento demostrado históricamente, inferencia de viabilidad y comportamiento nuevo todavía por construir/verificar. No se ha ejecutado un recorrido deportivo, inspección visual de navegador ni aceptación humana.

| Ref. | Evidencia / origen | Autoridad y límite |
| --- | --- | --- |
| F1 | [Architecture v0.5](../../../00-governance/program-architecture.md), [ADR-001](../../../00-governance/decisions/ADR-001-bounded-tes-semantic-authority.md), [ADR-002](../../../00-governance/decisions/ADR-002-logical-separation-composition-runtime-read-models.md) | Fronteras aceptadas. Las extensiones de producto son posibles si se clasifican, declaran límites y no redefinen TES. AppSnapshot no es un modelo canónico universal. |
| F2 | [ADR-003](../../../00-governance/decisions/ADR-003-desired-effective-demo-composition.md), [ADR-004](../../../00-governance/decisions/ADR-004-experience-scenario-demo-script-separation.md), [ADR-005](../../../00-governance/decisions/ADR-005-neutral-evidence-authority-bounded-contextual-evaluation.md) | Composición efectiva; acciones y estado bajo runtime; Script y Activity sin autoridad factual; evaluación acotada por premisas. Los shapes actuales no son normativos. |
| F3 | [Contratos Factory](../prototype/src/demo-factory/contracts.ts), [contratos anteriores de dominio](../prototype/src/domain/contracts.ts) | Hechos de implementación. AppSnapshot/DemoFixture exigen member; EvidenceInput carece de payload de esfuerzo/resultado; ContextReference sólo admite booking/stay/property. El ExperienceParticipation anterior exige memberId y no gobierna esta vertical. |
| F4 | [bootstrap](../prototype/src/demo-factory/bootstrap.ts), [manifests](../prototype/src/demo-factory/manifests.ts), [main](../prototype/src/main.tsx), [bootstrap tests](../prototype/src/demo-factory/bootstrap.test.ts) | Resolución, errores e aislamiento demostrados en composiciones existentes. Bootstrap instancia siempre MockDataAdapter; no existe selector general de providers. |
| F5 | [MockDataAdapter](../prototype/src/demo/mock-adapter.ts), [tests básicos](../prototype/src/demo/mock-adapter.test.ts) | Frontera pública, validación de acción/checkpoint, clonación y reset. Las guards de atribución/tipo son condicionales a requiresEnabledSubject. No constituyen validación general de cualquier payload. |
| F6 | [artifacts A](../prototype/src/demo-factory/artifacts.ts), [artifacts Costa](../prototype/src/demo-factory/costa-artifacts.ts), [fixtures](../prototype/src/demo-factory/fixtures.ts) | Configuración TypeScript situada; pasos y presentación. No editor sin programación ni definición deportiva. |
| F7 | [vertical-evaluation](../prototype/src/demo-factory/vertical-evaluation.ts), [evidence-relevance](../prototype/src/demo-factory/evidence-relevance.ts), [evidence-sufficiency](../prototype/src/demo-factory/evidence-sufficiency.ts) | Implementaciones experimentales diferentes. La vertical ejecutada usa booking/stay/property, marcadores y K de Treasure Hunt. No es evaluador deportivo ni motor de insignias. |
| F8 | [App](../prototype/src/app/App.tsx), [S37](session-37-activity-attribution-claim-provenance-and-reduction.md), [harness actual H37](../prototype/src/demo-factory/activity-attribution-reduction-h37.test.ts) | App consume runtime. H37 verifica producto acumulado y reduce claims de actor/cuenta. Las perspectivas existentes siguen siendo específicas de aventura. |
| F9 | [S39 consolidada](session-39-effective-composition-navigation-identity.md), [matriz final](evidence/session-39/pre-delta-navigation-matrix-final.json) | Identidad/provider/estado de A/B en superficies ejecutadas; Retail/Arrival con recarga reconstruida en jsdom. No prueba navegación deportiva ni navegador nativo. |
| F10 | [S38](session-38-historical-replay-portability-evidence-integrity.md), [guía S01–S38](guia-maestra-sesiones-01-38.md) | Separación de replay histórico y verificación acumulada; límites de entorno y mantenimiento. La guía sirve como índice, no sustituye evidencia. |
| F11 | [PSC-P01](../../../01-semantic-contract/product-semantic-contract-pressure-register.md), [ocurrencia/traza/Evento](../../../01-semantic-contract/product-interpretations/observed-occurrence-trace-event.md), [Desafío Activo](../../../01-semantic-contract/product-experience-definitions/active-challenge.md) | PSC-P01 abierto. Desafío Activo es candidata Hospitality no ejecutable; insignia, contador y beneficio no prueban Progression ni Result. No se puede renombrar como Experience deportiva validada. |
| F12 | [suite final S39](evidence/session-39/full-suite-final-results.json), [intento actual](evidence/sports-season-safe-to-build/suite-attempt.log), [verificación](evidence/sports-season-safe-to-build/verification.json) | 113 PASS pertenecen a S39. El intento actual falla antes de ejecutar tests por firma nativa de Rolldown; no hay nuevo PASS de suite. |

La inspección negativa se limita al sistema local recibido, sus contratos, productores y consumidores. No afirma imposibilidad general ni capacidad de APIs externas.

## Estado histórico preservado

| Elemento | Estado conservado |
| --- | --- |
| S39 | CLOSED / STOP PRE-DELTA |
| P39 | FALSIFIED / NOT REPRODUCED |
| H39 | SUPPORTED WITH QUALIFICATION |
| NO-NEW-NAVIGATION-RELATION | LOCALLY SUFFICIENT / NOT PROMOTED |
| H21 / H36 | HISTORICALLY FALSIFIED / PRESERVED |
| H37 | SUPPORTED WITH QUALIFICATION / CURRENT CUMULATIVE VERIFICATION |
| Regla S38 | LOCAL / EXPERIMENTAL / NOT PROMOTED |
| Costa B | EXPERIMENTAL COMPOSITION / NOT COMMERCIAL DEMO ACCEPTANCE |
| Architecture / ADR / TES / PSC | v0.5 y ADR-001–005 sin cambios; TES/PSC sin cambios; PSC-P01 OPEN; PSC-P02 no creado |
| S01–S38 restantes | Informes, baselines, tests, trazas y veredictos conservados; ninguna reclasificación retrospectiva |

## Matriz de capacidades contra la definición

Las seis categorías son las solicitadas. **MISSING BUT NON-BLOCKING** significa que la ausencia no exige violar una garantía; puede requerir trabajo obligatorio de construcción. No significa que se pueda omitir del recorrido una función requerida. Configuración significa datos declarativos; código significa implementación/contrato/proyección que hoy falta. Ningún test hotelero se presenta como demostración de la versión deportiva.

| Necesidad | Clasificación | Evidencia | Autoridad / origen | Capacidad actual | Gap exacto | ¿Requiere cambio? | ¿Bloquea y por qué? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Identidad de composición | AVAILABLE WITH QUALIFICATION | F4/F9 | Resolver; H39 local | Referencias y runtime resueltos; A/B conservan identidad | No composición deportiva ni navegación suya ensayada | Nuevos artefactos; integrar superficie | No: reutilizar identidad efectiva y verificar nuevo recorrido |
| Marca, logo y colores | REUSABLE WITH SITUATED CONFIGURATION | F4/F6 | BrandArtifact y validación bootstrap | Nombre, logoUrl y tokens | Marca deportiva ficticia | Datos y asset nuevo | No: slots existentes |
| Estado aislado y reset | AVAILABLE WITH QUALIFICATION | F5; F8 H37 | Runtime | Clonación, transición y reset locales | Estado deportivo adicional aún inexistente | Código situado y controles del nuevo estado | No: conserva la misma frontera; no requiere persistencia |
| Temporada distinta de evento | MISSING BUT NON-BLOCKING | F3/F6 | Input situado; F1 | Scenario puede situar contexto; no season/event deportivo tipado | seasonRef/eventRef y catálogo deportivo | Datos y representación local nueva | No: relación de producto; no necesita TES ni motor de temporadas |
| Carrera, Vela, Vóley visibles | REUSABLE WITH SITUATED CONFIGURATION | F6/F8 | Contenido situado e interfaz | Datos y tarjetas de contenido; no catálogo deportivo | Tres ofertas visibles y estado de disponibilidad | Datos y UI situada | No: sólo Carrera necesita acciones |
| Persona distinta de miembro/cliente | MISSING BUT NON-BLOCKING | F3/F5/F8 | SubjectReference; F1/F11 | Sujeto individual separado, pero fixture/snapshot exigen member | Estado miembro/externo, vínculo explícito a persona y proyección sin membresía ficticia | Código y datos obligatorios | No: extensión funcional explícita permitida; no usar member como prueba de alta |
| Inscripción visible | MISSING BUT NON-BLOCKING | F3/F5/F6 | ADR-004 | Enlist habilita sujeto y no produce Evidence | No conserva inscripción a evento con modalidad elegida | Acción y estado locales obligatorios | No: reutilizar frontera pública; enlist no se presenta como inscripción ya existente |
| Modalidad por participación | MISSING BUT NON-BLOCKING | F3/F8 | Definición situada | No selector ni campo de modalidad | Guardar elección en inscripción persona+evento | Datos, UI, payload y validación | No: no se incorpora a identidad permanente de persona |
| Evidence neutral con origen | AVAILABLE WITH QUALIFICATION | F3/F5/F7 | ADR-005 | id, type, source, occurredAt, reliability, subjects, contexts | No payload deportivo; provenance y reliability no acreditan verdad externa | Campos locales y proyección si necesarios | No: se conserva factualidad comunicada y alcance simulado |
| Presencia por QR simulado | MISSING BUT NON-BLOCKING | F3/F5 | Input fija fuente; runtime | Aceptación de Evidence tipada en acciones configuradas | Acción de check-in deportivo y referencia al evento | Datos y código situado | No: botón simulado explícito; no precisa integración QR |
| Esfuerzo suave/medio/intenso | MISSING BUT NON-BLOCKING | F3/F8 | Declaración simulada de participante | No input de valores ni payload de esfuerzo | Elección real y valor almacenado aparte de presencia | UI, payload y estado obligatorios | No: hecho autodeclarado, sin cálculo fisiológico ni inferencia de presencia |
| Resultado y posición competitivos | MISSING BUT NON-BLOCKING | F3/F11 | Definición situada | Sin representación operativa deportiva | Dos valores declarados y su origen | Sólo contrato conceptual/contraste ahora; ejecución posterior | No: fuera del recorrido primario; no confundir con esfuerzo |
| Atribución individual | AVAILABLE WITH QUALIFICATION | F3/F5/F8 | Evidence.subjects; guards; H37 | Atribución por ID conservada y rechazos en alcance probado | Liga persona→inscripción→evento→Evidence→badge | Binding local y controles nuevos | No: un sujeto ejecutado, sin composición cross-subject |
| Relación con Experience | AVAILABLE WITH QUALIFICATION | F2/F3/F4/F11 | ADR-004; referencias gobernadas | Scenario exige una experienceRef en TS; resolver la busca; retail no tiene Scenario | Scenario deportivo sin Experience validada no encaja literalmente en ese shape | Ajuste técnico local si se usa Scenario; no crear Experience falsa | No: ADR-004 permite referencia, no obliga a semántica TES en todo recorrido; booster se difiere |
| Evaluación deportiva | MISSING BUT NON-BLOCKING | F5/F7 | Runtime y política local futura | Sólo Family Adventure ejecuta su evaluación vertical | Criterio local para insignia, no K hotelero | Código acotado obligatorio | No: regla explícita de demo, sin claim de transformación TES |
| Insignia visible y explicada | MISSING BUT NON-BLOCKING | F3/F5/F8 | Regla local; read model | No estado/acción/proyección de concesión de badge; estilos visuales no lo prueban | Destinatario, motivo, evidencias y consecuencia | Código y contenido obligatorios | No: resultado de producto simulado, no TES Result |
| Trofeo distinto de badge | MISSING BUT NON-BLOCKING | F3/F8 | Narrativa competitiva | Sin motor de trofeos | Diferenciación conceptual en contraste | Copy; concesión diferida | No: no gobierna el recorrido primario |
| Beneficio distinto de reconocimiento | AVAILABLE WITH QUALIFICATION | F3/F5/F8 | CouponReadModel/fixtures | Beneficios mock visibles; no concesión contextual de beneficio | Política de acceso anticipado por recurrencia | Diferir concesión y recurrencia | No: captación es la consecuencia mínima; no convertir badge en cupón |
| Oportunidad de alta | MISSING BUT NON-BLOCKING | F3/F5/F8 | Input comercial; política situada | No conversión ni read model de captación | Invitación posterior al badge; estado externo intacto | Proyección/UI obligatorias | No: oportunidad ≠ consentimiento, lead enviado, alta o intención de compra |
| Primera participación inmediata | MISSING BUT NON-BLOCKING | F5/F11 | Política situada | Checkpoint local no es reconocimiento | Un badge tras presencia+esfuerzo; motivo explícito | Código situado | No: no necesita acumulación ni Progression |
| Segunda participación / booster | MISSING BUT NON-BLOCKING | F7/F11 | Input; límites TES | No acumulación deportiva demostrada ni Progression autorizada | Regla de continuidad y su relación con Experience | Diferida; no semilla ficticia de avance TES | No: primario de primera participación está autorizado; no afirmar booster ejecutado |
| Cambio participante→Marketing/CRM | AVAILABLE WITH QUALIFICATION | F8/F9 | Proyección de un mismo runtime | Aventura ofrece Guest/Supervision y conserva sesión | Vista CRM deportiva y campos faltantes | UI/proyección obligatorias | No: reutilizar separación y estado compartido, no renombrar Supervisión hotelera |
| Configurar copy/nombres/pasos | REUSABLE WITH SITUATED CONFIGURATION | F3/F6/F8 | Script H25/H27/H30/H32 locales | Labels, framing, relato por acción y Activity situada | UI nueva debe consumir sus datos; muchos textos App son literales | Datos y conexión de UI | No: no se requiere sistema editorial universal |
| Autoría sin programar | MISSING BUT NON-BLOCKING | F4/F6/F8 | Inspección de catálogos TS | Artefactos editables por desarrollador; no editor de demos | Formularios/importación/validación de autoría | Diferidos | No: objetivo futuro; no debe anunciarse como capacidad actual |
| Equipos y lógica entre deportes | MISSING BUT NON-BLOCKING | F7/F11 | Input v0.1 | Cross-subject hotelero experimental, no semántica deportiva colectiva | Organización visible; resultados/colectivos ausentes | Copy mínimo; lógica diferida | No: un sujeto, una carrera, reconocimiento individual |
| Identidad/estado al navegar | AVAILABLE WITH QUALIFICATION | F8/F9 | H39 local | A/B SPA conserva runtime; generic links no garantizan esto | Selección/navegación deportiva por construir | UI situada y comprobación | No: no exige nueva relación universal; no reutilizar entrada genérica a A |
| Integridad histórica | AVAILABLE / DEMONSTRATED | F10/F12; preservación de esta revisión | Archivos y SHA-256 | Los 640 archivos de baseline S39 coinciden | Harnesses fijan bytes y afectarán futuros deltas intencionales | Sólo nuevas evidencias aquí; trabajo futuro aislado | No: no se necesita reescribir pasado para construir |
| UX entendida / navegador / dispositivo | UNKNOWN — INSUFFICIENT EVIDENCE | F9/F12 | Límites de evidencia | DOM histórico no acredita aceptación humana; no demo deportiva existente | Uso real, comprensión y visual en navegador | Observación posterior a BUILD | No: requisito de aprendizaje posterior, no prueba previa posible |
| Ejecución actual de suite | AVAILABLE WITH QUALIFICATION | F12 | Evidencia histórica y entorno actual | S39: 113 PASS; ahora startup error de firma nativa | Toolchain compatible para nueva ejecución | Entorno de ejecución posterior; sin reparación aquí | No semántico: no impide representación responsable; sí impide anunciar nueva suite verde |

## Recorrido trazado, sin ejecutar ni rellenar huecos

Para distinguir readiness de implementación, «missing but can be deferred» tiene dos destinos explícitos: **BUILD obligatorio**, si la pieza debe existir antes de enseñar el slice, o **fuera del slice**, si se excluye. No se disfraza código faltante como configuración. La tabla no describe una demo deportiva que ya funcione.

| Transición | Estado solicitado | Recorrido real reutilizable / gap | Trabajo y autoridad |
| --- | --- | --- | --- |
| Selección→manifest→composición efectiva | already exists | main→selectDemoId→resolveDemo→referencias→MockDataAdapter→App | Manifest/marca deportivos nuevos; resolver mantiene autoridad, App no selecciona provider |
| Manifest→Scenario deportivo | missing but can be deferred — BUILD obligatorio | Referencia Scenario existe; el deportivo no; contextos y experienceRef actuales tienen límites concretos | Datos situados y ajuste local de contrato/resolución; no booking ficticio ni Experience inventada |
| Scenario→Demo Script, si se usa | requires situated configuration | Script declara pasos/expectativas; bootstrap valida vinculación y primer paso | Nuevo guion; no regla de badge dentro del Script; elección humana no sustituida por paso fijo |
| Scenario→representación de participante | missing but can be deferred — BUILD obligatorio | SubjectReference individual existe; no membresía externa explícita en snapshot | Persona/membresía y binding local; no account=actor |
| Participante→evento+modalidad→inscripción | missing but can be deferred — BUILD obligatorio | Enlist demuestra habilitación sin Evidence; no inscripción deportiva | Formulario y acción con valores elegidos, validados y guardados por runtime |
| Inscripción→QR simulado→presencia | can be represented with existing capability | Acción Evidence neutral con origen y sujeto; no acción deportiva actual | Acción y referencia de evento situadas; check-in no crea esfuerzo |
| Presencia→input de esfuerzo | missing but can be deferred — BUILD obligatorio | App sólo envía step.action fijo; no input de nivel | Selector y payload local separado, jamás extraído del copy |
| UI/Script→public action | already exists | App→provider.executeAction | Nueva acción de formulario usará esa frontera; no mutación de snapshot desde React |
| Public action→runtime→estado | already exists | Adapter valida identidad/checkpoint; conserva estado y resetea | Añadir validaciones deportivas de persona/evento/modalidad/valor antes de mutar |
| Runtime→evaluación aplicable | missing but can be deferred — BUILD obligatorio | evaluateVerticalEvidence sólo en family-adventure; no aplicar a deporte | Criterio local presencia+esfuerzo; no K, no reutilización de premise hotelero |
| Estado/evaluación local→read model | can be represented with existing capability | projectSnapshot demuestra separación; snapshot deportivo ausente | Proyección nueva de hechos aceptados y regla aplicada; no Activity como origen |
| Read model→badge/motivo/consecuencia | missing but can be deferred — BUILD obligatorio | No badge deportivo ni concesión existentes | Reconocimiento individual con evidencia citada; condición gobierna runtime |
| Badge→oportunidad de captación | missing but can be deferred — BUILD obligatorio | No automatismo de alta existente | Mostrar invitación si persona externa; membership permanece external |
| Participante→Marketing/CRM | can be represented with existing capability | Cambio de superficie sobre mismo runtime demostrado en A/B | Nueva proyección comercial con hechos/orígenes y oportunidad separados; sin reset |
| Primera→segunda participación→Experience/beneficio | missing but can be deferred — fuera del slice | No implementación deportiva ni autoridad para Progression | Se observa continuidad como posibilidad; no se simula la capacidad ausente |

Las relaciones funcionales realmente ausentes son persona–membresía; inscripción–evento–modalidad; Evidence deportiva–inscripción/evento; reconocimiento individual–criterio–Evidence; oportunidad–persona/estado de club. Se necesitan representaciones explícitas locales. La relación modalidad–Experience permanece abierta: no es necesaria para acreditar las tres acciones y su consecuencia de producto. No se necesita Group, relación universal de navegación, authority service ni un registro general de reglas.

## Garantías del primer slice

| Garantía | Evaluación y condición concreta para conservarla |
| --- | --- |
| Composition identity | Base F4/F9 reutilizable; resolver sports antes del render y conservar runtime al cambiar perspectiva. No interpretar marca/query por sí sola como prueba de identidad viva. |
| State integrity | Estado exclusivamente en runtime; rechazos sin mutación, snapshots aislados y reset completo. La evidencia actual no demuestra esto para campos aún por construir. |
| Participant ≠ customer/member automático | Persona fixture externa explícita; no usar nombre, id member ni puntos cero como prueba de relación con club. La invitación no altera el estado. Relación de cliente queda no establecida. |
| Modality ≠ clasificación permanente | Elección sólo en inscripción a ese evento; no en persona, perfil o segmento inferido. |
| Presence ≠ effort ≠ competitive result | Registros/tipos/campos separados; cada fuente acredita únicamente lo que declara. Registro de inscripción no acredita presencia. |
| Evidence provenance | Mostrar check-in simulado y esfuerzo autodeclarado; conservar IDs, origen, sujeto, evento y tiempo en datos, no reconstruirlos desde Activity. |
| Recognition ≠ commercial benefit | Badge local explícito y oportunidad de alta separada; no cupón/beneficio concedido en este slice. |
| Individual attribution | Todos los inputs y badge refieren al mismo sujeto e inscripción aceptados; cambiar label/cuenta no cambia atribución. |
| No unsupported collective semantics | Vóley informa sobre organización por equipos; ninguna acción colectiva, claim compartido ni Group ejecutados. |
| Historical evidence integrity | Nuevos documentos/evidencias únicamente. No regenerar baseline, trazas, expectations o verdicts para acomodar esta lectura. |
| Experimental ≠ promoted | Datos, regla y nueva UI locales; capabilities no declaran real ni general. No comercialmente aceptada, ni productiva, ni TES validada por llevar tesBaseline. |

No hay afirmación de que estas once garantías ya estén verificadas para deporte. Hay evidencia de fronteras reutilizables y una especificación verificable para las piezas nuevas, sin contradicción necesaria.

## Presiones S01–S39 frente a este recorrido

La revisión usa la guía histórica como índice, ADR aceptados como autoridad y cierres posteriores como evidencia de alcance. No aplica una instrucción antigua ni convierte una presión ya cualificada en un defecto actual por su sola aparición histórica.

| Presión heredada | ¿Invalida el slice? / tratamiento situado |
| --- | --- |
| S01–S08: paquete soberano, adaptador universal, separación de autoridades | NOT BLOCKING FOR THIS DEMO SLICE. ADR-001–004 ya fijan las fronteras necesarias; no construir provider universal ni motor de scripts. |
| S09–S14: relevancia, autoridad, desconocido frente a negativo, candidatas | NOT BLOCKING FOR THIS DEMO SLICE. La regla local reconoce requisitos comunicados; no infiere bienestar, compra, Evento TES ni validación de Desafío Activo. No mapping taxonómico externo. |
| S15–S18: K, composición cross-subject, ámbito de claim / PSC-P01 | NOT BLOCKING FOR THIS DEMO SLICE. Un participante y su propio evento; no trasladar un claim de un sujeto/ámbito a otro. PSC-P01 permanece abierto. |
| S19–S20: sujeto, alistamiento, activación y segunda persona | NOT BLOCKING FOR THIS DEMO SLICE. Modelo de persona simulada explícito; inscripción no equivale a alta de club. No usar habilitación de huésped como inscripción ya probada. |
| H21/H22: selección por Scenario/Experience y reuse | NOT BLOCKING FOR THIS DEMO SLICE. No reetiquetar family-adventure como deporte para activar el evaluador. Integración deportiva local queda por construir y probar. H21 sigue falsificada. |
| H23: contexts incompletos/contradictorios y premisa hotelera | NOT BLOCKING FOR THIS DEMO SLICE. Registrar evento real de la configuración situada; no disfrazarlo de booking/stay/property ni importar su premise. |
| H24/H25/H30/H32: procedencia del relato, ausencia y hosts de presentación | NOT BLOCKING FOR THIS DEMO SLICE. Copy configura la explicación; hechos y elegibilidad permanecen en runtime. La UI situada requiere trabajo, no arquitectura editorial general. |
| H26–H29/H33/H34/H36/H37: viewer/actor, cuenta y segunda persona | NOT BLOCKING FOR THIS DEMO SLICE. «Participante simulado: …» y hechos atribuidos por ID; no claim de identidad autenticada ni de cuenta ejecutora. Cambiar perspectiva no cambia actor/sujeto. |
| H35: título Experience frente a título situado | NOT BLOCKING FOR THIS DEMO SLICE. Temporada/evento tienen título de producto; no usar Experience.name para fingir validación deportiva. |
| Equipos / semántica colectiva | NOT BLOCKING FOR THIS DEMO SLICE. Vóley informativo y reconocimientos individuales; semántica colectiva diferida. |
| Navegación / H39 | NOT BLOCKING FOR THIS DEMO SLICE. Reusar identidad efectiva en nuevos enlaces. No cambiar H39 ni atribuir a B el fallo no reproducido. La Home genérica no sirve directamente como Home deportiva. |
| Browser/dispositivo/UX | NOT BLOCKING FOR THIS DEMO SLICE. Son comprobaciones de la construcción y uso futuros; todavía no hay aceptación. Fallos reales del recorrido construido sí deberán impedir presentarlo como listo. |
| Replay histórico y congelación de fuentes | NOT BLOCKING FOR THIS DEMO SLICE. Baseline preservada. H37/H39 comprueban bytes: futuros cambios de App/contracts/bootstrap provocarían diferencias intencionales. Mantener ejecución histórica aislada y registrar aparte pruebas de código nuevo; no quitar asserts ni actualizar hashes antiguos. |
| Toolchain/rutas/assets/concurrencia | NOT BLOCKING FOR THIS DEMO SLICE a nivel de representación. Hoy el Node disponible falla al cargar Rolldown; debe resolverse el entorno antes de afirmar validación ejecutable nueva. Ningún arreglo en esta revisión. |
| Terminología diagnóstica de Supervisión | NOT BLOCKING FOR THIS DEMO SLICE. Construir lectura Marketing/CRM desde hechos; no basta cambiar el título de la vista de K. Es trabajo de UI, no presión TES. |
| Duplicación literal de K | NOT BLOCKING FOR THIS DEMO SLICE. No se consume K ni su rótulo. La regla deportiva no copia ni generaliza ese evaluador. |
| Cardinalidad modalidad/Experience, booster, recurrencia | NOT BLOCKING FOR THIS DEMO SLICE. No se promete progreso TES; primera participación y captación bastan. Continuidad comercial permanece por observar. |

Ninguna presión seleccionada para experimento. No H40.

## Demo-author UX: alcance real

| Lo que quiere variar el autor | Situación observada | Fricción que se conserva para observar |
| --- | --- | --- |
| Marca, nombre, logo, colores | BrandArtifact configurable por catálogo TS | Edición técnica y alta en catálogo; no interfaz sin código |
| Copy, nombres visibles, intro y pasos | Campos de Script experimentales locales | No todos los textos App consumen esos campos; transporte a UI deportiva requiere código |
| Temporada, disciplinas, eventos, fechas | No shape deportivo existente | Nuevos datos situados y consumidores, no motor general |
| Participantes y membresía | Subjects/labels disponibles; member obligatorio | Falta relación externa explícita; no copiar fixture con miembro inventado |
| Modalidades y valores de esfuerzo | No input/estado existente | UI, payload y validación locales |
| Experience refs | Resolución singular disponible | Referenciar no valida; no declarar cardinalidad general ni inventar Experience deportiva |
| Criterios, badges, trofeos, beneficios | Cupones mock; no motor de concesión deportiva | Badge requiere código; trofeo, beneficio recurrente y editor de reglas se difieren |
| Imágenes | Logo configurable; no colección visual deportiva gobernada | Assets de contenido opcionales; no requisito para probar la tesis |
| Recorrido narrativo y perspectivas | Script/action/checkpoint y dos perspectivas hoteleras | Formularios y CRM deportivos nuevos; no demostración de autoría arbitraria |

**Código nuevo requerido:** representación deportiva local, inputs, validaciones, estado de insignia/oportunidad y proyecciones. **Código duplicado requerido por evidencia:** ninguno demostrado. Copiar App, MockDataAdapter o K completos sería una elección, no una necesidad acreditada; no se prescribe. Referencias y labels pueden repetirse entre Scenario/Script: fricción ya observable, sin corregirla aquí ni prometer eliminarla. Los nombres de módulos/datos futuros no son un protocolo promovido.

## Comprobaciones realizadas y límites

Se inspeccionaron fuentes locales y evidencia histórica. No se usaron fuentes web porque la pregunta versa sobre el working tree y su autoridad local.

- Comparación con baseline archivada S39: **640/640 archivos coinciden**, sin cambiar su inventario.
- Intento actual de Vitest con Node v24.14.0 de Codex: **error de arranque**, `ERR_DLOPEN_FAILED`; macOS rechaza el binding Rolldown por Team IDs distintos. Ningún test ejecutado. No se acepta la sugerencia automática del error de borrar dependencias/lockfile.
- Comprobación de tipos del proyecto App con caché en `/tmp`: **PASS**, documentado en [verification.json](evidence/sports-season-safe-to-build/verification.json). No equivale a build, suite ni UI deportiva.
- Lint, build, navegador nativo y aceptación humana no ejecutados en esta revisión. Ninguna afirmación nueva sobre UX, dispositivo o recarga documental.
- [Preservación antes/después](evidence/sports-season-safe-to-build/preservation-check.json): **675/675 archivos materiales recibidos intactos**; sólo documentos y evidencia nuevos. Se conserva el working tree previo, incluidos cambios ajenos. Se inventariaron aparte 12 archivos Finder `.DS_Store`; se observaron variaciones ambientales en cinco, sin editarlos desde esta intervención ni atribuir su autoría a un proceso concreto. Esta clasificación del inventario de revisión no altera ninguna baseline histórica.

## Aplicación de la condición de STOP

Una demo deportiva **sin cambios de producto** no es ejecutable hoy. Eso no satisface por sí solo las dos condiciones de MATERIAL BLOCKER. Las piezas faltantes pueden añadirse como construcciones de producto locales bajo ADR-001/002/004/005, con autoridad explícita y sin resolver TES o las presiones históricas generales.

Se descartan como atajos ilegítimos: inventar membresía para satisfacer AppSnapshot; convertir esfuerzo en presencia; usar booking/stay para un evento deportivo; renombrar Family Adventure/Desafío Activo para obtener una Experience validada; producir badges desde copy; reutilizar K como regla deportiva; llamar Progression/Completion al checkpoint. Ninguno es necesario en la especificación mínima.

La conclusión autoriza **definir el siguiente trabajo de construcción**, no lo implementa ni acredita su éxito. La aceptación posterior exige las comprobaciones observables especificadas; una contradicción material realmente descubierta en ese trabajo tendrá que registrarse, no ocultarse bajo esta conclusión.

## Veredicto

```text
A.
FIRST DEMO SLICE
→ SAFE TO BUILD WITH QUALIFICATIONS
```
