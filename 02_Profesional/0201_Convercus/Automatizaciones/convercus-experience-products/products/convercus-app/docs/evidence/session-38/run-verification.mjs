import { spawn } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const proto = resolve(here, '../../../prototype');
const results = [];
for (const [name, args, recording] of [
  ['full-suite', ['test', '--', '--reporter=default', '--reporter=json', '--outputFile=' + resolve(here, 'full-suite-results.json')], true],
  ['current-h37', ['test', '--', 'src/demo-factory/activity-attribution-reduction-h37.test.ts', '--reporter=default', '--reporter=json', '--outputFile=' + resolve(here, 'current-h37-results.json')], false],
  ['typecheck', ['run', 'typecheck'], false], ['lint', ['run', 'lint'], false], ['build', ['run', 'build'], false],
]) {
  console.log('START ' + name);
  const start = Date.now();
  const result = await new Promise((ok, fail) => {
    const child = spawn(resolve(dirname(process.execPath), 'npm'), args, { cwd: proto, env: { ...process.env, PATH: dirname(process.execPath) + ':' + process.env.PATH,
      ...(recording ? { H38_RECORD_PATH: resolve(here, 'execution-trace.json'), H37_RECORD_PATH: resolve(here, 'current-cumulative-trace.json') } : {}) } });
    let output = '';
    child.stdout.on('data', b => { output += b; }); child.stderr.on('data', b => { output += b; });
    child.on('error', fail); child.on('close', code => ok({ code, output }));
  });
  writeFileSync(resolve(here, name + '.log'), result.output, { flag: 'wx' });
  results.push({ name, command: 'npm ' + args.join(' '), code: result.code, milliseconds: Date.now() - start, log: name + '.log' });
  console.log(JSON.stringify(results.at(-1)));
}
writeFileSync(resolve(here, 'verification-commands.json'), JSON.stringify({ recordedAt: new Date().toISOString(), node: process.version, platform: process.platform + '-' + process.arch, runnerConfigDelta: 'NONE', concurrency: 'Vitest default; no serial override; no timeout increase', results }, null, 2) + '\n', { flag: 'wx' });
if (results.some(r => r.code !== 0)) process.exitCode = 1;
