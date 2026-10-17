---
title: "ADR-002 — Separación lógica de composición, estado de runtime y read models"
aliases:
- "Logical Separation of Composition, Runtime State and Read Models"
language: es
version: "v1.0"
status: "aceptado"
date: "2026-09-03"
project: "Convercus Experience Products"
document_type: "registro de decisión de arquitectura"
scope: "separación de responsabilidades entre intención de demo, estado mutable de ejecución y estructuras de presentación"
repository_role: "decisión de arquitectura de Convercus App"
semantic_authority: "construcción técnica de producto subordinada; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
decision_id: "ADR-002"
decision_status: "accepted"
---

# ADR-002 — Separación lógica de composición, estado de runtime y read models

## Estado

**Aceptado.** Esta decisión formaliza la decisión revisada de Session 3 anteriormente asociada a ADR-005.

## Contexto

El prototipo actual utiliza `AppSnapshot` como respuesta del adaptador y modelo directo de lectura, mientras el mock modifica elementos de Activity dentro del propio snapshot. A medida que una demo incorpora acciones, reset, fuentes externas o simulación, esa coincidencia puede convertir la vista en autoridad accidental sobre el estado. El extremo contrario —crear de antemano almacenes canónicos, event logs y múltiples proyecciones— impondría una plataforma innecesaria a demos estáticas o live.

Las demos previstas no comparten la misma necesidad de estado. Una demo mock puede ser enteramente local; una híbrida puede combinar una referencia externa con un overlay; una live puede dejar la autoridad en el sistema remoto. La arquitectura necesita separar responsabilidades sin imponer una materialización física uniforme.

## Decisión

Demo Factory distingue lógicamente tres planos:

1. **Composición/configuración:** declara qué demo se pretende, sus referencias, módulos, capacidades y política aplicable.
2. **Estado de runtime:** conserva o referencia el estado mutable controlado durante la ejecución cuando la demo lo necesita.
3. **Read models/proyecciones:** prepara estructuras para la UI y la presentación, entre ellas `AppSnapshot` y Activity.

La separación es de autoridad y responsabilidad, no una obligación de crear tres stores, bases de datos ni copias de todos los datos.

La realización mínima depende del modo:

| Modo | Realización mínima permitida |
|---|---|
| Static/mock | Un read model directo puede ser suficiente. |
| Simulation | Estado local controlado más las proyecciones que consuma la UI. |
| Hybrid | Referencia a estado externo más overlay local y proyección efectiva. |
| Live | La fuente externa puede seguir siendo autoritativa; localmente puede existir solo caché o read model. |

Solo se introduce estado canónico local cuando acciones, simulación, auditoría o reset lo requieren. Solo se añade una proyección separada cuando reduce acoplamiento o resuelve una necesidad de presentación concreta.

## Alcance de autoridad

| Plano | Decide | No decide |
|---|---|---|
| Composición/configuración | Qué artefactos y capacidades desea una demo | Disponibilidad real del deployment ni estado de sesión |
| Estado de runtime | Estado mutable local o referencias a estado externo durante una ejecución | Identidad semántica de Experience ni estructura visual final |
| Read model/proyección | Forma consumible por una superficie concreta | Verdad factual, reglas de dominio o autoridad del origen |
| Fuente externa | Estado real dentro de su contrato y ámbito | Configuración completa de la demo ni significado TES por sí sola |

## Consecuencias explícitas

### `AppSnapshot`

- Se conserva como read model de la aplicación, no como contrato universal de estado canónico.
- Puede derivarse de estado local, componerse desde varias fuentes o recibirse directamente de un proveedor estático.
- Sus campos orientados a presentación —por ejemplo fechas formateadas, etiquetas, iconos y tonos— no deben convertirse en hechos de dominio por conveniencia.
- La UI puede depender de `AppSnapshot`; las reglas o acciones no deben depender de volver a interpretar su copy visual.

### Activity

- Activity permanece como proyección/read model.
- Puede mezclar elementos proyectados desde datos reales, evidencias mock o acciones simuladas solo si preserva procedencia suficiente y el disclosure apropiado.
- Añadir una tarjeta a Activity no constituye por sí mismo registrar evidencia factual ni reconocer un Evento TES.
- El experimento mínimo puede proyectar directamente desde estado local sin crear un almacén general de occurrences o evidencias.

### Reset

- El reset determinista se limita al estado bajo control local de la demo.
- Una demo estática puede reconstruir su snapshot inicial; una simulación puede resembrar su estado desde fixtures versionados.
- El estado live externo no se borra ni se promete reiniciar mediante este contrato.
- Una demo híbrida debe declarar si el reset elimina solo el overlay, utiliza un sandbox controlado o requiere un procedimiento externo explícito.

### Fuentes externas

- Una fuente externa puede permanecer autoritativa y ser referenciada en vez de duplicada.
- Caché, snapshot o overlay local deben declarar su relación con la fuente y tolerar latencia o staleness según una política explícita.
- La composición solicitada no concede capacidad de mutar o reiniciar la fuente.
- La reconciliación entre fuentes, si llega a ser necesaria, será una decisión posterior basada en contratos reales.

### Plataforma de eventos

- Esta separación no autoriza ni exige event sourcing, un event bus, un occurrence store o una canalización universal de cuatro objetos.
- Un array local o una estructura in-memory son suficientes para el experimento si expresan la autoridad requerida.
- La persistencia, auditoría y replay solo se incorporarán cuando un caso verificable los exija.
- Las distinciones semánticas pueden preservarse mediante tipos, referencias o metadatos sin materializar cada concepto como entidad persistida.

## Consecuencias generales

### Positivas

- La UI deja de ser autoridad accidental sobre el estado mutable.
- Cada modo puede usar la realización más pequeña compatible con sus garantías.
- Las fuentes live no se duplican por defecto ni reciben promesas falsas de reset.
- Las proyecciones pueden evolucionar con la superficie sin redefinir evidencia o semántica.
- El experimento puede retirarse sin migraciones ni limpieza de infraestructura.

### Costes y obligaciones

- Bootstrap y proveedores deben hacer explícito qué plano satisfacen.
- Cuando exista estado mutable, las acciones deben atravesar un límite público y no mutar read models desde componentes.
- La procedencia debe conservarse al mezclar fuentes o modos.
- Los tests deben verificar determinismo local y evitar asumirlo para estado externo.
- Puede haber transformaciones adicionales entre estado y UI, aunque deben mantenerse mínimas.

## Interpretaciones prohibidas

Esta decisión no implica:

- tres bases de datos, tres stores ni tres copias de cada dato;
- un estado canónico local obligatorio en todos los modos;
- que `AppSnapshot` sea un agregado de dominio o fuente factual;
- que Activity sea un ledger, un store de evidencia o una lista de Eventos TES;
- que reset pueda revertir sistemas live;
- que toda fuente deba implementar `getSnapshot/dispatch/reset`;
- que separar planos justifique construir una plataforma genérica de eventos antes de necesitarla.

## Implicaciones de versionado

- La versión de una composición identifica intención y referencias, no captura automáticamente el estado vivo.
- Los fixtures o checkpoints utilizados para reset deben estar versionados o fijados de forma reproducible.
- Los esquemas de runtime y de read model pueden evolucionar de manera independiente si sus adaptadores o proyectores mantienen contratos explícitos.
- Un snapshot persistido, si algún modo lo requiere en el futuro, debe declarar origen, versión de proyección y momento de captura.
- Cambiar una proyección no reinterpreta el estado histórico ni altera por sí mismo la baseline TES.

## Condiciones de reconsideración

La decisión debe revisarse si:

- las primeras demos no pueden expresar acciones y reset sin duplicación material o sincronización insegura;
- una API verificada exige una topología incompatible con la separación lógica;
- los read models directos no pueden preservar la procedencia necesaria;
- requisitos de auditoría, privacidad o replay hacen imprescindible una materialización adicional;
- el coste de mantener límites explícitos supera de forma demostrable el riesgo de mezclar autoridades;
- un caso live requiere semántica transaccional entre estado externo y overlay local que esta decisión no cubre.

## Revisión de aceptación

Permanece abierta la cantidad exacta de interacción local de las primeras demos, pero no impide aceptar la decisión: el ADR permite tanto read models directos como estado local cuando sea necesario y no fija una topología física prematura.
