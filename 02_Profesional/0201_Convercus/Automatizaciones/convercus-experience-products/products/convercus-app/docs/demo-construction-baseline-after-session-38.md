# Base para preparar demos — recapitulación tras S38

Estado: recapitulación documental del producto recibido, no una nueva sesión de producto ni aceptación comercial. [Informe y evidencia S38](session-38-historical-replay-portability-evidence-integrity.md).

## Con qué contamos

Existe una App React/TypeScript mobile-first, con datos mock, acciones simuladas y reset. Las composiciones comparten la maquinaria actual; sus referencias seleccionan marca, fixtures, Scenario y Script. No es todavía un generador general de demos ni una integración con Convercus real.

| Composición existente | Selector local | Qué acredita hoy |
| --- | --- | --- |
| Retail | /?demo=retail-baseline | Control genérico de perfil, beneficios, contenido y actividad mock |
| Llegada Aurora | /?demo=hospitality-stay | Recorrido simulado de llegada y regresión del runtime actual |
| Aventura Familiar A | /?demo=hospitality-family-adventure | Recorrido A completo, atribución por subjects, evaluación y Activity situada |
| Aventura Familiar B / Costa | /?demo=hospitality-family-adventure-costa | Contraste experimental de composición y recorrido B; NO demo comercial aceptada |

Fuentes: [manifests](../prototype/src/demo-factory/manifests.ts), [bootstrap](../prototype/src/demo-factory/bootstrap.ts), [contratos](../prototype/src/demo-factory/contracts.ts), [artefactos A](../prototype/src/demo-factory/artifacts.ts) y [B](../prototype/src/demo-factory/costa-artifacts.ts). Son puntos de inspección, no autorización para editarlos dentro de S38.

## Qué deja asentado esta sesión

La base de verificación vuelve a ejecutar todos sus tests: 106 PASS / 0 FAIL; tipos, lint y build PASS. H21–H23 ya no necesitan metadata Finder ausente y siguen detectando alteración o retirada de fuentes materiales.

La verificación actual H37 ejecuta 14 recorridos App, 77 frames y 231 capturas DOM, más controles negativos y observaciones aisladas. Histórico y actual se comprueban separadamente. El producto permanece byte-idéntico a S37.

No se rehace la historia: H21 y H36 conservan sus falsaciones. La infraestructura reparada no convierte hipótesis históricas en capacidades aceptadas.

## Límites que una demo debe hacer visibles

Las acciones y hallazgos son simulados. Evidence acredita lo que acepta el runtime del experimento, no un hecho externo. Un subject, un nombre editorial, la cuenta mostrada y quien pulsa una acción no son identidades intercambiables.

Activity conserva títulos situados y atribución operacional, pero las descripciones H37 no afirman quién ejecutó o desde qué cuenta se registró el hallazgo. Una etiqueta narrativa tampoco prueba identidad humana o presencia física.

No están acreditados staging/API real, autenticación, funcionamiento en dispositivo real, aceptación visual/comercial ni generación arbitraria de nuevas Experiences. /showcase es una presentación en marco iPhone, no emulación de Safari/iOS.

## Cómo retomar el trabajo local

Desde prototype, con Node >=24 y las dependencias existentes: npm run dev. Usar la URL que anuncie el servidor y añadir uno de los selectores anteriores. npm run check reúne tipos, lint, tests y build. [Guía de ejecución existente](../prototype/README.md).

S38 se verificó con Node oficial 24.14.0 arm64. El Node incluido en Codex había mostrado un rechazo de firma nativa en S37. El replay DOM mantiene una dependencia de la ruta absoluta del logo: mover el repositorio puede requerir estudiar esa presión antes de prometer reproducibilidad. No ocultar el fallo actualizando snapshots sin auditoría.

## Decisiones todavía necesarias para construir una demo concreta

Falta elegir destinatario y objetivo narrativo, composición de partida, recorrido y resultado que se quiere enseñar, contenido permitido y criterio de aceptación visual. La recapitulación no toma esas decisiones ni selecciona automáticamente una presión para H39.

Una futura construcción deberá distinguir reutilización de lo ya demostrado de cualquier capacidad nueva que requiera su propio experimento. El resultado de S38 es una base local verificable para preparar ese trabajo; no certifica que una demo concreta esté lista para clientes.

Architecture v0.5 y ADR-001–005 sin cambios; TES/PSC sin cambios; PSC-P01 abierto; PSC-P02 no creado. Regla de evidencia S38 y heurísticas semánticas anteriores NOT PROMOTED.
