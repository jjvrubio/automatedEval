---
title: "Arquitectura conjunta: Convercus App y Experience Builder"
aliases:
- "Arquitectura del programa Convercus Experience Products"
- "Demo Factory Architecture v0.5"
language: es
version: "v0.5"
status: "activo"
date: "2026-09-04"
project: "Convercus Experience Products"
document_type: "arquitectura de programa"
scope: "relación estructural, independencia y activos compartidos de Convercus App y Experience Builder"
repository_role: "documento rector de arquitectura conjunta"
semantic_authority: "producto subordinado a TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Arquitectura conjunta: Convercus App y Experience Builder

## Estatuto del documento

Este documento amplía la propuesta estructural del TES Experience Builder para reconocer explícitamente dos productos relacionados, pero distintos:

1. **Convercus App**, dirigida al cliente final y prioritaria para demostraciones comerciales.
2. **Experience Builder**, dirigido a quienes diseñan y operan Experiences y estratégico como capacidad diferencial.

No se trata de fusionar ambos productos ni de convertir la App en una vista secundaria del Builder. La propuesta consiste en yuxtaponerlos dentro de un programa común, conservar sus límites y compartir únicamente el contrato semántico, las traducciones funcionales y los activos que realmente pertenezcan a ambos.

El programa está anclado en el TES, sistema ontológico y editorial autónomo que permanece fuera de este repositorio y conserva siempre la autoridad. El código no incorpora su núcleo: trabaja contra una derivación controlada y versionada.

## Tesis estructural

Los dos productos representan perspectivas complementarias de una misma capacidad:

```text
Experience Builder                         Convercus App
Diseña y gobierna                          Hace visible y vivible
la transformación                         la transformación
        │                                         ▲
        ▼                                         │
Definición de Experience                   Participación individual
        │                                         ▲
        ▼                                         │
Workflows y capacidades Convercus ────────────────┘
```

El Builder trabaja sobre la definición, ejecutabilidad, simulación, validación y evolución de una Experience. La App trabaja sobre la participación concreta del cliente: situación, intervenciones, progresión, beneficios, resultados y continuidad.

La relación no es simplemente “backoffice y frontend”. Ambos productos tienen modelos de interacción, ciclos de vida y criterios de éxito diferentes.

## Por qué existen dos productos

### Producto 1 — Convercus App

La App responde a una necesidad comercial inmediata: disponer de una demostración convincente para clientes y prospectos.

Debe permitir experimentar cómo se presenta Convercus al usuario final mediante:

- Perfil y membresía.
- Puntos y niveles.
- Cupones.
- Noticias y actividad.
- Incentivos y recompensas.
- Intervenciones contextuales.
- Experiences visibles cuando resulte apropiado.
- Continuidad entre canales y momentos.

Su primera entrega será una simulación mobile-first con datos controlados. Posteriormente podrá conectarse de forma gradual a la API de staging.

### Producto 2 — Experience Builder

El Experience Builder responde a una necesidad estratégica: hacer productizable la capacidad diferencial de diseñar y orquestar Experiences sin reducirlas a campañas o workflows.

Debe permitir:

- Formular una Experience candidata.
- Reconocer el patrón que la justifica.
- Diseñar secuencias con progresión.
- Relacionar eventos y fuentes de evidencia.
- Configurar reglas e intervenciones.
- Incorporar incentivos y recompensas.
- Definir resultados observables.
- Preparar medición y aprendizaje.
- Simular, validar, publicar y versionar.
- Mapear el diseño a Workflows y otras capacidades de Convercus.

El Builder no es urgente para la primera demo, pero constituye una capacidad estratégica de medio plazo.

## Definición comparada

| Dimensión | Convercus App | Experience Builder |
|---|---|---|
| Usuario principal | Cliente o miembro del programa | Diseñador, consultor, marketer u operador |
| Perspectiva | Participación vivida | Definición y gobierno |
| Propósito inmediato | Demostrar valor al cliente | Diseñar la capacidad diferencial |
| Prioridad | Alta e inmediata | Estratégica a medio plazo |
| Superficie | Mobile-first | Escritorio, lienzo e inspector |
| Operaciones | Consultar, actuar, avanzar, disfrutar | Crear, editar, simular, validar, publicar |
| Unidad visible | Situación, intervención, próxima acción | Experience, recorrido, regla y capacidad |
| Relación con Workflows | Recibe sus efectos | Los configura o genera de forma mediada |
| API inicial | Mock; después staging | Mock y contrato; después APIs técnicas |
| Criterio de éxito | Demo comprensible y convincente | Diseño congruente, ejecutable y medible |

## Un principio que debe preservarse

> La App no debe reducir Experiences a tarjetas de retos, y el Builder no debe reducirlas a workflows visuales.

En la App, una Experience puede manifestarse mediante una noticia, una recomendación, una progresión, un cupón desbloqueado o una intervención contextual. No siempre necesita aparecer como objeto explícito.

En el Builder, el Workflow es parte de la ejecutabilidad, pero no sustituye la cadena experiencial completa:

```text
Event
→ Pattern
→ Sequence
→ Progression
→ Result
→ Measurement
→ Learning
```

La cadena expresa la referencia TES; no prescribe interfaces, DTOs, stores ni contratos software independientes.

## Papeles de cada espacio de trabajo

VS Code debe convertirse en el espacio operativo y la fuente de verdad de las especificaciones y artefactos de producto. No es la fuente de autoridad ontológica, que continúa en el TES externo. Lunacy, Pixelmator Pro, SVG y otras herramientas conservan funciones especializadas.

| Espacio | Función |
|---|---|
| VS Code | Repositorio, documentación, modelos, aplicaciones, pruebas y contratos |
| Git | Historial, ramas, versiones, comparación y recuperación |
| Lunacy | Sistema visual editable y pantallas del Builder |
| Pixelmator Pro | Tratamiento de imágenes y composiciones rasterizadas |
| SVG | Representación visual editable e interoperable |
| Codex | Arquitectura, implementación, pruebas, revisión y mantenimiento |
| Obsidian | Exploración y navegación del corpus TES amplio, si se mantiene |

## Cuatro ámbitos que no deben confundirse

La incorporación de la App exige distinguir cuatro ámbitos:

1. **TES**, como sistema ontológico y editorial amplio.
2. **Contrato semántico de producto**, como derivación TES mínima, congelada y versionada.
3. **Convercus App**, como experiencia de cliente y demostrador comercial.
4. **Experience Builder**, como herramienta de diseño y gobierno.

El repositorio no debe duplicar el núcleo completo del TES. Debe contener referencias controladas, decisiones aplicables a producto, trazabilidad y contratos derivados.

## Baseline arquitectónica v0.5

Esta versión consolida las fronteras aceptadas en ADR-001–005 y la evidencia de Sessions 5, 7, 11 y 13. No convierte los mecanismos de esos experimentos en componentes normativos.

La arquitectura contiene dos flujos distintos que convergen. La composición resuelve qué demo y runtime son efectivos. La evaluación contextual deriva un claim desde inputs semánticos/situados y evidencia factual. La evidencia no se fuerza dentro de la cadena de composición.

```text
FLUJO DE COMPOSICIÓN — ACCEPTED

TES semantic authority
        ↓ trazabilidad
Product interpretations and governed Experience references
        (distinct roles; maturity may differ)
        ↓ referenced or instantiated by
Scenario
        ↓ separado de
Demo Script ──public action──→ Runtime boundary
        ↓
Desired Demo Composition
        ↓ bootstrap / capability resolution
Effective Demo Composition
        ↓
Runtime state ──projection──→ AppSnapshot / Activity / UI


FLUJO DE EVALUACIÓN CONTEXTUAL — ACCEPTED BOUNDARY

Product semantic premises + situated context
                         ↘
                          Contextual evaluation
                         ↗
Neutral factual evidence + other authoritative premises in scope
                                      ↓
                         Derived evaluation claim
                                      ↓
                  Runtime/read-model use when applicable

POSSIBLE FUTURE RELATION — UNRESOLVED

Derived evaluation claim - - ? - -> [TES Event recognition boundary]
                                  (not a required gate; inputs and authority undecided)
```

El uso de un claim en runtime o read models no requiere reconocimiento de Evento TES por defecto. La relación lateral mostrada no afirma que el claim derivado sea el input único ni suficiente de una futura frontera de reconocimiento.

La convergencia no crea una capa soberana de autoridad. Las premisas pueden proceder de fuentes diferentes y cada una conserva su competencia, scope, procedencia y madurez. El claim derivado no puede superar esos límites conjuntamente. Una ausencia solo puede sostener una exclusión cuando existe base suficiente para excluir dentro del scope evaluado; knowledge insuficiente no se degrada a un negativo por conveniencia.

### ACCEPTED

- TES gobierna significado e invariantes semánticos; producto y técnica gobiernan sus traducciones sin redefinirlo (ADR-001).
- Composición, estado de runtime y read models son responsabilidades lógicamente separadas; Activity permanece como proyección (ADR-002).
- La intención solicitada y la composición efectiva resuelta son distintas (ADR-003).
- Experience Definition, Scenario y Demo Script conservan responsabilidades separadas; las acciones atraviesan una frontera pública cuyo comportamiento posee y valida el runtime (ADR-004).
- Evidencia factual neutral y evaluación relativa a Experience son distintas. El claim derivado queda acotado por sus premisas; insuficiencia no equivale a negativo; relevancia contextual no equivale a reconocimiento de Evento TES; Activity no origina ni fortalece autoridad (ADR-005).

### SUPPORTED

- La evaluación experimental puede mantener Evidence y ExperienceContext constantes y producir un claim distinto cuando cambia la autoridad clasificatoria disponible dentro de scope.
- La evaluación contextual probada no necesita branches por identificador de Experience, Activity, reconocimiento de Evento TES, taxonomy engine, registry ni provider architecture.

`SUPPORTED` registra evidencia experimental reproducible. No convierte las formas TypeScript utilizadas para obtenerla en arquitectura aceptada.

### PROVISIONAL

- La forma concreta de los inputs y outputs de evaluación, sus códigos, referencias y trazabilidad.
- La materialización y composición runtime de fuentes autoritativas.
- La representación de madurez de las Product Experience Definitions y de sus claims derivados.
- Los contratos actuales de `ExperienceDefinition`, Scenario, acciones, checkpoints, evidence y evaluation outcomes.
- La frontera que conecte eventualmente una evaluación con consumers de runtime o proyecciones productivas.

`PROVISIONAL` expresa utilidad parcial o evidencia limitada; no identifica servicios o aggregates que deban construirse.

### UNRESOLVED

- Topología de fuentes de autoridad clasificatoria.
- Taxonomías compartidas o alineación entre taxonomías.
- Autoridad, versionado y acreditación de mappings semánticos.
- Acreditación de autoridades, confianza, suficiencia y exhaustividad.
- Precedencia y resolución de claims conflictivos.
- Frontera y autoridad de reconocimiento de Eventos TES.
- Naming y representación de madurez de `ExperienceDefinition` candidata, validada y runtime.
- Preservación y UX de evaluaciones no resueltas en Activity y otras superficies.
- Contratos con APIs reales, persistencia, auditoría o reevaluación histórica.

Nada en `UNRESOLVED` representa un componente productivo existente. En particular, v0.5 no introduce `Authority Service`, `Classification Authority Layer`, registry, provider universal ni aggregate `AvailableAuthority`.

### NON-NORMATIVE / FUTURE PRODUCT DIRECTION

Las descripciones heredadas de capacidades, pantallas, estructuras de carpetas, escenarios potenciales, modos de datos, flujos futuros, roadmaps y secuencias de entrega conservan visión de producto e historia de planificación. No son arquitectura aceptada por aparecer en este documento activo. Sus verbos prospectivos expresan dirección o hipótesis y quedan subordinados a `ACCEPTED`, `SUPPORTED`, `PROVISIONAL` y `UNRESOLVED`.

En una revisión futura podrá separarse program architecture, product vision y roadmaps. Esa reorganización no forma parte de v0.5 ni de este parche.

## Jerarquía histórica/prospectiva — NON-NORMATIVE PRODUCT DIRECTION

En lugar de crear un repositorio centrado exclusivamente en el Builder, conviene utilizar una raíz que reconozca el programa de dos productos:

```text
convercus-experience-products/
│
├── README.md
├── CHANGELOG.md
├── ROADMAP.md
├── CONTRIBUTING.md
│
├── 00-governance/
│   ├── program-scope.md
│   ├── product-boundaries.md
│   ├── principles.md
│   ├── decision-register.md
│   ├── terminology-policy.md
│   ├── versioning-policy.md
│   └── source-precedence.md
│
├── 01-semantic-contract/
│   ├── README.md
│   ├── tes-baseline-manifest.yaml
│   ├── semantic-impact-log.md
│   ├── product-observations-log.md
│   ├── source-excerpts/
│   └── product-interpretations/
│
├── 02-shared-contracts/
│   ├── experience-domain/
│   └── workflows-relationship.md
│
├── 03-shared-assets/
│   ├── brand/
│   ├── tokens/
│   ├── icons/
│   ├── scenarios/
│   └── fixtures/
│
├── products/
│   ├── convercus-app/
│   │   ├── README.md
│   │   ├── ROADMAP.md
│   │   ├── docs/
│   │   ├── design/
│   │   ├── prototype/
│   │   ├── tests/
│   │   └── archive/
│   │
│   └── experience-builder/
│       ├── README.md
│       ├── ROADMAP.md
│       ├── docs/
│       ├── design/
│       ├── prototype/
│       ├── tests/
│       └── archive/
│
├── validation/
│   ├── shared/
│   ├── convercus-app/
│   └── experience-builder/
│
├── references/
│   ├── tes-source-index.md
│   ├── convercus-api/
│   ├── convercus-brand/
│   └── external-references/
│
└── archive/
    ├── pre-crystallization/
    ├── lovable/
    └── deprecated/
```

No es necesario crear o rellenar todas estas carpetas al comienzo. La estructura actúa como mapa de crecimiento y frontera entre productos.

## Gobierno común

La carpeta `00-governance` debe establecer:

- Qué pertenece al programa común.
- Qué pertenece exclusivamente a la App.
- Qué pertenece exclusivamente al Builder.
- Qué fuentes tienen precedencia.
- Qué términos están permitidos.
- Cómo se documentan decisiones transversales.
- Cómo se evita que la urgencia de la App deforme el Builder.
- Cómo se evita que la complejidad del Builder bloquee la App.

El documento `product-boundaries.md` será especialmente importante.

## Contrato semántico de producto

`01-semantic-contract` contiene la derivación mínima del TES aceptada para una baseline concreta. No es un fundamento autónomo ni una copia del núcleo TES. Sus extractos conservan procedencia y hash; cualquier cambio posterior se somete a evaluación de impacto.

Una interpretación de producto útil, siempre subordinada al contrato, será:

> Experiences es la capacidad de Convercus para configurar y operar transformaciones situadas: reconoce eventos significativos y patrones, los ordena en secuencias con progresión, coordina intervenciones según el estado de cada participación y permite distinguir resultado, medición y aprendizaje.

Esta capa no debe contener decisiones de pantalla específicas de ninguno de los productos ni construcciones técnicas presentadas como conceptos TES.

## Contratos compartidos

Los contratos compartidos solo se incorporan cuando una responsabilidad reutilizable entre App y Builder ha sido demostrada y existe realmente en el repositorio. La existencia de un concepto TES no implica por sí misma que deba materializarse como interfaz, DTO, store o contrato técnico independiente.

```text
Current shared contracts
→ only those actually demonstrated and present

Future shared contracts
→ evidence-driven
```

La futura colaboración entre Builder y App puede reutilizar identificadores o vocabulario sin presuponer desde ahora una lista de contratos compartidos.

## Activos compartidos

`03-shared-assets` debe contener solamente activos reutilizables:

- Identidad de Convercus.
- Tokens realmente comunes.
- Iconos.
- Escenarios canónicos.
- Fixtures de prueba.
- Traducciones.

No todos los componentes visuales serán compartidos. El Builder requiere lienzo, bloques, conectores e inspector. La App requiere navegación móvil, tarjetas, feeds, saldo, detalle de cupón y acciones de participación.

## Producto 1 — Estructura de Convercus App

```text
products/convercus-app/
├── README.md
├── ROADMAP.md
├── docs/
│   ├── product-scope.md
│   ├── personas.md
│   ├── information-architecture.md
│   ├── screen-map.md
│   ├── demo-script.md
│   ├── simulation-model.md
│   ├── staging-integration.md
│   └── unresolved-questions.md
├── design/
│   ├── foundations/
│   ├── components/
│   ├── screens/
│   └── references/
├── prototype/
│   ├── src/
│   ├── public/
│   ├── data/
│   └── tests/
├── tests/
│   ├── scenarios/
│   ├── responsive/
│   └── demo/
└── archive/
    └── lovable-baseline/
```

### Pantallas iniciales

La primera versión puede incluir:

1. Inicio de sesión simulado.
2. Inicio personalizado.
3. Cupones.
4. Detalle y código de cupón.
5. Noticias y actividad.
6. Detalle de noticia.
7. Perfil y nivel.
8. Experiences cuando deban mostrarse explícitamente.
9. Panel interno de simulación.

### Tres modos de datos

```text
Mock
  Datos fijos para construir y asegurar la demostración.

Simulation
  Eventos que alteran participación, progresión e intervenciones.

Staging
  Datos reales de cuenta, saldo, cupones, noticias y transacciones.
```

El modo mock debe seguir disponible aunque se active staging, para asegurar una demostración repetible.

### Escenarios potenciales y conceptos comerciales — NON-NORMATIVE PRODUCT DIRECTION

El backlog histórico de demo incluye elementos con estatutos semánticos diferentes:

- **Circuito de decisión: ocasión:** hipótesis de trabajo y escenario canónico inicial según su documentación vigente; esta mención no añade validación semántica.
- **Aventura Familiar:** Product Experience Definition candidate, `READY WITH EXPLICIT GAPS`, no ejecutable e interpretada contra TES.
- **Desafío Activo:** Product Experience Definition candidate, `READY WITH EXPLICIT GAPS`, no ejecutable e interpretada contra TES.
- **Maratón de Temporada:** concepto comercial/campaña/reto de fidelización; no asumir que sea una Experience validada.

La inclusión en una demo no modifica el estatuto semántico del artefacto. Cualquier narración presentada como Experience debe justificar su transformación y no limitarse a una secuencia de pantallas.

### Panel interno de simulación

El panel permitirá activar eventos sin confundirlos con acciones normales del cliente:

- Escanear una prenda.
- Visitar una tienda.
- Comprar en una categoría.
- Completar una actividad.
- Alcanzar un umbral.
- Recibir o utilizar un cupón.
- Avanzar el tiempo.
- Reiniciar el escenario.

Debe mostrar qué patrón, estado, Workflow e intervención resultan afectados.

## Producto 2 — Estructura del Experience Builder

La estructura originalmente propuesta para `tes-experience-builder` se conserva dentro de su producto:

```text
products/experience-builder/
├── README.md
├── ROADMAP.md
├── docs/
│   ├── product-baseline/
│   ├── functional-model/
│   ├── information-architecture/
│   ├── technical-contract/
│   ├── data-model/
│   └── validation/
├── design/
│   ├── design-system/
│   ├── screens/
│   ├── prototypes/
│   └── assets/
├── prototype/
│   ├── src/
│   ├── public/
│   ├── data/
│   └── tests/
├── tests/
└── archive/
    └── v0.4.1-baseline/
```

La baseline v0.4.1 debe congelarse como evidencia, comparación y activo histórico.

## Qué hacer con las pantallas existentes del Builder

Las pantallas actuales deben conservarse en tres condiciones.

### Evidencia de diseño

Demuestran que se han explorado:

- Biblioteca, lienzo e inspector.
- Etapas y bifurcaciones.
- Reglas de avance.
- Diferencia visual entre eventos, incentivos y recompensas.
- Simulación y validación técnica.

### Baseline de comparación

La v0.4.1 debe permitir decidir qué conservar, recolocar o retirar para hacer el producto congruente con el TES cristalizado.

### Activo histórico versionado

No debe corregirse silenciosamente. Debe congelarse, etiquetarse y acompañarse de problemas conocidos.

## Qué hacer con Lovable

El trabajo de Lovable pertenece al historial del producto App, no al Builder.

Debe conservarse como:

- Baseline visual.
- Fuente de decisiones previas.
- Referencia para comparar navegación y presentación.
- Posible origen de activos reutilizables.

No debe gobernar el modelo de dominio ni la arquitectura del nuevo prototipo.

## Qué puede compartir la App con el Builder

| Elemento | Compartido | Observación |
|---|---:|---|
| Definición de Experience | Sí | Sin decisiones de interfaz |
| Léxico de producto | Sí | Con políticas de precedencia |
| Identificadores de dominio | Sí | Contrato estable |
| Escenarios canónicos | Sí | Diferentes vistas del mismo escenario |
| Fixtures | Sí | Definición y participación separadas |
| Mapa de API | Sí | Adaptadores específicos por producto |
| Identidad de marca | Sí | Componentes distintos |
| Componentes React | Parcialmente | Solo primitivas realmente comunes |
| Navegación | No | Usuarios y tareas diferentes |
| Estado de interfaz | No | Ciclos diferentes |
| Workflow visual | No | Propio del Builder |
| Panel de simulación | Parcialmente | Diferente profundidad y propósito |

## Flujo futuro entre productos — NON-NORMATIVE PRODUCT DIRECTION

Cuando ambos productos maduren, el flujo deseable será:

```text
Builder
  configura una Experience
        ↓
Validación conceptual y técnica
        ↓
Mapeo a Workflows y capacidades Convercus
        ↓
Publicación
        ↓
Participación de una cuenta
        ↓
App
  presenta situación, intervención y próxima acción
        ↓
Eventos y resultados
        ↓
Medición y aprendizaje
        ↓
Builder
  permite revisar o versionar la definición
```

La primera versión de la App simulará este ciclo sin requerir que el Builder esté implementado.

## Dos carriles de desarrollo — NON-NORMATIVE PRODUCT DIRECTION

### Carril A — App urgente

```text
A0. Consolidar alcance y referencias. [completado]
A1. Crear aplicación React/TypeScript mobile-first y modo de presentación iPhone. [completado]
A2. Implementar puntos, cupones, noticias y perfil con mocks.
A3. Incorporar comportamientos de simulación acotados a escenarios demostrados, mediante runtime boundaries reversibles y sin asumir un Experience engine o rules engine general.
A4. Implementar escenarios canónicos.
A5. Validar, preparar guion de demo e instalar y probar la PWA en un iPhone real.
A6. Conectar staging por módulos.
```

### Carril B — Builder estratégico

```text
B0. Congelar baseline v0.4.1.
B1. Inventariar y evaluar activos.
B2. Completar cristalización semántico-funcional v0.5.0.
B3. Rebasar visualmente Journey Builder.
B4. Implementar Experiencia candidata.
B5. Conectar ambas superficies.
B6. Construir simulación y validación técnica.
B7. Mapear y ejecutar Workflows reales.
```

El carril B no debe bloquear A. Las decisiones compartidas mínimas se fijan como contratos provisionales versionados y se revisan explícitamente cuando el Builder avance.

## Secuencia inmediata recomendada — NON-NORMATIVE PRODUCT DIRECTION

```text
1. Adoptar el marco de dos productos.
2. Conservar la documentación y maquetas actuales del Builder.
3. Registrar sus fuentes y su estatuto.
4. Crear la estructura mínima común.
5. Abrir el carril de Convercus App.
6. Crear el prototipo App sin dependencia del Builder.
7. Reutilizar escenarios y contratos, no pantallas del Builder.
8. Mantener una lista explícita de decisiones compartidas provisionales.
```

## Estructura mínima para empezar — NON-NORMATIVE PRODUCT DIRECTION

La jerarquía completa no debe convertirse en trabajo burocrático. Para comenzar la App basta con:

```text
convercus-experience-products/
├── README.md
├── 00-governance/
│   ├── product-boundaries.md
│   └── source-precedence.md
├── 01-semantic-contract/
│   ├── README.md
│   ├── tes-baseline-manifest.yaml
│   ├── source-excerpts/
│   └── product-interpretations/
├── 02-shared-contracts/
│   ├── experience-domain/
│   └── workflows-relationship.md
├── 03-shared-assets/
│   └── scenarios/
└── products/
    ├── convercus-app/
    │   ├── README.md
    │   ├── docs/
    │   └── prototype/
    └── experience-builder/
        ├── README.md
        └── archive/
            └── v0.4.1-baseline/
```

Las demás carpetas se crearán cuando exista trabajo real que depositar en ellas.

## Criterios para evitar contaminación entre productos

1. Ningún componente de la App se comparte solo porque visualmente se parezca a uno del Builder.
2. Ningún concepto del Builder se expone al cliente sin traducción a lenguaje comprensible.
3. Ninguna limitación de la demo se incorpora como restricción permanente del dominio.
4. Ninguna hipótesis TES se presenta como capacidad técnica confirmada sin validación.
5. Ningún Workflow se equipara por sí mismo a una Experience.
6. Ninguna Experience se obliga a aparecer como reto o tarjeta en la App.
7. Ningún avance del Builder retrasa el modo mock de la App.
8. Ningún dato sensible de staging se introduce en el frontend.

## Resultado esperado — NON-NORMATIVE PRODUCT DIRECTION

La estructura propuesta permite que la App avance con urgencia comercial sin perder la dirección estratégica del Builder.

La App será el **demostrador y lugar de vivencia**. El Builder será el **instrumento de diseño y gobierno**. Los contratos compartidos harán posible que ambas superficies hablen de la misma capacidad sin convertirse en el mismo producto.

La idea rectora queda ampliada así:

> **VS Code organiza y gobierna.**
>
> **El TES define y conserva la autoridad ontológica.**
>
> **El Builder diseña y valida.**
>
> **Workflows ejecuta.**
>
> **La App hace visible y vivible.**
>
> **La API restringe y habilita.**
