---
title: "Session 4 — Hipótesis y experimento mínimo reversible de Demo Factory"
aliases:
- "ADR Formalization and Minimum Reversible Experiment Specification"
- "Demo Factory Architecture v0.2 experiment"
language: es
version: "v1.0"
status: "especificado; no implementado"
date: "2026-09-03"
project: "Convercus App"
document_type: "especificación de hipótesis y experimento de arquitectura"
scope: "prueba reversible de composición multidemostración, separación conceptual, procedencia y resolución externa de proveedores"
repository_role: "entrada de implementación para Session 5"
semantic_authority: "construcción experimental de producto subordinada; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 4 — Hipótesis y experimento mínimo reversible de Demo Factory

## 1. Conclusión ejecutiva de Session 4

La Arquitectura v0.2 está suficientemente madura para aceptar solo dos decisiones:

1. el TES gobierna significado, relaciones e invariantes semánticos dentro de un ámbito explícitamente acotado;
2. composición, estado de runtime y read models son autoridades lógicamente distintas sin requerir tres stores.

Las demás decisiones conservan incertidumbre sobre granularidad, sujetos, fuentes y contratos reales. Se registran como H1–H4 y no como ADR aceptados.

El experimento propuesto aplica el principio **«dos demos, un núcleo, cero forks»**. Mantiene Retail cerca del prototipo y añade una configuración Hospitality que cambia marca, contenido, fixtures, módulos, contexto, sujetos y checkpoint. Un bootstrap seleccionado por identificador de demo resuelve referencias y puertos mock antes de renderizar `App`. El experimento no introduce backend, persistencia, integración live, motor completo de Experiences ni store general de evidencias.

La prueba es reversible porque todo el estado nuevo permanece in-memory y todos los artefactos nuevos son configuración o código local del prototipo. No exige migraciones, limpieza de API, cambios TES ni cambios en Experience Builder.

## 2. ADR formalizados

- [ADR-001 — Autoridad semántica acotada del TES](../../../00-governance/decisions/ADR-001-bounded-tes-semantic-authority.md).
- [ADR-002 — Separación lógica de composición, estado de runtime y read models](../../../00-governance/decisions/ADR-002-logical-separation-composition-runtime-read-models.md).

No se acepta ningún otro ADR en esta sesión.

## 3. Hipótesis provisionales H1–H4

### H1 — Demo Manifest + composición efectiva de bootstrap

**Hipótesis.** Un manifiesto de demo pequeño y versionado puede declarar la composición lógica deseada, mientras una política de bootstrap/deployment resuelve la composición efectiva.

**Clasificación.** Inferencia arquitectónica provisional; no es concepto TES ni decisión aceptada.

**Forma mínima que se probará.**

- `schemaVersion`, `demoId`, `prospectId`, `locale` y módulos visibles.
- Referencias versionadas a marca, fixture, Scenario y Demo Script; Scenario y Script son opcionales.
- Solicitudes lógicas de capacidades, sin clases, endpoints, tokens ni secretos.
- Un catálogo local de artefactos y un registro local de proveedores que pertenecen al bootstrap, no al manifiesto.
- Una salida efectiva que contiene artefactos validados, capacidades resueltas y procedencia.

**Preguntas sometidas a prueba.**

- ¿Permite el contrato dos manifiestos con el mismo `prospectId` y distinto `demoId`?
- ¿Las referencias versionadas evitan que el manifiesto copie artefactos completos?
- ¿Puede distinguirse una capacidad solicitada de una resuelta?
- ¿Falla el arranque con un error explícito ante referencia inexistente o incompatible?
- ¿Permanece el manifiesto libre de secretos y de implementaciones concretas?

No se decidirán aún granularidad futura, resolución remota, firma de artefactos, deployment productivo ni multitenancy.

### H2 — Separación Scenario / Experience / Demo Script

**Hipótesis.** Experience Definition, Scenario y Demo Script permanecen distintos y pueden depender de acuerdo con:

```text
Experience Definition ← Scenario ← Demo Script
```

**Clasificación.** Interpretación de producto provisional subordinada al TES.

**Forma mínima que se probará.**

- Retail omite Scenario y Demo Script para demostrar que ambos son opcionales.
- Hospitality incluye un Scenario que referencia una Experience Definition mínima y aporta contexto `booking`/`stay`, sujetos y checkpoint inicial.
- Hospitality incluye un único Demo Script que referencia el Scenario y el checkpoint.
- El Script contiene identificadores y argumentos de acciones públicas; no incluye reducers, reglas de progresión ni mutaciones de estado.
- Dos checkpoints distintos deben poder expresarse como referencias, pero solo se implementará uno en Hospitality.

**Sujetos mínimos de Hospitality.**

- una persona que reserva, representada como `subjectRef` con tipo `person`;
- un grupo acompañante, representado como `subjectRef` con tipo `group`;
- una reserva y una estancia como referencias de contexto, no como miembros ficticios adicionales.

No se generalizará el ciclo de vida de participación ni se declarará `memberId` como identificador universal. La relación formal entre sujeto individual, colectivo y participación sigue fuera de alcance.

### H3 — Evidence / Occurrence / TES Event / proyección Activity

**Hipótesis.** El producto necesita preservar la distinción entre entrada factual/evidenciaria e interpretación como Evento TES, pero no necesita persistir cada concepto como objeto independiente.

**Clasificación.** Interpretación de producto y arquitectura provisional.

**Forma mínima que se probará.**

- Una acción pública de Hospitality aporta una entrada de evidencia in-memory referida al check-in de una reserva.
- La entrada conserva identidad, tipo, instante, fuente, fiabilidad y referencias de contexto.
- Puede adjuntar una interpretación TES separada y explícita; esa interpretación no sobrescribe la evidencia.
- El estado local controlado guarda solo la estructura mínima necesaria durante la sesión.
- `ActivityItem` se calcula mediante una función de proyección y mantiene procedencia suficiente para diferenciar fixture, mock y acción simulada.
- La prueba demuestra que puede existir evidencia sin Evento TES y que, cuando existe interpretación, ambos conceptos siguen distinguibles.

No se crearán `OccurrenceStore`, `EvidenceStore`, event log, deduplicación general, correcciones, replay ni persistencia. Tampoco se intentará modelar todas las formas de occurrence contempladas por Session 3.

### H4 — Resolución de proveedores por capacidad

**Hipótesis.** Los proveedores deben resolverse fuera de `App.tsx`, potencialmente por capability/port, en vez de asumir un adaptador universal por demo.

**Clasificación.** Inferencia arquitectónica provisional.

**Forma mínima que se probará.**

- `App.tsx` recibe un runtime ya resuelto y no instancia `MockDataAdapter`.
- El manifiesto solicita dos puertos lógicos mínimos: lectura del snapshot y acciones de demo.
- Bootstrap resuelve ambos desde un registro local; el mismo `MockDataAdapter` puede satisfacer los dos para evitar abstracciones innecesarias.
- Cada binding efectivo declara `capabilityId`, `providerId`, modo y procedencia.
- Los fixtures se inyectan al constructor del mock y no viven dentro de su implementación.

No se diseñan puertos de producción, reconciliación de fuentes, selección dinámica remota ni un adaptador universal nuevo. El experimento solo introduce la costura necesaria para sacar la resolución de `App.tsx`.

## 4. Estado de las analíticas experimentales

### Experience-portfolio observation overlap

**Estado:** idea analítica experimental; no ADR, contrato ni feature.

Exploraría el solapamiento y las occurrences observadas no relacionadas entre evaluaciones de Experiences dentro de límites explícitos de periodo, fuente, escenario, población y consentimiento. No expresa calidad, amplitud ni valor de una Experience.

### Experience evidence sufficiency profile

**Estado:** idea analítica experimental; no ADR, contrato ni feature.

Representaría evidencia suficiente, insuficiente, contradictoria o pendiente, preservando criticidad, dependencias y calidad. No es un porcentaje, no equivale a TES Progression y no determina Completion o Result.

Ninguna de las dos ideas se implementará ni se añadirá a tipos, UI, fixtures o pruebas de Session 5.

## 5. Especificación del experimento mínimo reversible

### 5.1 Pregunta experimental

¿Puede el núcleo actual arrancar una demo Retail y otra Hospitality a partir de composición declarada y resuelta externamente, preservando separaciones semánticas mínimas, sin introducir forks, estado productivo ni arquitectura genérica anticipada?

### 5.2 Principio y límites

**Dos demos. Un core. Cero forks.**

El mismo bundle y el mismo árbol de componentes se ejecutarán con `?demo=retail-baseline` o `?demo=hospitality-stay`. Cambiar la demo significa cambiar el identificador de arranque, no editar ni recompilar `App.tsx`.

La ausencia de `demo` seleccionará `retail-baseline`. Un valor desconocido detendrá el bootstrap y mostrará un error explícito; no caerá silenciosamente en Retail.

### 5.3 Demo A — Retail baseline

Se preservan, en lo posible, comportamiento y presentación actuales:

- `demoId`: `retail-baseline`;
- `prospectId`: `convercus-retail-reference`;
- marca: Convercus existente;
- locale: `es`;
- módulos: home, benefits, activity y profile;
- contenido y datos: fixture extraído del `initialSnapshot` actual;
- capacidades: lectura mock y acciones mock;
- Scenario: ausente;
- Demo Script: ausente;
- reset: reseed determinista del fixture Retail.

La prueba de cardinalidad crea en test un segundo manifiesto mínimo con el mismo `prospectId` y otro `demoId`; no se añade una tercera demo ejecutable.

### 5.4 Demo B — Hospitality

Configuración deliberadamente distinta:

- `demoId`: `hospitality-stay`;
- `prospectId`: `aurora-hospitality-group`;
- marca ficticia: `Aurora Stay`, con logotipo y roles de color propios;
- locale: `es` para no convertir internacionalización en variable del experimento;
- módulos: home, activity y profile; benefits queda desactivado;
- contenido: bienvenida de estancia, información de llegada y actividad hotelera;
- fixture: persona, saldo, contenido y actividad diferentes de Retail;
- Scenario: `arrival-and-stay`, con `bookingRef`, `stayRef`, persona que reserva y grupo acompañante;
- Experience Definition referenciada: una definición mínima de bienvenida situada validada contra `TES_CONVERCUS_BUILDER_2026_07_R1`;
- checkpoint inicial: `pre-arrival-confirmed`;
- Demo Script: un paso ejecutable, `confirm-check-in`, que invoca la acción pública `recordEvidence`;
- módulos y navegación: resueltos desde la composición efectiva;
- reset: reseed determinista del fixture Hospitality.

El Scenario aporta contexto y sujetos; no implementa el motor de Experience. La Experience Definition no contiene contenido de marca. El Script no decide progresión y no accede al estado interno del mock.

### 5.5 Manifiesto deseado y composición efectiva

Flujo mínimo:

```text
demoId de arranque
        ↓
catálogo de Demo Manifests versionados
        ↓ validación de referencias
catálogos locales de marca, fixture, Experience, Scenario y Script
        ↓ resolución de capacidades
registro local de providers
        ↓
ResolvedDemoRuntime
        ├── brand + assets
        ├── locale + visibleModules
        ├── readPort
        ├── actionPort
        ├── requestedCapabilities
        ├── resolvedCapabilities + provenance
        └── Scenario/Script opcionales
        ↓ inyección
App
```

El manifiesto declara referencias y necesidades. Bootstrap posee catálogos, política, selección y fallos. El provider posee comportamiento mock. `App` solo consume el runtime efectivo.

### 5.6 Contratos mínimos del experimento

Solo se introducirán estas formas conceptuales:

- `DemoManifest`: identidad, versión, prospecto, referencias, módulos y capability requests.
- `ArtifactRef`: cadena opaca con identificador y versión; no un sistema general de paquetes.
- `ScenarioDefinition`: Experience refs, context refs, subject refs y checkpoints.
- `DemoScript`: Scenario ref, initial checkpoint y lista de public actions.
- `EvidenceInput` y `TesEventInterpretation`: estructuras distintas, con interpretación opcional.
- `ResolvedCapability`: solicitud, proveedor, modo y procedencia efectivos.
- `ResolvedDemoRuntime`: dependencias listas para `App`.
- `AppReadPort` y `DemoActionPort`: las dos costuras que el prototipo usa realmente.

No se añadirá un contenedor de inyección, un framework de plugins, un bus de comandos ni un catálogo remoto.

### 5.7 Estado, proyección y reset

`MockDataAdapter` recibirá un fixture inyectado y mantendrá una copia in-memory de su estado. `getSnapshot()` proyectará un `AppSnapshot`; no devolverá la referencia interna. `recordEvidence()` modificará solo el estado local mediante el puerto público. Activity se reconstruirá como read model a partir de registros del fixture y de la evidencia de sesión.

`reset()` volverá a clonar el fixture que corresponde a la demo resuelta. No tocará almacenamiento del navegador, backend ni fuente externa. Dos instancias creadas desde el mismo fixture producirán el mismo snapshot inicial.

### 5.8 Selección, errores y aislamiento

- La selección explícita usa el query parameter `demo` en este experimento; no constituye una decisión de deployment futuro.
- La validación ocurre antes de renderizar la App.
- Referencias ausentes, versiones no soportadas, módulos desconocidos y capabilities sin provider producen errores identificables con el `demoId` y la referencia causante.
- No se usa fallback para corregir manifiestos inválidos.
- Cada bootstrap crea una instancia nueva del provider con un clone del fixture; no existe singleton mutable compartido entre demos.
- Los tests recorren snapshots serializados y texto visible para detectar identificadores, nombres y contenidos del otro prospecto.

### 5.9 Reversibilidad y retirada

La retirada completa consiste en:

1. borrar los archivos nuevos enumerados en 7.1;
2. revertir únicamente los cambios mínimos enumerados en 7.2;
3. restaurar la instanciación actual de `MockDataAdapter`, la marca Convercus y el render síncrono actuales.

No hay base de datos, esquema persistido, servicio, endpoint, secreto, cola, API, dato remoto ni artefacto TES que limpiar. Experience Builder no se toca. La UI conserva las mismas páginas y componentes; solo recibe dependencias en vez de importarlas, por lo que el rollback no es un refactor transversal.

### 5.10 No objetivos

Quedan excluidos:

- integración live con API Convercus;
- autenticación de producción;
- backend o persistencia;
- event sourcing, bus de eventos o store general de occurrences/evidencias;
- motor completo de Experiences o ciclo de participación completo;
- analíticas de coverage;
- Experience Builder;
- multitenancy de producción;
- reconciliación de fuentes híbridas;
- refactor amplio de componentes React;
- reescritura de design system;
- framework global de estado;
- i18n general;
- parametrización runtime del manifiesto PWA por prospecto.

La metadata PWA se neutralizará como «Demo Factory» durante el experimento para evitar identidad de prospecto cruzada; hacer instalables PWAs independientes por demo queda fuera de alcance.

## 6. Criterios de aceptación

| # | Criterio | Prueba prevista |
|---|---|---|
| 1 | El mismo core arranca ambas demos. | Test de bootstrap y smoke render para `retail-baseline` y `hospitality-stay` usando la misma exportación `App`. |
| 2 | Cambiar demo no exige editar aplicación. | Arrancar con dos valores de `?demo=`; ningún branch por prospecto existe en `App.tsx`. |
| 3 | No hay fuga de marca, contenido o fixtures. | Aserciones negativas cruzadas sobre runtime y DOM: Retail no contiene `Aurora`; Hospitality no contiene nombres, IDs, cupones ni logo del fixture Retail. |
| 4 | Un prospecto puede poseer varias demos. | Validar en test dos manifiestos de distinto `demoId` con igual `prospectId`. |
| 5 | El manifiesto declara composición deseada. | Test estructural sobre referencias, módulos y capability requests, sin provider concreto ni secreto. |
| 6 | Bootstrap resuelve composición efectiva. | Aserciones sobre artefactos, puertos y `resolvedCapabilities` del runtime. |
| 7 | Referencias inválidas o ausentes fallan explícitamente. | Tests por brand ref, fixture ref, Scenario ref, Script ref, Experience ref y capability sin provider. |
| 8 | La marca procede de configuración. | Render con nombre, logo y variables CSS de cada marca; búsqueda estática impide identidad Convercus literal en `App.tsx`. |
| 9 | Los fixtures son externos al mock. | `MockDataAdapter` requiere fixture en constructor; búsqueda estática y test confirman ausencia de `initialSnapshot` embebido. |
| 10 | El provider se resuelve fuera de `App.tsx`. | `App` recibe `ResolvedDemoRuntime`; test de arquitectura comprueba ausencia de `new MockDataAdapter` en ese archivo. |
| 11 | Activity sigue siendo read model. | Test de proyección: una evidencia modifica estado local y el Activity resultante se obtiene mediante projector, sin mutar un `ActivityItem` desde la acción. |
| 12 | Puede representarse procedencia por capability. | Cada capability efectiva expone request, `providerId`, modo y provenance. |
| 13 | Reset local es determinista. | Dispatch + reset en cada demo produce deep equality con su snapshot inicial y no con el de la otra demo. |
| 14 | Hospitality expresa booking/stay y varios actores sin `memberId` universal. | Validación de Scenario exige context refs y dos `subjectRef` tipados; esas referencias no usan `memberId`. |
| 15 | Demo Script usa una acción pública. | Test ejecuta `confirm-check-in` por `DemoActionPort`; el Script contiene solo action ID/args y no recibe estado interno. |

La puerta final será `npm run check` más los dos smoke renders de selección. No se exige test end-to-end en navegador ni validación en iPhone para falsificar H1–H4.

## 7. Archivos esperados para Session 5

La lista es deliberadamente cerrada. Cualquier archivo adicional requiere justificar qué criterio no puede probarse con estos.

### 7.1 Archivos nuevos

Todos bajo `products/convercus-app/prototype/src/demo-factory/` salvo indicación contraria:

| Archivo | Contenido mínimo |
|---|---|
| `contracts.ts` | Manifiesto, referencias, Scenario, Script, evidence/event interpretation, puertos y runtime resuelto. |
| `manifests/retail-baseline.ts` | Composición deseada de Demo A. |
| `manifests/hospitality-stay.ts` | Composición deseada de Demo B. |
| `artifacts/fixtures.ts` | Fixtures Retail y Hospitality separados del provider. |
| `artifacts/experiences.ts` | Única Experience Definition mínima referenciada por Hospitality. |
| `artifacts/scenarios.ts` | Scenario `arrival-and-stay`, sujetos, contextos y checkpoint. |
| `artifacts/scripts.ts` | Un Script Hospitality con una acción pública. |
| `artifacts/hospitality-brand.ts` | Configuración ficticia de `Aurora Stay`. |
| `artifacts/aurora-stay-logo.svg` | Wordmark ficticio local sin dependencia externa. |
| `bootstrap.ts` | Catálogos, validación, provider registry y resolución efectiva. |
| `bootstrap.test.ts` | H1, H2, H4, aislamiento, cardinalidad y fallos explícitos. |
| `projection.test.ts` | H3, Activity como proyección y reset determinista de ambas demos. |

### 7.2 Archivos existentes con cambio mínimo

| Archivo | Cambio mínimo previsto |
|---|---|
| `products/convercus-app/prototype/src/demo/mock-adapter.ts` | Recibir fixture; separar estado local de `AppSnapshot`; implementar los dos puertos y proyección de Activity. |
| `products/convercus-app/prototype/src/demo/mock-adapter.test.ts` | Conservar garantías actuales y parametrizarlas por fixture. |
| `products/convercus-app/prototype/src/config/brand.ts` | Hacer genérica la validación y aplicación de una marca ya resuelta; mantener exports compatibles cuando sea posible. |
| `products/convercus-app/prototype/src/config/brand.test.ts` | Probar dos configuraciones en vez de asumir exclusivamente `brand_id: convercus`. |
| `products/convercus-app/prototype/src/app/App.tsx` | Recibir runtime; eliminar imports/instanciación globales; usar marca, módulos, puertos y metadata efectivos. |
| `products/convercus-app/prototype/src/main.tsx` | Seleccionar `demo`, resolver bootstrap, aplicar marca y renderizar runtime o error explícito. |
| `products/convercus-app/prototype/vite.config.ts` | Neutralizar metadata PWA como `Demo Factory`; no resolver demos aquí. |

### 7.3 Archivos que no cambian

- Contrato semántico y fuentes TES.
- `02-shared-contracts/experience-domain/`.
- Experience Builder completo.
- `products/convercus-app/config/app.yaml`.
- Componentes de `src/ui/`.
- Routing TES/multiexperience existente.
- Backend, APIs y cualquier almacenamiento persistente.

`canonical-demo-package.ts` puede permanecer como artefacto previo no ejecutado durante el experimento. Eliminarlo o migrarlo ampliaría el rollback sin aportar falsación adicional.

## 8. Plan de implementación de Session 5 ordenado por dependencias

### Paso 1 — Congelar la línea base observable

- **Propósito:** asegurar que Retail conserva comportamiento y que la puerta de calidad está verde antes del experimento.
- **Archivos:** ninguno; solo ejecución de pruebas.
- **Validación:** `npm run check` y snapshot/manual smoke de rutas actuales.
- **Rollback:** no aplica; no hay cambios.
- **Hipótesis:** control experimental previo, no prueba H1–H4.

### Paso 2 — Definir contratos experimentales puros

- **Propósito:** expresar solo manifiesto, refs, Scenario, Script, evidencia/interpretación, puertos y runtime necesarios.
- **Archivos:** nuevo `demo-factory/contracts.ts`.
- **Validación:** typecheck; revisión de que no incluye secretos, persistencia, reglas de Experience ni conceptos de coverage.
- **Rollback:** borrar el archivo.
- **Hipótesis:** H1, H2, H3 y H4 a nivel de expresabilidad.

### Paso 3 — Extraer fixtures e introducir proyección explícita

- **Propósito:** convertir el snapshot embebido en semilla inyectable y mantener Activity como read model.
- **Archivos:** nuevos `artifacts/fixtures.ts` y `projection.test.ts`; cambios en `demo/mock-adapter.ts` y su test.
- **Validación:** aislamiento de clones, evidencia con/sin interpretación, Activity proyectada y reset Retail determinista.
- **Rollback:** restaurar el mock y su test; borrar fixtures y prueba de proyección.
- **Hipótesis:** H3; soporta H4.

### Paso 4 — Añadir artefactos Hospitality separados

- **Propósito:** introducir la diferencia mínima que tensiona marca, contenido, Experience, Scenario, sujetos, contexto y Script.
- **Archivos:** nuevos `artifacts/experiences.ts`, `scenarios.ts`, `scripts.ts`, `hospitality-brand.ts` y `aurora-stay-logo.svg`.
- **Validación:** typecheck y tests unitarios de referencias, dependencias y ausencia de `memberId` en subject/context refs.
- **Rollback:** borrar los cinco archivos.
- **Hipótesis:** H2 y H3.

### Paso 5 — Declarar los dos manifiestos

- **Propósito:** representar composición deseada sin implementaciones ni secretos.
- **Archivos:** nuevos `manifests/retail-baseline.ts` y `manifests/hospitality-stay.ts`.
- **Validación:** schema/version refs, módulos, capability requests; test sintético de dos demos por prospecto.
- **Rollback:** borrar ambos manifiestos.
- **Hipótesis:** H1.

### Paso 6 — Resolver bootstrap y providers por capability

- **Propósito:** producir `ResolvedDemoRuntime`, validar referencias y resolver los dos puertos fuera de React.
- **Archivos:** nuevos `bootstrap.ts` y `bootstrap.test.ts`.
- **Validación:** resolución de ambas demos, requested vs resolved, procedencia, provider por puerto y matriz completa de errores de referencia.
- **Rollback:** borrar ambos archivos.
- **Hipótesis:** H1 y H4; integra H2.

### Paso 7 — Generalizar la carga de marca

- **Propósito:** aplicar la marca efectiva sin identidad Convercus fijada en el loader.
- **Archivos:** `config/brand.ts` y `config/brand.test.ts`.
- **Validación:** parseo/variables de ambas marcas y rechazo de configuración incompleta.
- **Rollback:** restaurar ambos archivos; el resto del experimento puede seguir probándose sin render.
- **Hipótesis:** H1.

### Paso 8 — Inyectar runtime en el mismo core React

- **Propósito:** quitar resolución y provider de `App.tsx`, filtrar módulos y mostrar identidad efectiva con el menor cambio de componentes.
- **Archivos:** `app/App.tsx` y `main.tsx`.
- **Validación:** smoke render de ambas selecciones, navegación configurada, búsqueda estática de instanciación/provider e identidades hard-coded.
- **Rollback:** restaurar los dos archivos; bootstrap y artefactos quedan inertes y borrables.
- **Hipótesis:** H1 y H4.

### Paso 9 — Neutralizar metadata de instalación

- **Propósito:** evitar que el nombre de un prospecto se filtre en la demo del otro sin construir PWA por prospecto.
- **Archivos:** `vite.config.ts`.
- **Validación:** build y revisión del web manifest generado con identidad neutral `Demo Factory`.
- **Rollback:** restaurar un archivo.
- **Hipótesis:** H1, específicamente aislamiento de marca.

### Paso 10 — Ejecutar la falsación integrada

- **Propósito:** decidir H1–H4 con evidencia y no solo confirmar que compila.
- **Archivos:** solo ajustes a tests nuevos si revelan una expectativa incorrecta; no se añaden features.
- **Validación:** `npm run check`, smoke render de ambos IDs, manifiesto inválido, comparación cruzada de fugas, dos reset y ejecución del único paso de Script.
- **Rollback:** si una hipótesis se rechaza, revertir desde el último paso que depende de ella; no compensar el fallo con nuevas capas.
- **Hipótesis:** H1–H4.

## 9. Criterios de rechazo de H1–H4

### H1 se rechaza si

- Hospitality exige branching por prospecto dentro de `App.tsx` o editar código para cambiar de demo;
- el manifiesto necesita contener secretos, instancias de providers o estado mutable para arrancar;
- requested y resolved composition no pueden distinguirse de forma útil;
- referencias versionadas no pueden validarse antes del render;
- representar varias demos por prospecto obliga a duplicar el core o a cambiar la identidad del prospecto.

### H2 se rechaza si

- el Scenario no puede aportar booking/stay, sujetos y checkpoint sin duplicar o redefinir la Experience;
- el Script necesita implementar una regla de dominio o mutar estado interno para producir el paso de demo;
- la separación añade objetos obligatorios a Retail aunque Scenario y Script no aporten valor;
- un checkpoint no puede referenciarse sin fusionar Scenario y Script;
- la Experience mínima queda ligada a contenido o marca exclusivamente por la separación elegida.

### H3 se rechaza si

- el experimento no puede distinguir una entrada factual de su interpretación TES sin crear un store o pipeline general;
- Activity tiene que convertirse en fuente factual o ser mutada directamente para soportar el paso Hospitality;
- preservar evidencia e interpretación separadas exige persistir todos los conceptos como objetos autónomos;
- el mismo modelo fuerza a tratar toda evidencia como Evento TES o todo Activity como evidencia.

### H4 se rechaza si

- sacar `MockDataAdapter` de `App.tsx` no permite cambiar fixture/provider mediante bootstrap;
- dos puertos mínimos no pueden expresar lectura y acción sin recrear un adaptador universal más complejo;
- la procedencia efectiva no puede asociarse a cada capability;
- el provider debe conocerse en el manifiesto o en componentes React;
- la costura exige un contenedor/framework cuyo coste excede el valor de resolver el mock actual.

## 10. Revisión final pre-implementación

### Supuestos no resueltos en los ADR aceptados

- **ADR-001:** sigue sin definirse la mecánica completa de migración entre baselines. No impide aceptación porque la decisión solo fija autoridad, trazabilidad y prohibición de reinterpretación silenciosa.
- **ADR-002:** sigue sin conocerse cuánta interacción local necesitarán demos reales. No impide aceptación porque la decisión permite read model directo, estado local, overlay o autoridad externa sin fijar stores.

Ninguno de esos supuestos invalida la aceptación de los ADR.

### ¿El experimento prueba arquitectura o solo la implementa?

Prueba arquitectura si los tests atraviesan los contraejemplos: segunda marca, módulos distintos, fixture distinto, Scenario opcional, sujetos no universales, referencia inválida, capability sin provider y evidencia sin interpretación TES. Sería mera implementación si solo moviera el mock a otra carpeta y comprobara que Retail sigue funcionando. Por ello, Hospitality y los casos negativos son parte obligatoria de la prueba.

### Features experimentales retiradas por no ser necesarias

No se incluyen motor de Experience, segunda Experience activa, coordinación de intervenciones, proveedor live, overlay híbrido, catálogo remoto, múltiples scripts ejecutables, lifecycle completo, persistencia, event bus, analytics, i18n general, selector visual de demos ni PWA separada por prospecto. Un query parameter, un Scenario, un Script y una acción pública aportan falsación suficiente.

### Fallo único más informativo

El fallo más informativo sería que **Hospitality no pudiera resolverse y ejecutarse con un manifiesto pequeño sin introducir lógica específica del prospecto en `App.tsx`, en el Script o en el provider**. Ese resultado demostraría que la frontera propuesta entre composición, contexto, acción y runtime está mal colocada; no sería un bug aislado de configuración.

## 11. Incertidumbres restantes

- Contratos y granularidad reales de la API Convercus.
- Si deployments reales seleccionarán demo en runtime, build time o mediante artefactos separados.
- Necesidades de privacidad, consentimiento, auditoría y retención de evidencias.
- Modelo TES formal de participación individual y colectiva.
- Ciclo de vida real de booking, stay, group y roles en un prospecto Hospitality.
- Forma futura de providers híbridos y reconciliación de fuentes.
- Necesidad de IDs estables, deduplicación, correcciones e idempotencia.
- Nivel de disclosure de procedencia apropiado en la interfaz comercial.
- Si una Experience Definition será reusable entre sectores o específica de cada contexto.
- Estrategia productiva de branding y metadata PWA por deployment.
- Utilidad real de las dos analíticas experimentales, que requiere casos y datos posteriores.

Estas incertidumbres están fuera del experimento salvo cuando constituyen un criterio explícito de rechazo.

## 12. Recomendación Go / No-Go

**GO condicionado para Session 5.**

Puede implementarse exactamente el experimento especificado porque:

- los dos ADR no conservan supuestos abiertos que impidan su aceptación;
- H1–H4 tienen resultados observables y criterios de rechazo;
- el caso Hospitality tensiona la arquitectura en lugar de duplicar Retail con otro color;
- la retirada no requiere migraciones, backend, API, TES, Builder ni rollback amplio de UI;
- el alcance excluye explícitamente las features que no aportan falsación.

La condición de Go es detener la implementación si necesita archivos o capas no enumerados sin vincularlos a un criterio de aceptación. Ante un rechazo de H1–H4, Session 5 debe registrar el resultado y volver a decisión arquitectónica; no ampliar el experimento hasta hacerlo pasar.
