---
title: "Sesión 25 — Script-Bound Situated Activity Representation"
language: es
version: "v1.0"
status: "H25 supported with qualification; experimental local relation, not promoted"
date: "2026-09-14"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 25 — Script-Bound Situated Activity Representation

## H24 CONSOLIDATED INPUT

**H25 → SUPPORTED WITH QUALIFICATION dentro del recorrido A/B probado.** El Script declara una representación posterior separada de la affordance. Esa representación aparece únicamente tras una acción de Evidence aceptada, puede variar sin alterar hechos/evaluación y puede faltar sin impedir la consecuencia factual. El adaptador deja de decidir jardín/fuente desde el sujeto.

El [resultado consolidado de H24](session-24-situated-activity-representation-provenance.md) permanece **FALSIFIED**: bajo su restricción de usar sólo relaciones existentes, no había procedencia legítima de representación situada posterior. Introducir una relación nueva en H25 no cambia aquella premisa ni aquel resultado.

```text
SESSION 20 → CLOSED
H21 → FALSIFIED for historical baseline
H22 → SUPPORTED WITH QUALIFICATION
H23 → SUPPORTED WITH QUALIFICATION
H24 → FALSIFIED / NO LEGITIMATE EXISTING SOURCE
L1 → SITUATED BINDING EXECUTION-VERIFIED
L2a/L2b → EXPERIENCE-BASED SELECTION EXECUTION-VERIFIED
L5 → EXECUTION-CONFIRMED / OPEN (entrada H25)
L3 → EXECUTION-CONFIRMED / OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN
```

## H25 HYPOTHESIS

**H25 — Script-Bound Situated Activity Representation.** Un paso de DemoScript puede declarar representación situada de Activity distinta de su affordance previa. Sólo se materializa después de aceptar la acción correspondiente y puede variar o faltar sin modificar Evidence, atribución, contexto, estado operacional, admisibilidad, K o claim.

La relación es experimental, local y reversible; no es un contrato productivo ni un concepto TES.

## VARIABLE UNDER TEST

La nueva relación `DemoScript.steps[].activityPresentation → Activity posterior a la acción aceptada`, exclusivamente para la rama de acciones de Evidence con `requiresEnabledSubject` ya existente en Family Adventure A/B. Se comprueba procedencia y separación respecto del hecho, no ubicación arquitectónica definitiva de Activity.

Se congelan las guardas de aceptación, selectores H22, binding H23, evaluadores H17, criterio K, premisa, atribución, GuestPerspective y App. No se estudia recurrencia fuera de este recorrido.

## WHY A NEW RELATION IS NOW PERMITTED

La instrucción de Sesión 25 autoriza expresamente probar la relación que H24 identificó como ausente. Esa autorización tiene un alcance nuevo y limitado: campo opcional local dentro del paso de Script y transporte mínimo al adaptador mock. No permite reinterpretar `presenterLabel`, introducir un registro de contenido ni revisar H24 retrospectivamente.

## CANDIDATE HOST ANALYSIS

Inspección previa al delta: se revisaron [contratos](../prototype/src/demo-factory/contracts.ts), [resolver](../prototype/src/demo-factory/bootstrap.ts), [adaptador/proyección](../prototype/src/demo/mock-adapter.ts), artefactos [A](../prototype/src/demo-factory/artifacts.ts) y [B](../prototype/src/demo-factory/costa-artifacts.ts), integración H23 y harness históricos. Se confirmó que `resolveDemo()` ya dispone de Scenario y Script resueltos y construye el provider en un único punto.

| Host o ruta | Decisión y motivo |
| --- | --- |
| Paso de DemoScript | Seleccionado bajo autorización H25. Ya relaciona un paso con `action.actionId`; puede alojar una representación separada de la etiqueta previa. |
| `presenterLabel` | No reutilizado. Sigue siendo affordance; no se analiza, convierte ni sustituye texto. |
| `EvidenceInput` / Public Action | Intactos. No necesitan transportar narrativa: el resolver ya tiene el Script. |
| Scenario / Experience | No reciben contenido nuevo ni cambian semántica. Scenario sigue gobernando transiciones y sujetos. |
| Fixture Activity inicial | Sigue representando registros ya materializados; no se precargan hallazgos futuros. |
| Nuevo registry, engine o servicio público | Innecesario y fuera de autorización. No se introduce. |

## EXPERIMENTAL SCRIPT SHAPE

El contrato local existente usa una forma inline para `DemoScript.steps`; no se crea una interfaz nominal amplia ni un tipo `completion*`.

```ts
steps: Array<{
  id: string;
  presenterLabel: string; // affordance BEFORE action
  // H25: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
  activityPresentation?: {
    title: string;
    description: string;
  };
  expectedCheckpoint: string;
  action: DemoAction | DemoEnableAction;
}>;
```

`DemoScriptStep.activityPresentation` designa aquí ese campo conceptual del paso, no un nuevo concepto productivo. En A/B sólo lo declaran los dos pasos de Evidence. Enlist y activate mantienen el comportamiento previo, sin añadir Activity.

## REPRESENTATION AUTHORITY

`activityPresentation` es **presentation input**, no fact, Evidence, estado de ocurrencia, entrada de evaluación ni autoridad semántica. La copia privada de Script en el constructor es configuración presentacional de la demo resuelta; no añade hechos al runtime.

El adaptador consulta únicamente `step.action.actionId` para relacionar la representación con la acción recibida y lee `title/description`. No obtiene del Script Evidence efectiva, checkpoint de destino, habilitación o contexto evaluado. Las validaciones ya existentes del resolver siguen siendo validaciones de composición; no convierten una declaración en ocurrencia.

## THREADING PATH

```text
resolved DemoScript
→ MockDataAdapter(fixture, scenario, script?)
→ copia de configuración presentacional

Public Action (sin cambios)
→ guardas existentes de Scenario, checkpoint, habilitación y atribución
→ si se rechaza: sin mutación factual ni Activity nueva
→ si se acepta Evidence: colección factual + evaluación existente
→ step ligado por actionId → activityPresentation opcional
→ ActivitySourceRecord → projectSnapshot() → AppSnapshot.activity
```

La nueva dependencia es el tercer argumento opcional del constructor concreto mock. `DemoProvider` conserva exactamente `getSnapshot`, `executeAction` y `reset`, con las mismas responsabilidades y firmas. La acción pública conserva su forma; no recibe textos adicionales.

Materialización continúa en el punto local existente. El checkpoint se actualiza al final de la misma llamada como antes. No se cambia ese procedimiento ni se afirma que ésta sea la ubicación final adecuada para Activity.

## BASELINE

Suite previa al delta: **86/86 PASS, 18 archivos**. La [baseline H25](evidence/session-25/baseline.json) captura 146 archivos del estado de trabajo recibido, con sus cambios previos sin commit. De ellos, 137 se conservan byte a byte y nueve tienen un delta explícito: cinco fuentes de aplicación y cuatro harness con adaptación de reproducción histórica.

Los nueve originales se archivan byte a byte bajo [test-fixtures/h24](../prototype/src/demo-factory/test-fixtures/h24/mock-adapter.ts). Los cuatro harness originales se conservan como `.test.ts.txt`, evitando una segunda ejecución accidental. El harness H25 verifica cada archivo preservado y cada original archivado contra su huella anterior.

Baselines, informes y trazas históricos no se reescriben. Se conservan también TES, Architecture v0.5, ADR, Product Semantic Contract y registro de presiones. La comparación del delta utiliza esta baseline del estado recibido, no HEAD, que contiene diferencias acumuladas de sesiones anteriores.

## CODE DELTA

El [delta de aplicación contra H24](evidence/session-25/application-delta.patch) contiene exactamente:

| Archivo | Cambio |
| --- | --- |
| `contracts.ts` | Campo opcional inline `activityPresentation` dentro de los pasos, con cuarentena explícita. EvidenceInput, Public Action y DemoProvider intactos. |
| `artifacts.ts` | Dos representaciones explícitas de A: jardín/fuente y sus descripciones originales. Ningún cambio factual, operacional ni de affordance. |
| `costa-artifacts.ts` | Dos representaciones explícitas de B: mirador/patio, con descripciones situadas Inés/Mateo. |
| `bootstrap.ts` | `new MockDataAdapter(fixture, scenario, script)` en vez de dos argumentos. |
| `mock-adapter.ts` | Copia privada de Script; lectura por actionId después de aceptación; materialización condicional de título/descripción suministrados. Se eliminan los ternarios narrativos P1/jardín y resto/fuente. |

Para la rama `requiresEnabledSubject`, ausencia de representación significa que no se inserta un registro situado. La rama genérica conserva `title: evidence.type` y «Evidencia recibida desde source». No es fallback de Family Adventure: se selecciona por la rama preexistente, no por faltar representación.

`projectSnapshot()` permanece idéntica. Todas las guardas anteriores a agregar Evidence permanecen idénticas. El harness verifica estas secciones y que el adaptador no contenga jardín/fuente/mirador/patio ni `presenterLabel`. Integración H23, K y proyecciones guest/supervision permanecen intactos.

La instrumentación añade el [harness H25](../prototype/src/demo-factory/script-bound-activity-h25.test.ts). Las reproducciones H21–H24 ahora resuelven la composición y el bootstrap previos desde el archivo H24, conservando las versiones H21/H22 de adaptador/evaluación que ya usaban. H23/H24 ejecutan el adaptador previo a H25, con la integración H23 intacta. Las expectativas y veredictos originales se mantienen.

Un helper exclusivo de tests dirige las comprobaciones de huellas a las fuentes archivadas cuando corresponde. Dos reexports y dos copias de logos resuelven imports relativos del bootstrap/artefactos archivados sin editar sus bytes. No entran en el bundle de aplicación. La regresión sobre el provider vivo se verifica separadamente en H25.

## A CONTROL

Se ejecuta `enlist-p1 → discover-clue-a → activate-p2 → discover-clue-b` sobre el resolver y provider vivos. Los cinco frames, incluido el inicial, coinciden íntegramente con H24; reset devuelve el snapshot inicial.

| Acción factual | Activity efectiva |
| --- | --- |
| `evidence-a-p1 → subject-p1 → marker-a` | «Pista del jardín encontrada» / «Hallazgo aportado por ti.» |
| `evidence-b-p2 → subject-p2 → marker-b` | «Pista de la fuente encontrada» / «Hallazgo atribuido al huésped 2, registrado desde tu cuenta.» |

Se conservan ID, fecha, icono, tono, provenance y orden de Activity, además de la evaluación y todas las otras superficies. La regresión vertical existente verifica también la navegación y textos aceptados de A, sin cambiar su aceptación histórica.

## B CONTROL

La misma secuencia y clase de provider produce:

| Acción factual | Activity efectiva |
| --- | --- |
| `evidence-costa-a-p1 → subject-p1 → marker-a` | «Pista del mirador encontrada» / «Hallazgo aportado por Inés.» |
| `evidence-costa-b-p2 → subject-p2 → marker-b` | «Pista del patio encontrada» / «Hallazgo atribuido a Mateo, registrado desde la cuenta de Inés.» |

Las Activity correspondientes a estos hallazgos no contienen jardín/fuente. El harness compara todos sus campos no textuales con H24 y verifica que únicamente varían título/descripción. No corrige otras superficies de B.

Para A y B, todos los frames comparan Evidence íntegra, argumentos verticales, entrada completa del evaluador conjunto, premisa, criterio, resultados y claim completa contra H24. La entrada contextual mantiene Aurora/AS-8842/stay-AS-8842 en A y Costa/CC-205/stay-CC-205 en B. Property situada sigue aportándose desde Scenario cuando falta en Evidence, como en H23; H25 no convierte esa aportación en una nueva observación factual.

## DECLARATION / OCCURRENCE CONTROL

Cada Script original contiene dos `activityPresentation` antes de ejecutar nada. El snapshot inicial sólo proyecta los registros previos del fixture: no hay Activity de pistas, Evidence está vacía, K está `not-attempted` y claim `not-produced`.

Alistar P1 tampoco crea Evidence ni Activity. La representación del primer hallazgo aparece al aceptar `discover-clue-a`; activar P2 no crea la del segundo. Ésta sólo aparece al aceptar `discover-clue-b`. Todas las variantes conservan esa separación temporal. Reset elimina las ocurrencias generadas y vuelve al inicial aunque el Script siga declarando representaciones.

## FACT / REPRESENTATION INDEPENDENCE CONTROL

Se crean dos variantes X/Y de cada Script, exclusivamente en el harness. Sólo cambian `activityPresentation.title/description`. Al retirar el nuevo campo de la vista de comparación, ambos Scripts son idénticos al original: mismos actionIds, Public Actions, Evidence payload/IDs/type, sujetos y contextos; Scenario también permanece igual.

Se ejecutan los cuatro pasos en cada variante. Tras la primera Evidence y tras A+B:

```text
facts X == facts Y
operational state X == Y
context / markers / premise X == Y
evaluation / K / full claim X == Y
Activity title/description X != Y
Activity other fields X == Y
```

Los spies invocan los evaluadores originales y capturan argumentos/resultados; no fabrican resultados de evaluación. No se edita el snapshot para producir diferencias. Las vistas que omiten Activity o neutralizan sus textos se usan sólo en comparaciones, después de recibir el output real.

Un control adicional cambia todas las affordances manteniendo `activityPresentation`: los frames completos permanecen iguales. Otro introduce `expectedCheckpoint` incorrecto y payloads declarados distintos en los pasos de Evidence del Script, pero envía las acciones públicas originales: la ejecución conserva exactamente el resultado original. La nueva dependencia no reemplaza el hecho presentado ni las transiciones gobernadas por Scenario. No se presenta este diagnóstico como validación general de Scripts arbitrarios.

## REJECTED ACTION CONTROL

En cada composición se declara la representación, pero se intenta:

1. `discover-clue-a` sin alistar P1: rechazo por sujeto no habilitado.
2. `discover-clue-b` desde el checkpoint inicial: rechazo por checkpoint incorrecto.

Son cuatro rechazos por guardas preexistentes intactas. Los snapshots anteriores/posteriores son iguales, Evidence permanece vacía, no hay Activity nueva y no se llama a evaluación. La representación declarada no fuerza el hecho. La regresión vertical preserva además los controles de atribución incorrecta, payload mixto y marcador incompatible.

## ABSENCE CONTROL

En A y B se ejecutan tres variantes: representación ausente en la primera acción de Evidence, en la segunda y en ambas. Sólo se elimina el campo opcional; la acción factual sigue siendo válida.

Los frames fuera de Activity y todos los argumentos/resultados de evaluación son idénticos al control original. Activity equivale exactamente al control original quitando los registros correspondientes a las representaciones ausentes. Se conservan los registros iniciales y cualquier otro hallazgo representado; no se inventan textos situados ni se usa la rama genérica como sustituto.

```text
accepted fact + no activityPresentation
→ Evidence and evaluation remain
→ no new situated Activity record for that action

LOCAL EXPERIMENTAL ABSENCE BEHAVIOR
NOT PRODUCT FALLBACK POLICY
```

No se necesita otro contrato o estado para expresar esta ausencia local. No se define una política productiva para contenido vacío, malformado, traducción ausente o diagnóstico al usuario; esos casos no son equivalentes a omitir el campo y no se promueven por este resultado.

## GENERIC ACTIVITY REGRESSION

Retail y Hospitality Arrival se ejecutan sobre el código vivo y conservan sus snapshots H23 de inicio/acción/reset. Arrival no declara `activityPresentation` y sigue creando Activity con `booking.checked_in` y «Evidencia recibida desde demo-control». No recibe GuestPerspective, SupervisionPerspective ni evaluación Family Adventure. Retail conserva su Activity inicial sin Experience declarada.

Los consumidores existentes y la suite de proyección permanecen compatibles. No se obliga a otras Experiences a adoptar la nueva relación y no se afirma recurrencia representacional entre Experiences.

## EXECUTION TRACE

La [traza principal](evidence/session-25/execution-trace.json) se capturó el **2026-09-14T16:09:21.867Z**, 17:09:21 Europe/Lisbon. Incluye huellas de baseline, cinco fuentes de aplicación y harness ejecutado.

| Ruta de traza | Contenido |
| --- | --- |
| `controls[0/1].original` | A/B vivos, Script/Scenario, cinco frames y reset; hechos y evaluación comparados con H24 |
| `controls[0/1].variants[0/1]` | X/Y, variando exclusivamente representación |
| `controls[0/1].absenceControls[0..2]` | Ausencia de primera, segunda o ambas representaciones |
| `controls[0/1].changedAffordance` | Affordance independiente de Activity |
| `controls[0/1].scriptAuthority` | Script no sustituye payload público ni checkpoint runtime |
| `controls[0/1].rejected` | Cuatro rechazos sin mutación ni evaluación |
| `genericActivityRegression` | Retail/Arrival con snapshots históricos conservados |
| `mismatchControls` | Dos sentidos de contradicción factual/contextual H23 sobre provider vivo |
| `authorityControls` | Seis controles sobre evaluador real: premisa ausente, scope incorrecto o cobertura insuficiente |

Hay 16 secuencias completas originales/variantes/diagnósticos A/B, dos secuencias adicionales de contradicción, cuatro intentos rechazados y los controles genéricos/de autoridad. Los frames factuales registran el payload efectivo completo y los argumentos/resultados reales del evaluador, incluida claim completa. No se infiere conservación factual únicamente desde el read model de supervisión.

En la regresión de contradicción, Evidence conserva el contexto presentado y K queda sin intentar, sin claim producida. Una acción factual aceptada aún puede materializar su representación suministrada: **representar un hallazgo no acredita suficiencia ni autoridad**. Los controles sin premisa aplicable preservan indeterminación. H23 sigue reproduciendo también sus controles originales de contexto incompleto y cobertura de sujetos.

Las ejecuciones ordinarias no escriben trazas. `H25_RECORD_PATH` permite un destino nuevo y usa escritura exclusiva; la captura principal no se sobrescribe durante la suite posterior.

| Verificación | Resultado |
| --- | --- |
| Suite previa al delta | 86/86 PASS, 18 archivos |
| H25 focalizado y captura principal | 1/1 PASS, controles secuenciales completos |
| H24 histórico + H23 + H22 + H21 histórico + Sesión 20 vertical | 14/14 PASS, 5 archivos |
| Suite completa final | 87/87 PASS, 19 archivos |
| Typecheck | PASS |
| Lint | PASS |
| Build TypeScript + Vite + PWA | PASS |

Reproducción desde `products/convercus-app/prototype/`:

```sh
npm test -- src/demo-factory/script-bound-activity-h25.test.ts
npm test -- src/demo-factory/situated-activity-provenance-h24.test.ts src/demo-factory/situated-evaluation-context-h23.test.ts src/demo-factory/experience-stable-selection-h22.test.ts src/demo-factory/composition-boundary-h21.test.ts src/demo-factory/family-adventure-vertical.test.ts
npm run check
```

No se necesita navegador: `projectSnapshot()` conserva título/descripción y ActivityList consume esos campos directamente. No se renderiza B ni se declara nueva aceptación manual de UI.

## L5 RESULT

**L5 → SCRIPT-BOUND SITUATED REPRESENTATION EXECUTION-VERIFIED en A/B, con cualificación.** El acoplamiento histórico por sujeto se elimina del adaptador vivo en la rama ensayada. La representación está explícitamente situada en el Script y no participa en la evaluación.

El estado histórico EXECUTION-CONFIRMED / OPEN permanece en H24. H25 resuelve experimentalmente esa manifestación de L5; no cierra una arquitectura general de procedencia o representación de Activity.

## L3 STATUS

**L3 → PRESERVED / OUT OF SCOPE / EXECUTION-CONFIRMED.** GuestPerspective B conserva Lucía/jardín/fuente en sus fases correspondientes. Sus frames coinciden con H24. `activityPresentation` no se reutiliza para corregir esta superficie: contenido parecido no demuestra la misma responsabilidad representacional.

## L4 STATUS

**L4 → PRESERVED / SOURCE-INSPECTION FINDING / OUT OF SCOPE.** `App.tsx` permanece byte a byte igual. Verificar Activity pública no demuestra la corrección global del renderizado B.

## FALSIFICATION ANALYSIS

| Falsador H25 | Observación |
| --- | --- |
| Script necesita asumir autoridad operacional/factual | No observado: sólo se consultan actionId y los dos textos; guardas y hechos efectivos se conservan. |
| Declaración crea Activity antes de aceptar acción | No observado: inicio y enlist no añaden pistas; reset vuelve al inicial con Script todavía declarado. |
| Cambiar representación altera hechos, contexto, atribución, K o claim | No observado: X/Y conservan payloads, frames operacionales y evaluación completa. |
| Runtime sigue infiriendo narrativa desde sujeto/marcador/identidad | No observado: desaparecen ternarios y literales situados; se transportan textos declarados. La rama genérica conserva su conducta previa. |
| Threading requiere arquitectura general o cambia responsabilidad pública | No observado: tercer argumento opcional del constructor concreto; DemoProvider/Public Action intactos. |
| Regresión de A | No observada: snapshots completos y evaluación iguales a H24; vertical y suite completas PASS. |

No aparece falsador material ni impedimento externo. El harness registra SUPPORTED sólo después de completar los controles; ante una aserción fallida detendría la secuencia con fase y error. No se introdujo abstracción adicional para salvar el ensayo.

## H25 VERDICT

```text
H25 → SUPPORTED WITH QUALIFICATION
L5 → SCRIPT-BOUND SITUATED REPRESENTATION EXECUTION-VERIFIED (A/B scope)
SCRIPT-BOUND REPRESENTATION → SUPPORTED within tested scope
FACT / REPRESENTATION INDEPENDENCE → SUPPORTED within tested scope
H24 → FALSIFIED / unchanged
L3 → PRESERVED / OUT OF SCOPE
L4 → PRESERVED / SOURCE-INSPECTION
NEXT MATERIAL PRESSURE → OBSERVED but NOT SELECTED
```

La cualificación limita el resultado a los pasos de Evidence con `requiresEnabledSubject` y actionIds inequívocos de los Scripts A/B resueltos. La shape y la ausencia son decisiones locales experimentales. No se demuestra una relación universal para toda acción, contenido arbitrario o todas las Experiences.

## ARCHITECTURAL CONSEQUENCE

El experimento añade una relación de configuración presentacional en el paso de Script y una dependencia opcional del mock. Runtime conserva la decisión de aceptación y deja de decidir la narrativa situada de los hallazgos. No se decide dónde debería residir finalmente la materialización de Activity ni se construye infraestructura general de contenido.

Architecture v0.5 → **ACTIVE / unchanged**. ADR-001–005 → **ACCEPTED / unchanged**. No se crea ADR. La presencia de la shape en contratos TypeScript locales de Demo Factory no la promueve a contrato productivo o de Experience.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract → unchanged. PSC-P01 → OPEN / unchanged. PSC-P02 → NOT CREATED. Group → NOT INTRODUCED en esta sesión; se preservan las formas históricas fuera del recorrido.

```text
DEMO COMPOSITION ≠ RUNTIME FACT ≠ DERIVED EVALUATION ≠ READ MODEL ≠ UI LOCAL STATE
Evidence ≠ Activity
DemoScript declaration ≠ runtime occurrence
presenterLabel ≠ activityPresentation
action affordance ≠ post-action representation
representation input ≠ factual authority
Activity representation ≠ evaluation input
representation provenance ≠ semantic authority
```

La representación no reconstruye Evidence o K. La ausencia de un registro representacional no elimina el hecho ni vuelve indeterminada una evaluación que dispone de sus entradas originales. La existencia de un registro tampoco establece suficiencia.

## ARTIFACT QUARANTINE

```text
DemoScriptStep.activityPresentation
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

La cuarentena figura tanto en el comentario junto a la shape como en este informe y la traza. Las variantes X/Y, ausencia, rechazo y autoridad permanecen exclusivamente en el harness. No se registran como demos comerciales.

Revertir el experimento está acotado por el patch de cinco fuentes y los originales archivados; no requiere deshacer cambios semánticos o de gobernanza porque no se han producido. No se realiza esa reversión tras un resultado positivo.

No se convierte el campo en product contract, Experience contract, concepto TES o arquitectura general de presentación. **Recurrencia futura ≠ promoción automática.**

## WHAT H25 DOES NOT PROVE

- Arquitectura general de contenido o de Activity, localización o ubicación definitiva de su materialización.
- Procedencia de GuestPerspective, corrección global de UI o aceptación comercial completa de B.
- Recurrencia entre Experiences o representación universal para enlistment, activation u otras clases de acción.
- Política productiva de ausencia, validación editorial, textos vacíos/malformados, duplicidad de actionIds o múltiples relatos por acción.
- Autoridad productiva de la premisa H23 ni resolución de sus límites de scope/property contextual.
- Revisión retrospectiva de H24 o promoción automática de esta relación local.

## REMAINING PRESSURES

Quedan observadas la procedencia de otras superficies, la validación y ausencia productivas de representación y la responsabilidad final de materializar Activity. L3/L4 siguen abiertos y fuera de alcance. Se conservan las cualificaciones H23 sobre premisa experimental, contexto factual incompleto y referencias de evaluación.

**La siguiente presión material queda observada, pero NO SELECCIONADA. H26 no se abre automáticamente.**
