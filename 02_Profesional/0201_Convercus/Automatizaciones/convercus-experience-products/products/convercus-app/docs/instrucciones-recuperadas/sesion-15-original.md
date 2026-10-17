# Session 15 — Treasure Hunt: Distributed Evidence and Sufficiency Experiment

Trabaja sobre el repositorio existente:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

No empieces desde cero.

No rediseñes Architecture v0.5.

No reabras ADR-001–005 salvo contradicción genuina.

No conviertas Treasure Hunt en una nueva Experience Definition validada.

No diseñes todavía Treasure Hunt completo.

Esta sesión inicia un nuevo ciclo experimental:

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

Nunca amplíes semántica o infraestructura solo para conseguir tests verdes.

---

# 1. Estado arquitectónico vigente

El baseline actual es:

```text
ADR-001 → ACCEPTED
ADR-002 → ACCEPTED
ADR-003 → ACCEPTED
ADR-004 → ACCEPTED
ADR-005 → ACCEPTED

Architecture v0.5 → ACTIVE
```

Architecture v0.5 distingue:

```text
Composition flow
```

de:

```text
Contextual evaluation flow
```

y deja explícitamente unresolved:

* TES Event recognition;
* taxonomy alignment;
* semantic mapping authority;
* authority accreditation;
* conflict precedence;
* naming/maturity de `ExperienceDefinition`;
* Activity UX para evaluaciones no resueltas;
* APIs reales.

Treasure Hunt fue declarado:

```text
READY FOR A BOUNDED NEXT EXPERIMENT
```

No significa que Treasure Hunt sea ya una Experience validada ni que posea un domain model aprobado.

---

# 2. Qué simplificación de los experimentos anteriores vamos a tensionar

Cooking Class utilizó esencialmente:

```text
one participant
+
one factual Evidence
+
one ExperienceContext
+
one contextual evaluation
```

Session 13 corrigió la simplificación closed-world:

```text
unknown
≠
negative
```

Treasure Hunt permite ahora tensionar una simplificación diferente:

```text
one atomic Evidence
```

Session 15 debe investigar:

```text
multiple independent factual evidences
        ↓
sufficiency evaluation
```

sin introducir todavía:

```text
group participation
TES Sequence
TES Progression
TES Result
TES Completion
generic Experience engine
```

---

# 3. Product scenario mínimo

Utiliza un único participante.

Narrativamente puede ser:

```text
Business Guest
```

durante una estancia en un hotel orientado a negocios.

El contexto comercial puede formularse como una pequeña búsqueda distribuida por distintos espacios del hotel.

Por ejemplo:

```text
Participant P
Stay S
Property H
Treasure Hunt scenario T
```

No es necesario fijar qué sistema identifica finalmente a `P`.

No decidas todavía si representa:

* loyalty member;
* booking owner;
* account;
* device holder;
* TES participant;
* ExperienceParticipation.

Para este experimento basta una referencia estable y controlada.

---

# 4. No refinar todavía el Contrato semántico de producto

El escenario actual mantiene:

```text
one participant
```

y un dominio experimental controlado de validación/suficiencia.

Por tanto, Session 15 NO debe refinar el actual:

```text
Contrato semántico de producto
```

ni modificar la tesis general App/Builder para introducir semántica colectiva.

Registra únicamente este trigger futuro:

> El Contrato semántico de producto deberá reconsiderarse cuando un experimento cooperativo requiera distinguir de forma material participante individual, contribuyente, grupo, pertenencia, atribución de evidencia o resultado colectivo.

En forma abreviada:

```text
single-participant Treasure Hunt
→ no semantic-contract refinement required

cooperative / multi-participant Treasure Hunt
→ semantic-contract review trigger
```

No anticipes esa revisión.

---

# 5. Evidence factual

Utiliza tres evidencias independientes:

```text
Evidence A
Evidence B
Evidence C
```

Narrativamente pueden corresponder a tres pistas o marcadores situados en espacios diferentes del hotel.

Ejemplo no normativo:

```text
A → marker observed/validated in lobby
B → marker observed/validated in business lounge
C → marker observed/validated in another eligible hotel area
```

No fijes QR, NFC, staff validation, provider o API.

La evidencia debe conservarse factual y neutral.

Puede contener únicamente aquello necesario para identificar:

```text
evidenceRef
subjectRef
scenario/huntRef
observed clue/marker identity
situated context needed by the experiment
```

No añadas como facts:

```text
progress
percentage
cluesFound
sufficient
solved
completed
reward
Result
TES Event
```

En particular:

```text
Evidence
≠
its evaluation
```

según ADR-005.

---

# 6. Criterio experimental de suficiencia

Para evitar que suficiencia se reduzca a un contador, utiliza el siguiente criterio experimental:

```text
A AND (B OR C)
```

Por tanto:

```text
A + B
→ sufficient evidence

A + C
→ sufficient evidence

A
→ sufficiency not established

B
→ sufficiency not established

C
→ sufficiency not established

B + C
→ sufficiency not established

A + A
→ sufficiency not established
```

El criterio existe únicamente para falsificar:

```text
quantity
≠
sufficiency
```

y:

```text
aggregation
≠
sufficiency
```

No promociones:

```text
A AND (B OR C)
```

como regla general de Treasure Hunt.

No construyas un generic expression engine.

No construyas rules DSL.

No construyas un `TreasureHuntRulesEngine`.

Una función pura y fixtures explícitos son preferibles.

---

# 7. Hipótesis principal

## H15 — Distributed Evidence Sufficiency

> Varias Evidence factual e independientemente válidas pueden contribuir conjuntamente a un claim derivado de suficiencia, pero su pluralidad, cantidad u orden no establecen por sí solos esa suficiencia. El claim requiere un criterio scoped y autoritativo distinto del contenido factual de cada Evidence.

Formulación analítica provisional:

```text
SufficiencyClaim =
f(
    EvidenceSet,
    SituatedContext,
    SufficiencyCriterion
)
```

No conviertas esta fórmula en arquitectura.

`EvidenceSet` no debe convertirse automáticamente en aggregate persistente.

`SufficiencyCriterion` no debe convertirse automáticamente en service, engine o TES concept.

---

# 8. Subhipótesis

## H15a — Evidence independence

Cada Evidence conserva identidad factual independiente de las demás y de la evaluación de suficiencia.

```text
Evidence A
≠
"Sufficient"
```

## H15b — Quantity is not sufficiency

Dos registros no son suficientes simplemente porque:

```text
count = 2
```

Debe cumplirse el criterio cualitativo experimental.

Por tanto:

```text
A + B → sufficient
B + C → not established
```

aunque ambos conjuntos tengan cardinalidad 2.

## H15c — Duplicate evidence does not create sufficiency

```text
A + A
```

no debe satisfacer:

```text
A AND (B OR C)
```

La duplicación de records no equivale a contribuciones semánticamente distintas.

No diseñes una plataforma genérica de deduplicación.

Representa únicamente el caso mínimo necesario para falsificar el contador ingenuo.

## H15d — Order independence

Para Session 15, las pistas son deliberadamente unordered.

Por tanto:

```text
A then B
```

y:

```text
B then A
```

deben sostener el mismo claim.

Esto debe preservar:

```text
multiple evidence
≠
TES Sequence
```

No modeles pistas habilitantes, encadenadas u ordenadas todavía.

Registra:

```text
ordered / enabling clues
→ future experiment
```

## H15e — Open-world insufficiency

Cuando el criterio no se satisface con Evidence disponible:

```text
sufficiency not established
```

NO significa necesariamente:

```text
hunt failed
solution false
participant failed
impossible to satisfy
```

La Evidence puede:

* no haber llegado todavía;
* estar retrasada;
* estar pendiente de validación;
* ser ambigua;
* proceder después de otra fuente;
* entrar posteriormente en conflicto.

Session 15 no debe construir latency/conflict infrastructure.

Solo debe conservar la diferencia:

```text
not established
≠
established false
```

## H15f — Sufficiency is not solution recognition

Incluso cuando:

```text
A + B
```

establece evidencia suficiente, el claim máximo de este experimento es equivalente a:

```text
sufficient evidence established
under criterion K
within scenario T
```

No implica automáticamente:

```text
solution recognized
Treasure Hunt solved
Treasure Hunt completed
TES Result
TES Completion
TES Event
```

La posible frontera:

```text
Sufficient Evidence
        ↓ ?
Solution Recognition
```

permanece:

```text
UNRESOLVED
```

## H15g — Sufficiency is not TES Progression

No inferir:

```text
A = 33%
A+B = 66%
A+B+C = 100%
```

como TES Progression.

Tampoco:

```text
number of clues
=
Progression
```

Un contador UI podría existir en el futuro como read model, pero no adquiere semántica TES por ello.

## H15h — Partial incentive remains downstream

Cuando existe:

```text
sufficient evidence established
```

el huésped **puede quedar en condiciones de recibir un incentivo parcial**.

La relación experimental permitida es:

```text
SufficiencyClaim
        ↓
possible eligibility / authorization
for partial incentive
```

Pero:

```text
partial incentive
≠
proof of sufficiency
```

y:

```text
partial incentive
≠
TES Result
```

y:

```text
partial incentive
≠
Treasure Hunt completion
```

La dirección es únicamente:

```text
sufficiency evaluation
        ↓
downstream incentive eligibility/use
```

Nunca:

```text
incentive exists
        ↓
therefore evidence was sufficient
```

No construyas reward engine.

No construyas incentive engine.

Si el repositorio ya posee una representación mínima compatible, puede utilizarse de forma experimental.

Si no existe, usa únicamente una derivación test-local o documenta la posibilidad downstream.

No crees infraestructura para demostrarla.

## H15i — Activity remains downstream

Activity no participa en:

```text
evidence aggregation
sufficiency evaluation
criterion satisfaction
```

Puede eventualmente presentar:

```text
clue observed
sufficient evidence established
partial incentive available
```

pero no originar dichos claims.

---

# 9. Authority Frontier candidata

Session 15 investiga provisionalmente una nueva pregunta:

> ¿Quién tiene autoridad para afirmar que un conjunto de Evidence es suficiente para sostener un claim concreto dentro de un scope?

Denomina analíticamente, si ayuda:

```text
Evidence Sufficiency Authority
```

pero NO promociones el término a componente arquitectónico.

No crees:

```text
EvidenceSufficiencyAuthorityService
SufficiencyRegistry
RuleProvider
CriteriaEngine
```

La pregunta es sobre autoridad del claim, no sobre topología de software.

---

# 10. Distinción entre aggregation y sufficiency

Esta distinción es central.

```text
Aggregation
```

puede significar únicamente:

```text
these Evidence records are being considered together
```

No significa:

```text
they are sufficient
```

Por tanto:

```text
aggregation
≠
sufficiency
```

Y tampoco:

```text
sufficiency
≠
solution recognition
```

Conserva las tres posibles fronteras:

```text
Independent factual Evidence
        ↓
considered together / aggregation
        ↓
Sufficiency evaluation
        ↓
Sufficiency claim
        ↓ ?
Future solution-recognition boundary
```

No promociones `aggregation` como nuevo aggregate/domain entity salvo que la implementación mínima lo exija de forma demostrada.

---

# 11. Diseño experimental mínimo obligatorio

Mantén constantes:

```text
Participant P
Stay S
Property H
Treasure Hunt scenario T
Sufficiency criterion K = A AND (B OR C)
```

Cambia únicamente la Evidence disponible.

## Caso A — no evidence

```text
{}
```

Expected:

```text
sufficiency not established
```

No failure.

## Caso B — A only

```text
{A}
```

Expected:

```text
sufficiency not established
```

## Caso C — B + C

```text
{B, C}
```

Expected:

```text
sufficiency not established
```

Crítico porque:

```text
count = 2
```

pero el criterio no se satisface.

## Caso D — A + B

```text
{A, B}
```

Expected:

```text
sufficiency established
```

## Caso E — A + C

```text
{A, C}
```

Expected:

```text
sufficiency established
```

## Caso F — A + A

Dos records que representan la misma contribución factual relevante.

Expected:

```text
sufficiency not established
```

No:

```text
count 2 → sufficient
```

## Caso G — order independence

```text
[A, B]
```

vs.

```text
[B, A]
```

Expected:

```text
same sufficiency claim
```

## Caso H — extra evidence

```text
{A, B, C}
```

Expected:

```text
sufficiency established
```

pero NO stronger claim que A+B o A+C.

En particular, NO:

```text
more evidence
→ more Progression
→ stronger Result
```

## Caso I — downstream partial incentive

Para un outcome de suficiencia establecido:

```text
possible partial-incentive eligibility
```

puede derivarse downstream.

Para un outcome no establecido:

```text
no eligibility may be inferred from sufficiency
```

Esto NO debe convertir el incentive en autoridad retroactiva.

Si implementar este caso exige infraestructura nueva, déjalo como documented downstream implication y NO lo fuerces al código.

---

# 12. Latency, ambiguity and confusing evidence

La observación siguiente debe quedar registrada:

> En escenarios reales, una aparente insuficiencia puede provenir no solo de ausencia factual sino también de latencia, evidencia todavía no validada, ambigüedad, confusión de identidad, duplicación o conflicto.

Session 15 NO debe resolver esos casos.

No diseñes:

* pending evidence state machine;
* latency model;
* conflict engine;
* confidence model;
* identity-resolution system.

Solo preserva el invariant:

```text
insufficiency under currently available evidence
does not prove failure
```

Registra esos factores como futuras Authority Frontiers/cualificaciones candidatas.

---

# 13. No convertir Treasure Hunt en TES semantics

Está expresamente prohibido inferir:

```text
Clue
=
TES Event
```

```text
multiple clues
=
Pattern
```

```text
ordered clues
=
Sequence
```

```text
clue count
=
Progression
```

```text
sufficient evidence
=
Result
```

```text
all clues
=
Completion
```

```text
partial incentive
=
Result
```

La cadena TES sigue siendo:

```text
Event
→ Pattern
→ Sequence
→ Progression
→ Result
→ Measurement
→ Learning
```

Session 15 no operacionaliza ninguno de estos conceptos.

---

# 14. No convertir Treasure Hunt en Experience Definition

Treasure Hunt en esta sesión es:

```text
experimental situated scenario
```

No:

```text
Validated Product Experience Definition
```

No crees un Product Experience Definition completo para Treasure Hunt.

No añadas artificialmente:

* Pattern;
* Sequence;
* Progression;
* Result;
* Measurement;
* Learning;

para hacerlo parecer semánticamente completo.

Si el experimento requiere esas construcciones:

```text
STOP
```

porque el diseño ha excedido el scope.

---

# 15. Inspección del repositorio antes de implementar

Localiza como mínimo:

* `evidence-relevance.ts`;
* `evidence-relevance.test.ts`;
* cualquier tipo factual de Evidence existente;
* cualquier representación de authority;
* Activity/AppSnapshot;
* incentive/reward contracts existentes;
* runtime/public-action boundary;
* ADR-005;
* Architecture v0.5;
* Session 13;
* Session 14.

Determina si la nueva evaluación de suficiencia debe:

```text
A. extender experimentalmente una frontera existente
```

o:

```text
B. usar una función pura separada
```

No decidas por simetría.

La preferencia semántica es **no mezclar relevance con sufficiency** si representan claims diferentes.

Por tanto, no sobrecargues:

```text
evaluateEvidenceRelevance()
```

solo porque ya existe.

Si una función experimental separada es más honesta:

```text
evaluateEvidenceSufficiency(...)
```

o nombre equivalente puede ser preferible.

Pero el nombre NO se promociona a arquitectura.

---

# 16. Preferencia de implementation delta

Preferencia:

```text
existing factual Evidence concepts
+
minimal experimental sufficiency boundary
+
explicit fixtures
+
focused tests
+
Session 15 document
```

No:

```text
Treasure Hunt module hierarchy
generic rules engine
new domain platform
```

La implementación debe ser fácilmente eliminable si H15 falla.

---

# 17. Falsifiers

Considera H15 total o parcialmente falsificada/no soportada si ocurre cualquiera de estos casos:

1. `B + C` produce sufficiency simplemente porque hay dos evidencias;
2. `A + A` produce sufficiency por count;
3. cambiar el orden A/B cambia el claim en un experimento declarado unordered;
4. Evidence individual necesita contener `sufficient`;
5. Activity count se utiliza como input autoritativo;
6. sufficiency requiere TES Progression;
7. sufficiency se implementa como TES Result;
8. sufficiency requiere Event recognition;
9. incentive concedido se utiliza para inferir retroactivamente suficiencia;
10. para implementar `A AND (B OR C)` hace falta un generic DSL/rules engine;
11. Treasure Hunt debe convertirse en Experience Definition completa;
12. se necesita group semantics para ejecutar este caso unipersonal;
13. la ausencia de una Evidence produce `failed` en vez de preservar no-determinación;
14. más Evidence produce un claim semánticamente “más completo” sin criterio adicional;
15. el experimento obliga a refinar el Contrato semántico de producto pese a mantener un solo participante.

Si ocurre:

```text
do not expand architecture
```

Documenta el resultado.

---

# 18. Contrato semántico de producto — trigger futuro obligatorio

Session 15 debe terminar registrando explícitamente:

```text
Semantic Product Contract review trigger:
first cooperative / multi-participant Treasure Hunt experiment
```

Esa futura revisión deberá cuestionar, como mínimo:

```text
individual participant
contributor
group
membership
evidence attribution
shared evidence
group sufficiency
group outcome
```

No respondas ahora esas preguntas.

Solo registra el trigger.

---

# 19. Pistas habilitantes / ordenadas — trigger futuro

Session 15 utiliza:

```text
unordered clues
```

No presupone que Treasure Hunt general sea unordered.

Registra:

```text
ordered or enabling clues
→ separate future experiment
```

Ese experimento deberá distinguir, llegado el momento:

```text
temporal order
causal enablement
narrative order
TES Sequence
```

No los mezcles ahora.

---

# 20. Incentivo parcial — límites

La observación de producto a preservar es:

> Cuando existe evidencia suficiente bajo el criterio experimental, el huésped puede recibir un incentivo parcial.

No convertir esta frase en:

```text
sufficiency automatically grants incentive
```

sin pasar por la autoridad operacional apropiada.

Distingue:

```text
SufficiencyClaim
        ↓
possible incentive eligibility
        ↓
runtime/public action or product policy
        ↓
incentive presentation/use
```

si el repositorio real permite representar esa separación mínimamente.

No diseñes esta cadena si no existe infraestructura suficiente.

En ese caso documenta únicamente:

```text
partial incentive
→ downstream implication
→ not tested operationally
```

---

# 21. Tests y verificaciones

Añade únicamente los tests necesarios para falsificar H15.

Después ejecuta la suite real del repositorio:

```text
tests
typecheck
lint
build
```

si existen.

Informa:

* test files;
* total tests;
* nuevos tests;
* typecheck;
* lint;
* build;
* archivos modificados;
* archivos nuevos;
* archivos eliminados.

Comprueba especialmente:

```text
no generic rule engine
no Experience-ID branching
no TES terminology introduced as runtime semantics
no Activity dependency
no Product Semantic Contract changes
```

---

# 22. Documento Session 15

Crea:

```text
Session 15 — Treasure Hunt: Distributed Evidence and Sufficiency Experiment
```

Debe incluir:

## 1. Hypothesis

H15 y subhipótesis.

## 2. Why Treasure Hunt

Qué simplificación de Cooking Class tensiona.

## 3. Scope

```text
one participant
unordered clues
distributed Evidence
sufficiency
partial incentive downstream
```

## 4. Explicit exclusions

Group semantics, TES semantics, ordered clues, engines, APIs.

## 5. Repository inspection

Estado real previo.

## 6. Experimental model

A, B, C y K = A AND (B OR C).

## 7. Authority Frontier

Qué autoridad experimental sostiene el criterio de suficiencia.

## 8. Test matrix

Expected vs observed.

## 9. Aggregation vs sufficiency

Conclusión explícita.

## 10. Sufficiency vs solution recognition

Conclusión explícita.

## 11. Sufficiency vs incentive

Conclusión explícita.

## 12. Open-world implications

Latency, ambiguity, missing evidence y conflict como límites no resueltos.

## 13. Activity frontier

Confirmación de downstream.

## 14. Semantic Product Contract

Confirmación de que NO se refinó y trigger para cooperative scenario.

## 15. Evidence

Qué quedó realmente demostrado.

## 16. Claims supported

## 17. Claims not supported

## 18. Limitations

## 19. Architectural evaluation

No promotion automática.

## 20. Verdict

Uno de:

```text
SUPPORTED
SUPPORTED WITH QUALIFICATION
INCONCLUSIVE
NO-GO
STOP
```

---

# 23. Claims que una Session 15 positiva podría soportar

Como máximo:

```text
multiple independent Evidence
can participate in one derived evaluation
```

```text
evidence count
does not establish sufficiency
```

```text
evidence aggregation
does not establish sufficiency
```

```text
sufficiency can be derived
without TES Progression / Result
```

```text
unordered Evidence
need not imply TES Sequence
```

```text
missing qualifying Evidence
does not prove failure
```

```text
sufficiency may support
a downstream partial-incentive decision
without becoming the incentive or Result
```

```text
Activity can remain downstream
```

---

# 24. Claims que Session 15 NO puede soportar

No puede demostrar:

* Treasure Hunt como TES-validada Experience;
* Treasure Hunt Completion;
* TES Event;
* TES Pattern;
* TES Sequence;
* TES Progression;
* TES Result;
* Measurement;
* Learning;
* solution-recognition semantics;
* group participation;
* group evidence;
* family semantics;
* contributor membership;
* shared evidence attribution;
* group sufficiency;
* ordered/enabling clue semantics;
* generic rules engine;
* generic sufficiency engine;
* incentive/reward engine;
* real provider architecture;
* persistence;
* latency infrastructure;
* confidence;
* conflict resolution;
* API contracts;
* semantic-contract changes.

---

# 25. Promotion prohibition

Aunque H15 resulte SUPPORTED:

```text
NO ADR-006
NO Architecture v0.6
NO Product Semantic Contract refinement
NO Treasure Hunt Experience Definition
NO group model
```

Session 15 produce:

```text
Experiment
→ Evidence
```

La evaluación/promoción posterior deberá ser una sesión separada si la evidencia lo merece.

---

# 26. Final adversarial questions

Antes del verdict, responde:

1. ¿`A+B` es suficiente porque son dos evidencias o porque satisface K?
2. ¿`B+C` demuestra que count y sufficiency son distintos?
3. ¿`A+A` demuestra que record count no equivale a evidence contribution?
4. ¿El orden alteró accidentalmente el resultado?
5. ¿Se introdujo una TES Sequence implícita?
6. ¿Se introdujo Progression mediante counts?
7. ¿Se convirtió sufficiency en Result o Completion?
8. ¿Se convirtió el incentive en prueba retroactiva?
9. ¿La ausencia se interpretó como fracaso?
10. ¿El evaluator adquirió autoridad que pertenecía al criterio?
11. ¿Treasure Hunt se convirtió accidentalmente en Experience Definition?
12. ¿Se refinó innecesariamente el Contrato semántico de producto?
13. ¿Latency/ambiguity/conflict se mantuvieron abiertos?
14. ¿Group semantics siguen completamente fuera?
15. ¿Ordered/enabling clues siguen fuera?
16. ¿La implementación podría retirarse sin alterar ADR-001–005?

Si alguna respuesta revela sobrepromoción, reduce el verdict.

---

# 27. Respuesta final esperada de Codex

Devuelve:

1. Repository inspection.
2. Baseline compatibility.
3. Experimental model actually implemented.
4. Why the delta is minimal.
5. Evidence representation.
6. Sufficiency criterion representation.
7. Whether relevance evaluator was reused or a separate boundary was created, and why.
8. Full test matrix.
9. Aggregation vs sufficiency result.
10. Duplicate-evidence result.
11. Order-independence result.
12. Open-world insufficiency result.
13. Sufficiency vs solution-recognition assessment.
14. Partial-incentive downstream assessment.
15. Activity frontier assessment.
16. Confirmation that Product Semantic Contract was not changed.
17. Future semantic-contract review trigger.
18. Ordered/enabling-clue future trigger.
19. Latency/ambiguity/conflict unresolved findings.
20. Test/typecheck/lint/build results.
21. Files created/modified/deleted.
22. Claims supported.
23. Claims NOT supported.
24. Limitations.
25. Authority-laundering review.
26. Session 15 verdict.
27. Recommended next step.

Sé adversarial.

No construyas Treasure Hunt para demostrar que Treasure Hunt funciona.

Utilízalo únicamente para falsificar si varias evidencias independientes pueden sostener un claim de suficiencia sin convertir cantidad, orden, incentivo o presentación en semántica que todavía no hemos demostrado.
