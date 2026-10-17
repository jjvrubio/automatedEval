# Convercus Demo Factory — BUILD 02

## Implementación de la revisión cerrada del plano usuario

Continúa sobre el estado actual del proyecto **Convercus Demo Factory**.

La `Demo definition v_0_3.md` es ahora la especificación situada autoritativa del plano usuario.

La revisión humana del plano usuario está cerrada y consolidada documentalmente.

Tu tarea es realizar un **delta de producto limitado al plano usuario** para que la demo ejecutable permita comprobar los cambios definidos en v0.3.

Esta tarea sí autoriza modificaciones de producto.

No revisar ni rediseñar todavía la perspectiva Marketing/CRM.

No abrir una nueva hipótesis H40 salvo que durante la construcción aparezca una presión concreta que no pueda resolverse dentro de esta especificación.

---

## 1. Objetivo

Construir el siguiente estado:

```text
BUILD 01
+
Demo Definition v0.3 — plano usuario
↓
BUILD 02
```

El resultado debe permitir que una persona abra la demo y **observe efectivamente las diferencias surgidas de la revisión humana**.

No basta con que los nuevos conceptos existan en contratos, fixtures o código interno.

Deben ser visibles y utilizables desde la interfaz cuando la especificación así lo exige.

---

## 2. Fuente autoritativa

Utilizar:

```text
Demo definition v_0_3.md
```

como fuente principal de requisitos.

Preservar:

```text
Demo definition v_0_2.md
BUILD 01
Visual Delta 01
S01–S39
historial de experimentos
arquitectura / ADR
TES / PSC
```

como evidencia histórica.

No reescribirlos retrospectivamente.

---

## 3. Principio de implementación

El cambio principal es que el recorrido de usuario ya no debe comenzar únicamente como un participante externo abstracto.

Debe hacer visible:

```text
PERSONA
↓
RELACIÓN CON LA MARCA
↓
RELACIÓN CON EL PROGRAMA
↓
INTENCIÓN ACTUAL
↓
RECORRIDO DEL EVENTO
```

Mantener:

```text
persona
!=
cliente
!=
miembro
!=
participante
```

---

## 4. Selección de persona

Incorporar en la interfaz una forma clara de seleccionar o reconocer una persona simulada.

Debe permitir probar, como mínimo:

```text
A. cliente conocido / no miembro
B. cliente conocido / miembro
```

y hacer visible conceptualmente:

```text
C. no cliente / no miembro
```

El caso C puede mantener parte de su onboarding narrado, según v0.3.

La selección es una mecánica de demo.

No simular autenticación productiva.

---

## 5. Cliente conocido / no miembro

Éste es el **caso primario ejecutable de BUILD 02**.

Después de seleccionar a esta persona, la UI debe mostrar de forma comprensible:

* que es cliente;
* que no pertenece al programa;
* algunos datos conocidos relevantes;
* historial transaccional ficticio;
* valor contrafactual del programa.

Debe existir una representación visible equivalente a:

```text
Con tus compras realizadas,
si hubieras pertenecido al programa,
habrías obtenido…
```

Puede utilizar:

* puntos potenciales;
* nivel potencial;
* beneficios potenciales;

según la configuración situada.

Debe quedar visual y semánticamente claro:

```text
CONTRAFACTUAL
!=
SALDO REAL
```

No acreditar retroactivamente beneficios.

---

## 6. Cliente / miembro

Debe existir como caso de contraste seleccionable.

Al elegirlo, la UI debe mostrar el estado ficticio correspondiente del programa:

* pertenencia;
* puntos si procede;
* nivel si procede;
* beneficios o reconocimientos pertinentes.

No convertir la pertenencia al programa en modalidad deportiva.

---

## 7. No cliente / no miembro

Mantener visible que una persona desconocida puede acceder a un evento.

Debe poder comprenderse:

```text
NO CLIENTE
+
NO MIEMBRO
→
PUEDE PARTICIPAR
```

No es necesario construir todavía un alta completa productiva.

Puede representarse mediante un formulario mínimo situado o un recorrido parcialmente narrado.

No crear:

* CRM real;
* alta productiva;
* consentimiento productivo;
* autenticación.

---

## 8. Intención actual

Después de establecer la relación de la persona con la marca, la interfaz debe ofrecer explícitamente:

```text
PARTICIPAR
```

y:

```text
NO PARTICIPAR
PERO QUIERO RECIBIR INFORMACIÓN
```

No esconder esta segunda alternativa dentro de otra pantalla.

Debe ser comprobable como rama diferenciada.

Mantener:

```text
no participar
!=
no estar interesado
```

---

## 9. Rama «recibir información»

Si la persona no participa pero quiere información, permitir expresar intereses situados, por ejemplo:

* deportes;
* disciplinas;
* eventos;
* próximas convocatorias.

No crear inscripción deportiva.

No generar:

* presencia;
* esfuerzo;
* insignia de participación.

No enviar comunicaciones reales.

La demo debe hacer visible que se ha registrado un interés declarado.

---

## 10. QR de inscripción

Añadir en la superficie web un acceso claramente identificable equivalente a:

```text
LEER QR DE INSCRIPCIÓN
```

No requiere cámara ni QR físico.

Puede ser una simulación interactiva.

Su finalidad es representar el acceso desde el evento al proceso de inscripción.

Mantener obligatoriamente:

```text
QR DE INSCRIPCIÓN
!=
QR DE PRESENCIA
```

No reutilizar un único botón con dos significados.

---

## 11. Reconocimiento desde QR

La simulación del QR de inscripción debe permitir comprobar dos situaciones.

### Cliente reconocido

```text
QR de inscripción
↓
cliente reconocido
↓
datos ya conocidos
↓
estado del programa
↓
continuar inscripción
```

No pedir de nuevo los datos que la simulación ya conoce.

### Persona desconocida

Debe poder mostrarse conceptualmente:

```text
QR de inscripción
↓
persona desconocida
↓
formulario mínimo
↓
inscripción
```

Su alta completa puede seguir fuera del corte.

---

## 12. Información adicional voluntaria

Durante el recorrido de participación, diferenciar claramente:

```text
DATOS NECESARIOS PARA INSCRIBIRSE
```

de:

```text
INFORMACIÓN ADICIONAL VOLUNTARIA
```

La segunda puede incluir de forma situada:

* frecuencia de práctica;
* preferencias;
* objetivos;
* disciplinas de interés;
* equipamiento.

Debe identificarse como información declarada.

---

## 13. Incentivo por información

Incorporar una razón visible para aportar voluntariamente esa información.

Representar:

```text
información adicional
→
incentivo
```

El incentivo no debe confundirse con:

* insignia deportiva;
* premio por resultado;
* pertenencia al club.

La persona debe poder continuar aunque no aporte la información voluntaria.

---

## 14. Recomendaciones de equipamiento

Después de seleccionar Carrera, incorporar recomendaciones contextualizadas de equipamiento.

Por ejemplo:

* calzado;
* textil técnico;
* hidratación;
* accesorios.

Deben ser claramente recomendaciones situadas/editoriales.

No implementar:

* motor de recomendación;
* IA;
* inventario real;
* precios productivos;
* comercio electrónico.

La finalidad es comprobar si la recomendación resulta contextual y útil dentro del recorrido.

---

## 15. Presencia

Preservar el mecanismo ya existente:

```text
QR / check-in simulado
→
Evidencia de presencia
```

pero mantenerlo visualmente diferenciado del nuevo QR de inscripción.

La persona debe poder comprender que uno sirve para entrar/inscribirse y otro para acreditar presencia.

---

## 16. Esfuerzo e insignia

Preservar:

```text
suave
medio
intenso
```

como esfuerzo autodeclarado.

Preservar la regla situada actual de la insignia:

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

No ampliar ahora la semántica deportiva.

---

## 17. Web y App

La revisión humana exige que ambas superficies compartan el mismo estado funcional.

Mantener:

```text
INTERFAZ WEB
!=
INTERFAZ APP
```

pero asegurar:

```text
ESTADO FUNCIONAL WEB
=
ESTADO FUNCIONAL APP
```

Cuando sea relevante, ambas deben poder reflejar:

* persona seleccionada;
* cliente/no cliente;
* miembro/no miembro;
* transacciones;
* contrafactual;
* intención;
* inscripción;
* información declarada;
* incentivo;
* recomendaciones;
* Evidencias;
* reconocimiento.

No crear dos modelos de negocio independientes.

---

## 18. Marketing/CRM

No modificar funcionalmente la perspectiva Marketing/CRM salvo lo estrictamente necesario para que continúe funcionando con el mismo estado compartido.

No añadir todavía:

* nuevos paneles;
* segmentaciones;
* indicadores;
* campañas;
* automatizaciones;
* puntuaciones;
* nuevas oportunidades;
* nuevos recorridos comerciales.

La revisión humana de esa perspectiva se realizará después de BUILD 02.

---

## 19. Diseño visual

Preservar Visual Delta 01 y la paleta Convercus ya aplicada.

Esta tarea no es un rediseño visual general.

Los cambios visuales deben limitarse a hacer comprensible la nueva interacción.

No construir un sistema general de temas.

---

## 20. Qué debe poder observar Juan después del BUILD

Al abrir la demo debe ser posible constatar visualmente, sin inspeccionar código:

1. que puede seleccionar/reconocer personas;
2. que distingue cliente de miembro;
3. que existe un cliente no miembro con compras;
4. que puede ver su contrafactual de fidelización;
5. que puede elegir participar o sólo recibir información;
6. que existe un QR simulado de inscripción;
7. que éste es distinto del check-in de presencia;
8. que puede distinguir información necesaria de información voluntaria;
9. que existe un incentivo por la información adicional;
10. que aparecen recomendaciones de equipamiento;
11. que el recorrido continúa hasta presencia, esfuerzo e insignia;
12. que App y Web representan el mismo estado funcional relevante.

Si alguno de estos puntos sólo existe en código y no puede observarse durante la demo, no considerar BUILD 02 terminado.

---

## 21. Controles

Antes del delta:

* ejecutar las pruebas aplicables;
* registrar el estado baseline;
* no corregir retrospectivamente guardas históricas para hacerlas pasar.

Después del delta:

* pruebas específicas del nuevo recorrido;
* pruebas del estado compartido;
* typecheck;
* lint;
* build;
* prueba en navegador de escritorio;
* prueba de la superficie móvil/App correspondiente.

Preservar y documentar cualquier fallo histórico provocado exclusivamente por guardas hash de sesiones anteriores.

No suprimirlo.

---

## 22. Informe BUILD 02

Crear un informe específico:

```text
build-02-sports-season-user-plane.md
```

Debe incluir:

* baseline;
* archivos modificados;
* capacidades implementadas;
* recorrido principal ejecutable;
* casos de contraste;
* comportamiento Web/App;
* pruebas;
* resultados de navegador;
* elementos todavía narrados;
* diferencias entre v0.3 e implementación final;
* fricciones de UX dejadas deliberadamente para revisión humana;
* cualquier presión nueva observada.

---

## 23. STOP

Finalizado BUILD 02:

```text
STOP
```

No corregir preventivamente las fricciones humanas encontradas durante la construcción si no impiden ejecutar la especificación.

No abrir H40 automáticamente.

No iniciar Marketing/CRM.

No generar v0.4.

El siguiente paso será:

```text
BUILD 02
↓
REVISIÓN HUMANA DEL NUEVO PLANO USUARIO
```

Sólo después decidiremos si el plano usuario queda aceptado o genera una nueva presión.
