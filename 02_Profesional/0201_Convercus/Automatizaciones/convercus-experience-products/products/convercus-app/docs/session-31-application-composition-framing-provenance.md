---
title: "Sesión 31 — Application Composition Framing Provenance"
language: es
version: "v1.0"
status: "CLOSED / H31 FALSIFIED / NO-NEW-RELATION INSUFFICIENT / STOP BEFORE APP DELTA"
date: "2026-09-18"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de inspección de procedencia y falsación"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 31 — Application Composition Framing Provenance

## H30 CONSOLIDATED INPUT

[S30](session-30-script-bound-situated-journey-narrative.md) permanece CLOSED, H30 SUPPORTED WITH QUALIFICATION dentro de Family Adventure A/B. Se recibe la baseline acumulada del working tree; no se reconstruye desde Git ni se reabren decisiones anteriores.

- existing availableActionId: selector H30 EXECUTION-VERIFIED dentro de A/B; NOT UNIVERSALIZED.
- checkpoint: REJECTED AS H30 SELECTOR; su semántica permanece intacta.
- L3c journey narrative: EXPERIMENTALLY ADDRESSED / EXECUTION-VERIFIED dentro de A/B; separación narrativa/hechos respaldada dentro del alcance probado.
- VIEWER RELATION: NOT INTRODUCED.
- L3c overall: EXPERIMENTALLY ADDRESSED dentro de A/B / NOT PROMOTED.
- L4: PRESERVED / SOURCE-INSPECTION / OPEN.
- L5: PRESERVED / EXPERIMENTALLY ADDRESSED H25.
- RECURRING PRESENTATION PRESSURE: OBSERVED / NOT PROMOTED.

Architecture v0.5 ACTIVE; ADR-001–005 ACCEPTED; TES y Product Semantic Contract sin cambios. PSC-P01 continúa OPEN / EVIDENCE-BACKED PRESSURE con su cualificación existente. PSC-P02 NOT CREATED. Artefactos H25–H30 en cuarentena; DemoScript no se promueve.

## H31 HYPOTHESIS

Dentro de Family Adventure, las relaciones y artefactos existentes pueden proporcionar a App título y framing introductorio situados para A/B sin hardcodes A en App, nuevas relaciones, parsing/agregación de copy ni derivación desde GuestPerspective.message. Runtime, Evidence, evaluación, K y claim deben conservarse; App debe seguir siendo consumidor.

Condición ensayada: **EXISTING RELATIONS ONLY / NO-NEW-RELATION**. El resultado no evalúa una futura relación autorizada.

## VARIABLE UNDER TEST

Exclusivamente los dos textos de [HomePage](../prototype/src/app/App.tsx):

- línea 113: `Mi aventura · Aurora Stay`.
- línea 115: `Busca las pistas del jardín y de la fuente durante tu estancia.`

Precisión de superficie: el primero está en un **p.eyebrow**, no en el h1. El h1 de la línea 114 renderiza `adventure.huntName`. Se inventaría este campo, pero no se lo confunde con el literal seleccionado ni se modifica su procedencia.

No se seleccionan sessionLabel, subjects[].label/status, message, Activity, SupervisionPerspective, Evidence, evaluación ni otros literales de App.

## WHY L4 IS DIAGNOSTICALLY SPLIT

La cabecera ofrece una presentación estática de la composición; Supervisión representa sujetos, sesión y resultados operacionales. Sus fuentes y responsabilidades son distintas. Su coexistencia en App.tsx no autoriza resolver ambas con la misma relación ni reutilizar H27 para Supervisión.

La separación solo organiza esta inspección. No se crean L4a/L4b ni taxonomía contractual.

## CURRENT APP LITERAL INVENTORY

Inspección completa de las 570 líneas de App.tsx, sus componentes auxiliares de render y el punto de entrada actual. Se recorrieron también todos los literales, templates y expresiones JSX mediante el parser TypeScript instalado: [inventario sintáctico](evidence/session-31/app-syntax-inventory.json), **670 nodos en cuatro archivos**, con archivo, componente, línea, columna, expresión exacta y hash de fuente.

La captura sintáctica incluye deliberadamente tokens técnicos; la clasificación semántica siguiente agrupa por superficie sin omitir copy visible, accesible, condicional, vacío, de error o de diagnóstico. No es una nueva entidad de presentación. Las líneas se refieren al working tree capturado.

Categorías: **UI** = generic application UI; **CP** = composition-specific presentation; **GP** = GuestPerspective rendering; **SP** = Supervision rendering; **AR** = Activity rendering; **DG** = debug/diagnostic presentation. “A” indica dependencia específica de la composición A, no que el texto esté presente en A.

### App.tsx — componentes compartidos y HomePage

| Línea / componente | Literal o expresión | Superficie / clase | ¿A? | Fuente actual y candidatos existentes |
| --- | --- | --- | --- | --- |
| 12–14 / formatPoints | Intl.NumberFormat("es-ES").format(points) | Formato de cifras / UI | No | Número del read model; locale literal. manifest.locale existe, sin cambiarlo. |
| 16–35 / SectionHeading | eyebrow, title, “Ver todo” | Encabezados y enlace / UI | Según props | Copy del caller; enlace genérico de App. |
| 40–57 / CouponCard | coupon.tag, title, description, validUntil | Tarjetas de beneficios / CP | Según fixture | Fixture → snapshot.coupons; no framing de aventura. |
| 61–68 / ActivityList | “Aún no hay actividad”; “Tus movimientos y novedades aparecerán aquí.” | Estado vacío / AR + UI | No | Copy local de ausencia; Activity no aporta estos strings. |
| 74–89 / ActivityList | item.title, description, displayDate; occurredAt como dateTime | Filas de historial / AR | Según fuente | snapshot.activity; registros fixture / H25 y formato del adapter. |
| 82–85 / ActivityList | signo “+”, item.points, “pts” | Puntos de una fila / AR + UI | No | Número del item + convención local. |
| 113 / HomePage | “Mi aventura · Aurora Stay” | Cabecera p.eyebrow / UI + CP | **Sí, sufijo** | Etiqueta local + candidato de marca explícita runtime.brand.name. Seleccionado H31. |
| 114 / HomePage | adventure.huntName | h1 #adventure-title / GP | No específico de A | Read model actual; projector fija “Aventura Familiar”. Experience.name coincide, pero no alimenta este campo. Fuera del delta. |
| 115 / HomePage | “Busca las pistas del jardín y de la fuente durante tu estancia.” | Introducción estática / CP | **Sí** | Literal local; candidatos inspeccionados sin relación autorizante. Seleccionado H31. |
| 118 / HomePage | guestActionLabel ? “Tu siguiente paso” : “Resultado de la aventura” | Encabezado de acción / UI + GP | No | Presencia del label decide copy local; no equivale por sí sola a suficiencia. Preservado. |
| 119 / HomePage | adventure.message | Mensaje role=status / GP | Situado A/B por H30 | Read model; autoridad mixta H30; no fuente de resumen estático. |
| 120 / HomePage | guestActionLabel | Botón de acción / CP | Según Script | steps.find(actionId === availableActionId).presenterLabel; autoridad de affordance. |
| 121 / HomePage | discoveredClueCount + “pista descubierta” / “pistas descubiertas” | Contador / GP + UI | No | Read model + plural local. |
| 124 / HomePage | “Quién puede explorar” | Encabezado de sujetos / UI + GP | No | Etiqueta de App; sujetos/estados llegan proyectados. |
| 128 / HomePage | subject.label | Tarjeta de sujeto / GP | Según H27 | Relación explícita subjectRef→label → read model. |
| 129 / HomePage | subject.status + “ · ” + clueCount + “pista aportada” / “pistas aportadas” | Estado y conteo / GP + UI | No en plantilla | H29 + conteo proyectado; App compone separador y plural. |
| 133 / HomePage | adventure.sessionLabel | Cuenta/sesión presentada / GP | Según H28 | member.name → projector → sessionLabel; no identidad viewer. |
| 143–146 / HomePage genérico | “Buenos días”; “Hola, ” + member.name; “Ver notificaciones y actividad” | Saludo y nombre accesible / UI + CP | Según fixture para nombre | MemberReadModel para nombre; saludo y aria-label locales. |
| 152–159 / HomePage genérico | “Resumen de fidelización”; “Tu saldo”; formatPoints(member.points) + “pts”; member.level | Saldo/nivel / UI + CP | No específico | Fixture.member → snapshot; envoltura UI. |
| 163–166 / HomePage genérico | progress + “% hacia ” + nextLevel; pointsToNextLevel + “pts restantes”; “Progreso hacia ” + nextLevel | Progreso y accesibilidad / UI + CP | No específico | MemberReadModel; no TES Progression inferida aquí. |
| 170–182 / HomePage genérico | “Ver mi cuenta”; “Accesos rápidos”; “Mis cupones”; “Actividad”; “Mi perfil”; “Búsqueda del tesoro” | Accesos y enlaces / UI | Último destino **sí** | Destino fijo /?demo=hospitality-family-adventure; catálogo de manifests existe. Se registra, no se corrige. |
| 186–187 / HomePage genérico | “Para ti”; “Beneficios destacados” | Sección de beneficios / UI | No | App; coupons proporciona tarjetas, no este encabezado. |
| 200–203 / HomePage genérico | news[0]?.category/title/summary; “Descubrir más” | Tarjeta editorial / CP + UI | Según fixture | NewsReadModel del fixture; no relación de framing de aventura. |
| 207–209 / HomePage genérico | “Actividad reciente”; ActivityList(activity.slice(0,2)) | Resumen de historial / AR + UI | Según items | App limita filas y rotula; no agrega títulos para describir itinerarios. |

### App.tsx — otras páginas

| Línea / componente | Literal o expresión | Superficie / clase | ¿A? | Fuente actual y candidatos existentes |
| --- | --- | --- | --- | --- |
| 219–226 / BenefitsPage | “Tu selección”; “Beneficios”; “Ventajas disponibles para disfrutar ahora y propuestas seleccionadas para ti.”; “Filtros de beneficios”; “Todos”; “Disponibles”; “Próximamente” | Cabecera/filtros / UI | No | Copy local; no framing Family Adventure. |
| 229–236 / BenefitsPage | coupons.length + “beneficios disponibles”; “Listado de beneficios”; “No hay beneficios disponibles”; “Vuelve pronto para descubrir nuevas ventajas.” | Lista/ausencia / UI | No | Conteo snapshot + copy local. |
| 247–253 / ActivityPage | “Todo al día”; “Actividad”; “Consulta tus puntos, beneficios y últimas interacciones.”; “Últimos movimientos” | Cabecera de historial / AR + UI | No | Copy local genérico, incluso en aventura; se conserva como evidencia. |
| 263–267 / ProfilePage | member.initials/fullName; “Mi perfil”; “Miembro desde ” + memberSince | Identificación de cuenta / CP + UI | Según fixture | MemberReadModel; no fuente de property ni sujeto. |
| 273–277 / ProfilePage | “Nivel actual”; member.level; points + “puntos”; “disponibles para tus próximas ventajas.” | Membresía / CP + UI | No específico | MemberReadModel + plantilla local. |
| 281–284 / ProfilePage | “Tu cuenta”; “Datos personales”; “Nombre, idioma y preferencias”; “Comunicaciones”; “Noticias y notificaciones” | Opciones / UI | No | Etiquetas locales. |
| 285–286 / ProfilePage | “Vista iPhone”; “Modo de presentación comercial”; “Estado de la demo”; “Información técnica y capacidades” | Acceso a showcase/diagnóstico / DG + UI | No | Rutas y etiquetas locales. |
| 298–303 / IPhoneShowcase | “Modo de presentación”; runtime.brand.name + “ en iPhone”; “Salir” | Presentación comercial / CP + DG | Según brandRef | Marca resuelta usada como marca; ejemplo existente de transporte a App. |
| 309–320 / IPhoneShowcase | “Simulación visual de ” + brand.name + “ en un iPhone”; brand.name + “ — vista iPhone”; iframe src con manifest.demoId | Accesibilidad/iframe / CP + DG | Según composición | Marca y demo explícitas, sin parsing de identificadores. |
| 326–327 / IPhoneShowcase | “Simulación visual a 393 × 852 px. La validación en un iPhone real se realizará en A5.” | Nota de simulación / DG | No | Copy histórico, no resultado de validación S31. |

### App.tsx — Supervisión y diagnóstico

| Línea / componente | Literal o expresión | Superficie / clase | ¿A? | Fuente actual y candidatos existentes |
| --- | --- | --- | --- | --- |
| 349–351 / SystemPage aventura | “Supervisión”; “Estado de la aventura”; “Observa lo que cambia al actuar en «Mi aventura». Cambiar de vista conserva la sesión.” | Cabecera / SP + UI | No | Copy local. |
| 353–356 / SystemPage aventura | “Sujetos existentes”; subject.id === "subject-p1" ? “P1 · Lucía” : “P2 · Huésped 2” | Etiquetas de sujetos / SP | **Sí** | Branch local A; SupervisionPerspective no declara labels. H27 no autoriza sustituirlo. Congelado. |
| 357 / SystemPage aventura | subject.id + “ · exists: ” + String(exists) + operationalState + “ · Evidence: ” + evidenceCount | Datos por sujeto / SP + DG | No en plantilla | SupervisionPerspective y copy técnico local. |
| 361–364 / SystemPage aventura | “Evaluación compartida”; “Cuenta/sesión operativa” + sessionSubjectRef; “Criterio K” + “A AND (B OR C)” | Sesión/criterio / SP + DG | No literal A, sí encuadre local | Referencia operacional proyectada; rótulo ambiguo y representación de K locales. No son autoridad de cuenta ni de evaluación. |
| 365–368 / SystemPage aventura | “Evidence recibida” + evidence.length; “Admisibilidad conjunta” + jointAdmissibility; “Suficiencia K” + sufficiency; “Afirmación derivada” + derivedClaim | Resultados / SP + DG | No | Read model; App no evalúa. |
| 372–374 / SystemPage aventura | “Evidence y atribución”; “Todavía no hay Evidence. Alistarse o activar a un huésped no aporta pistas.”; item.id + subjectRefs.join(", ") + provenance, separados por “ · ” | Evidence/ausencia / SP + DG | No | Proyección de Evidence; copy explicativo local. |
| 391–398 / SystemPage genérico | “Panel interno”; “Estado de la demo”; “Información para preparar y verificar la demostración.”; “Estado del sistema”; “Demo” + manifest.demoId; “Marca” + brand.name | Diagnóstico / DG | Según composición | Runtime efectivo. Mostrar marca explícita no declara nombre de property. |
| 399–400 / SystemPage genérico | “Datos” + capabilityStatuses.join(" + "); “Red” + “disponible” / “sin conexión” | Capabilities/red / DG | No | runtime.capabilities y navigator.onLine. |
| 401–402 / SystemPage genérico | “Baseline” + experience?.tesBaseline / “No aplica a esta demo”; “Futura” + “bloqueada hasta verificar licencia” | Baseline/tipografía / DG | No | Experience resuelta o fallback técnico; estado Futura literal, sin reevaluación S31. |
| 407–419 / SystemPage genérico | “Control de presentación”; “Escenario actual”; “Checkpoint”; “Resultado esperado”; scenario.checkpoint; scriptStep.expectedCheckpoint; scriptStep.presenterLabel | Control de presentador / DG + CP | Según Scenario/Script | Acción disponible o primer step para diagnóstico; no fuente de framing. |
| 421–424 / SystemPage genérico | actionError; “Volver al perfil” | Alerta/enlace / DG + UI | Según error | Error emitido por App/provider; etiqueta local. |

### App.tsx — shell, navegación y estados globales

| Línea / componente | Literal o expresión | Superficie / clase | ¿A? | Fuente actual y candidatos existentes |
| --- | --- | --- | --- | --- |
| 429–433 / navigation | “Inicio”; “Beneficios”; “Actividad”; “Perfil” | Navegación genérica / UI | No | Constante de App. |
| 449 / AppShell | Script step por availableActionId → presenterLabel | Transporte a HomePage / CP | Según Script | Relación de affordance existente; no resumen. |
| 454–460 / AppShell | “Saltar al contenido”; “Ir al inicio”; img alt=runtime.brand.name; src=logoUrl | Shell/accesibilidad/branding / UI + CP | Según brandRef | Marca resuelta explícitamente; App ya recibe brand. |
| 463–464 / AppShell | “Cuenta de ” + snapshot.member.name; member.initials; “Abrir perfil” | Cuenta/avatar / UI + CP | Según fixture | MemberReadModel. No se reconstruye sessionLabel ni se infiere sujeto. |
| 470–475 / AppShell | “Navegación de la aventura”; “Mi aventura”; “Actividad”; “Supervisión”; actionError | Navegación/alerta / UI + DG | No | Etiquetas locales; demoId solo transporta selección en URL. |
| 494 / AppShell | “Esta página no existe”; “Vuelve al inicio para seguir explorando.”; “Ir al inicio” | Ruta desconocida / UI | No | FeedbackState con copy del caller. |
| 499–502 / AppShell | “Demo · hallazgos simulados”; “Reiniciar aventura”; “Navegación principal” | Herramientas/nav / DG + UI | No | Copy local; reset invoca provider. |
| 529 / App | “No hemos podido cargar la App”; “Comprueba la conexión e inténtalo de nuevo.”; “Reintentar” | Error de carga / UI + DG | No | Catch de getSnapshot; FeedbackState. |
| 533 / App | “Preparando tu espacio”; “Estamos cargando tus beneficios.” | Carga / UI | No | Copy genérico compartido; no se corrige incidentalmente. |
| 547–549, 566 / App | actionFailure.message; “No se pudo ejecutar la acción de presentación.”; “No se pudo reiniciar la aventura.” | Errores de acción/reset / DG | Según error | Error del provider o fallback local; no fuente de framing. |

### Perímetro de render complementario

| Archivo / componente | Literal o expresión | Superficie / clase | ¿A? | Fuente actual y candidatos existentes |
| --- | --- | --- | --- | --- |
| main.tsx:25 | runtime.brand.name + “ — Demo” | Título del documento / CP + DG | Según brandRef | Bootstrap → marca resuelta; título del documento ≠ título de la aventura. |
| main.tsx:19,35–39 | “No se encontró el contenedor raíz de Demo Factory.”; error.message / “Error de configuración desconocido.”; “No se pudo iniciar la demo” | Error de arranque / DG | No | Error técnico y fallback local. |
| ui/FeedbackState.tsx | title, description, action.label | Encabezado/texto/acción / UI + DG | Según caller | Solo representa props; no añade framing propio. |
| ui/Icon.tsx | paths[name]; svg aria-hidden=true | Iconografía decorativa | No | No añade copy visible o nombre accesible propio. |

Los paths, imports, className, icon names, IDs DOM, roles, claves de routing, separadores vacíos, dimensiones y atributos ARIA de estado son tokens técnicos, no fuentes de contenido. Están capturados en el inventario sintáctico; los atributos ARIA con texto y todos los textos de accesibilidad se clasifican arriba. El link fijo a A se conserva expresamente como presión adyacente.

Este inventario se completa antes de cualquier posible delta de aplicación. **No hubo delta de aplicación.**

## FRAMING DECOMPOSITION

| Componente | Significado acotado | Procedencia posible | Límite |
| --- | --- | --- | --- |
| “Mi aventura” | Nombre genérico de una vista/canal de App | UI local; misma etiqueta en navegación | El posesivo no establece viewer, ownership ni relación account→subject. La candidata documental identifica “Mi Aventura” como UI/canal. |
| “ · ” | Separador de presentación | UI local | Sin significado de dominio. |
| “Aurora Stay” | Nombre de la marca configurada, bajo una lectura de branding | manifest.brandRef → BrandArtifact.name | No equivale a property ni al nombre de una composición. |
| h1 huntName | Nombre presentado por GuestPerspective | Projector actual → read model → App | Es “Aventura Familiar” literal del projector; no hay threading desde Experience.name. No seleccionado. |
| “Busca las pistas…” | Invitación genérica de exploración | Copy local | Por sí sola no determina lugares ni itinerario. |
| “jardín” / “fuente”, unidos por “y” | Selección de lugares y afirmación de que ambos integran esta aventura | Falta declaración de framing de composición | Conocer dos lugares en otras presentaciones no autoriza esta afirmación estática. |
| “…durante tu estancia” | Encuadre temporal situado con voz de segunda persona | Copy local; Scenario posee referencias stay | Una referencia stay no declara vigencia, destinatario ni texto de presentación. No se crea viewer para resolverlo. |

La descomposición es analítica. No se transforma en campos ni contratos; tampoco se propone un nuevo literal B.

## EXISTING SOURCE INVENTORY

Las referencias de código son las actuales, no las copias test-fixtures históricas.

| Fuente inspeccionada | Datos y relación efectivamente existentes | Competencia para H31 |
| --- | --- | --- |
| [manifests.ts](../prototype/src/demo-factory/manifests.ts):36–68 y [contracts.ts](../prototype/src/demo-factory/contracts.ts):172–183 | A/B seleccionan brandRef, fixtureRef, scenarioRef y scriptRef. demoId/prospectId/locale y capabilities son identidad/configuración; no hay título ni intro de composición. | La relación de **marca seleccionada** existe. IDs no son display names ni criterios de copy. |
| [bootstrap.ts](../prototype/src/demo-factory/bootstrap.ts):95–180 | Resuelve y valida marca, fixture, Scenario, Experience y Script; entrega runtime antes de render. Script se comprueba contra Scenario. | Transporta artefactos existentes, no crea ni valida un resumen estático. |
| [artifacts.ts](../prototype/src/demo-factory/artifacts.ts):19–54 | Brand A.name = “Aurora Stay”; Experience compartida.name = “Aventura Familiar”. | Marca y nombre de Experience son datos con funciones declaradas diferentes. Experience runtime solo tiene id/name/tesBaseline. |
| [costa-artifacts.ts](../prototype/src/demo-factory/costa-artifacts.ts):5–39 | Brand B.name = **“Costa Clara Resort”**; property context ID = costa-clara-resort. | Nombre de marca explícito, no nombre de property derivado del ID. No es un título B observado. |
| Scenario A artifacts.ts:79–134; Scenario B costa-artifacts.ts:29–84 | Sujetos, property/booking/stay, checkpoints, estados y acciones; misma experienceRef. A.property ID = aurora-resort. | Contexto operacional; ContextReference solo declara type/id. No PropertyArtifact con display name, ruta turística o resumen. |
| Script A artifacts.ts:175–260; Script B costa-artifacts.ts:86–171 | subjectPresentations H27; experimentalJourneyPresentations H30; steps con presenterLabel, activityPresentation H25, expectedCheckpoint y acción. | Relaciones de sujeto, posición, affordance y ocurrencia. Ninguna declara framing estático a nivel de composición. |
| [fixtures.ts](../prototype/src/demo-factory/fixtures.ts):83–183 | Member, coupons, news y activityRecords. A reutiliza hospitality-stay; B posee fixture propio. | Cuenta/contenido/historial; el contenedor no convierte todo su copy en descripción de Experience. |
| News B fixtures.ts:169–174 | id costa-adventure-introduction; title “Inés y Mateo en Costa Clara”; summary “El mirador y el patio son los lugares de esta aventura. Mateo ya figura en la estancia.” | Aunque el texto parece pertinente, la relación declarada es NewsReadModel. Ni el ID ni el contenido establecen un rol de intro de App. |
| News A fixtures.ts:117–124 | “Lisboa empieza en Aurora”; resumen de reserva/llegada. | Confirma que news[0] no es un contrato común de framing Family Adventure. No se reutiliza ni se parsea. |
| [mock-adapter.ts](../prototype/src/demo/mock-adapter.ts):42–126 | Copia member/coupons/news, proyecta Activity y añade GP/SP por Experience; transporta H27/H30 y cuenta. | No hay framing de composición en snapshot ni cálculo autoritativo de itinerario. |
| [vertical-evaluation.ts](../prototype/src/demo-factory/vertical-evaluation.ts):130–197 | huntName fijo; sessionLabel H28; labels H27; status H29; message H30; SP separado. | Estas autoridades no se trasladan a App ni se reutilizan como resumen. |
| Evaluación vertical:30–127; contratos de Evidence | Contextos, markerRef derivado del tipo, criterio K, admisibilidad y claim. | Autoridad factual/evaluativa; no autoridad editorial. No se extraen nombres de lugares de Evidence. |
| [Family Adventure candidata](../../../01-semantic-contract/product-experience-definitions/family-adventure.md) | READY WITH EXPLICIT GAPS / non-executable; sitúa copy de bienvenida en Scenario/composición y “Mi Aventura” como UI/canal. | Delimita responsabilidades; **no declara** un binding ejecutable A/B ni un texto de framing autorizado para estas composiciones. |
| [ADR-003](../../../00-governance/decisions/ADR-003-desired-effective-demo-composition.md) y [ADR-004](../../../00-governance/decisions/ADR-004-experience-scenario-demo-script-separation.md) | Composición deseada/efectiva y separación Experience/Scenario/Script/runtime. | Autorizan sus responsabilidades; no añaden por implicación una relación editorial ausente. |
| config/brand.ts; 03-shared-assets/brands; SVG Aurora/Costa | Configuración/tokens/logos y branding. | Identidad visual; no descripción de aventura ni relación brand→property. |
| config/app-config.ts; domain/contracts.ts; canonical-demo-package.ts; config/app.yaml | Nombre genérico de App y DemoPackage anterior; ExperienceDefinition legacy tiene purpose/transformationHypothesis, pero canonical.experiences = []. | No son la ExperienceDefinition importada por Demo Factory ni una composición A/B resuelta. No se activa un modelo legacy para llenar el gap. |
| 02-shared-contracts/experience-domain/README.md; 03-shared-assets/scenarios/README.md | Contrato/catálogo en preparación; no framing A/B ejecutable. | Ninguna declaración adicional que cierre la relación ausente. |

## TITLE SOURCE ANALYSIS

**Componente genérico:** “Mi aventura” es etiqueta de UI ya existente. Su conservación no requiere Scenario ni una nueva relación de identidad. No se le atribuye semántica de ownership.

**Componente de marca:** hay más que un string coincidente: existe una relación explícita `manifest.brandRef` resuelta como `runtime.brand`. BrandArtifact.name declara nombre de **marca**. App ya lo representa como marca en el logo, showcase y panel interno; main.tsx lo usa para el título del documento.

La fuente es legítima **si el sufijo se mantiene estrictamente como identificación de la marca seleccionada**. Esa lectura acotada permite reconocer una fuente existente para el componente nominal del eyebrow, sin afirmar brand == property ni brand == composition title. No se acredita una relación independiente de “título de propiedad/composición”; no se necesita inventarla para nombrar únicamente la marca.

```text
A manifest.brandRef → brands["brand:aurora-stay@1"].name
B manifest.brandRef → costaBrand.name
    → resolveDemo().brand
    → App.runtime → AppShell.runtime
    → consumidores de branding ya existentes
```

HomePage recibe snapshot/guestAction/guestActionLabel, **no runtime.brand**. Para este componente acotado habría un gap local de transporte hacia HomePage, no ausencia de nombre de marca. **No se ensaya ese transporte ni se corrige el título**, porque la intro no supera la condición conjunta.

Valores de fuente: A “Aurora Stay”, B “Costa Clara Resort”. Son valores declarados de marca, no framing B ejecutado ni prescripción de un título nuevo. Si se exigiera que el sufijo designase una propiedad o un título editorial de composición, la relación también faltaría y se aplicaría STOP a esa lectura.

## INTRODUCTORY FRAMING SOURCE ANALYSIS

**No existe una relación declarada de Experience-level situated framing para estas composiciones.**

La Experience runtime compartida no tiene descripción; Scenario declara contextos/acciones, no un itinerario presentado; Script solo relaciona copy con sujetos, affordances, posiciones y ocurrencias. Fixture contiene news, pero no identifica una noticia como framing de la composición.

No se puede justificar el literal A mediante las tres frases H30 ni el B mediante mirador/patio en H25/H30/news:

- Tres mensajes de posición no declaran una descripción estática de todo el recorrido.
- Dos representaciones de hallazgo no definen qué lugares debe anunciar una aventura antes de actuar.
- La lista de acciones no declara una política para enumerar o resumir lugares.
- El ID de una noticia con “introduction” no cambia la semántica NewsReadModel.
- La coexistencia de stay y copy en segunda persona no declara destinatario ni resumen situado.

La relación que falta es la que **vincula explícitamente la composición seleccionada con su presentación introductoria estática autorizada**. Esto nombra la carencia; no diseña un campo, host, contrato ni mecanismo nuevo.

## DATA / RELATION DISTINCTION

| Dato disponible | Relación existente | Relación que no se puede inferir |
| --- | --- | --- |
| Aurora Stay / Costa Clara Resort | Nombre de la marca referenciada por manifest | Nombre de propiedad o título editorial de composición |
| Jardín/fuente; mirador/patio en H30 | availableActionId → mensaje situado | Composición → resumen estático de aventura |
| Lugares en H25 | Step de Evidence aceptada → representación de Activity | Itinerario declarado de la Experience |
| News B con descripción de lugares | Fixture → feed de noticias | Noticia designada como framing de la aventura |
| Contextos property/booking/stay | Referencias contextuales del Scenario | Display names, vigencia de estancia o destinatario de “tu” |
| Experience.name y GP.huntName coincidentes | Nombre de Experience por un lado; literal proyectado por otro | Threading entre ambos o descripción situada |

## TRANSPORT / RELATION DISTINCTION

**Marca:** la relación de selección existe y el dato ya alcanza App/AppShell. Falta pasarlo a HomePage para esa superficie. Sería transporte local de una marca, no modelado de una propiedad.

**Introducción:** no hay fuente con el rol requerido que transportar. Añadir dos strings al snapshot o extender props no resolvería primero quién autoriza su contenido. Agregar una declaración al Script sería una **relación nueva**, no “solo transporte”.

Por ello no se crea ningún transporte experimental H31. App no importa artifacts.ts ni costa-artifacts.ts.

## NO-NEW-RELATION ANALYSIS

La condición es conjunta: título **y** introducción deben tener fuentes legítimas antes de modificar App. La disponibilidad acotada de branding no compensa la ausencia de introducción.

```text
marca explícita disponible para el componente de branding
+
relación de introducción situada ausente
→ NO-NEW-RELATION INSUFFICIENT
→ H31 FALSIFIED
→ STOP BEFORE APP DELTA
```

No es un problema resuelto mediante copy genérico, eliminación de lugares, fallback A, agregación H25/H30 ni branching A/B. Esos caminos alterarían o eludirían la variable sin demostrar la hipótesis.

## APP CONSUMER BOUNDARY

La frontera preexistente se conserva:

```text
manifest + catálogos → resolveDemo
    → runtime.brand/experience/scenario/script/provider
    → App
provider.getSnapshot / executeAction / reset
    → snapshot → representación de App
```

App actualmente posee los dos hardcodes inventariados: es la **presión heredada**, no evidencia de autoridad legítima para componerlos. “PRESERVED” significa que S31 no traslada nuevas responsabilidades a App; no certifica que la baseline esté libre de presentación específica.

HomePage renderiza GP; SystemPage renderiza SP. No se reconstruyen labels, status, sessionLabel o message ni se inventa un lookup de copy según IDs.

## BASELINE

[baseline.json](evidence/session-31/baseline.json) registra SHA-256 de **343 archivos existentes**: código completo y harness históricos, gobernanza, contrato semántico, activos compartidos, documentación/evidencia previa, configuración y archivos raíz del prototipo. Captura del working tree recibido, anterior a crear el informe/inventario S31, no comparación contra HEAD.

El repositorio ya contenía cambios y archivos sin seguimiento de sesiones anteriores. No se revierten ni se incorporan como delta S31. No se crea commit.

[Preservation check](evidence/session-31/preservation-check.json) comprueba igualdad byte a byte contra esta captura. La preservación documental incluye las evidencias de S30 y los replay anteriores.

La suite 93/93, typecheck/lint/build/PWA de S30 es **evidencia histórica referenciada**, no ejecución atribuida a S31.

## CODE DELTA OR STOP

**STOP. Cero cambios de código de aplicación, contratos, transporte, fixtures, runtime o tests.**

Solo se crean este informe y evidencia documental de S31. No se repara parcialmente el título; ambos hardcodes siguen visibles. No se crea campo de framing, default semántico, nuevo artefacto de composición ni PSC-P02.

Este STOP completa la rama de falsación solicitada; no es una implementación pendiente dentro de S31.

## A CONTROL

Inspección de fuente actual:

- A selecciona marca Aurora Stay y Scenario/Script Family Adventure existentes.
- App.tsx:113/115 conserva los dos textos A literales.
- Su coincidencia con los lugares declarados en H25/H30 no acredita procedencia: las expresiones de cabecera no consultan esos artefactos.
- Cuenta H28, sujetos H27, status H29, mensaje H30, Activity H25 y hechos permanecen intactos.

Control de ejecución A en App: **NOT EXECUTED en S31**. No se presenta la inspección como observación DOM.

## B CONTROL

Inspección de fuente actual:

- B selecciona marca “Costa Clara Resort”, Scenario/Script B y fixture B.
- HomePage usa la misma rama si existe guestPerspective; los dos textos de cabecera siguen siendo literales A, sin lookup B.
- Los valores mirador/patio existentes no tienen la relación de framing que H31 necesita.
- No existe una cadena legítima declarada que permita registrar “declared source → observed B framing” para la intro. Esa cadena queda **NOT ESTABLISHED**.

No se inventa texto B ni se atribuye la cabecera predicha por la fuente a una ejecución realizada. Control de ejecución B en App: **NOT EXECUTED en S31**.

## COMPOSITION SWITCH CONTROL

El harness de composición existente permite seleccionar A/B mediante resolveDemo y el query param demo antes de render; App recibe el mismo tipo de runtime y el mismo código.

Lo que demuestra la inspección: cambiar composición puede cambiar marca/read models, pero las expresiones estáticas seleccionadas no dependen de esa entrada. No se ensaya alternancia en caliente, recarga, montaje A/B ni una salida nueva.

**Same App + different resolved composition → legitimate different framing: NOT ESTABLISHED.** La falta de intro es de relación; la falta de prop de marca en HomePage es de transporte. No se fusionan.

## READ-MODEL PRESERVATION

| Output | Autoridad recibida | Resultado S31 |
| --- | --- | --- |
| sessionLabel | H28, nombre de cuenta existente | PRESERVED |
| subjects[].label | H27, relación explícita de presentación de sujeto | PRESERVED |
| subjects[].status | H29, estado operacional | PRESERVED |
| message | H30, autoridad operacional/derivada + relación por posición | PRESERVED |
| Activity | H25 para representación de Evidence aceptada | PRESERVED |
| huntName | Literal del projector actual; no nueva procedencia desde Experience | PRESERVED / fuera de selección |
| SupervisionPerspective | Proyección separada de sujetos y evaluación | PRESERVED |

La garantía nueva es **identidad de fuente por hash**, no repetición de verificación dinámica acumulada. Las afirmaciones de ejecución H25–H30 se conservan con su alcance histórico.

## NEGATIVE CONTROLS

Retail y Arrival conservan todos sus archivos de composición, tipos y comportamiento implementado sin delta. No se les añade framing, journey presentations ni campos obligatorios/fallbacks.

- Retail: manifest sin Scenario/Script; fixture existente.
- Arrival: experience:arrival-welcome@1, Script de llegada, sin las relaciones H25/H27/H30 de Family Adventure.
- App conserva la rama genérica; no se modifica la condición de GP/SP en projectSnapshot.

**SOURCE-PRESERVATION VERIFIED.** No se ejecutan nuevos recorridos Retail/Arrival ni se declara regression PASS dinámica en S31.

## CURRENT APP EXECUTION

No ejecutada. La instrucción de S31 permite cerrar por inspección si el STOP ocurre antes de modificar App; esa es la rama aplicada.

La infraestructura disponible incluye Vitest/jsdom y render con React createRoot/MemoryRouter en pruebas existentes. No se añade un harness solo para reconstatar dos literales cuando el veredicto depende de la ausencia de autoridad declarada. Tampoco se usa un projector histórico para afirmar comportamiento actual de App.

## BROWSER / DOM VERIFICATION STATUS

| Verificación | Estado S31 |
| --- | --- |
| Current source inspection | EXECUTED |
| Inventario sintáctico TypeScript | EXECUTED; análisis estático, no render |
| Baseline/preservación SHA-256 | EXECUTED |
| Current App DOM/integration verification | NOT EXECUTED |
| Browser visual validation | NOT EXECUTED |
| Ejecución A/B con framing corregido | NOT EXECUTED / NOT ESTABLISHED |
| npm test / typecheck / lint / build | NOT EXECUTED; sin delta de código |
| Historical replay H21–H30 | No reejecutado; fuentes/trazas preservadas |

No se afirma validación visual, éxito de tests actuales ni resultados de aplicación que no se hayan ejecutado.

## SUPERVISION FREEZE

App.tsx:356 conserva `subject.id === "subject-p1" ? "P1 · Lucía" : "P2 · Huésped 2"`. La línea 363 conserva “Cuenta/sesión operativa” y sessionSubjectRef. También permanecen el criterio visible, conteos y resto de copy de SP.

H27 no se usa como autoridad de representación para SP. GP y SP no se equiparan. La ambigüedad cuenta/sujeto sigue visible; no se introduce viewer ni account→subject para resolverla.

## RECURRING PRESENTATION PRESSURE

H25, H27 y H30 alojan respectivamente presentación de Activity, de sujetos y narrativa por posición en Script. La inspección confirma que ninguno tiene competencia declarada para el framing estático seleccionado.

La ausencia H31 añade evidencia de una necesidad presentacional distinta. **No demuestra que DemoScript sea su host correcto**, ni selecciona PresentationModel, registry, resolver o nueva capa.

Recurring host != authority for a new relation. Recurrence != promotion.

## FALSIFICATION ANALYSIS

| Falsificador / restricción | Evidencia actual | Resultado |
| --- | --- | --- |
| La intro requiere una relación que no existe | Contratos, catálogos y proyección actuales no declaran framing estático de composición | **Falsificador observado** |
| El título no puede distinguir sus componentes | UI genérica separable de marca explícitamente seleccionada; property/title editorial no declarados | Fuente parcial legítima, estrictamente como branding; no rescata la intro |
| Solo se consigue usando otros textos | H25/H30/news contienen lugares, con responsabilidades diferentes | Sustitución no autorizada; no implementada |
| Transformar H30 en Experience summary | availableActionId→message no declara resumen | Prohibido; no realizado |
| Transformar H25 en itinerario | activityPresentation es representación posterior a Evidence aceptada | Prohibido; no realizado |
| App decide significado según IDs o artefactos A/B | No hay delta ni imports/branches nuevos | Frontera preservada |
| Resolver a la vez SP/viewer/account→subject | No se requiere para localizar la relación ausente | No seleccionado; congelado |
| Nuevos requisitos sobre Retail/Arrival | Cero cambio de contratos o composición | No introducidos |
| Corregir solo título | La regla exige suficiencia conjunta previa | No realizado |

El falsificador es una **ausencia acotada a las fuentes y relaciones actuales inspeccionadas**, no una imposibilidad general de producir framing ni una prueba de qué modelo futuro debe hacerlo.

## H31 VERDICT

**FALSIFIED bajo NO-NEW-RELATION.** La introducción situada carece de relación autorizante. Los datos existentes no bastan; la fuente legítima del componente de branding se registra independientemente.

No se clasifica INCONCLUSIVE por no ejecutar App: esta rama admite inspección de fuente y el gap se establece en las declaraciones, antes del transporte/render.

## L4 FRAMING RESULT

**SOURCE-INSPECTED / MISSING INTRODUCTORY FRAMING RELATION / STOP / OPEN.**

La presión queda identificada, no reparada. La cabecera específica de A continúa en App. No hay afirmación EXISTING-SOURCE / EXECUTION-VERIFIED para el framing conjunto.

## ARCHITECTURAL CONSEQUENCE

Architecture v0.5 ACTIVE y ADR-001–005 ACCEPTED, sin cambios. App continúa recibiendo la composición efectiva existente; no se añade autoridad nueva al consumidor.

El análisis distingue una posible necesidad mínima de transporte de marca de una relación ausente de introducción. No selecciona host, shape, arquitectura general o promoción de DemoScript. No se abre H32.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract intactos. PSC-P01 conserva su estado y texto; PSC-P02 no se crea. Ningún valor se reinterpreta como property, viewer, Participation, Sequence, TES Progression o Result.

Having a value != having framing authority. Having situated journey copy != having Experience summary. Having Activity location copy != having itinerary definition. App rendering != App semantic authority.

## ARTIFACT QUARANTINE

| Artefacto | Estatuto conservado |
| --- | --- |
| H25 activityPresentation | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED |
| H26 inspección/falsación de procedencia | Evidencia histórica; no contrato |
| H27 subjectPresentations | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED |
| H28 transporte de cuenta | LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED |
| H29 state→status | LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED |
| H30 experimentalJourneyPresentations, selector y ausencia | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED; no selector/fallback universal |
| Informe, baseline, inventario y preservación S31 | Evidencia de inspección; no nueva autoridad ni representación de producto |

No hay un artefacto nuevo de framing que promover o transportar.

## WHAT H31 DOES NOT PROVE

- Que brand == property o que el nombre de marca sea un título editorial de composición.
- Que Experience.name alimente actualmente huntName.
- Qué texto B debería mostrarse ni que B se haya renderizado/validado visualmente en esta sesión.
- Que una relación futura de framing deba residir en Script, Scenario, Fixture o Experience.
- Que exista viewer o una identidad humana inferible desde cuenta/sesión/sujeto.
- Que los restantes literales de App sean correctos o estén legitimados por haber sido preservados.
- Que las pruebas históricas certifiquen App actual.
- Que STOP implique una imposibilidad fuera de NO-NEW-RELATION.
- Que L4, L3c o Demo Factory estén promovidos/cerrados productivamente.

## REMAINING PRESSURES

Se observa la relación ausente entre composición y framing introductorio estático; su eventual experimento requiere selección posterior. La presentación nominal de propiedad/título editorial tampoco está declarada, si una sesión futura exige ese significado más fuerte que marca.

Supervisión sigue abierta con sus labels A y encuadre de sesión. huntName literal del projector, link genérico fijo a A, copy genérico de carga/Actividad y demás elementos inventariados permanecen fuera de selección. La recurrencia de hosts presentacionales continúa observada, sin promoción.

No se selecciona automáticamente ninguna presión posterior ni se abre H32.

| Dimensión | Resultado |
| --- | --- |
| H31 | **FALSIFIED** |
| NO-NEW-RELATION | **INSUFFICIENT** |
| APP TITLE AUTHORITY | **UI shell + resolved brand name AVAILABLE, qualified as branding only; property/composition-title authority NOT ESTABLISHED; no partial correction** |
| APP INTRODUCTORY FRAMING AUTHORITY | **MISSING DECLARED RELATION** |
| APP CONSUMER BOUNDARY | **PRESERVED; inherited hardcodes remain visible** |
| A/B COMPOSITION FRAMING | **NOT ESTABLISHED; no current App execution claimed** |
| L3a | **PRESERVED / EXPERIMENTALLY ADDRESSED H28** |
| L3b | **PRESERVED / EXPERIMENTALLY ADDRESSED H27** |
| L3c | **PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30** |
| L4 APPLICATION FRAMING | **SOURCE-INSPECTED / STOP / OPEN** |
| L4 SUPERVISION | **PRESERVED / OPEN** |
| L5 | **PRESERVED / EXPERIMENTALLY ADDRESSED H25** |
| RECURRING PRESENTATION PRESSURE | **OBSERVED / NOT PROMOTED** |
| NEXT MATERIAL PRESSURE | **Missing composition introductory framing relation observed but NOT SELECTED; H32 NOT OPENED** |

