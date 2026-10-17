# Convercus Demo Factory

## Recapitulación integral del proyecto y punto de reanudación

9 de octubre de 2026 · Reconstrucción del trabajo realizado hasta la sesión 38

## 1. Resumen ejecutivo: qué hemos construido y dónde estamos

Convercus Demo Factory nació con un objetivo comercial muy concreto: disponer de una factoría capaz de producir demostraciones personalizadas de Convercus para diferentes prospectos, reutilizando una arquitectura común y evitando desarrollar una aplicación distinta para cada cliente.

El proyecto evolucionó considerablemente desde esa formulación inicial. Lo que comenzó como una inspección de un prototipo React terminó convirtiéndose en un programa de ingeniería de producto gobernado por contratos semánticos, decisiones arquitectónicas explícitas y una metodología de experimentación y falsación.

La idea fundamental que se ha mantenido es:

> Construir una capacidad reutilizable para demostrar cómo Convercus transforma interacciones de clientes en Experiences con progresión, resultados y valor observable, sin confundir la demostración comercial, la semántica del producto y la infraestructura tecnológica.

Sin embargo, encontramos que la dificultad principal no era generar pantallas, sino garantizar que lo que esas pantallas representaban tuviera un significado coherente y que la arquitectura pudiera reproducirlo en diferentes escenarios.

De ahí las 38 sesiones de Codex.

ÚLTIMA SESIÓN DOCUMENTADA

# 38

21 de septiembre de 2026

BASE ARQUITECTÓNICA

# v0.5

ADR-001 a ADR-005 aceptados

VERIFICACIÓN FINAL S38

# 106 / 106

Pruebas superadas, cero fallos

COMPOSICIONES EXISTENTES

# 4

Retail, Arrival, Aventura A y B

Estos resultados no significan que la factoría esté terminada. Significan que tenemos una base técnica experimental verificable, con varias composiciones ejecutables, pero todavía sin acreditar un generador general de demos, integración con la API real de Convercus ni aceptación comercial o visual.

### Una distinción importante sobre las fuentes

He localizado documentación histórica que permite ir más allá de las memorias resumidas de nuestras conversaciones: existe una recopilación de instrucciones originales de las sesiones 01–38, con 35 instrucciones principales recuperadas íntegramente, la sesión 20 parcialmente recuperada y las aperturas originales de las sesiones 18 y 19 todavía pendientes.

También he localizado la arquitectura v0.5 y el documento de estado posterior a S38. Por tanto, podemos reconstruir con bastante fidelidad el método y la progresión del proyecto, aunque no sería correcto afirmar que se dispone de absolutamente cada conversación original o de cada decisión intermedia.

## 2. La concepción del programa: dos productos y una fuente de autoridad

Uno de los resultados estratégicos más importantes fue comprender que estábamos desarrollando dos productos complementarios, no una única aplicación.

TES — Sistema semántico y ontológico

Autoridad sobre significado, relaciones e invariantes de Experience

Contrato semántico de producto

Derivación mínima, controlada y versionada del TES

Convercus App

Producto de participación para el cliente final.

Visualiza situaciones, acciones, progresión, recompensas y resultados.

Experience Builder

Producto de diseño y gobierno para operadores.

Define, simula, valida y configura Experiences.

Activos y contratos compartidos únicamente donde existe una responsabilidad común acreditada.

### Convercus App: prioridad comercial

La App es la superficie mobile-first destinada a mostrar al usuario final los efectos de la plataforma: perfil, membresía, puntos, niveles, cupones, contenidos, intervenciones y participación en Experiences.

Su prioridad era inmediata porque necesitamos demos que un prospecto pueda comprender, utilizar y relacionar con sus objetivos de negocio.

La decisión inicial fue trabajar con datos simulados y avanzar posteriormente hacia la API de staging, no bloquear la presentación comercial hasta tener una integración completa.

### Experience Builder: prioridad estratégica

El Builder responde a un problema diferente: convertir la capacidad de diseñar Experiences en un producto configurable y gobernable.

Debía permitir trabajar con definiciones de Experience, eventos, secuencias, progresión, evidencias, reglas, incentivos, resultados, medición y aprendizaje, así como su traducción a las capacidades ejecutables de Convercus.

Este producto no debía absorber a la App ni convertirse en requisito para la primera demo.

### TES: la frontera que hemos protegido

El TES (Transformational Experience System) proporciona la autoridad semántica. No es simplemente una biblioteca de tipos, una colección de workflows ni un motor de campañas.

La secuencia conceptual que hemos utilizado es:

Event

Pattern

Sequence

Progression

Result

Measurement

Learning

La decisión fue conservar la autoridad ontológica fuera del código del producto. El repositorio debe incorporar traducciones y contratos subordinados, no reinventar o duplicar el TES.

Consecuencia: una colección de acciones no constituye por sí misma una Sequence; un contador no demuestra Progression; una recompensa no equivale necesariamente a Result; y un hecho observado no es automáticamente un TES Event.

Esta distinción explica buena parte de nuestras sesiones posteriores.

## 3. Evolución histórica: de la inspección del prototipo a la primera arquitectura estable

El historial permite dividir el trabajo en grandes etapas, con una transición desde investigación arquitectónica hasta demostraciones ejecutables.

### Etapa I — Sesiones 01–04: comprender antes de construir

Las primeras sesiones estuvieron destinadas a evitar un error habitual en la productización de prototipos: confundir la estructura existente del código con la arquitectura que debería tener el producto.

S01 — Inspección arquitectónica. Codex examinó el repositorio existente: componentes React, fuentes de datos, estado, navegación, branding, fixtures, dependencias y posibles puntos de acceso a Convercus. La conclusión inicial fue que disponíamos de una PWA basada en mocks, pero no de una factoría multicliente plenamente operativa ni de un cliente de API real.

S02 — Anatomía semántica. Se incorporó el TES como referencia y se estudiaron los conceptos `DemoPackage`, `AppSnapshot`, `DataAdapter`, `ExperienceDefinition`, `Scenario`, `DemoScript` y `Activity`.

Las hipótesis fueron contrastadas contra escenarios de retail, aerolíneas, movilidad y hospitality, incluyendo un hotel de negocios y un resort.

S03 — Revisión adversarial. En lugar de aceptar Architecture v0.1, solicitamos a Codex que intentara falsarla.

Se cuestionaron, entre otras, tres ideas: que `DemoPackage` debiera ser la raíz soberana de todo el sistema, que un adaptador universal fuera necesariamente la solución correcta y que la cobertura de una Experience pudiera expresarse mediante un porcentaje general.

La consecuencia fue Architecture v0.2: un diseño más modesto, con mejores fronteras de responsabilidad.

S04 — Decisiones mínimas. Se aceptaron los dos primeros ADR y se diseñó un experimento reversible:

> Two demos. One core. No forks.

Esta fórmula condensaba nuestro propósito: demostrar reutilización real antes de hablar de una factoría general.

### Etapa II — Sesiones 05–08: composición y ejecución

Aquí comenzó la implementación experimental.

S05 introdujo dos composiciones, Retail y Hospitality, sobre el mismo núcleo de aplicación. El objetivo no era producir dos aplicaciones independientes, sino seleccionar configuraciones, datos y recursos diferentes desde un bootstrap compartido.

S06 permitió aceptar la distinción entre composición deseada y composición efectiva.

Esta distinción evita asumir que aquello que solicita un manifest está necesariamente disponible o correctamente resuelto en el runtime.

S07 incorporó una acción pública de demostración en Hospitality, con una transición de llegada controlada por el runtime y reflejada después en los modelos de lectura.

S08 consolidó la separación entre Experience, Scenario y Demo Script.

El resultado fue Architecture v0.4 y cuatro decisiones arquitectónicas aceptadas.

La contribución principal de esta etapa fue establecer que la interfaz debe representar y solicitar acciones, pero no convertirse en autoridad sobre el estado ni sobre la legalidad de las transiciones.

### Etapa III — Sesiones 09–14: evidencia, interpretación y autoridad

Esta etapa contiene algunas de las decisiones epistemológicas más relevantes.

S09 intentó demostrar que una misma evidencia factual podía interpretarse en dos Experiences diferentes. El experimento se detuvo por insuficiencia de definiciones semánticas defendibles.

El STOP fue un resultado correcto: no se inventó una segunda Experience para satisfacer el test.

S10 recurrió al material comercial Convercus New Generation Loyalty ES para identificar Experiences candidatas. Aparecieron tres especialmente relevantes: Aventura Familiar, Desafío Activo y Circuito Sostenible. Se consideraron aptas para investigación con gaps explícitos, no definiciones TES plenamente validadas.

S11 mostró, con evidencia de una actividad Cooking Class, que el mismo hecho podía adquirir distinta relevancia según el contexto de Experience.

S12 introdujo un problema más profundo: la evaluación negativa no siempre es legítima en condiciones de conocimiento incompleto.

En otras palabras:

> Ausencia de prueba no equivale a prueba de ausencia, salvo que la fuente competente permita concluirlo dentro del ámbito examinado.

S13 ensayó una evaluación de mundo abierto, limitada por autoridad y alcance, y S14 consolidó Architecture v0.5 y ADR-005.

Llegamos así a una separación fundamental:

- La evidencia factual registra algo aceptado por una fuente dentro de su alcance.
- El contexto proporciona las condiciones de interpretación.
- La evaluación deriva una afirmación, cuya validez depende de las premisas utilizadas.
- Activity presenta información, pero no crea la verdad del acontecimiento ni la autoridad de la evaluación.

Dos flujos que convergen sin confundirse

Esta arquitectura no contiene un servicio universal de autoridad, ni un motor general de reconocimiento de eventos TES, ni un sistema completo de clasificación semántica. Tales posibilidades permanecen sin resolver porque no fueron demostradas como necesarias.

## 4. Etapa IV — Sesiones 15–20: el nacimiento de «Aventura Familiar»

Aquí abandonamos gradualmente los ejemplos arquitectónicos y empezamos a construir una experiencia que pudiera vivirse.

### La búsqueda del tesoro como instrumento experimental

Elegimos Hospitality / Resort / Aventura Familiar porque obligaba a resolver problemas que un programa convencional de puntos no pone de manifiesto.

En una búsqueda del tesoro pueden existir pistas independientes, participantes distintos, evidencias de procedencia diferente, condiciones de suficiencia y resultados derivados.

S15 demostró que no es suficiente contar hallazgos. Dos conjuntos con la misma cardinalidad pueden tener significados distintos.

El criterio experimental utilizado posteriormente fue:

\[ K=A\land(B\lor C) \]

Es decir, para satisfacer la condición se necesita A y, además, B o C. Dos evidencias A duplicadas no cumplen el criterio, aunque existan dos registros.

Es una regla local del experimento, no una ley universal de Experiences.

### La cuestión de los dos participantes

Este aspecto merece recuperarse con precisión, porque lo discutimos expresamente.

Nuestro escenario contiene dos sujetos individuales, P1 y P2, que pueden participar en una misma búsqueda del tesoro. El segundo participante se habilita desde la cuenta o sesión del primero.

Pero esta operación no constituye por sí misma un Group, una membresía colectiva ni una identidad compartida.

P1 y P2 mantienen sus propias referencias, estados y atribuciones de evidencia.

También establecimos que compartir reserva, estancia o experiencia no proporciona automáticamente autoridad para combinar sus evidencias.

Por eso las sesiones 16–18 se ocuparon de separar atribución, admisibilidad conjunta, suficiencia y validez contextual de un claim derivado.

S17 produjo evidencia suficiente para registrar la presión semántica `PSC-P01`, pero no para modificar el contrato semántico de producto.

### La primera vertical ejecutable

S19 concluyó que existía preparación suficiente, con limitaciones identificadas, para construir la vertical sin esperar una API real, una ontología de Group o un modelo completo de beneficiarios.

S20 conectó:

1. Resolución de la composición Hospitality / Aventura Familiar.
2. Alistamiento explícito de P1.
3. Exploración y registro de Evidence A atribuida a P1.
4. Habilitación de P2, manteniendo su identidad individual.
5. Registro de Evidence B atribuida a P2.
6. Evaluación de admisibilidad y suficiencia conjunta.
7. Proyección de los resultados en las vistas de huésped, Activity y Supervisión.

Un matiz fundamental: alistarse y habilitar a P2 no producen por sí mismos evidencia de haber encontrado una pista.

El primer recorrido reveló, además, un problema real de experiencia de usuario: después de comenzar la aventura, la pantalla no exponía claramente la siguiente acción de exploración. Era posible tener un runtime técnicamente correcto y una demostración prácticamente incomprensible.

Se corrigió esa carencia y el cierre documentado de S20 registró 22 de 22 pasos de aceptación superados en el recorrido establecido.

El veredicto fue:

FIRST VERTICAL DEMO — EXECUTABLE WITH PRESENTATION GAPS.

Ese matiz es esencial. Ya existía una demostración funcional; no se había alcanzado todavía el nivel de presentación y madurez que necesitaríamos para mostrarla como producto comercial terminado.

## 5. Etapa V — Sesiones 21–26: la segunda composición y la falsación de la reutilización

Después de S20 llegó una pregunta decisiva: ¿habíamos construido realmente una factoría o simplemente una demo bien implementada?

Para contestarla, introdujimos una segunda composición de Aventura Familiar, correspondiente a Costa Clara Resort, con marca, contexto, participantes, localizaciones y narrativa diferentes.

El contraste principal fue:

| Dimensión              | A — Aurora        | B — Costa Clara            |
| ---------------------- | ----------------- | -------------------------- |
| Establecimiento        | Aurora Stay       | Costa Clara Resort         |
| Participantes visibles | Lucía / Huésped 2 | Inés / Mateo               |
| Entorno narrativo      | Jardín / fuente   | Mirador / patio            |
| Experience             | Familia Aventura  | Misma familia experiencial |
| Núcleo runtime         | Compartido        | Compartido                 |
| Regla experimental K   | Conservada        | Conservada                 |

La segunda composición se creó como instrumento de falsación de la reutilización arquitectónica, no como una nueva demo comercial aceptada.

### El aprendizaje de S21

S21 quedó falsada.

La nueva composición B podía resolverse, pero no recibía correctamente sus perspectivas iniciales porque una selección interna de comportamiento dependía del identificador de Scenario de A.

Esto era exactamente lo que buscábamos descubrir: un acoplamiento oculto que invalidaba la pretensión de reutilización.

S22 sustituyó el discriminante dependiente del Scenario por una relación existente con Experience. La reparación fue acotada y no exigió crear un registro general de comportamientos.

S23 encontró otro problema: la evaluación seguía utilizando contexto situado que pertenecía a A. La corrección transportó el contexto de Scenario efectivamente resuelto hasta el punto de evaluación.

### El problema de Activity

S24 identificó que parte de la narrativa de Activity procedía de información que no correspondía legítimamente al nuevo escenario.

Sin una relación semántica apropiada, no era legítimo fabricar el texto utilizando otros campos disponibles.

La hipótesis de que bastaban las relaciones existentes quedó falsada.

S25 autorizó una declaración explícita de presentación vinculada al paso de Script, materializada solamente después de que el runtime aceptara la acción.

No se convirtió el Script en autoridad sobre hechos: se le permitió declarar una representación editorial de la acción.

S26 llevó el análisis a las vistas de huésped. Separó tres problemas: cuenta visible, etiquetas de sujetos y narrativa del recorrido. El resultado fue otra falsación parcial: había una fuente de cuenta, pero no relaciones suficientes para generar toda la presentación situada sin introducir ninguna relación nueva.

Resultado de esta etapa: la arquitectura de composición mejoró y quedó sometida a pruebas A/B; sin embargo, la reutilización exigía revisar también las dependencias semánticas y narrativas de los modelos de lectura. 

guia-maestra-sesiones-01-38.md



## 6. Etapa VI — Sesiones 27–35: ordenar la procedencia de lo que ve el usuario

Esta secuencia puede parecer excesivamente detallada vista desde fuera, pero produjo una disciplina de diseño relevante: cada afirmación visible debe tener una fuente apropiada.

Las sesiones se concentraron en responsabilidades pequeñas y explícitas.

| Sesión | Problema abordado            | Decisión o resultado                                         |
| ------ | ---------------------------- | ------------------------------------------------------------ |
| S27    | Etiquetas de participantes   | Introducir presentación situada `subjectRef → label`, sin declarar identidad humana. |
| S28    | Nombre de cuenta             | Derivar `sessionLabel` de la cuenta existente, sin equipararla al sujeto. |
| S29    | Estado del participante      | Representar únicamente el estado operacional: sin alistar, sin habilitar, habilitado. |
| S30    | Mensaje del recorrido        | Seleccionar narrativa situada desde una posición operacional probada. |
| S31    | Introducción de App          | Falsación: la fuente disponible no bastaba para toda la introducción. |
| S32    | Framing introductorio        | Declaración explícita opcional de presentación de composición. |
| S33    | Tarjetas de supervisión      | Usar el identificador operacional del sujeto y no nombres hardcoded. |
| S34    | Etiqueta de sujeto de sesión | Evitar confundir sujeto operacional y cuenta.                |
| S35    | Nombre de Experience         | Procedencia directa de `ExperienceDefinition.name`.          |

La distinción entre sujeto, cuenta, usuario que visualiza y persona que ejecuta una acción fue particularmente importante.

Por ejemplo, el hecho de que P2 sea habilitado desde una sesión gestionada por P1 no permite deducir que toda acción posterior de P2 haya sido físicamente ejecutada por P1.

Igualmente, una etiqueta como «Lucía» o «Mateo» puede ser una declaración presentacional vinculada a un sujeto, pero no acredita una identidad real ni una autenticación.

### Qué ganamos

La aplicación pasó a depender menos de literales propios de Aurora o Costa y a representar de forma más explícita la información que pertenecía a cada composición.

También aprendimos a distinguir los casos donde no hacía falta una relación nueva —bastaba reducir la afirmación— de los casos donde sí se necesitaba una declaración adicional para la presentación.

Eso evitó construir prematuramente un gran Presentation Model o una capa universal de identidad.

### Qué no demostramos

La verificación de procedencia no garantiza por sí misma una buena experiencia de usuario.

Un texto puede provenir del artefacto correcto y seguir resultando poco comprensible, poco atractivo o comercialmente irrelevante.

Esta limitación sería decisiva al concluir la sesión 39.

## 7. Etapa VII — Sesiones 36–38: autoridad narrativa e integridad de la evidencia

### S36 — Una falsación de gran interés epistemológico

Intentamos auditar exhaustivamente la autoridad de las afirmaciones visibles.

Aparecieron dos expresiones especialmente problemáticas en Activity:

- «Por ti».
- «Desde tu cuenta».

La aplicación no tenía autoridad suficiente para identificar al ejecutor humano de la acción ni para atribuirle necesariamente la cuenta utilizada.

S36 quedó falsada en su pretensión exhaustiva.

No significaba que todos los avances anteriores fueran incorrectos. Significaba que algunas afirmaciones de presentación superaban la autoridad de sus fuentes.

### S37 — Reducir la afirmación al hecho acreditable

La respuesta no fue crear inmediatamente un nuevo modelo de actor, viewer, ejecutor y cuenta.

Primero ensayamos una alternativa más parsimoniosa: eliminar lo que no podíamos justificar y conservar la información factual legítima.

Por ejemplo:

> Hallazgo registrado.

O bien:

> Hallazgo atribuido a Mateo.

Las expresiones ya no pretenden saber quién pulsó el botón, quién estaba físicamente presente o desde qué cuenta se ejecutó la acción.

El resultado fue favorable dentro del alcance ensayado y preservó la narración situada introducida previamente.

Esta sesión me parece ilustrativa de nuestra metodología: en determinados casos, reducir la afirmación tiene mayor rigor y menor coste estructural que aumentar la ontología.

### S38 — Recuperar los instrumentos de verificación

S37 había terminado con 95 pruebas superadas y tres fallos ambientales en las reproducciones históricas H21–H23.

El problema concreto era la ausencia de un archivo `.DS_Store` cuya existencia se había incorporado indebidamente al inventario material de preservación.

S38 investigó si era posible separar los archivos ambientalmente incidentales de las fuentes necesarias para verificar los resultados históricos.

La sesión introdujo una clasificación acotada, ensayó la ausencia y presencia de esos metadatos y mantuvo la detección de modificaciones materiales.

Cierre técnico de S38

Verificado localmente

# 106

Tests PASS

# 0

Tests FAIL

# 31

Archivos de test

Typecheck, lint y build también pasaron. Se conservaron las falsaciones históricas y no se modificó el comportamiento productivo para reparar los tests.

La auditoría actual de S37 dentro de aquella ejecución incluía 14 recorridos App, 77 frames y 231 capturas DOM. Eso representa un grado relevante de cobertura de comportamiento, pero no sustituye una inspección humana de la experiencia visual. 

session-38-historical-replay-portability-evidence-integrity.md



## 8. La sesión 39: el verdadero cierre de la última etapa

22 de septiembre de 2026 · Consolidación el 23 de septiembre

Al ampliar la consulta documental más allá de la recopilación de sesiones 01–38, he localizado `session-39-effective-composition-navigation-identity.md`, que actualiza nuestro último estado conocido.

Por tanto, la cifra 38 con la que abrí la recapitulación corresponde al último bloque del archivo histórico inicial, no a la última sesión efectivamente realizada.

### Qué se investigó

Se sospechaba que la navegación de Costa Clara podía conducir incorrectamente a la composición Aurora, debido a un enlace literal presente en Home.

La sesión distinguió dos proposiciones:

P39 — Supuesto del problema. Desde Family Adventure B, el usuario era dirigido a A y se necesitaba una reparación.

H39 — Hipótesis de suficiencia. La identidad efectiva disponible ya bastaba para conservar A→A y B→B en la navegación seleccionada.

### Resultado

P39

Falsada

El supuesto defecto B→A no pudo reproducirse en la superficie investigada.

H39

Apoyada con reservas

La navegación específica de las dos aventuras conservó su identidad y estado en los recorridos ensayados.

El enlace literal existía, pero pertenecía a la Home genérica de Retail y Arrival, desde donde se utilizaba para entrar en Aventura Familiar A.

Las aventuras A y B ya disponían de una navegación propia mediante «Mi aventura», que conservaba la composición efectiva.

En consecuencia, Codex no efectuó una reparación de producto. Se detuvo en el control previo al cambio, evitando resolver un problema que no se reproducía.

La sesión añadió pruebas de la hipótesis local y terminó con:

# 113 / 113

Pruebas superadas en S39

# 0

Cambios productivos

La verificación de navegación se realizó en DOM/jsdom, con reconstrucción explícita para algunas recargas, no mediante una sesión visual de navegador nativo. La aceptación humana quedó sin ejecutar. 

session-39-effective-composition-navigation-identity(1).md



### La decisión más importante de S39 no fue técnica

La consolidación incorporó un cambio de orientación que considero central para nuestra reanudación:

> Las presiones abiertas no son automáticamente impedimentos para construir una demo.

El trabajo anterior había aplicado con éxito la falsación sobre problemas arquitectónicos potenciales. Sin embargo, continuar identificando riesgos sin exponer el producto a usuarios podía impedirnos obtener evidencia de mayor valor.

S39 propuso pasar progresivamente del análisis arquitectónico preventivo a ciclos de construcción, interacción y observación.

Separó además dos fuentes de aprendizaje:

Demo-author UX: la experiencia de quien configura la demostración, descubre dependencias, reutiliza artefactos y necesita modificar código.

Participant UX: la experiencia de quien utiliza la demo, comprende las acciones, recibe feedback, reconoce consecuencias y percibe el valor.

No son intercambiables. Una factoría puede ser cómoda para sus desarrolladores y producir demos deficientes; también puede generar una demo excelente mediante un proceso de autoría demasiado costoso para escalar.

La formulación resultante fue:

Composición pequeña demostrable → interacción humana → presión observada → hipótesis acotada → experimento.

Se cerró S39 sin abrir H40, pero con una orientación inequívoca hacia la producción de demostraciones útiles. 

session-39-effective-composition-navigation-identity(1).md



## 9. El último frente de trabajo localizado: Sports Season

23 de septiembre de 2026 · Revisión de viabilidad y especificación mínima

Esta es la continuación más reciente que he encontrado en la documentación del proyecto.

Después de S39 aparece una nueva propuesta de demostración, Sports Season, con dos documentos principales:

- `sports-season-safe-to-build-review.md`
- `sports-season-smallest-buildable-slice.md`

No es una sesión H40 ni una demo implementada. Es un estudio de viabilidad seguido de una especificación concreta para construir la siguiente vertical.

### Qué pretende demostrar

El escenario plantea una marca ficticia relacionada con el deporte y un club que organiza una temporada de actividades: Carrera, Vela y Vóley playa.

El caso se centra en una persona que todavía no pertenece al club. Participa en una carrera, registra información de su participación, recibe reconocimiento y descubre una oportunidad de vincularse comercialmente con la marca.

La lógica del recorrido propuesto es:

1. Explorar la temporada

   Carrera, Vela y Vóley playa como eventos diferenciados.

2. Inscribirse en Carrera

   Elegir modalidad Social o Bienestar y confirmar la inscripción.

3. Registrar presencia

   Check-in simulado, sin afirmar verificación física real.

4. Declarar esfuerzo

   Elegir suave, medio o intenso; registrar el dato como autodeclaración.

5. Obtener reconocimiento

   Conceder una insignia individual con un motivo explícito y evidencias referenciadas.

6. Descubrir la oportunidad comercial

   Presentar una invitación a conocer el club, sin simular automáticamente un alta.

7. Cambiar a Marketing/CRM

   Examinar cómo la misma participación genera información y una oportunidad de relación comercial, conservando el estado.

### Por qué es un buen siguiente experimento

Aventura Familiar estaba centrada principalmente en la suficiencia de evidencia, la atribución y la presentación.

Sports Season introduce otro conjunto de restricciones útiles:

- Una persona puede participar sin ser miembro ni cliente.
- La inscripción no constituye presencia efectiva.
- La presencia no equivale a esfuerzo.
- El esfuerzo autodeclarado no constituye un resultado deportivo medido.
- Una insignia no es un cupón ni un beneficio económico.
- Una invitación comercial no acredita consentimiento, conversión ni alta.
- El cambio de perspectiva hacia CRM no debe inventar nuevos hechos.

Es un escenario más próximo a la relación entre participación, reconocimiento y activación comercial.

### Qué concluyó la revisión

El resultado fue SAFE TO BUILD, con código funcional nuevo todavía pendiente.

La arquitectura existente ofrece responsabilidades reutilizables: composición, resolución, frontera pública de acciones, estado, proyecciones y aislamiento.

Pero la demo deportiva exige implementar piezas nuevas: inscripción con modalidad, sujeto externo, check-in, esfuerzo, política de insignia, oportunidad comercial y proyección CRM.

No puede construirse simplemente cambiando el nombre de una Experience o añadiendo otro manifest.

El documento insiste en que la regla de insignia es una política de producto situada, no una demostración de Progression o Result bajo TES. Tampoco permite hacer pasar la Experience candidata «Desafío Activo» por una Experience deportiva validada. 

sports-season-safe-to-build-review.md

sports-season-smallest-buildable-slice.md



### Estado de Sports Season

| Elemento                                   | Situación documentada        |
| ------------------------------------------ | ---------------------------- |
| Revisión de viabilidad                     | Completada                   |
| Corte mínimo de construcción               | Especificado                 |
| Composición deportiva ejecutable           | No acreditada                |
| Inscripción, check-in, esfuerzo e insignia | Pendientes de implementación |
| Vista Marketing/CRM deportiva              | Pendiente                    |
| Pruebas y aceptación del recorrido         | No ejecutadas                |
| H40                                        | No abierta                   |

Además, la revisión intentó ejecutar la suite, pero encontró un problema de firma nativa de Rolldown antes de iniciar los tests. Por tanto, los 113 tests superados corresponden al cierre de S39; no debe presentarse esa cifra como una nueva validación de Sports Season.

## 10. Estado consolidado del sistema

Al reunir los expedientes de las 39 sesiones y la especificación deportiva, este es el inventario que considero más útil.

| Dominio                       | Estado                         | Interpretación                                            |
| ----------------------------- | ------------------------------ | --------------------------------------------------------- |
| TES                           | Autoridad preservada           | No se ha subordinado al código.                           |
| Product Semantic Contract     | Sin modificación adicional     | Derivación semántica controlada.                          |
| Architecture v0.5             | Activa                         | Base arquitectónica consolidada.                          |
| ADR-001 a ADR-005             | Aceptados                      | Fronteras de responsabilidad establecidas.                |
| Composición multídemo         | Demostrada con reservas        | Variantes sobre maquinaria común.                         |
| Runtime y acciones públicas   | Demostrados en casos concretos | No es motor universal de Experiences.                     |
| Evaluación contextual         | Experimental y acotada         | No equivale a reconocimiento TES general.                 |
| Aventura Familiar A           | Ejecutable                     | Primera vertical con aceptación de recorrido documentada. |
| Aventura Familiar B           | Experimental                   | Instrumento de reutilización, no demo comercial aceptada. |
| Sports Season                 | Especificada, no implementada  | Candidata para siguiente construcción.                    |
| Integración Convercus API     | No acreditada                  | Predominan mocks y estado local.                          |
| Experience Builder operativo  | No acreditado en esta Factory  | Sigue siendo objetivo estratégico separado.               |
| Generador arbitrario de demos | No demostrado                  | La composición requiere trabajo técnico situado.          |
| Aceptación comercial/visual   | Pendiente                      | No sustituible por suites verdes.                         |

### Las cinco decisiones arquitectónicas aceptadas

001

Bounded TES Semantic Authority

TES gobierna significado e invariantes; no decide automáticamente APIs, servicios, almacenamiento, despliegue o implementación.

002

Logical Separation of Composition, Runtime and Read Models

Separa configuración, comportamiento/estado y presentación.

003

Desired vs Effective Demo Composition

Distingue lo solicitado de lo realmente resuelto y disponible.

004

Experience / Scenario / Demo Script Separation

Evita que la narrativa o el guion de presentación gobiernen las transiciones del producto.

005

Neutral Evidence and Authority-Bounded Contextual Evaluation

La evaluación depende de evidencia y premisas competentes, sin convertir ausencia de conocimiento en negativo ni Activity en autoridad.

### Presiones todavía abiertas

La presión semántica `PSC-P01`, relacionada con la composición y admisibilidad de evidencia entre sujetos, continúa abierta y respaldada por evidencia. No se creó `PSC-P02` y no se introdujo una ontología de Group para resolver artificialmente el escenario de P1/P2.

También persisten limitaciones del entorno de pruebas, de la infraestructura de replay, de la autoría de demos y de la presentación. Algunas podrían necesitar tratamiento posterior; ninguna debe considerarse automáticamente bloqueante para todas las demostraciones.

## 11. Cómo hemos trabajado con Codex: el método que debemos preservar

Este aspecto es especialmente importante porque en nuestros últimos intercambios me pediste expresamente que recuperara el patrón seguido al formular instrucciones para Codex, en lugar de inventar un procedimiento nuevo.

El archivo recuperado de instrucciones originales y la guía maestra confirman una metodología bastante consistente, que fue ganando precisión con el tiempo.

El ciclo fundamental es:

Hipótesis

Falsación

Experimento

Evidencia

Evaluación

Consolidación

La promoción a arquitectura o contrato es eventual, nunca automática.

Cada instrucción madura a Codex tenía que establecer una baseline recibida, fuentes autorizadas, hipótesis, variable examinada, constantes, controles positivos y negativos, falsadores, condiciones STOP, archivos congelados, delta permitido y resultados exigidos.

No todas las sesiones permitían implementar. Algunas eran exclusivamente análisis, otras consolidación documental y otras experimentos ejecutables.

### Las reglas metodológicas que resultaron más valiosas

Primera: un hallazgo no es una decisión arquitectónica. Que aparezca una dependencia problemática no significa que debamos crear inmediatamente una abstracción general.

Segunda: falsación no significa fracaso del proyecto. S21, S24, S26, S31 y S36 fueron útiles precisamente porque invalidaron hipótesis y permitieron localizar fronteras reales.

Tercera: no perseguir pruebas verdes a cualquier precio. Un test puede demostrar correctamente que una hipótesis fue falsada. No se deben modificar expectativas históricas para eliminar ese resultado.

Cuarta: conservar separados los estados de autoridad. Un experimento respaldado no transforma automáticamente su implementación, sus tipos o su vocabulario en contratos generales.

Quinta: mantener trazabilidad de procedencia. La autoridad de una descripción editorial no se confunde con la autoridad de Evidence o con una identidad humana autenticada.

Sexta: preservar la historia del repositorio. Cada delta tiene alcance delimitado; las evidencias antiguas no se reescriben para acomodar el comportamiento actual.

Séptima: distinguir las distintas clases de validación. Tests unitarios, DOM, navegador visual, dispositivo real y aceptación comercial son niveles diferentes.

Octava: la siguiente sesión no se abre automáticamente. El cierre registra el resultado y las presiones observadas; la elección del nuevo objetivo corresponde a una decisión posterior.

Esta última regla sigue vigente después de S39. 

guia-maestra-sesiones-01-38.md

instrucciones-originales-sesiones-01-38(1).md



## 12. Dónde recomiendo reanudar el trabajo

Considero que hemos alcanzado un cambio de fase. Hasta ahora hemos invertido una cantidad considerable de esfuerzo en evitar que la factoría se apoyase en relaciones semánticas ficticias y acoplamientos técnicos ocultos.

Ese trabajo tiene valor. Pero la hipótesis comercial original sigue sin haber sido suficientemente contrastada: ¿podemos producir demostraciones convincentes para prospectos distintos, con un esfuerzo marginal razonable, manteniendo el núcleo común?

La mejor forma de investigarlo ya no es únicamente auditar código. Es construir y utilizar demostraciones.

### Mi propuesta de continuación

Primero — Recuperar la aplicación ejecutable

Arrancar las cuatro composiciones documentadas y observar su comportamiento, sin efectuar inicialmente modificaciones de producto. Verificar entorno y regresiones, y revisar de forma humana Aventura Familiar A y Costa B.

La guía documenta el directorio `products/convercus-app/prototype`, el requisito Node 24 o superior y los comandos `npm run dev` y `npm run check`. Esos comandos constituyen el procedimiento histórico, no una ejecución que haya realizado hoy.

Segundo — Observar la experiencia como usuario

Comprobar si una persona entiende qué es la aventura, cómo se alista, qué acción sigue, cómo habilita P2, cómo registra evidencias y qué resultado obtiene. Registrar las fricciones, diferenciando UX de participante y UX de autor.

Tercero — Iniciar la construcción acotada de Sports Season

Tomar `sports-season-smallest-buildable-slice.md` como especificación candidata y formular una instrucción BUILD para Codex. Exigir el recorrido mínimo completo, con código situado y pruebas nuevas, sin alterar retrospectivamente los resultados anteriores.

Cuarto — Evaluar por primera vez la productividad de la factoría

Medir lo que realmente nos interesa: qué componentes se reutilizan, cuáles requieren configuración, dónde hay que escribir código, cuántas dependencias inesperadas aparecen y cuánto esfuerzo cuesta convertir un objetivo comercial en una experiencia demostrable.

Una vez comprobado lo anterior, podremos formular una hipótesis más sólida sobre la productización de la factoría y sus próximos contratos funcionales. No recomendaría abrir otra gran revisión arquitectónica antes de obtener esa evidencia de construcción y uso, salvo que se identifique un bloqueo material concreto.

## 13. Mi conclusión

La trayectoria desde S01 hasta S39 muestra tres aprendizajes acumulativos.

Primero, la separación semántica era indispensable. Sin ella habríamos construido una colección de pantallas con contadores, recompensas y actividades etiquetadas como Experiences, sin garantizar que representaran realmente el producto diferencial de Convercus.

Segundo, la reutilización necesita probarse en composiciones distintas. La experiencia B/Costa demostró que compartir componentes React no es suficiente cuando la selección de comportamiento, el contexto o la narrativa siguen dependiendo implícitamente de A.

Tercero, el rigor experimental empieza a producir rendimientos decrecientes si no se contrasta con uso real. Ese es precisamente el cambio reconocido en la consolidación de S39.

La pregunta que ahora debe orientar nuestras decisiones ya no es solamente si podemos preservar la arquitectura. Es si somos capaces de utilizar esa arquitectura para producir Experiences demostrables, inteligibles y comercialmente relevantes, con rapidez y control.

Mi recomendación es recuperar Aventura Familiar como referencia funcional y avanzar después hacia Sports Season como primer ejercicio deliberado de construcción de una nueva vertical.

No necesitamos repetir las 39 sesiones. Necesitamos aprovechar lo que demostraron.

Y hay algo más que conviene no perder de vista: el objetivo original no era construir un laboratorio de validación semántica. Era construir una factoría de demos. El laboratorio fue un medio para asegurar sus fundamentos. Ahora corresponde empezar a comprobar que esos fundamentos sirven al propósito comercial.

Alcance de la reconstrucción: he contrastado el historial de conversaciones disponible, la memoria contextual y los documentos recuperables del proyecto. He encontrado originales íntegros de 35 instrucciones principales, informes de las sesiones 18–20 que permiten reconstruir sus decisiones, la sesión 39 consolidada y la documentación Sports Season del 23 de septiembre. No he verificado hoy el repositorio mediante ejecución ni puedo certificar que no haya cambios locales posteriores a esa fecha. Esta recapitulación distingue deliberadamente estado documentado de estado ejecutado en tiempo real.