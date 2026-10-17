---
title: "Sesión 28 — Account-Sourced Guest Presentation"
language: es
version: "v1.0"
status: "H28 supported with qualification; account-only display within A/B"
date: "2026-09-16"
project: "Convercus Demo Factory / Convercus Experience Products"
document_type: "informe de ejecución experimental"
semantic_authority: "subordinado a TES, Architecture v0.5 y ADR-001–005"
---

# Sesión 28 — Account-Sourced Guest Presentation

## H27 CONSOLIDATED INPUT

**H28 → SUPPORTED WITH QUALIFICATION dentro de Family Adventure A/B.** La fuente existente `fixture.member.name` proporciona una presentación exclusivamente de cuenta en `GuestPerspective.sessionLabel`. Los controles ejecutados permiten variar esa presentación y la representación de sujetos independientemente, manteniendo hechos, evaluación y Activity.

La [Sesión 27](session-27-explicit-situated-subject-representation.md) queda **CLOSED**, con **H27 → SUPPORTED WITH QUALIFICATION**. Sus labels explícitos, ligados a Script, permanecen verificados dentro de A/B. `DemoScript.subjectPresentations` continúa **EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED**.

**H26 → FALSIFIED**, con baseline histórica intacta. El resultado de H28 no revisa retrospectivamente H26 ni autoriza resolver toda GuestPerspective. Al entrar en esta sesión, L3a y L3c permanecían abiertos; L4 era un hallazgo por inspección de fuente y L5 estaba abordado experimentalmente por H25.

## H28 HYPOTHESIS

La fuente de cuenta existente puede proporcionar una presentación situada exclusivamente de cuenta para `sessionLabel`, independiente de `subjectPresentations`, sin introducir relaciones account→subject, viewer→subject o session→subject, ni modificar referencias, sesión operacional, atribución de Evidence, subjectStates, Activity, contexto, evaluación, K o claim.

Se ensaya `account source → account-only presentation`. La independencia se contrasta en ambos sentidos mediante cambios controlados de entrada y comparación de snapshots completos, llamadas y resultados de evaluación.

## VARIABLE UNDER TEST

Exclusivamente **`GuestPerspective.sessionLabel`**. El resultado literal es `Cuenta de ${accountName}`. El nombre procede de la cuenta; el prefijo no afirma identidad de viewer, posición P1/P2, acción, capacidad ni relación con otro sujeto.

No cambian `subjects[].label`, `subjects[].status`, `message`, `supervision`, Activity ni App. En los controles de perturbación se modifican copias de entradas en memoria, sin editar los artefactos A/B persistidos. Los labels siguen teniendo como única fuente `DemoScript.subjectPresentations`.

## EXISTING ACCOUNT SOURCE

`DemoFixture.member.name` ya existe. `MockDataAdapter` conserva una copia del fixture y `projectSnapshot` copia `fixture.member` a `snapshot.member`. App ya utiliza `snapshot.member.name` para presentar la cuenta y consume `guestPerspective.sessionLabel` como texto.

H28 no crea otro nombre de cuenta, no reinterpreta `member.id` y no obtiene autoridad desde una coincidencia con un label de sujeto. En las variantes de nombre tampoco se sincronizan artificialmente otros campos de member: la comparación completa verifica que permanecen intactos.

## ACCOUNT / SUBJECT / SESSION SEPARATION

| Plano | Fuente preservada | Alcance |
| --- | --- | --- |
| Presentación de cuenta | `fixture.member.name` | Nombre presentado en `sessionLabel` y copia existente en `snapshot.member`. |
| Presentación de sujetos | `DemoScript.subjectPresentations` | Labels H27, asociados explícitamente por `subjectRef`. |
| Sujetos y estado operacional | Scenario subjects, subjectStates, `operationalSessionSubjectRef` | Referencias y estados; ninguna identidad de autenticación. |
| Evidence y suficiencia | Acciones admitidas, Evidence, contexto y evaluadores existentes | Atribución factual, K y claim; independientes del nombre presentado. |

Se preserva: account/member ≠ Experience subject; subject presentation ≠ subject identity; operationalSessionSubjectRef ≠ authentication identity; represented subject ≠ authenticated user. No aparece un mapping member→subject, viewer→subject, account→subject o session→subject. La sesión operacional sigue apuntando a P1 mientras la segunda Evidence pertenece a P2.

## SOURCE AND HOST ANALYSIS

La inspección y decisión se registraron **antes del delta** en la [baseline](evidence/session-28/baseline.json). Se revisaron fixture/member, copia de snapshot, adaptador, firma y cuerpo de `projectGuestPerspective`, declaraciones A/B y consumidores App.

| Host o transporte comparado | Observación y decisión |
| --- | --- |
| `projectSnapshot` | Ya reúne fixture y proyecciones. Extrae únicamente `fixture.member.name` y lo transporta; no añade interpretación de identidad. |
| `projectGuestPerspective` | Ya construye `sessionLabel`. Se conserva allí la transformación textual, recibiendo un escalar explícito. |
| Member completo | Innecesario: expondría ID y otros atributos ajenos a esta variable. No se transporta al projector. |
| `snapshot.member` frente a fixture | La copia de member procede del mismo fixture sin transformación semántica. Usar el escalar del fixture evita depender de la salida parcialmente construida. |
| Script / subjectPresentations | Fuente de labels de sujeto, sin autoridad para presentar la cuenta. No participa en la expresión de `sessionLabel`. |
| Scenario / Evidence / referencia de sesión | Aportan información operacional/factual; no fundamentan la presentación de cuenta. No se consultan para construir el texto. |
| App | Consumidor existente del read model. No necesita modificación y permanece congelado. |

El projector recibe otros argumentos por sus responsabilidades preexistentes, pero la expresión de `sessionLabel` depende solamente del nuevo escalar. La comparación exacta de código y los controles independientes distinguen coexistencia de argumentos de dependencia presentacional.

## THREADING PATH

```text
existing fixture.member.name
  → MockDataAdapter fixture copy
  → projectSnapshot(...)
  → projectGuestPerspective(..., fixture.member.name)
  → sessionLabel = `Cuenta de ${accountName}`
  → existing App consumer

existing fixture.member
  → snapshot.member (existing copy, unchanged)

DemoScript.subjectPresentations
  → subjects[].label (H27, unchanged)
```

El quinto argumento es un string; no hay objeto nuevo ni contrato compartido nuevo. La firma conserva `accountName = ""` para compatibilidad con llamadas históricas de menor aridad. El adaptador vivo siempre proporciona `fixture.member.name`. Ese valor por defecto no establece una política para cuentas ausentes: H28 prueba nombres presentes y no valida la presentación de entradas incompletas.

## BASELINE

Baseline capturada el **2026-09-16T17:06:47.901822+00:00**, con SHA-256 de **191 archivos existentes**. Antes del cambio: **89/89 pruebas, 21 archivos**. Se preserva el estado de trabajo recibido, incluidas modificaciones de sesiones anteriores; no se sustituye por una revisión Git.

De esos 191 archivos, **188 permanecen byte a byte iguales**. Las tres excepciones delimitadas son el adaptador, el módulo de evaluación/proyección y el harness H27. Sus versiones previas se archivan con los hashes originales en `test-fixtures/h27`; las rutas están registradas en la baseline.

La instrumentación H27 se conecta a esas fuentes históricas y adapta sus lecturas de hashes. No se cambian sus aserciones ni sus resultados grabados. H21–H26 mantienen sus fuentes/harness históricos. Los bridges de H27 reexportan módulos compartidos que permanecen sin cambios; los helpers sólo existen bajo test-fixtures.

## CODE DELTA

El [delta de aplicación](evidence/session-28/application-delta.patch) contiene únicamente dos archivos:

1. `src/demo/mock-adapter.ts`: añade `fixture.member.name` a la llamada existente del projector.
2. `src/demo-factory/vertical-evaluation.ts`: recibe el escalar y sustituye la frase fija mixta por `Cuenta de ${accountName}`.

El [harness H28](../prototype/src/demo-factory/account-sourced-guest-h28.test.ts) comprueba que los archivos nuevos equivalen exactamente a los originales con esas sustituciones. Esto preserva byte a byte el evaluador y la construcción de los demás campos. La adaptación del harness H27 y sus archivos de soporte son instrumentación histórica, no comportamiento de producto.

No cambian contratos, fixtures, Scripts persistidos, Scenario, App, resolver ni evaluadores compartidos. No se introduce ninguna abstracción Actor, Operator, Participant, Representative, AccountSubject, ViewerSubject, AuthenticatedSubject ni equivalente.

## A CONTROL

En `hospitality-family-adventure`, `member.name = Lucía` produce **`Cuenta de Lucía`**. Los labels siguen siendo **Lucía / Huésped 2**, desde Script. El resto de cada frame coincide con la traza H27 y el reset devuelve el estado inicial completo.

La igualdad Lucía/Lucía no acredita relación: son entradas independientes, como comprueban las variantes siguientes. La cuenta se presenta ya antes de cualquier Evidence, sin crear hechos.

## B CONTROL

En `hospitality-family-adventure-costa`, `member.name = Inés` produce **`Cuenta de Inés`**, con labels **Inés / Mateo**. También aquí coinciden con H27 todos los campos fuera de `sessionLabel`, junto con los inputs y resultados de evaluación.

Activity mantiene sus representaciones H25 de mirador/patio. La narrativa de GuestPerspective todavía contiene jardín/fuente: sigue siendo evidencia de L3c abierto y no se oculta corrigiendo el nombre de cuenta.

## ACCOUNT DECOUPLING CONTROL

Sobre B se cambia únicamente `member.name` a **Cuenta Demo**. Resultado simultáneo:

| Campo | Observado |
| --- | --- |
| sessionLabel | `Cuenta de Cuenta Demo` |
| P1 label | `Inés` |
| P2 label | `Mateo` |
| Sesión operacional | `subject-p1` |
| Evidence A / B | Atribuciones P1 / P2 preservadas. |
| Resto del frame | Idéntico al B base, descontando exclusivamente member.name y sessionLabel. |

La repetición «Cuenta de Cuenta Demo» es el resultado literal de la forma ensayada; no se añade una regla léxica para ese caso. No se crea mapping para explicar la diferencia de nombres. Activity, estados, contexto, evaluación, K y claim permanecen iguales.

## INVERSE DECOUPLING CONTROL

Con member.name **Inés**, se cambia únicamente el label de P1 a **Participante Alfa** en una copia de Script. Se observa `Cuenta de Inés`, P1 `Participante Alfa`, P2 `Mateo`.

La comparación completa de frames, exceptuando los campos de label autorizados, pasa. La rutina verifica además los dos labels exactos, por lo que P2 no puede cambiar inadvertidamente. La cuenta no se reconstruye desde P1.

## REPRESENTATION INDEPENDENCE CONTROL

Se ejecutan ambos ejes X/Y en **cada composición A y B**, conservando Scenario, acciones, referencias, contexto y la parte de Script que no se perturba.

| Perturbación | Presentación de cuenta | Labels de sujetos | Hechos, evaluación y Activity |
| --- | --- | --- | --- |
| Labels `Sujeto X primero/segundo` → `Sujeto Y primero/segundo`; member fijo | Iguales | Diferentes | Iguales |
| Nombre `Cuenta X` → `Cuenta Y`; subjectPresentations fijo | `Cuenta de Cuenta X` → `Cuenta de Cuenta Y` | Iguales | Iguales |

Las comparaciones usan copias de snapshots sólo para excluir los campos que deben variar; no alteran el provider, sus salidas ni los resultados de los evaluadores. Se comparan los frames enteros, no únicamente un resumen de K. En todos los casos el reset coincide exactamente con el estado inicial de su variante.

## EXECUTION TRACE

La [traza principal](evidence/session-28/execution-trace.json), grabada el **2026-09-16T17:12:50.496Z**, incluye hashes de baseline, aplicación y harness, argumentos del projector, snapshots, llamadas y resultados de ambos evaluadores. Se creó con escritura exclusiva, tras pasar el ensayo previo y la verificación completa.

Se ejecutaron **12 secuencias Family Adventure**: base, dos variantes de sujeto y dos de cuenta por composición, más los controles principal e inverso de B. Cada una registra cinco frames y un snapshot de reset: **72 observaciones de snapshot**. Se capturan los seis juegos de argumentos del projector por secuencia; el quinto argumento coincide siempre con el nombre de cuenta declarado.

| Fase | K / sufficiency | Claim |
| --- | --- | --- |
| initial | not-attempted | not-produced |
| enlist-p1 | not-attempted | not-produced |
| discover-clue-a | not-established | not-established |
| activate-p2 | not-established | not-established |
| discover-clue-b | established | established |
| reset | not-attempted | not-produced |

Las acciones con Evidence llaman una vez al evaluador vertical y al evaluador conjunto; habilitar un sujeto no los invoca. La traza preserva los argumentos factuales, premisas y resultados de H27. Los cuatro argumentos anteriores del projector coinciden con H27 en los controles base.

`retail-baseline` y `hospitality-stay` se ejecutan también mediante el provider vivo: sus frames y reset coinciden íntegramente con H27. No se modifica la rama genérica de Activity.

| Comprobación | Resultado |
| --- | --- |
| Regresión dirigida H21–H27 y vertical S20 | 17/17 pruebas; 8 archivos. |
| Ensayo focal H28 previo | 1/1 PASS. |
| `npm run check` | Typecheck, lint, 90/90 pruebas en 22 archivos y build PASS. |
| Captura principal H28 | 1/1 PASS; traza exclusiva creada. |
| Auditoría final | [verification.json](evidence/session-28/verification.json): hashes, alcance del delta y secciones requeridas. |

Comando reproducible del ensayo: `npm test -- src/demo-factory/account-sourced-guest-h28.test.ts`. Para una captura nueva se puede asignar `H28_RECORD_PATH` a una ruta inexistente; no se sobrescribe la evidencia consolidada. No se ejecutó navegador ni se declara validación visual.

## L3a RESULT

**ACCOUNT-SOURCED ACCOUNT-ONLY SESSION LABEL → EXECUTION-VERIFIED within A/B.** La única autoridad de entrada añadida es el nombre existente de cuenta. Las salidas ensayadas no contienen segunda persona, referencia de sujeto ni afirmación de capacidad. La expresión de formato no añade esas afirmaciones.

El ensayo no sanitiza valores arbitrarios de member.name; prueba los nombres explícitos de estos controles. Tampoco convierte la etiqueta histórica del campo `sessionLabel` en identidad autenticada ni amplía su contrato.

## L3b STATUS

**PRESERVED / EXPERIMENTALLY ADDRESSED H27.** Labels explícitos desde Script, sin fallback a member ni a la referencia de sesión. La derivación H27 permanece intacta; variar la cuenta no afecta a los labels y variar los labels no afecta a la cuenta.

## L3c STATUS

**PRESERVED / OPEN.** Continúan los textos de estado y recorrido, lugares, género y segunda persona fuera de la variable estudiada. El harness comprueba expresamente jardín, fuente y `Habilitado por ti`, incluso en B. El cuerpo de construcción de message/status permanece byte a byte igual. No se selecciona ni resuelve su procedencia narrativa.

## L4 STATUS

**PRESERVED / SOURCE-INSPECTION FINDING / OPEN.** App conserva sus textos y consumidores. Su integridad se verifica por hash; no se afirma que la composición B esté completamente situada en la interfaz ni que haya pasado una inspección visual.

## L5 STATUS

**PRESERVED / EXPERIMENTALLY ADDRESSED H25.** Activity conserva contenido y orden completos frente a H27, incluyendo títulos/descripciones de jardín/fuente en A y mirador/patio en B. Los cambios de cuenta y de representación de sujetos no la alteran. `activityPresentation` sigue en cuarentena.

## FALSIFICATION ANALYSIS

| Falsificador propuesto | Evidencia y resultado |
| --- | --- |
| Necesitar mapping member→subject o identidad viewer/session | No aparece relación nueva; basta el escalar name. No observado. |
| Necesitar subjectPresentations, sesión, Evidence o rol para construir la cuenta | La expresión usa sólo accountName; perturbaciones independientes pasan. No observado. |
| Cambiar cuenta altera labels, referencias, Evidence, Activity, contexto, evaluación, K o claim | Comparación íntegra de cada frame, excluyendo sólo nombre de cuenta y sessionLabel. No observado. |
| Cambiar subjectPresentations altera sessionLabel | Controles X/Y A/B e inverso B conservan la cuenta. No observado. |
| Ampliar semántica de SubjectReference/member/referencia de sesión | Contratos y fuentes preservados por hash; no hay cambio semántico necesario. No observado. |
| Necesitar nueva abstracción o promoción de H25/H27 | Dos cambios locales de aplicación, sin modelo/registro/engine nuevo. No observado. |
| Conservar segunda persona en la variable estudiada | Valores exactos de cuenta comprobados en las 12 secuencias. No observado dentro de las entradas ensayadas. |

Ningún falsificador seleccionado se activa. El resultado se restringe a las ejecuciones y fuentes inspeccionadas; no demuestra una independencia universal para cualquier futuro cambio o fixture.

## H28 VERDICT

**SUPPORTED WITH QUALIFICATION.** La fuente existente basta para account-only presentation dentro de A/B, con separación cuenta/sujeto verificada por ejecución en ambos sentidos.

La calificación es material: datos presentes de demo, provider mock, proyección local y sin autenticación real. L3c y L4 permanecen abiertos, y H25/H27 mantienen su carácter experimental. H28 no rehabilita H26 ni completa GuestPerspective.

## ARCHITECTURAL CONSEQUENCE

Se demuestra que esta variable admite un transporte mínimo hacia el projector existente. No hace falta pasar member completo ni introducir un host de presentación compartido.

**Architecture v0.5 → ACTIVE**, **ADR-001–005 → ACCEPTED**, sin cambios. No se crea PresentationModel, PresentationRegistry, ContentRegistry, PerspectiveEngine ni equivalente. El delta local y sus fuentes previas permiten revisar o revertir el experimento sin adoptar un modelo universal.

## SEMANTIC CONSEQUENCE

Presentar un nombre de cuenta no declara quién es el sujeto representado ni quién opera autenticado. La coincidencia o divergencia entre nombres de cuenta y labels no modifica referencias ni atribuciones.

**TES y Product Semantic Contract permanecen sin cambios. PSC-P01 → OPEN / EVIDENCE-BACKED PRESSURE, sin cambios. PSC-P02 → NOT CREATED.** No se promueven nuevas relaciones a semántica de producto.

## ARTIFACT QUARANTINE

| Artefacto | Estado |
| --- | --- |
| `DemoScriptStep.activityPresentation` | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. |
| `DemoScript.subjectPresentations` | EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. |
| Transporte y formato H28 | Experimento local del prototype; sin promoción de contrato o arquitectura. |
| Fuentes archivadas y helpers H27 | Instrumentación histórica; no autoridad de runtime productivo. |

La evidencia de H28 no convierte DemoScript en modelo universal de presentación. Sus fuentes H25/H27 mantienen sus responsabilidades previas y no intervienen en la autoridad de cuenta.

## WHAT H28 DOES NOT PROVE

- No demuestra member→subject, viewer→subject, account→subject ni session→subject.
- No demuestra autenticación, identidad de dominio, representación legal ni autorización de capabilities.
- No resuelve message/status, lugares, género o segunda persona fuera de sessionLabel.
- No valida visualmente App ni completa la composición B.
- No establece políticas para cuenta ausente, nombres vacíos, entradas arbitrarias, localización o cambios de cuenta durante una sesión viva; las variantes usan instancias independientes.
- No promueve los artefactos H25/H27 ni identifica un modelo universal de presentación.

## REMAINING PRESSURES

L3c conserva la presión observada de procedencia narrativa situada para estados y recorrido. L4 conserva los hallazgos por inspección de fuente en App. La eventual relación entre viewer/cuenta/sesión y sujeto representado permanece ausente; H28 no la necesita ni la infiere.

Estas presiones quedan observadas y **NOT SELECTED**. No se abre H29 automáticamente.

| Dimensión | Resultado consolidado |
| --- | --- |
| H28 | **SUPPORTED WITH QUALIFICATION** |
| L3a ACCOUNT DISPLAY | **ACCOUNT-SOURCED / ACCOUNT-ONLY / EXECUTION-VERIFIED within A/B** |
| ACCOUNT / SUBJECT PRESENTATION SEPARATION | **PRESERVED within tested scope** |
| L3b | **PRESERVED / EXPERIMENTALLY ADDRESSED H27** |
| L3c | **PRESERVED / OPEN** |
| L4 | **PRESERVED / SOURCE-INSPECTION / OPEN** |
| L5 | **PRESERVED / EXPERIMENTALLY ADDRESSED H25** |
| NEXT MATERIAL PRESSURE | **L3c y L4 observed but NOT SELECTED; H29 NOT OPENED** |
