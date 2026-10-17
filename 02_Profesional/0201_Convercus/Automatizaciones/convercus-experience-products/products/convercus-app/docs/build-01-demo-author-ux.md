# BUILD 01 — registro de Demo-Author UX

Fecha: 2026-09-23. Observaciones realizadas durante la primera construcción deportiva. LOCAL / EXPERIMENTAL / NOT PROMOTED. Este registro describe trabajo real de configuración y programación; no evalúa un editor inexistente ni la UX del participante.

La demo se ha construido con artefactos TypeScript. Cambiar texto o fechas dentro de los slots incorporados resulta posible editando datos; crear esos slots, su transporte y sus consecuencias ha exigido código. No se ha construido autoría sin programación.

| Variación deseada | Clasificación principal de la resolución en BUILD | Configuración disponible al empezar | Código / configuración nueva necesarios | ¿Duplicación requerida? | Fricción observada |
| --- | --- | --- | --- | --- | --- |
| Marca | existing configuration | BrandArtifact, tokens, logoUrl y resolución de marca | Marca Brisa Sport, SVG local, registro de catálogo; favicon de esta composición | No copia de otra App | Alta técnica en catálogo; algunos tokens de contraste no son obligatorios en la validación heredada |
| Temporada | new situated configuration | No representación deportiva | season con ID/título/periodo y superficie que lo diferencia del evento | No | Fue necesario definir tipos y lectura antes de poder variar datos |
| Disciplinas y eventos | new situated configuration | Contenido/fixtures, sin eventos deportivos | Tres eventos con seasonRef, disciplina, fecha, lugar y ejecutabilidad explícita | No | Sólo Carrera tiene comportamiento; convertir otra tarjeta en ejecutable requiere más que cambiar copy y el runtime local lo rechaza |
| Fechas y lugares | new situated configuration | Strings de fixtures existentes, sin evento deportivo | Datos ISO de cada evento y formateo visible | No | Edición manual en TypeScript; no calendario de autoría ni validación general de fechas |
| Modalidades | new situated product code | No selector ni valor por inscripción | Radios Social/Bienestar, payload, validación y persistencia local | No | Labels/descripciones se editan en artefactos; añadir una modalidad real exige código, no basta añadir una etiqueta |
| Persona | new situated product code | SubjectReference individual; AppSnapshot heredado exigía member | Persona local explícita; nombre ficticio; relación como cliente no establecida | No | No se pudo reutilizar el fixture de miembro responsablemente; se conserva lectura deportiva separada |
| Membership status | new situated product code | Perfil de miembro; sin estado externo explícito | external/member en persona; externo ejecutado, miembro de contraste informativo | No | Este corte sólo admite persona ejecutada externa; cambiarla a miembro falla explícitamente, no simula el recorrido secundario |
| Copy | new situated configuration | Script y algunos slots experimentales | Introducción, eventos, modalidades, badge e invitación en artefactos; textos de interacción en componente local | No lógica copiada | Parte del copy sigue siendo literal de UI. No todo se puede variar desde un único archivo |
| Presencia | new situated product code | Frontera pública y Evidence hotelera con contexto incompatible | Registro local con persona/inscripción/evento, source fijo simulated-check-in y marca simulation | No reutilización falsa de hotel | Nueva representación necesaria; fuente no editable desde un label para fingir acreditación externa |
| Esfuerzo | new situated product code | No payload ni input de intensidad | Selector y registro independiente con source participant-self-report | No | Tres valores técnicos aceptados; texto visual y valor no son intercambiables |
| Regla | new situated product code | K hotelero no aplicable | Función local de reconocimiento por inscripción+presencia+esfuerzo y coincidencia de referencias | No copia de K | Criterio en código y versión explícita; no editor de reglas. Cambiarlo requiere programación y nuevas pruebas |
| Insignia | new situated product code | Sin concesión de badge en runtime | Estado individual con ruleRef, Evidence refs, motivo y representación visible | No | Título/motivo configurables; elegibilidad y vínculo a Evidence no se pueden editar desde copy |
| Oportunidad de captación | new situated product code | Sin conversión/CRM implementados | Proyección de invitación disponible después de badge; información de club como datos | No | No hay alta ni lead ni consentimiento. El botón informa; añadir conversión sería otro corte |
| Perspectiva CRM | new situated product code | Dos perspectivas de Aventura Familiar | Nueva lectura del mismo snapshot: datos ficticios, registros, reconocimiento y oportunidad separados | No copia de Supervisión/K | Fue necesario crear una lectura comercial; cambiar el título de Supervisión no habría bastado |
| Composición y entrada | small reusable code extension | Manifest, brand resolver, bootstrap antes de App | Referencia deportiva local, resolveAppDemo y consumidor DemoApp; resolución heredada conservada | No copia de resolver ni adaptador completos | Referencias a fixture/scenario y selector local se registran manualmente en más de un lugar y se comprueba su coherencia |
| Experience references | new situated product code | Scenario heredado exige experienceRef | Shape local de SportsScenario sin Experience ni contextos hoteleros | No copia/renombrado de Experience | El tipo heredado no representaba el caso; no se ha generalizado a todos los Scenarios |
| Vela / equipos Vóley | new situated configuration | Sin ejecución deportiva | Tarjetas informativas con exclusión visible de inscripción y reconocimientos colectivos | No | Variar contenido sí; disponer de ejecución no |
| Competición, trofeos y beneficio por recurrencia | new situated configuration | Sin implementación deportiva | Sólo contraste textual claramente sin ejecutar; no estado competitivo fabricado | No | Estas variaciones siguen sin poder producirse mediante este corte |
| Reset / independencia | new situated product code | Patrón público getSnapshot/executeAction/reset demostrado | Estado local deportivo, clonación y reset; tests cruzados con R/H/A/B | No copia de MockDataAdapter | Se reutiliza la frontera de responsabilidad, pero no el shape de miembro ni los datos de hotel |

No se observó necesidad de duplicar App, MockDataAdapter, Family Adventure ni K. La implementación tiene un nuevo runtime situado, no una copia renombrada de esos archivos. Las categorías duplication required, manual workaround y blocked no describen una solución adoptada en el producto.

## Fricciones adicionales observadas

- Antes de programar, Node incluido con Codex no podía cargar el binding nativo; Node oficial temporal ejecutó la baseline sin cambiar dependencias. Es fricción de entorno, no capacidad nueva del producto.
- La ampliación inicial de la firma de App conflictuó con un harness histórico que tipaba el componente archivado. Se conservó la firma de App y se añadió un consumidor de composición pequeño, DemoApp. No se editó el harness.
- Los harnesses de S21–S39 mezclan verificación histórica con comprobación de bytes del working tree. Después de un delta intencional, 18 controles fallan por hashes antiguos. Se conserva la evidencia y se separa el resultado actual; no se creó infraestructura general de replay.
- Dos rechazos de formulario fueron útiles para observar la presentación del error en móvil: aparecía fuera de pantalla. Se colocó junto al recorrido y se le dio foco al rechazar la acción para cumplir la condición de errores legibles del BUILD; no se cambió validación.
- En móvil, la inscripción queda después de las tres tarjetas de eventos. El recorrido es largo y el cambio de perspectiva está arriba. Se registra como fricción para uso humano; no se reorganizó la UX para resolverla.
- El copy de datos ficticios, simulación y procedencia ocupa espacio. Su comprensión y carga deben ser cuestionadas por una persona; no se ha sustituido esa observación por una aceptación del agente.

La prueba de variación de nombre/labels/copy verifica que no cambian hechos, atribución ni elegibilidad. Esto prueba independencia local, no que el autor no pueda escribir un texto engañoso ni que exista validación editorial automática.

No se selecciona trabajo posterior. Este registro queda como input para evaluar juntos las fricciones de autoría después del uso humano.
