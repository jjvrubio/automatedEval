# INSTRUCCIÓN SESION 1   
Inspect the entire current repository without modifying any files. I am turning this project into a reusable “Convercus Demo Factory” whose purpose is to generate prospect-specific demos on top of the Convercus API.

Produce an architectural assessment containing:

1. current repository structure and technology stack;
2. application entry points;
3. where Convercus API access is implemented;
4. where demo-specific data, branding and configuration currently live;
5. reusable components already present;
6. hard-coded prospect-specific logic;
7. duplicated patterns;
8. current testing and validation mechanisms;
9. environment/configuration dependencies;
10. architectural obstacles to supporting multiple customized demos from a common core.

Do not propose a large refactor yet. First describe the system as it actually exists, distinguish facts from inference, and identify the five most important architectural questions we need to resolve before designing the Demo Factory.

---
---
# Architectural assessment: current Convercus repository

Scope: `02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products`. I also checked repository-level Git and CI configuration where it could affect this project. Other sibling automation projects were excluded.

No files were modified. I did not run the build or tests because those commands can write caches and `dist`; I inspected their definitions and the existing source instead.

## Executive assessment

The repository currently contains a sound early-stage frontend prototype plus substantial semantic/governance documentation. It is not yet a Demo Factory.

The executable system is one React PWA:

- One Convercus-branded application.
- One hard-coded mock member and content dataset.
- One fixed mock adapter instantiated directly by the application.
- One static `DemoPackage`, used only by tests.
- No Convercus API client, backend, proxy, authentication or runtime tenant selection.
- No executable Experience Builder.

The most promising foundations for a Demo Factory are already present:

- `DataAdapter` abstraction.
- `DemoPackage` contract and validator.
- Capability-status vocabulary.
- Central brand YAML and CSS-variable mapping.
- Separation between semantic authority, product contracts and UI.
- Pure event-routing logic.
- Deterministic mock reset.

However, these foundations are currently parallel to the application rather than composing it: the UI does not load or render a `DemoPackage`, and adapter/brand selection is fixed at build time.

---

## 1. Current structure and technology stack

### Actual repository structure

```text
convercus-experience-products/
├── 00-governance/
│   ├── product-boundaries.md
│   ├── program-architecture.md
│   ├── semantic-change-process.md
│   ├── source-precedence.md
│   └── tes-observation-process.md
├── 01-semantic-contract/
│   ├── product-interpretations/
│   ├── source-excerpts/
│   ├── tes-baseline-manifest.yaml
│   └── observation/change logs
├── 02-shared-contracts/
│   ├── experience-domain/
│   └── workflows-relationship.md
├── 03-shared-assets/
│   ├── brands/convercus/
│   └── scenarios/
├── products/
│   ├── convercus-app/
│   │   ├── config/app.yaml
│   │   ├── docs/
│   │   ├── archive/lovable-baseline/
│   │   └── prototype/
│   └── experience-builder/
│       ├── docs/data-model/
│       └── archive/
├── archive/
├── Convercus_Marco_Aplicado_Medicion_Sectorial.md
└── README.md
```

Fact: the only executable product manifest is [prototype/package.json](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/package.json). The Experience Builder currently contains documentation, a JSON Schema and a fixture, but no application code.

### Frontend stack

Fact:

- React `19.2.7`.
- React DOM `19.2.7`.
- React Router DOM `7.18.1`.
- TypeScript `6.0.3`, strict mode.
- Vite `8.1.5`.
- `vite-plugin-pwa` `1.3.0`, generating a Workbox service worker.
- YAML `2.9.0` for runtime parsing.
- Vitest `4.1.10` with `jsdom`.
- ESLint `10.0.1`.
- Plain global CSS; no Tailwind, CSS Modules or component library.
- Local SVG logos and Sofia Sans TTF fonts.
- Node.js `>=24`; the inspected environment has Node `24.18.0` and npm `11.16.0`.

Fact: there is no backend framework, server runtime, database, API-client library, query/cache library, form library or global state-management library.

Inference: the application is currently best described as a static SPA/PWA prototype rather than a full-stack application.

---

## 2. Application entry points

### Development and build entry points

Defined in [package.json](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/package.json):

- `npm run dev` → Vite development server.
- `npm run build` → TypeScript build validation followed by Vite production build.
- `npm run preview` → production-build preview.
- `npm run check` → typecheck, lint, tests and build.
- `npm test` → Vitest.

### Browser entry points

Fact:

1. [index.html](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/index.html) supplies the root DOM element and static metadata.
2. [main.tsx](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/main.tsx) applies brand variables, registers the PWA service worker and mounts React under `BrowserRouter`.
3. [App.tsx](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/app/App.tsx) instantiates the mock adapter, loads its snapshot and owns all screens and routes.

Current routes:

- `/` — home.
- `/benefits` — coupon/benefit catalogue.
- `/activity` — activity feed.
- `/profile` — member profile.
- `/system` — technical demo status.
- `/showcase` — iPhone-frame presentation mode, handled before the main route tree.
- `*` — not-found state.

Fact: `/showcase` embeds `/` through an iframe. It is a presentation wrapper, not another application.

---

## 3. Where Convercus API access is implemented

### Executable implementation

Fact: it is not implemented.

Evidence:

- No `fetch`, Axios, `XMLHttpRequest`, GraphQL, WebSocket or API URL appears in executable source.
- No environment-variable access exists.
- No authentication/token management exists.
- No backend or secure proxy exists.
- [App.tsx](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/app/App.tsx:14) directly creates `new MockDataAdapter()`.
- `app.yaml` declares `default_data_mode: mock`.

The existing abstraction is [DataAdapter](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts:23), with:

- `getSnapshot()`
- `dispatch(event)`
- `reset()`

Only [MockDataAdapter](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/mock-adapter.ts:130) implements it.

### API documentation

Fact: a historical, non-executable API assessment exists in [archive/lovable-baseline/README.md](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/archive/lovable-baseline/README.md:96). It records prospective staging endpoints for:

- Login.
- Account details.
- Balance.
- Coupons and coupon codes.
- Redemption.
- Newsfeed.
- Transactions.
- Levels.

It also records expected Bearer authentication, `org`, `accountId` and `interaction-id`, and recommends a secure proxy or Edge Function.

Fact: the document is explicitly archived and does not govern current implementation. The shared Workflows document also states that exact endpoint and payload mapping remains unverified.

Inference: the endpoint inventory is useful discovery material, but it cannot yet be treated as a current API contract.

---

## 4. Where demo-specific data, branding and configuration live

### Mock member and content

Fact: all member-facing demo data is embedded in [mock-adapter.ts](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/mock-adapter.ts):

- Alex Martín.
- Essential/Plus levels.
- Point balances and progress.
- Three coupons.
- One news item.
- Three activity items.
- Spanish display dates and marketing copy.
- UI tone and icon selection.

This is TypeScript source, not an external fixture or prospect package.

### Product configuration

Fact: [config/app.yaml](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/config/app.yaml) contains:

- App ID and name.
- Default locale.
- Brand ID and declared brand source.
- Data mode.
- TES baseline.
- Experience-support mode.

It is imported as raw text and partially validated in [app-config.ts](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/config/app-config.ts).

Important fact: `brand_source` exists in YAML but is not represented, validated or used by `app-config.ts`.

### Branding

Fact: the canonical Convercus brand lives in:

- [brand.yaml](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/03-shared-assets/brands/convercus/brand.yaml)
- `03-shared-assets/brands/convercus/assets/`

[brand.ts](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/config/brand.ts) loads that exact directory using the Vite alias `@convercus-brand`.

Important facts:

- The validator explicitly requires `brand_id === "convercus"`.
- Logo files are statically imported by their Convercus filenames.
- The header’s image alt text is hard-coded as `Convercus`.
- PWA metadata and HTML metadata repeat Convercus name and colors.
- Many CSS colors use variables, but numerous Convercus-derived colors remain hard-coded in global CSS.
- Futura exists locally but is Git-ignored because its redistribution licence is unverified.

### Demo package

Fact: [canonical-demo-package.ts](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/canonical-demo-package.ts) defines:

- Package identity.
- Brand and locale references.
- Data mode.
- TES applicability and baseline.
- Capability-status manifest.
- Empty Experiences array.

Critical fact: this object is imported only by tests. `App.tsx` does not load or consume it.

Inference: the repository has the beginning of a demo-package vocabulary but not a package-driven application.

---

## 5. Reusable components and abstractions already present

### Reusable exported UI

Fact:

- [Icon](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/ui/Icon.tsx) — typed SVG icon set.
- [FeedbackState](/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/ui/FeedbackState.tsx) — loading, error, empty and not-found presentation with optional action.

### Reusable but App-local UI

Fact: `SectionHeading`, `CouponCard` and `ActivityList` are reusable functions, but they live inside the 380-line `App.tsx` and are not exported.

### Domain and application abstractions

Fact:

- `DataMode` and capability-status vocabulary.
- Generic `DataAdapter<TSnapshot,TEvent>`.
- `DemoPackage`, `ExperienceDefinition`, participation, event, rule and effect contracts.
- Demo-package validation and assertion.
- Pure `evaluateEventAcrossExperiences` function.
- Deterministic `MockDataAdapter`.
- Brand YAML → CSS-variable mapper.
- Typed configuration parsing.
- PWA shell and responsive navigation.

### Semantic/governance assets

Fact: the repository has a strong documented separation between:

- TES semantic authority.
- Product-level functional translation.
- Technical implementation.
- Shared contracts.
- Shared scenarios and brand assets.

Inference: this separation can provide useful governance for generated demos, but it currently has little automated enforcement beyond a small set of TypeScript tests.

---

## 6. Hard-coded prospect-specific logic

There is no named commercial prospect in the current code.

The hard-coding is instead **canonical-demo-specific** and would become prospect-specific if this pattern were copied for each demo.

Fact:

- Member identity and loyalty state are embedded in TypeScript.
- Benefits, dates, campaign copy, news and activity are embedded in TypeScript.
- Spanish interface copy is embedded throughout `App.tsx`.
- The navigation model and available screens are fixed.
- Convercus branding, logos, title, theme colors and PWA manifest are fixed.
- Capability declarations are fixed in a TS module.
- The mock adapter is selected directly in code.
- The iPhone viewport is fixed at `393 × 852`.
- The app assumes a single current member snapshot.
- Dates include human-readable strings such as “Ayer” rather than deriving presentation from locale and timestamps.
- `Coupon` and `ActivityItem` data include `IconName` and visual `tone`, coupling business/demo data to this UI implementation.

Inference: producing a prospect demo today would require editing source files and rebuilding, rather than supplying a prospect package to a stable core.

---

## 7. Duplicated patterns

### Configuration duplication

Fact:

- `Convercus`, locale and colors recur across `app.yaml`, `brand.yaml`, `index.html`, `vite.config.ts`, `App.tsx` and the canonical package.
- PWA theme colors are duplicated between `brand.yaml`, Vite config and HTML.
- Capability availability is declared separately from the actual rendered routes and screens.
- `appConfig.dataMode` says `mock`, while adapter selection is independently fixed with `new MockDataAdapter()`.

### Validation duplication

Fact: both `app-config.ts` and `brand.ts` implement their own `isRecord` helper and custom shallow parsing.

### UI pattern duplication

Fact:

- Card, list-row, badge, icon-container and section-heading patterns are repeated through one large CSS file.
- Several settings rows are repeated inline.
- Marketing strings and presentation rules are interleaved with page composition.

### Parallel but disconnected models

Fact:

- `DemoPackage` describes capabilities and Experiences.
- `AppSnapshot` separately describes the data rendered by the App.
- Neither contains or references the other.
- Experience routing exists independently and is not connected to the active adapter or UI.

Inference: this is more consequential than ordinary code duplication. There are currently multiple representations of “what this demo is” without one runtime source of truth.

---

## 8. Current testing and validation mechanisms

### Automated frontend tests

Fact: five test files define ten Vitest tests:

1. App YAML loads with expected values.
2. Brand YAML and accessibility metadata load.
3. Brand CSS-variable mapping works.
4. Both logos bundle.
5. Mock snapshots are isolated from consumers.
6. Mock dispatch inserts activity.
7. Mock reset is deterministic.
8. Canonical `DemoPackage` passes validation.
9. Required-TES packages need a baseline and Experience.
10. Duplicate capability IDs are rejected.
11. A single routing test verifies independent effects across two Experiences.

The raw `it(...)` count is ten because some listed behaviours share tests.

### Static validation

Fact:

- TypeScript strict mode.
- ESLint with TypeScript and React Hooks rules.
- `npm run check` chains typecheck, lint, tests and production build.
- Vite production build generates a PWA and Workbox precache.

### Semantic and schema validation

Fact:

- TES baseline files include frozen IDs and SHA-256 hashes.
- Experience Builder includes a JSON Schema and example fixture.
- The inspected JSON documents are syntactically valid.
- `DemoPackage` has programmatic validation.

Limitations—facts:

- No tests render `App` or exercise React Router.
- No component interaction tests.
- No visual-regression tests.
- No accessibility automation.
- No browser/E2E tests or Playwright dependency, despite Playwright appearing in the implementation plan.
- No API contract tests.
- No test for switching brands, prospects or adapters.
- No test proves the capability manifest matches rendered functionality.
- No project-specific GitHub Actions workflow.
- Coverage reporters are configured, but there is no coverage script or coverage threshold.
- The JSON Schema fixture has no validation command in `package.json`.
- TES manifest hashes have no visible automated verification command.
- YAML validation is shallow and uses type assertions after a few top-level checks.

Inference: current tests protect foundational utilities but not the user-facing application or a multi-demo architecture.

---

## 9. Environment and configuration dependencies

### Runtime/build dependencies

Fact:

- Node.js 24+ and npm.
- `node_modules` installed from the lockfile.
- Vite must be able to read files outside `prototype/`:
  - `../config`
  - `../../../03-shared-assets/brands/convercus`
- Browser support for:
  - Service workers.
  - `structuredClone`.
  - `Intl.NumberFormat`.
  - `navigator.onLine`.
  - iframe rendering.
- SPA hosting must support `BrowserRouter` navigation fallback.
- PWA output assumes root deployment through `start_url: "/"` and absolute routes.

### Environment variables and secrets

Fact:

- There are no `.env` files in the project.
- No `import.meta.env` or `process.env` use.
- No API URL, organisation, account ID, credentials or token configuration.
- No secrets are currently required because no API is contacted.

### Non-runtime governance dependencies

Fact:

- The canonical TES corpus is externally maintained in a OneDrive path recorded in the baseline manifest.
- Frozen excerpts are checked into this repository.
- Updating the semantic baseline therefore depends on an external source and explicit impact review.

### Branding dependency

Fact:

- Sofia Sans is checked in with an OFL licence.
- Futura is present locally but excluded from Git and marked unavailable for distribution pending licence verification.

---

## 10. Main obstacles to multiple customized demos from a common core

These are architectural observations, not a refactor proposal.

1. **No runtime demo-composition boundary**

   `DemoPackage` exists but does not provide the content rendered by the App and is not loaded by the App. There is no single selectable unit containing prospect, brand, content, capabilities, scenario and data-source configuration.

2. **Build-time Convercus brand coupling**

   Brand assets are statically imported, the validator only accepts `convercus`, and metadata/colors are duplicated in build configuration, HTML and CSS. Changing prospect identity cannot currently be done by data alone.

3. **Fixed mock data source**

   The App constructs a singleton `MockDataAdapter` at module load. There is no adapter factory, dependency injection, tenant selection, API adapter or hybrid mode. The four declared data modes are vocabulary rather than working runtime alternatives.

4. **No secure Convercus integration boundary**

   There is no backend/proxy, auth/session lifecycle, organisation/account resolution, API DTO layer, error normalization, caching or permission policy. This is especially important because prospect demos may involve different Convercus organisations and account data.

5. **Demo content and presentation are interleaved**

   Prospect content resides in TypeScript objects, while page copy, navigation and some presentation decisions reside directly in `App.tsx`. Data objects themselves depend on UI icons and tones.

6. **The frontend is concentrated in two large files**

   Most UI composition lives in a 380-line `App.tsx`; most styling lives in a 334-line global stylesheet. This is manageable for one demo but increases collision risk when variation starts.

7. **No explicit tenant/prospect isolation model**

   There is no prospect ID, package resolver, URL namespace, deployment strategy, cache partition or service-worker isolation rule. A PWA service worker makes this question particularly important because cached assets/configuration can survive between sessions.

8. **No executable contract between API data and UI data**

   The archived endpoint map suggests likely resources, but there are no verified DTOs or mapping functions from Convercus responses to `AppSnapshot`.

9. **No localization/content pipeline**

   Locale is declared as `es`, but all copy and formatted dates are embedded in code. Changing locale or market would require source edits.

10. **Validation does not yet cover customization**

   Nothing currently verifies that two demo packages can coexist, that branding is complete, that required content exists, or that a package’s declared capabilities match the chosen adapter and visible UI.

---

# Five architectural questions to resolve first

## 1. What is the unit of customization and deployment?

Will each prospect receive:

- A separate build/deployment?
- A package selected at runtime by URL or prospect ID?
- A salesperson-controlled demo catalogue?
- A combination of shared core plus isolated deployments?

This determines security, caching, service-worker behaviour, asset loading and operational complexity.

## 2. What must a complete `DemoPackage` own?

We need to decide whether the package is the authoritative source for:

- Prospect identity and branding.
- Locale and copy.
- Member fixtures.
- Benefits, news and activity.
- Routes/features.
- Experience scenarios.
- Capability claims.
- Convercus organisation/account mapping.
- Data mode and API mapping.
- Demo script and reset behaviour.
- TES baseline and validation evidence.

Until this boundary is settled, the system has no stable contract between generated material and the common core.

## 3. Where is the secure Convercus API boundary?

We need an explicit decision about:

- Browser versus backend/proxy responsibilities.
- Authentication and token storage.
- Organisation and account selection.
- Staging versus production.
- Read-only versus mutation permissions.
- Per-prospect secrets.
- Auditing and rate/error handling.

The archived recommendation says “secure proxy”, but no current implementation or governing decision exists.

## 4. Which variations are configuration, and which are product code?

We need to define the permitted customization surface:

- Brand tokens and assets only?
- Content and scenarios?
- Navigation and enabled modules?
- Page composition?
- API field mappings?
- Custom prospect-specific components?

Without this decision, generated demos risk becoming forks of the application rather than instances of a common core.

## 5. How do mock, simulation and live API data coexist?

The declared modes are `mock`, `simulation`, `staging` and `production`, but their behavioural contract is undefined. We need to decide:

- Whether a demo may mix live and simulated modules.
- How data provenance is shown.
- How deterministic reset works with live data.
- What happens when the API is unavailable.
- How fixtures correspond to API DTOs.
- How capability status is derived from the active adapter rather than manually asserted.

This question determines whether a demo remains repeatable while still demonstrating real Convercus capabilities.

---
---

# Demo Factory — Sesión 2

## Repository Anatomy: de prototipo único a arquitectura componible

El diagnóstico de Codex es suficientemente bueno como para avanzar. Y, más importante, nos permite abandonar ya las abstracciones y trabajar sobre **tu sistema real**.

La conclusión inicial que quiero que retengas es ésta:

> **No tenemos que construir Demo Factory desde cero. Tenemos que conectar correctamente varias piezas que ya existen y convertirlas en un único modelo ejecutable.**

Ésta es una situación mucho mejor.

Actualmente tienes un frontend React/PWA funcional, una abstracción `DataAdapter`, un contrato `DemoPackage`, vocabulario de capacidades, configuración YAML, branding centralizado, lógica de eventos y una capa semántica/gobernanza considerable. El problema es que esos elementos existen en paralelo: la aplicación no se construye a partir del `DemoPackage`, el adaptador es fijo y el branding sigue acoplado a Convercus. 

Nuestro objetivo durante esta sesión será comprender **qué tenemos, qué significa arquitectónicamente y cuál debe ser la primera hipótesis de diseño**.

---

# 1. Qué sistema tenemos realmente

Codex clasifica correctamente el ejecutable actual como una SPA/PWA estática más que como una aplicación full-stack: React 19, TypeScript, Vite, PWA, Vitest y CSS global, pero sin backend, base de datos, cliente API, autenticación ni state-management externo. 

Esto tiene una consecuencia importante.

**No tenemos todavía una integración con Convercus que haya que desmontar.**

Tenemos principalmente:

$$
UI + Mock\ Domain + Semantic\ Contracts
$$

Esto reduce bastante el coste arquitectónico del cambio.

La aplicación actual hace esencialmente:

```text
App
 ↓
new MockDataAdapter()
 ↓
AppSnapshot
 ↓
React UI
```

Lo que queremos llegar a hacer es aproximadamente:

```text
DemoPackage
     │
     ├── Brand
     ├── Scenario
     ├── Capabilities
     ├── Content
     ├── Data configuration
     └── Locale
             │
             ▼
      Demo Runtime
             │
      Adapter Resolver
       /      |      \
    Mock  Simulation  API
             │
             ▼
       Domain Snapshot
             │
             ▼
       Capability UI
```

Todavía no vamos a programarlo.

Primero necesitamos entender por qué ésta es una mejor ontología.

---

# 2. Clasificación de la arquitectura existente

En la sesión anterior dijimos que clasificaríamos cada elemento como:

**Core / API Adapter / Modules / Configuration / Demo-specific / Technical debt / Candidate abstraction.**

Éste es mi mapa inicial.

| Elemento actual                  | Clasificación                             | Estado                             |
| -------------------------------- | ----------------------------------------- | ---------------------------------- |
| `DataAdapter<TSnapshot,TEvent>`  | **Core**                                  | Muy valioso                        |
| `MockDataAdapter`                | **Adapter**                               | Reutilizable                       |
| `DemoPackage`                    | **Core / Candidate composition contract** | Crucial pero desconectado          |
| `ExperienceDefinition`           | **Core domain**                           | Prometedor                         |
| `evaluateEventAcrossExperiences` | **Core domain**                           | Reutilizable                       |
| Capability-status vocabulary     | **Core domain**                           | Reutilizable                       |
| TES contracts                    | **Governance / semantic core**            | Valioso                            |
| `brand.yaml`                     | **Configuration**                         | Bien encaminado                    |
| Brand → CSS variables            | **Core rendering infrastructure**         | Reutilizable                       |
| Alex Martín + coupons + news     | **Demo-specific data**                    | Debe salir de TS                   |
| Convercus logos hard-coded       | **Demo-specific / tech debt**             | Debe parametrizarse                |
| Spanish strings in `App.tsx`     | **Demo-specific / tech debt**             | Deben externalizarse               |
| Routes hard-coded                | **Candidate module composition**          | Deben vincularse a capabilities    |
| `AppSnapshot`                    | **Core domain candidate**                 | Debe reconciliarse con DemoPackage |
| 380 líneas de `App.tsx`          | **Technical debt**                        | Todavía manejable                  |
| CSS global 334 líneas            | **Technical debt**                        | No urgente                         |
| `/showcase`                      | **Presentation layer**                    | Potencialmente reutilizable        |
| `canonical-demo-package.ts`      | **Configuration candidate**               | Hoy sólo test fixture              |
| `app.yaml`                       | **Configuration**                         | Parcialmente efectivo              |
| Experience Builder docs/schema   | **Future product / tooling**              | No ejecutable aún                  |

Codex señala correctamente que `DataAdapter`, `DemoPackage`, los contratos de Experiences y la lógica pura de routing ya representan bases razonables para una arquitectura común. 

Esto nos lleva al diagnóstico arquitectónico central.

---

# 3. El verdadero problema no es el hard-coding

Puedes pensar inicialmente:

> «El problema es que Alex Martín, los cupones, el logo y los colores están hard-coded.»

Eso es cierto, pero no es el problema fundamental.

Codex detecta algo más importante:

> Existen actualmente varias representaciones distintas de **“qué es esta demo”**.

Tenemos:

```text
app.yaml
brand.yaml
canonical-demo-package.ts
AppSnapshot
MockDataAdapter
App.tsx
vite.config
index.html
```

Cada una contiene una fracción de identidad, configuración o comportamiento.

Por ejemplo, `DemoPackage` describe capabilities y Experiences, mientras que `AppSnapshot` describe lo que realmente renderiza la aplicación; ninguno referencia al otro. 

Éste es un problema ontológico.

No existe una entidad autoritativa que pueda responder:

> **¿Qué es exactamente la demo que estoy ejecutando?**

Y sin esa entidad, cada nueva demo terminará introduciendo decisiones en diferentes puntos del código.

Por tanto:

## Primera hipótesis arquitectónica

> **`DemoPackage` debe evolucionar hacia el contrato autoritativo de una instancia de demo.**

No afirmo todavía que todo deba almacenarse físicamente dentro de un único JSON gigantesco.

Eso sería otra cuestión.

Lo importante es que conceptualmente:

$$
DemoPackage \equiv Demo\ Identity
$$

Puede contener referencias a otros artefactos:

```yaml
demo:
  id: hotel-chain-x
  industry: hospitality
  locale: es-ES

brand:
  ref: hotel-chain-x

scenario:
  ref: business-and-resort-loyalty

data:
  mode: simulation
  fixture: hotel-chain-x-default

capabilities:
  - profile
  - benefits
  - tiers
  - experiences
```

Pero debe existir **una raíz de composición**.

Éste es probablemente el descubrimiento más importante de esta sesión.

---

# 4. DemoPackage como Composition Root

Quiero introducirte aquí un concepto de arquitectura de software: **Composition Root**.

Es el lugar donde decidimos:

* qué componentes existen;
* qué implementaciones utilizamos;
* cómo se conectan;
* qué configuración gobierna el runtime.

Actualmente esa composición está dispersa.

Por ejemplo:

`appConfig.dataMode = mock`

pero la aplicación independientemente hace:

```text
new MockDataAdapter()
```

Por tanto la configuración dice una cosa y el código selecciona otra. Codex identifica exactamente esa duplicación. 

En Demo Factory queremos algo parecido a:

```text
DemoPackage
      │
      ▼
DemoRuntime.create(package)
      │
      ├── resolveBrand()
      ├── resolveCapabilities()
      ├── resolveScenario()
      ├── resolveAdapter()
      └── resolveContent()
```

Entonces sí tendremos:

> **configuration drives behaviour**.

Ésta es una expresión que quiero que conserves.

En una Factory madura:

**el código define lo que es posible;**

**la configuración define qué instancia de esas posibilidades estamos ejecutando.**

---

# 5. Las cinco preguntas de Codex: nuestras primeras respuestas

Codex termina correctamente con cinco preguntas arquitectónicas. 

No debemos dejarlas simplemente abiertas. Voy a darte nuestra **hipótesis v0.1** para cada una.

---

## Pregunta 1 — ¿Cuál es la unidad de customización y deployment?

Codex plantea:

* build independiente;
* selección runtime;
* catálogo comercial;
* modelo híbrido.

### Nuestra hipótesis

**Shared Core + DemoPackage + despliegues potencialmente aislados.**

Es decir:

```text
                   Shared code
                       │
           ┌───────────┼───────────┐
           │           │           │
      DemoPackage A DemoPackage B DemoPackage C
           │           │           │
         Build       Build       Build
```

Inicialmente prefiero **aislamiento operacional** antes que multi-tenancy sofisticado.

¿Por qué?

Porque todavía estamos creando demos comerciales.

No estamos creando un SaaS público.

Construir desde el principio:

> `demo.convercus.com/?tenant=air-europa`

con multi-tenancy completo, auth y resolución dinámica puede añadir complejidad que aún no necesitamos.

Nuestro objetivo no es optimizar infraestructura.

Es optimizar:

$$
Time\ to\ Customized\ Demo
$$

Por tanto podríamos compartir código y configuración, pero generar artefactos/deployments separados.

Más adelante podremos evolucionar hacia catálogo runtime.

---

# 6. Pregunta 2 — ¿Qué debe poseer DemoPackage?

Aquí mi respuesta es más firme.

**DemoPackage debe poseer o referenciar todo aquello cuya modificación no deba exigir cambiar código.**

Ésa será nuestra regla.

Por tanto probablemente:

### Identity

* prospect;
* industry;
* demo ID;
* variant.

### Brand

* logo;
* typography;
* colors;
* visual assets.

### Locale

* idioma;
* formatting;
* copy overrides.

### Capabilities

* qué módulos están activos;
* qué claim hacemos sobre ellos.

### Scenario

* journey;
* starting state;
* interactions;
* outcomes.

### Data

* fixture;
* member;
* campaigns;
* benefits;
* activity.

### Adapter

* mock;
* simulation;
* staging;
* production;
* eventualmente híbrido.

### Governance

* TES baseline;
* provenance;
* validation.

### Demo operations

* reset;
* presentation mode;
* quizás demo script.

Esto coincide bastante con los elementos que Codex plantea como frontera todavía no resuelta. 

---

# 7. Pregunta 3 — ¿Dónde está el límite seguro de la API?

Aquí no debemos improvisar.

Codex confirma que **actualmente no existe integración executable con la API de Convercus**: no hay `fetch`, cliente API, auth, variables de entorno, backend o proxy; sólo existe documentación histórica archivada sobre posibles endpoints. 

Esto en realidad es positivo.

Tenemos oportunidad de diseñarlo correctamente.

Nuestro principio será:

```text
Browser
   │
   ▼
Domain Adapter
   │
   ▼
Secure Demo API / Proxy
   │
   ▼
Convercus API
```

No quiero credenciales reales de Convercus incrustadas en el frontend.

Por tanto, cuando lleguemos a esa sesión, probablemente diseñaremos:

**`ConvercusAdapter`**

pero éste debería hablar con una **integration boundary** segura, no necesariamente directamente con la API pública desde el navegador.

Todavía no implementaremos esto.

Antes necesitaremos documentación actual y verificada de la API.

---

# 8. Pregunta 4 — ¿Qué es configuración y qué es código?

Ésta será una de las reglas fundamentales de nuestra Factory.

## Configuración

Algo es configuración cuando:

> queremos razonablemente cambiarlo entre dos demos sin cambiar cómo funciona conceptualmente la plataforma.

Ejemplos:

* logo;
* color;
* copy;
* usuario;
* puntos;
* rewards;
* campaign;
* journeys;
* módulos activos;
* imágenes;
* locale.

## Código

Algo pertenece al producto cuando:

> introduce una nueva capacidad o un nuevo comportamiento reutilizable.

Ejemplo:

Una demo hotelera quiere:

> «mostrar una recompensa de late checkout».

Eso debería ser **configuración**.

Pero quiere:

> «permitir seleccionar hotel, fechas y simular una reserva completa».

Si esa interacción todavía no existe, probablemente hemos descubierto un **nuevo módulo reutilizable**.

Esto nos da una regla muy poderosa:

> **Una necesidad específica de un cliente puede originar nuevo código; el código resultante no debería pertenecer al cliente si representa una capacidad generalizable.**

---

# 9. Aquí el escenario hotelero empieza a resultar muy útil

El caso que has añadido —una cadena con hoteles de negocios y resorts— es arquitectónicamente excelente.

Porque rompe una simplificación que podríamos haber hecho:

```text
One prospect = One customer journey
```

No necesariamente.

Podemos tener:

```text
Hotel Chain
    │
    ├── Business Hotels
    │       ├── frequent stays
    │       ├── status
    │       ├── upgrades
    │       ├── breakfast
    │       └── late checkout
    │
    └── Resorts
            ├── family stays
            ├── seasonal offers
            ├── experiences
            ├── spa
            ├── F&B
            └── activities
```

Esto nos obliga a distinguir:

**Prospect**

de

**Scenario**.

Y eso es muy valioso.

Una misma demo package podría quizás contener varios scenarios:

```yaml
scenarios:
  - business_traveller
  - resort_family
```

El comercial podría seleccionar uno u otro.

Más adelante incluso podríamos tener:

$$
DemoPackage = ProspectContext + \{Scenario_1,...,Scenario_n\}
$$

Esto será importante cuando diseñemos el contrato.

---

# 10. Pregunta 5 — Mock, Simulation y Live

Aquí quiero introducir una distinción semántica muy estricta.

Actualmente existen nombres para varios modos, pero no contratos conductuales claros. Codex lo señala explícitamente. 

Yo propondría provisionalmente:

### MOCK

Datos completamente locales.

```text
fixture → adapter → UI
```

Ventajas:

* determinista;
* rápido;
* offline;
* reset perfecto.

### SIMULATION

Estado local pero **comportamiento realista**.

Por ejemplo:

> hago clic en «redeem» → cambian puntos → aparece transaction → cambia reward.

No hay API real, pero existe causalidad.

### STAGING

Interacción con Convercus real en un entorno controlado.

### PRODUCTION

Por ahora no asumiría que una demo comercial debe acceder directamente a producción.

Y quizá aparezca un quinto modo:

### HYBRID

Una parte live y otra simulada.

Pero **no lo diseñaremos todavía** hasta tener un caso real que lo necesite.

---

# 11. Un punto donde discrepo ligeramente de la prioridad implícita de Codex

Codex identifica como obstáculo que `App.tsx` tenga 380 líneas y el CSS 334. 

Es cierto.

Pero **yo no lo refactorizaría todavía como prioridad**.

¿Por qué?

Porque podemos caer en:

> “vamos a limpiar el código antes de entender la arquitectura”.

Y terminar creando unos maravillosos:

```text
CouponCard.tsx
ActivityList.tsx
Navigation.tsx
...
```

sin resolver la cuestión esencial:

> ¿quién decide qué componentes aparecen?

Prefiero primero establecer:

**DemoPackage → Runtime → Modules**

y después la modularización del UI aparecerá con fronteras funcionales más naturales.

Esto es un ejemplo importante de pensamiento arquitectónico:

> **No todo technical debt debe pagarse inmediatamente.**

Hay deuda que conviene mantener hasta disponer de suficiente información para saber cuál es la abstracción correcta.

---

# 12. Arquitectura conceptual v0.1

A esta altura de la formación, nuestra primera hipótesis puede representarse así:

```text
                     DEMO FACTORY
                          │
                          │
                    DemoPackage
                          │
          ┌───────────────┼───────────────┐
          │               │               │
       Brand          Scenario         Capabilities
          │               │               │
          └───────────────┬───────────────┘
                          │
                     Demo Runtime
                          │
              ┌───────────┴───────────┐
              │                       │
        Adapter Resolver        Module Resolver
              │                       │
       ┌──────┼──────┐          ┌─────┼─────┐
       │      │      │          │     │     │
     Mock Simulation API      Home Benefits Profile ...
       │      │      │
       └──────┴──────┘
              │
              ▼
         Domain State
              │
              ▼
          React UI
```

El principio profundo es:

> **DemoPackage configura; Runtime compone; Adapters obtienen/modifican estado; Modules presentan capacidades.**

Ésta me parece, por ahora, una ontología suficientemente robusta.

---

# 13. Lo que NO vamos a hacer todavía

No quiero que Codex ahora:

* cree un backend;
* conecte la API;
* desmonte `App.tsx`;
* introduzca Redux;
* cambie el framework;
* añada Tailwind;
* implemente multi-tenancy;
* cree veinte interfaces;
* convierta todo en JSON;
* cree demos de hoteles.

Todavía no.

Estamos en:

$$
Observation \rightarrow Architecture
$$

Antes de:

$$
Architecture \rightarrow Implementation
$$

---

# 14. Tu ejercicio de la Sesión 2 en Codex

Ahora sí quiero que vuelvas a VS Code.

Esta vez vamos a pedir a Codex que utilice nuestro modelo conceptual para realizar una **segunda inspección mucho más dirigida**, pero todavía sin modificar archivos.

Pásale exactamente esto:

> Using the repository assessment already produced, perform a second architecture analysis for the proposed Convercus Demo Factory. Do not modify any files.
>
> Treat the following as the working architectural hypothesis, not as an instruction to force-fit the code:
>
> * `DemoPackage` should become the authoritative composition contract for a demo.
> * A demo should primarily be an instance of a shared core rather than a fork.
> * `DemoPackage` may reference separate brand, scenario, content and fixture assets rather than containing everything inline.
> * Runtime behaviour should be driven by configuration where possible.
> * `DataAdapter` should remain the abstraction between domain/UI and data sources.
> * Mock, simulation and future Convercus API adapters should share an explicit behavioural contract.
> * Prospect-specific requirements should become configuration unless they represent a genuinely reusable new capability.
>
> Analyze the existing repository against this hypothesis and produce:
>
> 1. A proposed responsibility map for:
>
>    * DemoPackage
>    * Demo Runtime
>    * DataAdapter
>    * Brand
>    * Scenario
>    * Capabilities/Modules
>    * Fixtures/content
>    * UI
>    * TES/semantic governance
>
> 2. Identify every current file or abstraction that could participate in each responsibility.
>
> 3. Identify conflicts, overlaps or missing boundaries.
>
> 4. Explain how `DemoPackage` and `AppSnapshot` could relate without prematurely redesigning either.
>
> 5. Identify the minimum architectural changes required to make a second demo possible without copying or forking the application.
>
> 6. Identify what should explicitly NOT be refactored yet.
>
> 7. Propose no more than three alternative composition models, comparing their complexity, extensibility and suitability for a commercial Demo Factory.
>
> Include the following future scenarios as architectural tests, but do not implement them:
>
> * airline loyalty;
> * retail loyalty;
> * public transport / sustainable mobility;
> * hospitality: one hotel chain containing both business hotels and vacation resorts.
>
> For the hospitality case, explicitly test whether the proposed architecture can support multiple demo scenarios or journeys under the same prospect/brand.
>
> Distinguish repository facts, architectural inference and recommendation. Do not modify files or generate implementation code.

---

# 15. Qué estamos aprendiendo realmente

Fíjate en cómo ha cambiado nuestra interacción con Codex en sólo dos sesiones.

En la primera:

> **“Dime qué hay.”**

Ahora:

> **“Contrasta lo que hay contra una hipótesis arquitectónica.”**

Más adelante:

> **“Diseña alternativas.”**

Después:

> **“Implementa una decisión explícita.”**

Y finalmente:

> **“Verifica que la implementación mantiene las invariantes.”**

Ésta es la diferencia entre usar un agente como **generador de código** y utilizarlo como componente de un **proceso de ingeniería**.

Y ésta será una constante de toda la formación.

No queremos maximizar cuánto puede hacer Codex por nosotros.

Queremos maximizar:

$$
Quality\ of\ decision \times Reusability \times Verification
$$

---

## Siguiente paso

Por tanto, tu tarea ahora vuelve a ser muy concreta:

**ve a Codex, dentro del mismo repositorio, y ejecuta el prompt anterior.**

Cuando termine, sube de nuevo el `.md`.

Con ese resultado haremos la **Sesión 3: Architecture Decision**, donde ya no nos limitaremos a analizar: compararemos los modelos propuestos por Codex, escogeremos uno, justificaremos por qué descartamos los demás y empezaremos a construir el primer **ADR — Architecture Decision Record** de Demo Factory.

Ahí daremos el siguiente salto importante: de **entender el sistema** a **gobernar explícitamente su evolución**.


---
---
Sí. **La cambia de manera importante y, además, la mejora.** No ejecutaría todavía el prompt de la Sesión 2 tal como te lo di. Tus observaciones obligan a corregir antes nuestro modelo conceptual.

## 1. “Activity” no debe ser una entidad universal de Demo Factory

En el diagnóstico de Codex, `Activity` corresponde literalmente a una característica de **la demo canónica actual**: existe una ruta `/activity`, descrita como *activity feed*, y el mock contiene tres `activity items`.  

Por tanto, cuando yo escribí en la propuesta de `DemoPackage`:

> member, campaigns, benefits, activity...

estaba elevando indebidamente una **representación concreta de la UI actual** a la categoría de concepto general de dominio.

Codex da incluso otra pista: los actuales `ActivityItem` contienen `IconName` y `tone`, lo que acopla el dato de negocio a su representación visual. 

Debemos corregirlo.

### ¿Qué debería existir entonces?

No:

```text
DemoPackage
 └── Activity
```

sino algo conceptualmente más parecido a:

```text
Domain state / events
        │
        ├── transactions
        ├── participation
        ├── rewards
        ├── experience state
        ├── interactions
        └── other capability-specific state
                    │
                    ▼
             UI projections
                    │
         ┌──────────┼──────────┐
         │          │          │
     Activity    Timeline    History
       feed       etc.        etc.
```

Es decir:

> **“Activity feed” puede ser un módulo o una proyección de presentación, pero no debemos asumir que “Activity” forma parte de la ontología universal de una demo.**

Y efectivamente, la disparidad sectorial que señalas lo demuestra.

Una aerolínea podría mostrar:

* vuelo;
* acumulación de puntos;
* cambio de tier;
* redención;
* participación en experiencia.

Un hotel de negocios:

* estancia;
* check-in;
* upgrade;
* desayuno;
* puntos;
* late checkout.

Un resort:

* reserva;
* spa;
* restauración;
* actividad familiar;
* experiencia;
* recompensa.

Retail:

* compra;
* referral;
* cupón;
* redemption.

Movilidad:

* trayecto;
* reto;
* participación;
* badge;
* recompensa.

Podríamos querer presentar todas esas cosas mediante una interfaz temporal denominada “Actividad”, pero eso es una **decisión de presentación**.

No significa que todas pertenezcan a un mismo tipo semántico `Activity`.

Por tanto, sí: deberá existir **configuración específica de escenario/capacidad/sector**, sin caer en el extremo contrario de crear cuatro modelos incompatibles.

---

# 2. Tu segunda observación es todavía más importante: Journey ≠ Experience

Aquí mi terminología anterior necesita corrección.

El repositorio ya contiene:

* `ExperienceDefinition`;
* participation;
* events;
* rules;
* effects;
* lógica `evaluateEventAcrossExperiences`.

Es decir, **Experience ya es un concepto de dominio existente**. 

Además, la gobernanza del repositorio distingue explícitamente:

**TES semantic authority → product functional translation → technical implementation**. 

Eso significa que no deberíamos introducir alegremente un concepto como `Journey` que pueda competir semánticamente con `Experience`.

Aquí aplicaría una regla importante para toda Demo Factory:

> **Si TES ya define una entidad del dominio, Demo Factory debe consumirla o traducirla; no crear una entidad paralela con significado aproximadamente equivalente.**

Ésta es precisamente la utilidad de haber construido esa capa semántica.

---

# 3. Journey debería desaparecer del núcleo de nuestra arquitectura

No necesariamente prohibiría la palabra *journey* en una conversación comercial.

Por ejemplo:

> “Queremos demostrar el customer journey desde la reserva hasta la recompensa.”

Eso es perfectamente comprensible.

Pero **no utilizaría `Journey` como contrato arquitectónico de Demo Factory**.

Tenemos que distinguir al menos tres cosas:

### Scenario

Describe **el contexto que queremos demostrar**.

Por ejemplo:

```text
Prospect:
Hotel Group X

Scenario:
Business Traveller

Actor:
Frequent corporate guest

Initial state:
Gold member

Business hypothesis:
Increase direct booking and ancillary consumption
```

### Experience

Es el constructo funcional/semántico gobernado por TES.

Y aquí incorporamos tu aclaración esencial:

> Una Experience **puede requerir completion o no**, y su estructura **puede ser temporal/secuencial o no secuencial**.

Además existe el concepto de **coverage**, que puede condicionar el reconocimiento, recompensa o incentivo.

No quiero todavía inventar una estructura del tipo:

```yaml
completion: true
sequence: false
coverage: 0.8
reward: ...
```

porque sería precisamente repetir el error que estamos intentando evitar: **inventar nuestro propio TES de memoria**.

El siguiente análisis de Codex debe consultar el contrato TES disponible en el repositorio y decirnos cómo se representa realmente cada dimensión.

### Demo Script

Éste es el concepto que anteriormente estaba llamando vagamente *Journey*.

Un Demo Script sería simplemente:

> **la secuencia de acciones que nosotros decidimos ejecutar durante una demostración comercial.**

Por ejemplo:

```text
1. Abrir perfil.
2. Mostrar status Gold.
3. Registrar estancia.
4. Mostrar avance de Experience.
5. Completar segunda condición.
6. Mostrar incentivo obtenido.
7. Redimir beneficio.
```

Eso **no significa que Experience sea secuencial**.

La secuencia pertenece a nuestra **narración de la demo**.

Es una diferencia crítica:

$$
Demo\ Script \neq Experience
$$

Un script necesariamente tiene orden porque una presentación transcurre en el tiempo.

Una Experience puede no tenerlo.

---

# 4. Scenario tampoco equivale a Experience

Esto es especialmente importante para el caso hotelero.

Podemos tener:

```text
Hotel Chain
│
├── Scenario A
│   Business traveller
│
└── Scenario B
    Resort guest
```

Cada Scenario podría utilizar:

```text
Scenario A
 ├── Experience X
 ├── Experience Y
 └── Experience Z
```

mientras que:

```text
Scenario B
 ├── Experience Y
 ├── Experience Q
 └── Experience R
```

Incluso una misma Experience podría aparecer en más de un escenario si conceptualmente tiene sentido.

Por tanto obtenemos una ontología mucho más limpia:

```text
PROSPECT
   │
   ▼
DEMO PACKAGE
   │
   ├──────── BRAND
   │
   ├──────── LOCALE
   │
   ├──────── CAPABILITIES
   │
   ├──────── DATA SOURCE
   │
   │
   └──────── SCENARIOS
                │
                ├──────── Actors / initial conditions
                │
                ├──────── EXPERIENCES
                │            │
                │            ├── events
                │            ├── rules
                │            ├── participation
                │            ├── effects
                │            ├── completion semantics
                │            ├── temporal semantics
                │            └── coverage / incentives
                │
                └──────── Optional Demo Script
```

Los términos exactos de la rama Experience tendrán que venir de **TES**, no de este esquema conceptual mío.

---

# 5. Esto modifica también el papel de `DemoPackage`

Antes habíamos dicho:

> `DemoPackage` debe convertirse en la fuente autoritativa de qué es la demo.

Lo mantengo.

Pero con una precisión importante:

> **DemoPackage no debe convertirse en una nueva autoridad semántica sobre Experiences.**

Debe ser una **composition root**.

Es decir, puede declarar:

> esta demo utiliza estas Experiences.

Pero el significado de esas Experiences procede de TES y de los contratos derivados apropiados.

Esto conserva la arquitectura que ya existe en tu repositorio:

```text
TES
 ↓
semantic contract
 ↓
product interpretation
 ↓
DemoPackage composition
 ↓
runtime
 ↓
UI
```

Esto me parece mucho más robusto que:

```text
DemoPackage
 ↓
inventa todos los conceptos
```

---

# 6. También cambia nuestra concepción de “sector”

Tu primera observación permite introducir otra mejora.

No quiero hacer:

```text
AirlineData
HotelData
RetailData
TransportData
```

como cuatro grandes estructuras independientes.

Eso nos llevaría rápidamente a forks semánticos.

Preferiría que el sector influya fundamentalmente en:

**Scenario + Content + Capabilities + Experiences + Fixtures + Presentation**

Por ejemplo:

```text
Hospitality
  │
  ├── scenario: business-traveller
  │
  └── scenario: resort-family
```

puede utilizar capacidades comunes:

```text
Profile
Rewards
Benefits
Experiences
Transactions
Status
```

pero instanciadas de manera muy diferente.

Por eso Demo Factory deberá distinguir entre:

> **capacidad genérica**

y

> **representación sectorial de esa capacidad**.

Ese es exactamente el tipo de abstracción que queremos descubrir, no imponer prematuramente.

---

# 7. Hay que modificar el prompt para Codex

Sí. **No utilizaría ya el anterior sin modificaciones.**

Además, ahora quiero aprovechar la siguiente iteración para obligar a Codex a consultar el conocimiento TES que ya está en el repositorio.

Usa esta versión en su lugar:

> Using the repository assessment already produced, perform a second architecture analysis for the proposed Convercus Demo Factory. Do not modify any files.
>
> Treat the following as working architectural hypotheses to test against the repository and the TES-derived semantic contracts, not as instructions to force-fit the code.
>
> ### Architectural principles
>
> * `DemoPackage` should evolve toward the authoritative **composition contract** for a demo, but it must NOT become a competing semantic authority for domain concepts already governed by TES.
> * TES and the derived semantic/product contracts remain authoritative for the meaning of `Experience` and related domain concepts.
> * A demo should primarily be an instance of a shared core rather than a fork.
> * `DemoPackage` may reference separate brand, scenario, content, fixture and Experience assets rather than containing everything inline.
> * Runtime behaviour should be driven by configuration where possible.
> * `DataAdapter` should remain the abstraction between domain/UI and data sources.
> * Mock, simulation and future Convercus API adapters should share an explicit behavioural contract.
> * Prospect-specific requirements should become configuration unless they represent a genuinely reusable new capability.
>
> ### Important semantic corrections
>
> 1. Do NOT assume that the current `Activity` / activity-feed model is a universal domain concept.
>
>    Inspect what `Activity`, `ActivityItem`, transactions, events, participation and other related concepts currently mean in the repository.
>
>    Determine whether the existing activity feed should be understood as:
>
>    * a domain concept;
>    * a capability-specific model;
>    * a UI projection of underlying domain events/state;
>    * or something else.
>
>    Consider sectoral variability across airline, retail, public transport and hospitality before recommending a common abstraction.
>
> 2. Do NOT use `Journey` as a substitute for `Experience`.
>
>    Inspect the TES baseline, semantic contracts, product interpretations and shared contracts available in this repository and reconstruct the actual semantics of `Experience`.
>
>    In particular, identify how the existing authoritative material represents or constrains:
>
>    * participation;
>    * events;
>    * rules;
>    * effects;
>    * completion versus non-completion;
>    * temporal/sequential versus non-sequential behaviour;
>    * coverage/progress;
>    * reward or incentive consequences associated with coverage or participation.
>
>    Use the terminology found in TES/contracts rather than inventing replacement terminology. If any of these concepts is not actually defined in the inspected sources, state that explicitly.
>
> 3. Distinguish clearly between:
>
>    * **Scenario**: the commercial/demo context, actor(s), initial conditions and use case being demonstrated.
>    * **Experience**: the TES-governed domain construct.
>    * **Demo Script**: an optional presenter-facing sequence of actions used to demonstrate a scenario. The temporal order of a Demo Script must not imply that the underlying Experience itself is sequential.
>
>    Test whether these three concepts should remain distinct in the architecture.
>
> ### Analysis requested
>
> Produce:
>
> 1. A proposed responsibility map for:
>
>    * DemoPackage
>    * Demo Runtime
>    * DataAdapter
>    * Brand
>    * Scenario
>    * Experience
>    * Demo Script
>    * Capabilities/Modules
>    * Fixtures/content
>    * UI projections
>    * TES/semantic governance
>
> 2. Identify every current file or abstraction that could participate in each responsibility.
>
> 3. Identify conflicts, overlaps, duplicated semantic representations or missing boundaries.
>
> 4. Explain how `DemoPackage`, `AppSnapshot`, `ExperienceDefinition`, events, participation, rules and effects currently relate, and how they could relate without prematurely redesigning them.
>
> 5. Determine whether the current activity feed should remain a reusable UI module, become configurable, be derived from underlying state/events, or be treated differently. Do not assume the answer in advance.
>
> 6. Identify the minimum architectural changes required to make a second demo possible without copying or forking the application.
>
> 7. Identify what should explicitly NOT be refactored yet.
>
> 8. Propose no more than three alternative composition models, comparing their complexity, extensibility, semantic fidelity to TES and suitability for a commercial Demo Factory.
>
> ### Architectural test scenarios
>
> Test the alternatives conceptually against:
>
> * airline loyalty;
> * retail loyalty;
> * public transport / sustainable mobility;
> * hospitality: one hotel chain containing both business hotels and vacation resorts.
>
> For hospitality, explicitly test:
>
> * whether one prospect/brand can contain multiple Scenarios;
> * whether those Scenarios can use different combinations of Experiences;
> * whether the same Experience could be reused across Scenarios where semantically valid;
> * whether presentation/activity/history views can differ without changing the underlying semantic model.
>
> Do not implement any of these scenarios.
>
> ### Epistemic requirements
>
> For every important conclusion distinguish:
>
> * **repository fact**;
> * **TES/semantic-contract fact**;
> * **architectural inference**;
> * **recommendation**.
>
> Cite the repository files or TES-derived artifacts supporting semantic claims.
>
> Do not modify files, generate implementation code or perform a refactor.

Éste es ahora el prompt que yo lanzaría.

---

## Y hemos aprendido algo importante antes incluso de programar

Tus dos objeciones son exactamente el tipo de revisión que queremos introducir en Demo Factory.

La primera detecta un error de **generalización ontológica**:

> una pantalla existente → no implica una entidad universal.

La segunda detecta un error de **duplicación semántica**:

> una palabra intuitiva (*Journey*) → no debe desplazar un concepto ya gobernado (*Experience*).

Eso nos indica que la arquitectura de Demo Factory necesitará mantener tres clases de verdad separadas:

**TES define qué significa el producto.**

**DemoPackage define qué combinación del producto demostramos.**

**UI define cómo hacemos observable esa combinación.**

Y probablemente ésa sea una de las decisiones arquitectónicas más importantes que hemos establecido hasta ahora.

---
---
Sí. Y creo que aquí has encontrado una abstracción bastante más interesante: **`Activity` podría tener entidad arquitectónica propia, pero no con el significado que posee actualmente en el prototipo**.

En el código actual, `ActivityItem` es básicamente una representación para una pantalla: incluso incorpora `IconName` y `tone`, mezclando el acontecimiento con decisiones visuales.  Eso no sirve todavía como concepto de dominio.

Pero tu propuesta sería otra cosa:

> **Activity = trama observable de interacciones del consumidor con el ecosistema.**

Y sobre esa trama se proyectarían las **Experiences** definidas conforme a TES.

Creo que ésta puede ser una pieza central de Demo Factory.

---

# 1. Activity como trama de interacción

Imaginemos un consumidor \(u\).

Durante un determinado periodo realiza una serie de interacciones:

$$
T_u = \{e_1,e_2,e_3,\ldots,e_n\}
$$

Cada \(e_i\) sería un evento observado con determinadas propiedades:

$$
e_i =
(type,\ time,\ context,\ attributes,\ outcome)
$$

Por ejemplo, para una cadena hotelera:

```text
booking
check-in
breakfast
restaurant purchase
spa visit
second night
mobile-app interaction
late checkout
survey
referral
```

Eso sería la **trama de interacción**.

No implica todavía:

* puntos;
* incentivos;
* recompensas;
* Experiences;
* completion.

Es simplemente:

> **qué ha hecho el consumidor y en qué contexto.**

Y esto me parece epistemológicamente limpio porque separa **observación** de **interpretación**.

---

# 2. Una Experience sería una estructura interpretativa aplicada sobre esa trama

Aquí aparece tu idea de intersección.

Supongamos que tenemos tres Experiences:

$$
E_1,E_2,E_3
$$

La trama del consumidor puede tener diferentes grados de correspondencia con ellas.

Conceptualmente:

$$
T_u \cap E_1
$$

puede representar una cobertura parcial.

Mientras que:

$$
T_u \cap E_2
$$

puede representar cobertura completa.

Y:

$$
T_u \cap E_3 = \varnothing
$$

puede significar que ninguna interacción relevante para esa Experience se ha producido.

Esto sería extraordinariamente útil.

Pero haría una precisión matemática importante:

> **la intersección de conjuntos funciona como buena intuición, pero probablemente no sea suficiente como modelo formal.**

Porque, como tú mismo has señalado, una Experience puede ser:

* secuencial;
* no secuencial;
* completada;
* no completada;
* potencialmente dependiente de cobertura;
* potencialmente dependiente de condiciones.

Por tanto necesitamos algo más general que una simple intersección.

---

# 3. Yo introduciría un operador de cobertura

Conceptualmente:

$$
C(E,T)
$$

donde:

* \(E\) = Experience;
* \(T\) = trama de interacción;
* \(C\) = función de correspondencia/cobertura.

Y:

$$
0 \leq C(E,T) \leq 1
$$

Podríamos tener:

$$
C(E,T)=0
$$

sin cobertura;

$$
0<C(E,T)<1
$$

cobertura parcial;

$$
C(E,T)=1
$$

cobertura completa.

**Pero esto es sólo nuestra abstracción matemática de trabajo.** No debemos asumir que TES utilice exactamente esta escala o estos estados; Codex deberá reconstruir del corpus TES cómo están modelados realmente coverage, participation, completion, rules y effects.

El repositorio sí confirma que ya existen contratos para `ExperienceDefinition`, participation, event, rule y effect, además de una función que evalúa eventos sobre varias Experiences. 

Por tanto nuestra idea no surge completamente desde cero: parece compatible con una arquitectura que ya empieza a considerar:

$$
Event \rightarrow Experience \rightarrow Rules \rightarrow Effects
$$

---

# 4. Y ahí aparece la incentivación

Tu siguiente razonamiento me parece especialmente importante.

No debería necesariamente existir:

$$
Experience\ completed \Rightarrow Reward
$$

como única posibilidad.

Podría existir una función:

$$
I(E,T)=f(C(E,T),R_E,S_E,\ldots)
$$

donde:

* \(C\) = cobertura;
* \(R_E\) = reglas de la Experience;
* \(S_E\) = estado relevante;
* \(I\) = consecuencia/incentivo.

De este modo podrían existir distintas situaciones.

### Cobertura parcial no incentivada

$$
C=0.3 \Rightarrow I=0
$$

### Cobertura parcial incentivada

$$
C=0.5 \Rightarrow I=A
$$

### Cobertura avanzada

$$
C=0.8 \Rightarrow I=B
$$

### Cobertura completa

$$
C=1 \Rightarrow I=C
$$

O incluso:

$$
C=1 \not\Rightarrow Reward
$$

si esa Experience no estuviera diseñada para producir una recompensa.

Esto coincide exactamente con tu observación:

> **completion y incentivación no deben ser semánticamente equivalentes.**

Y es una distinción fundamental.

---

# 5. Una misma Activity puede intersectar varias Experiences

Aquí es donde el modelo empieza a ser especialmente poderoso.

Supongamos una trama:

```text
T =

hotel booking
      ↓
direct booking
      ↓
2-night stay
      ↓
restaurant consumption
      ↓
spa visit
      ↓
survey
```

Ahora tenemos:

```text
Experience A
Direct Booking
```

```text
Experience B
Discover the Hotel
```

```text
Experience C
Wellness
```

```text
Experience D
Engagement
```

Un mismo acontecimiento podría contribuir a diferentes Experiences.

Por ejemplo:

```text
spa visit
```

podría contribuir a:

```text
Experience B → Discover the Hotel
Experience C → Wellness
```

Por tanto:

$$
T \cap E_B \neq \varnothing
$$

y simultáneamente:

$$
T \cap E_C \neq \varnothing
$$

Esto significa que las Experiences no necesariamente particionan Activity.

Pueden **solaparse**.

Éste es un detalle arquitectónico importante.

No debemos modelar:

```text
event → one Experience
```

sino potencialmente:

```text
                    Experience A
                   /
Interaction event ─── Experience B
                   \
                    Experience C
```

siempre que TES permita semánticamente dicha multiplicidad.

---

# 6. Y esto resuelve elegantemente tu problema sectorial

Ahora podemos reinterpretar lo que discutíamos sobre hoteles.

No necesitamos que Demo Factory tenga:

```text
HotelBusinessActivity
ResortActivity
AirlineActivity
RetailActivity
TransportActivity
```

Podemos tener un concepto más general:

## Interaction Trace

con eventos contextualizados.

Por ejemplo:

### Business hotel

```text
booking
mobile check-in
breakfast
meeting-room booking
second stay
late checkout
```

### Resort

```text
booking
restaurant
spa
kids club
excursion
pool activity
survey
```

La estructura abstracta es la misma:

```text
Consumer
    │
    ▼
Interaction
    │
    ├── type
    ├── timestamp
    ├── context
    ├── attributes
    └── outcome
```

Lo sectorial aparece en:

* tipos de interacción;
* atributos;
* contexto;
* Experiences disponibles;
* reglas;
* presentación.

No necesariamente en el concepto fundamental de Activity.

Eso es una abstracción mucho más escalable.

---

# 7. Pero evitaría llamar a la entidad interna `ActivityItem`

Aquí mantendría dos niveles.

### Capa semántica

Podríamos utilizar provisionalmente algo como:

**Interaction Event**

y:

**Interaction Trace**

o incluso tu término:

**Consumer Interaction Trace**.

### Capa visual

Podríamos seguir teniendo:

**Activity Feed**.

Entonces:

```text
Interaction Trace
       │
       ├──────── Experience evaluation
       │
       ├──────── Coverage computation
       │
       └──────── Activity Feed projection
```

Esto es muchísimo más limpio.

El Activity Feed se convierte simplemente en **una vista** de la trama.

Por ejemplo:

```text
09:32  Check-in completed
12:43  Restaurant purchase
16:20  Spa visit
18:15  Wellness Experience 75%
```

Pero internamente no tenemos por qué almacenar todo como `ActivityItem`.

---

# 8. El caso secuencial exige otra precisión

Aquí debemos ser rigurosos.

Supongamos una Experience:

```text
A → B → C
```

Entonces tener:

$$
\{A,B,C\}
$$

en Activity no garantiza completion.

Si el consumidor hizo:

```text
C → A → B
```

la intersección de conjuntos sería completa:

$$
T \cap E = E
$$

pero la Experience secuencial no habría sido satisfecha.

Por tanto necesitaremos conceptualmente:

$$
C(E,T)
$$

que no sólo examine **qué acontecimientos existen**, sino las reglas de correspondencia.

Podría comprobar:

### Experience no secuencial

Presencia:

$$
A \land B \land C
$$

### Experience secuencial

Orden:

$$
A \prec B \prec C
$$

### Experience cuantitativa

Por ejemplo:

$$
count(A)\geq5
$$

### Experience temporal

Por ejemplo:

$$
B-A<30\ days
$$

### Experience condicionada

Por ejemplo:

$$
A \land B \land segment=Gold
$$

No sabemos todavía cuáles de estos mecanismos están realmente definidos por TES. Por tanto deben considerarse **ejemplos de clases lógicas**, no características confirmadas de Convercus.

---

# 9. Esto nos permite separar cinco capas extraordinariamente bien

Creo que estamos acercándonos a una arquitectura de dominio interesante:

```text
                CONSUMER
                    │
                    ▼
          INTERACTION TRACE
                    │
           observed events
                    │
                    ▼
             EXPERIENCE
               MATCHER
                    │
         ┌──────────┼──────────┐
         │          │          │
       Exp A      Exp B      Exp C
        40%        100%       70%
         │          │          │
         ▼          ▼          ▼
       Rules      Rules      Rules
         │          │          │
         └──────────┼──────────┘
                    ▼
             EFFECTS /
            INCENTIVES
                    │
                    ▼
                 STATE
                    │
           ┌────────┴────────┐
           ▼                 ▼
     Activity Feed      Experience UI
```

Y fíjate en algo muy importante:

**Activity no depende de Experience.**

El consumidor interactúa.

Después:

**Experience interpreta Activity.**

Eso me parece conceptualmente muy potente.

---

# 10. Además preserva causalidad epistemológica

Desde una perspectiva DIKW, incluso queda muy elegante.

### DATA

```text
hotel check-in
restaurant purchase
spa visit
```

### INFORMATION

Los acontecimientos pertenecen a una misma trama de consumidor.

### KNOWLEDGE

La trama cubre:

```text
Experience A → 100%
Experience B → 60%
Experience C → 20%
```

### DECISION / EFFECT

Conforme a reglas:

```text
Experience A → reward
Experience B → progress incentive
Experience C → no effect yet
```

Es decir:

$$
Interactions
\rightarrow
Coverage
\rightarrow
Interpretation
\rightarrow
Effect
$$

Esto es bastante superior a una arquitectura donde simplemente tenemos:

```text
ActivityItem[]
```

---

# 11. Y modifica ligeramente nuestro modelo de Demo Factory

Yo cambiaría ahora:

```text
DemoPackage
 ├── Scenario
 ├── Experiences
 ├── Activity
```

por:

```text
DemoPackage
│
├── Prospect / Brand
├── Scenario
│
│    ├── Actors
│    ├── Initial State
│    └── Interaction Fixtures
│
├── Experiences
│    └── references to TES-governed definitions
│
├── Data Source
│
├── Capabilities
│
└── Presentation
```

Y Runtime produciría:

```text
Interaction events
       ↓
Experience evaluation
       ↓
Experience state / coverage
       ↓
Effects
       ↓
UI projections
```

Eso es significativamente más coherente.

---

## La conclusión importante

Tu intuición acerca de Activity no sólo es compatible con lo que estamos haciendo; creo que **resuelve uno de los problemas que Codex detectó**.

Codex decía que actualmente:

* `DemoPackage` describe Experiences;
* `AppSnapshot` describe lo que muestra la aplicación;
* ambos están desconectados. 

La **Interaction Trace** puede ser parte del puente conceptual entre ambos:

$$
DataAdapter
\rightarrow Interaction\ State
\rightarrow Experience\ Evaluation
\rightarrow Derived\ State
\rightarrow AppSnapshot/UI
$$

Mi única precaución sería **no cristalizar todavía nombres ni estructuras** hasta que Codex haga la lectura dirigida de TES que le hemos pedido. Particularmente debemos verificar cómo TES conceptualiza exactamente *events, participation, completion, coverage, rules y effects*.

Pero como hipótesis arquitectónica, yo actualizaría nuestro modelo así:

> **Activity, entendida no como feed sino como trama de interacción observable del consumidor, puede constituir el sustrato factual sobre el que las Experiences proyectan sus reglas, produciendo diferentes grados de cobertura y, conforme a sus reglas y efectos, diferentes incentivaciones.**

Ésta me parece ahora una de las hipótesis más importantes que debería **añadirse al prompt de Codex antes de ejecutar la segunda inspección**.

---
---

# INSTRUCCIÓN SESION 2

# Convercus Demo Factory — Session 2: Repository Anatomy and Semantic Architecture

## Purpose of this session

Using the repository assessment already produced, perform a second, deeper architectural analysis of the current Convercus repository.

Do **not** modify any files, generate implementation code, perform a refactor, install dependencies, or redesign the application.

The purpose of this session is to progress through the following cognitive sequence:

**REMEMBER → UNDERSTAND → APPLY → ANALYZE → EVALUATE → CREATE**

The final output should therefore not merely describe the repository. It should reconstruct the current architecture, understand the TES-governed semantic model, test architectural hypotheses against representative commercial scenarios, compare alternatives, and create an evidence-based target architecture hypothesis for the future Demo Factory.

Treat all architectural statements below as **hypotheses to test**, not conclusions to force onto the repository.

---

# 0. Epistemic rules

For every material conclusion, explicitly distinguish between:

* **Repository Fact**
* **TES / Semantic Contract Fact**
* **Architectural Inference**
* **Recommendation**
* **Unresolved / Insufficient Evidence**

Never convert an inference into a fact.

Never invent TES semantics.

When describing `Experience`, participation, events, rules, effects, completion, temporal behaviour, coverage, incentives or related concepts, inspect the actual TES baseline, semantic contracts, product interpretations and shared contracts available in the repository.

Cite the repository files or TES-derived artifacts that support each important semantic conclusion.

If a concept discussed in this instruction is not supported by the repository or TES material, state that explicitly.

---

# BLOOM LEVEL 1 — REMEMBER

## Reconstruct the current system

Using the previous repository assessment as a starting point, identify the existing artifacts that currently represent or participate in:

* `DemoPackage`
* `AppSnapshot`
* `DataAdapter`
* `MockDataAdapter`
* `ExperienceDefinition`
* participation
* events
* rules
* effects
* capability status
* scenarios
* brand configuration
* application configuration
* demo fixtures/data
* routes
* UI projections
* TES semantic governance
* product interpretations
* shared contracts

For each item provide:

1. current file(s);
2. current responsibility;
3. whether it is executable, declarative, semantic/governance, or test-only;
4. whether it currently participates in runtime composition.

Do not propose changes yet.

The objective of this section is factual reconstruction.

---

# BLOOM LEVEL 2 — UNDERSTAND

## Reconstruct the semantic model

Study the TES baseline, semantic contracts, product interpretations and shared contracts relevant to `Experience`.

Explain, using the terminology actually present in those sources, how the repository currently understands:

* Experience;
* participation;
* event;
* rule;
* effect;
* state, where applicable;
* completion versus non-completion;
* temporal or sequential behaviour;
* non-sequential behaviour;
* coverage or progress;
* reward;
* incentive;
* consequences/effects of participation or coverage.

Do not assume that all Experiences:

* must be completed;
* must be sequential;
* must produce a reward;
* have identical coverage semantics.

Explicitly determine whether TES supports, rejects, or leaves undefined those possibilities.

Also explain the existing `evaluateEventAcrossExperiences` logic and what it actually establishes semantically versus what remains outside its current implementation.

---

# BLOOM LEVEL 2B — UNDERSTAND THE ACTIVITY HYPOTHESIS

## Distinguish current Activity from a possible interaction model

The current application contains `ActivityItem` and an Activity Feed.

Do not assume that this current implementation represents a valid universal domain abstraction.

First reconstruct what the existing `Activity`, `ActivityItem`, transactions, events and related concepts actually represent.

Then evaluate the following architectural hypothesis:

> A useful domain-level concept may exist corresponding to the observable interaction trace of a consumer: a set or temporally ordered stream of interactions/events generated through the consumer's relationship with the ecosystem.

For the purposes of analysis, refer to this provisionally as:

**Consumer Interaction Trace**

Do not rename repository entities or assume this term belongs in the final implementation.

Determine whether the repository and TES material support a conceptual separation between:

1. underlying consumer interactions/events;
2. Experience evaluation against those interactions;
3. resulting Experience state/coverage/effects;
4. presentation projections such as an Activity Feed, history or timeline.

Specifically analyze whether the current `ActivityItem` model is:

* a domain object;
* a capability-specific object;
* a UI projection;
* a mixture of these;
* or something else.

Pay particular attention to the current coupling between data and UI concepts such as icons, visual tone and presentation strings.

---

# BLOOM LEVEL 3 — APPLY

## Apply the semantic model to representative commercial scenarios

Without implementing anything, test the reconstructed domain model against four representative sectors:

### A. Airline loyalty

Possible interactions may include, only as test examples:

* booking;
* flight;
* ancillary purchase;
* status progression;
* redemption;
* campaign participation.

### B. Retail loyalty

Possible interactions may include:

* purchase;
* product/category behaviour;
* coupon use;
* referral;
* promotion participation;
* redemption.

### C. Public transport / sustainable mobility

Possible interactions may include:

* trip;
* route usage;
* mobility challenge;
* participation;
* badge/reward-related effects;
* repeated behavioural patterns.

### D. Hospitality

Model one hotel chain containing at least two distinct commercial scenarios:

#### Business Hotel Scenario

Examples may include:

* booking;
* stay;
* check-in;
* breakfast;
* repeated stays;
* upgrades;
* meeting-related services;
* late checkout.

#### Vacation Resort Scenario

Examples may include:

* booking;
* stay;
* restaurant consumption;
* spa;
* activities;
* family services;
* excursions;
* engagement with resort experiences.

These interaction examples are analytical probes, not assumed Convercus entities.

For each sector determine whether the same underlying architecture can represent:

* different interaction types;
* different combinations of Experiences;
* different presentation views;
* different incentives;
* different scenario configurations;

without requiring a sector-specific fork of the application.

---

# BLOOM LEVEL 3B — APPLY THE EXPERIENCE / INTERACTION RELATIONSHIP

Test the following hypothesis against TES:

> Consumer interactions may provide the observable factual substrate against which one or more Experiences are evaluated.

Investigate whether a single interaction/event may legitimately contribute to:

* no Experience;
* one Experience;
* multiple Experiences;

according to the existing semantic model.

Also determine whether different Experiences may overlap in the interactions relevant to them.

Do not assume simple set intersection is sufficient.

Explicitly consider whether Experience evaluation may depend on properties such as:

* presence of events;
* ordering;
* timing;
* frequency/count;
* conditions;
* accumulated state;
* coverage;
* other TES-defined rules.

If TES does not support any of these dimensions, state so.

---

# BLOOM LEVEL 4 — ANALYZE

## Analyze the architecture as a composition system

Treat the following as a working hypothesis:

> `DemoPackage` may evolve into the authoritative composition contract for a demo, while TES remains the semantic authority for domain concepts such as `Experience`.

Analyze whether this separation is coherent with the existing repository.

In particular distinguish:

### Semantic authority

What defines what an Experience **means**?

### Composition authority

What defines which Experiences, capabilities, data, brand and scenarios belong to a specific demo?

### Runtime authority

What decides which adapter, modules and state are active?

### Presentation authority

What decides how underlying state is displayed?

---

## Analyze these candidate responsibilities

Produce a responsibility map for:

* DemoPackage
* Demo Runtime
* DataAdapter
* Data source / adapter resolver
* Brand
* Scenario
* Experience
* Consumer Interaction Trace
* Demo Script
* Capabilities / Modules
* Fixtures / Content
* Domain State
* AppSnapshot
* UI projections
* TES / semantic governance

For each responsibility identify:

1. what it should conceptually own;
2. what it should not own;
3. which current repository artifacts could participate;
4. overlaps with existing abstractions;
5. missing boundaries;
6. semantic risks.

---

# Scenario vs Experience vs Demo Script

Explicitly test whether these concepts should remain separate.

## Scenario

Working definition:

A commercial/demo context describing:

* prospect context;
* actors;
* initial conditions;
* use case;
* business hypothesis;
* relevant configuration.

## Experience

Must use TES-derived meaning.

Do not redefine it from the working definition of Scenario.

## Demo Script

Working definition:

An optional presenter-facing sequence used to demonstrate a Scenario.

A Demo Script is necessarily ordered because a presentation occurs through time.

Its ordering must **not imply that the underlying Experience itself is sequential**.

Determine whether this distinction is architecturally useful and semantically safe.

---

# Interaction Trace vs Experience

Analyze the possible relationship:

Consumer Interaction Trace
→ Experience evaluation
→ participation / coverage / state
→ rules / effects
→ incentives or other consequences
→ UI projections

Do not assume this exact pipeline exists in TES.

Determine which parts are:

* supported;
* partially supported;
* inferred;
* unsupported.

---

# DemoPackage vs AppSnapshot

Analyze the current disconnect between `DemoPackage` and `AppSnapshot`.

Explain:

* what each represents today;
* whether one should contain the other;
* whether both should instead depend on a third runtime/domain model;
* whether `AppSnapshot` should remain adapter-facing;
* how Experience-derived state might become visible to the UI without coupling TES directly to React.

Do not redesign either interface prematurely.

---

# BLOOM LEVEL 5 — EVALUATE

## Evaluate architectural alternatives

Propose **no more than three** alternative composition architectures.

Each alternative must preserve, as far as possible:

* TES semantic authority;
* a shared application core;
* prospect isolation;
* configurable branding;
* multiple scenarios per prospect;
* multiple Experiences per scenario;
* potential reuse of an Experience across scenarios;
* configurable sector-specific interaction content;
* mock/simulation/future API data modes;
* deterministic demo behaviour where required;
* future secure Convercus API integration.

For each architecture evaluate:

### Semantic fidelity

Does it preserve TES as semantic authority?

### Reusability

Can new prospects be created mainly through configuration?

### Sector scalability

Can airline, retail, mobility and hospitality coexist?

### Scenario flexibility

Can one hotel brand support both business-hotel and resort scenarios?

### Experience flexibility

Can scenarios use different Experience combinations without redefining Experience?

### Interaction flexibility

Can the same interaction model support sector-specific interaction types without requiring sector-specific application forks?

### API evolution

Can mock, simulation and future Convercus API adapters coexist?

### Complexity

What technical complexity does the model introduce?

### Marginal Demo Code Cost

Would each additional demo tend to require less new code?

### Risk

What are the likely failure modes?

---

# Explicitly evaluate the following working principles

Assess whether the evidence supports these principles:

1. **A demo should be an instance of a shared core rather than a fork.**

2. **DemoPackage should be a composition root, not a competing semantic ontology.**

3. **TES should remain the semantic authority for Experience.**

4. **Prospect-specific variation should become configuration unless it represents a genuinely reusable capability.**

5. **Consumer Interaction Trace may be a useful factual substrate from which Experience state can be derived.**

6. **Activity Feed should likely be treated as a presentation projection rather than assumed to be the universal interaction model.**

7. **Scenario, Experience and Demo Script should remain distinct concepts.**

8. **Completion, coverage and incentivization must not be assumed to be equivalent concepts.**

For each principle classify it as:

* strongly supported;
* provisionally supported;
* unsupported;
* contradicted;
* requires further TES clarification.

---

# BLOOM LEVEL 6 — CREATE

## Create an evidence-based target architecture hypothesis

Without generating implementation code, create a proposed **Demo Factory Architecture v0.1**.

This is not yet an implementation specification.

It should contain:

### 1. Architecture map

Show the proposed relationships between:

* TES;
* semantic/product contracts;
* DemoPackage;
* Scenario;
* Experience;
* interaction/event state;
* DataAdapter;
* runtime;
* capabilities/modules;
* domain/application state;
* UI projections.

### 2. Authority map

Explicitly state which layer is authoritative for:

* semantic meaning;
* demo composition;
* data acquisition;
* Experience evaluation;
* runtime state;
* presentation;
* branding;
* scenario configuration.

### 3. Core invariants

Propose a small set of architectural invariants that future implementation should not violate.

Example form:

> “Adding a new prospect must not require redefining TES domain concepts.”

Do not simply copy this example; derive the invariants from the evidence.

### 4. Minimum viable architectural transition

Identify the **minimum architectural changes** required to make a second prospect demo possible without copying or forking the application.

Do not implement them.

Order them by dependency, not by coding convenience.

### 5. Explicit non-goals

Identify what should **not** be refactored or built yet.

Include consideration of:

* large-scale UI decomposition;
* CSS redesign;
* backend implementation;
* API integration;
* multi-tenancy;
* production connectivity;
* unnecessary state-management frameworks;
* Experience Builder implementation.

### 6. Open semantic questions

List all remaining TES/domain questions that must be resolved before implementation.

Do not hide unresolved semantic uncertainty behind architectural abstractions.

### 7. Architecture Decision candidates

Identify the decisions that are now mature enough to become future ADRs.

Do not write the ADRs yet.

---

# Final architectural stress test

Before concluding, use the Hospitality case as the hardest current test.

Assume:

One hotel company
→ one brand or brand family
→ Business Hotels + Vacation Resorts
→ multiple Scenarios
→ potentially overlapping Experiences
→ different interaction patterns
→ potentially different incentives
→ potentially different UI projections.

Determine whether Demo Factory Architecture v0.1 can represent this without:

* creating two separate applications;
* redefining Experience;
* introducing business-hotel-specific or resort-specific core domain types unnecessarily;
* forcing all interaction events into a single generic UI-oriented `ActivityItem`;
* assuming all Experience progress is sequential;
* assuming completion necessarily produces a reward.

If the architecture fails this test, explain where and revise the architecture hypothesis before completing the report.

---

# Output structure

Use exactly this top-level structure:

1. Executive conclusion
2. Bloom 1 — Repository reconstruction
3. Bloom 2 — Semantic understanding
4. Bloom 2B — Activity / Consumer Interaction Trace
5. Bloom 3 — Sector application
6. Bloom 3B — Interaction-to-Experience evaluation
7. Bloom 4 — Architectural analysis
8. Bloom 5 — Alternative evaluation
9. Bloom 6 — Demo Factory Architecture v0.1
10. Minimum transition path
11. Explicit non-goals
12. Open TES / semantic questions
13. Candidate ADRs
14. Final hospitality stress test
15. Confidence and evidence gaps

Do not modify repository files.

Do not generate implementation code.

Do not begin the refactor.

The purpose of Session 2 is to move from **repository knowledge** to **semantic understanding**, then to **architectural analysis**, **evaluation**, and finally a defensible **architecture hypothesis**.

---
---

# RESPUESTA instrucción sesión 2

# 1. Executive conclusion

- **Repository Fact:** El repositorio contiene actualmente una aplicación React/PWA ejecutable —`convercus-app`— y un segundo producto conceptual —`experience-builder`— todavía sin implementación ejecutable. Alrededor de ellos existe una capa documental de gobierno, extractos TES, interpretaciones de producto, contratos candidatos y recursos compartidos.

- **Repository Fact:** La aplicación visible es una demo monocliente de Convercus alimentada por datos simulados. El runtime no carga un paquete de demo, no selecciona prospecto, no ejecuta Experiences y no accede todavía a la API real. La aplicación instancia directamente un `MockDataAdapter` y consume un `AppSnapshot`.

- **TES / Semantic Contract Fact:** Una Experience no equivale a una campaña, pantalla, promoción, interacción o actividad aislada. Debe permitir reconstruir la cadena:

  `evento → patrón → secuencia → progresión → resultado → medición → aprendizaje`

  También debe declarar el arquetipo del participante y su propensión sectorial. Esto está establecido en el [Experience Ledger](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/TES_Experience_Ledger.md>).

- **Architectural Inference:** El repositorio ya contiene varias piezas adecuadas para una futura Demo Factory —contratos de dominio, adaptador de datos, paquete canónico, manifiesto de capacidades, evaluación independiente de eventos, branding YAML y separación documental TES/producto—, pero esas piezas todavía no forman un sistema conectado.

- **Architectural Inference:** El obstáculo principal no es la falta de componentes visuales. Es la falta de una autoridad de composición que determine, para una demo concreta:

  - qué prospecto y marca están activos;
  - qué escenarios se incluyen;
  - qué Experiences intervienen;
  - qué datos son reales, simulados o mixtos;
  - qué contenido y fixtures se usan;
  - qué módulos se muestran;
  - cómo se inicializa y reinicia el estado;
  - qué script comercial guía la demostración.

- **Recommendation:** La arquitectura v0.1 debería evolucionar hacia un núcleo común configurado mediante paquetes de demo versionados, con una separación explícita entre:

  1. semántica TES;
  2. contratos funcionales de producto;
  3. Experience definitions;
  4. escenarios sectoriales;
  5. paquetes específicos de prospecto;
  6. estado de ejecución;
  7. proyecciones de interfaz.

- **Unresolved / Insufficient Evidence:** Antes de diseñar definitivamente la Demo Factory deben resolverse cinco cuestiones:

  1. ¿Cuál es el modelo oficial de participación y ciclo de vida de una Experience?
  2. ¿Qué topologías admite una secuencia: ramas, repetición, condiciones y N-de-M?
  3. ¿Qué es exactamente una interacción observable y cuándo se convierte en evento significativo para una Experience?
  4. ¿Qué significa `progression` operacionalmente y existe realmente un concepto de “coverage”?
  5. ¿Qué capacidades y contratos ofrece hoy la API de Convercus para Experiences, participaciones, reglas, eventos y resultados?

# 2. Bloom 1 — Repository reconstruction

## 2.1 Estructura y responsabilidades actuales

| Elemento | Ubicación | Responsabilidad actual | Clasificación | Composición en runtime |
|---|---|---|---|---|
| Gobierno | [`00-governance`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/00-governance>) | Principios, decisiones y disciplina documental | Repository Fact | No participa |
| Baseline TES | [`baseline-manifest.yaml`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/baseline-manifest.yaml>) | Identifica las fuentes y versiones del baseline | TES / Semantic Contract Fact | No se verifica al arrancar |
| Extractos TES | [`source-excerpts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts>) | Fuente semántica congelada | TES / Semantic Contract Fact | No participa |
| Interpretación de Experience | [`experience-understanding.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/product-interpretations/experience-understanding.md>) | Traducción provisional de TES a producto | Repository Fact | No participa |
| Contrato de dominio candidato | [`experience-domain/README.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/02-shared-contracts/experience-domain/README.md>) | Lista entidades funcionales compartidas | Repository Fact | No está conectado al TypeScript |
| Relación Experience/Workflow | [`workflows-relationship.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/02-shared-contracts/workflows-relationship.md>) | Delimita provisionalmente responsabilidades | Repository Fact | No participa |
| Marca compartida | [`brand.yaml`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/03-shared-assets/brands/convercus/brand.yaml>) | Tokens y activos de marca Convercus | Repository Fact | Sí, mediante importación estática |
| Configuración de app | [`app.yaml`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/config/app.yaml>) | Título, capacidades y configuración de la app | Repository Fact | Parcialmente |
| Entry point HTML | [`index.html`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/index.html>) | Contenedor y metadatos iniciales | Repository Fact | Sí |
| Bootstrap React | [`main.tsx`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/main.tsx>) | Monta React y el router | Repository Fact | Sí |
| Aplicación y rutas | [`App.tsx`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/app/App.tsx>) | Navegación, pantallas y composición visual | Repository Fact | Sí, concentra la interfaz |
| `DataAdapter` | [`contracts.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts>) | Contrato para obtener snapshot, despachar y reiniciar | Repository Fact | Sí, a través del mock |
| `MockDataAdapter` | [`mock-adapter.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/mock-adapter.ts>) | Datos ficticios y actualización del feed | Repository Fact | Sí, instanciado directamente |
| `AppSnapshot` | [`mock-adapter.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/mock-adapter.ts>) | Datos que la UI presenta: miembro, beneficios, noticias y actividad | Repository Fact | Sí |
| `DemoPackage` | [`contracts.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts>) | Descriptor tipado de una demo | Repository Fact | No |
| Paquete canónico | [`canonical-demo-package.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/canonical-demo-package.ts>) | Ejemplar y contrato de prueba de `DemoPackage` | Repository Fact | Solo pruebas |
| `ExperienceDefinition` | [`contracts.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts>) | Representación ejecutable preliminar de una Experience | Repository Fact | No |
| `ExperienceParticipation` | [`contracts.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts>) | Estado individual por Experience y miembro | Repository Fact | Solo pruebas de routing |
| `SignificantEvent` | [`contracts.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts>) | Evento candidato a evaluación | Repository Fact | Solo mock y pruebas |
| Reglas y efectos | [`routing.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/routing.ts>) | Evalúa un evento de manera independiente en distintas Experiences | Repository Fact | No se usa por la UI |
| Estado de capacidades | [`contracts.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/domain/contracts.ts>) | Declara capacidades como reales, simuladas, mock, propuestas o no soportadas | Repository Fact | Visible parcialmente como configuración |
| Actividad UI | [`mock-adapter.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/mock-adapter.ts>) | Mezcla hechos, texto, fecha formateada, puntos, tono e icono | Repository Fact | Sí |
| Experience Builder | [`products/experience-builder`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/experience-builder>) | Documentación y modelo preliminar del futuro constructor | Repository Fact | No es ejecutable |
| Framework de demo | [`canonical-demo-framework.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/docs/canonical-demo-framework.md>) | Principios de demos, escenarios, trazabilidad y múltiples Experiences | Repository Fact | No participa |

## 2.2 Stack tecnológico

- **Repository Fact:** React 19, ReactDOM, React Router 7, TypeScript 6 en modo estricto, Vite 8 y `vite-plugin-pwa`.
- **Repository Fact:** Vitest con `jsdom` para pruebas unitarias.
- **Repository Fact:** ESLint 10.
- **Repository Fact:** YAML para configuración y branding.
- **Repository Fact:** CSS y SVG propios; no existe una librería de componentes externa.
- **Repository Fact:** La versión declarada de Node es 24 o superior.
- **Repository Fact:** No existe backend, base de datos, gestión global de estado, SDK de API ni cliente HTTP especializado dentro del prototipo. Las dependencias están declaradas en [`package.json`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/package.json>).

## 2.3 Puntos de entrada y flujo real

```text
index.html
   ↓
src/main.tsx
   ↓
BrowserRouter
   ↓
App.tsx
   ↓
new MockDataAdapter()
   ↓
AppSnapshot
   ↓
pantallas React
```

- **Repository Fact:** Las rutas principales son `/`, `/benefits`, `/activity`, `/profile` y `/system`. Existe además `/showcase`, que presenta la app dentro de un marco tipo iPhone mediante un `iframe` apuntando a `/`.

- **Repository Fact:** La instancia del adaptador es un singleton creado en el módulo de la aplicación, no una dependencia resuelta a partir de configuración.

- **Architectural Inference:** Cambiar `dataMode` en el YAML no cambia realmente el origen de datos. El modo se declara, pero el runtime sigue acoplado al mock.

## 2.4 Acceso a la API de Convercus

- **Repository Fact:** No hay llamadas `fetch`, Axios, autenticación, lectura de secretos ni variables `VITE_*` que conecten la aplicación con una API.

- **Repository Fact:** El único mapa de API localizado pertenece a un baseline archivado y enumera login, cuenta, cupones, noticias, transacciones y niveles, además de Bearer token e `interaction-id`: [`archive/lovable-baseline/README.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/archive/lovable-baseline/README.md>).

- **Unresolved / Insufficient Evidence:** La documentación archivada no demuestra que dichos endpoints, esquemas o requisitos sigan vigentes. Tampoco demuestra la existencia de endpoints nativos para Experience definitions, participations, event evaluation o learning.

## 2.5 Datos, configuración y branding específicos

- **Repository Fact:** El miembro “Alex Martín”, puntos, nivel, cupones, noticias y actividad se encuentran codificados en [`mock-adapter.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/demo/mock-adapter.ts>).

- **Repository Fact:** La configuración general reside en [`app.yaml`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/config/app.yaml>).

- **Repository Fact:** La marca Convercus reside en [`brand.yaml`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/03-shared-assets/brands/convercus/brand.yaml>) y en los recursos gráficos adyacentes.

- **Repository Fact:** El campo `brand_source` de la configuración no resuelve dinámicamente la marca. [`brand.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/src/config/brand.ts>) importa estáticamente la marca Convercus y exige `brand_id === "convercus"`.

- **Repository Fact:** Título, colores y metadatos de marca se repiten entre YAML, CSS, `index.html` y la configuración PWA de [`vite.config.ts`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/prototype/vite.config.ts>).

## 2.6 Reutilización, duplicación y validación

- **Repository Fact:** Son reutilizables los tipos de dominio, `DataAdapter`, el validador de `DemoPackage`, `MockDataAdapter`, el evaluador puro de routing, el cargador de configuración y el mapeo de marca a CSS.

- **Repository Fact:** `Icon` y `FeedbackState` son componentes exportados. `SectionHeading`, `CouponCard` y `ActivityList` existen, pero permanecen internos a `App.tsx`.

- **Repository Fact:** Hay dos modelos desconectados:

  - `DemoPackage`, orientado a describir la demo;
  - `AppSnapshot`, orientado a alimentar la UI.

  La aplicación usa el segundo y las pruebas cubren principalmente el primero.

- **Repository Fact:** La comprobación auxiliar `isRecord` está duplicada en módulos de configuración.

- **Repository Fact:** El repositorio contiene cinco archivos de prueba y diez casos unitarios. Cubren configuración, branding, adaptador mock, paquete de demo y routing.

- **Repository Fact:** No existen pruebas renderizadas de `App`, E2E, visual regression, accesibilidad, contratos de API o validación automatizada del baseline TES.

- **Repository Fact:** No se observa CI propia del proyecto ni umbrales de cobertura obligatorios.

# 3. Bloom 2 — Semantic understanding

## 3.1 Qué es una Experience

- **TES / Semantic Contract Fact:** Una Experience es una unidad de transformación situada. Requiere un campo de mediación, al menos un evento significativo, un patrón emergente, una secuencia, una progresión, un resultado, medición, aprendizaje reutilizable y un arquetipo participante. Fuente principal: [`TES_Experience_Ledger.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/TES_Experience_Ledger.md>).

- **TES / Semantic Contract Fact:** El ecosistema es el campo donde ocurre la mediación; no es la secuencia ni el journey.

- **TES / Semantic Contract Fact:** Un evento es fuerte semánticamente cuando inaugura o altera de manera relevante la situación. No todo hecho observable constituye por sí mismo un evento significativo.

- **TES / Semantic Contract Fact:** El patrón es la regularidad que emerge de la relación entre eventos, no una propiedad aislada de uno de ellos.

- **TES / Semantic Contract Fact:** La secuencia hace reconstruible el tránsito entre eventos, estados, hitos o transiciones.

- **TES / Semantic Contract Fact:** La progresión exige un desplazamiento reconocible. No puede reducirse a acumulación, repetición o incremento de un contador. Esta distinción también está fijada por el [`TES_Lexico.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/TES_Lexico.md>).

- **TES / Semantic Contract Fact:** El resultado es el estado o efecto producido. Debe distinguirse de la intención, promesa comercial o incentivo.

- **TES / Semantic Contract Fact:** La medición reconstruye las consecuencias del resultado. El aprendizaje reutilizable cierra la cadena al extraer conocimiento de una experiencia reconstruida, medida y contrastada.

## 3.2 Secuencia, temporalidad y no linealidad

- **TES / Semantic Contract Fact:** Toda Experience requiere secuencia y progresión. Por tanto, una Experience completamente no secuencial no sería compatible con el contrato disponible.

- **TES / Semantic Contract Fact:** La ontología advierte que la cadena de acción situada —preferencia, propensión, intención, ordinalidad y ubicuidad— no debe interpretarse siempre como una cronología rígida. Esto se refiere a los componentes de reconstrucción de la acción situada, no elimina la exigencia de secuencia de una Experience. Véase [`TES_Ontologia_Accion_Situada.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/TES_Ontologia_Accion_Situada.md>).

- **Architectural Inference:** Una Experience podría admitir ramas, pasos opcionales o repetición si sigue existiendo un orden reconstruible entre estados y una progresión significativa.

- **Unresolved / Insufficient Evidence:** TES no proporciona en los artefactos revisados una semántica técnica suficiente para branching, bucles, N-de-M, eventos fuera de orden, ventanas temporales o resolución de concurrencia.

## 3.3 Completion y no-completion

- **TES / Semantic Contract Fact:** El léxico define “complete” como el cierre de una secuencia que alcanza el conjunto o estado previsto. También diferencia completar de acumular.

- **TES / Semantic Contract Fact:** La definición de Experience requiere un resultado, pero no establece que toda participación deba llegar necesariamente a un estado técnico `completed`.

- **Repository Fact:** La interpretación de producto contempla continuidad, abandono, reentrada y reactivación; también propone estados como `available`, `active`, `paused`, `completed`, `expired` o `abandoned`. Sin embargo, los presenta como cuestiones todavía abiertas en [`experience-understanding.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/product-interpretations/experience-understanding.md>).

- **Repository Fact:** El TypeScript actual solo declara `available`, `active`, `completed` y `closed`.

- **Architectural Inference:** Deben distinguirse al menos tres conceptos:

  - que la definición de Experience tenga una cadena semánticamente completa;
  - que una participación se encuentre activa, abandonada o cerrada;
  - que el participante haya alcanzado el resultado previsto.

  Usar un único booleano `completed` para los tres produciría ambigüedad.

## 3.4 Incentivos, recompensas y consecuencias

- **TES / Semantic Contract Fact:** Un incentivo intenta orientar una conducta, activación o progresión. Puede ser un beneficio, contenido, descuento o regla, pero no tiene que existir en todas las Experiences.

- **TES / Semantic Contract Fact:** Una recompensa se concede como consecuencia de una conducta, condición, regla o logro. No es sinónimo de incentivo.

- **TES / Semantic Contract Fact:** Los puntos pueden apoyar progresión, recompensa o redención, pero no equivalen automáticamente a progresión.

- **Repository Fact:** La interpretación de producto admite cero, uno o varios incentivos y establece que una recompensa puede aparecer al cumplirse un hito sin ser necesariamente el resultado final de la Experience.

- **Architectural Inference:** La arquitectura no debe colocar `reward` como cierre obligatorio de toda Experience ni inferir progreso únicamente porque se otorgaron puntos.

## 3.5 Reglas, eventos y transición

- **TES / Semantic Contract Fact:** El contrato semántico trasladado al repositorio establece la relación mínima:

```text
evento observable
   ↓ aporta evidencia
regla de avance
   ↓ autoriza
transición
   ↓ materializa
progresión
```

  La relación está documentada en [`01-guia-contrato-semantico.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/01-semantic-contract/source-excerpts/01-guia-contrato-semantico.md>).

- **TES / Semantic Contract Fact:** El evento por sí solo no produce progresión; debe ser interpretado dentro de una Experience mediante condiciones, estado y reglas.

- **Repository Fact:** `evaluateEventAcrossExperiences` ya refleja parcialmente esta separación: filtra reglas aplicables y evalúa el mismo evento independientemente para cada participación.

- **Architectural Inference:** El evaluador es una semilla correcta, pero no implementa todavía la semántica completa. No ordena reglas, mantiene historial, persiste transiciones, evalúa secuencias, detecta patrones, controla idempotencia ni produce resultados, mediciones o aprendizajes.

## 3.6 “Coverage”

- **Unresolved / Insufficient Evidence:** “Coverage” no aparece en los extractos revisados como entidad o propiedad central de una Experience. Sus apariciones están relacionadas con cobertura semántica, medición o inventario, no con un porcentaje universal de participación.

- **Repository Fact:** El código contiene una propiedad numérica `progression`.

- **Architectural Inference:** Presentar `progression: 75` como “75% de Experience cubierta” sería una decisión de producto, no una conclusión TES.

- **Recommendation:** Hasta obtener una definición oficial, cualquier indicador deberá nombrar la magnitud concreta: hitos alcanzados, estado actual, pasos válidos completados, evidencia observada o distancia hacia un resultado. No debería introducirse `coverage` como sinónimo de progresión.

# 4. Bloom 2B — Activity / Consumer Interaction Trace

## 4.1 Qué representa hoy “Activity”

- **Repository Fact:** `ActivityItem` combina en el mismo objeto:

  - identidad y momento del hecho;
  - descripción editorial;
  - fecha ya formateada;
  - puntos;
  - tono visual;
  - nombre del icono.

- **Architectural Inference:** El feed actual no es un ledger de dominio ni una fuente factual normalizada. Es una proyección preparada para la interfaz.

- **Repository Fact:** Cuando recibe un `SignificantEvent`, `MockDataAdapter.dispatch()` lo convierte inmediatamente en una fila de actividad y pierde parte de la semántica original, como `properties` y `reliability`.

- **Architectural Inference:** No debería utilizarse `ActivityItem` como registro canónico para evaluar Experiences. Su inclusión de `tone`, `displayDate` e `icon` la hace dependiente de la presentación.

## 4.2 Hipótesis de Consumer Interaction Trace

- **Architectural Inference:** Una Demo Factory necesita probablemente un registro neutral de interacciones observadas. “Consumer Interaction Trace” es un nombre arquitectónico provisional; no es un término TES establecido.

Podría representar hechos como:

```text
quién / qué identidad
qué interacción ocurrió
cuándo ocurrió y cuándo fue recibida
en qué canal o sistema
qué propiedades observables contenía
cuál es su procedencia
qué fiabilidad o estado de validación tiene
qué identificador permite deduplicarla
```

- **TES / Semantic Contract Fact:** Una interacción registrada no se convierte automáticamente en evento significativo ni en progresión.

- **Architectural Inference:** La significación debe ser contextual. Una reserva, compra o visita puede:

  - no afectar a ninguna Experience;
  - aportar evidencia a una;
  - aportar evidencias distintas a varias Experiences.

- **Repository Fact:** La documentación canónica de demo sostiene explícitamente que un evento compartido puede ser evaluado independientemente por varias participaciones y producir progreso, intervención, cambio de estado o ningún efecto: [`canonical-demo-framework.md`](</Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones/convercus-experience-products/products/convercus-app/docs/canonical-demo-framework.md>).

- **Unresolved / Insufficient Evidence:** TES no especifica por sí sola la cardinalidad de routing entre una interacción y múltiples Experiences. Esa capacidad procede por ahora de la interpretación de producto.

## 4.3 Flujo conceptual recomendado

```text
fuente real o simulada
        ↓
interacción observable normalizada
        ↓
registro factual / deduplicación
        ↓
evaluación contextual por Experience
        ↓
efectos autorizados
        ↓
estado de participación y resultados
        ↓
proyecciones: actividad, progreso, mensajes, dashboard
```

- **Recommendation:** Separar el registro factual de sus interpretaciones. Un solo hecho debe conservarse una vez y producir cero o más evaluaciones vinculadas mediante identificadores.

- **Recommendation:** La actividad visible debe construirse como proyección de:

  - interacciones observadas;
  - cambios de participación;
  - recompensas concedidas;
  - intervenciones;
  - resultados.

  Cada tipo debe mantener su procedencia, aunque la UI los presente juntos.

- **Unresolved / Insufficient Evidence:** Quedan sin definir las reglas de ordenación, ventanas temporales, correcciones, eliminación, privacidad, retención, eventos tardíos e idempotencia.

# 5. Bloom 3 — Sector application

Los siguientes casos son pruebas arquitectónicas, no definiciones TES ni afirmaciones sobre capacidades actuales de la API.

## 5.1 Aerolínea

| Dimensión | Aplicación de prueba |
|---|---|
| Interacciones | búsqueda de ruta, reserva, selección de asiento, check-in, embarque, compra auxiliar, incidencia, encuesta |
| Experiences candidatas | preparación fluida del viaje; continuidad del viajero frecuente; recuperación tras una incidencia |
| Presentación | tarjeta del próximo vuelo, hitos de preparación, mensajes contextuales y beneficios |
| Incentivos posibles | embarque prioritario, millas adicionales, lounge, contenido útil |
| Configuración sectorial | aeropuertos, rutas, cabinas, estados de reserva, ventanas previas al vuelo |
| ¿Requiere fork? | No debería. Requiere eventos, contenido, reglas, componentes sectoriales opcionales y adaptadores |

- **TES / Semantic Contract Fact:** “Comprar un vuelo” no sería por sí mismo una Experience. Solo puede ser evento dentro de una transformación reconstruible.

- **Architectural Inference:** La arquitectura actual podría tipar un evento de reserva, pero no puede operar la secuencia del viaje ni mostrar múltiples participaciones reales sin nuevo runtime.

## 5.2 Retail

| Dimensión | Aplicación de prueba |
|---|---|
| Interacciones | vista de producto, wishlist, compra, ticket, devolución, reparación, recomendación |
| Experiences candidatas | decisión para una ocasión; prolongación de vida del producto; relación de recomendación |
| Presentación | progreso contextual, recomendaciones, servicios posventa, historial |
| Incentivos posibles | acceso anticipado, reparación bonificada, recompensa por recomendación |
| Configuración sectorial | catálogo, tienda, categorías, canales, SKU, política de devolución |
| ¿Requiere fork? | No debería. Es el caso más próximo al mock actual |

- **Repository Fact:** El escenario “Circuito de decisión: ocasión” ya aparece como escenario canónico inicial en la documentación de demo.

- **Architectural Inference:** El modelo actual de cupones y noticias puede participar en la presentación, pero no constituye una Experience por sí mismo.

## 5.3 Movilidad

| Dimensión | Aplicación de prueba |
|---|---|
| Interacciones | consulta de ruta, desbloqueo, trayecto, cambio modal, suscripción, incidencia |
| Experiences candidatas | adopción de una rutina sostenible; descubrimiento de movilidad multimodal |
| Presentación | trayectos, hitos de hábito, ahorro estimado y sugerencias |
| Incentivos posibles | viajes gratuitos, mejora de plan, crédito o reconocimiento |
| Configuración sectorial | zonas, vehículos, operadores, emisiones y reglas tarifarias |
| ¿Requiere fork? | No debería, si las unidades y métricas son extensibles |

- **Architectural Inference:** Una sucesión de trayectos idénticos no demuestra automáticamente progresión. Sería necesario reconstruir un cambio de estado o patrón relevante.

## 5.4 Hospitality — cliente corporativo

| Dimensión | Aplicación de prueba |
|---|---|
| Interacciones | reserva, check-in, preferencia de habitación, restauración, Wi-Fi, checkout, nueva reserva |
| Experiences candidatas | estancia de negocios sin fricción; continuidad del viajero recurrente |
| Presentación | agenda de estancia, servicios útiles, preferencias y próximo paso |
| Incentivos posibles | desayuno, late checkout, espacio de trabajo, mejora de habitación |
| Configuración sectorial | hoteles, tarifas corporativas, estancias, servicios y fidelidad |
| ¿Requiere fork? | No debería |

## 5.5 Hospitality — resort

| Dimensión | Aplicación de prueba |
|---|---|
| Interacciones | reserva familiar, composición del grupo, actividades, spa, restauración, excursiones y feedback |
| Experiences candidatas | descubrimiento familiar del resort; itinerario de bienestar |
| Presentación | agenda diaria, participantes, disponibilidad, recomendaciones y recuerdos |
| Incentivos posibles | actividad incluida, experiencia sorpresa, beneficio familiar |
| Configuración sectorial | huéspedes múltiples, horarios, capacidad, edad, clima y localización |
| ¿Requiere fork? | No debería, pero somete el modelo a una tensión mayor |

- **Architectural Inference:** Este segundo escenario demuestra que `memberId + Experience` puede ser insuficiente. Algunas Experiences podrían pertenecer a una estancia, grupo, familia o reserva, con varios participantes y roles.

- **Architectural Inference:** Los cinco sectores pueden compartir un núcleo si los conceptos de interacción, Experience, participación, escenario y presentación son extensibles. Lo que debe variar son los paquetes, módulos y adaptadores, no el núcleo semántico.

# 6. Bloom 3B — Interaction-to-Experience evaluation

## 6.1 Una interacción puede afectar a varias Experiences

Ejemplo analítico de hospitality:

```text
Interacción: reserva de cena para cuatro huéspedes
         ├── Experience A: estancia familiar
         │       └── aporta evidencia a un hito de planificación
         ├── Experience B: descubrimiento gastronómico
         │       └── activa una intervención previa
         └── Experience C: bienestar
                 └── ningún efecto
```

- **Repository Fact:** El routing actual permite que reglas vinculadas a Experiences distintas evalúen el mismo evento.

- **TES / Semantic Contract Fact:** El hecho no basta para producir progresión. La regla debe determinar si aporta evidencia válida y autoriza una transición.

- **Architectural Inference:** La pertenencia no debe modelarse como una intersección estática de conjuntos. La evaluación puede depender de:

  - tipo y propiedades de la interacción;
  - estado de la participación;
  - orden previo de eventos;
  - condiciones de elegibilidad;
  - identidad o rol;
  - contexto de reserva, viaje o estancia;
  - resultado de reglas anteriores.

## 6.2 Evaluación actual frente a la necesaria

| Capacidad | Código actual | Soporte semántico/producto | Situación |
|---|---|---|---|
| Mismo evento, varias Experiences | Sí | Interpretación de producto | Parcialmente disponible |
| Evaluación independiente | Sí | Coherente con separación semántica | Disponible como función pura |
| Condiciones por evento | `accepts()` | Contrato trasladado | Parcial |
| Estado previo | No se pasa al evaluador, salvo participación básica | Interpretación de producto | Ausente |
| Orden o secuencia | No | TES lo exige | Ausente |
| Repeticiones o N-de-M | No | Provisional | Sin resolver |
| Ventanas temporales | No | Evidencia insuficiente | Sin resolver |
| Persistencia de efectos | No | Necesaria para operación | Ausente |
| Idempotencia | No | Necesidad arquitectónica | Ausente |
| Recompensas/intervenciones | Solo como categorías de efecto | Conceptualmente diferenciadas | No operativas |
| Resultado/medición/aprendizaje | No | TES los exige | Ausente |

- **Recommendation:** Mantener el evaluador independiente y determinista, pero no promoverlo todavía a “motor de Experiences”. Antes necesita un contrato explícito para contexto, historial, reglas, transición y efectos.

# 7. Bloom 4 — Architectural analysis

## 7.1 Capas de autoridad

| Capa | Debe ser autoridad sobre | No debe ser autoridad sobre | Situación actual |
|---|---|---|---|
| TES | Significado de Experience y conceptos semánticos | Detalles de React, API o layout | Correctamente documental |
| Interpretación de producto | Traducción provisional y preguntas abiertas | Redefinir TES | Existe, con algunos puntos aún ambiguos |
| Contrato funcional compartido | Entidades y relaciones aprobadas | Branding o contenido comercial | Solo candidato |
| Experience definition | Transformación, estados, secuencia, reglas y resultados | Fixtures o script de venta | Tipo TS preliminar |
| Scenario | Contexto, participantes, condiciones iniciales y selección de Experiences | Semántica universal | Solo documentado |
| DemoPackage | Composición desplegable para un prospecto | Redefinir conceptos TES | Existe como tipo, no como autoridad runtime |
| Runtime | Estado mutable y evaluación | Configuración maestra | Solo `AppSnapshot`/React state |
| Adapter | Integración con fuentes | Contenido y presentación | Mock mezcla actualmente varias capas |
| UI projection | Forma específica de presentación | Hechos o reglas de dominio | `ActivityItem` mezcla ambas |
| Branding | Tokens y activos visuales | Lógica sectorial o Experiences | Parcialmente separado |

## 7.2 Mapa de responsabilidades

| Pieza | Debe poseer | No debe poseer | Evidencia/riesgo actual |
|---|---|---|---|
| `DemoPackage` | IDs, versiones, referencias, prospecto, escenarios, módulos y modo | Estado mutable de usuarios | Hoy no se carga |
| `AppSnapshot` | Lectura preparada para la UI | Fuente canónica de hechos o reglas | Hoy es el centro real |
| `DataAdapter` | Frontera con datos/integraciones | Copy, iconos o layout | Su snapshot está acoplado al mock |
| `MockDataAdapter` | Comportamiento determinista simulado | Marca, narrativa o semántica TES | Contiene fixture y proyección |
| `ExperienceDefinition` | Definición reutilizable de transformación | Estado de una persona concreta | Es demasiado mínima para ejecutar |
| `ExperienceParticipation` | Estado de ejecución de una instancia | Definición global | Carece de contexto/grupo/historial |
| Interacción observable | Hecho normalizado y procedencia | Significación universal | Falta como entidad neutral |
| `SignificantEvent` | Interpretación contextual de un hecho | Campos de UI | El nombre presupone significación antes de evaluar |
| Reglas | Evidencia requerida y transición permitida | Renderizado | Son callbacks TS, difíciles de serializar |
| Efectos | Resultado declarado de una evaluación | Mutación implícita | No se aplican |
| Capabilities | Veracidad y procedencia por función | Promesa comercial vaga | Buen comienzo, desconectado |
| Scenario | Situación demostrable y estado inicial | Definición TES | Documental |
| Demo Script | Orden narrativo para el presentador | Lógica real de Experience | Falta como modelo |
| Branding | Tokens, logos, tipografía, manifest | Datos del miembro | Importación fija a Convercus |
| App config | Shell, módulos, navegación | Datos ficticios | Actualmente repite branding |
| Fixtures | Personas, interacciones e historial simulado | Componentes de UI | Están dentro del adaptador |
| Routing | Encontrar evaluaciones aplicables | Persistencia y rendering | Correcto pero muy limitado |
| UI modules | Presentar capacidades | Inferir verdad de negocio | Concentrados en `App.tsx` |
| TES baseline | Semántica/versiones | Configuración del prospecto | No hay verificación automática |

## 7.3 Scenario, Experience y Demo Script

- **TES / Semantic Contract Fact:** Experience es la unidad de transformación situada reconstruible.

- **Architectural Inference:** Scenario es el contexto ejecutable de una demostración: personas, situación inicial, datos, Experiences activas, canal y condiciones.

- **Architectural Inference:** Demo Script es la dramaturgia comercial: acciones que el presentador realiza, orden recomendado, mensajes a explicar, estados a preparar y puntos de recuperación.

Ejemplo:

```text
Experience:
  "Estancia de negocios sin fricción"

Scenario:
  "Laura llega esta tarde a Lisboa, tiene una reunión a las 09:00
   y todavía no ha indicado hora de llegada"

Demo Script:
  1. Abrir perfil de Laura
  2. Mostrar señal de llegada pendiente
  3. Simular confirmación del vuelo
  4. Mostrar intervención y cambio de estado
```

- **Recommendation:** No introducir acciones del presentador dentro de `ExperienceDefinition`. Tampoco convertir el escenario en una Experience distinta para cada prospecto si la transformación subyacente es reutilizable.

## 7.4 `DemoPackage` frente a `AppSnapshot`

- **Repository Fact:** `DemoPackage` incluye metadatos, baseline TES, capacidades y Experiences.

- **Repository Fact:** `AppSnapshot` incluye únicamente lo que necesita la interfaz actual: miembro, cupones, noticias y actividad.

- **Architectural Inference:** Son objetos de capas diferentes:

  - `DemoPackage`: configuración inmutable o versionada de una demo;
  - estado runtime: participaciones, interacciones, resultados y estado del script;
  - read model: proyección derivada para la UI.

- **Architectural Inference:** El nombre `AppSnapshot` puede seguir siendo útil como read model, pero no debería ser simultáneamente la respuesta cruda del backend, el estado canónico y la presentación.

## 7.5 Obstáculos para múltiples demos

Los obstáculos más relevantes son:

1. **Repository Fact:** Marca fijada estáticamente a Convercus.
2. **Repository Fact:** Fixtures y copy embebidos en el adaptador y `App.tsx`.
3. **Repository Fact:** `DemoPackage` no controla el arranque.
4. **Repository Fact:** El modo de datos es declarativo, no operativo.
5. **Repository Fact:** No existe catálogo ni resolución de demos.
6. **Repository Fact:** No existe estado runtime explícito de Experience.
7. **Repository Fact:** Las reglas son funciones TypeScript; no son configurables ni serializables.
8. **Repository Fact:** Escenario, fixture y script carecen de contrato ejecutable.
9. **Repository Fact:** El activity feed mezcla dominio y presentación.
10. **Repository Fact:** PWA, manifest, título y caché asumen una sola aplicación/marca.
11. **Architectural Inference:** Un despliegue multicliente podría filtrar activos o contenido entre prospectos si el aislamiento de paquete y caché no se diseña.
12. **Unresolved / Insufficient Evidence:** La API real podría obligar a adaptar esta frontera cuando se conozcan sus contratos.

# 8. Bloom 5 — Alternative evaluation

## Alternativa A — Una compilación autocontenida por demo

Cada prospecto se compila con un paquete, marca y conjunto de fixtures concretos.

| Criterio | Evaluación |
|---|---|
| Aislamiento | Alto |
| Simplicidad de despliegue | Alta por demo, menor al gestionar muchas |
| Riesgo de filtración | Bajo |
| Cambio de prospecto en caliente | No |
| Escalabilidad organizativa | Media |
| Compatibilidad PWA | Alta |
| Uso sin conexión | Alto |
| Complejidad inicial | Baja-media |
| Riesgo principal | Deriva entre builds y multiplicación de pipelines |

- **Architectural Inference:** Encaja bien con demostraciones comerciales sensibles y despliegues independientes.
- **Architectural Inference:** No exige forks si todas las compilaciones utilizan el mismo núcleo y paquetes declarativos.

## Alternativa B — Registro runtime de paquetes seleccionados por `demoId`

Una única aplicación resuelve al arrancar qué paquete, marca, escenario y adaptadores debe cargar.

| Criterio | Evaluación |
|---|---|
| Aislamiento | Medio; requiere disciplina fuerte |
| Simplicidad de despliegue | Alta para muchas demos |
| Cambio de prospecto | Alto |
| Velocidad de creación | Alta |
| Compatibilidad PWA | Media; hay que aislar caché |
| Uso sin conexión | Posible precargando el paquete |
| Complejidad inicial | Media |
| Riesgo principal | Carga accidental de contenido de otro prospecto |

- **Recommendation:** Es la alternativa preferente para la Demo Factory v0.1, siempre que el paquete resuelto sea explícito, validado y aislado.

- **Architectural Inference:** Puede conservar una modalidad de exportación/build autocontenido para demos sensibles, combinando ventajas de A y B sin crear otra arquitectura.

## Alternativa C — Orquestación remota y cliente delgado

Un servicio remoto selecciona paquetes, mantiene estado y evalúa Experiences; la PWA presenta read models.

| Criterio | Evaluación |
|---|---|
| Fidelidad a datos reales | Alta |
| Integración enterprise | Alta |
| Uso sin conexión | Bajo |
| Complejidad operativa | Alta |
| Tiempo hasta Demo Factory útil | Alto |
| Observabilidad central | Alta |
| Riesgo principal | Diseñar un backend antes de conocer la API real |

- **Architectural Inference:** Puede ser apropiada en una fase posterior, pero hoy introduciría decisiones prematuras sobre persistencia, seguridad y contratos de API.

## 8.1 Principios de trabajo

| Principio | Clasificación | Motivo |
|---|---|---|
| TES sigue siendo autoridad semántica | **Preserve as-is** | Ya está claramente separado |
| Interpretaciones de producto subordinadas a TES | **Preserve as-is** | Evita redefiniciones accidentales |
| Evaluar un evento independientemente por Experience | **Preserve but formalize** | Buen principio, implementación incompleta |
| Un `DataAdapter` como frontera de datos | **Preserve but formalize** | Útil, pero su contrato actual está demasiado ligado al snapshot |
| `DemoPackage` como descripción de una demo | **Preserve but formalize** | Debe convertirse en autoridad runtime |
| Branding externo en YAML | **Preserve but formalize** | La intención es buena, la resolución sigue estática |
| Capability status real/simulated/mocked/etc. | **Preserve but formalize** | Necesita procedencia y validación visible |
| `AppSnapshot` como único objeto de datos | **Replace** | Mezcla estado/read model y excluye Experiences |
| `ActivityItem` como registro de eventos | **Replace** | Es una proyección visual |
| Singleton `new MockDataAdapter()` en `App.tsx` | **Replace** | Impide selección de demo y adaptador |
| Reglas como callbacks dentro de configuración | **Clarify before deciding** | Son útiles en código, pero no serializables ni gobernables |
| `progression: number` universal | **Clarify before deciding** | TES no define una escala universal |
| Estado de participación actual | **Clarify before deciding** | Ciclo de vida insuficientemente resuelto |
| Experiencias ramificadas/N-de-M | **Clarify before deciding** | La interpretación lo admite provisionalmente; TES técnico no lo fija |

# 9. Bloom 6 — Demo Factory Architecture v0.1

Esta sección es una hipótesis arquitectónica, no una especificación de implementación.

## 9.1 Vista general

```text
┌─────────────────────────────────────────────────────┐
│ Autoridad TES                                       │
│ baseline + léxico + ontología + Experience Ledger   │
└─────────────────────────┬───────────────────────────┘
                          ↓ trazabilidad
┌─────────────────────────────────────────────────────┐
│ Contratos funcionales versionados                   │
│ Experience, participation, interaction, effects     │
└─────────────────────────┬───────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│ Catálogos reutilizables                             │
│ Experience definitions · UI modules · adapters      │
└─────────────────────────┬───────────────────────────┘
                          ↓ referencias
┌─────────────────────────────────────────────────────┐
│ DemoPackage por prospecto                           │
│ brand · scenarios · fixtures · capabilities         │
│ content · adapter policy · demo scripts             │
└─────────────────────────┬───────────────────────────┘
                          ↓ bootstrap
┌─────────────────────────────────────────────────────┐
│ Demo Runtime                                        │
│ interaction trace · participations · evaluator      │
│ interventions · results · deterministic reset       │
└─────────────────────────┬───────────────────────────┘
                          ↓ selectors
┌─────────────────────────────────────────────────────┐
│ Read models / UI projections                        │
│ Home · Benefits · Activity · Profile · System       │
│ más módulos sectoriales opcionales                  │
└─────────────────────────────────────────────────────┘
```

## 9.2 Autoridad y composición

- **Recommendation:** TES debe conservarse como referencia semántica versionada, no convertirse en configuración runtime.

- **Recommendation:** Los contratos funcionales deben traducir TES con trazabilidad explícita y marcar qué conceptos son:

  - normativos;
  - interpretación de producto;
  - extensión técnica;
  - incógnita pendiente.

- **Recommendation:** `DemoPackage` debe convertirse en la raíz de composición inmutable de cada demo.

Un paquete debería poder identificar, sin contener necesariamente todos los objetos embebidos:

- versión del esquema;
- identidad y namespace del prospecto;
- marca;
- locale;
- baseline semántico;
- escenarios incluidos;
- Experience definitions referenciadas;
- fixtures e interacciones iniciales;
- capacidades y procedencia;
- política de datos/adaptadores;
- módulos y navegación;
- contenido;
- scripts comerciales;
- políticas de reset y semilla determinista.

- **Recommendation:** El paquete debe referenciar contratos y Experiences reutilizables por ID y versión. No debería copiar definiciones semánticas distintas para cada prospecto.

## 9.3 Estado runtime

- **Recommendation:** Separar tres formas de estado:

  1. **Configuración:** paquete y escenario seleccionados.
  2. **Estado canónico de ejecución:** interacciones, participaciones, transiciones, intervenciones, recompensas y resultados.
  3. **Read models:** datos ya preparados para cada pantalla.

- **Architectural Inference:** El actual `AppSnapshot` puede evolucionar hacia la tercera categoría sin ser eliminado necesariamente.

- **Recommendation:** El reset debe reconstruir de forma determinista el escenario inicial a partir del paquete y una semilla o fixture conocido. Esto es esencial para una demo comercial repetible.

## 9.4 Adaptadores y realidad

- **Recommendation:** Resolver adaptadores durante el bootstrap, no dentro de `App.tsx`.

- **Recommendation:** La veracidad debe expresarse por capacidad y procedencia, no únicamente mediante un `dataMode` global. Una demo puede legítimamente combinar:

  - perfil real;
  - beneficios reales;
  - interacciones simuladas;
  - evaluación propuesta;
  - resultados mock.

- **Recommendation:** Toda capacidad visible debería poder informar si es `real`, `simulated`, `mocked`, `proposed` o `unsupported`, junto con la fuente o adaptador responsable.

- **Unresolved / Insufficient Evidence:** No debe diseñarse todavía un adaptador de producción definitivo hasta verificar la API real.

## 9.5 Experiences y evaluación

- **Recommendation:** Mantener `ExperienceDefinition` separada de `ExperienceParticipation`.

- **Recommendation:** El evaluador debe recibir explícitamente:

  - la interacción o evidencia;
  - definición y versión de Experience;
  - participación;
  - contexto relevante;
  - historial necesario;
  - reglas;
  - reloj o tiempo de evaluación.

- **Recommendation:** Su salida debe declarar efectos, no realizar mutaciones opacas. La aplicación de efectos puede entonces persistirse, auditarse y proyectarse.

- **Recommendation:** Cada evaluación debe conservar trazabilidad desde la interacción hasta la regla, transición, progresión y resultado afectados.

## 9.6 Scenarios y scripts

- **Recommendation:** `Scenario` debería ligar un contexto sectorial con:

  - actores o participantes;
  - estado inicial;
  - Experiences activas;
  - fixtures;
  - interacciones programables;
  - contenido;
  - excepciones demostrables.

- **Recommendation:** `DemoScript` debería ser opcional y separado, con pasos del presentador, mensajes y acciones de recuperación.

- **Architectural Inference:** Esta separación permite reutilizar la misma Experience en distintos prospectos y demostrarla de maneras diferentes.

## 9.7 UI y branding

- **Recommendation:** La navegación debe componerse desde módulos permitidos por el paquete, manteniendo un shell estable.

- **Recommendation:** Los módulos existentes pueden seguir funcionando mientras se extraen gradualmente sus dependencias de copy, branding y fixtures.

- **Recommendation:** El branding debe resolverse por ID o referencia durante el arranque. Debe gobernar CSS tokens, logos, tipografía, título, manifest e iconos PWA.

- **Recommendation:** En despliegues multi-demo, la caché de service worker y los activos deben estar namespaced por demo o deployment para impedir contaminación cruzada.

## 9.8 Invariantes del núcleo

1. **Recommendation:** Ningún evento produce progreso sin evaluación de una regla.
2. **Recommendation:** El registro factual no contiene decisiones visuales.
3. **Recommendation:** Una UI projection no se convierte en fuente canónica.
4. **Recommendation:** Una Experience definition no contiene datos específicos de un prospecto salvo que formen parte real de su definición versionada.
5. **Recommendation:** Un escenario no redefine TES.
6. **Recommendation:** Un script comercial no modifica silenciosamente reglas de negocio.
7. **Recommendation:** Cada capacidad muestra su nivel de realidad.
8. **Recommendation:** Dos demos pueden coexistir sin compartir estado, caché, fixtures o branding.
9. **Recommendation:** Reset reproduce el mismo estado inicial.
10. **Recommendation:** Toda desviación del contrato semántico queda declarada y trazada.

# 10. Minimum transition path

Este camino evita una gran refactorización inicial.

1. **Resolver las preguntas semánticas bloqueantes.**  
   Confirmar participación, ciclo de vida, topologías de secuencia, interacción observable y significado de progresión.

2. **Ratificar un contrato mínimo de `DemoPackage`.**  
   Establecer identidad, versión, brand, scenario, capabilities, fixtures, modules y adapter policy. El validador actual puede servir como punto de partida, pero necesita validación estructural completa.

3. **Crear una segunda configuración real de prospecto como prueba arquitectónica.**  
   No hace falta otra aplicación. Debe demostrar que marca, contenido, fixtures y escenario pueden variar sin editar el núcleo.

4. **Introducir un bootstrap/resolver de demo.**  
   Sustituir la construcción directa de `MockDataAdapter` por resolución desde el paquete seleccionado.

5. **Extraer los fixtures del adaptador.**  
   `MockDataAdapter` debería simular comportamiento sobre fixtures recibidos, no ser propietario de Alex Martín ni del relato comercial.

6. **Separar interacción factual y actividad visual.**  
   Mantener temporalmente el feed, pero derivarlo desde registros neutros o efectos runtime.

7. **Conectar una participación mínima al runtime.**  
   Utilizar una única Experience sencilla y trazable antes de generalizar el motor.

8. **Añadir validaciones de fábrica.**  
   Como mínimo:

   - cargar dos paquetes;
   - validar referencias;
   - comprobar activos;
   - garantizar IDs aislados;
   - hacer smoke render;
   - ejecutar reset determinista;
   - verificar que ninguna capacidad declarada como real usa mock.

9. **Verificar la API antes de A5/realidad.**  
   Contrastar autenticación, endpoints, esquemas, CORS/proxy, sandbox, rate limits y disponibilidad de datos de Experience.

- **Recommendation:** La primera prueba de éxito no debería ser “tenemos carpetas para varias demos”, sino: “la misma compilación o núcleo arranca dos prospectos distintos sin cambiar código de aplicación y sin filtrar datos entre ellos”.

# 11. Explicit non-goals

En esta fase no se propone:

- reescribir la aplicación;
- introducir un backend nuevo;
- construir todavía el Experience Builder;
- convertir toda la UI en una librería de componentes;
- implementar un motor general de workflows;
- inventar endpoints de Experience;
- asumir que el API archivado sigue vigente;
- definir branching o N-de-M sin confirmación semántica;
- equiparar puntos, progreso, completion y coverage;
- mover TES al código como si fuera configuración;
- diseñar multi-tenancy productivo;
- implementar autenticación enterprise;
- resolver analytics, privacidad o retención completas;
- sustituir todos los mocks de una sola vez;
- crear forks específicos para aerolínea, retail, movilidad u hospitality.

# 12. Open TES / semantic questions

Las cinco primeras son bloqueantes para la arquitectura.

1. **Unresolved / Insufficient Evidence:** ¿Cuál es la entidad oficial para la participación concreta de una persona, grupo, estancia o cuenta en una Experience?

2. **Unresolved / Insufficient Evidence:** ¿Qué estados y transiciones de ciclo de vida están permitidos y cuáles representan ejecución, resultado o cierre administrativo?

3. **Unresolved / Insufficient Evidence:** ¿Admite una secuencia ramas, repetición, pasos opcionales, N-de-M y reentrada? ¿Con qué invariantes conserva ordinalidad?

4. **Unresolved / Insufficient Evidence:** ¿Debe registrarse primero una interacción neutral y calificarse después como evento significativo, o `SignificantEvent` es ya la entrada oficial?

5. **Unresolved / Insufficient Evidence:** ¿Cómo debe representar el producto la progresión: estado nominal, hitos, relación parcial, porcentaje u otra estructura?

6. ¿Existe un concepto TES de “coverage” aplicable a Experience?

7. ¿Cuándo una repetición constituye patrón y cuándo es mera acumulación?

8. ¿Qué relación formal existe entre resultado individual de participación y resultado agregado de Experience?

9. ¿Puede una Experience no alcanzar su resultado y aun producir medición y aprendizaje?

10. ¿La Experience pertenece siempre a un individuo o puede tener sujeto colectivo?

11. ¿Cómo se representa la fiabilidad o contradicción entre evidencias?

12. ¿Qué condiciones convierten un incentivo en intervención?

13. ¿Una recompensa puede participar en la progresión sin ser resultado?

14. ¿Cómo se interpretan eventos tardíos o correcciones de eventos previos?

15. ¿Workflow es únicamente mecanismo técnico o puede ser parte formal del contrato de Experience?

# 13. Candidate ADRs

No se crean ADRs todavía; estos son candidatos.

1. **Autoridad de composición de una demo**  
   Decidir que `DemoPackage` sea la raíz de composición runtime.

2. **Resolución y despliegue de paquetes**  
   Elegir entre build autocontenido, registro runtime o modalidad híbrida.

3. **Trazabilidad del baseline semántico**  
   Definir cómo contratos y paquetes referencian versiones TES.

4. **Separación Interaction Trace / Activity Feed**  
   Establecer el registro factual y sus proyecciones.

5. **Separación Scenario / Experience / Demo Script**  
   Evitar que contexto, transformación y narrativa comercial se mezclen.

6. **Política de adaptadores y capacidades mixtas**  
   Resolver qué significa real, simulated, mocked, proposed y unsupported por función.

7. **Estado runtime y reset determinista**  
   Determinar autoridad, persistencia y reproducción de escenarios.

8. **Estrategia de marca y activos**  
   Resolver carga, validación, manifest PWA, fuentes y fallback.

9. **Aislamiento entre prospectos**  
   Definir namespace de IDs, almacenamiento, caché y recursos.

10. **Representación de reglas**  
    Decidir qué reglas son datos, código versionado o responsabilidad de un servicio externo.

11. **Contrato de participación**  
    Resolver individuo, grupo, reserva, estancia y actores múltiples.

12. **Frontera de la API Convercus**  
    Documentar capacidades reales verificadas antes de diseñar el adaptador productivo.

# 14. Final hospitality stress test

Se somete la arquitectura v0.1 a dos demos para la misma cadena hotelera.

## Demo A — Viajero corporativo

- Marca: misma cadena, tono ejecutivo.
- Persona: huésped individual.
- Experience: estancia de negocios sin fricción.
- Datos: reserva, llegada, preferencias y servicios.
- Interacciones: confirmación de vuelo, check-in, Wi-Fi y checkout.
- Resultado candidato: reducción reconstruible de fricciones durante la estancia.
- Demo script: mostrar cómo una señal de llegada modifica la intervención.

## Demo B — Resort familiar

- Marca: misma cadena, submarca y tono vacacional.
- Participantes: adultos, menores y reserva compartida.
- Experiences: descubrimiento familiar y planificación de actividades.
- Datos: disponibilidad, edades, clima, horarios y preferencias.
- Interacciones: reservas de actividades, restauración, cancelaciones y feedback.
- Resultado candidato: itinerario familiar adaptado y efectivamente realizado.
- Demo script: mostrar cómo una reserva de actividad afecta de manera distinta a dos Experiences.

## Resultado de la prueba

- **Architectural Inference:** Brand, Scenario, Experience y Demo Script deben ser independientes. La misma marca puede producir demos muy distintas sin duplicar el núcleo.

- **Architectural Inference:** `ExperienceParticipation(memberId, experienceId)` no cubre bien el resort familiar. Hace falta admitir un contexto o sujeto operacional más amplio: grupo, stay, booking o account.

- **Architectural Inference:** Una interacción puede referirse simultáneamente a una reserva, varios huéspedes y una Experience individual o colectiva. El modelo necesita correlación y roles, no solo `memberId`.

- **Architectural Inference:** El adaptador no debería devolver directamente un único `member`. Debe poder suministrar sujetos, relaciones y contextos, o un read model que los represente.

- **Architectural Inference:** La arquitectura propuesta supera la prueba solo si `Participation` y `Interaction` permanecen extensibles.

## Revisión resultante de la hipótesis v0.1

- **Recommendation:** Añadir al contrato pendiente un concepto neutral de `subject/context reference`, sin fijar todavía su implementación.

- **Recommendation:** Permitir que un escenario declare participantes y roles, no solo un miembro principal.

- **Recommendation:** Mantener Experience, escenario y prospecto con namespaces independientes.

- **Recommendation:** No introducir `memberId` como clave universal del núcleo.

Con estas correcciones, no resulta necesario un fork de hospitality. El caso requiere extensiones de configuración, adaptadores y módulos, pero no una arquitectura diferente.

# 15. Confidence and evidence gaps

## Confianza alta

- **Repository Fact:** Estructura, stack, entry points, rutas, uso del mock y ausencia de API ejecutable.
- **Repository Fact:** Localización de configuración, branding, fixtures y lógica fija.
- **Repository Fact:** Cobertura de pruebas y ausencia de E2E/CI.
- **TES / Semantic Contract Fact:** Cadena evento–patrón–secuencia–progresión–resultado–medición–aprendizaje.
- **TES / Semantic Contract Fact:** Distinciones entre ecosistema, secuencia, progresión, incentivo, recompensa, puntos y resultado.

## Confianza media

- **Architectural Inference:** Separar interacción observable de evento significativo.
- **Architectural Inference:** Evaluación del mismo hecho por múltiples Experiences.
- **Architectural Inference:** `DemoPackage` como autoridad de composición.
- **Architectural Inference:** Escenarios no lineales compatibles si preservan orden y progresión reconstruibles.
- **Architectural Inference:** Soporte de capacidades reales y simuladas dentro de una misma demo.

Estas conclusiones son coherentes con los documentos de producto, pero no todas son mandatos TES.

## Confianza baja o insuficiente

- **Unresolved / Insufficient Evidence:** API vigente de Convercus.
- **Unresolved / Insufficient Evidence:** Existencia de API nativa para Experiences.
- **Unresolved / Insufficient Evidence:** Ciclo de vida oficial de participación.
- **Unresolved / Insufficient Evidence:** Branching, repetición, N-de-M y ventanas temporales.
- **Unresolved / Insufficient Evidence:** Significado de “coverage”.
- **Unresolved / Insufficient Evidence:** Persistencia, consistencia e idempotencia requeridas.
- **Unresolved / Insufficient Evidence:** Sujeto colectivo y múltiples participantes.
- **Unresolved / Insufficient Evidence:** Estrategia productiva de seguridad, consentimiento, privacidad y retención.

La conclusión operativa es que el repositorio posee una buena base conceptual, pero todavía es una demo única con arquitectura preparatoria. El siguiente diseño debería concentrarse primero en hacer que `DemoPackage` gobierne una segunda demo real desde el mismo núcleo y en cerrar las cinco preguntas semánticas bloqueantes. No se ha modificado ningún archivo.

---
---
# TRAS LA CONSULTA A TES
# Product Interpretation — Observed Occurrence, Trace, TES Event and Activity Projection

## Status

Product-level interpretation derived from the current TES corpus.

This document does not modify, extend or supersede TES.

Its purpose is to make explicit within Convercus Demo Factory a semantic distinction that TES already contains and that the product architecture must materialize correctly.

---

## 1. Governing principle

Convercus Demo Factory must **adapt the product layer** to the distinction already contained in TES between:

* observable occurrence or fact;
* trace/evidence that allows the occurrence to be reconstructed or confirmed;
* significant event recognized within a specific Experience.

No new TES entity is introduced by this interpretation.

TES remains the semantic authority.

---

## 2. TES distinction

TES establishes that not every observable fact constitutes an event in the strong experiential sense.

An occurrence becomes relevant as a TES Event when it produces a meaningful difference within the dynamics of a particular Experience.

Therefore:

**observable occurrence ≠ TES Event**

and the significance of an occurrence should not be treated by the product as an intrinsic, universal attribute of the occurrence itself.

The product should preserve the possibility that significance is contextual and relational to an Experience.

---

## 3. Product-level occurrence

Demo Factory may need to persist observable facts independently of their later interpretation by an Experience.

For product purposes, the provisional term:

**Observed Occurrence**

may be used for such a fact.

This is a product/technical term, not a new TES concept.

An Observed Occurrence may require technical properties such as:

* identifier;
* occurrence time;
* reception time;
* source;
* actor or subject reference;
* contextual references;
* payload or observable properties;
* provenance;
* reliability or validation metadata;
* deduplication information.

These properties belong to instrumentation and implementation, not to the TES ontology.

---

## 4. Trace

The term **Trace** should remain aligned with its TES methodological use.

A Trace is evidence that allows an action, condition or transition to be reconstructed or confirmed as having occurred.

Therefore:

**occurrence ≠ trace ≠ TES Event**

A persisted occurrence may produce or contain a trace, but the trace does not itself replace experiential interpretation.

---

## 5. Recognition within an Experience

The product must not assume:

`ObservedOccurrence.significant = true`

as an absolute property.

Instead, significance should remain conceptually dependent on the relationship between an occurrence, an Experience and its relevant context.

A single observed occurrence may, where semantically valid:

* be irrelevant to all active Experiences;
* be relevant to one Experience;
* be relevant in different ways to several Experiences.

This many-to-many possibility is a product interpretation strongly compatible with TES, not an explicit TES cardinality rule.

---

## 6. Preserve the TES experiential chain

Instrumentation must not replace or extend the TES Experience Ledger.

The TES experiential plane remains:

**Event → Pattern → Sequence → Progression → Result → Measurement → Learning**

Observed occurrences and traces belong to a different product/instrumentation plane that can provide evidence to the experiential plane.

Conceptually:

### Instrumentation / reconstruction plane

**Observed Occurrence → Trace → contextual recognition / confirmation**

### Experiential TES plane

**Event → Pattern → Sequence → Progression → Result → Measurement → Learning**

The first plane feeds the second.

It must not be inserted into the Experience Ledger as though all elements belonged to the same ontological level.

---

## 7. Pattern

A collection or “trace” of consumer occurrences must not be equated with a TES Pattern.

TES Pattern refers to the recognizable regularity that emerges from relationships between Events.

Therefore:

* an occurrence is not a Pattern;
* a collection of occurrences is not automatically a Pattern;
* repeated occurrences are not automatically Progression;
* Pattern recognition requires the relations and experiential context established by TES.

---

## 8. Activity

`Activity` must not be treated as a sovereign semantic entity or source of truth.

The current Activity representation may remain useful as a product/read-model concept.

An Activity view may combine, for presentation purposes:

* observed occurrences;
* TES Event interpretations;
* participation changes;
* interventions;
* rewards or incentives;
* results;
* editorial copy;
* visual presentation.

However:

**Activity View ≠ canonical factual record**

and:

**Activity View ≠ TES Event**

The canonical factual and experiential layers must remain independently reconstructible.

---

## 9. Coverage — analytical hypothesis

`Coverage` is retained only as a **candidate analytical construct**, inspired by set-covering theory.

It is not a TES concept and must not be used as a synonym for:

* Progression;
* Completion;
* Result;
* reconstruction quality;
* Experience state.

One possible analytical formulation is:

Let:

`U = set of observed occurrences within a defined scenario/window`

and let:

`S_E ⊆ U`

represent the subset of those occurrences that are recognized as relevant evidence/events in relation to Experience `E`.

For a family of Experiences `𝓔`, the union:

`⋃ S_E`

may be used analytically to investigate how the observed behavioural field is related to the Experience portfolio.

This does **not** imply that the proportion of occurrences covered measures Experience Progression.

A second possible notion —how much of the evidence or structure required by one Experience is currently satisfied— is a different analytical problem and must not be conflated with occurrence-set coverage.

Because TES requires Pattern, Sequence and Progression, simple set intersection or percentage coverage cannot, by itself, establish experiential Progression.

The usefulness and limits of this analytical construct remain subject to architectural falsification.

---

## 10. Product invariants

The following product rules should be treated as candidate invariants:

1. An observable occurrence does not automatically constitute a TES Event.
2. Trace/evidence does not replace experiential interpretation.
3. Significance must not be stored as an unconditional universal property of an occurrence.
4. An occurrence may potentially be evaluated in relation to zero, one or multiple Experiences.
5. The original factual record must remain independent of subsequent interpretations.
6. Activity and other UI projections must not become canonical sources of factual or TES meaning.
7. Pattern must not be reduced to a collection of occurrences.
8. Progression must not be inferred from accumulation alone.
9. Coverage, if used, remains an analytical/product construct and never a synonym for TES Progression.
10. TES remains authoritative for Event → Pattern → Sequence → Progression → Result → Measurement → Learning.

---

## 11. Reopening condition

TES should not be reopened because of this product need.

The semantic corpus should only be reconsidered if a concrete product or real-world case appears that cannot be coherently represented through the existing distinction:

**observable occurrence / trace → contextual recognition as TES Event**

and therefore provides evidence of a genuine semantic anomaly rather than a product-instrumentation requirement.
