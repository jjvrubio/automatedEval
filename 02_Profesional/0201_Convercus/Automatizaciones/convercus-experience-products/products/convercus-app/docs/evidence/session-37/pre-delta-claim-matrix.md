# H37 — matriz de claims anterior al delta

Registrada después de inspeccionar los cuatro pares title/description y antes de editar sus declaraciones. Fuentes: `artifacts.ts:203–240`, `costa-artifacts.ts:110–151`, contratos `EvidenceInput`, `DemoAction`, `ScenarioDefinition`, `DemoScript`, guards/materialización de `mock-adapter.ts:132–192` y proyección SP. La baseline JSON registra bytes y textos recibidos. S36 se recibe cerrado; no se revisa su veredicto.

## Declaraciones canónicas recibidas

| Clave | Composición | Step / actionId | Title actual | Description actual |
| --- | --- | --- | --- | --- |
| A1 | A | discover-clue-a | Pista del jardín encontrada | Hallazgo aportado por ti. |
| A2 | A | discover-clue-b | Pista de la fuente encontrada | Hallazgo atribuido al huésped 2, registrado desde tu cuenta. |
| B1 | B | discover-clue-a | Pista del mirador encontrada | Hallazgo aportado por Inés. |
| B2 | B | discover-clue-b | Pista del patio encontrada | Hallazgo atribuido a Mateo, registrado desde la cuenta de Inés. |

Las claves de cada fila siguiente incorporan composición, step, title y description de esta tabla; las dos tablas constituyen una sola matriz por fragmento. O/E se usan con las cualificaciones de S36.

| Clave | Fragmento significativo | Claim afirmado | Fuente factual/editorial existente | Relación necesaria | Autoridad | Decisión |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | title: Pista… encontrada | Ocurrencia simulada aceptada representada como hallazgo | Acción, guards, Evidence efectiva + H25 | Aceptación antes de materializar fila | O + E, acotada | KEEP |
| A1 | title: del jardín | Ubicación del relato situado | Declaración H25 del step | actionId → presentación situada | E; no geolocalización factual | KEEP |
| A1 | description: Hallazgo | Mismo hallazgo de la fila admitida | Evidence aceptada + H25 | Ocurrencia → fila seleccionada | O + E | KEEP |
| A1 | description: aportado por ti | Viewer aportó/ejecutó el hallazgo | Literal H25; Evidence.subjects sólo identifica subject-p1 | viewer → contribuidor/ejecutor; eventualmente viewer → sujeto | AUSENTE para relación; E sólo para palabras | REDUCE a registro sin ejecutor |
| A1 | composición: ti + ocurrencia atribuida | Viewer identificado con sujeto/contribuidor de esa Evidence | No existe viewer en acción, Scenario ni read models | viewer → subject-p1/contribuidor | AUSENTE | REMOVE |
| A2 | title: Pista… encontrada | Ocurrencia admitida presentada | Guards + Evidence + H25 | Aceptación → fila | O + E | KEEP |
| A2 | title: de la fuente | Contenido situado | Declaración H25 | actionId → presentación | E | KEEP |
| A2 | description: Hallazgo atribuido | Atribución del hallazgo, sin afirmar quién pulsó/ejecutó | Evidence.subjects = subject-p2 + relato H25 | Atribución operacional por ID; relato local separado | O para ID; E para narración | KEEP |
| A2 | description: al huésped 2 | Etiqueta narrativa local del sujeto atribuido | H25 explícito; acción/Evidence atribuidas a subject-p2 | Correspondencia situada del step; no parsing del ID ni lookup H27 | E local, no identidad humana universal | KEEP cualificado |
| A2 | description: registrado | Existencia de registro tras aceptación | Materialización del adapter | Ocurrencia aceptada + presentación → fila | O + E | KEEP como significado de la fila |
| A2 | description: desde tu cuenta | Cuenta del viewer como origen de ejecución | Sólo literal; member.name es presentación de cuenta H28 | viewer → cuenta; cuenta → ejecución | AUSENTE | REMOVE cláusula; registro queda en fila |
| B1 | title: Pista… encontrada | Ocurrencia admitida presentada | Guards + Evidence + H25 | Aceptación → fila | O + E | KEEP |
| B1 | title: del mirador | Ubicación editorial situada | H25 explícito | actionId → presentación | E | KEEP |
| B1 | description: Hallazgo | Ocurrencia de la fila | Evidence aceptada + H25 | Ocurrencia → fila | O + E | KEEP |
| B1 | description: Inés | Nombre dentro del relato local | H25; H27 contiene separadamente etiqueta GP | Ninguna identidad universal acreditada | E para nombre narrativo solamente | REMOVE aquí, porque ocupa el argumento del predicado ejecutor retirado |
| B1 | description: aportado por Inés | Inés es contribuidora/ejecutora del hallazgo | Literal H25; Evidence sólo atribuye subject-p1 | Nombre humano → contribuidor/ejecutor | AUSENTE; igualdad con member/GP no basta | REDUCE a registro sin ejecutor |
| B2 | title: Pista… encontrada | Ocurrencia admitida presentada | Guards + Evidence + H25 | Aceptación → fila | O + E | KEEP |
| B2 | title: del patio | Ubicación editorial situada | H25 explícito | actionId → presentación | E | KEEP |
| B2 | description: Hallazgo atribuido | Atribución narrativa del hallazgo admitido | Evidence.subjects = subject-p2 + H25 | Atribución ID y narración local, sin identidad de ejecutor | O + E cualificado | KEEP |
| B2 | description: a Mateo | Etiqueta humana local del relato | H25 explícito, independiente de subjectPresentations | Correspondencia narrativa declarada para este step | E; no prueba identidad, actor, autenticación ni label universal | KEEP cualificado |
| B2 | description: registrado | Existencia de registro | Adapter después de guards | Aceptación + presentación → fila | O + E | KEEP como significado de la fila |
| B2 | description: desde la cuenta de Inés | Cuenta identificada como origen de ejecución | Literal H25; no cuenta ejecutora en acción/Evidence | cuenta → ejecución; titular → contribuidor no inferible | AUSENTE | REMOVE cláusula; registro queda en fila |

La atribución operacional `Evidence.subjects[].id` (proyectada como `SP.evidence[].subjectRefs`) queda congelada en A1/B1=subject-p1 y A2/B2=subject-p2. No se elimina ni reconstruye en las descripciones.

## Decisión después de la matriz

| Clave | Nueva description propuesta | Predicados que permanecen |
| --- | --- | --- |
| A1 | Hallazgo registrado. | Registro del hallazgo aceptado, sin agente, viewer ni cuenta |
| A2 | Hallazgo atribuido al huésped 2. | Atribución narrativa H25; referencia operacional permanece en Evidence; no ejecución humana |
| B1 | Hallazgo registrado. | Registro del hallazgo aceptado, sin agente, viewer ni cuenta |
| B2 | Hallazgo atribuido a Mateo. | Atribución narrativa H25 local; Mateo no es identidad operacional ni fuente dinámica H27 |

Los cuatro títulos conservan jardín/fuente/mirador/patio. No contienen atribución viewer/cuenta/ejecutor que obligue a ampliar la variable. No se ha encontrado relación existente contradictoria con S36. `operationalSessionSubjectRef` interviene en guards de enlist/activate; no identifica viewer ni registra ejecutor. `Evidence.source=demo-control` tampoco identifica una persona o cuenta.

Se conserva la etiqueta narrativa de A2/B2 porque «atribuido a» no afirma quién realizó la interacción. En B1 «aportado por» sí predica contribución humana: la autoridad de Inés como nombre narrativo no acredita ese verbo. Esta distinción mantiene la cualificación H36 de nombres H25; no transforma H27 en identidad universal. La compatibilidad resultante es local y editorial, no verificación de personas reales.
