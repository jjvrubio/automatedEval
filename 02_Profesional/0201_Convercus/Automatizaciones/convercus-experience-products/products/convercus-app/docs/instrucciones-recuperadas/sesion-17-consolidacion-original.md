# Consolidación de la Sesión 17 — Composición de evidencia entre sujetos acotada por autoridad

Continúa el proyecto existente:

`Convercus Demo Factory / Convercus Experience Products`

Repositorio:

`02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`

No empieces desde cero.

Esta sesión es exclusivamente de **consolidación epistemológica y documental** de la Sesión 17.

No diseñes todavía la Sesión 18.

No añadas nueva arquitectura de producto.

No modifiques todavía el Contrato semántico de producto.

---

# 1. Propósito de la consolidación

La Sesión 17 experimentó la primera frontera cooperativa:

```text
authority-bounded cross-subject evidence composition
```

La operación observada fue:

```text
joint admissibility
```

A efectos de documentación en español, interpretar estos términos como:

```text
composición de evidencia entre sujetos acotada por autoridad

admisibilidad conjunta
```

La Sesión 17 produjo evidencia de que:

```text
atribución de Evidence
≠
admisibilidad conjunta

admisibilidad conjunta
≠
evaluación de suficiencia

contexto situado compartido
≠
autoridad para establecer admisibilidad conjunta

pluralidad de sujetos
≠
necesidad de Group
```

La consolidación debe determinar:

1. qué parte de esos resultados queda respaldada;
2. qué parte permanece local al experimento;
3. qué mecanismos experimentales no deben convertirse en semántica de producto;
4. qué presión real aparece sobre el Contrato semántico de producto;
5. cómo registrar futuras presiones semánticas sin resolverlas prematuramente;
6. qué preguntas deben permanecer abiertas antes de seleccionar la variable de la Sesión 18.

---

# 2. Línea de base vinculante

Mantener:

```text
ADR-001–005
→ ACCEPTED

Architecture v0.5
→ ACTIVE / unchanged
```

La Sesión 16 concluyó:

```text
ADR-006
→ NOT NEEDED

Architecture v0.6
→ NOT NEEDED
```

La Sesión 17 concluyó:

```text
H17
→ SUPPORTED WITH QUALIFICATION

ADR-005
→ ACCEPTED / unchanged

Architecture v0.5
→ ACTIVE / unchanged

new ADR
→ NOT NEEDED

architecture revision
→ NOT NEEDED

Product Semantic Contract
→ REVIEW WARRANTED / unchanged

Group
→ NOT REQUIRED BY THIS EXPERIMENT / UNRESOLVED
```

No reabras estas conclusiones salvo que la consolidación encuentre una contradicción material en la evidencia de la Sesión 17.

---

# 3. Alcance de la evidencia que debe consolidarse

La Sesión 17 mantuvo constante:

```text
K = A AND (B OR C)
```

y demostró experimentalmente:

```text
A@P1
B@P2
+
premisa autoritativa aplicable
        ↓
admisibilidad conjunta establecida
        ↓
K(A,B)
        ↓
suficiencia establecida
```

También demostró:

```text
A@P1
B@P2
+
contexto compartido
-
premisa autoritativa aplicable
        ↓
admisibilidad conjunta
no puede establecerse actualmente
```

Los controles incluyeron:

* ausencia de autoridad aplicable;
* ámbito incorrecto;
* sujetos incorrectos;
* misma reserva sin autoridad semántica;
* evidencia adicional sin autoridad suficiente.

Preservar:

```text
ausencia de autoridad suficiente
≠
prohibición

no puede establecerse actualmente
≠
falso
≠
imposible
≠
fracaso
```

---

# 4. Resultado central que debe consolidarse

Consolidar H17 como:

```text
SUPPORTED WITH QUALIFICATION
```

La cualificación principal es:

> La competencia de la premisa autoritativa se asumió por construcción dentro del artefacto experimental.

Por tanto, la Sesión 17 demuestra:

```text
una premisa autoritativa y aplicable
puede acotar legítimamente
la admisibilidad conjunta
de Evidence atribuida
a sujetos distintos
```

pero NO demuestra:

```text
cómo se origina esa autoridad
cómo se acredita
cómo se revoca
cómo se resuelven conflictos entre autoridades
cuántas evaluaciones puede gobernar
cuántas premisas puede requerir una evaluación
qué forma productiva debe adoptar
```

No promover:

```text
AuthoritativePremise
```

como componente de arquitectura.

---

# 5. Separación epistemológica consolidable

Evaluar y, si la evidencia lo permite, consolidar con alcance explícitamente experimental:

```text
atribución de Evidence
≠
admisibilidad conjunta
```

```text
admisibilidad conjunta
≠
suficiencia
```

```text
hecho contextual autoritativo
≠
autoridad sobre la consecuencia semántica inferida
```

Ejemplo:

```text
P1 y P2 pertenecen a la misma reserva
```

puede ser un hecho acreditado por una fuente competente.

Pero:

```text
sus Evidence pueden entrar juntas
en una evaluación de suficiencia
```

es una afirmación distinta que requiere autoridad adecuada para esa consecuencia.

Consolidar, por tanto:

```text
autoridad sobre un hecho
≠
autoridad sobre toda inferencia
derivada de ese hecho
```

Tratar esta formulación como consecuencia analítica de ADR-005, no como nuevo ADR.

---

# 6. Pluralidad de sujetos y Group

La Sesión 17 logró ejecutar la frontera cooperativa sin:

* identidad colectiva;
* membership;
* persistencia colectiva;
* Evidence colectiva;
* suficiencia colectiva;
* outcome colectivo.

Consolidar únicamente:

```text
Group
→ NOT REQUIRED BY H17
```

Mantener:

```text
Group
→ UNRESOLVED
```

No concluir:

```text
Group is unnecessary
```

en términos generales.

La evidencia solo permite afirmar:

> La identidad colectiva no es necesaria para resolver el problema específico de admisibilidad conjunta estudiado en la Sesión 17.

No promover:

* Group;
* GroupParticipation;
* collective participation;
* membership;
* collective Evidence;
* collective outcome.

---

# 7. Vigilancia crítica 1 — ubicación de `bookingRef`

Prestar especial atención a este punto.

La implementación experimental añadió:

```text
bookingRef
```

dentro de:

```text
CrossSubjectMarkerEvidence
```

Esto NO debe consolidarse como semántica de Evidence.

La cuestión permanece abierta:

```text
¿la relación con una reserva
es un hecho intrínseco
sobre la propia Evidence?

o

¿es una relación contextual
utilizada cuando esa Evidence
se evalúa en un ámbito determinado?
```

La Sesión 17 no resolvió esta cuestión.

Clasificar:

```text
bookingRef placement
→ EXPERIMENTAL
→ NOT PROMOTED
→ UNRESOLVED
```

La consolidación debe impedir explícitamente que futuras sesiones interpreten:

```text
CrossSubjectMarkerEvidence.bookingRef
```

como contrato semántico de producto.

Preservar conceptualmente:

```text
Evidence A@P1
Evidence B@P2

+

relaciones contextuales situadas

+

premisas autoritativas aplicables
```

sin decidir todavía dónde debe residir estructuralmente la relación con reserva, estancia, propiedad o escenario.

No refactorizar código durante esta consolidación salvo que exista una contradicción material.

---

# 8. Vigilancia crítica 2 — control de sujeto único

La Sesión 17 utilizó:

```text
A@P1
B@P1
```

como control de regresión para demostrar que la extracción de la evaluación K no rompía el comportamiento de la Sesión 15.

Este control NO demuestra:

```text
mismo sujeto
→ Evidence siempre conjuntamente admisible
```

La ausencia de una premisa de admisibilidad entre sujetos en ese control significa únicamente:

> La Sesión 17 no introduce retroactivamente un nuevo requisito de cooperación en el experimento de sujeto único de la Sesión 15.

Consolidar expresamente:

```text
same-subject control
→ regression control only
```

No promover:

```text
same subject
→ automatic admissibility
```

como regla de producto.

La admisibilidad general de Evidence perteneciente al mismo sujeto NO fue la variable estudiada.

Mantener esa cuestión fuera del alcance de la consolidación.

---

# 9. Vigilancia crítica 3 — forma de `AuthoritativePremise`

La implementación utilizó experimentalmente:

```text
AuthoritativePremise
```

con elementos como:

```text
identity
provenance
scope
covered subjects
```

Todo ello permanece como:

```text
PROVISIONAL EXPERIMENTAL SHAPE
NOT PROMOTED
```

En particular:

```text
coveredSubjects
```

no debe convertirse en:

```text
general semantic model
for cooperative authority
```

La autorización futura podría depender de relaciones, condiciones, delegación, invitación, pertenencia contextual u otros mecanismos todavía desconocidos.

No asumir:

```text
premisa autoritativa
=
lista explícita de sujetos autorizados
```

Preservar:

```text
authority accreditation
→ UNRESOLVED

authority revocation
→ UNRESOLVED

authority conflict
→ UNRESOLVED

authority-premise/evaluation cardinality
→ UNRESOLVED
```

---

# 10. Cardinalidad entre premisas y evaluaciones

La Sesión 17 utilizó una única premisa opcional por conveniencia experimental.

Esto no demuestra:

```text
1:1
1:N
N:1
N:N
```

entre:

```text
premisas autoritativas
↔
contextos de evaluación
```

Consolidar explícitamente:

```text
cardinality
→ UNRESOLVED
```

No permitir que la forma de la función experimental sea citada posteriormente como evidencia de cardinalidad semántica.

---

# 11. Presión sobre el Contrato semántico de producto

La Sesión 16 activó el disparador de revisión:

```text
primer experimento cooperativo
→ revisión del Contrato semántico de producto
```

La Sesión 17 ya constituye ese primer experimento.

Por tanto:

```text
trigger
→ REACHED
```

y:

```text
Product Semantic Contract
→ REVIEW NOW
```

La consolidación NO debe modificar todavía el contrato.

Debe identificar formalmente la presión observada.

La presión actualmente respaldada es:

```text
atribución del sujeto de Evidence
≠
ámbito en el que esa Evidence
puede participar en una evaluación
```

La Sesión 17 demostró que:

```text
A@P1
B@P2
```

pueden conservar sus atribuciones individuales y, bajo autoridad competente, participar en una misma evaluación.

Por tanto, queda tensionada cualquier simplificación equivalente a:

```text
un sujeto
=
un ámbito de participación
=
un ámbito de evaluación
```

No concluir todavía cuál debe ser la solución.

---

# 12. No elegir aún la solución semántica

La consolidación NO debe promover:

```text
ParticipationScope
EvaluationScope
ContributionScope
CollectiveParticipation
Collaboration
Group
Membership
```

ni equivalentes.

El hecho observado es anterior a la solución conceptual.

La consolidación debe distinguir:

```text
presión observada
```

de:

```text
concepto que eventualmente
podría resolver esa presión
```

Preservar el método:

```text
evidencia
→ presión semántica
→ revisión
→ hipótesis
→ experimento
→ eventual promoción
```

No:

```text
evidencia
→ nuevo concepto
→ arquitectura
```

---

# 13. Crear un registro de presiones semánticas

A partir de esta consolidación, crear o introducir en la documentación un mecanismo ligero de seguimiento denominado:

```text
Registro de presiones sobre el Contrato semántico de producto
```

No convertirlo en componente de software.

No crear repositorio técnico, servicio, esquema de persistencia ni API.

Debe ser únicamente una disciplina documental.

Cada presión registrada debe contener como mínimo:

```text
Identificador
Fuente experimental
Distinción observada
Evidencia disponible
Autoridad afectada
Estado epistemológico
Qué NO demuestra
Preguntas abiertas
Riesgo de promoción prematura
Condición para nueva experimentación
Condición para posible refinamiento del contrato
```

Para la presión surgida en Sesión 17, registrar algo equivalente a:

```text
PSC-P01
```

con:

```text
Fuente:
Session 17

Presión:
atribución del sujeto de Evidence
≠
ámbito de contribución/evaluación

Evidencia:
Evidence atribuida a P1 y P2
puede entrar en una misma evaluación
sin borrar las atribuciones individuales
y sin crear Group.

Estado:
SUPPORTED WITH QUALIFICATION
como presión observada.

No demuestra:
qué es ParticipationScope;
qué es EvaluationScope;
que deba existir Group;
que deba existir CollectiveParticipation;
que participant y contributor sean entidades distintas;
quién es el sujeto del claim;
quién es beneficiario de consecuencias posteriores.

Condición de futura promoción:
evidencia adicional que demuestre
que el contrato actual no puede expresar
correctamente un comportamiento necesario
sin introducir una nueva distinción semántica.
```

---

# 14. El registro debe prepararse para nuevas presiones

No asumir que PSC-P01 será la única tensión.

El registro debe poder recibir futuras presiones provenientes de:

* cooperación;
* ayuda externa;
* contributor frente a participant;
* identidad de contribución;
* claim derivado;
* ámbito del claim;
* solución reconocida;
* incentivos;
* orden y dependencia entre pistas;
* latencia;
* ambigüedad;
* conflicto;
* autoridad;
* posible participación colectiva;
* futuras diferencias entre Experience Definition y realización de producto.

Pero no registrar como presión confirmada una cuestión que todavía solo sea una posibilidad.

Distinguir:

```text
presión observada
```

de:

```text
frontera potencial futura
```

---

# 15. Evitar acumulación silenciosa de presión semántica

La finalidad del registro es impedir este patrón:

```text
experimento n
→ pequeña excepción local

experimento n+1
→ otra excepción local

experimento n+2
→ otra excepción local

        ↓

contrato semántico implícitamente obsoleto
sin decisión explícita
```

En su lugar:

```text
nueva evidencia
        ↓
¿presiona al contrato?
        ↓
sí
        ↓
registrar presión
        ↓
acumular evidencia
        ↓
revisión explícita
        ↓
mantener / refinar / rechazar
```

La consolidación debe indicar que una presión acumulada no modifica por sí sola el contrato.

---

# 16. Umbral para modificar el Contrato semántico de producto

No establecer un umbral numérico.

Definir un criterio epistemológico.

Una modificación del contrato debería considerarse cuando exista evidencia suficiente de que:

```text
1. una distinción semántica es necesaria
para representar correctamente
comportamientos de producto legítimos;

2. la distinción no puede permanecer
como simple detalle de Scenario;

3. no es únicamente consecuencia
de un artefacto experimental;

4. su ausencia produce ambigüedad,
contradicción o pérdida semántica recurrente;

5. existe suficiente evidencia
para definir la distinción
sin inventar ontología adicional.
```

No modificar el contrato simplemente porque:

```text
un experimento utiliza una nueva propiedad
```

o:

```text
dos sesiones encuentran la misma palabra útil
```

---

# 17. Diferenciar presión semántica y presión arquitectónica

La consolidación debe preservar:

```text
presión sobre el Contrato semántico de producto
≠
necesidad de nueva arquitectura
```

La Sesión 17 es ejemplo de ello:

```text
presión semántica
→ sí

nueva responsabilidad arquitectónica
→ no demostrada
```

Por tanto:

```text
ADR-005
→ ACCEPTED / unchanged

Architecture v0.5
→ ACTIVE / unchanged
```

La revisión del contrato no debe provocar automáticamente:

* nuevo ADR;
* nueva capa;
* nuevo agregado;
* nuevo servicio;
* nueva persistencia.

---

# 18. No promover aún una entidad colectiva

Mantener:

```text
Group identity
→ UNRESOLVED

membership
→ UNRESOLVED

collective participation
→ UNRESOLVED

group Evidence
→ UNRESOLVED

group sufficiency
→ UNRESOLVED

group outcome
→ UNRESOLVED
```

La presión sobre el contrato NO debe resolverse mediante Group por defecto.

Preservar:

```text
evaluación compartida
≠
sujeto colectivo demostrado
```

---

# 19. No resolver aún el sujeto del claim

La Sesión 17 produjo una nueva cuestión:

```text
cuando A@P1 y B@P2
son conjuntamente admisibles
y K establece suficiencia,

¿de qué o de quién habla
la afirmación derivada?
```

No resolverla en esta consolidación.

Registrar separadamente:

```text
claim subject / referent
→ UNRESOLVED
```

En español:

```text
sujeto o referente
de la afirmación derivada
→ NO RESUELTO
```

No identificar automáticamente:

```text
sujeto del claim
=
P1
```

ni:

```text
=
P2
```

ni:

```text
=
P1 + P2
```

ni:

```text
=
Group
```

ni:

```text
=
beneficiary
```

---

# 20. Separar sujeto del claim, ámbito y beneficiario

Registrar como fronteras distintas:

```text
sujeto/referente de la afirmación
≠
ámbito de la afirmación
≠
beneficiario de una consecuencia posterior
```

No usar `beneficiary` como nombre de la siguiente frontera experimental.

En español:

```text
beneficiario
```

debe reservarse para consecuencias posteriores, potencialmente relacionadas con:

* incentivo;
* recompensa;
* elegibilidad;
* derecho;
* resultado comercial.

Estas materias permanecen fuera de la consolidación.

---

# 21. No seleccionar todavía la Sesión 18

La consolidación debe terminar sin diseñar la Sesión 18.

Debe dejar candidatas separadas, como mínimo:

```text
A. sujeto/referente de la afirmación derivada

B. ámbito de la afirmación derivada

C. participant/contributor distinction

D. external actor assistance

E. authority accreditation

F. authority conflict / multiple premises
```

No decidir todavía cuál será la siguiente.

La decisión debe tomarse después de revisar:

```text
PSC-P01
```

y el Contrato semántico de producto actual.

---

# 22. Revisión del Contrato semántico de producto

Durante esta consolidación:

1. localizar el Contrato semántico de producto vigente;
2. identificar exactamente qué formulaciones presuponen o favorecen una perspectiva individual;
3. comparar esas formulaciones con la evidencia de Sesión 17;
4. NO editar el contrato;
5. documentar la tensión con referencias concretas;
6. indicar si la evidencia actual produce:

```text
NO PRESSURE

OBSERVED PRESSURE

REFINEMENT CANDIDATE

CONTRADICTION
```

La clasificación esperable, salvo evidencia contraria, es:

```text
OBSERVED PRESSURE
```

No elevar a:

```text
REFINEMENT CANDIDATE
```

solo porque se haya activado la revisión.

---

# 23. Criterio para `REFINEMENT CANDIDATE`

Solo clasificar una presión como:

```text
REFINEMENT CANDIDATE
```

cuando exista evidencia suficiente para sostener:

> El contrato necesita una nueva distinción semántica concreta y existe evidencia suficiente para expresar esa distinción sin inventar significado adicional.

Actualmente Sesión 17 demuestra una tensión, pero no determina todavía si la solución es:

* nuevo concepto;
* nueva relación;
* nuevo ámbito;
* nueva cualificación de participación;
* o ninguna nueva entidad.

Por tanto, evitar promoción prematura.

---

# 24. Documento de consolidación requerido

Crear:

`docs/experiments/session-17-consolidation-authority-bounded-cross-subject-evidence-composition.md`

o la ubicación equivalente establecida por el repositorio.

El documento debe incluir:

## A. Veredicto sobre H17

```text
H17
→ SUPPORTED WITH QUALIFICATION
```

con explicación de la cualificación.

## B. Evidencia consolidada

Qué separaciones quedan respaldadas y con qué alcance.

## C. Qué NO demuestra Sesión 17

Enumerar explícitamente las inferencias no autorizadas.

## D. Cuarentena de artefactos experimentales

Como mínimo:

```text
AuthoritativePremise
coveredSubjects
bookingRef placement
single optional premise
outcome literals
cross-subject fixture shapes
```

Clasificarlos como:

```text
NOT PROMOTED
```

o:

```text
UNRESOLVED
```

según corresponda.

## E. Control de sujeto único

Explicar que:

```text
A@P1 + B@P1
```

fue un control de regresión y no evidencia de admisibilidad universal intra-sujeto.

## F. Relación con ADR-005

Determinar si la Sesión 17:

* contradice;
* extiende evidencia;
* requiere nueva responsabilidad.

Resultado esperado si no surge contradicción:

```text
supporting evidence for ADR-005
```

## G. Impacto arquitectónico

Evaluar:

```text
ADR-005
Architecture v0.5
nuevo ADR
nueva versión arquitectónica
```

## H. Revisión del Contrato semántico de producto

Citar las formulaciones actuales relevantes y describir la presión observada.

No modificar el contrato.

## I. Registro de presiones semánticas

Crear o actualizar el registro e introducir:

```text
PSC-P01
```

## J. Fronteras que permanecen abiertas

Incluir:

```text
contribution identity
participant/contributor distinction
claim subject/referent
claim scope
Group identity
membership
collective participation
authority accreditation
authority revocation
authority conflict
authority-premise/evaluation cardinality
external actor assistance
solution recognition
incentive eligibility
ordered/enabling clues
latency
ambiguity
identity confusion
TES Event recognition
real API contracts
```

Cuando el término disponga de equivalente español estable en el documento, utilizarlo.

Los nombres de tipos o identificadores de código pueden conservarse literalmente.

## K. Candidatas a siguiente frontera

Enumerarlas sin seleccionar una.

## L. Veredicto final

Incluir:

```text
H17 → ?

ADR-005 → ?

Architecture v0.5 → ?

new ADR → ?

architecture revision → ?

Product Semantic Contract → ?

PSC-P01 → ?

Group → ?

bookingRef placement → ?

same-subject control interpretation → ?

Recommended immediate next action → ?
```

---

# 25. Veredicto esperado salvo contradicción

Si la inspección no descubre evidencia nueva que contradiga el informe de Sesión 17, la consolidación debería aproximarse a:

```text
H17
→ SUPPORTED WITH QUALIFICATION

ADR-005
→ ACCEPTED / unchanged

Architecture v0.5
→ ACTIVE / unchanged

new ADR
→ NOT NEEDED

architecture revision
→ NOT NEEDED

Product Semantic Contract
→ REVIEWED / OBSERVED PRESSURE / unchanged

PSC-P01
→ OPEN / EVIDENCE-BACKED PRESSURE

Group
→ NOT REQUIRED BY H17 / UNRESOLVED

bookingRef placement
→ EXPERIMENTAL / NOT PROMOTED / UNRESOLVED

same-subject control
→ REGRESSION CONTROL ONLY

AuthoritativePremise shape
→ EXPERIMENTAL / NOT PROMOTED
```

No fuerces estos resultados si la evidencia contradice alguno.

---

# 26. Prohibiciones

No construir:

* Group;
* ParticipationScope;
* EvaluationScope;
* CollectiveParticipation;
* Contributor;
* Participant;
* authority service;
* authority registry;
* semantic-pressure registry como software;
* new aggregate;
* persistence;
* API;
* TES Event recognition;
* incentive model;
* solution recognition.

No modificar:

* ADR-005;
* Architecture v0.5;
* Product Semantic Contract;

salvo contradicción explícita y documentada.

Si aparece una contradicción:

```text
STOP
```

y documentarla.

---

# 27. Resultado metodológico buscado

La consolidación debe dejar el proyecto preparado para que futuras sesiones puedan distinguir:

```text
nuevo hallazgo experimental
```

de:

```text
nueva presión semántica
```

de:

```text
necesidad de refinar
el Contrato semántico de producto
```

de:

```text
necesidad de nueva arquitectura
```

Preservar siempre:

```text
hallazgo
≠
promoción
```

```text
presión
≠
refinamiento
```

```text
refinamiento semántico
≠
arquitectura nueva
```

La finalidad de la consolidación no es cerrar las preguntas cooperativas.

Es evitar que las próximas respuestas locales degraden silenciosamente la coherencia semántica global del producto.

Procede con inspección, consolidación documental y registro de la primera presión semántica observada.
