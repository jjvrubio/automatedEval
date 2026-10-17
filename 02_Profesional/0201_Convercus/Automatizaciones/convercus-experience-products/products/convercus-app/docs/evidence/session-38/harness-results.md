# S38 — resultado por archivo de test

Configuración habitual, ejecución concurrente predeterminada. Todos los archivos disponibles ejecutados; sin skip ni timeout.

| Archivo | Función | Resultado | Tests PASS |
| --- | --- | --- | --- |
| src/demo/mock-adapter.test.ts | Verificación actual | PASSED | 2 |
| src/config/app-config.test.ts | Verificación actual | PASSED | 1 |
| src/config/brand.test.ts | Verificación actual | PASSED | 3 |
| src/demo-factory/account-sourced-guest-h28.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/activity-attribution-reduction-h37.test.ts | Verificación actual | PASSED | 1 |
| src/demo-factory/app-smoke.test.tsx | Verificación actual | PASSED | 2 |
| src/demo-factory/bootstrap.test.ts | Verificación actual | PASSED | 9 |
| src/demo-factory/composition-boundary-h21.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/cross-subject-evidence-admissibility.test.ts | Verificación actual | PASSED | 8 |
| src/demo-factory/derived-claim-contextual-validity.test.ts | Verificación actual | PASSED | 6 |
| src/demo-factory/evidence-relevance.test.ts | Verificación actual | PASSED | 12 |
| src/demo-factory/evidence-sufficiency.test.ts | Verificación actual | PASSED | 15 |
| src/demo-factory/experience-sourced-guest-name-h35.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/experience-stable-selection-h22.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/explicit-introductory-framing-h32.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/explicit-subject-representation-h27.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/family-adventure-vertical.test.ts | Replay histórico | PASSED | 10 |
| src/demo-factory/historical-replay-portability-h38.test.ts | Infraestructura H38 | PASSED | 8 |
| src/demo-factory/operational-session-subject-h34.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/operational-subject-status-h29.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/operational-supervision-subject-h33.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/pre-delta-position-h30.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/presenter-action.test.tsx | Verificación actual | PASSED | 6 |
| src/demo-factory/projection.test.ts | Verificación actual | PASSED | 4 |
| src/demo-factory/script-bound-activity-h25.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/script-bound-journey-h30.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/situated-activity-provenance-h24.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/situated-evaluation-context-h23.test.ts | Replay histórico | PASSED | 1 |
| src/demo-factory/situated-guest-provenance-h26.test.ts | Replay histórico | PASSED | 1 |
| src/domain/demo-package.test.ts | Verificación actual | PASSED | 3 |
| src/domain/routing.test.ts | Verificación actual | PASSED | 1 |

H31 y H36: sin harness independiente; sus informes y evidencias permanecen byte-idénticos. No se contabilizan como tests PASS.

Totales: 106 PASS / 0 FAIL / 0 pendientes; 31 archivos.
