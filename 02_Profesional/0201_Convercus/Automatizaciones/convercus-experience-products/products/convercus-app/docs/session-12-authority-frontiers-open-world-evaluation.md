---
title: "Session 12 — Fronteras de autoridad y semántica de evaluación open-world"
aliases:
- "Authority Frontiers and Open-World Evaluation Semantics"
language: es
version: "v1.0"
status: "consolidated analysis"
date: "2026-09-04"
project: "Convercus Experience Products"
document_type: "informe de análisis y consolidación de arquitectura"
scope: "autoridad de claims, evaluación contextual open-world y ambigüedad de ExperienceDefinition"
repository_role: "preparación de ADR-005 y del siguiente experimento falsable"
semantic_authority: "análisis de producto/arquitectura subordinado; Authority Frontier no es un concepto TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 12 — Fronteras de autoridad y semántica de evaluación open-world

## 1. Conclusión ejecutiva

ADR-001–004 permanecen compatibles con Session 11. No existe una contradicción genuina: las decisiones aceptadas ya separan autoridad semántica, factual, compositiva, operacional y de presentación. Session 11 encaja como investigación subordinada. Sí aparecen dos fronteras no resueltas: quién puede clasificar una actividad y cuándo existe autoridad suficiente para afirmar una evaluación negativa.

**Authority Frontier** añade poder explicativo frente a “capas” porque no solo ordena componentes: delimita los claims que cada actor está autorizado a emitir y exige una nueva validación al cruzar el límite. Ayuda a detectar *authority laundering*: que un dato de provider, un baseline nominal, una clasificación de Scenario o un read model parezcan adquirir autoridad semántica por circular por el sistema.

La semántica binaria de Session 11 no es promovible. `evaluateEvidenceRelevance()` devuelve `false` para tres situaciones distintas: contexto stay/property incompatible, actividad ausente del catálogo y clasificación sin intersección. Los reason codes conservan parte de la diferencia, pero el booleano colapsa desconocimiento, insuficiencia y negativo. Incluso Cooking Class → Active Challenge solo es un negativo seguro si una autoridad competente afirma que la clasificación es completa o que Cooking Class está excluida de sport/wellness. La mera ausencia de la etiqueta no basta en un mundo abierto.

Los tres artefactos llamados o tratados como `ExperienceDefinition` también poseen autoridades distintas. Una candidata de Session 10 referencia una baseline **interpretada**, el contrato rico es una traducción funcional provisional y el tipo Demo Factory es solo un descriptor runtime. `tesBaseline` no demuestra validación. El nombre común crea riesgo material de falsa autoridad, aunque puede mitigarse mediante terminología y metadata de relación TES sin renombrar todavía.

El invariant propuesto para ADR-005 es conceptualmente sólido, pero su comportamiento open-world carece de evidencia ejecutable. La recomendación única es **Option B — realizar un experimento focalizado adicional antes de ADR-005**. Debe distinguir un negativo conocido de una evaluación indeterminada, sin fijar enum universal, taxonomía ni precedencia arbitraria.

## 2. Compatibilidad de ADR-001–004

| ADR | Autoridad ya explícita | Autoridad solo implícita o frontera abierta | Impacto de Session 11 | Veredicto |
|---|---|---|---|---|
| ADR-001 — Bounded TES Semantic Authority | TES gobierna significado, relaciones e invariantes; producto gobierna traducción/arquitectura subordinada; read models no redefinen TES; baseline y versión técnica son distintas. | La frase “toda `ExperienceDefinition`” no distingue candidata, validada y descriptor. `tesBaseline` no especifica si fue interpretada, validada o asociada. | El evaluator es construcción de producto y no afirma TES Event; es compatible. La pluralidad de artefactos hace visible la ambigüedad nominal. | **Compatible; requiere aclaración de alcance futura, no reconsideración.** |
| ADR-002 — Composition / runtime / read models | Declara autoridad de composición, runtime/source y proyección; Activity no es evidencia ni Evento TES. | No asigna autoridad para clasificar inputs ni para producir un claim relacional. | El evaluator puro no usa Activity y no muta runtime. | **Compatible; nueva frontera subordinada.** |
| ADR-003 — Desired / effective composition | Manifest declara intención; bootstrap valida/resuelve; deployment aporta capacidades; runtime/read model no se confunden. | No decide cómo se resuelve una autoridad de clasificación ni cómo se cualifica una evaluación. | Los contexts de Session 11 son fixtures locales no integrados con bootstrap; no contradicen su decisión. | **Compatible; resolución de clasificación sigue abierta.** |
| ADR-004 — Experience / Scenario / Script / runtime | Experience gobierna significado; Scenario sitúa; Script presenta; runtime valida y posee mutación. | Scenario puede aportar catálogo, pero no se decide quién gobierna la clasificación de sus entradas. | Session 11 mantiene Definition y Scenario separados, pero asigna de facto la clasificación local al Scenario. | **Compatible con cualificación experimental.** |

### Contradicción frente a frontera no resuelta

No se observó ningún comportamiento que viole una decisión aceptada. Las cuestiones nuevas son **fronteras no resueltas**, no contradicciones:

- autoridad para decir que una actividad pertenece o no a una clase;
- completitud/alcance de esa autoridad;
- semántica de outcome cuando faltan datos, contexto o soporte;
- relación entre nombre, madurez y autoridad de `ExperienceDefinition`.

Por tanto, no se modifica ni reabre ADR-001–004.

## 3. Evaluación del concepto Authority Frontier

Definición de trabajo aceptada como término analítico de producto/arquitectura:

> Una Authority Frontier identifica el ámbito en el que un artefacto, componente o fuente está legitimado para emitir un claim, y el punto a partir del cual hace falta otra interpretación, validación o autoridad.

### Valor añadido respecto a layering

Una capa explica posición y dependencia; una Authority Frontier responde además:

- qué afirmación puede realizarse legítimamente;
- con qué procedencia, versión y alcance;
- qué información puede consumirse sin elevar su autoridad;
- cuándo la ausencia de datos no autoriza una conclusión;
- qué nuevo actor debe validar el paso siguiente.

Ejemplos:

- un provider puede afirmar “recibí una validación QR bajo este contrato”, no “esto es un TES Event”;
- Scenario puede indicar que Cooking Class existe localmente, no convertirse por ello en autoridad global sobre categorías;
- un evaluator puede afirmar “relevante bajo estos inputs y autoridad”, no “Experience progresó”;
- Activity puede mostrar un outcome, no volverlo factual o semántico;
- `tesBaseline` puede expresar relación documental, no certificar validación por sí solo.

El concepto aporta valor porque hace visible el salto de claim, no porque introduzca una nueva capa o una entidad TES.

## 4. Authority Frontier Matrix

| Artefacto / capa | Claims autoritativos | Inputs que puede confiar | Claims que puede derivar | Claims que NO debe hacer | Procedencia / versión requerida | Preguntas abiertas |
|---|---|---|---|---|---|---|
| TES corpus | Significado, relaciones e invariantes TES dentro de su versión. | Fuentes y proceso de gobernanza TES. | Evolución semántica mediante su gobernanza. | Topología de software, provider, UI o persistencia salvo declaración expresa. | Identidad/versionado del corpus y decisión de adopción. | Cómo migra cada producto entre baselines. |
| Product Interpretation | Lectura de producto subordinada y gaps explícitos. | Baseline TES identificada y fuentes trazables. | Mediaciones funcionales cualificadas. | Ontología nueva, corrección de TES o validación ejecutiva automática. | Documento, versión, status, baseline y fuentes. | Umbral y responsable de aprobación. |
| Commercial/product source material | Lo que la fuente comunica como intención, ejemplo o claim comercial. | Su propia autoría y contexto documental. | Ningún claim TES sin interpretación. | Experience semánticamente validada, Event, Progression o Result por terminología de marketing. | Título, owner, fecha, hash/version, slide/page, audiencia. | Confidencialidad, licencia y vigencia. |
| Candidate Product Experience Definition | Interpretación candidata, límites y gaps declarados. | TES + Product Interpretation + source material. | Hipótesis semánticas explícitamente provisionales. | Claim de validación completa, ejecutabilidad o estado real. | ID/versión, status, `tes_relationship`, baseline, fuentes y revisión. | Quién valida y qué evidencia cierra gaps. |
| Validated Product Experience Definition — **conceptual** | Significado de producto validado contra una baseline y alcance concreto. | Corpus/contrato semántico y proceso de validación gobernado. | Criterios semánticos dentro de lo validado. | Hechos del mundo, estado de participación, disponibilidad local o verdad UI. | ID/versión, baseline, evidencia/decisión de validación, vigencia. | Todavía no existe un artefacto aprobado de este tipo. |
| Runtime Experience descriptor/reference | Identidad y binding de una Definition que la composición puede resolver. | Registry/bootstrap y Definition referenciada. | Disponibilidad/compatibilidad efectiva de la referencia. | Significado completo o validación TES por contener `tesBaseline`. | Ref versionada/digest, Definition status y resolución. | Debe llevar baseline directamente o heredarlo de la Definition. |
| Scenario | Actores/contextos/condiciones locales y configuración situada declarada. | Definition referenciada, source/property config y manifest. | Aplicabilidad situada dentro de su configuración. | Redefinir Experience, TES o taxonomía universal; afirmar hechos observados. | ID/versión, sources de configuración y Definition ref. | Qué parte del catálogo/clasificación puede gobernar legítimamente. |
| Catálogo/clasificación de actividad — **experimental/conceptual** | Existencia y clasificación dentro de un ámbito si posee autoridad declarada. | Product/property data y fuentes clasificadoras. | Membership positiva; negativa solo si el catálogo es completo para ese dominio. | Significado TES, relevancia por Experience o exclusión fuera de su cobertura. | Source, versión, scope, completeness y reglas de clasificación. | Autoridad final, conflictos, localización y taxonomía. |
| Provider/source | Observación o estado dentro de su contrato y ámbito. | Sistema origen, autenticación y contrato de integración. | Claim factual cualificado por fiabilidad/procedencia. | Significación TES, clasificación semántica de producto o composición total por sí solo. | Provider ID, contrato/esquema, timestamp, source record/version. | Corrección, duplicados, divergencia y fuentes múltiples. |
| Neutral EvidenceInput | Contenido recibido/registrado y su procedencia declarada. | Provider/source dentro de su contrato. | Ninguno por sí mismo; puede preservar correlación y reliability. | `relevant`, `significant`, Experience membership, Progression, Result o copy de Activity. | Evidence ID, source, tiempo, esquema y referencias factuales. | Neutralidad real de APIs que entreguen datos ya interpretados. |
| Contextual relevance evaluator — **experimental** | Outcome relacional limitado a inputs, criterios y autoridad disponibles. | Evidencia, Definition/descriptor, Scenario y classification authority compatibles. | Positivo, negativo o indeterminado con rationale y scope. | TES Event, Pattern, Progression, Result, reward o verdad fuera de versión/contexto. | Evaluator/version, refs/versiones de inputs, autoridad clasificadora y reason. | Forma de outcomes, conflicto, incomplete authority y soporte. |
| `SignificantEvent` — **legacy/provisional position** | Si está previamente reconocido, podría representar un Event significativo bajo contexto declarado. | Futura frontera de reconocimiento; hoy el contrato no la explicita. | Effects solo bajo reglas y participación apropiadas, aún no gobernadas. | Servir como evidencia neutral o presuponer significación antes de evaluación. | Event/evidence refs, Experience context, recognition authority y baseline. | Posición final, rename/migration y reconocimiento. |
| Runtime state | Estado mutable operacional de una sesión/participación dentro de su dueño. | Acciones públicas validadas y sources resueltos. | Transiciones operativas permitidas. | Redefinir TES, convertir checkpoint en Progression o elevar proyección a hecho. | Runtime/session ID, version/config y action provenance. | Participación real, persistencia y multi-provider. |
| Demo Script | Orden, copy e instrucciones de demostración y referencias a acciones públicas. | Scenario y composición efectiva. | Expectativas de demo verificables. | Mutar estado, ejecutar reglas, reconocer Event o gobernar Experience. | Script/version y Scenario/action refs. | Multi-step y recuperación siguen experimentales. |
| Demo Manifest | Intención y referencias deseadas de una demo. | Artefactos versionados y requisitos de capability. | Composición deseada. | Disponibilidad efectiva, secretos, estado runtime o significado TES. | Schema + instance version/digest + refs. | Versionado de instancia pendiente. |
| Bootstrap/resolution | Compatibilidad y composición efectiva en un entorno. | Manifest, registry, deployment policy y providers disponibles. | Resuelto/rechazado/cualificado. | Redefinir semántica o conceder autoridad factual por resolver una ref. | Resolver version, manifest digest, bindings y deployment context. | Cómo incorporar classification authority. |
| AppSnapshot | Estado de lectura para la superficie actual. | Runtime/source y proyectores autorizados. | Representación consumible. | Fuente factual, semántica TES o estado canónico universal. | Snapshot schema, source refs y generated-at cuando sea necesario. | Cuánta procedencia necesita exponer. |
| Activity/read model | Presentación/editorialización downstream. | Sources, runtime y outcomes proyectables. | Título, orden, agrupación, icono, tono y resumen. | Evaluar relevancia, reconocer Event o convertirse en evidence ledger. | Projection version y refs a sources/outcomes. | Cómo resumir relaciones sin perder trazabilidad. |

## 5. Autoridad de clasificación

Session 11 asigna de facto al fixture de Scenario esta afirmación:

```text
Cooking Class → shared-hotel-activity
```

La Definition declara qué clasificaciones acepta. Esta división fue útil para falsificar branches por ID, pero no acredita al Scenario como taxonomía final ni declara si su clasificación es completa.

| Localización candidata | Adecuación semántica | Reuse/versionado | Variación local | Riesgo principal | Compatibilidad ADR-004 | Veredicto actual |
|---|---|---|---|---|---|---|
| Scenario | Bueno para disponibilidad y alias locales. Débil como taxonomía general. | Baja si duplica clases por Scenario; necesita versión propia. | Alta. | Scenario absorbe significado reusable y se vuelve autoridad semántica accidental. | Compatible solo para configuración situada. | Conveniencia experimental, no autoridad final. |
| Product Experience Definition | Adecuado para expresar qué clase de actividad puede ser relevante al núcleo. | Alta entre Scenarios; versionable con Definition. | Baja para catálogo local. | Incrustar productos/actividades concretos y mezclar semántica con disponibilidad. | Compatible si conserva núcleo y no narrativa/localidad. | Autoridad plausible sobre criterio, no sobre clasificación del observado. |
| Catálogo reusable de actividad/producto | Adecuado para identidad y clasificación de items compartidos. | Alta si schema/source/version están gobernados. | Media; necesita overlays o scopes. | Convertir una taxonomía comercial en semántica TES o asumir exhaustividad. | Compatible: Scenario puede referenciarlo. | Candidato plausible, no demostrado. |
| Provider/source | Autoridad fuerte sobre atributos que su contrato realmente entrega. | Alta dentro del sistema origen; versionado contractual. | Alta según property/source. | Provider data se interpreta como product meaning; taxonomías externas pueden no coincidir. | Compatible si se media y no redefine Experience. | Fuente factual, no autoridad semántica automática. |
| Property configuration | Fuerte para oferta/disponibilidad y clasificación operacional local. | Reuse limitado por propiedad; requiere vigencia. | Muy alta. | Variación incoherente o claims negativos fuera de scope. | Compatible como aporte de Scenario. | Buena autoridad situada cuando existe y declara cobertura. |
| Shared taxonomy | Buena para vocabulario reusable si existe gobierno. | Alta; exige versionado y mappings. | Baja sin extensiones locales. | Generalización prematura y falsa universalidad. | Compatible como artefacto referenciado, no dentro de Scenario. | No hay evidencia suficiente para crearla. |
| Clasificación externa suministrada | Depende del contrato y procedencia. | Variable. | Alta. | Confiar en labels opacas o cambiantes; autoridad ajena al producto. | Compatible si bootstrap/provider cualifican. | Debe mediarse, nunca aceptarse por presencia. |
| Autoridad compuesta | Puede combinar source factual, catálogo local y mapping de producto. | Potencialmente alta con bindings versionados. | Alta sin perder núcleo reusable. | Complejidad, conflicto y precedencia accidental. | Encaja con Definition + Scenario separados. | Hipótesis más realista, aún sin evidencia para arquitectura final. |

### Respuesta a la pregunta clave

Ningún actor actual tiene autoridad final demostrada para afirmar membership de clasificación. En Session 11, el **Scenario fixture tiene autoridad de facto y experimental**. Una solución futura probablemente componga:

- source/provider: identidad y atributos observados;
- property/catalogue: clasificación y disponibilidad dentro de un scope declarado;
- Product Experience Definition: qué clasificaciones son pertinentes;
- evaluator: relación resultante y límites de autoridad.

Esta composición es una hipótesis analítica. No se decide taxonomía, precedence ni implementación.

## 6. Semántica de relevancia open-world

El mundo es abierto cuando la ausencia de una afirmación no implica que su negación sea cierta. Por tanto:

```text
not found / not classified / missing context
                     ≠
authoritatively not relevant
```

### Situaciones conceptuales mínimas

| Situación | Condición | Claim permitido |
|---|---|---|
| Positive determination | Evidencia y contexto identificados; clasificación competente positiva; criterio de Experience compatible. | Relevante dentro de Experience/context/version declarados. |
| Negative determination | Evidencia y contexto identificados; autoridad competente y suficientemente completa excluye la clasificación/relación; evaluator soporta el caso y no hay conflicto abierto. | No relevante dentro de ese scope, con rationale. |
| Undetermined | Falta evidencia, contexto, autoridad, cobertura o resolución de conflicto para afirmar positivo o negativo. | Solo “no determinado bajo la información/autoridad disponible”. |

Otras causas futuras pueden necesitar distinción operacional sin convertirse ahora en enum:

- clasificación desconocida;
- contexto requerido ausente;
- evaluator o tipo de evidencia no soportado;
- fuentes contradictorias;
- source con fiabilidad insuficiente;
- versión no compatible o fuera de vigencia;
- política de clasificación no evaluable;
- autoridad disponible pero no exhaustiva.

### Invariant mínimo

> **Una evaluación negativa solo puede emitirse cuando existe autoridad suficiente para excluir la relación dentro de un scope y versión declarados; la ausencia o insuficiencia de conocimiento debe permanecer no determinada.**

Este invariant evita el colapso sin definir un enum final ni una state machine.

### Cualificación de Session 11

El booleano `relevant` no preserva el invariant. Aunque `reason` distingue tres fallos, todos producen `false`:

- `scenario-context-mismatch` puede ser mismatch conocido o contexto equivocado/incompleto;
- `activity-not-in-scenario` es ausencia, no exclusión, salvo catálogo exhaustivo;
- `activity-classification-not-relevant` solo es negativo si la clasificación es completa o hay exclusión explícita.

El positivo Cooking Class → Family Adventure sigue respaldado por las fuentes. El negativo Cooking Class → Active Challenge queda **cualificado por una asunción closed-world experimental no declarada en el contrato**.

## 7. Autoridad × EvaluationOutcome

La formulación más precisa es:

```text
EvaluationOutcome = f(
  Evidence,
  ExperienceContext,
  AvailableAuthority
)
```

`AvailableAuthority` no tiene por qué convertirse en un objeto universal; expresa que el claim resultante nunca puede exceder cobertura, versión y competencia de sus inputs.

| Ejemplo | Autoridad disponible | Análisis | Claim seguro |
|---|---|---|---|
| 1. Known negative: Cooking Class está autoritativamente clasificada como no sport/wellness para ese catálogo/scope | Catálogo competente, versionado y completo o exclusión explícita; Definition Active Challenge requiere sport/wellness. | Existe base para excluir la intersección. | `not relevant` para Active Challenge bajo ese contexto y versiones. No afirma nada fuera de ellos. |
| 2. Unknown activity: ID no aparece en catálogo local | Solo se sabe que no fue encontrada; no hay garantía de exhaustividad. | Puede ser nueva, alias, dato tardío, catálogo incompleto o fuera de scope. | Undetermined / unknown / unevaluable; no negativo. |
| 3. Missing property/stay context | El input existe, pero no puede cotejarse con el Scenario aplicable. | Falta situación, no evidencia de incompatibilidad. | Undetermined por contexto insuficiente. Si el input contiene valores explícitamente distintos y la autoridad confirma ambos scopes, podría ser mismatch conocido, no una regla universal. |
| 4. Conflicting classifications | Dos fuentes competentes dicen cosas distintas. | El evaluator no debe inventar precedence. Se necesita policy/autoridad de resolución o preservar conflicto. | Undetermined/conflicting bajo autoridad actual. |

La fiabilidad baja tampoco equivale a irrelevancia. Puede impedir una conclusión o cualificar confianza, pero no cambia por sí sola el significado del input.

## 8. Ambigüedad de `ExperienceDefinition`

El repositorio utiliza el mismo nombre para responsabilidades y madurez distintas. La inferencia siguiente es inválida:

```text
object named ExperienceDefinition
+ tesBaseline
= TES-validated semantic definition
```

`tesBaseline` solo es un identificador. La relación con esa baseline debe expresar si el artefacto fue **interpretado**, **validado** o está **meramente asociado**.

### Riesgo material

- El tipo rico parece completo por número de campos, pero no demuestra Pattern, Sequence, Progression, Result, Measurement o Learning ni un proceso de validación.
- El tipo mínimo parece una Definition porque se llama así, aunque solo permite identidad/nombre/baseline.
- Las candidatas documentales dicen `READY WITH EXPLICIT GAPS` y son seguras mientras se lea el status; herramientas o consumidores podrían ignorarlo.
- Bootstrap resolver una referencia puede convertir disponibilidad técnica en aparente validación semántica.

El tipo Demo Factory es el más probable para **transferir autoridad falsa en runtime**, porque se resuelve efectivamente y viaja como `runtime.experience` pese a ser solo un header. El tipo rico es el más probable para **sobreprometer completitud funcional**.

## 9. Matriz de madurez, autoridad y representación de artefactos Experience

| Artefacto | Autoridad semántica | Madurez | Rol de representación | Ejecutabilidad | Relación TES actual | Riesgo de confusión |
|---|---|---|---|---|---|---|
| Session-10 Product Experience Definitions | Hipótesis interpretativa explícita; gaps y prohibiciones. No autoridad TES. | Candidate, `READY WITH EXPLICIT GAPS`. | Definición documental candidata. | Non-executable. | `tes_baseline` significa **interpreted against**, no validated against. El campo no lo explicita estructuralmente. | Status puede perderse al citar solo ID/nombre/baseline. |
| `domain/contracts.ts::ExperienceDefinition` | Traducción funcional candidata subordinada. Sus campos no prueban completitud. | Experimental/legacy candidate; shared contract “en preparación”. | Definición funcional agregada en `DemoPackage`. | Contrato TypeScript ejecutable como forma, sin comportamiento activo; runtime actual no lo consume. | `tesBaseline` está asociado por contrato; no existe evidencia de validación de instancia. | Nombre y riqueza sugieren falsa completitud/validación. |
| `demo-factory/contracts.ts::ExperienceDefinition` | Ninguna semántica más allá de identidad nominal y baseline declarada. | Runtime-only experimental descriptor. | Reference/header resuelto. | Forma runtime consumida por bootstrap. | `tesBaseline` está meramente asociado al descriptor; la Definition gobernada no se resuelve. | Es el mayor riesgo de authority laundering operativo. |
| Validated Product Experience Definition — **conceptual** | Definición de producto validada contra TES dentro de scope/version. | No existe todavía. | Definición semántica gobernada. | Non-executable por defecto; podría ser referenciada. | `validated against` con evidencia de validación explícita. | Confundir validación semántica con disponibilidad runtime. |

### Terminología conceptual recomendada

Sin renombrar ahora, la documentación futura debería distinguir al menos:

```text
CandidateProductExperienceDefinition
ValidatedProductExperienceDefinition
RuntimeExperienceReference
RuntimeExperienceDescriptor
```

El beneficio no es estético: impide que “Definition” y `tesBaseline` actúen como credenciales implícitas.

## 10. Compatibilidad de wording de ADR-001

La frase actual dice:

> Toda `ExperienceDefinition` debe identificar la baseline TES contra la que fue validada.

### Evaluación

| Pregunta | Respuesta |
|---|---|
| ¿Debe aplicar solo a definiciones semánticamente validadas? | La parte “contra la que fue validada” sí. Candidate y descriptor no pueden afirmar esa relación. |
| ¿Puede una candidata referenciar baseline sin afirmar validación? | Sí; debe declarar `interpreted against` y status/gaps, no usar la referencia como certificado. |
| ¿Puede runtime heredar baseline indirectamente? | Conceptualmente sí, mediante una referencia versionada a la Definition validada. Copiar baseline en descriptor puede ayudar al check de compatibilidad, pero no sustituye esa referencia. |
| ¿El wording crea riesgo? | Sí cuando `ExperienceDefinition` se usa como nombre genérico para candidatos/descriptores. No altera la decisión de fondo de ADR-001. |
| ¿Puede resolverse sin reabrir ADR-001? | Sí, provisionalmente mediante terminología, metadata de `tes_relationship` y validación que distinga status. |

**Clasificación: ADR-001 requiere aclaración futura, no amendment inmediato ni reconsideración.**

La aclaración debería interpretar “ExperienceDefinition” en esa obligación como **semantically validated Product Experience Definition**. Los candidatos deben identificar qué baseline interpretan y declarar que no han sido validados; los descriptors deben referenciar el artefacto gobernado y no reclamar validación propia.

No se modifica ADR-001 en esta sesión porque no existe contradicción con su invariant central y el propio ADR ya exige clasificación, trazabilidad y separación de versiones.

## 11. Requisitos mínimos de provenance de autoridad

Sin diseñar un schema, un claim derivado necesita suficientes dimensiones para no aparentar más autoridad que sus inputs:

| Dimensión | Por qué es necesaria |
|---|---|
| Evidence/source identity | Permite localizar el hecho recibido y su contrato de origen. |
| Source authority + scope | Explica qué puede afirmar la fuente y dónde. |
| Source/schema version + observed time | Evita aplicar significado actual a un payload incompatible o fuera de vigencia. |
| Experience Definition ref/version/status | Distingue candidata de validada y fija los criterios utilizados. |
| TES relationship/baseline | Separa interpreted/validated/associated y preserva trazabilidad. |
| Scenario ref/version | Fija stay/property/configuración situada. |
| Classification authority/version/scope/completeness | Determina si membership o exclusión son claims legítimos. |
| Evaluator identity/version | Permite reproducir la derivación sin convertir algoritmo en autoridad semántica. |
| Outcome rationale | Explica qué criterio y evidencia sostienen el claim. |
| Unresolved conflict/insufficiency | Impide que missing/contradictory se proyecte como negativo. |

No todas las dimensiones deben viajar en cada DTO o pantalla. Deben permanecer reconstruibles en el nivel que sostenga el claim; Activity puede mostrar un resumen y referenciar la procedencia.

## 12. Readiness y scope propuesto de ADR-005

### Readiness

El invariant conceptual está maduro; la decisión ejecutable completa no:

- Session 11 prueba separación de evidencia, evaluación relacional y Activity.
- Session 12 demuestra que authority scope forma parte del outcome.
- Session 11 no prueba known negative frente a unknown/insufficient/conflicting.
- La clasificación de Scenario carece de autoridad/completeness formal.

**ADR-005 no está listo para creación/aceptación.** Su scope sí está listo para guiar un último experimento focalizado.

### Scope candidato

**Neutral Evidence and Authority-Bounded Contextual Evaluation**

Invariant candidato:

> La evidencia factual permanece separada de la evaluación relativa a Experience. Todo claim derivado de relevancia queda acotado al Experience context y a la autoridad disponible. La ausencia de autoridad, clasificación o contexto suficientes no se convierte silenciosamente en un claim negativo. Relevancia no reconoce por sí sola un TES Event y no pertenece a Activity.

### Lo que ADR-005 no debe decidir

- enum final de relevance/evaluation;
- taxonomía de actividades/productos;
- implementación o topología de classification authority;
- precedence de fuentes en conflicto;
- Event recognition;
- migración/rename de `SignificantEvent` o `ExperienceDefinition`;
- persistencia, event sourcing o audit framework;
- rules/Experience engine;
- participación individual/colectiva;
- Pattern, Sequence, Progression, Result, Measurement o Learning;
- provider/API topology;
- UI de explicación o Activity.

## 13. Implicaciones de Architecture v0.5 candidata

Architecture v0.4 no cambia todavía. Como anotación candidata para análisis:

```text
┌─────────────────────────────────────────────────────┐
│ Source / Evidence Authority              PROVISIONAL│
│ Claims factuales dentro de contrato/scope/version   │
└─────────────────────────┬───────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ Neutral factual evidence                 SUPPORTED  │
└─────────────────────────┬───────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ Experience Definition + Scenario                    │
│ + classification authority              PROVISIONAL│
└─────────────────────────┬───────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ Authority-bounded contextual evaluation PROVISIONAL│
│ positive / negative / undetermined distinction     │
└─────────────────────────┬───────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ Future recognition boundary              UNRESOLVED │
└─────────────────────────┬───────────────────────────┘
                          ▼
┌─────────────────────────────────────────────────────┐
│ Runtime / projections as applicable                 │
│ Existing v0.4 authorities survive                   │
└─────────────────────────────────────────────────────┘
```

No se publica Architecture v0.5: el diagrama añade una hipótesis y una frontera sin evidencia open-world ejecutable. Tras el siguiente experimento podrá decidirse si es arquitectura aceptada o solo una anotación de governance.

## 14. Preparación del experimento Treasure Hunt

**Treasure Hunt sigue reservado y no se implementa.** Su futuro valor aumenta porque debe falsificar cuatro simplificaciones de Cooking Class: evidencia atómica, sujeto individual, outcome binario y una sola fuente clasificadora.

### Claims y autoridades que deberá tensionar

| Claim futuro | Autoridad candidata a investigar | Riesgo |
|---|---|---|
| Clue observado | Source/device/staff dentro de su contrato. | Confundir observación con solución. |
| Clue resuelto | Criterio de reto + evidence sufficiency authority. | Convertir una marca del staff en verdad semántica total. |
| Contribución pertenece a participante | Identity/participation binding situado. | Atribución incorrecta o identidad compartida. |
| Contribuciones pertenecen a un grupo | Group/Scenario/participation authority aún no definida. | Agregar por proximidad o booking sin legitimidad. |
| Solución parcial es válida | Reglas de suficiencia gobernadas, no Activity. | Confundir ausencia de pistas con fallo. |
| Hunt completa está resuelta | Composición de evidencias + criterio validado. | Inferir Completion/Result TES desde un contador. |

### Semántica open-world a preservar

El diseño futuro deberá distinguir, sin fijar aún vocabulario final:

- clue observada frente a no observada;
- clue no resuelta frente a resolución desconocida;
- evidencia insuficiente frente a solución falsa;
- contribución no atribuida frente a no perteneciente al grupo;
- fuentes contradictorias frente a resultado negativo;
- conjunto parcial conocido frente a universo completo de pistas;
- orden requerido, orden desconocido y pistas explícitamente no ordenadas.

Preguntas aún abiertas: múltiples participantes; sujeto individual/grupal; evidencia parcial; agregación; cooperación; resolución parcial; pistas ordenadas/no ordenadas; conflicto/ausencia; suficiencia; reconstrucción de outcome grupal. Ninguna autoriza TES Progression o Completion.

## 15. Riesgos restantes

- El booleano actual puede consumirse ignorando su reason code.
- La etiqueta ausente se trata de facto como clasificación negativa.
- Scenario posee clasificación sin source, versión, scope ni completeness.
- `ActivityClassification` parece taxonomy aunque solo tiene dos strings experimentales.
- No existe representación de conflicto o unsupported evaluation.
- `reliability` está presente pero no participa en el claim.
- Candidate Definitions se referencian desde tests como si fueran consumibles, sin resolver su status documental.
- `tes_baseline` no expresa el tipo de relación con TES.
- Dos interfaces TypeScript comparten `ExperienceDefinition` y una viaja en runtime.
- Bootstrap no valida status/madurez de la Definition.
- Un catálogo externo o API puede usar taxonomías, scopes y completitud incompatibles.
- La negativa puede variar con actualización de catálogo sin cambiar la evidencia.
- No hay policy para conflicto entre property, provider y shared catalogue.
- Activity futura podría omitir que un outcome fue undetermined o provisional.
- Treasure Hunt requerirá autoridades de identidad, grupo y suficiencia aún inexistentes.
- No hay evidencia de performance, persistencia o temporalidad, aunque tampoco son necesarias para el invariant actual.

## 16. Siguiente paso recomendado

**Option B — realizar un experimento focalizado adicional antes de ADR-005 porque authority/open-world sigue infraevidenciado.**

El experimento mínimo debe reutilizar Cooking Class y el evaluator sin construir engine. Debe contrastar únicamente:

1. **positivo conocido:** clasificación autoritativa compatible;
2. **negativo conocido:** exclusión explícita o catálogo declarado completo dentro de scope;
3. **indeterminado:** actividad ausente, contexto insuficiente, clasificación no autoritativa o conflicto.

Debe comprobar que cambiar completeness/authority sin cambiar Evidence puede cambiar el tipo de claim permitido, y que ningún caso indeterminado se proyecta como negativo. No debe definir taxonomy final, enum universal ni resolver conflictos.

Option A es prematura porque el invariant open-world carece de evidencia ejecutable. Option C no procede porque no existe contradicción. Option D es prematura: Treasure Hunt multiplicaría actores y agregación antes de corregir la semántica binaria básica.

## Revisión adversarial final

1. **¿Authority Frontier añade más que layering?** Sí: limita claims, explicita provenance/scope y señala cuándo una nueva autoridad es obligatoria.
2. **¿Qué artefacto puede sobredimensionar más su autoridad?** El `ExperienceDefinition` mínimo del runtime; su nombre y `tesBaseline` acompañan una resolución efectiva pese a ser solo descriptor.
3. **¿Quién clasifica de facto en Session 11?** El fixture de Scenario mediante `activityCatalogue.classifications`.
4. **¿Es legítimo?** Es legítimo como conveniencia de experimento situada, no como autoridad final ni negativa open-world.
5. **¿Cuándo puede afirmarse `not relevant`?** Con input/contexto suficientes y una autoridad competente, vigente y exhaustiva o explícitamente excluyente, sin conflicto abierto.
6. **¿Qué colapsa hoy en `false`?** Mismatch, actividad ausente, clasificación no intersectada, y potencialmente unknown/incomplete authority.
7. **¿Puede haber negativo sin classification authority?** No; solo un resultado indeterminado o no evaluable.
8. **¿`tesBaseline` significa lo mismo siempre?** No: puede ser interpreted against, validated against o merely associated.
9. **¿`ExperienceDefinition` transfiere autoridad falsa?** Sí, materialmente, si el consumidor ignora status/rol.
10. **¿Puede resolverse sin cambiar ADR-001?** Sí, primero mediante terminología, `tes_relationship`, refs gobernadas y validación de status. Una aclaración futura puede estrechar el wording.
11. **¿Cuál es la provenance mínima?** Evidence/source; Definition ref/version/status/TES relationship; Scenario; classification authority/scope/completeness; evaluator version; rationale/conflict.
12. **¿ADR-005 está maduro?** Su scope e invariant sí; su aceptación no, por falta de test open-world.
13. **¿Qué falsifica Treasure Hunt que Cooking Class no?** Evidencia distribuida/parcial, sujetos individuales y grupales, agregación, suficiencia, conflicto y resolución cooperativa.
14. **¿Se diseñó una ontología de relevance?** No. Se identificó un invariant sobre autoridad y desconocimiento; no se definió enum, state machine ni taxonomía final.
