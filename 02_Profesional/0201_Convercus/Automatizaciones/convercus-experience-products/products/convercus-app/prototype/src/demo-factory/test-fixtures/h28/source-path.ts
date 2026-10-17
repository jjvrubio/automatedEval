// Test-only routing to the byte-identical H28 sources preserved before H29.
const prefix = "products/convercus-app/prototype/src/";
const archived = new Set([
  "demo-factory/family-adventure-vertical.test.ts",
  "demo-factory/situated-evaluation-context-h23.test.ts",
  "demo-factory/situated-activity-provenance-h24.test.ts",
  "demo-factory/script-bound-activity-h25.test.ts",
  "demo-factory/situated-guest-provenance-h26.test.ts",
  "demo-factory/explicit-subject-representation-h27.test.ts",

  "demo-factory/vertical-evaluation.ts",
  "demo-factory/account-sourced-guest-h28.test.ts",
]);

export function historicalH28Path(path: string): string {
  const relative = path.slice(prefix.length);
  if (!path.startsWith(prefix) || !archived.has(relative)) return path;
  const name = relative.slice(relative.lastIndexOf("/") + 1);
  return `${prefix}demo-factory/test-fixtures/h28/${name}${name.includes(".test.") ? ".txt" : ""}`;
}
