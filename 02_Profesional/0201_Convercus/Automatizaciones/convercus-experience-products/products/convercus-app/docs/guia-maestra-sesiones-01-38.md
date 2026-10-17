---
title: "Convercus Demo Factory — Guía maestra de las sesiones 01–38"
language: es
version: "1.0"
date: "2026-09-22"
status: "Guía documental de reconstrucción; no promoción arquitectónica"
scope: "Instrucciones de trabajo, fuentes, controles y cierres históricos de las 38 sesiones"
---

# Convercus Demo Factory — Instrucciones para las 38 sesiones

## 1. Propósito y alcance

Este documento reúne una guía operativa para reconstruir, revisar o retomar las 38 sesiones de Convercus Demo Factory / Convercus Experience Products. Cada ficha indica qué estudiar o construir, qué debe permanecer congelado, cómo contrastarlo y qué resultado quedó documentado.

No es una transcripción literal de los 38 prompts originales. Las instrucciones se han sintetizado a partir de las fuentes locales citadas. Las instrucciones originales de las sesiones 1 y 2 sí están conservadas en [Architectural assessment — current Convercus](../../../Architectural%20assessment%20-%20current%20Conv.md). Para las sesiones 5 y 7, la principal evidencia retrospectiva procede de las consolidaciones 6 y 8.

Los resultados históricos son referencias de contraste, no conclusiones que deban forzarse. Si una repetición produce otro resultado, registra la divergencia y su baseline; no reescribas el pasado para conseguir coincidencia.

Esta guía presupone el repositorio y sus artefactos citados. No es un instalador autónomo ni garantiza reconstruir todas las baselines desde una carpeta vacía.

### Dos maneras de utilizarla

- **Reconstrucción histórica:** estudiar las sesiones en orden y ejecutar cada experimento sólo sobre una baseline aislada que corresponda a su momento.
- **Construcción de una demo nueva:** partir de la [base posterior a S38](demo-construction-baseline-after-session-38.md), identificar la composición y el objetivo concreto, y consultar únicamente las sesiones relevantes. No hay que repetir 38 experimentos por cada cliente.

No ejecutes las instrucciones antiguas como 38 cambios consecutivos sobre el producto actual: varias fueron falsadas, otras eran exclusivamente análisis y muchas de sus modificaciones ya están incorporadas.

## 2. Fuentes y autoridad

Orden de consulta:

1. [Precedencia de fuentes](../../../00-governance/source-precedence.md) y [contrato semántico recibido](../../../01-semantic-contract/README.md).
2. [Arquitectura vigente](../../../00-governance/program-architecture.md) y ADR aceptados.
3. Informe, protocolo y consolidación de la sesión concreta.
4. Baselines, trazas, código, harnesses y controles de preservación correspondientes.
5. Esta guía, como índice de instrucciones sintetizadas, nunca como sustituto de las fuentes.

Al reconstruir una sesión histórica, distingue el estado de autoridad de entonces del actual. Architecture v0.5 y ADR-001–005 son el resultado consolidado posterior; no deben atribuirse retrospectivamente a las sesiones iniciales.

Reglas permanentes:

- Distinguir hecho del repositorio, hecho TES/contrato, inferencia, recomendación e insuficiencia de evidencia.
- No inventar semántica TES, capacidad API, identidad humana ni autoridad para un claim.
- No tratar Activity, un texto visible o un mock como prueba de un hecho externo.
- Mantener Experience, Scenario, Script, estado operacional y presentación como responsabilidades distintas.
- No promover automáticamente tipos experimentales a contratos de producto.
- No ampliar alcance para corregir todas las presiones detectadas.
- No confundir test PASS con hipótesis SUPPORTED: un test puede reproducir correctamente una falsación.
- Conservar los cierres y expectativas originales. Una reparación posterior no convierte un FALSIFIED anterior en SUPPORTED.
- Preservar cambios ajenos y no usar una restauración destructiva del repositorio para recrear una baseline.

## 3. Preparación y modo de ejecución

### Ubicación de trabajo

La raíz del proyecto es convercus-experience-products. La aplicación está en products/convercus-app/prototype y los informes en products/convercus-app/docs.

Desde la raíz del proyecto:

~~~bash
cd products/convercus-app/prototype
node --version
npm run typecheck
npm run lint
npm test
npm run build
~~~

npm run check reúne esas cuatro comprobaciones. npm run dev inicia la App local; usa la URL que anuncie el servidor.

El proyecto declara Node >=24. S38 se ejecutó con Node oficial 24.14.0 arm64 y dependencias ya instaladas. El Node incluido en Codex había mostrado un rechazo de firma nativa en S37. Es una condición del entorno, no un fallo semántico.

No instales dependencias ni ejecutes comandos que escriban cachés durante las sesiones estrictamente de lectura 1 y 2. En una reconstrucción técnica autorizada, comprueba primero package.json, lockfile y entorno; una instalación limpia pertenece a una copia aislada, no a una reparación improvisada del working tree.

### Antes de cada experimento

1. Lee el informe previo y la fuente completa de la sesión.
2. Identifica hipótesis, variable independiente, constantes, controles, falsadores y condiciones STOP.
3. Captura la baseline material y el estado de los archivos que se permite cambiar.
4. Separa código productivo, instrumentación de test y documentación.
5. Ejecuta primero la reproducción del problema cuando el protocolo la exija.
6. Aplica sólo el delta autorizado y después contrasta controles positivos, negativos y regresiones.
7. Registra comandos, entorno, resultados, errores y comprobaciones no ejecutadas.
8. Cierra con un veredicto acotado y sin seleccionar automáticamente la siguiente sesión.

Si falta una baseline o un insumo necesario, declara qué parte no puede reproducirse. No todas las copias archivadas constituyen snapshots completos del repositorio.

### Plantilla de instrucción común

Combina este bloque con la ficha de la sesión elegida y su protocolo original disponible:

~~~text
Trabaja exclusivamente en la sesión [N] de Convercus Demo Factory.

Lee la fuente y la consolidación citadas. Antes de actuar, identifica:
- baseline aplicable;
- hipótesis y variable;
- archivos permitidos y congelados;
- controles, falsadores y STOP;
- entregables requeridos.

Distingue hechos, inferencias y evidencia insuficiente.
No adoptes el resultado histórico como resultado obligatorio.

Si la sesión es de análisis, no implementes.
Si permite implementación, aplica únicamente su delta acotado.
Preserva producto, semántica y evidencias que estén fuera de alcance.
No actualices expectativas históricas para obtener PASS.

Separa replay histórico y verificación actual.
Registra lo ejecutado, lo fallido y lo no ejecutado.
Ante un falsador, conserva la evidencia y detén la implementación
afectada; no amplíes el modelo para salvar la hipótesis.

Entrega el informe, las fuentes de evidencia y el veredicto.
No abras automáticamente la siguiente sesión.
~~~

Las fichas siguientes son instrucciones resumidas: los protocolos citados pueden exigir matrices o secciones adicionales.

## 4. Mapa de las 38 sesiones

| Bloque | Sesiones | Trabajo principal |
| --- | --- | --- |
| A | 01–04 | Inspeccionar el sistema y formular una arquitectura falsable |
| B | 05–08 | Probar composición y frontera pública de acciones |
| C | 09–14 | Separar evidencia, evaluación y autoridad |
| D | 15–20 | Suficiencia, composición entre sujetos y primera vertical |
| E | 21–26 | Someter a prueba la reutilización A/B y localizar fugas |
| F | 27–35 | Resolver responsabilidades concretas de presentación |
| G | 36–38 | Auditar claims, reducir sobreafirmaciones y recuperar replay |

Nota de numeración: H1–H4 son las hipótesis iniciales definidas en S4, no nombres alternativos de las sesiones 1–4. No se deben renumerar los informes ni los ADR candidatos antiguos para hacerlos coincidir con los actuales.

## Bloque A — Inspección y arquitectura falsable

### Sesión 01 — Inspección arquitectónica del repositorio

**Carácter:** lectura y análisis, sin implementación.  
**Fuente:** [instrucción original S1 e informe](../../../Architectural%20assessment%20-%20current%20Conv.md).

Instrucciones:

1. Inspecciona estructura, stack, entry points y flujo real de la App.
2. Localiza acceso API, datos demo, branding, configuración, componentes reutilizables, hardcodes y duplicaciones.
3. Describe pruebas, validaciones y dependencias de entorno sin ejecutarlas si generan archivos.
4. Identifica obstáculos para varias demos desde un núcleo común y formula las cinco preguntas arquitectónicas más importantes. No propongas todavía un gran refactor.

**Entrega y contraste:** assessment con hechos e inferencias separados. La baseline histórica era una PWA con mock, sin cliente API ni Factory ejecutable; el informe no modificó archivos ni ejecutó build/tests. Ese diagnóstico describe aquella baseline, no necesariamente el código actual.

### Sesión 02 — Anatomía semántica y Architecture v0.1

**Carácter:** análisis, sin código, instalaciones ni refactor.  
**Fuente:** sección “INSTRUCCIÓN SESION 2” del [documento histórico](../../../Architectural%20assessment%20-%20current%20Conv.md).

Instrucciones:

1. Sigue la secuencia recordar → comprender → aplicar → analizar → evaluar → crear.
2. Reconstruye responsabilidades de DemoPackage, AppSnapshot, DataAdapter, Experience, Scenario, Script y Activity, consultando TES y contratos.
3. Somete las hipótesis a aerolínea, retail, movilidad y hospitality, con hotel de negocios y resort. No presupongas que Experience equivale a recorrido, secuencia, completion o recompensa.
4. Compara como máximo tres arquitecturas; produce mapas de responsabilidad/autoridad, invariantes, transición mínima, no-objetivos, preguntas abiertas y candidatos ADR.

**Entrega y contraste:** propuesta Architecture v0.1, no arquitectura aceptada. Conserva la estructura de 15 apartados del prompt original si lo reproduces. DemoPackage como raíz soberana, Interaction Trace y coverage eran hipótesis que después se revisaron.

### Sesión 03 — Revisión adversarial de Architecture v0.1

**Carácter:** falsación documental.  
**Fuente:** [auditoría de S3](../../../sesio%CC%81n-3.md).

Instrucciones:

1. Descompón las propuestas en supuestos y busca contraejemplos reales de composición, datos híbridos, sujetos y presentación.
2. Contrasta la autoridad TES acotada; distingue manifiesto deseado de composición efectiva y separación conceptual de persistencia obligatoria.
3. Ataca el adaptador universal, el prospecto=paquete único y coverage como porcentaje universal.
4. Clasifica cada propuesta como superviviente, cualificada, revisable, rechazada o pendiente y formula la revisión v0.2.

**Entrega y contraste:** matriz adversarial y arquitectura revisada. No convertir la numeración de los ADR candidatos de v0.1 en la numeración de los ADR finalmente aceptados. No implementar la revisión todavía.

### Sesión 04 — ADR mínimos y experimento reversible

**Carácter:** formalización y diseño experimental.  
**Fuente:** [S4](session-4-hypotheses-minimum-reversible-experiment.md).

Instrucciones:

1. Formaliza sólo las decisiones justificadas: autoridad semántica acotada y separación lógica composición/runtime/read models.
2. Formula H1 — composición deseada/efectiva; H2 — Experience/Scenario/Script; H3 — evidencia/interpretación/Activity; H4 — resolución externa de proveedores.
3. Diseña “dos demos, un núcleo, cero forks”: Retail y Hospitality mediante manifiestos, referencias, fixtures y bootstrap.
4. Define controles, fallos explícitos, reversibilidad y exclusiones. No construir backend, motor general de Experience, persistencia ni analíticas de coverage.

**Entrega y contraste:** ADR-001/002 y especificación de entrada para S5; experimento todavía no implementado en esta sesión.

## Bloque B — Composición y acciones públicas

### Sesión 05 — Implementar el experimento mínimo de dos demos

**Carácter:** implementación reversible.  
**Fuentes:** [especificación S4](session-4-hypotheses-minimum-reversible-experiment.md) y [verificación retrospectiva S6](session-6-experiment-consolidation.md).

Instrucciones:

1. Implementa el mínimo contrato de manifiesto y resolución efectiva de marca, fixture, capacidades y artefactos opcionales.
2. Resuelve el runtime antes de renderizar App; inyecta fixtures y evita selección de prospecto dentro de React.
3. Conserva Retail sin Scenario/Script y añade Hospitality con las referencias mínimas definidas por S4.
4. Comprueba referencias inválidas, demo desconocida, ausencia de fallback silencioso, aislamiento de instancias, reset y Activity como proyección.

**Entrega y contraste:** dos composiciones sobre el mismo core. S6 registró 25 tests en 8 archivos y check completo PASS. H2–H4 no quedaron universalmente demostradas; la operación del Script en UI aún necesitaba el experimento S7. Estas instrucciones son una reconstrucción, no un prompt S5 original independiente.

### Sesión 06 — Consolidar la composición deseada y efectiva

**Carácter:** verificación y promoción selectiva.  
**Fuente:** [S6](session-6-experiment-consolidation.md).

Instrucciones:

1. Verifica independientemente la implementación S5 y clasifica hechos, evidencia e inferencia.
2. Decide qué promover, cualificar, mantener experimental o considerar legacy.
3. Formaliza ADR-003 para composición deseada/efectiva, sin convertir catálogos, query parameters o un mock único en arquitectura universal.
4. Compara candidatos posteriores y documenta la elección del ensayo operacional de Scenario/Script.

**Entrega y contraste:** Architecture v0.3; H2 todavía provisional y H3/H4 parciales. No convertir el GO de una siguiente prueba en su ejecución dentro de S6.

### Sesión 07 — Acción pública de presentador y transición controlada

**Carácter:** implementación mínima.  
**Fuentes:** [entrada desde S6](session-6-experiment-consolidation.md) y [consolidación S8](session-8-h2-consolidation.md).

Instrucciones:

1. Expón exactamente una acción de llegada desde el Script mediante la frontera pública del provider.
2. Haz que runtime valide acción/checkpoint y posea la transición; el Script no escribe estado ni decide reglas.
3. Publica el resultado en snapshot y Activity y conecta el control de presentación.
4. Contrasta acción válida, repetición rechazada, reset determinista y aislamiento Retail.

**Entrega y contraste:** recorrido pre-arrival-confirmed → checked-in. Son checkpoints demo, no TES Progression/Result/Completion. S8 registró 31 tests en 9 archivos y check PASS. Instrucciones reconstruidas desde la consolidación; no se presume un runner general de Scripts.

### Sesión 08 — Consolidar H2 y aceptar ADR-004

**Carácter:** verificación y promoción limitada.  
**Fuente:** [S8](session-8-h2-consolidation.md).

Instrucciones:

1. Recorre Script → Public Action → runtime → transición → read model/UI.
2. Verifica que la UI no decide legalidad ni muta estado y que Activity sigue siendo proyección.
3. Separa las responsabilidades acreditadas de las shapes locales: strings, una transición y ejecución de steps[0].
4. Formaliza ADR-004 y Architecture v0.4 con esos límites.

**Entrega y contraste:** H2 SUPPORTED / formalizada. H3 contextual sigue pendiente; no se promueven branching, concurrencia de Scripts, motor de Experience ni todas sus cardinalidades.

## Bloque C — Evidencia y autoridad contextual

### Sesión 09 — Comprobar prerrequisitos de evaluación multi-Experience

**Carácter:** gate semántico previo a implementación.  
**Fuente:** [S9](session-9-contextual-multi-experience-evaluation.md).

Instrucciones:

1. Busca dos Experience references defendibles capaces de evaluar el mismo input factual.
2. Revisa definiciones y autoridad; IDs sintéticos o capabilities propuestas no sustituyen Experience Definitions.
3. Si no hay material semántico suficiente, detén la implementación y explica el gap.
4. No inventes una segunda Experience ni reutilices una frontera SignificantEvent/progression fuera del alcance permitido.

**Entrega y contraste:** STOP / H3 INCONCLUSIVE. Históricamente faltaba la segunda definición defendible. No hay una reparación de código que deba introducirse para hacer pasar esta sesión.

### Sesión 10 — Readiness de fuentes comerciales

**Carácter:** interpretación documental, no runtime.  
**Fuente:** [S10](session-10-commercial-experience-semantic-readiness.md).

Instrucciones:

1. Inspecciona la fuente comercial identificada en el informe y clasifica su autoridad como no normativa.
2. Distingue Experience candidata, campaña, incentivo, reto y marco de lifecycle.
3. Redacta candidatas no ejecutables sólo cuando mantengan una transformación defendible al retirar puntos, insignias y recompensas.
4. Construye la matriz Evidence-to-Experience y explicita gaps de Pattern, Result, Measurement y Learning.

**Entrega y contraste:** Aventura Familiar, Desafío Activo y Circuito Sostenible READY WITH EXPLICIT GAPS; GO acotado para reconsiderar H3. No equivale a validación TES plena. Si la fuente comercial no está disponible, limita la reconstrucción a la evidencia conservada y decláralo.

### Sesión 11 — Relevancia contextual de evidencia neutral

**Carácter:** experimento de evaluación pura.  
**Fuente:** [S11](session-11-contextual-evidence-relevance-experiment.md).

Instrucciones:

1. Mantén una Evidence de Cooking Class independiente de Experience, interpretación y presentación.
2. Construye dos contextos apoyados en las definiciones candidatas y el Scenario.
3. Implementa la frontera mínima de relevancia sin ramas por Experience ID, mutación, estado oculto ni Activity como input.
4. Prueba renaming, orden, repetición e independencia de datos y resultados.

**Entrega y contraste:** H3 SUPPORTED WITH QUALIFICATION para relevancia contextual. No demuestra reconocimiento de TES Event. La lectura binaria negativa de este experimento debe conservar su estatuto histórico: S12 identificó que no era promovible sin autoridad suficiente de clasificación.

### Sesión 12 — Fronteras de autoridad y mundo abierto

**Carácter:** análisis y preparación, no promoción automática.  
**Fuente:** [S12](session-12-authority-frontiers-open-world-evaluation.md).

Instrucciones:

1. Audita qué actor puede afirmar cada claim y detecta transferencia aparente de autoridad entre capas.
2. Separa clasificación ausente, contexto incompatible, conocimiento incompleto y exclusión defendible.
3. Distingue los artefactos llamados ExperienceDefinition y su madurez real; tesBaseline no significa validación.
4. Formula requisitos de competencia, scope y cobertura y prepara una prueba falsable.

**Entrega y contraste:** matriz de autoridad y crítica de la semántica binaria. Falta de conocimiento ≠ negativo. No aceptar aún ADR-005 ni crear un Authority Service.

### Sesión 13 — Evaluación open-world acotada por autoridad

**Carácter:** experimento controlado.  
**Fuente:** [S13](session-13-authority-bounded-open-world-evaluation.md).

Instrucciones:

1. Mantén Evidence/contexto y varía únicamente la autoridad disponible.
2. Prueba membership positiva, exclusión explícita, conocimiento incompleto y cobertura exhaustiva dentro de scope.
3. Incluye autoridad ausente, scope incorrecto y conflicto sin inventar una regla de precedencia.
4. Comprueba que el evaluator deriva conclusiones, no se acredita a sí mismo ni convierte Activity en autoridad.

**Entrega y contraste:** H13 SUPPORTED WITH QUALIFICATION. Positive/negative requieren premisas competentes; ausencia o conflicto pueden quedar undetermined. La autoridad de los fixtures se asume por construcción, no es acreditación real.

### Sesión 14 — Promoción limitada de ADR-005

**Carácter:** consolidación arquitectónica.  
**Fuente:** [S14](session-14-consolidation-architectural-promotion-decision.md).

Instrucciones:

1. Revisa la cadena S11–S13 y evalúa cada cláusula candidata de forma independiente.
2. Promueve sólo separación de evidencia/evaluación y límites de los claims por autoridad, scope y madurez.
3. Mantén tipos, enums, reason codes, catálogos y fixtures como experimentales.
4. Evalúa separadamente si Architecture v0.5 añade comprensión sin crear nuevos servicios o aggregates.

**Entrega y contraste:** ADR-005 ACCEPTED; Architecture v0.5 publicada. Treasure Hunt queda listo para una prueba acotada, no demostrado de antemano. Los informes anteriores permanecen históricos.

## Bloque D — Suficiencia y primera vertical

### Sesión 15 — Evidencia distribuida y suficiencia

**Carácter:** experimento mínimo unipersonal y no ordenado.  
**Fuente:** [S15](session-15-treasure-hunt-distributed-evidence-sufficiency-experiment.md).

Instrucciones:

1. Conserva hechos A/B/C independientes y define un criterio experimental scoped de suficiencia.
2. Contrasta conjuntos de igual cardinalidad con resultados distintos: A+B frente a B+C.
3. Prueba duplicados A+A, inversión de orden, evidencia adicional y ausencia de contribuciones requeridas.
4. Mantén suficiencia separada de solution recognition, Progression, Result, Completion e incentivo.

**Entrega y contraste:** H15 SUPPORTED WITH QUALIFICATION. Contar registros no establece suficiencia; el criterio y su autoridad son fixtures, no una ley TES ni un modelo de grupo.

### Sesión 16 — Preparar la frontera entre atribución y admisibilidad

**Carácter:** discusión y diseño; la fuente es deliberativa.  
**Fuente:** [S16](session-16-consolidation-distributed-evidence-sufficiency.md).

Instrucciones:

1. Separa “Evidence atribuida a P1/P2” de “Evidence que puede usarse conjuntamente”.
2. Mantén booking, stay y Hunt compartidos como contexto, no como autoridad positiva automática.
3. Diseña una única premisa experimental scoped para autorizar la consideración conjunta de P1/P2.
4. Formula controles sin autoridad, scope incorrecto, sujetos no cubiertos y control unipersonal; conserva beneficiario y Group sin resolver.

**Entrega y contraste:** preparación de H17. No inventar un veredicto ejecutable H16 ni una implementación adicional: el archivo conserva discusión y observaciones, no un informe de test equivalente a los posteriores.

### Sesión 17 — Composición entre sujetos acotada por autoridad

**Carácter:** experimento y consolidación diferenciados.  
**Fuentes:** [experimento](session-17-authority-bounded-cross-subject-evidence-composition.md) y [consolidación](session-17-consolidation-authority-bounded-cross-subject-evidence-composition.md).

Instrucciones:

1. Mantén atribución A@P1/B@P2, contexto y criterio K; introduce sólo la premisa de admisibilidad conjunta.
2. Evalúa admisibilidad antes de intentar suficiencia.
3. Prueba premisa válida, ausente, fuera de scope, sujetos equivocados y booking compartido sin autoridad.
4. Conserva la regresión unipersonal y documenta la presión sobre el contrato sin crear Group, membership o beneficiario colectivo.

**Entrega y contraste:** H17 SUPPORTED WITH QUALIFICATION; PSC-P01 OPEN / EVIDENCE-BACKED PRESSURE. La consolidación registra la presión, no modifica PSC ni promueve AuthoritativePremise.

### Sesión 18 — Validez contextual del claim derivado

**Carácter:** experimento corregido y posterior consolidación.  
**Fuentes:** [informe corregido](session-18-derived-claim-contextual-validity.md) y [consolidación](session-18-consolidation-derived-claim-contextual-validity.md).

Instrucciones:

1. Parte de un claim derivado en S1 y pregunta si su uso en S2 está acreditado.
2. No conviertas igualdad de IDs de scope en la regla semántica que pretendes demostrar.
3. Introduce una base autoritativa experimental, explícita y direccional para S1→S2; prueba ausencia, inaplicabilidad y uso autorizado.
4. Separa autoridad de derivación de autoridad de reutilización. No infieras simetría, transitividad, revocación, propietario o nueva derivación en S2.

**Entrega y contraste:** el informe corregido quedó INCONCLUSIVE pendiente de revisión; la consolidación posterior cerró SUPPORTED WITH QUALIFICATION. Preservar ambas etapas, no borrar la corrección epistemológica.

### Sesión 19 — Preparación para la primera demo vertical

**Carácter:** assessment, sin implementación.  
**Fuente:** [S19](session-19-first-demo-readiness.md).

Instrucciones:

1. Reconstruye el camino efectivo desde manifiesto hasta UI.
2. Identifica el primer enlace ausente entre Evidence del runtime y evaluación contextual.
3. Evalúa qué gaps bloquean realmente una vertical Aventura Familiar y cuáles pueden permanecer abiertos.
4. Delimita la integración mínima, UI requerida y deuda aceptable sin crear arquitectura general.

**Entrega y contraste:** FIRST DEMO READINESS READY WITH GAPS. API real, Group y referente/beneficiario del claim no eran prerrequisitos de esta demo acotada. Todavía no se acredita una vertical completa.

### Sesión 20 — Construir y corregir Aventura Familiar

**Carácter:** implementación vertical, corrección y aceptación del recorrido.  
**Fuente:** [informe de cierre S20](session-20-first-family-adventure-vertical.md); usar la revisión cerrada, no una aceptación anterior superada.

Instrucciones:

1. Parte de P1 y P2 existentes; distingue P1 no alistado y P2 no habilitado. Las acciones no crean sujetos.
2. Conecta alistamiento P1 → Evidence A@P1 → activación P2 → Evidence B@P2 → evaluación. Alistamiento y activación no producen Evidence.
3. Mantén la atribución factual distinta de la sesión operativa y preserva K = A AND (B OR C).
4. Presenta Mi aventura, Actividad y Supervisión sobre la misma fuente; ofrece siguiente acción clara, navegación que conserve runtime y reset.
5. Ejecuta la checklist exacta de 22 pasos del informe con evidencia de navegador, además de guardas, negativos y regresiones. No avances mediante modificación interna del estado.

**Entrega y contraste:** vertical EXECUTABLE WITH PRESENTATION GAPS; cierre histórico 22/22 PASS. El informe distingue ejecución de navegador del 8 de septiembre de su cotejo del día 12. No atribuyas a una repetición actual evidencias antiguas ni certifiques iPhone real.

## Bloque E — Reutilización y procedencia A/B

### Sesión 21 — Falsar la reutilización de composición

**Carácter:** auditoría, protocolo y ejecución sobre maquinaria congelada.  
**Fuentes:** [auditoría](session-21-composition-boundary-factory-reusability-audit.md) y [ejecución](session-21-composition-boundary-factory-reusability-execution.md).

Instrucciones:

1. Captura las fuentes protegidas de A y el mapa de responsabilidades.
2. Crea B/Costa con marca, contenidos, contexto y referencias propias, manteniendo Experience, sujetos de control, acciones, guards, K y maquinaria compartida.
3. Verifica resolución e instancias distintas y avanza sólo mientras no aparezca un falsador material.
4. Detente ante la primera frontera que exija cambiar lo congelado; no repares el runtime dentro de H21.

**Entrega y contraste:** H21 FALSIFIED en L2: B no recibía sus perspectivas iniciales porque la selección dependía de Scenario A. Última frontera superada: resolución, providers distintos y snapshots genéricos. Cero acciones y reset tras ese STOP; no certificar etapas que no se ejecutaron.

### Sesión 22 — Selección estable por Experience

**Carácter:** reparación mínima sometida a prueba.  
**Fuente:** [S22](session-22-experience-stable-behavior-selection.md).

Instrucciones:

1. Conserva la falsación H21 y toma los dos puntos concretos de selección del adapter.
2. Sustituye el discriminante Scenario.id por la relación Experience existente, sin crear un registro general de behaviors.
3. Prueba A/B positivas y Retail/Arrival negativas, incluidas perspectivas y llamadas reales de evaluación.
4. Mantén contexto, copy, K y contratos fuera del delta; registra fugas observadas sin corregirlas.

**Entrega y contraste:** H22 SUPPORTED WITH QUALIFICATION. Resuelve selección local, no reutilización integral ni integridad contextual.

### Sesión 23 — Transporte del contexto situado a evaluación

**Carácter:** experimento de binding contextual.  
**Fuente:** [S23](session-23-situated-evaluation-context-binding.md).

Instrucciones:

1. Mapea por separado contexto factual de Evidence, contexto de evaluación y premisa autoritativa.
2. Transporta Scenario.contexts de la composición resuelta a la integración, sin reutilizar constantes de A en B.
3. Prueba A/B, contradicciones en ambos sentidos y premisa ausente o inaplicable.
4. No reescribas Evidence para que encaje ni permitas que contexto correcto sustituya autoridad.

**Entrega y contraste:** H23 SUPPORTED WITH QUALIFICATION; binding situado verificado. H17, K, selectores H22 y los textos permanecen fuera del cambio.

### Sesión 24 — Buscar una fuente existente para Activity situada

**Carácter:** inspección y falsación bajo “sin nueva relación”.  
**Fuente:** [S24](session-24-situated-activity-representation-provenance.md).

Instrucciones:

1. Traza title/description desde la acción aceptada hasta Activity.
2. Busca una relación ya existente y apropiada para narrativa posterior a la ocurrencia.
3. No derives lugares desde subjectRef/markerRef ni conviertas presenterLabel previo en descripción retrospectiva.
4. Si falta la fuente legítima, conserva la fuga A/B y detén cualquier cambio de runtime o contrato.

**Entrega y contraste:** H24 FALSIFIED; L5 abierto. No concluye que separar hecho/presentación sea imposible; demuestra que la baseline no tenía la relación requerida.

### Sesión 25 — Declaración explícita de Activity por paso

**Carácter:** nueva relación local autorizada tras S24.  
**Fuente:** [S25](session-25-script-bound-situated-activity-representation.md).

Instrucciones:

1. Evalúa el host y añade sólo la declaración opcional activityPresentation del paso de Script.
2. Materializa title/description únicamente después de aceptar la acción correspondiente.
3. Prueba variación, ausencia y contradicción del texto sin modificar hechos, atribución, contexto, estados, evaluación o K.
4. Conserva guards, GuestPerspective y App; no eleves Script a propietario universal de presentación.

**Entrega y contraste:** H25 SUPPORTED WITH QUALIFICATION para los pasos Evidence ensayados. Presentación editorial explícita no garantiza verdad de todos sus predicados; esa limitación se examina en S36.

### Sesión 26 — Auditar GuestPerspective sin relaciones nuevas

**Carácter:** falsación de suficiencia de las fuentes existentes.  
**Fuente:** [S26](session-26-situated-guest-perspective-provenance.md).

Instrucciones:

1. Separa diagnósticamente cuenta, labels de sujeto y narrativa de recorrido.
2. Comprueba qué fuentes existen y qué relaciones faltan, sin inferir sujeto desde cuenta o sesión.
3. No utilices Activity como autoridad narrativa general ni copies hardcodes A/B a otra capa.
4. Ante el primer falsador, reproduce y documenta; no aproveches para reparar parcialmente los tres componentes.

**Entrega y contraste:** H26 FALSIFIED. Cuenta tenía fuente disponible; labels situados y narrativa carecían de relaciones suficientes. NO-NEW-RELATION INSUFFICIENT para el conjunto, no para todo problema posterior.

## Bloque F — Responsabilidades de presentación acotadas

### Sesión 27 — Labels situados de sujetos

**Carácter:** relación presentacional explícita.  
**Fuente:** [S27](session-27-explicit-situated-subject-representation.md).

Instrucciones:

1. Limita la variable a GuestPerspective.subjects[].label.
2. Declara la relación subjectRef → presentación situada en el host experimental justificado.
3. Perturba cuenta y labels independientemente, incluidos nombres iguales para sujetos distintos.
4. Prueba ausencia/mismatch sin cambiar subjectRef, sesión operacional, estados, Evidence, contexto o evaluación.

**Entrega y contraste:** H27 SUPPORTED WITH QUALIFICATION. subjectPresentations es presentación local, no identidad humana, autenticación ni relación account→subject. sessionLabel, status y message quedan fuera.

### Sesión 28 — Presentación exclusivamente de cuenta

**Carácter:** reutilización de fuente existente.  
**Fuente:** [S28](session-28-account-sourced-guest-presentation.md).

Instrucciones:

1. Limita la variable a GuestPerspective.sessionLabel.
2. Transporta el nombre de cuenta existente y representa “Cuenta de [nombre]”.
3. Cambia sólo cuenta y luego sólo subjectPresentations para demostrar independencia en ambos sentidos.
4. Congela labels, estado, mensaje, Activity, referencias, evaluación y App.

**Entrega y contraste:** H28 SUPPORTED WITH QUALIFICATION. Mostrar una cuenta no acredita quién es el viewer, quién contribuyó Evidence o qué sujeto representa.

### Sesión 29 — Estado operacional neutral del sujeto

**Carácter:** reducción de significado sin nueva relación.  
**Fuente:** [S29](session-29-operational-subject-status-provenance.md).

Instrucciones:

1. Audita qué afirma cada status y qué puede justificar subjectStates.
2. Limita GuestPerspective.subjects[].status a estado presente: sin alistar, sin habilitar o habilitado.
3. Prueba transiciones y cambios independientes de cuenta, labels y Activity.
4. Comprueba que Evidence, evaluación o narrativa causal no sean necesarias para producir el status.

**Entrega y contraste:** H29 SUPPORTED WITH QUALIFICATION. No afirmar quién habilitó al sujeto ni por qué. La narrativa de recorrido sigue siendo una presión distinta.

### Sesión 30 — Narrativa situada por posición operacional

**Carácter:** relación local para GuestPerspective.message.  
**Fuente:** [S30](session-30-script-bound-situated-journey-narrative.md).

Instrucciones:

1. Captura la matriz pre-delta de posiciones y evalúa los discriminantes existentes antes de elegir uno.
2. Contrasta que checkpoint solo no distingue todos los intervalos; usa availableActionId únicamente si resulta suficiente en el recorrido probado.
3. Asocia declaraciones narrativas explícitas a ese discriminante sin recalcular guards ni disponibilidad desde Script.
4. Prueba A/B, ausencia, mismatch, independencia de cuenta/labels/status/Activity y contradicción factual del texto.

**Entrega y contraste:** H30 SUPPORTED WITH QUALIFICATION. availableActionId no se promueve a estado universal del journey; ausencia de acción no significa completion y no exige inventar una acción sentinel.

### Sesión 31 — Auditoría del framing introductorio de App

**Carácter:** inspección bajo “relaciones existentes únicamente”.  
**Fuente:** [S31](session-31-application-composition-framing-provenance.md).

Instrucciones:

1. Aísla el eyebrow “Mi aventura · Aurora Stay” y el párrafo introductorio; no los confundas con el h1.
2. Busca fuentes legítimas ya disponibles para marca e introducción situada.
3. No construyas introducción mediante parsing o agregación de otros textos ni desde GuestPerspective.message.
4. Si falta relación para la introducción, detén implementación y conserva App.

**Entrega y contraste:** H31 FALSIFIED bajo NO-NEW-RELATION. La marca tiene fuente; la introducción necesita una relación distinta. Fue auditoría de fuente, no una ejecución App que deba afirmarse retroactivamente.

### Sesión 32 — Introducción explícita de composición

**Carácter:** relación mínima tras S31.  
**Fuente:** [S32](session-32-explicit-composition-introductory-framing.md).

Instrucciones:

1. Justifica el host y añade la introducción estática opcional experimentalIntroductoryFraming.
2. Transporta separadamente la marca resuelta para el eyebrow.
3. Haz que App consuma ambos valores sin lookup A/B ni inferencias de significado.
4. Prueba variación, ausencia y renaming de IDs; conserva h1, hechos, evaluación y restantes superficies.

**Entrega y contraste:** H32 SUPPORTED WITH QUALIFICATION. Script es host local de esta declaración, no PresentationModel general ni autoridad factual.

### Sesión 33 — Identificación neutral en Supervisión

**Carácter:** reducción acotada en App.  
**Fuente:** [S33](session-33-operational-supervision-subject-representation-provenance.md).

Instrucciones:

1. Limita el delta al h2 de cada tarjeta de sujeto en Supervisión.
2. Sustituye la selección hardcoded “P1 · Lucía” / “P2 · Huésped 2” por subject.id tal como llega en el read model.
3. No incorpores nombres de H27, parsing del identificador o una relación nueva.
4. Ejecuta los recorridos A/B y compara hechos, evaluación y DOM restante con la baseline.

**Entrega y contraste:** H33 SUPPORTED WITH QUALIFICATION; NO-NEW-RELATION SUFFICIENT para identificación diagnóstica. No garantiza una identidad humana ni aceptación de usabilidad.

### Sesión 34 — Rótulo neutral de sujeto de sesión

**Carácter:** reducción de un único literal.  
**Fuente:** [S34](session-34-operational-session-subject-representation-provenance.md).

Instrucciones:

1. Aísla el par rótulo/valor que muestra supervision.sessionSubjectRef.
2. Cambia “Cuenta/sesión operativa” por “Sujeto de sesión operativa”; conserva el valor y su expresión.
3. Contrasta independencia de cuenta, labels y composición.
4. Distingue recorridos válidos de observaciones aisladas de transporte con otras referencias; no presentes estas últimas como sesiones autenticadas admisibles.

**Entrega y contraste:** H34 SUPPORTED WITH QUALIFICATION. No añade semántica de account owner, viewer, persona o autenticación.

### Sesión 35 — Nombre procedente de Experience

**Carácter:** transporte de fuente existente.  
**Fuente:** [S35](session-35-experience-sourced-guest-experience-name-provenance.md).

Instrucciones:

1. Limita la variable a la procedencia de GuestPerspective.huntName y su h1.
2. Transporta literalmente ExperienceDefinition.name de la Experience resuelta.
3. Prueba variación independiente de marca, Scenario, Script y otros campos; observa ausencia/valor vacío según el protocolo.
4. Mantén App como consumidor de huntName, sin acceso paralelo a catálogos, composición de títulos ni fallback oculto.

**Entrega y contraste:** H35 SUPPORTED WITH QUALIFICATION. No renombrar contratos ni transformar el nombre de Experience en título de campaña o instancia. Registrar por separado cualquier sensibilidad de recursos/timeouts.

## Bloque G — Claims e integridad del instrumento

### Sesión 36 — Auditoría de autoridad por afirmación

**Carácter:** auditoría semántica y de procedencia, sin reparación de producto.  
**Fuente:** [S36](session-36-presentation-authority-provenance-stratification-audit.md).

Instrucciones:

1. Descompón las superficies abordadas en afirmaciones significativas, no sólo campos o archivos.
2. Para cada claim, registra origen textual, relación necesaria, autoridad disponible y modo de producción; usa U/D/O/E conforme al protocolo, no como categorías que deban salvar todo caso.
3. Contrasta especialmente viewer, actor y cuenta ejecutora en Activity.
4. Si un texto afirma una relación no acreditada, registra el falsador; no declares Script autoridad universal ni inventes otra categoría para absorberlo.

**Entrega y contraste:** H36 FALSIFIED en su pretensión exhaustiva. “Por ti” y “desde tu cuenta” excedían la autoridad disponible. Los resultados locales H25–H35 siguen válidos dentro de sus límites; no se reparan en S36.

### Sesión 37 — Reducir atribuciones no acreditadas en Activity

**Carácter:** delta de cuatro descripciones, sin nuevas relaciones.  
**Fuente:** [S37](session-37-activity-attribution-claim-provenance-and-reduction.md).

Instrucciones:

1. Construye primero la matriz de claims de las cuatro descripciones A/B y confirma qué autoridad conserva cada fragmento.
2. Aplica únicamente las reducciones siguientes, manteniendo títulos, ocurrencias, atribución factual y narrativa situada:

   | Composición / hallazgo | Descripción conservada tras la reducción |
   | --- | --- |
   | A / primero | Hallazgo registrado. |
   | A / segundo | Hallazgo atribuido al huésped 2. |
   | B / primero | Hallazgo registrado. |
   | B / segundo | Hallazgo atribuido a Mateo. |

3. Prueba independencia de cuenta, labels de sujeto y transporte de referencia de sesión, separando recorridos canónicos de observaciones aisladas.
4. Ejecuta rechazos sin ocurrencia, regresiones Retail/Arrival y App actual. Mantén hechos, evaluación, contratos, App y arquitectura fuera del delta.

**Entrega y contraste:** H37 SUPPORTED WITH QUALIFICATION; NO-NEW-RELATION SUFFICIENT en este alcance. H36 sigue FALSIFIED históricamente. S37 cerró con 95 PASS y tres fallos ambientales H21–H23, no con suite global verde.

### Sesión 38 — Portabilidad del replay e integridad de evidencia

**Carácter:** infraestructura exclusivamente; producto, semántica y arquitectura congelados.  
**Fuentes:** [informe/protocolo consolidado S38](session-38-historical-replay-portability-evidence-integrity.md), [análisis pre-delta](evidence/session-38/pre-delta-analysis.md) y [regla local](evidence/session-38/evidence-integrity-manifest.md).

Instrucciones:

1. Reproduce H21/H22/H23 antes de reparar. Registra assertion, stack, ruta solicitada e invariante protegido.
2. Reconstruye su intención histórica y clasifica materialidad de cada dependencia .DS_Store por uso y evidencia, no por extensión.
3. Inventaría harnesses, copias, imports, mapas, precedencias y lectores; distingue históricos de verificación actual.
4. Compara allowlist material, exclusiones explícitas, manifest por raíces/tipos, paquete hermético y captura completa antes de seleccionar un mecanismo.
5. Valida el candidato en fixtures temporales: metadata ausente/presente; fuente material mutada/retirada; archivo ambiental desconocido; fuente actual mutada; shadows de archivo antiguo/nuevo/actual; normalización NFC/NFD sin cambiar bytes.
6. Sólo tras superar el gate aplica el mínimo delta de selección de fuentes. No cambies hashes/expectativas históricas, no fabriques archivos ausentes para pasar y no ocultes fallos con skip, timeouts o serialización.
7. Ejecuta suite histórica disponible y verificación actual por separado; mide preservación de producto y coste de mantenimiento.
8. Documenta reglas locales y limitaciones. Conserva los fallos de relocalización de assets y alias de paths; no los confundas con variación de metadata.

**Entrega y contraste:** H38 SUPPORTED WITH QUALIFICATION. Cierre registrado: 106 PASS / 0 FAIL, 31 archivos, tipos/lint/build PASS; 98 tests heredados PASS en cada condición de metadata. Cinco rutas incidentales auditadas; mutación material detectada; 480 archivos heredados intactos y sólo tres harnesses modificados.

La regla queda LOCAL / EXPERIMENTAL / NOT PROMOTED. Portabilidad universal, otra plataforma, instalación hermética y aceptación visual no están acreditadas. No abrir H39 automáticamente.

## 5. Qué resultados históricos no deben borrarse

| Sesión | Resultado o matiz que debe conservarse |
| --- | --- |
| 02–03 | Architecture v0.1 fue hipótesis revisada, no diseño final aceptado |
| 09 | STOP semántico; H3 INCONCLUSIVE |
| 11–12 | El resultado contextual inicial no legitima promover un booleano negativo open-world |
| 16 | Discusión preparatoria, no suite o veredicto ejecutable propio |
| 18 | Corrección INCONCLUSIVE seguida de consolidación SUPPORTED WITH QUALIFICATION |
| 20 | Aceptación inicial revisada; usar el cierre y checklist de la revisión vigente |
| 21 | FALSIFIED en perspectivas iniciales; no completar retrospectivamente su recorrido |
| 24 | FALSIFIED por ausencia de relación legítima existente para Activity situada |
| 26 | FALSIFIED bajo NO-NEW-RELATION para GuestPerspective |
| 31 | FALSIFIED bajo NO-NEW-RELATION para introducción situada |
| 36 | FALSIFIED para cobertura exhaustiva de autoridad por afirmación |
| 37 | Producto verificado en su alcance; suite global aún tenía tres fallos ambientales |
| 38 | Recupera replay frente a metadata, no resuelve toda la portabilidad |

## 6. Plantilla de entrega y evidencia

Cada nueva ejecución o revisión debe identificarse como tal, sin sobreescribir el expediente histórico original.

~~~markdown
# Sesión N — Título
## Baseline recibida
## Hipótesis o pregunta
## Variable y constantes
## Fuentes y autoridad
## Archivos autorizados y congelados
## Controles y falsadores
## Delta implementado o STOP
## Evidencia de ejecución
## Regresiones y preservación
## Resultados no ejecutados o bloqueados
## Veredicto y cualificaciones
## Límites y presiones observadas
## Estado de promoción
~~~

Cuando el protocolo fuente exija más apartados, conserva su estructura completa; esta plantilla no reduce obligaciones. Para las sesiones 1 y 2, el informe es una salida de análisis, no permiso para modificar el repositorio inspeccionado.

Registrar como mínimo:

- Comandos, versión de Node/plataforma y configuración relevante.
- Hashes o baselines materiales, distinguiendo fuente actual de archivada.
- Inputs, snapshots, llamadas/resultados y DOM cuando formen parte de la afirmación ensayada.
- Fallos y trazas negativas, no sólo capturas exitosas.
- Diferencias autorizadas frente a inesperadas.
- PASS, FAIL, TIMEOUT y NOT EXECUTED separados.
- Veredicto de la hipótesis separado del resultado del test.
- Validación funcional, DOM, navegador visual y dispositivo real como garantías distintas.

No convertir una comparación de bytes en prueba suficiente de replay semántico. No convertir ausencia de fallo observado en garantía universal.

## 7. Punto de partida para construir demos después de S38

El estado de referencia aquí citado es el cierre documentado del 21 de septiembre de 2026; no una nueva ejecución de tests el día de creación de esta guía.

Se dispone de cuatro composiciones:

| Demo | Selector | Estatuto |
| --- | --- | --- |
| Retail | /?demo=retail-baseline | Control genérico mock |
| Hospitality Arrival | /?demo=hospitality-stay | Recorrido simulado de llegada |
| Family Adventure A | /?demo=hospitality-family-adventure | Vertical experimental A |
| Family Adventure B / Costa | /?demo=hospitality-family-adventure-costa | Contraste experimental B; no aceptación comercial |

Para preparar una demo concreta hay que definir cliente, audiencia, objetivo narrativo, composición inicial, datos/contenidos permitidos, capacidades que se mostrarán y criterio de aceptación visual. Esa elección no está hecha por este documento.

Consulta la [recapitulación de base](demo-construction-baseline-after-session-38.md), la [guía local del prototipo](../prototype/README.md) y el [protocolo de especificación de demos](demo-specification-protocol.md). Los documentos tempranos de planificación describen también objetivos futuros: no deben leerse como catálogo de capacidades ya implementadas.

Base preservada: Architecture v0.5; ADR-001–005 aceptados; TES y PSC sin modificaciones en S38; PSC-P01 abierto; PSC-P02 no creado. Mock/simulación no significa integración real. /showcase no significa validación en iPhone. Una demo que compila no está por ello aceptada comercialmente.

Esta guía documenta las 38 sesiones; no las reejecuta, no modifica el producto, no promueve sus artefactos experimentales y no selecciona la siguiente presión.
