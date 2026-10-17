import assert from 'node:assert/strict';
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const inventory = JSON.parse(readFileSync(resolve(here, 'replay-inventory-before.json')));
const variables = [...new Set(inventory.harnesses.flatMap(h => h.recordingVariables))];
const results = ['absent', 'present'].map(label => { const r = JSON.parse(readFileSync(resolve(here, 'inherited-' + label, 'results.json'))); assert.equal(r.success, true); return { label, passed: r.numPassedTests, failed: r.numFailedTests, pending: r.numPendingTests, files: r.testResults.length }; });
const differences = [];
function diff(a, b, path) {
  if (a === b) return;
  if (a && b && typeof a === 'object' && typeof b === 'object') { for (const key of new Set([...Object.keys(a), ...Object.keys(b)])) diff(a[key], b[key], path + '/' + key); }
  else differences.push({ path, absent: a, present: b });
}
for (const variable of variables) {
  const filename = variable.toLowerCase() + '.json';
  const a = JSON.parse(readFileSync(resolve(here, 'inherited-absent', filename)));
  const b = JSON.parse(readFileSync(resolve(here, 'inherited-present', filename)));
  diff(a, b, variable);
  // Only the observation timestamp, never occurredAt, DOM, facts or hashes.
  const field = variable === 'H30_MATRIX_PATH' ? 'capturedAt' : 'recordedAt';
  for (const t of [a, b]) { assert.ok(Number.isFinite(Date.parse(t[field]))); delete t[field]; }
  assert.deepEqual(a, b, variable);
}
assert.ok(differences.every(d => d.path === (d.path.startsWith('H30_MATRIX_PATH/') ? 'H30_MATRIX_PATH/capturedAt' : d.path.split('/')[0] + '/recordedAt')));
const result = { session: 38, recordedAt: new Date().toISOString(), scope: 'All 30 inherited test files in both metadata conditions; new H38 tests verified separately in actual tree', results, comparedTraceVariables: variables, traceEquality: 'Exact deep equality after removing only top-level recordedAt, or capturedAt for H30_MATRIX_PATH', observedDifferences: differences, initialComparatorObservation: 'Initial strict comparison removed recordedAt only and correctly reported H30 capturedAt; full structural diff found only 16 capture timestamps. No material field, historical assertion or stored trace was changed.', environmentQualification: 'Same macOS arm64, official Node and installed dependencies; brand asset origin held fixed with fixture-only explicit Vite fs.allow entry', productDelta: 'NONE', historicalExpectedDelta: 'NONE' };
writeFileSync(resolve(here, 'inherited-environment-matrix.json'), JSON.stringify(result, null, 2) + '\n', { flag: 'wx' });
console.log(JSON.stringify({ results, comparedTraces: variables.length, differences: differences.length, materialEquality: 'PASS' }));
