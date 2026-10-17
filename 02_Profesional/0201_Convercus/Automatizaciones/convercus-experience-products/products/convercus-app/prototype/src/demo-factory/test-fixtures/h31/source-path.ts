// Test-only S31 source routing. Earlier archive paths retain precedence.
const paths: Record<string, string> = {
  "products/convercus-app/prototype/src/app/App.tsx": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/App.tsx",
  "products/convercus-app/prototype/src/demo-factory/contracts.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/contracts.ts",
  "products/convercus-app/prototype/src/demo-factory/artifacts.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/artifacts.ts",
  "products/convercus-app/prototype/src/demo-factory/costa-artifacts.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/costa-artifacts.ts",
  "products/convercus-app/prototype/src/demo-factory/explicit-subject-representation-h27.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/explicit-subject-representation-h27.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/script-bound-activity-h25.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/script-bound-activity-h25.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/situated-activity-provenance-h24.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/situated-activity-provenance-h24.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/operational-subject-status-h29.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/operational-subject-status-h29.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/experience-stable-selection-h22.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/experience-stable-selection-h22.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/script-bound-journey-h30.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/script-bound-journey-h30.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/situated-guest-provenance-h26.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/situated-guest-provenance-h26.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/situated-evaluation-context-h23.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/situated-evaluation-context-h23.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/pre-delta-position-h30.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/pre-delta-position-h30.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/account-sourced-guest-h28.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/account-sourced-guest-h28.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/composition-boundary-h21.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/composition-boundary-h21.test.ts.txt",
  "products/convercus-app/prototype/src/demo-factory/family-adventure-vertical.test.ts": "products/convercus-app/prototype/src/demo-factory/test-fixtures/h31/family-adventure-vertical.test.ts.txt"
};
export const historicalH31Path = (path: string): string => paths[path] ?? path;
