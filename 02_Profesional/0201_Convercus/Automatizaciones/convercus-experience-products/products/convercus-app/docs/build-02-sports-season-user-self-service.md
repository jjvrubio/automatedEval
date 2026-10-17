**BUILD 02 — Sports Season · plano usuario y continuidad Self Service**

Fecha: 30 de septiembre de 2026. Estado: **COMPLETE · USER / SELF SERVICE READY FOR HUMAN CHALLENGE**. La aceptación humana de claridad y utilidad está pendiente.

[Abrir Web local](http://127.0.0.1:4173/?demo=sports-season-running) · [Abrir App](http://127.0.0.1:4173/showcase?demo=sports-season-running). Si el servidor está detenido, ejecutar [Abrir demo.command](../prototype/Abrir%20demo.command) y mantener su terminal abierta.

**1. Baseline previo**

Se continúa desde el árbol de trabajo recibido, que ya contenía BUILD 01, Visual Delta 01 y una implementación anterior del plano usuario de BUILD 02. Esta última tenía selección de personas, QR de inscripción, intereses, información voluntaria e incentivo, pero utilizaba compras ilustrativas y cifras anteriores: 194 puntos contrafactuales para Lea y 860 puntos / Activo para Diego. No contenía esta continuidad Self Service.

HEAD de referencia: `66b2465c7fd47087aa9b4d69289dec166d2b4e73`. Había numerosas modificaciones y archivos sin seguimiento previos; no se restablecieron ni se incluyeron cambios ajenos. Se guardaron [hashes de partida](evidence/build-02-self-service/baseline-hashes.json) y una [ejecución completa previa](evidence/build-02-self-service/baseline-tests.json): 150 pruebas, 131 PASS y 19 FAIL.

La autorización de construcción procede de la instrucción BUILD 02 de esta sesión. Sustituye, para este corte, la restricción de no construir que conserva el cierre histórico de v0.3. No se ha reescrito esa definición.

**2. Datasets consumidos**

Se consumen `sports_season_transactions_v0_1.csv`, situado en la raíz del proyecto Convercus Experience Products, y `sports_season_loyalty_dataset_v0_1.json`, recibido en la raíz del workspace de automatizaciones. Las copias empaquetadas en `prototype/src/demo-factory/sports-season/data/` son idénticas byte a byte a las fuentes, incluido el BOM y los finales de línea del CSV. Los hashes y la comprobación están en [preservation-check.json](evidence/build-02-self-service/preservation-check.json).

El dataset no contiene nombres. La configuración situada conserva Lea Martín para P01, Diego Vidal para P02 y Persona sin identificar para P03, con los datos ficticios de contexto anteriores. Esos nombres no se presentan como información deducida de las compras.

**3. Consistencia de datos**

La validación inicial se realizó antes de incorporar los datos al producto, con suma decimal de los importes y comparación de identificadores. El adaptador vuelve a validar en cada carga. [Resultado de fixtures](evidence/build-02-self-service/fixture-validation.json):

| Persona | Transacciones | Gasto | Membresía | Saldo real de la demo | Nivel real |
| --- | ---: | ---: | --- | --- | --- |
| P01 | 8 | 511,75 € | non_member | null | null |
| P02 | 8 | 731,20 € | active | 731 | Pro |
| P03 | 0 | 0,00 € | non_member | null | null |

P01 tiene exclusivamente una proyección de 511 puntos potenciales / Active, con `credited: false`. Se comprueban cabeceras, importes de línea, cantidades, fechas, canales, moneda, identificadores duplicados, referencias de persona, membresías, niveles, sumas CSV/JSON y referencias/base/regla del contrafactual. Las pruebas negativas introducen discrepancias y verifican que se detiene la carga. No se reconcilian ni corrigen silenciosamente los fixtures.

El saldo de P02 se toma del JSON. La interfaz no lo calcula a partir de sus compras. Los importes comerciales se representan en céntimos y su acumulado se deriva al proyectar el estado.

**4. Contrato normalizado y frontera**

`relationship-contract.ts` define `SportsDataAdapter`, `NormalizedSportsData`, `Person`, `CommerceTransaction`, `LoyaltyState`, `LoyaltyCounterfactual`, `RelationshipBadge`, `Coupon`, `NewsItem` y `ExperienceSummary`.

`FixtureAdapter.load()` interpreta y valida CSV/JSON y entrega ese contrato. El bootstrap conecta su resultado al provider deportivo. Los componentes reciben `SportsSnapshot` y su proyección `PersonRelationship`; no importan archivos de datos, ni el adaptador, ni esquemas físicos.

`CommerceTransaction` describe compras observadas; no es un movimiento de puntos. `hypotheticalPoints / hypotheticalLevel` son distintos de `pointsBalance / actualLevel`. `ExperienceSummary` es una proyección local para Self Service, sin redefinir TES Experience.

Las reglas de euro completo, redondeo, niveles y beneficios permanecen en los datos y en la validación situada de este adaptador. No se han promovido al núcleo semántico de Demo Factory. Se mantiene la compatibilidad del runtime con los fixtures anteriores para sus pruebas; la composición vigente usa los datos normalizados.

Un futuro adaptador de lectura podrá entregar el mismo contrato. No se ha definido ni implementado `ConvercusAdapter`, autenticación, endpoints o schemas REST. El bootstrap actual carga datos locales de forma síncrona; una fuente remota requerirá decidir posteriormente su ciclo de carga.

**5. Archivos modificados y añadidos**

Se modificaron seis archivos existentes de producto:

- `prototype/src/demo-factory/bootstrap.ts`: composición del adaptador y provider.
- `prototype/src/demo-factory/sports-season/contracts.ts`: proyección de relación y procedencia `user_declared`.
- `prototype/src/demo-factory/sports-season/runtime.ts`: relación normalizada, continuidad por persona y proyección de insignias/Experiences.
- `prototype/src/app/SportsUserPanels.tsx`: identificadores P01–P03, compras y fidelización normalizadas.
- `prototype/src/app/SportsSeasonApp.tsx`: navegación Self Service y acceso desde la insignia.
- `prototype/src/styles/sports-season.css`: historial, perfil, contenidos y adaptación móvil de Self Service; corrección local de visibilidad del enlace de accesibilidad cuando no tiene foco.

Se añadieron `relationship-contract.ts`, `fixture-adapter.ts`, los dos datasets empaquetados, `SportsRelationshipPanels.tsx`, `self-service.test.ts`, `self-service-ui.test.tsx`, este informe y la carpeta de evidencias `build-02-self-service/`.

No se modificaron las pruebas anteriores, los informes BUILD 01 / BUILD 02 usuario previo / Visual Delta 01, v0.2/v0.3, S01–S39, SAFE-TO-BUILD, ADR, TES/PSC ni las guardas históricas. Se verificaron 717 archivos históricos y de contratos sin cambios. Se excluyó únicamente metadata de Finder `.DS_Store` de esa comparación.

**6. Recorrido P01**

Elegir a Lea Martín muestra P01, cliente conocido y no miembro, las ocho transacciones con producto, fecha, canal, categoría, cantidad e importe, y el gasto acumulado. El bloque de fidelización muestra ausencia de saldo/nivel y la simulación de 511 puntos / Active con su advertencia de ausencia de derechos adquiridos.

El QR de inscripción reconoce a P01 sin repetir su nombre. Participar sitúa Carrera, presenta las cuatro recomendaciones configuradas y permite elegir Social o Bienestar. Después de confirmar, la persona puede compartir frecuencia/objetivo y abrir la guía, o continuar sin responder. Check-in y esfuerzo generan evidencias distintas. La insignia Primeros kilómetros aparece como reconocimiento de Sports Season y ofrece acceso directo a Self Service.

En Self Service se conservan no membresía, compras, contrafactual, Experience abierta, noticias y oportunidad informativa de conocer Brisa Club. La nueva insignia aparece allí sin puntos retroactivos. [Compras y contrafactual](evidence/build-02-self-service/browser-final/p01-commerce-counterfactual.png) · [Self Service P01](evidence/build-02-self-service/browser-final/p01-self-service.png).

**7. Recorrido P02**

Diego Vidal muestra P02, cliente conocido y miembro activo, ocho compras / 731,20 €, saldo de 731 puntos y nivel Pro. Self Service presenta los dos cupones/beneficios del fixture, Constancia deportiva, Explorador multideporte, tres noticias y las tres Experiences asignadas, incluida Vóley playa Sunset Session en estado Inscrito.

Después de Carrera, Self Service presenta tres insignias: las dos anteriores y Primeros kilómetros. Su saldo, nivel y cupones se mantienen; el evento aparece Completado en la proyección de Experiences. [P02 antes de participar](evidence/build-02-self-service/browser-final/p02-self-service-before.png) · [P02 con la nueva insignia](evidence/build-02-self-service/browser-final/p02-self-service-new-badge.png).

**8. Tratamiento de P03**

P03 está visible desde la selección inicial. El QR informa de que no reconoce a la persona. Un nombre ficticio mínimo permite completar el mismo recorrido deportivo sin convertirla en cliente ni miembro. En la comprobación se utilizó Alex Demo.

Self Service conserva ese nombre, ausencia de historial comercial, saldo y nivel, y muestra noticias y la insignia obtenida. Identificación completa, alta y consentimiento permanecen narrados. [P03 en Web estrecha](evidence/build-02-self-service/browser-final/p03-self-service-narrow-web.png).

**9. Continuidad Self Service**

La navegación cambia la superficie de presentación, no el provider. La insignia nueva se proyecta desde la inscripción y las evidencias del runtime, con persona, evento, inscripción y referencias de apoyo. No se escribe otra copia independiente de la insignia para Self Service.

El provider guarda el recorrido inactivo de cada persona y restaura su intención, datos declarados, inscripción, evidencias e insignia al seleccionarla otra vez. El recorrido activo tiene un único propietario; no queda una segunda copia activa en el mapa. Reiniciar demo borra todos los recorridos de sesión y conserva los fixtures originales.

Las Experiences deportivas se proyectan como Inscrito, En curso y Completado según inscripción, presencia y reconocimiento. Los estados disponibles/inscritos del JSON se conservan. No se crea `DashboardState`, ni se introduce progresión TES.

**10. Pruebas y verificación histórica separadas**

[Comandos y resultados finales](evidence/build-02-self-service/final-checks.json):

| Comprobación | Resultado |
| --- | --- |
| TypeScript | PASS |
| ESLint | PASS |
| Pruebas vigentes de Sports Season | 63 PASS / 0 FAIL |
| Compilación Vite y PWA | PASS |
| Suite completa, incluidos controles antiguos | 158 PASS / 21 FAIL |

Las 63 pruebas seleccionadas incluyen 29 nuevas de datos, continuidad y DOM real, más las 34 pruebas anteriores de runtime deportivo y plano usuario. Cubren las tres personas, contrafactual sin crédito, referencias y discrepancias, QR, intereses sin hechos deportivos, información aportada/omitida, incentivo, recomendaciones, evidencia inválida, estados de Experience, insignia, conservación entre personas y reinicio. [Resultado vigente](evidence/build-02-self-service/current-tests.json).

La suite completa conserva los 19 fallos de partida: 18 controles históricos y una prueba UI de BUILD 01 cuya entrada precede a la selección de persona/intención. Aparecen además dos incompatibilidades explícitas de las pruebas UI de la entrega anterior: esperan 194 puntos potenciales y 860 puntos / Activo. Esas fuentes y expectativas no se alteraron ni se excluyeron de `npm test`. Las nuevas pruebas DOM comprueban 511 / Active y 731 / Pro. [Comparación por nombre](evidence/build-02-self-service/suite-comparison.json) · [Suite completa](evidence/build-02-self-service/full-tests.json).

Por tanto, **`npm test` y `npm run check` no se declaran globalmente verdes**. La verificación del producto actual se ejecuta explícitamente con:

```bash
npx vitest run src/demo-factory/sports-season/self-service.test.ts src/demo-factory/sports-season/self-service-ui.test.tsx src/demo-factory/sports-season/runtime.test.ts src/demo-factory/sports-season/user-plane.test.ts
```

Ejecutar desde `prototype/` con Node 24 y las dependencias locales ya instaladas. No se han cambiado dependencias.

**11. Browser challenge y revisión visual**

Se ejecutó [browser-challenge.mjs](evidence/build-02-self-service/browser-challenge.mjs) con Playwright y Edge instalado, en segundo plano, perfil temporal y servidor local. La herramienta del navegador integrado no estaba disponible; no se atribuye a ella esta verificación.

[Resultado final](evidence/build-02-self-service/browser-final/report.json): **16 estados comprobados, 8 comparaciones Web/App idénticas, 0 errores de página, 0 errores de consola, 0 solicitudes externas y 0 desbordamientos horizontales en los estados inspeccionados**.

Se completaron P01 con información voluntaria/incentivo, P02 omitiéndola, P03 con formulario mínimo, y la rama independiente de información. Se comprobaron borradores entre superficies, nueva insignia en Self Service, conservación del recorrido de P01 tras completar P02, y ausencia de inscripción/insignia nueva al declarar intereses.

Escritorio: 1280 × 960. Marco App: viewport móvil del prototipo. Web estrecha: 390 × 844. Las capturas se inspeccionaron visualmente. La primera pasada funcional ya fue PASS; reveló en las capturas una superposición del enlace Saltar al contenido. Se corrigió su ocultación sin foco únicamente dentro de Sports Season y se repitió la verificación. Se conserva también [la primera pasada](evidence/build-02-self-service/browser-attempt-1/report.json). [Self Service en App](evidence/build-02-self-service/browser-final/p01-self-service-app.png).

Esto acredita la ejecución local comprobada, no una revisión humana ni una App nativa/Safari/iOS.

**12. Estado Web / App / Self Service**

Las tres superficies consumen el mismo estado. Web y App mantienen presentaciones distintas mediante el marco móvil/portal existente. Se conservan persona, condición comercial, membresía, puntos, nivel, compras, intención, declaraciones, inscripción, evidencias e insignias al navegar dentro de la misma pestaña.

La persistencia es en memoria durante la sesión: recargar o abrir otra pestaña crea otra ejecución. No hay sincronización entre dispositivos ni almacenamiento remoto. El selector de persona está en Participante; desde Self Service se vuelve a la temporada para cambiar de persona.

**13. Elementos todavía narrados**

Siguen narrados o fuera del corte: alta en Brisa Club, autenticación, CRM real, consentimientos productivos, comunicaciones, QR/cámara físicos, canje de cupones, inscripción operativa en las Experiences de contenido, ecommerce, inventario, precios productivos, personalización automática, competición/resultados, Vela y Vóley ejecutables, equipos, segunda participación/refuerzo y progresión TES. La guía es un incentivo editorial local; no es insignia, cupón ni saldo.

**14. Diferencias respecto de v0.3 y concreciones**

Este delta incorpora la continuidad Self Service solicitada después de la definición v0.3. Los datasets sustituyen las cifras ilustrativas de la implementación recibida. Los nombres y el contexto ficticio conocido se conservan mediante una asignación situada a P01–P03.

La información voluntaria se concreta en frecuencia y objetivo, después de inscribirse; el equipamiento se muestra al elegir Carrera. La guía de 5 km sigue siendo el incentivo configurado. El evento ejecutable sigue siendo Kilómetros en compañía / 5 km; la noticia y la Experience 10K del dataset son contenidos distintos, no un cambio de distancia de ese evento.

Seleccionar otra persona ahora conserva su recorrido anterior durante la sesión. Los estados en castellano de Experiences corresponden a `available/enrolled/active/completed`. No se identifica un requisito ejecutable del corte solicitado pendiente; las capacidades narradas se distinguen en la interfaz y aquí.

**15. Fricciones UX para revisión humana**

El historial abierto con ocho compras alarga la página, especialmente en App; puede plegarse. Selección, relación comercial, intención, evento y recorrido siguen en una página larga. La navegación Marketing/CRM ocupa una segunda línea en móvil. Cambiar de persona exige volver desde Self Service a la temporada.

La intención permanece fijada durante el recorrido: para probar la otra rama de esa misma persona hay que reiniciar. Continuar sin información requiere una acción explícita. Cambiar Web/App puede reiniciar desplazamiento o desplegables nativos, aunque mantiene datos y borradores.

Noticias, beneficios, simulación y procedencia aportan bastante texto. Las recomendaciones son iguales para todas las personas de Carrera. La utilidad, claridad del contrafactual y posible presión comercial quedan para revisión de Juan. La rama de información registra intereses sin recoger un canal de contacto ni prometer un envío.

**16. Presiones arquitectónicas observadas**

La separación de adaptador y contrato permite sustituir la procedencia sin llevar CSV/JSON a la UI. Introducir una lectura remota requerirá decidir carga asíncrona, errores y refresco de datos, con lectura antes de cualquier escritura.

La conservación de recorridos por persona mejora la continuidad dentro de la demo, pero no constituye persistencia productiva ni un modelo general de múltiples eventos. El doble uso de ciertas pruebas antiguas como evidencia y como puerta del producto vigente continúa produciendo fallos esperados; necesita una decisión posterior de mantenimiento. No se reescribieron guardas ni se abrió H40 para resolverlo.

El cuerpo de Marketing/CRM permanece sin rediseño ni nuevas funcionalidades. Los nuevos tipos y datos sólo llegan a través del estado compartido necesario para la compatibilidad existente.

**17. Confirmación REST y cierre**

**No hubo conexión REST real con Convercus ni escritura externa.** El adaptador lee archivos empaquetados; las acciones se ejecutan en memoria. La inspección de navegador registró cero solicitudes a destinos externos. No se inventaron endpoints, autenticación ni schemas REST.

`BUILD 02 → COMPLETE`

`USER / SELF SERVICE → READY FOR HUMAN CHALLENGE`

**STOP.** No se inicia rediseño Marketing/CRM, BUILD 03, H40, integración REST ni v0.4. El siguiente paso es la revisión humana del plano usuario y Self Service.
