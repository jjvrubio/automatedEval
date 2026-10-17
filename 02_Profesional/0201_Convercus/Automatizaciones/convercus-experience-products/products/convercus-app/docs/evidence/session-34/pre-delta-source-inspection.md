# S34 — inspección semántica anterior al delta

Inspección realizada sobre la App S33 recibida. Baseline y copias byte-identical de App/harness H33 capturadas antes del delta. El inventario `reference-use-inventory.txt` registra todos los usos textuales de ambos campos en fuentes, tests, archivos históricos y documentación del programa; se excluyen dependencias, builds y trazas serializadas. Estas últimas se leen como evidencia histórica, no como productores. No se reconstruyen decisiones anteriores.

## Matriz de procedencia y efectos

| Campo / capa declarante | Productor | Consumidores | Efecto operacional | Afirmación respaldada | Afirmaciones no respaldadas |
| --- | --- | --- | --- | --- | --- |
| ScenarioDefinition.operationalSessionSubjectRef?: string — contrato local | Scenario A y B declaran subject-p1 | MockDataAdapter/projectSnapshot | Selecciona referencia usada por guards | Referencia declarada de sujeto para el mecanismo local de sesión operacional | Cuenta, autenticación, viewer, ownership, nombre humano |
| Scenario.subjects[].id / actions[].subjectRef | Scenario A/B | Guards de admisión y atribución | Enlist/activate requieren sujeto en colección y estado esperado; enlist exige igualdad con session ref; activate exige session subject enabled y destino distinto | Correlación operacional explícita por igualdad de referencias en guards; no sólo parecido de nombres | Identidad real, actor humano que pulsa el botón, usuario con permiso productivo |
| subjectStates[operationalSessionSubjectRef] — adapter | Estados declarados y transiciones admitidas | projectSnapshot para affordance activate; executeAction para admisión activate | La activación de otro sujeto requiere habilitación del sujeto de sesión | Dependencia operacional local de estado | Autenticación, sesión web, titularidad |
| sessionSubjectRef?: string — SupervisionPerspectiveReadModel | projectSupervisionPerspective recibe argumento y lo copia sin transformación | App SystemPage | Ninguno al renderizar; transporte diagnóstico | Referencia operacional recibida | No valida por sí solo pertenencia a subjects ni crea una identidad |
| fixture.member — cuenta | Fixture → snapshot.member; member.name → GP.sessionLabel H28 | Presentación de cuenta/GP | No se consulta para seleccionar session ref ni admitir estas acciones | Presentación de cuenta separada | member→subject o cuenta→sesión operacional |
| «Cuenta/sesión operativa» + SP.sessionSubjectRef — App | Literal de UI + campo proyectado | Lector de Supervisión | Ninguno | Valor literal; sesión operacional en el alcance local inspeccionado | La palabra Cuenta añade una atribución no declarada |

Fuentes vigentes inspeccionadas: `contracts.ts` (ambos contratos, DemoProvider, acciones); `artifacts.ts` y `costa-artifacts.ts` (declaraciones); `bootstrap.ts` (resolución y construcción del adapter); `mock-adapter.ts` (constructor, projectSnapshot, getSnapshot, executeAction, reset); `vertical-evaluation.ts` (projectSupervisionPerspective); `App.tsx` (SystemPage). Los usos restantes son tests, archivos históricos o documentación: no añaden productores vigentes.

## Matriz de soporte semántico

| Pregunta | Estado | Alcance / evidencia |
| --- | --- | --- |
| A. Referencia a un sujeto | SUPPORTED | A/B declaran subject-p1 en subjects y lo seleccionan como session ref; enlist compara explícitamente referencias |
| B. Sujeto asociado al mecanismo operacional de sesión | SUPPORTED | Las guards usan esa selección y su estado para enlist/activate. Es el mecanismo simulado local, no autenticación |
| C. Sujeto que puede ejecutar ciertas acciones | NOT SUPPORTED como identidad del ejecutor | SUPPORTED sólo la restricción operacional: enlist sobre ese sujeto, activate sobre otro si aquél está enabled. executeAction recibe una acción, no credenciales ni actor. Quién ejecuta humanamente: NOT DETERMINED |
| D. Identidad de cuenta | NOT SUPPORTED | member tiene otra procedencia, sin mapping a session ref |
| E. Identidad autenticada | NOT SUPPORTED | No token/principal ni relación de autenticación en este flujo |
| F. Viewer | NOT SUPPORTED | No relación viewer→subject |
| G. Titularidad/ownership | NOT SUPPORTED | No contrato ni guard que atribuya propiedad |

La oferta de enlist en projectSnapshot comprueba estado, pero su admisión en executeAction además comprueba igualdad con la referencia de sesión. Por eso variar la referencia a subject-p2 en una copia de Scenario puede dejar un botón ofrecido que sería rechazado; NO se ejecutarán acciones en esa variante. No se corrige esta diferencia incidentalmente. Las acciones Evidence comprueban su propio subjectRef, estado y atribución; la sesión no reatribuye Evidence a sí misma.

## Descomposición y candidatos

«Cuenta» no está autorizada por SP.sessionSubjectRef. La barra mezcla dos nociones. «Sesión operativa» tiene respaldo en el mecanismo local inspeccionado, sin implicar sesión autenticada. El valor subject-p1 es referencia literal, no alias P1 ni nombre.

| Candidato | Evaluación |
| --- | --- |
| Referencia de sesión operativa | Puede sugerir ID de sesión en vez de referencia a sujeto |
| Sujeto de sesión operativa | Seleccionado: nombra el sujeto seleccionado por el mecanismo operacional; dd conserva la referencia literal |
| Referencia operacional de sujeto | Válido pero pierde la responsabilidad específica que sí respaldan las guards |
| sessionSubjectRef (campo crudo) | Alternativa diagnóstica suficiente; no imprescindible al existir soporte A/B para la formulación seleccionada |
| Cuenta, usuario, operador, P1 o nombre humano | Rechazado: necesita relación adicional o parsing |

## Decisión previa al delta

Modificar exclusivamente el dt «Cuenta/sesión operativa» por «Sujeto de sesión operativa». Mantener dd `{supervision.sessionSubjectRef}` byte a byte. No nuevo campo, transporte, relación, parsing ni lookup. No se modifica runtime, guards, evaluación o cualquier otra superficie. Remover lenguaje de cuenta no demuestra que no exista cuenta: sólo que esta fuente no autoriza esa afirmación.

Controles: App actual A/B mediante acciones públicas, navegación y reset; seis perturbaciones independientes por composición; comparación con App S33 archivada y traza S33 excluyendo sólo el dt autorizado; Retail/Arrival sin SP familiar. Variar session ref a subject-p1/subject-p2 en copia local de Scenario sólo para snapshot/render, sin acciones ni afirmación de recorrido alcanzable. Referencia opaca sólo como argumento de proyección y sustitución de read model, sin nuevo sujeto o Scenario productivo. Separar DOM/integration de browser visual.
