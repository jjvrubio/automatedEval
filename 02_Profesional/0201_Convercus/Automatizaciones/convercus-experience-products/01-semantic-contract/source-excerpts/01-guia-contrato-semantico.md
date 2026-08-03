---
title: "Guía del contrato semántico del TES Experience Builder"
aliases:
  - "Guía de derivación funcional TES → Builder"
  - "Contrato semántico del Experience Builder"
language: es
version: "v0.1"
status: "borrador de cristalización"
date: "2026-07-16"
project: "TES Experience Builder"
document_type: "guía operativa"
scope: "traducción controlada de conceptos TES al modelo funcional, visual y técnico del Builder"
repository_role: "documento rector del repositorio independiente del TES Experience Builder"
---

# Guía del contrato semántico del TES Experience Builder

## Propósito

Esta guía establece cómo debe utilizar el **TES Experience Builder** los conceptos procedentes del TES sin absorber, duplicar ni modificar el sistema ontológico y editorial del que deriva.

El TES y el TES Experience Builder son construcciones independientes:

- el **TES** desarrolla y gobierna la ontología, el lenguaje, la arquitectura experiencial, la traducción editorial, la medición y sus mecanismos de validación;
- el **TES Experience Builder** es un producto digital derivado que utiliza una selección explícita y versionada de conceptos TES para permitir crear, configurar, simular, validar, versionar y publicar experiencias.

La relación entre ambos sistemas debe estar mediada por un **contrato semántico de producto**.

> [!important]
> El Builder consume significado gobernado por el TES, pero no adquiere autoridad para redefinirlo.

Esta guía debe utilizarse como referencia para:

- redactar el baseline funcional y semántico del Builder;
- construir el modelo de entidades;
- diseñar pantallas y componentes;
- definir esquemas de datos;
- formular reglas de validación;
- evaluar el impacto de futuras evoluciones del TES;
- y evitar que decisiones de interfaz o implementación se conviertan accidentalmente en definiciones ontológicas.

## Principio de independencia

El TES Experience Builder debe mantenerse en un repositorio completamente independiente.

El repositorio del Builder no constituye una carpeta del TES, una copia reducida del Telar Editorial Situado ni una extensión técnica del núcleo ontológico.

Su relación correcta es:

```text
TES — sistema ontológico y editorial
        │
        │ derivación controlada y versionada
        ▼
Contrato semántico de producto
        │
        │ traducción funcional
        ▼
TES Experience Builder
        │
        ├── modelo funcional
        ├── arquitectura de información
        ├── GUI
        ├── modelo de datos
        ├── prototipo
        └── integraciones técnicas
```

El TES actúa como sistema **upstream** de significado.

El Builder actúa como sistema **downstream** de operacionalización.

El flujo no es simétrico. Las necesidades del Builder pueden producir observaciones o tensiones relevantes para el TES, pero no deben modificarlo automáticamente.

## Regla de no invasión

El TES Experience Builder no crea, redefine ni corrige conceptos ontológicos del TES.

Toda entidad, campo, componente, pantalla o comportamiento del Builder debe clasificarse como una de las siguientes categorías:

- **derivación directa de un concepto TES**;
- **traducción funcional de uno o varios conceptos TES**;
- **construcción propia del producto**;
- **capacidad técnica**;
- **elemento de interfaz**.

Las construcciones propias del Builder no adquieren por ello estatuto ontológico.

Ejemplos de construcciones propias del producto:

- estado de experiencia candidata;
- incidencia de validación;
- gap técnico;
- ejecución de simulación;
- selección de bloque;
- guardado automático;
- historial de versión;
- comprobación de publicación.

Estas entidades pueden ser esenciales para el producto sin formar parte del TES.

## Precedencia entre capas

Cuando aparezca una tensión entre significado, funcionalidad, interfaz o implementación, debe aplicarse la siguiente precedencia:

```text
Definición ontológica TES
        >
Contrato semántico del producto
        >
Modelo funcional
        >
Modelo de interacción
        >
Representación visual
        >
Conveniencia técnica
```

Esta precedencia no implica ignorar las restricciones técnicas o de usabilidad.

Cuando un concepto no pueda implementarse directamente, el Builder deberá:

- declarar la limitación;
- introducir una mediación explícita;
- reducir el alcance;
- clasificar la capacidad como pendiente;
- o registrar un gap técnico.

No deberá fingir una equivalencia inexistente.

## Baseline semántica

El Builder no debe depender de una noción abstracta de “la versión vigente del TES”.

Cada versión significativa del producto debe declarar la baseline semántica concreta que utiliza.

Ejemplo:

```yaml
tes_semantic_baseline:
  baseline_id: TES-BUILDER-2026-07
  frozen_at: 2026-07-16
  sources:
    ontology:
      document: TES_Ontologia_Accion_Situada
      version: v2.0
    experience_ledger:
      document: TES_Experience_Ledger
      version: v2.0
    lexicon:
      document: TES_Lexico
      version: v3.1
    subject_ecosystem:
      document: TES_Ecosistema_Sujetos_Participantes
      version: v1.2
```

La baseline no congela el TES. Congela únicamente la base semántica utilizada por una versión del Builder.

Cuando el TES evolucione, deberá realizarse una evaluación de impacto antes de actualizar la baseline.

## Qué es una ficha de mapeo semántico-funcional

La ficha de mapeo semántico-funcional es la unidad mínima del contrato semántico.

Su función consiste en declarar:

- qué concepto TES se utiliza;
- qué fuente lo gobierna;
- cómo lo interpreta el Builder;
- cómo se representa en la GUI;
- qué entidad de datos lo soporta;
- qué invariantes debe conservar;
- y qué decisiones siguen abiertas.

La ficha no copia toda la definición TES ni crea una definición paralela.

La ficha explica cómo una versión del producto consume un concepto gobernado externamente.

## Plantilla mínima de ficha

```yaml
concept_id:
concept_name:
contract_status:

source_authority:
  primary:
    document:
    version:
  complementary:
    document:
    version:

tes_meaning:

builder_interpretation:

gui_representation:
  type:
  placement:
  prohibited_placement:

data_representation:
  entity:
  cardinality:
  source:
  versioned_reference:

invariants:

allowed_operations:

prohibited_operations:

validation_rules:

open_decisions:

semantic_dependencies:

product_impact:
  entities:
  screens:
  components:
  validations:
```

## Ejemplo: Arquetipo

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
  o transformación que hace inteligible una forma de progresión
  o vínculo dentro de una experiencia.

builder_interpretation:
  Marco estructural utilizado para formular, orientar y contrastar
  la hipótesis de transformación de una experiencia.

gui_representation:
  type: persistent_experience_context
  placement:
    - candidate_experience
    - experience_header
    - foundation_inspector
  prohibited_placement:
    - journey_stage
    - observable_event
    - transition
    - operational_actor

data_representation:
  entity: archetype_reference
  cardinality: unresolved
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
  - Vincularlo a una hipótesis de transformación.
  - Registrar el motivo de su selección.
  - Crear una instanciación contextual para una experiencia.
  - Proponer un arquetipo candidato sin incorporarlo al canon.

prohibited_operations:
  - Modificar silenciosamente su definición.
  - Convertirlo en segmento comercial.
  - Utilizarlo como actor operativo.
  - Insertarlo como etapa temporal del recorrido.
  - Publicar una definición local como arquetipo TES canónico.

validation_rules:
  - La selección debe expresar una lógica de transformación.
  - Debe existir una distinción explícita respecto al perfil de lealtad.
  - La hipótesis de transformación debe ser compatible con el arquetipo.
  - La fuente gobernada y su versión deben permanecer trazables.

open_decisions:
  - Si una experiencia puede referenciar varios arquetipos.
  - Si existe un arquetipo dominante y otros secundarios.
  - Cómo se evalúa una propuesta de arquetipo candidato.

semantic_dependencies:
  - experiencia
  - hipotesis_de_transformacion
  - perfil_de_lealtad
  - actor

product_impact:
  entities:
    - archetype_reference
    - archetype_instantiation
    - archetype_candidate
  screens:
    - candidate_experience
    - journey_builder
    - simulation
  components:
    - archetype_selector
    - archetype_summary
    - archetype_validation_notice
  validations:
    - SEM-ARCH-001
    - SEM-ARCH-002
```

## La ficha atómica no es suficiente

Una colección de fichas correctas no garantiza un producto coherente.

El contrato semántico debe operar en tres niveles.

### Ficha atómica

Define qué significa cada concepto dentro del Builder.

Responde a preguntas como:

- ¿Qué es?
- ¿Qué fuente lo gobierna?
- ¿Cómo lo representa el producto?
- ¿Qué no debe significar?

### Contrato relacional

Define cómo se conectan los conceptos y qué cardinalidades mantienen.

Responde a preguntas como:

- ¿Qué entidad referencia a cuál?
- ¿Qué concepto hace inteligible otro?
- ¿Qué elementos pueden coexistir?
- ¿Qué relaciones son obligatorias?
- ¿Qué relaciones están prohibidas?

### Contrato operativo

Define cómo se seleccionan, editan, almacenan, validan, simulan y versionan los conceptos.

Responde a preguntas como:

- ¿Qué puede hacer el diseñador?
- ¿Qué campos son obligatorios?
- ¿Qué pantalla los presenta?
- ¿Qué validación se ejecuta?
- ¿Cómo se registra el cambio?
- ¿Qué ocurre cuando falta información?

## Contrato relacional mínimo

El contrato relacional debe preservar, como mínimo, las siguientes distinciones:

```text
Arquetipo
    hace inteligible
Hipótesis de transformación

Perfil de lealtad
    representa empíricamente
Sujeto de la experiencia

Actor circunstancial
    actualiza situadamente
Perfil de lealtad

Actor operativo
    ejecuta o sostiene
Intervención

Evento observable
    aporta evidencia a
Regla de avance

Regla de avance
    evalúa
Condición y evidencia

Regla de avance
    autoriza
Transición

Transición
    materializa
Progresión

Incentivo
    favorece
Avance futuro

Recompensa
    gratifica
Condición o hito alcanzado

Resultado
    permite
Medición mínima

Medición
    precede a
Aprendizaje
```

Este mapa deberá convertirse progresivamente en un modelo de entidades y relaciones.

## Invariantes mínimos del Builder

Los invariantes son condiciones que no deben romperse aunque cambien las pantallas o la implementación.

```text
INV-001
Un arquetipo nunca funciona como etapa del recorrido.

INV-002
Un perfil de lealtad nunca se utiliza como sinónimo de arquetipo.

INV-003
Un actor se define por su posición de intervención, restricción o efecto.

INV-004
Un evento observable no produce por sí solo progresión.
Debe ser evaluado mediante una regla.

INV-005
La progresión no puede reducirse a acumulación indiferenciada.

INV-006
Una recompensa exige una condición, estado o hito alcanzado.

INV-007
Un incentivo favorece el avance, pero no equivale a la gratificación concedida.

INV-008
La experiencia debe conservar resultado, medición mínima y aprendizaje
sin convertirse en dashboard.

INV-009
El ecosistema representa el campo de mediación.
El recorrido representa la secuencia.

INV-010
La representación visual puede agrupar elementos para facilitar la operación,
pero no puede fusionarlos en el modelo funcional o de datos.
```

## Operaciones sobre conceptos gobernados

El Builder debe diferenciar tres operaciones especialmente importantes.

### Referenciar

El Builder apunta a una figura ya gobernada por el TES.

Ejemplo:

```text
archetype_reference
```

La referencia debe incluir identidad, fuente y versión.

### Instanciar

El Builder contextualiza un concepto existente para una experiencia concreta sin redefinirlo.

Ejemplo:

```text
archetype_instantiation
```

La instanciación puede añadir:

- contexto sectorial;
- hipótesis de comportamiento;
- fricciones;
- señales relevantes;
- relación con el perfil de lealtad;
- criterios de observación.

### Proponer un candidato

El Builder registra una hipótesis emergente que podría merecer evaluación dentro del TES.

Ejemplo:

```text
archetype_candidate
```

Un candidato:

- no forma parte automáticamente del canon;
- no sustituye una figura gobernada;
- debe permanecer identificado como propuesta;
- y debe transferirse al proceso de revisión propio del TES.

## Representación en la GUI

Cada concepto relevante debe declarar su comportamiento por pantalla.

Ejemplo para `Arquetipo`:

```yaml
gui:
  candidate_experience:
    visibility: full
    interaction: selectable
    required: true
    editable_definition: false

  journey_builder:
    visibility: compact
    interaction: inspectable
    required: true
    editable_definition: false

  simulation:
    visibility: contextual
    interaction: read_only
    purpose: explain_expected_response

  technical_validation:
    visibility: indirect
    purpose: verify_operationalization
```

La declaración debe impedir que el mismo concepto adopte funciones incompatibles en distintas pantallas.

## Contrato de datos

Nombrar una entidad no es suficiente. Debe declararse su estructura mínima y su trazabilidad.

Ejemplo:

```yaml
archetype_reference:
  archetype_id: string
  source_system: string
  source_document: string
  source_version: string
  catalogue_version: string
  label: string
  selection_status:
    enum:
      - provisional
      - validated
  rationale: string
  relevance:
    primary: boolean
    weight: optional
  local_instantiation_id: optional
```

El contrato de datos debe conservar diferencias semánticas aunque la interfaz agrupe visualmente elementos relacionados.

## Contrato de validación

Cada concepto o relación debe tener reglas comprobables.

Ejemplo de validación del arquetipo:

```text
¿La selección expresa una lógica de transformación?
¿Se ha confundido con una descripción demográfica?
¿Se ha usado como nombre de segmento?
¿Existe un perfil de lealtad diferenciado?
¿La hipótesis de transformación es compatible con el arquetipo?
¿Las etapas representan estados de progresión y no rasgos del arquetipo?
¿La selección está respaldada por una fuente gobernada?
```

Los resultados de validación pueden clasificarse como:

- válido;
- válido con observaciones;
- provisional;
- inconsistente;
- bloqueante.

Las limitaciones semánticas no deben permanecer como notas pasivas. Deben traducirse, cuando sea posible, en validaciones de producto.

## Trazabilidad e impacto

Toda derivación relevante debe permitir identificar:

- la fuente TES;
- la versión utilizada;
- la interpretación funcional;
- las entidades afectadas;
- las pantallas afectadas;
- los componentes afectados;
- las validaciones afectadas;
- y las migraciones necesarias.

Ejemplo:

```yaml
semantic_dependency:
  concept: archetype
  tes_source_version:
    lexicon: v3.1
    subject_ecosystem: v1.2

product_usage:
  entities:
    - archetype_reference
    - archetype_instantiation
  screens:
    - candidate_experience
    - journey_builder
    - simulation
  validations:
    - SEM-ARCH-001
    - SEM-ARCH-002
```

## Evaluación de cambios del TES

Cuando una fuente TES cambie, no debe actualizarse automáticamente el Builder.

Debe abrirse una revisión de impacto.

Preguntas mínimas:

- ¿Ha cambiado la definición?
- ¿Ha cambiado una distinción relevante?
- ¿Ha cambiado una relación?
- ¿Afecta al modelo funcional?
- ¿Afecta al modelo de datos?
- ¿Afecta a una pantalla?
- ¿Afecta a una validación?
- ¿Exige migración?
- ¿Puede mantenerse la baseline anterior durante la versión actual?

El resultado debe registrarse en:

```text
semantic-impact-log.md
```

## Conjunto mínimo de conceptos para la baseline v0.5

No hace falta derivar funcionalmente todo el TES.

Solo deben incorporarse al contrato los conceptos que crucen la frontera del producto.

Un concepto cruza la frontera cuando:

- aparece en la GUI;
- forma parte del modelo funcional;
- genera una entidad de datos;
- condiciona una regla;
- participa en una validación;
- o limita una capacidad técnica.

### Fundamento de la experiencia

- Experiencia.
- Propósito.
- Hipótesis de transformación.
- Estado inicial.
- Estado relacional deseado.
- Resultado.
- Medición mínima.
- Aprendizaje.

### Sistema de sujetos

- Arquetipo.
- Perfil de lealtad.
- Actor estructural.
- Actor operativo.
- Actor circunstancial.

El perfil de adopción debe mantenerse fuera del modelo del sujeto final de la experiencia. Puede ser relevante para la adopción organizativa del Builder, pero no debe confundirse con el perfil de lealtad.

### Arquitectura del recorrido

- Ecosistema.
- Recorrido.
- Secuencia.
- Etapa o estado.
- Transición.
- Progresión.
- Bifurcación.
- Condición de entrada.
- Condición de salida.

### Observación y evidencia

- Evento observable.
- Propiedad del evento.
- Fuente de evidencia.
- Fiabilidad.
- Latencia.
- Umbral.
- Patrón.

### Acción del sistema

- Regla de avance.
- Intervención.
- Incentivo de progresión.
- Recompensa de gratificación.
- Beneficio.
- Regla alternativa o fallback.

### Gobernanza propia del producto

- Experiencia candidata.
- Validación semántica.
- Validación técnica.
- Gap técnico.
- Simulación.
- Versión.
- Publicación.
- Pausa.
- Archivo.

Los conceptos de este último grupo son, principalmente, construcciones propias del Builder.

## Organización recomendada del contrato semántico

Para evitar fragmentación excesiva, no se recomienda crear un archivo por concepto durante la primera fase.

Estructura inicial:

```text
01-contrato-semantico/
├── README.md
├── tes-baseline-manifest.yaml
├── 01-experience-contract.md
├── 02-subjects-contract.md
├── 03-journey-contract.md
├── 04-event-evidence-contract.md
├── 05-progression-rule-contract.md
├── 06-incentive-reward-contract.md
├── 07-result-measurement-learning-contract.md
├── 08-gui-data-mapping.md
├── 09-semantic-validation-rules.md
└── 10-semantic-impact-log.md
```

Cada documento puede contener varias fichas atómicas relacionadas.

Esta estructura combina:

- precisión conceptual;
- legibilidad;
- relaciones entre conceptos;
- trazabilidad;
- y facilidad de mantenimiento.

## Registro de decisiones

Las decisiones del contrato deben utilizar cuatro estados:

- **crystallized**: decisión estable que no debe reabrirse sin evidencia nueva;
- **adjust**: formulación válida que necesita una corrección;
- **resolve**: decisión pendiente;
- **technical_verification**: depende de capacidades, datos o API.

Ejemplo:

```yaml
decision_id: DA-001
title: Independencia entre TES y TES Experience Builder
status: crystallized
date: 2026-07-16

decision:
  TES se mantiene como sistema ontológico y editorial autónomo.
  TES Experience Builder se desarrolla como producto derivado e independiente.
  El Builder consume una baseline versionada mediante un contrato semántico.
  Ninguna necesidad funcional, visual o técnica del Builder modifica
  automáticamente el núcleo TES.

consequences:
  - repositorios separados;
  - gobernanzas separadas;
  - trazabilidad explícita;
  - baselines semánticas versionadas;
  - evaluación de impacto ante cambios TES;
  - prohibición de copiar el núcleo como documentación viva del producto;
  - distinción entre conceptos TES y construcciones propias del Builder.
```

## Uso de las pantallas existentes

Las pantallas y maquetas ya creadas no deben abandonarse.

Deben cambiar de estatuto:

```text
Diseño vigente que debe seguir ampliándose
                ↓
Baseline visual previa a cristalización
                ↓
Activo que debe evaluarse contra el contrato semántico
```

La versión anterior debe:

- congelarse;
- inventariarse;
- documentarse;
- evaluarse;
- y rebasarse en una nueva versión.

Criterios de evaluación:

- conservar;
- conservar con ajuste;
- trasladar de nivel;
- dividir;
- fusionar;
- retirar;
- verificar técnicamente.

La GUI puede agrupar elementos para facilitar la operación, pero el modelo profundo debe conservar sus diferencias.

## Secuencia recomendada de trabajo

```text
Crear y gobernar el contrato semántico
        ↓
Definir relaciones e invariantes
        ↓
Construir el modelo funcional
        ↓
Definir el modelo de datos
        ↓
Revisar la arquitectura de pantallas
        ↓
Rebasar la maqueta existente
        ↓
Construir el prototipo interactivo
        ↓
Validar semántica, uso y ejecución
```

No debe rebasarse visualmente la pantalla antes de cerrar las decisiones semánticas que condicionan su estructura.

## Criterio de cierre de la guía

El contrato semántico puede considerarse suficientemente establecido para iniciar el rebase visual cuando:

- cada concepto TES utilizado por el Builder tiene una fuente trazable;
- cada concepto tiene una interpretación funcional explícita;
- las relaciones principales están definidas;
- los invariantes están registrados;
- las operaciones permitidas y prohibidas están diferenciadas;
- las entidades de datos principales están identificadas;
- existen reglas de validación;
- las construcciones propias del producto están etiquetadas;
- y las decisiones pendientes están visibles.

> [!summary]
> La ficha semántica es el átomo del contrato, pero el sistema completo exige relaciones, invariantes, operaciones, datos, validación y trazabilidad.
