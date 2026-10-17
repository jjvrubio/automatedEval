# S35 — inspección de nombre anterior al delta

Baseline S34 capturada antes de cualquier edición. Inventario de usos: `name-use-inventory.txt`. Se inspeccionan contrato ExperienceDefinition, declaraciones A/B/Arrival, resolveDemo, ResolvedDemoRuntime, projectSnapshot/MockDataAdapter, projectGuestPerspective, GuestPerspectiveReadModel.huntName y HomePage. No se reconstruyen decisiones anteriores.

| Campo / capa | Productor | Consumidor | Responsabilidad actual | Transporte actual | Correspondencia |
| --- | --- | --- | --- | --- | --- |
| ExperienceDefinition.id/name/tesBaseline, Demo Factory | artifacts.experiences | resolveDemo → runtime.experience | Referencia técnica, nombre legible y baseline semántica, respectivamente | Experience se resuelve por Scenario.experienceRef; name no llega al provider/proyector | Nombre de la Experience referenciada, no branding |
| Scenario.experienceRef | Scenario A/B | resolveDemo y selección operacional existente del adapter | Referencia a Experience compartida | Mismo artefacto family-adventure en A/B | Selecciona artefacto; no genera copy |
| ResolvedDemoRuntime.experience | resolveDemo | App usa tesBaseline en panel genérico; runtime disponible | Artefacto resuelto | Provider se construye sólo con Fixture/Scenario/Script | Falta transporte del nombre hacia GP |
| GP.huntName | Literal en projectGuestPerspective | HomePage h1 #adventure-title | Título presentado de la Experience | Literal → GP → h1 | Correspondencia semántica documentada; procedencia ejecutable ausente |

Evidencia semántica adicional al código: S21 audit M05 clasifica la duplicación como «Aventura Familiar / Experience» y sitúa identidad/nombre resueltos como fuente del read model. S26, matriz de procedencia, define huntName como «Título presentacional de Experience; no hecho» y precisa que no hay nombre distinto de instancia de hunt. S26 candidatos identifica ExperienceDefinition como nombre y referencia/semántica de Experience. S31 distingue expresamente nombre de marca, nombre de Experience e introducción de composición. Estas responsabilidades permanecen en el código actual: h1 sólo consume GP; Script no declara huntName ni título de campaña; A/B distintos Scenarios apuntan al mismo artefacto.

La definición candidata documental family-adventure.md también tiene name, pero no es la fuente runtime ni su lectura equivale a promoverla. Se usa la ExperienceDefinition efectiva de Demo Factory, sin conectar un modelo legacy.

## Matriz semántica

| Pregunta | Estado | Límite |
| --- | --- | --- |
| A. name identifica la Experience como artefacto semántico | SUPPORTED como denominación | La identidad técnica sigue siendo id/referencia; name no es clave única ni criterio de evaluación |
| B. Nombre destinado a lectura humana | SUPPORTED | Nombre explícito legible frente a id técnico y responsabilidad documentada; no se prueba localización universal |
| C. Estable entre Scenarios/composiciones de la misma Experience | SUPPORTED en A/B | Ambos resuelven el mismo artefacto; no inmutabilidad temporal universal |
| D. huntName significa nombre presentado de esa Experience | SUPPORTED en esta superficie | S26 explícito, M05 S21 y consumidor h1 actual; no sólo igualdad de strings |
| E. Título de composición/journey/campaña u otra responsabilidad | NOT SUPPORTED en la superficie inspeccionada | No relación declarada con instancia/campaña; intro y mensajes tienen autoridades separadas. Requisitos futuros: NOT DETERMINED |

## Candidatos y decisión

Experience.name tiene autoridad compatible. DemoScript aloja contenido situado pero no nombre de Experience; recurrencia no autoriza apropiarlo. Scenario define situación/operación y referencia, no nombre. BrandArtifact.name nombra marca. Manifest/demoId identifica/configura composición; no se parsea. Literal del proyector es síntoma, no autoridad.

Decisión: RELATIONSHIP SEMANTICS EXISTING / TRANSPORT MISSING. Transportar únicamente escalar name desde Experience resuelta por resolveDemo, vía constructor del provider y projectSnapshot hasta projectGuestPerspective.huntName. App y contratos se mantienen. No objeto completo, lookup alternativo ni relación editorial. Parámetros finales con texto vacío para llamadas sin Experience mantienen compatibilidad de utilidades genéricas; ningún fallback a Script o literal histórico. El resolver normal suministra name obligatorio del artefacto a A/B.

name:string es obligatorio; no se borrará ni se debilitará contrato. La cadena vacía sí es un string válido y no existe validación non-empty: puede observarse en harness como nombre declarado vacío, sin inventar ausencia o fallback.

Variación ID: Experience.id puede cambiar sólo en copia de catálogo manteniendo clave de referencia estable; el resolver usa la clave, no parsea id. No se cambiará experienceRef: el adapter selecciona Family Adventure por esa referencia y hacerlo ampliaría el experimento a selección operacional. Se distinguirá independencia de id del alcance no ensayado de renombrar la clave de catálogo.

Plan: App actual A/B y negativos Retail/Arrival; variación sólo name y vacío; id técnico; brand; cinco presentaciones Script (incluido presenterLabel); member; estados/Evidence por acciones públicas. Comparar todos los facts/evaluaciones y DOM contra S34 salvo huntName/h1 en variantes de nombre. Mantener H25/H27–H30/H32–H34. Históricos se aislarán con copias y rutas explícitas de instrumentación, sin rebasar hashes ni modificar evidencia previa. Browser visual y DOM/integration se informarán separadamente.
