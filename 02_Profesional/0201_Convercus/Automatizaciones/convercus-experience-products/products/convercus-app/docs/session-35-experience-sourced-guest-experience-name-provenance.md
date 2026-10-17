---
title: "Sesión 35 — Experience-Sourced Guest Experience Name Provenance"
language: es
version: "v1.0"
status: "CLOSED / H35 SUPPORTED WITH QUALIFICATION within Family Adventure A/B"
date: "2026-09-18"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 35 — Experience-Sourced Guest Experience Name Provenance

## H34 CONSOLIDATED INPUT

[S34](session-34-operational-session-subject-representation-provenance.md) permanece CLOSED / SUPPORTED WITH QUALIFICATION. NO-NEW-RELATION SUFFICIENT; session subject desde autoridad operacional existente, account claim REMOVED AS UNSUPPORTED, viewer/authentication NOT INTRODUCED. A/B CURRENT APP DOM-INTEGRATION VERIFIED en S34. No se reconstruyen decisiones anteriores.

L3a/H28, L3b/H27, L3c/H29–H30, L4 framing/H32, L4 sujetos supervisados/H33, L4 sesión supervisora/H34 y L5/H25 se reciben preservados/experimentalmente abordados. Recurrencia Script-bound OBSERVED / FURTHER QUALIFIED / NOT PROMOTED. Architecture v0.5 ACTIVE, ADR-001–005 ACCEPTED, TES y Product Semantic Contract unchanged. PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE unchanged; PSC-P02 NOT CREATED. H25–H34 no se promueven.

## H35 HYPOTHESIS

ExperienceDefinition.name ya posee autoridad semántica para el nombre presentado de la Experience en GuestPerspective.huntName. Puede transportarse sin nuevo contenido editorial, Script, inferencia desde Scenario/marca/manifest, cambio de runtime state, Evidence, evaluación, K o claim. Condición NO-NEW-RELATION.

## VARIABLE UNDER TEST

Sólo la procedencia de GP.huntName y su h1 en HomePage. No se seleccionan marca/eyebrow, introducción, cuenta, sujetos, estados, mensajes, Activity, Supervisión, enlace fijo, navegación genérica o document title. La única nueva dependencia autorizada es Experience.name → GP.huntName.

## WHY NO NEW RELATION IS AUTHORIZED

Existe una ExperienceDefinition resuelta con nombre declarado. Primero se determina si nombra lo mismo que esta superficie. La recurrencia de presentaciones en Script no autoriza una relación experimental huntName ni un fallback editorial. Si la correspondencia no estuviera respaldada habría que detenerse; la inspección encuentra soporte semántico previo y un transporte ausente.

## EXPERIENCE NAME SOURCE INSPECTION

La [inspección previa al delta](evidence/session-35/pre-delta-source-inspection.md) precede a las ediciones. El [inventario](evidence/session-35/name-use-inventory.txt) registra ExperienceDefinition, experience.name y huntName en código/documentación/archivos históricos; excluye dependencias, build y trazas serializadas.

| Campo/capa | Productor | Consumidor | Responsabilidad | Transporte recibido |
| --- | --- | --- | --- | --- |
| ExperienceDefinition.id/name/tesBaseline | Catálogo artifacts.experiences | resolveDemo → ResolvedDemoRuntime | Identidad técnica, denominación y baseline semántica distintas | Artefacto resuelto por Scenario.experienceRef |
| Scenario.experienceRef | Scenario A/B/Arrival | Resolver; selección operacional del adapter | Referencia a Experience, no copy | A/B comparten family-adventure |
| runtime.experience | resolveDemo | Panel genérico usa tesBaseline; composición resuelta | Artefacto de Experience efectivo | name no llegaba al provider/proyector |
| GP.huntName | Literal projectGuestPerspective | HomePage h1 #adventure-title | Nombre presentado de Experience | Literal → GP → h1 |
| Script/Brand/Manifest | Sus artefactos | Sus consumidores propios | Presentación situada, marca, selección/configuración | Ningún transporte autorizado a huntName |

Se inspeccionaron contratos, declaraciones A/B/Arrival/Retail, resolver, runtime, constructor/getSnapshot/projectSnapshot, projector y HomePage. No existe otro consumidor de experience.name que ya alimente huntName. App consume GP y no consulta Experience para el h1.

## HUNTNAME SEMANTIC ANALYSIS

La correspondencia no se deduce del nombre de la propiedad ni de strings iguales. [S21 audit, M05](session-21-composition-boundary-factory-reusability-audit.md) identifica «Aventura Familiar / Experience» como definición referenciada y nombre duplicado, con identidad/nombre resueltos como fuente del read model. [S26, matriz de procedencia](session-26-situated-guest-perspective-provenance.md) clasifica huntName como «Título presentacional de Experience; no hecho» y precisa que no se declara nombre distinto de instancia de hunt. S26 también distingue ExperienceDefinition de fuentes de nombres humanos y narrativa.

[S31](session-31-application-composition-framing-provenance.md) separa h1 de Experience, eyebrow de marca e introducción de composición. El código actual conserva esa separación: h1 copia huntName, Script no declara título de campaña/instancia y A/B resuelven una Experience común. Esto sostiene localmente la responsabilidad del campo. No se promueve la definición candidata documental family-adventure.md ni se activa el modelo legacy de dominio; la fuente ejecutada es la ExperienceDefinition de Demo Factory.

## SEMANTIC SUPPORT MATRIX

| Pregunta | Estado | Alcance |
| --- | --- | --- |
| A. name identifica la Experience como artefacto semántico | SUPPORTED como denominación | id/referencia sigue siendo identidad técnica; name no es clave única o evaluativa |
| B. Nombre destinado a lectura humana | SUPPORTED | Denominación explícita y responsabilidad documentada; no política universal de localización |
| C. Estable entre Scenarios/composiciones que comparten Experience | SUPPORTED en A/B | Misma fuente resuelta; no inmutabilidad temporal |
| D. huntName es nombre presentado de esa Experience | SUPPORTED localmente | S21/S26, separación S31 y consumidor actual |
| E. Título de composición, journey, campaña u otra responsabilidad | NOT SUPPORTED en esta superficie | No relación declarada de instancia/campaña; posibles requisitos futuros NOT DETERMINED |

## CANDIDATE SOURCE ANALYSIS

| Candidato | Decisión |
| --- | --- |
| ExperienceDefinition.name | Seleccionado: denominación de la Experience compartida |
| DemoScript | No seleccionado: contenido situado/affordances, no autoridad sobre nombre de Experience |
| Scenario | No seleccionado: situación, comportamiento y referencia; no produce nombre |
| BrandArtifact.name | No seleccionado: nombre de marca, separado del nombre semántico |
| Manifest/demoId | No seleccionado: identidad/configuración de composición; no parsing |
| Literal del proyector | Síntoma histórico, sin procedencia declarada |

## STRING EQUALITY / AUTHORITY DISTINCTION

Antes del delta ambos textos eran «Aventura Familiar» pero no había flujo entre ellos. Same text != same authority. La decisión usa la responsabilidad documental de huntName y la Experience resuelta; la ejecución causal se acredita variando sólo Experience.name y observando GP/h1 con hechos intactos. La apariencia canónica igual no se presenta como prueba suficiente.

## TRANSPORT / RELATION DISTINCTION

RELATIONSHIP SEMANTICS EXISTING / TRANSPORT MISSING. El resolver ya localiza la Experience legítima. Se añade transporte de su nombre a un read model cuyo campo ya representa esa denominación. No se declara un título editorial nuevo, mapping, relación Script→huntName o modelo de presentación.

## SOURCE DECISION

Fuente: ExperienceDefinition.name de la Experience resuelta por resolveDemo. Se copia literalmente, sin trim, parsing, prefijo, localización, concatenación de marca o fallback al literal anterior. Se conserva el nombre del campo huntName; renombrar contratos está fuera del experimento.

## THREADING PATH

```text
Scenario.experienceRef → catálogo Experience resuelto por resolveDemo
Experience.name → MockDataAdapter(experienceName)
→ getSnapshot → projectSnapshot(experienceName)
→ projectGuestPerspective(experienceName) → GP.huntName
→ HomePage h1
```

Scenario selecciona por referencia, no infiere ni fabrica el nombre. Se transporta un escalar: el provider no necesita id, tesBaseline u objeto Experience completo para esta superficie. El parámetro es privado/readonly en el adapter y no interviene en acciones/reset/evaluación. Los argumentos finales admiten texto vacío para utilidades sin Experience; no contienen el literal histórico ni consultan Script. El resolver canónico suministra el campo name obligatorio en A/B y Arrival. Retail carece de Experience y sigue sin GP.

## APP CONSUMER BOUNDARY

PRESERVED: App permanece byte-identical a S34. HomePage sigue `<h1 id="adventure-title">{adventure.huntName}</h1>`. No acceso paralelo a runtime.experience.name, branch A/B o lookup de artefactos desde App. Navegación fija, otras etiquetas y document title permanecen congelados.

## BASELINE

[Baseline](evidence/session-35/baseline.json): 405 archivos del programa recibidos, excluyendo dependencias/build, .git, .DS_Store, tsbuildinfo y evidencia S35 nueva. El árbol contiene cambios heredados; no se sustituye por HEAD. Se conservan copias exactas de los tres archivos de producto y de la instrumentación histórica que requiere adaptación.

El primer `npm run check` completó typecheck/lint, pero cuatro pruebas agotaron sus límites de tiempo bajo concurrencia por defecto (92 PASS / 4 timeouts); no se había editado producto. Se conserva el [log inicial](evidence/session-35/baseline-check.log). La repetición con `npm test -- --maxWorkers=1` pasó 96/96 tests en 28 archivos y build/PWA: [log serial](evidence/session-35/baseline-serial-check.log). No se cambiaron timeouts, assertions ni configuración del proyecto para obtener ese resultado.

Auditoría: 387 archivos recibidos idénticos, tres archivos de producto con transporte y 15 harnesses históricos con instrumentación; cero ausentes/cambios inesperados. App, gobernanza, semántica y toda la evidencia S34 permanecen iguales. Los hashes originales no se rebasan.

## CODE DELTA OR STOP

Se ejecuta el [delta de transporte](evidence/session-35/application-delta.patch), sin STOP: bootstrap pasa experience?.name al provider; adapter conserva/pasa el escalar; projector asigna huntName: experienceName. App, contratos, artefactos, Scenario, Script, Fixture, guards, evaluadores, CSS y navegación no cambian.

El código de evaluación anterior a projectGuestPerspective, projectSupervisionPerspective entero y executeAction/reset se comparan con S34. La [instrumentación histórica](evidence/session-35/historical-instrumentation-delta.patch) se separa del delta de producto.

## A CONTROL

App vigente, hospitality-family-adventure: initial → enlist-p1 → discover-clue-a → activate-p2 → discover-clue-b → reset. Se navega por Home, Supervisión y Activity en cada fase. GP.huntName y h1 igualan exactamente runtime.experience.name. Para el nombre canónico, snapshots, acciones, evaluaciones y todo DOM coinciden con S34.

## B CONTROL

App vigente, hospitality-family-adventure-costa, mismo recorrido y verificaciones. Conserva marca/contexto/cuenta/presentación B, con el mismo nombre de Experience que A. Cada composición se compara contra su propia traza S34, sin exigir igualdad de hechos contextuales entre A/B.

## SHARED EXPERIENCE CONTROL

A/B tienen distintos Scenario.id y la misma experienceRef. Sus nombres GP/h1 permanecen iguales durante todas las fases/reset aunque difieran Script, marca, Fixture, cuenta, sujetos presentados, intro, narrativa y Activity. Same Experience → same Experience name en el alcance demostrado.

## EXPERIENCE NAME VARIATION CONTROL

En cada composición, una copia de catálogo cambia únicamente Experience.name a «Travesía compartida · H35». Experience.id, Scenario, Script, Fixture, marca y comandos se conservan. Cambian sólo GP.huntName y el h1 que lo consume. Los facts, evaluación completa, SP, Activity, intro y branding son iguales; Home sólo difiere en el contenido del h1. El control refuta dependencia del string histórico.

## EXPERIENCE ID INDEPENDENCE CONTROL

Se cambia únicamente Experience.id a `opaque:experience/Z-42` en copia de catálogo conservando name y la clave referenciada. El resolver usa esa clave y no impone que sea una derivación de id; las referencias existentes siguen resolviendo el artefacto. HuntName, snapshots y DOM permanecen iguales; no se parsea id.

No se renombra la clave `experience:family-adventure@1`: selecciona comportamiento en el adapter, y cambiarla ampliaría el alcance a selección operacional. La independencia acreditada corresponde al campo id, no a todas las formas posibles de renombrar referencias.

## BRAND INDEPENDENCE CONTROL

Sólo BrandArtifact.name cambia a «Marca H35». Cambian sus superficies de branding, conservando GP.huntName, hechos y SP. Brand name != Experience name. App mantiene el framing H32 y la intro independiente.

## SCRIPT PRESENTATION INDEPENDENCE CONTROL

Cinco perturbaciones separadas por composición: subjectPresentations, experimentalJourneyPresentations, experimentalIntroductoryFraming, activityPresentation y presenterLabel. Sus superficies legítimas cambian y huntName se mantiene. El recorrido pulsa los botones públicos y verifica su texto contra presenterLabel; cambiar affordance copy no cambia el comando recibido ni evaluación.

No se crea experimentalHuntName, presentation.title, experienceTitle u otro fallback en Script. La recurrencia editorial no se usa como autoridad universal.

## SCENARIO INDEPENDENCE CONTROL

A/B constituyen el control principal: Scenarios/contextos distintos y Experience compartida producen mismo nombre. No se crea Scenario artificial. No se infiere copy desde Scenario.id, acciones o contextos.

## ACCOUNT / SUBJECT / STATE INDEPENDENCE

Perturbar member.name cambia sólo account display/GP.sessionLabel; cambiar subjectPresentations cambia GP labels. Las acciones legítimas cambian estados, Evidence y determinaciones hasta claim established. HuntName conserva su fuente en cada fase/reset. No depende de cuenta, sujeto habilitado, Evidence o resultado evaluativo.

## ABSENCE OBSERVATION

ExperienceDefinition.name es `string` obligatorio. No se elimina, no se introduce undefined mediante cast ni se debilita el contrato. Sí se prueba name="": cadena válida bajo el tipo y sin validador non-empty existente. GP.huntName y el h1 quedan vacíos, conservando todos los hechos y demás DOM. No se recupera «Aventura Familiar» ni contenido de Script.

Es observación local de nombre declarado vacío, no requisito de producto ni diseño de UX de error. La ausencia real del campo queda fuera del contrato y no se inventa.

## NEGATIVE CONTROLS

Retail carece de Experience resuelta; Arrival resuelve experience:arrival-welcome@1 cuyo name es «Llegada acompañada». App usa tesBaseline de Experience en su panel genérico, no name como título de aventura. Transportar name de Arrival no crea GP porque se conserva la selección operacional existente.

Ambos recorren App actual, acciones y reset. Snapshots, evaluación y DOM de Home/Activity/panel genérico coinciden con S34. GP/SP familiar permanecen ausentes; no huntName, defaults o UI Family Adventure nueva.

## CURRENT APP DOM / INTEGRATION EXECUTION

EXECUTED mediante React createRoot, MemoryRouter y jsdom, App actual, resolver/provider/proyectores vigentes y acciones públicas. No se sustituye getSnapshot ni se mockean módulos de producto en H35. Capturas Home/Supervisión/Activity y llamadas/resultados completos de ambos evaluadores por fase. Navegar no modifica snapshot ni dispara evaluación.

La comparación usa la traza inmutable S34; H35 no acredita ejecución vigente mediante runtime archivado. La traza contiene 24 recorridos actuales: A/B canónicos, diez variantes por composición y Retail/Arrival. Son 137 fases/reset y 411 capturas DOM. No se incluye ningún recorrido histórico en esos recuentos.

## BROWSER VISUAL VALIDATION STATUS

NOT EXECUTED. No se evalúa layout/móvil, legibilidad de nombres extensos o UX del nombre vacío. DOM/integration no equivale a validación visual. La cualificación afecta a la suficiencia local y procedencia, no a preferencias de presentación.

## CURRENT CUMULATIVE REGRESSION

H25 Activity, H27 labels, H28 cuenta, H29 status, H30 message, H32 brand/intro, H33 IDs supervisores y H34 par de sesión se comprueban sobre código actual durante canónicos y perturbaciones. Canonical DOM completo igual a S34; variantes de Experience.name sólo alteran huntName/h1. K, atribución, estados y claim siguen sus fuentes anteriores.

Validación final: typecheck PASS, lint PASS, **97/97 tests en 29 archivos**, build/PWA PASS. Se ejecutaron `npm run typecheck`, `npm run lint`, `npm test -- --maxWorkers=1` y `npm run build`; la concurrencia limitada es una opción de ejecución, no una modificación del proyecto. Ver [typecheck](evidence/session-35/typecheck.log), [lint](evidence/session-35/lint.log), [tests finales](evidence/session-35/final-tests.log) y [build](evidence/session-35/final-build.log).

## HISTORICAL REPLAY STATUS

Los harnesses históricos conservan sus aserciones y mocks de versiones previas. Cuando aún dependían de módulos actuales modificados en H35, se añade routing explícito a copias S34. El helper test-only historical-read redirige únicamente archivos exactos enumerados en archive-paths.json; rutas históricas anteriores conservan precedencia. No hay mock global de fs ni relajación de hashes. Las copias fuente .txt son exactas; las copias ejecutables de bootstrap/vertical sólo relocalizan imports.

H34 se etiqueta como replay S34 y su grabación opcional pasa a H34_REPLAY_RECORD_PATH. Las evidencias originales no se sobrescriben. H35 importa node:fs y módulos de producto actuales directamente; no utiliza el helper de lectura histórica para acreditar ejecución vigente. La baseline H35 contrasta explícitamente originales archivados y fuentes que deben permanecer intactas.

## EXECUTION TRACE

[Traza H35](evidence/session-35/execution-trace.json): originales y diez variantes por composición, negativos, acciones, snapshots, DOM de tres superficies y ambas evaluaciones. Incluye hashes de baseline, App, tres fuentes de transporte y harness. Se graba sólo después de pasar todas las aserciones, mediante creación exclusiva en H35_RECORD_PATH.

[Preservación](evidence/session-35/preservation-check.json) y [resumen](evidence/session-35/verification-summary.json) distinguen producto/instrumentación y enlazan evidencia/fuentes. Para repetir con los mismos límites de recursos, usar los comandos documentados en el resumen; para grabar otra traza elegir una ruta nueva.

## L3a STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H28. Cuenta desde member.name; sin autoridad sobre nombre de Experience.

## L3b STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H27. Labels de sujeto siguen su relación experimental GP.

## L3c STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30. Estado operacional y narrativa situada no nombran la Experience.

## L4 FRAMING STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H32. Marca e introducción siguen separadas del nombre semántico.

## L4 SUPERVISION SUBJECT STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H33. IDs literales en encabezados, no nombre humano.

## L4 SUPERVISION SESSION STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H34. «Sujeto de sesión operativa» y referencia literal intactos.

## L4 HUNTNAME RESULT

EXPERIENCE-SOURCED / EXISTING SEMANTIC NAME / MINIMAL LOCAL TRANSPORT / CURRENT APP DOM-INTEGRATION VERIFIED within A/B. La superficie canónica conserva su texto; ahora tiene procedencia causal desde la autoridad seleccionada.

## L5 STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H25. Activity mantiene contenido situado y no alimenta huntName.

## PRESENTATION AUTHORITY STRATIFICATION

EVIDENCE STRENGTHENED / NOT PROMOTED. H35 aporta evidencia local de semantic definition metadata → semantic presentation, junto a autoridad operacional/diagnóstica en H33/H34 y contenido editorial situado explícito en H25/H27/H30/H32. Refuerza la contraevidencia a «all presentation belongs in Script».

No se convierte en regla universal. No ADR, PresentationBoundary, PresentationModel ni promoción de DemoScript o ExperienceDefinition a propietarios universales de presentación.

## FALSIFICATION ANALYSIS

| Falsador | Observación |
| --- | --- |
| Experience.name no autoriza semánticamente huntName | No observado: responsabilidades documentadas y consumidor actual compatibles |
| huntName requiere título editorial distinto | No observado en A/B; no se inventa necesidad de campaña/instancia |
| Requiere Script, Scenario copy, brand, parsing o App branching | No observado: escalar resuelto y controles independientes |
| Variar name altera runtime/Evidence/evaluación/K/claim | No observado: facts y evaluaciones completos iguales salvo campo GP |
| App debe abandonar GP como fuente | No observado: App byte-identical |
| Nombre vacío requiere fallback histórico | No observado: se conserva literalmente la cadena vacía |

## H35 VERDICT

SUPPORTED WITH QUALIFICATION. NO-NEW-RELATION SUFFICIENT para esta responsabilidad local de GP/h1. Cualificaciones: A/B, denominación de Experience efectiva de Demo Factory, sin título de instancia/campaña, independencia limitada del campo id, comportamiento vacío observado y sin validación visual. No prueba suficiencia universal.

## ARCHITECTURAL CONSEQUENCE

Architecture v0.5 y ADR-001–005 unchanged. App consumidor preservado. Se transporta metadata existente sin nueva abstracción o relación editorial. La estratificación permanece evidencia emergente, no principio promovido.

## SEMANTIC CONSEQUENCE

TES, Product Semantic Contract y PSC-P01 unchanged; PSC-P02 NOT CREATED. No cambia semántica de Experience, evaluación, admisibilidad, K o claim. Experience.name denomina; id/referencia identifica técnicamente. Se reduce duplicación de copy sin inferir nueva identidad o relación.

## ARTIFACT QUARANTINE

H25–H34 y H35 permanecen EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. El delta puede revertirse restaurando los tres archivos de producto archivados, sin migración de datos. Harnesses/copias son instrumentación experimental. H36 NOT OPENED.

## WHAT H35 DOES NOT PROVE

No prueba nombre único/global, localización, título de composición, instancia o campaña, igualdad de marca y Experience, clasificación universal de presentación, usabilidad de texto vacío o largo ni renombrado libre de claves de selección operacional. No promueve la definición candidata documental ni acredita productización del runtime.

## REMAINING PRESSURES

Navegación fija a A y otras superficies no seleccionadas permanecen visibles y sin resolver. Posibles títulos situados futuros necesitarían responsabilidad/fuente explícita; H35 no la crea. NEXT MATERIAL PRESSURE OBSERVED BUT NOT SELECTED; H36 no abierto.

| Dimensión | Veredicto final |
| --- | --- |
| H35 | SUPPORTED WITH QUALIFICATION |
| NO-NEW-RELATION | SUFFICIENT |
| HUNTNAME AUTHORITY | Experience.name |
| EXPERIENCE / HUNTNAME SEMANTIC CORRESPONDENCE | SUPPORTED within tested scope |
| APP CONSUMER BOUNDARY | PRESERVED |
| A/B HUNTNAME | CURRENT APP DOM-INTEGRATION VERIFIED |
| L3a | PRESERVED / EXPERIMENTALLY ADDRESSED H28 |
| L3b | PRESERVED / EXPERIMENTALLY ADDRESSED H27 |
| L3c | PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30 |
| L4 FRAMING | PRESERVED / EXPERIMENTALLY ADDRESSED H32 |
| L4 SUPERVISION SUBJECT | PRESERVED / EXPERIMENTALLY ADDRESSED H33 |
| L4 SUPERVISION SESSION | PRESERVED / EXPERIMENTALLY ADDRESSED H34 |
| L4 HUNTNAME | EXPERIENCE-SOURCED / MINIMAL TRANSPORT / EXPERIMENTALLY ADDRESSED H35 |
| L5 | PRESERVED / EXPERIMENTALLY ADDRESSED H25 |
| PRESENTATION AUTHORITY STRATIFICATION | EVIDENCE STRENGTHENED / NOT PROMOTED |
| NEXT MATERIAL PRESSURE | OBSERVED BUT NOT SELECTED |
