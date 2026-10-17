# Demo Definition v0.2 — Temporada deportiva de fidelización

## 0. Estatuto

```
SITUATED DEMO SPECIFICATION
v0.2
EXPERIMENTAL
LOCAL
NOT A GENERAL PROTOCOL
NOT PROMOTED
```

Esta especificación deriva de una narrativa comercial concreta.

**Delta respecto de v0.1:** esta versión cierra exclusivamente dos decisiones que permanecían provisionales: (1) Carrera será la disciplina del primer recorrido ejecutable extremo a extremo; (2) la presencia se acreditará mediante un QR/check-in simulado. No incorpora resultados del SAFE-TO-BUILD review ni modifica el resto de la especificación situada.

Su función es permitir construir y someter a crítica una primera demo de Convercus Demo Factory desde dos superficies diferentes:

```
DEMO-AUTHOR UX
PARTICIPANT / RECIPIENT UX
```

No pretende establecer todavía un protocolo universal para definir demostraciones.

# 1. Contexto comercial

## Tipo de empresa

Cadena ficticia de distribución de moda y equipamiento deportivo.

La empresa ya dispone de:

```
club de fidelización existente
+
programa de eventos deportivos
```

El problema no consiste en crear un programa de fidelización desde cero.

La oportunidad consiste en conectar:

```
fidelización
+
participación deportiva
+
reconocimiento
+
captación
+
activación comercial
```

# 2. Interlocutor de la demostración

Interlocutor principal único.

Perfil suficientemente transversal para representar inicialmente:

```
Marketing
+
CRM / Loyalty
```

Marketing será previsiblemente la puerta de entrada comercial.

CRM estará normalmente más próxima a la operación cotidiana del programa.

La primera demo no especializará todavía recorridos separados para ambos perfiles.

Debe ser:

```
comprensible para Marketing
+
operacionalmente creíble para CRM
```

# 3. Tesis comercial principal

La demo debe hacer visible que la actividad deportiva de la marca puede convertirse simultáneamente en:

```
relación
captación
conocimiento
reconocimiento
activación
```

La proposición comercial principal no es solamente:

```
“podemos incorporar eventos al club”
```

Debe aproximarse a:

```
Los eventos deportivos pueden convertirse en una nueva superficie
de adquisición y fidelización.

Convercus permite reconocer cómo participa cada persona,
mantener continuidad entre participaciones
y transformar esa relación en oportunidades relevantes
de captación, renovación y compra.
```

Dos resultados comerciales tienen especial importancia:

### A. Captación

Un participante en un evento:

```
no tiene por qué ser cliente
ni miembro del club
```

Su participación constituye una oportunidad legítima de captación.

No asumir:

```
participant = customer = club member
```

### B. Activación comercial

La actividad deportiva puede proporcionar contexto para activaciones como:

```
acceso anticipado a colecciones
renovación de material
acceso a categorías superiores
sesiones de mejora
encuentros con figuras públicas
cupones dependientes de nivel
```

La demo no debe convertir automáticamente participación en intención de compra.

Debe mostrar una oportunidad de activación derivada de una relación deportiva observable.

# 4. Universo deportivo

La demo representa una:

```
TEMPORADA DEPORTIVA
```

La temporada contiene varios eventos individuales.

Debe hacer perceptibles simultáneamente:

```
temporada
!=
evento
```

La primera composición contendrá tres disciplinas deportivas.

Candidatas iniciales:

```
Carrera
Vela
Vóley playa
```

La selección concreta puede cambiar durante la construcción sin alterar la intención de la especificación.

Las tres deben ser visibles como posibilidades del programa.

Sólo una disciplina necesita recorrerse completamente extremo a extremo en v0.2.

# 5. Temporalidad

La temporada permite mostrar que la relación no termina en una activación puntual.

Modelo situado:

```
Temporada
    ↓
varios eventos
    ↓
participaciones individuales
    ↓
reconocimiento inmediato
    +
continuidad potencial
```

Un evento puede tener valor por sí mismo.

Una serie de eventos puede producir además progresión acumulada.

No se diseña todavía una máquina genérica de temporadas.

# 6. Participantes

Deben poder coexistir al menos dos situaciones:

```
A. miembro existente del club
B. participante externo
```

## Miembro existente

Ya existe dentro de la relación de fidelización.

Su actividad deportiva puede enriquecer:

```
reconocimiento
continuidad
recorrido
activación comercial
```

## Participante externo

Puede inscribirse y participar sin ser previamente miembro del club.

Su participación crea:

```
captation opportunity
```

No convertir automáticamente:

```
external participant
→ club member
```

La eventual alta debe constituir una acción o decisión diferenciable.

# 7. Inscripción

La inscripción forma parte del recorrido visible.

La persona elige:

```
evento
+
modalidad
```

En v0.2 la modalidad es elegida por el participante.

El modelo futuro puede permitir también:

```
evento con modalidad única
```

pero no es necesario demostrarlo ahora.

# 8. Modalidades de participación

Una misma persona puede participar de formas diferentes dependiendo del evento.

No existe una clasificación permanente:

```
persona = casual
persona = social
persona = competitor
```

Debe preservarse:

```
persona
!=
modalidad fija
```

La misma persona puede, por ejemplo:

```
competir en carrera
participar socialmente en vela
participar por bienestar en otro evento
```

Las orientaciones iniciales son:

```
competición
social
bienestar
casual
```

La relación exacta entre estas orientaciones y las Experience Definitions de Convercus queda:

```
OPEN
```

No decidir todavía si:

```
1 modalidad = 1 Experience
```

ni si varias modalidades comparten una Experience.

La propia construcción de la demo debe proporcionar evidencia para esa decisión.

# 9. Experience

La temporada puede contener varias Experiences Convercus.

Sin embargo, v0.2 no fija todavía su cardinalidad ni la correspondencia exacta entre:

```
modalidad
motivación
evento
disciplina
Experience
```

Principio obligatorio:

```
no convertir una motivación situada
en una identidad permanente del participante
```

# 10. Evidencia de participación

Distinguir al menos:

```
presencia
esfuerzo
resultado competitivo
```

No tratarlas como un mismo hecho.

## Presencia

DECISIÓN TODAVÍA NO CERRADA.

Candidato operativo v0.2:

```
QR / check-in simulado -> Evidencia de prewsencia
→ Evidencia de presencia
```

El QR/check-in es una mecánica simulada de la demo y no implica integración real, lectura de un QR físico ni acreditación externa de asistencia.
La Evidencia de presencia debe permanecer diferenciada de la Evidencia de esfuerzo.

## Esfuerzo

Para modalidades no competitivas:

```
suave
medio
intenso
```

En v0.2 puede ser:

```
autodeclarado por el participante
```

El esfuerzo no demuestra por sí mismo presencia.

## Competición

El participante puede introducir:

```
resultado
+
posición
```

En v0.2 esa declaración es suficiente.

No se requiere todavía validación externa por organizador, federación, dispositivo o sistema tercero.

Esto constituye una simplificación experimental explícita.

# 11. Reconocimientos

Distinguir:

```
insignias
trofeos
beneficios
```

## Insignia

Será el reconocimiento principal de la primera ejecución.

Puede reconocer:

```
participación
hito
continuidad
```

## Trofeo

Puede estar asociado a resultados competitivos.

Debe existir conceptualmente en la demo, pero no necesita ser el centro del primer recorrido.

## Beneficios

Los reconocimientos pueden conectarse posteriormente con beneficios como:

```
acceso anticipado a colecciones
invitaciones a sesiones de mejora
entrevistas / encuentros con figuras públicas
cupones de canje asociados a niveles
```

No asumir:

```
badge = coupon
trophy = reward
```

El reconocimiento y el beneficio deben poder distinguirse.

# 12. Participación acumulada

La lógica es dual.

Una primera participación puede producir:

```
reconocimiento inmediato
```

Una nueva participación posterior puede actuar como:

```
booster
```

y provocar entrada o progreso dentro de un recorrido Experience.

Para hacer visible esa capacidad sin construir una temporada completa en tiempo real, la demo puede partir de un estado situado donde exista una participación anterior.

Ejemplo experimental:

```
Participation 1
→ already recorded

Participation 2
→ performed during demo

Participation 2
→ immediate badge
+
meaningful progression / entry into Experience
```

La denominación y semántica exactas de ese progreso deberán respetar TES y las capacidades ya demostradas.

No inventar TES Progression si no existe autoridad para ello.

# 13. Relación entre disciplinas

En v0.2:

```
Carrera
Vela
Vóley playa
```

pueden coexistir dentro de la temporada.

Sus progresiones permanecen inicialmente:

```
INDEPENDENT
```

No implementar todavía:

```
participa en tres deportes
→ recompensa transversal
```

ni:

```
cross-sport progression
```

La complementariedad existe narrativamente, no necesita todavía una regla operacional compartida.

# 14. Equipos

La temporada puede contener deportes colectivos.

Ejemplo:

```
vóley playa
```

Los participantes pueden formar equipos.

En v0.2:

```
equipo
→ mecanismo de organización de participantes
```

Los reconocimientos permanecen:

```
INDIVIDUALES
```

No inferir todavía:

```
equipo deportivo
=
Group TES
```

No introducir todavía:

```
collective recognition
collective outcome
collective claim
team-owned reward
```

La existencia de equipos constituye una presión real observada por la narrativa, pero su resolución semántica no es necesaria para el primer recorrido individual ejecutado.

Estado:

```
OBSERVED
NOT YET SELECTED
NON-BLOCKING FOR FIRST EXECUTED PATH
```

# 15. Ranking

No implementar ranking global en v0.2.

Para competición basta:

```
mi resultado
+
mi posición
+
mi reconocimiento
```

No se necesita:

```
leaderboard
ranking social
clasificación completa
```

# 16. Recorrido primario del participante

La primera ejecución extremo a extremo utilizará una disciplina.

Candidato:

```
La disciplina seleccionada para el primer recorrido extremo a extremo es:
CARRERA
```

Recorrido mínimo:

```
Temporada
↓
selección de evento
↓
inscripción
↓
selección de modalidad
↓
participación
↓
Evidencia correspondiente
↓
reconocimiento
↓
continuidad / consecuencia
```

Debe poder recorrerse desde una interfaz visible.

# 17. Dos variantes humanas dentro del escenario

La demo debe poder representar al menos dos casos sin convertirlos en segmentos permanentes.

## Caso A — miembro existente / competición

```
miembro del club
↓
elige evento de carrera
↓
elige competición
↓
participa
↓
introduce resultado + posición
↓
obtiene reconocimiento individual
↓
queda disponible una activación relevante
```

## Caso B — participante externo / social-bienestar

```
no miembro
↓
se inscribe
↓
elige modalidad social / bienestar
↓
acredita presencia
↓
declara esfuerzo suave / medio / intenso
↓
obtiene insignia
↓
aparece oportunidad de incorporación al club
```

La demo no necesita ejecutar ambos recorridos completos si hacerlo mezcla variables innecesariamente.

Debe ser posible mostrar el contraste.

# 18. Recorrido principal candidato para v0.2

Por la tesis comercial prioritaria, el recorrido más informativo inicialmente es:

```
PARTICIPANTE EXTERNO
→ EVENTO
→ PARTICIPACIÓN
→ RECONOCIMIENTO
→ OPORTUNIDAD DE CAPTACIÓN
```

Esto permite probar directamente que:

```
evento deportivo
!=
sólo activación para clientes existentes
```

y que puede funcionar como una superficie anterior a la adhesión al club.

El segundo recorrido puede mostrar posteriormente:

```
miembro existente
→ nueva participación
→ continuidad
→ activación comercial / renovación
```

# 19. Momento principal de satisfacción

En v0.2:

```
INSIGNIA
```

debe constituir la consecuencia visible principal tras completar el recorrido.

Debe ser perceptible:

```
qué consiguió
por qué lo consiguió
qué cambia después
```

No basta con incrementar silenciosamente un contador.

# 20. Activación comercial posterior

Después del reconocimiento puede existir una consecuencia comercial contextual.

Ejemplos permitidos:

```
acceso anticipado a colección relacionada
invitación a sesión de mejora
encuentro con figura pública
cupón asociado a nivel
```

No es necesario implementar todas.

Debe escogerse una consecuencia fácil de comprender.

Una candidata especialmente coherente con la narrativa sería:

```
participación recurrente en running
→ acceso anticipado a colección performance running
```

Esta relación constituye una activación contextual.

No debe presentarse como prueba de que el participante necesariamente quiere comprar.

# 21. Cambio de perspectiva

La demo debe contener expresamente un segundo momento.

Después de vivir el recorrido como participante:

```
PARTICIPANT VIEW
↓
PERSPECTIVE CHANGE
↓
MARKETING / CRM VIEW
```

La segunda perspectiva debe permitir comprender qué información y posibilidades ha producido la interacción.

Como mínimo debería poder distinguir:

```
persona
membership status
evento
disciplina
modalidad elegida
participación observada
Evidencia recibida
reconocimiento obtenido
continuidad relevante
oportunidad de captación / activación
```

Esta superficie no debe presentar inferencias no respaldadas como hechos.

# 22. Historia comercial completa

La demostración debe permitir contar aproximadamente:

```
La marca ya tiene un club
y ya organiza eventos deportivos.

Una temporada agrupa distintos eventos y disciplinas.

Las personas pueden participar
aunque todavía no pertenezcan al club.

Cada participante elige cómo quiere participar.

La experiencia no necesita tratar igual
a quien compite
y a quien busca bienestar o dimensión social.

La participación produce evidencia diferente
y puede recibir reconocimiento diferente.

Las participaciones sucesivas crean continuidad
y pueden abrir recorridos Experience.

Para un no miembro,
la relación deportiva crea una oportunidad de captación.

Para un miembro,
la continuidad puede habilitar reconocimiento,
renovación, acceso y activación comercial relevante.

Marketing / CRM puede observar esa relación
sin reducirla a una transacción de compra.
```

# 23. Alcance visual de la primera demo

Debe existir una temporada con tres disciplinas visibles.

Propuesta inicial:

```
TEMPORADA
├── Carrera
├── Vela
└── Vóley playa
```

Sólo Carrera necesita ejecutar completamente el recorrido v0.2.

Vela demuestra variedad de disciplina.

Vóley playa hace visible que existen eventos con equipos, sin obligar todavía a resolver una semántica colectiva completa.

# 24. Fuera de alcance v0.2

No exigir todavía:

```
ranking general
validación externa de resultados
wearables
integraciones deportivas reales
federaciones
GPS
Strava u otras plataformas
cross-sport progression
recompensa colectiva de equipos
Group TES
team-owned result
team-owned reward
modalidades asignadas automáticamente
personalización IA
API productiva
autenticación real
CRM real
inventario real
ecommerce real
redención comercial real
motor genérico de temporadas
motor genérico de Experiences
```

Su ausencia no constituye por sí misma defecto de la primera demo.

# 25. DEMO-AUTHOR UX — objetivo experimental

La expectativa futura es que el creador de demos pueda variar sin programar:

```
marca
temporada
disciplinas
eventos
fechas
modalidades
participantes
estado miembro / externo
Experiences relacionadas
criterios de participación
Evidencia esperada
insignias
trofeos
beneficios
copy
imágenes
recorrido narrativo
```

No se presupone que Demo Factory ya sea capaz de hacerlo.

La construcción v0.2 debe observar:

```
qué puede configurarse
qué exige duplicación
qué exige tocar código
qué relaciones faltan
qué artefactos resultan difíciles de entender
qué operaciones son innecesariamente técnicas
```

Cualquier fricción observada constituye:

```
DEMO-AUTHOR UX Evidencia
```

y no debe corregirse preventivamente antes de observarla.

# 26. PARTICIPANT UX — objetivo experimental

Durante el recorrido deben poder cuestionarse:

```
¿entiendo qué temporada estoy viendo?
¿entiendo a qué evento puedo apuntarme?
¿entiendo qué modalidades existen?
¿entiendo qué implica cada modalidad?
¿entiendo qué tengo que hacer?
¿entiendo qué información estoy aportando?
¿entiendo si he participado correctamente?
¿entiendo por qué recibo una insignia?
¿entiendo qué cambia después?
¿entiendo la relación con el club?
¿entiendo la oportunidad de alta si todavía no soy miembro?
¿percibo continuidad o sólo una campaña aislada?
```

No definir todavía las respuestas correctas de UX.

La finalidad de la demo es permitir desafiarlas.

# 27. Garantías SAFE TO BUILD

Antes de construir, sólo deben considerarse bloqueantes las presiones capaces de invalidar materialmente este experimento.

Garantías mínimas:

```
composition identity preserved
state integrity preserved
participant != automatically customer/member
modality != permanent person classification
Evidencia provenance distinguishable
competitive result != presence != effort
recognition != commercial benefit
no unsupported collective semantics
historical Evidencia not rewritten
experimental behavior not promoted as product capability
```

Las restantes incógnitas pueden continuar abiertas mientras el recorrido pueda producir evidencia útil.

# 28. Presiones observadas pero no automáticamente bloqueantes

```
exact Experience/modalidad cardinality
team semantic identity
external participant → membership conversion mechanism
native browser/device validation
general event engine
general season engine
general reward engine
cross-sport progression
real integrations
ranking
result verification
advanced CRM segmentation
```

Estado:

```
OBSERVED
NOT AUTOMATICALLY BLOCKING
```

Cada una deberá ganarse su condición de blocker respecto del recorrido concreto.

# 29. Única decisión funcional pendiente de v0.2

> ## 29. Decisiones cerradas en v0.2
>
> Respecto de `Demo Definition v0.1`, se cierran exclusivamente dos decisiones situadas:
>
> **Disciplina del primer recorrido ejecutable**
>
> ```
> Carrera
> ```
>
> Las otras disciplinas de la temporada permanecen visibles como parte de la narrativa, pero no necesitan recorrido extremo a extremo en el primer Corte.
>
> **Acreditación de presencia**
>
> ```
> QR / check-in simulado → Evidencia de presencia
> ```
>
> Esta Evidencia representa presencia aceptada dentro de la simulación. No acredita asistencia física real ni una integración QR productiva.
>
> Se mantiene separada de:
>
> ```
> suave / medio / intenso → esfuerzo autodeclarado
> ```
>
> Ninguna otra decisión, alcance o relación de `Demo Definition v0.1` se modifica mediante esta versión.

> ## 29. Decisiones cerradas en v0.2
>
> Respecto de `Demo Definition v0.1`, se cierran exclusivamente dos decisiones situadas:
>
> **Disciplina del primer recorrido ejecutable**
>
> ```
> Carrera
> ```
>
> Las otras disciplinas de la temporada permanecen visibles como parte de la narrativa, pero no necesitan recorrido extremo a extremo en el primer Corte.
>
> **Acreditación de presencia**
>
> ```
> QR / check-in simulado → Evidencia de presencia
> ```
>
> Esta Evidencia representa presencia aceptada dentro de la simulación. No acredita asistencia física real ni una integración QR productiva.
>
> Se mantiene separada de:
>
> ```
> suave / medio / intenso → esfuerzo autodeclarado
> ```
>
> Ninguna otra decisión, alcance o relación de `Demo Definition v0.1` se modifica mediante esta versión.

### 									

# 30. Siguiente gate

No implementar inmediatamente toda la narrativa.

Siguiente operación:

```
DEMO DEFINITION v0.2
↓
SAFE-TO-BUILD REVIEW
↓
¿alguna capacidad necesaria está realmente bloqueada?
```

Si:

```
NO MATERIAL BLOCKER
```

entonces:

```
BUILD FIRST DEMO Corte
```

Si:

```
MATERIAL BLOCKER FOUND
```

entonces únicamente ese bloqueo obtiene derecho a convertirse en:

```
bounded hypothesis
→ experiment
```

No seleccionar automáticamente otra presión histórica.

No abrir H40 sólo porque H39 esté cerrada.