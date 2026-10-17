---
title: "Session 6 — Consolidación del experimento y promoción de arquitectura"
aliases:
- "Experiment Consolidation and Architecture Promotion"
- "Demo Factory Architecture v0.3"
language: es
version: "v1.0"
status: "consolidado"
date: "2026-09-03"
project: "Convercus App"
document_type: "informe de consolidación de arquitectura"
scope: "verificación de Session 5, promoción selectiva, fuentes de autoridad y siguiente pregunta empírica"
repository_role: "evaluación posterior al experimento y entrada de decisión para Session 7"
semantic_authority: "análisis de producto y arquitectura subordinado; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Session 6 — Consolidación del experimento y promoción de arquitectura

## 1. Conclusión ejecutiva

Session 5 aporta evidencia suficiente para aceptar [ADR-003 — Composición deseada y efectiva de una demo](../../../00-governance/decisions/ADR-003-desired-effective-demo-composition.md). Retail y Hospitality se resuelven antes del render y utilizan el mismo `App.tsx`; marca y fixtures cambian sin lógica de prospecto dentro del core, los fallos materiales son explícitos y el estado mock se aísla por instancia.

La promoción debe ser selectiva. Se promueven la separación desired/effective, la inyección de fixtures y Activity como proyección. Se conservan con cualificación el bootstrap actual, los contratos agregados y el mock único. Query parameter, catálogos estáticos, referencias de sujetos/contexto y artefactos Hospitality continúan experimentales. `DemoPackage`, `canonical-demo-package.ts` y parte de `app.yaml` compiten con los manifiestos nuevos y deben tratarse como legacy o candidatos a migración, no como autoridad paralela.

H2 sigue provisional; H3 y H4 solo obtuvieron evidencia parcial. La recomendación para Session 7 es el **Candidate D — Scenario / Demo Script operational test**, porque cierra la laguna más concreta con el menor compromiso irreversible.

## 2. Verificación independiente de Session 5

Se inspeccionaron la implementación, sus importaciones y todos los tests. Se ejecutó `npm run check` el 3 de septiembre de 2026 con este resultado: typecheck correcto, lint correcto, **8 test files y 25 tests superados**, y build PWA correcto.

| Afirmación | Repositorio fact | Test evidence | Architectural inference | Veredicto |
|---|---|---|---|---|
| Retail y Hospitality usan el mismo core | `main.tsx` resuelve un runtime y renderiza siempre `App`; solo existe un `App.tsx`. | `app-smoke.test.tsx` renderiza ambas configuraciones con la misma exportación. | No fue necesario un fork por vertical. | Confirmada. |
| No hay lógica de prospecto en `App.tsx` | No importa manifiestos, fixtures, mock ni nombres Retail/Hospitality. | `projection.test.ts` inspecciona el source y prohíbe esos imports. | El core consume composición efectiva. | Confirmada. |
| Manifiesto y runtime están separados | `DemoManifest` declara referencias; `ResolvedDemoRuntime` contiene artefactos y provider resueltos. | El test comprueba que requests no tienen `providerId` y los resultados sí. | Intención y materialización tienen autoridades distintas. | Confirmada. |
| Bootstrap resuelve explícitamente | `resolveDemo()` valida y compone marca, fixture, Experience, Scenario, Script, provider y capabilities. | Tests resuelven ambas demos. | Bootstrap es la frontera efectiva actual. | Confirmada. |
| Demo desconocida falla | `resolveDemo()` lanza error sin fallback. | Caso `missing-demo`. | Se reduce el riesgo de fuga por sustitución silenciosa. | Confirmada. |
| Fixtures externos al mock | `MockDataAdapter` exige `DemoFixture` en constructor; los datos están en `fixtures.ts`. | Tests crean el adapter con fixture explícito. | El provider ya no posee narrativa de prospecto. | Confirmada. |
| Marca resuelta por composición | `brandRef` se resuelve a `BrandArtifact`; `main.tsx` aplica tokens; `App` usa el artefacto. | Se verifican marcas distintas, assets/tokens inválidos y DOM sin fuga cruzada. | La identidad visible depende de composición efectiva. | Confirmada. |
| Activity es read model | `activityRecords` no contienen icono/tono; `projectSnapshot()` produce `ActivityItem`. | Tests verifican derivación visual y ambos fixtures. | Se respeta ADR-002 sin una plataforma de eventos. | Confirmada. |
| Hospitality expresa booking/stay y varios sujetos/contextos | Scenario contiene individuo, grupo, property, booking y stay; no usa `memberId`. | Test estructural dedicado. | Una referencia extensible basta para este caso. | Confirmada solo para el caso mínimo. |
| Reset está aislado | Cada resolver construye un provider con clones propios del fixture. | Dispatch en Hospitality no cambia Retail; reset recupera el snapshot inicial. | El estado local pertenece a la sesión resuelta. | Confirmada. |
| Procedencia de capabilities es representable | `ResolvedCapability` contiene `providerId`, `status` y `provenance`. | Tests preservan `mocked` y `simulated` por capability. | No hace falta un `dataMode` global para representarla. | Confirmada como representación, no como resolución multi-provider. |

### Discrepancias y cualificaciones

No se detectó una afirmación principal falsa, pero sí estos límites:

1. `DemoManifest.schemaVersion` versiona el esquema, no una instancia concreta del manifiesto. Las referencias sí contienen versión; una identidad de versión o digest de manifiesto sigue pendiente.
2. Todas las capabilities resueltas señalan al mismo `mock-data-adapter`; no existe prueba de provider por capability.
3. La prueba de múltiples demos por prospecto utiliza un manifiesto sintético en test; el catálogo real contiene un demo por cada uno de sus dos prospectos.
4. `visibleModules` se declara, pero la UI actual no consume ese campo.
5. El Demo Script se ejecuta únicamente a través del provider en tests; no existe acción de presentador ni transición operacional de checkpoint.
6. Evidence y Event llegan ya relacionados en el input; el experimento no prueba evaluación contextual.

## 3. ADR-003

Se acepta el ADR-003 porque la separación entre intención y resolución sobrevivió al caso Hospitality, a fallos de referencias y al aislamiento de estado. Su aceptación no promueve el query parameter, los catálogos TypeScript ni el mock único.

## 4. Matriz de promoción de Session 5

Cada elemento recibe exactamente una clasificación.

| Elemento | Clasificación | Decisión y límite |
|---|---|---|
| `src/demo-factory/contracts.ts` | **PROMOTE WITH QUALIFICATION** | Se conserva la frontera de contratos. El archivo mezcla tipos maduros con H2–H4 provisionales y no debe tratarse entero como modelo final. |
| `manifests.ts` | **PROMOTE WITH QUALIFICATION** | Los manifiestos pasan a ser la intención ejecutable de la baseline. Su almacenamiento conjunto, falta de versión de instancia y `visibleModules` inactivo son temporales. |
| `fixtures.ts` | **PROMOTE WITH QUALIFICATION** | Se promueve la inyección externa de fixtures. El esquema agregado y ambos datasets concretos pueden cambiar con próximos experimentos. |
| `artifacts.ts` | **RETAIN AS EXPERIMENTAL** | Mezcla brand registry con Experience, Scenario y Script provisionales; no es una autoridad de catálogo definitiva. |
| `bootstrap.ts` | **PROMOTE WITH QUALIFICATION** | Se promueve la frontera desired/effective y el fallo explícito. Catálogos, capabilities soportadas y construcción del mock permanecen experimentales. |
| Artefactos Hospitality | **RETAIN AS EXPERIMENTAL** | Son un stress case ficticio, no una plantilla normativa de hospitality. |
| Artefactos Retail | **PROMOTE WITH QUALIFICATION** | Conservan la regresión del prototipo, pero no definen un modelo universal de demo. |
| Selección por query parameter | **RETAIN AS EXPERIMENTAL** | Es un mecanismo mínimo de laboratorio, no una decisión de deployment o multitenancy. |
| Catálogos estáticos | **RETAIN AS EXPERIMENTAL** | Permiten validación local, pero no prueban discovery, packaging ni compatibilidad distribuida. |
| Mock provider único | **PROMOTE WITH QUALIFICATION** | Se promueven la inyección de fixture, clon y reset local. El contrato único no se promueve como arquitectura final. |
| Costura de proyección de Activity | **PROMOTE** | Separar `ActivitySourceRecord` de `ActivityItem` está respaldado por ADR-002 y por pruebas en dos demos. |
| Representación de procedencia por capability | **PROMOTE WITH QUALIFICATION** | Se conserva `status/providerId/provenance`; todavía no se ha contrastado con providers heterogéneos. |
| Referencias de sujeto/contexto | **RETAIN AS EXPERIMENTAL** | Resuelven un caso mínimo sin `memberId`, pero no constituyen ontología ni modelo de participación. |
| Identidad PWA neutral | **PROMOTE WITH QUALIFICATION** | Evita fuga estática en el bundle compartido; la metadata instalable por deployment sigue sin decidir. |
| `canonical-demo-package.ts` | **DEPRECATE** | Está validado por tests pero fuera del runtime; compite con `retailManifest` y no debe guiar nuevas demos. |
| `app.yaml` | **DEPRECATE** | Conserva valor histórico y configuración de producto testeada, pero sus defaults de marca, locale y modo ya no componen el runtime. Debe estrecharse o migrarse antes de volver a ser autoritativo. |

No se clasifica ningún elemento como REMOVE: los artefactos experimentales aún sostienen las pruebas o la siguiente investigación. Deprecate tampoco autoriza borrado en esta sesión.

## 5. Fuentes de verdad competidoras

| Artefacto | Qué representa hoy | Uso runtime | Uso en tests | Solapamiento | Estatuto |
|---|---|---|---|---|---|
| `DemoPackage` en `domain/contracts.ts` | Contrato anterior que agrega identidad, marca, locale, `dataMode`, TES y capabilities. | Ninguno. | Validado mediante `domain/demo-package.test.ts`. | Solapa `DemoManifest`, Experience ref y capabilities; confunde deseo con modo efectivo. | **Legacy; candidate for future migration.** |
| `canonical-demo-package.ts` | Instancia Retail/Convercus del contrato anterior. | Ninguno. | Fuente de los tests de `DemoPackage`. | Duplica identidad, marca, locale, baseline y capabilities de `retailManifest`/`app.yaml`. | **Legacy y deprecado.** |
| `app.yaml` | Defaults históricos de producto: app, marca, locale, data mode, baseline y soporte TES. | No compone demos; solo llega a `canonical-demo-package.ts`, que no usa el runtime. | `app-config.test.ts` y tests del paquete anterior. | Marca/locale/modo/baseline solapan manifiesto, brand artifact y Experience ref. | **Subordinado histórico; candidato a estrechar o migrar.** |
| Session-5 manifests | Intención deseada por `demoId` y `prospectId`, con referencias y capability requests. | Sí, entrada de `resolveDemo()`. | Sí, directa e indirectamente. | Sustituyen el papel compositivo pretendido por `DemoPackage`. | **Autoridad de trabajo para composición deseada.** |
| `fixtures.ts` | Semilla versionada por referencia para estado mock local y read models. | Sí, se clona dentro del provider. | Sí. | Parte de los antiguos datos embebidos en el mock; no compite con el manifiesto porque este solo referencia. | **Autoridad de trabajo para fixture inicial local.** |
| `artifacts.ts` | Catálogo local de marcas, Experience headers, Scenarios y Scripts. | Sí, a través de bootstrap. | Sí. | La marca Convercus procede a su vez de `brand.yaml`; Experience header solapa parcialmente el contrato de dominio previo. | **Experimental y subordinado a sus fuentes gobernadas.** |
| Catálogos en `bootstrap.ts` | Índices de referencias a implementaciones disponibles en este bundle. | Sí. | Sí, además son sustituibles en tests. | Pueden confundirse con un registry definitivo o con deployment policy. | **Experimental.** |
| `bootstrap.ts` | Validación y composición efectiva local. | Sí, llamado por `main.tsx`. | Sí. | Absorbe hoy catálogo, policy y provider factory en un solo archivo. | **Autoridad de trabajo para resolución efectiva; implementación cualificada.** |

### Competencias que requieren señalización

1. **`DemoPackage` vs `DemoManifest`:** ambos parecen contratos de composición; solo el segundo alimenta el runtime. El primero debe marcarse deprecado en una sesión de migración.
2. **`canonical-demo-package.ts` vs `retailManifest`:** representan la demo base con capabilities parcialmente diferentes (`coupon-wallet/news-feed` frente a `benefit-wallet/content-feed`). No deben evolucionar en paralelo.
3. **`app.yaml` vs manifiestos:** marca, locale y modo parecen defaults efectivos, pero el bootstrap no los consulta.
4. **`app.yaml`/canonical package vs capability provenance:** el `dataMode: mock` global compite con statuses resueltos por capability.
5. **`brand.yaml` vs `artifacts.ts`:** `brand.yaml` conserva autoridad sobre marca Convercus; el artifact debe ser un binding subordinado, no una copia alternativa. Aurora, en cambio, solo existe como artifact experimental.
6. **Experience Definition de dominio vs `ExperienceDefinition` mínimo de Demo Factory:** comparten nombre pero no profundidad contractual. El segundo es en realidad un header resoluble experimental y no debe interpretarse como definición TES completa.
7. **README actual vs runtime:** el README todavía afirma que `app.yaml` es configuración de producto sin aclarar que no compone las demos; esto puede inducir cambios en la fuente equivocada.

## 6. Madurez de H2 — Scenario / Experience / Demo Script

**Clasificación: STILL PROVISIONAL.**

Session 5 prueba que las tres representaciones pueden permanecer separadas, que Scenario y Script son opcionales y que Hospitality puede expresar contexto y varios sujetos. No prueba todavía:

- una acción de Script iniciada desde una frontera operacional de presentador;
- que el comando alcance y registre un checkpoint nuevo de manera determinista;
- precondiciones, repetición, fallo o idempotencia de comandos;
- dos scripts con checkpoints iniciales distintos;
- participación colectiva y relación entre individuo, grupo y participación;
- reutilización de una Experience en un segundo Scenario materialmente distinto;
- reutilización de un Scenario con otro Script;
- que el Script no se convierta en controlador a medida cuando crezca más allá de un paso.

La ejecución exclusiva en tests aporta evidencia de contrato, no evidencia de operación real en la aplicación.

## 7. Madurez de H3 — Evidence / Occurrence / TES Event / Activity

**Clasificación: parcial y no preparada para ADR.**

Quedó probado que Activity puede derivarse de registros sin icono ni tono y conservar procedencia, y que `EvidenceInput` puede distinguirse de una interpretación TES opcional. No quedó probado:

- cómo se reconoce o evalúa un Event a partir de evidencia; la interpretación actual ya viene adjunta;
- una misma evidencia evaluada de forma diferente frente a dos Experiences;
- cero, una o varias interpretaciones por evidencia;
- múltiples trazas de un hecho, deduplicación, corrección o retractación;
- inferencias, agregados, ausencia de acción o eventos tardíos;
- privacidad, minimización, retención o referencias a fuentes externas;
- procedencia atravesando más de un provider;
- persistencia, replay o necesidad de cualquier store;
- impacto real de un Event sobre participación, Progression o Result.

La promoción de Activity como read model no promueve una arquitectura general de evidence/events.

## 8. Madurez de H4 — Provider Resolution

**Clasificación: parcial y no preparada para ADR multi-provider.**

Session 5 prueba que `App.tsx` no necesita seleccionar ni construir el mock y que bootstrap puede inyectar un fixture distinto. También prueba que la procedencia cabe por capability. No prueba:

- provider por capability;
- dos providers simultáneos;
- contratos heterogéneos de lectura y acción;
- precedencia o reconciliación entre fuentes;
- overlay real/simulado;
- error parcial de una capability con otras disponibles;
- compatibilidad con la API real de Convercus;
- secretos, endpoints o restricciones de deployment reales;
- reset más allá del estado mock local.

El `DemoProvider` actual sigue agrupando `getSnapshot`, `dispatch` y `reset`; debe verse como conveniencia experimental, no como puerto universal aceptado.

## 9. Demo Factory Architecture v0.3

```text
┌────────────────────────────────────────────────────┐
│ TES                                                │
│ Autoridad sobre significado e invariantes          │
└────────────────────────┬───────────────────────────┘
                         │ trazabilidad
┌────────────────────────▼───────────────────────────┐
│ Versioned product contracts                        │
│ Traducción funcional; extensiones no-TES marcadas  │
└────────────────────────┬───────────────────────────┘
                         │
┌────────────────────────▼───────────────────────────┐
│ Desired demo composition / manifest                │
│ Identidad + referencias + capability requirements  │
│ Scenario / Experience ref / Script: PROVISIONAL    │
└────────────────────────┬───────────────────────────┘
                         │ validar y resolver
┌────────────────────────▼───────────────────────────┐
│ Bootstrap + environment constraints                │
│ Boundary: PROMOTED                                 │
│ Static catalogues/query selector: EXPERIMENTAL     │
│ Provider-per-capability: UNPROVEN                  │
└────────────────────────┬───────────────────────────┘
                         │
┌────────────────────────▼───────────────────────────┐
│ Effective composition                              │
│ Artefactos + capabilities/provenance + provider    │
└────────────────────────┬───────────────────────────┘
                         │
┌────────────────────────▼───────────────────────────┐
│ Runtime state, only as required                    │
│ Mock clone/reset: SUPPORTED                        │
│ Evidence/Event evaluation: PROVISIONAL             │
└────────────────────────┬───────────────────────────┘
                         │ projection
┌────────────────────────▼───────────────────────────┐
│ Read models / UI                                   │
│ AppSnapshot + Activity projection                  │
└────────────────────────────────────────────────────┘
```

Esta versión añade únicamente la decisión desired/effective a los ADR previos. No eleva los detalles del experimento a plataforma.

## 10. Candidatos para Session 7

| Candidato | Información ganada | Hipótesis | Coste | Reversibilidad | Riesgo de generalización prematura | Dependencia API/TES |
|---|---|---|---|---|---|---|
| A — Third-demo marginal-cost test | Comprueba si el coste bajo se repite y revela campos específicos ocultos. | H1 y Marginal Demo Code Cost. | Medio: nueva marca, datos, manifiesto y pruebas. | Alta. | Medio: puede convertir el tercer caso en un pseudo-esquema universal. | Baja si es solo fidelización; media si añade semántica nueva. |
| B — H3 contextual Experience evaluation | Distingue evidencia de significación contextual en dos Experiences. | H3. | Medio-alto aunque sea in-memory. | Alta técnicamente. | Alto: riesgo de motor de Experience y semántica inventada. | Alta dependencia TES; baja dependencia API. |
| C — H4 hybrid provider experiment | Revela si provider por capability es necesario y si el contrato único se rompe. | H4. | Medio: dos mocks, bindings y fallos parciales. | Alta. | Medio-alto: puede cristalizar puertos sin API real. | Baja API ejecutiva, pero compatibilidad real seguirá desconocida. |
| D — Scenario / Demo Script operational test | Comprueba la frontera pública, checkpoint determinista y papel real del Script. | H2. | Bajo: una acción de presentador y estado/checkpoint mínimo. | Muy alta. | Bajo si se limita a un comando y no añade reglas TES. | Baja API; media-baja TES si no se afirma Progression. |

## 11. Recomendación para Session 7

**Recomendar exactamente Candidate D — Scenario / Demo Script operational test.**

Es la mayor información por unidad de complejidad irreversible porque convierte la principal evidencia puramente estructural de H2 en evidencia operacional usando artefactos ya existentes. El experimento debe limitarse a:

1. una acción visible de presentador;
2. un comando público ya declarado por el Script;
3. transición determinista entre `pre-arrival-confirmed` y `checked-in` dentro de estado mock local;
4. Activity proyectada como consecuencia visible;
5. reset al checkpoint inicial;
6. prueba de que el Script no accede al estado interno ni implementa reglas de Experience.

Debe detenerse si alcanzar el checkpoint exige definir Progression TES, participación colectiva completa o un controlador genérico de scripts.

## 12. Propuesta de medición de Marginal Demo Code Cost

La medición futura será un vector, no un conteo bruto de líneas:

| Dimensión | Medida mínima | Señal favorable |
|---|---|---|
| Core churn | Archivos y líneas modificadas en `app/`, `domain/`, provider y bootstrap compartido. | Cero cambios de lógica core para una demo compatible. |
| Abstraction churn | Nuevos tipos, branches, registries o generalizaciones creados solo para admitir la demo. | Cero abstracciones nuevas o una extensión justificada por un caso falsificador. |
| Artifact effort | Archivos/configuración específicos añadidos y complejidad de sus referencias. | Trabajo concentrado en manifiesto, marca, fixture y contenido. |
| Existing-file touch surface | Número y centralidad de archivos existentes modificados. | Cambios limitados al registro explícito; ningún componente compartido. |
| Validation effort | Tests nuevos por aislamiento, referencias y comportamiento distintivo. | Tests específicos pequeños que reutilizan helpers existentes. |
| Regression exposure | Suites afectadas, fallos cruzados y datos filtrados entre demos. | Suite completa verde y cero cambios de snapshots ajenos. |
| Reversibility | Archivos que hay que borrar/revertir y existencia de datos externos. | Retirada por eliminación de artefactos sin migración. |
| Semantic novelty | Nuevos supuestos TES/producto necesarios. | Ninguno para una demo declarada compatible; cualquier novedad se separa como hipótesis. |

### Procedimiento

1. Etiquetar el estado anterior a la tercera demo.
2. Clasificar cada diff como core compartido, extensión genérica, artifact específico, test o documentación.
3. Registrar por qué se tocó cada archivo existente y si el cambio beneficiaría una cuarta demo.
4. Ejecutar toda la suite y una matriz de fuga cruzada entre las tres demos.
5. Retirar temporalmente la tercera demo y comprobar que la eliminación no requiere compensaciones.
6. Comparar el vector con Session 5; no sumar dimensiones heterogéneas en un único número sin pesos justificados.

La afirmación «una tercera demo requiere principalmente manifiesto y artefactos» se considerará apoyada si no cambia lógica de `App.tsx`, no crea branches de prospecto, no exige un provider nuevo por accidente y no introduce una abstracción genérica cuya única evidencia sea ese caso. Se considerará falsada si cada vertical obliga a modificar core, ampliar un union central y reescribir tests cruzados de forma creciente.

## 13. Riesgos restantes

- Dos contratos de composición (`DemoPackage` y `DemoManifest`) siguen coexistiendo.
- `app.yaml` parece efectivo aunque el runtime nuevo no lo consume.
- `ExperienceDefinition` de Demo Factory comparte nombre con un contrato de dominio más rico.
- El manifiesto carece de versión/digest de instancia.
- `visibleModules` está declarado pero no aplicado.
- El bootstrap combina resolución, catálogos, policy y provider construction.
- La lista de capabilities soportadas está hard-coded en bootstrap.
- Procedencia declarada y provider real coinciden por construcción, no por integración heterogénea.
- Subject/context refs son insuficientes para una participación colectiva real.
- Evidence/Event no ha sido evaluado contextualmente.
- El mock único puede ocultar diferencias de contratos por capability.
- El selector por query y el default Retail no representan una política productiva.
- La identidad PWA neutral evita fuga, pero no resuelve instalación por marca.
- Activity conserva títulos/descripciones en el source record; solo los campos visuales fueron proyectados.

## 14. Recomendación Go / No-Go

**GO para consolidar ADR-003 y mantener Session 5 como baseline cualificada.**

**GO condicionado para Session 7 exclusivamente con Candidate D.** No debe iniciarse migración de fuentes legacy, arquitectura multi-provider, evaluación contextual H3 ni tercera demo dentro de ese experimento. Si el comando público necesita semántica de Progression, participación colectiva completa o un motor de scripts, la sesión debe detenerse y registrar la falsación.
