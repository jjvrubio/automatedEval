# Apertura de la frontera cooperativa: de la atribución a la co-admisibilidad

He tomado la consolidación de Session 16 como baseline vinculante. Por tanto, no reabrimos ADR-005, no creamos ADR-006, Architecture v0.5 permanece activa, y no modificamos todavía el Contrato semántico de producto. Session 16 concluyó precisamente que la evidencia distribuida de Session 15 sigue siendo una instancia de evaluación contextual gobernada por ADR-005 y que la siguiente frontera legítima es la cooperación entre varios sujetos.

Hay, sin embargo, una corrección conceptual que considero importante hacer **antes de redactar Session 17**:

> La nueva variable experimental no debería llamarse primariamente `cross-subject evidence attribution`.

Propongo una formulación más precisa:

```text
cross-subject evidence co-admissibility
```

o, de manera t==odavía más explícita==:

```text
authority-bounded cross-subject evidence composition
```

La razón es que **atribución** y **composición** son problemas diferentes.

------

## 1. Qué significa realmente «Evidence producida por sujetos distintos»

El enunciado aparentemente sencillo:

```text
P1 contributes A
P2 contributes B
```

contiene varias afirmaciones que todavía no tenemos derecho a equiparar.

En particular:

```text
P1 produced A
≠
A is attributed to P1
≠
P1 performed the observed action
≠
P1 submitted the record
≠
P1 validated the record
≠
P1 is a participant
≠
P1 is an eligible contributor
```

Esto importa mucho en Hospitality.

Imaginemos una pista física de Treasure Hunt. Un niño encuentra el objeto, el padre escanea el QR con su teléfono, el sistema atribuye la actividad a un miembro del programa y un empleado del hotel valida posteriormente la acción. ¿Quién «produjo» la Evidence?

No tenemos respuesta, y **no la necesitamos todavía**.

Session 15 fue deliberadamente mucho más modesta: utilizó una `subjectRef` estable sin decidir si representaba loyalty member, booking owner, account, device holder, TES participant o ExperienceParticipation.

Por tanto, para Session 17 deberíamos evitar el verbo causal *produce* salvo como lenguaje informal. La formulación experimental más limpia sería:

```text
Evidence A is attributed to P1
Evidence B is attributed to P2
P1 != P2
```

Eso nos proporciona exactamente una novedad respecto de Session 15 sin obligarnos a resolver todavía qué es ontológicamente P1.

------

# 2. La verdadera frontera está entre atribución y suficiencia

Hasta ahora teníamos aproximadamente:

```text
Evidence A
Evidence B
      ↓
     K
      ↓
SufficiencyClaim
```

Session 15 demostró que K, y no el mero número de records, hace que A+B pueda resultar suficiente.

Pero el escenario cooperativo introduce una operación previa:

```text
A attributed to P1
B attributed to P2

        ↓

ARE A AND B
JOINTLY ADMISSIBLE?

        ↓

if yes:
evaluate K(A,B)
```

Ahí está la nueva frontera. ==(¿Se refiere al grupo de actores?)==

Propongo distinguir analíticamente tres relaciones:

```text
1. Attribution

Evidence A → P1
Evidence B → P2
2. Co-admissibility

May A@P1 and B@P2
be premises of the same evaluation?
3. Sufficiency

Given the admissible Evidence,
does K establish the derived claim?
```

Y debemos preservar rigurosamente:

```text
attribution
≠
co-admissibility
≠
sufficiency
```

Esta separación me parece la consecuencia epistemológica más importante de la transición de Session 15 a Session 17. ==(Distincion clara, estoy de acuerdo)==

------

# 3. Un modelo cooperativo mínimo

No propongo todavía ningún modelo de dominio.

Propongo solamente una **notación experimental**:

```text
A@P1
B@P2
```

Significa únicamente:

> Evidence A está atribuida a P1 y Evidence B está atribuida a P2.

Luego introducimos, como premisa experimental controlada, algo conceptualmente equivalente a:

```text
C(P1, P2, S, K)
```

donde `C` no es un objeto de arquitectura ni un schema, sino una abreviatura para:

> Existe una premisa competente, dentro del scope S, que autoriza a considerar conjuntamente Evidence atribuida a P1 y P2 para la evaluación K.
>
> (==Es posibke que sea necearia determinar una frontera nítida entre evaluación   y la premisa competente ‘C’. Además,  más adelante habría que estar atento a relaciónes N:N entre ambas.== )

Entonces:

```text
A@P1
B@P2
C(P1,P2,S,K)

        ↓

A and B are jointly admissible
for evaluation K in S

        ↓

K(A,B)

        ↓

possible SufficiencyClaim
```

Fíjate en lo que **no aparece**:

```text
Group
GroupId
GroupMembership
GroupParticipation
SharedEvidence
EvidenceSet
GroupOutcome
```

No necesitamos ninguno para hacer la primera pregunta falsable.

------

# 4. Lo que autoriza la composición no puede provenir de la Evidence

Esta es, creo, la extensión natural de ADR-005.

==(Estamos usando el término ‘composión’ que puede originar confusiones de dominio: premisa, experiencias, journeys,…) Atento.==

ADR-005 ya establece:

```text
factual Evidence
≠
derived contextual claim
```

y Architecture v0.5 declara que el claim derivado queda limitado por autoridad, scope y madurez de las premisas que convergen en la evaluación.

Ahora podemos aplicar exactamente el mismo razonamiento una capa antes.

El hecho:

```text
A@P1
```

no contiene:

```text
A may contribute together with B@P2
```

De igual modo:

```text
same booking
same stay
same room
same property
same Treasure Hunt
```

son, en el mejor de los casos, **facts o situated context**.

No contienen por sí mismos la norma:

```text
Evidence may be shared across subjects
```

Por tanto:

```text
common context
≠
composition authority
```

Esta desigualdad es crucial porque evita una forma especialmente peligrosa de **authority laundering**.

Por ejemplo:

```text
P1 and P2 have the same booking
```

puede estar acreditado perfectamente por un PMS.

Pero de ello no se sigue:

```text
P1's evidence may satisfy
a criterion together with P2's evidence
```

El PMS podría ser autoridad competente sobre reservas y completamente incompetente para definir las reglas de cooperación de una Experience.

------

# 5. Evaluación de las autoridades candidatas

Ahora podemos reconsiderar las hipótesis que proponía la instrucción.

### Same Hunt participation

Es informativa, pero no parece suficiente por sí sola.

Dos personas podrían participar simultáneamente en el mismo Hunt y competir individualmente.

Por tanto:

```text
same Hunt
↛
cross-subject composition
```

salvo que exista otra premisa que dé ese significado a la participación.

### Shared objective

Todavía más débil.

Dos individuos pueden perseguir exactamente el mismo objetivo sin cooperar.

```text
shared objective
↛
shared evidence
```

### Common booking, room, property o stay

Son buenas premisas contextuales y podrían ayudar a delimitar scope.

Pero no autorizan cooperación.

```text
same booking
→ contextual relation

same booking
↛
composition authority
```

### Invitation

Más interesante.

Una invitación expresa una relación intencional entre sujetos. Pero incluso aquí debemos evitar una inferencia prematura:

```text
invitation fact
≠
authorized evidence composition
```

Para que la invitación tenga ese efecto debería existir una premisa de producto que diga que **esa clase de invitación**, emitida por un sujeto competente y dentro de determinado scope, autoriza una cooperación determinada.

### Delegation

Conceptualmente todavía más fuerte, porque puede otorgar una facultad.

Pero abre inmediatamente preguntas sobre dirección, autoridad del delegante, alcance y revocación.

Sería probablemente una variable posterior.

### Membership

Podría justificar composición, pero introducirla ahora casi equivale a empezar construyendo aquello que queremos descubrir.

Además:

```text
membership
≠
Group necessarily
```

y tampoco sabemos todavía si membership sería TES, producto o simplemente configuración de Scenario.

### Explicit collaboration relation

==Es, por ahora, mi candidato preferido para el experimento.== 

No porque debamos promover `Collaboration` como concepto, sino porque podemos **estipular localmente en el fixture**una premisa competente:

```text
within scope S,
Evidence attributed to P1 and P2
may be jointly considered for K
```

Eso prueba exactamente la variable que nos interesa sin pretender haber descubierto qué mecanismo productivo la originará finalmente.

------

# 6. La Authority Frontier que propongo

Podemos representar provisionalmente la frontera así:

```text
Neutral factual Evidence
A@P1       B@P2
      \     /

       X
       │
       │ cross-subject composition
       │ NOT YET AUTHORIZED
       │
       ▼

Authoritative scoped
composition premise
       │
       ▼

joint admissibility
       │
       ▼

sufficiency evaluation K
       │
       ▼

derived claim
```

El punto `X` es la nueva **Authority Frontier**.

Y contiene una propiedad muy importante:

```text
absence of composition authority
≠
prohibition of composition
```

Exactamente como aprendimos anteriormente:

```text
insufficient knowledge
≠
negative determination
```

Si no poseemos una premisa competente que autorice P1+P2, la conclusión debe ser algo conceptualmente equivalente a:

```text
cross-subject composition
cannot currently be established
```

No:

```text
P1 and P2 cannot cooperate
```

Esto preserva el carácter open-world de ADR-005.

------

# 7. No necesitamos `Group`

Por ahora, mi conclusión es bastante fuerte:

```text
Group
→ NOT REQUIRED FOR FIRST COOPERATIVE EXPERIMENT
```

Y la razón no es que los grupos no existan.

Es que la pregunta de Session 17 puede contestarse completamente sin identidad colectiva.

Supongamos:

```text
P1 → A
P2 → B
```

y existe una premisa scoped que autoriza su composición.

Eso basta para preguntar si A+B pueden alimentar K.

No necesitamos responder:

```text
What is the group called?
When was it created?
Who owns it?
Who joins it?
Who leaves it?
Does it persist after the stay?
Does it possess Evidence?
Does it receive a Result?
```

Introducir `Group` ahora convertiría una relación en una entidad antes de demostrar que necesita identidad o lifecycle.

Es exactamente el mismo riesgo que evitamos con `EvidenceSet`:

```text
multiple Evidence
≠
EvidenceSet aggregate
```

Ahora debemos preservar:

```text
multiple cooperating subjects
≠
Group aggregate
```

El concepto `Group` empezaría a ser justificable cuando aparecieran propiedades que **no pudiéramos explicar satisfactoriamente mediante relaciones scoped entre sujetos**: identidad colectiva estable, membership mutable, lifecycle propio, autorización colectiva persistente, ownership, policies comunes, claims dirigidos al colectivo o resultados cuya unidad semántica sea el colectivo.

Hasta que alguno de esos elementos sea necesario:

```text
Group
→ UNRESOLVED
```

------

# 8. El punto más interesante: participant y contributor podrían no ser entidades diferentes

Aquí veo una oportunidad de evitar overarchitecture.

El contrato semántico podría necesitar eventualmente distinguir:

```text
participant
```

de:

```text
contributor
```

pero **eso no significa que debamos tener `Participant` y `Contributor` como entidades**.

Podrían ser roles relativos.

Por ejemplo:

```text
P1 participates in scope S

P1 contributes Evidence A
```

y:

```text
P2 participates in scope S

P2 contributes Evidence B
```

La misma identidad puede ocupar distintas relaciones.

Incluso podría darse posteriormente:

```text
P3 contributes Evidence C
```

sin que P3 sea necesariamente participante, por ejemplo si P3 fuese un empleado que certifica una observación. No afirmo que ese sea el modelo correcto; señalo precisamente por qué sería prematuro identificar:

```text
evidence subject
=
participant
=
contributor
```

Session 15 no lo resolvió, y Session 17 tampoco necesita resolverlo completamente.

==(Atención: esto podria descartar ayudas. Por ejemplo, un empleado de hotel puede aconsejar, dar pistas. Aunque sea un actor externo y así debe ser considerado frente al huésped/es.)==

------

# 9. Tensión real sobre el Contrato semántico de producto

Architecture v0.5 todavía presenta a Convercus App fundamentalmente desde la perspectiva de una **«participación individual»**.

Esto tiene una tensión real con el material comercial previo.

En Aventura Familiar la fuente comercial ya habla de «familia/grupo», niños/participantes y «participación compartida», pero el propio análisis de Session 10 dejó explícitamente como ambigua la unidad individual/grupal.

Eso es importante.

Significa que el experimento cooperativo no está inventando gratuitamente una complejidad: está alcanzando una ambigüedad que **ya estaba presente en la intención de producto**, aunque la fuente comercial no tenga autoridad para resolverla.

La simplificación histórica:

```text
one participation
→ one individual
```

puede resultar insuficiente.

Pero todavía no podemos sustituirla por:

```text
participation
→ individual or group
```

porque eso introduciría `group` precisamente antes de demostrar qué necesitamos.

La distinción mínima que actualmente parece emerger es otra:

```text
subject attribution of Evidence
≠
scope in which Evidence may contribute
```

Esta podría ser la auténtica modificación futura del Contrato semántico de producto.

No digo que debamos incorporarla ya. Digo que **es la candidata que Session 17 debería intentar falsificar**.

------

# 10. Mi propuesta de H17

Yo reformularía la hipótesis de la siguiente manera:

```text
H17

Evidence attributed to different subjects
may participate in the same contextual
sufficiency evaluation only when an
authoritative scoped premise makes their
cross-subject composition admissible.

Such admissibility does not by itself require
Group identity, group membership,
group Evidence or group outcome.
```

En español:

> **H17:** La Evidence atribuida a sujetos distintos puede participar conjuntamente en una evaluación contextual de suficiencia cuando existe una premisa competente y scoped que autoriza esa composición; la mera coexistencia situacional de los sujetos no basta, y dicha composición no requiere por sí sola asumir identidad, membership, Evidence u outcome de grupo.

Tiene una virtud: modifica **una sola variable**.

Session 15 queda constante:

```text
A
B
K
unordered evidence
neutral Evidence
sufficiency evaluation
```

La novedad es:

```text
subjectRef(A) != subjectRef(B)
```

y manipulamos únicamente:

```text
availability / applicability
of the scoped composition premise
```

No manipulamos Group, TES Event, solution recognition, ordered clues, incentives ni Progression.

------

# 11. Qué debería intentar falsificar Session 17

Todavía no redactaría el prompt de Codex, pero ya podemos establecer la matriz epistemológica que debería informar ese experimento:

| Caso                   | Atribución  | Contexto                 | Premisa de composición      | Resultado esperado           |
| ---------------------- | ----------- | ------------------------ | --------------------------- | ---------------------------- |
| Control                | A@P1 + B@P1 | mismo scope              | no necesaria para cruce     | Session 15 sigue funcionando |
| Cooperativo autorizado | A@P1 + B@P2 | mismo scope              | autoriza P1/P2 para K       | A+B pueden llegar a K        |
| Sin autoridad          | A@P1 + B@P2 | mismo Hunt/stay/property | ausente                     | composición no establecida   |
| Scope incorrecto       | A@P1 + B@P2 | S1                       | autoridad válida solo en S2 | composición no establecida   |
| Sujetos incorrectos    | A@P1 + B@P3 | S                        | autoridad solo P1/P2        | composición no establecida   |
| Common booking only    | A@P1 + B@P2 | misma booking            | ninguna autoridad adicional | composición no establecida   |

El caso más importante probablemente sea el último.

Porque falsifica:

```text
same booking
→ cooperative evidence
```

sin tener que afirmar su contrario universal.

------

# 12. Estado epistemológico que propongo antes de Session 17

No cambiaría todavía ningún estado aceptado.

Añadiría únicamente, como **hipótesis de análisis previa**, estas separaciones:

```text
evidence attribution
≠
cross-subject co-admissibility
cross-subject co-admissibility
≠
sufficiency
shared situated context
≠
cross-subject composition authority
cross-subject evidence composition
≠
Group
```

Las cuatro permanecen, por ahora, **candidatas a falsificación**, no nuevas decisiones arquitectónicas.

Y mantendría:

```text
participant/contributor distinction
→ UNRESOLVED

Group
→ UNRESOLVED

membership
→ UNRESOLVED

collective participation
→ UNRESOLVED

group sufficiency/outcome
→ UNRESOLVED
```

Esto es coherente con la consolidación de Session 16.

------

## La decisión que sometería ahora a tu crítica

Antes de preparar Session 17, necesito especialmente tus observaciones sobre cinco puntos:

1. **Cambiaría la variable experimental de `cross-subject evidence attribution` a `cross-subject evidence co-admissibility`**, porque la atribución P1/A y P2/B puede fijarse como hecho, mientras la verdadera incógnita es si podemos utilizar A y B conjuntamente. 
   1. Prefiero: authority-bounded cross-subject evidence composition
2. **No usaría common booking, same stay o same Hunt como autoridad positiva**. Los mantendría deliberadamente como contexto compartido para demostrar que contexto común no basta.
   1. No veo casos POR los que llegarían a  considerarse  autoridad positiva.
3. **Introduciría una única premisa experimental explícita y scoped que autorice P1/P2**, sin llamarla Group, Membership ni SharedParticipation y sin convertirla en componente arquitectónico.
   1. DE acuerdo para experimentar
4. **Mantendría indeterminado el beneficiario colectivo**. Session 17 probaría la legitimidad de las premisas de una evaluación, no quién «posee» posteriormente el SufficiencyClaim.
   1. OK
5. **No modificaría todavía el Contrato semántico de producto**. La hipótesis a falsificar sería que quizá lo que necesita el contrato no es inicialmente `Group`, sino separar `Evidence subject attribution` de `evaluation/participation scope`.
   1. OK

Especialmente el **punto 4** me parece la frontera delicada: podemos demostrar que dos evidencias son legítimamente co-admisibles sin decidir todavía si el claim pertenece a P1, a P2, a ambos o a una entidad colectiva. Si aceptamos esa separación, Session 17 puede seguir siendo extremadamente estrecha; si consideramos que todo SufficiencyClaim debe poseer necesariamente un sujeto semántico, entonces habremos encontrado precisamente el primer gap real que obliga a revisar el Contrato semántico de producto antes de poder completar el experimento.
