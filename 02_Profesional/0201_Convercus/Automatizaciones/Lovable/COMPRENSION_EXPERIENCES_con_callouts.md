# Comprensión conceptual de Experiences en Convercus

## Propósito de este documento

Este documento recoge una comprensión de trabajo sobre **Experiences**, la funcionalidad de Convercus destinada a orquestar experiencias de cliente. Está escrito para poder leerse de forma continua, revisar el razonamiento y detectar términos que todavía necesiten precisión.

No pretende sustituir una especificación funcional ni describir una API. Su función es establecer un lenguaje común antes de diseñar pantallas, modelos de datos o integraciones.

## Punto de partida

En Convercus, **Experiences** es el nombre en inglés de una funcionalidad de producto. Su propósito es orquestar experiencias en el sentido amplio y original de la palabra: algo que una persona atraviesa, vive y acumula a lo largo de un recorrido.

> [!warning] Desviación — experiencia reducida a recorrido y acumulación
> Esta formulación capta la vivencia y la continuidad, pero resulta insuficiente para explicar cómo Convercus desarrolla una experiencia. Una Experience no se define porque una persona «acumule» acciones o beneficios, sino porque configura una **transformación situada reconstruible**. La acumulación puede existir, pero solo constituye progresión cuando expresa desplazamiento entre estados, hitos o umbrales. La cadena mínima que debe poder recuperarse es: **evento → patrón → secuencia → progresión → resultado → medición → aprendizaje**.

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

> [!warning] Desviación — resultado confundido con orientación deseada
> Convercus puede orientar el recorrido hacia un resultado previsto, pero el **resultado** no es aquello que se desea, promete o programa. Es el estado o efecto efectivamente producido por la secuencia y su progresión. Conviene distinguir aquí entre **objetivo de diseño**, **condición de finalización** y **resultado observado**.

Una **Experience** concreta sería, por tanto, una configuración operativa de ese recorrido. La **experiencia del cliente** es lo que la persona vive como resultado de atravesarlo.

> [!warning] Desviación — la Experience no es solo la configuración del recorrido
> La configuración operativa es una parte necesaria, pero no agota la Experience. Para que el recorrido opere como experiencia debe existir un campo de mediación reconocible, al menos un evento significativo, un patrón emergente, una secuencia, progresión, resultado distinguible, medición compatible y aprendizaje reutilizable. De lo contrario puede haber un flujo de trabajo, una campaña o una secuencia automatizada, pero no una experiencia plenamente reconstruible.

## Una formulación breve

> **Experiences es la capacidad de Convercus para convertir eventos dispersos del cliente en recorridos con contexto, estado, progresión e intervenciones coordinadas.**

> [!important] Precisión necesaria — falta la transformación completa
> La formulación es útil como entrada pedagógica, pero queda incompleta como definición operativa. No basta con coordinar eventos y mantener estado: Convercus desarrolla Experiences al **reconocer regularidades o patrones**, ordenar una secuencia, producir progresión, obtener un resultado contrastable y convertir la medición en aprendizaje reutilizable.

Esta formulación contiene la diferencia fundamental frente a un incentivo aislado. Experiences no se limita a provocar una acción: organiza la continuidad entre varias acciones, decisiones y momentos.

## Experiencia vivida y funcionalidad Experiences

Conviene separar dos planos.

En el plano humano, una experiencia es el recorrido vivido por una persona. Incluye lo que encuentra, interpreta, decide, hace y recibe. Puede comenzar con una necesidad poco definida y terminar en una compra, un aprendizaje, una participación, una relación más fuerte con la marca o una futura reactivación.

> [!warning] Desviación — cierre enumerativo de posibles finales
> Una experiencia no se valida porque termine en cualquiera de estos elementos. Compra, participación, aprendizaje o reactivación pertenecen a planos distintos y deben distinguirse. El cierre correcto exige identificar **qué cambio de estado produjo realmente la secuencia**, cómo se midió y qué aprendizaje dejó. Una compra puede ser evento, hito o resultado según la arquitectura concreta; no posee un estatuto fijo por sí misma.

En el plano del producto, Experiences es el sistema que hace operable ese recorrido. No “fabrica” directamente la vivencia subjetiva, pero coordina las condiciones que permiten acompañarla:

```text
Señales + contexto + eventos + reglas + estado + intervenciones
                              ↓
                 experiencia orquestada
```

> [!warning] Desviación — cadena de desarrollo incompleta
> Este esquema describe los insumos de orquestación, pero omite la operación experiencial que permite reconstruir el desarrollo. Entre los eventos y la experiencia no hay un salto directo: deben hacerse legibles el **patrón**, la **secuencia**, la **progresión**, el **resultado**, la **medición** y el **aprendizaje**.

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

> [!warning] Desviación — observabilidad insuficiente para definir evento
> No todo hecho observable constituye un evento en sentido experiencial fuerte. Para operar como evento debe inaugurar, alterar o aportar una diferencia relevante a la dinámica de la Experience. Un inicio de sesión, una visita o un escaneo pueden registrarse sin producir progreso ni cambio de estado; su función depende de las reglas y de la secuencia en la que se inscriben.

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

> [!warning] Desviación — progresión reducida a persistencia o acumulación
> Mantener memoria y continuidad es necesario, pero no suficiente. La progresión exige un **avance reconocible entre estados, hitos o umbrales**. Un saldo persistente, una lista creciente de acciones o la mera conservación del historial pueden existir sin que haya progresión significativa.

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

> [!note] Precisión — evitar atribución cognitiva antropomórfica
> En términos operativos, Convercus no necesita «comprender» como un sujeto. Necesita **resolver el estado de participación** a partir de eventos, contexto, reglas y patrones disponibles, y determinar la intervención compatible con ese estado. Esta formulación mejora la trazabilidad entre capacidad de producto y comportamiento del sistema.

## Reentrada y reactivación

Una Experience no tiene por qué terminar cuando el cliente no realiza la conducta esperada. Puede conservar la intención y preparar una reentrada.

> [!warning] Desviación — la intención no debe tratarse como estado directamente conservable
> Convercus puede conservar señales, contexto, eventos, estado, pasos completados o condiciones pendientes. La **intención** pertenece al plano de orientación de la acción y no debe presentarse como dato persistido salvo que exista una operacionalización explícita. Para reentrada conviene hablar de conservar **trazas de la intención o del recorrido incompleto**, no la intención misma.

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

> [!note] Precisión léxica
> En documentación general en español, el término preferente del TES es **TPV**; `POS` puede mantenerse entre paréntesis cuando el contexto técnico lo requiera.

Estado y progresión
  0/3 → 1/3 → 2/3 → 3/3.

Intervenciones
  Mensajes, progreso visual y badges.

> [!note] Precisión léxica
> En español funcional conviene usar **insignias** como forma principal y reservar *badges* para interoperabilidad o documentación técnica.

Incentivo comunicado
  Spa, smoothie o mejora de bienestar al completar el reto.

Recompensa
  Beneficio concedido automáticamente tras la tercera validación.
```

El spa o smoothie no es la Experience. Es un beneficio utilizado dentro de ella. La Experience es la secuencia completa, incluida su elegibilidad, seguimiento y resolución.

> [!warning] Desviación — Experience equiparada a secuencia completa
> La secuencia es una unidad estructural de la Experience, no su totalidad. En este ejemplo faltan todavía el **patrón** que justifica el reto, el **resultado efectivo** más allá de completar 3/3, la **medición** del cambio producido y el **aprendizaje** reutilizable. Elegibilidad, seguimiento y resolución describen operación, pero no sustituyen la cadena experiencial completa.

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

> [!warning] Desviación de aplicación — interfaz centrada en objeto y estado, no necesariamente en transformación
> Esta propuesta es plausible para una demostración, pero no debe fijarse como traducción necesaria de la capacidad. Mostrar Experiences como tarjetas «activas, disponibles o completadas» puede reducirlas a objetos de catálogo. La interfaz debería hacer visible, según el caso, la **situación de entrada**, el patrón relevante, el cambio de estado, la próxima acción y el resultado que se está construyendo, sin convertir toda Experience en un reto explícito para el usuario.

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

> [!warning] Desviación — modelo conceptual sin patrón ni aprendizaje
> El modelo separa correctamente definición y participación, pero reproduce una arquitectura de flujo de trabajo. Para representar cómo Convercus desarrolla experiencias debe incorporar, al menos, la lógica o hipótesis de **patrón**, la definición del **resultado observable**, la relación entre resultado y **medición**, y la captura de **aprendizaje** para reutilización o ajuste de futuras configuraciones. «Métricas de éxito» no sustituye estos elementos.

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

> [!warning] Desviación — prueba de clasificación demasiado permisiva
> Conectar eventos, estados e intervenciones en el tiempo permite reconocer una orquestación, pero no basta para declarar una Experience. La prueba debe exigir también: **patrón reconocible, secuencia con progresión, resultado distinguible de la promesa, medición compatible y aprendizaje reutilizable**. Sin esos elementos, una automatización compleja podría clasificarse erróneamente como Experience.

## Síntesis final

Experiences es una funcionalidad de orquestación. Su unidad de sentido no es el cupón, el mensaje ni la recompensa, sino el recorrido.

Los incentivos son instrumentos utilizados dentro de ese recorrido para influir en determinadas conductas. Las recompensas materializan beneficios después de verificar resultados.

> [!note] Precisión — la recompensa sigue a una condición, no necesariamente al resultado experiencial
> Una recompensa suele concederse después de verificar una conducta, logro, umbral o condición. Esa concesión puede ser un evento o un hito dentro de la Experience y no equivale necesariamente al resultado final de la transformación. Los eventos aportan evidencia, la progresión conserva continuidad y las intervenciones permiten responder al momento concreto del cliente.

La experiencia del cliente emerge de esa combinación, pero no se reduce a ninguno de sus componentes.

> **Experiences convierte interacciones aisladas en una trayectoria comprensible y operable, y permite que Convercus intervenga con relevancia a lo largo de ella.**

> [!important] Reformulación de cierre recomendada
> **Experiences es la capacidad de Convercus para configurar y operar transformaciones situadas: reconoce eventos significativos y patrones, los ordena en secuencias con progresión, coordina intervenciones según el estado de cada participación y permite distinguir resultado, medición y aprendizaje.**

## Fuentes analizadas

- `Experiencias Canónicas Alimentación Moda.md`
- `Convercus New Generation Loyalty ES.pdf`
- `Convercus_Experiencia_1_Variante_B_GROUPED_MASTER.svg`
