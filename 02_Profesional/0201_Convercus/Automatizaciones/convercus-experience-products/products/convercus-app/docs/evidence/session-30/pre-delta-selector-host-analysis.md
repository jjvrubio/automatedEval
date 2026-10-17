# H30 — análisis previo al delta de aplicación

Matriz ejecutada y persistida ANTES de modificar contratos o aplicación. Baseline: 91/91 pruebas. H26 NO-NEW-RELATION sigue FALSIFIED; se estudia sólo la relación ausente, sin repetir la búsqueda de fuente narrativa.

| A/B | Observación | Checkpoint | Acción disponible | Guest state | P1 | P2 | Evidence / P1 / P2 | Suficiencia | Claim | Message actual | Próximo presenterLabel |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | initial | ready | enlist-p1 | ready | not-enlisted | not-enabled | 0/0/0 | not-attempted | not-produced | La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas. | Alistarme |
| A | enlist-p1 | ready | discover-clue-a | active | enabled | not-enabled | 0/0/0 | not-attempted | not-produced | Estás alistada y habilitada. Todavía no has encontrado ninguna pista. Explora el jardín y registra tu hallazgo. | Encontrar la pista del jardín · yo |
| A | discover-clue-a | clue-a-discovered | activate-p2 | exploring | enabled | not-enabled | 1/1/0 | not-established | not-established | Tu pista del jardín está aportada. Activa al huésped 2 para que pueda explorar; activarlo no aporta ninguna pista. | Activar al huésped 2 desde mi cuenta |
| A | activate-p2 | clue-a-discovered | discover-clue-b | exploring | enabled | enabled | 1/1/0 | not-established | not-established | Has habilitado al huésped 2. Todavía no ha aportado pistas. Registra su hallazgo en la fuente cuando lo encuentre. | Encontrar la pista de la fuente · huésped 2 |
| A | discover-clue-b | adventure-established | ausente | complete | enabled | enabled | 2/1/1 | established | established | Las pistas aportadas cumplen la condición de esta aventura. | ausente |
| A | reset | ready | enlist-p1 | ready | not-enlisted | not-enabled | 0/0/0 | not-attempted | not-produced | La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas. | Alistarme |
| B | initial | ready | enlist-p1 | ready | not-enlisted | not-enabled | 0/0/0 | not-attempted | not-produced | La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas. | Alistarme |
| B | enlist-p1 | ready | discover-clue-a | active | enabled | not-enabled | 0/0/0 | not-attempted | not-produced | Estás alistada y habilitada. Todavía no has encontrado ninguna pista. Explora el jardín y registra tu hallazgo. | Encontrar la pista del mirador · Inés |
| B | discover-clue-a | clue-a-discovered | activate-p2 | exploring | enabled | not-enabled | 1/1/0 | not-established | not-established | Tu pista del jardín está aportada. Activa al huésped 2 para que pueda explorar; activarlo no aporta ninguna pista. | Activar a Mateo desde mi cuenta |
| B | activate-p2 | clue-a-discovered | discover-clue-b | exploring | enabled | enabled | 1/1/0 | not-established | not-established | Has habilitado al huésped 2. Todavía no ha aportado pistas. Registra su hallazgo en la fuente cuando lo encuentre. | Encontrar la pista del patio · Mateo |
| B | discover-clue-b | adventure-established | ausente | complete | enabled | enabled | 2/1/1 | established | established | Las pistas aportadas cumplen la condición de esta aventura. | ausente |
| B | reset | ready | enlist-p1 | ready | not-enlisted | not-enabled | 0/0/0 | not-attempted | not-produced | La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas. | Alistarme |

## Comparación y decisión de selector

| Candidato existente | Observación | Decisión |
| --- | --- | --- |
| checkpoint | Igual en A/B, pero ready colapsa initial/enlist-p1 y clue-a-discovered colapsa discover-clue-a/activate-p2. | REJECT AS SELECTOR. No se cambia checkpoint. |
| availableActionId | Igual en A/B: enlist-p1, discover-clue-a, activate-p2, discover-clue-b, ausente, enlist-p1. Distingue los tres momentos situados. | Seleccionado como discriminante técnico local de affordance, no como journey state universal. |
| GuestPerspective.state | exploring antes/después de habilitar P2. | Insuficiente. No ampliar valores. |
| subjectStates combination | enabled/not-enabled colapsa enlist-p1/discover-clue-a; enabled/enabled colapsa activate-p2/final. | Insuficiente. |
| Evidence/evaluation combination | Idéntica antes/después de enlist y de activate. | Insuficiente. No convertir Evidence IDs/tipos/markers en copy. |
| checkpoint + subjectStates | Distingue las posiciones ensayadas, pero reconstruye una clave compuesta con sujetos concretos cuando existe ya una affordance calculada. | Suficiente pero redundante; no seleccionado. |
| subjectStates + Evidence/evaluation | Puede distinguir dentro de A/B; exige recomponer múltiples dimensiones y acoplar selección a conteos/evaluación. | No seleccionado; evaluación conserva autoridad final. |
| Script expectedCheckpoint / índice del step | expectedCheckpoint también colapsa habilitaciones; el índice no es posición runtime autoritativa. | No seleccionado. presenterLabel no se interpreta. |

availableActionId = ausente al final no recibe sentinel ni entrada artificial. La finalización conserva evaluation.sufficiency == established como autoridad. Ausencia de acción por sí sola no significa completado.

## Comparación de hosts

| Host | Razón contextual | Decisión |
| --- | --- | --- |
| ScenarioDefinition | Es autoridad de sujetos, contextos, checkpoints, guards y transiciones. Podría transportar copy, pero el experimento sólo varía presentación manteniendo Scenario idéntico. Añadirlo aquí acoplaría esa variación a definición operacional sin necesidad observada. | No seleccionado. |
| DemoScript | Ya transporta presentación situada de la composición; el adapter recibe Script y puede pasar una relación opcional independiente del copy de affordance/Activity. | Seleccionado provisionalmente, sin convertirlo en PresentationModel. |
| GuestPerspectiveReadModel | Salida proyectada: alojar contenido autoritativo aquí invertiría la dirección de proyección. | Rechazado como fuente. |
| Fixture | Fuente de datos simulados y cuenta; proximidad no declara relación con posición. Puede extenderse técnicamente, pero no aporta mejor vínculo ni transporte que Script. | No seleccionado. |

## Forma experimental decidida después de la comparación

`DemoScript.experimentalJourneyPresentations?: Array<{ availableActionId: string; message: string }>`.
Únicamente tres entradas por A/B: discover-clue-a, activate-p2 y discover-clue-b. Son acciones DISPONIBLES en el presente, no la última acción ejecutada. Mensajes declarados explícitamente, sin parsing/interpolación.
Inicial: representación neutral desde ausencia de Evidence y P1 not-enlisted; no nueva entrada por uniformidad. Final: conservar literalmente representación derivada de evaluación. Prioridad de proyección: evaluación establecida; inicial neutral; relación situada aplicable; vacío.
Sin relación aplicable: message vacío como ausencia experimental local. No política UX productiva.

## Separación TES y límites

checkpoint != TES Progression; checkpoint != Experience semantic phase; checkpoint sequence != TES Sequence; checkpoint transition != TES Event. Rechazar checkpoint aquí no altera su rol operacional existente.
available action != journey state; conocer posición != disponer de narrativa; texto != hechos. Sólo GuestPerspective.message puede cambiar. App, supervisión, Activity, account/subject labels/status, TES, PSC, ADR y arquitectura quedan preservados. No viewer/account/session→subject. No H31.
