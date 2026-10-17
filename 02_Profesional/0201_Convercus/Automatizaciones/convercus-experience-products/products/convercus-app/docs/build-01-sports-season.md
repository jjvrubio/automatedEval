# BUILD 01 — Sports Season / Carrera / Captación

Fecha: 2026-09-23. LOCAL / EXPERIMENTAL / REVERSIBLE / NOT PROMOTED. Construcción situada autorizada, sin H40.

La demo está disponible en [Sports Season / Brisa Sport](http://127.0.0.1:4173/?demo=sports-season-running) mientras siga activo el servidor local. Ejecuta inscripción con modalidad elegida, check-in simulado, esfuerzo autodeclarado, insignia individual explicada e invitación al club. La persona permanece externa. Participante y Marketing/CRM consumen el mismo estado.

**Resultado:** recorrido utilizable para desafío humano, sin aceptación de UX o comercial. Hay una cualificación de verificación importante: los 17 tests nuevos pasan; la suite completa da 112 PASS / 18 FAIL porque 18 controles históricos comparan los bytes actuales con fuentes anteriores al delta. Esos fallos se han ejecutado, clasificado y conservado; no se han desactivado controles ni cambiado expectativas.

## A. Pre-build gate

Fuentes aplicadas: [Demo Definition v0.2](../../../Demo%20definition%20v_0_2.md), [SAFE-TO-BUILD review](sports-season-safe-to-build-review.md), [smallest buildable slice](sports-season-smallest-buildable-slice.md), Architecture v0.5/ADR-001–005 y evidencia S01–S39. La [instrucción BUILD recibida](evidence/build-01/build-instruction.md) se conserva como input.

v0.2 mantiene un rótulo antiguo «decisión todavía no cerrada» en §10, pero su declaración de delta y §29 cierran Carrera y check-in simulado, igual que BUILD 01. Se ha seguido esa decisión explícita sin modificar la definición ni subsanar sus repeticiones editoriales.

| Aspecto | Hecho de esta ejecución |
| --- | --- |
| Problema recibido | Codex Node rechazaba el binding nativo de Rolldown por Team ID mismatch |
| Intervención | Descarga de Node oficial 24.14.0 arm64 en /tmp y verificación SHA-256 contra SHASUMS256.txt oficial |
| Binario usado | /private/tmp/node-v24.14.0-darwin-arm64/bin/node |
| Node / arquitectura | v24.14.0 / arm64 |
| Dependencias | node_modules existente; package.json, package-lock.json y framework de tests intactos |
| CWD | products/convercus-app/prototype dentro del proyecto recibido |
| Baseline antes de delta | 113 PASS / 0 FAIL; exit code 0; tests ejecutables |
| Producto antes de gate | Sin modificaciones; se había capturado el working tree recibido |

Comando de baseline:

```sh
/private/tmp/node-v24.14.0-darwin-arm64/bin/node node_modules/vitest/vitest.mjs run --no-file-parallelism --reporter=json --outputFile=../docs/evidence/build-01/baseline-suite.json
```

Se eliminaron del entorno de ejecución las variables de grabación Hxx para evitar regenerar trazas históricas. Esto no desactiva assertions ni suites. [Entorno, comando absoluto y exit code](evidence/build-01/pre-build-gate.json), [reporter baseline](evidence/build-01/baseline-suite.json), [inventario recibido](evidence/build-01/received-baseline.json) y [fuentes previas archivadas](evidence/build-01/pre-build-sources.tar.gz).

La descarga inicial dentro del sandbox falló por resolución DNS; la descarga de los mismos archivos oficiales con acceso de red autorizado funcionó. El servidor local requirió permiso para escuchar en 127.0.0.1. Ninguna de estas intervenciones cambió código para resolver el entorno.

## B. Delta implementado, archivo por archivo

Cinco archivos productivos recibidos modificados y ocho archivos nuevos de producto/tests. El [patch contra el estado recibido](evidence/build-01/product-delta.patch) distingue este trabajo de cambios ajenos anteriores; no usa HEAD como baseline.

| Archivo | Qué cambió / por qué lo exige el corte | Estatuto |
| --- | --- | --- |
| [contracts.ts](../prototype/src/demo-factory/contracts.ts) | Selector opcional sportsSeasonRef en DemoManifest. Conserva contratos de miembro/hotel; no inserta una persona externa en MemberReadModel. | Extensión técnica local |
| [manifests.ts](../prototype/src/demo-factory/manifests.ts) | Registra una composición deportiva con referencias propias. Las cuatro identidades previas se conservan. | Reutiliza catálogo declarativo |
| [bootstrap.ts](../prototype/src/demo-factory/bootstrap.ts) | resolveAppDemo resuelve referencia deportiva, marca, compatibilidad y capabilities simuladas; delega las demás composiciones al resolveDemo existente. | Composición efectiva; una extensión local, no registry general de providers |
| [main.tsx](../prototype/src/main.tsx) | Consume resolveAppDemo y entrega resultado a DemoApp; aplica favicon de marca en la composición deportiva. | Entrada compartida reutilizada |
| [App.tsx](../prototype/src/app/App.tsx) | DemoApp consume la composición resuelta y presenta SportsSeasonApp o App heredada. La firma y el cuerpo de App para las composiciones anteriores se conservan. | Consumidor pequeño; sin reglas, fixtures ni selección de proveedor en React |
| [sports contracts](../prototype/src/demo-factory/sports-season/contracts.ts) — nuevo | Persona/membership, Scenario deportivo, inscripción, dos Evidence, insignia, oportunidad, acciones y snapshot locales. | Construcción de producto, no TES |
| [sports artifacts](../prototype/src/demo-factory/sports-season/artifacts.ts) — nuevo | Brisa Sport, temporada, Carrera/Vela/Vóley, Lea externa, Diego miembro de contraste, modalidades/esfuerzos, badge/copy/club y manifest. | Datos ficticios situados |
| [sports runtime](../prototype/src/demo-factory/sports-season/runtime.ts) — nuevo | Valida acciones, guarda registros separados, aplica una regla local, proyecta oportunidad, clona snapshots y resetea. | Código situado; no copia de MockDataAdapter ni K |
| [logo Brisa](../prototype/src/demo-factory/sports-season/brisa-logo.svg) — nuevo | Marca ficticia en cabecera y favicon. | Asset local sencillo |
| [SportsSeasonApp.tsx](../prototype/src/app/SportsSeasonApp.tsx) — nuevo | Captura elecciones, solicita acciones y renderiza las dos perspectivas, insignia, motivo, invitación, errores y reset. | Interfaz situada |
| [sports-season.css](../prototype/src/styles/sports-season.css) — nuevo | Presentación legible en escritorio/móvil, estilos limitados a la superficie deportiva. | Interfaz; global.css recibido intacto |
| [runtime.test.ts](../prototype/src/demo-factory/sports-season/runtime.test.ts) — nuevo | 16 tests: seis combinaciones modalidad/esfuerzo y controles de hechos, atribución, errores, reset, composición y aislamiento R/H/A/B. | Evidencia nueva |
| [ui.test.tsx](../prototype/src/demo-factory/sports-season/ui.test.tsx) — nuevo | Un recorrido DOM del consumidor actual: selección real, rechazos, reconocimiento, invitación, cambio de perspectiva y reset. | Evidencia nueva; no aceptación humana |

El Scenario deportivo usa un shape local que no requiere Experience ni contextos hoteleros. El shape heredado permanece intacto para sus consumidores. No se creó una Experience falsa ni se renombró Desafío Activo/Family Adventure. El comportamiento deportivo no importa su evaluador, K o premise.

No se necesita DemoScript ejecutable en este corte: las elecciones proceden del formulario y cruzan la frontera pública. El guion narrativo reside en contenido situado; no fija silenciosamente modalidad o esfuerzo. La relación modalidad–Experience sigue abierta.

No se construyeron motores generales, editor, plataforma de participantes, autenticación, conversión de membresía ni nuevas relaciones de navegación.

## C. Recorrido ejecutado

La [traza nueva del runtime](evidence/build-01/new-runtime-trace-final.json) conserva estados completos de Social/Bienestar × suave/medio/intenso, con reloj de test fijado. La [traza de navegador](evidence/build-01/browser-final/report.json) conserva la ejecución visible con tiempos reales de recepción de la simulación.

| Input / acción | Estado aceptado | Evidence / regla / resultado | Proyección |
| --- | --- | --- | --- |
| Abrir sports-season-running | Persona Lea, membershipStatus=external; sin inscripción, Evidence, badge ni oportunidad | Datos de fixture; relación como cliente no establecida | Temporada distinta de evento; tres disciplinas; sólo Carrera elegible |
| Elegir Carrera y Social o Bienestar; confirmar | Inscripción con registrationId, personRef, eventRef, selectedModality, status=accepted | No crea presencia ni esfuerzo | Inscripción confirmada y modalidad elegida |
| Simular check-in | Una Evidence de presencia para esa inscripción | source=simulated-check-in, simulation=true, occurredAt y referencias; sin nivel de esfuerzo | Presencia aceptada dentro de la simulación; sin asistencia física acreditada |
| Elegir suave/medio/intenso; registrar esfuerzo | Segunda Evidence independiente | source=participant-self-report; valor recibido; misma persona/evento/inscripción | Esfuerzo autodeclarado y sin medición externa |
| Aplicación de regla por runtime | Una insignia individual | accepted registration + presencia + esfuerzo válido + referencias coincidentes. ruleRef=sports-season:accepted-registration-presence-effort@1 | «Primeros kilómetros», motivo, Evidence refs disponibles en CRM |
| Proyección posterior al badge | Invitación disponible | Oportunidad derivada local, separada del reconocimiento | Conocer Club Brisa; ninguna alta, consentimiento, conversión o envío |
| Participante↔Marketing/CRM | Mismo runtime/proveedor, persona, inscripción, Evidence, badge y oportunidad | Cero acciones de negocio, cero resets por cambiar perspectiva | CRM distingue fixture, registros de la simulación, reconocimiento derivado y oportunidad |
| Reiniciar | Estado inicial recuperado | Se eliminan inscripción, Evidence y badge; oportunidad deja de proyectarse | Persona sigue externa; selección del formulario vacía; las demás demos no cambian |

La insignia guarda badgeId, personRef, eventRef, registrationRef, ruleRef, supportingEvidenceRefs y reason. La elegibilidad no lee copy, Activity, navegación, nombre de persona ni intensidad como jerarquía de valor. Los tres esfuerzos satisfacen la misma condición.

La oportunidad se deriva del reconocimiento en el snapshot; no requiere otro almacén. El reset elimina su fundamento y vuelve a ausencia de oportunidad. La persona es configuración explícita inmutable para la ejecución, no una transición a miembro.

## D. Pruebas: PASS, FAIL y NOT EXECUTED

| Conjunto | Resultado efectivo | Qué acredita / qué no |
| --- | --- | --- |
| PRE-BUILD baseline, antes del delta | **113 PASS / 0 FAIL** | Baseline ejecutable recibida, con sus replays/guards originales |
| Tests nuevos, fuentes finales | **17 PASS / 0 FAIL** | Regla, valores, atribución, fuentes separadas, rechazos, reset, aislamiento y recorrido DOM |
| Suite completa sobre producto final | **112 PASS / 18 FAIL / 0 skipped**; exit 1 | Incluye los 17 tests nuevos y 95 anteriores aprobados; los otros 18 se detienen en guards de hashes antiguos |
| Typecheck final | **PASS**, exit 0 | tsc -b sobre configuración recibida; no cambios a tsconfig |
| Lint final | **PASS**, exit 0 | eslint sobre prototype |
| Build final | **PASS**, exit 0 | Bundle Vite y PWA generados |
| Navegador final | **PASS**, 20 fases | Edge headless, escritorio y móvil; sin overflow horizontal ni errores de página/consola |
| Uso humano, aceptación comercial, dispositivo real | **NOT EXECUTED** | No se infieren desde DOM ni navegador del agente |
| Cuerpos posteriores a los 18 guards históricos fallidos sobre producto nuevo | **NOT EXECUTED** | No se afirma que las fases no alcanzadas de esos tests hayan pasado |

[Comandos/exit codes finales](evidence/build-01/current-checks-final.json), [reporter íntegro](evidence/build-01/current-full-suite-final.json), [clasificación individual de los 18 fallos](evidence/build-01/historical-failure-classification.json), [log de suite](evidence/build-01/full-suite-final.log), [tipos](evidence/build-01/typecheck-final.log), [lint](evidence/build-01/lint-final.log) y [build](evidence/build-01/build-final.log).

Los 18 fallos corresponden a guards de H21, H22, H23, H24, H25, H26, H27, H28, H29, dos harnesses H30, H32, H33, H34, H35, H37, H38 y H39. Todos señalan App.tsx, main.tsx, contracts.ts o manifests.ts modificados intencionalmente. No hay un fallo deportivo oculto bajo esa clasificación. Sus resultados siguen siendo FAIL en el reporter.

Los tests actuales que sí alcanzan comportamiento incluyen bootstrap, aislamiento de provider, proyección, humo de las composiciones previas y las seis pruebas de navegación H39 previas a su guard de preservación. Se conservan alcance y cualificaciones: ningún PASS recrea aceptación comercial de Costa ni convierte H21/H36 en supported.

Las pruebas nuevas comprueban repetición sin duplicación, orden inválido, valores inválidos, persona/evento/inscripción ajenos sin mutación, snapshots aislados, configuración clonada, reset y cambio de copy/nombres sin cambio factual. Las seis combinaciones permiten observar que el nivel de esfuerzo no cambia la elegibilidad.

Durante la implementación hubo un typecheck fallido por ampliar la firma de App utilizada por un harness histórico. Se corrigió mediante el consumidor DemoApp y la firma heredada conservada; no se editó el harness. La primera inspección de navegador terminó en FAIL por favicon.ico ausente después de completar 20 fases; también reveló que el error móvil quedaba fuera de pantalla. [Hallazgos y correcciones acotadas](evidence/build-01/browser-findings.json), [primera evidencia](evidence/build-01/browser-attempt-1/report.json). La pasada final conserva el criterio estricto y pasa, no se debilitaron assertions.

## E. Preservación histórica

[Comparación de preservación](evidence/build-01/historical-preservation.json):

- 697 archivos recibidos inventariados: 685 materiales y 12 de metadata Finder.
- 680 materiales byte-idénticos; cinco fuentes de producto modificadas intencionalmente, con hashes antes/después y bytes anteriores archivados.
- 458 archivos históricos de tests, fixtures, informes, experimentos y evidencia comprobados: **ninguno modificado**.
- Demo Definition v0.2, los dos documentos de readiness, Architecture, ADR, TES, PSC, evaluadores hoteleros, fixtures A/B, package/lock y harnesses históricos permanecen intactos.
- No hay archivos recibidos eliminados ni cambios materiales fuera del delta previsto. Variaciones de siete .DS_Store registradas aparte; no se editan ni se cambia su clasificación en inventarios históricos.

```text
historical replay != current verification
current product changed intentionally
historical evidence NOT rewritten
```

La baseline completa se ejecutó **antes** de modificar producto, con el código recibido. Tras el delta se ejecutó la suite completa sin skips para observar los límites de los guards. No se presentaron hashes históricos como hashes de producto nuevo; no se editaron expectativas, lectores, fuentes archivadas ni baselines para conseguir verde. La copia de fuentes previas y los documentos históricos preservados mantienen la procedencia de aquella ejecución.

La presión de separar mejor replay de verificación actual queda observada. No impide verificar este corte mediante tests nuevos, controles actuales que siguen ejecutándose, tipos/build y navegador. No se arregla esa infraestructura en BUILD 01.

S39 sigue CLOSED / STOP PRE-DELTA; P39 FALSIFIED / NOT REPRODUCED; H39 SUPPORTED WITH QUALIFICATION; NO-NEW-NAVIGATION-RELATION local/not promoted; H21/H36 históricamente falsificadas; H37 conserva su estatuto histórico de verificación acumulada cualificada. Regla S38 local/no promovida y Costa experimental/no aceptada comercialmente. PSC-P01 abierto, PSC-P02 no creado; H40 no abierto.

## F. Demo-Author UX

El [registro separado de autoría](build-01-demo-author-ux.md) clasifica marca, temporada, eventos/fechas, modalidades, persona/membresía, copy, Evidence, regla, insignia, oportunidad y perspectiva CRM, indicando configuración inicial, código requerido, duplicación y fricción.

Hecho principal: la marca y algunos slots de copy se reutilizaron; persona externa, inscripción, inputs, regla y proyecciones deportivas necesitaron programación situada. Ahora se pueden variar sus datos dentro del alcance construido editando artefactos; no existe editor sin código ni soporte arbitrario de modalidades, eventos o reglas.

No se duplicaron App, MockDataAdapter, K ni Family Adventure. Se observó repetición manual de referencias y distribución del copy entre artefactos y componentes, sin diseñar una solución general para mejorar retrospectivamente la autoría.

## G. Browser inspection

La habilidad de navegador se leyó antes de intentar automatización. Esta sesión no expone node_repl js ni herramienta de descubrimiento; no fue posible controlar el navegador integrado. Se utilizó como alternativa **Microsoft Edge instalado, Playwright 1.57.0, modo headless y perfil temporal**, sin sesión personal del usuario.

La [ejecución final](evidence/build-01/browser-final/report.json) recorre diez fases por viewport: inicio, selección/inscripción rechazada por modalidad vacía, inscripción elegida, presencia, rechazo por esfuerzo vacío, insignia, invitación, CRM, retorno a participante y reset. Escritorio: 1280×960, Bienestar/Intenso. Móvil: 390×844, Social/Suave.

Se comprobó que los errores aparecen dentro del viewport sin desplazamiento manual, la procedencia simulada/autodeclarada es visible, Vela/Vóley siguen informativos, la insignia conserva motivo y el cambio de perspectiva conserva datos. No hay overflow horizontal ni errores de página/consola en la ejecución final.

Capturas revisadas visualmente:

- [Inicio escritorio](evidence/build-01/browser-final/desktop-initial.png).
- [Insignia y recorrido móvil](evidence/build-01/browser-final/mobile-badge.png).
- [Marketing/CRM](evidence/build-01/browser-final/desktop-crm.png).
- [Error de inscripción móvil](evidence/build-01/browser-final/mobile-registration-error.png).

Esto es **inspección del agente**, no observación ni aceptación de UX por una persona. Las capturas full-page se hacen desde scroll 0 para evitar artefactos de captura del enlace fijo fuera de viewport; no se ocultan elementos funcionales.

## H. Límites y uso humano

Para probar ahora: abrir la [demo local](http://127.0.0.1:4173/?demo=sports-season-running), elegir Carrera, escoger una modalidad y continuar. «Conocer Club Brisa» sólo muestra información. «Marketing / CRM» cambia la lectura sin actuar en negocio. «Reiniciar demo» permite otro recorrido; recargar también reinicia porque el estado es local en memoria.

Para arrancar en otra sesión, con Node oficial >=24 disponible, desde prototype:

```sh
npm run dev -- --host 127.0.0.1 --port 4173
```

En este entorno se ha dejado Vite activo con el Node temporal verificado. La ruta /tmp puede desaparecer; no se instaló ni sustituyó el Node del sistema.

Queda NOT PROVEN: competición, resultado+posición, trofeos, ranking, segunda participación, booster, TES Progression/Completion/Result, beneficio por recurrencia/acceso anticipado, lógica entre deportes, semántica de equipo/Group/reconocimiento colectivo, QR/asistencia/auth reales, conversión de membresía, CRM/ecommerce/APIs deportivos, no-code, protocolo general y aceptación comercial o de UX.

La persona miembro de contraste es información de diseño, sin acción competitiva ni resultados observados. No hay conexión con sistemas externos ni almacenamiento persistente. El calendario, marca y personas son ficticios.

Las fricciones que se entregan para desafío humano incluyen recorrido móvil largo, ubicación del formulario tras las tres tarjetas, regreso a la parte superior para cambiar de perspectiva y densidad del lenguaje de procedencia. No se rediseña la demo para eliminarlas en este BUILD.

## I. Veredicto

El recorrido funciona, los rechazos son legibles, el reset restaura el estado, la procedencia está visible y no se conoce un atajo semántico que invalide el corte. La cualificación de suite histórica queda explícita y no se confunde con éxito global.

```text
BUILD COMPLETED
→ READY FOR HUMAN UX CHALLENGE
```

No se implementa el siguiente corte, competición, booster o editor. No se abre H40. El siguiente nivel de evidencia requiere que una persona utilice y cuestione lo construido.
