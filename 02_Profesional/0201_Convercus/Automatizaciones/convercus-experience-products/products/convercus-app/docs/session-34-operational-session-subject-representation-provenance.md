---
title: "Sesión 34 — Operational Session Subject Representation Provenance"
language: es
version: "v1.0"
status: "CLOSED / H34 SUPPORTED WITH QUALIFICATION within Family Adventure A/B"
date: "2026-09-18"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 34 — Operational Session Subject Representation Provenance

## H33 CONSOLIDATED INPUT

[S33](session-33-operational-supervision-subject-representation-provenance.md) permanece CLOSED / SUPPORTED WITH QUALIFICATION. NO-NEW-RELATION SUFFICIENT para identificar sujetos de Supervisión mediante `SupervisionPerspective.subjects[].id`. Presentación humana NOT REQUIRED para el propósito diagnóstico probado. Separación GP/SP y frontera de consumo preservadas; A/B CURRENT APP DOM-INTEGRATION VERIFIED en S33.

L3a/H28, L3b/H27, L3c/H29–H30, L4 framing/H32, L4 sujeto supervisor/H33 y L5/H25 se reciben preservados y experimentalmente abordados. L4 sesión supervisora estaba OPEN. Recurrencia Script-bound OBSERVED / QUALIFIED BY H33 / NOT PROMOTED. No se reconstruyen decisiones anteriores ni se promueven relaciones H25–H33.

Architecture v0.5 ACTIVE, ADR-001–005 ACCEPTED, TES y Product Semantic Contract unchanged. PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE unchanged; PSC-P02 NOT CREATED.

## H34 HYPOTHESIS

La relación operacional existente que produce `sessionSubjectRef` basta para representar neutralmente esa referencia en Supervisión, sin cuenta, autenticación, viewer, ownership, identidad humana o relación nueva, y sin alterar runtime, sujetos, Evidence, evaluación, K o claim.

Relación ensayada: existing operational session subject reference → neutral diagnostic representation. Condición NO-NEW-RELATION. No se ensaya session subject → account owner/authenticated user/viewer/human identity.

## VARIABLE UNDER TEST

Sólo el par diagnóstico compuesto por el `dt` «Cuenta/sesión operativa» y el `dd` que recibe `supervision.sessionSubjectRef`. El delta finalmente necesario afecta exclusivamente al texto del `dt`; valor, expresión del `dd`, estructura y estilo quedan iguales.

H33, resto de SP, GP, Activity, marca, introducción, huntName y navegación quedan congelados. La cuenta puede continuar apareciendo en sus superficies legítimas H28; H34 no modifica esos textos.

## WHY NO NEW RELATION IS AUTHORIZED

SP ya recibe la referencia y las guards ya le asignan una responsabilidad operacional. Primero se contrasta esa autoridad con la afirmación de UI. La palabra «Cuenta» excede lo acreditado, pero no falta información para mostrar la referencia operacional. Overclaim in copy != missing data. Reducir copy a la autoridad existente no crea semántica.

## SESSION SUBJECT SOURCE INSPECTION

La [inspección previa al delta](evidence/session-34/pre-delta-source-inspection.md) documenta decisión y matrices antes de editar App. El [inventario de usos](evidence/session-34/reference-use-inventory.txt) abarca ambos campos en fuentes, tests, archivos históricos y documentación del programa, excluyendo dependencias/build y trazas serializadas. Las trazas se usan como evidencia histórica, no como productores.

| Campo / capa declarante | Productor | Consumidores | Efecto operacional | Semántica respaldada | No respaldado |
| --- | --- | --- | --- | --- | --- |
| ScenarioDefinition.operationalSessionSubjectRef | Scenario A/B: subject-p1 | projectSnapshot; executeAction | Selección usada en guards enlist/activate | Referencia de sujeto asociada al mecanismo local de sesión | Cuenta, principal autenticado, viewer, ownership |
| actions[].subjectRef / subjects[].id | Scenario A/B | Admisión de acciones | Enlist exige sujeto declarado, estado esperado e igualdad con session ref; activate exige otro sujeto y session subject enabled | Correlación operacional explícita entre referencias | Identidad humana de quien ejecuta |
| subjectStates[session ref] | Estado inicial y transiciones admitidas | Oferta/admisión de activate | Condición de habilitación | Dependencia de estado local | Autenticación o permisos productivos |
| SP.sessionSubjectRef | projectSupervisionPerspective copia su argumento | App SystemPage | Ninguno al renderizar | Transporte literal de referencia | Validación universal de pertenencia/identidad |
| fixture.member | Fixture → snapshot / GP H28 | Presentación de cuenta | Ninguno sobre selección de session ref | Cuenta como fuente separada | member→operationalSessionSubjectRef |
| Par dt/dd de SystemPage | Literal App + SP | Render diagnóstico | Ninguno | Valor proyectado; responsabilidad operacional inspeccionada | Asociación con cuenta añadida por copy |

`MockDataAdapter` copia Scenario al construirlo, mantiene la referencia durante acciones/reset y entrega el campo a `projectSupervisionPerspective()`. El proyector no consulta member, Script ni nombres. `bootstrap` resuelve los artefactos y construye el provider sin añadir mapping de identidad.

Las guards no equivalen a autenticación: `executeAction` recibe una acción, no un actor, credencial o principal. Enlist comprueba igualdad entre sujeto destino y referencia de sesión; activate comprueba habilitación de ésta y destino distinto. Evidence mantiene su propia atribución y checks de estado/tipo. La referencia de sesión no sustituye al sujeto de Evidence.

## SEMANTIC SUPPORT MATRIX

| Pregunta | Estado | Límite preciso |
| --- | --- | --- |
| A. Referencia a un sujeto | SUPPORTED | A/B seleccionan un ID declarado en subjects y enlist correlaciona por igualdad |
| B. Sujeto asociado al mecanismo operacional de sesión | SUPPORTED | Uso efectivo de selección/estado en guards locales; no deducido sólo del nombre del campo |
| C. Sujeto que puede ejecutar ciertas acciones | NOT SUPPORTED como identidad del ejecutor | Sí están respaldadas las restricciones sobre sujetos destino y estado; quién ejecuta humanamente permanece NOT DETERMINED |
| D. Identidad de cuenta | NOT SUPPORTED | No existe mapping member→session ref |
| E. Identidad autenticada | NOT SUPPORTED | No existe principal/credencial en este flujo |
| F. Viewer | NOT SUPPORTED | No existe relación viewer→subject |
| G. Titularidad/ownership | NOT SUPPORTED | Ninguna declaración atribuye propiedad |

«NOT SUPPORTED» expresa ausencia de autoridad en las fuentes inspeccionadas, no demostración universal de inexistencia de cuentas, autenticación o propiedad.

## CURRENT COPY DECOMPOSITION

«Cuenta» agrega una asociación no declarada. La barra yuxtapone cuenta y sesión como si el mismo valor acreditase ambas. «Sesión operativa» tiene soporte en la selección utilizada por las guards locales. El valor `subject-p1` es referencia de sujeto, no ID de cuenta, alias P1 o nombre humano. La corrección elimina la atribución excedente sin modificar el dato.

## ACCOUNT NEGATIVE AUTHORITY

`fixture.member → account presentation H28` y `operationalSessionSubjectRef → operational responsibility` siguen separadas. No se ha encontrado `member → operationalSessionSubjectRef` ni `account → Experience subject`. La perturbación independiente de member.name comprueba esa separación sobre App vigente.

Removing unsupported account language != proving that no account exists operationally. H34 sólo establece que esta fuente no autoriza esa afirmación. No se crea mapping para conservar la palabra ni se formula una teoría negativa universal sobre cuentas/autenticación.

## H33 / SESSION REPRESENTATION SEPARATION

H33 conserva `SP.subjects[].id` como identificación diagnóstica de cada tarjeta. H34 muestra la referencia seleccionada para una responsabilidad operacional distinta. La correlación está respaldada por las comparaciones explícitas de las guards, no sólo por observar dos strings iguales. Value equality != new identity relation; ninguna igualdad acredita cuenta o viewer.

El proyector recibe un string opcional y lo copia: no valida por sí solo que esté en subjects. El control opaco documenta precisamente ese límite, sin crear un nuevo sujeto.

## CANDIDATE NEUTRAL REPRESENTATIONS

| Candidato | Resultado |
| --- | --- |
| Referencia de sesión operativa | Ambiguo: podría interpretarse como identificador de sesión |
| Sujeto de sesión operativa | Seleccionado: sujeto asociado al mecanismo existente; el valor sigue siendo su referencia literal |
| Referencia operacional de sujeto | Neutral pero omite la responsabilidad de sesión que sí está respaldada |
| sessionSubjectRef como campo crudo | Alternativa suficiente; no necesaria para el alcance demostrado |
| Cuenta/usuario/operador/titular o nombre humano | Rechazado; necesita relación no declarada |

## REPRESENTATION DECISION

`Sujeto de sesión operativa` + `supervision.sessionSubjectRef` literal. En A y B resulta «Sujeto de sesión operativa · subject-p1» como par dt/dd; el separador de esta explicación no se añade a la UI. No se afirma persona, autenticación, cuenta, viewer o ownership. Es una representación diagnóstica local, no una definición nueva de sesión en TES.

## NO-PARSING ANALYSIS

La expresión de valor permanece `{supervision.sessionSubjectRef}`. No hay split, regex, replace, substring, sufijos, índice, branch por referencia/composición o mapping a P1/nombre. El harness exige igualdad de todo App con la copia S33 tras reemplazar exclusivamente el literal `dt`. El replace usado en esa aserción compara código fuente; no transforma referencias de producto.

## NO-NEW-RELATION ANALYSIS

SUFFICIENT dentro de A/B: el dato y la responsabilidad operacional existen. No se añade relación presentacional, campo, contrato, lookup, transporte o fuente de identidad. No es necesario representar cuenta/viewer/usuario autenticado para identificar diagnósticamente esta referencia. No se activa STOP.

## APP CONSUMER BOUNDARY

Se conserva Scenario → adapter/proyector → SupervisionPerspective → App → render. SystemPage consume el campo ya recibido; no consulta Scenario, member, Script, subjectPresentations o fixtures para explicarlo. El rótulo no varía por A/B ni por el valor de la referencia.

## BASELINE

[Baseline](evidence/session-34/baseline.json): 391 archivos del programa antes del delta; excluye dependencias, build, `.git`, `.DS_Store`, tsbuildinfo y la evidencia S34 recién creada. No se utiliza HEAD como baseline porque el árbol contiene trabajo heredado de otras sesiones. Se archivan App S33 y harness H33 byte a byte antes de editar.

[Check inicial](evidence/session-34/baseline-check.log): typecheck, lint, 95/95 tests en 27 archivos y build/PWA PASS. [Auditoría de preservación](evidence/session-34/preservation-check.json): 389 archivos iguales, un archivo de producto cambiado, un harness histórico adaptado, cero archivos ausentes y cero cambios inesperados. Gobernanza, semántica y evidencia S33 permanecen idénticas.

## CODE DELTA OR STOP

Único [delta de producto](evidence/session-34/application-delta.patch), una línea de App/SystemPage:

```diff
- <div><dt>Cuenta/sesión operativa</dt><dd>{supervision.sessionSubjectRef}</dd></div>
+ <div><dt>Sujeto de sesión operativa</dt><dd>{supervision.sessionSubjectRef}</dd></div>
```

No se modifican runtime, guards, contratos, proyector, Scenario, Script, Fixture, evaluadores, CSS o navegación. Se añade harness H34 y evidencia local. El [delta de instrumentación histórica](evidence/session-34/historical-instrumentation-delta.patch) se documenta por separado. STOP no activado.

## A CONTROL

App actual con `hospitality-family-adventure`: initial → enlist-p1 → discover-clue-a → activate-p2 → discover-clue-b → reset. Cada fase visita Home/Mi aventura, Supervisión y Activity. El par permanece `Sujeto de sesión operativa / subject-p1`. No usa lenguaje de cuenta/viewer en ese par.

Snapshots, inputs, llamadas/resultados de ambos evaluadores y acciones coinciden con S33. El DOM de Home/Activity es idéntico; Supervisión sólo cambia en el dt seleccionado. Se comprueban todos los valores SP, incluidos headings H33 y atribución.

## B CONTROL

Misma App con `hospitality-family-adventure-costa`, mismo recorrido y controles. La representación de sesión es idéntica a A porque ambas seleccionan subject-p1. No depende de Inés, Lucía, marca, intro, contexto o H27. Cada composición conserva sus propios hechos y presentación situados, comparados contra su propia baseline.

## ACCOUNT INDEPENDENCE CONTROL

En cada composición se perturba únicamente member.name a «Cuenta H34». Cambian la cabecera de cuenta y GP.sessionLabel a «Cuenta de Cuenta H34». El snapshot sólo difiere en member.name y GP.sessionLabel; SP completo y la representación H34 quedan iguales en todas las fases/reset. No se demuestra account→sessionSubjectRef.

## SUBJECT PRESENTATION INDEPENDENCE CONTROL

Sólo DemoScript.subjectPresentations cambia a Participante Alfa/Beta. GP muestra esas etiquetas; SP entero, headings H33 y par H34 permanecen iguales. Acciones y evaluaciones no cambian. Los nombres de esta perturbación son autoridad de GP, no nuevos labels supervisores.

## BRAND / INTRO / JOURNEY / ACTIVITY INDEPENDENCE CONTROL

Cuatro perturbaciones independientes por composición: brand.name, experimentalIntroductoryFraming, experimentalJourneyPresentations y activityPresentation. Cada una cambia su superficie legítima; ninguna modifica SP o el par de sesión en ninguna fase. Marca/intro no cambian snapshots; narrativa sólo GP.message; Activity sólo title/description. Se comparan facts completos después de excluir únicamente esos campos autorizados.

## STATE / EVIDENCE INDEPENDENCE CONTROL

Las acciones públicas producen estados not-enlisted/not-enabled → enabled/not-enabled → enabled/enabled; Evidence por sujeto pasa [0,0] → [1,0] → [1,1]. El claim pasa de not-produced a established mediante evaluación legítima. La referencia y representación de sesión siguen iguales. Reset restaura el snapshot inicial y conserva la referencia. No se reconstruye el par a partir de estado, Evidence o claim.

## SESSION SUBJECT VARIATION CONTROL

ISOLATED COMPOSITION OBSERVATION: en copias de catálogo/Scenario exclusivamente de harness, se varía únicamente operationalSessionSubjectRef entre subject-p1 y subject-p2, tanto en A como en B. Se usa resolver/provider real, getSnapshot y App actual en /system. La representación cambia al valor seleccionado con el mismo rótulo. Todos los demás campos del snapshot son iguales; no se ejecutan acciones.

No se acredita una ruta operacional con subject-p2: la oferta inicial de enlist depende del estado, mientras la admisión exige igualdad con la referencia de sesión. Esa variante sería incoherente con la guard de enlist-p1. El control se limita a transporte/proyección/render, no modifica semántica productiva ni corrige guards. Los catálogos originales permanecen intactos.

## OPAQUE REF OBSERVATION

ISOLATED PROJECTOR / READ MODEL: `opaque:session-subject/X` entra exclusivamente como argumento del proyector, con sujetos/estados originales y evaluación inicial vacía. El SP resultante sólo cambia sessionSubjectRef. Se entrega a App actual mediante getSnapshot sustituido de forma explícita.

Se renderiza exactamente `Sujeto de sesión operativa / opaque:session-subject/X`; no hay alias, nombre o parsing. No se modifica Scenario, no se crea sujeto, no se ejecuta acción y no se afirma pertenencia o validez productiva de la referencia. Prueba el consumidor y transporte literal, no semántica de una composición nueva.

## OTHER SUPERVISION FREEZE

H33 subject IDs, exists, estado, recuento, Evaluación compartida, Criterio K, Evidence recibida, Admisibilidad conjunta, Suficiencia K, Afirmación derivada y Evidence y atribución quedan intactos. La comparación DOM excluye sólo el contenido del dt seleccionado; conserva el dd y todo lo demás. También se contrastan valores con el snapshot.

## HUNTNAME FREEZE

GP.huntName y su h1 permanecen idénticos. Se verifica el h1 contra GP en cada captura y todo Home contra App/traza S33. No se conecta huntName con Experience.name.

## NAVIGATION FREEZE

El acceso fijo `/?demo=hospitality-family-adventure` permanece igual. El freeze de todo App y las comparaciones completas de Home/Activity preservan enlaces y navegación. No se resuelve esta presión en H34.

## CURRENT APP DOM / INTEGRATION EXECUTION

EXECUTED: App actual importada directamente, React createRoot, MemoryRouter y jsdom. Provider real, acciones mediante botones públicos, navegación y reset, spies transparentes de executeAction y ambos evaluadores. 16 recorridos actuales: A/B canónicos, seis perturbaciones por composición y Retail/Arrival. 89 observaciones de fase/reset y 267 capturas DOM de tres superficies.

Separadamente se ejecutan cuatro recorridos de App S33 archivada: 17 fases/reset y 51 capturas para comparación. Cinco observaciones aisladas actuales: cuatro de variación de referencia A/B y una opaca, con cinco capturas. Total H34: 111 observaciones y 323 capturas DOM. Sólo la opaca sustituye getSnapshot; las cuatro variantes usan provider real sin acciones. Ninguna observación aislada acredita un recorrido operacional nuevo.

## BROWSER VISUAL VALIDATION STATUS

NOT EXECUTED. No se valida layout en navegador, móvil o usabilidad visual. DOM/integration EXECUTED no equivale a browser visual. El resultado acredita procedencia y preservación operacional local, no preferencia de usuarios por el rótulo o referencia técnica.

## NEGATIVE CONTROLS

Retail (`retail-baseline`) y Arrival (`hospitality-stay`) se ejecutan con App actual y S33 archivada. Conservan snapshots, acciones, evaluaciones y DOM completo de Home, Activity y panel genérico durante sus fases/reset. GP/SP familiar permanecen ausentes. No se añade campo, rótulo o fallback de sesión: absence remains absence.

## CURRENT CUMULATIVE REGRESSION

H25 Activity, H27 GP labels, H28 account display, H29 status, H30 message, H32 brand/intro y H33 subject IDs se verifican sobre App actual durante recorridos y perturbaciones. Comparación con App S33 montada por separado y su traza original. No se sustituye acreditación vigente por replay.

Check final: typecheck PASS, lint PASS, 96/96 tests en 28 archivos, build/PWA PASS. La única diferencia de producto frente a S33 es el rótulo seleccionado. Ver [log final](evidence/session-34/final-check.log) y [resumen de verificación](evidence/session-34/verification-summary.json).

## HISTORICAL REPLAY STATUS

H33 congelaba expresamente «Cuenta/sesión operativa» y todo App. Se preservan sus aserciones y se redirigen su import/lectura de App a la copia byte-identical S33. Nombre, comentario, método y procedencia se etiquetan como replay histórico; su variable opcional de grabación pasa a H33_REPLAY_RECORD_PATH. No sobrescribe la traza S33 ni se presenta como App vigente.

El nuevo harness `operational-session-subject-h34.test.ts` importa App actual. El resto de replays, informe y evidencia S33 permanecen sin cambios. Las copias originales de App/harness H33 se verifican contra hashes de la baseline S34.

## EXECUTION TRACE

[Traza H34](evidence/session-34/execution-trace.json): snapshots completos, inputs, acciones, llamadas/resultados de evaluación vertical y cross-subject, DOM de Home/Supervisión/Activity, par de sesión, perturbaciones, reset, variantes aisladas y observación opaca. Sólo se escribe tras superar todas las aserciones, con creación exclusiva, sin sobrescribir evidencias anteriores.

Reproducción: `npm run check` desde prototype. Para nueva traza, definir H34_RECORD_PATH con una ruta nueva. Los hashes de App, harness y baseline vinculan la evidencia con las fuentes ejecutadas. El [resumen](evidence/session-34/verification-summary.json) contrasta esos hashes y recuentos.

Durante preparación se corrigió un import del nuevo harness que apuntaba a h34/App en vez de la copia h33/App; typecheck detectó el error antes de ejecutar controles. No requirió cambio de producto ni afectó a las fuentes operacionales. Se conserva la distinción entre corrección de instrumentación y falsador semántico.

## L3a STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H28. Cuenta desde member.name, independiente de referencia de sesión. Sin account→subject.

## L3b STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H27. GP conserva labels situadas; no adquieren autoridad sobre sesión supervisora.

## L3c STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30. Estados desde subjectStates y mensajes desde la relación experimental/affordance existente; no reconstruyen la referencia.

## L4 FRAMING STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H32. Marca resuelta e introducción conservan sus autoridades y presentación.

## L4 SUPERVISION SUBJECT STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H33. Encabezados sujetos = IDs operacionales literales, sin H27 o nombres humanos.

## L4 SUPERVISION SESSION RESULT

EXISTING OPERATIONAL SOURCE / LOCAL NEUTRAL RENDER / CURRENT APP DOM-INTEGRATION VERIFIED within A/B. Se elimina la afirmación de cuenta no respaldada; se conserva referencia, responsabilidad operacional y toda la semántica ejecutable.

## L4 REMAINING PRESSURES

huntName, navegación fija y restante terminología supervisora siguen preservados y sin seleccionar. H34 no demuestra una necesidad de representación humana supervisora, autenticación, viewer o propiedad. El hallazgo no cierra toda L4.

## L5 STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H25. Activity mantiene presentación Script-bound y atribución existente; su perturbación no afecta sesión supervisora.

## RECURRING PRESENTATION PRESSURE

OBSERVED / FURTHER QUALIFIED / NOT PROMOTED. H34 se suma a H33 como contraevidencia local a «all presentation belongs in Script»: esta representación diagnóstica usa autoridad operacional existente. Se mantiene la distinción emergente entre presentación situada/editorial y representación operacional/diagnóstica.

No se promueve «derive operational presentation / declare experiential presentation» a principio arquitectónico. No se crea ADR, PresentationBoundary ni propietario universal de presentación.

## FALSIFICATION ANALYSIS

| Falsador | Resultado observado |
| --- | --- |
| Semántica existente insuficiente sin cuenta/viewer/authentication | No observado: selección y guards respaldan la referencia diagnóstica |
| Necesita member, H27, Script o mapping nuevo | No observado: seis perturbaciones independientes conservan SP/par |
| Necesita parsing, branch A/B o alias | No observado: dd literal, variantes p1/p2 y referencia opaca |
| Modifica refs, estado, Evidence, evaluación, K o claim | No observado: snapshots/evaluaciones iguales a S33, fuentes congeladas |
| Exige corregir huntName, navegación o terminología colateral | No observado: freeze de código y DOM completo salvo dt |
| Variante de referencia acredita nuevo recorrido válido | No se afirma: sólo transporte aislado; sin acciones con guards incoherentes |

No se activa falsador bajo el alcance probado. Los límites de tipo/validación de una referencia opcional y la inexistencia de autoridad sobre el ejecutor humano no se rellenan con inferencias de UI.

## H34 VERDICT

SUPPORTED WITH QUALIFICATION. NO-NEW-RELATION SUFFICIENT para la representación diagnóstica local probada. Cualificaciones: A/B, mecanismo operacional simulado, variantes sólo de transporte, referencia opaca no validada productivamente y ausencia de validación visual/usabilidad. El resultado no identifica a una persona o cuenta.

## ARCHITECTURAL CONSEQUENCE

Architecture v0.5 y ADR-001–005 unchanged. Frontera de consumidor preservada, sin abstracción, campo o relación nueva. Evidencia experimental local, no promoción arquitectónica.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract unchanged. PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE unchanged; PSC-P02 NOT CREATED. No cambia admisibilidad, K, claim, estados o atribución. Rendering a declared reference != creating a new identity relation. Remover copy no autorizado no prueba la proposición contraria.

## ARTIFACT QUARANTINE

H25–H33 y H34 permanecen EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. Revertir el literal de dt restaura el único delta de producto, sin migración o modificación de datos. Copias históricas y harness son instrumentación, no composición productiva. H35 NOT OPENED.

## WHAT H34 DOES NOT PROVE

No prueba identidad autenticada, viewer, propiedad, cuenta=sujeto, actor humano de una acción o validez de cualquier referencia arbitraria. No acredita nueva ruta con subject-p2, nuevo sujeto opaco, autenticación productiva, validación visual ni suficiencia para todos los Scenarios/futuros roles. No convierte Script o la derivación operacional en regla universal de presentación.

## REMAINING PRESSURES

huntName, enlace fijo a A y otra terminología diagnóstica se observan sin seleccionarlas. Cualquier futura necesidad de cuenta/viewer/operador humano tendría que acreditar su relación correspondiente; H34 no la crea. NEXT MATERIAL PRESSURE OBSERVED BUT NOT SELECTED. H35 no abierto.

| Dimensión | Veredicto final |
| --- | --- |
| H34 | SUPPORTED WITH QUALIFICATION |
| NO-NEW-RELATION | SUFFICIENT |
| SESSION SUBJECT AUTHORITY | EXISTING OPERATIONAL SOURCE |
| ACCOUNT CLAIM | REMOVED AS UNSUPPORTED |
| VIEWER / AUTHENTICATION RELATION | NOT INTRODUCED |
| APP CONSUMER BOUNDARY | PRESERVED |
| A/B SESSION REPRESENTATION | DOM-INTEGRATION VERIFIED |
| L3a | PRESERVED / EXPERIMENTALLY ADDRESSED H28 |
| L3b | PRESERVED / EXPERIMENTALLY ADDRESSED H27 |
| L3c | PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30 |
| L4 FRAMING | PRESERVED / EXPERIMENTALLY ADDRESSED H32 |
| L4 SUPERVISION SUBJECT | PRESERVED / EXPERIMENTALLY ADDRESSED H33 |
| L4 SUPERVISION SESSION | EXISTING-SOURCE / LOCAL NEUTRAL RENDER / EXPERIMENTALLY ADDRESSED H34 |
| L5 | PRESERVED / EXPERIMENTALLY ADDRESSED H25 |
| RECURRING SCRIPT-BOUND PRESENTATION PRESSURE | OBSERVED / FURTHER QUALIFIED / NOT PROMOTED |
| NEXT MATERIAL PRESSURE | OBSERVED BUT NOT SELECTED |
