---
title: "Session 14 — Consolidation and Architectural Promotion Decision"
aliases:
- "Consolidación y decisión de promoción arquitectónica"
language: es
version: "v1.0"
status: "consolidado"
date: "2026-09-04"
project: "Convercus App"
document_type: "informe de consolidación y promoción"
scope: "evaluación adversarial de Sessions 11–13, decisión sobre ADR-005 y Architecture v0.5"
repository_role: "registro de evidencia, límites de promoción y estado epistemológico posterior"
semantic_authority: "análisis de producto y arquitectura subordinado; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 14 — Consolidation and Architectural Promotion Decision

## 1. Executive conclusion

```text
ADR-005 → ACCEPT
Architecture v0.5 → PUBLISH
Treasure Hunt readiness → READY FOR A BOUNDED NEXT EXPERIMENT
```

La promoción recae únicamente sobre el invariante que sobrevivió a Sessions 11–13: evidencia factual y evaluación contextual son responsabilidades distintas; una conclusión derivada no puede superar conjuntamente la autoridad, scope y madurez de sus premisas; falta de conocimiento no equivale a exclusión; relevancia contextual no reconoce por sí misma un Evento TES; Activity no origina ni fortalece el claim.

Se acepta [ADR-005](../../../00-governance/decisions/ADR-005-neutral-evidence-authority-bounded-contextual-evaluation.md) con esa frontera mínima. No se promueven los tipos, enums, reason codes, fixtures ni shapes usados por Session 13.

La decisión sobre [Architecture v0.5](../../../00-governance/program-architecture.md) es independiente. Se publica porque añade comprensión real frente a v0.4: representa por separado el flujo de composición y el flujo factual/contextual que converge en evaluación, preservando ADR-003 y ADR-004 y sin crear un `Authority Service` ni una capa clasificatoria normativa.

Treasure Hunt queda listo como siguiente experimento acotado. Esta sesión no lo diseña y no valida anticipadamente semánticas de grupo, pistas, agregación, suficiencia o resolución parcial.

## 2. Evidence chain

```text
Session 11
  separación ejecutable Evidence / Experience-relative evaluation / Activity
  + limitación: relevant/not_relevant bajo supuesto closed-world
        ↓
Session 12
  análisis de Authority Frontier
  + absence of knowledge != negative claim
  + limitación: evidencia ejecutable insuficiente para ADR
        ↓
Session 13
  mismo Evidence + mismo ExperienceContext
  + autoridad clasificatoria/suficiencia diferente
  → distinto tipo de claim legítimo
  + limitación: solo se manipula directamente la dimensión clasificatoria
        ↓
Session 14
  inspección independiente + test focalizado + evaluación adversarial
  → promoción del invariante mínimo, no del mecanismo
```

### Repository/document inspection

Se revisaron ADR-001–004, las Product Experience Definitions candidatas de Session 10, los informes de Sessions 11–13, `evidence-relevance.ts`, sus tests y los contratos relacionados con Evidence, ExperienceContext, Scenario, Activity, AppSnapshot y las dos formas actuales de `ExperienceDefinition`.

La topología encontrada coincide con Session 13:

- Evidence es un input factual neutral y no contiene `experienceRef`, interpretación ni relevancia.
- ExperienceContext aporta criterios de la definición candidata y contexto situado del Scenario.
- La autoridad clasificatoria es un tercer input local del experimento.
- El evaluator es puro, no contiene branches por los IDs de Family Adventure o Active Challenge y no depende de Activity.
- Activity se mantiene como read model derivado desde registros fuente mediante `projectSnapshot()` y no consume el evaluator en producción.
- `domain/contracts.ts::ExperienceDefinition` sigue siendo un contrato funcional rico y provisional.
- `demo-factory/contracts.ts::ExperienceDefinition` sigue siendo un descriptor mínimo de identidad/binding runtime.
- Las definiciones comerciales siguen marcadas `READY WITH EXPLICIT GAPS — non-executable candidate` e interpretadas contra TES.
- No existe consumer externo del evaluator que convierta su unión experimental en API pública.

La verificación ejecutable focalizada del 4 de septiembre de 2026 obtuvo:

```text
Test Files  1 passed (1)
Tests      12 passed (12)
```

No se encontró divergencia material entre código, tests e informe. No se modificó código productivo ni se repitió la suite completa, conforme al alcance documental de esta sesión.

### Session 11–13 compatibility

| Sesión | Claim conservado | Cualificación conservada | Compatibilidad |
|---|---|---|---|
| 11 | Evidence neutral, evaluación relativa y Activity son separables; no hacen falta branches por Experience ID. | El booleano closed-world no se promueve. | Compatible y absorbida por el invariante mínimo. |
| 12 | `Authority Frontier` permite analizar capacidad de claim, scope y procedencia; unknown no equivale a negative. | Es concepto analítico no-TES y entonces no tenía evidencia suficiente para ADR. | Compatible; Session 13 aporta la falsificación que faltaba para una dimensión. |
| 13 | La autoridad clasificatoria disponible limita el claim; ausencia, out-of-scope y conflicto pueden quedar sin resolver. | No prueba todas las Authority Frontiers ni una topología final. | Compatible; la cualificación se incorpora en ADR-005. |

## 3. Claims promoted

Se promueven exactamente estos invariants:

1. **Neutral evidence:** la evidencia factual permanece separada de la evaluación relativa a Experience.
2. **Open-world distinction:** insuficiencia de conocimiento, contexto o autoridad no equivale a conclusión negativa.
3. **Bounded exclusion:** una conclusión negativa requiere base suficiente para excluir la relación dentro del scope evaluado.
4. **Derived-claim non-escalation:** un claim derivado no puede superar conjuntamente autoridad, scope y madurez de sus premisas.
5. **TES Event separation:** relevancia contextual no equivale por sí misma a reconocimiento de Evento TES.
6. **Activity separation:** Activity/read models no originan ni fortalecen la autoridad de la evaluación que muestran.

El cuarto punto combina evidencia directa de la frontera clasificatoria con inferencia arquitectónica respaldada por ADR-001–004. No se afirma que Sessions 11–13 hayan ensayado simétricamente todas las premisas.

## 4. Experimental mechanisms NOT promoted

Permanecen experimentales o locales, no normativos:

- los literales `positive`, `negative` y `undetermined`;
- todos los reason codes de Session 13;
- `ActivityClassificationAuthority`;
- `authorityRef`;
- `coverage = incomplete | exhaustive`;
- el shape actual de `scope`, `propertyRef` y `catalogueVersion`;
- `claims`, `includes` y `excludes` como representación definitiva;
- la taxonomía fixture `shared-hotel-activity | sport-wellness`;
- las signatures y shapes de `evaluateEvidenceRelevance`;
- la ubicación del catálogo en Scenario;
- cualquier provider, registry, aggregate o service de autoridad;
- persistencia, audit log, event sourcing, accreditation, confianza y precedencia;
- integración productiva con Activity o UI.

La evidencia promueve la diferencia epistemológica, no el vocabulario que la representa.

## 5. Authority Frontier consolidation

`Authority Frontier` se consolida como instrumento analítico de producto/arquitectura, no como concepto TES ni como obligación de crear componentes.

| Frontera | Puede aportar | No puede afirmar por sí sola | Estado |
|---|---|---|---|
| Factual authority | Ocurrencia, identidad, procedencia y cualificación factual dentro de su competencia. | Relevancia para una Experience o reconocimiento TES. | Principio aceptado; fuentes concretas provisionales. |
| Experience interpretation authority | Criterios semánticos con baseline, procedencia y madurez declaradas. | Validación TES si el artefacto solo es candidato. | Frontera aceptada; candidatos actuales provisionales. |
| Situated context authority | Pertenencia a estancia, propiedad, catálogo o situación dentro del scope declarado. | Taxonomía universal o verdad factual fuera de scope. | Separación aceptada; shape provisional. |
| Classification/mapping authority | Inclusión, exclusión o equivalencia dentro de competencia y scope suficientes. | Semántica de Experience, hechos de ocurrencia o precedencia automática. | Classification soportada con cualificación; mapping unresolved. |
| Evaluation transformation | Derivar un claim reproducible desde premisas explícitas. | Crear autoridad o reparar una premisa débil. | Boundary aceptada; implementación provisional. |
| Runtime | Validar y ejecutar comportamiento operacional permitido. | Aumentar certeza semántica o factual. | Aceptado por ADR-002–004. |
| Projection | Hacer consumible un resultado en AppSnapshot, Activity o UI. | Originar, excluir o fortalecer el claim. | Aceptado como read-model boundary; integración concreta provisional. |

No se crea un artefacto por cada fila ni se introduce una autoridad soberana común.

## 6. ADR-001 tension

La tensión se clasifica como:

```text
C. requiere aclaración futura
+
D. permanece correctamente como open issue
```

No contradice ADR-001 ni requiere amendment inmediato. ADR-001 ya distingue baseline TES, derivación semántica y producto. El riesgo está en que `ExperienceDefinition` junto con `tesBaseline` pueda leerse como certificado de validación cuando hoy conviven tres papeles:

```text
Candidate Product Experience Definition
→ interpreted against TES

Validated Product Experience Definition
→ validated against TES

Runtime Experience Descriptor / Reference
→ identity and binding
```

Las Product Experience Definitions de Session 10 pertenecen al primer caso. La forma rica de dominio y el descriptor mínimo de Demo Factory no resuelven por naming la madurez semántica. Session 14 no renombra ni migra tipos; registra que baseline, interpretación y validación son dimensiones diferentes.

```text
classification certainty
!=
semantic validation of Experience
```

Una clasificación fuerte no repara una definición candidata. Esta desigualdad refuerza ADR-001 en lugar de reabrirlo.

## 7. Activity frontier

Queda respaldado que Activity no necesita participar en evaluation y puede permanecer downstream. ADR-002 ya la define como read model/projection; el evaluator de Session 13 no la importa ni recibe.

Se promueve únicamente:

> Activity y otros read models no pueden originar ni fortalecer la autoridad de un evaluation claim.

No está demostrado que todas las futuras proyecciones productivas preserven correctamente cada cualificación epistémica. No se decide copy, etiquetas, iconos, confidence, presentación de conflicto ni UX de resultados no resueltos. Esa integración sigue provisional/unresolved.

## 8. Classification authority

### Demostrado

- Con Evidence y ExperienceContext constantes, cambiar las afirmaciones clasificatorias disponibles puede cambiar legítimamente el claim.
- Membership explícita y competente puede sostener un positivo.
- Exclusión explícita dentro de scope puede sostener un negativo.
- Ausencia bajo conocimiento insuficiente no sostiene un negativo.
- Ausencia puede contribuir a excluir solo cuando la autoridad es suficiente dentro del scope.
- Authority missing, fuera de scope o conflictiva sin precedencia mantiene el caso no resuelto.

### Abierto

- quién posee o acredita esa autoridad;
- cómo se expresa competencia y scope en APIs reales;
- cómo se demuestra suficiencia para excluir;
- si exhaustividad es binaria, parcial, temporal o multidimensional;
- cómo se componen fuentes;
- precedencia, confianza y conflicto;
- provider, registry, persistence y versionado operacional.

`coverage = incomplete | exhaustive` fue un mecanismo de falsificación. ADR-005 conserva la regla «base suficiente para excluir dentro del scope», no el enum.

## 9. Taxonomy alignment

```text
taxonomy alignment / semantic mapping authority → UNRESOLVED
```

Session 13 usa deliberadamente el mismo vocabulario en criterio de Experience y fuente clasificatoria. No prueba traducción entre taxonomías. Una futura relación como `culinary_experience → shared-hotel-activity` necesitaría su propia procedencia, scope, madurez y autoridad de mapping. No se crea shared taxonomy ni se decide mapping alguno.

## 10. Event recognition boundary

```text
EvidenceInput
        ↓
Contextual evaluation
        ↓
Runtime / read-model use when applicable

Possible future relation:

[inputs and authority not yet established]
        - - ? - ->
[TES Event recognition boundary — UNRESOLVED]
```

El esquema es orientativo, no una especificación. Ni evidencia relevante ni evaluación positiva reconocen automáticamente un Evento TES, y el uso en runtime o read models no atraviesa esa frontera por defecto. No se define la frontera, sus inputs, su autoridad, sus contratos ni una migración de `SignificantEvent`.

## 11. ADR-005 decision

### Evaluación cláusula por cláusula

| Cláusula candidata | Tipo de soporte | Evaluación | Resultado |
|---|---|---|---|
| Evidence factual permanece separada de evaluación relativa a Experience. | Directo: Session 11 y estructura/tests vigentes. | Sobrevive a dos Experiences, renaming y ausencia de Activity. | **Promover.** |
| Todo claim derivado queda limitado por autoridad, scope y madurez de sus premisas. | Directo para clasificación; inferencia convergente para otras premisas desde ADR-001–004 y madurez candidata declarada. | Válida si no presenta todas las fronteras como igualmente ensayadas ni prescribe shapes. | **Promover con cualificación explícita.** |
| Falta de información, clasificación, contexto o autoridad no se convierte silenciosamente en negativo. | Directo para casos de contexto y autoridad en Session 13; consistente con Session 12. | El vocabulario de outcome no es necesario para sostenerlo. | **Promover.** |
| Negativo requiere base suficiente para excluir dentro del scope. | Directo mediante explicit exclusion y ausencia bajo cobertura suficiente frente a conocimiento incompleto. | Puede formularse sin `coverage: exhaustive`. | **Promover.** |
| Relevancia contextual no reconoce por sí misma un Evento TES. | Evidencia negativa de dependencias + límites normativos de ADR-001 y guardrails de Sessions 11–13. | No define recognition boundary. | **Promover como separación, no como modelo de reconocimiento.** |
| Relevancia no pertenece a Activity. | Directo para ausencia de dependencia; ADR-002 para autoridad de projection. | La integración futura no está demostrada. | **Promover solo que Activity no origina/fortalece autoridad.** |

### Checklist adversarial ADR-005

| # | Pregunta | Respuesta |
|---:|---|---|
| 1 | ¿Evidencia ejecutable de separación Evidence/evaluation? | **Sí**, Session 11 preservada en Session 13. |
| 2 | ¿Evidencia ejecutable de unknown ≠ negative? | **Sí**, missing, incomplete, out-of-scope y conflict. |
| 3 | ¿Negativo por ausencia exige autoridad suficiente? | **Sí**, contraste incomplete/exhaustive experimental. |
| 4 | ¿Formulable sin fijar `coverage = exhaustive`? | **Sí**, como suficiencia para excluir dentro de scope. |
| 5 | ¿Sin congelar outcomes? | **Sí**, como diferencia entre exclusión e insuficiencia. |
| 6 | ¿Sin autoridad clasificatoria final? | **Sí**, no se prescribe topología ni contrato. |
| 7 | ¿Sin hacer Scenario taxonomy authority? | **Sí**, Scenario solo aporta contexto situado. |
| 8 | ¿Sin elevar una definición candidata? | **Sí**, la limitación de madurez es explícita. |
| 9 | ¿Sin Event recognition? | **Sí**, queda separado y unresolved. |
| 10 | ¿Sin convertir Activity en evaluator? | **Sí**, permanece downstream. |
| 11 | ¿Compatible con ADR-001? | **Sí**, aplica no escalado de autoridad. |
| 12 | ¿Compatible con ADR-002? | **Sí**, preserva runtime/read-model separation. |
| 13 | ¿Compatible con ADR-003? | **Sí**, no altera desired/effective composition. |
| 14 | ¿Compatible con ADR-004? | **Sí**, no altera Definition/Scenario/Script/runtime. |
| 15 | ¿Reconsiderable con API real? | **Sí**, el ADR incluye condiciones expresas. |
| 16 | ¿Distingue invariant de mecanismo? | **Sí**, enums, DTOs, scopes y fixtures están prohibidos como norma. |

### Verdict

```text
ADR-005 → ACCEPT
```

Se crea el ADR real. La calificación `SUPPORTED WITH QUALIFICATION` de Session 13 no se borra: explica por qué el ADR generaliza solo el principio de no escalado y deja las realizaciones concretas abiertas.

## 12. Architecture v0.5 decision

La evaluación se realizó después y de forma independiente a ADR-005. Publicar v0.5 solo es legítimo si el diagrama añade la distinción entre composición y evaluación sin cosificar los fixtures.

### Checklist adversarial Architecture v0.5

| # | Criterio | Resultado |
|---:|---|---|
| 1 | Expresa autoridad sin inventar Authority Service. | **Sí**; habla de premisas/fuentes, no de una capa. |
| 2 | Distingue Evidence flow de composition flow. | **Sí**; son dos diagramas que convergen solo cuando corresponde. |
| 3 | Preserva Experience → Scenario → Demo Script. | **Sí**; mantiene roles y frontera pública de ADR-004. |
| 4 | Preserva Desired ≠ Effective Composition. | **Sí**; mantiene bootstrap/capability resolution de ADR-003. |
| 5 | Preserva Activity downstream. | **Sí**; solo aparece como projection/read model. |
| 6 | Event recognition queda unresolved. | **Sí**, fuera de la evaluación aceptada. |
| 7 | Taxonomy no aparece decidida. | **Sí**, se lista como unresolved. |
| 8 | `AvailableAuthority` no es aggregate nuevo. | **Sí**, el término no se modela como componente. |
| 9 | Distingue accepted/provisional/unresolved. | **Sí**, en secciones separadas. |
| 10 | Añade comprensión real frente a v0.4. | **Sí**; evita que Evidence parezca parte lineal del manifest/bootstrap y muestra dónde converge. |

### Verdict

```text
Architecture v0.5 → PUBLISH
```

Se actualiza exclusivamente el artefacto rector `00-governance/program-architecture.md`, de v0.1 documental a baseline v0.5 consolidada. Los diagramas históricos v0.3/v0.4 permanecen en sus informes como evidencia; no se reescriben ADR-001–004 ni documentos de sesiones anteriores.

La arquitectura publicada declara:

- **ACCEPTED:** fronteras promovidas por ADR-001–005;
- **PROVISIONAL:** contracts, shapes, composición de fuentes e integración concreta;
- **UNRESOLVED:** topología, taxonomía, mappings, acreditación, precedencia, Event recognition, naming/madurez de `ExperienceDefinition` y Activity UX.

## 13. Remaining risks

| Riesgo | Por qué permanece | Tratamiento actual |
|---|---|---|
| Authority laundering por `tesBaseline` | Puede confundirse trazabilidad con validación. | Madurez candidata explícita; naming futuro abierto. |
| Sobre-generalizar classification authority | Solo esa frontera fue manipulada directamente. | ADR distingue evidencia directa e inferencia de no escalado. |
| Falso negativo con APIs reales | Scope, completitud y staleness pueden diferir del fixture. | Negativo exige base suficiente; reconsideración con API real. |
| Taxonomías incompatibles | No hubo mapping entre vocabularios. | Unresolved; ningún mapping implícito. |
| Conflicto entre fuentes | No existe precedence legítima probada. | Conservar no resolución; policy futura separada. |
| Event recognition accidental | Una evaluación positiva podría etiquetarse como Evento. | Separación normativa; recognition boundary unresolved. |
| Pérdida de cualificación en UI | No existe projector productivo EvaluationOutcome → Activity. | Activity no fortalece autoridad; UX futura debe probarse. |
| Reificación del diagrama | Fuentes conceptuales podrían leerse como servicios. | Estados explícitos y prohibición de Authority Layer/Service. |

## 14. Treasure Hunt readiness

```text
Treasure Hunt → READY FOR A BOUNDED NEXT EXPERIMENT
```

No queda una frontera previa más pequeña que bloquee legítimamente comenzar su falsificación: la separación de evidencia, evaluación, runtime y projection ya está gobernada; unknown no debe degradarse a negative; y las limitaciones de autoridad están explícitas.

`READY` no significa que Treasure Hunt esté semántica o técnicamente validado. Su siguiente sesión debe comenzar por hipótesis y falsificadores, y detenerse si necesita inventar autoridad TES o taxonómica. Esta evaluación no decide participant groups, clues, group evidence, aggregation, sufficiency ni partial resolution, y no crea ningún schema.

## 15. Final project state

### Estado epistemológico

| Estado | Elementos después de Session 14 |
|---|---|
| **ACCEPTED** | ADR-001 autoridad TES acotada; ADR-002 composition/runtime/read-model separation; ADR-003 desired/effective composition; ADR-004 Definition/Scenario/Script/runtime; ADR-005 neutral evidence y evaluación acotada por premisas; Architecture v0.5 como representación de esas fronteras. |
| **SUPPORTED** | Evaluación contextual sin branches por Experience ID; cambio de claim al variar autoridad clasificatoria; negativos por exclusión explícita o base scoped suficiente; pureza y determinismo del evaluator; Activity puede permanecer downstream. |
| **PROVISIONAL** | Product Experience Definitions candidatas; ambas formas actuales de `ExperienceDefinition`; shapes de Evidence, ExperienceContext, Scenario, classification authority y outcomes; integración runtime/projection; representación de madurez. |
| **UNRESOLVED** | Taxonomy alignment; mapping authority; acreditación, suficiencia y exhaustividad; precedencia/conflicto; topología de fuentes; Event recognition; naming/madurez de `ExperienceDefinition`; Activity UX para claims no resueltos; contratos API reales. |
| **REJECTED / NOT PROMOTED** | Semántica binaria closed-world de Session 11; enums y reason codes como ontología; `coverage` como regla arquitectónica; Scenario como taxonomy authority; Classification Authority Layer/Service; elevación de candidatos a TES-validados; Activity como evaluator/evidence ledger; equivalencia relevance = TES Event. |

### Final adversarial check

| Pregunta | Conclusión |
|---|---|
| ¿Se promovió un invariante o la última implementación? | El invariante; todos los shapes concretos quedan fuera del ADR. |
| ¿Classification authority se convirtió en capa soberana? | No; es una premisa posible y su topología sigue unresolved. |
| ¿La clasificación fuerte elevó la definición candidata? | No; el claim conserva la madurez de su premisa más limitada. |
| ¿El enum experimental se convirtió en ontología? | No; solo se exige distinguir insuficiencia de exclusión. |
| ¿Activity adquirió autoridad por ser visible? | No; permanece downstream y no puede fortalecer claims. |
| ¿v0.5 añadió poder explicativo? | Sí; separa el flujo de composición del flujo factual/contextual convergente. |
| ¿La decisión sobrevive a otra API y taxonomía? | Sí; exige límites y suficiencia, no nombres ni shapes actuales. |

### Archivos y cambios de alcance

Creado:

- `00-governance/decisions/ADR-005-neutral-evidence-authority-bounded-contextual-evaluation.md`.
- `products/convercus-app/docs/session-14-consolidation-architectural-promotion-decision.md`.

Modificado:

- `00-governance/program-architecture.md`, promovido a v0.5 con dos flujos convergentes y estados epistemológicos separados.

Eliminado: ninguno.

Código productivo modificado: ninguno.

### Recommended next session

**Session 15 — Treasure Hunt: hypothesis and minimum reversible experiment.**

La sesión debe establecer primero una hipótesis mínima falsable y sus límites semánticos, sin heredar como resueltos group evidence, aggregation, sufficiency o partial resolution. Si el primer caso requiere cualquiera de esas semánticas, deberá tratarlas como objeto explícito de falsificación, no como infraestructura asumida.
