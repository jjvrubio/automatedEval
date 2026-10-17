---
title: "Sesión 38 — Historical Replay Portability and Evidence Integrity"
language: es
date: "2026-09-21"
status: "CLOSED / SUPPORTED WITH QUALIFICATION"
scope: "Infraestructura de evidencia; sin delta de producto, semántica ni arquitectura"
---

# Sesión 38 — Historical Replay Portability and Evidence Integrity

## H37 CONSOLIDATED INPUT

[S37](session-37-activity-attribution-claim-provenance-and-reduction.md) CLOSED / SUPPORTED WITH QUALIFICATION. NO-NEW-RELATION SUFFICIENT para los cuatro textos seleccionados. Claims viewer/actor y cuenta→ejecución retirados; ocurrencia Activity, atribución Evidence y presentación situada H25 preservadas. H36 permanece históricamente FALSIFIED; heurística de reducción EVIDENCE STRENGTHENED / NOT PROMOTED.

Architecture v0.5 ACTIVE; ADR-001–005 ACCEPTED; TES y PSC unchanged. PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE; PSC-P02 NOT CREATED. No se reconstruyen decisiones H21–H37.

## H38 HYPOTHESIS

Separar evidencia histórica material de metadata ambiental incidental permite reproducir los resultados sin reescribir expectativas ni ocultar mutaciones, manteniendo historical replay ≠ current cumulative verification.

Resultado: SUPPORTED WITH QUALIFICATION para la variación de metadatos ensayada. No equivale a portabilidad universal de directorio, plataforma, assets o toolchain.

## INFRASTRUCTURE PRESSURE RECEIVED

S37 cerró con 95 PASS / 3 FAIL en 30 archivos: H21/H22/H23 no alcanzaban sus controles semánticos por ausencia de 00-governance/.DS_Store. La acumulación de copias, imports reubicados, mapas y lectores era una presión independiente.

S38 recupera esos replays y conserva visible el coste general. El resultado final local es 106 PASS / 0 FAIL en 31 archivos; ocho pruebas nuevas corresponden a H38.

## FAILURE REPRODUCTION

Antes de modificar infraestructura se ejecutaron juntos los tres harnesses con Node oficial 24.14.0 arm64. Los tres fallaron por ENOENT sobre la misma ruta. [Log completo](evidence/session-38/failure-reproduction.log).

| Harness recibido | Punto de fallo | Invariante pretendido |
| --- | --- | --- |
| composition-boundary-h21.test.ts | SHA(read(...)), línea 69; enumeración línea 63 | Preservar las fuentes shared/protected al componer B |
| experience-stable-selection-h22.test.ts | SHA(read(...)), línea 59; enumeración línea 52 | Preservar baseline salvo los dos cambios autorizados, comprobados aparte |
| situated-evaluation-context-h23.test.ts | SHA(read(...)), línea 44; enumeración línea 42 | Preservar baseline salvo cinco excepciones originales, también controladas |

La cadena relevante es harness → rutas particulares → historical-read H34:12 → H36:12 → node:fs. No existe ruta archivada para ese .DS_Store; la lectura cae al working tree. El archivo entró por el inventario de preservación, no por una dependencia productiva. ENOENT ocurre antes de comparar el hash y antes del veredicto semántico.

## H21–H23 HISTORICAL INTENT

| Sesión | Hipótesis y variable originales | Fuentes y mecanismo | Conclusión que se conserva |
| --- | --- | --- | --- |
| H21 | Composición B distinta con maquinaria compartida congelada | 55 entradas shared/protected; bytes, composición A/B y perspectivas iniciales | FALSIFIED: B se resuelve, pero la selección por Scenario.id impide sus perspectivas; STOP sin acciones ni reset |
| H22 | Selección estable por Experience | 78 entradas; dos sustituciones Scenario.id→experienceRef, comprobación exacta del adapter y controles positivos/negativos | SUPPORTED WITH QUALIFICATION: ambas fronteras funcionan; contexto Aurora heredado en B sigue observado |
| H23 | Binding situado Scenario.contexts hacia evaluación | 99 entradas; preservación y comparación de cambios autorizados; inputs/resultados efectivos A/B y contradicciones | SUPPORTED WITH QUALIFICATION: contexto situado, Evidence intacta, contradicción sin establecer y separación de autoridad |

Informes, fuentes, baselines y trazas originales se inspeccionaron antes de decidir; la [decisión pre-delta](evidence/session-38/pre-delta-analysis.md) registra el análisis. Quitar la obligación de leer los cinco archivos incidentales no cambia acciones, contextos, perspectivas, inputs/resultados ni los STOP históricos. PASS del harness H21 significa reproducir su FALSIFIED, no convertirlo en una hipótesis apoyada.

## .DS_STORE MATERIALITY ANALYSIS

Clasificación: INCIDENTAL ENVIRONMENT METADATA para cinco rutas concretas. El informe original H21 ya calificaba sus cuatro entradas como «sin significado arquitectónico». Sus hashes se propagaron a H22/H23; H23 añadió prototype/src/.DS_Store. No hay lectura, generación, importación ni interpretación productiva de esos bytes; sólo inventarios y comprobaciones de preservación. Tampoco son inputs de las trazas.

| Rutas auditadas | H21 | H22 | H23 |
| --- | --- | --- | --- |
| 00-governance/.DS_Store | Incidental | Incidental | Incidental |
| 01-semantic-contract/.DS_Store | Incidental | Incidental | Incidental |
| 01-semantic-contract/source-excerpts/.DS_Store | Incidental | Incidental | Incidental |
| 02-shared-contracts/.DS_Store | Incidental | Incidental | Incidental |
| products/convercus-app/prototype/src/.DS_Store | No inventariado | No inventariado | Incidental |

No fueron declaraciones experimentales intencionales según los usos y documentos inspeccionados. Sólo se conservaron hashes, no sus bytes: no se puede atribuir retrospectivamente el proceso creador exacto. La muestra actualmente existente en este Mac tiene cabecera Bud1, propia del formato Finder. Cambiar los bytes históricos habría detenido un chequeo ambiental, pero no habría cambiado los hechos o runtime que acreditaban el veredicto. No se clasifica exclusivamente por nombre.

## MATERIAL EVIDENCE DEFINITION

Es material el contenido o identidad necesario para acreditar fuente productiva, lógica de harness, fixture/manifest/Scenario/Script/Experience/contrato, expectativas factuales o representacionales, evaluación, traza, relación experimental o preservación intencional de una baseline. Los documentos protegidos siguen siendo materiales aunque no se importen en runtime.

El conjunto positivo retiene 51 entradas H21, 74 H22 y 94 H23, incluidos hashes originales y excepciones históricas comprobadas por cada harness. No se crea un contrato de producto.

## INCIDENTAL METADATA ANALYSIS

.DS_Store se trata por las cinco rutas auditadas, no por glob. Thumbs.db, desktop.ini, AppleDouble ._*, temporales de editor y swap no aparecieron en los inventarios/fuentes inspeccionados; no se incorporan a una blacklist.

tsbuildinfo es caché de compilación; dist es salida regenerada; node_modules aporta dependencias de ejecución fijadas por package/lock. Ninguno pertenecía al conjunto H21–H23. Los logs de build declarados como evidencia sí siguen protegidos. No se equipara «generado» a «irrelevante», ni se eliminan archivos del usuario.

## CURRENT REPLAY ARCHITECTURE INVENTORY

[Inventario recibido](evidence/session-38/replay-inventory-before.json): 30 archivos de test; 130 archivos en test-fixtures; 65 copias .txt para comparación de bytes y 47 módulos TypeScript runtime archivados, algunos reexports. Seis helpers de rutas y dos lectores históricos. Los imports se reubican mediante rutas relativas, alias de Vite, reexports y vi.mock local al harness; no mediante un mock global de fs.

| Componente | Entradas | Consumidores principales / propósito |
| --- | --- | --- |
| H24 source-path | 9 | H21–H25: composición previa a presentación H25 |
| H26 source-path | 9 | H23–H27 según harness: preservar selección previa |
| H27 source-path | 3 | H27/H28 |
| H28 source-path | 8 | H23–H29 según harness |
| H29 source-path | 14 | H21–H30 según harness |
| H31 source-path | 16 | H21–H30 y H32 según harness |
| H34 archive-paths / reader | 18 | Lecturas históricas de H21–H35 según imports |
| H36 archive-paths / reader | 7 | Cadena H34 y lectura directa H35; conservar delta H37 |

Total: 84 entradas explícitas, 24 claves lógicas distintas. No incluye condicionales inline particulares H21/H22 ni casos especiales H33/H34: no se anuncia como recuento de toda condición de routing. El inventario conserva rutas, imports, dependencias y variables concretas.

La marca textual historical del inventario detecta 17 archivos, pero H37 sólo compara copias y ejecuta código actual: son 16 harnesses con replay runtime histórico, no 17.

## ROUTING CHAIN ANALYSIS

Cada harness selecciona la cadena correspondiente a su época, no «el archivo más nuevo». Las rutas antiguas se aplican primero; su resultado ya es una ruta de archivo y deja de coincidir con las claves de fuentes actuales de los mapas posteriores. H34 aplica su mapa exacto y encadena H36; H36 aplica el suyo y termina en node:fs. Una ruta no mapeada conserva la lectura original.

Las 84 entradas apuntan a destinos existentes; ningún destino vuelve a ser clave de esos mapas: no se observan ciclos. El orden de lectura no depende de recorrer directorios. El solapamiento entre épocas es intencional y exige mantener el orden explícito.

Las copias pre-S38 añadidas bajo h37 sirven para acreditar el delta de los tres harnesses, no crean nuevas rutas. No hay un «lector S37» ni un «lector S35» universal. Las fechas del directorio no eligen por sí mismas la fuente.

Los lectores heredados comparan rutas léxicamente respecto a process.cwd()/../../..; no canonicalizan symlinks ni Unicode. Los paths de sus mapas son ASCII. Se conservan dos presiones: alias absolutos /var frente a /private/var, y URL absoluta de asset en DOM. Véanse los controles específicos; no se altera la precedencia para ocultarlas.

## HISTORICAL SOURCE / ENVIRONMENT SEPARATION

Las tres baselines mezclaban fuentes intencionales con archivos encontrados al capturar el filesystem. La frontera S38 separa ambos sin reescribir esos inventarios: su JSON íntegro, incluidos los antiguos hashes incidentales, queda byte-idéntico como evidencia de captura.

El selector verifica primero SHA-256 del JSON original y la partición completa path/hash material+incidental. Sólo devuelve el conjunto material para los loops existentes. Ausencia física de metadata incidental no es ausencia de fuente histórica; una entrada desconocida en el inventario sí es error.

## CANDIDATE PORTABILITY STRATEGIES

La [comparación previa](evidence/session-38/pre-delta-analysis.md) valora fidelidad, ocultación, portabilidad, coste, reversibilidad y compatibilidad de las cinco alternativas:

| Estrategia | Decisión |
| --- | --- |
| A. Allowlist material explícita | Adoptada sólo para las tres baselines; positiva, verificable y reversible, a costa de duplicar inventario |
| B. Exclusión incidental explícita | Aporta clasificación individual; no se adopta un filtro general por nombres |
| C. Manifest por raíces/tipos | Positivo, pero exigiría nuevo ownership y podría omitir documentos heredados |
| D. Paquete hermético | Mayor aislamiento potencial; exige closure de imports/runtime y rediseño fuera del alcance |
| E. Captura filesystem íntegra | Conserva acoplamiento ambiental y no resuelve los archivos ausentes |

## STRATEGY DECISION

A acotada, con partición incidental auditada y comportamiento fail-closed. Se conservan hashes de todas las entradas materiales, cuerpos de assertions y allowedChangedFiles originales. La solución no consiste en aceptar cualquier ENOENT ni en ignorar un sufijo.

[Selector](../prototype/src/demo-factory/test-fixtures/h38/material-baseline.ts) y [manifest](../prototype/src/demo-factory/test-fixtures/h38/material-source-set.json). La cobertura futura de otras baselines requiere inspección; no se aplica automáticamente esta clasificación a todo el repositorio.

## MINIMAL INFRASTRUCTURE DELTA GATE

Antes de aplicar cambios reales se instaló el candidato en dos copias temporales. H21/H22/H23 y H37 pasaron con metadata ausente y presente; resultados materiales iguales. Mutar el adapter histórico produjo tres fallos; retirarlo produjo fallos de import/preservación; mutar el adapter actual conservó H21–H23 y falló H37.

[Gate registrado](evidence/session-38/portability-controls.json): PASS antes del delta. No se debilitó ninguna expectativa ni fue necesario cambiar producto. El control inicial de relocalización completa falló por la URL del logo y se conserva; la prueba acotada mantiene ese origen constante.

## BASELINE

[Baseline S38](evidence/session-38/baseline.json): 483 archivos recibidos tras el cierre S37, no HEAD. Metadata actual inventariada aparte; dependencias, cachés, build y nuevos artefactos S38 fuera de esa captura. El worktree ya contenía cambios ajenos, conservados.

El control final distingue exactamente tres archivos heredados modificados y 480 byte-idénticos. La traza final de S37 y sus sourceHashes vinculan además las fuentes productivas a la evidencia de cierre anterior. [Preservación](evidence/session-38/preservation-check.json).

## INFRASTRUCTURE DELTA OR STOP

Tres harnesses: una importación nueva y sustitución de Object.entries(...) por materialBaselineEntries(...). Los cuerpos completos restantes se comparan con sus copias pre-S38, cuyos hashes coinciden con la baseline.

Nuevos archivos de infraestructura: tres copias .txt probatorias, un selector, un manifest y el harness H38 de ocho tests. Cero cambios en mapas existentes, lectores históricos, runner, timeouts, workers, package o lockfile. Scripts, logs y documentos S38 se contabilizan como evidencia, no como producto.

La primera versión del nuevo control de routing confundió el alias temporal /var con el cwd real /private/var. Se conserva el [fallo](evidence/session-38/routing-alias-probe.log); el fixture usa ahora su ruta real para ensayar precedencia y verifica aparte la limitación del alias. No se cambió una expectativa histórica.

## PRODUCT FREEZE

App, contratos, bootstrap, adapter, projectors/evaluation, artifacts A/B, fixtures, manifests y definiciones Scenario/Script/Experience permanecen byte-idénticos a la entrada S37. Lo comprueban el harness H38 sobre 480 archivos y los hashes de la traza actual H37 frente a su cierre anterior.

PRODUCT DELTA NONE. Los assets originales sólo se leen en los controles temporales; no se crean metadatos faltantes en el working tree.

## SEMANTIC FREEZE

Sin cambios en wording H37, GuestPerspective, SupervisionPerspective, Evidence, subjects, session, Experience, evaluación, K ni claim. La selección de archivos de preservación no aporta autoridad semántica. Expectativas y veredictos H21–H37 permanecen congelados.

## H21 CONTROL

Antes: ENOENT ambiental. Después: PASS del mismo experimento, con FALSIFIED histórico, B sin perspectivas iniciales y cero executeAction/reset. Las 51 entradas materiales conservan sus hashes. [Traza](evidence/session-38/controlled-asset-origin/absence-h21.json).

## H22 CONTROL

Antes: ENOENT ambiental. Después: PASS de assertions originales, incluidos cambios exactos de selección y negativos. SUPPORTED WITH QUALIFICATION permanece; no se corrige retrospectivamente el contexto heredado. [Traza](evidence/session-38/controlled-asset-origin/absence-h22.json).

## H23 CONTROL

Antes: ENOENT ambiental. Después: PASS de inputs efectivos A/B, contradicciones y separación de autoridad; Evidence no reescrita. SUPPORTED WITH QUALIFICATION permanece. [Traza](evidence/session-38/controlled-asset-origin/absence-h23.json).

## INCIDENTAL METADATA ABSENCE CONTROL

Entorno A sin ninguno de los cinco archivos incidentales: H21/H22/H23/H37 PASS. Después se ejecutaron los 30 archivos heredados completos: 98 PASS / 0 FAIL. [Matriz completa](evidence/session-38/inherited-environment-matrix.json).

Son copias de fuentes aisladas, no dos máquinas: comparten macOS arm64, Node y dependencias. La primera copia con assets totalmente relocalizados produjo H21–H23 PASS y H37 FAIL en DOM Retail por /@fs/ruta-absoluta/logo.svg. [Fallo preservado](evidence/session-38/absence.log). Portabilidad a una raíz arbitraria OPEN.

## INCIDENTAL METADATA PRESENCE CONTROL

Entorno B: mismos bytes materiales y una muestra Finder preexistente del mismo Mac en las cinco rutas, sólo dentro del fixture temporal. No se reconstruyen hashes históricos ni se fabrica metadata para reparar el proyecto. H21/H22/H23/H37 PASS; suite heredada completa 98 PASS / 0 FAIL.

Las 16 trazas A/B son idénticas salvo su timestamp superior de captura: recordedAt, o capturedAt en H30_MATRIX_PATH. Una comparación inicial olvidó este último nombre y lo señaló; el diff estructural completo conserva las 16 diferencias observadas. No se ignoran occurredAt, DOM, hechos, hashes ni resultados.

Para mantener constante el origen del logo se usa un symlink al asset original. Vite inicialmente lo denegó por su allowlist: [log](evidence/session-38/fixed-asset-origin/absence.log). Un wrapper exclusivo del fixture temporal añade sólo el directorio real de marca a fs.allow. No modifica el config del proyecto, assertions, workers o timeouts. Este aislamiento parcial se declara expresamente: no es un paquete hermético portable.

## MATERIAL CONTENT MUTATION CONTROL

Se añadió un comentario únicamente al adapter archivado H21 dentro del entorno temporal. Los tres replays fallaron por SHA distinto, incluso siendo una mutación sin efecto runtime. [Log](evidence/session-38/controlled-asset-origin/material-mutation.log). Se restauraron los bytes antes del siguiente control. Portabilidad no equivale a laxitud de comparación.

## MATERIAL FILE REMOVAL CONTROL

Se ocultó temporalmente ese mismo archivo: H21/H22 fallaron al resolver import y H23 por ENOENT en preservación. Tres archivos de test fallidos; uno alcanzó una assertion. [Log](evidence/session-38/controlled-asset-origin/material-removal.log). No hubo fallback a una fuente actual ni catch convertido en éxito.

## UNKNOWN FILE CONTROL

Un archivo ambiental desconocido fuera del conjunto material no afectó a H21–H23 ni a sus trazas. Es la política explícita de conjunto positivo, no una omisión accidental.

En cambio, añadir/quitar una entrada del inventario declarado, cambiar su hash o crear una clasificación conflictiva falla en el selector. Un archivo llamado .DS_Store dentro del conjunto material sintético sigue protegido: el nombre no lo exime.

## CURRENT / HISTORICAL SOURCE SEPARATION CONTROL

Mutar sólo src/demo/mock-adapter.ts actual en el fixture conserva H21/H22/H23 PASS y sus trazas; H37 falla por hash del archivo actual, en su línea 59. [Log](evidence/session-38/controlled-asset-origin/current-source-mutation.log). Tras restaurar, ambas suites completas de entorno pasan.

H37 ejecuta App/provider actuales, usa node:fs nativo para su control de bytes y no tiene vi.mock de fuentes históricas. Los archivos archivados sirven como comparación, no como reemplazo runtime. No se interceptó su lector.

## ROUTING SHADOW CONTROL

El nuevo test crea fuente actual, archivo intermedio H31, nuevo H36 y antiguo H24 para artifacts.ts. La composición real H24→H29→H31→reader H34/H36 selecciona OLDER. Lectura directa H36 selecciona NEWER; node:fs selecciona CURRENT. Al retirar OLDER se obtiene ENOENT aunque las alternativas existan.

El experimento adicional de alias registra que una ruta absoluta con /var frente al cwd /private/var puede no coincidir con el mapa y leer CURRENT. Es una limitación real de los lectores heredados, no una garantía: los harnesses inspeccionados construyen las rutas desde su cwd coherente. No se generaliza a clientes arbitrarios de ese helper.

## UNICODE / PATH NORMALIZATION CONTROL

El selector nuevo normaliza identidad lógica POSIX a NFC, rechaza colisiones NFC/NFD, traversal, rutas absolutas y backslash; no convierte mayúsculas/minúsculas. En macOS se escribió un archivo por su nombre NFD y se leyó por NFC, con bytes idénticos, incluso conservando texto descompuesto y CRLF.

Normalizar identidad no normaliza contenido. Los helpers antiguos no cambian: sus claves ASCII no requieren NFC para este experimento. La observación macOS/APFS no certifica Windows/Linux ni todos los sistemas de archivos. [Observaciones H38](evidence/session-38/execution-trace.json).

## NODE ENVIRONMENT OBSERVATION

package.json y README ya declaran Node >=24. S38 ejecutó Node oficial 24.14.0 darwin-arm64 temporal, el mismo validado en S37. El rechazo de firma nativa del Node incluido en Codex se recibe como observación S37; no se atribuye a la semántica ni se repite como fallo nuevo.

NODE TOOLCHAIN DELTA NONE. Dependencias existentes, package.json y lockfile intactos; no se acredita una instalación limpia ni otra plataforma.

## CONCURRENCY / TIMEOUT OBSERVATION

Suite final y ambas condiciones completas utilizaron concurrencia predeterminada de Vitest. Cero timeouts observados. Ejecución serial NOT EXECUTED; cero aumentos de timeout. El H37 separado comprueba current cumulative verification, no es una reparación mediante serialización.

La sensibilidad concurrente observada en S35 sigue siendo antecedente abierto, no una presión resuelta por quitar metadata.

## FULL HISTORICAL REPLAY RESULT

[Log completo](evidence/session-38/full-suite.log), [reporter JSON](evidence/session-38/full-suite-results.json) y [resultado por archivo](evidence/session-38/harness-results.md).

| Sesión / harness histórico | Resultado S38 |
| --- | --- |
| Family Adventure vertical heredado | PASS: 10 tests |
| H21 / composition-boundary | PASS; reproduce FALSIFIED |
| H22 / experience-stable-selection | PASS |
| H23 / situated-evaluation-context | PASS |
| H24 / situated-activity-provenance | PASS |
| H25 / script-bound-activity | PASS |
| H26 / situated-guest-provenance | PASS |
| H27 / explicit-subject-representation | PASS |
| H28 / account-sourced-guest | PASS |
| H29 / operational-subject-status | PASS |
| H30 / pre-delta-position y script-bound-journey | PASS ambos |
| H31 | NOT EXECUTED como test independiente: auditoría, sin harness dedicado; documentos preservados |
| H32 / explicit-introductory-framing | PASS |
| H33 / operational-supervision-subject | PASS |
| H34 / operational-session-subject | PASS |
| H35 / experience-sourced-guest-name | PASS |
| H36 | NOT EXECUTED como test independiente: auditoría, sin harness dedicado; FALSIFIED/documentos preservados |
| H37 actual | PASS; se contabiliza separado del replay histórico |
| H38 infraestructura | PASS: 8 tests |

Todos los 31 archivos disponibles se ejecutaron: 106 PASS, 0 FAIL, 0 pendientes, 0 timeouts. Las dos condiciones temporales ejecutaron todos los 30 archivos heredados, no el nuevo test H38, con 98 PASS cada una. Los estados documentales no se convierten en PASS de tests inexistentes.

## CURRENT CUMULATIVE VERIFICATION

H37 también se ejecutó por separado: PASS. [Traza actual](evidence/session-38/current-cumulative-trace.json): 14 recorridos App, 77 frames, 231 capturas DOM, 16 rechazos y seis observaciones aisladas de transporte de sesión. A/B y regresiones Retail/Arrival ejecutan fuentes actuales.

Typecheck, lint y build PASS. [Comandos y códigos de salida](evidence/session-38/verification-commands.json). No se ejecutó validación visual de navegador, iPhone real, staging o despliegue. Igualdad DOM no implica aceptación visual/comercial.

## EVIDENCE-INTEGRITY MANIFEST

[Regla documental](evidence/session-38/evidence-integrity-manifest.md): TEST INFRASTRUCTURE EVIDENCE RULE / LOCAL / EXPERIMENTAL / NOT PROMOTED.

Bytes: igualdad exacta para fuentes/documentos declarados, copias probatorias y baselines. Imports reubicados y módulos de replay requieren además ejecución de assertions originales; una copia idéntica aislada no prueba comportamiento. La mera existencia no basta para ninguna fuente material del conjunto. Las cinco entradas ambientales conservan su existencia documental, no una obligación de existir físicamente.

## REPLAY MAINTENANCE COST

| Métrica | Antes | Después |
| --- | --- | --- |
| Entradas de mapas/helpers históricos | 84 | 84 |
| Claves lógicas distintas en esos mapas | 24 | 24 |
| Helpers de rutas / lectores históricos | 6 / 2 | 6 / 2 |
| Copias .txt probatorias | 65 | 68 |
| Módulos runtime históricos, excluidos helpers | 47 | 47 |
| Selectores de materialidad S38 | 0 | 1 |
| Archivos en test-fixtures | 130 | 135 |
| Harnesses runtime históricos | 16 | 16 |
| Harnesses heredados adaptados en S38 | 0 | 3 |
| Archivos de test totales | 30 | 31 |

La clasificación positiva añade un manifest de tres baselines y 219 entradas materiales acumuladas, no 219 archivos únicos. Evita que nuevos archivos ambientales se conviertan automáticamente en obligaciones de esos tres replays. No resuelve el crecimiento general de copias/rutas ni gobierna futuras capturas automáticamente.

## TEST-INFRASTRUCTURE PRESSURE RESULT

Metadata portability EXPERIMENTALLY ADDRESSED en el alcance ensayado. Archive routing complexity PRESERVED / OPEN. Toolchain OPEN / NON-BLOCKING con Node oficial. Concurrency OPEN como antecedente / NON-BLOCKING en estas ejecuciones.

Relocalización de assets y alias absolutos: OPEN; bloquean una afirmación más amplia de portabilidad, no la igualdad A/B de metadata demostrada. Infraestructura general MATERIAL / NON-BLOCKING para la base local actual, no «resuelta».

## FALSIFICATION ANALYSIS

| Falsador | Observación |
| --- | --- |
| Metadata material para el veredicto | No: usos/documentación y controles A/B sostienen incidentalidad |
| Se ocultan mutaciones materiales | No: mutación y retirada fallan |
| Se debilitan expectativas históricas | No: cuerpos exactos, hashes originales y trazas materiales iguales |
| Tests actuales consumen archivos archivados | No en callers ensayados: H37 detecta fuente actual mutada |
| Replay histórico consume fuente actual incorrecta | No en callers ensayados; alias absoluto inconsistente constituye límite explícito fuera de ese dominio |
| Requiere fabricar archivos ambientales para pasar | No: el entorno ausente pasa; la presencia sólo es una perturbación de control |
| Requiere cambiar producto/semántica/borrar tests | No |
| Portabilidad arbitraria de raíz | No demostrada: fallo literal del asset conservado, sin relajar DOM |

No se activa un falsador de la separación acotada metadata/material. Una lectura universal de H38 sin condiciones de raíz/toolchain sería excesiva; esos fallos se preservan y no se continúa refactorizando para eliminarlos.

## H38 VERDICT

SUPPORTED WITH QUALIFICATION: las assertions materiales H21–H37 disponibles se reproducen con metadata ausente/presente y mantienen sensibilidad a fuentes materiales. El resultado está limitado al entorno, rutas coherentes y origen de assets documentados. No se proclama portabilidad universal ni hermeticidad completa.

## ARCHITECTURAL CONSEQUENCE

Architecture v0.5 ACTIVE / unchanged; ADR-001–005 ACCEPTED / unchanged. Ningún ADR nuevo, nuevo framework de replay, contrato runtime o ownership productivo. El producto queda congelado.

## SEMANTIC CONSEQUENCE

TES, PSC y PSC-P01 unchanged; PSC-P02 NOT CREATED. Veredictos históricos no reinterpretados. Reparar el instrumento de comprobación no cambia el estatuto semántico de sus resultados.

## PROMOTION GATE STATUS

Regla candidata de evidencia respaldada localmente / NOT PROMOTED. No se consolida como gobierno general del repositorio y no se abre H39.

## WHAT H38 DOES NOT PROVE

No prueba portabilidad Windows/Linux, aislamiento de dependencias, clon limpio ejecutable sin condiciones, root relocation completa, robustez frente a todos los symlinks, ausencia futura de timeouts, coste de mantenimiento sostenible ni fidelidad visual.

No prueba identidad/actor/cuenta, verdad externa de Evidence, integración real, ontología general de Experience o suficiencia universal de las reducciones previas. No convierte Costa B en demo comercial aceptada.

## REMAINING PRESSURES

Se mantienen complejidad de rutas, versión/firma de toolchain, sensibilidad de recursos, URL absoluta de assets y alias de paths. Del producto siguen observadas las presiones anteriores de nombres Activity/GP, affordances de segunda persona/cuenta, navegación histórica, terminología diagnóstica y duplicación literal de K.

La [base recapitulada para preparar demos](demo-construction-baseline-after-session-38.md) separa composiciones ejecutables, invariantes, límites y decisiones todavía pendientes. Es un punto de entrada documental, no una selección de la próxima presión ni una nueva especificación aceptada. NEXT MATERIAL PRESSURE OBSERVED BUT NOT SELECTED.

| Dimensión | Resultado final |
| --- | --- |
| H38 | SUPPORTED WITH QUALIFICATION |
| HISTORICAL REPLAY PORTABILITY | Experimentally supported para metadata; relocalización universal no acreditada |
| .DS_STORE MATERIALITY | INCIDENTAL en cinco rutas auditadas |
| H21 / H22 / H23 REPLAY | PASS / PASS / PASS |
| MATERIAL MUTATION DETECTION | PRESERVED |
| HISTORICAL EXPECTATIONS / PRODUCT SOURCES | UNCHANGED / UNCHANGED |
| HISTORICAL / CURRENT SEPARATION | PRESERVED en callers ensayados |
| METADATA PORTABILITY PRESSURE | EXPERIMENTALLY ADDRESSED |
| ARCHIVE ROUTING COMPLEXITY | OPEN |
| TOOLCHAIN / CONCURRENCY PRESSURE | OPEN / NON-BLOCKING en este entorno |
| TEST-INFRASTRUCTURE PRESSURE | MATERIAL / NON-BLOCKING; no resuelta globalmente |
| CANDIDATE EVIDENCE GOVERNANCE RULE | EVIDENCE-BACKED / NOT PROMOTED |
| NEXT MATERIAL PRESSURE | OBSERVED BUT NOT SELECTED; H39 NOT OPENED |
