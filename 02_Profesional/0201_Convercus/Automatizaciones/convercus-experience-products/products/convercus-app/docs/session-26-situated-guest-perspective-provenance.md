---
title: "Sesión 26 — Situated Guest Perspective Provenance"
language: es
version: "v1.0"
status: "H26 FALSIFIED; inspection STOP; L3 open; no application delta"
date: "2026-09-14"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de audit y reproducción diagnóstica"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 26 — Situated Guest Perspective Provenance

## H25 CONSOLIDATED INPUT

**H26 → FALSIFIED dentro de la baseline actual y la exigencia de no añadir relaciones.** Hay fuentes legítimas para el nombre de cuenta y la affordance disponible, pero falta representación situada explícitamente vinculada a los sujetos. Éste es el primer falsador material: STOP antes de implementar una solución. El audit también identifica la carencia de una fuente para la narrativa situada de estado presente.

Se parte del [resultado consolidado de H25](session-25-script-bound-situated-activity-representation.md). No se revisan sus resultados ni la falsación histórica de H24:

```text
SESSION 20 → CLOSED
H21 → FALSIFIED / historical baseline
H22 → SUPPORTED WITH QUALIFICATION / Experience-based behavior selection
H23 → SUPPORTED WITH QUALIFICATION / situated evaluation context binding
H24 → FALSIFIED / no legitimate existing Activity representation source
H25 → SUPPORTED WITH QUALIFICATION / script-bound Activity representation
L1 → experimentally addressed
L2a/L2b → experimentally addressed
L5 → SCRIPT-BOUND SITUATED REPRESENTATION EXECUTION-VERIFIED within A/B
L3 → EXECUTION-CONFIRMED / OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN

DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
```

## H26 HYPOTHESIS

**H26 — Situated Guest Perspective Provenance.** Dentro de Family Adventure, GuestPerspective podría combinar estado/hechos/evaluación derivados con datos presentacionales ya disponibles en la composición resuelta para representar coherentemente A/B, sin hardcodes específicos de A, inferencia de identidad de sujeto desde cuenta/sesión ni uso de Activity como autoridad narrativa general.

H26 exige inicialmente relaciones existentes. La falsación expresa insuficiencia de esa baseline, no imposibilidad universal de resolver la presión con otro alcance autorizado.

## VARIABLE UNDER TEST

Exclusivamente **L3**, procedencia situada de GuestPerspective. La descomposición L3a/L3b/L3c es diagnóstica y experimental. No se promueve a arquitectura ni se considera suficiente sustituir nombres/lugares por textos genéricos.

El audit se completó antes de crear el harness. Tras identificar el primer falsador sólo se reproduce el problema y se verifican regresiones; no se implementan reparaciones parciales de L3a, L3b o L3c.

## GUEST PERSPECTIVE OUTPUT MAP

Fuentes inspeccionadas: [GuestPerspectiveReadModel y contratos](../prototype/src/demo-factory/contracts.ts), [projectGuestPerspective y evaluación vertical](../prototype/src/demo-factory/vertical-evaluation.ts), [projectSnapshot/adaptador](../prototype/src/demo/mock-adapter.ts), [consumidores App](../prototype/src/app/App.tsx), artefactos [A](../prototype/src/demo-factory/artifacts.ts)/[B](../prototype/src/demo-factory/costa-artifacts.ts), [fixtures](../prototype/src/demo-factory/fixtures.ts) y [resolver](../prototype/src/demo-factory/bootstrap.ts).

La llamada efectiva actual es:

```text
projectGuestPerspective(evaluation, scenario.subjects, subjectStates)
```

No recibe member, BrandArtifact, ExperienceDefinition, contexts, operationalSessionSubjectRef, Script ni availableActionId. El snapshot sí transporta member y acción disponible por otros campos. La composición resuelta contiene más datos, pero su coexistencia no establece una relación de identidad ni una responsabilidad narrativa compartida.

Inventario completo de campos y alternativas textuales del projector. «Fuente candidata» indica legitimidad limitada, no una implementación realizada.

| OUTPUT FIELD / TEXT | CURRENT SOURCE | CURRENT TRANSFORMATION | CURRENT HARDCODE | EXPECTED RESPONSIBILITY / CLASE | CANDIDATE EXISTING SOURCE |
| --- | --- | --- | --- | --- | --- |
| `huntName`: «Aventura Familiar» | Literal del projector | Ninguna | Texto completo | Título presentacional de Experience; no hecho | `ExperienceDefinition.name` ya declara ese mismo nombre en A/B; no declara un nombre distinto de instancia de hunt |
| `state`: ready / active / exploring / complete | `evaluation.sufficiency`, longitud Evidence, `subjectStates["subject-p1"]` | Prioridad: suficiencia established → complete; alguna Evidence → exploring; P1 enabled → active; resto ready | Clave P1 y reglas locales; sin selección narrativa A/B | OPERACIONAL / DERIVED | Estado runtime y evaluación existentes; no copy |
| `discoveredClueCount` | `evaluation.evidence.length` | Cuenta registros, no deduplica por lugar/marcador | Ninguno situado | FACTUAL → DERIVED COUNT | Evidence runtime |
| `sessionLabel`: «Usas la cuenta de Lucía, huésped 1. El huésped 2 ya figura en esta estancia: puedes habilitarlo y registrar su hallazgo desde aquí.» | Literal del projector | Ninguna; no consulta sesión ni cuenta | Frase completa; Lucía y vinculación deíctica a huésped 1 | ACCOUNT PRESENTATION + SUBJECT PRESENTATION + narrativa de capacidad/contexto | `member.name` sólo para cuenta; `operationalSessionSubjectRef` sólo para referencia operacional; ninguno acredita identidad cuenta=sujeto |
| `subjects[].id` | `ScenarioDefinition.subjects[].id` | Copia por `subjects.map()` | Ninguno | Referencia de sujeto de composición, usada también en hechos/operaciones; no display name | SubjectReference existente |
| `subjects[].label`: «Tú · huésped 1» / «Huésped 2 · ya existe en esta estancia» | `id === "subject-p1"` | Bifurcación P1/resto | Dos frases completas; todo sujeto no-P1 se representa como huésped 2 | SUBJECT PRESENTATION y relación con perspectiva | id/type/role permiten referencia/rol, no nombre ni «Tú»; falta relación explícita de presentación situada |
| `subjects[].status`: «Alistada y habilitada» / «Habilitado por ti» | `subjectStates[id] === "enabled"`, después P1/resto | Estado enabled elige rama; id elige texto | Género y «por ti», además de textos fijos | OPERACIONAL + SUBJECT PRESENTATION | enabled es legítimo; nombre, género y referencia humana a quien habilitó no vienen del estado |
| `subjects[].status`: «Sin alistar» / «Sin habilitar» | Cualquier estado no-enabled, después P1/resto | No distingue explícitamente el valor de estado en la segunda bifurcación; utiliza el rol fijo P1/resto | Dos textos y asignación por ID | OPERACIONAL presentado con regla local | `subjectStates`; no proporciona nombres ni identidad de cuenta |
| `subjects[].clueCount` | Evidence que contiene el ID en `subjects` | Cuenta por `some(subject.id === id)` | Ninguno situado | FACTUAL → DERIVED COUNT | Atribución factual existente; no member |
| `message`, ready: «La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas.» | No complete, Evidence vacía, P1 no-enabled | Selección de rama | Frase completa y perspectiva en segunda persona | OPERACIONAL/DERIVED + SITUATED NARRATIVE | Estado/count respaldan la fase local; affordance puede mostrarse por separado; no hay fuente general de narrativa presente |
| `message`, active: «Estás alistada y habilitada. Todavía no has encontrado ninguna pista. Explora el jardín y registra tu hallazgo.» | No complete, Evidence vacía, P1 enabled | Selección de rama | Género, «tú» y jardín | OPERACIONAL/DERIVED + SUBJECT PRESENTATION + SITUATED NARRATIVE | Estado habilitado/count legítimos; lugar y perspectiva humana no transportados |
| `message`, exploring antes de activar P2: «Tu pista del jardín está aportada. Activa al huésped 2 para que pueda explorar; activarlo no aporta ninguna pista.» | No complete, Evidence no vacía, P2 no-enabled | Selección de rama | Jardín, «tu», ordinal humano | FACTUAL/OPERACIONAL + SITUATED NARRATIVE | Evidence/estado respaldan el avance del recorrido probado; no aportan narrativa situada |
| `message`, exploring con P2 enabled: «Has habilitado al huésped 2. Todavía no ha aportado pistas. Registra su hallazgo en la fuente cuando lo encuentre.» | No complete, Evidence no vacía, P2 enabled | Selección de rama; no calcula aquí el contador de P2 | Fuente y «has»; presupuestos de la secuencia local | OPERACIONAL/DERIVED + SITUATED NARRATIVE | Estado/count por sujeto existen; la rama actual presupone la secuencia ensayada; no declara contenido situado presente |
| `message`, complete: «Las pistas aportadas cumplen la condición de esta aventura.» | `evaluation.sufficiency === "established"` | Selección de rama | Texto genérico, sin hardcode específico A | DERIVED, presentado en lenguaje humano | Evaluación existente; no usa copy ni Activity para establecer K |

Los campos `type` y `role` de SubjectReference no se usan para construir labels en el projector actual. `operationalSessionSubjectRef` sí se pasa a SupervisionPerspective, pero no a GuestPerspective. La regla P1 habilitado/ready y las frases en segunda persona son convenciones locales existentes, no prueba de autenticación.

Inventario de consumo y texto añadido por App al presentar GuestPerspective:

| CONSUMPTION / TEXT | CURRENT SOURCE / TRANSFORMATION | HARDCODE / RESPONSIBILITY / CANDIDATE |
| --- | --- | --- |
| Presencia de `snapshot.guestPerspective` | Selecciona Home de aventura y `isAdventure` | Selección de superficie por read model; no deriva identidad |
| `<h1>{adventure.huntName}</h1>` | Copia título | Sin transformación narrativa; candidato Experience.name pertenece al projector |
| `<p role="status">{adventure.message}</p>` | Copia mensaje | Sin transformación; L3 llega directamente a UI |
| Count global + «pista descubierta» / «pistas descubiertas» | Count y comparación `=== 1` | Gramática genérica UI, no decide hechos |
| Lista de sujetos | `subject.id` como key; muestra label/status/clueCount | Copia del read model; sufijos «pista aportada» / «pistas aportadas» por count |
| «Quién puede explorar» | Literal de sección | Etiqueta UI genérica |
| `<p>{adventure.sessionLabel}</p>` | Copia frase | No valida identidad ni la corrige |
| `adventure.state` | No hay consumo directo en App | No gobierna el botón ni el encabezado de siguiente paso |
| `guestActionLabel` | Busca step cuyo actionId coincide con `snapshot.scenario.availableActionId`; toma presenterLabel completo | Relación de affordance ya existente, fuera de GuestPerspectiveReadModel; sin parsing de lugares o nombres |
| «Tu siguiente paso» / «Resultado de la aventura» | Presencia/truthiness de guestActionLabel | Encabezado UI por disponibilidad de etiqueta, no por lectura directa de claim; no se modifica |
| Botón de siguiente acción | Muestra guestActionLabel; callback vuelve a localizar step por availableActionId y envía step.action | Runtime determina disponibilidad/aceptación; Script presenta/suministra la acción de demo, no decide disponibilidad |
| «Cuenta de {snapshot.member.name}» | Campo público member copiado del fixture | ACCOUNT PRESENTATION legítima ya existente; no afirma por sí sola identidad con P1 |
| Logo y alt | `runtime.brand.logoUrl/name` | BRAND PRESENTATION legítima |
| «Mi aventura · Aurora Stay» | Literal de Home, después de recibir GuestPerspective | **L4**, nombre de marca A añadido por App; BrandArtifact es candidato para marca, no narrativa |
| «Busca las pistas del jardín y de la fuente durante tu estancia.» | Literal de Home | **L4**, lugares A añadidos por App; no se intenta remediar |

En la superficie de supervisión, separada de GuestPerspective, App añade además `P1 · Lucía` / `P2 · Huésped 2` por ID, y denomina «Cuenta/sesión operativa» a `sessionSubjectRef`. Son hallazgos de **inspección L4**, no una relación nueva de identidad ni una ejecución/renderizado B.

## L3 DECOMPOSITION

| Presión diagnóstica | Resultado de inspección |
| --- | --- |
| **L3a — session/account display provenance** | Fuente de nombre de cuenta disponible: member.name. La frase sessionLabel actual mezcla esa presentación con sujeto/perspectiva; no existe prueba de identidad cuenta=P1. Sigue sin corregir. |
| **L3b — subject display provenance** | Sólo id/type/role explícitos. Nombres narrativos en otros textos no son una fuente de labels de sujeto. **Primer falsador material; STOP.** |
| **L3c — situated journey/status narrative provenance** | Estado, counts y evaluación disponibles. Faltan contenidos situados legítimamente asociados a la perspectiva presente. Affordance e historia Activity tienen otras responsabilidades. |

Estas divisiones no se convierten en componentes, contratos o conceptos de producto.

## EXISTING SOURCE CANDIDATES

| Candidato inspeccionado | Uso legítimo disponible | Límite |
| --- | --- | --- |
| BrandArtifact | Marca, logo y tokens; Aurora Stay / Costa Clara Resort | No identifica sujetos ni proporciona mensajes de fase |
| ExperienceDefinition | Nombre «Aventura Familiar» y referencia/semántica de Experience | No declara nombres personales, lugares o narrativa por estado |
| DemoFixture.member | Nombre visible de cuenta: Lucía / Inés, con sus member IDs propios | No contiene subjectRef ni relación con P1/P2; no acredita autenticación |
| ScenarioDefinition.subjects | `{type: individual, id: subject-p1/subject-p2, role: guest}` | No contiene display name ni perspectiva «tú» |
| ScenarioDefinition.contexts | Referencias property/booking/stay situadas | IDs contextuales no son narrativa ni directorio de nombres |
| operationalSessionSubjectRef | Identifica la referencia operacional P1 usada por el recorrido | No es identidad de autenticación ni mapping member→subject |
| DemoScript.presenterLabel | Affordance completa de la acción disponible | No se extraen Inés/Mateo/mirador/patio para otros campos |
| DemoScript.activityPresentation | Representación histórica de ocurrencia aceptada, consolidada H25 | No es narrativa presente ni fuente general de labels de sujeto |
| runtime subjectStates | Estado operacional por ID | No proporciona género, nombre de cuenta ni display name |
| runtime Evidence | IDs, atribución, tipos, contexto y contadores derivados | No contiene narrativa de estado o identidad de cuenta |
| vertical evaluation / claim | Suficiencia y admisibilidad derivadas, claim completa | No determina lugares ni nombres a partir del resultado |
| resolved DemoRuntime | Reúne composición resuelta y provider; permite localizar datos existentes | Coexistencia de datos no crea las relaciones semánticas ausentes |
| Fixture news / otros textos | Contenido editorial, en B menciona Inés/Mateo/mirador/patio | Proximidad narrativa no autoriza extraer mappings ni mensajes de estado |

## ACCOUNT / SESSION PROVENANCE

`fixture.member.name → snapshot.member.name → «Cuenta de …»` ya es una relación de presentación de cuenta en App. El harness observa Lucía en A e Inés en B y reproduce esa expresión existente sobre el snapshot público, sin renderizar UI ni añadir campos a GuestPerspective. Es un control de la fuente/expresión de cuenta, no una nueva implementación de sessionLabel.

El nombre `sessionLabel: string` permite conceptualmente representar sólo cuenta/sesión; la forma del read model no obliga a afirmar identidad del sujeto. Por eso **la presentación de cuenta aislada dispone de fuente legítima**. Sin embargo, la frase actual añade «huésped 1» y segunda persona, y la perspectiva de sujetos usa «Tú»: no se puede preservar esa afirmación identificatoria sustituyendo Lucía por Inés y dando el problema por resuelto.

Los hechos siguen atribuidos a P1 y P2; la sesión operacional permanece P1. No se introduce `memberId → subjectRef`, no se equipara el nombre de cuenta con identidad semántica ni se importa una relación de Arrival a Family Adventure. No se aplica una corrección parcial después del STOP de L3b.

## SUBJECT DISPLAY PROVENANCE

Para representar los dos sujetos de Experience de forma situada se necesita una procedencia explícita de su representación humana, vinculada a la referencia de sujeto. A/B sólo declaran id/type/role. El nombre de member es presentación de cuenta; los nombres Inés/Mateo están dispersos en affordance, Activity y news, con responsabilidades distintas.

**Relación ausente exacta:** referencia de sujeto de Experience → representación situada explícita de ese sujeto. Si se conserva «Tú» o se identifica P1 con el titular de cuenta, hace falta además una relación explícita que justifique esa perspectiva cuenta/sujeto. H26 no selecciona cómo deberían expresarse esas relaciones.

El punto de STOP es anterior a afirmar `P1 = Inés`, `P2 = Mateo` o inferirlo por copy. Mostrar sólo IDs o «huésped 1/2» no demuestra que se haya resuelto la representación situada requerida. Que A pareciera coherente históricamente no acredita el mapping que falta en su forma.

## NEXT-ACTION AFFORDANCE PROVENANCE

La relación ya existe fuera del objeto GuestPerspective: runtime determina `availableActionId` desde checkpoint, acciones de Scenario y habilitación; App localiza el step y muestra su `presenterLabel` sin transformación. El callback usa el mismo ID para enviar la acción pública, que runtime vuelve a validar.

| Fase | A: affordance efectiva seleccionada | B: affordance efectiva seleccionada |
| --- | --- | --- |
| Initial | Alistarme | Alistarme |
| Enlisted | Encontrar la pista del jardín · yo | Encontrar la pista del mirador · Inés |
| A@P1 | Activar al huésped 2 desde mi cuenta | Activar a Mateo desde mi cuenta |
| P2 enabled | Encontrar la pista de la fuente · huésped 2 | Encontrar la pista del patio · Mateo |
| A@P1+B@P2 | Sin acción/etiqueta disponible | Sin acción/etiqueta disponible |
| Reset | Alistarme | Alistarme |

El harness comprueba esta selección con los snapshots reales y la expresión inspeccionada de App. No renderiza B ni crea un campo nuevo. Se verifica la relación de affordance existente; no se usa su texto como narrativa general ni para identificar sujetos.

## STATUS NARRATIVE PROVENANCE

SubjectStates respalda habilitación; Evidence respalda conteo/atribución; evaluación respalda suficiencia. En la secuencia probada esos datos permiten distinguir ready, active, exploring y complete. No contienen por sí mismos jardín/mirador/fuente/patio ni el significado humano de «tú» o «por ti».

«Alistado», «pista aportada», «P2 habilitado» y «resultado alcanzado» tienen componentes operativos/derivados observables. El destinatario personal, el lugar y la instrucción situada «sigue explorando aquí» requieren otra procedencia. El projector actual combina ambos planos en frases fijas. Sus frases de fase presuponen además la secuencia local; no se promueve una teoría general de mensajes para cualquier conjunto de Evidence.

**Relación ausente observada en el audit:** fase/estado presente de la perspectiva → contenido situado apropiado para esa perspectiva. H26 no determina la forma de esa relación. La affordance completa puede seguir mostrándose como acción disponible, pero no se transforma para ocupar el lugar de esos mensajes. Activity posterior sigue siendo historia de una ocurrencia, no fuente de guía presente.

## REJECTED SOURCE CANDIDATES

- **Member como identidad del sujeto:** confunde cuenta con sujeto; falta vínculo explícito.
- **Nombres dentro de presenterLabel:** extraerlos o transformar verbos cambia la responsabilidad de affordance y requiere parsing prohibido.
- **activityPresentation como mensaje de fase o directorio personal:** generaliza una relación histórica experimental H25 fuera de su alcance.
- **News/brand/context IDs:** contenido editorial o referencias técnicas sin relación explícita con sujetos/mensajes de fase.
- **Subject ID, Evidence type o markerRef para decidir lugares:** vuelve a hardcodear la narrativa desde identidad factual/operacional.
- **Sustitución por «huésped/pista/lugar» como solución total:** elimina la prueba de situación; no resuelve las relaciones ausentes.

## NO-NEW-RELATION TEST

**INSUFFICIENT.** El audit permite reconocer fuentes legítimas parciales, pero no construir la GuestPerspective completa requerida. No se añade shape, registry, mapping, Actor, Operator, Representative, Participant, Contributor, AccountSubject ni equivalente.

Se detiene la implementación en el primer falsador material de L3b. Las observaciones L3c forman parte del inventario obligatorio, no de una segunda tentativa de solución. El harness posterior sólo reproduce los síntomas y verifica conservación de la baseline; no prueba un candidato reparado ni esquiva el STOP con copy genérico.

## BASELINE

Antes de añadir instrumentación: **87/87 tests PASS, 19 archivos**. La [baseline H26](evidence/session-26/baseline.json) registra 166 archivos de aplicación, configuración, documentación, gobernanza y reproducciones históricas del estado de trabajo recibido. Todos quedan congelados; `allowedChangedFiles` está vacío. No se atribuyen a H26 diferencias anteriores contra HEAD.

Se conservan byte a byte informes, baselines, trazas, harness y fuentes archivadas H21–H25. No se necesita adaptar ninguna reproducción histórica porque no hay delta de aplicación ni contrato.

## CODE DELTA

**Ningún archivo existente cambia.** Sólo se añaden el [harness diagnóstico H26](../prototype/src/demo-factory/situated-guest-provenance-h26.test.ts), este informe y evidencia bajo `docs/evidence/session-26/`.

No se modifica projectGuestPerspective, App, adaptador, Script, activityPresentation, Scenario, Experience, runtime state ni evaluadores. El harness usa spies transparentes sobre exports originales y compara los resultados reales con H25; no sustituye implementaciones, hechos o evaluaciones. No hay fixture comercial nuevo ni variante de solución.

## A CONTROL

Se ejecutan initial, enlist, A@P1, activar P2, A@P1+B@P2 y reset. GuestPerspective completa, todos los snapshots y la entrada/salida de evaluación son iguales a H25. A mantiene Lucía/jardín/fuente y sus textos aceptados. La repetición no acredita que la antigua vinculación narrativa entre cuenta/P1 constituya una relación explícita.

Cuenta visible disponible: Lucía. Evidence conserva `evidence-a-p1 → subject-p1 → marker-a` y `evidence-b-p2 → subject-p2 → marker-b`, con contexto Aurora/AS-8842/stay-AS-8842. Activity mantiene jardín/fuente desde el Script H25. Reset devuelve el snapshot inicial íntegro.

## B CONTROL

Se ejecuta la misma secuencia sobre la misma maquinaria. **GuestPerspective de B es idéntica a la de A en cada fase**, aunque snapshot.member.name es Inés, las affordances son las de Costa y Activity contiene mirador/patio.

| Fase | GuestPerspective B observada | Plano operacional/derivado |
| --- | --- | --- |
| Initial | ready; frase de cuenta Lucía; labels «Tú · huésped 1» / «Huésped 2…» | P1 not-enlisted, P2 not-enabled; 0 Evidence; K not-attempted; claim not-produced |
| Enlisted | active; «Explora el jardín…»; cuenta Lucía | P1 enabled, P2 not-enabled; 0 Evidence; K not-attempted |
| A@P1 | exploring; «Tu pista del jardín…» | 1 Evidence P1; K not-established |
| P2 enabled | exploring; «Registra su hallazgo en la fuente…» | Ambos enabled; sigue 1 Evidence P1; K not-established |
| A@P1+B@P2 | complete; frase de condición cumplida; cuenta Lucía | 2 Evidence P1/P2; admisibilidad y K established; claim established |
| Reset | GuestPerspective inicial | Estados, Evidence, evaluación y Activity devueltos al inicial |

B conserva `evidence-costa-a-p1 → subject-p1 → marker-a` y `evidence-costa-b-p2 → subject-p2 → marker-b`, contexto Costa/CC-205/stay-CC-205 y sesión operacional P1. Se confirma Lucía/jardín/fuente en el read model. **Aurora Stay no aparece en GuestPerspective**: su aparición potencial en Home procede del literal de App y se clasifica separadamente como L4.

## FACT / PRESENTATION SEPARATION

Se comparan por separado estado operacional público y hechos/entrada contextual/evaluación completos, además del snapshot íntegro, contra H25. Los frames contienen argumentos/resultados de `evaluateVerticalEvidence`, tupla y resultado completos del evaluador conjunto, premisa/criterio y claim. La captura de `projectGuestPerspective` muestra sus tres argumentos reales y su resultado original.

Los planos factuales, operacionales y de evaluación permanecen iguales a H25; Activity también. Esto acredita conservación durante el diagnóstico. **No demuestra una reparación presentacional independiente**, porque no se implementó una GuestPerspective distinta. La prueba positiva de independencia de Activity de H25 sigue pasando, sin generalizarla a GuestPerspective.

La [traza diagnóstica](evidence/session-26/execution-trace.json), capturada el **2026-09-14T16:52:21.174Z** (17:52:21 Europe/Lisbon), contiene:

- `controls[0/1].frames`: cinco snapshots inicial/acciones y entradas/resultados factuales y de evaluación.
- `controls[0/1].reset`: snapshot público de reset verificado.
- `controls[0/1].observations`: seis fases con argumentos efectivos del projector, candidatos disponibles, expresión de cuenta existente y affordance seleccionada.
- Huellas de baseline/harness, primer falsador y clasificación final de L3a/L3b/L3c.

No se renderiza B. La expresión de cuenta y selección de affordance se reproducen desde sus datos públicos, con inspección de su consumidor; no se presentan como un test de DOM B. La escritura opcional `H26_RECORD_PATH` exige destino nuevo y no sobrescribe la captura principal en ejecuciones ordinarias.

| Verificación | Resultado |
| --- | --- |
| Suite previa | 87/87 PASS, 19 archivos |
| H26 diagnóstico y captura | 1/1 PASS; reproduce H26 FALSIFIED |
| H25 + H24 histórico + H23 + H22 + H21 histórico + vertical Sesión 20 | 15/15 PASS, 6 archivos |
| Full suite final | 88/88 PASS, 20 archivos |
| Typecheck | PASS |
| Lint | PASS |
| Build TypeScript + Vite + PWA | PASS |

PASS del harness significa reproducción correcta del falsador, no apoyo a H26. Desde `products/convercus-app/prototype/`:

```sh
npm test -- src/demo-factory/situated-guest-provenance-h26.test.ts
npm test -- src/demo-factory/script-bound-activity-h25.test.ts src/demo-factory/situated-activity-provenance-h24.test.ts src/demo-factory/situated-evaluation-context-h23.test.ts src/demo-factory/experience-stable-selection-h22.test.ts src/demo-factory/composition-boundary-h21.test.ts src/demo-factory/family-adventure-vertical.test.ts
npm run check
```

## L3 RESULT

**L3 → EXECUTION-CONFIRMED / OPEN.** Las fuentes existentes son insuficientes para la perspectiva completa requerida.

```text
L3a ACCOUNT DISPLAY
→ SOURCE AVAILABLE for account-only display
→ existing App expression verified from public data
→ GuestPerspective sessionLabel UNCHANGED / OPEN

L3b SUBJECT DISPLAY
→ NO LEGITIMATE EXISTING SOURCE / OPEN
→ FIRST MATERIAL FALSIFIER / STOP

L3c JOURNEY NARRATIVE
→ operational/derived inputs AVAILABLE
→ situated present-state narrative source ABSENT / OPEN
```

La ausencia de display de sujeto y la ausencia de narrativa presente se documentan como relaciones ausentes distintas; no se selecciona su forma futura ni se promueven las subdivisiones.

## L4 STATUS

**L4 → PRESERVED / SOURCE-INSPECTION FINDING / OUT OF SCOPE.** App intacto. El audit registra los literales de marca/lugares de Home y de sujeto en supervisión, además de los consumidores de GuestPerspective. Ninguno se corrige ni se eleva a hallazgo de renderizado B por esta sesión.

## L5 STATUS

**L5 → PRESERVED / SCRIPT-BOUND SITUATED REPRESENTATION EXECUTION-VERIFIED within A/B.** Los snapshots y la regresión H25 conservan las Activity jardín/fuente de A y mirador/patio de B, así como independencia, ausencia y rechazo bajo el alcance H25.

`activityPresentation` permanece EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. No se usa como autoridad narrativa de GuestPerspective. H24 permanece FALSIFIED bajo su baseline histórica.

## FALSIFICATION ANALYSIS

| Falsador previsto | Observación / decisión |
| --- | --- |
| Inventar mapping cuenta→sujeto | Sería necesario para afirmar identidad de cuenta/P1 sin relación explícita; no se hace. La ausencia contribuye al STOP de L3b. |
| Reutilizar Activity como narrativa general | Candidato rechazado: historia posterior y perspectiva presente tienen responsabilidades diferentes. |
| Parsear presenterLabel | Candidato rechazado para nombres/lugares; sólo se conserva como affordance completa. |
| Añadir shape/registry/arquitectura | Haría falta una relación ausente para resolver subject display/narrativa; H26 no la autoriza. **Primer falsador de insuficiencia de baseline.** |
| Hardcodear A/B en proyección | No se intenta; hardcodes existentes continúan como síntoma reproducido. |
| Presentación cambia hechos/evaluación | No hay candidato reparado; la reproducción conserva hechos/evaluación/Activity de H25. No se declara prueba positiva inexistente. |
| Regresión de A | No observada: snapshots completos iguales y suite vertical PASS. |

No existe un impedimento externo. La falta de relación requerida es evidencia interna al experimento, por lo que el veredicto es FALSIFIED, no INCONCLUSIVE. El STOP se respeta sin sustituirlo por una solución parcial.

## H26 VERDICT

```text
H26 → FALSIFIED
L3a ACCOUNT DISPLAY → source available; GuestPerspective unchanged / OPEN
L3b SUBJECT DISPLAY → no legitimate existing source / OPEN
L3c JOURNEY NARRATIVE → situated source absent / OPEN
NO-NEW-RELATION → INSUFFICIENT
L4 → PRESERVED / SOURCE-INSPECTION
L5 → PRESERVED / EXPERIMENTALLY ADDRESSED within A/B
NEXT MATERIAL PRESSURE → OBSERVED but NOT SELECTED
```

## ARCHITECTURAL CONSEQUENCE

La composición contiene material situado, pero no todas las relaciones necesarias para representarlo con responsabilidades legítimas en GuestPerspective. H25 resolvió una relación distinta y no la convierte automáticamente en fuente general de contenido.

Architecture v0.5 → ACTIVE / unchanged. ADR-001–005 → ACCEPTED / unchanged. No se crea ADR, contrato, servicio, registry ni shape. La siguiente sesión no queda autorizada automáticamente a adoptar una forma concreta de las relaciones ausentes.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract → unchanged. PSC-P01 → OPEN / unchanged. PSC-P02 → NOT CREATED. Group → NOT INTRODUCED en esta sesión; las formas históricas ajenas al ensayo se conservan.

```text
DEMO COMPOSITION ≠ RUNTIME FACT ≠ DERIVED EVALUATION ≠ READ MODEL ≠ UI LOCAL STATE
account/session ≠ subject identity
operationalSessionSubjectRef ≠ authentication identity
GuestPerspective ≠ Activity history
presenterLabel ≠ activityPresentation
state-derived message ≠ situated content source
display name ≠ semantic identity
content similarity ≠ shared responsibility
presentation ≠ factual authority
```

La coincidencia narrativa entre account name, acciones y nombres del Script no establece identidad semántica. Evidence conserva su atribución explícita, y contenido presentacional no decide enabled, conteo, admisibilidad, K o claim.

## WHAT H26 DOES NOT PROVE

- No resuelve L3 ni demuestra GuestPerspective situada correcta para B.
- No acredita mapping entre cuenta, sesión operacional, sujeto y autenticación.
- No selecciona shape o ubicación para display de sujeto o narrativa presente.
- No demuestra que falta todo contenido situado: cuenta, marca, Experience y affordances ya tienen fuentes legítimas limitadas.
- No invalida H25 ni extiende su shape experimental a otras responsabilidades.
- No corrige ni verifica globalmente UI B, ni promueve L3a/L3b/L3c a arquitectura.
- No demuestra imposibilidad de una solución bajo un futuro alcance distinto expresamente autorizado.

## REMAINING PRESSURES

Se observan la procedencia explícita de representación de sujetos, la justificación de la perspectiva cuenta/sujeto cuando se use segunda persona y la procedencia de narrativa situada de estado presente. L4 sigue abierto y fuera de alcance. L5 mantiene su consolidación experimental; persisten las cualificaciones H23/H25 previas.

**La siguiente presión material queda observada, pero NO SELECCIONADA. H27 no se abre automáticamente.**
