---
title: "Sesión 37 — Activity Attribution Claim Provenance and Reduction"
language: es
version: "v1.0"
status: "CLOSED / SUPPORTED WITH QUALIFICATION / NO-NEW-RELATION SUFFICIENT"
date: "2026-09-21"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "experimento local de reducción de afirmaciones de atribución en Activity"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 37 — Activity Attribution Claim Provenance and Reduction

## H36 CONSOLIDATED INPUT

[S36](session-36-presentation-authority-provenance-stratification-audit.md) se recibe CLOSED / H36 FALSIFIED como pretensión exhaustiva de significado compatible. U/D/O/E conservan utilidad parcial y cualificada, sin promoción. DemoScript universal ownership y App semantic authority NOT SUPPORTED. El principio candidato sólo tiene respaldo como disciplina de revisión; promotion gate CLOSED.

C1/M05 localiza «por ti» sin relación viewer/actor; C2/M06 localiza «desde tu cuenta» / «desde la cuenta de Inés» sin relación cuenta→ejecución. Se conserva la distinción entre procedencia del texto y autoridad de cada afirmación. H25, H27–H30 y H32–H35 mantienen sus alcances y cualificaciones. No se reconstruyen sus decisiones.

Architecture v0.5 ACTIVE; ADR-001–005 ACCEPTED; TES y Product Semantic Contract unchanged. PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE unchanged; PSC-P02 NOT CREATED. H25–H36 siguen sin promoción.

## H37 HYPOTHESIS

La Activity situada H25 puede conservarse reduciendo sólo afirmaciones no acreditadas de viewer/cuenta/ejecutor, manteniendo ocurrencia aceptada, atribución operacional y declaración editorial situada, sin introducir las relaciones ausentes.

Resultado local: SUPPORTED WITH QUALIFICATION. Cuatro sustituciones de description eliminan los predicados seleccionados; dos etiquetas narrativas se conservan con autoridad editorial local. La ejecución actual acredita conservación de hechos, evaluación y representación. No certifica identidad humana ni compatibilidad de todos los textos de la App.

## VARIABLE UNDER TEST

Exclusivamente los cuatro valores DemoScriptStep.activityPresentation.description de Family Adventure A/B. [artifacts.ts](../prototype/src/demo-factory/artifacts.ts) aporta A; [costa-artifacts.ts](../prototype/src/demo-factory/costa-artifacts.ts) aporta B.

Los títulos, host/estructura de activityPresentation, filas, IDs, fechas, provenance, Public Actions, Evidence, subjects, Scenario, guards, checkpoints, contexto, evaluación, K y claim permanecen iguales. No hay delta en App, adapter, resolver, projectors, contratos, fixtures o manifests. Las adaptaciones de replay se contabilizan aparte.

## WHY NO NEW RELATION IS AUTHORIZED

S36 demostró ausencia de autoridad para ciertas relaciones afirmadas; no demostró que el producto necesitase esas relaciones. Se prueba primero una afirmación menor. Historical wording no equivale a requisito; retirar un predicado no acreditado no exige retirar atribución factual ni contenido situado.

La inspección de contratos, guards y proyección no encuentra una relación viewer/cuenta/ejecutor contradictoria con S36. Evidence.source=demo-control identifica la fuente simulada, no una persona o cuenta. No se activa STOP por evidencia contradictoria.

## PRE-DELTA ACTIVITY CLAIM MATRIX

La [matriz pre-delta completa](evidence/session-37/pre-delta-claim-matrix.md) fue escrita antes de modificar las declaraciones. Contiene los cuatro pares title/description, composición, step/actionId y 22 unidades por fragmento o composición, con claim, fuente, relación requerida, autoridad y KEEP/REDUCE/REMOVE. La [baseline](evidence/session-37/baseline.json) conserva textos y hashes recibidos.

| Composición / acción | Title recibido y conservado | Description recibida | Fragmentos y decisión |
| --- | --- | --- | --- |
| A / discover-clue-a | Pista del jardín encontrada | Hallazgo aportado por ti. | Hallazgo KEEP; jardín editorial KEEP; «aportado por ti» REDUCE; viewer→contribuidor REMOVE |
| A / discover-clue-b | Pista de la fuente encontrada | Hallazgo atribuido al huésped 2, registrado desde tu cuenta. | Hallazgo/atribución narrativa/huésped 2 KEEP; fuente editorial KEEP; cuenta→ejecución REMOVE |
| B / discover-clue-a | Pista del mirador encontrada | Hallazgo aportado por Inés. | Hallazgo/mirador KEEP; Inés sólo tiene autoridad de nombre narrativo; «aportado por Inés» REDUCE por predicar contribución humana |
| B / discover-clue-b | Pista del patio encontrada | Hallazgo atribuido a Mateo, registrado desde la cuenta de Inés. | Hallazgo/atribución narrativa/Mateo/patio KEEP; cuenta de Inés→ejecución REMOVE |

Las filas de la matriz completa separan aceptación de Evidence, atribución subjectRef, lugar situado, nombre narrativo, viewer, cuenta y ejecución. Ningún título contiene la clase de atribución seleccionada; no se amplía la variable.

## ACTIVITY OCCURRENCE AUTHORITY

[MockDataAdapter.executeAction](../prototype/src/demo/mock-adapter.ts) comprueba acción/checkpoint, habilitación, tipo y atribución de Evidence antes de almacenarla. Para hallazgos Family, sólo después busca activityPresentation por actionId y materializa la fila si existe declaración.

La existencia de fila requiere aceptación operacional y presentación H25. La nueva redacción no admite acciones ni crea Evidence. Los 16 controles de rechazo conservan el snapshot íntegro; no invocan evaluadores ni producen una fila correspondiente.

## EVIDENCE SUBJECT ATTRIBUTION AUTHORITY

El contrato de entrada usa EvidenceInput.subjects; SP.evidence[].subjectRefs proyecta sus IDs. El término subjectRefs del protocolo se verifica en ese read model y mediante los payloads completos recibidos por el evaluador.

Después del primer hallazgo A/B sigue subject-p1; después del segundo se conserva además subject-p2. No se sustituye atribución operacional por copy neutral. Target de acción, sujeto atribuido y persona que pulsa la UI siguen siendo responsabilidades distintas.

## H25 EDITORIAL AUTHORITY

La declaración seleccionada por actionId conserva title y descripción local posterior a la ocurrencia aceptada. Jardín/fuente y mirador/patio siguen siendo contenido editorial situado; no se derivan de marker-a/marker-b ni prueban presencia física.

La igualdad de hechos al perturbar description mantiene el límite H25: el texto puede cambiar e incluso contradecir la ocurrencia sin alterar Evidence o K. El host físico Script no convierte sus palabras en autoridad factual.

## VIEWER CLAIM ANALYSIS

«Hallazgo aportado por ti» asignaba una contribución al viewer que no estaba representado. Se reduce a «Hallazgo registrado». El predicado nuevo acredita sólo el registro de una ocurrencia simulada aceptada, visible en Activity.

B1 «aportado por Inés» también predicaba contribución humana. Que Inés sea un nombre editorial legítimo no acredita ese verbo. Se reduce de la misma manera. Este análisis examina nombre+predicado dentro de la variable autorizada; no revisa S36 ni descubre una nueva relación.

## ACCOUNT EXECUTION CLAIM ANALYSIS

Se retiran «registrado desde tu cuenta» y «registrado desde la cuenta de Inés». No hay cuenta ejecutora en Public Action, Evidence o read models; tampoco puede reconstruirse desde fixture.member.name.

Las descripciones conservadas no dicen que el titular de una cuenta ejecutó/aportó/registró el hallazgo. H28 sigue mostrando la cuenta como antes, incluida su perturbación a «Cuenta de Cuenta X H37».

## H27 / ACTIVITY SEPARATION

«Huésped 2» y «Mateo» se conservan en «Hallazgo atribuido…» como **Activity-local editorial declaration** H25. La atribución operacional sigue siendo por subject-p2. La descripción no verifica identidad humana, no identifica ejecutor ni presenta un lookup dinámico H27.

Cambiar sólo subjectPresentations a «Etiqueta H37 1/2» cambia GP y deja Activity intacta. En B puede persistir Mateo cuando GP muestra otra etiqueta: independencia editorial, no garantía universal de coherencia entre nombres. Ésta es una cualificación material del resultado.

## SESSION SUBJECT / ACTIVITY SEPARATION

La referencia de sesión interviene en guards de enlist/activate. No se interpreta como viewer, cuenta o ejecutor. Se observa su transporte por el proyector y la App sobre Activity no vacía procedente de un recorrido canónico admitido.

Los controles p1/p2/opaco son observaciones aisladas. No se ejecutan acciones bajo guards alteradas ni se presenta la referencia opaca como un nuevo Scenario válido.

## REDUCTION DECISION

Se conserva la atribución narrativa que no predica ejecución; se elimina el origen de cuenta y se sustituye «aportado por» por registro sin agente. La diferencia entre «atribuido a Mateo» y «aportado por Inés» es el verbo: asignación narrativa local frente a contribución humana afirmada.

La reducción no añade lugares, actores, propietarios, relaciones ni defaults. La representación situada permanece en los títulos. No se borran Activity, activityPresentation o description.

## CANONICAL DESCRIPTION DELTA

| Composición / acción | Antes | Después |
| --- | --- | --- |
| A / discover-clue-a | Hallazgo aportado por ti. | Hallazgo registrado. |
| A / discover-clue-b | Hallazgo atribuido al huésped 2, registrado desde tu cuenta. | Hallazgo atribuido al huésped 2. |
| B / discover-clue-a | Hallazgo aportado por Inés. | Hallazgo registrado. |
| B / discover-clue-b | Hallazgo atribuido a Mateo, registrado desde la cuenta de Inés. | Hallazgo atribuido a Mateo. |

El harness comprueba igualdad byte a byte entre cada fuente actual y su copia recibida aplicando exactamente estas sustituciones. Se conserva cada carácter fuera de ellas.

## NO-NEW-RELATION ANALYSIS

NO-NEW-RELATION SUFFICIENT para estos cuatro textos. No se crean viewerRef, actorRef, operatorRef, performedBy, executedBy, accountRef, memberRef on Evidence, account→subject o account→execution. No se infiere identidad desde sesión, member.name o labels GP.

Contratos y código operacional son byte-idénticos a la baseline. El experimento de sesión sustituye getSnapshot sólo en su observación aislada; los 14 recorridos actuales ejecutan provider y guards reales sin esa sustitución.

## APP CONSUMER BOUNDARY

[App.tsx](../prototype/src/app/App.tsx) conserva sus bytes. ActivityList consume item.title y item.description del snapshot; no resuelve nombres, cuenta, viewer ni semántica de atribución. No se añaden imports de catálogos a App ni reglas de reescritura durante render.

El nuevo contenido llega por la cadena H25 existente: step → adapter después de aceptación → snapshot.activity → ActivityList.

## BASELINE

[baseline.json](evidence/session-37/baseline.json) registra 454 archivos del working tree recibido, antes del delta. Excluye dependencias/build, .git, metadatos Finder, tsbuildinfo y nuevos artefactos de evidencia S37. HEAD no sustituye los cambios recibidos.

Los 445 hashes registrados por S36 coinciden. La ruta de sesión-3 necesitó normalización Unicode NFC para comparar claves de inventario en macOS; sus bytes también coinciden. No hay AGENTS.md aplicable encontrado.

La primera tentativa de suite con Node incluido en Codex no ejecutó tests por rechazo de firma macOS de una dependencia nativa. Se usó Node oficial 24.14.0 arm64 temporal, verificado con SHASUMS256 oficial: a1a54f46a750d2523d628d924aab61758a51c9dad3e0238beb14141be9615dd3. No se reinstalaron dependencias ni cambiaron package.json/lockfile.

[Baseline paralela ejecutada](evidence/session-37/baseline-parallel-node-tests.log): 94 PASS / 3 FAIL, 29 archivos. H21/H22/H23 fallan antes de sus recorridos al leer 00-governance/.DS_Store, ausente en este Mac. Sus checks posteriores no se certifican.

## CODE DELTA OR STOP

Delta productivo: dos archivos, cuatro valores escalares de description. No se activó STOP semántico, de títulos o de infraestructura.

Delta de verificación: [harness H37](../prototype/src/demo-factory/activity-attribution-reduction-h37.test.ts), copias históricas S36 y adaptación limitada del replay existente. El [control de preservación](evidence/session-37/preservation-check.json) distingue siete archivos heredados modificados: dos de contenido, cuatro harnesses históricos y un lector histórico. El resto permanece byte-idéntico.

Un primer typecheck detectó una anotación ausente en el array de rechazos del harness nuevo. Se añadió el tipo y se reejecutó con PASS. No afectó a fuentes productivas.

## A CONTROL

App actual: initial → enlist-p1 → discover-clue-a → activate-p2 → discover-clue-b → reset. Navegación explícita a Actividad y Supervisión en cada estado, incluidos ambos hallazgos; regreso a Mi aventura mediante enlaces.

Se conserva el número de filas inicial + [0, 0, 1, 1, 2], con reset a la colección inicial. IDs, occurredAt, displayDate, provenance, títulos y orden coinciden con S35. Descripciones: «Hallazgo registrado» y «Hallazgo atribuido al huésped 2».

## B CONTROL

Mismo componente, resolver, adapter y reglas actuales. Recorrido completo y reset; navegación a Actividad después de cada Evidence aceptada. Mirador y patio permanecen en títulos originales.

B sigue situada sin «cuenta de Inés». Description usa registro sin ejecutor en el primer hallazgo y atribución narrativa local a Mateo en el segundo. Hechos, atribución por ID, evaluación y restantes superficies coinciden con S35.

## ACCOUNT INDEPENDENCE CONTROL

Dos recorridos completos A/B perturbando sólo member.name. GP.sessionLabel y account-display muestran «Cuenta de Cuenta X H37». Snapshot.activity y el subárbol Activity son iguales al control.

El DOM completo incluye account-display y puede cambiar allí; la lista Activity se compara separadamente. Snapshots/evaluación se comparan íntegros salvo los campos de cuenta del control. Ninguna descripción conserva una cuenta como origen de ejecución.

## SUBJECT PRESENTATION INDEPENDENCE CONTROL

Dos recorridos A/B cambian sólo subjectPresentations. GP pasa a «Etiqueta H37 1/2». Snapshot.activity y su lista DOM quedan intactos. Evidence, atribución, estado, K, claim y SP siguen iguales.

Mateo y huésped 2 no se reconstruyen desde labels GP. Su presencia en Activity sigue siendo una declaración local.

## SESSION SUBJECT INDEPENDENCE CONTROL

Seis observaciones: A/B × subject-p1, subject-p2 y opaque:session-h37. El input factual y Activity materializada proceden del recorrido canónico final con dos hallazgos. El proyector real recibe esos datos con la única variación de operationalSessionSubjectRef; App consume el resultado por getSnapshot sustituido explícitamente.

SP y su par rótulo/valor cambian con la referencia; Activity y su DOM quedan iguales. Cero acciones públicas, cero evaluaciones nuevas. Clasificación: **isolated transport/composition observation**, no recorrido admisible ni evidencia sobre autenticación.

## EVIDENCE ATTRIBUTION PRESERVATION

Las secuencias SP.subjectRefs son [] → [] → [[subject-p1]] → [[subject-p1]] → [[subject-p1],[subject-p2]]; reset vuelve a []. Payloads completos de Public Action/Evidence, llamadas/resultados de evaluación y determinación derivada coinciden con S35.

La comparación sólo neutraliza description de los IDs de los dos hallazgos. No omite Activity completa, subjects, contexto, premise, criterion K o claim. Las guards no cambian y los rechazos se ejecutan.

## OCCURRENCE NEGATIVE CONTROL

Ocho rechazos por composición, 16 en total: sujeto no alistado, checkpoint incorrecto, actionId desconocido, sujeto atribuido incompatible, tipo Evidence incompatible, interpretación no admitida, p2 no habilitado y repetición tras checkpoint terminal.

Cada rechazo conserva snapshot antes/después exactamente igual y no invoca evaluadores. Las descripciones ya existen en Script, pero no crean fila para el hallazgo rechazado. Las aceptaciones intercaladas establecen sólo el estado previo necesario de cada guard.

## EDITORIAL INDEPENDENCE CONTROL

Cuatro recorridos: A/B × description X/Y. Cambia sólo a «Hallazgo registrado. Texto situado X/Y». Títulos, action, Evidence, subjectRefs, state, contexto, evaluación, K, claim y resto de Script coinciden.

Los textos llegan al DOM de Activity; frames factuales, Home y Supervisión conservan igualdad. El wording sigue siendo contenido H25 sin autoridad factual nueva.

## CONTRADICTION CONTROL

Dos recorridos A/B usan sólo en harness «No se ha registrado ningún hallazgo». El texto se renderiza tras materializar registros y la suficiencia final sigue established. La contradicción no transforma hechos.

El control no introduce viewer/cuenta/actor y no se publica como copy canónico. Declarar palabras no garantiza su verdad; el contenido elegido requiere revisión semántica.

## SEMANTIC NEGATIVE CHECK

| Description actual | Predicados conservados | Predicados ausentes / cualificación |
| --- | --- | --- |
| Hallazgo registrado. | Registro del hallazgo simulado admitido | Sin ejecutor, viewer, titular o cuenta fuente; soporte en fila real |
| Hallazgo atribuido al huésped 2. | Atribución narrativa local H25; atribución operacional a subject-p2 en Evidence | No dice quién ejecutó/aportó/pulsó ni desde qué cuenta; no parsing del ID |
| Hallazgo atribuido a Mateo. | Etiqueta narrativa Activity-local de atribución H25 | No verifica persona, actor, titular o identidad universal; no obtiene nombre desde H27 |

Además de strings exactos y chequeo lexical, se revisaron verbos y argumentos. «Aportado por» atribuye contribución; «desde la cuenta» atribuye origen de ejecución; ambos se retiran. «Atribuido a» conserva narración local cualificada y no acredita identidad humana del ejecutor.

No se extiende la certificación a presenterLabel, headings u otros literales congelados.

## CURRENT APP DOM / INTEGRATION EXECUTION

**EXECUTED.** [Traza final](evidence/session-37/execution-trace-final.json): 14 recorridos App actual = 12 Family (A/B canónicos y cinco variantes por composición) + Retail + Arrival. 77 estados incluidos resets y 231 capturas DOM Home/Activity/Supervisión. Se añaden seis observaciones App aisladas y 16 rechazos de provider, contabilizados separadamente.

Se usa createRoot/MemoryRouter en jsdom, clics públicos, resolver/provider/guards/projectors vigentes y spies transparentes de evaluadores. H37 importa node:fs y fuentes actuales directamente; no cuenta catálogos archivados como evidencia actual.

Cada captura Activity verifica título, description, datetime, fecha visible y número de filas contra snapshot. Navegar conserva snapshot y llamadas de evaluación. Home verifica nombre Experience, marca, intro, mensaje, cuenta, etiquetas y estados. Supervisión verifica referencias exactas, sesión, Evidence, K y determinaciones.

## BROWSER VISUAL VALIDATION STATUS

**NOT EXECUTED.** Este hilo no expone una herramienta de control de navegador invocable. No se han generado screenshots ni evaluado clipping, tipografía o layout en navegador real. jsdom y build no cuentan como validación visual.

«CURRENT APP DOM-INTEGRATION VERIFIED» se limita a esa capa de evidencia.

## NEGATIVE CONTROLS

Retail conserva initial/reset; Arrival conserva initial → confirm-arrival → reset. Snapshots, frames factuales/evaluadores y los tres DOM completos coinciden con S35 sin neutralizar descriptions.

Fixture Activity y rama genérica Arrival permanecen byte-idénticas. No se introduce un default Family global ni se retira contenido genérico.

## CURRENT CUMULATIVE REGRESSION

| Superficie | Evidencia actual |
| --- | --- |
| H25 ocurrencia/title/id/occurredAt/provenance | Igualdad con S35 salvo cuatro descriptions; aceptación/rechazo vigente |
| H27 GP labels | Render + perturbación independiente A/B |
| H28 cuenta | Render + cambio de member.name A/B |
| H29 estado | Secuencia not-enlisted/not-enabled/enabled y detalle SP iguales |
| H30 journey message | Render por fase; Home completo igual a S35 |
| H32 marca + intro | Cabecera renderizada; Home igual a S35 |
| H33 referencias supervisión | IDs exactos, orden y Evidence atribuida renderizados |
| H34 sesión supervisora | Par rótulo/ref canónico conservado; transporte aislado X/Y/opaco |
| H35 Experience.name | h1 == Experience.name en cada captura; transporte sin delta |

Igualdad sobre fuentes actuales y recorridos nuevos. Los PASS históricos no se contabilizan como ejecución actual H37.

## HISTORICAL REPLAY STATUS

Se archivaron bytes pre-H37 y se conservaron expectativas históricas. H32/H33/H34/H35 seleccionan declaraciones S36 con wording antiguo; replays anteriores mantienen rutas más antiguas. El lector S34 encadena el nuevo S36 sólo para rutas todavía no resueltas.

Los ensayos H25–H35 existentes pasan en la suite final; S36 fue auditoría documental sin harness ejecutable. Su informe/evidencias siguen byte-idénticos. H25 no espera retrospectivamente el wording H37.

La suite global no está verde: H21/H22/H23 conservan el fallo previo por metadatos ausentes. No se relajan sus assertions ni se inventa el archivo Finder. Sus etapas posteriores quedan sin certificar.

## TEST-INFRASTRUCTURE PRESSURE OBSERVATION

| Observación | Resultado |
| --- | --- |
| Harnesses históricos modificados | 4: H32, H33, H34, H35 |
| Lector histórico modificado | 1: S34 encadena S36 tras sus rutas existentes |
| Rutas nuevas de bytes archivados | 7: dos declaraciones, cuatro harnesses, un lector |
| Catálogos runtime nuevos de replay | 2 copias con imports reubicados; cuatro puntos de selección en harnesses |
| Harness actual nuevo | 1: H37 |
| Primera tentativa con Node de Codex | Startup error por firma nativa; 0 tests ejecutados |
| Baseline paralela con Node oficial | 94 PASS / 3 FAIL, 29 archivos |
| Final paralela con Node oficial | 95 PASS / mismos 3 FAIL, 30 archivos |
| Timeouts observados en ambas suites | 0 |
| Ejecución serial | NOT EXECUTED; fallos deterministas por archivo ausente, sin timeout que justificase repetir |
| Typecheck / lint / build PWA | PASS |
| Runner, worker defaults y timeouts existentes | Sin modificaciones |

La presión sigue MATERIAL y afecta a portabilidad del replay. No bloqueó H37 ni requirió refactorización sustancial. Añadir rutas al mecanismo existente tiene coste; no se presenta como solución de esa presión.

[Log final paralelo](evidence/session-37/final-parallel-tests.log), [typecheck final](evidence/session-37/typecheck-final.log), [lint](evidence/session-37/lint.log) y [build](evidence/session-37/build.log) registran resultados. La suite completa devuelve exit 1 por tres fallos heredados; no se anuncia npm run check como PASS.

## EXECUTION TRACE

[execution-trace-final.json](evidence/session-37/execution-trace-final.json) contiene controles A/B, variantes, inputs, snapshots, llamadas/resultados de evaluadores, DOMs por fase, resets, genéricos, rechazos y observaciones aisladas. Registra hashes de baseline, traza S35, harness y fuentes actuales.

[verification-summary.json](evidence/session-37/verification-summary.json) verifica hashes y cobertura del informe. [preservation-check.json](evidence/session-37/preservation-check.json) comprueba los 454 archivos heredados, copias exactas y cambios inesperados. La [matriz pre-delta](evidence/session-37/pre-delta-claim-matrix.md) conserva el razonamiento anterior a las sustituciones.

La traza inicial execution-trace.json corresponde al primer PASS funcional antes de la anotación TypeScript del array de rechazos. La traza final procede del harness final y es evidencia de cierre. S35/S36 no se sobreescribieron.

## H25 STATUS

PRESERVED: presentación situada explícita por paso, posterior a aceptación operacional, independiente de evaluación. Títulos y materialización intactos. Reducir ciertas descripciones no refuta el resultado acotado H25 ni lo convierte en garantía de verdad de todo literal.

## H36 HISTORICAL VERDICT STATUS

PRESERVED / FALSIFIED. C1/C2 estaban presentes en la baseline examinada por S36 y falsaban correctamente la cobertura exhaustiva. Reducirlos ahora no modifica ese hecho histórico ni convierte H36 en SUPPORTED.

Informe S36, matriz y evidencias mantienen sus bytes. No se proclama ahora un modelo exhaustivo U/D/O/E.

## ACTIVITY ATTRIBUTION RESULT

Los claims viewer/actor seleccionados y cuenta→ejecución se eliminan de descriptions canónicas. Permanece la atribución factual por IDs en Evidence/SP y, cuando existía sin predicar ejecución, una etiqueta narrativa Activity-local.

Se conservan lugares por composición, filas y secuencia. El registro sigue siendo simulado. No se concluye que una persona concreta ejecutase la acción ni que los nombres representen identidades verificadas.

## AUTHORITY MODEL OBSERVATION

La evidencia refuerza la heurística: cuando una presentación sobreafirma respecto de su autoridad disponible, ensayar primero una reducción antes de expandir el modelo. H29/H33/H34 y H37 aportan casos locales compatibles.

EVIDENCE-BACKED REVIEW HEURISTIC / NOT PROMOTED. No prueba suficiencia universal de reducción ni ownership universal de Script.

## FALSIFICATION ANALYSIS

| Falsador / STOP | Observación |
| --- | --- |
| Activity pierde sentido sin viewer/cuenta | No observado: títulos situados y registros visibles conservados |
| Necesidad de relación viewer/actor/cuenta/member→subject | No observada; delta de cuatro strings |
| H27 usado como identidad universal | No; labels perturbados sin cambio de Activity |
| Cambian Evidence, subjectRefs, estados, contexto, K o claim | No; frames y llamadas/resultados iguales a S35 |
| Se elimina fila, activityPresentation o description | No; counts, materialización y campos conservados |
| Relación legítima contradice S36 | No encontrada en fuentes inspeccionadas |
| Título contiene misma atribución indebida | No encontrado; títulos congelados |
| Infraestructura exige refactorización sustancial | No; adaptación limitada al replay existente |
| Sobrevive relación equivalente en nueva description | No en el alcance; revisión de predicados además de strings |

Cualificaciones: A/B, verdad simulada, nombres editoriales locales, sesión observada aisladamente y falta de validación visual. Los tres fallos de metadatos son previos; no se convierten en falsadores semánticos ni en suite aprobada.

## H37 VERDICT

SUPPORTED WITH QUALIFICATION. NO-NEW-RELATION SUFFICIENT para preservar Activity H25 tras la reducción seleccionada. Resultado actual acreditado en DOM/integración, con hechos y evaluación conservados.

## ARCHITECTURAL CONSEQUENCE

Architecture v0.5 ACTIVE y ADR-001–005 ACCEPTED unchanged. No nuevo ADR, frontera, registro de presentación, ownership universal ni modelo de identidad. App consumidor; promotion gate CLOSED.

Representar estos registros sin actor/cuenta reduce esa presión concreta del modelo actual; no excluye necesidades distintas en un producto futuro.

## SEMANTIC CONSEQUENCE

TES, Product Semantic Contract y PSC-P01 unchanged; PSC-P02 NOT CREATED. No cambia la semántica de sujeto, Evidence, estado, K, claim o Experience. La menor afirmación se limita a description.

Los vínculos ausentes no se declaran falsos en el mundo real: no están acreditados aquí y no fueron necesarios para esta representación.

## ARTIFACT QUARANTINE

H25–H37 EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. Las sustituciones son reversibles desde copias pre-delta; restaurarlas recuperaría también las sobreafirmaciones.

X/Y/contradicción y referencias opacas sólo viven en harness/evidencias. No se incorporan a catálogos canónicos ni arquitectura.

## WHAT H37 DOES NOT PROVE

No prueba identidad humana, quién pulsó UI, autenticación, viewer, cuenta ejecutora, cuenta=sujeto, verdad externa o coherencia universal de nombres. Títulos situados no equivalen a geolocalización factual. Una declaración editorial puede mentir.

No prueba compatibilidad de todos los literales App, UX visual, suficiencia universal U/D/O/E, ownership universal de Script, que toda presión de identidad pueda resolverse con copy o que nunca se necesite un modelo de actor/cuenta.

No acredita etapas no ejecutadas H21/H22/H23 ni suite global verde.

## REMAINING PRESSURES

Siguen observadas divergencia GP/nombres Activity, segunda persona/cuenta en affordances/headings fuera del alcance, navegación histórica fija a A, terminología diagnóstica y duplicación literal de K. La infraestructura sigue material, con dependencia de metadatos Finder evidenciada en este Mac.

NEXT MATERIAL PRESSURE OBSERVED BUT NOT SELECTED. H38 NOT OPENED.

| Dimensión | Resultado final |
| --- | --- |
| H37 | SUPPORTED WITH QUALIFICATION |
| NO-NEW-RELATION | SUFFICIENT |
| VIEWER / ACTOR CLAIM | REMOVED AS UNSUPPORTED en descriptions seleccionadas |
| ACCOUNT EXECUTION CLAIM | REMOVED AS UNSUPPORTED |
| ACTIVITY OCCURRENCE AUTHORITY | PRESERVED |
| EVIDENCE SUBJECT ATTRIBUTION | PRESERVED |
| H25 SITUATED ACTIVITY PRESENTATION | PRESERVED; etiquetas narrativas locales cualificadas |
| APP CONSUMER BOUNDARY | PRESERVED |
| A/B ACTIVITY REPRESENTATION | CURRENT APP DOM-INTEGRATION VERIFIED |
| H36 HISTORICAL VERDICT | PRESERVED / FALSIFIED |
| SEMANTIC REDUCTION HEURISTIC | EVIDENCE STRENGTHENED / NOT PROMOTED |
| TEST-INFRASTRUCTURE PRESSURE | MATERIAL; 95 PASS / 3 fallos previos por metadatos; no bloquea H37 |
| NEXT MATERIAL PRESSURE | OBSERVED BUT NOT SELECTED |
