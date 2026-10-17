import { createHash } from 'node:crypto';
import { readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { dirname, relative, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../../../../..');
const ignored = new Set(['node_modules', 'dist', '.git', '.vite', 'coverage', '.DS_Store']);
const sha = (bytes) => createHash('sha256').update(bytes).digest('hex');
const files = {};
function walk(dir) {
  for (const item of readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    const path = resolve(dir, item.name);
    if (ignored.has(item.name) || item.name.endsWith('.tsbuildinfo') || path === here) continue;
    if (item.isDirectory()) walk(path);
    else if (item.isFile()) files[relative(root, path).normalize('NFC')] = sha(readFileSync(path));
  }
}
walk(root);
const s36 = JSON.parse(readFileSync(resolve(here, '../session-36/baseline.json'), 'utf8'));
const differences = Object.entries(s36.files).filter(([path, hash]) => files[path] !== hash).map(([path]) => path);
const prefix = 'products/convercus-app/prototype/src/demo-factory/';
const declarations = ['artifacts.ts', 'costa-artifacts.ts'].flatMap((filename, index) => {
  const source = readFileSync(resolve(root, prefix + filename), 'utf8');
  return [...source.matchAll(/activityPresentation: \{\s*title: "([^"]+)",\s*description: "([^"]+)"/g)].map((match, step) => ({
    composition: index ? 'B' : 'A', source: prefix + filename,
    line: source.slice(0, match.index).split('\n').length,
    step: step ? 'discover-clue-b' : 'discover-clue-a', actionId: step ? 'discover-clue-b' : 'discover-clue-a',
    title: match[1], description: match[2],
  }));
});
if (declarations.length !== 4) throw new Error('Expected exactly four canonical presentations; inspect before continuing.');
const baseline = {
  session: 37, capturedAt: new Date().toISOString(),
  basis: 'received working tree after CLOSED S36; before any H37 product or historical-harness delta',
  excluded: [...ignored, '*.tsbuildinfo', 'docs/evidence/session-37'],
  fileCount: Object.keys(files).length, files,
  continuityWithS36: { compared: Object.keys(s36.files).length, differences },
  canonicalPresentations: declarations,
  applicableAgents: [],
  workingTreeStatus: execFileSync('git', ['status', '--short', '--', '.'], { cwd: root, encoding: 'utf8' }),
};
writeFileSync(resolve(here, 'baseline.json'), JSON.stringify(baseline, null, 2) + '\n', { flag: 'wx' });
console.log(JSON.stringify({ capturedAt: baseline.capturedAt, files: baseline.fileCount, differences, declarations }, null, 2));
