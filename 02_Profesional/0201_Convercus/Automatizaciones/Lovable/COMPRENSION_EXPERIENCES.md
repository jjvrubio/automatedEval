# Comprensión conceptual de Experiences en Convercus

## Propósito de este documento

Este documento recoge una comprensión de trabajo sobre **Experiences**, la funcionalidad de Convercus destinada a orquestar experiencias de cliente. Está escrito para poder leerse de forma continua, revisar el razonamiento y detectar términos que todavía necesiten precisión.

No pretende sustituir una especificación funcional ni describir una API. Su función es establecer un lenguaje común antes de diseñar pantallas, modelos de datos o integraciones.

## Punto de partida

En Convercus, **Experiences** es el nombre en inglés de una funcionalidad de producto. Su propósito es orquestar experiencias en el sentido amplio y original de la palabra: algo que una persona atraviesa, vive y acumula a lo largo de un recorrido.

Por tanto, Experiences no debe traducirse mentalmente como un catálogo de actividades, premios especiales o beneficios “experienciales”. Tampoco es simplemente otro nombre para campañas, cupones o gamificación.

La funcionalidad Experiences permite construir y operar recorridos en los que Convercus:

- Reconoce un contexto o una señal de entrada.
- Observa eventos verificables del cliente.
- Interpreta esos eventos dentro de una secuencia.
- Mantiene el estado y la progresión de cada participante.
- Decide si debe intervenir y en qué momento.
- Activa contenidos, incentivos, reconocimientos o recompensas.
- Conduce hacia un resultado deseado.
- Conserva continuidad para permitir seguimiento, reentrada o reactivación.

Una **Experience** concreta sería, por tanto, una configuración operativa de ese recorrido. La **experiencia del cliente** es lo que la persona vive como resultado de atravesarlo.

## Una formulación breve

> **Experiences es la capacidad de Convercus para convertir eventos dispersos del cliente en recorridos con contexto, estado, progresión e intervenciones coordinadas.**

Esta formulación contiene la diferencia fundamental frente a un incentivo aislado. Experiences no se limita a provocar una acción: organiza la continuidad entre varias acciones, decisiones y momentos.

## Experiencia vivida y funcionalidad Experiences

Conviene separar dos planos.

En el plano humano, una experiencia es el recorrido vivido por una persona. Incluye lo que encuentra, interpreta, decide, hace y recibe. Puede comenzar con una necesidad poco definida y terminar en una compra, un aprendizaje, una participación, una relación más fuerte con la marca o una futura reactivación.

En el plano del producto, Experiences es el sistema que hace operable ese recorrido. No “fabrica” directamente la vivencia subjetiva, pero coordina las condiciones que permiten acompañarla:

```text
Señales + contexto + eventos + reglas + estado + intervenciones
                              ↓
                 experiencia orquestada
```

Esta distinción evita atribuir al software la totalidad de la experiencia humana. Convercus orquesta el recorrido y sus intervenciones; el cliente vive la experiencia.

## Qué es un incentivo

Un incentivo es un instrumento destinado a aumentar la probabilidad de una conducta. Puede actuar sobre una conducta de consumo, participación, exploración, recomendación, disfrute o continuidad.

No tiene que ser exclusivamente económico. Son posibles incentivos:

- Un descuento.
- Puntos adicionales.
- Un cupón.
- Acceso prioritario.
- Reconocimiento o estatus.
- Contenido exclusivo.
- Una sesión de estilismo.
- Una actividad de bienestar.
- La posibilidad de desbloquear una recompensa futura.

El incentivo responde a una pregunta local:

> ¿Qué intervención puede aumentar la probabilidad de la siguiente conducta deseada?

Experiences responde a una pregunta más amplia:

> ¿Qué recorrido estamos construyendo, qué está viviendo el cliente ahora y qué intervención tiene sentido en este momento?

## Incentivo, recompensa y beneficio

Estos términos se relacionan, pero no son idénticos.

Un **incentivo** opera como expectativa antes de la conducta. Un mensaje como “completa tres actividades y recibirás acceso al spa” utiliza el acceso al spa como motivo para actuar.

Una **recompensa** es el beneficio que se concede después de verificar la conducta. Cuando la tercera actividad queda registrada, el acceso al spa deja de ser solamente una promesa y se convierte en recompensa otorgada.

Un **beneficio** es el valor concreto que recibe o puede recibir el cliente. Puede ser económico, funcional, social, emocional o experiencial.

El mismo objeto puede cambiar de función según el momento:

```text
Beneficio anunciado  → incentivo
Conducta verificada  → condición cumplida
Beneficio concedido  → recompensa
```

Experiences conecta esos momentos y mantiene el estado necesario para saber qué se anunció, qué ocurrió y qué debe concederse.

## El incentivo dentro de una Experience

Una Experience puede contener ninguno, uno o varios incentivos. El incentivo no define por sí solo la Experience.

En “Circuito de decisión: ocasión”, la clienta comienza con una búsqueda poco definida. El escaneo de una prenda convierte la exploración en señal. Convercus interpreta la ocasión, aporta dirección y construye continuidad mediante opciones coherentes. El incentivo aparece únicamente cuando la intención ha madurado.

La Experience completa es:

```text
Duda inicial
  → activación contextual
  → dirección de ocasión
  → continuidad relevante
  → intervención oportuna
  → resolución o reactivación
```

El incentivo es solo una posible intervención dentro de ese recorrido. Si se adelantara, podría degradar la experiencia convirtiéndola en una promoción genérica. Su valor proviene tanto de lo que ofrece como del momento en que se activa.

## La importancia de los eventos

Un evento es un hecho observable que Convercus puede registrar o recibir. Por ejemplo:

- Registro en el programa.
- Inicio de sesión.
- Escaneo de un código QR.
- Escaneo de una prenda.
- Visita a una tienda.
- Compra en una categoría.
- Participación en una actividad.
- Canje de un cupón.
- Devolución de una prenda para reparación.
- Recomendación de otra persona.

El evento no es necesariamente el final del proceso. En Experiences, un evento puede funcionar como:

- Entrada al recorrido.
- Evidencia de progreso.
- Condición para cambiar de estado.
- Señal para elegir una rama.
- Disparador de una intervención.
- Confirmación de un resultado.

Esta idea es esencial: la compra no tiene por qué cerrar la relación y el escaneo no es únicamente una interacción aislada. Ambos adquieren significado al situarse dentro de una secuencia.

## Evento, paso y estado

Tampoco conviene tratar estos tres conceptos como sinónimos.

Un **evento** es algo que sucede. Un **paso** es una unidad comprensible del recorrido diseñado. Un **estado** representa la situación actual de una participación concreta.

Por ejemplo:

```text
Evento: compra registrada en la categoría "zapatos"
Paso: completar una categoría de la Maratón de Temporada
Estado: 2 de 4 categorías completadas
```

Varios eventos pueden contribuir al mismo paso. Un evento también puede invalidarse, repetirse o no producir progreso si no cumple las condiciones de la Experience.

## Progresión

La progresión convierte acciones dispersas en continuidad visible. Permite que el cliente no tenga que “empezar de cero” en cada interacción.

Puede expresarse como:

- Pasos completados.
- Categorías exploradas.
- Actividades realizadas.
- Puntos o estrellas acumuladas.
- Nivel alcanzado.
- Hitos desbloqueados.
- Tiempo restante.
- Próxima acción recomendada.

La progresión no tiene que ser siempre lineal. Una Experience puede incluir rutas alternativas, condiciones opcionales, repeticiones o una regla como “completa dos de estas tres acciones”.

## Intervención

Una intervención es una respuesta deliberada del sistema ante el contexto y el estado del recorrido.

Puede consistir en:

- Mostrar contenido explicativo.
- Recomendar una combinación de productos.
- Recordar el siguiente paso.
- Reconocer el progreso.
- Activar un incentivo.
- Conceder una recompensa.
- Invitar a compartir o recomendar.
- Reactivar una intención que no terminó en compra.

Por ello, no toda intervención es un incentivo. Aportar información sobre composición, función o uso de una prenda puede cambiar el criterio de decisión sin ofrecer ninguna ventaja económica.

## Orquestación

Orquestar significa coordinar elementos distintos para que actúen como un recorrido coherente. En Experiences, la orquestación une:

- Diferentes canales: app, web, POS, QR, tienda o personal.
- Distintos momentos: antes, durante y después.
- Eventos procedentes de sistemas diferentes.
- Reglas de elegibilidad y progresión.
- Contenidos, incentivos y recompensas.
- Objetivos del cliente y objetivos de negocio.

La orquestación no es solamente automatización. Una automatización puede decir “si ocurre X, envía Y”. Una Experience necesita además comprender dónde se encuentra la persona dentro de un recorrido y qué continuidad debe producirse después.

## Reentrada y reactivación

Una Experience no tiene por qué terminar cuando el cliente no realiza la conducta esperada. Puede conservar la intención y preparar una reentrada.

La reactivación no debería ser un recordatorio genérico. Debe utilizar el contexto acumulado:

- Qué exploró la persona.
- Qué pasos completó.
- Dónde abandonó.
- Qué condición todavía puede cumplirse.
- Qué intervención sería ahora relevante.

Esto convierte la ausencia de conversión en un estado del recorrido, no necesariamente en un fracaso definitivo.

## Gamificación y Experiences

La gamificación es un conjunto de técnicas que puede utilizarse dentro de Experiences:

- Retos.
- Marcadores.
- Insignias.
- Niveles.
- Colecciones.
- Rachas.
- Desbloqueos.
- Progreso visual.

Una Experience no tiene que ser gamificada. Del mismo modo, mostrar puntos o una insignia no constituye por sí solo una Experience. La gamificación adquiere sentido cuando representa y refuerza la progresión del recorrido.

## Cupones y Experiences

Un cupón es un instrumento de beneficio o redención. Puede utilizarse como incentivo, recompensa o mecanismo operativo dentro de una Experience.

Un cupón aislado contiene normalmente condiciones de uso, validez, valor y código de canje. Una Experience necesita además contexto, participación, eventos, estado, progresión e intervenciones.

Por tanto:

> Una Experience puede generar, desbloquear o entregar un cupón, pero no debe modelarse simplemente como un cupón con más campos.

## Noticias y Experiences

Una noticia o publicación puede formar parte de una Experience como:

- Descubrimiento inicial.
- Explicación de un reto.
- Comunicación de progreso.
- Recordatorio.
- Reconocimiento.
- Reactivación.
- Narración del impacto conseguido.

La noticia es contenido o canal de intervención. La Experience es el sistema que decide por qué aparece, para quién, en qué momento y qué continuidad ofrece.

## El doble uso de la palabra “experiencia”

Existe una ambigüedad importante. En expresiones como “recibe una experiencia exclusiva de estilismo”, la palabra experiencia designa el beneficio disfrutado: una sesión, actividad o servicio.

Ese beneficio experiencial puede ser el incentivo o la recompensa de una Experience orquestada por Convercus. No son el mismo concepto.

Para evitar confusiones, este documento utiliza:

- **Experiences**: funcionalidad o capacidad de producto de Convercus.
- **Experience**: recorrido concreto configurado y orquestado mediante esa funcionalidad.
- **experiencia del cliente**: vivencia resultante para la persona.
- **beneficio experiencial**: actividad o servicio entregado como beneficio.

## Ejemplo: Desafío Activo

Una posible lectura del Desafío Activo sería:

```text
Objetivo
  Aumentar la participación en actividades deportivas y de bienestar.

Entrada
  Huésped elegible durante su estancia.

Secuencia
  Completar tres actividades.

Eventos verificables
  Validaciones mediante QR, POS o app.

Estado y progresión
  0/3 → 1/3 → 2/3 → 3/3.

Intervenciones
  Mensajes, progreso visual y badges.

Incentivo comunicado
  Spa, smoothie o mejora de bienestar al completar el reto.

Recompensa
  Beneficio concedido automáticamente tras la tercera validación.
```

El spa o smoothie no es la Experience. Es un beneficio utilizado dentro de ella. La Experience es la secuencia completa, incluida su elegibilidad, seguimiento y resolución.

## Ejemplo: Maratón de Temporada

La Maratón de Temporada busca transformar compras aisladas en una progresión entre categorías.

Una compra en zapatos, accesorios o abrigo no se interpreta solamente como una transacción. Se convierte en evidencia de avance dentro de un recorrido. El cliente puede consultar cuánto ha progresado y qué falta para completar la maratón.

El cupón o la sesión de estilismo final son recompensas posibles. El valor diferencial de Experiences está en reconocer las compras, relacionarlas entre sí, mantener el estado y decidir cuándo comunicar el siguiente paso.

## Qué no es Experiences

Con la comprensión actual, Experiences no es únicamente:

- Un gestor de cupones.
- Un constructor de campañas.
- Un sistema de puntos.
- Un catálogo de actividades.
- Una herramienta de notificaciones.
- Una pantalla con retos.
- Una secuencia fija de mensajes.
- Una recompensa experiencial.

Puede utilizar todos esos elementos, pero su función diferencial es orquestarlos alrededor del estado y la evolución de cada participación.

## Consecuencias para la aplicación de demostración

La app debería mostrar Experiences como recorridos activos, disponibles o completados, no como una categoría adicional de cupones.

Una tarjeta resumida podría contener:

- Nombre de la Experience.
- Propósito o promesa.
- Estado de participación.
- Progreso actual.
- Próxima acción.
- Tiempo o condiciones restantes.
- Beneficio potencial, cuando corresponda.

El detalle debería explicar:

- Por qué participa el usuario.
- Qué pasos forman el recorrido.
- Qué eventos ya se han validado.
- Qué alternativas existen.
- Qué debe hacer a continuación.
- Qué incentivos están activos o bloqueados.
- Qué recompensa se ha obtenido.
- Qué ocurre después de completar o abandonar el recorrido.

## Modelo conceptual provisional

Este modelo no presupone todavía la estructura técnica real de Convercus:

```text
ExperienceDefinition
├── propósito
├── audiencia y elegibilidad
├── eventos de entrada
├── pasos y posibles ramas
├── reglas de progresión
├── intervenciones
├── incentivos y recompensas
├── condiciones de finalización
├── reglas de reentrada
└── métricas de éxito

ExperienceParticipation
├── cliente o cuenta
├── estado actual
├── eventos recibidos
├── pasos completados
├── progreso
├── intervenciones realizadas
├── incentivos activados
├── recompensas concedidas
└── siguiente acción
```

La separación entre definición y participación es importante. Una misma Experience puede estar configurada una vez, pero cada cliente necesita su propio estado y recorrido.

## Preguntas todavía abiertas

La comprensión conceptual es consistente, pero siguen abiertas cuestiones que deben contrastarse con producto y tecnología:

1. ¿Experience es el término oficial para cada recorrido configurado o existe otro nombre interno?
2. ¿Qué componentes forman actualmente una Experience dentro del producto?
3. ¿Las secuencias admiten ramas, repeticiones y condiciones “N de M”?
4. ¿Cómo se define la elegibilidad y cómo se inicia una participación?
5. ¿Qué eventos pueden recibirse de forma nativa y cuáles requieren integración?
6. ¿Dónde se guarda el estado individual de progresión?
7. ¿Cómo se distinguen los estados disponible, activa, pausada, completada, caducada y abandonada?
8. ¿Qué relación técnica existe con cupones, newsfeed, transacciones, niveles y segmentos?
9. ¿Qué intervenciones puede ejecutar actualmente el orquestador?
10. ¿Existe una API específica de Experiences que no aparece en el Swagger revisado?
11. ¿Qué métricas utiliza Convercus para medir el éxito de una Experience?
12. ¿El término “Experiences” debe conservarse siempre en inglés en materiales en español?

Estas preguntas no invalidan la definición. Señalan la frontera entre la comprensión conceptual y la especificación real del producto.

## Criterio para resolver futuras ambigüedades

Ante cualquier elemento nuevo, puede utilizarse esta prueba:

1. Si solo ofrece un motivo para actuar, probablemente es un **incentivo**.
2. Si representa el valor concedido tras una acción, probablemente es una **recompensa**.
3. Si registra un hecho observable, es un **evento**.
4. Si expresa dónde se encuentra el cliente, es **estado o progresión**.
5. Si responde al contexto con contenido o una acción, es una **intervención**.
6. Si conecta todos esos elementos en el tiempo y mantiene continuidad, es una **Experience**.

## Síntesis final

Experiences es una funcionalidad de orquestación. Su unidad de sentido no es el cupón, el mensaje ni la recompensa, sino el recorrido.

Los incentivos son instrumentos utilizados dentro de ese recorrido para influir en determinadas conductas. Las recompensas materializan beneficios después de verificar resultados. Los eventos aportan evidencia, la progresión conserva continuidad y las intervenciones permiten responder al momento concreto del cliente.

La experiencia del cliente emerge de esa combinación, pero no se reduce a ninguno de sus componentes.

> **Experiences convierte interacciones aisladas en una trayectoria comprensible y operable, y permite que Convercus intervenga con relevancia a lo largo de ella.**

## Fuentes analizadas

- `Experiencias Canónicas Alimentación Moda.md`
- `Convercus New Generation Loyalty ES.pdf`
- `Convercus_Experiencia_1_Variante_B_GROUPED_MASTER.svg`
