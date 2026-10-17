import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const control = JSON.parse(readFileSync(resolve(here, 'portability-controls.json')));
const inventory = JSON.parse(readFileSync(resolve(here, 'replay-inventory-before.json')));
const variables = [...new Set(inventory.harnesses.flatMap(h => h.recordingVariables))];
const results = [], traces = [];
for (const [label, suffix] of [['absent', 'environment-a-absent'], ['present', 'environment-b-present']]) {
  const output = resolve(here, 'inherited-' + label); mkdirSync(output);
  const proto = resolve(control.temporaryRoot, suffix, 'products/convercus-app/prototype');
  const recording = Object.fromEntries(variables.map(v => [v, resolve(output, v.toLowerCase() + '.json')]));
  console.log('START inherited suite ' + label);
  const result = await new Promise((ok, fail) => {
    const child = spawn(process.execPath, [resolve(proto, 'node_modules/vitest/vitest.mjs'), 'run', '--config=h38-controlled-origin.config.ts', '--reporter=default', '--reporter=json', '--outputFile=' + resolve(output, 'results.json')], { cwd: proto, env: { ...process.env, ...recording, PATH: dirname(process.execPath) + ':' + process.env.PATH } });
    let log = ''; child.stdout.on('data', b => { log += b; }); child.stderr.on('data', b => { log += b; });
    child.on('error', fail); child.on('close', code => ok({ code, log }));
  });
  writeFileSync(resolve(output, 'suite.log'), result.log);
  const reporter = JSON.parse(readFileSync(resolve(output, 'results.json')));
  const row = { label, code: result.code, passed: reporter.numPassedTests, failed: reporter.numFailedTests, files: reporter.testResults.length };
  results.push(row); console.log(JSON.stringify(row));
  assert.equal(result.code, 0);
  traces.push(Object.fromEntries(variables.map(v => {
    assert.ok(existsSync(recording[v]), v);
    const trace = JSON.parse(readFileSync(recording[v]));
    delete trace.recordedAt;
    return [v, trace];
  })));
}
await import('./compare-environment-traces.mjs');
console.log('INHERITED ENVIRONMENT MATRIX PASS');
