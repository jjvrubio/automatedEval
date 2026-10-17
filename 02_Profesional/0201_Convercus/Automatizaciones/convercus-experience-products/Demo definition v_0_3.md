---
title: "Definición de demo — Temporada deportiva de fidelización"
author: "Juan Vázquez"
date: "2026-09-24"
lang: "es"
doc_class: "especificaciones"
status: "borrador"
version: "0.3"
content_id: "CDF-SPORTS-SEASON-DEMO-DEFINITION"
content_series: "Convercus Demo Factory — Definiciones de demo"
project: "Convercus Demo Factory"
source_of_truth: "markdown-obsidian"
supersedes: "Demo definition v_0_2.md"
revision_note: "Incorpora los aprendizajes de la primera revisión humana del plano de usuario. La perspectiva Marketing/CRM permanece pendiente de revisión específica."
---

# Definición de demo — Temporada deportiva de fidelización

Esta definición describe una demo concreta para una empresa ficticia de distribución de moda y equipamiento deportivo.

No describe todavía una capacidad general de Convercus Demo Factory.

No debe utilizarse para inferir que cualquier elemento aquí representado existe como capacidad productiva general.

------

## 2. Delta respecto de v0.2

La v0.3 incorpora exclusivamente los aprendizajes obtenidos durante la primera revisión humana desde el **plano de usuario**.

Quedan incorporadas las siguientes decisiones:

```text
relación con la marca
!=
pertenencia al programa de fidelización
!=
intención respecto del evento
```

Se introducen tres relaciones comerciales posibles:

```text
no cliente / no miembro
cliente / no miembro
cliente / miembro
```

Se incorpora una intención alternativa:

```text
no participar
+
quiero recibir información
```

Se distinguen:

```text
QR de inscripción
!=
QR de presencia
```

Se incorporan:

```text
recomendaciones de equipamiento
+
información adicional voluntaria
+
incentivo por información
```

Web y App deberán representar el mismo estado funcional.

La perspectiva Marketing/CRM no se revisa todavía en esta versión.

------

# 3. Contexto de negocio

La empresa es una cadena ficticia de distribución de moda, material y equipamiento deportivo.

Dispone de:

- clientes identificados;
- histórico transaccional;
- un programa de fidelización existente;
- actividades y eventos deportivos;
- canales web y App;
- capacidad para relacionar participación deportiva, conocimiento del cliente y activación comercial.

El interlocutor de la demo puede ser Marketing o CRM, pero esta versión no diferencia todavía dos recorridos comerciales especializados.

------

# 4. Tesis de la demo

La demo debe mostrar cómo los eventos deportivos pueden convertirse en una superficie para:

```text
participación
+
fidelización
+
captación
+
conocimiento del cliente
+
reconocimiento
+
recomendación comercial
+
activación futura
```

El evento no se entiende únicamente como una promoción puntual.

Puede funcionar simultáneamente como:

```text
actividad deportiva
+
punto de contacto
+
ocasión de identificación
+
fuente de información declarada
+
oportunidad de fidelización
```

------

# 5. Objetivo comercial principal

El objetivo principal es demostrar cómo la actividad deportiva puede contribuir a:

1. captar nuevos consumidores;
2. convertir clientes existentes en miembros del programa de fidelización;
3. enriquecer el conocimiento de clientes ya identificados;
4. activar compras relacionadas con la práctica deportiva;
5. reforzar la continuidad de relación con miembros ya fidelizados.

El primer recorrido no necesita ejecutar productivamente todas estas posibilidades.

------

# 6. Temporada deportiva

La demo representa una **temporada deportiva**.

La temporada contiene varios eventos.

Mantener:

```text
temporada
!=
evento
```

Deben aparecer al menos tres disciplinas:

```text
Carrera
Vela
Vóley playa
```

Carrera continúa siendo la disciplina seleccionada para el primer recorrido ejecutable extremo a extremo.

Vela y Vóley playa pueden permanecer visibles sin recorrido completo.

------

# 7. Personalidad de los eventos

Los eventos pueden combinar dos dimensiones:

### Competición y reconocimiento

La persona participa buscando:

- resultado;
- posición;
- mejora;
- reconocimiento;
- trofeo u otro hito deportivo.

### Presencia, bienestar y dimensión social

La persona participa buscando:

- actividad;
- presencia;
- disfrute;
- relación social;
- bienestar;
- continuidad.

Estas dimensiones no determinan un perfil permanente de persona.

Mantener:

```text
modalidad de participación
!=
segmento permanente
!=
arquetipo
```

Una misma persona puede competir en un deporte y participar socialmente en otro.

------

# 8. Modalidades

En el recorrido primario deben mantenerse inicialmente:

```text
Social
Bienestar
```

La modalidad:

- se elige para una inscripción concreta;
- pertenece a un evento concreto;
- no se almacena como clasificación permanente de la persona.

La modalidad Competición permanece disponible como contraste conceptual para una iteración posterior.

La relación:

```text
modalidad
↔
Experience
```

permanece abierta.

No debe resolverse artificialmente en esta versión.

------

# 9. Relación de la persona con la marca

La demo debe distinguir tres situaciones.

## 9.1 No cliente / no miembro

La persona:

```text
no es cliente conocido
no pertenece al programa
```

Puede, no obstante:

```text
participar en un evento
```

Los eventos constituyen una oportunidad de captación de consumidores todavía no conocidos por la marca.

Su participación puede iniciar:

```text
identificación
→
relación
→
posible captación
```

pero:

```text
inscribirse en un evento
!=
convertirse automáticamente en cliente
!=
darse de alta automáticamente en el programa
```

Este caso debe permanecer explícito en la narrativa.

No es obligatorio ejecutar todavía todo su proceso de alta.

------

## 9.2 Cliente / no miembro

La persona:

```text
es cliente conocido
+
tiene transacciones
+
no pertenece al programa de fidelización
```

La marca puede reconocerla y mostrar:

- datos ficticios conocidos;
- historial de compras simulado;
- relación comercial existente;
- ausencia de pertenencia al programa.

Además, puede calcularse y mostrarse un **resultado contrafactual**:

```text
“Si hubieras pertenecido al programa,
tus compras habrían generado…”
```

Este resultado puede expresarse mediante:

- puntos;
- nivel;
- beneficios;
- recompensas potenciales;

siempre que quede claramente identificado como contrafactual.

Mantener:

```text
valor contrafactual
!=
valor realmente obtenido
```

No se crean retroactivamente puntos, premios o derechos reales.

------

## 9.3 Cliente / miembro

La persona:

```text
es cliente conocido
+
pertenece al programa de fidelización
```

La interfaz debe poder mostrar su situación actual simulada dentro del programa.

Puede incluir:

- pertenencia;
- nivel;
- puntos;
- beneficios;
- reconocimientos;
- otra información pertinente para la demo.

Estos datos deben proceder de la configuración situada.

La pertenencia al programa no determina la modalidad deportiva elegida.

------

# 10. Selección de persona

La UI debe permitir seleccionar una persona simulada.

Esta selección no representa autenticación real.

Su finalidad es comparar cómo cambia la experiencia según la relación existente con la marca.

La selección debe permitir mostrar al menos:

```text
cliente no miembro
cliente miembro
```

El caso:

```text
no cliente / no miembro
```

debe permanecer visible como posibilidad comercial, aunque su recorrido completo pueda ser narrado.

Después de seleccionar o reconocer a la persona, la interfaz debe responder claramente:

```text
¿es cliente?
¿pertenece al programa?
¿qué conoce la marca sobre ella?
```

------

# 11. Relación con la marca e intención

Después de establecer la relación con la marca, debe preguntarse qué desea hacer la persona.

Mantener:

```text
relación con la marca
!=
intención actual
```

La demo debe admitir al menos:

```text
PARTICIPAR
```

y:

```text
NO PARTICIPAR
PERO QUIERO RECIBIR INFORMACIÓN
```

No participar no implica ausencia de interés.

------

# 12. Rama: participar

Si la persona desea participar:

```text
persona
↓
elegir evento
↓
inscripción
↓
información adicional opcional
↓
recomendaciones de equipamiento
↓
participación
↓
reconocimiento
```

La relación comercial previa determina qué información puede recuperar la marca, pero no impide participar a quien todavía no sea cliente.

------

# 13. Rama: no participar pero recibir información

La persona puede decidir:

```text
no participar
+
mantener interés
```

La interfaz puede permitir seleccionar:

- deportes;
- disciplinas;
- tipos de eventos;
- futuras convocatorias;
- información de interés.

Esta información debe tratarse como declarada.

Mantener:

```text
interés declarado
!=
participación
```

y:

```text
interés declarado
!=
intención de compra
```

No es necesario implementar en esta fase:

- envío real de comunicaciones;
- automatización de marketing;
- CRM externo;
- consentimiento productivo;
- suscripciones reales.

------

# 14. QR de inscripción

La UI web debe contemplar un punto de entrada:

```text
LEER QR DE INSCRIPCIÓN
```

Este QR representa el acceso al proceso de inscripción de un evento.

No representa todavía presencia en el evento.

Mantener:

```text
QR de inscripción
!=
QR de presencia
```

------

# 15. Reconocimiento desde QR de inscripción

Después de entrar mediante el QR de inscripción:

```text
QR
↓
¿persona reconocida?
```

## Persona reconocida como cliente

La demo puede:

```text
recuperar persona
↓
mostrar datos conocidos
↓
mostrar pertenencia o no al programa
↓
continuar inscripción
```

No debe obligar a introducir nuevamente información ya conocida dentro de la simulación.

## Persona no reconocida

La demo debe poder explicar el recorrido:

```text
persona desconocida
↓
formulario
↓
datos mínimos
↓
inscripción al evento
```

Este caso demuestra la función del evento como superficie de captación.

Su ejecución completa puede permanecer fuera del siguiente corte para evitar complejidad innecesaria.

------

# 16. Inscripción

La inscripción debe conservar como mínimo:

```text
persona
evento
modalidad
estado
```

La inscripción:

```text
!=
pertenencia al programa
```

y:

```text
!=
presencia
```

y:

```text
!=
resultado deportivo
```

Una persona no cliente puede inscribirse sin que ello suponga automáticamente ninguna otra relación comercial.

------

# 17. Información necesaria e información adicional

Debe distinguirse:

```text
información necesaria para participar
```

de:

```text
información adicional voluntaria
```

La información adicional puede incluir, por ejemplo:

- práctica deportiva;
- frecuencia;
- preferencias;
- objetivos;
- tipo de equipamiento;
- intereses deportivos.

Debe quedar claro que se trata de información declarada por la persona.

Mantener:

```text
información declarada
!=
información observada
```

------

# 18. Incentivos por aportar información

La persona puede recibir un incentivo explícito por aportar información adicional.

La demo debe poder representar:

```text
información adicional voluntaria
→
incentivo
```

pero no:

```text
participar
→
obligación de entregar información adicional
```

El incentivo debe diferenciarse de:

- la insignia deportiva;
- un trofeo;
- una recompensa por resultado;
- la pertenencia al programa.

------

# 19. Recomendaciones de equipamiento

Después de seleccionar un evento, la demo puede presentar recomendaciones de equipamiento relacionadas con la disciplina.

Ejemplo:

```text
Carrera
↓
equipamiento recomendado
```

Puede incluir:

- calzado;
- textil;
- accesorios;
- hidratación;
- otros productos relacionados.

En esta fase las recomendaciones pueden ser editoriales y situadas.

No se requiere:

```text
motor de recomendación
IA
stock real
precio real
ecommerce real
```

La recomendación debe aparecer como recomendación comercial contextual.

No como inferencia automática de necesidad.

------

# 20. Evidencia de presencia

Una vez inscrita la persona, la presencia puede acreditarse en la simulación mediante:

```text
QR / check-in simulado
→
Evidencia de presencia
```

Este QR es distinto del QR de inscripción.

Debe permanecer explícitamente simulado.

No acredita:

- lectura física real de QR;
- presencia física verificada;
- integración con organizador;
- validación externa.

------

# 21. Evidencia de esfuerzo

La persona puede declarar:

```text
suave
medio
intenso
```

La declaración genera una Evidencia distinta de la presencia.

Debe conservarse como:

```text
esfuerzo autodeclarado
```

Mantener:

```text
presencia
!=
esfuerzo
```

y:

```text
esfuerzo declarado
!=
medición objetiva
```

La intensidad no debe utilizarse para valorar a la persona ni inferir capacidad de compra.

------

# 22. Resultado competitivo

El resultado competitivo permanece fuera del recorrido primario.

En una futura modalidad Competición podrían registrarse:

```text
resultado
+
posición
```

declarados por la persona.

No requieren todavía validación externa.

Mantener:

```text
resultado competitivo
!=
presencia
!=
esfuerzo
```

------

# 23. Reconocimiento

La primera participación puede producir reconocimiento inmediato.

El reconocimiento primario continúa siendo una **insignia individual**.

Debe distinguirse:

```text
insignia
!=
trofeo
!=
cupón
!=
beneficio
!=
nivel
```

La insignia debe explicar:

- qué se ha obtenido;
- por qué;
- qué Evidencias sustentan el reconocimiento.

------

# 24. Regla situada de la insignia

Para el primer recorrido ejecutable puede mantenerse:

```text
inscripción aceptada
+
Evidencia de presencia
+
Evidencia de esfuerzo válida
+
misma persona
+
mismo evento
→
insignia individual
```

Esta regla es:

```text
LOCAL
SITUADA
EXPERIMENTAL
NO TES
NO UNIVERSAL
```

No debe promoverse como regla general de eventos deportivos.

------

# 25. Continuidad

La narrativa general contempla que una segunda participación pueda actuar como:

```text
booster
```

o reforzar una trayectoria posterior.

Esta idea permanece abierta.

No demostrar todavía:

```text
TES Progression
TES Completion
TES Result
```

La primera participación basta para el recorrido actual.

------

# 26. Deportes cruzados

Las disciplinas permanecen independientes en esta versión.

Participar en Carrera no produce automáticamente estado o progresión en Vela o Vóley playa.

No implementar todavía lógica transversal entre deportes.

------

# 27. Equipos

Los participantes pueden formar equipos en deportes colectivos.

Por ejemplo:

- futsal;
- vóley playa.

En esta versión:

```text
equipo
→
organización de participantes
```

Los reconocimientos continúan siendo individuales.

No inferir:

```text
equipo
=
Group TES
```

No ejecutar todavía:

- Evidencia colectiva;
- resultado colectivo;
- recompensa colectiva;
- identidad colectiva;
- Group TES.

------

# 28. Superficie WEB

La UI web debe permitir representar progresivamente:

```text
selección o reconocimiento de persona
↓
estatus comercial
↓
pertenencia al programa
↓
intención
↓
evento
↓
inscripción
↓
información adicional
↓
recomendaciones
↓
participación
```

Debe existir un acceso mediante:

```text
QR de inscripción
```

y posteriormente un mecanismo diferente para:

```text
QR de presencia
```

La web puede mostrar más información contextual que la App si resulta adecuado.

Pero no debe poseer un modelo funcional distinto.

------

# 29. Superficie APP

La App debe adoptar el mismo modelo funcional que la web.

Debe poder representar:

- persona;
- condición de cliente;
- condición de miembro;
- transacciones cuando proceda;
- contrafactual para cliente no miembro;
- intención;
- evento;
- inscripción;
- información adicional;
- incentivo;
- recomendaciones;
- Evidencia;
- reconocimiento.

Mantener:

```text
UI web
!=
UI App
```

pero:

```text
estado funcional Web
=
estado funcional App
```

No construir dos lógicas de negocio.

------

# 30. Caso primario preferente

Después de la revisión humana, el caso preferente para el siguiente recorrido ejecutable pasa a ser:

```text
CLIENTE CONOCIDO
+
NO MIEMBRO DEL PROGRAMA
```

El recorrido permite mostrar:

```text
selección / reconocimiento
↓
historial transaccional
↓
resultado contrafactual del programa
↓
intención de participar
↓
Carrera
↓
inscripción
↓
información adicional opcional
↓
recomendaciones
↓
participación
↓
Evidencia
↓
insignia
↓
oportunidad de incorporarse al programa
```

Este caso combina:

- valor comercial conocido;
- coste de oportunidad de no pertenecer al programa;
- participación;
- información declarada;
- recomendación;
- reconocimiento;
- captación hacia fidelización.

------

# 31. Casos de contraste

## Caso A — Cliente / no miembro

Recorrido preferente ejecutable.

## Caso B — Cliente / miembro

Debe permitir contrastar:

- pertenencia;
- estado del programa;
- datos ya conocidos;
- participación sin necesidad de captación hacia el club.

## Caso C — No cliente / no miembro

Debe permanecer explícitamente representado como oportunidad de adquisición.

Puede narrarse:

```text
evento
→
QR de inscripción
→
formulario
→
participación
→
nueva relación potencial
```

sin implementar todavía todo el alta productiva.

------

# 32. No participar pero recibir información

Esta rama debe existir independientemente del estado comercial.

Una persona puede:

```text
ser cliente o no
+
ser miembro o no
+
no participar
+
querer información
```

No debe producir:

- inscripción;
- presencia;
- Evidencia de esfuerzo;
- insignia de participación.

------

# 33. Perspectiva Marketing/CRM

La demo mantiene una superficie Marketing/CRM basada en el mismo estado de ejecución.

La revisión humana de esta perspectiva queda **pendiente**.

La v0.3 no añade todavía requisitos nuevos a dicha superficie derivados de la revisión del usuario.

No reinterpretar automáticamente desde Marketing/CRM los nuevos estados descritos en esta versión hasta completar esa revisión.

------

# 34. Autoría de demos

En esta fase no se requiere una interfaz gráfica para crear demos.

El canal de autoría previsto es:

```text
narrativa escrita
↓
interpretación
↓
definición situada
↓
construcción
```

Cada nueva demo debe servir para descubrir:

- variables recurrentes;
- relaciones necesarias;
- decisiones opcionales;
- campos configurables;
- validaciones necesarias;
- fricciones de autoría.

Este aprendizaje podrá alimentar en el futuro:

```text
protocolo de definición
+
interfaz de autoría
```

No construir preventivamente esa interfaz.

------

# 35. Paleta visual

En ausencia de una marca cliente real, Brisa Sport utiliza actualmente como configuración visual la paleta Convercus:

```text
Ultramarine  #090685
Mid Blue     #092BFD
Tech Blue    #0AEFFF
Berry Red    #F72585
Warm Grey    #F1F1F1
White        #FFFFFF
```

Esta decisión es local a la demo.

No constituye todavía una regla general promovida de Demo Factory.

La identidad visual no debe determinar comportamiento funcional.

------

# 36. Garantías semánticas

La demo debe conservar:

```text
persona
!=
cliente
cliente
!=
miembro
miembro
!=
participante
relación con la marca
!=
intención actual
modalidad
!=
clasificación permanente
inscripción
!=
presencia
QR de inscripción
!=
QR de presencia
presencia
!=
esfuerzo
!=
resultado
información declarada
!=
información observada
recomendación
!=
necesidad inferida
insignia
!=
beneficio
oportunidad
!=
conversión
```

------

# 37. Fuera de alcance

Continúan fuera:

- autenticación real;
- QR/cámara real;
- alta real de cliente;
- alta real en programa;
- consentimiento productivo;
- envío real de comunicaciones;
- CRM externo;
- ecommerce;
- inventario;
- precios reales;
- recomendación algorítmica;
- IA de personalización;
- integración deportiva externa;
- wearables;
- validación federativa;
- clasificación competitiva real;
- ranking global;
- trofeos ejecutados;
- recompensa colectiva;
- Group TES;
- segunda participación ejecutada;
- booster ejecutado;
- TES Progression;
- TES Completion;
- TES Result;
- correspondencia general modalidad–Experience;
- protocolo general de demos;
- interfaz sin código de autoría.

------

# 38. Preguntas de UX — plano usuario

El siguiente recorrido deberá permitir observar:

1. ¿Comprende la persona por qué aparece como reconocida?
2. ¿Distingue ser cliente de pertenecer al programa?
3. ¿Comprende el resultado contrafactual mostrado al cliente no miembro?
4. ¿Distingue participar de querer recibir información?
5. ¿Entiende qué evento ha seleccionado?
6. ¿Distingue QR de inscripción y QR de presencia?
7. ¿Comprende qué información es obligatoria y cuál voluntaria?
8. ¿Comprende qué incentivo obtiene por aportar información adicional?
9. ¿Percibe las recomendaciones de equipamiento como útiles?
10. ¿Las interpreta como presión comercial?
11. ¿Entiende que inscribirse no implica darse de alta en el programa?
12. ¿Entiende qué cambia si ya pertenece al programa?
13. ¿Resulta creíble que un no cliente pueda comenzar su relación con la marca a través de un evento?
14. ¿Comprende qué hechos conoce realmente la marca y cuáles proceden de declaraciones realizadas durante el recorrido?

No debe escribirse copy únicamente para conducir artificialmente a respuestas afirmativas.

------

# 39. Decisiones cerradas en v0.3

Quedan fijadas:

```text
Carrera
→ primera disciplina ejecutable
QR/check-in simulado
→ Evidencia de presencia
la relación con la marca
precede a la intención
no cliente / no miembro
cliente / no miembro
cliente / miembro
→ estados diferenciados
cliente / no miembro
→ caso primario preferente
no cliente / no miembro
→ caso comercialmente relevante
→ puede permanecer parcialmente narrado
participar
!=
recibir información
QR de inscripción
!=
QR de presencia
información adicional voluntaria
→ puede recibir incentivo
evento
→ puede producir recomendaciones situadas de equipamiento
Web y App
→ mismo estado funcional
```

------

# 40. Estado de construcción respecto de esta definición

BUILD 01 y el Delta Visual 01 preceden a esta v0.3.

Por tanto:

```text
v0.3
!=
estado actualmente implementado
```

La versión actualmente construida no debe presentarse como cumplimiento de todos los requisitos incorporados aquí.

La v0.3 recoge aprendizaje humano posterior a BUILD 01.

------

# 41. Próximo paso

No iniciar todavía un nuevo BUILD.

Antes debe revisarse separadamente:

```text
PLANO MARKETING / CRM
```

Después de esa revisión deberá determinarse si:

```text
v0.3
→ v0.4
```

integra ambos planos antes de volver a construir.

La siguiente construcción debe responder a una definición consolidada, no a observaciones parciales tomadas de forma independiente.