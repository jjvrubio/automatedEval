# SESIÓN 36 — PRESENTATION AUTHORITY PROVENANCE STRATIFICATION AUDIT

Continuamos Convercus Demo Factory / Convercus Experience Products inmediatamente después de:

```text
SESSION 35 — Experience-Sourced Guest Experience Name Provenance
```

No reconstruir decisiones anteriores.

---

# 1. BASELINE CONSOLIDADA

```text
SESSION 35 → CLOSED

H35
→ SUPPORTED WITH QUALIFICATION

NO-NEW-RELATION
→ SUFFICIENT

HUNTNAME AUTHORITY
→ ExperienceDefinition.name

EXPERIENCE / HUNTNAME SEMANTIC CORRESPONDENCE
→ SUPPORTED within tested scope

APP CONSUMER BOUNDARY
→ PRESERVED

L3a
→ PRESERVED / EXPERIMENTALLY ADDRESSED H28

L3b
→ PRESERVED / EXPERIMENTALLY ADDRESSED H27

L3c
→ PRESERVED / EXPERIMENTALLY ADDRESSED H29–H30

L4 FRAMING
→ PRESERVED / EXPERIMENTALLY ADDRESSED H32

L4 SUPERVISION SUBJECT
→ PRESERVED / EXPERIMENTALLY ADDRESSED H33

L4 SUPERVISION SESSION
→ PRESERVED / EXPERIMENTALLY ADDRESSED H34

L4 HUNTNAME
→ EXPERIENCE-SOURCED / EXPERIMENTALLY ADDRESSED H35

L5
→ PRESERVED / EXPERIMENTALLY ADDRESSED H25

PRESENTATION AUTHORITY STRATIFICATION
→ EVIDENCE STRENGTHENED
→ NOT PROMOTED
```

Preservar:

```text
Architecture v0.5 → ACTIVE / unchanged
ADR-001–005 → ACCEPTED / unchanged

TES → unchanged
Product Semantic Contract → unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE
→ unchanged

PSC-P02 → NOT CREATED
```

Todos los artefactos experimentales H25–H35 permanecen en cuarentena.

---

# 2. CHARACTER OF SESSION 36

S36 es una sesión de:

```text
CROSS-EXPERIMENTAL AUDIT
+
FALSIFICATION
+
CONSOLIDATION
```

No es, por defecto, una sesión de implementación.

Objetivo:

```text
test whether the accumulated presentation evidence
admits a coherent provenance model
without inventing a universal presentation owner
```

No crear arquitectura para hacer que la hipótesis pase.

---

# 3. H36 — HYPOTHESIS

Hipótesis falsable:

```text
Dentro del alcance experimental H25–H35,
cada afirmación presentacional significativa
puede rastrearse hasta una autoridad explícita
compatible con su significado,

y las relaciones observadas pueden distinguirse
en modos de procedencia diferentes

sin necesitar un PresentationModel universal,
sin convertir DemoScript en propietario
de toda presentación,
y sin convertir App en autoridad semántica.
```

La hipótesis NO exige:

```text
one UI surface
→ one authority
```

Al contrario, debe admitir:

```text
one visual surface
→ multiple independent authorities
```

cuando cada fragmento tenga procedencia separada.

---

# 4. PROVISIONAL AUTHORITY MODES

Utilizar exclusivamente como hipótesis de clasificación inicial:

## MODE U — UI-LOCAL CONVENTION

Copy o transformación puramente presentacional que no introduce una afirmación nueva de dominio.

Ejemplos candidatos:

```text
"Mi aventura"
separadores
pluralización
"Estado:"
generic headings
```

Preservar:

```text
UI-local copy
must not manufacture domain meaning
```

---

## MODE D — DECLARED DOMAIN / ARTIFACT DATA

Valores ya declarados por una fuente cuya responsabilidad incluye ese significado.

Ejemplos candidatos:

```text
Experience.name
BrandArtifact.name
member.name
```

No asumir que cualquier campo descriptivo entra aquí.

La responsabilidad debe estar demostrada.

---

## MODE O — OPERATIONAL / DERIVED AUTHORITY

Representaciones derivadas de estado, referencias, Evidence o evaluación cuyo significado ya está determinado por el runtime/read model.

Ejemplos candidatos:

```text
subjectStates
Supervision.subjects[].id
sessionSubjectRef
Evidence counts
evaluation.sufficiency
derivedClaim
```

Preservar:

```text
derived presentation
must not claim more than the operational/derived source proves
```

---

## MODE E — EXPLICIT SITUATED EDITORIAL DECLARATION

Contenido situado que no puede derivarse legítimamente de hechos/metadata existentes y que necesita declaración explícita para la composición/demostración.

Ejemplos experimentales:

```text
H25 activityPresentation
H27 subjectPresentations
H30 experimentalJourneyPresentations
H32 experimentalIntroductoryFraming
```

Preservar:

```text
declared presentation
!=
factual authority
```

---

# 5. THESE MODES ARE NOT ARCHITECTURE

Los cuatro modos anteriores son:

```text
AUDIT CATEGORIES
```

NO:

```text
layers
services
interfaces
modules
contracts
ownership boundaries
ADR decisions
TES concepts
```

No renombrar clases o mover código para reflejarlos.

Si la clasificación falla:

```text
H36 must fail or qualify
```

No modificar categorías ad hoc sólo para obtener cobertura perfecta.

---

# 6. UNIT OF ANALYSIS

La unidad de análisis NO será:

```text
field
component
page
read model
```

por defecto.

Será:

```text
presentation claim / meaningful fragment
```

porque una sola superficie puede contener múltiples autoridades.

Ejemplo obligatorio:

```text
Mi aventura · Aurora Stay
```

debe analizarse al menos como:

```text
"Mi aventura"
→ U candidate

"Aurora Stay"
→ D candidate
```

No asignar automáticamente la cabecera completa a un solo modo.

---

# 7. H30 MIXED-AUTHORITY CONTROL

`GuestPerspective.message` debe utilizarse como falsador principal contra:

```text
one field → one authority
```

Clasificar separadamente:

```text
initial representation
intermediate situated representations
completion representation
```

y sus fuentes.

Debe quedar visible que:

```text
same output field
can legitimately use different authorities
depending on runtime condition
```

Si esta afirmación no puede sostenerse con las fuentes H30:

```text
H36 → FALSIFIED / QUALIFIED
```

No diseñar un owner común para resolverlo.

---

# 8. H32 COMPOSED-SURFACE CONTROL

Analizar la cabecera de Family Adventure actual:

```text
eyebrow
h1
introductory paragraph
```

como una superficie visual compuesta.

Registrar autoridad de:

```text
generic UI shell
BrandArtifact.name
Experience.name
experimentalIntroductoryFraming
```

Comprobar:

```text
co-location in DOM
!=
shared semantic authority
```

---

# 9. H25 ACTIVITY CONTROL

Analizar H25 cuidadosamente porque combina:

```text
occurred factual Activity / Evidence acceptance
+
declared situated representation
```

Determinar qué autoridad decide:

```text
that an Activity exists
```

y qué autoridad decide:

```text
how that Activity is presented
```

No clasificar toda Activity como MODE E.

Preservar:

```text
factual occurrence authority
!=
presentation-content authority
```

Esta distinción es obligatoria.

---

# 10. H27 SUBJECT PRESENTATION CONTROL

Analizar:

```text
Scenario subject existence/reference
+
DemoScript.subjectPresentations
```

Distinguir:

```text
subject exists
→ non-editorial authority

subject human/situated label
→ explicit editorial declaration
```

Preservar:

```text
presentation cannot create subject
```

---

# 11. H28 ACCOUNT PRESENTATION CONTROL

Descomponer:

```text
Cuenta de Inés
```

como mínimo en:

```text
"Cuenta de"
→ candidate UI convention

"Inés"
→ member.name authority
```

Comprobar que la composición textual no crea:

```text
member → subject
account → viewer
```

Si el prefijo introduce más significado que la fuente acredita:

registrarlo como contraejemplo.

No asumir que H28 prueba automáticamente MODE U + MODE D.

---

# 12. H29 STATUS CONTROL

Analizar:

```text
Estado: habilitado
```

como:

```text
"Estado:"
→ UI/local representation candidate

enabled
→ operational authority

mapping enabled → "habilitado"
→ presentation transformation
```

Determinar si ese mapping cabe legítimamente como presentación derivada o revela una categoría adicional.

No alterar las categorías para salvar el resultado.

---

# 13. H33 / H34 DIAGNOSTIC CONTROLS

Analizar:

```text
subject-p1

Sujeto de sesión operativa
subject-p1
```

Distinguir:

```text
raw operational value
UI diagnostic label
operational relationship
```

Comprobar que App no añade significado no soportado.

H33/H34 deben constituir contraevidencia explícita a:

```text
all human-readable presentation
requires explicit Script declaration
```

---

# 14. H35 SEMANTIC NAME CONTROL

Analizar:

```text
Experience.name
→ GuestPerspective.huntName
```

como posible MODE D.

Compararlo con:

```text
BrandArtifact.name
member.name
```

y determinar si realmente comparten una clase útil de autoridad o si agruparlos oculta diferencias materiales.

Si:

```text
semantic metadata
account factual data
branding configuration
```

resultan demasiado distintos para una misma categoría:

registrar la falsación o cualificación.

No crear subtipos ilimitados sólo para preservar la hipótesis.

---

# 15. COMPLETE ADDRESSED-SURFACE MATRIX

Construir una matriz exhaustiva de todas las superficies modificadas o estudiadas desde H25 hasta H35.

Como mínimo:

```text
Activity existence
Activity title
Activity description

GP huntName
GP sessionLabel
GP subjects[].label
GP subjects[].status
GP message

App eyebrow generic part
App eyebrow brand part
App introductory framing

SP subject heading
SP subject detail ID
SP session label
SP sessionSubjectRef

completion message
initial message
intermediate messages
```

Para cada fragmento registrar:

```text
surface
claim
source
relationship
authority mode candidate
transport
consumer
factual/editorial
composition-specific?
runtime-varying?
experiment proving it
qualification
```

---

# 16. DO NOT LIMIT THE AUDIT TO SUCCESSFUL PATCHES

Incluir también falsaciones y STOP relevantes:

```text
H24
H26
H31
```

porque proporcionan evidencia sobre:

```text
what was NOT authorized
```

Especialmente registrar:

```text
H24
activity situated representation missing

H26
GuestPerspective situated narrative/human representation gaps

H31
composition introductory relation missing
```

y cómo sesiones posteriores pudieron experimentar sólo después de esas falsaciones.

La arquitectura emergente debe explicar también los STOP.

---

# 17. COUNTEREXAMPLE SEARCH

Buscar deliberadamente en las superficies auditadas ejemplos que contradigan cualquiera de estas proposiciones:

```text
P1:
existing authoritative meaning
→ should always be derived

P2:
composition-specific editorial meaning
→ always belongs in DemoScript

P3:
operational presentation
→ never needs explicit declaration

P4:
semantic/artifact metadata
→ can always be presented directly

P5:
UI-local convention
→ never introduces domain meaning

P6:
one claim
→ one authority source
```

No intentar demostrar las seis.

Intentar falsarlas.

Registrar cada una como:

```text
SUPPORTED WITHIN OBSERVED SET
FALSIFIED
INCONCLUSIVE
```

---

# 18. PARTICULARLY IMPORTANT FALSIFIERS

H36 debe considerarse materialmente cualificada o falsificada si encuentra:

```text
a supposedly generic UI string
that actually adds domain meaning
```

o:

```text
an operational output
that legitimately requires composition-specific declaration
```

o:

```text
a DemoScript presentation
that actually functions as factual/runtime authority
```

o:

```text
semantic metadata
whose display needs a separate editorial relationship
```

o:

```text
a presentation claim
whose authority cannot be assigned
without circular reasoning
```

o:

```text
a surface where transport convenience
has been mistaken for semantic ownership
```

---

# 19. NO PRODUCT DELTA BY DEFAULT

S36 should begin with:

```text
CODE DELTA → NONE
```

No cambiar producto para conseguir una clasificación más limpia.

Si durante la auditoría aparece un bug/overclaim nuevo:

```text
record pressure
do not repair it
```

salvo que la ausencia de una corrección impida materialmente observar las fuentes.

En ese caso:

```text
STOP
```

y documentar.

---

# 20. CURRENT SOURCE VERIFICATION

Aunque no haya delta, comprobar que las relaciones actuales siguen presentes en fuentes vigentes.

No depender únicamente de informes históricos.

Inspeccionar directamente al menos:

```text
contracts
artifacts A/B
bootstrap
MockDataAdapter
vertical-evaluation/projectors
App
```

y contrastar con los verdictos H25–H35.

No es necesario repetir todos los recorridos si no hay cambio de código, pero cualquier afirmación sobre fuentes actuales debe proceder del working tree vigente.

---

# 21. HISTORICAL EVIDENCE USE

Los informes/trazas H25–H35 pueden utilizarse como evidencia experimental de:

```text
causality
independence
falsification
```

pero preservar:

```text
historical experiment
!=
current runtime execution
```

No reejecutar toda la historia sólo para producir una tabla si las fuentes están intactas y las trazas son suficientes.

Si se ejecuta suite actual:

registrar el resultado separadamente.

---

# 22. UI-LOCAL COPY GUARDRAIL

No clasificar automáticamente como legítimo todo copy que permanezca en App.

Para cada fragmento UI-local seleccionado preguntar:

```text
does this string merely organize/present?
```

o:

```text
does it assert something about
Experience,
subject,
account,
session,
state,
journey,
facts,
evaluation,
ownership,
viewer?
```

Si hace lo segundo:

```text
UI-local authority alone is insufficient
```

salvo evidencia específica.

Este control debe explicar por qué:

```text
"Mi aventura"
```

puede ser distinto de:

```text
"Cuenta/sesión operativa"
```

históricamente.

---

# 23. PRESENTATION TRANSFORMATION QUESTION

Investigar explícitamente el estatus de mappings como:

```text
enabled → "habilitado"
not-enabled → "sin habilitar"
not-enlisted → "sin alistar"
```

y:

```text
evaluation.sufficiency = established
→ completion sentence
```

Preguntar si son:

```text
derived representation
```

o:

```text
editorial declaration hidden in code
```

No decidir por su ubicación en el projector.

Esta cuestión puede falsar una clasificación demasiado simple.

---

# 24. AUTHORITY VS CONTENT DISTINCTION

Para cada caso distinguir:

```text
authority to say something
```

de:

```text
exact wording used to say it
```

Ejemplo conceptual:

```text
subjectState=enabled
may authorize the claim that it is enabled

but may not uniquely determine
the Spanish wording "Estado: habilitado"
```

Registrar esta diferencia.

No crear localización/content architecture en S36.

---

# 25. AUTHORITY COMPOSITION

Cuando una frase combine fuentes distintas, representar explícitamente la composición.

Ejemplo:

```text
"Cuenta de " + member.name
```

No esconderla bajo una única categoría.

Registrar:

```text
fragment A authority
fragment B authority
combined claim
whether combination introduces extra semantics
```

La combinación misma puede necesitar autoridad.

---

# 26. OUTPUT — PROVENANCE GRAPH

Además de la matriz, producir un grafo textual o Mermaid equivalente:

```text
source authority
→ transformation/declaration
→ read model/runtime
→ App surface
```

para las principales relaciones H25–H35.

El grafo debe mostrar múltiples fuentes convergiendo en una superficie cuando ocurra.

No crear una nueva arquitectura de runtime a partir del grafo.

Es documentación de evidencia.

---

# 27. OUTPUT — PROVISIONAL MODEL

Sólo después del análisis, producir un modelo provisional de autoridad.

Puede resultar:

```text
four modes supported
```

o:

```text
three modes + exceptions
```

o:

```text
proposed stratification falsified
```

No prescribir de antemano el resultado.

Si se conserva una clasificación, cada modo debe incluir:

```text
definition
positive examples
counterexamples
boundary conditions
what it must NOT be used to infer
```

---

# 28. PROMOTION GATE

S36 NO puede:

```text
create ADR
modify Architecture v0.5
modify TES
modify PSC
create PSC-P02
promote DemoScript
create PresentationBoundary
create PresentationModel
create PresentationRegistry
```

aunque H36 resulte positiva.

Como máximo puede concluir:

```text
CANDIDATE ARCHITECTURAL PRINCIPLE
→ EVIDENCE-BACKED
→ NOT PROMOTED
```

Una sesión posterior deberá decidir expresamente si hay materia suficiente para promoción.

---

# 29. KNOWN UNRESOLVED PRESSURES

Mantener visibles y NO resolver:

```text
fixed navigation link to A

remaining supervision terminology
if any

other App literals from S31 inventory
```

No utilizar su existencia automáticamente para falsar H36 si están fuera del conjunto experimental auditado.

Pero pueden utilizarse como:

```text
challenge probes
```

si ayudan a probar los límites de la clasificación.

---

# 30. TEST-INFRASTRUCTURE OBSERVATION

Registrar separadamente la presión observada en la infraestructura experimental:

```text
historical replay count
archived-source routing
test concurrency/timeouts
instrumentation maintenance
```

S35 observó timeouts bajo concurrencia y PASS serial sin cambio de producto.

No modificar infraestructura en S36.

Clasificar únicamente:

```text
NO MATERIAL PRESSURE
OBSERVED PRESSURE
MATERIAL PRESSURE
```

con evidencia.

No mezclarla con el veredicto semántico de H36.

---

# 31. H36 FALSIFIERS

H36 queda FALSIFIED si:

```text
no coherent provenance classification
can account for the addressed presentation claims
without circular or ad hoc categories
```

o si:

```text
DemoScript must be treated
as factual authority
for any demonstrated case
```

o si:

```text
operational/runtime sources
cannot explain representations
previously classified as derived
```

o si:

```text
semantic metadata / UI-local / operational / editorial
boundaries collapse under existing counterexamples
```

o si:

```text
the same relationship
must be classified differently
only to make the model pass
```

H36 queda SUPPORTED WITH QUALIFICATION si:

```text
a useful, bounded classification survives
the counterexample search
```

aunque existan:

```text
mixed-authority surfaces
transformations
unresolved pressures
```

si están explícitamente explicadas.

---

# 32. OUTPUT

Producir:

```text
session-36-presentation-authority-provenance-stratification-audit.md
```

con al menos:

```text
H35 CONSOLIDATED INPUT

H36 HYPOTHESIS

AUDIT SCOPE

PROVISIONAL AUTHORITY MODES

UNIT OF ANALYSIS

CURRENT SOURCE VERIFICATION

ADDRESSED SURFACE MATRIX

H24 / H26 / H31 FALSIFICATION INPUT

H25 ACTIVITY AUTHORITY ANALYSIS

H27 SUBJECT PRESENTATION ANALYSIS

H28 ACCOUNT PRESENTATION ANALYSIS

H29 STATUS PRESENTATION ANALYSIS

H30 MIXED MESSAGE AUTHORITY ANALYSIS

H32 COMPOSED HEADER AUTHORITY ANALYSIS

H33 SUPERVISION SUBJECT ANALYSIS

H34 SUPERVISION SESSION ANALYSIS

H35 EXPERIENCE NAME ANALYSIS

UI-LOCAL COPY ANALYSIS

PRESENTATION TRANSFORMATION ANALYSIS

AUTHORITY / WORDING DISTINCTION

AUTHORITY COMPOSITION ANALYSIS

COUNTEREXAMPLE SEARCH

PROPOSITION P1–P6 RESULTS

PROVENANCE GRAPH

PROVISIONAL AUTHORITY MODEL

CURRENT UNRESOLVED PRESSURES

TEST-INFRASTRUCTURE OBSERVATION

FALSIFICATION ANALYSIS

H36 VERDICT

ARCHITECTURAL CONSEQUENCE

SEMANTIC CONSEQUENCE

PROMOTION GATE STATUS

WHAT H36 DOES NOT PROVE

REMAINING PRESSURES
```

---

# 33. FINAL VERDICT FORMAT

Concluir únicamente con una matriz equivalente a:

```text
H36
→ SUPPORTED WITH QUALIFICATION
  / FALSIFIED
  / INCONCLUSIVE

PRESENTATION AUTHORITY CLASSIFICATION
→ supported / qualified / falsified

UI-LOCAL CONVENTION
→ status

DECLARED DOMAIN / ARTIFACT DATA
→ status

OPERATIONAL / DERIVED AUTHORITY
→ status

EXPLICIT SITUATED EDITORIAL DECLARATION
→ status

MIXED-AUTHORITY SURFACES
→ supported / problematic

DEMO SCRIPT UNIVERSAL OWNERSHIP
→ NOT SUPPORTED / supported-invalidly

APP SEMANTIC AUTHORITY
→ NOT SUPPORTED / supported-invalidly

CANDIDATE ARCHITECTURAL PRINCIPLE
→ evidence-backed / insufficient
→ NOT PROMOTED

TEST-INFRASTRUCTURE PRESSURE
→ status

NEXT MATERIAL PRESSURE
→ observed but NOT SELECTED
```

No abrir H37 automáticamente.

---

# 34. METHODOLOGICAL GUARDRAIL

Preservar:

```text
where text lives
!=
where authority comes from

where authority comes from
!=
where wording must live

authority to make a claim
!=
exact wording of the claim

one field
!=
one authority

one component
!=
one authority

one visual surface
!=
one authority

presentation
!=
editorial declaration

presentation
!=
factual authority

derivation
!=
inference without authority

declaration
!=
truth

UI-local copy
!=
permission to assert domain meaning

recurrence
!=
ownership

classification
!=
architecture

evidence-backed principle
!=
promoted principle
```

El objetivo de S36 es intentar destruir nuestra explicación actual de la procedencia presentacional antes de convertirla en arquitectura.

Si sobrevive, habremos ganado una base de promoción.

Si falla, habremos descubierto qué categoría o relación todavía no comprendemos.
