# Consolidación Git de Convercus App — 2026-10-17

Se consolida el trabajo recibido desde `66b2465`, incluidos el contrato semántico,
las decisiones de arquitectura, las sesiones experimentales, Sports Season y Self
Service. Se conserva la evidencia histórica y sus fixtures sin modificar las
expectativas de las pruebas para hacerlas pasar.

## Verificación ejecutada

Desde `prototype/`, con Node 24.18.0 y las dependencias locales instaladas:

| Comando | Resultado |
| --- | --- |
| `npm run typecheck` | PASS |
| `npm run lint` | PASS |
| `npx vitest run src/demo-factory/sports-season/self-service.test.ts src/demo-factory/sports-season/self-service-ui.test.tsx src/demo-factory/sports-season/runtime.test.ts src/demo-factory/sports-season/user-plane.test.ts` | 63 PASS, 0 FAIL |
| `npm test` | 159 PASS, 22 FAIL, 181 pruebas |
| `npm run build` | PASS, incluida PWA |

La suite completa **no está verde** y `npm run check` tampoco lo estará.
Los 21 fallos registrados en `evidence/build-02-self-service/suite-comparison.json`
siguen presentes. Esta ejecución descubre además el fallo del caso de Sesión 40
que llama a `executeAction` sin seleccionar previamente una persona; el runtime
lo rechaza con «Selecciona una persona antes de participar». Es un resultado de
la versión recibida, anterior a cualquier modificación de producto por esta
consolidación. El informe anterior contiene 179 pruebas; esta ejecución contiene
181. No se actualizan retrospectivamente informes ni resultados históricos.

Esta consolidación guarda una versión del trabajo; no certifica una entrega con
la suite completa aprobada. La conciliación de las pruebas antiguas con el
contrato vigente queda como tarea técnica explícita. No se repite una validación
visual de navegador porque no se modifica el producto.

## Archivos incluidos y copias locales

Se incluyen los fuentes, documentación, evidencias y el dataset original
`sports_season_loyalty_dataset_v0_1.json` de la raíz del repositorio. Se mantienen
los dos `pre-build-sources.tar.gz` como evidencia referenciada de sus builds.
Los ZIP `00-governance.zip`, `products/convercus-app.zip` y
`products/convercus-app/docs.zip` permanecen en disco, excluidos de Git.

## Casos fallidos de la suite completa

- BUILD 01 actual App: choices, public errors, badge, invitation, same-state CRM and deterministic reset
- BUILD 02 visible member contrast and information-only branch produce declared interests without a registration
- BUILD 02 visible primary path: recognized customer, counterfactual, required data, optional skip, unchanged badge and shared CRM
- H21 frozen-baseline falsification experiment records the first material falsifier and stops at B's initial read-model boundary
- H22 — Experience-Stable Behavior Selection (local experiment) checks frozen inputs, positive/negative controls and both selection boundaries; stops on first falsifier
- H23 — Situated Evaluation Context Binding checks effective A/B inputs, contradictions and independent authority; stops on first material falsifier
- H24 — Situated Activity Representation Provenance records the existing-source falsifier without changing runtime or inventing a representation contract
- H25 — Script-Bound Situated Activity Representation separates declaration, accepted facts, optional representation and evaluation on the live shared provider
- H26 — Situated Guest Perspective Provenance reproduces the inspected missing subject/narrative relation without changing any application source
- H27 — Explicit Situated Subject Representation keeps declared subject labels independent of account, facts, session, evaluation and Activity
- H28 — Account-Sourced Guest Presentation derives account-only sessionLabel from member.name independently of subject presentation and all factual inputs
- H29 — Operational Subject Status Provenance represents only existing present state, independently of account, subject labels, Activity and Evidence
- H30 current-live: script-bound situated narrative preserves facts and accumulated H25–H29 behavior
- H30 pre-delta: records and compares all six operational positions in A/B
- H32 historical S32 App DOM replay: independent brand and explicit static intro preserve cumulative facts and presentation authorities
- H33 historical S33 App replay: operational subject references alone identify supervision subjects across A/B and independent presentation perturbations
- H34 historical S34 replay: existing session subject reference alone represents operational session across A/B and independent presentation perturbations
- H35 historical S35 replay: Experience.name supplies the GuestPerspective name across A/B and independent presentation perturbations
- H37 current App: reduce unsupported Activity attribution without new relations or factual changes
- H38 inherited product, historical evidence, routing, config and all other sources remain byte-identical
- H39 STOP gate preserves every received material file and existing H37/H38 assertions
- Session 40 — first executable Sports Season vertical runs enrollment, simulated presence and self-reported effort as distinct records
