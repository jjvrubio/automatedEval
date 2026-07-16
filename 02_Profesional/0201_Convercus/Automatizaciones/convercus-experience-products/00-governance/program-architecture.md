# Arquitectura conjunta: Convercus App y Experience Builder

## Estatuto del documento

Este documento amplía la propuesta estructural del TES Experience Builder para reconocer explícitamente dos productos relacionados, pero distintos:

1. **Convercus App**, dirigida al cliente final y prioritaria para demostraciones comerciales.
2. **Experience Builder**, dirigido a quienes diseñan y operan Experiences y estratégico como capacidad diferencial.

No se trata de fusionar ambos productos ni de convertir la App en una vista secundaria del Builder. La propuesta consiste en yuxtaponerlos dentro de un programa común, conservar sus límites y compartir únicamente los fundamentos, contratos y activos que realmente pertenezcan a ambos.

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
evento significativo
→ patrón
→ secuencia
→ progresión
→ resultado observado
→ medición
→ aprendizaje reutilizable
```

## Papeles de cada espacio de trabajo

VS Code debe convertirse en el espacio operativo y la fuente de verdad del programa, mientras que Lunacy, Pixelmator Pro, SVG y otras herramientas conservan funciones especializadas.

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
2. **Fundamento de producto**, como derivación mínima necesaria para operar Experiences.
3. **Convercus App**, como experiencia de cliente y demostrador comercial.
4. **Experience Builder**, como herramienta de diseño y gobierno.

El repositorio no debe duplicar el núcleo completo del TES. Debe contener referencias controladas, decisiones aplicables a producto, trazabilidad y contratos derivados.

## Jerarquía recomendada

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
├── 01-shared-foundation/
│   ├── README.md
│   ├── source-map.md
│   ├── experience-definition.md
│   ├── subject-system.md
│   ├── experience-ledger-mapping.md
│   ├── incentives-and-rewards.md
│   ├── workflows-relationship.md
│   └── glossary-product.md
│
├── 02-shared-contracts/
│   ├── experience-domain/
│   ├── events/
│   ├── workflows/
│   ├── incentives/
│   ├── rewards/
│   ├── measurements/
│   ├── learning/
│   └── api/
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

## Fundamento compartido

`01-shared-foundation` debe contener la traducción mínima del TES y de la comprensión de Experiences necesaria para ambos productos.

Su definición operativa de referencia será:

> Experiences es la capacidad de Convercus para configurar y operar transformaciones situadas: reconoce eventos significativos y patrones, los ordena en secuencias con progresión, coordina intervenciones según el estado de cada participación y permite distinguir resultado, medición y aprendizaje.

Esta capa no debe contener decisiones de pantalla específicas de ninguno de los productos.

## Contratos compartidos

`02-shared-contracts` debe expresar modelos y contratos sin acoplarlos a una interfaz.

Una primera división podría ser:

```text
ExperienceDefinition
ExperienceParticipation
SignificantEvent
PatternHypothesis
Sequence
ProgressionState
Intervention
Incentive
Reward
ObservedOutcome
Measurement
ReusableLearning
WorkflowReference
```

El Builder produce o modifica definiciones. La App consulta o representa participaciones. Ambos pueden utilizar los mismos identificadores y vocabulario sin compartir componentes de interfaz.

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

### Escenarios iniciales

La App debe demostrar, al menos:

- Circuito de decisión: ocasión.
- Maratón de Temporada.
- Desafío Activo o Aventura Familiar.

Cada escenario debe poder reconstruirse como transformación y no solamente como secuencia de pantallas.

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

## Flujo futuro entre productos

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

## Dos carriles de desarrollo

### Carril A — App urgente

```text
A0. Consolidar alcance y referencias.
A1. Crear aplicación React/TypeScript mobile-first.
A2. Implementar puntos, cupones, noticias y perfil con mocks.
A3. Incorporar motor de simulación de Experiences/Workflows.
A4. Implementar escenarios canónicos.
A5. Validar y preparar guion de demo.
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

## Secuencia inmediata recomendada

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

## Estructura mínima para empezar

La jerarquía completa no debe convertirse en trabajo burocrático. Para comenzar la App basta con:

```text
convercus-experience-products/
├── README.md
├── 00-governance/
│   ├── product-boundaries.md
│   └── source-precedence.md
├── 01-shared-foundation/
│   ├── experience-definition.md
│   └── workflows-relationship.md
├── 02-shared-contracts/
│   └── experience-domain/
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

## Resultado esperado

La estructura propuesta permite que la App avance con urgencia comercial sin perder la dirección estratégica del Builder.

La App será el **demostrador y lugar de vivencia**. El Builder será el **instrumento de diseño y gobierno**. Los contratos compartidos harán posible que ambas superficies hablen de la misma capacidad sin convertirse en el mismo producto.

La idea rectora queda ampliada así:

> **VS Code organiza y gobierna.**
>
> **El TES fundamenta.**
>
> **El Builder diseña y valida.**
>
> **Workflows ejecuta.**
>
> **La App hace visible y vivible.**
>
> **La API restringe y habilita.**
