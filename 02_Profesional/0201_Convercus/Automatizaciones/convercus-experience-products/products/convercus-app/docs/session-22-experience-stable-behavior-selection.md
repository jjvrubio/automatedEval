---
title: "Sesión 22 — Experience-Stable Behavior Selection"
language: es
version: "v1.0"
status: "experiment executed; H22 supported with qualification; no architectural promotion"
date: "2026-09-13"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Sesión 22 — Experience-Stable Behavior Selection

## H21 CONSOLIDATED INPUT

**H22 → SUPPORTED WITH QUALIFICATION dentro del ámbito probado.** Cambiar los dos selectores de identidad de Scenario por su referencia existente a Family Adventure permite seleccionar las proyecciones y la evaluación compartidas en A y B. Los controles existentes Retail y Hospitality Arrival conservan su comportamiento. Esto no acepta B como demo completa.

Se parte de la [ejecución consolidada de H21](session-21-composition-boundary-factory-reusability-execution.md) y su [auditoría](session-21-composition-boundary-factory-reusability-audit.md):

```text
SESSION 20 → CLOSED → FIRST VERTICAL DEMO
           → EXECUTABLE WITH PRESENTATION GAPS
H21 → FALSIFIED para su baseline congelada
```

Última frontera superada en H21: manifest/artifacts → `resolveDemo()` → runtimes distintos → providers distintos → snapshots iniciales genéricos. Primer falsador material: **L2a**, selección de proyecciones Family Adventure por identidad de Scenario A.

La nomenclatura se precisa desde esta sesión: L2a = `scenario.id → projection selection`, EXECUTION-CONFIRMED en H21; L2b = `scenario.id → evaluation selection`, SOURCE-INSPECTION FINDING en H21, sin ejecución de acciones entonces. L1/L3/L4/L5 entran como hallazgos de inspección. Los resultados posteriores se atribuyen a H22, sin reescribir H21.

El hallazgo que gobierna el ensayo es local: la identidad particular de Scenario no fue un selector estable entre las composiciones Family Adventure probadas. No se convierte en regla universal de dominio.

## H22 HYPOTHESIS

**H22 — Experience-Stable Behavior Selection.** Dentro de Family Adventure, dos composiciones que resuelven la misma Experience pueden seleccionar el mismo comportamiento ejecutable específico mediante su relación resuelta con esa Experience, sin utilizar la identidad particular del Scenario como proxy y sin conceder ese comportamiento a otras Experiences.

## VARIABLE UNDER TEST

El discriminante de los dos puntos de selección del adaptador: `scenario.id` pasa a `scenario.experienceRef`. La observación se realiza sobre perspectivas iniciales, comandos públicos y llamadas reales de evaluación durante las acciones de Evidence.

## CONTROLLED VARIABLES

Se mantienen los Scenario IDs distintos, la Experience compartida, los manifests, fixtures, marcas, Scripts, acciones, checkpoints, sujetos, sesión P1, habilitación y atribución de Evidence. Se mantienen evaluadores, contexto fijo, K = A AND (B OR C), admisibilidad conjunta y premisa de autoridad. Permanecen congeladas las proyecciones, sus textos, App.tsx, estilos y narrativa de Activity.

La [baseline de H22](evidence/session-22/baseline.json) registra 78 archivos previos: fuentes, composiciones, contratos y documentos protegidos, además de los resultados de H21. El harness verifica sus huellas, con dos excepciones declaradas: adaptador y adaptación del harness histórico. No se modifica la semántica de Scenario/Script ni `DemoProvider`.

## EXPERIMENTAL SELECTOR CANDIDATE

```ts
scenario?.experienceRef === "experience:family-adventure@1"
```

Se utiliza la relación explícita ya resuelta por `resolveDemo()`. No se deduce la Experience por número de sujetos, P1/P2, acciones, checkpoints ni forma del Script. El literal es un candidato experimental local; no se introduce un catálogo de comportamientos.

## WHY EXPERIENCE IS TESTED

Inspección previa del [contrato](../prototype/src/demo-factory/contracts.ts) y del [bootstrap](../prototype/src/demo-factory/bootstrap.ts):

| Frontera | Referencia disponible y uso actual |
| --- | --- |
| `ResolvedDemoRuntime` | Contiene `experience?: ExperienceDefinition` y `scenario?: ScenarioDefinition`. |
| Scenario / artefactos resueltos | `ScenarioDefinition.experienceRef: string`; A y B referencian `experience:family-adventure@1`. |
| Resolución | `requiredArtifact(catalogs.experiences, scenario.experienceRef, ...)` valida la existencia de la Experience antes de construir el provider. |
| Construcción del provider | `new MockDataAdapter(fixture, scenario)` ya recibe ese Scenario completo. |
| Construcción del adaptador | Conserva una copia del Scenario con su `experienceRef`. |
| Proyección y acciones | `projectSnapshot()` recibe el Scenario; `executeAction()` accede a `this.scenario`. |

La ruta mínima utiliza directamente `scenario.experienceRef` en ambos puntos. **No requiere threading, cambio de bootstrap ni nuevo contrato.** El `id` del objeto Experience es `family-adventure`; la clave referenciada y validada en el catálogo es `experience:family-adventure@1`. Se prueba esta última relación.

## WHAT EXPERIENCE DOES NOT MEAN

No se afirma `Experience = Behavior`, ni `one Experience → exactly one behavior`. La referencia a Experience no es una ontología de comportamiento ni una fuente nueva de autoridad semántica. El ensayo no introduce BehaviorRef, CapabilityRef, BehaviorProfile, ExperienceEngine, registros de estrategia o arquitectura de plugins. Las capabilities preexistentes no participan en el nuevo discriminante.

## BASELINE

Antes de editar se reprodujo H21 y pasó la suite existente: **83/83 tests, 15 archivos**. Se verificaron las 55 huellas originales de H21. Su hash consolidado permanece:

```text
b21a44cc80cfe3d64ce753a5120bd4229a53938cddc2068f1d608d83d0570eb1
```

Se archivó el [adaptador exacto de H21](../prototype/src/demo-factory/test-fixtures/h21/mock-adapter.ts), byte a byte, antes del cambio. Su SHA-256 coincide con la baseline histórica:

```text
2329da2c2bf75683fe7fc04910d3fed0097d2b23b4c168af7281240cbb4d5b3b
```

El [harness H21](../prototype/src/demo-factory/composition-boundary-h21.test.ts) ahora importa ese adaptador mediante sustitución de módulo exclusivamente en el test y comprueba su huella en la ubicación archivada. Sigue usando la lógica intacta de `resolveDemo()`, comprobando el resto de los archivos congelados y deteniéndose ante la ausencia inicial de perspectivas B, sin acciones ni reset. Es una reproducción histórica explícita, no una expectativa de que el código H22 mantenga el defecto.

Los informes, baseline y traza originales H21 quedan intactos. El archivo histórico sólo se importa desde pruebas, no desde la aplicación. El nuevo informe se guarda directamente en `docs/`; la baseline y la traza técnica H22 se guardan en `docs/evidence/session-22/`.

## CODE DELTA

El cambio de código de aplicación está limitado a **dos líneas** de [mock-adapter.ts](../prototype/src/demo/mock-adapter.ts):

```diff
- if (scenario?.id === "family-adventure") {
+ if (scenario?.experienceRef === "experience:family-adventure@1") {

- if (this.scenario?.id === "family-adventure") this.evaluation = evaluateVerticalEvidence(this.evidence);
+ if (this.scenario?.experienceRef === "experience:family-adventure@1") this.evaluation = evaluateVerticalEvidence(this.evidence);
```

El [harness H22](../prototype/src/demo-factory/experience-stable-selection-h22.test.ts) reconstruye el archivo esperado aplicando exactamente esas dos sustituciones al adaptador archivado y exige igualdad con el archivo actual. Los demás añadidos son instrumentación de pruebas, evidencia y documentación; el README del producto enlaza este informe.

## POSITIVE CONTROLS

| Control | Composition A | Composition B |
| --- | --- | --- |
| Demo | `hospitality-family-adventure` | `hospitality-family-adventure-costa` |
| Scenario ID | `family-adventure` | `family-adventure-costa` |
| Experience ref | `experience:family-adventure@1` | `experience:family-adventure@1` |
| Objeto Experience resuelto | Mismo objeto del catálogo | Mismo objeto del catálogo |
| Provider | Instancia propia de `MockDataAdapter` | Instancia propia del mismo prototipo |
| Datos de cuenta iniciales | Lucía | Inés |
| Perspectivas iniciales | Guest y supervision presentes | Guest y supervision presentes |
| Estado inicial | P1 not-enlisted, P2 not-enabled; sin Evidence ni claim | Igual estado, propio del provider B |

No se igualan Scenario IDs ni se introduce una implementación específica para B.

## NEGATIVE CONTROLS

| Demo existente | Experience | Observación |
| --- | --- | --- |
| `retail-baseline` | Sin Scenario ni Experience declarada | Sin perspectivas Family Adventure al inicio y tras reset; snapshot inicial igual al adaptador anterior. |
| `hospitality-stay` | `experience:arrival-welcome@1` | Sin perspectivas Family Adventure al inicio, tras `confirm-arrival` y tras reset; snapshots iguales a la baseline. La acción no invoca evaluación Family Adventure. |

Retail es un control de ausencia de relación, **no una segunda Experience declarada**. Arrival es el control real de otra Experience. No se fabrica una demo negativa. Se conserva la inicialización neutral preexistente `evaluateVerticalEvidence([])` en constructor/reset del adaptador genérico; no produce perspectivas Family Adventure en estos controles. La ausencia de llamada de evaluación documentada para Arrival se refiere a su acción de Evidence.

## L2a RESULT

**Selección por Experience verificada en ejecución.** Ambos snapshots iniciales contienen guest y supervision, con estado inicial sin Evidence. El primer falsador material histórico de H21 queda superado en el código H22. Los controles negativos no reciben esas perspectivas.

## L2b RESULT

**Selección por Experience verificada en ejecución de acciones.** En B, `enlist-p1` habilita P1 sin Evidence y sin llamada de evaluación por la acción. `discover-clue-a` acepta `evidence-costa-a-p1`, atribuida sólo a P1, e invoca una vez el evaluador vertical real y una vez su evaluador conjunto. El snapshot muestra una Evidence y sufficiency `not-established`.

Se continúa con las dos acciones existentes restantes para comprobar persistencia de la selección: habilitar P2 no aporta Evidence ni reevalúa; `discover-clue-b` incorpora Evidence de P2 e invoca de nuevo ambos evaluadores compartidos. El resultado observado es `established`. Esto demuestra selección y continuidad de la ruta, **sin acreditar integridad contextual**.

El gate antiguo L2b era un hallazgo de inspección en H21. H22 aporta ejecución directa del selector nuevo en ese punto; no atribuye retrospectivamente una ejecución de L2b a H21.

## EXECUTION TRACE

La [traza principal H22](evidence/session-22/execution-trace.json) se registró el **2026-09-13T10:51:31.100Z** (11:51:31, Europe/Lisbon). Contiene composiciones, entradas de comandos, snapshots completos, argumentos y resultados reales de evaluadores, controles negativos y reset. Incluye huellas de baseline y adaptador ejecutado.

| Fase A y B | P1 / P2 | Evidence por sujeto | Evaluación durante la acción | Sufficiency / claim |
| --- | --- | --- | --- | --- |
| Inicial | not-enlisted / not-enabled | 0 / 0 | Ninguna acción | not-attempted / not-produced |
| `enlist-p1` | enabled / not-enabled | 0 / 0 | No | not-attempted / not-produced |
| `discover-clue-a` | enabled / not-enabled | 1 / 0 | Sí, una llamada vertical y una conjunta | not-established / not-established |
| `activate-p2` | enabled / enabled | 1 / 0 | No | not-established / not-established |
| `discover-clue-b` | enabled / enabled | 1 / 1 | Sí, una llamada vertical y una conjunta | established / established |
| Reset | not-enlisted / not-enabled | 0 / 0 | Inicialización neutral vacía | not-attempted / not-produced |

La sesión sigue atribuida a P1. Se preservan los payloads suministrados; activar sujetos no añade Activity de Evidence. El reset devuelve exactamente el snapshot inicial.

Los controles usan `resolveDemo()` y el provider público. Para observar L1 y la invocación de L2b se emplean spies transparentes sobre exports de evaluadores: llaman a las implementaciones originales, sin sustituir resultados ni cambiar código o estado privado. La evidencia principal de selección es observable también en los snapshots públicos. No se renderiza ni navega B en esta sesión.

## REGRESSIONS

**A permanece aceptada sin regresión observada.** Se compara cada snapshot completo de A —inicial, cuatro acciones y reset— con el adaptador congelado de H21 y todos coinciden. Además pasan los diez tests existentes de Sesión 20, incluido el recorrido de UI con navegación, habilitación, atribución, evaluación y reset. No se repite aceptación manual de navegador; se conserva la aceptación histórica.

| Verificación | Resultado |
| --- | --- |
| Suite antes del cambio | 83/83 PASS, incluida reproducción de H21 |
| Focalizados H22 + H21 histórico + vertical A | 12/12 PASS, 3 archivos |
| Suite completa posterior | 84/84 PASS, 16 archivos |
| Typecheck | PASS |
| Lint | PASS |
| Build TypeScript + Vite + PWA | PASS |

Desde `products/convercus-app/prototype/`:

```sh
npm test -- src/demo-factory/experience-stable-selection-h22.test.ts src/demo-factory/composition-boundary-h21.test.ts src/demo-factory/family-adventure-vertical.test.ts
npm run check
```

Las pruebas ordinarias no sobrescriben la traza. Para una nueva captura, indicar otro destino existente mediante `H22_RECORD_PATH`, conservando la ejecución principal. H21 continúa pasando porque reproduce su falsador histórico, no porque H21 se haya vuelto supported.

## OUT-OF-SCOPE LEAKS OBSERVED

| Leak | Estado al terminar H22 | Evidencia y límite |
| --- | --- | --- |
| L1: contexto fijo | **EXECUTION-CONFIRMED** | El comando B lleva `stay-CC-205` y booking `CC-205`; el evaluador vertical recibe ese payload intacto. La llamada real anidada recibe Evidence remapeada y contexto con `propertyRef: aurora-resort`, `bookingRef: AS-8842`, `stayRef: stay-AS-8842`. Está capturado en `positiveControls[1].frames[2]` y `[4]`, campos `evaluationCalls` y `crossCalls`. |
| L3: copy de guest | **EXECUTION-CONFIRMED** | `positiveControls[1].frames[0].snapshot.guestPerspective.sessionLabel` dice Lucía, aunque el member B es Inés. Mensajes tras alistamiento/A/activación mencionan jardín y fuente en lugar de mirador/patio. |
| L4: literales de App | **SOURCE-INSPECTION FINDING** | App.tsx permanece congelado; no se renderiza B. Observar texto en un read model no confirma su presentación en App. |
| L5: narrativa de Activity | **EXECUTION-CONFIRMED** | Los snapshots B tras las acciones de Evidence contienen Activity «Pista del jardín encontrada» y «Pista de la fuente encontrada», identificadas por los IDs de Evidence Costa. |

L1 se confirma por argumentos reales de evaluación, no por el resultado K. Ninguno de estos leaks se repara. No impiden observar la selección y, por tanto, no falsifican H22 bajo este protocolo.

## H22 FALSIFICATION ANALYSIS

| Falsador previsto | Resultado observado |
| --- | --- |
| La referencia no discrimina A/B frente a otras Experiences | No observado: A/B seleccionadas, Arrival excluida; Retail sin relación excluido. |
| Otra demo recibe perspectivas o ruta de evaluación Family Adventure | No observado en los controles existentes probados. |
| Transportar la relación exige nuevo contrato arquitectónico o semántico | No: ya llega en Scenario. |
| Aparece regresión de A | No observada: snapshots iguales a baseline y regresión automatizada PASS. |
| La evaluación sigue dependiendo de Scenario A | No: B invoca el evaluador con ID de Scenario propio. |

No se presenta un falsador material H22 ni impedimento externo. El harness usa aserciones secuenciales y registra el veredicto sólo al completar los controles; una primera contradicción detiene ese ensayo. No se añade una abstracción para salvarlo.

## H22 VERDICT

```text
H22 → SUPPORTED WITH QUALIFICATION
L2a → EXPERIENCE-BASED SELECTION EXECUTION-VERIFIED
L2b → EXPERIENCE-BASED SELECTION EXECUTION-VERIFIED
EXPERIENCE AS LOCAL SELECTOR → SUPPORTED within tested scope
NEXT MATERIAL PRESSURE → contextual binding / situated content
                         → OBSERVED, NOT SELECTED
```

La cualificación es obligatoria: H22 no prueba un mapeo general Experience→Behavior, no prueba integridad contextual, no prueba transporte de contenido, no repara históricamente H21 y no prueba reutilización completa de la Factory.

## ARCHITECTURAL CONSEQUENCE

La referencia existente a Experience sostiene un selector local de Family Adventure para las composiciones y controles ejecutados. Esta evidencia no promueve el selector a arquitectura general. No se crea ADR ni se modifica el significado de Experience o `DemoProvider`.

```text
TES → unchanged
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED
Product Semantic Contract → unchanged
PSC-P01 → unchanged
PSC-P02 → NOT CREATED
Group → NOT INTRODUCED
```

Se conservan las distinciones: Composition ≠ Runtime State ≠ Derived Evaluation ≠ Read Model ≠ UI Local State; Scenario identity ≠ semantic authority; Experience reference ≠ Behavior ontology; selector experimental ≠ arquitectura promovida; successful reuse ≠ general Factory architecture.

## WHAT H22 DOES NOT PROVE

- No demuestra una correspondencia universal ni única entre Experience y comportamiento; tampoco otras versiones de Family Adventure o providers.
- No demuestra enlace contextual correcto: L1 sigue activo y confirmado en B.
- No demuestra transporte de contenido ni presentación comercial correcta: L3/L5 siguen activos; L4 permanece por inspección.
- No modifica la falsación histórica de H21 ni completa Composition B.
- No acredita reutilización integral de Factory, aislamiento intercalado exhaustivo o aceptación manual de B.

## REMAINING PRESSURES

Quedan observados el enlace del contexto de composición/Evidence con la evaluación y el transporte de contenido situado hacia las perspectivas y Activity. App mantiene sus literales inspeccionados. Son fronteras distintas de la selección que H22 ha probado.

**H23 no se selecciona ni se abre automáticamente.** La siguiente presión material queda documentada para decidir su alcance en otra sesión, sin corrección adicional ni generalización arquitectónica.
