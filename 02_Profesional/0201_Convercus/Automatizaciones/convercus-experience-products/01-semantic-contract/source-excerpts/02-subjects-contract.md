---
title: "Contrato semántico y funcional — Sistema de sujetos"
aliases:
  - "Subjects Contract"
  - "Arquetipo, perfil de lealtad y actores"
language: es
version: "v0.1"
product_baseline: "TES Experience Builder v0.5"
status: "cristalizado para implementación MVP"
date: "2026-07-16"
project: "TES Experience Builder"
document_type: "contrato semántico, relacional y operativo"
scope: "arquetipo, perfil de lealtad y actores de la experiencia"
repository_path: "01-contrato-semantico/02-subjects-contract.md"
depends_on:
  - "TES_Experience_Builder_Guia_Contrato_Semantico_v0_1"
semantic_baseline:
  ontology:
    document: "TES_Ontologia_Accion_Situada"
    version: "v2.0"
  experience_ledger:
    document: "TES_Experience_Ledger"
    version: "v2.0"
  lexicon:
    document: "TES_Lexico"
    version: "v3.1"
  subject_ecosystem:
    document: "TES_Ecosistema_Sujetos_Participantes"
    version: "v1.2"
---

# Contrato semántico y funcional — Sistema de sujetos

## Propósito

Este documento aplica los tres niveles del contrato semántico del TES Experience Builder al primer dominio completo de producto: el **sistema de sujetos de una experiencia**.

Los tres niveles son:

1. **Ficha atómica:** qué significa cada concepto TES dentro del Builder.
2. **Contrato relacional:** cómo se conectan los conceptos y qué invariantes preservan.
3. **Contrato operativo:** cómo se representan, editan, almacenan, validan y versionan.

Este contrato está preparado para servir como especificación de desarrollo de la baseline **v0.5**.

> [!important]
> Este documento no redefine el TES. Fija cómo el Builder consume, representa y opera una baseline semántica versionada del TES.

---

## Decisiones de alcance del MVP

Para que el desarrollador pueda implementar un primer modelo coherente sin ambigüedades, se cristalizan las siguientes decisiones.

### DS-001 — Un arquetipo primario por experiencia

Cada experiencia debe referenciar exactamente **un arquetipo primario**.

La versión v0.5 no admite arquetipos secundarios ni ponderaciones múltiples. Esta simplificación es funcional, no ontológica. La ampliación a varios arquetipos requerirá una decisión posterior y una migración explícita.

### DS-002 — Un perfil de lealtad primario por experiencia

Cada experiencia debe definir exactamente **un perfil de lealtad primario**.

El perfil representa empíricamente al sujeto cuya relación se pretende estructurar. Las experiencias dirigidas a perfiles sustancialmente diferentes deberán modelarse como experiencias distintas o como variantes futuras expresamente gobernadas.

### DS-003 — Un actor circunstancial primario obligatorio

Al crear el perfil de lealtad, el Builder crea un **actor circunstancial primario** asociado a ese perfil.

Este actor representa la actualización situada del perfil dentro del recorrido. Puede recibir un nombre contextual, pero no puede cambiar de especie actoral.

### DS-004 — Actores estructurales y operativos opcionales

Una experiencia puede incorporar:

- cero o más actores estructurales;
- cero o más actores operativos;
- uno o más actores circunstanciales.

La existencia de actores estructurales u operativos depende del ecosistema y de la ejecución real de la experiencia.

### DS-005 — El perfil de adopción queda fuera del recorrido

El perfil de adopción no forma parte del sistema de sujetos del recorrido de experiencia en la baseline v0.5.

Podrá incorporarse en el futuro al dominio de adopción organizativa, administración o implantación del Builder. No debe confundirse con el perfil de lealtad.

### DS-006 — Los arquetipos canónicos son de solo lectura

El Builder puede:

- referenciar un arquetipo gobernado;
- contextualizarlo mediante una instanciación local;
- registrar un arquetipo candidato.

El Builder no puede modificar la definición canónica ni convertir una propuesta local en arquetipo TES vigente.

### DS-007 — Los actores no son etapas

Los actores se definen en el contexto de la experiencia y se referencian desde etapas, eventos, intervenciones o reglas. No se insertan como nodos temporales del recorrido.

### DS-008 — Sin mapeo técnico automático

La existencia de un arquetipo, perfil o actor en el Builder no implica que exista un equivalente directo en la API o en la plataforma de ejecución.

Todo mapeo técnico debe declararse por separado como:

- `builder_native`;
- `mappable`;
- `integration_required`;
- `not_verified`;
- `not_supported`.

---

# Nivel 1 — Fichas atómicas

## Arquetipo

```yaml
concept_id: TES-CONCEPT-ARCHETYPE
concept_name: Arquetipo
contract_status: crystallized

source_authority:
  primary:
    document: TES_Lexico
    version: v3.1
  complementary:
    document: TES_Ecosistema_Sujetos_Participantes
    version: v1.2

tes_meaning:
  Lógica estructural recurrente de motivación, reconocimiento
  o transformación que hace inteligible una forma de progresión,
  vínculo o cambio dentro de una experiencia.

builder_interpretation:
  Marco estructural utilizado para formular, orientar y contrastar
  la hipótesis de transformación de una experiencia.

gui_representation:
  type: persistent_experience_context
  placement:
    - candidate_experience
    - experience_context_bar
    - subjects_inspector
    - simulation_context
  prohibited_placement:
    - journey_stage
    - observable_event
    - transition
    - actor_node

data_representation:
  entity: archetype_reference
  cardinality: exactly_one_primary
  source: governed_catalogue
  versioned_reference: true

invariants:
  - No equivale a perfil de lealtad.
  - No equivale a segmento.
  - No equivale a actor.
  - No equivale a descripción demográfica.
  - No constituye una etapa del recorrido.
  - No constituye un evento observable.

allowed_operations:
  - Seleccionar un arquetipo gobernado.
  - Consultar su definición.
  - Registrar la justificación de selección.
  - Crear una instanciación contextual.
  - Sustituirlo mientras la experiencia no esté publicada.
  - Registrar una propuesta de arquetipo candidato.

prohibited_operations:
  - Editar la definición canónica.
  - Usarlo como actor.
  - Usarlo como nombre de segmento.
  - Insertarlo en la secuencia como nodo.
  - Publicar un arquetipo candidato como si fuera canónico.

validation_rules:
  - Debe existir una referencia primaria.
  - La fuente y versión deben ser trazables.
  - La justificación debe relacionarlo con la hipótesis de transformación.
  - No puede utilizarse una referencia marcada como retirada.
```

### Campos de instanciación local del arquetipo

La instanciación local no redefine el arquetipo. Explica cómo se manifiesta en una experiencia concreta.

Campos:

- `context_name`;
- `transformation_relevance`;
- `expected_motivations`;
- `expected_frictions`;
- `recognition_signals`;
- `progression_hypothesis`;
- `designer_rationale`;
- `evidence_notes`.

---

## Perfil de lealtad

```yaml
concept_id: TES-CONCEPT-LOYALTY-PROFILE
concept_name: Perfil de lealtad
contract_status: crystallized

source_authority:
  primary:
    document: TES_Ecosistema_Sujetos_Participantes
    version: v1.2
  complementary:
    document: TES_Lexico
    version: v3.1

tes_meaning:
  Representación empírica y operativa del sujeto cuya relación,
  continuidad, preferencia, confianza, recurrencia, adherencia
  o prescripción se desea estructurar mediante una experiencia.

builder_interpretation:
  Descripción operativa del sujeto final para el que se instancia
  el recorrido y sobre el que se formularán estados, eventos,
  fricciones, reglas de avance e intervenciones.

gui_representation:
  type: editable_subject_definition
  placement:
    - candidate_experience
    - subjects_inspector
    - experience_context_bar
    - simulation_context
  prohibited_placement:
    - archetype_catalogue
    - actor_type_selector
    - journey_stage_as_identity

data_representation:
  entity: loyalty_profile
  cardinality: exactly_one_primary
  source: experience_local
  versioned_reference: false

invariants:
  - No equivale a arquetipo.
  - No equivale a actor.
  - No puede reducirse a demografía.
  - Debe declarar la relación que se desea estructurar.
  - Debe ser suficientemente operativo para orientar el recorrido.
  - Puede actualizarse situacionalmente como actor circunstancial.

allowed_operations:
  - Crear y editar el perfil dentro de la experiencia.
  - Definir estados inicial y deseado.
  - Registrar comportamientos observables relevantes.
  - Registrar fricciones y condiciones contextuales.
  - Asociarlo al arquetipo primario.
  - Duplicarlo únicamente mediante duplicación o variante de experiencia.

prohibited_operations:
  - Usarlo como sinónimo de arquetipo.
  - Usarlo como rol operativo.
  - Definirlo únicamente mediante edad, género, localización o renta.
  - Publicar la experiencia sin una relación objetivo explícita.

validation_rules:
  - Debe tener nombre operativo.
  - Debe declarar estado inicial.
  - Debe declarar estado relacional deseado.
  - Debe declarar el tipo de relación que se estructura.
  - Debe contener al menos una conducta observable relevante.
  - Debe contener al menos una fricción o condición contextual.
  - Debe estar vinculado al arquetipo primario.
```

### Estructura mínima del perfil de lealtad

- `name`;
- `description`;
- `relationship_objective`;
- `relationship_dimensions`;
- `initial_state`;
- `desired_state`;
- `observable_behaviours`;
- `frictions`;
- `context_conditions`;
- `evidence_requirements`;
- `archetype_alignment`;
- `status`.

Dimensiones de relación permitidas en v0.5:

- `continuity`;
- `preference`;
- `trust`;
- `recurrence`;
- `adherence`;
- `prescription`;
- `combined`.

---

## Actor

```yaml
concept_id: TES-CONCEPT-ACTOR
concept_name: Actor
contract_status: crystallized

source_authority:
  primary:
    document: TES_Ecosistema_Sujetos_Participantes
    version: v1.2
  complementary:
    document: TES_Lexico
    version: v3.1

tes_meaning:
  Posición efectiva de intervención dentro de una escena,
  una secuencia o una red operativa, definida por su capacidad
  de acción, restricción y efecto.

builder_interpretation:
  Rol situado que participa en la experiencia, condiciona su
  posibilidad, ejecuta intervenciones o actualiza el recorrido
  mediante una conducta observable.

gui_representation:
  type: experience_participant_role
  placement:
    - subjects_inspector
    - actor_panel
    - journey_node_references
    - event_actor_field
    - intervention_actor_field
  prohibited_placement:
    - archetype_selector
    - loyalty_profile_identity
    - journey_stage_as_time_node

data_representation:
  entity: actor
  cardinality: one_or_more_total
  source: experience_local
  versioned_reference: false

invariants:
  - No equivale a arquetipo.
  - No equivale a perfil.
  - Debe declarar una especie actoral.
  - Debe declarar una posición o capacidad de intervención.
  - Puede referenciar una entidad organizativa real sin reducirse a ella.

allowed_operations:
  - Crear actores locales.
  - Tipificarlos como estructurales, operativos o circunstanciales.
  - Asociarlos a eventos, etapas, reglas e intervenciones.
  - Desactivarlos en una nueva versión de la experiencia.
  - Reutilizarlos dentro de la misma experiencia.

prohibited_operations:
  - Crear un actor sin especie.
  - Utilizar el actor como sustituto del perfil de lealtad.
  - Convertir una entidad jurídica en actor sin declarar su rol.
  - Eliminar un actor que esté referenciado sin resolver sus dependencias.
```

---

## Actor estructural

```yaml
concept_id: TES-CONCEPT-STRUCTURAL-ACTOR
concept_name: Actor estructural
contract_status: crystallized

builder_interpretation:
  Posición que define condiciones de posibilidad, gobierno,
  propiedad, autorización o restricción de la experiencia
  sin quedar reducida a una escena puntual.

data_representation:
  entity: actor
  discriminator: structural

required_fields:
  - name
  - role_description
  - structural_capacity
  - influence_scope

typical_examples:
  - operador de marca
  - propietario de red
  - unidad rectora
  - fabricante que gobierna la experiencia
  - administración o entidad autorizante

validation_rules:
  - Debe declarar qué condición de posibilidad o restricción introduce.
  - No puede definirse solo por el nombre de una empresa.
```

---

## Actor operativo

```yaml
concept_id: TES-CONCEPT-OPERATIONAL-ACTOR
concept_name: Actor operativo
contract_status: crystallized

builder_interpretation:
  Posición que ejecuta, traduce, administra o sostiene
  la experiencia en la práctica cotidiana.

data_representation:
  entity: actor
  discriminator: operational

required_fields:
  - name
  - role_description
  - operational_actions
  - intervention_channels

typical_examples:
  - personal de tienda
  - equipo de atención
  - recepción
  - coordinación
  - equipo de activación
  - operador de servicio

validation_rules:
  - Debe declarar al menos una acción o intervención.
  - Debe declarar los canales o contextos en los que opera.
```

---

## Actor circunstancial

```yaml
concept_id: TES-CONCEPT-CIRCUMSTANTIAL-ACTOR
concept_name: Actor circunstancial
contract_status: crystallized

builder_interpretation:
  Posición episódica que actualiza con su conducta la secuencia
  de la experiencia. El actor circunstancial primario es la
  actualización situada del perfil de lealtad.

data_representation:
  entity: actor
  discriminator: circumstantial

required_fields:
  - name
  - role_description
  - linked_loyalty_profile_id
  - participation_scope

invariants:
  - Debe existir al menos uno.
  - El actor circunstancial primario debe vincularse al perfil de lealtad.
  - La vinculación no elimina la diferencia entre perfil y actor.

validation_rules:
  - El actor circunstancial primario es obligatorio.
  - La referencia al perfil debe ser válida.
  - Debe declarar en qué parte del recorrido participa.
```

---

# Nivel 2 — Contrato relacional

## Modelo conceptual

```text
Experience
│
├── has exactly 1 ArchetypeReference
│       └── may have 0..1 ArchetypeInstantiation
│
├── has exactly 1 LoyaltyProfile
│       └── aligned_with 1 ArchetypeReference
│
└── has 1..n Actors
        ├── 0..n StructuralActor
        ├── 0..n OperationalActor
        └── 1..n CircumstantialActor
                └── primary actor linked_to 1 LoyaltyProfile
```

## Cardinalidades cristalizadas

| Relación | Cardinalidad v0.5 | Regla |
|---|---:|---|
| Experiencia → arquetipo primario | 1 | Obligatoria |
| Arquetipo → instanciación local | 0..1 | Opcional |
| Experiencia → perfil de lealtad | 1 | Obligatoria |
| Perfil de lealtad → arquetipo | 1 | Debe coincidir con el primario |
| Experiencia → actores | 1..n | Al menos el circunstancial primario |
| Experiencia → actores estructurales | 0..n | Opcional |
| Experiencia → actores operativos | 0..n | Opcional |
| Experiencia → actores circunstanciales | 1..n | Obligatorio |
| Actor circunstancial primario → perfil | 1 | Obligatoria |
| Etapa → actor responsable | 0..1 | Opcional en v0.5 |
| Evento → actor originador | 0..1 | Opcional |
| Intervención → actor ejecutor | 0..1 | Opcional |
| Regla → actor afectado | 0..1 | Opcional |

## Relaciones semánticas

```text
Arquetipo
    hace inteligible
Hipótesis de transformación

Perfil de lealtad
    representa empíricamente
Sujeto cuya relación se estructura

Perfil de lealtad
    se alinea con
Arquetipo primario

Actor circunstancial primario
    actualiza situadamente
Perfil de lealtad

Actor estructural
    condiciona
Campo de mediación

Actor operativo
    ejecuta o sostiene
Intervención y operación

Actor circunstancial
    realiza o recibe
Acciones situadas en el recorrido
```

## Invariantes relacionales

### INV-SUBJ-001 — No degradación del arquetipo

El arquetipo no puede materializarse como perfil, segmento o actor.

### INV-SUBJ-002 — No sustitución del perfil

El perfil de lealtad no puede utilizarse como rol operativo ni como especie actoral.

### INV-SUBJ-003 — Actor tipificado

Todo actor debe tener exactamente una especie:

- `structural`;
- `operational`;
- `circumstantial`.

### INV-SUBJ-004 — Actualización situada

El actor circunstancial primario debe estar vinculado al perfil de lealtad, pero ambas entidades deben conservar identificadores y responsabilidades diferentes.

### INV-SUBJ-005 — Trazabilidad del arquetipo

La referencia al arquetipo debe conservar:

- identificador;
- documento fuente;
- versión fuente;
- versión de catálogo;
- estado de vigencia.

### INV-SUBJ-006 — Integridad de referencias

No puede eliminarse un actor mientras esté referenciado por una etapa, evento, intervención o regla.

### INV-SUBJ-007 — Unicidad primaria

Solo puede existir:

- un arquetipo primario;
- un perfil de lealtad primario;
- un actor circunstancial marcado como primario.

### INV-SUBJ-008 — Separación de planos

El perfil de adopción no puede incorporarse al campo `loyalty_profile` ni utilizarse como actor circunstancial primario.

---

# Nivel 3 — Contrato operativo

## Flujo de creación

```text
1. Crear experiencia candidata
        ↓
2. Seleccionar arquetipo primario
        ↓
3. Registrar justificación e instanciación contextual
        ↓
4. Definir perfil de lealtad
        ↓
5. Crear automáticamente actor circunstancial primario
        ↓
6. Añadir actores estructurales u operativos cuando proceda
        ↓
7. Ejecutar validación semántica
        ↓
8. Habilitar acceso al diseño del recorrido
```

La navegación al Journey Builder puede permitirse con un sistema incompleto, pero la experiencia no puede superar la compuerta `subjects_validated` sin cumplir las validaciones bloqueantes.

---

## Estados del sistema de sujetos

```yaml
subject_system_status:
  - empty
  - incomplete
  - provisional
  - valid
  - blocked
  - outdated_reference
```

### `empty`

No existe selección ni definición.

### `incomplete`

Existe información parcial, pero faltan campos obligatorios.

### `provisional`

El sistema está completo, pero utiliza un arquetipo candidato, una referencia pendiente o una decisión no validada.

### `valid`

Supera todas las validaciones bloqueantes.

### `blocked`

Existe una colisión semántica o una referencia inválida que impide publicación.

### `outdated_reference`

La experiencia utiliza una versión anterior de una fuente TES. No se migra automáticamente.

---

## Pantalla Experiencia candidata

### Sección Arquetipo

Componentes:

- `ArchetypeSelector`;
- `ArchetypeDefinitionPreview`;
- `ArchetypeSourceBadge`;
- `ArchetypeRationaleField`;
- `ArchetypeInstantiationForm`;
- `ArchetypeCandidateAction`.

Comportamiento:

- el catálogo canónico es de solo lectura;
- la selección es obligatoria;
- la justificación es obligatoria;
- la instanciación contextual es opcional;
- un arquetipo candidato coloca el sistema en estado `provisional`.

### Sección Perfil de lealtad

Componentes:

- `LoyaltyProfileForm`;
- `RelationshipDimensionSelector`;
- `InitialStateEditor`;
- `DesiredStateEditor`;
- `ObservableBehaviourList`;
- `FrictionList`;
- `ContextConditionList`;
- `ArchetypeAlignmentField`.

Comportamiento:

- edición local completa;
- validación incremental;
- creación automática del actor circunstancial primario al guardar por primera vez;
- aviso cuando el perfil se define únicamente mediante rasgos descriptivos.

### Sección Actores

Componentes:

- `ActorList`;
- `ActorTypeBadge`;
- `ActorEditor`;
- `ActorReferenceUsage`;
- `AddActorAction`.

Comportamiento:

- el actor circunstancial primario aparece bloqueado en su especie;
- puede editarse su nombre contextual y alcance;
- los actores adicionales pueden crearse, editarse, desactivarse o eliminarse;
- la eliminación se bloquea si existen referencias.

---

## Journey Builder

El arquetipo y el perfil de lealtad deben permanecer visibles como **contexto persistente**, no como bloques del canvas.

Componentes:

- `SubjectContextBar`;
- `ActorReferencePicker`;
- `ActorBadge`;
- `SubjectsInspectorTab`.

### Representación recomendada v0.5

- El arquetipo aparece como referencia compacta en la cabecera.
- El perfil aparece como sujeto principal del recorrido.
- Los actores se muestran mediante badges o selectores en etapas, eventos e intervenciones.
- No se implementan swimlanes actorales en el MVP.
- La vista por lanes queda reservada para una evolución posterior.

---

## Simulación

La simulación debe mostrar:

- arquetipo primario como marco interpretativo;
- perfil de lealtad como sujeto simulado;
- actor circunstancial activo;
- actores operativos que ejecutan intervenciones;
- actores estructurales que introducen restricciones o condiciones.

La simulación no debe tratar el arquetipo como agente ejecutor.

---

## Edición

### Arquetipo

- La referencia puede sustituirse en borrador.
- La sustitución obliga a revalidar el perfil de lealtad.
- En una experiencia activa, el cambio requiere nueva versión.
- La definición canónica nunca es editable.

### Perfil de lealtad

- Editable en borrador.
- Cambios sustanciales en una experiencia activa requieren nueva versión.
- La modificación del estado inicial o deseado invalida la simulación anterior.
- La eliminación no está permitida; debe sustituirse mediante nueva versión.

### Actores

- Editables mientras la experiencia esté en borrador.
- Pueden desactivarse en una nueva versión.
- No deben borrarse físicamente si existe historial publicado.
- La eliminación en borrador exige resolver referencias.

---

## Persistencia

El sistema se almacena bajo el objeto `subject_system`.

```json
{
  "subject_system": {
    "status": "valid",
    "archetype": {},
    "loyalty_profile": {},
    "actors": [],
    "semantic_baseline_id": "TES-BUILDER-2026-07"
  }
}
```

El esquema completo se adjunta en:

```text
08-data-model/schemas/subjects.schema.json
```

---

## Versionado

Deben distinguirse dos ejes.

### Versión de fuentes TES

Permite saber contra qué baseline fue creada la interpretación.

Campos:

- `semantic_baseline_id`;
- `source_document`;
- `source_version`;
- `catalogue_version`.

### Versión de experiencia

Registra cambios locales en:

- instanciación del arquetipo;
- perfil de lealtad;
- actores;
- relaciones y referencias.

Reglas:

- no se actualizan referencias semánticas automáticamente;
- una fuente nueva puede marcar `outdated_reference`;
- la migración requiere acción explícita;
- el historial conserva la referencia anterior;
- las experiencias activas se modifican mediante nueva versión.

---

## Validaciones

| Código | Severidad | Regla |
|---|---|---|
| SUBJ-001 | block | Falta arquetipo primario |
| SUBJ-002 | block | La referencia del arquetipo no es trazable |
| SUBJ-003 | block | Falta perfil de lealtad |
| SUBJ-004 | block | Falta actor circunstancial primario |
| SUBJ-005 | block | El actor circunstancial primario no referencia el perfil |
| SUBJ-006 | block | Un actor no tiene especie válida |
| SUBJ-007 | block | Existen varios arquetipos primarios |
| SUBJ-008 | block | Existen varios perfiles primarios |
| SUBJ-009 | block | Existen varios actores circunstanciales primarios |
| SUBJ-010 | warn | El perfil se define solo mediante rasgos demográficos |
| SUBJ-011 | warn | Falta actor operativo pese a existir una intervención humana |
| SUBJ-012 | warn | Falta actor estructural pese a existir una dependencia de autorización |
| SUBJ-013 | block | Se ha utilizado un arquetipo como actor |
| SUBJ-014 | block | Se ha utilizado un perfil como especie actoral |
| SUBJ-015 | warn | Referencia TES anterior a la baseline recomendada |
| SUBJ-016 | block | Arquetipo candidato en experiencia preparada para publicación |
| SUBJ-017 | block | Intento de eliminar actor con referencias |
| SUBJ-018 | warn | Falta justificación de alineación arquetipo-perfil |

---

## Regla de publicación

El sistema de sujetos no bloquea el trabajo exploratorio del canvas, pero sí bloquea la publicación.

Para publicar, deben cumplirse:

- estado `valid`;
- arquetipo canónico y trazable;
- perfil de lealtad completo;
- actor circunstancial primario;
- ausencia de errores `block`;
- baseline semántica registrada.

---

## Contrato técnico provisional

| Entidad | Estado técnico v0.5 | Observación |
|---|---|---|
| Arquetipo | `builder_native` | Referencia semántica del Builder |
| Instanciación de arquetipo | `builder_native` | No requiere equivalente de API |
| Perfil de lealtad | `builder_native` | Puede mapearse parcialmente a segmentos; no verificado |
| Actor estructural | `builder_native` | Puede mapear dependencias o permisos; no automático |
| Actor operativo | `builder_native` | Puede vincularse a canales, equipos o integraciones |
| Actor circunstancial | `builder_native` | Puede corresponder a usuario/cliente; requiere mapeo de identidad |
| Relación perfil-segmento | `not_verified` | No asumir equivalencia |
| Relación actor-usuario técnico | `not_verified` | Depende de la plataforma |

---

# Casos de aceptación para desarrollo

## CA-SUBJ-001 — Crear sistema mínimo válido

Dado un borrador de experiencia:

- el usuario selecciona un arquetipo canónico;
- registra una justificación;
- crea un perfil de lealtad completo;
- el sistema crea un actor circunstancial primario;
- la validación devuelve `valid`.

## CA-SUBJ-002 — Impedir arquetipo como actor

Cuando el usuario intenta utilizar el identificador del arquetipo en un campo `actor_id`, el sistema rechaza la operación con `SUBJ-013`.

## CA-SUBJ-003 — Referencia obsoleta

Cuando la baseline recomendada cambia:

- la experiencia conserva su referencia;
- el estado pasa a `outdated_reference`;
- no se modifica automáticamente;
- se ofrece una acción de evaluación o migración.

## CA-SUBJ-004 — Arquetipo candidato

Cuando se usa un arquetipo candidato:

- el estado es `provisional`;
- el diseño puede continuar;
- la publicación queda bloqueada mediante `SUBJ-016`.

## CA-SUBJ-005 — Eliminación de actor referenciado

Cuando un actor está referenciado por una etapa o intervención:

- la eliminación se bloquea;
- se muestran las referencias;
- el usuario debe reasignar o eliminar esas dependencias.

## CA-SUBJ-006 — Cambio de arquetipo

Cuando se sustituye el arquetipo:

- se conserva el historial;
- se invalida la alineación previa del perfil;
- el sistema pasa a `incomplete` o `provisional`;
- se requiere nueva validación.

---

# Trabajo técnico recomendado

## Dominio y persistencia

- Implementar el objeto `subject_system`.
- Validar con JSON Schema.
- Mantener identificadores estables.
- Diferenciar referencias gobernadas y entidades locales.
- No usar una única entidad genérica `user_type`.

## Servicios de dominio

Funciones mínimas:

```text
selectArchetype()
replaceArchetype()
createArchetypeInstantiation()
createArchetypeCandidate()
createLoyaltyProfile()
updateLoyaltyProfile()
createPrimaryCircumstantialActor()
addActor()
updateActor()
removeActor()
validateSubjectSystem()
evaluateSemanticBaseline()
```

## Interfaz

Primera iteración:

- selector de arquetipo;
- formulario de perfil;
- lista/editor de actores;
- barra contextual;
- panel de validación;
- mock data local.

## Pruebas

- validación de cardinalidades;
- separación de identificadores;
- bloqueo de operaciones prohibidas;
- migración no automática;
- integridad de referencias;
- estados del sistema;
- casos de aceptación anteriores.

---

# Fuera de alcance v0.5

- varios arquetipos por experiencia;
- varios perfiles primarios;
- catálogo editable desde el Builder;
- aprobación canónica de arquetipos candidatos;
- swimlanes actorales;
- mapeo automático con segmentos CRM/CDP;
- permisos organizativos basados en actores;
- sincronización automática con el repositorio TES;
- migraciones semánticas automáticas.

---

# Criterio de cierre

El dominio Sistema de sujetos puede considerarse implementado para v0.5 cuando:

- el esquema de datos valida;
- existe exactamente un arquetipo primario;
- existe exactamente un perfil de lealtad;
- existe un actor circunstancial primario vinculado;
- los actores conservan su especie;
- la GUI mantiene arquetipo y perfil fuera del canvas temporal;
- las referencias TES son trazables;
- las validaciones bloqueantes funcionan;
- el historial no se destruye;
- y los casos de aceptación están cubiertos.

> [!summary]
> El arquetipo hace inteligible la transformación; el perfil de lealtad formaliza al sujeto; el actor ocupa una posición situada. El Builder debe operar estas tres capas sin fusionarlas.
