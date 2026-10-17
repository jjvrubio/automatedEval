# Sports Season — smallest buildable slice

Fecha: 2026-09-23. Especificación para una construcción posterior, no implementación. SITUATED / EXPERIMENTAL / LOCAL / NOT PROMOTED. Deriva del [SAFE-TO-BUILD review](sports-season-safe-to-build-review.md) y su input congelado. No abre H40 ni define un protocolo general de demos.

El resultado buscado es que una persona recorra una inscripción a Carrera como participante externo, elija modalidad, registre presencia simulada, declare esfuerzo, vea una insignia explicada y una invitación a conocer el club. Después podrá cambiar a Marketing/CRM y comprobar qué hechos y oportunidad ha producido ese mismo recorrido.

## Corte mínimo

```text
Temporada: Carrera / Vela / Vóley playa
  → evento de Carrera
  → elegir Social o Bienestar y confirmar inscripción
  → check-in simulado
  → declarar esfuerzo: suave / medio / intenso
  → badge individual + motivo
  → invitación al club, sin alta
  → cambiar a Marketing/CRM conservando persona, composición y estado
```

La primera participación produce reconocimiento inmediato al aportar los dos registros exigidos por la política local. La continuidad visible es una participación registrada dentro de una temporada que contiene otros eventos y una invitación a mantener la relación. **No se demuestra todavía segunda participación, booster, acceso a colección ni avance en Experience.** Esos elementos permanecen clasificados en el review; no se anuncian como ejecutados.

## Capacidad reutilizada y trabajo nuevo

Se reutilizan las responsabilidades y piezas demostradas: resolución de composición/marca antes de App; referencias de Scenario/Script; frontera pública de acciones; validación antes de transición; estado local aislado; reset; proyección hacia UI; navegación de perspectivas sobre el mismo runtime. Iconos y estilos existentes pueden servir para la presentación mínima.

Se requiere código situado nuevo para persona/membresía, inscripción con valores, contexto deportivo, recepción de esfuerzo, regla y estado de insignia, oportunidad y proyección CRM. No se promete que insertar un manifest haga funcionar estas capacidades. La rama y el evaluador de Family Adventure no se activarán mediante una referencia semántica deportiva falsa.

La incorporación mantendrá App como consumidor: composición y selección de comportamiento se resuelven antes de renderizar; App no importará fixtures por prospecto ni construirá el proveedor. El mecanismo técnico exacto de integración deberá ser mínimo y local. Esta especificación no pide una arquitectura de providers ni copiar el adaptador entero.

## Archivos y artefactos probablemente implicados

Todas las modificaciones de esta tabla corresponden a una **futura instrucción BUILD**. Esta revisión no las ejecuta.

| Archivo / artefacto | Uso o modificación mínima esperada |
| --- | --- |
| `prototype/src/demo-factory/sports-season-artifacts.ts` — nuevo, nombre orientativo | Marca, temporada, tres eventos, dos personas fixture, modalidades, criterio/versión de badge, copy y declaraciones situadas. Datos separados del estado mutable. |
| `prototype/src/demo-factory/manifests.ts` | Incorporar una composición deportiva, con referencias propias y capabilities honestas. No alterar identidades A/B ni controles Retail/Arrival. |
| `prototype/src/demo-factory/bootstrap.ts` | Resolver los nuevos artefactos y comportamiento; rechazar referencias deportivas incompatibles. El catálogo actual y proveedor único no lo hacen todavía. |
| `prototype/src/demo-factory/contracts.ts` y tipos locales deportivos, si se separan | Ampliación acotada que no obligue al externo a ocupar MemberReadModel; payloads con valores/contexto deportivo y lectura de ambas perspectivas. No cambiar contratos TES/PSC. |
| `prototype/src/demo-factory/sports-season-runtime.ts` — nuevo, nombre orientativo | Comportamiento deportivo local y proyección; validaciones y regla de badge en runtime. Reutilizar frontera/reset/aislamiento existentes, no un motor de reglas. |
| `prototype/src/demo/mock-adapter.ts` | Posible punto de conexión del comportamiento local, según integración concreta. Su evaluación hotelera no constituye la implementación deportiva. Evitar duplicación del archivo completo. |
| `prototype/src/app/App.tsx` y componente deportivo local nuevo | Consumo de perspectiva deportiva, controles de valores, resultado e invitación, cambio a CRM y reset. Ninguna regla factual alojada en el componente. |
| `prototype/src/styles/global.css`, iconos/assets locales | Sólo lo necesario para legibilidad y badge distinguible de beneficio. No hace falta imagen generada, QR real ni nueva biblioteca. |
| Pruebas nuevas junto al módulo deportivo | Recorrido, rechazo/aislamiento, reset, persona externa y diferencias de evidencia; no espejos de copy o de la implementación. |
| Documentación/evidencia nuevas del slice | Fuentes y resultados actuales separados de S01–S39; registro de fricción de autoría y uso humano. |

`main.tsx` ya compone antes de renderizar; no se presupone cambio allí. No se necesitan nuevas ExperienceDefinitions, evaluadores K/cross-subject, navigation framework, motor de temporadas, contratos compartidos ni harnesses históricos reescritos. Si la implementación exige más, deberá explicar la necesidad concreta antes de ampliar el corte.

**Incompatibilidades de shape conocidas que BUILD debe atender explícitamente:** ScenarioDefinition exige experienceRef y bootstrap la resuelve; EvidenceInput no tiene payload de esfuerzo y sólo acepta contextos hoteleros; AppSnapshot/DemoFixture exigen member; App sólo envía step.action predefinida y selecciona la superficie de aventura por guestPerspective. No se omiten estos límites ni se sortean mediante casts, strings vacíos, tipos hoteleros falsos o members ficticios. Un ajuste técnico local debe preservar las distinciones funcionales; su comportamiento tendrá evidencia nueva.

Scenario no necesita fingir una Experience validada: ADR-004 admite referencias cuando correspondan. En este slice no se ejecuta transformación TES ni se establece cardinalidad modalidad/Experience. Si se muestra alguna referencia candidata, será documental, cualificada y ajena a la condición que concede el badge; no es necesaria para el corte mínimo.

## Datos mínimos

Nombres e identificadores siguientes son ilustrativos y sustituibles por configuración situada al construir; no modifican los catálogos existentes.

| Dato | Mínimo y procedencia |
| --- | --- |
| Composición | Un demoId propio, por ejemplo `sports-season-running`, una marca ficticia y referencias versionadas. Sin reutilizar el ID de A/B. |
| Marca | Una cadena ficticia de moda/equipamiento deportivo con club existente. Nombre/logo/tokens simples. |
| Temporada | Un seasonId, título y fechas coherentes declaradas como calendario de demo. |
| Eventos | Tres IDs distintos ligados a seasonId: Carrera ejecutable; Vela y Vóley playa informativos, claramente sin recorrido disponible. Fecha y disciplina por evento. Temporada no es el evento de Carrera. |
| Persona ejecutada | Un subject/person ID estable, nombre ficticio y `membershipStatus: external` explícito. La relación como cliente queda no establecida, no se deduce de participación. |
| Persona de contraste | Otro ID, nombre y `membershipStatus: member` declarado por fixture. Caso informativo, sin acciones ni hechos deportivos fingidos. No es un segundo actor en la sesión ejecutada. |
| Modalidades | Social y Bienestar elegibles en Carrera; la elección se guarda con la inscripción a ese evento. Competición sólo en contraste conceptual posterior. |
| Inscripción | ID, personRef, eventRef, modalidad elegida y estado local; seasonRef se conserva o resuelve desde catálogo. No implica pertenencia al club. |
| Evidence | Dos registros distintos: check-in simulado y esfuerzo autodeclarado; IDs, tiempos, origen, sujeto y evento; esfuerzo con valor explícito. Sin interpretación TES. |
| Badge | ID y nombre, por ejemplo «Primera Carrera», motivo, regla local versionada, personRef/registrationRef y referencias a ambas Evidence. No es cupón ni trofeo. |
| Oportunidad | Invitación situada al club dirigida al externo después del badge. Separada del reconocimiento; ninguna prueba de intención de compra ni alta. |
| Continuidad | Primera participación registrada; los otros eventos pertenecen a la misma temporada. Sin participación previa inventada ni contador presentado como TES Progression. |

No se necesita contacto real, dato sensible, credencial, CRM externo, persistencia entre recargas ni estado multiusuario. Los hechos comunicados son de simulación local; sus fuentes deben ser visibles en términos comprensibles.

## Acciones mínimas y dueño del estado

| Acción | Input y precondición | Cambio permitido en runtime | Lo que no produce |
| --- | --- | --- | --- |
| Confirmar inscripción | Persona simulada externa; evento Carrera disponible; una modalidad elegida por la persona usuaria | Registro de inscripción persona+evento+modalidad | Ni Evidence de presencia, ni badge, ni membresía |
| Simular check-in | Inscripción vigente del mismo sujeto/evento | Una Evidence de presencia, origen explícitamente simulado | Ni esfuerzo, ni resultado competitivo, ni verificación física |
| Declarar esfuerzo | Presencia recibida para esa inscripción; valor suave/medio/intenso seleccionado | Evidence de esfuerzo separada; evaluación de la regla local; badge y oportunidad si corresponde | Ni medición objetiva, ni clasificación permanente, ni alta automática |
| Ver información del club | Oportunidad disponible | Mostrar información de la invitación; no necesita mutación de negocio | Ni consentimiento, ni solicitud enviada, ni conversión |
| Cambiar participante/CRM | Misma composición y runtime | Sólo perspectiva de presentación | No nuevas acciones de negocio, reset, cambio de persona o reenlistment |
| Reiniciar | Demo local | Recuperar estado inicial; eliminar inscripción, registros de esta ejecución, badge y oportunidad | No modifica otras composiciones ni historia S01–S39 |

Cambiar un select antes de confirmar sólo cambia el formulario. Las transiciones aceptadas y la fuente factual residen en runtime. El Script puede orientar al presentador, pero no fijar silenciosamente la respuesta de modalidad/esfuerzo cuando se promete elección a la persona.

## Evidence y regla del reconocimiento

| Clase | Qué se conserva | Alcance del hecho |
| --- | --- | --- |
| Presencia | Registro de check-in con sujeto/evento/inscripción, tiempo y origen `simulated-check-in` o equivalente explícito | Presencia aceptada dentro de la simulación; no prueba asistencia física real ni integración QR |
| Esfuerzo | Registro separado con valor suave/medio/intenso y origen `participant-self-report` en la simulación | Declaración recibida para esa participación; no valida presencia, rendimiento ni bienestar |
| Resultado competitivo | Ninguno en el recorrido primario | El contraste describe futura entrada de resultado+posición sin validación externa; no la mezcla con los registros anteriores |

El criterio local propuesto es: **inscripción aceptada + presencia simulada + un esfuerzo válido declarado para la misma persona y el mismo evento → una insignia individual de participación**. Los tres niveles satisfacen el mismo criterio; no se valora a la persona ni se infiere intención comercial desde intensidad. La versión de la regla y las Evidence que la sustentan se conservan con el reconocimiento.

Este criterio es una **decisión de producto situada propuesta para BUILD**, no una capacidad demostrada del evaluador actual, una condición universal de deporte o una derivación TES. La explicación visible debe decir qué registro se recibió y por qué la política concede la insignia. La UI no creará un badge sólo por llegar a una pantalla o por coincidir con un texto del Script.

Antes de cumplir la regla, mostrar requisitos pendientes de esta simulación; no afirmar que la persona no haya participado en el mundo real. El check-in por sí solo no concede la insignia de este recorrido, y el esfuerzo por sí solo tampoco.

## Estado y superficies mínimas

Un único estado local reseteable basta. Puede describirse mediante cuatro posiciones de demo: disponible; inscripción aceptada; presencia recibida; esfuerzo recibido con reconocimiento. Son posiciones operacionales, no TES Progression/Completion/Result. Los registros y sus referencias explican cada posición; un contador o un texto no sustituyen a esos datos.

Sólo se necesitan dos superficies:

1. **Participante.** Cabecera de temporada y marca; tres disciplinas/eventos visibles; Carrera con inscripción y elección; pasos de presencia y esfuerzo; badge con motivo; invitación al club y continuidad de temporada. Nombre de persona simulada y condición externa visibles sin simular sesión autenticada. Vela/Vóley se distinguen como informativos. El check-in se nombra simulado.
2. **Marketing/CRM.** La misma persona y la misma inscripción: pertenencia al club, temporada, evento, disciplina, modalidad, presencia y esfuerzo con sus orígenes, reconocimiento y criterio, continuidad realmente registrada y oportunidad de captación. Distinguir datos de fixture, acciones registradas y decisión comercial. No mostrar «convertido», «interesado en comprar» o «esfuerzo verificado».

El cambio de perspectiva puede usar dos vistas o un control dentro de una ruta. Debe conservar el runtime efectivo y su estado. No se requiere nueva relación de navegación; tampoco debe pasar por el enlace genérico que entra en Family Adventure. Si se usa URL, mantener identificador efectivo coherente. Recargar puede reiniciar la simulación, con ese límite visible; cambiar de vista no debe hacerlo.

## Contraste miembro / competición

Un caso estático de contraste basta: persona que ya pertenece al club, Carrera, modalidad competición situada, futura entrada de resultado y posición y reconocimiento individual. Debe rotularse como caso de diseño, sin registros ni consecuencias supuestamente observados.

El diseño primario conserva las separaciones que ese caso necesitará: persona independiente de membership; inscripción independiente de modalidad permanente; registro competitivo separado de presencia/esfuerzo; reconocimiento independiente de beneficio. Elegir social/bienestar en un evento no impide competir en otro. Esto es compatibilidad conceptual inspeccionada, **no ejecución ni demostración del segundo recorrido**.

## Resultado observable y comprobaciones de BUILD

El observable central será: después de tres acciones aceptadas hay una inscripción, dos Evidence distinguibles, una insignia atribuida con motivo y una oportunidad de alta; la persona **sigue siendo externa**. Marketing/CRM ve esos mismos datos. Un reset vuelve al estado inicial.

Comprobaciones acotadas que justificarán enseñar la nueva demo:

- Social y Bienestar producen inscripciones con su elección real; suave/medio/intenso se conservan como valores declarados, sin alterar la modalidad ni la persona.
- No se obtiene badge antes de reunir los requisitos; repetir la última acción no duplica insignias o registros. Acción desconocida, orden inválido, sujeto/evento distinto y valor inválido se rechazan sin mutación.
- Inscripción no cuenta como presencia; presencia no cuenta como esfuerzo; ningún resultado competitivo se fabrica. Cambiar labels, nombre mostrado o copy no cambia hechos, atribución ni elegibilidad.
- El estado de membresía permanece external durante inscripción, check-in, esfuerzo, reconocimiento, invitación y cambio a CRM. La persona de contraste no recibe acciones o recompensas del externo.
- Persona/evento/evidencias que justifican el badge coinciden con los aceptados por runtime. La proyección no reconstruye estas relaciones desde Activity ni desde títulos.
- Cambiar perspectiva conserva identidad efectiva, proveedor/estado y resultado; un snapshot devuelto no permite mutar el estado interno; reset restaura todo el estado local y no modifica Retail/Arrival/A/B.
- Inspección en navegador del recorrido nuevo, incluido error legible y reset, seguida de uso humano. El resultado se registrará como evidencia nueva; DOM/test no sustituye comprensión humana.

Las pruebas históricas no son un gate indiferenciado para código nuevo: H37 y el control de preservación H39 fijan bytes de la baseline recibida. El trabajo posterior debe conservar una copia identificada de esa baseline para su replay y registrar por separado validación del slice sobre fuentes nuevas. No se autoriza cambiar expectativas o hashes históricos para conseguir verde ni presentar tests excluidos como aprobados. Este review no crea ni modifica esa infraestructura.

El intento de suite de esta revisión falla por firma nativa de Rolldown con el Node disponible. La ejecución futura necesita un entorno compatible antes de anunciar resultados nuevos. No se requiere un rediseño del producto para resolver ese límite ambiental.

## Exclusiones explícitas

Quedan fuera: recorrido competitivo ejecutado, trofeos concedidos, leaderboard, resultados/equipos colectivos, TES Group, claim cross-subject, lógica entre deportes, segunda participación ejecutada, booster/Progression/Completion/Result TES, acceso anticipado condicionado a recurrencia, motor de recompensas, correspondencia general modalidad–Experience, editor no-code, identidad/auth real, alta real de club, envío de leads, CRM/API/ecommerce reales, QR/cámara real, validación organizador/federación/wearable y persistencia productiva.

La consecuencia comercial del corte es **captación potencial mediante invitación**, no beneficio económico concedido. La narrativa de recurrencia y activación de miembros permanece disponible para una iteración posterior; no se convierte ahora en una promesa operativa.

## Preguntas de UX que deben seguir abiertas

- ¿Distingue la persona temporada y evento? ¿Entiende que Vela y Vóley pertenecen al programa pero no se ejecutan en este slice?
- ¿Comprende Social/Bienestar como elecciones para esta participación y sabe qué hacer a continuación?
- ¿Entiende que check-in simula presencia y que esfuerzo es una declaración diferente? ¿Qué cree que ha quedado verificado?
- ¿Identifica la insignia, su motivo y qué cambia después? ¿La confunde con un cupón o un premio competitivo?
- ¿Comprende que aún no pertenece al club, que participar era posible sin pertenecer y que la invitación requiere otra decisión?
- ¿Percibe continuidad suficiente o sólo una campaña aislada? Esa respuesta decidirá si merece construir recurrencia/booster.
- ¿Marketing/CRM distingue datos conocidos, declaraciones y oportunidades, sin inferir intención de compra?
- ¿Qué necesita editar el creador para variar marca, fechas, personas, copy o criterios? Registrar campos confusos, ediciones de código y duplicación efectivamente necesaria; no resolver preventivamente un editor general.

La siguiente instrucción podrá ordenar esta construcción pequeña y reversible. Esta entrega sólo fija su alcance y condiciones observables; no implementa la demo ni abre H40.
