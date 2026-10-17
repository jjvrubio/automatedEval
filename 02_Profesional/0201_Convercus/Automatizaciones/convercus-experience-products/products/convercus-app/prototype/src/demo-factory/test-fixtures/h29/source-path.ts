// Test-only H29 source routing; earlier archive paths retain precedence.
const paths: Record<string, string> = {
  "products/convercus-app/prototype/src/demo/mock-adapter.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/mock-adapter.ts",
  "products/convercus-app/prototype/src/demo-factory/contracts.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/contracts.ts",
  "products/convercus-app/prototype/src/demo-factory/vertical-evaluation.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/vertical-evaluation.ts",
  "products/convercus-app/prototype/src/demo-factory/artifacts.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/artifacts.ts",
  "products/convercus-app/prototype/src/demo-factory/costa-artifacts.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/costa-artifacts.ts",
  "products/convercus-app/prototype/src/demo-factory/account-sourced-guest-h28.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/account-sourced-guest-h28.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/composition-boundary-h21.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/composition-boundary-h21.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/experience-stable-selection-h22.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/experience-stable-selection-h22.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/explicit-subject-representation-h27.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/explicit-subject-representation-h27.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/operational-subject-status-h29.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/operational-subject-status-h29.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/script-bound-activity-h25.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/script-bound-activity-h25.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/situated-activity-provenance-h24.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/situated-activity-provenance-h24.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/situated-evaluation-context-h23.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/situated-evaluation-context-h23.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/situated-guest-provenance-h26.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h29/situated-guest-provenance-h26.test.ts.txt"
};
export const historicalH29Path = (path: string): string => paths[path] ?? path;
