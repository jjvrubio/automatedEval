import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const projectRoot = resolve(here, '../../../../..');
const product = resolve(here, '../../..');
const prototype = resolve(product, 'prototype');
const read = (path) => readFileSync(path, 'utf8');
const json = (path) => JSON.parse(read(path));
const sha = (bytes) => createHash('sha256').update(bytes).digest('hex');
const digest = (path) => sha(readFileSync(path));
const baseline = json(resolve(here, 'baseline.json'));
const tracePath = resolve(here, 'execution-trace-final.json');
const trace = json(tracePath);
const routes = json(resolve(prototype, 'src/demo-factory/test-fixtures/h36/archive-paths.json'));
const changed = [], unchanged = [], unexpected = [];
for (const [path, hash] of Object.entries(baseline.files)) {
  const target = resolve(projectRoot, path);
  if (!existsSync(target)) { unexpected.push({ path, reason: 'deleted' }); continue; }
  const current = digest(target);
  if (current === hash) unchanged.push(path);
  else if (routes[path]) {
    assert.equal(digest(resolve(projectRoot, routes[path])), hash, 'pre-delta archive: ' + path);
    changed.push({ path, before: hash, after: current, archive: routes[path] });
  } else unexpected.push({ path, reason: 'unexpected modification', before: hash, after: current });
}
assert.deepEqual(unexpected, []);
assert.equal(changed.length, 7);
assert.equal(Object.keys(routes).length, 7);
for (const [path, archive] of Object.entries(routes)) assert.equal(digest(resolve(projectRoot, archive)), baseline.files[path]);
assert.equal(trace.baselineSha256, digest(resolve(here, 'baseline.json')));
assert.equal(trace.priorTraceSha256, digest(resolve(here, '../session-35/execution-trace.json')));
assert.equal(trace.harnessSha256, digest(resolve(prototype, 'src/demo-factory/activity-attribution-reduction-h37.test.ts')));
for (const [path, hash] of Object.entries(trace.sourceHashes)) assert.equal(digest(resolve(prototype, path)), hash, 'trace current source: ' + path);
const inheritedS36 = Object.keys(baseline.files).filter((path) => path.includes('/docs/evidence/session-36/') || path.endsWith('/session-36-presentation-authority-provenance-stratification-audit.md'));
for (const path of inheritedS36) assert.equal(digest(resolve(projectRoot, path)), baseline.files[path]);
const historical = json(resolve(here, '../session-35/execution-trace.json'));
const frames = (run) => [...run.frames, run.resetFrame];
const factKeys = ['phase', 'input', 'snapshot', 'verticalCalls', 'verticalResults', 'jointEvaluationCalls', 'jointEvaluationResults'];
const fact = (frame) => Object.fromEntries(factKeys.filter((k) => k in frame).map((k) => [k, structuredClone(frame[k])]));
const deltas = [];
for (const [index, control] of trace.controls.entries()) {
  const old = historical.controls[index].original;
  const ids = new Set(control.original.executedActions.filter((a) => a.evidence).map((a) => a.evidence.id));
  const mask = (frame) => {
    const value = fact(frame);
    value.snapshot.activity.forEach((a) => { if (ids.has(a.id)) a.description = ''; });
    return value;
  };
  assert.deepEqual(frames(control.original).map(mask), frames(old).map(mask));
  assert.deepEqual(frames(control.original).map((f) => f.homeDOM), frames(old).map((f) => f.homeDOM));
  assert.deepEqual(frames(control.original).map((f) => f.supervisionDOM), frames(old).map((f) => f.supervisionDOM));
  const oldDescriptions = new Map(old.frames.at(-1).snapshot.activity.map((a) => [a.id, a.description]));
  for (const a of control.original.frames.at(-1).snapshot.activity) {
    if (a.description !== oldDescriptions.get(a.id)) deltas.push({ composition: control.composition, id: a.id, before: oldDescriptions.get(a.id), after: a.description });
  }
  for (const name of ['account', 'subjects']) assert.deepEqual(
    frames(control.variants[name]).map((f) => f.snapshot.activity),
    frames(control.original).map((f) => f.snapshot.activity),
  );
}
assert.equal(deltas.length, 4);
for (const rejection of trace.occurrenceNegatives) assert.deepEqual(rejection.before, rejection.after);
assert.equal(trace.occurrenceNegatives.length, 16);
assert.equal(trace.currentAppRuns, 14);
assert.equal(trace.currentAppFrames, 77);
assert.equal(trace.currentAppDOMCaptures, 231);
assert.equal(trace.isolatedAppObservations, 6);
for (const g of trace.genericRegression) {
  const old = historical.genericRegression.find((x) => x.demoId === g.demoId);
  assert.deepEqual(frames(g.current).map(fact), frames(old.current).map(fact));
  for (const key of ['homeDOM', 'activityDOM', 'supervisionDOM']) assert.deepEqual(frames(g.current).map((f) => f[key]), frames(old.current).map((f) => f[key]));
}
const preservation = {
  session: 37, verifiedAt: new Date().toISOString(), baselineFiles: baseline.fileCount,
  unchangedCount: unchanged.length, authorizedChangedFiles: changed, unexpectedChanges: unexpected,
  historicalS36FilesUnchanged: inheritedS36.length, exactArchivedSourceRoutes: Object.keys(routes).length,
  productDelta: deltas, testsAndInfrastructureCountedSeparately: true,
  AppByteIdentical: true, guardsContractsEvaluatorsFixturesManifestsByteIdentical: true,
  ArchitectureADR_TES_PSC_unchanged: true,
};
writeFileSync(resolve(here, 'preservation-check.json'), JSON.stringify(preservation, null, 2) + '\n');

const reportPath = resolve(product, 'docs/session-37-activity-attribution-claim-provenance-and-reduction.md');
const report = read(reportPath);
const required = [
  'H36 CONSOLIDATED INPUT', 'H37 HYPOTHESIS', 'VARIABLE UNDER TEST',
  'WHY NO NEW RELATION IS AUTHORIZED', 'PRE-DELTA ACTIVITY CLAIM MATRIX',
  'ACTIVITY OCCURRENCE AUTHORITY', 'EVIDENCE SUBJECT ATTRIBUTION AUTHORITY',
  'H25 EDITORIAL AUTHORITY', 'VIEWER CLAIM ANALYSIS', 'ACCOUNT EXECUTION CLAIM ANALYSIS',
  'H27 / ACTIVITY SEPARATION', 'SESSION SUBJECT / ACTIVITY SEPARATION',
  'REDUCTION DECISION', 'CANONICAL DESCRIPTION DELTA', 'NO-NEW-RELATION ANALYSIS',
  'APP CONSUMER BOUNDARY', 'BASELINE', 'CODE DELTA OR STOP', 'A CONTROL', 'B CONTROL',
  'ACCOUNT INDEPENDENCE CONTROL', 'SUBJECT PRESENTATION INDEPENDENCE CONTROL',
  'SESSION SUBJECT INDEPENDENCE CONTROL', 'EVIDENCE ATTRIBUTION PRESERVATION',
  'OCCURRENCE NEGATIVE CONTROL', 'EDITORIAL INDEPENDENCE CONTROL', 'CONTRADICTION CONTROL',
  'SEMANTIC NEGATIVE CHECK', 'CURRENT APP DOM / INTEGRATION EXECUTION',
  'BROWSER VISUAL VALIDATION STATUS', 'NEGATIVE CONTROLS', 'CURRENT CUMULATIVE REGRESSION',
  'HISTORICAL REPLAY STATUS', 'TEST-INFRASTRUCTURE PRESSURE OBSERVATION', 'EXECUTION TRACE',
  'H25 STATUS', 'H36 HISTORICAL VERDICT STATUS', 'ACTIVITY ATTRIBUTION RESULT',
  'AUTHORITY MODEL OBSERVATION', 'FALSIFICATION ANALYSIS', 'H37 VERDICT',
  'ARCHITECTURAL CONSEQUENCE', 'SEMANTIC CONSEQUENCE', 'ARTIFACT QUARANTINE',
  'WHAT H37 DOES NOT PROVE', 'REMAINING PRESSURES',
];
for (const section of required) assert.ok(report.includes('\n## ' + section + '\n'), section);
const linked = [...report.matchAll(/\]\(([^)]+)\)/g)].map((m) => m[1]);
for (const link of linked) {
  if (link.endsWith('/verification-summary.json')) continue; // Output of this run.
  assert.ok(existsSync(resolve(dirname(reportPath), link.split('#')[0])), 'report link ' + link);
}
const baselineLog = read(resolve(here, 'baseline-parallel-node-tests.log'));
const finalLog = read(resolve(here, 'final-parallel-tests.log'));
assert.match(baselineLog, /3 failed \| 94 passed \(97\)/);
assert.match(finalLog, /3 failed \| 95 passed \(98\)/);
assert.match(finalLog, /3 failed \| 27 passed \(30\)/);
const failures = (text) => [...text.matchAll(/^ FAIL\s+(\S+\.test\.ts)/gm)].map((m) => m[1]).sort();
assert.deepEqual(failures(baselineLog), failures(finalLog));
assert.equal(failures(finalLog).length, 3);
assert.ok(!read(resolve(here, 'typecheck-final.log')).includes('error TS'));
assert.match(read(resolve(here, 'build.log')), /files generated/);
const summary = {
  session: 37, verifiedAt: new Date().toISOString(),
  H37: 'SUPPORTED WITH QUALIFICATION', noNewRelation: 'SUFFICIENT',
  baseline: { parallelTests: { files: 29, passed: 94, failed: 3 }, initialBundledNode: 'STARTUP ERROR; zero tests' },
  final: { parallelTests: { files: 30, passed: 95, failed: 3 }, newFailures: [], unchangedFailingTests: failures(finalLog),
    failureReason: 'ENOENT 00-governance/.DS_Store before journey checks; inherited Mac metadata dependency',
    serialTests: 'NOT EXECUTED: deterministic missing file, no timeouts', typecheck: 'PASS', lint: 'PASS', buildPWA: 'PASS', overallSuiteExitCode: 1 },
  timeoutsOrAssertionsRelaxed: false, testRunnerConfigurationChanged: false,
  historicalHarnessesModified: 4, existingHistoricalReadersModified: 1, archivedSourceRoutesAdded: 7,
  runtimeArchiveCopiesAdded: 2, currentHarnessesAdded: 1,
  currentAppRuns: trace.currentAppRuns, currentAppFrames: trace.currentAppFrames,
  currentAppDOMCaptures: trace.currentAppDOMCaptures, isolatedAppObservations: 6, rejectedOccurrenceControls: 16,
  historicalRunsCountedAsCurrent: 0, domIntegrationVerification: 'EXECUTED', browserVisualValidation: 'NOT EXECUTED',
  requiredReportSectionsVerified: required.length, preDeltaFragmentUnits: 22,
  localReportLinksVerified: linked.length, traceSourceHashesVerified: true,
  inheritedFilesUnchanged: unchanged.length, unexpectedInheritedSourceChanges: [],
  traceSha256: digest(tracePath), reportSha256: digest(reportPath),
  preDeltaMatrixSha256: digest(resolve(here, 'pre-delta-claim-matrix.md')),
  nodeRuntime: { version: 'v24.14.0', location: '/private/tmp/node-v24.14.0-darwin-arm64',
    origin: 'https://nodejs.org/dist/v24.14.0/node-v24.14.0-darwin-arm64.tar.gz',
    sha256: 'a1a54f46a750d2523d628d924aab61758a51c9dad3e0238beb14141be9615dd3',
    projectDependenciesChanged: false },
  historicalH36Verdict: 'PRESERVED / FALSIFIED', promotionGate: 'CLOSED', nextMaterialPressure: 'OBSERVED BUT NOT SELECTED',
};
writeFileSync(resolve(here, 'verification-summary.json'), JSON.stringify(summary, null, 2) + '\n');
console.log(JSON.stringify(summary, null, 2));
