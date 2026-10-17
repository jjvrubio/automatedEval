// Historical harness routing only. Apply older archive routing first when a
// session predates H25; this maps remaining live paths to their pre-H27 bytes.
const prefix = "products/convercus-app/prototype/src/";
const archived = new Set([
  "demo-factory/contracts.ts",
  "demo-factory/artifacts.ts",
  "demo-factory/costa-artifacts.ts",
  "demo/mock-adapter.ts",
  "demo-factory/vertical-evaluation.ts",
  "demo-factory/situated-evaluation-context-h23.test.ts",
  "demo-factory/situated-activity-provenance-h24.test.ts",
  "demo-factory/script-bound-activity-h25.test.ts",
  "demo-factory/situated-guest-provenance-h26.test.ts",
]);

export function historicalH26Path(path: string): string {
  const relative = path.slice(prefix.length);
  if (!path.startsWith(prefix) || !archived.has(relative)) return path;
  const name = relative.slice(relative.lastIndexOf("/") + 1);
  return `${prefix}demo-factory/test-fixtures/h26/${name}${name.includes(".test.") ? ".txt" : ""}`;
}
