// Test-only routing for sources archived before H25. No baseline is rewritten.
// H21/H22 retain their older adapter/evaluation routing before using this helper.
const prefix = "products/convercus-app/prototype/src/";
const archived = new Set([
  "demo/mock-adapter.ts",
  "demo-factory/contracts.ts",
  "demo-factory/bootstrap.ts",
  "demo-factory/artifacts.ts",
  "demo-factory/costa-artifacts.ts",
  "demo-factory/composition-boundary-h21.test.ts",
  "demo-factory/experience-stable-selection-h22.test.ts",
  "demo-factory/situated-evaluation-context-h23.test.ts",
  "demo-factory/situated-activity-provenance-h24.test.ts",
]);

export function historicalH24Path(path: string): string {
  const relative = path.slice(prefix.length);
  if (!path.startsWith(prefix) || !archived.has(relative)) return path;
  const name = relative.slice(relative.lastIndexOf("/") + 1);
  return `${prefix}demo-factory/test-fixtures/h24/${name}${name.includes(".test.") ? ".txt" : ""}`;
}
