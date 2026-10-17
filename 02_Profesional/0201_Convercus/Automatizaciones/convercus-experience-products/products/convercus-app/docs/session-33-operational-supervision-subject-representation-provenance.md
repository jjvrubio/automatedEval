---
title: "Sesión 33 — Operational Supervision Subject Representation Provenance"
language: es
version: "v1.0"
status: "CLOSED / H33 SUPPORTED WITH QUALIFICATION within Family Adventure A/B"
date: "2026-09-18"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 33 — Operational Supervision Subject Representation Provenance

## H32 CONSOLIDATED INPUT

[S32](session-32-explicit-composition-introductory-framing.md) permanece CLOSED / SUPPORTED WITH QUALIFICATION. La relación introductoria de DemoScript es EXPLICIT / EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. Marca resuelta e introducción conservan autoridades separadas y verificación DOM de App A/B. No se reconstruyen decisiones anteriores.

Se reciben L3a/H28, L3b/H27, L3c/H29–H30 y L5/H25 preservados y experimentalmente abordados. L4 framing queda preservado; L4 Supervisión estaba OPEN. Viewer relation NOT INTRODUCED. La recurrencia presentacional de Script estaba STRENGTHENED / NOT PROMOTED.

Architecture v0.5 ACTIVE, ADR-001–005 ACCEPTED, TES y Product Semantic Contract sin cambios. PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE sin cambios; PSC-P02 NOT CREATED.

## H33 HYPOTHESIS

Las referencias operacionales existentes de SupervisionPerspective pueden proporcionar identificación diagnóstica neutral suficiente sin H27, nombres humanos, nuevas relaciones, parsing de IDs ni modificación de sujetos, sesión, Evidence, estados, evaluación, K o claim.

Relación ensayada: fuente operacional existente → representación supervisora neutral. No se ensaya subjectRef → identidad humana, GP → presentación SP ni account → sujeto supervisado.

## VARIABLE UNDER TEST

Únicamente el `h2` de cada tarjeta de sujeto en SystemPage/Supervisión. Se conservan íntegros el párrafo diagnóstico, id, exists, operationalState, evidenceCount, sesión, evaluación, K, claim y atribución. GP, Activity, branding e introducción quedan fuera del delta.

## WHY NO NEW RELATION IS AUTHORIZED YET

SP ya transporta el identificador usado por el branch previo. Antes de postular una relación presentacional adicional procede comprobar su suficiencia diagnóstica. La apariencia humana del hardcode no demuestra un requisito de identidad humana. La identificación operacional disponible resulta suficiente dentro del experimento; no se solicita ni introduce relación nueva.

## SUPERVISION SOURCE INSPECTION

La [inspección anterior al delta](evidence/session-33/pre-delta-source-inspection.md) contiene la matriz por sujeto y precede a la edición de App. Fuentes: contratos `SupervisionPerspectiveReadModel`, `SubjectReference`, `ScenarioDefinition`, `EvidenceInput`; Scenario A/B; `subjectStates`, `operationalSessionSubjectRef` y atribución en adapter; `projectSupervisionPerspective()`; consumidor SystemPage.

| Campo SP | Fuente y responsabilidad | Conocimiento autorizado |
| --- | --- | --- |
| subjects[].id | Scenario.subjects[].id, copiado literalmente | Referencia operacional del sujeto suministrado |
| subjects[].exists | true al mapear la colección de Scenario | Presencia declarada en esa colección; no existencia humana universal |
| subjects[].operationalState | subjectStates[id], fallback existente not-enabled | Estado operacional local |
| subjects[].evidenceCount | Evidence con alguna atribución cuyo id coincide | Recuento por sujeto; no identidad humana |
| evidence[].subjectRefs | IDs de los sujetos de cada Evidence | Atribución operacional preservada |
| sessionSubjectRef | Scenario.operationalSessionSubjectRef | Ref de sesión, sin propiedad de cuenta o viewer |
| jointAdmissibility / sufficiency / derivedClaim | evaluation y claim existentes | Resultados evaluados, no autoridad presentacional |

SP no contiene nombre humano, account ownership, viewer identity ni la presentación H27 de GP. El adapter entrega subjectPresentations a GP y no a SP.

## CURRENT COPY DECOMPOSITION

| Fragmento previo | Procedencia efectiva | Autoridad para H33 |
| --- | --- | --- |
| P1 | Literal de branch App al comparar subject-p1 | No hay alias declarado. No se legitima abreviándolo del ID |
| Lucía | Literal App coincidente con copy A | Sin relación supervisora que autorice el nombre |
| P2 | Literal del else para cualquier otro ID | No hay alias declarado; tampoco autoridad por índice |
| Huésped 2 | Literal del mismo else | Presentación humana numerada sin fuente SP |

La coincidencia con H27 o member.name no establece procedencia legítima para Supervisión. En B tampoco se sustituyen estos nombres por Inés/Mateo.

## OPERATIONAL SUBJECT AUTHORITY

En A/B, Scenario declara `subject-p1` y `subject-p2`. El proyector transporta ambos valores sin transformación como `SP.subjects[].id`. Esa misma referencia correlaciona la tarjeta con su estado, atribución y ref de sesión. El resultado renderiza exactamente esos valores.

`subject-p1` no se interpreta como nombre, abreviatura, titular ni persona. El párrafo ya repetía ese ID; se conserva la repetición porque los datos diagnósticos están congelados.

## H27 / SUPERVISION SEPARATION

H27 sigue autorizando DemoScript.subjectPresentations → GP.subjects[].label exclusivamente dentro del alcance demostrado. Perturbar esa relación cambia las etiquetas de GP y deja SP completo y sus encabezados idénticos. Same subjectRef across read models != same presentation authority.

## CANDIDATE EXISTING REPRESENTATIONS

| Candidato | Resultado |
| --- | --- |
| SP.subjects[].id literal | Seleccionado; fuente mínima ya transportada, identifica cada tarjeta |
| P1/P2 | Rechazado; alias local o parsing, no valor declarado |
| Scenario.type = individual | Clasificación; no display name; no llega a SP |
| Scenario.role = guest | Rol; no nombre ni autorización para humanizar; no llega a SP |
| subjectStates / evidenceCount | Describen propiedades cambiantes; no identifican por sí solos |
| sessionSubjectRef | Referencia de sesión; no identifica todos los sujetos ni declara account ownership |
| H27/member/Script editorial | Otras autoridades; no se reutilizan |

No se añade transporte de role/type: no es necesario para el resultado seleccionado ni autoriza exactamente un nombre humano.

## NO-PARSING ANALYSIS

El delta contiene literalmente `<h2>{subject.id}</h2>`. No contiene split, replace, regex, substring, extracción de sufijos, branch por ID/demo/composición ni acceso por índice. El harness compara todo App con S32 después de sustituir exclusivamente la expresión autorizada, por lo que también congela imports, navegación y demás código.

Las transformaciones de DOM del harness sólo normalizan el orden de atributos y vacían los h2 seleccionados para comparar el resto; no forman parte del producto ni transforman IDs.

## NO-NEW-RELATION ANALYSIS

SUFFICIENT para identificación diagnóstica neutral en A/B. No se añade contrato, campo, mapping, lookup, artefacto ni relación de presentación. Operational identification AVAILABLE. Human supervision presentation NO RELATION DECLARED / NOT REQUIRED para H33. No se demuestra que nombres humanos sean innecesarios para cualquier uso futuro.

## APP CONSUMER BOUNDARY

Se conserva Scenario → proyector SP → snapshot → App → render. App consume `subject.id` de la tarjeta recibida. No consulta Scenario, DemoScript, subjectPresentations o member para resolver el encabezado. No hay nueva inferencia de identidad.

## BASELINE

[Baseline](evidence/session-33/baseline.json): 400 archivos del árbol recibido antes del delta, excluidos directorios generados/dependencias. Incluye gobernanza, semántica, fuentes, documentación y evidencia previa. El árbol ya contenía cambios heredados, preservados; no se usa HEAD como sustituto del cierre S32.

`npm run check` antes del delta: typecheck PASS, lint PASS, 94/94 tests en 26 archivos, build/PWA PASS. Se archivaron copias byte-identical de App S32 y su harness antes de modificarlos.

Auditoría posterior: 394 archivos idénticos, un archivo de producto cambiado, un harness histórico adaptado y cuatro `.DS_Store` con deriva de metadatos registrada por separado. Cero cambios inesperados de fuentes y cero archivos ausentes. Los hashes iniciales no se rebasan.

## CODE DELTA OR STOP

Se ejecuta el delta, no se activa STOP. [Patch de producto](evidence/session-33/application-delta.patch): una línea de `prototype/src/app/App.tsx`, en SystemPage.

```diff
- <h2>{subject.id === "subject-p1" ? "P1 · Lucía" : "P2 · Huésped 2"}</h2>
+ <h2>{subject.id}</h2>
```

Contratos, proyectores, adapter, Scenario, Script, Fixture, Experience, Manifest, evaluadores, CSS y navegación permanecen idénticos. Se añade harness H33, archivo App S32 y evidencia documental. El [patch de instrumentación histórica](evidence/session-33/historical-instrumentation-delta.patch) está separado del delta de producto.

## A CONTROL

App vigente, `hospitality-family-adventure`, recorrido público completo: initial → enlist-p1 → discover-clue-a → activate-p2 → discover-clue-b → reset. En cada fase se visita Supervisión, Activity y Mi aventura.

Encabezados: subject-p1 / subject-p2. Los párrafos diagnósticos y paneles coinciden con el snapshot. Todos los snapshots, inputs y llamadas/resultados de ambos evaluadores coinciden con S32. DOM de GP y Activity idéntico; DOM de Supervisión idéntico al anterior salvo los dos encabezados.

## B CONTROL

App vigente, `hospitality-family-adventure-costa`, mismo recorrido y comparaciones. Los encabezados también son subject-p1 / subject-p2. No dependen de Lucía/Huésped 2 ni incorporan Inés/Mateo de H27. GP continúa mostrando su presentación B. El resto del DOM supervisor y todos los hechos permanecen iguales a S32 para B.

## CROSS-COMPOSITION CONTROL

A/B comparten refs operacionales y producen los mismos encabezados durante las cinco fases y reset. Sus cuentas, H27, marcas, intros, mensajes, Activity y contextos difieren legítimamente. No se exige igualdad de Evidence/contextos entre A y B; cada recorrido se contrasta con su propia baseline.

## SUBJECT PRESENTATION INDEPENDENCE CONTROL

En cada composición, sólo subjectPresentations cambia a Participante Alfa/Beta. GP renderiza esas etiquetas. SP completo y sus encabezados quedan idénticos durante todo el recorrido y reset. Los snapshots completos sólo difieren en las etiquetas GP autorizadas; acciones y evaluaciones permanecen iguales.

## ACCOUNT INDEPENDENCE CONTROL

En cada composición, sólo member.name cambia a Cuenta H33. Se verifica `Cuenta de Cuenta H33` en GP y la cabecera de cuenta. Los snapshots sólo difieren en member.name y sessionLabel; SP y sus encabezados no cambian. El texto de cuenta que rodea la superficie no se confunde con identificación del sujeto supervisor.

## BRAND / INTRO / JOURNEY INDEPENDENCE CONTROL

Cuatro perturbaciones independientes por composición: brand.name, experimentalIntroductoryFraming, experimentalJourneyPresentations y activityPresentation. Cambian las superficies legítimas correspondientes; cada una conserva SP entero y sus encabezados en todas las fases. Marca/intro no alteran snapshots; narrativa sólo altera GP.message; Activity sólo altera title/description de su representación. Inputs y evaluaciones completos permanecen iguales.

## STATE INDEPENDENCE CONTROL

Se cambia estado exclusivamente mediante botones públicos de alistamiento/activación, sin mutar Scenario. La secuencia de estados p1/p2 es: not-enlisted/not-enabled → enabled/not-enabled → enabled/not-enabled → enabled/enabled → enabled/enabled. Los encabezados no cambian. Reset restaura estados iniciales y mantiene las refs.

## EVIDENCE INDEPENDENCE CONTROL

El recorrido legítimo produce recuentos por sujeto [0,0] → [0,0] → [1,0] → [1,0] → [1,1]. Alistamiento/activación no añaden Evidence. Las refs y encabezados se mantienen. Se verifica la lista DOM completa de atribuciones y provenance, así como evaluación, suficiencia, K y claim; reset vuelve a [0,0].

## ORDER CONTROL

Control aislado de proyector/read model, no Scenario productivo: se invierte la colección de refs originales al proyectar el estado tras discover-clue-a. El array resultante conserva exactamente los registros por ID, con p2 antes de p1. App vigente renderiza en ese orden el ID correcto, su estado y su recuento. El primer sujeto ya no es p1. No se ejecutan acciones sobre esta colección ni se afirma semántica de orden nueva.

## UNKNOWN SUBJECT OBSERVATION

En una entrada aislada del proyector se añade la referencia opaca `opaque:diagnostic/7-Z`, type individual, role guest, estado not-enabled y cero Evidence atribuida. No se modifica ningún Scenario/catálogo productivo ni se crea P3. Se transporta el read model resultante a App mediante sustitución explícita de getSnapshot sólo en este control.

El encabezado es exactamente `opaque:diagnostic/7-Z`; su detalle conserva esa referencia, exists true, not-enabled y Evidence 0. No recibe P2/Huésped 2 ni alias por orden o sintaxis. No se ejecutan acciones ni evaluación con ese sujeto: se reutiliza un resultado evaluado previo para observar exclusivamente proyección/render. No demuestra soporte de una tercera persona en K o en la premisa de admisibilidad.

## CUENTA/SESIÓN OPERATIVA FREEZE

Se conserva exactamente «Cuenta/sesión operativa» y el valor sessionSubjectRef. El control DOM comprueba ambos en todas las fases. La mezcla potencial account/session permanece visible como presión separada y abierta.

## OTHER SUPERVISION FREEZE

Evaluación compartida, Criterio K, Evidence recibida, Admisibilidad conjunta, Suficiencia K, Afirmación derivada y Evidence y atribución permanecen intactos. La comparación de DOM sólo excluye el contenido de los h2 de las tarjetas seleccionadas; no excluye estos textos, sus valores, el párrafo diagnóstico ni la lista de Evidence.

## CURRENT APP DOM / INTEGRATION EXECUTION

EXECUTED: React createRoot, MemoryRouter y jsdom sobre App vigente. 16 recorridos actuales completos: A/B canónicos + seis variantes independientes por composición + Retail/Arrival. 89 observaciones de fase, incluyendo reset; cada una captura tres superficies (267 capturas DOM). Provider real, acciones por botones públicos, spies transparentes de executeAction/reset y ambos evaluadores. Navegar no cambia snapshot ni añade llamadas evaluadoras.

Separadamente: cuatro recorridos de App S32 archivada, 17 fases (51 capturas DOM) para comparación; dos observaciones aisladas de read model con App actual (dos capturas DOM). Las dos sustituciones getSnapshot están identificadas y no acreditan recorridos operacionales canónicos. Total del harness H33: 108 observaciones de fase/aisladas y 320 capturas DOM, con procedencia diferenciada.

## BROWSER VISUAL VALIDATION STATUS

NOT EXECUTED. No se ejecutó navegador visual ni inspección de layout, móvil o accesibilidad visual. DOM/integration EXECUTED no equivale a validación visual. La suficiencia acreditada es operacional y de procedencia, no una evaluación de usabilidad del identificador técnico.

## NEGATIVE CONTROLS

Retail `retail-baseline` y Arrival `hospitality-stay` se ejecutan con App actual y S32 archivada. Sus snapshots, acciones, evaluaciones y reset coinciden con la traza S32. DOM completo de Inicio, Activity y panel genérico idéntico en cada fase. No aparece SupervisionPerspective, GuestPerspective ni tarjetas familiares; absence remains absence. No se introducen defaults.

## CURRENT CUMULATIVE REGRESSION

H25 Activity, H27 labels GP, H28 cuenta, H29 estado, H30 mensaje y H32 marca/intro se comprueban sobre App vigente en cada captura, con recorridos y perturbaciones reales. Los canónicos coinciden con snapshots completos y DOM Home/Activity de la traza S32; además se ejecuta App S32 por separado y se compara cada fase.

Check final: typecheck PASS, lint PASS, 95/95 tests en 27 archivos, build/PWA PASS. La única diferencia de producto es el encabezado de sujeto de SP. El freeze de código compara todo App byte a byte tras la sustitución única autorizada.

## HISTORICAL REPLAY STATUS

El harness H32 contenía un freeze explícito de las etiquetas supervisoras antiguas. Se preservan sus aserciones, se importa App S32 archivada y se lee esa misma fuente para su freeze; nombre, comentario y método se etiquetan como replay histórico. No se presenta su éxito como evidencia de App H33 vigente. El resto de replays permanece sin modificaciones.

Las copias previas de App y harness H32 son byte-identical a la baseline. La traza, informe y evidencia originales S32 permanecen idénticos. El nuevo harness H33 importa directamente App actual y aporta la acreditación acumulativa vigente.

## EXECUTION TRACE

[Traza H33](evidence/session-33/execution-trace.json): inputs públicos, snapshots completos, llamadas/resultados de evaluateVerticalEvidence y evaluateCrossSubjectEvidenceSufficiency, DOM de las tres superficies por fase, encabezados, diagnósticos, variantes, reset y controles aislados. Se escribe sólo al completar todas las aserciones, con creación exclusiva; no sobrescribe traza anterior.

[Preservación](evidence/session-33/preservation-check.json) separa delta de producto, instrumentación histórica y metadatos. [Resumen de verificación](evidence/session-33/verification-summary.json) registra resultados, recuentos y hashes. Harness reproducible: `prototype/src/demo-factory/operational-supervision-subject-h33.test.ts`; `npm run check` ejecuta la suite sin reescribir evidencia. Para nueva traza usar H33_RECORD_PATH con una ruta nueva.

Durante preparación hubo un fallo de auditoría por `.DS_Store` en la raíz: se extendió la exclusión de metadatos para cubrir ese nombre además de rutas anidadas. La baseline permaneció intacta y la deriva queda registrada. No fue un fallo funcional ni un falsador de H33. El harness pasó después y el check completo final pasó con la traza definitiva.

## L3a STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H28. Account presentation sigue derivando de member.name; no declara account → supervised subject ni viewer.

## L3b STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H27. Subject labels situadas pertenecen al alcance probado de GP; no adquieren autoridad universal por compartir subjectRef.

## L3c STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30. Estados dependen de subjectStates; narrativa de su declaración experimental y affordance existente. Ninguno identifica al sujeto de SP.

## L4 FRAMING STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H32. BrandArtifact resuelto y relación introductoria estática conservan autoridades independientes. huntName y link fijo a A permanecen intactos; no se amplía su interpretación.

## L4 SUPERVISION SUBJECT RESULT

EXISTING OPERATIONAL SOURCE / LOCAL RENDER / CURRENT APP DOM-INTEGRATION VERIFIED within A/B. El encabezado se reduce al identificador exacto ya transportado. Se elimina copy humana no autorizada, sin perder semántica operacional demostrada ni introducir relación presentacional.

## L4 REMAINING SUPERVISION PRESSURE

La superficie «Cuenta/sesión operativa» continúa PRESERVED / OPEN. No se resuelve propiedad de cuenta, viewer, terminología diagnóstica o presentación humana supervisora. La suficiencia del identificador no cierra todas las presiones de L4.

## L5 STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H25. Activity conserva su presentación local Script-bound; su perturbación no afecta identificación supervisora ni hechos evaluados.

## RECURRING PRESENTATION PRESSURE

OBSERVED / QUALIFIED BY H33 / NOT PROMOTED. H25/H27/H30/H32 aportan recurrencia situada experiencial/editorial. H33 añade contraevidencia local a «all presentation belongs in Script»: esta representación diagnóstica se resuelve desde autoridad operacional ya presente en SP.

No se convierte el hallazgo en principio arquitectónico universal. No se crea ADR ni PresentationBoundary, ni se promueve DemoScript como propietario general de presentación.

## FALSIFICATION ANALYSIS

| Falsador | Observación |
| --- | --- |
| SP no identifica sujetos desde campos existentes | No observado: id literal distingue y correlaciona las tarjetas |
| Requiere H27, member o Script | No observado: seis perturbaciones por composición mantienen SP |
| Requiere parsing, índice o branch A/B | No observado: expresión literal, orden invertido y ref opaca verificados |
| Cambia sujetos, estados, sesión, Evidence, evaluación, K o claim | No observado: fuentes congeladas y facts completos iguales a S32 |
| Obliga a resolver cuenta/sesión o viewer | No observado: freeze DOM y source exacto |
| Introduce nueva relación para humanizar | No observado: human presentation no requerida para el objetivo diagnóstico |

La suficiencia es local a los recorridos probados. No se infiere identidad humana, autorización, unicidad global ni calidad UX de esos IDs.

## H33 VERDICT

SUPPORTED WITH QUALIFICATION. NO-NEW-RELATION SUFFICIENT para identificación supervisora neutral en Family Adventure A/B. La ejecución vigente respalda el cambio mínimo; las cualificaciones son alcance local, controles adicionales aislados y ausencia de validación visual/estudio de usabilidad.

## ARCHITECTURAL CONSEQUENCE

Architecture v0.5 y ADR-001–005 unchanged. Se preserva la frontera consumidor read model → App. No se introduce abstracción o contrato nuevo ni se promueve artefacto. El hallazgo es evidencia experimental sobre procedencia, no decisión arquitectónica adicional.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract unchanged. PSC-P01 conserva OPEN / EVIDENCE-BACKED PRESSURE; PSC-P02 NOT CREATED. Renderizar una referencia existente no crea identidad nueva. Reducir copy no autorizada no equivale a perder semántica demostrada. No se cambia admisibilidad, criterio K o claim.

## ARTIFACT QUARANTINE

H25–H32 permanecen EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. H33 y su evidencia también son locales y reversibles: restaurar la expresión archivada revierte el único delta de producto, sin migración o cambio de datos. No se abre H34.

## WHAT H33 DOES NOT PROVE

No prueba que los IDs sean nombres humanos, que siempre basten para UX, que GP y SP compartan autoridad presentacional, que Script sea dueño universal de presentación, que un sujeto adicional sea admisible en la premisa/K, ni que la sesión implique propiedad de cuenta o viewer. No acredita browser visual, producción, todos los Scenarios ni todos los futuros roles/types.

## REMAINING PRESSURES

Se observan, sin seleccionarlas: «Cuenta/sesión operativa», huntName, navegación fija a A y otra terminología diagnóstica. Una posible presentación humana de Supervisión necesitaría una relación declarada y una necesidad explícita; H33 no exige ni autoriza crearla. Recurrencia Script-bound permanece cualificada y no promovida. NEXT MATERIAL PRESSURE OBSERVED BUT NOT SELECTED; H34 NOT OPENED.
