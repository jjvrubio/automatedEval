# Inspección previa al delta H29

Capturada antes de modificar aplicación o harness histórico.

Scenario.subjects determina existencia/orden. Scenario.initialSubjectStates se clona al construir MockDataAdapter y al reset. executeAction valida checkpoint, sujeto, operación y condiciones de sesión antes de asignar enabled al sujeto objetivo. Las acciones Evidence no asignan subjectStates. getSnapshot pasa el mismo mapa a projectSnapshot y éste al tercer argumento del guest projector. operationalSessionSubjectRef se utiliza para admisión y supervisión, pero no acredita viewer. Evidence se usa para evaluación y contadores, no como fuente de estado.

El copy actual elige por enabled y por id P1/P2: añade alistamiento/género en P1 y causalidad perspectival en P2. No representa not-enlisted frente a not-enabled por su valor, sino por referencia.

| Composición | subjectRef | operational state | phase/action | current status copy | Información justificada | Información NO justificada |
| --- | --- | --- | --- | --- | --- | --- |
| A | subject-p1 | not-enlisted | initial | Sin alistar | Ausencia de alistamiento en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p2 | not-enabled | initial | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p1 | enabled | enlist-p1 | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p2 | not-enabled | enlist-p1 | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p1 | enabled | discover-clue-a | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p2 | not-enabled | discover-clue-a | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p1 | enabled | activate-p2 | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p2 | enabled | activate-p2 | Habilitado por ti | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p1 | enabled | discover-clue-b | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p2 | enabled | discover-clue-b | Habilitado por ti | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p1 | not-enlisted | reset | Sin alistar | Ausencia de alistamiento en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| A | subject-p2 | not-enabled | reset | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p1 | not-enlisted | initial | Sin alistar | Ausencia de alistamiento en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p2 | not-enabled | initial | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p1 | enabled | enlist-p1 | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p2 | not-enabled | enlist-p1 | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p1 | enabled | discover-clue-a | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p2 | not-enabled | discover-clue-a | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p1 | enabled | activate-p2 | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p2 | enabled | activate-p2 | Habilitado por ti | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p1 | enabled | discover-clue-b | Alistada y habilitada | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p2 | enabled | discover-clue-b | Habilitado por ti | Habilitación operacional presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p1 | not-enlisted | reset | Sin alistar | Ausencia de alistamiento en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |
| B | subject-p2 | not-enabled | reset | Sin habilitar | Ausencia de habilitación en el estado presente | Causa, actor, viewer, género personal, lugar, narrativa; enabled tampoco distingue alistamiento de activación |

Los tres valores del tipo DemoSubjectState aparecen en A/B. enabled es el mismo valor para ambos sujetos y no retiene causa/actor/historia. La fuente es suficiente para una traducción neutral del estado actual. Host elegido: expresión status existente; no hay transporte nuevo.

Mapping posterior a esta inspección: not-enlisted → Estado: sin alistar; not-enabled → Estado: sin habilitar; enabled → Estado: habilitado. Habilitado concuerda con Estado, no con la persona. La ausencia de entrada no autoriza inferir ninguno de los tres valores: se emitirá texto vacío fuera del camino A/B completo; no se establece política productiva.
