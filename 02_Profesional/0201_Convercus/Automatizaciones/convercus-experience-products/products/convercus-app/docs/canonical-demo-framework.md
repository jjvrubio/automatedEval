---
title: "Marco de la demo canónica de Convercus App"
aliases:
- "Demo canónica de Convercus App"
- "Canonical Demo Framework"
language: es
version: "v0.4"
status: "borrador de producto"
date: "2026-07-17"
project: "Convercus App"
document_type: "marco de demostración de producto"
scope: "arquitectura multiexperiencia, recorrido, controles y evolución de la demo canónica hacia una App operativa"
repository_role: "documento rector de la demo canónica"
semantic_authority: "construcción de producto subordinada; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Marco de la demo canónica de Convercus App

## Estatuto

Este documento es una **construcción propia de producto**. Define cómo demostrar y, más adelante, operar capacidades de Convercus App. No introduce conceptos ontológicos ni modifica el contrato semántico TES.

## Propósito

La demo canónica debe ser simultáneamente:

1. una demostración comercial comprensible, estable y repetible;
2. la primera instancia de una arquitectura capaz de generar versiones personalizadas;
3. un paso válido hacia una App operativa para clientes, no una maqueta desechable.

El objetivo no es enseñar todas las funciones de Convercus. Es hacer visible, mediante un caso coherente, cómo fidelización, contenidos, incentivos y orquestación experiencial actúan conjuntamente sobre una o varias participaciones concretas. El relato comercial puede concentrarse en una Experience principal, pero la arquitectura no debe presuponer que sea la única activa para el miembro.

El marco reconoce que Convercus es un sistema operativo de fidelización y que no todos los clientes necesitan o están preparados para operar estrategias basadas en Experiences. Una versión puede demostrar únicamente capacidades de fidelización, siempre que no las presente como Experiences. Cuando una capacidad se formule como Experience, deberá obedecer íntegramente la baseline TES aplicable.

## Resultado esperado

Al finalizar la demo, el interlocutor debe comprender:

- quién es el miembro y cuál es su situación;
- qué intenta hacer o disfrutar;
- cómo Convercus reconoce señales y conserva continuidad;
- si la versión opera solo con fidelización o contiene Experiences en sentido TES;
- cuando existan, qué Experiences están activas y cuál organiza el relato principal;
- a qué Experience o Experiences puede afectar un evento;
- por qué aparece cada intervención y, cuando corresponda, qué Experience la justifica;
- qué papel desempeña un incentivo sin confundirlo con la Experience;
- cómo cambia de forma independiente el estado de cada participación;
- cómo se coordinan intervenciones coincidentes, incompatibles o redundantes;
- qué resultado se observa en cada Experience mostrada;
- qué puede medirse y aprenderse;
- qué partes son capacidades reales, simuladas o futuras.

## Arquitectura de una versión

```text
Núcleo estable de Convercus App
        │
        ├── configuración de cliente y marca
        ├── paquete de contenidos y fidelización
        ├── paquete de escenario experiencial
        │       ├── una o varias Experiences
        │       ├── participaciones y estados independientes
        │       ├── señales, eventos y reglas de evaluación
        │       └── coordinación de intervenciones
        ├── guion de demostración
        ├── manifiesto de capacidades
        └── adaptador de datos
                ├── mock
                ├── simulation
                ├── staging
                └── production
```

### Núcleo estable

Incluye navegación, componentes, accesibilidad, estado de sesión, motor de presentación, contratos internos, observabilidad y manejo de errores. No contiene nombres, promociones ni recorridos específicos de un cliente.

### Configuración de cliente y marca

Define identidad visible, tono, textos legales, idioma, canales y reglas de presentación. Personaliza la App sin bifurcar su núcleo.

### Paquete de contenidos y fidelización

Contiene miembros ficticios o autorizados, noticias, cupones, niveles, saldos, beneficios y actividad necesarios para esa versión.

### Paquete de escenario experiencial

Solo es obligatorio cuando la versión presenta una o varias Experiences. Describe las Experiences y participaciones que deben poder reconstruirse. Para cada Experience conserva situación, arquetipo de sujeto participante, propensión ordinal sectorial y su fuente, señales relevantes, fuentes de evidencia, eventos significativos, patrón, secuencia, progresión, reglas, intervenciones, incentivos, recompensas, resultado, medición y aprendizaje. Debe citar la baseline semántica utilizada.

Una versión exclusivamente orientada a fidelización puede omitir este paquete y declarar su aplicabilidad TES experiencial como `not_applicable`. Esta declaración no permite denominar Experience a una campaña, beneficio, Workflow o secuencia sin transformación reconstruible.

Cuando existan participaciones simultáneas, el paquete declara además:

- qué señales, datos y eventos pueden ser evaluados por cada Experience;
- qué regla aplica cada Experience y qué efecto independiente produce;
- qué dependencias, exclusiones o prioridades existen entre participaciones;
- cómo se coordinan intervenciones coincidentes, incompatibles o redundantes;
- qué parte de esta arquitectura se selecciona para el recorrido de demostración.

### Guion de demostración

Indica el estado inicial, las acciones del presentador o del usuario, los cambios esperados, los mensajes que se desea explicar y la forma de reiniciar la demo.

### Superficies de presentación y validación

La demo distingue tres superficies que no deben confundirse:

| Superficie | Finalidad | Garantía |
|---|---|---|
| App responsive | Usar y evaluar directamente la interfaz comercial en navegador | Comportamiento funcional del prototipo |
| Modo iPhone `/showcase` | Presentar la misma App dentro de un marco visual de 393 × 852 px | Composición comercial y aproximación del viewport |
| iPhone real | Instalar y ejecutar la PWA en hardware y Safari/iOS | Compatibilidad, instalación, áreas seguras, rendimiento y comportamiento offline |

El modo iPhone es una envolvente de presentación y no una segunda implementación. La App se ejecuta dentro del marco sin modificar su navegación ni su estado de capacidades. Este modo no constituye evidencia de compatibilidad con iOS, no simula el motor de Safari y no sustituye la validación en dispositivo real prevista para A5.

La envolvente debe quedar fuera de la experiencia del miembro, ofrecer una salida clara y declarar visualmente que se trata de una simulación. Puede utilizarse para revisión interna, capturas y demostraciones comerciales.

### Manifiesto de capacidades

Clasifica cada capacidad mostrada como:

- `real`: disponible y conectada a una capacidad verificada;
- `simulated`: comportamiento representativo ejecutado localmente;
- `mocked`: dato fijo sin ejecución subyacente;
- `proposed`: visión futura que no se presenta como disponible;
- `unsupported`: significado reconocido que la versión no puede representar.

### Adaptador de datos

Separa la interfaz y el escenario de su fuente de datos. El paso de demo a operación debe producirse sustituyendo adaptadores y reforzando garantías, no reescribiendo el modelo de presentación.

## Modelo de simultaneidad y alcance de eventos

Cuando existan Experiences, un miembro puede participar simultáneamente en varias. Sus estados, progresiones, resultados, mediciones y aprendizajes permanecen diferenciados aunque compartan señales, datos o eventos.

```text
Señal, dato o evidencia recibida
        ↓
Evento observable reconocido
        ↓
Enrutamiento a participaciones potencialmente afectadas
        ├── Experience A → regla A → progresión + intervención
        ├── Experience B → regla B → cambio de estado sin intervención
        └── Experience C → regla C → sin efecto
                                ↓
                    coordinación de intervenciones
```

La recepción o el enrutamiento no producen progresión por sí solos. Cada Experience evalúa el evento conforme a su contexto, estado y reglas. Un mismo evento puede ser significativo para una Experience, meramente contextual para otra y no producir efecto en una tercera.

La coordinación de intervenciones es una responsabilidad de producto distinta de la evaluación experiencial. Puede aplicar prioridad, exclusión, composición, aplazamiento o supresión, pero no fusiona las Experiences ni altera silenciosamente el estado que cada una resolvió.

## Fidelidad TES, superficie y validación

La demo es una superficie de producto: puede simplificar lenguaje, densidad y recorrido para ajustarse a la audiencia, pero no puede alterar la arquitectura profunda de una Experience. Cuando la versión contenga Experiences deberá someterse, como mínimo, a estos controles:

1. **reconstruibilidad**: campo de mediación, evento, patrón, secuencia, progresión, resultado, medición y aprendizaje pueden recuperarse;
2. **coherencia de capas**: configuración, fidelización, Experience, participación, Workflow, medición y superficie no se sustituyen entre sí;
3. **integridad de activos**: cada activo visual se clasifica por su función y conserva relación con el ecosistema, la secuencia, el resultado o la explicación que representa;
4. **evidencia**: toda afirmación de resultado, eficacia o aprendizaje declara el soporte que permite sostenerla;
5. **dictamen**: la versión registra si es conforme, conforme con ajustes o no conforme con la baseline.

La producción visual seguirá la secuencia `reconstrucción → activos → instrucción → generación`. La generación o selección de activos no comenzará antes de reconstruir qué función deben cumplir.

## Escenario canónico inicial

Se adopta como hipótesis de trabajo y Experience principal **Circuito de decisión: ocasión**. Es adecuada porque permite mostrar continuidad entre inspiración, exploración, decisión, compra o participación y seguimiento posterior sin reducir la Experience a una promoción.

La primera narración comercial puede concentrarse únicamente en esta Experience para mantener claridad. El escenario y el motor deberán, no obstante, admitir otras Experiences activas y participaciones simultáneas sin cambiar el núcleo. Una Experience secundaria solo se hará visible en la primera demo si ayuda a explicar el valor de un evento compartido o de la coordinación entre intervenciones.

La definición detallada se realizará en un documento separado. Como mínimo deberá incluir:

1. miembro y situación inicial;
2. necesidad u ocasión reconocible;
3. arquetipo de sujeto participante, fuente y versión;
4. propensión ordinal reconocible en el sector, escala, fuente y justificación;
5. perfil de lealtad y actores de la participación concreta;
6. señales, datos y fuentes de evidencia relevantes;
7. eventos significativos observables;
8. patrón o regularidad que organiza la interpretación;
9. secuencia y estados de progresión;
10. reglas de evaluación y avance;
11. intervenciones justificadas por el estado;
12. incentivo y recompensa claramente diferenciados;
13. resultado observado;
14. medición compatible con el resultado;
15. aprendizaje reutilizable;
16. Experiences concurrentes, aunque no se muestren, y alcance compartido de eventos;
17. reglas de coordinación entre intervenciones;
18. activos visuales y su clasificación funcional;
19. validación de reconstruibilidad, capas, activos y evidencia;
20. límites de simulación y dependencias técnicas.

## Recorrido mínimo de la demo

```text
Restablecer escenario
        ↓
Presentar miembro, situación y Experience principal
        ↓
Explorar inicio, noticias, perfil y beneficios
        ↓
Producir o simular una señal o evidencia
        ↓
Reconocer un evento y evaluar las Experiences afectadas
        ├── participación principal → cambio visible
        └── otras participaciones → efecto independiente o ninguno
        ↓
Coordinar y mostrar la intervención contextual pertinente
        ↓
Realizar la siguiente acción
        ↓
Mostrar cambio de estado o progresión por Experience
        ↓
Desbloquear o entregar el elemento correspondiente
        ↓
Cerrar con resultados, medición y aprendizaje atribuibles
```

La pantalla del miembro solo mostrará aquello que tenga sentido en su situación y evite interferencias entre Experiences. No necesita exponer toda la evaluación multiexperiencia. La reconstrucción completa, la atribución de efectos, la coordinación, la medición y el aprendizaje podrán aparecer en un panel interno de demostración.

## Estados y controles obligatorios

- Estado inicial determinista.
- Reinicio completo en una acción.
- Estado independiente y consultable por participación.
- Activación, reinicio y cierre controlados por Experience sin corromper las demás.
- Avance manual del escenario desde un panel interno.
- Posibilidad de repetir un paso.
- Etiqueta visible del modo de datos para el presentador.
- Registro cronológico de señales, eventos y cambios de estado.
- Trazabilidad `señal o dato → evento → Experience → regla → efecto`.
- Inspección de un evento compartido y de su efecto en cada participación.
- Visualización de prioridades, exclusiones o supresiones entre intervenciones.
- Referencia del arquetipo, propensión ordinal sectorial y fuentes utilizadas.
- Clasificación funcional de los activos visuales mostrados.
- Dictamen de validación TES de la versión.
- Separación entre vista del miembro y controles de demo.
- Funcionamiento sin red en modo mock o simulation.

## Del demostrador a la App operativa

La evolución prevista es gradual:

| Etapa | Datos | Ejecución | Usuarios | Garantía principal |
|---|---|---|---|---|
| Demo canónica | Fijos y simulados | Motor local | Presentador | Repetibilidad |
| Demo personalizada | Paquete por cliente | Motor local y conectores selectivos | Presentador y cliente | Fidelidad del caso |
| Piloto | Staging o entorno aislado | Capacidades reales limitadas | Usuarios autorizados | Trazabilidad y seguridad |
| App operativa | Producción | Servicios Convercus verificados | Miembros reales | Fiabilidad, privacidad y soporte |

La transición a piloto o producción exige autenticación real, autorización, privacidad, consentimiento, accesibilidad, observabilidad, recuperación de errores, contratos de API verificados y operación segura. Ninguna simulación se considerará automáticamente apta para producción.

## Criterios de aceptación del marco

La demo canónica estará bien estructurada cuando:

- pueda personalizarse sin modificar el núcleo;
- pueda describirse mediante un protocolo estable;
- distinga contenido, configuración, Experiences, participaciones, escenario y ejecución;
- permita versiones de fidelización sin Experiences y declare esa aplicabilidad sin ambigüedad;
- exija cumplimiento TES completo a toda capacidad presentada como Experience;
- permita una o varias Experiences activas sin fusionar sus estados;
- permita que una señal o evento sea evaluado por una o varias Experiences;
- atribuya cada efecto a la regla y participación correspondientes;
- coordine explícitamente las intervenciones concurrentes;
- declare arquetipo participante y propensión ordinal sectorial por Experience;
- valide reconstruibilidad, coherencia de capas, integridad de activos y evidencia;
- clasifique los activos antes de producirlos o incorporarlos;
- diferencie el recorrido comercial de la arquitectura experiencial completa;
- mantenga el modo de presentación separado de la interfaz del miembro;
- identifique el marco iPhone como simulación y no como validación en dispositivo;
- sea reiniciable y repetible;
- declare con honestidad el estatuto de cada capacidad;
- conserve la congruencia con la baseline semántica;
- permita sustituir mocks por adaptadores reales por módulos;
- no imponga a la futura App operativa decisiones propias del guion comercial.

## Siguientes decisiones

1. Cristalizar «Circuito de decisión: ocasión» como Experience principal.
2. Decidir si la primera demo hará visible una Experience secundaria concurrente.
3. Definir el esquema técnico de un `DemoPackage` multiexperiencia.
4. Definir el enrutamiento de eventos y la coordinación de intervenciones.
5. Seleccionar y justificar el arquetipo y la propensión ordinal sectorial del escenario.
6. Seleccionar las pantallas y clasificar los activos necesarios para el recorrido canónico.
7. Definir el dictamen de validación previo a cada versión demostrable.
8. Determinar qué capacidades estarán simuladas en la primera versión.
