# Session 13 — Authority-Bounded Open-World Evaluation Experiment

Trabaja sobre el repositorio existente:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

No empieces desde cero.

No rediseñes la arquitectura.

No conviertas esta sesión en una implementación de plataforma.

La arquitectura vigente está definida por ADR-001, ADR-002, ADR-003 y ADR-004. Session 12 ya está consolidada y NO debe repetirse.

ADR-005 todavía NO existe como decisión aceptada y NO debe crearse durante esta sesión.

Architecture v0.5 NO debe publicarse durante esta sesión.

Treasure Hunt / Búsqueda del Tesoro permanece reservado para un experimento posterior.

El método obligatorio es:

```text
hypothesis
→ falsification
→ reversible experiment
→ evidence
→ evaluation
```

Un resultado:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NO-GO
STOP
```

es legítimo.

Nunca introduzcas semántica, tipos, taxonomías, engines o arquitectura únicamente para obtener tests verdes.

---

# 1. Objetivo de Session 13

Session 11 demostró, con cualificación:

```text
neutral factual evidence
        ≠
Experience-relative relevance
        ≠
Activity projection
```

Session 12 identificó una limitación material del experimento:

```text
relevant / not_relevant
```

no es una semántica promovible en un mundo abierto porque:

```text
absence of knowledge
≠
negative claim
```

Session 13 debe producir evidencia ejecutable mínima sobre una cuestión más precisa:

> ¿Puede cambiar el tipo de claim legítimo al cambiar la autoridad disponible, manteniendo constantes la Evidence y el ExperienceContext?

La sesión debe investigar únicamente la diferencia entre:

```text
known positive
known negative
undetermined
```

sin convertir esos términos en una ontología universal ni en un enum arquitectónico definitivo.

---

# 2. Hipótesis experimental

## H13 — Authority-bounded evaluation

> Para Evidence y ExperienceContext constantes, el tipo de claim que puede emitir una evaluación contextual está limitado por la competencia, scope y cobertura de la autoridad disponible. La ausencia de autoridad suficiente no autoriza un claim negativo.

Formulación analítica provisional:

```text
EvaluationOutcome =
f(
    Evidence,
    ExperienceContext,
    AvailableAuthority
)
```

`AvailableAuthority` es una variable experimental/conceptual.

NO debes asumir que necesita convertirse en:

* objeto universal;
* service;
* registry;
* provider;
* interface arquitectónica;
* catálogo global;
* authority engine.

La forma exacta deberá ser únicamente la mínima necesaria para falsificar la hipótesis.

---

# 3. Subhipótesis a intentar falsificar

## H13a — Positive authority

Una clasificación positiva explícita emitida por una autoridad competente puede sostener un positive determination dentro de su scope.

## H13b — Explicit negative authority

Una exclusión explícita emitida por una autoridad competente puede sostener un negative determination dentro de su scope.

## H13c — Incomplete knowledge

La ausencia de una clasificación en una fuente o catálogo que NO declara cobertura exhaustiva no puede sostener un negative determination.

Debe permanecer:

```text
undetermined
```

o equivalente experimental.

## H13d — Scoped exhaustive coverage

La ausencia de una clasificación puede sostener un negative determination únicamente cuando una autoridad competente declara cobertura suficientemente exhaustiva para el scope/version evaluados.

## H13e — Missing authority

La ausencia de classification authority competente debe permanecer indeterminada.

## H13f — Conflicting authority

Claims competentes en conflicto, sin una policy de precedence ya demostrada, deben permanecer indeterminados/conflicting.

El evaluator NO debe inventar precedence.

## H13g — Evaluator non-authority

El evaluator puede derivar un claim relacional a partir de inputs y autoridad disponible.

NO puede convertirse él mismo en fuente de:

* clasificación;
* semántica TES;
* factual truth;
* Experience validation;
* Event recognition.

## H13h — Activity non-escalation

Activity puede proyectar downstream un EvaluationOutcome, pero no puede:

* originarlo;
* reforzar su autoridad;
* reinterpretarlo;
* convertir `undetermined` en `negative`;
* eliminar qualifiers de conflicto o insuficiencia;
* convertir relevance en TES Event, Progression, Result o Completion.

---

# 4. Inspección obligatoria antes de modificar código

Antes de implementar nada, inspecciona el repositorio real.

Localiza como mínimo:

* el evaluator introducido en Session 11, probablemente `evaluateEvidenceRelevance`;
* sus tipos de Evidence;
* sus tipos/contextos de Experience;
* los fixtures de Cooking Class;
* Family Adventure;
* Active Challenge;
* Scenario utilizado en Session 11;
* `activityCatalogue`;
* `ActivityClassification` o forma equivalente;
* tests actuales del evaluator;
* cualquier consumidor runtime del evaluator;
* cualquier consumidor UI/read model;
* Activity;
* AppSnapshot;
* `domain/contracts.ts::ExperienceDefinition`;
* `demo-factory/contracts.ts::ExperienceDefinition`;
* cualquier campo `tesBaseline`;
* documentación de Session 11;
* documentación de Session 12;
* ADR-001–004.

Primero informa brevemente de la topología real encontrada.

No adaptes silenciosamente la arquitectura a esta instrucción.

Si encuentras una contradicción material entre el repositorio y el baseline descrito aquí:

```text
STOP
```

y documenta la contradicción.

Una diferencia de naming o localización de archivo no es por sí misma contradicción material.

---

# 5. Baseline arquitectónico que debes preservar

Arquitectura aceptada aproximada v0.4:

```text
TES semantic authority
        ↓
Product contracts / interpretations
        ↓
Experience Definition
        ↓
Scenario
        ↓
Demo Manifest / desired composition
        ↓
Bootstrap / effective composition
        ↓
Runtime
        ↓
Read Models / UI
```

Separación Experience / Scenario / Demo Script:

```text
Experience Definition
        ↑ instantiated/referenced by
Scenario
        ↑ demonstrated through
Demo Script
```

Frontera operacional:

```text
Demo Script
→ Public Action
→ Runtime Boundary
→ Controlled Runtime Transition
→ Read Model / UI
```

Separación lógica aceptada:

```text
Composition
Runtime State
Read Models
```

No implica tres stores físicos.

Activity permanece:

```text
read model / projection
```

y nunca:

```text
factual authority
evidence ledger
TES Event ledger
```

---

# 6. Guardrail upstream — tensión de ADR-001 y Experience authority

Session 12 confirmó una ambigüedad real:

no todos los artefactos llamados `ExperienceDefinition` poseen la misma autoridad.

Actualmente deben distinguirse conceptualmente, aunque NO deben renombrarse necesariamente en esta sesión:

```text
Candidate Product Experience Definition
→ interpreted against TES
→ non-executable candidate
→ explicit gaps

domain/contracts.ts::ExperienceDefinition
→ functional/product translation candidate
→ richer contract
→ not demonstrated as TES-complete

demo-factory/contracts.ts::ExperienceDefinition
→ runtime Experience descriptor/reference
→ minimal runtime representation
```

No debes asumir:

```text
object named ExperienceDefinition
+
tesBaseline
=
TES-validated Experience Definition
```

Tampoco debes asumir:

```text
bootstrap resolved Experience reference
=
semantic validation
```

Ni:

```text
tesBaseline
=
validation certificate
```

Para esta sesión:

```text
runtime Experience descriptor
≠
validated Product Experience Definition
≠
classification authority
```

El evaluator NO puede utilizar:

* el nombre `ExperienceDefinition`;
* presencia de `tesBaseline`;
* resolución bootstrap;
* presencia runtime;

como evidencia de autoridad semántica o clasificadora.

Si el experimento necesita hacerlo para alcanzar los resultados esperados:

```text
STOP
```

No reabras ADR-001.

No renombres todavía las interfaces salvo que exista una necesidad estrictamente local y reversible, y en tal caso documenta por qué.

No conviertas esta sesión en una migración de `ExperienceDefinition`.

---

# 7. Guardrail downstream — Authority Frontier de Activity

Activity permanece downstream.

La dirección legítima es:

```text
Evidence
   ↓
Authority-bounded contextual evaluation
   ↓
EvaluationOutcome
   ↓
Projection
   ↓
Activity / UI
```

La dirección inversa está prohibida:

```text
Activity
   ↓
Evaluation
```

Activity puede eventualmente presentar o resumir un EvaluationOutcome.

Pero Activity NO puede:

* convertirse en input autoritativo del evaluator;
* demostrar que la actividad ocurrió;
* clasificar la actividad;
* resolver incertidumbre;
* escoger entre fuentes en conflicto;
* convertir un `undetermined` en `negative`;
* convertir una evaluación relativa a Experience en TES Event;
* inferir Progression, Result o Completion;
* adquirir mayor autoridad por ser visible en UI.

Invariant experimental:

> Activity may project or summarize an EvaluationOutcome but may not strengthen, resolve or reinterpret its epistemic status.

Expresado provisionalmente:

```text
Authority(Activity representation)
<=
Authority(projected source claim)
```

No promociones esta fórmula como axioma arquitectónico general durante esta sesión.

Úsala únicamente como guardrail experimental.

Cuando inspecciones el repositorio, comprueba si Activity participa actualmente en el evaluator.

Si no existe dependencia:

* documenta la separación;
* no construyas un test artificial de UI solo para demostrar lo evidente.

Si existe dependencia:

* identifícala como riesgo material;
* aplica el cambio mínimo necesario para restaurar la dirección correcta;
* documenta el delta.

Una modificación o eliminación de la proyección Activity no debe alterar el outcome del evaluator.

---

# 8. Qué NO cuenta como AvailableAuthority

Para este experimento:

```text
AvailableAuthority
≠
runtime resolution
≠
artifact naming
≠
tesBaseline field
≠
Activity/read-model presentation
≠
evaluator implementation itself
≠
provider label by mere presence
```

La autoridad debe proceder de un input explícitamente tratado como competente para el claim que emite, dentro de un scope declarado o experimentalmente controlado.

No conviertas esa afirmación en una arquitectura final de authority management.

---

# 9. Evidence constante

Reutiliza el mismo caso factual de Session 11.

Conceptualmente:

```text
participant completed Cooking Class
during stay S
at property P
```

El input debe permanecer neutral respecto a Experience.

No añadas al Evidence campos que afirmen:

```text
relevant
significant
TES Event
progress
result
reward
```

Si `EvidenceInput.interpretation` existe actualmente, no lo uses como atajo para introducir la conclusión que el evaluator debería derivar.

Si participa materialmente, documenta cómo se trata y preserva su carácter provisional.

---

# 10. ExperienceContext constante en los tests críticos

Para aislar la variable autoridad, los tests centrales deben mantener constantes:

```text
Evidence
+
ExperienceContext
```

y cambiar únicamente la autoridad/cobertura disponible.

El caso recomendado para los tests críticos es:

```text
Evidence:
Cooking Class completed

ExperienceContext:
Active Challenge
+
same stay
+
same property
```

Active Challenge requiere experimentalmente una clasificación relacionada con:

```text
sport-wellness
```

No branches por Experience ID.

Los criterios deben proceder de la representación existente de la Product Experience Definition/contexto experimental.

---

# 11. Casos obligatorios

## Caso A — Positive control

Usa Family Adventure como control positivo ya defendible desde Session 11.

Una autoridad competente afirma explícitamente:

```text
Cooking Class
→ shared-hotel-activity
```

Family Adventure acepta esa clase.

Resultado permitido:

```text
positive determination
```

No interpretes el resultado como TES Event.

---

## Caso B — Explicit known negative

Mantén:

```text
Evidence = Cooking Class
ExperienceContext = Active Challenge + same stay/property
```

Una autoridad competente afirma explícitamente:

```text
Cooking Class
NOT sport-wellness
```

Active Challenge requiere `sport-wellness`.

Resultado permitido:

```text
negative determination
```

El negativo queda limitado al scope/version de la autoridad.

No extrapoles universalmente:

```text
Cooking Class is never sport/wellness
```

---

## Caso C — Incomplete authority

Mantén EXACTAMENTE:

```text
same Evidence
same Active Challenge ExperienceContext
```

La autoridad afirma:

```text
Cooking Class
→ shared-hotel-activity
```

pero NO declara que el conocimiento de clasificaciones de Cooking Class sea completo.

La ausencia de:

```text
sport-wellness
```

NO autoriza un negativo.

Resultado esperado:

```text
undetermined
```

Este es un falsificador central de Session 13.

Si devuelve negative:

```text
H13c FAILED
```

No modifiques semántica para evitarlo.

---

## Caso D — Scoped exhaustive authority

Mantén:

```text
same Evidence
same ExperienceContext
```

Ahora la autoridad declara que el conjunto conocido de clasificaciones es exhaustivo para un scope/version concretos.

Por ejemplo conceptualmente:

```text
known classifications:
- shared-hotel-activity

coverage:
complete for activity classification
within property P / catalogue version V
```

Si:

```text
sport-wellness
```

no pertenece al conjunto exhaustivo conocido, puede sostenerse:

```text
negative determination
```

únicamente dentro de ese scope.

No conviertas `complete` en propiedad universal.

---

## Caso E — Missing classification authority

Mismos:

```text
Evidence
ExperienceContext
```

No existe classification authority competente disponible.

Resultado esperado:

```text
undetermined
```

Nunca:

```text
negative
```

---

## Caso F — Conflicting authority

Mismos:

```text
Evidence
ExperienceContext
```

Dos claims competentes disponibles entran en conflicto.

Conceptualmente:

```text
Authority A:
Cooking Class → sport-wellness

Authority B:
Cooking Class NOT sport-wellness
```

No existe una precedence policy aceptada.

Resultado esperado:

```text
undetermined / conflicting
```

No:

```text
choose A
```

ni:

```text
choose B
```

NO implementes source precedence.

---

# 12. Representación experimental del outcome

El booleano de Session 11:

```text
relevant: boolean
```

es sospechoso porque puede colapsar:

```text
known negative
undetermined
```

en:

```text
false
```

Inspecciona primero sus consumidores.

Si no existen consumidores que exijan compatibilidad, puedes sustituir o cualificar el contrato mediante la forma local mínima que preserve los tres tipos de claim.

Puede utilizarse, por ejemplo:

* discriminated union;
* literal union;
* test-local representation;
* objeto experimental mínimo.

Pero NO promociones la forma elegida a:

* ontology;
* universal `EvaluationOutcome`;
* API contract;
* TES concept;
* cross-domain rules language.

La representación utilizada es:

```text
experimental mechanism
```

hasta evaluación posterior.

No elijas nombres pensando en arquitectura final.

El objetivo es preservar la diferencia epistemológica, no diseñar vocabulario definitivo.

---

# 13. Representación experimental de authority/completeness

Puedes introducir únicamente lo mínimo necesario para expresar experimentalmente:

```text
positive classification assertion
explicit exclusion
incomplete coverage
scoped exhaustive coverage
missing authority
conflicting claims
```

No construyas:

```text
ClassificationAuthorityRegistry
AuthorityService
TaxonomyService
AuthorityProvider
PrecedencePolicyEngine
GenericCataloguePlatform
```

Una función pura + fixtures explícitos es preferible si basta.

Los fixtures NO se promocionan a arquitectura.

---

# 14. Falsificadores explícitos

Considera H13 total o parcialmente falsificada/no soportada si ocurre cualquiera de estos casos:

1. ausencia en un catálogo incompleto produce negative;
2. missing classification authority produce negative;
3. conflicto entre claims competentes se resuelve mediante precedence inventada;
4. el evaluator necesita branch por Experience ID;
5. el evaluator inventa clasificaciones;
6. el evaluator usa Activity como input autoritativo;
7. Activity transforma `undetermined` en `negative` como parte de la lógica;
8. el evaluator usa `tesBaseline` como certificado de validación;
9. el evaluator usa el nombre `ExperienceDefinition` como prueba de autoridad;
10. bootstrap resolution se interpreta como semantic validation;
11. el evaluator necesita reconocer TES Event para calcular relevance;
12. hace falta construir taxonomy/authority/rules engine para ejecutar el experimento;
13. cambiar authority/coverage no puede cambiar el claim legítimo manteniendo constantes Evidence y ExperienceContext;
14. el experimento solo funciona añadiendo semántica no respaldada por las Product Experience Definition candidates existentes.

Si ocurre una de estas situaciones, no amplíes el sistema para obtener el resultado esperado.

Documenta:

```text
FAILED
INCONCLUSIVE
NO-GO
STOP
```

según corresponda.

---

# 15. Restricciones permanentes de Session 13

NO debes:

* crear ADR-005;
* publicar Architecture v0.5;
* reabrir ADR-001–004 salvo contradicción genuina;
* declarar `ExperienceDefinition` semánticamente validada por nombre;
* asumir `tesBaseline = validated`;
* resolver la nomenclatura final de Experience artifacts;
* fijar classification authority final;
* asumir Scenario como classification authority final;
* asumir provider como semantic authority;
* construir shared taxonomy;
* diseñar taxonomy final;
* implementar precedence de fuentes;
* crear Experience engine;
* crear participation engine;
* crear generic rules DSL;
* introducir persistencia;
* introducir event sourcing;
* crear evidence ledger;
* crear audit platform;
* reconocer TES Event;
* promover `RelevantEvidence = SignificantEvent`;
* modificar `SignificantEvent` salvo necesidad estricta e incidental;
* diseñar TES Pattern;
* diseñar TES Sequence;
* diseñar TES Progression;
* diseñar TES Result;
* diseñar Measurement;
* diseñar Learning;
* diseñar Treasure Hunt;
* inventar arquitectura API sin API real verificada.

---

# 16. Preference for minimum reversible delta

Preferencia:

```text
existing evaluator
+
minimal authority representation
+
open-world outcome distinction
+
focused tests
+
session documentation
```

No:

```text
new architectural subsystem
```

El experimento debe poder retirarse con un delta pequeño si H13 no sobrevive.

No conviertas implementaciones experimentales en contratos públicos salvo que ya sean necesarios por la topología real existente.

---

# 17. Tests mínimos esperados

La matriz experimental mínima debe demostrar:

| Evidence      | ExperienceContext | Authority                                   | Coverage                       | Expected claim           |
| ------------- | ----------------- | ------------------------------------------- | ------------------------------ | ------------------------ |
| Cooking Class | Family Adventure  | positive membership → shared-hotel-activity | sufficient for positive        | positive                 |
| Cooking Class | Active Challenge  | explicit exclusion from sport-wellness      | scoped competent               | negative                 |
| Cooking Class | Active Challenge  | shared-hotel-activity only                  | incomplete                     | undetermined             |
| Cooking Class | Active Challenge  | classification set without sport-wellness   | explicitly exhaustive in scope | negative                 |
| Cooking Class | Active Challenge  | none                                        | none                           | undetermined             |
| Cooking Class | Active Challenge  | conflicting competent claims                | unresolved                     | undetermined/conflicting |

Añade únicamente tests adicionales si una condición real del repositorio los exige.

Comprueba también:

```text
no Experience-ID branching
```

y:

```text
Activity not required for evaluator outcome
```

Si Activity solo es downstream y no participa en el evaluator, no construyas una gran batería UI.

---

# 18. Verificación del repositorio

Ejecuta todas las verificaciones reales que ya utilice el proyecto.

Como mínimo, si existen:

```text
tests
typecheck
lint
build
```

No sustituyas la suite completa por tests aislados.

Informa:

* test files totales;
* tests totales;
* tests passing/failing;
* typecheck;
* lint;
* build;
* archivos modificados;
* archivos nuevos;
* archivos eliminados;
* branches específicos por Experience ID encontrados o no encontrados.

Si alguna verificación no existe en el repositorio, indícalo.

---

# 19. Documento de Session 13

Crea un documento de sesión siguiendo el estilo real de las sesiones anteriores.

Título:

```text
Session 13 — Authority-Bounded Open-World Evaluation Experiment
```

Debe contener como mínimo:

## Hypothesis

H13 y subhipótesis.

## Falsifiers

Lista explícita.

## Repository state before experiment

Qué existía antes y qué autoridad tenía cada artefacto relevante.

## Authority guardrails

Documenta expresamente:

```text
tesBaseline ≠ validation certificate
runtime Experience descriptor ≠ semantic authority
Activity ≠ factual/evaluation authority
evaluator ≠ classification authority
```

## Experimental design

Qué variable permanece constante y cuál cambia.

## Implementation delta

Delta exacto y por qué es el mínimo.

## Test matrix

Expected vs observed.

## Evidence

Qué demuestra realmente la ejecución.

## Unexpected findings

Incluye dependencias, consumers, authority laundering o incompatibilidades inesperadas.

## Limitations

Qué NO se ha demostrado.

## Architectural evaluation

Sin promoción automática.

## Verdict

Uno de:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NO-GO
STOP
```

---

# 20. Claims que una ejecución positiva podría soportar

Incluso con todos los tests verdes, Session 13 podría como máximo aportar evidencia para claims del tipo:

```text
neutral Evidence can remain independent
from Experience-relative evaluation

same Evidence + same ExperienceContext
can legitimately yield different claim types
when authority/coverage changes

absence in incomplete knowledge
does not justify a negative determination

a scoped negative requires sufficient authority
to exclude the relation

missing or conflicting authority
can remain undetermined

the evaluator need not become classification authority

Activity can remain downstream
without influencing the evaluation
```

No conviertas automáticamente estos claims en arquitectura aceptada.

La promoción corresponde a una evaluación posterior.

---

# 21. Claims que Session 13 NO puede soportar

No puede demostrar:

* cuál debe ser la classification authority final;
* que Scenario sea classification authority;
* que un provider sea classification authority;
* que exista una universal taxonomy;
* que un catálogo de propiedad sea suficiente en todos los casos;
* precedence entre fuentes;
* schema definitivo de authority;
* enum definitivo de EvaluationOutcome;
* TES Event recognition;
* Pattern;
* Sequence;
* Progression;
* Result;
* Measurement;
* Learning;
* participation semantics;
* group semantics;
* Treasure Hunt;
* persistencia;
* event sourcing;
* provider architecture;
* API architecture;
* Activity UX final;
* semantic completeness de `ExperienceDefinition`;
* necesidad de modificar ADR-001.

---

# 22. Criterio de éxito epistemológico

El éxito de Session 13 NO es:

```text
all tests green
```

El éxito es obtener evidencia capaz de discriminar esta diferencia:

```text
we cannot establish X
≠
we have established NOT X
```

y demostrar que esa diferencia puede mantenerse a través del evaluator sin:

* autoridad inventada upstream;
* authority laundering en `ExperienceDefinition`;
* authority laundering downstream en Activity;
* taxonomía universal;
* Event recognition;
* rules engine.

El patrón crítico esperado es:

```text
same Evidence
+
same ExperienceContext
+
different available authority / coverage
        ↓
different legitimate evaluation claims
```

---

# 23. Condición de STOP por sobrearquitectura

Si para distinguir:

```text
positive
negative
undetermined
```

resulta necesario introducir una infraestructura sustancial de:

* taxonomy;
* providers;
* registries;
* precedence;
* persistence;
* workflow;
* rules;
* participation;

detente.

El resultado correcto será:

```text
INCONCLUSIVE
```

o:

```text
NO-GO
```

para la forma propuesta.

No construyas la infraestructura.

---

# 24. No promoción al terminar

Aunque H13 resulte SUPPORTED:

```text
Experiment
→ Evidence
→ Evaluation
→ Promotion
```

Por tanto, al terminar Session 13:

```text
NO ADR-005
NO Architecture v0.5
NO Treasure Hunt
```

La siguiente fase, si la evidencia lo justifica, será una sesión posterior de consolidación/evaluación arquitectónica.

---

# 25. Respuesta final esperada de Codex

Devuélveme exactamente una evaluación estructurada que incluya:

1. **Repository inspection**

   * topología encontrada;
   * evaluator actual;
   * consumers;
   * ExperienceDefinition variants;
   * Activity dependencies.

2. **Baseline compatibility**

   * contradicciones materiales, si existen;
   * diferencias no materiales.

3. **Experimental delta**

   * cambios realizados;
   * por qué constituyen el delta mínimo.

4. **Authority representation**

   * cómo representaste positive/exclusion/coverage/missing/conflict;
   * por qué NO debe interpretarse como arquitectura final.

5. **Evaluation outcome representation**

   * cómo evitaste colapsar negative y undetermined;
   * impacto sobre el booleano previo.

6. **ADR-001 guardrail**

   * confirmación de que `tesBaseline`, naming y bootstrap no se utilizaron como autoridad semántica.

7. **Activity Authority Frontier**

   * confirmación de que Activity sigue downstream;
   * cualquier riesgo detectado de strengthening/reinterpretation.

8. **Test matrix**

   * expected;
   * observed;
   * verdict por caso.

9. **Verification**

   * tests;
   * test files;
   * typecheck;
   * lint;
   * build.

10. **Files changed**

    * nuevos;
    * modificados;
    * eliminados.

11. **Authority laundering review**

    * upstream;
    * evaluator;
    * downstream.

12. **Claims supported by evidence**

13. **Claims NOT supported by evidence**

14. **Limitations**

15. **Session 13 verdict**

    * SUPPORTED;
    * SUPPORTED WITH QUALIFICATION;
    * INCONCLUSIVE;
    * NO-GO;
    * STOP.

16. **Recommended next step**

    * sin crear ADR-005;
    * sin publicar Architecture v0.5;
    * sin avanzar a Treasure Hunt.

Sé adversarial.

Si la hipótesis no sobrevive al experimento, dilo.

No cambies la arquitectura para protegerla.
