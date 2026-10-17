import { createHash } from 'node:crypto';
import { existsSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { dirname, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../../../..');
const prototype = resolve(root, 'products/convercus-app/prototype');
const sha = (bytes) => createHash('sha256').update(bytes).digest('hex');
const readJSON = (path) => JSON.parse(readFileSync(path, 'utf8'));
const save = (name, value) => writeFileSync(resolve(here, name), JSON.stringify(value, null, 2) + '\n', { flag: 'wx' });
const excludedDirectories = new Set(['.git', 'node_modules', 'dist', '.vite', 'coverage']);
function inventory(directory = root, files = {}, ambient = {}) {
  for (const entry of readdirSync(directory, { withFileTypes: true })) {
    const path = resolve(directory, entry.name);
    if (excludedDirectories.has(entry.name) || path === here) continue;
    if (entry.isDirectory()) inventory(path, files, ambient);
    else if (entry.isFile()) {
      const key = relative(root, path).normalize('NFC');
      if (key in files || key in ambient) throw new Error('Ambiguous logical path: ' + key);
      const target = entry.name === '.DS_Store' || entry.name.endsWith('.tsbuildinfo') ? ambient : files;
      target[key] = sha(readFileSync(path));
    }
  }
  return { files, ambient };
}

const mode = process.argv[2];
if (mode === 'baseline') {
  const captured = inventory();
  save('baseline.json', {
    session: 39, capturedAt: new Date().toISOString(),
    basis: 'Received working tree after user reconstruction; not HEAD. Before any S39 harness or product edit.',
    authorizedProductFiles: [], authorizedExistingFileChanges: [], ...captured,
    excluded: [...excludedDirectories, 'new session-39 evidence directory', 'Finder metadata and tsbuildinfo inventoried separately; no historical inventories changed'],
    node: { version: process.version, executable: process.execPath, platform: process.platform, arch: process.arch, declaredEngine: readJSON(resolve(prototype, 'package.json')).engines.node },
  });
  console.log(JSON.stringify({ files: Object.keys(captured.files).length, ambient: Object.keys(captured.ambient).length, node: process.version }));
} else if (mode === 'run') {
  const name = process.argv[3];
  const commandName = name.replace(/-final$/, '');
  const commands = {
    'baseline-suite': ['node_modules/vitest/vitest.mjs', 'run', '--reporter=json', '--outputFile=' + resolve(here, 'baseline-suite-results.json')],
    'navigation': ['node_modules/vitest/vitest.mjs', 'run', 'src/demo-factory/effective-composition-navigation-h39.test.tsx', '--reporter=json', '--outputFile=' + resolve(here, 'navigation-results.json')],
    'current-h37': ['node_modules/vitest/vitest.mjs', 'run', 'src/demo-factory/activity-attribution-reduction-h37.test.ts', '--reporter=json', '--outputFile=' + resolve(here, 'current-h37-results.json')],
    'full-suite': ['node_modules/vitest/vitest.mjs', 'run', '--reporter=json', '--outputFile=' + resolve(here, 'full-suite-results.json')],
    'typecheck': ['node_modules/typescript/bin/tsc', '-b', '--pretty', 'false'],
    'lint': ['node_modules/eslint/bin/eslint.js', '.'],
    'build': [resolve(dirname(process.execPath), 'npm'), 'run', 'build'],
  };
  const args = commands[commandName]?.map((arg) => arg.replace(commandName + '-results.json', name + '-results.json'));
  if (!args) throw new Error('Unknown command');
  if (existsSync(resolve(here, name + '-command.json'))) throw new Error('Refusing to overwrite recorded execution');
  const env = { ...process.env, PATH: dirname(process.execPath) + ':' + process.env.PATH };
  if (commandName === 'navigation') env.H39_RECORD_PATH = resolve(here, name.endsWith('-final') ? 'pre-delta-navigation-matrix-final.json' : 'pre-delta-navigation-matrix.json');
  if (name === 'current-h37') env.H37_RECORD_PATH = resolve(here, 'current-cumulative-trace.json');
  const startedAt = new Date().toISOString();
  const result = spawnSync(process.execPath, args, { cwd: prototype, env, encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 });
  writeFileSync(resolve(here, name + '.log'), (result.stdout ?? '') + (result.stderr ?? ''), { flag: 'wx' });
  const recorded = { name, startedAt, finishedAt: new Date().toISOString(), executable: process.execPath, args, cwd: prototype,
    exitCode: result.status, signal: result.signal, error: result.error?.message ?? null };
  save(name + '-command.json', recorded);
  console.log(JSON.stringify(recorded));
  console.log((result.stdout ?? '') + (result.stderr ?? ''));
  process.exitCode = result.status ?? 1;
} else if (mode === 'verify') {
  const baseline = readJSON(resolve(here, 'baseline.json'));
  const current = inventory();
  const changed = Object.entries(baseline.files).filter(([path, hash]) => current.files[path] !== hash).map(([path, before]) => ({ path, before, after: current.files[path] ?? 'MISSING' }));
  const additions = Object.keys(current.files).filter((path) => !(path in baseline.files));
  const h37Before = readJSON(resolve(here, '../session-38/current-cumulative-trace.json'));
  const h37Now = readJSON(resolve(here, 'current-cumulative-trace.json'));
  const traceChanges = [...new Set([...Object.keys(h37Before), ...Object.keys(h37Now)])].filter((key) => key !== 'recordedAt' && JSON.stringify(h37Before[key]) !== JSON.stringify(h37Now[key]));
  const allowedAdditions = [
    'products/convercus-app/prototype/src/demo-factory/effective-composition-navigation-h39.test.tsx',
    'products/convercus-app/docs/session-39-effective-composition-navigation-identity.md',
  ];
  const unexpectedAdditions = additions.filter((path) => !allowedAdditions.includes(path));
  const result = { session: 39, verifiedAt: new Date().toISOString(), receivedFiles: Object.keys(baseline.files).length,
    unchangedFiles: Object.keys(baseline.files).length - changed.length, changed, additions, unexpectedAdditions,
    h37CurrentTrace: { source: 'CURRENT App/provider; inherited harness unchanged', comparison: 'S38 current-cumulative-trace.json; only top-level recordedAt excluded', changedFields: traceChanges },
    productDelta: 'NONE', existingHarnessDelta: 'NONE', historicalEvidenceDelta: 'NONE',
    pass: changed.length === 0 && unexpectedAdditions.length === 0 && traceChanges.length === 0 };
  save('preservation-check.json', result);
  const commands = readdirSync(here).filter((name) => name.endsWith('-command.json')).sort().map((name) => readJSON(resolve(here, name)));
  const tests = Object.fromEntries(['baseline-suite', 'navigation-final', 'current-h37', 'full-suite-final'].map((name) => {
    const report = readJSON(resolve(here, name + '-results.json'));
    return [name, { success: report.success, passed: report.numPassedTests, failed: report.numFailedTests,
      pending: report.numPendingTests, files: report.testResults.length,
      perFile: report.testResults.map((file) => ({ path: relative(prototype, file.name), status: file.status,
        assertions: file.assertionResults.length, failures: file.assertionResults.filter((assertion) => assertion.status !== 'passed') })) }];
  }));
  const matrixBefore = readJSON(resolve(here, 'pre-delta-navigation-matrix.json'));
  const matrixFinal = readJSON(resolve(here, 'pre-delta-navigation-matrix-final.json'));
  const matrixChanges = [...new Set([...Object.keys(matrixBefore), ...Object.keys(matrixFinal)])].filter((key) => !['recordedAt', 'harnessSha256'].includes(key) && JSON.stringify(matrixBefore[key]) !== JSON.stringify(matrixFinal[key]));
  const harness = readFileSync(resolve(prototype, 'src/demo-factory/effective-composition-navigation-h39.test.tsx'), 'utf8');
  const beforeTypeAnnotation = harness.replace('catalogs: DemoCatalogs = defaultDemoCatalogs', 'catalogs = defaultDemoCatalogs');
  const exactHarnessAdjustment = sha(beforeTypeAnnotation) === matrixBefore.harnessSha256 && sha(harness) === matrixFinal.harnessSha256;
  const finalCommands = ['navigation-final', 'current-h37', 'full-suite-final', 'typecheck-final', 'lint-final', 'build-final'];
  const verified = result.pass && exactHarnessAdjustment && matrixChanges.length === 0 &&
    finalCommands.every((name) => commands.some((command) => command.name === name && command.exitCode === 0)) &&
    Object.values(tests).every((test) => test.success && test.failed === 0 && test.pending === 0);
  save('verification-summary.json', {
    session: 39, verifiedAt: new Date().toISOString(), verdict: 'FALSIFIED AS PROBLEM ASSUMPTION / STOP',
    tests, commands, preservation: result, matrixChanges,
    exactHarnessAdjustment: { pass: exactHarnessAdjustment, scope: 'Only added DemoCatalogs parameter type annotation to fix unused import lint; first and final traces materially identical' },
    browser: 'NOT EXECUTED / required in-app execution tool unavailable; generic document reload explicitly modeled in jsdom',
    productDelta: 'NONE', dependenciesInstalled: false, h40: 'NOT OPENED', evidenceVerificationPass: verified,
  });
  const evidenceFiles = Object.fromEntries(readdirSync(here).filter((name) => name !== 'evidence-checksums.json').sort().map((name) => [name, sha(readFileSync(resolve(here, name)))]));
  save('evidence-checksums.json', { session: 39, capturedAt: new Date().toISOString(), files: evidenceFiles,
    report: { path: 'products/convercus-app/docs/session-39-effective-composition-navigation-identity.md', sha256: sha(readFileSync(resolve(here, '../../session-39-effective-composition-navigation-identity.md'))) },
    harness: { path: 'products/convercus-app/prototype/src/demo-factory/effective-composition-navigation-h39.test.tsx', sha256: sha(harness) } });
  console.log(JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ evidenceVerificationPass: verified, exactHarnessAdjustment, matrixChanges }));
  process.exitCode = verified ? 0 : 1;
} else throw new Error('Expected baseline, run <command>, or verify');
