---
title: "Sesión 27 — Explicit Situated Subject Representation"
language: es
version: "v1.0"
status: "H27 supported with qualification; local experimental display relation, not promoted"
date: "2026-09-14"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 27 — Explicit Situated Subject Representation

## H26 CONSOLIDATED INPUT

**H27 → SUPPORTED WITH QUALIFICATION dentro del alcance A/B probado.** Una relación explícita en DemoScript aporta únicamente los labels de los sujetos de GuestPerspective. Los labels varían independientemente del nombre de cuenta; referencias, sesión operacional, hechos, contexto, evaluación y Activity permanecen iguales.

El [resultado consolidado de H26](session-26-situated-guest-perspective-provenance.md) permanece **FALSIFIED**. Su condición era utilizar exclusivamente relaciones existentes; la relación nueva sólo está autorizada en H27. Tampoco se revisa H24 después de H25.

```text
SESSION 20 → CLOSED
H21 → FALSIFIED / historical baseline
H22 → SUPPORTED WITH QUALIFICATION / Experience-based behavior selection
H23 → SUPPORTED WITH QUALIFICATION / situated evaluation context binding
H24 → FALSIFIED / no legitimate existing Activity representation source
H25 → SUPPORTED WITH QUALIFICATION / script-bound Activity representation
H26 → FALSIFIED / existing sources insufficient for complete GuestPerspective

L3a → legitimate account source available; GuestPerspective sessionLabel OPEN
L3b → NO LEGITIMATE EXISTING SOURCE; FIRST H26 FALSIFIER; OPEN (entrada H27)
L3c → operational/derived inputs available; situated narrative source absent; OPEN
L4 → SOURCE-INSPECTION FINDING / OPEN
L5 → SCRIPT-BOUND SITUATED REPRESENTATION EXECUTION-VERIFIED within A/B

DemoScriptStep.activityPresentation
→ EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED
```

## H27 HYPOTHESIS

**H27 — Explicit Situated Subject Representation.** Dentro de Family Adventure, una relación presentacional explícita puede asociar cada subjectRef con una representación humana situada, y ésta puede variar independientemente de la cuenta/sesión sin modificar identidad factual, operationalSessionSubjectRef, atribución de Evidence, contexto, evaluación, K o claim.

La relación `subjectRef → situated presentation` sólo determina presentación. No constituye identidad de dominio ni una relación entre cuenta y sujeto.

## VARIABLE UNDER TEST

Exclusivamente la procedencia de **`GuestPerspective.subjects[].label`** para A/B. El conjunto y orden de sujetos siguen procediendo de Scenario, los contadores de Evidence y los estados de subjectStates. No se cambian sessionLabel, message, subjects[].status, supervision ni App.

El cambio autorizado de A desde «Tú · huésped 1» a «Lucía» y desde «Huésped 2 · ya existe…» a «Huésped 2» es la variable bajo ensayo. El resto de sus snapshots y resultados se compara íntegramente con H26 para detectar regresiones.

## WHY A NEW RELATION IS NOW PERMITTED

H26 identificó la ausencia de una procedencia explícita de representación de sujetos. La instrucción de S27 autoriza una relación nueva mínima, local y reversible para estudiar ese límite. La autorización no proviene de reutilizar nombres coincidentes en member, affordance, Activity o news.

```text
co-located data ≠ declared relationship
same human name across artifacts ≠ subject identity relation
```

## SUBJECT / ACCOUNT / SESSION SEPARATION

Se mantienen tres responsabilidades diferentes:

| Plano | Fuente en el ensayo | Lo que no acredita |
| --- | --- | --- |
| Cuenta presentada | `fixture.member` → `snapshot.member`; App ya muestra «Cuenta de {name}» | Que esa cuenta sea P1/P2 o una identidad autenticada |
| Referencias operacionales/factuales | Scenario subjects, `operationalSessionSubjectRef`, subjectStates y Evidence | Nombre humano o perspectiva «Tú» |
| Representación situada de sujeto | Nueva declaración `DemoScript.subjectPresentations` | Identidad de dominio, autenticación o titularidad de cuenta |

La coincidencia intencionada Lucía/Lucía o Inés/Inés en los controles base procede de dos declaraciones separadas. No se genera el label desde member. La sesión operacional sigue siendo P1 cuando la segunda Evidence se atribuye a P2, cualquiera que sea el nombre mostrado.

## CANDIDATE HOST ANALYSIS

El análisis previo al delta se registra también en la [baseline](evidence/session-27/baseline.json). Se inspeccionaron contratos, resolver, adaptador, projector, artefactos A/B, fixtures y consumidores/harness anteriores.

| Host comparado | Evaluación | Decisión |
| --- | --- | --- |
| ScenarioDefinition | Ya declara referencias de sujetos, contexto y transiciones. Añadir displayName a subjects mezclaría la relación presentacional nueva con SubjectReference compartido. | No se modifica. No hay necesidad de alterar semántica de sujeto. |
| DemoScript | Configuración de presentación situada de la demo; ya llega al adaptador desde H25. Una lista explícita puede relacionar referencia y label sin decidir hechos o acciones. | **Seleccionado.** Campo inline local, separado de steps/affordance/Activity. |
| GuestPerspectiveReadModel | Ya dispone de `subjects[].label`; es salida de proyección. Usarlo como origen requeriría precargar o editar el read model, sin procedencia independiente. | Se conserva como consumidor, no como host de entrada. |
| Fixture | Podría alojar otra entrada presentacional separada, pero member no es el sujeto y el fixture no declara esa relación. Script resulta suficiente y ya está transportado. | No se añade una relación al fixture ni se usa member como fuente de label. |

No se infiere una prohibición universal de otros hosts. El ensayo confirma que Script puede alojar la relación con el delta local permitido; no demuestra su ubicación productiva definitiva.

## EXPERIMENTAL REPRESENTATION SHAPE

En [DemoScript](../prototype/src/demo-factory/contracts.ts), junto a sus metadatos y separada de `steps`, se añade:

```ts
// H27: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
// Display relation only; no account, authentication or subject identity claim.
subjectPresentations?: Array<{ subjectRef: string; label: string }>;
```

No se crea SubjectProfile, SubjectIdentity, Participant, Persona, AccountSubject ni equivalente nominal. No se cambia SubjectReference ni se añade displayName a Scenario. Se conserva íntegra la shape experimental de Activity H25.

## REPRESENTATION AUTHORITY

La lista sólo puede aportar el texto de un label. El projector itera **los sujetos existentes de Scenario** y localiza por `subjectRef === id` la representación correspondiente. No itera la lista presentacional para crear sujetos. El label no participa en búsqueda/filtrado de Evidence, transiciones, habilitación, sesión, contexto, premisa, K o claim.

Los labels base son nominales/descriptivos explícitos. No se deriva «Tú» desde P1, operationalSessionSubjectRef o member. Que un texto arbitrario pueda declararse no convierte su contenido en una afirmación de identidad acreditada por el runtime.

## THREADING PATH

```text
resolved DemoScript
→ copia privada de Script en MockDataAdapter (ruta H25 existente)
→ getSnapshot(): this.script?.subjectPresentations
→ projectSnapshot(..., subjectPresentations)
→ projectGuestPerspective(evaluation, subjects, subjectStates, subjectPresentations)
→ Scenario subjects.map(id)
→ lookup presentacional por subjectRef
→ GuestPerspective.subjects[].label
```

Bootstrap y constructor permanecen intactos: ya recibían Script. Los nuevos argumentos sólo transportan la lista presentacional hasta la proyección. No atraviesan EvidenceInput, Public Action, subjectStates o evaluación. No se pasa member a projectGuestPerspective.

App sigue consumiendo `subject.label` del read model. No accede directamente a subjectPresentations ni se modifica para saltarse la proyección. A diferencia de Activity posterior a una acción, el label puede verse desde el inicio porque los sujetos ya existen en Scenario: declarar presentación no crea esos sujetos.

## BASELINE

Suite previa: **88/88 PASS, 20 archivos**. Se capturan 171 archivos del estado de trabajo recibido. Los nueve archivos cuyo cambio está previsto se archivan byte a byte bajo `src/demo-factory/test-fixtures/h26/`: cinco fuentes de aplicación y cuatro harness que requieren adaptación de reproducción histórica. Los 162 restantes quedan intactos.

Los cuatro harness originales se conservan como `.test.ts.txt`, sin ejecutarlos accidentalmente una segunda vez. El harness H27 verifica tanto archivos intactos como originales archivados contra sus huellas. No se usa HEAD para atribuir a esta sesión cambios recibidos de sesiones anteriores.

Informes, baselines y trazas H21–H26 permanecen intactos. H21/H22 conservan las fuentes históricas que ya utilizaban. Las reproducciones H23/H24 mantienen sus adaptadores/composiciones previos y reciben la proyección anterior a H27. H25/H26 ejecutan sus artefactos, adaptador y proyección anteriores a H27 con las mismas expectativas. H26 sigue reproduciendo su falsación.

## CODE DELTA

El [patch de aplicación contra H26](evidence/session-27/application-delta.patch) contiene cinco fuentes:

| Archivo | Delta |
| --- | --- |
| [contracts.ts](../prototype/src/demo-factory/contracts.ts) | Campo opcional inline en DemoScript con cuarentena explícita. Ninguna modificación de SubjectReference, EvidenceInput, Public Action, Scenario o read model. |
| [artifacts.ts](../prototype/src/demo-factory/artifacts.ts) | Declaraciones A: P1 → Lucía, P2 → Huésped 2. Todo el Script restante y Scenario se conservan. |
| [costa-artifacts.ts](../prototype/src/demo-factory/costa-artifacts.ts) | Declaraciones B: P1 → Inés, P2 → Mateo, independientes de member. |
| [mock-adapter.ts](../prototype/src/demo/mock-adapter.ts) | Transporte desde Script en getSnapshot y argumento adicional en projectSnapshot hacia el projector guest. executeAction y reset intactos. |
| [vertical-evaluation.ts](../prototype/src/demo-factory/vertical-evaluation.ts) | Importación sólo de tipo, argumento presentacional opcional en el projector y sustitución de la expresión de label. Evaluación y SupervisionPerspective intactas. |

La expresión nueva es `subjectPresentations.find(({ subjectRef }) => subjectRef === id)?.label ?? ""`. No consulta member, sesión, marcador o identidad de Scenario para escoger el texto. Los ternarios de status y las frases de sessionLabel/message permanecen exactamente como estaban, dentro de sus presiones abiertas.

La instrumentación añade el [harness H27](../prototype/src/demo-factory/explicit-subject-representation-h27.test.ts) y un helper exclusivo de tests para dirigir lecturas de fuentes a los archivos históricos. Dos reexports de evaluadores compartidos y dos copias de logos resuelven imports de los originales archivados sin alterar sus bytes. No entran en el bundle de aplicación ni constituyen nueva arquitectura de producto.

## A CONTROL

En initial, enlisted, A@P1, P2 enabled, A@P1+B@P2 y reset, GuestPerspective muestra:

```text
subject-p1 → Lucía
subject-p2 → Huésped 2
```

Se declaran literalmente en Script, sin derivación desde member. Las referencias siguen siendo P1/P2, Evidence sigue `evidence-a-p1 → subject-p1 → marker-a` y `evidence-b-p2 → subject-p2 → marker-b`. Sesión P1 y contexto Aurora/AS-8842/stay-AS-8842 permanecen iguales.

Al excluir exclusivamente `subjects[].label` de la comparación, todos los frames son iguales a H26, incluidos Activity, sessionLabel, message, status, state, contadores, supervisión y evaluación completa. La regresión de la vertical Sesión 20 mantiene los tests UI existentes; no se reescribe su aceptación histórica ni se exige conservar los labels que esta sesión autoriza sustituir.

## B CONTROL

Las mismas seis fases exponen:

```text
subject-p1 → Inés
subject-p2 → Mateo
```

Ya no se usan «Tú · huésped 1» ni «Huésped 2 · ya existe…» como labels derivados por ID. La colección conserva exactamente los dos sujetos de Scenario. Evidence sigue `evidence-costa-a-p1 → subject-p1 → marker-a` y `evidence-costa-b-p2 → subject-p2 → marker-b`, con Costa/CC-205/stay-CC-205 y sesión P1.

Todas las diferencias frente a H26 se limitan a los dos labels. Los campos congelados pueden seguir diciendo Lucía/jardín/fuente o «por ti»; esos síntomas se registran aparte y no falsifican H27. Activity permanece mirador/patio, con sus descripciones H25.

## ACCOUNT / SUBJECT DECOUPLING CONTROL

Variante exclusivamente de harness sobre B: se cambia sólo el label declarado de P1 a **«Participante Alfa»**. Scenario, member, todos los pasos, actions y ActivityPresentation permanecen iguales.

Se observa simultáneamente, en todas las fases:

```text
snapshot.member.name → Inés
GuestPerspective subject-p1 label → Participante Alfa
GuestPerspective subject-p2 label → Mateo
operationalSessionSubjectRef → subject-p1
```

La atribución A@P1/B@P2, payloads completos, contextos, estados y evaluación son idénticos al control B. «Participante Alfa» es sólo un string adversarial solicitado, no la introducción de un concepto Participant.

Se observa la presentación de cuenta mediante su campo público; App ya lo consume como «Cuenta de …». No se afirma una sesión autenticada ni se renderiza B. Activity y otras frases pueden conservar nombres previos: la variante prueba independencia de responsabilidades, no una composición comercial terminada.

## INVERSE DECOUPLING CONTROL

Otra variante B cambia exclusivamente `fixture.member.name` a **«Cuenta Demo»**. Script, sus labels Inés/Mateo y Scenario permanecen iguales. El resto del fixture no se altera.

```text
account presentation → Cuenta Demo
subject-p1 label → Inés
subject-p2 label → Mateo
```

El harness compara los frames completos con B neutralizando sólo ese campo de nombre de cuenta: todo lo demás es idéntico, incluidos los labels de sujetos, Activity, sessionLabel todavía congelado y la evaluación. No se infiere el label de member.name ni se añade mapping para mantenerlo.

## REPRESENTATION INDEPENDENCE CONTROL

En A y B se crean variantes X/Y que cambian únicamente `subjectPresentations[].label`. Se conservan las referencias de la lista, Scenario, member, operationalSessionSubjectRef, actions y payloads, contextos, evaluación y Activity. Se ejecuta la misma secuencia completa.

```text
facts X == facts Y
operational state/session X == Y
evaluation/premise/K/full claim X == Y
Activity X == Activity Y
subject labels X != subject labels Y
```

La diferencia de labels aparece desde el inicial y se mantiene después de las acciones y reset. Los snapshots provienen del provider vivo; no se editan para fabricar el resultado. Las vistas sin labels o con el nombre de cuenta neutralizado son sólo herramientas de comparación posteriores a la ejecución.

Un control adicional declara **«Nombre compartido» para P1 y P2**. Ambos labels son iguales, pero siguen existiendo dos referencias distintas y Evidence permanece atribuida separadamente a P1/P2. No se fusionan sujetos ni se filtran hechos por nombre: display-name equality no implica identity equality.

## ABSENCE / MISMATCH OBSERVATION

Se prueba en A y B:

| Variante | Resultado |
| --- | --- |
| Campo subjectPresentations ausente | Los dos sujetos de Scenario permanecen, con label vacío; hechos, estado, sesión, contexto, evaluación y Activity iguales al control. |
| Presentación de P1 apunta a `subject-not-in-scenario` | No se crea ese sujeto. P1 sigue existiendo con label vacío y P2 conserva su label válido. No cambia Evidence ni atribución. |

La ausencia se expresa usando el string vacío ya permitido por `GuestPerspective.subjects[].label`. No se cambia la forma del read model, no se elimina el sujeto ni se inventa un nombre genérico, una identidad, «Tú» o un mapping de cuenta. El argumento ausente se normaliza a lista vacía antes del lookup.

Esto es **observación local experimental de ausencia**, no política productiva general ni aceptación de UX con encabezados vacíos. No necesita un contrato adicional para preservar con seguridad los hechos en este ensayo, por lo que no se activa el STOP condicionado a esa necesidad. No se diseña validación editorial, diagnóstico de datos incompletos, tratamiento de referencias duplicadas o fallback universal.

## EXECUTION TRACE

La [traza principal](evidence/session-27/execution-trace.json) fue capturada el **2026-09-14T17:23:07.675Z**, 18:23:07 Europe/Lisbon. Registra huellas de baseline, cinco fuentes de aplicación y harness ejecutado.

| Ruta de traza | Evidencia |
| --- | --- |
| `controls[0/1].original` | A/B, Scenario y Script declarados, cinco frames inicial/acciones, reset y seis tuplas efectivas del projector |
| `controls[0/1].variants[0/1]` | X/Y con variación exclusiva de labels |
| `controls[0/1].absence` | Ausencia completa de lista; sujetos/hechos preservados |
| `controls[0/1].unknown` | Referencia presentacional inexistente, sin creación de sujeto ni cambio factual |
| `accountSubjectDecoupling` | Cuenta Inés y label P1 Participante Alfa |
| `inverseDecoupling` | Cuenta Demo y label P1 Inés |
| `equalLabelControl` | Labels iguales, identidades/atribución distintas |
| `genericRegression` | Retail y Arrival sobre provider vivo, snapshots H25 íntegramente conservados |

Son 13 secuencias completas Family Adventure con reset: cinco por composición y tres controles adicionales B, más Retail/Arrival. Los spies invocan projector/evaluadores originales y capturan argumentos/resultados completos. Las tuplas de evaluación incluyen Evidence convertida, contexto, criterio y premisa; los resultados incluyen claim completa. No se usa sólo el resumen público de supervisión para afirmar conservación factual.

En el recorrido base la secuencia de K sigue siendo `not-attempted → not-attempted → not-established → not-established → established`; los labels no participan en esa determinación. La sesión sigue siendo P1, aun cuando la última Evidence pertenece a P2.

Las ejecuciones normales no escriben trazas. `H27_RECORD_PATH` exige un destino nuevo con escritura exclusiva; la suite posterior no sobrescribe la evidencia histórica ni la captura principal.

| Verificación | Resultado |
| --- | --- |
| Suite previa | 88/88 PASS, 20 archivos |
| H27 focalizado y captura principal | 1/1 PASS, todos los controles descritos |
| H26 histórico + H25 + H24 histórico + H23 + H22 + H21 histórico + vertical Sesión 20 | 16/16 PASS, 7 archivos |
| Full suite final | 89/89 PASS, 21 archivos |
| Typecheck | PASS |
| Lint | PASS |
| Build TypeScript + Vite + PWA | PASS |

Durante la preparación se corrigieron el tipado de la colección de controles del nuevo harness y su expectativa de argumento ausente (`undefined` frente a la lista vacía normalizada). No se cambió el runtime para superar esas correcciones de instrumentación. La captura principal corresponde al harness final, con verificación completa satisfactoria.

Desde `products/convercus-app/prototype/`:

```sh
npm test -- src/demo-factory/explicit-subject-representation-h27.test.ts
npm test -- src/demo-factory/situated-guest-provenance-h26.test.ts src/demo-factory/script-bound-activity-h25.test.ts src/demo-factory/situated-activity-provenance-h24.test.ts src/demo-factory/situated-evaluation-context-h23.test.ts src/demo-factory/experience-stable-selection-h22.test.ts src/demo-factory/composition-boundary-h21.test.ts src/demo-factory/family-adventure-vertical.test.ts
npm run check
```

No se necesita navegador para los labels: están en el snapshot público consumido por App. No se renderiza B ni se afirma corrección global de su UI.

## L3b RESULT

**L3b → EXPLICIT SCRIPT-BOUND SUBJECT LABELS EXECUTION-VERIFIED within A/B.** La fuente explícita sustituye la bifurcación P1/resto para el label. Cuenta y presentación de sujeto varían en ambos sentidos sin alterar hechos o evaluación.

El hallazgo histórico de ausencia de relación en H26 permanece válido. H27 aborda experimentalmente esta subpresión, no toda GuestPerspective ni un modelo general de sujetos.

## L3a STATUS

**L3a → PRESERVED / OPEN.** sessionLabel conserva la frase «Usas la cuenta de Lucía, huésped 1…», también en B y en variantes. No se sustituye por member.name ni por los labels nuevos: la frase mezcla cuenta, sujeto, segunda persona y narrativa de capacidad. La fuente legítima de presentación de cuenta aislada permanece disponible en member.

## L3c STATUS

**L3c → PRESERVED / OPEN.** message conserva jardín/fuente y segunda persona en B; subjects[].status conserva género y «Habilitado por ti». No se reutilizan subjectPresentations, presenterLabel o activityPresentation para corregir esos textos.

## L4 STATUS

**L4 → PRESERVED / SOURCE-INSPECTION FINDING / OUT OF SCOPE.** App.tsx permanece byte a byte igual. Sus literales de marca/lugares y labels de supervisión continúan bajo la presión L4. No se añade acceso directo a Script para evadir GuestPerspective.

## L5 STATUS

**L5 → PRESERVED / EXPERIMENTALLY ADDRESSED within A/B.** A Activity mantiene jardín/fuente; B Activity mantiene mirador/patio. Sus snapshots completos son iguales a H26 en todas las variantes de presentación de sujeto, incluida separación inversa de cuenta.

La regresión H25 conserva sus controles originales de representación de Activity, ausencia y rechazo sobre su baseline archivada; H27 verifica por separado la conservación de Activity en el provider vivo. executeAction permanece idéntico. `activityPresentation` no se modifica, generaliza ni promueve.

## FALSIFICATION ANALYSIS

| Falsador H27 | Observación |
| --- | --- |
| Label no puede variar independientemente de cuenta | No observado: Participante Alfa/Inés y Cuenta Demo/Inés prueban ambos sentidos; X/Y conservan member. |
| Representación cambia subjectRef, atribución, sesión, contexto o evaluación | No observado: comparación completa contra H26 y entre variantes; labels iguales no fusionan hechos. |
| Se requiere mapping member→subject | No: member no se consume en la resolución del label. |
| Debe modificarse SubjectReference | No: permanece idéntico, junto con Scenario y las formas factuales/públicas. |
| Se necesita Actor/Participant/Representative u otro modelo | No: lista inline de dos strings por entrada, sólo representacional. |
| App debe cambiar para transportar la relación | No: ya consume el label del read model. |
| Regresión A | No observada fuera del cambio de labels expresamente autorizado; todo lo restante coincide con H26 y la vertical pasa. |

No aparece falsador material ni impedimento externo. El harness registra SUPPORTED sólo al terminar los controles; una contradicción material detendría la secuencia con fase y error. No se introduce una relación perspectival para solucionar síntomas fuera del alcance.

## H27 VERDICT

```text
H27 → SUPPORTED WITH QUALIFICATION
L3b SUBJECT DISPLAY → EXPLICIT SCRIPT-BOUND SUBJECT LABELS EXECUTION-VERIFIED within A/B
ACCOUNT / SUBJECT PRESENTATION SEPARATION → SUPPORTED within tested scope
H26 → FALSIFIED / unchanged
L3a → PRESERVED / OPEN
L3c → PRESERVED / OPEN
L4 → PRESERVED / SOURCE-INSPECTION
L5 → PRESERVED / EXPERIMENTALLY ADDRESSED within A/B
NEXT MATERIAL PRESSURE → OBSERVED but NOT SELECTED
```

La cualificación cubre la relación inline local en Script, las composiciones controladas con referencias inequívocas y la ausencia expresada como label vacío dentro del ensayo. No se demuestra identidad de sujeto, relación cuenta/sujeto, perspectiva del viewer, autenticación ni arquitectura general de presentación.

## ARCHITECTURAL CONSEQUENCE

La composición puede declarar explícitamente una presentación de sujetos sin mezclarla con sus referencias operacionales/factuales. La ruta H25 de Script al adaptador permite un transporte adicional hasta el projector. Sólo el read model usa el label; las funciones de evaluación no reciben esa lista.

Architecture v0.5 → ACTIVE / unchanged. ADR-001–005 → ACCEPTED / unchanged. No se crea ADR ni un modelo productivo de sujetos/participantes. La importación TypeScript de DemoScript en el archivo del projector es dependencia local de tipo, no ampliación semántica de evaluación.

## SEMANTIC CONSEQUENCE

TES y Product Semantic Contract → unchanged. PSC-P01 → OPEN / unchanged. PSC-P02 → NOT CREATED. Group → NOT INTRODUCED en esta sesión; formas históricas ajenas al recorrido se conservan.

```text
subject presentation ≠ subject identity
account presentation ≠ subject presentation
account/member ≠ Experience subject
operationalSessionSubjectRef ≠ authentication identity
represented subject ≠ authenticated user
same display name ≠ same identity
co-located data ≠ declared relationship
display relation ≠ factual authority
GuestPerspective ≠ Activity history
subjectPresentations ≠ journey narrative
```

No se añaden accountSubjectRef, viewerSubjectRef, actorRef, operatorRef, representativeRef ni un mapping memberId→subjectRef. Los labels no reconstruyen identidad, Evidence o K.

## ARTIFACT QUARANTINE

```text
DemoScript.subjectPresentations
→ EXPERIMENTAL
→ LOCAL
→ REVERSIBLE
→ NOT PROMOTED
```

La cuarentena figura junto al campo, en la traza y en este informe. Las variantes de separación, nombres iguales y ausencia/mismatch son exclusivamente de harness; no se registran como demos comerciales. Los originales archivados y el patch delimitan una reversión técnica local; no se realiza tras el resultado positivo.

La relación no se convierte en Experience contract, Subject contract, Product Semantic Contract, concepto TES ni modelo general de identidad. La relación Activity H25 conserva su cuarentena independiente. **Recurrencia futura no implica promoción.**

## WHAT H27 DOES NOT PROVE

- Modelo de identidad de sujetos, relación cuenta→sujeto, perspectiva viewer/session→subject o autenticación.
- Modelo general de participante o autoridad representativa de una cuenta sobre otro sujeto.
- Procedencia de journey narrative, sessionLabel, género o segunda persona.
- Arquitectura general de presentación, localización o validación editorial.
- Política productiva de ausencia, duplicidad de referencias de presentación, contenido inválido o UX con label vacío.
- Corrección global de App/B o promoción de la relación a otras Experiences.
- Revisión retrospectiva de H26 ni resolución completa de L3.

## REMAINING PRESSURES

Se observan la composición de sessionLabel, la procedencia de narrativa presente y la justificación de segunda persona/género/perspectiva en los campos todavía congelados. L4 permanece abierto; L5 y L3b mantienen sólo sus alcances experimentales. La ausencia productiva y referencias ambiguas de presentación no se resuelven aquí.

**La siguiente presión material queda observada, pero NO SELECCIONADA. H28 no se abre automáticamente.**
