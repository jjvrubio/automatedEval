---
title: "Sesión 39 — Effective Composition Navigation Identity"
language: es
date: "2026-09-22"
consolidated: "2026-09-23"
status: "CLOSED / STOP PRE-DELTA"
scope: "Cierre documental de S39 y orientación posterior; sin reejecución, delta de producto ni apertura de H40"
---

# Sesión 39 — Effective Composition Navigation Identity

## SESSION STATUS

CLOSED / STOP PRE-DELTA. P39, el supuesto «Costa navega a A mediante la superficie Family Adventure seleccionada y necesita reparación», queda FALSIFIED / NOT REPRODUCED. H39, la suficiencia de la identidad efectiva existente para conservar A→A y B→B sin una nueva relación de navegación, queda SUPPORTED WITH QUALIFICATION dentro de las garantías ejecutadas.

El enlace fijo solo se renderiza en la Home genérica, mientras que Family Adventure ya consume la identidad efectiva en «Mi aventura». Al desaparecer la premisa que habría autorizado una reparación, el STOP fue obligatorio: PRODUCT / SEMANTIC / ARCHITECTURAL / NAVIGATION RELATION DELTA → NONE.

Durante la ejecución S39 se añadieron este informe, evidencia y un harness de siete controles; ningún archivo entonces recibido se modificó. La inspección visual en navegador no se pudo ejecutar y no se sustituye por una afirmación de aceptación humana.

## CONSOLIDATION SCOPE

La consolidación del 2026-09-23 corrige la clasificación final de dos proposiciones distintas y registra una orientación para la fase posterior. No reejecuta S39 ni abre una sesión experimental. La ejecución del 2026-09-22 y sus resultados permanecen como ocurrieron; los resultados de tests, tipos, lint y build citados más abajo pertenecen a esa ejecución.

El único archivo editado en esta consolidación es este informe. Se preservan producto, App, bootstrap, manifests, providers/adapters, artifacts/fixtures, Scenario, DemoScript, ExperienceDefinitions, GuestPerspective, Supervision, Evidence, evaluadores, K, claims, contratos, CSS, navegación, todos los harnesses y toda la evidencia experimental S39 e histórica S37/S38. No se sustituyen, borran ni regeneran trazas, baselines o expectations para acomodar el cierre.

La orientación posterior permite avanzar hacia demos útiles e interacción real tan pronto como sea metodológicamente seguro. No selecciona una demo, una presión ni H40; tampoco constituye un ADR.

## H38 CONSOLIDATED INPUT

[S38](session-38-historical-replay-portability-evidence-integrity.md) permanece CLOSED / SUPPORTED WITH QUALIFICATION. Historical replay y current cumulative verification siguen separados. H21 y H36 permanecen HISTORICALLY FALSIFIED; H37 permanece SUPPORTED WITH QUALIFICATION y verifica el producto actual, no un runtime archivado.

Architecture v0.5 ACTIVE; ADR-001–005 ACCEPTED; TES y Product Semantic Contract unchanged. PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE, fortalecido por evidencia previa, unchanged; PSC-P02 NOT CREATED. La regla S38 de integridad permanece LOCAL / EXPERIMENTAL / NOT PROMOTED. Costa B continúa siendo composición experimental, no demo comercial aceptada. Todas las cualificaciones S38, incluidas rutas, assets, toolchain y concurrencia, se preservan.

## PRESSURE SELECTED

Únicamente la navegación de Home supuestamente fijada a `hospitality-family-adventure` cuando una composición Family Adventure ya está resuelta. Se inspecciona «Búsqueda del tesoro» y, donde esa Home no se renderiza, su equivalente actual «Mi aventura».

No se seleccionan otras rutas, enlaces, framing, semántica de Activity, presentación, branding ni infraestructura de replay.

## P39 — PROBLEM ASSUMPTION

La composición B / Costa, cuando Family Adventure ya está resuelta, navega hacia A mediante la superficie seleccionada y necesita una reparación.

Resultado: FALSIFIED / NOT REPRODUCED. La existencia del enlace genérico fijo a A no implica que ese enlace sea alcanzable desde la Home Family Adventure de B. La inspección y ejecución S39 muestran que A/B utilizan «Mi aventura», que consume la identidad efectiva ya resuelta.

## H39 — EFFECTIVE COMPOSITION NAVIGATION IDENTITY

La identidad efectiva ya disponible es suficiente para conservar A→A y B→B en la superficie seleccionada, sin introducir una nueva relación de navegación, preservando el comportamiento heredado de Retail y Arrival dentro de las garantías efectivamente ejecutadas.

Resultado: SUPPORTED WITH QUALIFICATION. Las comprobaciones de identidad, provider y estado respaldan esa suficiencia local; Retail/Arrival quedan cualificados por la reconstrucción de bootstrap y la ausencia de recarga documental nativa. La falsación corresponde a P39 y la evidencia favorable corresponde a H39.

NO-NEW-NAVIGATION-RELATION → LOCALLY SUFFICIENT / EVIDENCE-BACKED FOR THE TESTED SURFACE / NOT PROMOTED. No se demuestra que todos los enlaces deban preservar `demoId` ni que `runtime.manifest.demoId` sea el modelo general de navegación futura. Los PASS del harness respaldan las observaciones dentro de su alcance; por sí solos no determinan el veredicto de una hipótesis ni acreditan una reparación.

## PRE-DELTA NAVIGATION MATRIX

Matriz ejecutada antes de cualquier delta productivo, que finalmente no existe. [Traza completa final](evidence/session-39/pre-delta-navigation-matrix-final.json), [primera ejecución](evidence/session-39/pre-delta-navigation-matrix.json) y [resultados de assertions](evidence/session-39/navigation-final-results.json).

Para abreviar las tablas: R = `retail-baseline`; H = `hospitality-stay`; A = `hospitality-family-adventure`; B = `hospitality-family-adventure-costa`. `/?demo=X` significa el identificador completo, no la letra. El JSON conserva todas las rutas, snapshots, DOM y campos literales.

| Composición | manifest.demoId | Ruta inicial | guestPerspective | Etiqueta seleccionada | href/to actual | reloadDocument |
| --- | --- | --- | --- | --- | --- | --- |
| R | R | `/?demo=R` | Ausente | Búsqueda del tesoro | `/?demo=A` | true, expresión existente |
| H | H | `/?demo=H` | Ausente | Búsqueda del tesoro | `/?demo=A` | true, expresión existente |
| A | A | `/?demo=A` | Presente | Mi aventura | `/?demo=A` | false, omitido en NavLink |
| B | B | `/?demo=B` | Presente | Mi aventura | `/?demo=B` | false, omitido en NavLink |

| Composición | Runtime antes→después | Composición URL antes→después | Evidencia de composición después | Fuente del target | Autoridad / estatuto |
| --- | --- | --- | --- | --- | --- |
| R | R→A* | R→A* | Aurora Stay, Aventura Familiar, Lucía, jardín/fuente | Literal de Home genérica | Entrada intencional existente a A |
| H | H→A* | H→A* | Aurora Stay, Aventura Familiar, Lucía, jardín/fuente | Literal de Home genérica | Entrada intencional existente a A |
| A | A→A | A→A | Aurora Stay, Lucía/Huésped 2, jardín/fuente | `runtime.manifest.demoId` vía `demoSearch` | Identidad efectiva ya resuelta |
| B | B→B | B→B | Costa Clara Resort, Inés/Mateo, mirador/patio | `runtime.manifest.demoId` vía `demoSearch` | Identidad efectiva ya resuelta |

*R/H: clic DOM ejecutado; React Router no lo intercepta. El harness intercepta únicamente la navegación documental no implementada por jsdom y reconstruye explícitamente unmount→URL de destino→`selectDemoId`→`resolveDemo`→App nueva. La URL inmediatamente después del clic interceptado sigue siendo R/H y consta en la traza. El resultado A posterior pertenece a esa reconstrucción de bootstrap; **no es una recarga nativa ejecutada en navegador**.

A/B: clic real sobre el DOM de App y actualización real de history por BrowserRouter dentro de jsdom, sin reconstrucción del runtime. Se comprueban Home inicial, Home con una pista y vuelta desde Actividad; URL, runtime, provider y snapshot permanecen coherentes. «Evidencia visible» designa texto expuesto por el DOM, no una captura visual revisada por una persona.

## SOURCE / AUTHORITY ANALYSIS

| Fuente inspeccionada | Función y límite de autoridad |
| --- | --- |
| `main.tsx` | Resuelve una vez al arrancar: `resolveDemo(selectDemoId(window.location.search))`; pasa ese runtime a App. No vuelve a resolverlo por cada cambio de ruta SPA. |
| `bootstrap.ts`: `selectDemoId` | La query `demo` elige la entrada inicial; ausencia selecciona Retail. La URL no es por sí sola prueba de la composición que sigue viva tras navegar. |
| `bootstrap.ts`: `resolveDemo` | Resuelve manifest, referencias, artifacts y proveedor. No se altera resolución, selección ni instancia. |
| Identidad del manifest | `demoId` identifica la composición resuelta; no declara un modelo universal de destinos intencionales. |
| Runtime resuelto | Vincula manifest, brand, scenario, script, experience y provider efectivos. Se comprueban por separado identidad y estado, no solo query o marca. |
| `App.tsx:112–141` | Si existe GuestPerspective, Home retorna la rama de aventura. No alcanza el quick link genérico de la línea 186. |
| `App.tsx:186` | Target literal A y `reloadDocument={!snapshot.guestPerspective}`. En la rama alcanzable de ese enlace, GuestPerspective está ausente: es entrada a A desde el contexto genérico. |
| `App.tsx:453–477` | AppShell usa `isAdventure` para la superficie y `runtime.manifest.demoId` para `demoSearch`. «Mi aventura» ya enlaza la identidad efectiva. |

La mera búsqueda del literal A no demuestra una navegación B→A alcanzable. GuestPerspective elige la rama existente, pero sus labels, mensajes o subjects no eligen la identidad del target. No se introduce parsing de copy ni autoridad de Activity. Tampoco se convierte «hay demoId disponible» en «todos los enlaces deben preservar la demo actual».

## BASELINE

[Baseline capturada](evidence/session-39/baseline.json): 640 archivos materiales del working tree recibido, no HEAD, y 11 entradas de metadata/caché inventariadas aparte. Conserva la reconstrucción documental del usuario. Dependencias, build regenerable y nueva evidencia S39 quedan fuera de ese inventario; no se modifica la clasificación de ninguna baseline histórica.

Archivos productivos autorizados a cambiar: ninguno, tras el STOP. Hashes SHA-256 pre-delta:

| Fuente | SHA-256 |
| --- | --- |
| `src/app/App.tsx` | `cde3b490f05d42bf11abff185f09b9be5e8828897cc0a96a1c064a964a99b8ef` |
| `src/main.tsx` | `cb88ce48d25e4dfe894e0483efbdd495b77e2460e802a66cdbb7e43934e5fd9f` |
| `src/demo-factory/bootstrap.ts` | `6388ada8fde7ea4b043d6f5c75f8fa925f213499350ffd6f0dd038e7caa1cd54` |
| `src/demo-factory/manifests.ts` | `61123b910189581eec6b785c365d9aef9c6ba4cdfcb757312189e08da6dac083` |

La suite recibida pasa antes de añadir el harness: 106 tests, 31 archivos, cero fallos. [Reporter de baseline](evidence/session-39/baseline-suite-results.json).

## VARIABLE UNDER TEST

Identidad destino de la navegación seleccionada. No se modifica mecanismo de recarga: Family Adventure sigue con navegación SPA; los enlaces genéricos siguen solicitando carga documental para entrar a A. Las variantes de identificador son fixtures en memoria del test, no cambios a manifests productivos.

## FREEZE

App, main, manifests/demo IDs, bootstrap, provider, adapter, artifacts A/B, fixtures, Scenario, DemoScript, ExperienceDefinitions, acciones, guards, checkpoints, Evidence, subjectRefs, evaluación vertical/cross-subject, K y claim permanecen byte-idénticos. También GuestPerspective, Supervision, framing H32, resultados H33–H35, reducciones H37, branding, assets, copy, CSS, contratos, package/lock, configuración, lectores históricos y todos los harnesses recibidos.

El [control de preservación](evidence/session-39/preservation-check.json) compara todos los archivos recibidos. La salida `dist` se regenera por build y no se presenta como delta de fuente.

## DELTA OR STOP

STOP: la premisa B→A no se reproduce y la identidad B ya se conserva. PRODUCT DELTA NONE; no hay patch productivo que acreditar. No se añade prop a Home, relación de navegación, campo de manifest, registry, rama por ID ni abstracción de routing.

Durante la ejecución S39 se añadieron exclusivamente [el harness de evidencia H39](../prototype/src/demo-factory/effective-composition-navigation-h39.test.tsx), este documento y el directorio de evidencia S39. Siete tests: cuatro composiciones, dos renombrados estructurales y preservación de los 640 archivos recibidos. La consolidación posterior solo edita este informe.

## A CONTROL

Runtime y query A antes/después; target A. «Búsqueda del tesoro» no está en el DOM de aventura. «Mi aventura» mantiene el mismo objeto runtime y provider, sin llamadas a reset ni acciones añadidas por navegar.

Se ejecutan dos acciones públicas para obtener una pista y Activity no vacía, se vuelve a pulsar el enlace y se hace Actividad→Mi aventura. Checkpoint `clue-a-discovered`, snapshot completo, copy de jardín/fuente y marca Aurora permanecen. Así no se confunde un reinicio silencioso con una composición inicial aparentemente igual.

## B / COSTA CONTROL

Runtime/query/target B en todos los puntos. Mismo provider y snapshot tras cada clic, cero resets y cero acciones provocadas por navegar. Tras una pista y el recorrido por Actividad siguen Costa Clara Resort, Inés/Mateo, framing mirador/patio y el checkpoint acumulado.

No aparece URL A con runtime B ni runtime A silencioso. Las mismas assertions estructurales sirven para A, B y los renombrados; no hay una rama productiva Costa. No se fabrica el problema suprimiendo GuestPerspective de B ni cambiando guards.

## RETAIL CONTROL

Estado inicial R, Home genérica Convercus/Alex, sin GuestPerspective. El enlace fijo solicita A con recarga documental. El clic llega a ese límite sin interceptación de React Router; el bootstrap explícitamente modelado resuelve A con provider nuevo. El provider R no se altera por el clic interceptado.

Se conserva la distinción entre entrar a una aventura y permanecer dentro de una aventura. No se cambia el target genérico a R. La recarga nativa de navegador sigue sin verificarse en esta sesión.

## ARRIVAL CONTROL

Estado inicial H, Aurora Stay/Lucía y checkpoint `pre-arrival-confirmed`, sin GuestPerspective. La entrada seleccionada sigue apuntando a A. La reconstrucción explícita de la recarga produce Family Adventure A en `ready` con provider nuevo, no Arrival convertido por navegación SPA. Misma cualificación de recarga nativa que Retail.

## NO-SPECIAL-CASE CONTROL

En dos catálogos clonados en memoria se renombra únicamente la clave del manifest y `manifest.demoId`: A→`h39-opaque-composition-x`, B→`h39-opaque-composition-y`. Se elimina la entrada antigua en cada catálogo; artifacts y rol estructural permanecen iguales.

Target, query y runtime siguen cada identidad nueva durante los tres recorridos, con provider/estado conservados. No hay lista A/B/Costa/Aurora en el código productivo para el target de «Mi aventura». El literal A de la entrada genérica cumple otra función y no se elimina. Estos fixtures no prueban demos arbitrarias ni IDs con cualquier sintaxis.

## CURRENT / HISTORICAL EVIDENCE INTEGRITY

La inspección previa detecta el conflicto potencial: H37 compara el hash de App actual con S37 y H38 exige preservación de fuentes recibidas. Un delta App real no permitiría ejecutar esos chequeos sin una autorización exacta o una transición histórica explícita. No se oculta esa presión mediante rebaseline, exclusión, skip, reader alternativo ni expectativas modificadas.

Como el gate pre-delta exige STOP, no procede elegir A o B para autorizar una modificación inexistente: se conserva el mecanismo actual completo. H37 continúa importando App/provider/evaluadores actuales y leyendo bytes con `node:fs` nativo; no pasa a replay histórico. H38 conserva todas sus assertions. Se preservan baselines, informes y trazas S37/S38.

[Nueva traza current H37](evidence/session-39/current-cumulative-trace.json): 14 recorridos, 77 frames, 231 capturas DOM, 16 controles de rechazo y seis observaciones aisladas. La comparación contra `session-38/current-cumulative-trace.json` excluye solo `recordedAt` superior: cero campos restantes distintos, incluidos hashes y resultados semánticos.

La suite completa ejecuta también los replays heredados. H21 PASS sigue significando reproducción de su FALSIFIED. H36 conserva su FALSIFIED documental; no se inventa un test H36 independiente. No se promueve la regla experimental S38 ni se declara resuelto el mantenimiento general de replay.

La preservación de hashes, lectores, trazas y harnesses acredita integridad de comprobación dentro de su alcance: es evidencia de infraestructura de test/replay. No acredita por sí misma semántica de producto, UX, aceptación comercial, navegador real, integración real ni comportamiento de demos arbitrarias. La evidencia de producto procede de las observaciones discriminantes ejecutadas, con sus cualificaciones; la regla S38 permanece LOCAL / EXPERIMENTAL / NOT PROMOTED.

## BROWSER / HUMAN INSPECTION

NOT EXECUTED / TOOL UNAVAILABLE en la ejecución S39. Según el [registro y protocolo no ejecutado](evidence/session-39/browser-inspection.md), entonces se leyó la habilidad `browser:control-in-app-browser` y su módulo estaba instalado, pero la herramienta de ejecución requerida no estaba expuesta. Esta consolidación conserva ese resultado y no realiza una inspección nueva.

No se produjo inspección manual local A/B ni smoke visual Retail/Arrival. Los clics jsdom sí se ejecutaron, con la limitación explícita de recarga genérica. No se llama «humana» a una inspección del agente ni se confunde DOM con fidelidad visual, aceptación comercial, `/showcase`, Safari/iOS o dispositivo real.

Esta limitación bloquea afirmar validación en navegador, no la conclusión pre-delta acotada: la rama fija no es alcanzable con la GuestPerspective de A/B y el equivalente actual conserva la identidad en las ejecuciones realizadas. Por ello no se convierte el STOP fundamentado en un fracaso semántico ni se implementa un delta para compensar la falta de navegador.

## VERIFICATION RESULTS — EXECUTION 2026-09-22

Resultados registrados durante S39, conservados sin reejecución en la consolidación documental.

| Comprobación | Resultado / evidencia |
| --- | --- |
| Suite recibida | 106 PASS / 0 FAIL, 31 archivos; [JSON](evidence/session-39/baseline-suite-results.json) |
| Matriz y controles H39 | 7 PASS / 0 FAIL; [JSON final](evidence/session-39/navigation-final-results.json) |
| H37 actual separado | PASS, assertions heredadas intactas; [JSON](evidence/session-39/current-h37-results.json) |
| Suite final completa | 113 PASS / 0 FAIL, 32 archivos; [JSON final](evidence/session-39/full-suite-final-results.json) |
| Typecheck | PASS; [comando](evidence/session-39/typecheck-final-command.json) |
| Lint final | PASS; [comando](evidence/session-39/lint-final-command.json) |
| Build final | PASS; [log](evidence/session-39/build-final.log) |
| Fuentes recibidas | 640/640 byte-idénticas; [preservación](evidence/session-39/preservation-check.json) |
| Navegador / aceptación humana | NOT EXECUTED, herramienta no disponible |

El primer lint señaló un tipo importado sin usar en el **nuevo** harness H39. Se utilizó ese tipo para anotar el parámetro de catálogo, sin cambiar comportamiento ni assertions. Se conservan [fallo inicial](evidence/session-39/lint.log), primera matriz, suite inicial y nuevas ejecuciones finales; no se sobrescribió evidencia para ocultarlo.

Entorno: Node oficial `v24.14.0`, darwin-arm64, `/private/tmp/node-v24.14.0-darwin-arm64/bin/node`; satisface `engines >=24`. Dependencias existentes: cero instalaciones, cero cambios package/lock, config, workers o timeouts. Cada ejecución tiene log y archivo `*-command.json` con argumentos, timestamps y exit code. No se acredita instalación limpia ni portabilidad adicional.

## OBSERVATION CLASSIFICATION

| Observación | Clase | Consecuencia |
| --- | --- | --- |
| El literal A existe, pero no se renderiza en Home A/B | BLOCKER del delta propuesto: falta la premisa que lo autoriza | STOP; ninguna reparación |
| Herramienta de navegador ausente | BLOCKER de inspección visual/humana; no del diagnóstico acotado con fuente y DOM | No reclamar validación browser; protocolo no ejecutado |
| R/H entran intencionalmente en A | NON-BLOCKING / comportamiento heredado | Preservar, no cambiar a demoId propio |
| Un futuro cambio de App chocaría con hashes H37/H38 | NON-BLOCKING en este STOP / FOLLOW-UP observado | No adaptar infraestructura anticipadamente |
| Otras rutas, IDs arbitrarios, URL sin query y modelo general de navegación | OUT-OF-SCOPE | No ensayar como presión alternativa ni corregir |
| Portabilidad de assets/paths, toolchain y coste de replay heredados | FOLLOW-UP observado, no seleccionado | Mantener cualificaciones S38 |

## FALSIFICATION ANALYSIS — P39 / H39 SEPARATION

| Falsador / gate | Evidencia |
| --- | --- |
| P39: B ya conserva identidad; problema supuesto no reproducible | P39 falsada: href/query/runtime B, provider y estado preservados; STOP obligatorio. Esta observación respalda H39 dentro del alcance ejecutado. |
| URL A con runtime B, o runtime cambiado a A | No observado en controles A/B |
| Necesidad de nueva relación semántica/manifest | No observada; no se diseña ninguna |
| Dependencia productiva de ID Costa/A/brand/scenario para el target seleccionado | No observada; renombrados estructurales pasan |
| Alteración del comportamiento Retail/Arrival | Ningún delta productivo; entrada a A preservada, recarga modelada con límite declarado |
| Debilitamiento histórico para lograr PASS | No: hashes/assertions intactos, comparación current H37 sin diferencias materiales |
| Entorno impide separar responsablemente el resultado | No para el STOP pre-delta; sí impide afirmar inspección visual nativa |

P39 queda falsada porque el comportamiento ya existente contradice el desvío supuesto y la necesidad de repararlo. H39 queda respaldada con cualificaciones porque las observaciones muestran la suficiencia local de la identidad efectiva sin nueva relación. Los siete PASS no se convierten en una implementación nueva ni en validación universal.

## P39 VERDICT

FALSIFIED / NOT REPRODUCED. En el alcance inspeccionado y ejecutado, B conserva B mediante la superficie Family Adventure seleccionada; el supuesto B→A que habría justificado una reparación no se reproduce. Este resultado exige STOP PRE-DELTA.

## H39 VERDICT

SUPPORTED WITH QUALIFICATION. La identidad efectiva existente basta para conservar A→A y B→B en «Mi aventura», con provider y estado preservados en App / BrowserRouter / jsdom para los recorridos ensayados. No hace falta una nueva relación de navegación para resolver el supuesto problema seleccionado.

Retail/Arrival conservan su entrada a A y la reconstrucción de bootstrap fue verificada en el harness; su recarga documental nativa no fue ejecutada. Browser/human inspection permanece NOT EXECUTED. Estas cualificaciones limitan el respaldo a H39 y no revierten el STOP obligatorio de S39. No se acredita una reparación, aceptación comercial ni suficiencia general de routing, ni se abre otra presión para sustituir la seleccionada.

## PRODUCT CONSEQUENCE

NONE. App y todas las fuentes productivas permanecen recibidas. La ejecución añadió evidencia y el harness diagnóstico H39; esta consolidación solo modifica el informe. NAVIGATION RELATION DELTA → NONE: no `navigationTarget`, `navigationCompositionRef`, campo de manifest, routing registry, demo nueva, tabla A/B, branch Costa, abstracción genérica de routing ni props sin necesidad demostrada. La ausencia de necesidad demostrada conserva NO NEW RELATION.

## SEMANTIC CONSEQUENCE

NONE. TES, PSC, PSC-P01, Evidence, atribución, sujetos, evaluación, K, claim y reducciones H37 intactos. PSC-P02 NOT CREATED. No se resuelven ni reinterpretan presiones viewer/actor, cuenta→ejecución o segunda persona.

## ARCHITECTURAL CONSEQUENCE

NONE. Architecture v0.5 y ADR-001–005 unchanged. No ownership nuevo, relación experimental nueva, refactor de bootstrap o navegación general. `demoId` conserva su papel local observado, sin promoción universal.

## PROMOTION GATE STATUS

CLOSED / NOT PROMOTED. Ninguna promoción arquitectónica, semántica, de demo comercial ni de gobierno de evidencia. Costa continúa experimental. La integridad S38 conserva su estatuto local/experimental.

## WHAT S39 ACTUALLY ESTABLISHES

### DEMONSTRATED / SUPPORTED WITHIN TESTED SCOPE

- A conserva A y B conserva B en la navegación Family Adventure ensayada; la identidad efectiva existente es suficiente para ese comportamiento.
- El estado y el provider se conservan en los recorridos A/B del harness: Home inicial, Home con progreso y Actividad→Mi aventura. Checkpoints, snapshots completos y contenido situado distinguen continuidad de un reinicio silencioso; una pantalla inicial igual no probaría una sesión conservada.
- No se necesita una nueva relación de navegación para resolver el supuesto problema seleccionado. No hay evidencia de un branch productivo especial Costa para esa navegación.

### FALSIFIED

- P39: B actualmente cae hacia A mediante la superficie Family Adventure seleccionada.
- La necesidad de reparar ese supuesto B→A en S39.

### QUALIFIED

- Retail/Arrival mantienen su entrada histórica a A; la reconstrucción de bootstrap se verificó en el harness y la recarga documental nativa no se ejecutó.
- Los dos renombrados estructurales respaldan la ausencia de special-case dentro de las perturbaciones ensayadas; no acreditan generación arbitraria universal.
- Browser/human inspection permanece NOT EXECUTED / TOOL UNAVAILABLE en S39; no se declara UX aceptada. Costa B sigue EXPERIMENTAL COMPOSITION / NOT COMMERCIAL DEMO ACCEPTANCE.

### UNKNOWN / NOT PROVEN

No prueba routing general, generación arbitraria de demos, IDs de cualquier sintaxis, comercialidad de Costa, comportamiento completo en navegador nativo, fidelidad visual, Safari/iOS, teléfono real, PWA, accesibilidad completa, navegación production-grade, API/auth real, identidad viewer/actor, cuenta→ejecución, reconocimiento de Event TES, resolución PSC-P01, duplicación de K, terminología diagnóstica, segunda persona ni portabilidad universal de replay. Tampoco prueba una recarga documental nativa de Retail/Arrival en un navegador de esta sesión.

## DEMO-CONSTRUCTION ORIENTATION — LOCAL / NOT PROMOTED

El objetivo operativo de Convercus Demo Factory es crear demos útiles y someterlas cuanto antes a interacción y crítica real. La búsqueda preventiva de presiones no debe convertirse en un fin en sí mismo. A partir de este cierre, una presión observada no es un bloqueo automático para construir una demo.

Una presión abierta debe impedir avanzar solo cuando exista evidencia razonable de que puede comprometer materialmente alguna de las garantías necesarias para la demo concreta:

- Validez semántica.
- Identidad de composición.
- Integridad de estado.
- Integridad de Evidence o de atribución.
- Reproducibilidad requerida por esa demo.
- El recorrido UX que realmente se va a evaluar.

Las restantes presiones pueden permanecer OPEN / OBSERVED / QUALIFIED / NOT BLOCKING y someterse a presión cuando una demo concreta las alcance. No se resuelven preventivamente todas las necesidades posibles de producto antes de permitir nuevas demos. Esta orientación no declara que todas las presiones heredadas sean inocuas ni resuelve si existe un bloqueo material para una demo aún no elegida.

### DEMO CONSTRUCTION AS EVIDENCE GENERATION

Construir y utilizar una demo puede ser un instrumento experimental. Esta orientación queda registrada sin promoción a ADR y con dos superficies de observación diferenciadas.

DEMO-AUTHOR UX — FUTURE OBSERVATION SURFACE. Desde la perspectiva del creador se podrá observar qué necesita configurar, qué puede reutilizar o debe duplicar, qué dependencias aparecen, qué exige tocar código y qué resulta innecesariamente difícil. También qué relaciones faltan realmente, si los artefactos son comprensibles, dónde hay ambigüedad de ownership y cuánto esfuerzo requiere pasar de intención a composición ejecutable. Es evidencia de UX de creación/configuración; no acredita automáticamente UX del participante.

PARTICIPANT / RECIPIENT UX — FUTURE OBSERVATION SURFACE. El recorrido visible permitirá examinar comprensión inicial, orientación, affordances, secuencia, feedback, continuidad, estados y lenguaje; reconocimiento de consecuencias, errores y recuperación; coherencia narrativa, carga cognitiva, percepción de valor y credibilidad. Es evidencia de UX de uso/experiencia; no constituye automáticamente aceptación comercial ni autoridad semántica.

DEMO-AUTHOR UX != PARTICIPANT UX, aunque una misma demo pueda producir evidencia para ambas. S39 no ejecutó ni acredita estas observaciones futuras.

### SAFE TO BUILD

SAFE TO BUILD no significa que todas las preguntas abiertas estén resueltas. Significa que las preguntas pendientes no invalidan el experimento que la demo se dispone a realizar. No se debe bloquear una demo por problemas que su propio uso pueda revelar o falsificar de manera más informativa, siempre que se conserven las garantías materiales anteriores.

La secuencia preferida es:

```text
small demonstrable composition
→ human interaction
→ observed UX pressure
→ bounded hypothesis
→ experiment
```

No se exige enumerar y resolver toda presión concebible antes de exponer una demo. Construir demos conserva el rigor experimental, la trazabilidad y las fronteras semánticas acumuladas durante S01–S39.

## CONSTRUCTION BASELINE / NEXT-PHASE DECISIONS

El punto de partida documental sigue siendo [demo-construction-baseline-after-session-38.md](demo-construction-baseline-after-session-38.md), preservado byte a byte. Este cierre lo actualiza conceptualmente con el alcance de navegación demostrado por S39 y la orientación anterior; no modifica la recapitulación ni la baseline congelada.

La fase posterior deberá elegir explícitamente destinatario, objetivo narrativo, composición inicial, recorrido que se quiere enseñar, contenido permitido, capacidades necesarias y criterios de UX que se quieren desafiar. Estas decisiones no implican por sí mismas una nueva construcción arquitectónica: se reutiliza primero lo demostrado y se experimenta cuando la demo requiera capacidad nueva o produzca una presión material.

Este cierre no toma esas decisiones. El paso posterior deberá determinar si un bloqueo material todavía impide construir una demo o si un ciclo concreto de construcción/uso es ya el siguiente experimento más seguro e informativo. «Crear demos» tampoco se convierte automáticamente en H40.

## REMAINING PRESSURES

Se mantienen las observaciones heredadas como OBSERVED BUT NOT SELECTED: inspección en navegador, navegación genérica, infraestructura histórica, límites ambientales, segunda persona, viewer/actor, cuenta, terminología y duplicación de K, entre otras. La discrepancia entre el supuesto de entrada y el flujo actual no autoriza buscar otro defecto ni extender el alcance de esta consolidación. Una eventual inspección visual sigue no ejecutada.

OPEN PRESSURE != BLOCKING PRESSURE. Su posible carácter bloqueante deberá justificarse frente a la demo concreta y las garantías que ésta requiera; esta consolidación no selecciona una de esas presiones ni decide el siguiente experimento. H40 → NOT OPENED.

## DOCUMENTARY CONSOLIDATION VERIFICATION — 2026-09-23

La comparación SHA-256 antes/después de los 681 archivos materiales inventariados encuentra un único cambio: este informe; los otros 680 permanecen byte-idénticos. Además, los 640 archivos de la baseline archivada S39 siguen coincidiendo con sus hashes originales. Los 39 archivos de evidencia experimental S39 y su harness se conservan sin cambios, al igual que los informes y la evidencia material S37/S38 y la base de construcción post-S38. No hay adiciones ni eliminaciones materiales.

El inventario de esta comprobación deja fuera dependencias (`node_modules`), salida regenerable (`dist`) y `.git`; registra aparte 12 archivos Finder `.DS_Store`. Se observaron variaciones ambientales en esa metadata, cuyos archivos no fueron editados por esta intervención. No se cambia la clasificación de ninguna baseline histórica.

Se contrastaron el cierre y sus enlaces con los resultados JSON ya archivados. No se reejecutaron el experimento, la suite, typecheck, lint o build ni se regeneró evidencia. Esta comprobación documental acredita preservación de archivos; no añade evidencia de comportamiento, semántica o UX.

## FINAL METHODOLOGICAL GUARDRAIL

```text
problem assumption != experimental hypothesis
test PASS != hypothesis automatically supported
historical PASS != historical verdict rewrite
historical replay != current verification
current green execution != historical verdict rewrite
source literal != reachable behavior
source inspection != DOM execution
DOM execution != browser visual verification
jsdom reconstruction != native browser document reload
browser validation != human UX acceptance
human UX acceptance != real device verification
test/replay infrastructure evidence != product / semantic evidence
experimental composition != commercial demo
open pressure != blocking pressure
unknown capability != required capability
missing generalization != permission to generalize
safe to build != everything solved
demo construction != abandonment of experimental rigor
demo-author UX != participant UX
UX observation != semantic authority
```

La factoría queda orientada a cambiar de régimen cuando sea seguro: de presión arquitectónica predominantemente preventiva hacia construir → experimentar la demo → cuestionar → observar → falsar → refinar. Esta orientación no altera los veredictos históricos ni promueve capacidades desconocidas.

## FINAL STATUS MATRIX

| Dimensión | Estado |
| --- | --- |
| SESSION 39 | CLOSED / STOP PRE-DELTA |
| P39 — Problem assumption: B navega actualmente a A en la superficie Family Adventure seleccionada | FALSIFIED / NOT REPRODUCED |
| H39 — La identidad efectiva existente basta para conservar A→A y B→B sin nueva relación en esa superficie | SUPPORTED WITH QUALIFICATION |
| NO-NEW-NAVIGATION-RELATION | LOCALLY SUFFICIENT / EVIDENCE-BACKED FOR THE TESTED SURFACE / NOT PROMOTED |
| A / B CURRENT NAVIGATION | A→A / B→B VERIFIED en App / BrowserRouter / jsdom; estado/provider conservados en los recorridos ensayados, iniciales y con progreso |
| RETAIL / ARRIVAL | EXISTING ENTRY TO A PRESERVED / BOOTSTRAP RECONSTRUCTION VERIFIED IN HARNESS / NATIVE DOCUMENT RELOAD NOT EXECUTED |
| No-special-case | Dos identidades renombradas en memoria PASS; alcance limitado a esas perturbaciones |
| PRODUCT DELTA | NONE |
| SEMANTIC DELTA | NONE |
| ARCHITECTURAL DELTA | NONE |
| NAVIGATION RELATION DELTA | NONE |
| ADR / TES / PSC delta | NONE |
| H37 | SUPPORTED WITH QUALIFICATION / CURRENT CUMULATIVE VERIFICATION PRESERVED; traza material igual a S38 |
| H21 / H36 | HISTORICALLY FALSIFIED / PRESERVED |
| HISTORICAL / CURRENT SEPARATION | PRESERVED |
| Historical assertions / evidence | UNCHANGED |
| Suite / typecheck / lint / build — ejecución S39 | 113 PASS / PASS / PASS / PASS; no reejecutados en la consolidación |
| Browser / human inspection | NOT EXECUTED / TOOL UNAVAILABLE |
| COSTA | EXPERIMENTAL COMPOSITION / NOT COMMERCIAL DEMO ACCEPTANCE |
| PSC-P01 | OPEN / UNCHANGED |
| PSC-P02 | NOT CREATED |
| S38 EVIDENCE RULE | LOCAL / EXPERIMENTAL / NOT PROMOTED |
| DEMO-CONSTRUCTION ORIENTATION | ADVANCE AS SOON AS SAFE / OPEN PRESSURE != AUTOMATIC BLOCKER; orientación sin promoción a ADR |
| DEMO AUTHOR UX | FUTURE OBSERVATION SURFACE |
| PARTICIPANT / RECIPIENT UX | FUTURE OBSERVATION SURFACE |
| NEXT MATERIAL PRESSURE | OBSERVED BUT NOT SELECTED |
| H40 | NOT OPENED |

NEXT MATERIAL PRESSURE → OBSERVED BUT NOT SELECTED

H40 → NOT OPENED
