import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { cpSync, existsSync, mkdirSync, mkdtempSync, readFileSync, renameSync, symlinkSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawn } from 'node:child_process';

const here = dirname(fileURLToPath(import.meta.url));
const sourceRoot = resolve(here, '../../../../..');
const relativeProto = 'products/convercus-app/prototype';
const sourceProto = resolve(sourceRoot, relativeProto);
// Hold the existing asset origin fixed while varying metadata. A first,
// fully relocated probe is retained separately: its H37 Retail DOM compares
// a literal /@fs absolute logo URL and fails. Do not rewrite that expectation.
const output = resolve(here, 'controlled-asset-origin');
mkdirSync(output, { recursive: true });
const temp = mkdtempSync('/private/tmp/convercus-h38-portability-');
const suites = [
  ['H21', 'composition-boundary-h21.test.ts'],
  ['H22', 'experience-stable-selection-h22.test.ts'],
  ['H23', 'situated-evaluation-context-h23.test.ts'],
];
const current = 'activity-attribution-reduction-h37.test.ts';
const prefix = 'src/demo-factory/';
const importLine = 'import { materialBaselineEntries } from "./test-fixtures/h38/material-baseline";\n';
const snapshots = JSON.parse(readFileSync(resolve(here, 'baseline.json'), 'utf8'));
const hash = (bytes) => createHash('sha256').update(bytes).digest('hex');
const excluded = new Set(['.git', 'node_modules', 'dist', '.vite', 'coverage', '.DS_Store']);
function createEnvironment(name) {
  const root = resolve(temp, name);
  cpSync(sourceRoot, root, {
    recursive: true,
    filter: (p) => p !== here && p !== resolve(sourceRoot, '03-shared-assets') && !excluded.has(p.split('/').at(-1)) && !p.endsWith('.tsbuildinfo'),
  });
  const proto = resolve(root, relativeProto);
  symlinkSync(resolve(sourceRoot, '03-shared-assets'), resolve(root, '03-shared-assets'), 'dir');
  symlinkSync(resolve(sourceProto, 'node_modules'), resolve(proto, 'node_modules'), 'dir');
  // Fixture-only access declaration: Vite checks the real path of the shared
  // asset. Preserve the repository config, assertions, workers and timeouts;
  // explicitly allow only the existing brand directory for these temp tests.
  writeFileSync(resolve(proto, 'h38-controlled-origin.config.ts'),
    'import config from "./vite.config";\n' +
    'export default { ...config, server: { ...config.server, fs: { ...config.server?.fs, allow: [...(config.server?.fs?.allow ?? []), ' +
    JSON.stringify(resolve(sourceRoot, '03-shared-assets/brands/convercus')) + '] } } };\n');
  const destination = resolve(proto, prefix, 'test-fixtures/h38');
  mkdirSync(destination, { recursive: true });
  for (const f of ['material-baseline.ts', 'material-source-set.json']) cpSync(resolve(here, 'candidate', f), resolve(destination, f));
  for (const [session, filename] of suites) {
    const p = resolve(proto, prefix, filename);
    let source = readFileSync(p, 'utf8');
    assert.equal(hash(source), snapshots.files[relativeProto + '/' + prefix + filename]);
    const expression = session === 'H21'
      ? 'Object.entries({ ...baseline.sharedFiles, ...baseline.protectedFiles })'
      : 'Object.entries(baseline.files)';
    assert.equal(source.split(expression).length, 2);
    source = source.replace('/// <reference types="node" />\n', '/// <reference types="node" />\n' + importLine)
      .replace(expression, 'materialBaselineEntries("' + session + '", ' + (session === 'H21' ? '{ ...baseline.sharedFiles, ...baseline.protectedFiles }' : 'baseline.files') + ')');
    writeFileSync(p, source);
  }
  return { root, proto };
}
const environmentA = createEnvironment('environment-a-absent');
const environmentB = createEnvironment('environment-b-present');
const metadataSample = readFileSync(resolve(sourceRoot, '.DS_Store'));
assert.equal(metadataSample.subarray(4, 8).toString(), 'Bud1');
const manifest = JSON.parse(readFileSync(resolve(here, 'candidate/material-source-set.json')));
const incidentalPaths = [...new Set(Object.values(manifest.sessions).flatMap((s) => Object.keys(s.incidental)))];
for (const path of incidentalPaths) {
  assert.ok(!existsSync(resolve(environmentA.root, path)));
  const p = resolve(environmentB.root, path); mkdirSync(dirname(p), { recursive: true }); writeFileSync(p, metadataSample);
}
const conditions = [];
async function run(name, environment, includeCurrent = false) {
  const jsonPath = resolve(output, name + '-results.json');
  const testPaths = suites.map(([, f]) => prefix + f);
  if (includeCurrent) testPaths.push(prefix + current);
  const recordPaths = Object.fromEntries(suites.map(([session]) => [session + '_RECORD_PATH', resolve(output, name + '-' + session.toLowerCase() + '.json')]));
  if (includeCurrent) recordPaths.H37_RECORD_PATH = resolve(output, name + '-h37.json');
  const args = [resolve(environment.proto, 'node_modules/vitest/vitest.mjs'), 'run', ...testPaths, '--config=h38-controlled-origin.config.ts', '--reporter=default', '--reporter=json', '--outputFile=' + jsonPath];
  console.log('START ' + name);
  const start = Date.now();
  const result = await new Promise((ok, fail) => {
    const child = spawn(process.execPath, args, {
      cwd: environment.proto,
      env: { ...process.env, ...recordPaths, PATH: dirname(process.execPath) + ':' + process.env.PATH, NO_COLOR: '1' },
    });
    let output = '';
    child.stdout.on('data', (b) => { output += b; });
    child.stderr.on('data', (b) => { output += b; });
    child.on('error', fail);
    child.on('close', (code) => ok({ code, output }));
  });
  writeFileSync(resolve(output, name + '.log'), result.output);
  const data = JSON.parse(readFileSync(jsonPath));
  const status = { name, environment: environment.root, code: result.code, milliseconds: Date.now() - start,
    passed: data.numPassedTests, failed: data.numFailedTests, failedSuites: data.numFailedTestSuites,
    tests: data.testResults.flatMap((t) => t.assertionResults.map((a) => ({ file: t.name.split('/src/').at(-1), name: a.fullName, status: a.status, failureMessages: a.failureMessages }))),
    log: name + '.log', reporter: name + '-results.json' };
  conditions.push(status);
  console.log(JSON.stringify({ name, code: status.code, passed: status.passed, failed: status.failed }));
  writeFileSync(resolve(output, 'portability-controls-progress.json'), JSON.stringify({ temp, conditions }, null, 2) + '\n');
  return status;
}
function outcomes(name) {
  return suites.map(([s]) => {
    const value = JSON.parse(readFileSync(resolve(output, name + '-' + s.toLowerCase() + '.json')));
    delete value.recordedAt;
    return value;
  });
}
function materialTraceOnly(trace) {
  // This also preserves descriptions, facts, evaluator calls/results and all DOM.
  const { recordedAt, ...rest } = trace;
  void recordedAt;
  return rest;
}
const absent = await run('absence', environmentA, true);
assert.equal(absent.code, 0);
const present = await run('presence', environmentB, true);
assert.equal(present.code, 0);
assert.deepEqual(outcomes('presence'), outcomes('absence'));
assert.deepEqual(materialTraceOnly(JSON.parse(readFileSync(resolve(output, 'presence-h37.json')))),
  materialTraceOnly(JSON.parse(readFileSync(resolve(output, 'absence-h37.json')))));

writeFileSync(resolve(environmentA.root, 'unrelated-environment-note.txt'), 'H38 unknown ambient file, outside declared material set.\n');
const unknown = await run('unknown-file', environmentA);
assert.equal(unknown.code, 0); assert.deepEqual(outcomes('unknown-file'), outcomes('absence'));

const material = resolve(environmentA.proto, prefix, 'test-fixtures/h21/mock-adapter.ts');
const bytes = readFileSync(material);
writeFileSync(material, Buffer.concat([bytes, Buffer.from('\n// H38 temporary material mutation probe.\n')]));
const mutation = await run('material-mutation', environmentA);
assert.notEqual(mutation.code, 0);
assert.ok(mutation.tests.some((t) => t.status === 'failed' && t.failureMessages.some((m) => /expected|assert/i.test(m))));
writeFileSync(material, bytes);
renameSync(material, material + '.h38-hidden');
const removal = await run('material-removal', environmentA);
assert.notEqual(removal.code, 0);
renameSync(material + '.h38-hidden', material);

const currentSource = resolve(environmentA.proto, 'src/demo/mock-adapter.ts');
const currentBytes = readFileSync(currentSource);
writeFileSync(currentSource, Buffer.concat([currentBytes, Buffer.from('\n// H38 temporary CURRENT source mutation, not an archive.\n')]));
const separation = await run('current-source-mutation', environmentA, true);
assert.notEqual(separation.code, 0);
for (const [, f] of suites) assert.equal(separation.tests.find((t) => t.file.endsWith(f)).status, 'passed');
assert.equal(separation.tests.find((t) => t.file.endsWith(current)).status, 'failed');
assert.deepEqual(outcomes('current-source-mutation'), outcomes('absence'));
writeFileSync(currentSource, currentBytes);

const baselineReportPaths = [
  'products/convercus-app/docs/session-21-frozen-baseline.json',
  'products/convercus-app/docs/evidence/session-22/baseline.json',
  'products/convercus-app/docs/evidence/session-23/baseline.json',
];
for (const environment of [environmentA, environmentB]) for (const p of baselineReportPaths) assert.equal(hash(readFileSync(resolve(environment.root, p))), snapshots.files[p]);
const evidence = {
  session: 38, recordedAt: new Date().toISOString(), scope: 'Candidate tested in temporary project copies before modifying project harnesses',
  platformsTested: [process.platform + '-' + process.arch], node: process.version, sharedDependencies: resolve(sourceProto, 'node_modules'),
  resultDirectory: 'controlled-asset-origin',
  temporaryConfigDelta: 'Only add the existing real brand directory to Vite fs.allow in an isolated fixture wrapper; repository config bytes, runner, workers and timeouts unchanged.',
  hermeticityLimit: 'Product/test source conditions isolated; dependencies, installed Node and asset origin shared. Not an OS/container or arbitrary-root relocation claim.',
  additionalPortabilityPressure: { fullRelocationProbe: 'absence.log', status: 'OPEN', cause: 'Historical Retail DOM contains literal /@fs absolute logo URL. No product or expectation changed; controlled metadata comparisons keep this asset origin fixed.' },
  metadataPresenceSource: { origin: 'preexisting Finder metadata on this same Mac', source: '.DS_Store', sha256: hash(metadataSample), headerHex: metadataSample.subarray(0, 16).toString('hex'),
    destinations: incidentalPaths, onlyInsideTemporaryEnvironmentB: true, originalMissingMetadataNotRestored: true },
  temporaryRoot: temp, conditions, materialMutationDetected: true, materialRemovalDetected: true,
  allThreeHistoricalOutputsEqualAbsentPresent: true, currentH37OutputsEqualAbsentPresent: true,
  historicalOutputsEqualUnderCurrentSourceMutation: true, currentVerificationDetectsCurrentMutation: true,
  candidateGate: 'PASS for implementation; no product or historical semantic assertion changes',
};
writeFileSync(resolve(here, 'portability-controls.json'), JSON.stringify(evidence, null, 2) + '\n', { flag: 'wx' });
console.log('CANDIDATE GATE PASS');
