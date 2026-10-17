# H32 — Candidate host analysis, before application delta

Fecha: 2026-09-18. Inspección sobre la baseline S31 recibida. Este documento precede al delta; la elección es provisional y queda sometida a los controles ejecutables H32.

| Candidato | Responsabilidad actual | Variación A/B | Acoplamiento introducido | Transporte | Reversibilidad / cambio de autoridad | Decisión |
| --- | --- | --- | --- | --- | --- | --- |
| Manifest | Selección declarativa por referencias, locale y capabilities | Sí | Copy inline mezclaría selección/configuración con edición; referenciar otro artefacto ampliaría el catálogo | Ya llega a App | Campo opcional reversible, pero amplía responsabilidad de selección sin necesidad | No seleccionado |
| ExperienceDefinition | Identidad/nombre/baseline de Experience compartida | No: misma experience:family-adventure@1 | Exigiría duplicar Experience, añadir overrides o contenido situado al significado compartido | runtime.experience | Reversible técnicamente; corrompe la independencia que se debe mantener | Rechazado |
| ScenarioDefinition | Contextos, sujetos, estados iniciales, acciones, guards/checkpoints/transiciones | Sí | Añade edición a definición operacional; no se demuestra necesidad de ese acoplamiento | runtime.scenario | Campo reversible, pero amplía responsabilidad actual | No seleccionado, no por convención sino por separación operacional/editorial requerida |
| DemoScript | Orquestación/presentación de demostración; relaciones experimentales independientes H25/H27/H30 | Sí | Nueva relación editorial estática, sin reglas ni fuente factual; no se agrega a las anteriores | manifest.scriptRef → resolver → runtime.script → AppShell → HomePage | Campo opcional local eliminable; no cambia autoridad operacional ni significado de Experience | Seleccionado provisionalmente |
| Fixture | Cuenta, beneficios, noticias, registros de Activity simulados | Sí, pero A comparte fixture con Arrival | Proximidad de copy no declara framing; noticia B no tiene ese rol. Un nuevo campo exigiría una responsabilidad editorial adicional y transporte al margen del snapshot actual | Provider/snapshot hoy; resolver tendría que exponer un dato adicional | No existe relación compatible de intro; no reutilizar news | No seleccionado |
| Nuevo artefacto dedicado | Ninguna responsabilidad/entidad existente | Podría | Añadiría identidad, referencia, catálogo y resolución para un string | Nueva referencia/validación/transportes | Mayor superficie; ningún candidato existente ha falsificado aún el experimento | No necesario bajo minimalidad |

## Decisión y límites

El framing probado describe editorialmente la demostración situada seleccionada, no un hecho ocurrido ni la definición de Experience. DemoScript permite declarar esa relación sin cambiar Scenario, Experience, Fixture o Manifest; su vinculación con la composición es explícita mediante scriptRef y scenarioRef, comprobada por bootstrap. No se elige porque haya alojado antes otros strings. La recurrencia es evidencia de presión, no autoridad automática.

Se ensayará exclusivamente `DemoScript.experimentalIntroductoryFraming?: string`, EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED. Sin agrupación común de presentaciones. Los controles de variación y contradicción deben demostrar que el nuevo dato no gobierna estado, hechos o evaluación.

Declaraciones propuestas como nuevas declaraciones editoriales, no extraídas de H25/H30/news:

- A: «Una aventura de pistas entre el jardín y la fuente.»
- B: «Una aventura de pistas entre el mirador y el patio.»

Son estáticas, introductorias y sin segunda persona ni atribución de estancia, hallazgo o habilitación. No confieren autoridad factual a los lugares nombrados.

## Dos autoridades y responsabilidad del transporte

`Mi aventura` queda como UI genérica. `runtime.brand.name` identifica exclusivamente la marca y viaja como prop local a HomePage. No se crea un campo de marca en contrato ni un título/propiedad de composición.

La intro llega desde `runtime.script?.experimentalIntroductoryFraming`, fuera de GuestPerspective/AppSnapshot. Es presentación estática de composición y no cambia con una transición; pasar por el snapshot solo por comodidad de props le atribuiría una responsabilidad no demostrada. La marca y la intro se pasan separadas, sin objeto envolvente nuevo.

Ausencia local: no renderizar el párrafo introductorio si no hay string no vacío; sin reconstrucción ni fallback. No es política UX productiva. Se preservan el h1/huntName, Supervisión, navegación fija y todo copy ajeno.

## Condición de continuación

Si controles actuales de App A/B, independencia, contradicción, ausencia o regresión factual muestran que esta relación exige otra autoridad o modifica hechos, STOP; no crear una abstracción sustituta en esta baseline.
