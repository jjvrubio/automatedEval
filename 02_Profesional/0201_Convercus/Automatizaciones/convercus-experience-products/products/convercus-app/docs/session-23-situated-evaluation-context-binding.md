---
title: "Sesión 23 — Situated Evaluation Context Binding"
language: es
version: "v1.0"
status: "experiment executed; H23 supported with qualification; no architectural or semantic promotion"
date: "2026-09-13"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 23 — Situated Evaluation Context Binding

## H22 CONSOLIDATED INPUT

**H23 → SUPPORTED WITH QUALIFICATION en el ámbito probado.** A y B llegan a la evaluación conjunta con sus referencias situadas correspondientes. Evidence contradictoria no se reescribe ni produce una evaluación establecida. La aplicabilidad de la premisa permanece como condición separada.

Sesión 20 CLOSED. H21 FALSIFIED para su baseline histórica. H22 SUPPORTED WITH QUALIFICATION. L2a/L2b seleccionan mediante Experience y están EXECUTION-VERIFIED. L1/L3/L5 están EXECUTION-CONFIRMED; L4 es SOURCE-INSPECTION FINDING. Se preservan los informes y las trazas históricos.

## H23 HYPOTHESIS

Dentro del recorrido Family Adventure, la maquinaria compartida puede recibir el contexto situado de la composición ejecutada, preservando referencias factuales y la premisa autoritativa experimental existente, sin sustituirlas por constantes de otra composición ni inferir autoridad únicamente de Evidence.

## VARIABLE UNDER TEST

Exclusivamente L1: procedencia y transporte de los campos contextuales a la integración y a la evaluación conjunta. El selector H22, K, H17 y los textos situados se mantienen.

## CONTEXT PROVENANCE MAP

Inspección completada antes de modificar las fuentes de aplicación. Valores en la baseline H22:

| SOURCE | VALUE A | VALUE B | AUTHORITY / ROLE | CURRENT CONSUMER | CURRENT TRANSFORMATION |
| --- | --- | --- | --- | --- | --- |
| `ScenarioDefinition.contexts` | property `aurora-resort`, booking `AS-8842`, stay `stay-AS-8842` | property `costa-clara-resort`, booking `CC-205`, stay `stay-CC-205` | Contexto situado declarado de composición; no autoridad por sí mismo | Resolver y copia de Scenario en provider | No se pasa a evaluación |
| `EvidenceInput.contexts` del Script / Evidence incorporada por acción | booking `AS-8842`, stay `stay-AS-8842`; sin property | booking `CC-205`, stay `stay-CC-205`; sin property | Referencias factuales; no premisa autoritativa | `executeAction()` → colección runtime → `evaluateVerticalEvidence(evidence)` | Payload conservado al entrar en integración |
| `ResolvedDemoRuntime` | Scenario A y Experience Family Adventure resueltos | Scenario B y misma Experience resueltos | Composición resuelta, no resultado ni autorización derivada | Construcción de provider | Scenario completo ya llega al adaptador |
| `evaluateVerticalEvidence()` | Recibe Evidence A, ningún argumento situado separado | Recibe Evidence B, ningún argumento situado separado | Integración experimental entre hecho y evaluación | Conversión y evaluador H17 | Usa `evaluationContext` fijo A |
| `toCrossSubjectEvidence()` | Copia Evidence ID, primer sujeto y marker; sustituye contexto por A | Copia Evidence ID, primer sujeto y marker; sustituye contexto por A | Adaptación de entrada; no acreditación de autoridad | `evaluateCrossSubjectEvidenceSufficiency()` | Descarta los contexts factuales y asigna hunt/stay/property/booking constantes |
| `evaluationContext` | `evaluation-family-adventure-1`, `hunt-family-adventure-1`, Aurora/AS-8842 | Exactamente A | Fixture de entrada a evaluación, separado de Evidence | Evaluador conjunto, criterio y premisa | Ninguna selección situada |
| Premisa experimental | `premise-family-adventure-p1-p2@1`; `fixture-policy:resort-family-adventure@1`; scope A; sujetos P1/P2 | Misma premisa con scope A | Supuesto autoritativo experimental explícito y separado; no autoridad productiva acreditada | `evaluateJointAdmissibility()` | Compara scope completo y cobertura de sujetos |
| `evaluateCrossSubjectEvidenceSufficiency()` | Evidence convertida A, contexto A, criterio y premisa A | Evidence Costa remapeada a A, contexto/criterio/premisa A | Evaluación derivada H17 | `evaluateJointAdmissibility()` y después K | Filtra referencias situadas y evalúa admisibilidad antes de suficiencia |
| `evaluateJointAdmissibility()` | Recibe A | Recibe A | Comprobación de aplicabilidad autoritativa, distinta de coincidencia factual | Llamada interna directa desde evaluador conjunto | En P1/P2 exige scope coincidente y sujetos cubiertos; en sujeto único conserva control H17 |
| Resultado | A: not-established tras pista A; established tras A+B | Mismos resultados, sin integridad contextual B | Resultado derivado, no fuente del contexto | Proyecciones guest/supervision | Read models no exponen contexto; K correcto no demuestra binding correcto |

La entrada efectiva del evaluador conjunto B con contexto Aurora ya está observada en la [traza H22](evidence/session-22/execution-trace.json). La llamada interna a `evaluateJointAdmissibility()` usa directamente esos mismos argumentos según el código H17 congelado; no se afirma que un spy intercepte una llamada interna léxica.

## FACTUAL CONTEXT

Booking y stay vienen de Evidence. Sus valores se conservarán en el payload y en la entrada convertida. Property no viene en los Scripts actuales: se transportará desde Scenario como dato situado de integración, identificado como tal, sin añadirlo al hecho original. Si una Evidence declara property, también deberá concordar. La carencia, ambigüedad o discrepancia de referencias requeridas no se resolverá escogiendo silenciosamente una fuente.

## EVALUATION CONTEXT

Ruta mínima candidata: `this.scenario.contexts` → segundo argumento de `evaluateVerticalEvidence()` → forma existente `CrossSubjectEvaluationContext`. No necesita nuevo contrato, servicio ni resolver. Hunt y evaluationRef permanecen referencias del fixture experimental Family Adventure; property/booking/stay se toman del contexto de composición explícito, nunca de Evidence para elegir el ámbito aplicable.

## AUTHORITATIVE PREMISE

Se conserva la declaración experimental existente: mismas referencias de premisa/autoridad y cobertura fija P1/P2, separada de K. Su scope y el del criterio se sitúan con la entrada explícita de integración. Esto instancia el mismo supuesto experimental para A/B; no acredita que Scenario o Evidence puedan emitir autoridad ni autoriza composiciones arbitrarias en producción. La aplicabilidad sigue comprobándose en H17. Se probará por separado la ausencia de premisa, scope incorrecto y cobertura insuficiente con las entradas efectivas capturadas.

## BASELINE

Antes del delta: 84/84 tests PASS, 16 archivos. [Huellas previas](evidence/session-23/baseline.json). Se archivan byte a byte adaptador e integración H22 para conservar reproducciones históricas verificables. No se modifican los artefactos A/B ni los evaluadores H17.

La baseline H23 registra 99 archivos previos. Las cinco excepciones de fuente están declaradas: integración, llamada del adaptador, adaptación de los dos harness históricos y argumento situado del test directo B+C. Los 94 restantes permanecen idénticos, incluidos contratos, artefactos, H17, copy/App y documentos/evidencia H21/H22. Las comparaciones usan el estado de trabajo previo, que ya tenía cambios sin commit.

El [adaptador H22 archivado](../prototype/src/demo-factory/test-fixtures/h22/mock-adapter.ts) tiene SHA-256 `e07f924ec852d0a33aa10a59daedc7d72a8d0b55a764f93db12ce66a8f24a72b`. La [integración H21/H22 archivada](../prototype/src/demo-factory/test-fixtures/h22/vertical-evaluation.ts) tiene SHA-256 `ba2423dcdd8eab8e059bd3f8081d5eec240b7801e6a42d9beac0c8a0dd05745a`. El test H23 exige coincidencia con esas fuentes originales.

## CODE DELTA

En [vertical-evaluation.ts](../prototype/src/demo-factory/vertical-evaluation.ts), `evaluateVerticalEvidence()` acepta un segundo argumento con la lista de `ContextReference` ya existente. Extrae una referencia inequívoca para property/booking/stay de la composición. No hay fallback a Aurora ni selección del contexto aplicable desde Evidence.

`toCrossSubjectEvidence()` conserva booking/stay desde el hecho y valida su concordancia. Una property factual explícita debe concordar; si está ausente, el input integrado utiliza la property situada de Scenario. No se modifica `EvidenceInput` ni se añade property a su colección factual. Las referencias hunt/evaluation del fixture Family Adventure permanecen iguales para este ensayo. El criterio conserva exactamente A AND (B OR C); sólo recibe la property situada en su scope. La premisa mantiene referencias y cobertura P1/P2, con scope situado para esta ejecución experimental.

Ante falta, ambigüedad o contradicción se devuelve el estado ya expresable en `VerticalEvaluationState`: Evidence conservada, `jointAdmissibility: cannot-currently-establish`, `sufficiency: not-attempted`, sin claim. No se llama al evaluador conjunto con datos contradictorios. Esta guarda evita que el filtrado interno preexistente H17 descarte una parte incoherente y permita interpretar el resto como validación del conjunto. No se cambia ese filtrado ni su semántica.

La única modificación en [mock-adapter.ts](../prototype/src/demo/mock-adapter.ts) es el argumento situado de la llamada:

```diff
- if (this.scenario?.experienceRef === "experience:family-adventure@1") this.evaluation = evaluateVerticalEvidence(this.evidence);
+ if (this.scenario?.experienceRef === "experience:family-adventure@1") this.evaluation = evaluateVerticalEvidence(this.evidence, this.scenario.contexts);
```

Constructor/reset mantienen la inicialización vacía sin contexto; no hay evaluación de Evidence que situar en ese momento. Una llamada no vacía sin contexto explícito devuelve indeterminación. El antiguo export `verticalEvaluationContext`, sin consumidores, desaparece con el objeto global fijo; no cambia un contrato de producto. `DemoProvider`, bootstrap y Scenario/Script permanecen intactos.

Instrumentación y documentación añadidas:

- [Harness H23](../prototype/src/demo-factory/situated-evaluation-context-h23.test.ts), con controles secuenciales y STOP ante el primer falsador material.
- Reproducciones H21/H22 dirigidas a fuentes archivadas, sin cambiar resultados esperados ni documentos históricos. Tres pequeños reexports resuelven los imports relativos del archivo archivado hacia contratos y evaluadores H17 compartidos intactos; no duplican H17.
- El test directo B+C de Sesión 20 recibe `runtime.scenario.contexts`; sus aserciones originales sobre admisibilidad y K no cambian. Su fuente anterior se conserva como archivo de evidencia de test para verificar la baseline H22.
- Informe directamente en `docs/`; baseline y traza bajo `docs/evidence/session-23/`; enlace desde README del producto.

Los dos selectores H22 se conservan exactamente. El harness exige que el adaptador actual sea el archivado más el único argumento nuevo, y que ambas funciones de proyección sean iguales byte a byte, salvo espacios finales externos a ellas.

## A CONTROL

`hospitality-family-adventure` conserva Scenario `family-adventure` y Experience `experience:family-adventure@1`. Las entradas reales tras A@P1 y A@P1+B@P2 contienen exclusivamente los campos situados `aurora-resort`, `AS-8842`, `stay-AS-8842`. No contienen referencias Costa.

Tras A@P1: una Evidence atribuida a P1; H17 aplica `same-subject-control`; K `not-established`. Tras B@P2: dos Evidence, atribución P1/P2 conservada; joint admissibility `established / applicable-authoritative-premise`; K `established`. Alistamiento y activación no añaden Evidence ni invocan evaluación. La sesión permanece P1.

Cada snapshot completo de A —inicio, cuatro acciones y reset— coincide con el registrado en H22. El recorrido aceptado de Sesión 20 conserva su regresión automatizada, incluida navegación UI.

## B CONTROL

`hospitality-family-adventure-costa` conserva Scenario `family-adventure-costa` y la misma Experience. Tras A@P1, la entrada efectiva a `evaluateCrossSubjectEvidenceSufficiency()` contiene:

```text
Evidence: evidence-costa-a-p1 → subject-p1 → marker-a
bookingRef: CC-205
stayRef: stay-CC-205
propertyRef: costa-clara-resort
evaluationRef: evaluation-family-adventure-1
huntRef: hunt-family-adventure-1
```

La premisa y el criterio reciben el mismo contexto B aplicable en sus campos de scope existentes. Tras B@P2 se añade `evidence-costa-b-p2 → subject-p2 → marker-b`, también con contexto Costa. En ambas llamadas se verifica la ausencia de `aurora-resort`, `AS-8842` y `stay-AS-8842` en toda la tupla efectiva: Evidence convertida, contexto, criterio y premisa.

La primera pista produce K `not-established`; A+B produce joint admissibility y K `established` bajo la premisa experimental. Ahora el input efectivo acredita el contexto B; el resultado K aislado seguiría sin bastar para ello.

## A/B CONTEXT SEPARATION

Las acciones se intercalan en dos instancias de la misma clase: alistar A/B, pista A en A/B, activar P2 en A/B y pista B en A/B. Cada llamada conserva su contexto propio. No hay estado contextual global mutable ni implementación específica B.

| Entrada efectiva | A | B |
| --- | --- | --- |
| Property | `aurora-resort` | `costa-clara-resort` |
| Booking | `AS-8842` | `CC-205` |
| Stay | `stay-AS-8842` | `stay-CC-205` |
| Referencias de la otra composición | Ausentes | Ausentes |
| Evaluador, K y referencias de premisa | Misma maquinaria y declaración experimental | Misma maquinaria y declaración experimental |

Los reset devuelven los snapshots iniciales. Este control prueba separación en la secuencia intercalada ejecutada, no una garantía general sobre concurrencia o scopes productivos.

## ADVERSARIAL MISMATCH CONTROL

Se crean payloads adversariales exclusivamente en el harness, sin registro de demo comercial:

| Scenario ejecutado | Contexto factual introducido | Resultado |
| --- | --- | --- |
| B: Costa/CC-205 | Evidence con booking/stay Aurora/AS-8842 | Evidence permanece en runtime; joint admissibility cannot-currently-establish; suficiencia not-attempted; sin claim |
| A: Aurora/AS-8842 | Evidence con booking/stay Costa/CC-205 | Mismo resultado indeterminado |

Se recorren las cuatro acciones existentes en cada caso. La llamada vertical recibe los facts contradictorios intactos y, por separado, el contexto original del Scenario. Su resultado conserva esa Evidence. La entrada al evaluador conjunto queda bloqueada: cero llamadas. No se elige un contexto ganador ni se reescribe silenciosamente el hecho. La acción factual y el checkpoint pueden avanzar; el avance del recorrido no acredita una evaluación establecida.

Otros seis controles directos de integración verifican ausencia de contexto aplicable separado, Scenario sin property, Scenario con booking ambiguo, Evidence sin stay, Evidence con booking ambiguo y Evidence con property explícita contradictoria. Todos conservan los argumentos y devuelven indeterminación sin invocar H17.

El rechazo ocurre en la integración de evaluación; no se crea una categoría semántica de Evidence inválida ni un nuevo outcome. Tampoco se atribuye a H17 una decisión sobre qué fuente debe prevalecer.

## AUTHORITY-SEPARATION CONTROL

Se capturan las entradas efectivas completas A+B de A y B y se vuelven a ejecutar sobre el export real H17, modificando sólo la premisa del harness:

| Premisa suministrada | Contexto factual y aplicable | Resultado en A y B |
| --- | --- | --- |
| Ausente | Correcto e idéntico al control positivo | cannot-currently-establish; suficiencia no intentada |
| Booking de scope distinto | Correcto | cannot-currently-establish; suficiencia no intentada |
| Sólo cubre P1 | Correcto; Evidence atribuida a P1/P2 | cannot-currently-establish; suficiencia no intentada |

Son seis controles sobre H17 sin mocks de resultado. Un séptimo pasa Evidence P1/P3 con contexto Costa correcto a la integración real: la premisa configurada sigue cubriendo P1/P2 y H17 devuelve indeterminación. No se altera la atribución admitida por los providers A/B; P1/P3 es entrada directa del harness.

**AUTHORITY SEPARATION → PRESERVED en el ensayo.** Correspondencia contextual no sustituye a una premisa aplicable para sujetos distintos. La excepción preexistente H17 de un solo sujeto conserva `same-subject-control`; no se presenta ese caso como prueba de necesidad de premisa conjunta.

Límite de autoridad: la premisa de integración continúa siendo un supuesto experimental explícito. Situar su scope con Scenario es la parametrización del fixture ensayada, no una demostración de que Scenario tiene autoridad para emitirla. No se han resuelto acreditación, provisión, revocación o conflicto de autoridades en producción. Las pruebas de premisa ausente/scope/cobertura se ejecutan en el harness H17; no se añade a `DemoProvider` un control de autoridad nuevo.

## EXECUTION TRACE

La [traza principal](evidence/session-23/execution-trace.json) fue registrada el **2026-09-13T12:49:32.147Z** (13:49:32, Europe/Lisbon). Incluye huellas de la baseline y de ambas fuentes de aplicación ejecutadas.

| Ruta de traza | Evidencia |
| --- | --- |
| `positiveControls[0/1].frames[2]` | A@P1, payload, snapshot, llamadas verticales y entrada/resultado efectivos del evaluador conjunto |
| `positiveControls[0/1].frames[4]` | A@P1+B@P2 y premisa aplicada |
| `negativeControls` | Retail y Arrival sobre código H23; sin comportamiento Family Adventure |
| `adversarialControls[0/1]` | Ambas direcciones de contradicción, con Evidence original y resultado indeterminado |
| `incompleteContextControls` | Seis controles de contexto ausente, ambiguo o contradictorio |
| `authoritySeparationControls` | Seis variaciones de premisa y control adicional P1/P3 |

Los spies sobre exports invocan implementaciones originales y registran argumentos/resultados, sin cambiar el evaluador. H17 llama internamente a `evaluateJointAdmissibility()` con los mismos argumentos; su determinación está en el resultado real capturado. Además, `jointReplay` reproduce explícitamente esa función pública sobre la tupla observada y coincide con la determinación real. Se distingue esa reproducción de una interceptación de la llamada interna léxica.

No se abre navegador para H23. Los tests UI existentes de A se ejecutan en su entorno automatizado. La traza de la ejecución principal no se sobrescribe durante la suite posterior.

## L1 RESULT

**L1 → SITUATED BINDING EXECUTION-VERIFIED en A/B, con cualificación.** El defecto de sustitución silenciosa por constantes de Aurora queda eliminado de la integración actual en los controles ejecutados. L1 continúa EXECUTION-CONFIRMED como hallazgo histórico de H22.

La cualificación cubre la property situada aportada por Scenario ante su ausencia factual, las referencias hunt/evaluation aún experimentales y la premisa asumida por el fixture. No constituye una solución productiva general a la autoridad del contexto.

## REGRESSIONS

| Verificación | Resultado exacto |
| --- | --- |
| Suite previa al delta | 84/84 PASS, 16 archivos |
| H21 histórico + H22 histórico + vertical Sesión 20 tras threading | 12/12 PASS, 3 archivos |
| H23 focalizado y captura principal | 1/1 PASS, con todos los controles secuenciales descritos |
| Suite completa final | 85/85 PASS, 17 archivos |
| Typecheck | PASS |
| Lint | PASS |
| Build TypeScript + Vite + PWA | PASS |

Además de la reproducción histórica de H22, H23 verifica su comportamiento sobre código vivo: misma Experience, Scenario IDs distintos, perspectivas y evaluación presentes en A/B. Retail continúa sin Experience declarada; Hospitality Arrival conserva `experience:arrival-welcome@1`. Sus snapshots iniciales, acción disponible y reset coinciden con H22; no reciben perspectivas Family Adventure ni invocan evaluación vertical durante la acción Arrival.

La regresión de A compara snapshots completos con la traza H22 y conserva los diez tests existentes de la vertical Sesión 20, incluido UI. No se declara una nueva aceptación manual de navegador ni aceptación comercial de B.

Reproducción desde `products/convercus-app/prototype/`:

```sh
npm test -- src/demo-factory/situated-evaluation-context-h23.test.ts
npm test -- src/demo-factory/composition-boundary-h21.test.ts src/demo-factory/experience-stable-selection-h22.test.ts src/demo-factory/family-adventure-vertical.test.ts
npm run check
```

Las ejecuciones ordinarias no escriben trazas. Para una nueva captura, `H23_RECORD_PATH` permite elegir otro destino existente, conservando la evidencia principal. Los harness H21/H22 siguen reproduciendo sus baselines archivadas y sus veredictos originales; H23 comprueba por separado las regresiones sobre la aplicación actual.

## OUT-OF-SCOPE LEAKS

| Leak | Estado en Sesión 23 |
| --- | --- |
| L3 | Preserved / out of scope; EXECUTION-CONFIRMED. Los snapshots B siguen diciendo Lucía, jardín y fuente. |
| L4 | Preserved / out of scope; SOURCE-INSPECTION FINDING. App.tsx intacto; B no se renderiza. |
| L5 | Preserved / out of scope; EXECUTION-CONFIRMED. Activity B conserva los títulos jardín/fuente. |

Estas superficies mantienen los mismos snapshots H22. No impiden observar la entrada contextual efectiva y no falsifican H23. No se aprovecha el cambio para limpiar copy.

## FALSIFICATION ANALYSIS

| Falsador previsto | Observación |
| --- | --- |
| B no alcanza evaluación situada sin nuevo concepto | No observado: se transporta la lista de contexts existente y se usa la forma experimental H17 existente. |
| Se siguen sustituyendo referencias por Aurora | No observado en evaluación B: ausentes en la tupla efectiva completa. |
| Evidence contradictoria recibe autoridad automática | No: ambos sentidos de contradicción devuelven indeterminación sin evaluación conjunta ni reescritura. |
| Contexto correcto sustituye una premisa aplicable | No: las siete pruebas de separación preservan indeterminación cuando falta aplicabilidad. |
| Regresión A | No observada: snapshots iguales a H22 y suite vertical PASS. |
| Se requiere modificar H17 o K | No: funciones H17 congeladas; criterio lógico y cobertura de premisa preservados. |

No se produce falsador material ni impedimento externo. El harness registra SUPPORTED sólo al terminar los controles; una contradicción detiene el ensayo y registra la fase alcanzada. No se introducen abstracciones adicionales para evitar un STOP.

## H23 VERDICT

```text
H23 → SUPPORTED WITH QUALIFICATION
L1 → SITUATED BINDING EXECUTION-VERIFIED within tested scope
CONTEXT BINDING → SUPPORTED within tested scope
AUTHORITY SEPARATION → PRESERVED under experimental premise
NEXT MATERIAL PRESSURE → OBSERVED, NOT SELECTED
```

La cualificación incluye el supuesto explícito de premisa experimental situada, property aportada desde Scenario cuando el hecho no la declara, las referencias experimentales compartidas hunt/evaluation y la ausencia de una arquitectura general de binding. No modifica los veredictos históricos ni demuestra reutilización integral de Factory.

## ARCHITECTURAL CONSEQUENCE

La relación contextual existente llega a la integración mediante una llamada técnica mínima. No se necesita ampliar `DemoProvider`, Scenario/Script o Experience para este ensayo. El selector H22 conserva su condición experimental local.

Architecture v0.5 permanece **ACTIVE / unchanged** y ADR-001–005 **ACCEPTED / unchanged**. No se crea ADR, servicio ContextBinding, ScopeResolver ni otra arquitectura de resolución de autoridad.

```text
DEMO COMPOSITION ≠ RUNTIME FACT ≠ DERIVED EVALUATION
                 ≠ READ MODEL ≠ UI LOCAL STATE
binding mechanism ≠ new semantic ontology
```

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract permanecen intactos. **PSC-P01 → OPEN / EVIDENCE-BACKED PRESSURE**, sin modificación. PSC-P02 no se crea. No se introducen Group, EvaluationScope, ContextScope, ParticipationScope, ContextAuthority ni equivalentes.

```text
Evidence factual context ≠ evaluation authority
subjectRef ≠ evaluation scope
shared booking/stay/property ≠ authority by itself
context equality ≠ semantic authority
context correspondence ≠ admissibility
admissibility ≠ sufficiency
experimental context transport ≠ Product Semantic Contract refinement
```

La propiedad declarada por Scenario se reconoce como dato situado de integración, no como una nueva observación factual ni una fuente de autoridad. La premisa permanece una declaración experimental diferenciada cuya aplicabilidad comprueba H17.

## WHAT H23 DOES NOT PROVE

- No determina una forma productiva universal del binding ni una ontología del scope.
- No acredita la autoridad productiva de la premisa ni demuestra que Scenario pueda emitirla. El fixture declara el supuesto y el ensayo verifica su aplicabilidad separada.
- No demuestra factualidad de property ausente en Evidence; preserva booking/stay factuales y declara el origen situado de property.
- No resuelve pertenencia a distintos hunts, identidad/unicidad productiva de evaluationRef, múltiples premisas o conflictos entre autoridades.
- No define qué fuente debe prevalecer en una discrepancia, ni introduce una política de corrección de hechos; devuelve indeterminación.
- No corrige L3/L4/L5, no acepta B como demo comercial completa, no acredita reutilización integral de Factory y no revisa H21/H22 históricamente.

## REMAINING PRESSURES

Se mantienen las presiones de procedencia/acreditación de premisa, datos contextuales factuales incompletos y referencias experimentales de evaluación. L3/L4/L5 conservan su estado y quedan fuera del alcance ejecutado. La salida actual expresa la discrepancia con estados existentes, sin añadir una explicación de conflicto a los read models.

**La siguiente presión material queda observada, pero no seleccionada. H24 no se abre automáticamente.**
