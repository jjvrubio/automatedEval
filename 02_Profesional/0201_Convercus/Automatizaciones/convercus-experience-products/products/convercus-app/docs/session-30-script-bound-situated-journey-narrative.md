---
title: "Sesión 30 — Script-bound Situated Journey Narrative"
language: es
version: "v1.0"
status: "CLOSED / H30 SUPPORTED WITH QUALIFICATION within Family Adventure A/B"
date: "2026-09-17"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 30 — Script-bound Situated Journey Narrative

## H29 CONSOLIDATED INPUT

**H30 → SUPPORTED WITH QUALIFICATION dentro de Family Adventure A/B.** Una relación declarada en Script presenta narrativa situada a partir de la **acción actualmente disponible**. El checkpoint se rechaza como selector porque no distingue las posiciones requeridas. La relación no crea posición operacional ni cambia Evidence, evaluación, K o claim.

[S29](session-29-operational-subject-status-provenance.md) permanece CLOSED: H29 SUPPORTED WITH QUALIFICATION; L3c SUBJECT STATUS EXPERIMENTALLY ADDRESSED / STATE-ONLY / EXECUTION-VERIFIED within A/B. La autoridad de estado/presentación sigue apoyada en subjectStates, sin atribución causal ni viewer. L3a/H28, L3b/H27 y L5/H25 se conservan. L4 permanece SOURCE-INSPECTION / OPEN.

Architecture v0.5 ACTIVE, ADR-001–005 ACCEPTED, TES y Product Semantic Contract siguen sin cambios. PSC-P01 continúa OPEN / EVIDENCE-BACKED PRESSURE; PSC-P02 no se crea. No se reconstruyen decisiones previas.

## H30 HYPOTHESIS

Una relación presentacional explícita puede asociar una posición operacional existente y distinguible con contenido situado de GuestPerspective.message, producir textos distintos en A/B para igual estructura operacional y mantener presentación separada de runtime, Evidence, subjectStates, evaluación, K y claim. No requiere viewer, account→subject, session→subject, identidad humana, TES Progression ni nueva máquina de estados.

La dirección ensayada es **existing operational position → situated message presentation**, nunca la inversa.

## VARIABLE UNDER TEST

Únicamente **GuestPerspective.message**. Se amplía el transporte local de presentación para ese campo. No cambian sessionLabel, subjects[].label/status, referencias, contadores, GuestPerspective.state, supervisión, Activity ni App.

Las perturbaciones adversariales y variantes existen sólo en el harness. Los textos deliberadamente inconsistentes no se añaden a las composiciones entregadas.

## WHY A NEW RELATION IS NOW PERMITTED

H26 falsificó NO-NEW-RELATION: los datos operacionales estaban disponibles, pero faltaba contenido narrativo situado relacionado explícitamente con la posición presente. S30 autoriza estudiar esa relación; no preselecciona ni host ni forma.

No se repite una búsqueda general de contenido existente. Se analiza primero la posición runtime y después dónde declarar presentación independiente.

## H26 NARRATIVE ABSENCE CONSOLIDATION

La [falsación H26](session-26-situated-guest-perspective-provenance.md) permanece intacta. Member, parsing de presenterLabel, activityPresentation, news, marca, IDs contextuales/de sujetos, tipo de Evidence y markerRef no proporcionan la relación ausente.

Conocer posición no equivale a disponer de narrativa. La sustitución genérica de todo el recorrido tampoco resolvería la diferencia jardín/fuente frente a mirador/patio. H30 conserva representación neutral sólo donde ya basta la autoridad operacional o derivada.

## PRE-DELTA RUNTIME POSITION MATRIX

La [matriz ejecutada de 12 observaciones](evidence/session-30/pre-delta-runtime-position-matrix.json) y el [análisis previo completo](evidence/session-30/pre-delta-selector-host-analysis.md) se persistieron **antes del delta de contratos/aplicación**. Incluyen snapshots íntegros, message y siguiente presenterLabel para A/B.

Esta parte operacional coincide exactamente en ambas composiciones:

| Observación A y B | Checkpoint | availableActionId | Guest state | P1 state | P2 state | Evidence total/P1/P2 | Suficiencia | Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| initial | ready | enlist-p1 | ready | not-enlisted | not-enabled | 0/0/0 | not-attempted | not-produced |
| enlist-p1 | ready | discover-clue-a | active | enabled | not-enabled | 0/0/0 | not-attempted | not-produced |
| discover-clue-a | clue-a-discovered | activate-p2 | exploring | enabled | not-enabled | 1/1/0 | not-established | not-established |
| activate-p2 | clue-a-discovered | discover-clue-b | exploring | enabled | enabled | 1/1/0 | not-established | not-established |
| discover-clue-b | adventure-established | ausente | complete | enabled | enabled | 2/1/1 | established | established |
| reset | ready | enlist-p1 | ready | not-enlisted | not-enabled | 0/0/0 | not-attempted | not-produced |

Copy previo y affordance: el message era idéntico en A/B, aunque los siguientes labels diferían.

| Observación | Message previo A = B | Siguiente presenterLabel A | Siguiente presenterLabel B |
| --- | --- | --- | --- |
| initial | La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas. | Alistarme | Alistarme |
| enlist-p1 | Estás alistada y habilitada. Todavía no has encontrado ninguna pista. Explora el jardín y registra tu hallazgo. | Encontrar la pista del jardín · yo | Encontrar la pista del mirador · Inés |
| discover-clue-a | Tu pista del jardín está aportada. Activa al huésped 2 para que pueda explorar; activarlo no aporta ninguna pista. | Activar al huésped 2 desde mi cuenta | Activar a Mateo desde mi cuenta |
| activate-p2 | Has habilitado al huésped 2. Todavía no ha aportado pistas. Registra su hallazgo en la fuente cuando lo encuentre. | Encontrar la pista de la fuente · huésped 2 | Encontrar la pista del patio · Mateo |
| discover-clue-b | Las pistas aportadas cumplen la condición de esta aventura. | ausente | ausente |
| reset | La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas. | Alistarme | Alistarme |

La fase de observación identifica la acción recién ejecutada; **availableActionId identifica la siguiente affordance actualmente disponible**. No se confunden.

## SELECTOR CANDIDATE ANALYSIS

| Candidato existente | Evidencia | Decisión |
| --- | --- | --- |
| checkpoint | Igual en A/B, pero ready colapsa initial/enlist-p1 y clue-a-discovered colapsa los dos exploring. | **REJECT AS SELECTOR**; no se modifica. |
| availableActionId | Igual identidad en posiciones equivalentes A/B y tres valores distintos en los momentos situados. | Seleccionado dentro del recorrido probado. |
| GuestPerspective.state | exploring antes y después de habilitar P2. | Insuficiente; valores intactos. |
| subjectStates combination | enabled/not-enabled colapsa enlist-p1/discover-clue-a; enabled/enabled colapsa activate-p2/final. | Insuficiente por sí sola. |
| Evidence/evaluation combination | No cambia al alistar ni al habilitar P2. | Insuficiente por sí sola. |
| checkpoint + subjectStates | Distingue las posiciones ensayadas. | No seleccionado: recompondría una clave con varios valores cuando ya existe la affordance derivada. |
| subjectStates + Evidence/evaluation | También puede discriminar dentro de A/B. | No seleccionado: mayor acoplamiento a estados, conteos y resultados para seleccionar copy. |
| Script expectedCheckpoint / índice de step | expectedCheckpoint colapsa habilitaciones; índice no es posición runtime autoritativa. | No seleccionado. |

Ningún selector usa lugares, nombre de cuenta, labels, IDs de Evidence, parsing de markerRef o identidad de composición.

## SELECTOR DECISION

**availableActionId**, calculado previamente por el runtime desde checkpoint y guards/subjectStates. H30 reutiliza ese resultado; no reproduce su cálculo ni asigna disponibilidad desde Script.

La selección narrativa compara igualdad exacta con una declaración explícita. No localiza copy de presenterLabel ni transforma nombres/lugares. Su suficiencia se acredita en estas posiciones; **available action != journey state** y no se propone como selector universal.

La ausencia final de availableActionId no se convierte en sentinel. No existe una entrada “none”, “complete” ni nueva acción. Sin evaluación establecida, ausencia de acción no acredita completion.

## CHECKPOINT / TES SEPARATION

Checkpoint conserva su función técnica local, aunque resulte insuficiente para seleccionar narrativa:

- checkpoint != TES Progression.
- checkpoint != Experience semantic phase.
- checkpoint sequence != TES Sequence.
- checkpoint transition != TES Event.

No cambia ninguna lista, valor, guard o transición de checkpoint.

## CANDIDATE HOST ANALYSIS

| Host | Evaluación contextual |
| --- | --- |
| ScenarioDefinition | Podría transportar copy técnicamente, pero ya determina sujetos, contextos, acciones y transiciones. Añadir narrativa acoplaría la variación editorial a definición operacional sin necesidad demostrada; los controles requieren Scenario idéntico. No seleccionado. |
| DemoScript | Transporta presentación situada y ya llega al adapter. Permite una relación opcional separada de affordance y Activity, manteniendo Scenario fijo. Seleccionado provisionalmente. |
| GuestPerspectiveReadModel | Es salida proyectada. Usarlo como fuente de su propia narrativa invertiría la autoridad. Rechazado como fuente. |
| Fixture | Aporta datos simulados y cuenta, pero la proximidad de textos no vincula posición y contenido. Extenderlo no aporta una relación o transporte más preciso que Script. No seleccionado. |

El host se elige después de comparar candidatos. Su uso recurrente en H25/H27/H30 no lo convierte en PresentationModel ni arquitectura universal.

## EXPERIMENTAL REPRESENTATION SHAPE

```ts
DemoScript.experimentalJourneyPresentations?: Array<{
  availableActionId: string;
  message: string;
}>;
```

Tres entradas por composición, correspondientes a discover-clue-a, activate-p2 y discover-clue-b **disponibles**. Campo marcado EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. No hay JourneyPhase, registry, resolver, motor narrativo ni nueva entidad.

## REPRESENTATION AUTHORITY

La construcción es mixta y mantiene la dirección de cada autoridad:

| Condición | Fuente / representación |
| --- | --- |
| evaluation.sufficiency == established | Conserva literalmente “Las pistas aportadas cumplen la condición de esta aventura.” |
| Sin Evidence y P1 not-enlisted | “La aventura está disponible. Alistamiento pendiente.” desde datos operacionales existentes. No requiere entrada narrativa. |
| Posición intermedia con declaración aplicable | Texto situado explícito de Script, seleccionado por availableActionId. |
| Posición intermedia sin declaración o sin acción disponible | String vacío, sin inventar lugar, persona ni completion. |

La evaluación establecida tiene prioridad sobre cualquier declaración. El estado inicial neutral también precede al lookup: no se amplía el artefacto por uniformidad.

Los mensajes entregados describen disponibilidad en jardín/mirador, una pista registrada y disponibilidad en fuente/patio. Su correspondencia se acredita dentro de la ruta ensayada; el texto no valida esos hechos. Una declaración editorial incorrecta puede mentir sin alterar el runtime, como muestra el control de contradicción.

## THREADING PATH

```text
Scenario checkpoint + guards + subjectStates
  → existing projectSnapshot availability calculation
  → snapshot.scenario.availableActionId ───────────────┐
                                                     │
resolved DemoScript → existing adapter Script clone  │
  → getSnapshot → projectSnapshot                     │
  → experimentalJourneyPresentations ────────────────┤
                                                     ↓
existing evaluation / initial operational inputs → projectGuestPerspective
  → derived completion OR neutral initial OR explicit situated lookup OR ""
  → GuestPerspective.message → existing App consumer
```

No hay retorno desde message hacia disponibilidad, estados o evaluadores. Reset restaura las fuentes operacionales existentes y vuelve a producir el mensaje inicial.

## BASELINE

[Baseline S30](evidence/session-30/baseline.json): hashes SHA-256 de **221 archivos** del working tree recibido, sin reconstruirlo desde Git. Suite previa: **91/91 pruebas, 23/23 archivos**.

El [control de preservación](evidence/session-30/preservation-check.json) verifica **207 archivos idénticos** y **14 cambios autorizados**, cuyas versiones anteriores están archivadas byte a byte en test-fixtures/h29: cinco archivos de aplicación y nueve harness históricos. Los documentos/trazas previos, App, arquitectura, ADR, TES y PSC se preservan.

El harness pre-delta reproduce las fuentes archivadas idénticas; su primera ejecución y escritura de matriz ocurrieron antes de editar aplicación. Los artefactos del análisis se mantienen separados de la traza posterior.

## CODE DELTA

El [patch de aplicación](evidence/session-30/application-delta.patch) contiene:

- contracts.ts: relación presentacional opcional experimental en DemoScript.
- artifacts.ts / costa-artifacts.ts: tres declaraciones A/B por composición.
- mock-adapter.ts: transporte del nuevo campo y de la acción disponible ya calculada.
- vertical-evaluation.ts: dos parámetros locales y sustitución exclusiva de message.

Las definiciones Scenario se conservan exactamente, incluso aunque convivan en los archivos de artefactos modificados. El evaluador, executeAction/reset, supervisión y resto de GuestPerspective se verifican por igualdad de fuente; las composiciones y frames se comparan contra H29.

El [patch de instrumentación histórica](evidence/session-30/historical-instrumentation-delta.patch) sólo añade rutas de archivo y mocks de fuentes anteriores. No sustituye expectativas históricas por el nuevo copy.

## A CONTROL

Cuenta de Lucía, sujetos Lucía / Huésped 2, status H29 y hechos se conservan. Los seis momentos son:

| Observación | Message A | Message B |
| --- | --- | --- |
| initial | La aventura está disponible. Alistamiento pendiente. | La aventura está disponible. Alistamiento pendiente. |
| enlist-p1 | Exploración disponible en el jardín. | Exploración disponible en el mirador. |
| discover-clue-a | Pista del jardín registrada. La siguiente acción está disponible. | Pista del mirador registrada. La siguiente acción está disponible. |
| activate-p2 | Nueva exploración disponible en la fuente. | Nueva exploración disponible en el patio. |
| discover-clue-b | Las pistas aportadas cumplen la condición de esta aventura. | Las pistas aportadas cumplen la condición de esta aventura. |
| reset | La aventura está disponible. Alistamiento pendiente. | La aventura está disponible. Alistamiento pendiente. |

Cada frame A, incluyendo entradas y resultados completos de evaluación, coincide con H29 al excluir **sólo message**. Reset coincide con initial.

## B CONTROL

Cuenta de Inés, labels Inés / Mateo, status H29, referencias y Activity mirador/patio permanecen. Las tres posiciones situadas presentan B sin residuos jardín/fuente dentro de message.

Los frames B también coinciden íntegramente con H29 salvo message. No se usa el contexto B, la marca ni sus identificadores como selector narrativo.

## CROSS-COMPOSITION SELECTOR CONTROL

A/B tienen iguales snapshots de checkpoint/availableActionId y estados/conteos operacionales por sujeto. Las tres declaraciones situadas difieren y producen mensajes distintos.

Intercambiar únicamente las nuevas declaraciones entre composiciones intercambia exactamente sus messages; los hechos de cada composición se conservan. Otro recorrido renombra demoId, scenario.id, script.id y brand.id manteniendo la declaración: frames y reset quedan idénticos a B.

## REPRESENTATION INDEPENDENCE CONTROL

X/Y cambian únicamente los strings de experimentalJourneyPresentations, conservando claves. En cada A/B se verifica igualdad de Script tras retirar ese único campo y de Scenario completo.

Los tres mensajes intermedios X/Y difieren. Frames íntegros, sujetos, estados, cuenta, contexto, Evidence, Activity, entradas/resultados de evaluación, K/claim y posición runtime coinciden al retirar exclusivamente message. Inicial, final y reset mantienen su representación derivada.

## ACCOUNT INDEPENDENCE CONTROL

Sólo member.name cambia a “Cuenta Demo”. Cambian member.name y sessionLabel; message y todos los otros campos permanecen idénticos. Script y estados/evaluación quedan fijos. Cuenta no adquiere autoridad narrativa ni relación con sujetos.

## SUBJECT PRESENTATION INDEPENDENCE CONTROL

Sólo subjectPresentations cambia a Etiqueta 1 / Etiqueta 2. Cambian labels; message no cambia. La comparación completa excluye únicamente labels. No se interpolan representaciones humanas dentro del mensaje.

## STATUS INDEPENDENCE CONTROL

Cada snapshot vivo mantiene el mapping H29 desde los tres estados existentes. La sección de fuente que calcula status permanece idéntica. El lookup narrativo no consulta strings de status.

Un control aislado mantiene declaración/selector en discover-clue-a y cambia sólo el estado subyacente P2 de not-enabled a enabled: cambia su status, message permanece fijo. Se identifica como entrada contrafactual al projector, no como nueva ruta admitida del provider. La neutralidad inicial sí usa legítimamente el estado operacional P1; esto no convierte status presentation en autoridad.

## ACTIVITY PRESENTATION INDEPENDENCE CONTROL

Sólo title/description de activityPresentation cambia. Activity materializada cambia después de Evidence; message permanece idéntico. La comparación conserva IDs, tiempos, procedencia, orden, Evidence, evaluación y todos los demás campos.

Un control adicional sustituye sólo presenterLabel por un texto sin ubicación: todos los frames completos coinciden. Ni la historia Activity ni el copy de affordance alimentan narrativa presente.

## ABSENCE CONTROL

Retirar la relación completa produce message vacío en las tres posiciones situadas de A/B. Inicial, final y reset se conservan; ningún hecho cambia. No aparece hardcode A ni fallback de member, labels, marca, news, Activity o markerRef.

Vacío es **comportamiento local experimental / NOT PROMOTED**, no política productiva de UX.

## MISMATCH CONTROL

Declarar únicamente nonexistent-runtime-action no selecciona su texto en ninguna posición, no crea checkpoint/acción/Evidence y no cambia evaluación. Intentar ejecutar esa supuesta acción es rechazado por el provider; el snapshot anterior/posterior es idéntico.

Otro control declara sólo discover-clue-b: no selecciona su message mientras la acción disponible sea discover-clue-a o activate-p2; lo selecciona cuando el runtime realmente habilita esa affordance. La presentación no crea el estado del que depende.

## NO-VIEWER CONTROL

Todos los mensajes seleccionados se inspeccionan y se comprueban contra formas de segunda persona, atribuciones personales y nombres de sujeto. Los textos entregados no requieren tú/tu/te, “por ti”, “has habilitado”, “estás”, “eres” o “contigo”, ni infieren género personal.

operationalSessionSubjectRef conserva P1 para su responsabilidad preexistente. No se introduce viewer→subject, cuenta→subject ni sesión→viewer. La segunda persona histórica preservada en App/affordances/Activity no acredita identidad y está fuera de esta variable.

## FACT / PRESENTATION CONTRADICTION CONTROL

Una variante de harness declara en las tres posiciones intermedias: “La condición de la aventura está establecida en el observatorio.” Contradice deliberadamente la presentación comercial y, al inicio de exploración, también la suficiencia todavía not-attempted.

Message cambia; los hechos y resultados íntegros de evaluación, K y claim permanecen iguales. Se registra como **representational inconsistency**, no como modificación factual ni UX admisible. No se añade validador editorial.

## CURRENT-LIVE REGRESSION

El [harness vivo H30](../prototype/src/demo-factory/script-bound-journey-h30.test.ts) importa el provider actual sin mocks de runtime. Spies transparentes registran argumentos/resultados reales.

| Control vivo | Resultado |
| --- | --- |
| A/B frente a traza H29 | Igualdad exacta salvo message; incluye evaluaciones y reset. |
| H25 | Activity situada y su independencia preservadas. |
| H27 | Labels explícitos e independencia de narrativa preservados. |
| H28 | Cuenta y sessionLabel independientes preservados. |
| H29 | Status desde estado operacional preservado en todos los frames. |
| Retail negative control | Todos los frames/reset idénticos a H29. |
| Arrival negative control | Todos los frames/reset idénticos a H29. |
| Completion authority | Evaluación establecida prevalece sobre declaración ajena; ausencia de acción no la sustituye. |

Además del control aislado de checkpoint final con evaluación no establecida, se ejecuta un **recorrido vivo negativo**: sólo la última Evidence recibe un contexto property incompatible. El provider admite la acción según sus reglas existentes y alcanza adventure-established, sin acción siguiente y con dos Evidence; el evaluador devuelve not-attempted / claim not-produced, GuestPerspective.state permanece exploring y message es vacío. El evaluador conjunto no se invoca para ese último conjunto incompatible. Reset restaura initial.

Este último ensayo perturba hechos/contexto intencionadamente para comprobar autoridad; no se presenta como variante X/Y de sólo representación.

## HISTORICAL REPLAY STATUS

Los replay H21–H29 conservan sus resultados y expectativas previas. Las rutas H29 se aplican después de las rutas históricas anteriores, que conservan precedencia. Los módulos archivados mantienen sus bytes; bridges de test reexportan evaluadores compartidos preservados.

**Historical replay != current cumulative behavior verification.** Las pruebas previas siguen comprobando sus versiones históricas; el harness H30 comprueba por separado el código actual y su comparación acumulada contra H29. No se reescriben documentos, baselines ni trazas H21–H29.

## EXECUTION TRACE

[Traza H30](evidence/session-30/execution-trace.json): escrita con creación exclusiva después de superar sus aserciones. Registra hashes de baseline, cinco archivos de aplicación y harness; Scenario/Script, frames completos, reset, inputs del projector y llamadas/resultados de evaluación vertical/conjunta para los controles principales.

Incluye **26 recorridos Family Adventure / 156 observaciones incluyendo resets**: original más once variantes por A/B (24), renombrado de identidad (1) y control vivo negativo de completion (1). Retail y Arrival se registran aparte. Los contrafactuales de proyección están explícitamente separados; la matriz previa aporta otras 12 observaciones históricas.

| Verificación | Resultado |
| --- | --- |
| Suite recibida | 91/91 pruebas; 23/23 archivos. |
| Matriz pre-delta | 1/1; 12 posiciones A/B registradas antes del cambio. |
| Replay tras delta y antes de harness vivo | 92/92; 24/24 archivos. |
| npm run check final | **PASS: typecheck, lint, 93/93 pruebas en 25 archivos, build/PWA.** |
| Preservación baseline | 207 archivos idénticos; 14 cambios autorizados y archivados; 0 cambios inesperados. |
| Navegador / validación visual App | **No ejecutado; no se afirma validación visual.** |

El primer intento del harness vivo detectó una expectativa instrumental incorrecta en ausencia: esperaba undefined en el argumento de narrativa, aunque projectSnapshot ya aplica el default vacío []. Se corrigió la aserción para ese transporte observado; no cambió aplicación ni comportamiento de ausencia. Después se añadió el control vivo de completion negativa y se ejecutó la comprobación completa.

## L3a STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H28. member.name conserva autoridad de presentación de cuenta y sólo cambia sessionLabel.

## L3b STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H27. Relación explícita subjectRef→label sin inferencia desde narrativa.

## L3c SUBJECT STATUS STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H29 / STATE-ONLY. Mapping operacional sin causa, viewer ni género personal.

## L3c JOURNEY NARRATIVE RESULT

EXPERIMENTALLY ADDRESSED / EXECUTION-VERIFIED within A/B. Las posiciones situadas distinguen composición por declaración explícita; inicial y completion conservan autoridad operacional/derivada.

## L3c OVERALL STATUS

EXPERIMENTALLY ADDRESSED within tested A/B, sumando status H29 y narrativa H30. **No cierre productivo universal ni promoción arquitectónica.** La suficiencia del discriminante depende del recorrido actual y de sus affordances distinguibles.

## L4 STATUS

PRESERVED / SOURCE-INSPECTION / OPEN. App permanece idéntica por hash, incluyendo:

- “Mi aventura · Aurora Stay”.
- “Busca las pistas del jardín y de la fuente durante tu estancia.”
- Supervisión: “P1 · Lucía”, “P2 · Huésped 2” y “Cuenta/sesión operativa”.

Son residuos conservados como evidencia de L4. No se reparan ni se afirma ejecución visual de B en navegador.

## L5 STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H25. Activity conserva su relación de representación de ocurrencia; no se convierte en fuente de narrativa presente.

## FALSIFICATION ANALYSIS

| Falsificador H30 | Observación |
| --- | --- |
| Ningún discriminante existente distingue las posiciones | No observado: availableActionId distingue los tres momentos situados A/B. Checkpoint sí resulta insuficiente, sin falsar los otros candidatos. |
| Hace falta parsing de presenterLabel/Activity | No: declaración independiente; perturbaciones preservan message. |
| Copy cambia posición/estado o Evidence | No: igualdad de frames salvo message en X/Y, mismatch y contradicción. |
| Copy cambia evaluación/K/claim | No: llamadas, premisas y resultados íntegros se conservan. |
| Requiere viewer/account/session→subject | No: textos sin perspectiva personal; controles de independencia. |
| Requiere promover checkpoint a TES o nuevas entidades/motores | No: checkpoint intacto y rechazado como selector. |
| Requiere modificar App o resolver L4 | No: App preservada por hash. |

## H30 VERDICT

**SUPPORTED WITH QUALIFICATION.** Se acredita relación explícita local basada en la affordance existente, con separación narrativa/hechos dentro de A/B. No se acredita un selector universal ni corrección editorial automática de toda declaración.

## ARCHITECTURAL CONSEQUENCE

**Recurring architectural presentation pressure observed / NOT PROMOTED.** H25, H27 y H30 alojan relaciones presentacionales en Script, pero su repetición no establece arquitectura universal. DemoScript != PresentationModel.

Architecture v0.5 sigue ACTIVE; ADR-001–005 ACCEPTED, sin cambios ni nueva ADR. No se crean JourneyEngine, NarrativeEngine, PerspectiveEngine, PresentationRegistry, ContentRegistry, PhaseRegistry, MessageResolver, Actor, Operator, Participant o Representative.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract permanecen intactos; PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE, PSC-P02 NOT CREATED. Ningún checkpoint se reinterpreta como Progression, phase, Sequence o Event.

Conocer posición != disponer de contenido; disponer de contenido != crear posición. PresenterLabel != journey message; Activity history != present journey narrative; message presentation != factual authority. Igual ruta con diferente composición puede producir diferente presentación; diferente presentación no debe producir diferentes hechos.

## ARTIFACT QUARANTINE

| Artefacto | Estado |
| --- | --- |
| DemoScriptStep.activityPresentation | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. |
| DemoScript.subjectPresentations | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. |
| Transporte/formato de cuenta H28 | LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED. |
| Mapping state→status H29 | LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED. |
| DemoScript.experimentalJourneyPresentations y transporte H30 | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. |
| Selector por availableActionId y ausencia vacía H30 | Discriminante/ausencia locales; no contrato universal ni política UX. |
| Archivos históricos, bridges, matriz y harness | Instrumentación de evidencia; no nueva autoridad de producto. |

## WHAT H30 DOES NOT PROVE

- No establece viewer, autenticación, identidad humana ni atribución causal.
- No generaliza availableActionId a rutas con acciones reutilizadas, varias affordances simultáneas o posiciones diferentes con igual disponibilidad.
- No garantiza veracidad editorial de texto arbitrario ni valida declaraciones duplicadas.
- No convierte message en prueba de lugar visitado, Evidence, estado o completion.
- No promueve relaciones H25/H27/H28/H29/H30 ni resuelve L4.
- No acredita validación visual App; los controles aislados no acreditan estados alcanzables.
- No define fallback productivo, localización multilingüe ni un modelo universal de narrativa.

## REMAINING PRESSURES

L4 permanece materialmente observable en los literales de App y supervisión. La repetición de relaciones de presentación constituye presión arquitectónica, todavía sin selección ni promoción. La relación viewer/account/session→sujeto sigue ausente y no es necesaria para estos mensajes.

No se abre H31 automáticamente.

| Dimensión | Resultado consolidado |
| --- | --- |
| H30 | **SUPPORTED WITH QUALIFICATION** |
| JOURNEY POSITION SELECTOR | **existing availableActionId; checkpoint rejected as insufficient** |
| L3c JOURNEY NARRATIVE | **EXPERIMENTALLY ADDRESSED / EXECUTION-VERIFIED within A/B** |
| NARRATIVE / FACT AUTHORITY SEPARATION | **SUPPORTED within tested scope** |
| VIEWER RELATION | **NOT INTRODUCED** |
| CHECKPOINT / TES PROGRESSION SEPARATION | **PRESERVED** |
| L3a | **PRESERVED / EXPERIMENTALLY ADDRESSED H28** |
| L3b | **PRESERVED / EXPERIMENTALLY ADDRESSED H27** |
| L3c SUBJECT STATUS | **PRESERVED / EXPERIMENTALLY ADDRESSED H29** |
| L3c OVERALL | **EXPERIMENTALLY ADDRESSED within A/B / NOT PROMOTED** |
| L4 | **PRESERVED / SOURCE-INSPECTION / OPEN** |
| L5 | **PRESERVED / EXPERIMENTALLY ADDRESSED H25** |
| RECURRING PRESENTATION PRESSURE | **OBSERVED / NOT PROMOTED** |
| NEXT MATERIAL PRESSURE | **L4 observed but NOT SELECTED; H31 NOT OPENED** |
