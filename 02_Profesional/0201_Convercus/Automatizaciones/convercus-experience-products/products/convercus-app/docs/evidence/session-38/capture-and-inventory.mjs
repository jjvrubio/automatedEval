import { createHash } from 'node:crypto';
import { readFileSync, readdirSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../../../..');
const proto = resolve(root, 'products/convercus-app/prototype');
const read = (p) => readFileSync(p, 'utf8');
const sha = (b) => createHash('sha256').update(b).digest('hex');
const ignored = new Set(['.git', 'node_modules', 'dist', '.vite', 'coverage']);
const entries = [];
function walk(dir) {
  for (const e of readdirSync(dir, { withFileTypes: true })) {
    const p = resolve(dir, e.name);
    if (ignored.has(e.name) || p === here) continue;
    if (e.isDirectory()) walk(p);
    else if (e.isFile()) entries.push({ path: relative(root, p).normalize('NFC'), bytes: readFileSync(p) });
  }
}
walk(root);
const ambient = entries.filter((e) => /(^|\/)\.DS_Store$|\.tsbuildinfo$/.test(e.path));
const files = Object.fromEntries(entries.filter((e) => !ambient.includes(e)).map((e) => [e.path, sha(e.bytes)]).sort(([a], [b]) => a.localeCompare(b)));
const baseline = { session: 38, capturedAt: new Date().toISOString(), basis: 'Received CLOSED S37 working tree, before infrastructure modifications; not HEAD',
  files, fileCount: Object.keys(files).length, excluded: [...ignored, '.DS_Store metadata inventoried separately', '*.tsbuildinfo', 'new session-38 evidence'],
  ambientObserved: ambient.map((e) => ({ path: e.path, sha256: sha(e.bytes), byteLength: e.bytes.length, headerHex: e.bytes.subarray(0, 16).toString('hex') })) };
writeFileSync(resolve(here, 'baseline.json'), JSON.stringify(baseline, null, 2) + '\n', { flag: 'wx' });

const inspectedIncidental = new Set([
  '00-governance/.DS_Store', '01-semantic-contract/.DS_Store', '01-semantic-contract/source-excerpts/.DS_Store',
  '02-shared-contracts/.DS_Store', 'products/convercus-app/prototype/src/.DS_Store',
]);
const manifest = { status: 'LOCAL / EXPERIMENTAL / NOT PROMOTED', rule: 'Positive material source sets from immutable session baselines; complete partition checked against original path/hash inventories; no glob exclusions',
  sessions: {} };
for (const [session, file] of [['H21', 'session-21-frozen-baseline.json'], ['H22', 'evidence/session-22/baseline.json'], ['H23', 'evidence/session-23/baseline.json']]) {
  const path = resolve(root, 'products/convercus-app/docs', file);
  const bytes = readFileSync(path), b = JSON.parse(bytes);
  const all = b.files ?? { ...b.sharedFiles, ...b.protectedFiles };
  manifest.sessions[session] = {
    baseline: relative(root, path), baselineSha256: sha(bytes),
    material: Object.fromEntries(Object.entries(all).filter(([p]) => !inspectedIncidental.has(p))),
    incidental: Object.fromEntries(Object.entries(all).filter(([p]) => inspectedIncidental.has(p))),
    reason: 'Original preservation inventory; only individually audited Finder metadata is nonmaterial. All other historical entries and expected hashes retained; existing allowedChangedFiles logic remains in each harness.',
  };
}
mkdirSync(resolve(here, 'candidate'), { recursive: true });
writeFileSync(resolve(here, 'candidate/material-source-set.json'), JSON.stringify(manifest, null, 2) + '\n', { flag: 'wx' });

const routes = [];
for (const session of [24, 26, 27, 28, 29, 31]) {
  const p = 'products/convercus-app/prototype/src/demo-factory/test-fixtures/h' + session + '/source-path.ts';
  const source = read(resolve(root, p));
  let map;
  if (source.includes('new Set([')) {
    const paths = [...source.split('new Set([')[1].split(']);')[0].matchAll(/"([^"]+)"/g)].map((m) => m[1]);
    const prefix = 'products/convercus-app/prototype/src/';
    map = Object.fromEntries(paths.map((v) => [prefix + v, prefix + 'demo-factory/test-fixtures/h' + session + '/' + v.split('/').at(-1) + (v.includes('.test.') ? '.txt' : '')]));
  } else map = Object.fromEntries([...source.matchAll(/"(products[^"]+)": "(products[^"]+)"/g)].map((m) => [m[1], m[2]]));
  routes.push({ session, file: p, kind: 'logical path mapping', count: Object.keys(map).length, map });
}
for (const session of [34, 36]) {
  const p = 'products/convercus-app/prototype/src/demo-factory/test-fixtures/h' + session + '/archive-paths.json';
  const map = JSON.parse(read(resolve(root, p)));
  routes.push({ session, file: p, kind: 'historical-read exact path map', count: Object.keys(map).length, map });
}
const fixturePaths = Object.keys(files).filter((p) => p.includes('/test-fixtures/'));
const tests = Object.keys(files).filter((p) => /\/src\/.*\.test\.tsx?$/.test(p));
const harnesses = tests.map((path) => {
  const source = read(resolve(root, path));
  return { path, sha256: files[path], historical: /test-fixtures|historicalH|readHistorical/.test(source),
    routeHelpers: [...source.matchAll(/import .*from "([^"]*(?:source-path|historical-read|archive-paths)[^"]*)"/g)].map((m) => m[1]),
    mocks: [...source.matchAll(/vi\.mock\("([^"]+)", \(\) => import\("([^"]+)"\)\)/g)].map((m) => ({ module: m[1], replacement: m[2] })),
    recordingVariables: [...new Set([...source.matchAll(/process\.env\.([A-Z0-9_]+)/g)].map((m) => m[1]))],
    portability: 'relative to prototype cwd; no universally relocatable/package guarantee',
  };
});
const relocatedImports = fixturePaths.filter((p) => p.endsWith('.ts') || p.endsWith('.tsx')).map((path) => ({
  path, imports: [...read(resolve(root, path)).matchAll(/(?:from |import\()"([^"]+)"/g)].map((m) => m[1]),
})).filter((x) => x.imports.length);
const unknownCandidates = entries.filter((e) => /(^|\/)(Thumbs\.db|desktop\.ini|\._[^/]+)|\.sw[op]$|~$|\.tmp$/.test(e.path)).map((e) => e.path);
const inventory = { session: 38, capturedAt: new Date().toISOString(), routes, routeCount: routes.reduce((n, r) => n + r.count, 0),
  pathMappingHelpers: 6, historicalReaders: 2, testFileCount: tests.length, fixtureFileCount: fixturePaths.length,
  archiveByteCopies: fixturePaths.filter((p) => p.endsWith('.txt')).length,
  archivedRuntimeModules: fixturePaths.filter((p) => /\.tsx?$/.test(p) && !p.endsWith('/source-path.ts') && !p.endsWith('/historical-read.ts')).length,
  fixtureFiles: fixturePaths, harnesses, relocatedImports,
  baselineManifests: Object.keys(files).filter((p) => /baseline.*\.json$/.test(p)),
  preservationChecks: Object.keys(files).filter((p) => /preservation|verify-session|verification-summary/.test(p)),
  incidentalObserved: baseline.ambientObserved, otherIncidentalCandidatesFound: unknownCandidates,
  nativeToolchain: { node: process.version, platform: process.platform, arch: process.arch, executable: process.execPath,
    declaredEngine: JSON.parse(read(resolve(proto, 'package.json'))).engines.node, delta: 'NONE' },
};
writeFileSync(resolve(here, 'replay-inventory-before.json'), JSON.stringify(inventory, null, 2) + '\n', { flag: 'wx' });
console.log(JSON.stringify({ files: baseline.fileCount, ambient: ambient.length, routes: inventory.routeCount, fixtures: inventory.fixtureFileCount,
  sessions: Object.fromEntries(Object.entries(manifest.sessions).map(([s, v]) => [s, { material: Object.keys(v.material).length, incidental: Object.keys(v.incidental).length }])),
  tests: inventory.testFileCount, otherIncidentalCandidates: unknownCandidates }, null, 2));
