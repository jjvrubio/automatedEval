// Test-only source routing for H27 replay; no historical baseline is rewritten.
const prefix = "products/convercus-app/prototype/src/";
const archived = new Set([
  "demo/mock-adapter.ts",
  "demo-factory/vertical-evaluation.ts",
  "demo-factory/explicit-subject-representation-h27.test.ts",
]);

export function historicalH27Path(path: string): string {
  const relative = path.slice(prefix.length);
  if (!path.startsWith(prefix) || !archived.has(relative)) return path;
  const name = relative.slice(relative.lastIndexOf("/") + 1);
  return `${prefix}demo-factory/test-fixtures/h27/${name}${name.includes(".test.") ? ".txt" : ""}`;
}
