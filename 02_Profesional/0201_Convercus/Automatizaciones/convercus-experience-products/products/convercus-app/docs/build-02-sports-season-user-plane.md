# BUILD 02 — Sports Season / plano usuario

Fecha: 24 de septiembre de 2026. Estado: **implementado y comprobado para revisión humana del nuevo plano usuario**. La suite global conserva fallos detallados más abajo; no se declara una puerta de calidad global verde ni aceptación humana.

## Alcance y autoridad

Delta local de BUILD 01 + Visual Delta 01 según `Demo definition v_0_3.md` y la [instrucción BUILD 02 recibida](evidence/build-02/instruction.md). Esta última autoriza expresamente construir ahora el plano usuario y mantener pendiente Marketing/CRM. Prevalece sobre el STOP documental anterior de las secciones 39–40 de v0.3; esas secciones y toda la especificación se conservan como fueron recibidas.

No se promueven contratos generales, TES, PSC ni hipótesis H40. Marketing/CRM conserva sus cuatro paneles y sólo adapta la persona, la relación comercial y la invitación al estado seleccionado.

## Baseline y conservación

Antes de editar se registraron:

- [799 hashes de material recibido](evidence/build-02/received-sha256.json).
- [Copia de fuentes anteriores](evidence/build-02/pre-build-sources.tar.gz), incluidos los tests, configuración, README y lanzador.
- [Controles baseline](evidence/build-02/baseline-checks.json): typecheck y lint PASS; suite **112 PASS / 18 FAIL / 0 pendientes**, sobre 130 pruebas.
- Las 17 pruebas deportivas existentes pasaban en el baseline. Los 18 fallos ya estaban presentes por guardas históricas de archivos congelados; no se modificaron esas expectativas.

La [auditoría final](evidence/build-02/preservation-audit.json) encuentra **792 de 799 archivos recibidos idénticos**, siete modificados dentro del delta y ninguno eliminado. Todos los tests históricos permanecen idénticos. También permanecen intactos v0.2, v0.3, informes y evidencias BUILD 01 / Visual Delta 01, S01–S39, experimentos, arquitectura/ADR, TES/PSC, dependencias, configuración y activos de marca.

La función de reconocimiento `recognize()` conserva exactamente sus bytes. La [traza obtenida nuevamente del núcleo BUILD 01](evidence/build-02/preserved-build-01-trace.json) es idéntica byte a byte a `build-01/new-runtime-trace-final.json`. El fixture deportivo original y su paleta tampoco cambian.

## Archivos del delta

Rutas relativas a `prototype/`. [Diff contra el estado recibido](evidence/build-02/product-delta.patch), independiente de otros cambios preexistentes en Git.

| Archivo | Cambio |
| --- | --- |
| `src/demo-factory/sports-season/contracts.ts` | Contratos locales de persona, compras, intención, declaraciones, incentivo y snapshot; el alias de acciones deportivas original se preserva. |
| `src/demo-factory/sports-season/runtime.ts` | El mismo provider incorpora configuración opcional y acciones del plano usuario, valida orden/atribución y aísla recorridos al cambiar de persona. |
| `src/demo-factory/bootstrap.ts` | Conecta la configuración BUILD 02 a Sports Season. |
| `src/app/SportsSeasonApp.tsx` | Selección/intención y nuevos paneles; mantiene borradores y perspectiva al cambiar de superficie; compatibilidad mínima CRM. |
| `src/app/App.tsx` | Web y App deportivas conservan la misma instancia de aplicación. |
| `src/styles/sports-season.css` | Estilos situados de las nuevas interacciones con los tokens Convercus existentes. |
| `README.md` | Accesos BUILD 02 y explicación correcta de la conservación de estado. |
| **Nuevo** `src/demo-factory/sports-season/user-plane-artifacts.ts` | Tres personas ficticias, transacciones, programa, intereses, incentivo editorial y equipamiento. |
| **Nuevo** `src/app/SportsUserPanels.tsx` | Paneles de persona/QR, intereses, información voluntaria e incentivo, equipamiento. |
| **Nuevo** `src/app/SportsSurface.tsx` | Marco App con portal React y viewport móvil; sin segundo bootstrap. |
| **Nuevo** `src/demo-factory/sports-season/user-plane.test.ts` | 18 pruebas nuevas del provider. |
| **Nuevo** `src/demo-factory/sports-season/user-plane-ui.test.tsx` | Dos pruebas nuevas sobre la App real. |

Se añaden este informe y `docs/evidence/build-02/`. No se alteran otros cambios recibidos en el workspace.

## Capacidades observables

| Requisito BUILD 02 | Dónde comprobarlo |
| --- | --- |
| Seleccionar/reconocer persona | Tres tarjetas: Lea, Diego y persona sin identificar. Se explica que es una selección de demo. |
| Cliente distinto de miembro | Dos estados separados en tarjetas y ficha seleccionada. |
| Cliente no miembro con compras | Lea: datos conocidos y tres compras ficticias por 194,80 €. |
| Contrafactual distinto de saldo | Lea: **194 puntos potenciales**, con etiqueta de contrafactual y ausencia explícita de abono retroactivo. Un punto por euro completo es una regla ilustrativa situada. |
| Participar o recibir información | Ambas decisiones están visibles tras seleccionar persona. Intereses: Carrera, Vela, Vóley playa y próximas convocatorias. |
| QR de inscripción | Botón propio, simulación sin cámara; selecciona el contexto Carrera y reconoce al cliente elegido, sin crear inscripción ni presencia. |
| QR de presencia diferente | Paso posterior «Tu presencia · QR de presencia», con botón «Simular check-in». |
| Necesario frente a voluntario | Persona/evento/modalidad para inscribirse; después, frecuencia y objetivo opcionales con salida sin respuestas. |
| Incentivo accesible | La guía editorial de preparación para 5 km se puede abrir tras aportar al menos una respuesta válida. No concede puntos, alta ni insignia. |
| Equipamiento contextual | Cuatro recomendaciones editoriales al elegir Carrera: calzado, textil, hidratación y accesorios. |
| Presencia, esfuerzo e insignia | Inscripción aceptada, check-in simulado, esfuerzo Suave/Medio/Intenso e insignia individual con la regla anterior. |
| Estado común Web/App | Los enlaces «Ver como App» / «Ver como Web» conservan estado funcional y borradores en la misma pestaña. |

Para el miembro Diego se muestran **860 puntos ficticios, nivel Activo y beneficios del club**, procedentes de la configuración. Puede elegir Social o Bienestar independientemente de su pertenencia. Al obtener la insignia no recibe otra invitación de alta ni aumenta su saldo.

El no cliente puede completar un nombre ficticio mínimo e inscribirse sin convertirse en cliente ni miembro. La rama de información funciona para cualquiera de los tres estados comerciales y sólo registra intereses declarados: no crea inscripción, presencia, esfuerzo, insignia ni comunicaciones.

La decisión voluntaria queda separada de las Evidencias deportivas. Se puede aportar información o continuar sin ella; ambas decisiones permiten el mismo reconocimiento deportivo. El incentivo no altera la elegibilidad, intensidad ni pertenencia.

## Abrir y recorrer

- [Web local](http://127.0.0.1:4173/?demo=sports-season-running)
- [App en marco móvil](http://127.0.0.1:4173/showcase?demo=sports-season-running)

Si el servidor no está activo, ejecutar `prototype/Abrir demo.command` y mantener la terminal abierta. Se comprobó respuesta HTTP 200 al reanudarlo para esta revisión.

Recorrido principal:

1. Pulsar **Leer QR de inscripción** y elegir **Lea Martín**; alternativamente, elegirla antes del QR.
2. Observar los datos conocidos, compras y 194 puntos contrafactuales. No se pide escribir otra vez su nombre.
3. Pulsar **Participar**. El QR ya sitúa Carrera; por entrada directa, pulsar **Elegir Carrera**.
4. Consultar equipamiento, elegir **Social** o **Bienestar** y confirmar inscripción.
5. Compartir frecuencia/objetivo para abrir la guía o pulsar **Continuar sin aportar información**.
6. Pulsar **Simular check-in**, declarar esfuerzo y **Registrar esfuerzo**.
7. Ver **Primeros kilómetros** y la invitación informativa a Club Brisa. Consultar el club no produce alta.
8. Cambiar con **Ver como App/Web** para comprobar continuidad; **Reiniciar demo** vuelve a la selección inicial.

Contrastes: Diego permite revisar miembro y rama de información; la persona sin identificar permite entrar por QR, completar el nombre mínimo y obtener la misma insignia sin establecer relación comercial. Elegir otra persona limpia el recorrido anterior, con aviso visible.

## Web y App: frontera de estado

Se utiliza un único provider y un único árbol React. La superficie App introduce un iframe vacío como viewport y recibe la misma interfaz mediante un portal; no ejecuta otra aplicación. La aplicación superior conserva snapshot, borradores, modalidad, esfuerzo, errores y perspectiva.

La continuidad se garantiza al navegar mediante los enlaces de superficie **en la misma pestaña**. Recargar, abrir un enlace en otra pestaña o iniciar otra sesión crea una ejecución independiente. No hay sincronización entre dispositivos ni persistencia remota. La posición de desplazamiento y la apertura nativa de un desplegable pueden reiniciarse al cambiar de superficie; su contenido y los hechos permanecen.

El marco móvil es una presentación responsive comprobada en Edge. No acredita una App nativa, Safari/iOS ni ejecución en un teléfono físico.

## Controles posteriores

[Comandos y códigos de salida](evidence/build-02/final-checks.json), ejecutados con Node oficial 24.14.0 local; no se cambiaron dependencias.

| Control | Resultado |
| --- | --- |
| Typecheck (`tsc -b --pretty false`) | PASS |
| Lint (`eslint .`) | PASS |
| 18 pruebas nuevas de runtime | PASS |
| Dos pruebas nuevas de interfaz real | PASS |
| 16 pruebas originales del núcleo deportivo | PASS |
| Suite completa: 150 pruebas | **131 PASS / 19 FAIL / 0 pendientes** |
| Build Vite/PWA, tras typecheck | PASS |

La [comparación completa baseline/final](evidence/build-02/suite-comparison.json) conserva exactamente los mismos 18 nombres de pruebas con fallos históricos. Siguen siendo guardas hash; el primer archivo/hash divergente puede variar al cambiar fuentes permitidas en BUILD 02.

**Hay además un fallo nuevo que no es de hashes.** `src/demo-factory/sports-season/ui.test.tsx`, prueba «BUILD 01 actual App…», presupone persona externa automática y acceso directo a Carrera. En BUILD 02 la interfaz exige seleccionar persona e intención: el test antiguo no encuentra «Confirmar inscripción». Su fuente se conserva como evidencia del recorrido anterior, sin excluirlo ni alterar expectativas para ocultar el fallo. Las dos pruebas nuevas ejercitan explícitamente la nueva entrada y el recorrido real. Por tanto, `npm test` y la puerta agregada `npm run check` **siguen sin pasar globalmente**.

Las nuevas pruebas cubren contrafactual sin crédito, las tres ramas de intereses sin hechos deportivos, reconocimiento de QR sin presencia, visitante sin conversión, validación atómica de valores/atribución/orden, elección de miembro independiente, aislamiento/reset y rechazo de registros de ejecuciones anteriores. En las seis combinaciones modalidad/esfuerzo se comparan resultados deportivos con información voluntaria aportada frente a omitida: son iguales. [Traza BUILD 02](evidence/build-02/user-plane-trace.json).

## Navegador y revisión visual

[Script reproducible](evidence/build-02/browser-inspection.mjs) con Playwright y Edge instalado, perfil temporal, pruebas locales en segundo plano. El conector del navegador integrado no estaba disponible como herramienta invocable; no se afirma haberlo utilizado.

[Resultado final](evidence/build-02/browser-attempt-2/report.json): **31 estados comprobados, seis comparaciones Web/App idénticas, cero errores de página/consola y cero desbordamientos horizontales en los estados inspeccionados**. Escritorio de 1280 × 1000; marco App y viewport estrecho de 390 × 844. Se inspeccionaron también las capturas: textos legibles, controles completos y paleta preservada.

Las seis comparaciones verifican contenido renderizado y valores de todos los campos antes/después de cambiar superficie: modalidad sin enviar, respuestas voluntarias sin enviar, inscripción e incentivo, insignia e invitación abierta, intereses registrados y actualización de intereses desde App. Se comprueban a través de la UI; no se sustituye el estado por fixtures en navegador.

El [primer intento](evidence/build-02/browser-attempt-1/report.json) detectó una diferencia de texto visible por la etiqueta «3 disciplinas», que el CSS recibido oculta en móvil. Se ajustó únicamente la comparación del script a contenido DOM y campos para separar visibilidad responsive de estado funcional; no se modificó producto para forzar igualdad visual. El segundo intento pasó completo.

Evidencia visual seleccionada:

- [Persona, compras y contrafactual](evidence/build-02/browser-attempt-2/known-customer-counterfactual.png).
- [Miembro y estado del programa](evidence/build-02/browser-attempt-2/member-contrast.png).
- [Intereses declarados](evidence/build-02/browser-attempt-2/declared-interests.png).
- [Guía obtenida por información](evidence/build-02/browser-attempt-2/voluntary-incentive.png).
- [App móvil inicial](evidence/build-02/browser-attempt-2/mobile-app-initial.png).
- [Formulario mínimo](evidence/build-02/browser-attempt-2/unknown-minimum-form.png) e [insignia de no cliente](evidence/build-02/browser-attempt-2/unknown-participant-badge.png).
- [Compatibilidad CRM del caso principal](evidence/build-02/browser-attempt-2/crm-primary-compatibility.png).

Se verificaron errores de modalidad vacía, intereses vacíos, nombre pendiente, información voluntaria vacía y esfuerzo sin elegir. También vuelta de CRM, reset desde CRM y ausencia de invitación de alta para el miembro. La aceptación de claridad/utilidad por Juan está **pendiente**.

## Concreciones y diferencias respecto de v0.3

No se identifica un requisito ejecutable del plano usuario de BUILD 02 pendiente. Las siguientes decisiones concretan las opciones abiertas de la definición:

- El contrafactual utiliza puntos, sin niveles ni beneficios potenciales adicionales.
- La información voluntaria se limita a frecuencia y objetivo; otros campos enumerados en v0.3 eran ejemplos.
- El incentivo es contenido editorial local, accesible en pantalla, sin canje.
- Equipamiento aparece inmediatamente después de seleccionar Carrera, antes del formulario; permanece visible después. Sigue la sección 18 y la instrucción BUILD 02, aunque el esquema conceptual de v0.3 lo dibuje tras la información adicional.
- El caso desconocido ejecuta nombre mínimo y participación; el alta completa continúa narrada.
- Web/App comparten la ejecución local al alternar vistas, sin construir dos clientes de negocio independientes.

Permanecen narrados o fuera del corte: identificación/alta productiva, autenticación, captación efectiva, consentimiento, comunicaciones, QR/cámara físicos, compra/inventario/precios reales, recomendación automática, competición/resultados/posición/trofeos, recorridos de Vela y Vóley, equipos/reconocimiento colectivo, segunda participación/refuerzo y semántica TES. La invitación informa; no convierte a nadie.

## Fricciones para la revisión humana y presiones

Se dejan sin corrección preventiva:

- La página acumula bastante contexto: selección, historial, intención, eventos y recorrido; en móvil exige desplazamiento prolongado.
- El cambio de persona reinicia el recorrido. La intención queda fijada hasta reiniciar o elegir otra persona; no existe comparación simultánea de recorridos.
- La información adicional se decide una vez. «Continuar sin aportar información» requiere una acción explícita antes del check-in, aunque no exige contestar.
- El contenido editorial de equipamiento es igual para todos los participantes de Carrera. Su utilidad y posible percepción de presión comercial requieren revisión humana.
- La cantidad de explicaciones sobre simulación, estado y procedencia puede hacer pesada la lectura.
- Cambiar de superficie conserva hechos y formularios, pero puede perder desplazamiento o apertura de desplegables.
- La rama de intereses de persona desconocida no recoge un canal de contacto. Registra una declaración dentro de la demo, sin prometer un envío ejecutable.

Presión de mantenimiento observada: el recorrido BUILD 01 preservado en la suite ya no es una especificación válida de la entrada actual. Su conservación como evidencia y el mantenimiento de una puerta de pruebas para el producto vigente necesitarán una decisión explícita posterior; no se reescribieron sus expectativas durante este delta.

No apareció una presión semántica o arquitectónica que exigiera H40 para ejecutar este corte. Las fricciones no se declaran aceptadas ni resueltas.

## STOP

BUILD 02 queda preparado para **revisión humana del nuevo plano usuario**. Se detiene aquí: sin v0.4, sin H40 y sin comenzar la revisión o ampliación de Marketing/CRM.

