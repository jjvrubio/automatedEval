import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { dirname, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { isDeepStrictEqual } from 'node:util';
const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../../../..');
const proto = resolve(root, 'products/convercus-app/prototype');
const read = p => readFileSync(p, 'utf8');
const sha = b => createHash('sha256').update(b).digest('hex');
const baseline = JSON.parse(read(resolve(here, 'baseline.json')));
const inventory = JSON.parse(read(resolve(here, 'replay-inventory-before.json')));
const prefix = 'products/convercus-app/prototype/src/demo-factory/';
const allowed = ['composition-boundary-h21.test.ts', 'experience-stable-selection-h22.test.ts', 'situated-evaluation-context-h23.test.ts'].map(n => prefix + n);
const changed = [], unchanged = [];
for (const [path, before] of Object.entries(baseline.files)) {
  const after = sha(readFileSync(resolve(root, path)));
  if (before === after) unchanged.push(path);
  else changed.push({ path, before, after });
}
assert.deepEqual(changed.map(c => c.path).sort(), allowed.slice().sort());
for (const c of changed) {
  const archive = resolve(root, prefix, 'test-fixtures/h37', c.path.split('/').at(-1) + '.txt');
  assert.equal(sha(readFileSync(archive)), c.before);
  c.archive = relative(root, archive);
}
const beforeTrace = JSON.parse(read(resolve(here, '../session-37/execution-trace-final.json')));
const afterTrace = JSON.parse(read(resolve(here, 'current-cumulative-trace.json')));
const traceDifferences = Object.keys(beforeTrace).filter(k => !isDeepStrictEqual(beforeTrace[k], afterTrace[k]));
assert.deepEqual(traceDifferences, ['recordedAt']);
for (const [path, hash] of Object.entries(beforeTrace.sourceHashes)) assert.equal(sha(readFileSync(resolve(proto, path))), hash);
assert.equal(sha(readFileSync(resolve(proto, 'src/demo-factory/activity-attribution-reduction-h37.test.ts'))), beforeTrace.harnessSha256);
const allRouteKeys = new Set(inventory.routes.flatMap(r => Object.keys(r.map)));
const missingRoutes = [], targetAlsoKey = [];
for (const r of inventory.routes) {
  assert.equal(sha(readFileSync(resolve(root, r.file))), baseline.files[r.file]);
  for (const [from, to] of Object.entries(r.map)) {
    if (!existsSync(resolve(root, to))) missingRoutes.push({ from, to });
    if (allRouteKeys.has(to)) targetAlsoKey.push({ from, to });
  }
}
assert.deepEqual(missingRoutes, []); assert.deepEqual(targetAlsoKey, []);
const fixtureFiles = [];
function walk(dir) { for (const e of readdirSync(dir, { withFileTypes: true })) { const p = resolve(dir, e.name); if (e.isDirectory()) walk(p); else if (e.isFile()) fixtureFiles.push(p); } }
walk(resolve(proto, 'src/demo-factory/test-fixtures'));
const afterInventory = {
  session: 38, archiveRouteEntries: inventory.routeCount, distinctLogicalRouteKeys: allRouteKeys.size,
  pathHelpers: 6, historicalReaders: 2, fixtureFiles: fixtureFiles.length,
  archivedByteCopies: fixtureFiles.filter(p => p.endsWith('.txt')).length,
  archivedRuntimeModules: inventory.archivedRuntimeModules, newMaterialSelectors: 1,
  historicalRuntimeHarnesses: 16, inheritedHarnessesAdaptedInS38: 3, testFiles: 31,
  missingRouteTargets: missingRoutes, routeTargetsThatAreAlsoKeys: targetAlsoKey,
  meaning: 'Entry count excludes inline special cases; no recursive archive search. h38 material-baseline is a new selector, not an archived runtime module or source-routing reader.',
};
assert.equal(afterInventory.fixtureFiles, 135); assert.equal(afterInventory.archivedByteCopies, 68);
writeFileSync(resolve(here, 'replay-inventory-after.json'), JSON.stringify(afterInventory, null, 2) + '\n');
writeFileSync(resolve(here, 'preservation-check.json'), JSON.stringify({
  session: 38, verifiedAt: new Date().toISOString(), baselineFiles: Object.keys(baseline.files).length,
  unchangedCount: unchanged.length, authorizedChangedFiles: changed, unexpectedChanges: [],
  sourceHashesEqualS37FinalTrace: true, finalS37TraceComparison: { differences: traceDifferences, allMaterialOutputAndHarnessHashesIdentical: true },
  productDelta: 'NONE', semanticDelta: 'NONE', archiveRoutingDelta: 'NONE', nodePackageLockConfigDelta: 'NONE',
  historicalExpectations: 'Exact original assertion bodies; only import and preservation enumeration changed; verified by H38 test',
}, null, 2) + '\n');
const suite = JSON.parse(read(resolve(here, 'full-suite-results.json')));
assert.equal(suite.numPassedTests, 106); assert.equal(suite.numFailedTests, 0); assert.equal(suite.numPendingTests, 0);
const names = new Map(inventory.harnesses.map(h => [h.path, h]));
const rows = suite.testResults.map(t => {
  const path = relative(root, t.name);
  const h = names.get(path);
  const kind = path.includes('historical-replay-portability-h38') ? 'Infraestructura H38'
    : h?.historical && !path.includes('activity-attribution-reduction-h37') ? 'Replay histórico' : 'Verificación actual';
  return { file: relative(proto, t.name), kind, status: t.status, pass: t.assertionResults.filter(a => a.status === 'passed').length };
});
const table = ['# S38 — resultado por archivo de test', '', 'Configuración habitual, ejecución concurrente predeterminada. Todos los archivos disponibles ejecutados; sin skip ni timeout.', '',
  '| Archivo | Función | Resultado | Tests PASS |', '| --- | --- | --- | --- |',
  ...rows.map(r => '| ' + r.file + ' | ' + r.kind + ' | ' + r.status.toUpperCase() + ' | ' + r.pass + ' |'),
  '', 'H31 y H36: sin harness independiente; sus informes y evidencias permanecen byte-idénticos. No se contabilizan como tests PASS.',
  '', 'Totales: 106 PASS / 0 FAIL / 0 pendientes; 31 archivos.', ''].join('\n');
writeFileSync(resolve(here, 'harness-results.md'), table);
const report = resolve(here, '../../session-38-historical-replay-portability-evidence-integrity.md');
const sections = ['H37 CONSOLIDATED INPUT','H38 HYPOTHESIS','INFRASTRUCTURE PRESSURE RECEIVED','FAILURE REPRODUCTION','H21–H23 HISTORICAL INTENT','.DS_STORE MATERIALITY ANALYSIS','MATERIAL EVIDENCE DEFINITION','INCIDENTAL METADATA ANALYSIS','CURRENT REPLAY ARCHITECTURE INVENTORY','ROUTING CHAIN ANALYSIS','HISTORICAL SOURCE / ENVIRONMENT SEPARATION','CANDIDATE PORTABILITY STRATEGIES','STRATEGY DECISION','MINIMAL INFRASTRUCTURE DELTA GATE','BASELINE','INFRASTRUCTURE DELTA OR STOP','PRODUCT FREEZE','SEMANTIC FREEZE','H21 CONTROL','H22 CONTROL','H23 CONTROL','INCIDENTAL METADATA ABSENCE CONTROL','INCIDENTAL METADATA PRESENCE CONTROL','MATERIAL CONTENT MUTATION CONTROL','MATERIAL FILE REMOVAL CONTROL','UNKNOWN FILE CONTROL','CURRENT / HISTORICAL SOURCE SEPARATION CONTROL','ROUTING SHADOW CONTROL','UNICODE / PATH NORMALIZATION CONTROL','NODE ENVIRONMENT OBSERVATION','CONCURRENCY / TIMEOUT OBSERVATION','FULL HISTORICAL REPLAY RESULT','CURRENT CUMULATIVE VERIFICATION','EVIDENCE-INTEGRITY MANIFEST','REPLAY MAINTENANCE COST','TEST-INFRASTRUCTURE PRESSURE RESULT','FALSIFICATION ANALYSIS','H38 VERDICT','ARCHITECTURAL CONSEQUENCE','SEMANTIC CONSEQUENCE','PROMOTION GATE STATUS','WHAT H38 DOES NOT PROVE','REMAINING PRESSURES'];
for (const title of sections) assert.ok(read(report).includes('## ' + title + '\n'), title);
const documents = [report, resolve(here, '../../demo-construction-baseline-after-session-38.md'), resolve(here, 'evidence-integrity-manifest.md')];
let links = 0;
for (const doc of documents) for (const match of read(doc).matchAll(/\]\(([^)]+)\)/g)) {
  const path = match[1]; if (/^https?:|^#/.test(path)) continue;
  assert.ok(existsSync(resolve(dirname(doc), path.split('#')[0])), doc + ': ' + path); links++;
}
const commands = JSON.parse(read(resolve(here, 'verification-commands.json')));
assert.ok(commands.results.every(r => r.code === 0));
const matrix = JSON.parse(read(resolve(here, 'inherited-environment-matrix.json')));
assert.ok(matrix.results.every(r => r.passed === 98 && r.failed === 0));
const checksumFiles = [];
function evidenceWalk(dir) { for (const e of readdirSync(dir, { withFileTypes: true })) { const p = resolve(dir, e.name); if (e.isDirectory()) evidenceWalk(p); else if (e.isFile() && e.name !== 'verification-summary.json' && e.name !== 'evidence-checksums.json') checksumFiles.push(p); } }
evidenceWalk(here);
for (const p of [report, documents[1], ...allowed.map(p => resolve(root, p)),
  resolve(proto, 'src/demo-factory/historical-replay-portability-h38.test.ts'),
  resolve(proto, 'src/demo-factory/test-fixtures/h38/material-baseline.ts'), resolve(proto, 'src/demo-factory/test-fixtures/h38/material-source-set.json')]) checksumFiles.push(p);
const checksums = Object.fromEntries(checksumFiles.sort().map(p => [relative(root, p), sha(readFileSync(p))]));
writeFileSync(resolve(here, 'evidence-checksums.json'), JSON.stringify({ session: 38, status: 'Local audit index, not a signature or adversarial tamper guarantee', files: checksums }, null, 2) + '\n');
const summary = { session: 38, verifiedAt: new Date().toISOString(), verdict: 'SUPPORTED WITH QUALIFICATION', requiredSections: sections.length, verifiedLocalLinks: links, frozenFiles: unchanged.length, changedInheritedFiles: changed.length,
  finalSuite: { passed: suite.numPassedTests, failed: suite.numFailedTests, files: rows.length },
  historicalRuntime: { files: rows.filter(r => r.kind === 'Replay histórico').length, tests: rows.filter(r => r.kind === 'Replay histórico').reduce((n,r) => n+r.pass,0) },
  currentVerification: { files: rows.filter(r => r.kind === 'Verificación actual').length, tests: rows.filter(r => r.kind === 'Verificación actual').reduce((n,r) => n+r.pass,0) },
  environmentMatrix: matrix.results, currentH37MaterialEqualityToS37FinalTrace: true, newEvidenceFilesHashed: checksumFiles.length,
  qualifications: ['macOS arm64 only', 'Shared Node/dependencies/asset origin in temporary conditions', 'Absolute asset URL/root relocation OPEN', 'Legacy lexical path alias pressure OPEN', 'No browser visual or commercial acceptance', 'Rule NOT PROMOTED; H39 NOT OPENED'] };
writeFileSync(resolve(here, 'verification-summary.json'), JSON.stringify(summary, null, 2) + '\n');
console.log(JSON.stringify(summary, null, 2));
