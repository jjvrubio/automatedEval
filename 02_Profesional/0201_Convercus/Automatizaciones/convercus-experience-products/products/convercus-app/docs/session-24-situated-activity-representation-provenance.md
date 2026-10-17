---
title: "Sesión 24 — Situated Activity Representation Provenance"
language: es
version: "v1.0"
status: "H24 FALSIFIED; L5 open; STOP before runtime or contract changes"
date: "2026-09-14"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 24 — Situated Activity Representation Provenance

## H23 CONSOLIDATED INPUT

**H24 → FALSIFIED dentro de la forma existente y del delta autorizado.** La inspección no identifica una relación legítima que aporte la representación situada de una acción completada. El harness reproduce la consecuencia: A y B conservan sus hechos y evaluación, pero ambas generan jardín/fuente en Activity. Se detiene la implementación antes de crear un contrato o reinterpretar otro campo para salvar la hipótesis.

Se parte del [resultado consolidado de H23](session-23-situated-evaluation-context-binding.md), sin revisar los resultados históricos:

```text
SESSION 20 → CLOSED
H21 → FALSIFIED for historical baseline
H22 → SUPPORTED WITH QUALIFICATION
       Experience-based behavior selection execution-verified
H23 → SUPPORTED WITH QUALIFICATION
L1 → SITUATED BINDING EXECUTION-VERIFIED
AUTHORITY SEPARATION → PRESERVED under experimental premise
L3 → EXECUTION-CONFIRMED / OPEN
L5 → EXECUTION-CONFIRMED / OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN
```

## H24 HYPOTHESIS

**H24 — Situated Activity Representation Provenance.** Una acción aceptada de Experience puede conservar su consecuencia factual y operacional independientemente de la representación humana situada proyectada en Activity. Dos composiciones con la misma semántica de acción deberían conservar Evidence, atribución, contexto y evaluación correctos y producir representaciones distintas, sin inferir narrativa desde subjectRef, markerRef o la identidad concreta de Scenario, cliente o composición.

La condición experimental exige una procedencia legítima ya existente; no autoriza una arquitectura general de contenido. La falsación se refiere a esa condición y recorrido actuales, no a la imposibilidad universal de separar representación y hecho.

## VARIABLE UNDER TEST

Exclusivamente **L5**, procedencia de `ActivitySourceRecord.title/description` para las acciones aceptadas. No se estudia corrección de copy aislada. La pregunta es si la consecuencia factual/operacional puede recibir una representación situada posterior desde una relación existente y semánticamente apropiada.

## ACTIVITY PROVENANCE MAP

Inspección completada antes de añadir el harness. No se refactorizó código durante la inspección ni posteriormente. Fuentes leídas: [contratos](../prototype/src/demo-factory/contracts.ts), [artefactos A](../prototype/src/demo-factory/artifacts.ts), [artefactos B](../prototype/src/demo-factory/costa-artifacts.ts), [fixtures](../prototype/src/demo-factory/fixtures.ts), [bootstrap](../prototype/src/demo-factory/bootstrap.ts), [adaptador y proyección](../prototype/src/demo/mock-adapter.ts), [integración H23](../prototype/src/demo-factory/vertical-evaluation.ts), [consumidor UI](../prototype/src/app/App.tsx).

| SOURCE | CARRIED VALUE A / B | CONSUMER | TRANSFORMATION | FACTUAL / OPERATIONAL / REPRESENTATIONAL |
| --- | --- | --- | --- | --- |
| `ScenarioDefinition.actions[].actionId` y `DemoScript.steps[].action.actionId` | Ambos: `enlist-p1`, `discover-clue-a`, `activate-p2`, `discover-clue-b` | Disponibilidad en `projectSnapshot()`; UI busca step; `executeAction()` selecciona transición | Igualdad de ID y validación de checkpoint | Operacional; no narrativa |
| `DemoScript.steps[].presenterLabel` | A: «Encontrar la pista del jardín · yo» / «Encontrar la pista de la fuente · huésped 2»; B: «Encontrar la pista del mirador · Inés» / «Encontrar la pista del patio · Mateo» | Controles de presentador de App | Etiqueta del control previo a la acción; se envía solamente `step.action` al provider | Representacional de affordance, no de acción completada |
| `ScenarioDefinition.actions[].subjectRef` | Ambos: `subject-p1` para A, `subject-p2` para B; misma atribución para enlist/activate | `executeAction()` | Valida existencia, habilitación y concordancia de Evidence; además selecciona título/descripción con ternario P1/resto | Operacional y guarda factual; también decisión representacional acoplada |
| `EvidenceInput.subjects` | Ambos: individual P1 / P2, role guest | Adaptador → colección Evidence → integración → supervisión | Copia factual; primer sujeto convertido a `subjectRef` H17 | Factual; no relato |
| `ScenarioDefinition.actions[].evidenceType` y `EvidenceInput.type` | Ambos: `treasure_hunt.marker-a` / `treasure_hunt.marker-b` | Aceptación y `toCrossSubjectEvidence()` | Igualdad requerida por acción; elimina prefijo `treasure_hunt.` para producir `marker-a` / `marker-b` | Factual/evaluación |
| `markerRef` | No es campo público de DemoAction ni EvidenceInput; surge como `marker-a` / `marker-b` en integración para ambos | H17 y criterio K | Conserva identidad de marcador derivada del tipo factual; no participa en el título actual | Entrada factual adaptada para evaluación |
| `EvidenceInput.source` | Ambos: `demo-control` | Colección Evidence y supervisión; rama genérica de Activity | Se conserva; en acciones sin `requiresEnabledSubject` se interpola en «Evidencia recibida desde …» | Procedencia factual; no lugar situado |
| Forma pública `DemoAction` / `DemoEnableAction` | `type`, `actionId`, `evidence` o `operation`; ningún texto de acción completada | `DemoProvider.executeAction()` | Transporta la acción; alistamiento/activación no producen Evidence ni Activity nueva | Factual/operacional |
| Contextos de Scenario / Evidence | A: Aurora, AS-8842, stay-AS-8842; B: Costa, CC-205, stay-CC-205; property no declarada en Evidence de los Scripts | Integración H23 → evaluación conjunta | Booking/stay desde hecho; property situada desde Scenario; premisa experimental separada | Factual/contextual/evaluación, no representación |
| `MockDataAdapter.executeAction()` → `ActivitySourceRecord.title` | Ambos: «Pista del jardín encontrada» / «Pista de la fuente encontrada» | `fixture.activityRecords.unshift()` | Si `requiresEnabledSubject`, ternario sobre `subjectRef === "subject-p1"`; en rama genérica usa `evidence.type` | Representacional decidido por maquinaria runtime |
| Mismo punto → `ActivitySourceRecord.description` | Ambos: «Hallazgo aportado por ti.» / «Hallazgo atribuido al huésped 2, registrado desde tu cuenta.» | Mismo registro materializado | Misma bifurcación P1/resto; rama genérica usa source | Representacional; no fuente de atribución factual |
| Evidence ID/time → Activity ID/time | A: `evidence-a-p1` / `evidence-b-p2`; B: `evidence-costa-a-p1` / `evidence-costa-b-p2`; mismas horas 10:00/10:05 UTC | Materialización de Activity | Copia ID y occurredAt, kind evidence, provenance simulated | Referencia al hecho en una representación; identidad compartida no equivale a autoridad |
| `DemoFixture.activityRecords` inicial | A: estancia/preferencia; B: estancia Costa; ningún registro de los futuros hallazgos | Constructor clona fixture; `projectSnapshot()` | Proyecta todos los registros existentes, sin resolver por actionId ni esperar aceptación | Representación ya materializada, no relación acción → representación posterior |
| `ActivitySourceRecord` → `projectSnapshot()` → `ActivityItem` | Título y descripción anteriores en A y B | `AppSnapshot.activity` | Copia textos sin transformación; deriva fecha, icono y tono | Read model representacional |
| `AppSnapshot.activity` → `ActivityList` | Mismos textos del snapshot | Home reciente y ruta `/activity` | `<h3>{item.title}</h3>` y `<p>{item.description}</p>` | Presentación efectiva; sin reconstrucción de Evidence o K |

## FACTUAL / OPERATIONAL INPUT

El Script aporta Evidence con ID, type, occurredAt, source, reliability, subjects y contexts. Scenario determina transiciones, sujeto de cada acción y habilitación; la sesión operacional sigue siendo P1 cuando registra el hallazgo de P2. La aceptación conserva la atribución factual. H23 sitúa el contexto de evaluación y mantiene la premisa experimental diferenciada.

K sigue siendo A AND (B OR C). Activity no entra en `evaluateVerticalEvidence()` ni reconstruye Evidence o K. El acoplamiento observado está en la decisión representacional dentro del mismo procedimiento de aceptación/materialización, no en una dependencia inversa del evaluador respecto del texto visible.

## REPRESENTATIONAL INPUT

Hay contenido situado en la etiqueta del Script y en member/news/records del fixture. Ninguno declara cómo representar la finalización de estas acciones. `presenterLabel` es una invitación; extraer sus lugares y convertir su verbo a pasado introduciría una regla narrativa nueva. `ActivitySourceRecord` sí contiene textos de actividad materializada, pero los fixtures A/B no aportan los registros de estos hallazgos ni una relación para incorporarlos después de aceptar la acción.

## CURRENT COUPLING

`executeAction()` valida y agrega Evidence, evalúa el estado factual y construye inmediatamente Activity. La rama `requiresEnabledSubject` decide jardín/fuente a partir de P1/resto. Por ello dos composiciones con esos mismos sujetos y marcadores generan idéntico relato de hallazgo aunque el Script B anuncie mirador/patio.

La descripción tampoco procede del Script: usa la misma bifurcación de sujeto. Reutilizar ese texto no demostraría reutilización arquitectónica. `projectSnapshot()` transporta el resultado, sin reparar su procedencia.

## EXISTING SOURCE CANDIDATES

| Candidato | Evaluación |
| --- | --- |
| Scenario actions / presenterAction | Modelan transición, tipo y sujeto; carecen de representación de finalización. Añadir un campo sería ampliar el contrato. |
| Script presenterLabel | Tiene lugares situados, pero su función es affordance. Reutilizarlo o analizarlo para escribir Activity confundiría dos representaciones. Además no llega al constructor del provider ni a la acción pública. |
| Evidence source/type/subjects/contexts | Describe hechos y referencias. Usarlo como depósito de narrativa alteraría su función; inferir lugar de sujeto/marcador viola el control. |
| Fixture member/news/brand | Contexto visual/editorial sin relación con la finalización de una acción. Analizar texto de news o identidad de cliente no aporta una procedencia legítima. |
| Fixture activityRecords / ActivitySourceRecord | Forma legítima para actividad existente, pero no fuente pendiente ligada a una acción. Todos sus registros son visibles desde el snapshot inicial. Precargar hallazgos o imponer búsqueda por ID y retención hasta aceptación crearía una convención/relación nueva aunque no añadiera una interfaz TypeScript. |
| ActivityItem / snapshot | Resultado ya proyectado; editarlo en un harness sólo probaría mutabilidad del read model, no procedencia de la acción aceptada. |

## NO LEGITIMATE EXISTING SOURCE

**No se selecciona una fuente experimental. STOP antes del delta de runtime.** La inspección de las relaciones y sus consumidores satisface el primer falsador de H24. La existencia aislada de campos string no constituye una relación semántica válida de representación posterior.

No se crean ActivityPresentation, ActivityTemplate, NarrativeDescriptor, registros de contenido, motores ni equivalentes implícitos por lookup, convención de ID o reinterpretación de campos.

## BASELINE

Suite previa: **85/85 PASS, 17 archivos**. La [baseline H24](evidence/session-24/baseline.json) conserva huellas del estado de trabajo recibido, incluidos cambios previos sin commit. Contiene 142 archivos capturados; 141 archivos de fuente/configuración/documentación quedan verificados sin cambios. El restante es `.DS_Store` en la raíz del prototipo, metadato de Finder capturado incidentalmente y excluido expresamente de la guarda final.

Se mantienen los informes, baselines, trazas y harness H21–H23, las fuentes archivadas, la aceptación histórica de A, TES, contratos y gobernanza. No se usan diferencias contra HEAD para atribuir cambios de sesiones anteriores a esta sesión.

## CODE DELTA

**Delta de aplicación: ninguno.** Adaptador, bootstrap, contratos, artefactos A/B, proyecciones, evaluadores, selector H22, binding H23 y App permanecen byte a byte iguales a la entrada H24.

Se añade únicamente el [harness H24](../prototype/src/demo-factory/situated-activity-provenance-h24.test.ts), este informe y la evidencia bajo `docs/evidence/session-24/`. Los fixtures diagnósticos se clonan dentro del harness, sin registro comercial. No se modifican harness históricos ni sus expectativas.

## A CONTROL

Se ejecuta `enlist-p1 → discover-clue-a → activate-p2 → discover-clue-b`. Activity efectiva contiene jardín y fuente, con los dos textos de atribución existentes. Los cinco snapshots, desde inicio hasta A+B, coinciden íntegramente con H23; reset devuelve el inicial. No aparecen mirador/patio en la Activity de los hallazgos A.

Evidence conserva `evidence-a-p1` / `evidence-b-p2`, P1/P2 y marker-a/marker-b. Los argumentos verticales y la tupla completa de evaluación conjunta coinciden con H23: Aurora/AS-8842/stay-AS-8842, mismo criterio y premisa. No se cambia la aceptación histórica de A.

## B CONTROL

Se ejecuta la misma secuencia con el provider compartido resuelto para Costa. Evidence conserva `evidence-costa-a-p1` / `evidence-costa-b-p2`, P1/P2 y marker-a/marker-b; la evaluación recibe Costa/CC-205/stay-CC-205. Sus snapshots y entradas/resultados de evaluación también coinciden con H23.

Activity efectiva sigue produciendo **«Pista del jardín encontrada»** y **«Pista de la fuente encontrada»**. No produce mirador/patio pese a que el Script los declara. Esta referencia cruzada indebida se registra como fallo del objetivo H24, no se oculta comparando únicamente el Script ni se corrige por sustitución de copy.

## FACT / REPRESENTATION INDEPENDENCE CONTROL

**El control positivo solicitado no es ejecutable legítimamente con la forma existente.** No hay una entrada de representación de acción completada que pueda variarse manteniendo el hecho constante. No se añade una para conseguir el resultado deseado.

Se ejecuta un diagnóstico subordinado en A y B: variar sólo `presenterLabel` de los pasos de Evidence a «Registrar hallazgo alternativo …». Actions, Evidence payload, Scenario, sujetos, marcadores y contexto permanecen idénticos. Los snapshots completos, estados operacionales, argumentos/resultados verticales y evaluación conjunta completa permanecen iguales, incluida Activity.

Esto demuestra que el candidato affordance no alimenta la representación posterior actual. **No demuestra** el resultado requerido «hechos iguales / Activity distinta» ni falsa por sí mismo «representation text = factual identity». Esa independencia queda sin apoyo en el recorrido ensayado. No se presenta como prueba positiva una edición directa del read model.

## ABSENCE CONTROL

No existe fuente seleccionada de representación completada, por lo que no hay una ausencia de esa fuente que pueda expresarse y verificarse bajo el contrato actual. El harness vacía únicamente el candidato rechazado `presenterLabel` en los pasos de Evidence para A y B, usando la misma forma string existente y el provider público.

Resultado: Evidence, habilitación, contexto, K y claim permanecen iguales; Activity sigue generando jardín/fuente. La ausencia de affordance no hace aparecer una representación situada alternativa ni impide el texto fijo. Esto es evidencia del acoplamiento existente, **no una política de fallback aprobada** ni una demostración de manejo correcto de ausencia. Expresar ausencia de representación posterior requiere una decisión nueva; se mantiene STOP y no se inventa esa política. No se renderiza una UI con etiqueta vacía.

## EXECUTION TRACE

La [traza final](evidence/session-24/execution-trace-final.json) conserva seis ejecuciones completas: A/B originales, A/B con affordance cambiada y A/B con affordance vacía, incluyendo reset. Cada frame contiene snapshot público; los frames factuales capturan Evidence y contexto reales mediante spies transparentes que invocan las implementaciones originales, más resultados verticales y tupla/resultado completos de H17. La claim completa se captura en evaluación, no se infiere del resumen de supervisión.

| Fase (igual determinación en A/B) | Evidence | Sesión/habilitación | Joint admissibility | K | Claim |
| --- | --- | --- | --- | --- | --- |
| Inicial | 0 | P1; P1 not-enlisted, P2 not-enabled | cannot-currently-establish | not-attempted | not-produced |
| Enlist P1 | 0 | P1; P1 enabled, P2 not-enabled | cannot-currently-establish | not-attempted | not-produced |
| Acción A | 1, P1 | Igual | established, same-subject-control | not-established | not-established |
| Activate P2 | 1, P1 | P1; ambos enabled | Conservada | Conservado | Conservada |
| Acción B | 2, P1/P2 | Igual | established, applicable-authoritative-premise | established | established |

Los invariantes factuales son iguales a H23 y entre variantes de cada composición. No se afirma equivalencia entre los IDs o contextos distintos de A y B. No hay comparación antes/después de una solución de runtime porque el delta se detuvo; sí hay reproducción exacta del estado previo y comparación de todos los controles diagnósticos.

La [primera captura](evidence/session-24/execution-trace.json) también se conserva. La posterior corrección de la guarda del harness excluye únicamente metadatos de Finder; la traza final declara esa exclusión. Las ejecuciones ordinarias no escriben evidencia. `H24_RECORD_PATH` permite un destino nuevo y la escritura exclusiva impide sobrescribir capturas.

## L5 RESULT

**L5 → EXECUTION-CONFIRMED / OPEN.** La procedencia sigue siendo la bifurcación del adaptador por sujeto. B mantiene los títulos de A. No hay solución promovida ni nueva arquitectura.

## REGRESSIONS

| Verificación | Resultado |
| --- | --- |
| Suite previa | 85/85 PASS, 17 archivos |
| H24 focalizado, captura final | 1/1 PASS; reproduce H24 FALSIFIED |
| H23 regression + H22 regression + H21 historical reproduction + Session 20 vertical regression | 13/13 PASS, 4 archivos |
| Full suite final | 86/86 PASS, 18 archivos |
| Typecheck | PASS |
| Lint | PASS |
| Build TypeScript + Vite + PWA | PASS |

PASS del harness significa que las aserciones reproducen el falsador y preservan los invariantes; no convierte H24 en SUPPORTED. H23 mantiene los controles de autoridad separada; H22/H21 reproducen sus fuentes históricas archivadas. La suite vertical conserva los tests UI de A. No se necesita navegador para Activity y no se renderiza B.

En el primer `npm run check`, la nueva guarda falló al detectar un cambio automático de `.DS_Store`. Typecheck/lint y los otros 85 tests pasaron; build aún no se ejecutó. Se corrigió sólo la selección de archivos del harness, conservando la baseline original, y se repitió la verificación completa. No fue un falsador semántico ni un impedimento externo que justificase INCONCLUSIVE.

Reproducción desde `products/convercus-app/prototype/`:

```sh
npm test -- src/demo-factory/situated-activity-provenance-h24.test.ts
npm test -- src/demo-factory/situated-evaluation-context-h23.test.ts src/demo-factory/experience-stable-selection-h22.test.ts src/demo-factory/composition-boundary-h21.test.ts src/demo-factory/family-adventure-vertical.test.ts
npm run check
```

## L3 STATUS

**L3 → PRESERVED / OUT OF SCOPE / EXECUTION-CONFIRMED.** GuestPerspective B conserva Lucía y las referencias jardín/fuente en sus fases correspondientes. Se observa en los snapshots del harness. No es falsador adicional de H24 y no se modifica su copy.

## L4 STATUS

**L4 → PRESERVED / SOURCE-INSPECTION FINDING / OUT OF SCOPE.** `App.tsx` permanece intacto. La inspección de ActivityList justifica usar el snapshot como representación efectiva, pero no constituye verificación de renderizado B ni de corrección global de App.

## FALSIFICATION ANALYSIS

| Falsador | Observación |
| --- | --- |
| No hay procedencia legítima existente sin nuevo contrato | **Observado.** Ningún candidato relaciona acción aceptada con narrativa completada situada. STOP de implementación. |
| Cambiar Activity modifica hechos/contexto/atribución/evaluación | No ensayado como control positivo: falta una entrada legítima de representación. La variación de affordance conserva ambos planos, incluida Activity. |
| Runtime necesita inferir lugares desde sujeto, marcador o identidad concreta | **Observado para subjectRef.** La bifurcación P1/resto sigue eligiendo jardín/fuente en A y B. No se afirma que el código actual derive el título desde markerRef. |
| Regresión de A | No observada: snapshots y evaluación H23 iguales, regresión vertical PASS. |

No hay impedimento externo al experimento. El resultado es FALSIFIED y no INCONCLUSIVE. Completar documentación y regresiones tras STOP no supone continuar una implementación prohibida.

## H24 VERDICT

```text
H24 → FALSIFIED
L5 → EXECUTION-CONFIRMED / OPEN
FACT / REPRESENTATION SEPARATION → UNSUPPORTED within tested scope
L3 → PRESERVED / OUT OF SCOPE
L4 → PRESERVED / SOURCE-INSPECTION
NEXT MATERIAL PRESSURE → OBSERVED but NOT SELECTED
```

La separación sigue siendo una guarda semántica; lo que no se sostiene es su realización mediante una procedencia situada existente en este recorrido. H24 no invalida el binding H23 ni los resultados factuales de A/B.

## ARCHITECTURAL CONSEQUENCE

Se identifica una relación ausente entre acción aceptada y representación posterior situada. La existencia del tipo `ActivitySourceRecord` no resuelve por sí misma esa relación. Cualquier ampliación requiere otro alcance explícito; esta sesión no selecciona su forma ni promueve arquitectura.

Architecture v0.5 → ACTIVE / unchanged. ADR-001–005 → ACCEPTED / unchanged. No se crea ADR ni arquitectura general de contenido. La aplicación conserva la separación estructural entre composición, hecho runtime, evaluación derivada, read model y estado local UI.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract → unchanged. PSC-P01 → OPEN / unchanged. PSC-P02 → NOT CREATED. Group → NOT INTRODUCED en esta sesión; no se revisan formas heredadas ajenas al ensayo.

```text
DEMO COMPOSITION ≠ RUNTIME FACT ≠ DERIVED EVALUATION ≠ READ MODEL ≠ UI LOCAL STATE
Evidence ≠ Activity
Activity → projection / representation → never factual authority
accepted action ≠ situated representation
action affordance ≠ completed-action representation
representation provenance ≠ semantic authority
copy reuse ≠ architectural reuse
```

El texto de Activity no se utiliza como autoridad de atribución ni como fuente para reconstruir Evidence, contexto o K. La ausencia de procedencia representacional no autoriza a cargar esa función en Evidence.

## WHAT H24 DOES NOT PROVE

- No demuestra una arquitectura general de contenido, localización o representación universal de Activity.
- No resuelve procedencia de contenido GuestPerspective ni corrección de renderizado de App.
- No demuestra independencia positiva «hechos iguales / Activity distinta» para acciones aceptadas con el contrato existente.
- No define representación ausente, política de fallback ni fuente productiva de narrativa posterior.
- No modifica la premisa experimental, acredita autoridad productiva ni amplía la aceptación comercial de B.
- No reescribe H21–H23 ni demuestra imposibilidad de resolver esta presión bajo un futuro alcance distinto.

## REMAINING PRESSURES

L5 sigue abierto: falta procedencia legítima de representación situada posterior y una forma de expresar su ausencia. L3/L4 siguen abiertos y fuera de alcance. Se conservan también las cualificaciones H23 sobre premisa experimental, property situada cuando falta en Evidence y referencias experimentales de evaluación.

**La siguiente presión material queda observada, pero NO SELECCIONADA. H25 no se abre automáticamente.**
