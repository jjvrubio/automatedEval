Yo no construiría todavía un **protocolo general de definición de demostraciones**. Sería demasiado pronto y existe un riesgo claro de repetir justo lo que acabamos de decidir evitar: **generalizar antes de tener presión empírica suficiente**.

La mejor secuencia ahora es **narrativa primero → especificación de una demo concreta → construcción/uso → protocolo derivado de la evidencia**.

S39 nos deja precisamente en ese punto. El cierre establece que la siguiente fase debe elegir destinatario, objetivo narrativo, composición, recorrido, contenido, capacidades y criterios UX, pero advierte que esas decisiones **no implican por sí mismas nueva arquitectura**.   session-39-effective-compositio… Y también establece que una presión sólo debe bloquear la demo si compromete las garantías que esa demo concreta necesita.   session-39-effective-compositio…

### Lo que haría

Tú me das **la primera narrativa como realmente te surgiría en el trabajo**, sin intentar adaptarla a la arquitectura actual ni rellenar una plantilla técnica.

Puede ser algo parecido a:

> «Quiero una demo para una cadena hotelera. La persona que la ve es la responsable de CRM. Quiero que primero experimente el programa como huésped, que se apunte a una experiencia familiar durante la estancia, que incorpore a un segundo participante desde su cuenta, que vaya obteniendo pistas y que al final vea una recompensa. Después quiero poder cambiar de perspectiva y explicar qué está haciendo Convercus por debajo.»

Eso es mucho más valioso ahora que veinte campos perfectamente definidos.

A partir de esa narrativa yo haría una **primera especificación situada**, todavía no un protocolo normativo. Ahí separaríamos, como mínimo:

- **Contexto comercial:** para quién es la demo y qué queremos que comprenda.
- **Destinatario de la demostración:** quién la presencia y desde qué papel.
- **Participante representado:** quién “vive” la Experience dentro de la demo.
- **Historia que queremos contar:** inicio, transformación y desenlace perceptible.
- **Momentos que necesariamente tienen que existir:** no pantallas todavía, sino acontecimientos que queremos experimentar.
- **Comportamientos observables:** qué debe poder hacer el usuario y qué debe ocurrir como consecuencia.
- **Datos/contenidos situados:** marca, personas, establecimiento, Experience, incentivos, recompensa, etc.
- **Capacidades necesarias:** solamente las que la narrativa realmente exige.
- **Perspectiva del creador:** qué queremos poder configurar o cambiar sin programar.
- **Perspectiva del participante:** qué queremos poder desafiar en comprensión, navegación, feedback, continuidad y sentido.
- **Garantías que no podemos sacrificar:** semántica, composición, estado, Evidence/atribución, reproducibilidad.
- **Desconocidos y presiones abiertas:** sin resolverlos todavía; clasificándolos como `BLOCKING`, `NOT BLOCKING` o `TO BE LEARNED BY USING THE DEMO`.

El elemento decisivo es el último.

Por ejemplo, si tu narrativa necesita que P1 incorpore a P2 desde su propia cuenta, sabemos por el trabajo anterior que **eso no autoriza a inventar un Group**. Esa sería una restricción semántica real. Pero si todavía no sabemos si el botón debe llamarse «Añadir participante», «Incorporar acompañante» o cualquier otra cosa, no necesitamos resolverlo arquitectónicamente: **ésa es precisamente una cuestión que queremos poder desafiar mediante UX**. 

### Y sólo después construiría el protocolo

La primera demo nos permitirá distinguir tres tipos de información que ahora serían muy difíciles de anticipar:

**Lo que siempre necesitamos para definir cualquier demo.** Eso acabará formando el núcleo del protocolo.

**Lo que sólo necesitábamos porque era Hospitality/Aventura Familiar.** Eso debe permanecer en la especificación de esa demo y no contaminar el protocolo general.

**Lo que creíamos que había que especificar pero resultó innecesario, o lo que descubrimos demasiado tarde que faltaba.** Ésta será probablemente la evidencia más importante para diseñar el protocolo.

De esta forma el protocolo no nace como una plantilla imaginada por nosotros, sino como una **generalización falsable de la experiencia de construir demos**.

Incluso evitaría inicialmente llamarlo `Demo Definition Protocol`. Lo trataría aproximadamente así:

**Narrativa 1 → Demo Definition v0.1 → construir → observar → corregir**

Después:

**Narrativa 2 → comprobar reutilización de v0.1 → delta necesario**

Y sólo cuando tengamos evidencia de que la estructura sirve para más de una demo materialmente distinta:

**Demo Definition Protocol v1.0**

Esto es exactamente coherente con la transición que acabamos de establecer:

**construir → experimentar → cuestionar → observar → falsar → refinar**, que el cierre de S39 deja expresamente como orientación de la factoría.   session-39-effective-compositio…

Así que **dame la narrativa**. Mejor todavía si me la cuentas como se la contarías a alguien de tu equipo: qué cliente imaginas, qué quieres mostrarle, qué debería experimentar y qué quieres demostrar con ello. **No intentes estructurarla para la Demo Factory.** Nuestro primer experimento como *creadores de demos* será precisamente comprobar si somos capaces de transformar esa intención humana en una especificación ejecutable sin obligarte a pensar como quien diseñó la arquitectura.

---

# primera narrativa

Quiero hacer una demo para una cadena de distribución de moda deportiva. Normalmente, la primera persona de contacto va a ser la responsable de marketing. Aunque, por lo general la responsable de CRM está más cerca del programa de fidelización. Aunque sólo sea por motivos operacionales.

Esta cadena ya tiene un club de fidelización. Quieren vincular sus iniciativas de eventos deportivos a dicho programa. Estos eventos deportivos, se pueden entender como de doble personalidad. Competición para aquellos que aspiran a obtener reconocimiento. Y, presenciales, para aquellos que est´na más cerca del aspecto social y del wellness. Pueden ser eventos discretos que ocurren como si fueran el equivalente de las campñas estilo Black Friday. O, como temporadas., Es decir que se repiten varias veces en un periodo de tiempo. Los clientes que se inscriban podrán recibir insignias por su participación o trofeos en función de los resultados o una combinación de todos los anteriores. Un cliente puede inscribirse en distintos eventos deportivos bajo diferentes modalidad, ya competición, ya wellness, ya social. Esto epodrías gobernado asociando las competiciones a una o distintas Experiencias (estilo Convercus), Para un deportista casual, para  un deportista social, para un competidor. Y, pueden lograr recorridos complementarios: ski, vela, carrera… Un cliente que participa en competición debiera introducir la posición y su resultado. Uno que sólo sea por presencia, un indicador de esfuerzo. Los participantes, no tienen porque ser clientes, sería otra formad e captar. Y, ademas, los participantes podrían formar equipos. YA que habrá eventos de deportes colectivos, por ejemplo: fútbol sala o beach-volley.



---



Sí: tu narrativa ya contiene bastante más de lo que parece. De hecho, **no te pediría que rellenaras una plantilla desde cero**. La convertiría primero en una especificación situada provisional y te preguntaría únicamente por las decisiones que cambian materialmente la demo.

Hay, además, una pequeña ambigüedad que quiero despejar: interpreto «un dictador de esfuerzo» como **un indicador de esfuerzo** —por ejemplo, intensidad o esfuerzo percibido—. Lo marco como pregunta y no lo doy por corregido sin confirmación.

Sí, con esta ampliación ya podemos cerrar bastantes de los 22 puntos y, sobre todo, aparecen dos cuestiones que antes no estaban suficientemente presentes: **participante ≠ cliente** y **participante individual ≠ necesariamente unidad de participación** porque ahora existen equipos.

Eso cambia materialmente la primera especificación situada. No es un detalle funcional: toca identidad, captación, inscripción, pertenencia y atribución de resultados. Pero no voy a resolverlo todavía mediante arquitectura; primero debemos fijar qué quieres que ocurra en la demo.

He rehecho los 22 puntos distinguiendo lo que considero ya respondido y lo que todavía necesito que decidas.

| #      | Dimensión                           | Interpretación actual a partir de tu narrativa               | Lo que todavía necesito de ti                                |
| ------ | ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **1**  | Empresa                             | Cadena de distribución de moda deportiva con club de fidelización ya existente y actividad propia de eventos deportivos. | Sigue abierta una decisión práctica: **¿marca ficticia o una cadena concreta?** Para el primer experimento tendería a ficticia, para no introducir restricciones accidentales. |
| **2**  | Interlocutor de la demo             | Marketing es normalmente puerta de entrada; CRM está más cerca de la operación del programa. La demo debe poder convencer a Marketing sin resultar ingenua para CRM. | ¿Quieres **un único recorrido demostrativo válido para ambos**, o un segundo momento donde cambiemos expresamente a una perspectiva CRM? |
| **3**  | Idea que debe dejar la demo         | Ya está bastante clara: **el club puede extender la relación con el cliente desde la compra hacia la práctica deportiva**, reconociendo motivaciones y modalidades diferentes; además, los eventos pueden actuar como vía de captación de personas que todavía no son clientes. | Me gustaría que confirmes si ésta es la tesis principal o si priorizarías otra. |
| **4**  | Relación participante-cliente       | **No todos los participantes son clientes ni miembros del club.** Tenemos al menos `cliente/miembro` y `participante externo`. Esto invalida mi supuesto anterior de empezar siempre con un miembro identificado. | ¿Un participante externo puede participar sin hacerse miembro del club, o su inscripción al evento debe abrir una oportunidad de alta/captación? |
| **5**  | Inscripción                         | Ahora considero que **sí debe formar parte del modelo de la demo**, porque determina evento, modalidad y quizá relación con el club. | ¿Quieres que la inscripción sea visible en el recorrido del participante? Mi inclinación ahora es **sí**. |
| **6**  | Temporalidad                        | Existen **eventos puntuales** —campañas comparables a Black Friday— y **temporadas** con varias ocurrencias durante un periodo. Ambos son conceptos relevantes. | Para la primera demo: ¿mostramos ambos o elegimos una temporada que contenga varios eventos y, de paso, haga visible también el concepto de evento individual? |
| **7**  | Disciplinas deportivas              | La persona puede participar en distintos deportes: esquí, vela, carrera, fútbol sala, vóley playa, etc. No son meros decorados: permiten recorridos complementarios. | Creo que la demo debería contener **más de una disciplina**, aunque no necesariamente ejecutar todas. ¿De acuerdo? |
| **8**  | Casual / social / competidor        | Ya no los interpretaría como segmentos rígidos de cliente. Son **orientaciones o motivaciones situadas** que pueden gobernarse mediante una o varias Experiences Convercus. | Necesito confirmar el matiz: ¿quieres que existan literalmente Experiences diferenciadas —por ejemplo, *Experiencia Social*, *Experiencia Competición*— o quieres dejar abierta todavía esa correspondencia? |
| **9**  | Variabilidad individual             | **Respondido.** La misma persona puede inscribirse en distintos eventos y hacerlo bajo modalidades diferentes. Por tanto, alguien puede competir en carrera y participar socialmente en vela. `persona != modalidad fija`. | No necesito decisión adicional salvo que quieras restringir combinaciones. |
| **10** | Evidencia de participación          | Hay al menos dos familias distintas: evidencia de **resultado competitivo** y evidencia de **participación/esfuerzo**. | Sigue faltando decidir cómo acreditamos la mera participación: QR/check-in, organizador, dispositivo, autodeclaración, etc. Podemos simular la fuente, pero debemos elegir qué ve el usuario. |
| **11** | Resultado competitivo               | El participante debe introducir **posición y resultado**.    | Punto importante: ¿esa declaración se considera suficiente en la demo o debe existir algún tipo de **validación** posterior por el organizador/sistema? |
| **12** | Indicador de esfuerzo               | Confirmado 😄. Para quien participa sin competir, queremos una señal de esfuerzo en lugar de posición/resultado. | ¿Qué imaginas exactamente: una escala autodeclarada —suave/medio/intenso o 1–10—, tiempo/distancia, datos de wearable, o algo distinto? |
| **13** | Reconocimientos                     | **Insignias** por participación y **trofeos** según resultados, pudiendo combinarse. Esto ya puede darse por establecido en la narrativa. | ¿Alguno de esos reconocimientos debe producir además **beneficio económico o privilegio de fidelización** —puntos, descuento, acceso, experiencia exclusiva— o en esta primera demo basta el reconocimiento? |
| **14** | Acumulación                         | La existencia de temporadas y recorridos complementarios implica que no todo termina en un evento. Puede existir reconocimiento inmediato y progresión acumulada. | ¿Quieres que un trofeo/insignia pueda depender también de una **serie de participaciones**, no sólo de un evento individual? |
| **15** | Relación entre deportes             | Carrera, esquí, vela, etc. pueden construir **recorridos complementarios** dentro de la relación con el club. | ¿Quieres demostrar una meta transversal, por ejemplo «participa en tres disciplinas», o inicialmente cada disciplina progresa independientemente? |
| **16** | Elección de modalidad               | La nueva narrativa aclara bastante esto: **la persona puede inscribirse a un evento bajo una modalidad determinada**: competición, bienestar/social, etc. Por tanto, existe una elección situada y no una clasificación permanente del cliente. | ¿La modalidad la selecciona siempre el participante o el propio evento puede admitir sólo una modalidad? Sospecho que necesitamos ambas posibilidades. |
| **17** | Momento de recompensa               | Tras participar debe existir una consecuencia perceptible: insignia, trofeo y/o progreso. | Necesitamos elegir el **momento principal de satisfacción** de la primera historia que ejecutemos. ¿Cuál debería ser? |
| **18** | Ranking                             | Posición y resultado permiten competición sin que necesariamente exista un ranking general. | ¿Quieres ranking visible entre participantes o, por ahora, sólo resultado personal + reconocimiento obtenido? |
| **19** | Dimensión social                    | Ya es más rica. Social no significa necesariamente grupo TES: puede existir participación social individual, pero además ahora aparecen **equipos reales** en deportes colectivos. | ¿Los equipos deben poder obtener resultados/reconocimientos como equipo, o inicialmente sólo sirven para organizar participantes y los reconocimientos continúan siendo individuales? Esta pregunta es muy importante. |
| **20** | Perspectiva Marketing/CRM posterior | La historia empieza como Experience del participante, pero hay una segunda historia comercial muy natural: mostrar qué ha aprendido el programa sobre participación, preferencias y relación deportiva. | ¿Quieres expresamente un **cambio de perspectiva** después del recorrido del participante para mostrar la visión Marketing/CRM? Yo lo incluiría. |
| **21** | UX del creador de demos             | Ahora ya sabemos mucho mejor qué deberíamos intentar configurar: marca, evento, temporalidad, disciplina, modalidad, Experience, criterios de participación, reconocimientos, clientes/no clientes, equipos y narrativa. | ¿Tu expectativa es que un creador pueda variar **todo esto sin programar**? No digo que hoy pueda hacerse; precisamente queremos comprobarlo. |
| **22** | Alcance de la primera demo          | Ya no creo que una única persona haciendo una única carrera sea suficientemente discriminante. La narrativa contiene heterogeneidad que merece estar presente. | Debemos elegir cuánto contraste incorporar en el primer experimento. Te propongo abajo una configuración concreta para que la confirmes o la cambies. |

### Lo que ha cambiado conceptualmente

Hay tres cosas especialmente importantes.

Primero, **casual/social/competidor no debería convertirse en una propiedad permanente del cliente**. Tu segunda versión prácticamente lo descarta: la persona elige distintas modalidades en distintos eventos. Eso encaja mucho mejor con la idea de que una Experience reconoce una motivación o transformación situada, no que «clasifica» ontológicamente a Juan como *competidor*. 

Segundo, aparece una distinción que tendremos que tratar con mucho cuidado:

**persona → participante → cliente/miembro del club**

no son necesariamente la misma cosa.

Una persona puede participar sin ser cliente. Y precisamente esa participación puede convertirse después en **captación**. Esto me parece comercialmente potentísimo porque la propuesta deja de ser solamente:

> «enriquece el programa de fidelización existente»

y pasa también a ser:

> «convierte la actividad deportiva de la marca en una fuente de relación identificada y potencial adquisición».

Pero no deberíamos fundir prematuramente `participante externo → cliente → miembro del club`. Necesitamos decidir en la demo cuándo y cómo ocurre cada cosa.

Tercero, **los equipos sí constituyen una presión semántica nueva y real**.

Hasta ahora habíamos sido deliberadamente estrictos evitando inferir `Group` de situaciones donde sólo había dos personas colaborando. Aquí la situación es diferente. Un equipo de fútbol sala o vóley playa puede tener **identidad, miembros, inscripción y potencialmente resultados propios**. Ya no estamos hablando simplemente de P1 gestionando a P2.

Esto no significa todavía:

```
equipo deportivo = Group TES
```

Pero significa que por primera vez tenemos una narrativa real que puede exigir una representación colectiva. Éste es exactamente el tipo de presión que queríamos que naciera **de una demo real**, no de especulación arquitectónica. 

### Mi candidato para el primer alcance

Antes de construir la especificación v0.1, yo probaría a condensar toda esta riqueza en una demo que tenga **una temporada deportiva y dos eventos realmente recorribles**.

Uno podría ser una **carrera** que admita dos modalidades. Una participante ya miembro del club se inscribe como competidora, introduce tiempo/resultado/posición y obtiene un trofeo. Otra persona, incluso no cliente, podría inscribirse en modalidad bienestar/social, acreditar presencia + indicador de esfuerzo y obtener una insignia.

El segundo podría ser **vóley playa** o **fútbol sala**, únicamente para introducir la cuestión de los equipos y comprobar qué significa realmente inscribir, participar y reconocer a una unidad colectiva.

Eso nos daría, en una sola demo, cinco contrastes muy valiosos:

**cliente / no cliente · competición / participación · individual / equipo · evento / temporada · reconocimiento inmediato / recorrido acumulado.**

No significa que tengamos que desarrollar cinco sistemas. Significa que la especificación tendría suficiente diversidad para descubrir rápidamente dónde la Factory es realmente configurable y dónde empiezan los supuestos ocultos.

Con tu nueva narrativa, de las 22 preguntas originales yo considero **resueltas o casi resueltas aproximadamente 12–14**. Las que realmente necesito que contestes antes de escribir la **Demo Definition v0.1** son: **1, 2, 4, 6, 8, 10–18, 19–22**, pero muchas admiten una respuesta de una línea. Especialmente críticas son **4, 11, 12, 13, 16 y 19**: participante externo, validación de resultados, naturaleza del indicador de esfuerzo, efecto de los reconocimientos, elección de modalidad y significado del equipo. Esas sí pueden alterar materialmente qué estamos intentando construir.

----

| #      | Dimensión                           | Interpretación actual a partir de tu narrativa               | Lo que todavía necesito de ti                                |
| ------ | ----------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **1**  | Empresa                             | Cadena de distribución de moda deportiva con club de fidelización ya existente y actividad propia de eventos deportivos. | Ficticia                                                     |
| **2**  | Interlocutor de la demo             | Marketing es normalmente puerta de entrada; CRM está más cerca de la operación del programa. La demo debe poder convencer a Marketing sin resultar ingenua para CRM. | Único, Ya hay tiempo para especializar.                      |
| **3**  | Idea que debe dejar la demo         | Ya está bastante clara: **el club puede extender la relación con el cliente desde la compra hacia la práctica deportiva**, reconociendo motivaciones y modalidades diferentes; además, los eventos pueden actuar como vía de captación de personas que todavía no son clientes. | Captación. E,. Inducción a compra de material de categoría superior, o renovaciones. |
|        | Relación participante-cliente       | **No todos los participantes son clientes ni miembros del club.** Tenemos al menos `cliente/miembro` y `participante externo`. Esto invalida mi supuesto anterior de empezar siempre con un miembro identificado. | Un participante externo es  una oportunidad de alta/captación. |
| **5**  | Inscripción                         | Ahora considero que **sí debe formar parte del modelo de la demo**, porque determina evento, modalidad y quizá relación con el club. | Sí                                                           |
| **6**  | Temporalidad                        | Existen **eventos puntuales** —campañas comparables a Black Friday— y **temporadas** con varias ocurrencias durante un periodo. Ambos son conceptos relevantes. | Elegimos una temporada que contenga varios eventos. Y, que haga visible también el concepto de evento individual. |
| **7**  | Disciplinas deportivas              | La persona puede participar en distintos deportes: esquí, vela, carrera, fútbol sala, vóley playa, etc. No son meros decorados: permiten recorridos complementarios. | Tres disciplinas pero vale con ejecutar 1.                   |
| **8**  | Casual / social / competidor        | Ya no los interpretaría como segmentos rígidos de cliente. Son **orientaciones o motivaciones situadas** que pueden gobernarse mediante una o varias Experiences Convercus. | Dejar abierta.                                               |
| **9**  | Variabilidad individual             | **Respondido.** La misma persona puede inscribirse en distintos eventos y hacerlo bajo modalidades diferentes. Por tanto, alguien puede competir en carrera y participar socialmente en vela. `persona != modalidad fija`. | Estupendo.                                                   |
| **10** | Evidencia de participación          | Hay al menos dos familias distintas: evidencia de **resultado competitivo** y evidencia de **participación/esfuerzo**. | Sigue faltando decidir cómo acreditamos la mera participación: QR/check-in, organizador, dispositivo, autodeclaración, etc. Podemos simular la fuente, pero debemos elegir qué ve el usuario. |
| **11** | Resultado competitivo               | El participante debe introducir **posición y resultado**.    | De momento es suficiente.                                    |
| **12** | Indicador de esfuerzo               | Confirmado 😄. Para quien participa sin competir, queremos una señal de esfuerzo en lugar de posición/resultado. | De momento vale con suave/medio/intenso .                    |
| **13** | Reconocimientos                     | **Insignias** por participación y **trofeos** según resultados, pudiendo combinarse. Esto ya puede darse por establecido en la narrativa. | Acceso anticipado a colecciones, invitaciones a sesiones de cómo mejorar, entrevistas con figuras públicas, y también cupones de canje por niveles. |
| **14** | Acumulación                         | La existencia de temporadas y recorridos complementarios implica que no todo termina en un evento. Puede existir reconocimiento inmediato y progresión acumulada. | Dual. Que se reconozca una segunda participación haría de ‘booster’ al entrar en un recorrido ‘Experiencia’ |
| **15** | Relación entre deportes             | Carrera, esquí, vela, etc. pueden construir **recorridos complementarios** dentro de la relación con el club. | De momento independiente.                                    |
| **16** | Elección de modalidad               | La nueva narrativa aclara bastante esto: **la persona puede inscribirse a un evento bajo una modalidad determinada**: competición, bienestar/social, etc. Por tanto, existe una elección situada y no una clasificación permanente del cliente. | Hacen falta ambas pero empezamos con que el participante escoge. |
| **17** | Momento de recompensa               | Tras participar debe existir una consecuencia perceptible: insignia, trofeo y/o progreso. | Insignia; lo sencillo.                                       |
| **18** | Ranking                             | Posición y resultado permiten competición sin que necesariamente exista un ranking general. | Por ahora, sólo resultado personal + reconocimiento obtenido. |
| **19** | Dimensión social                    | Ya es más rica. Social no significa necesariamente grupo TES: puede existir participación social individual, pero además ahora aparecen **equipos reales** en deportes colectivos. | Por ahora, sólo sirven para organizar participantes y los reconocimientos continúan siendo individuales. |
| **20** | Perspectiva Marketing/CRM posterior | La historia empieza como Experience del participante, pero hay una segunda historia comercial muy natural: mostrar qué ha aprendido el programa sobre participación, preferencias y relación deportiva. | Quiero expresamente un **cambio de perspectiva** después del recorrido del participante para mostrar la visión Marketing/CRM. |
| **21** | UX del creador de demos             | Ahora ya sabemos mucho mejor qué deberíamos intentar configurar: marca, evento, temporalidad, disciplina, modalidad, Experience, criterios de participación, reconocimientos, clientes/no clientes, equipos y narrativa. | S¿Tu expectativa es que un creador pueda variar **todo esto sin programar**? No digo que hoy pueda hacerse; precisamente queremos comprobarlo. Sí esta es mi expectativa para el futuro. |
| **22** | Alcance de la primera demo          | Ya no creo que una única persona haciendo una única carrera sea suficientemente discriminante. La narrativa contiene heterogeneidad que merece estar presente. | Conforme con el primer candidato que sugieres par demo.      |