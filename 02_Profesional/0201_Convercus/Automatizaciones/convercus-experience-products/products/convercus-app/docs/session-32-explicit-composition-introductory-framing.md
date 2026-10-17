---
title: "Sesión 32 — Explicit Composition Introductory Framing"
language: es
version: "v1.0"
status: "CLOSED / H32 SUPPORTED WITH QUALIFICATION within Family Adventure A/B"
date: "2026-09-18"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 32 — Explicit Composition Introductory Framing

## H31 CONSOLIDATED INPUT

[S31](session-31-application-composition-framing-provenance.md) permanece CLOSED / H31 FALSIFIED / NO-NEW-RELATION INSUFFICIENT. La marca resuelta ya disponía de autoridad de branding y carecía de transporte local hacia HomePage; la introducción situada carecía de relación declarada. S31 conservó App intacta, sin corrección parcial.

Se reciben sin reconstruir decisiones: L3a/H28, L3b/H27, L3c/H29–H30 y L5/H25 experimentalmente abordados dentro del alcance probado. L4 framing SOURCE-INSPECTED / STOP / OPEN; L4 Supervisión PRESERVED / OPEN. Recurrencia presentacional OBSERVED / NOT PROMOTED.

Architecture v0.5 ACTIVE; ADR-001–005 ACCEPTED; TES y Product Semantic Contract sin cambios. PSC-P01 conserva OPEN / EVIDENCE-BACKED PRESSURE y su cualificación existente; PSC-P02 NOT CREATED. Artefactos H25–H30 en cuarentena.

## H32 HYPOTHESIS

Una relación explícita y mínima puede asociar la composición situada seleccionada con una introducción estática diferente en A/B, sin parsing ni agregación de presentaciones, sin autoridad factual/operacional, sin cambiar Experience/Scenario, Evidence, evaluación, K o claim y con App como consumidor.

La marca existente puede transportarse independientemente para completar el eyebrow. Hipótesis probada dentro de Family Adventure A/B; no arquitectura general de presentación.

## VARIABLE UNDER TEST

Dos cambios autorizados y delimitados en HomePage:

1. La relación nueva proporciona exclusivamente el párrafo introductorio.
2. El eyebrow conserva “Mi aventura” y pasa a consumir la marca resuelta existente.

El h1 sigue renderizando exactamente `adventure.huntName`. Se congelan Supervisión, “Cuenta/sesión operativa”, link fijo a A, título del documento, copy genérico de Activity/carga/errores y viewer identity.

## WHY A NEW RELATION IS NOW PERMITTED

H31 identificó la relación ausente: composición seleccionada → introducción estática declarada. H25, H30, news, contextos y affordances contenían valores relevantes, pero no esa responsabilidad.

S32 autoriza ensayar precisamente esa relación. No reinterpreta H31 como éxito, no corrige su baseline y no concede permiso para construir una arquitectura general.

## TITLE / INTRO AUTHORITY SEPARATION

| Parte visible | Fuente | Responsabilidad |
| --- | --- | --- |
| “Mi aventura” | UI local existente | Etiqueta de vista/canal; no identidad de viewer |
| “ · ” | UI local | Separador |
| Aurora Stay / Costa Clara Resort | runtime.brand.name, seleccionado por manifest.brandRef | Branding, sin equivalencia con propiedad |
| Párrafo introductorio | Declaración H32 del Script seleccionado | Presentación editorial estática situada |
| h1 “Aventura Familiar” | GuestPerspective.huntName existente | Procedencia congelada; no se conecta a Experience.name |

No se crea compositionTitle, propertyName, experiencePropertyName ni campo nuevo de marca. Las props locales de HomePage transportan fuentes distintas; no son una estructura de dominio común.

## TWO-AUTHORITY COMPOSITION TEST

Sobre la misma App se ensayan por separado:

- Marca X/Marca Y, misma intro: cambian los eyebrows; intros, snapshots, acciones y evaluaciones iguales.
- Intro X/Intro Y, misma marca: cambian las intros; eyebrows, snapshots, acciones y evaluaciones iguales.

El shell genérico permanece fijo en ambos. Compartir cabecera no fusiona la responsabilidad de branding con la editorial.

## CANDIDATE HOST ANALYSIS

El [análisis previo](evidence/session-32/pre-delta-host-analysis.md) se escribió **antes del delta de aplicación**. Registra responsabilidades actuales, variabilidad A/B, acoplamiento, transporte, reversibilidad y cambio de autoridad de los seis candidatos.

| Host | Resultado de la comparación |
| --- | --- |
| Manifest | Selecciona referencias/configuración. Incluir copy mezclaría selección y edición; no es necesario. |
| ExperienceDefinition | Compartida por A/B. Variar aquí exigiría duplicación, override o contenido situado en significado compartido. Rechazada. |
| ScenarioDefinition | Varía A/B y transportaría el string, pero añadiría edición a sujetos/estados/acciones/guards/transiciones sin necesidad demostrada. No seleccionada. |
| DemoScript | Identifica la demostración/presentación situada seleccionada y llega resuelto a App. Permite añadir la relación editorial sin modificar reglas. Seleccionado provisionalmente. |
| Fixture | A comparte fixture con Arrival; member/news/Activity no declaran la responsabilidad requerida. No se promueve una noticia ni se usa su proximidad. |
| Artefacto dedicado | Añadiría identidad, catálogo, referencia, validación y transporte sin que se haya falsificado un host acotado existente. No necesario. |

## HOST DECISION

**DemoScript**, como host EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.

El argumento específico es que la intro presenta estáticamente la demostración situada, sin describir un resultado ya ocurrido ni alterar el significado de Experience. La relación con la composición se establece por el `scriptRef` explícito resuelto; `scenarioRef` conserva su validación de compatibilidad.

El uso previo en H25/H27/H30 no basta para seleccionarlo. Los controles H32 acreditan dentro de A/B que este dato puede variar sin modificar las responsabilidades operacionales existentes. No se promueve DemoScript a PresentationModel.

## EXPERIMENTAL REPRESENTATION SHAPE

En [contracts.ts](../prototype/src/demo-factory/contracts.ts), solo dentro de DemoScript:

```ts
// H32: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
// Static introduction for the selected demonstration, not runtime truth,
// branding, journey state or a viewer/subject/stay relationship.
experimentalIntroductoryFraming?: string;
```

Un campo opcional independiente. No se agrupan activityPresentation, subjectPresentations, experimentalJourneyPresentations e intro. No se cambia AppSnapshot, GuestPerspective, SupervisionPerspective ni ResolvedDemoRuntime.

## CONTENT AUTHORITY

Las nuevas declaraciones editoriales canónicas son:

| Composición | Declaración H32 exacta |
| --- | --- |
| A | Una aventura de pistas entre el jardín y la fuente. |
| B | Una aventura de pistas entre el mirador y el patio. |

Proceden de declaraciones explícitas añadidas en Script A/B. **No se derivan** de lugares extraídos de H25/H30, news, Evidence, markerRef o IDs. Que compartan vocabulario con otras presentaciones no establece una dependencia computacional ni transfiere su autoridad.

El campo tiene autoridad para determinar qué introducción se presenta, **no para validar la verdad editorial**, crear lugares, autorizar transiciones o producir Evidence.

## VIEWER GUARDRAIL

Las declaraciones canónicas son estáticas, introductorias, situadas y sin perspectiva personal. No contienen tú/tu/te/ti, eres, estás, has o contigo; el harness comprueba esas formas además de verificar los strings canónicos exactos.

Desaparece “durante tu estancia” del párrafo anterior. Es reducción de una atribución no acreditada, no pérdida de una relación demostrada. “Mi aventura” continúa siendo etiqueta genérica preexistente; no se infiere de su gramática una relación viewer→subject/stay ni account→stay owner.

No se corrige la segunda persona ajena a la variable —affordances, Activity o shell— ni se usa como evidencia de identidad.

## THREADING PATH

```text
Manifest.brandRef → existing resolveDemo → runtime.brand.name
    → App → AppShell → HomePage.brandName
    → "Mi aventura · " + brandName

Manifest.scriptRef + existing Scenario compatibility
    → existing resolveDemo → runtime.script.experimentalIntroductoryFraming
    → App → AppShell → HomePage.introductoryFraming
    → introductory paragraph, when non-empty

provider → unchanged snapshot/read models → existing App rendering
```

Bootstrap ya transportaba Script y BrandArtifact; no se modifica. La intro no atraviesa un nuevo projector ni se inserta en GuestPerspective por comodidad. Su responsabilidad es presentación estática de composición, independiente del snapshot dinámico.

El adapter ya clona el Script completo para sus responsabilidades anteriores; el nuevo campo puede coexistir en esa copia, pero el provider no lo consulta ni lo proyecta. Sus fuentes y reglas se conservan byte a byte.

## APP CONSUMER BOUNDARY

App solo pasa `runtime.brand.name` y `runtime.script?.experimentalIntroductoryFraming` como props independientes. HomePage renderiza su valor; no interpreta IDs ni compone un resumen.

No hay imports desde artifacts.ts/costa-artifacts.ts/fixtures.ts, lookup A/B, parsing o agregación. El control de identidades renombra demoId, scenario.id, script.id y brand.id conservando las declaraciones: framing y hechos permanecen iguales.

La navegación sigue transportando demoId como antes; eso no es selección de intro por branching.

## BASELINE

[Baseline S32](evidence/session-32/baseline.json): **347 archivos** del working tree recibido, incluidos código, pruebas, archivos históricos, documentación/trazas previas, configuración, gobernanza y contrato semántico. No se reconstruye desde Git HEAD.

Suite recibida antes del delta: **93/93 pruebas, 25/25 archivos**. H31 no había cambiado código; se conserva su documento, inventario y evidencia.

[Preservación](evidence/session-32/preservation-check.json):

- **330 archivos idénticos**.
- **4 archivos de aplicación modificados**, con originales archivados byte a byte.
- **12 harness históricos modificados solo como instrumentación**, con originales archivados byte a byte.
- **1 .DS_Store con drift**, registrado separadamente como metadato Finder no fuente; su hash de baseline no se reescribe.
- **0 archivos fuente modificados inesperadamente; 0 ausentes**.

La baseline capturó .DS_Store incidentalmente. La primera ejecución H32 se detuvo por cambio de ese metadato; el control de fuentes lo excluye explícitamente y el audit lo sigue registrando. No se relativizó ninguna comparación de código, configuración o evidencia.

## CODE DELTA

[Patch de aplicación](evidence/session-32/application-delta.patch), cuatro archivos:

| Archivo | Cambio |
| --- | --- |
| contracts.ts | Campo opcional experimental en DemoScript y comentario de límites |
| artifacts.ts | Una declaración de intro en Script A |
| costa-artifacts.ts | Una declaración de intro en Script B |
| App.tsx | Transporte local separado de marca/intro; eyebrow dinámico; párrafo condicional |

No cambian Experience, Scenario, Manifest, Fixture, bootstrap, adapter, evaluadores, proyecciones, estilos ni main.tsx. El harness elimina únicamente las sustituciones autorizadas de la fuente App actual y exige igualdad textual exacta con la App archivada: todo el resto permanece igual.

[Patch de instrumentación histórica](evidence/session-32/historical-instrumentation-delta.patch): enrutamiento de lecturas de fuentes hacia copias S31 donde corresponde; las rutas archivadas de sesiones anteriores mantienen prioridad. H30 usa composiciones S31 archivadas; el test UI histórico usa App/composiciones S31 y conserva su projector anterior. No se alteran expectativas para aceptar el nuevo framing como si fuera histórico.

Se añade un [harness actual H32](../prototype/src/demo-factory/explicit-introductory-framing-h32.test.ts). Las copias test-fixtures/h31 son instrumentación, no otra aplicación de producto.

## A CONTROL

**DOM / integration EXECUTED con App actual**, desde estado inicial, mediante clicks en sus cuatro acciones públicas, navegación y reset.

| Declaración / fuente | Render observado |
| --- | --- |
| runtime.brand.name = Aurora Stay | Mi aventura · Aurora Stay |
| Script A.experimentalIntroductoryFraming | Una aventura de pistas entre el jardín y la fuente. |

Se mantiene la misma intro en initial, enlist-p1, discover-clue-a, activate-p2, discover-clue-b y reset. Cambian los mensajes/estados según H29/H30; la intro no los selecciona ni describe resultados de ejecución.

Frames completos y reset, incluidos argumentos/resultados de evaluación, coinciden con la traza H30. La comparación DOM contra App S31, eliminando solo eyebrow e intro, es exacta.

## B CONTROL

**DOM / integration EXECUTED con la misma App actual**, otra instancia de composición resuelta.

| Declaración / fuente | Render observado |
| --- | --- |
| runtime.brand.name = Costa Clara Resort | Mi aventura · Costa Clara Resort |
| Script B.experimentalIntroductoryFraming | Una aventura de pistas entre el mirador y el patio. |

El párrafo B no contiene jardín/fuente/Aurora. Esto se comprueba para la superficie seleccionada; **no se declara que toda App B carezca de residuos A**: Supervisión continúa congelada.

Frames completos y reset coinciden con H30; la comparación DOM contra App S31 excluye solo los dos nodos autorizados. No se repara huntName, cuenta, estado ni otra presentación al obtener B.

## BRAND TRANSPORT CONTROL

A/B consumen BrandArtifact ya resuelto. La referencia property permanece en Scenario para su responsabilidad contextual y no se lee para producir nombres.

Marca X y Marca Y, aplicadas por separado en el harness de cada composición, cambian únicamente BrandArtifact.name en la entrada. Cambian los eyebrows y las superficies de branding preexistentes que legítimamente usan ese nombre; no cambian intro, Script, estados, acciones, Evidence ni evaluaciones.

No se afirma que solo un nodo de toda App cambie al cambiar la marca: el logo accesible y otras superficies de branding ya eran consumidores.

## BRAND / INTRO INDEPENDENCE CONTROL

En cada A/B:

```text
brand.name: Marca X / Marca Y, intro fija
→ eyebrow distinto; intro idéntica
→ frames/evaluaciones/acciones idénticos

brand fija, intro: "Introducción editorial X." / "Introducción editorial Y."
→ eyebrow idéntico; intro distinta
→ frames/evaluaciones/acciones idénticos
```

Se comprueban todos los momentos, incluido reset. La independencia no se infiere de tipos o de un getter aislado: se observa en App renderizada.

## REPRESENTATION INDEPENDENCE CONTROL

Las variantes X/Y alteran solo la nueva declaración. Manifests/referencias, brand, Experience, Scenario y demás declaraciones permanecen iguales. Los catálogos parten de copias completas del mismo baseline; no se mutan fixtures ni otros artefactos para conseguir la diferencia.

La comparación exige igualdad completa de snapshots, inputs de acciones, argumentos y resultados de evaluación vertical/conjunta, además de Scenario/Experience y Script tras retirar únicamente intro. Eso incluye H25/H27/H28/H29/H30, contextos, Evidence y claim; K aparece en las llamadas reales del evaluador conjunto.

El DOM completo coincide al retirar exclusivamente los dos nodos seleccionados; el eyebrow se compara además por separado y permanece fijo. Navegación a Supervisión/Actividad conserva su DOM y los mismos snapshots.

## FACT / PRESENTATION CONTRADICTION CONTROL

Variante exclusiva del harness:

> Una aventura sin pistas en el observatorio.

Se declara idéntica en cada A/B y se observa literalmente en App, mientras las rutas y la Evidence de pistas siguen siendo las originales. Las acciones, Scenario, Activity, journey message, estados, contextos, Evidence, argumentos/resultados de evaluación, K y claim coinciden íntegramente con el control canónico.

Clasificación: **representational inconsistency**, no factual mutation. El cambio editorial no crea un observatorio en el modelo ni invalida una pista. No se incorpora la frase contradictoria a los Scripts canónicos, y no se crea validador editorial.

## ABSENCE CONTROL

Dos variantes por composición:

1. Se elimina experimentalIntroductoryFraming.
2. Se declara string vacío.

Resultado en la App actual: **no hay párrafo introductorio**; queda un único p en la cabecera, el eyebrow. h1, marca, hechos y resto del DOM se conservan.

No aparece fallback A ni contenido recuperado de H25/H30, news, contextos, Evidence, markerRef o marca. El reset conserva esa ausencia.

**LOCAL EXPERIMENTAL ABSENCE BEHAVIOR / NOT PROMOTED**. No establece política productiva de UX ni tratamiento general de whitespace/localización.

## ACCOUNT / SUBJECT / STATUS / JOURNEY INDEPENDENCE

Perturbaciones independientes en **ambas** composiciones:

| Entrada perturbada | Diferencia observada / comprobación | Intro H32 |
| --- | --- | --- |
| member.name | Cambian cuenta y sessionLabel; comparación completa excluye solo esos campos | Igual en todos los frames/reset |
| subjectPresentations | Cambian labels H27; comparación completa excluye solo labels | Igual |
| experimentalJourneyPresentations | Cambian mensajes situados H30; comparación excluye solo message | Igual |
| activityPresentation | Cambian título/descripción de Activity tras Evidence; comparación excluye solo ese copy | Igual |
| presenterLabel | Cambia affordance y se sigue invocando la acción pública correcta; snapshots/evaluaciones íntegros iguales | Igual |
| news.title/summary | Cambia feed editorial; comparación excluye solo esos campos de news | Igual |
| initialSubjectStates.P1 = enabled | Cambian status inicial, acción disponible y recorrido; se omite legítimamente enlist-p1 | Igual en recorrido/reset |

El último control es **perturbación operacional declarada del Scenario de harness**, no variante de solo representación ni un snapshot falsificado. La App actual muestra “Estado: habilitado” y la primera acción disponible pasa a discover-clue-a. El runtime usa sus reglas existentes; no se exige igualdad factual entre entradas operacionales distintas.

El control inverso X/Y conserva exactamente sessionLabel, labels, status, message y Activity: modificar intro no altera sus autoridades.

## COMPOSITION SWITCH CONTROL

Mecanismo probado: instancias independientes creadas con `resolveDemo(demoId, catalogs)`, montadas mediante createRoot/MemoryRouter y desmontadas al terminar. Se conserva la misma App y ruta de render; cambia la composición seleccionada antes del montaje.

No se afirma hot-switch sin remount. Además:

- Intercambiar solo la intro A/B intercambia los párrafos y conserva la marca propia y todos los hechos.
- Renombrar demoId/scenario.id/script.id/brand.id en B conserva framing y frames completos.

No hay source edits entre ejecuciones ni cambio de reglas para conseguir la variación.

## NEGATIVE CONTROLS

**Retail y Arrival ejecutados en la App actual**, incluidos estado inicial, acciones existentes donde corresponden, navegación y reset.

Ninguno declara H32; la ausencia sigue siendo undefined. No se añade intro Family Adventure ni un campo falso para hacer pasar tipos. No aparece cabecera de aventura en las ramas genéricas.

Los snapshots y reset coinciden con H30. El DOM completo de sus frames y páginas navegadas coincide con App S31, sin excluir nodos. Sus manifests, fixtures, Experience/Scenario/Script y flujo implementado permanecen intactos.

## CURRENT APP DOM / INTEGRATION EXECUTION

[Harness H32](../prototype/src/demo-factory/explicit-introductory-framing-h32.test.ts), sin vi.mock ni snapshots sustituidos:

- App actual con React createRoot, MemoryRouter y jsdom.
- Acciones Family Adventure/Arrival invocadas mediante clicks en los botones renderizados.
- Reset Family Adventure mediante botón; en controles genéricos sin botón de reset, se llama a provider.reset y se remonta.
- Spies transparentes capturan llamadas públicas, evaluación vertical y evaluación conjunta reales.
- Cada frame comprueba eyebrow, intro, h1, message, sessionLabel, labels y status contra sus fuentes/proyecciones.
- Se visitan Supervisión y Activity; la navegación conserva snapshot.
- **35 recorridos de App actual / 201 observaciones incluyendo resets**.
- **4 recorridos adicionales de App archivada S31 / 17 observaciones** para comparación DOM explícitamente separada.

La serialización DOM ordena únicamente atributos para comparar: conserva nombres, valores, texto y orden de elementos. Esto evita confundir el orden de inserción de aria-current tras navegar con una diferencia de UI. No elimina contenido para los controles genéricos; en Family Adventure la comparación histórica adicional retira solo eyebrow/intro, que también tienen aserciones propias.

## BROWSER VISUAL VALIDATION STATUS

**NOT EXECUTED.** Las comprobaciones son DOM/integration bajo jsdom, no validación visual ni de layout, móvil real o navegador.

El entorno tiene navegador de escritorio instalado, pero no había un endpoint CDP activo en 127.0.0.1:9222 al comprobarlo. No se inició una sesión de navegador para este ensayo. El build/PWA correcto tampoco se usa como prueba visual.

## HUNTNAME FREEZE

El h1 continúa siendo `adventure.huntName`. vertical-evaluation.ts permanece idéntico; huntName sigue siendo su literal “Aventura Familiar”.

Experience.name no se conecta a ese campo. La coincidencia entre ambos strings no crea procedencia. Fuente y DOM se comprueban; esta presión permanece observada.

## SUPERVISION FREEZE

Se conservan íntegramente “P1 · Lucía”, “P2 · Huésped 2” y “Cuenta/sesión operativa”, incluida la selección histórica por subject.id. El harness los verifica al navegar a Supervisión en cada recorrido Family Adventure, también B.

No se aplica H27 a SP, no se fusionan GP/SP y no se introduce viewer/account/session→subject. El DOM de Supervisión canónico coincide con App S31.

## FIXED NAVIGATION LINK FREEZE

Se conserva el acceso genérico fijo a `/?demo=hospitality-family-adventure`. El control de igualdad de fuente fuera del delta y las comparaciones DOM genéricas lo preservan.

Navegación/composición es otra presión; no se corrige por proximidad al cambio de cabecera.

## CURRENT CUMULATIVE REGRESSION

| Autoridad/comportamiento | Evidencia sobre código actual |
| --- | --- |
| H25 Activity | Snapshots completos iguales a H30; DOM Activity comprobado; perturbación independiente |
| H27 labels | Proyección/DOM conservados y variantes de labels independientes de intro |
| H28 cuenta | Cuenta/sessionLabel conservados; cambio aislado de member.name no altera intro |
| H29 status | Proyección/DOM conservados; entrada operacional distinta cambia status y conserva intro |
| H30 journey | Mensajes iguales a H30 en ruta canónica; variantes narrativas no alteran intro |
| Estado / Evidence / contextos | Frames y acciones completos iguales al baseline H30 para cambios de solo representación |
| Evaluación / K / claim | Inputs/resultados reales de ambos evaluadores iguales en canónicos y variantes editoriales |
| Reset / navegación | Reset restaura baseline; navegación no modifica snapshot |
| Retail / Arrival | Snapshots/reset H30 y DOM App S31 conservados |

Estas comparaciones se ejecutan en H32 usando provider, evaluadores y App actuales. No se sustituyen por un PASS de replay histórico.

## HISTORICAL REPLAY STATUS

**93 pruebas heredadas siguen pasando**, con las mismas expectativas históricas. La suite total incorpora además el ensayo acumulado H32.

Las copias S31 de los cuatro archivos de aplicación y los doce harness modificados están en test-fixtures/h31. Las lecturas históricas aplican el nuevo routing después del anterior, de modo que una copia H21–H29 ya seleccionada conserva prioridad. La baseline y las trazas previas no se reescriben.

H30 mantiene su nombre histórico de ensayo “current-live” dentro del archivo, pero ahora se ejecuta expresamente como **replay con composiciones S31 archivadas**, con provider/projectors/evaluadores preservados. Ese nombre no se usa para atribuirle verificación de App H32. S31 es una inspección documental preservada, no se inventa un harness de ejecución H31.

**Historical replay != current cumulative verification.** El nuevo harness H32 acredita por separado la aplicación vigente.

## EXECUTION TRACE

[execution-trace.json](evidence/session-32/execution-trace.json), creada con escritura exclusiva después de superar todas las aserciones H32. Incluye:

- Hashes de baseline, App actual y harness.
- Manifests, marca, Experience, Scenario y Script de los recorridos.
- Snapshots completos, acciones ejecutadas, argumentos/resultados de evaluación vertical y conjunta.
- DOM de frames y navegación; eyebrow/intro/h1 observados por separado.
- Controles canónicos A/B, quince variantes por composición y renombrado de identidades.
- Comparaciones previas de App y controles negativos identificados separadamente.

| Comprobación | Resultado |
| --- | --- |
| Suite recibida | 93/93; 25 archivos |
| Replay tras delta, antes del harness H32 | 93/93; 25 archivos |
| Harness H32 | PASS; 35 recorridos actuales y 4 comparaciones con App previa |
| npm run check final | **PASS: typecheck, lint, 94/94 pruebas en 26 archivos, build/PWA** |
| Preservación | 330 idénticos; 16 cambios fuente archivados; drift Finder separado; 0 cambios fuente inesperados |
| Browser visual validation | NOT EXECUTED |

Incidencias instrumentales resueltas antes del registro final: la captura de .DS_Store hizo fallar inicialmente el control de fuente; se segregó como metadato sin rebaselinar. Una comparación de innerHTML literal detectó únicamente distinto orden de atributos tras navegación; se normalizó ese orden preservando todo el contenido. Lint detectó un identificador no usado y espacios de regex en el harness; se corrigieron. Ninguna de estas correcciones modificó aplicación ni expectativas factuales.

## L3a STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H28. Cuenta y sessionLabel conservan su autoridad y comportamiento. No relación de viewer.

## L3b STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H27. subjectPresentations mantiene su relación explícita y separada de intro y Supervisión.

## L3c STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30 dentro de A/B. Status mantiene procedencia operacional; message conserva autoridad mixta y selector availableActionId local. Checkpoint no se reinterpreta ni se rehabilita como selector H30 universal.

## L4 INTRODUCTORY FRAMING RESULT

**EXPERIMENTALLY ADDRESSED / DECLARED-SOURCE / CURRENT APP DOM-INTEGRATION EXECUTION-VERIFIED within A/B.**

La relación explícita produce variación editorial sin afectar hechos. No valida veracidad de copy arbitrario ni promueve política de ausencia o arquitectura productiva.

## L4 TITLE / BRAND RESULT

**EXISTING RESOLVED BRAND AUTHORITY / LOCAL TRANSPORT / CURRENT APP DOM-INTEGRATION EXECUTION-VERIFIED within A/B.**

Se elimina el hardcode Aurora Stay del eyebrow de App. Se conserva UI shell + branding; no se acredita nombre de propiedad, título editorial de composición ni procedencia nueva para huntName.

## L4 SUPERVISION STATUS

PRESERVED / OPEN. Residuos A y encuadre de sesión permanecen materialmente visibles; no se considera L4 resuelto en conjunto.

## L5 STATUS

PRESERVED / EXPERIMENTALLY ADDRESSED H25. Activity conserva autoridad de representación de ocurrencia, no de itinerario o framing.

## RECURRING PRESENTATION PRESSURE

H25 → Activity; H27 → sujetos; H30 → narrativa por posición; H32 → introducción estática de composición.

**RECURRING SCRIPT-BOUND PRESENTATION PRESSURE → STRENGTHENED / NOT PROMOTED.** La recurrencia cuenta con una responsabilidad adicional ejecutada, pero no demuestra que DemoScript sea PresentationModel ni autoriza consolidar todas las relaciones.

## FALSIFICATION ANALYSIS

| Falsificador | Resultado observado |
| --- | --- |
| Ningún host acotado puede expresar la relación sin corromper responsabilidades | No observado: Script opcional conserva responsabilidad editorial; separación operacional acreditada dentro de A/B |
| Exige duplicar Experience o cambiar Scenario | No: ambos preservados en composiciones canónicas; perturbación operacional solo en harness de independencia |
| Exige Manifest como contenedor de copy o reinterpretar News | No: fuentes preservadas; perturbación de news no cambia intro |
| App parsea/agrega H25/H30 o selecciona por IDs | No: fuente inspeccionada, perturbaciones y renombrado conservan intro declarada |
| Framing cambia runtime/Evidence/evaluación/K/claim | No: igualdad completa de frames y evaluaciones en variantes editoriales/branding |
| Intro requiere viewer/subject/stay ownership | No: declaraciones sin perspectiva personal; ninguna relación introducida |
| Requiere resolver huntName/SP/navegación fija | No: fuentes y render preservados |
| Marca e intro no pueden variar independientemente | No: controles bidireccionales pasan |
| Ausencia fuerza un fallback semántico | No: párrafo ausente sin reconstrucción; hechos iguales |
| No puede verificarse la App actual | No: A/B y negativos ejecutados en jsdom; validación visual no afirmada |

No aparece un falsificador dentro del alcance probado. La contradicción editorial demuestra el límite de la hipótesis: una presentación declarada puede ser inconsistente sin cambiar la verdad runtime.

## H32 VERDICT

**SUPPORTED WITH QUALIFICATION dentro de Family Adventure A/B.** La relación introductoria mínima funciona como presentación explícita independiente de branding y de autoridades factuales, con App actual como consumidor.

La cualificación limita el resultado a las composiciones, estados y variantes ejecutados; no establece arquitectura, autoridad editorial universal, relaciones de viewer ni validación visual.

## ARCHITECTURAL CONSEQUENCE

Architecture v0.5 ACTIVE y ADR-001–005 ACCEPTED, sin cambios. No nueva ADR ni Promotion. DemoScript no se convierte en PresentationModel; no se crean PresentationBoundary, PresentationRegistry, PresentationEngine, CompositionPresentation o ContentRegistry.

El transporte es local, separado y reversible. El campo puede retirarse con sus dos declaraciones y props sin cambiar el modelo factual. La recurrencia queda como presión para una hipótesis posterior independiente, no seleccionada aquí.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract intactos. PSC-P01 y su texto preservados; PSC-P02 NOT CREATED.

Static composition framing != journey narrative != Activity history. Declared presentation != factual validation. Brand authority != introductory framing authority. Ninguna referencia de property, cuenta o sujeto adquiere significado adicional por compartir cabecera.

## ARTIFACT QUARANTINE

| Artefacto | Estatuto |
| --- | --- |
| Relaciones H25/H27/H30 | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED |
| Experimentos H26/H28/H29 | Cualificaciones previas intactas; no promoción |
| experimentalIntroductoryFraming H32 | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED |
| Declaraciones A/B y transporte de intro | Ensayo local; no contrato productivo de contenido |
| Transporte brand.name a HomePage | Fuente existente; cambio local, sin entidad de título/propiedad |
| Ausencia de párrafo | LOCAL EXPERIMENTAL ABSENCE BEHAVIOR; no UX general |
| Variantes X/Y/contradicción/perturbaciones | Solo harness; nunca composiciones canónicas |
| Copias históricas, routing y trazas | Instrumentación de evidencia, sin autoridad de producto |

## WHAT H32 DOES NOT PROVE

- Que DemoScript deba alojar universalmente toda presentación.
- Que un lugar en copy exista factual u operacionalmente.
- Que una intro arbitraria sea verdadera, apropiada o coherente.
- Que marca == propiedad o que Experience.name alimente huntName.
- Que se haya introducido viewer, propiedad de estancia o identidad humana.
- Que el hot-switch sin remount funcione.
- Que todo B esté libre de copy A; Supervisión conserva sus residuos.
- Que el layout, navegador, PWA instalada o iPhone real hayan sido validados visualmente.
- Que la ausencia vacía sea una política UX productiva.
- Que L4 completo, L3c o Demo Factory estén cerrados/promovidos.

## REMAINING PRESSURES

La recurrencia de relaciones de presentación en Script queda fortalecida. Supervisión sigue abierta; la procedencia de huntName y el link fijo de navegación siguen observados. Las demás expresiones inventariadas en S31 no se reparan.

Ninguna presión posterior queda seleccionada. No se abre H33 automáticamente.

| Dimensión | Resultado |
| --- | --- |
| H32 | **SUPPORTED WITH QUALIFICATION** |
| INTRODUCTORY FRAMING RELATION | **EXPLICIT / EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED** |
| HOST | **DemoScript, selected experimental host** |
| APP BRAND AUTHORITY | **Existing resolved BrandArtifact / PRESERVED** |
| BRAND / INTRO AUTHORITY SEPARATION | **SUPPORTED within A/B** |
| APP CONSUMER BOUNDARY | **PRESERVED** |
| A/B COMPOSITION FRAMING | **EXECUTION-VERIFIED / CURRENT APP DOM-INTEGRATION** |
| VIEWER RELATION | **NOT INTRODUCED** |
| L3a | **PRESERVED / EXPERIMENTALLY ADDRESSED H28** |
| L3b | **PRESERVED / EXPERIMENTALLY ADDRESSED H27** |
| L3c | **PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30** |
| L4 INTRODUCTORY FRAMING | **EXPERIMENTALLY ADDRESSED within A/B / NOT PROMOTED** |
| L4 TITLE / BRAND | **EXISTING-SOURCE / LOCAL TRANSPORT / DOM-INTEGRATION EXECUTION-VERIFIED** |
| L4 SUPERVISION | **PRESERVED / OPEN** |
| L5 | **PRESERVED / EXPERIMENTALLY ADDRESSED H25** |
| RECURRING SCRIPT-BOUND PRESENTATION PRESSURE | **STRENGTHENED / NOT PROMOTED** |
| NEXT MATERIAL PRESSURE | **Observed but NOT SELECTED; H33 NOT OPENED** |

