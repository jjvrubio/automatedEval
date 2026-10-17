# 1. Executive adversarial verdict

La Arquitectura v0.1 no sobrevive intacta. Sus separaciones fundamentales son defendibles, pero tres propuestas eran demasiado absolutas y deben revisarse.

| Decisión | Veredicto |
|---|---|
| ADR-001 — TES Semantic Authority | **SURVIVES WITH QUALIFICATION** |
| ADR-002 — DemoPackage as Composition Root | **REVISE** |
| ADR-003 — Scenario / Experience / Demo Script | **SURVIVES WITH QUALIFICATION** |
| ADR-004 — Occurrence / Trace / Event / Projection | **REVISE** |
| Coverage A — Observed-field coverage | **Useful only under strict constraints** |
| Coverage B — Experience evidence/requirement coverage | **Useful only under strict constraints** |
| ADR-005 — Runtime State / Read Models | **SURVIVES WITH QUALIFICATION** |
| ADR-006 — Data Adapter Resolution | **REVISE** |

- **TES / Semantic Contract Fact:** TES sigue siendo la autoridad sobre el significado de Experience y su cadena experiencial, pero no prescribe arquitectura de software, persistencia, privacidad, integración o despliegue.

- **Architectural Inference:** `DemoPackage` no debe ser un objeto soberano que concentre toda la configuración y el runtime. Sobrevive como manifiesto declarativo de ensamblaje; la composición efectiva pertenece al bootstrap y a su entorno de despliegue.

- **Product Interpretation:** Scenario, Experience y Demo Script deben permanecer conceptualmente separados, aunque no completamente independientes.

- **Architectural Inference:** La distinción occurrence/trace/Event es válida, pero una tubería física obligatoria de cuatro objetos persistidos no lo es. Debe preservarse la distinción de responsabilidades sin imponer una única representación de almacenamiento.

- **Analytical Construct:** Coverage aporta utilidad limitada como instrumento exploratorio. No debe convertirse en KPI universal, porcentaje de Experience ni parte del vocabulario TES.

- **Architectural Inference:** La separación entre composición, estado mutable y read models sobrevive como separación lógica. No obliga a mantener tres copias persistentes del mismo dato.

- **Architectural Inference:** La resolución de fuentes durante el bootstrap sobrevive, pero la abstracción actual de un adaptador genérico por demo no soporta adecuadamente demostraciones híbridas.

# 2. Evidence hierarchy

La revisión utiliza la siguiente precedencia:

1. **TES / Semantic Contract Fact:** Extractos TES congelados, especialmente el [Experience Ledger](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/TES_Experience_Ledger.md>), la [Ontología de Acción Situada](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/TES_Ontologia_Accion_Situada.md>) y el [Léxico](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/TES_Lexico.md>).

2. **Product Interpretation:** Interpretaciones subordinadas, especialmente [experience-understanding.md](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/product-interpretations/experience-understanding.md>) y [observed-occurrence-trace-event.md](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/product-interpretations/observed-occurrence-trace-event.md>).

3. **Repository Fact:** Contratos y comportamiento realmente implementados en [contracts.ts](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts>), [routing.ts](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/routing.ts>), [mock-adapter.ts](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/mock-adapter.ts>) y [App.tsx](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/app/App.tsx>).

4. **Repository Fact:** Contratos candidatos y documentos de producto, como el [contrato de dominio](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/02-shared-contracts/experience-domain/README.md>) y el [marco de demo canónica](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/docs/canonical-demo-framework.md>).

5. **Architectural Inference:** Conclusiones derivadas de las evidencias anteriores.

- **Unresolved / Insufficient Evidence:** La API vigente de Convercus no está verificada. La documentación archivada no tiene autoridad suficiente para resolver contratos de producción.

# 3. ADR-001 falsification

## Supuestos descompuestos

La propuesta presupone que:

- TES proporciona significado suficientemente estable;
- los contratos ejecutables pueden mantener trazabilidad;
- TES y los contratos técnicos pueden versionarse independientemente;
- toda extensión legítima de producto puede formularse sin modificar TES;
- la subordinación no impedirá resolver necesidades técnicas.

## Evidencia favorable

- **TES / Semantic Contract Fact:** El Ledger define inequívocamente Experience, Evento, Pattern, Sequence, Progression, Result, Measurement y Learning.

- **Repository Fact:** Los documentos de interpretación declaran expresamente que son subordinados y no constituyen autoridad ontológica.

- **Repository Fact:** `ExperienceDefinition` ya incorpora `tesBaseline`, y `DemoPackage` puede identificar una baseline.

- **TES / Semantic Contract Fact:** TES distingue lo que el Ledger define de aquello que no define, como la implementación técnica completa de medición.

## Intento de falsificación

- **Counterexample:** TES no define deduplicación, reintentos, persistencia, privacidad, autorización, contratos HTTP, caches o resolución de adaptadores. Si “autoridad TES” se interpreta sobre toda decisión de producto, el desarrollo quedaría bloqueado.

- **Counterexample:** `Observed Occurrence`, `Trace`, `DemoPackage`, `AppSnapshot`, `DataAdapter` y `Demo Script` son necesidades de producto o arquitectura sin obligación de convertirse en entidades TES.

- **Counterexample:** Dos implementaciones pueden preservar la misma semántica y utilizar representaciones técnicas diferentes. TES no puede elegir entre event sourcing, estado derivado o snapshots.

- **Counterexample:** Un paquete antiguo puede apuntar a una baseline TES anterior. Reinterpretarlo silenciosamente con una baseline nueva destruiría reproducibilidad.

- **Counterexample:** Una ampliación legítima —por ejemplo, procedencia o idempotencia— puede no estar descrita por TES, aunque tampoco lo contradiga.

## Interacción con otros ADR

- ADR-002 debe referenciar baseline y contratos, no copiar sus definiciones.
- ADR-004 introduce conceptos técnicos subordinados.
- ADR-005 y ADR-006 quedan fuera de la autoridad técnica directa de TES.
- Scenario y Demo Script pueden simplificar la presentación, pero no redefinir una Experience.

## Veredicto

**SURVIVES WITH QUALIFICATION**

- **Recommendation:** TES debe ser autoridad sobre significado, relaciones e invariantes semánticos, no sobre decisiones técnicas o comerciales externas a su ámbito.

- **Recommendation:** Las extensiones de producto son legítimas cuando:

  - están clasificadas como no-TES;
  - no sustituyen conceptos TES;
  - no alteran silenciosamente su significado;
  - mantienen trazabilidad cuando operan una Experience.

- **Recommendation:** Cada Experience definition debe fijar la baseline con la que fue validada. Una actualización TES exige revisión o migración explícita, no reinterpretación automática.

- Evidencia favorable más fuerte: definiciones normativas y umbrales de deriva del Ledger.
- Evidencia falsificadora más fuerte: TES no pretende especificar arquitectura ejecutable.
- Supuesto no resuelto: procedimiento oficial de migración entre baselines.
- Consecuencia de error: o bien deriva semántica, o bien bloqueo indebido de extensiones técnicas legítimas.
- Confianza: **alta**.

# 4. ADR-002 falsification

## Supuestos descompuestos

La propuesta presupone que:

- existe un paquete principal por demo;
- todos los componentes pueden resolverse desde él;
- el paquete puede ser inmutable;
- referencias externas preservan reproducibilidad;
- configuración y runtime pueden separarse con claridad;
- prospecto y paquete tienen cardinalidad próxima a uno-a-uno.

## Evidencia favorable

- **Repository Fact:** Ya existe un `DemoPackage` tipado y validado en [demo-package.ts](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/demo-package.ts>).

- **Repository Fact:** El [paquete canónico](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/canonical-demo-package.ts>) agrupa identidad, marca, locale, modo, baseline, capacidades y Experiences.

- **Architectural Inference:** Una raíz declarativa ayuda a repetir, validar y comparar demos.

## Intento de falsificación

- **Counterexample:** Un grupo hotelero puede necesitar paquetes separados para hotel urbano, resort familiar, submarca premium y audiencia técnica, aunque el prospecto sea el mismo.

- **Counterexample:** Una demo puede tener varios scripts sobre el mismo escenario y varias variantes de escenario sobre las mismas Experiences.

- **Counterexample:** El estado vivo de una reserva, miembro o vuelo no puede residir en un paquete inmutable.

- **Counterexample:** La implementación de un adaptador y sus secretos dependen del entorno de despliegue. No deben viajar dentro del paquete.

- **Counterexample:** Referencias no versionadas a Experience, marca o fixture reducen reproducibilidad en vez de aumentarla.

- **Counterexample:** Un manifiesto que contiene marca, contenidos, fixtures, reglas, escenarios, módulos, scripts, adaptadores y reset puede convertirse en un “god configuration” difícil de validar y evolucionar.

- **Counterexample:** El deployment puede prohibir determinados proveedores o módulos aunque el paquete los solicite. El paquete no tiene autoridad final sobre lo que realmente puede arrancar.

## Interacción con otros ADR

- ADR-006 necesita que el entorno resuelva implementaciones reales.
- ADR-005 impide que el paquete posea estado mutable.
- ADR-003 permite que escenarios y scripts tengan ciclo de vida independiente.
- ADR-001 exige referencias semánticas versionadas.

## Veredicto

**REVISE**

`DemoPackage` sobrevive como manifiesto declarativo de una demo, pero no como única autoridad efectiva.

La composición revisada distingue:

```text
Demo manifest
    declara qué se desea ensamblar
            ↓
Bootstrap/deployment resolver
    determina qué puede resolverse y con qué implementación
            ↓
Runtime session
    mantiene el estado efectivo
```

- **Recommendation:** Permitir cero, uno o varios paquetes por prospecto.

- **Recommendation:** Versionar o fijar mediante digest las referencias necesarias para reproducibilidad.

- **Recommendation:** El paquete debe declarar requisitos lógicos de datos y capacidades; el entorno aporta implementaciones, credenciales y restricciones.

- **Recommendation:** Evitar un único documento monolítico. Puede existir una raíz pequeña con referencias a artefactos cohesionados.

- Evidencia favorable más fuerte: necesidad de una unidad repetible de ensamblaje.
- Evidencia falsificadora más fuerte: configuración declarada, disponibilidad del deployment y estado vivo poseen autoridades diferentes.
- Supuesto no resuelto: granularidad y mecanismo exacto de referencias.
- Consecuencia de error: paquete monolítico, secretos filtrados, versiones incompatibles o demos no reproducibles.
- Confianza: **media-alta**.

# 5. ADR-003 falsification

## Supuestos descompuestos

La propuesta presupone que:

- Experience tiene identidad fuera de una demo;
- Scenario contextualiza sin redefinir;
- Demo Script solo dirige la presentación;
- sus ciclos de vida pueden separarse;
- la indirection resultante es manejable.

## Evidencia favorable

- **TES / Semantic Contract Fact:** Experience posee estructura propia y no puede reducirse a un caso comercial o a una lista de acciones del presentador.

- **Repository Fact:** El marco canónico distingue configuración, fidelización, Experience, participación, escenario y ejecución.

- **Product Interpretation:** El mismo evento puede desempeñar papeles diferentes según Experience y participación.

## Intento de falsificación

- **Counterexample:** Una Experience de “estancia familiar en resort” puede depender de reglas, roles y resultados que solo tienen sentido en ese contexto.

- **Counterexample:** Un script puede necesitar efectuar una reserva, cancelar una actividad o emitir una señal. No es exclusivamente texto de presentación.

- **Counterexample:** Dos scripts pueden requerir estados iniciales incompatibles. Si ambos pertenecen al mismo Scenario, el Scenario deja de determinar por completo sus condiciones iniciales.

- **Counterexample:** Crear objetos separados para un demo de fidelización estático sin Experiences puede producir indirection sin valor.

- **Counterexample:** Una Experience reutilizada en dos marcas puede necesitar vocabulario y visualización distintos sin dejar de ser la misma transformación.

## Resultado del ataque

Los contraejemplos no obligan a fusionar los conceptos. Obligan a definir dependencias legítimas:

- Scenario puede referenciar e instanciar Experience definitions.
- Scenario puede aportar actores, roles, contexto, fixtures y condiciones iniciales.
- Una Experience puede ser específica de un prospecto y seguir siendo distinta del Scenario que la instancia.
- Demo Script puede invocar comandos públicos del escenario.
- Demo Script no debe implementar reglas ni mutar directamente el estado canónico.
- Si dos scripts requieren mundos iniciales materialmente diferentes, deben referenciar variantes o checkpoints explícitos.

## Veredicto

**SURVIVES WITH QUALIFICATION**

- **Recommendation:** Mantener las tres abstracciones, pero hacer Scenario y Demo Script opcionales cuando no aporten valor.

- **Recommendation:** La dependencia debe fluir así:

```text
Experience definition
        ↑ referenciada por
Scenario
        ↑ demostrado mediante
Demo Script
```

- **Recommendation:** El contenido y tono específicos de marca deben resolverse en la presentación o el escenario, no duplicar una Experience solo por diferencias editoriales.

- Evidencia favorable más fuerte: TES impide reducir Experience a narrativa o activación.
- Evidencia falsificadora más fuerte: los scripts necesitan provocar acciones y algunos escenarios condicionan fuertemente la Experience.
- Supuesto no resuelto: identidad y ciclo de vida de participaciones colectivas.
- Consecuencia de error: duplicación de Experiences o scripts convertidos en motores de dominio.
- Confianza: **media-alta**.

# 6. ADR-004 falsification

## Supuestos descompuestos

La propuesta presupone que:

- existe una occurrence discreta identificable;
- puede conservarse una traza;
- el Evento puede reconocerse después;
- occurrence, trace y Event pueden representarse por separado;
- una occurrence puede evaluarse contra varias Experiences;
- preservar el original siempre es viable.

## Evidencia favorable

- **TES / Semantic Contract Fact:** No todo hecho observable es un Evento significativo.

- **Product Interpretation:** [observed-occurrence-trace-event.md](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/product-interpretations/observed-occurrence-trace-event.md>) separa instrumentación y plano experiencial sin extender TES.

- **Repository Fact:** `ActivityItem` contiene icono, tono, copy y fecha formateada, confirmando que Activity es una proyección.

- **Repository Fact:** `evaluateEventAcrossExperiences` ya permite evaluaciones independientes, aunque el runtime no la utilice.

## Intento de falsificación

- **Counterexample:** Un workflow puede emitir un evento ya clasificado semánticamente para una Experience concreta.

- **Counterexample:** Una API puede exponer únicamente eventos interpretados, sin acceso a una occurrence previa.

- **Counterexample:** Un patrón de abandono puede inferirse de la ausencia de acciones; no existe una occurrence discreta que lo represente por sí sola.

- **Counterexample:** “Tres viajes sostenibles en siete días” es un hecho agregado derivado de varias ocurrencias y una ventana temporal.

- **Counterexample:** Una compra online, el ticket de tienda y el asiento contable pueden ser tres trazas de una sola ocurrencia.

- **Counterexample:** Una corrección o devolución puede invalidar la interpretación previa sin borrar el hecho histórico.

- **Counterexample:** Un evento tardío puede modificar retrospectivamente una secuencia.

- **Counterexample:** Una restricción de privacidad puede permitir conservar solo un hash, referencia o agregado, no la occurrence completa.

- **Counterexample:** Un sistema puede registrar una occurrence duplicada varias veces.

- **Counterexample:** Un evento experiencial puede resultar de inferencia probabilística y no de observación directa.

- **Counterexample:** Algunas occurrences son generadas dentro de una Experience y nacen con contexto, aunque su significación siga sin ser una propiedad universal.

## Many-to-many bajo ataque

- **Product Interpretation:** Soportar evaluación frente a cero, una o varias Experiences es fuertemente compatible con TES, pero no una cardinalidad TES explícita.

- **Architectural Inference:** La capacidad de evaluar múltiples Experiences es necesaria para los escenarios comerciales ya contemplados.

- **Counterexample:** Muchas occurrences tendrán un destino técnico exclusivo o no serán evaluadas experiencialmente.

- **Conclusion:** Many-to-many debe ser una capacidad soportada, no una relación estática obligatoria ni una tabla de pertenencia precomputada.

## Veredicto

**REVISE**

Sobreviven las distinciones; no sobrevive una materialización universal rígida.

- **Recommendation:** Utilizar un modelo de evidencia/procedencia capaz de representar, según la fuente:

  - observación directa;
  - referencia externa;
  - evento ya interpretado;
  - inferencia;
  - agregado;
  - corrección o retractación;
  - múltiples trazas del mismo hecho.

- **Recommendation:** No exigir que todos esos elementos se almacenen como objetos completos y separados.

- **Recommendation:** La significación contextual debe quedar vinculada a Experience, versión, participación y evaluación. No debe sobrescribir la evidencia de entrada.

- **Recommendation:** Activity permanece como read model derivado y puede omitir complejidad, pero debe conservar suficiente procedencia para no presentar simulación como realidad.

- Evidencia favorable más fuerte: distinción TES entre hecho observable y Evento significativo.
- Evidencia falsificadora más fuerte: no todos los Eventos proceden de una occurrence discreta preservable y no todas las fuentes exponen el plano previo.
- Supuesto no resuelto: capacidades reales de la API y restricciones de privacidad.
- Consecuencia de error: almacenamiento redundante, falsa precisión, imposibilidad de integrar fuentes o pérdida de trazabilidad.
- Confianza: **media**.

# 7. Coverage falsification experiment

## Modelo A — Observed-field coverage

### Ataque

- **Counterexample:** `U` nunca representa “todo el comportamiento”; solo aquello instrumentado dentro de un límite de canal, tiempo y consentimiento.

- **Counterexample:** Dos Experiences pueden compartir muchas occurrences y no ser redundantes porque interpretan transformaciones distintas.

- **Counterexample:** Una Experience con pocas occurrences puede ser más importante que otra con miles. La cardinalidad no mide valor ni relevancia.

- **Counterexample:** Un elemento “no cubierto” puede ser irrelevante para cualquier Experience.

- **Counterexample:** `S_E` no es necesariamente estable: cambia con la versión de reglas, contexto y participación.

- **Counterexample:** Buscar el conjunto mínimo de Experiences que cubre `U` podría incentivar diseños amplios y semánticamente débiles.

### Valor residual

- **Analytical Construct:** Las intersecciones pueden revelar concentración de evaluaciones sobre las mismas occurrences.
- **Analytical Construct:** Los elementos no relacionados pueden sugerir lagunas de instrumentación o posibles zonas de descubrimiento.
- **Analytical Construct:** La comparación entre versiones puede ayudar a detectar cambios en el alcance observable.

### Clasificación

**Useful only under strict constraints**

Condiciones:

- `U` debe estar delimitado por periodo, escenario, fuente, población y consentimiento.
- `S_E` debe significar “occurrences evaluadas como relevantes bajo una versión concreta”, no “acciones cubiertas por la Experience”.
- No debe utilizarse como KPI de éxito, amplitud estratégica o calidad.
- Los conteos deben acompañarse de interpretación cualitativa.

Término recomendado: **Experience-portfolio observation overlap** o **mapa de solapamiento observacional del portfolio**.

Debe evitarse “Experience coverage” sin calificador.

## Modelo B — Experience requirement/evidence coverage

### Ataque

- **Counterexample:** Las evidencias pueden ser ordinales y no intercambiables.
- **Counterexample:** Un requisito crítico ausente no se compensa con diez requisitos menores.
- **Counterexample:** Pattern y Sequence no son colecciones planas de casillas.
- **Counterexample:** Una Experience puede tener evidencia abundante sin haber producido Progression o Result.
- **Counterexample:** Un porcentaje ocultaría ramas, estados, calidad, contradicciones y temporalidad.

### Valor residual

- **Analytical Construct:** Puede ser útil declarar qué requisitos tienen evidencia suficiente, insuficiente, contradictoria o pendiente.
- **Analytical Construct:** Puede ayudar a diagnosticar reconstruibilidad sin afirmar progreso.
- **Analytical Construct:** En reglas discretas y validadas puede apoyar la inspección de una participación.

### Clasificación

**Useful only under strict constraints**

Término recomendado: **Experience evidence sufficiency profile** o **perfil de suficiencia de evidencia**.

- No debe presentarse necesariamente como número.
- No debe denominarse Progression.
- No debe determinar Completion o Result por agregación.
- Debe preservar requisitos críticos, ordinalidad, dependencias y calidad de evidencia.

## Decisión conjunta

- **Analytical Construct:** La hipótesis añade cierto valor diagnóstico, pero el término genérico `coverage` introduce más ambigüedad que precisión.

- **Recommendation:** Retener los dos análisis solo con nombres diferentes y fuera del contrato TES.

# 8. ADR-005 falsification

## Supuestos descompuestos

La propuesta presupone tres planos:

1. composición inmutable;
2. estado mutable;
3. read models.

También presupone que separar los planos no causará duplicación excesiva.

## Evidencia favorable

- **Repository Fact:** Hoy `AppSnapshot` opera simultáneamente como respuesta del adaptador y modelo de lectura.

- **Repository Fact:** El mock muta directamente `activity`, mientras que Experience state y routing permanecen fuera del runtime.

- **Repository Fact:** El marco canónico exige reset, participaciones independientes, trazabilidad y simulación offline.

## Intento de falsificación

- **Counterexample:** Una demo estática puede obtener directamente un read model del adaptador sin estado canónico intermedio.

- **Counterexample:** En modo live, el backend puede ser autoridad y duplicar su estado en el navegador crea sincronización y staleness.

- **Counterexample:** Mantener interaction store, Experience state y varias proyecciones podría exceder las necesidades de una demo.

- **Counterexample:** Un reset determinista no puede restablecer datos reales externos.

- **Counterexample:** Ciertos estados inferidos no pueden reconstruirse de manera determinista si dependen de reloj, datos externos o reglas no versionadas.

## Resultado del ataque

La separación conceptual permanece necesaria, pero no implica tres almacenes.

Posibles configuraciones mínimas:

| Tipo de demo | Estado mínimo |
|---|---|
| Mock estático | Read model directo |
| Simulación interactiva | Estado local canónico + proyecciones |
| Híbrida | Estado externo referenciado + overlay local |
| Live | Fuente externa como autoridad + caché/read model local |

## Veredicto

**SURVIVES WITH QUALIFICATION**

- **Recommendation:** Separar responsabilidades lógicas, no duplicar automáticamente datos.

- **Recommendation:** Introducir estado canónico local solo cuando haya acciones, simulación, auditoría o reset que lo requieran.

- **Recommendation:** `AppSnapshot` puede sobrevivir como read model.

- **Recommendation:** El reset determinista solo aplica al estado controlado por la demo. En modo live debe utilizar un sandbox, fixture, overlay o procedimiento explícito.

- Evidencia favorable más fuerte: la demo interactiva necesita evitar que la UI sea fuente de verdad.
- Evidencia falsificadora más fuerte: las demos simples o live no necesitan un store canónico local completo.
- Supuesto no resuelto: cantidad de interacción local requerida en las primeras demos.
- Consecuencia de error: duplicación, inconsistencias y una plataforma de eventos innecesaria.
- Confianza: **alta**.

# 9. ADR-006 falsification

## Supuestos descompuestos

La propuesta presupone que:

- el adaptador es una frontera uniforme;
- se resuelve durante el bootstrap;
- un adaptador puede atender toda la demo;
- `TSnapshot/TEvent` puede cubrir fuentes reales y simuladas;
- el paquete puede seleccionar su política.

## Evidencia favorable

- **Repository Fact:** `App.tsx` instancia directamente `MockDataAdapter`, impidiendo composición externa.

- **Repository Fact:** `DataAdapter<TSnapshot,TEvent>` ya establece una costura técnica mínima.

- **Repository Fact:** El marco de demo anticipa mock, simulation, staging y production.

## Intento de falsificación

- **Counterexample:** Una demo híbrida puede utilizar perfil real, cupones reales, interacciones simuladas y evaluación propuesta.

- **Counterexample:** Un único `mode` no expresa procedencia por capacidad.

- **Counterexample:** Algunos proveedores pueden exponer read models; otros, eventos; otros, operaciones; otros, estado remoto.

- **Counterexample:** Una API real puede invalidar `getSnapshot/dispatch/reset`. Por ejemplo, puede no permitir reset o dispatch genérico.

- **Counterexample:** Las credenciales y endpoints pertenecen al deployment, no al DemoPackage.

- **Counterexample:** Dos proveedores pueden contribuir a una misma proyección y requerir coordinación, precedencia o reconciliación.

## Veredicto

**REVISE**

- **Recommendation:** Resolver proveedores durante bootstrap, pero hacerlo por capability/port cuando sea necesario.

- **Recommendation:** El manifiesto declara necesidades y bindings lógicos; un registro del deployment aporta implementaciones concretas.

- **Recommendation:** No imponer un único contrato universal. Pueden existir puertos diferenciados para:

  - lectura de perfil o fidelización;
  - recepción de evidencias;
  - ejecución de comandos;
  - Experience state;
  - read models externos.

- **Recommendation:** `DataAdapter<TSnapshot,TEvent>` puede conservarse temporalmente para el prototipo, pero no debe declararse contrato definitivo antes de verificar la API.

- Evidencia favorable más fuerte: la instancia directa del mock bloquea personalización.
- Evidencia falsificadora más fuerte: una demo híbrida necesita varias fuentes con formas distintas.
- Supuesto no resuelto: contratos reales de la API.
- Consecuencia de error: adaptador monolítico, lógica de conciliación oculta y falsa declaración de realidad.
- Confianza: **alta** sobre la revisión; **baja** sobre la forma final de los puertos.

# 10. Cross-ADR contradictions

| Contradicción | Resolución revisada |
|---|---|
| Paquete inmutable vs datos vivos | El paquete declara composición; los proveedores aportan estado vivo |
| Paquete vs discovery de adaptadores | El paquete solicita bindings; deployment/bootstrap los resuelve |
| TES versionado vs contratos técnicos | Baselines y contratos tienen versiones independientes y trazables |
| Fixtures del Scenario vs estado runtime | Fixtures son semillas; el runtime crea estado de sesión |
| Demo Script vs reglas de dominio | El script invoca comandos públicos; no implementa reglas |
| Occurrence store vs datos del adaptador | Se conserva evidencia o referencia según procedencia y necesidad |
| Reset determinista vs live | Reset se limita al estado local o a entornos controlados |
| Activity con real y simulado | Procedencia conservada por ítem y disclosure en la superficie apropiada |
| Un prospecto vs un paquete | Relación uno-a-muchos |
| Experience reutilizable vs contexto sectorial | Scenario liga contexto y actores sin redefinir la transformación |
| Capability declarada vs efectiva | Diferenciar capacidad solicitada, resuelta y disponible |
| Read model vs estado canónico | El primero deriva del segundo cuando existe; puede venir directo en demos estáticas |

- **Architectural Inference:** El acoplamiento oculto más importante era asumir que una única raíz podía ser simultáneamente catálogo, deployment plan, política de integración y garantía de runtime.

- **Recommendation:** La arquitectura debe distinguir composición deseada de composición efectiva.

# 11. Sector stress tests

| Sector | Caso que tensiona la arquitectura | Resultado |
|---|---|---|
| Airline | Reserva corregida, reemisión y vuelo retrasado llegan fuera de orden | ADR-004 necesita correcciones, correlación y temporalidad |
| Airline | Loyalty real con preparación de viaje simulada | ADR-006 necesita proveedores por capacidad |
| Retail | Ticket físico y transacción online duplican una compra | Occurrence y Trace no pueden ser uno-a-uno |
| Retail | Devolución revierte puntos y afecta Experiences previas | El estado necesita compensación, no borrado |
| Movilidad | Solo se reciben agregados diarios por privacidad | No puede exigirse preservar occurrences individuales |
| Movilidad | Ausencia de uso detecta abandono | Un Evento inferido puede no tener occurrence discreta |
| Hospitality | Un grupo comparte reserva, pero cada huésped tiene Experiences diferentes | `memberId` es insuficiente como sujeto universal |
| Hospitality | Business hotel y resort comparten marca matriz y parte de las Experiences | Un prospecto necesita varios paquetes/escenarios |
| Hospitality | Una cena afecta estancia familiar y descubrimiento gastronómico | Debe soportarse evaluación contextual múltiple |
| Hospitality | Dos scripts parten de checkpoints diferentes | Script necesita declarar precondiciones o variante |
| Hospitality | Submarca cambia tono, servicios y navegación | Brand y módulos no pueden estar fijados al núcleo |
| Hospitality | Estado de reserva real y actividades simuladas | Requiere runtime híbrido y disclosure de procedencia |

## Resultado del stress test

- **Counterexample:** El caso hospitality invalida el supuesto de que toda participación pueda identificarse solo por `memberId`.

- **Recommendation:** La arquitectura debe admitir referencias de sujeto y contexto extensibles: individuo, grupo, booking, stay, account u otra unidad operacional.

- **Counterexample:** Un hotel group no se corresponde con un paquete único.

- **Product Interpretation:** Experiences pueden reutilizarse entre escenarios, pero algunas serán legítimamente específicas de un contexto o prospecto.

- **Architectural Inference:** Ningún sector obliga todavía a crear forks del núcleo. Sí obliga a que paquetes, contextos, participantes, módulos y proveedores sean extensibles.

# 12. Revised decision matrix

| Decisión revisada | Estado | Confianza |
|---|---|---|
| TES gobierna significado e invariantes, no implementación | **SURVIVES WITH QUALIFICATION** | Alta |
| Un manifiesto versionado declara la composición deseada | **REVISE** | Media-alta |
| Bootstrap/deployment determina la composición efectiva | **REVISE** | Media-alta |
| Scenario, Experience y Demo Script permanecen distintos | **SURVIVES WITH QUALIFICATION** | Media-alta |
| Evidence/occurrence y Event no se fusionan | **REVISE** | Media |
| Activity es una proyección | **SURVIVES** dentro de ADR-004 | Alta |
| Evaluación contextual múltiple es capacidad, no cardinalidad TES | **SURVIVES WITH QUALIFICATION** | Media |
| Composition, runtime state y read models son planos distintos | **SURVIVES WITH QUALIFICATION** | Alta |
| Un estado canónico local siempre es obligatorio | **REJECT** | Alta |
| Adaptadores/proveedores se resuelven fuera de `App.tsx` | **SURVIVES** dentro de ADR-006 | Alta |
| Un adaptador genérico por demo es suficiente | **REJECT** | Alta |
| Coverage es una magnitud universal | **REJECT** | Alta |
| Dos diagnósticos restringidos de coverage pueden conservarse | **DEFER / EXPERIMENTAL** | Media-baja |

# 13. Rejected assumptions

Las siguientes ideas de Sessions 1–2 no deberían guiar la implementación:

1. **Rejected assumption:** Un prospecto equivale a un único `DemoPackage`.
2. **Rejected assumption:** `DemoPackage` debe contener o controlar todas las preocupaciones.
3. **Rejected assumption:** La configuración declarada determina por sí sola la composición efectiva.
4. **Rejected assumption:** Toda fuente puede adaptarse limpiamente a `getSnapshot/dispatch/reset`.
5. **Rejected assumption:** Una demo utiliza un único adaptador y un único `dataMode`.
6. **Rejected assumption:** Siempre debe existir un estado canónico local completo.
7. **Rejected assumption:** Reset determinista puede aplicarse igual a datos mock y live.
8. **Rejected assumption:** Cada Evento TES procede de una occurrence discreta preservable.
9. **Rejected assumption:** Occurrence, Trace y Evento tienen cardinalidad uno-a-uno.
10. **Rejected assumption:** La relación occurrence–Experience debe materializarse como pertenencia estática.
11. **Rejected assumption:** `memberId` identifica universalmente toda participación.
12. **Rejected assumption:** Un porcentaje genérico puede expresar progression, evidence satisfaction o coverage.
13. **Rejected assumption:** La acumulación de occurrences aporta por sí misma Pattern o Progression.
14. **Rejected assumption:** Un Demo Script es solo texto pasivo.
15. **Rejected assumption:** Referenciar artefactos siempre mejora reproducibilidad sin versionarlos o fijarlos.

# 14. Deferred questions

## Requieren evidencia de API

- Contratos reales de autenticación, lectura, comandos y eventos.
- Disponibilidad de IDs estables y claves de idempotencia.
- Existencia de eventos interpretados o datos previos a su interpretación.
- Soporte de Experience state y Workflows.
- Capacidad de staging/reset.
- Procedencia y granularidad de datos.

## Requieren aclaración TES

- Ciclo de vida formal de una participación.
- Sujeto individual frente a colectivo.
- Ramas, repetición, N-de-M y eventos tardíos.
- Relación entre evidencia contradictoria y reconstruibilidad.
- Resultado de una Experience no completada.

## Requieren validación de producto

- Granularidad real de Scenario y sus variantes.
- Alcance de los comandos permitidos a Demo Script.
- Nivel de disclosure real/simulated en la interfaz comercial.
- Reutilización de Experience definitions entre sectores.
- Necesidad real de visualizar evaluación multiexperiencia.

## Requieren uso con un prospecto real

- Modelado de booking, stay, group y roles.
- Separación entre grupo hotelero y submarcas.
- Qué configuración cambia realmente entre demos.
- Qué contenido debe ser reutilizable y qué contenido es prospect-specific.

## Requieren experimento

- Manifiesto único frente a varios artefactos referenciados.
- Selección runtime frente a build autocontenido.
- Proveedores por capability.
- Overlay local sobre datos live.
- Valor analítico real de las dos nociones de coverage.

# 15. Demo Factory Architecture v0.2

```text
┌──────────────────────────────────────────────────────────┐
│ TES semantic authority                                   │
│ Significado, relaciones e invariantes experienciales     │
└──────────────────────────┬───────────────────────────────┘
                           │ trazabilidad
┌──────────────────────────▼───────────────────────────────┐
│ Versioned product contracts                              │
│ Traducción funcional + extensiones técnicas clasificadas │
└───────────────┬──────────────────────────┬───────────────┘
                │                          │
        ┌───────▼────────┐        ┌────────▼────────┐
        │ Experience     │        │ Reusable assets │
        │ definitions    │        │ brands/modules  │
        └───────┬────────┘        │ content/scripts │
                │                 └────────┬────────┘
                └──────────────┬───────────┘
                               │ referencias versionadas
                    ┌──────────▼───────────┐
                    │ Demo manifest        │
                    │ Prospect/demo ID     │
                    │ Scenario bindings    │
                    │ Capability needs     │
                    │ Fixtures/reset scope │
                    └──────────┬───────────┘
                               │ composición deseada
                    ┌──────────▼───────────┐
                    │ Bootstrap resolver   │
                    │ Deployment policy    │
                    │ Provider registry    │
                    └──────────┬───────────┘
                               │ composición efectiva
             ┌─────────────────▼──────────────────┐
             │ Demo runtime session               │
             │ Optional local state               │
             │ Evidence/provenance references     │
             │ Participation/context state        │
             │ Evaluation and effects             │
             └─────────────────┬──────────────────┘
                               │ selectors/adapters
                    ┌──────────▼───────────┐
                    │ Read models          │
                    │ Activity/UI modules  │
                    │ Presenter controls   │
                    └──────────────────────┘
```

## Autoridades revisadas

- **TES:** significado e invariantes.
- **Product contracts:** traducción funcional versionada.
- **Experience definition:** transformación reusable y semánticamente trazada.
- **Scenario:** contextualización, actores, bindings y estado inicial.
- **Demo manifest:** composición declarada de una demo.
- **Deployment/bootstrap:** composición realmente resoluble.
- **Providers:** acceso a capacidades y fuentes.
- **Runtime session:** estado mutable controlado por la demo.
- **Read models:** presentación.
- **Demo Script:** secuencia de demostración mediante comandos públicos.

## Invariantes sobrevivientes

1. Una occurrence no implica automáticamente un Evento TES.
2. Un Evento no produce automáticamente Progression.
3. Activity no es fuente factual o semántica soberana.
4. Pattern no se reduce a una colección.
5. La interpretación no debe borrar la evidencia de procedencia disponible.
6. Experience, Scenario y Demo Script no se sustituyen entre sí.
7. El estado mutable no reside en el manifiesto.
8. El deployment no redefine TES.
9. La veracidad debe poder declararse por capacidad y fuente.
10. El núcleo no debe asumir un único tipo de sujeto, contexto o proveedor.

# 16. ADR readiness

| Decisión | Readiness | Motivo |
|---|---|---|
| TES como autoridad semántica acotada | **Ready to write as ADR** | Límite respaldado por el propio corpus |
| Manifiesto declarativo + bootstrap efectivo | **Provisional ADR** | Falta probar granularidad y referencias |
| Separación Scenario/Experience/Demo Script | **Provisional ADR** | Falta validar grupo, contexto y checkpoints |
| Evidence/Occurrence/Event/Projection | **Provisional ADR** | Depende de API, privacidad y fuentes |
| Planos composition/state/read model | **Ready to write as ADR** | Puede adoptarse sin imponer stores |
| Resolución de providers por capability | **Provisional ADR** | La API puede cambiar la forma de los puertos |
| Coverage A | **Not ready for ADR** | Solo hipótesis analítica |
| Coverage B | **Not ready for ADR** | Necesita casos reales y terminología validada |

# 17. Minimum reversible experiment

El experimento mínimo debería cargar dos configuraciones de prospecto sobre el núcleo actual:

- una demo retail próxima al prototipo actual;
- una demo de hospitality con marca, contenido, fixtures y Scenario diferentes.

## Alcance

Cada configuración declararía:

- ID de demo y prospecto;
- referencia de marca;
- locale;
- módulos visibles;
- fixture inicial;
- capacidad y procedencia;
- Scenario opcional;
- Demo Script opcional;
- política de reset local.

Un bootstrap delgado seleccionaría una configuración por mecanismo explícito y resolvería el proveedor mock existente con fixtures distintos.

## Qué debe probar

1. La misma aplicación puede arrancar ambas demos sin editar `App.tsx` para cambiar de prospecto.
2. Marca, contenido y datos no se filtran entre demos.
3. Un prospecto puede tener más de una demo.
4. El reset local es determinista.
5. Activity sigue siendo una proyección.
6. Las capacidades declaran su procedencia.
7. Un script puede invocar una acción pública sin mutar directamente el estado.
8. La configuración hospitality puede representar un contexto booking/stay y más de un actor.
9. Las referencias inexistentes o incompatibles fallan durante bootstrap.
10. El experimento puede retirarse eliminando el resolver y las dos configuraciones, sin migraciones ni backend.

## Fuera del experimento

- API real;
- motor completo de Experiences;
- Builder;
- multi-tenancy;
- persistencia productiva;
- cálculo de coverage;
- refactor general de la UI.

- **Recommendation:** No implementar el modelo completo occurrence/trace hasta que el experimento demuestre que una interacción observable necesita evaluación contextual real dentro de las dos demos.

# 18. Meta-review

1. **¿Qué supuesto fue más fácil de falsificar?**  
   `DemoPackage` como raíz soberana y uno por prospecto. Hospitality demuestra rápidamente que un prospecto puede necesitar múltiples demos, escenarios y deployments.

2. **¿Qué supuesto sobrevivió el ataque más fuerte?**  
   TES como autoridad semántica, una vez limitado su ámbito. Ningún contraejemplo técnico exige redefinir Experience; solo exige conceptos técnicos adicionales claramente clasificados.

3. **¿Qué supuesto sigue siendo más peligroso?**  
   Que un modelo neutral de `Observed Occurrence` pueda normalizar todas las fuentes. Parece razonable, pero API, privacidad, agregados e inferencias pueden invalidarlo.

4. **¿Qué es más probable que se esté sobrediseñando?**  
   Un runtime canónico completo de eventos, evidencias y proyecciones antes de verificar API y necesidades de las primeras demos.

5. **¿Qué es más probable que se esté modelando insuficientemente?**  
   Sujeto, contexto y participación: individuo, grupo, booking, stay, account, roles y correlaciones. También procedencia, correcciones y mezcla real/simulada.

6. **¿Coverage añadió valor?**  
   Sí, pero solo como dos diagnósticos restringidos y con nombres distintos. El término genérico añadió ambigüedad. No justifica todavía una feature ni un KPI.

7. **¿Qué evidencia revisaría de nuevo v0.2?**  
   Principalmente:

   - contratos verificados de la API;
   - una demo real de hospitality;
   - restricciones concretas de privacidad;
   - comportamiento real de Workflows;
   - aclaraciones TES sobre participación y secuencias;
   - evidencia de que los prospectos necesitan builds aislados en lugar de selección runtime.

# 19. Confidence and evidence gaps

## Confianza alta

- **Repository Fact:** El runtime está acoplado directamente a `MockDataAdapter`.
- **Repository Fact:** `DemoPackage` no compone hoy la aplicación.
- **Repository Fact:** Activity es un modelo de presentación.
- **TES / Semantic Contract Fact:** Evento, Pattern, Sequence, Progression y Result no son equivalentes.
- **Architectural Inference:** Composition, mutable state y read models necesitan autoridades distintas.
- **Architectural Inference:** Un adaptador monolítico por demo no cubre bien fuentes híbridas.

## Confianza media

- **Product Interpretation:** Evaluación contextual frente a múltiples Experiences.
- **Architectural Inference:** Necesidad de providers por capability.
- **Architectural Inference:** Forma revisada de Scenario y Demo Script.
- **Architectural Inference:** Modelo de evidencia/procedencia flexible.

## Confianza baja o insuficiente

- **Unresolved / Insufficient Evidence:** Contratos vigentes de API.
- **Unresolved / Insufficient Evidence:** Necesidad de persistir occurrences o trazas.
- **Unresolved / Insufficient Evidence:** Cardinalidad real de sujetos y participaciones.
- **Unresolved / Insufficient Evidence:** Topología ejecutable de Experiences.
- **Unresolved / Insufficient Evidence:** Utilidad comercial de coverage.
- **Unresolved / Insufficient Evidence:** Necesidad real de selección runtime frente a builds aislados.
- **Unresolved / Insufficient Evidence:** Requisitos productivos de privacidad y consentimiento.

No se modificó ningún archivo ni se implementó el experimento propuesto.