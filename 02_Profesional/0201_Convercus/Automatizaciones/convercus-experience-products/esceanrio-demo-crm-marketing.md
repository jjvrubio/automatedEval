Sí. Me parece una evolución importante y, además, bastante más creíble que inventar una superficie Marketing/CRM completamente separada.

La clave sería que la demo dejara de parecer «un prototipo de eventos» y empezara a parecer una **extensión situada del ecosistema Convercus**. En la v0.3 ya hemos establecido que Web y App deben compartir el mismo estado funcional del usuario —persona, condición de cliente/miembro, transacciones, intención, inscripción, Evidencias, reconocimiento—, mientras Marketing/CRM sigue expresamente pendiente de diseño.  

Yo lo concebiría así:

**Self Service no sería otra demo paralela. Sería una superficie real de continuidad.**

El usuario podría pasar desde la experiencia deportiva hacia algo reconocible como Convercus Self Service y encontrar allí, según corresponda:

* sus puntos y nivel;
* sus insignias;
* cupones;
* noticias;
* Experiences;
* otros beneficios;
* eventualmente alguna representación de su actividad o progresión.

Y, desde la perspectiva Marketing/CRM, podríamos mostrar que estamos trabajando sobre **la misma identidad y el mismo estado**, no sobre una persona inventada específicamente para el escenario deportivo.

La conexión REST que propones me parece la forma correcta de plantearlo, con una precaución arquitectónica importante: **yo no acoplaría la demo directamente a la API de Self Service**.

Introduciría una pequeña capa de adaptación:

```text
Demo Factory
        │
        ▼
Convercus Data Adapter
        │
        ├──── modo demo / fixture
        │
        └──── API REST Convercus
                        │
                        ▼
                 Self Service / datos
```

De ese modo el contrato de la demo podría pedir algo conceptualmente estable como:

```text
persona
perfil de fidelización
saldo de puntos
nivel
insignias
cupones
noticias
Experiences
```

sin hacer que cada demo conozca los detalles concretos de autenticación, endpoints, nombres de campos o versiones de la API de Convercus.

Esto nos da algo especialmente valioso para la Factoría: **la misma demo podría funcionar con datos ficticios o con datos reales**, sin cambiar su semántica.

Para una presentación comercial tendríamos dos estados posibles:

```text
MODO DETERMINISTA
fixtures locales
→ demo siempre reproducible

MODO CONECTADO
API REST Convercus
→ continuidad real con Self Service
```

Y esto también protege el experimento. Si mañana la API no está disponible, la demo no deja de funcionar.

Hay otra consecuencia que me parece todavía más interesante. Hasta ahora hemos pensado mucho el plano usuario como recorrido:

```text
persona
→ evento
→ participación
→ Evidencia
→ insignia
```

Con Self Service aparece la continuidad:

```text
persona
→ evento
→ participación
→ Evidencia
→ insignia
→ Self Service
→ patrimonio de relación con la marca
```

Ahí la insignia deja de ser simplemente el «momento final bonito» de la demo. **Pasa a formar parte del estado persistente del cliente**, junto a puntos, nivel, cupones, Experiences, etc.

Y al otro lado:

```text
Self Service / persona
              ↕
      estado compartido
              ↕
     Marketing / CRM
```

Eso sí empieza a transmitir algo importante de Convercus: no estamos construyendo una aplicación aislada para gestionar una carrera, sino que el evento se integra en la relación de fidelización ya existente.

Hay una decisión que **no cerraría todavía**: cuánto escribimos de vuelta hacia Convercus. Para la primera integración, tendería a:

```text
API Convercus
→ lectura real

acciones demo
→ estado local controlado
```

y sólo después estudiar:

```text
acciones demo
→ escritura real vía API
```

Porque escribir puntos, insignias, cupones o estado de una Experience ya introduce consecuencias bastante mayores: autenticación, permisos, idempotencia, rollback, contaminación de datos de demo, etc.

Así que mi propuesta sería que la revisión Marketing/CRM partiera ya de un nuevo principio:

> **La demo deportiva debe poder presentarse como una extensión situada de Convercus Self Service, compartiendo identidad y estado de fidelización, con posibilidad futura de alimentarse mediante API REST sin hacer depender la ejecución de la demo de esa conexión.**

Y creo que esto cambia bastante cómo debemos revisar Marketing/CRM: ya no deberíamos preguntarnos sólo **«qué panel queremos enseñar»**, sino **«qué ve Marketing/CRM de la misma persona y de la misma actividad que el usuario acaba de ver en Self Service»**.

Ahí sí tenemos una continuidad narrativa y técnica mucho más potente.

---

Sí, pero distinguiría dos niveles.

Para **diseñar bien la continuidad con Self Service**, no necesito todavía acceso operativo a la API. Podemos definir desde ya el contrato funcional que la demo necesita: identidad de usuario, transacciones, puntos, nivel, insignias, cupones, noticias y Experiences. Con eso podemos construir un adaptador y fixtures coherentes.

Para **conectar de verdad la demo con Convercus**, sí necesitaré al menos la documentación de la API REST y ejemplos reales de payloads. Idealmente: endpoints disponibles, autenticación, modelo de usuario, transacciones, loyalty balance, niveles, insignias, cupones, Experiences y cualquier restricción de lectura/escritura. Si queremos probar contra entorno real, entonces además credenciales o un entorno sandbox/controlado. Yo empezaría sólo con lectura.

Y sí: las **transacciones comerciales simuladas son imprescindibles**. Sin ellas, el escenario «cliente conocido / no miembro» pierde credibilidad, porque no podemos mostrar ni historial ni el contrafactual de lo que habría obtenido en el programa.

Yo introduciría un pequeño historial transaccional por persona, por ejemplo:

* Cliente no miembro: 5–8 compras en distintas fechas, categorías y tickets.
* Cliente miembro: historial similar, pero con puntos realmente acumulados, nivel y quizá algún cupón derivado.
* No cliente: sin historial previo.

Cada transacción debería tener al menos:

```text
transaction_id
customer_id
date
store/channel
amount
currency
items/category
```

Y para el miembro, además, podríamos derivar:

```text
points_earned
tier_effect
coupon_eligibility
badge_or_experience_effect
```

Para el cliente no miembro haríamos el cálculo paralelo:

```text
historial real de compras
        ↓
reglas del programa
        ↓
resultado contrafactual
```

Eso nos permite mostrar algo mucho más creíble:

> «Has comprado 428 € en los últimos 6 meses. Si hubieras pertenecido al programa, habrías acumulado 428 puntos y alcanzado el nivel X.»

Sin falsear que esos puntos existan realmente.

Además, conviene separar dos cosas desde arquitectura:

```text
COMMERCE DATA
transacciones observadas

LOYALTY STATE
puntos, nivel, cupones, insignias, Experiences
```

Así evitamos que la demo trate el estado de fidelización como una propiedad inventada independiente de la actividad comercial.

Mi recomendación sería que el siguiente paso no fuese aún «conectar la API», sino **definir el contrato mínimo de datos y el juego de transacciones simuladas**. Después podremos mapear ese contrato contra la API REST real de Convercus y ver qué viene directamente, qué debe derivarse y qué requiere adaptación.
