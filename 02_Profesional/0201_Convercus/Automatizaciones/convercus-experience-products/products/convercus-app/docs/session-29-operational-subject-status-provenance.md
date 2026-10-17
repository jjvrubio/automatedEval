---
title: "Sesión 29 — Operational Subject Status Provenance"
language: es
version: "v1.0"
status: "H29 supported with qualification; existing operational state only within A/B"
date: "2026-09-16"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 29 — Operational Subject Status Provenance

## H28 CONSOLIDATED INPUT

**H29 → SUPPORTED WITH QUALIFICATION dentro de Family Adventure A/B.** Los estados existentes permiten representar el estado operacional presente sin atribuir causa, actor, viewer, género personal, lugar ni recorrido. El resultado aborda experimentalmente `subjects[].status`; **L3c continúa abierto por su narrativa**.

La [Sesión 28](session-28-account-sourced-guest-presentation.md) queda **CLOSED**, con H28 **SUPPORTED WITH QUALIFICATION**. L3a conserva presentación exclusivamente de cuenta desde `member.name` y separación cuenta/sujeto verificada dentro del alcance ensayado. L3b permanece abordado experimentalmente por H27; L5 por H25. L4 sigue siendo un hallazgo abierto por inspección de fuente. No se reconstruyen las decisiones anteriores ni se revisa H26, que permanece **FALSIFIED**.

Architecture v0.5 ACTIVE, ADR-001–005 ACCEPTED, TES y Product Semantic Contract se preservan sin cambios. PSC-P01 sigue OPEN / EVIDENCE-BACKED PRESSURE; PSC-P02 no se crea. Las relaciones experimentales H25/H27 y el transporte/formato H28 permanecen sin promoción.

## H29 HYPOTHESIS

`GuestPerspective.subjects[].status` puede representar exclusivamente el estado operacional presente de cada sujeto desde `subjectStates`, sin nuevas relaciones de composición y sin modificar referencias, cuenta, labels de sujeto, Activity, atribución de Evidence, sesión operacional, contexto, evaluación, K o claim.

La hipótesis estudia `existing subject operational state → neutral present-state representation`. No requiere reconstruir por qué existe ese estado, quién produjo una transición ni quién es el viewer.

## VARIABLE UNDER TEST

Únicamente la construcción de **`GuestPerspective.subjects[].status`**. Se conserva el resto de la proyección, incluidos `sessionLabel`, labels, `message`, contadores y estado agregado; también la proyección de supervisión, Activity y App.

Las perturbaciones de entradas sólo existen en instancias y copias del harness. No se modifican los fixtures, Scenario o Scripts persistidos para conseguir el resultado.

## WHY L3c IS DIAGNOSTICALLY SPLIT

`subjects[].status` y `message` contienen afirmaciones distintas y pueden falsarse independientemente. El mapa operacional puede acreditar un estado presente aunque todavía falte una fuente legítima para la narrativa de recorrido.

Esta separación es diagnóstica. No se crean L3c1/L3c2, contratos, taxonomías TES ni extensiones PSC. Una ejecución positiva de status no permite declarar L3c RESOLVED.

## EXISTING OPERATIONAL STATE SOURCE

La inspección previa identifica exactamente tres valores en `DemoSubjectState`: **`not-enlisted`, `not-enabled`, `enabled`**. Los tres aparecen en los recorridos A/B existentes.

Scenario declara P1 y P2, su estado inicial y las acciones admitidas. `MockDataAdapter` clona `Scenario.initialSubjectStates` al construirse: P1 `not-enlisted`, P2 `not-enabled`. La acción `enlist-p1` valida sujeto, operación, checkpoint y referencia de sesión antes de asignar `enabled` a P1. `activate-p2` valida las condiciones existentes de activación antes de asignar `enabled` a P2. Ambas producen una transición operacional sin producir Evidence.

`discover-clue-a` y `discover-clue-b` verifican habilitación y atribución antes de añadir Evidence y evaluar. No asignan `subjectStates`. El reset restaura la copia de estados iniciales del Scenario y vacía Evidence/evaluación.

`getSnapshot` pasa ese mapa a `projectSnapshot`, que ya lo entrega como tercer argumento de `projectGuestPerspective`. No se necesita transportar otra fuente. `operationalSessionSubjectRef` participa en la admisión operacional y en supervisión; no proporciona una relación viewer→P1. Evidence mantiene sus sujetos, contextos y evaluación propios.

## PRE-DELTA STATE / COPY MATRIX

La [inspección anterior al delta](evidence/session-29/source-inspection.md) y su [matriz completa de 24 filas](evidence/session-29/pre-delta-state-copy-matrix.json) registran A/B, ambas referencias y las seis fases. Se obtuvieron de las fuentes inspeccionadas y de la traza consolidada H28, antes de modificar aplicación o harness histórico.

Esta tabla agrupa A/B, cuyos estados y copy históricos coinciden:

| subjectRef | Estado operacional | Fase / acción | Copy anterior | Información justificada por el estado | Información NO justificada por el estado |
| --- | --- | --- | --- | --- | --- |
| P1 | not-enlisted | initial | Sin alistar | Ausencia de alistamiento presente. | Causa, actor, viewer, género, lugar o recorrido. |
| P2 | not-enabled | initial | Sin habilitar | Ausencia de habilitación presente. | Causa, actor, viewer, género, lugar o recorrido. |
| P1 | enabled | enlist-p1 | Alistada y habilitada | Habilitación operacional presente. | Género; historia de alistamiento desde enabled por sí solo. |
| P2 | not-enabled | enlist-p1 | Sin habilitar | Ausencia de habilitación presente. | Causa o actor responsable. |
| P1 | enabled | discover-clue-a | Alistada y habilitada | Habilitación operacional presente. | Género, causa o interpretación de la pista. |
| P2 | not-enabled | discover-clue-a | Sin habilitar | Ausencia de habilitación presente. | Causa o actor responsable. |
| P1 | enabled | activate-p2 | Alistada y habilitada | Habilitación operacional presente. | Género, causa o historia del estado. |
| P2 | enabled | activate-p2 | Habilitado por ti | Habilitación operacional presente. | «Por ti», actor causal y género personal. |
| P1 | enabled | discover-clue-b | Alistada y habilitada | Habilitación operacional presente. | Género, historia y conclusión de recorrido. |
| P2 | enabled | discover-clue-b | Habilitado por ti | Habilitación operacional presente. | «Por ti», actor causal y género personal. |
| P1 | not-enlisted | reset | Sin alistar | Ausencia de alistamiento presente. | Explicación causal del estado. |
| P2 | not-enabled | reset | Sin habilitar | Ausencia de habilitación presente. | Explicación causal del estado. |

El copy anterior distinguía P1/P2 mediante el identificador, después de comprobar únicamente si su estado era `enabled`. El mapa operacional sí distingue los dos valores negativos. `enabled` es el mismo valor para ambos sujetos: no conserva si provino de alistamiento o activación, ni quién debe recibir atribución.

## SOURCE AUTHORITY

La dirección conservada es **Scenario subject → corresponding existing subjectState → status representation**. Scenario sigue determinando existencia y orden; el identificador sólo sirve para consultar su entrada de estado. La representación no crea sujetos ni escribe estados.

El mapping, elegido después de inspeccionar esa fuente, es:

| Estado existente | Representación |
| --- | --- |
| not-enlisted | `Estado: sin alistar` |
| not-enabled | `Estado: sin habilitar` |
| enabled | `Estado: habilitado` |

«Habilitado» concuerda con el sustantivo **Estado**, cuyo género aporta el propio copy, sin atribuir género a la persona. El texto no promete capacidades concretas ni afirma causa, actor, lugar o avance de recorrido.

No se usa member, subjectPresentations, Activity, Evidence count, K o claim como fuente de status. La coincidencia temporal entre una acción y una transición no se convierte en atribución al viewer.

## NO-NEW-COMPOSITION-RELATION CONDITION

La fuente existente resulta suficiente para esta representación reducida. No se añade `subjectStatusPresentations` a Script, Scenario o Fixture; no se crea registro de estados presentacionales, PresentationModel, PerspectiveModel ni equivalente.

La tabla literal local traduce tres valores operacionales ya definidos. No declara una nueva relación de composición ni una narrativa específica A/B. Si un estado estuviera ausente, no habría autoridad para afirmar ninguno de esos valores: el projector devuelve texto vacío. Es un comportamiento local conservador, probado aisladamente; no añade un cuarto estado ni establece una política productiva para datos incompletos.

## HOST / PROJECTION ANALYSIS

| Alternativa examinada | Resultado |
| --- | --- |
| Expresión `status` en el projector existente | Ya dispone de sujeto y mapa operacional. Permite el delta mínimo y local; seleccionada. |
| MockDataAdapter / nueva lógica de transición | Ya crea y transporta los estados. No necesita modificación. |
| Nueva declaración en Script, Scenario o Fixture | No hace falta para expresar el significado de los tres estados existentes; además está fuera de la condición del experimento. |
| Labels, cuenta o Activity | Son presentaciones de otras cosas y carecen de autoridad para determinar el estado. |
| Evidence / K / claim | Pueden cambiar sin transición operacional. No se usan para reconstruir un estado que ya existe. |
| App | Consume la proyección existente; no necesita cambio. |

La nueva expresión sólo consulta `subjectStates[id]`. El resto del projector puede seguir usando evaluación y estados para responsabilidades preexistentes; esa coexistencia no autoriza incorporarlos a la expresión ensayada.

## THREADING PATH

```text
Scenario.subjects ───────────────────────────────→ subjects.map(id)
Scenario.initialSubjectStates → adapter clone             │
  → admitted enlist/activate transition → subjectStates    │
  → getSnapshot → projectSnapshot                          │
  → projectGuestPerspective(subjectStates)                 │
  → existing subjectStates[id] ←───────────────────────────┘
  → neutral status text

reset → restore Scenario.initialSubjectStates
Evidence actions → preserve subjectStates
```

Todo este transporte existía antes de H29. No hay nuevo parámetro, objeto, identidad ni relación account/viewer/session→subject.

## BASELINE

La [baseline H29](evidence/session-29/baseline.json) preserva hashes SHA-256 de **204 archivos** del estado de trabajo recibido. Suite previa: **90/90 pruebas en 22 archivos**. Se conserva la historia existente sin reconstruirla desde Git.

**196 archivos permanecen byte a byte iguales**. Las ocho excepciones son un archivo de aplicación y siete harness históricos; todas sus versiones previas están archivadas con sus hashes originales en `test-fixtures/h28`. Los documentos, trazas y baselines H21–H28 no se reescriben.

La primera regresión dirigida tuvo 17 pruebas correctas y un fallo de copy en el test UI S20, que todavía exigía «Alistada y habilitada». Se amplió de forma explícita la instrumentación histórica para que S20 use la proyección pre-H29. Se conservan sus aserciones, incluidas «Habilitado por ti», navegación y acciones. Los lectores de hashes H23–H28 se dirigen a las fuentes archivadas cuando corresponde; las rutas históricas anteriores tienen precedencia. Un intento intermedio durante esa adaptación detectó cuatro lecturas de hashes aún sin redirigir, corregidas antes del ensayo principal. Ninguno de esos fallos constituyó un falsificador operacional de H29.

El registro de ampliación está en la baseline; los hashes capturados antes del delta no se cambian. Los bridges de test reexportan módulos compartidos preservados. El ensayo H29 usa el provider y projector vivos, sin ese mock histórico.

## CODE DELTA

El [delta de aplicación](evidence/session-29/application-delta.patch) afecta únicamente a `src/demo-factory/vertical-evaluation.ts`: sustituye la expresión de status dependiente de enabled/P1 por el lookup neutral de los tres valores existentes.

El [harness H29](../prototype/src/demo-factory/operational-subject-status-h29.test.ts) verifica igualdad exacta del módulo completo contra la fuente archivada aplicando sólo esa sustitución. La construcción de `message`, cuenta, labels, contadores, estado agregado, supervisión y el evaluador permanece byte a byte igual. El adaptador, App, contratos y composiciones se mantienen por hash.

El [delta de instrumentación histórica](evidence/session-29/historical-instrumentation-delta.patch) contiene exclusivamente imports, rutas de lectura y el mock del projector pre-H29. No cambia expectativas históricas para hacer pasar el nuevo copy.

## A CONTROL

En `hospitality-family-adventure`, la cuenta sigue siendo `Cuenta de Lucía`; labels Lucía / Huésped 2. Las seis fases muestran el status correspondiente al mapa operacional, con independencia de las referencias y nombres presentados.

Cada frame completo coincide con H28 al excluir exclusivamente `subjects[].status`. Se comparan asimismo llamadas y resultados de evaluación. Activity conserva jardín/fuente, atribución de Evidence P1/P2, contexto A y claim final.

## B CONTROL

En `hospitality-family-adventure-costa`, la cuenta sigue siendo `Cuenta de Inés`; labels Inés / Mateo. Para igual referencia y estado, los status coinciden exactamente con A, aunque contexto, cuenta, labels y Activity mirador/patio difieren.

El resto de cada frame coincide con H28, incluida la narrativa histórica de jardín/fuente. El mismatch de B continúa visible y no se utiliza para personalizar el status. No aparece presión para añadir una declaración de status por composición dentro del alcance ensayado.

## TEMPORAL / TRANSITION CONTROL

| Fase | Estado P1 → status | Estado P2 → status | Cambio relevante |
| --- | --- | --- | --- |
| initial | not-enlisted → Estado: sin alistar | not-enabled → Estado: sin habilitar | Estados iniciales de Scenario. |
| enlist-p1 | enabled → Estado: habilitado | not-enabled → Estado: sin habilitar | Cambia únicamente el estado/status de P1. |
| discover-clue-a | enabled → Estado: habilitado | not-enabled → Estado: sin habilitar | Aumenta Evidence; status estable. |
| activate-p2 | enabled → Estado: habilitado | enabled → Estado: habilitado | Cambia únicamente el estado/status de P2. |
| discover-clue-b | enabled → Estado: habilitado | enabled → Estado: habilitado | Aumenta Evidence; status estable. |
| reset | not-enlisted → Estado: sin alistar | not-enabled → Estado: sin habilitar | Restaura ambos estados/status iniciales. |

Las transiciones de habilitación no producen Evidence ni Activity. En cada transición se comprueba que cambia el status del objetivo y permanece el del otro sujeto. El reset devuelve exactamente el snapshot inicial de cada variante.

## ACCOUNT INDEPENDENCE CONTROL

En A y B se perturba sólo `member.name` a **Cuenta Demo**. `sessionLabel` cambia a `Cuenta de Cuenta Demo`, manteniendo todos los status y labels.

Scenario y Script son iguales al control original. Los frames completos, descontando sólo member.name y sessionLabel, coinciden: Evidence, contexto, evaluación, Activity, estados y sesión operacional no cambian. La cuenta H28 no adquiere autoridad operacional.

## SUBJECT PRESENTATION INDEPENDENCE CONTROL

En ambas composiciones, una copia de Script cambia los labels a **Participante Alfa / Participante Beta**, conservando sus referencias y todas las demás entradas. Los labels resultantes cambian y los status no.

La comparación íntegra excluye únicamente los labels; cuenta, mapa de estados, Activity, Evidence, evaluación y claim son iguales. La rutina comprueba los labels exactos y Scenario idéntico, sin inferir estado desde representación humana.

## ACTIVITY REPRESENTATION INDEPENDENCE CONTROL

En A y B se sustituyen sólo title/description de las entradas H25 existentes por textos alternativos identificados por step. Se conservan actionId, payloads, sujetos, tiempos, contextos, referencias y todos los demás campos del Script.

La Activity materializada cambia tras las acciones de Evidence. El resto de los frames, descontando exclusivamente title/description de Activity, coincide con el original, incluidos status. Los IDs, fechas, procedencia y orden de Activity siguen iguales. Esto separa representación de lo ocurrido y estado operacional presente sin desactivar Activity para el ensayo.

## EVIDENCE DISCRIMINATION CONTROL

Se comparan `enlist-p1 → discover-clue-a` y `activate-p2 → discover-clue-b`. En ambas parejas aumenta Evidence en una unidad y cambia Activity; los mapas de estado y status permanecen idénticos.

La suficiencia pasa de not-attempted a not-established en la primera pareja y de not-established a established en la segunda. El claim pasa respectivamente de not-produced a not-established y de not-established a established. Esos cambios no alteran status.

Como control aislado adicional del projector, se fija P1/P2 en enabled y se compara evaluación vacía con evaluación completa tomada de la traza real. El status de ambos sigue siendo `Estado: habilitado`, también al variar cuenta y retirar labels. Este control es contrafactual de proyección: no se presenta como una secuencia alcanzable del provider.

## CAUSALITY NEGATIVE CONTROL

Después de `activate-p2`, el estado de P2 sólo se representa como **`Estado: habilitado`**, idéntico al de P1 con igual estado. No se conserva «por ti» ni se añade «por P1», «por Inés», «por Lucía» o «por la cuenta».

Las reglas operacionales pueden exigir una sesión P1 habilitada para admitir la acción; esa precondición no se convierte en identidad de viewer ni en una atribución causal dentro de status. La expresión no consulta acción anterior, sesión ni historial.

Otro control aislado intercambia los estados negativos entre P1/P2 y obtiene `Estado: sin habilitar` para P1 y `Estado: sin alistar` para P2. Demuestra que el texto sigue el valor y no una frase asociada al identificador. Con estados ausentes se obtienen strings vacíos, incluso ante Evidence/claim completos; con lista de sujetos vacía no aparecen sujetos aunque existan entradas de estados y labels. Esas entradas contrafactuales no amplían los estados alcanzables del Scenario ni legitiman una nueva composición.

## EXECUTION TRACE

La [traza principal H29](evidence/session-29/execution-trace.json) registra hashes de baseline, aplicación y harness; argumentos completos del projector; snapshots; llamadas y resultados de los evaluadores vertical y conjunto. Se generó con escritura exclusiva después de superar la verificación completa.

Contiene **ocho recorridos vivos Family Adventure**: original, variante de cuenta, variante de labels y variante de Activity por cada A/B. Cada recorrido incluye initial, cuatro acciones y reset: **48 observaciones de snapshot**. Los seis juegos de argumentos del projector quedan registrados por recorrido. En A/B originales coinciden íntegramente con H28; sólo cambia la construcción autorizada de status.

Las acciones Evidence invocan una vez cada evaluador; enlist/activate no los invocan. Se conservan los resultados y premisas completos, sin sustituirlos por un resumen visual de K. Los controles aislados de proyección están identificados aparte en la traza.

`retail-baseline` y `hospitality-stay` se ejecutan sobre el provider vivo: todos sus frames y reset coinciden con H28. La rama genérica de Activity se preserva.

| Verificación | Resultado |
| --- | --- |
| Suite antes del delta | 90/90 pruebas; 22 archivos. |
| S20, H21–H28 y nuevo H29, tras adaptar instrumentación histórica | 19/19 pruebas; 10 archivos. |
| `npm run check` | Typecheck, lint, 91/91 pruebas en 23 archivos y build PASS. |
| Captura principal H29 | 1/1 PASS; sin sobrescribir evidencia anterior. |
| Auditoría final | [verification.json](evidence/session-29/verification.json): hashes, delta permitido, secciones y enlaces. |

Reproducción: `npm test -- src/demo-factory/operational-subject-status-h29.test.ts`. Para otra captura, `H29_RECORD_PATH` debe apuntar a una ruta nueva. No se realizó validación visual en navegador; la prueba de navegación S20 usa jsdom y el projector histórico. El comportamiento nuevo se acredita por ejecución del provider/proyector vivo y por inspección de fuentes.

## L3a STATUS

**PRESERVED / EXPERIMENTALLY ADDRESSED H28.** `sessionLabel` sigue derivando únicamente del nombre de cuenta; su construcción y transporte no cambian. Variar la cuenta no afecta al estado presentado. El transporte/formato H28 permanece LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED.

## L3b STATUS

**PRESERVED / EXPERIMENTALLY ADDRESSED H27.** Los labels proceden exclusivamente de `DemoScript.subjectPresentations`; no determinan estado ni se reconstruyen desde él. La relación continúa EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.

## L3c SUBJECT STATUS RESULT

**EXPERIMENTALLY ADDRESSED / STATE-ONLY / EXECUTION-VERIFIED within A/B.** La fuente operacional existente acredita las tres representaciones neutrales. La afirmación se ha reducido a esa evidencia, eliminando género personal y atribución causal/perspectival de este campo.

No se declara un contrato productivo de estados, ni suficiencia universal para todas las Experiences o idiomas. El tipo operacional ya estaba marcado como experimento local de demo.

## L3c REMAINING NARRATIVE PRESSURE

**PRESERVED / OPEN.** `GuestPerspective.message` conserva su construcción byte a byte y sus salidas en todas las fases frente a H28. Permanecen «Estás alistada», «Tu pista del jardín», «Has habilitado» y la instrucción sobre la fuente, incluso en B con Activity mirador/patio.

La narrativa de recorrido, segunda persona, localización y género de message no se selecciona en esta sesión. Sus síntomas siguen siendo observables. No falsifican H29, cuya variable es status, ni quedan legitimados por su resultado positivo. L3c global sigue abierto.

## L4 STATUS

**PRESERVED / SOURCE-INSPECTION / OPEN.** App permanece byte a byte igual. No se usa una corrección incidental de interfaz para aparentar que B está completamente situada, ni se afirma validación visual actual de A/B.

## L5 STATUS

**PRESERVED / EXPERIMENTALLY ADDRESSED H25.** En controles originales Activity coincide íntegramente con H28. En variantes explícitas sólo cambia su copy declarado, sin efecto operacional ni sobre status. La representación H25 continúa en cuarentena.

## FALSIFICATION ANALYSIS

| Falsificador | Observación |
| --- | --- |
| Necesitar otra relación para derivar status | No observado: los tres valores existentes bastan para el significado reducido. |
| Cambiar cuenta cambia status | No observado en A/B; comparación completa de frames. |
| Cambiar labels cambia status | No observado en A/B, incluido Participante Alfa. |
| Cambiar representación Activity cambia status | No observado: copy alternativo con hechos y acciones idénticos. |
| Necesitar Evidence/K/claim para reconstruir estado | No observado; fases con evaluación distinta y estados/status iguales, más control aislado. |
| Necesitar actor/viewer/operator/participant/representative o relación equivalente | No se introduce. El estado habilitado no recibe atribución causal o de viewer. |
| Requerir status distintos por composición para igual estado | No observado; A/B producen idéntico status por fase. |
| Añadir una relación declarativa de composición | No se añade; delta restringido a la expresión existente. |

No se activa ningún falsificador seleccionado. El fallo inicial de copy UI era una expectativa histórica fuera del nuevo experimento; se conserva contra su fuente previa, sin alterar la expectativa ni retirar el control. Los controles vivos H29 demuestran el resultado nuevo independientemente de ese replay histórico.

## H29 VERDICT

**SUPPORTED WITH QUALIFICATION.** En los recorridos A/B, el estado operacional existente resulta autoridad suficiente para status neutral del presente, sin relación de composición nueva ni ampliación semántica para conservar el copy anterior.

La calificación comprende provider mock, conjunto finito de tres estados y proyección local. No demuestra identidad autenticada, causalidad, narrativa situada, una política general para ausencia de estado ni validez universal de este vocabulario. Las variantes son instancias separadas; no modelan cambios de cuenta en una sesión autenticada viva.

## ARCHITECTURAL CONSEQUENCE

Esta variable puede resolverse experimentalmente en su projector actual utilizando transporte existente. No hace falta ampliar Script, Scenario, Fixture, shared contracts ni diseñar un sistema general de presentación.

Architecture v0.5 sigue ACTIVE y ADR-001–005 ACCEPTED, sin cambios. No se crean Actor, Operator, Participant, Representative, accountSubject o viewerSubject. La separación diagnóstica status/message no se promueve a arquitectura. El parche es local y reversible.

## SEMANTIC CONSEQUENCE

Tener un estado no equivale a conocer su causa. Observar una transición no equivale a saber a quién atribuírsela. Conocer el sujeto operacional no identifica al viewer; saber que P1 opera en la sesión no acredita viewer=P1. La representación del estado tampoco acredita narrativa de recorrido.

TES y Product Semantic Contract permanecen intactos. PSC-P01 sigue **OPEN / EVIDENCE-BACKED PRESSURE** sin modificación; **PSC-P02 → NOT CREATED**. H29 no constituye promoción semántica ni altera las conclusiones históricas falsificadas.

## ARTIFACT QUARANTINE

| Artefacto | Estado conservado |
| --- | --- |
| `DemoScriptStep.activityPresentation` | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. |
| `DemoScript.subjectPresentations` | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. |
| Transporte/formato de cuenta H28 | LOCAL PROTOTYPE EXPERIMENT / NOT PROMOTED. |
| Mapping local status H29 | Experimento reversible de prototype; no contrato ni relación de composición promovida. |
| Archivos históricos y bridges | Instrumentación de regresión; no nueva autoridad de producto. |

## WHAT H29 DOES NOT PROVE

- No acredita quién habilitó a P2, quién merece atribución o quién es el viewer autenticado.
- No relaciona cuenta, viewer o autenticación con P1/P2.
- No demuestra género personal, ubicación, recorrido o capacidades específicas a partir de enabled.
- No resuelve message, L3c global ni App/L4.
- No generaliza a otras Experiences, estados futuros, idiomas o una política productiva para estados ausentes.
- No promueve H25/H27/H28 ni un modelo universal de presentación.
- Los controles aislados del projector no prueban que sus combinaciones contrafactuales sean alcanzables mediante las acciones admitidas.

## REMAINING PRESSURES

La procedencia de la narrativa de `GuestPerspective.message` permanece materialmente observable, junto con L4 en App. La relación viewer/account/authentication→subject sigue ausente; no se diseña para rescatar frases históricas.

Estas presiones quedan **observadas y NOT SELECTED**. No se abre H30 automáticamente.

| Dimensión | Resultado consolidado |
| --- | --- |
| H29 | **SUPPORTED WITH QUALIFICATION** |
| L3c SUBJECT STATUS | **EXPERIMENTALLY ADDRESSED / STATE-ONLY / EXECUTION-VERIFIED within A/B** |
| STATE / PRESENTATION AUTHORITY | **SUPPORTED from existing subjectStates within tested scope** |
| CAUSAL / VIEWER ATTRIBUTION | **NOT INTRODUCED** |
| L3a | **PRESERVED / EXPERIMENTALLY ADDRESSED H28** |
| L3b | **PRESERVED / EXPERIMENTALLY ADDRESSED H27** |
| L3c JOURNEY NARRATIVE | **PRESERVED / OPEN** |
| L4 | **PRESERVED / SOURCE-INSPECTION / OPEN** |
| L5 | **PRESERVED / EXPERIMENTALLY ADDRESSED H25** |
| NEXT MATERIAL PRESSURE | **message narrative y L4 observed but NOT SELECTED; H30 NOT OPENED** |
