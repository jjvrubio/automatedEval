/// <reference types="node" />
import { createHash } from "node:crypto";
import { mkdtempSync, mkdirSync, readFileSync, renameSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { expect, it } from "vitest";
import { logicalEvidencePath, materialBaselineEntries, selectMaterialEntries } from "./test-fixtures/h38/material-baseline";
import sourceSets from "./test-fixtures/h38/material-source-set.json";
import { historicalH24Path } from "./test-fixtures/h24/source-path";
import { historicalH29Path } from "./test-fixtures/h29/source-path";
import { historicalH31Path } from "./test-fixtures/h31/source-path";
import { readHistoricalH34FileSync } from "./test-fixtures/h34/historical-read";
import { readHistoricalH36FileSync } from "./test-fixtures/h36/historical-read";

const root = resolve(process.cwd(), "../../..");
const sha = (bytes: Buffer | string) => createHash("sha256").update(bytes).digest("hex");
const prefix = "products/convercus-app/prototype/src/demo-factory/";
const evidence = resolve(process.cwd(), "../docs/evidence/session-38");
const baseline = JSON.parse(readFileSync(resolve(evidence, "baseline.json"), "utf8")) as { files: Record<string, string> };
const harnesses = {
  H21: "composition-boundary-h21.test.ts",
  H22: "experience-stable-selection-h22.test.ts",
  H23: "situated-evaluation-context-h23.test.ts",
};
const observations: Record<string, unknown> = {};

it.each(["H21", "H22", "H23"] as const)("H38 %s positive material set retains all original non-incidental path/hash expectations", (session) => {
  const definition = sourceSets.sessions[session];
  const original = JSON.parse(readFileSync(resolve(root, definition.baseline), "utf8")) as {
    files?: Record<string, string>; sharedFiles: Record<string, string>; protectedFiles: Record<string, string>;
  };
  const captured = original.files ?? { ...original.sharedFiles, ...original.protectedFiles };
  const selected = materialBaselineEntries(session, captured);
  expect(Object.fromEntries(selected)).toEqual(definition.material);
  expect({ ...definition.material, ...definition.incidental }).toEqual(captured);
  expect(selected.length).toBe(session === "H21" ? 51 : session === "H22" ? 74 : 94);
  observations[session] = { material: selected.length, incidental: Object.keys(definition.incidental), originalHashesRetained: true };
});

it("H38 fails closed on missing, changed or unknown inventory entries; naming a file .DS_Store does not exempt material", () => {
  const sourceSet = { material: { "owned/source.ts": "source-hash", "owned/.DS_Store": "intentional-evidence-hash" },
    incidental: { "ambient/.DS_Store": "old-metadata-hash" } };
  const captured = { ...sourceSet.material, ...sourceSet.incidental };
  expect(selectMaterialEntries(sourceSet, captured)).toEqual(Object.entries(sourceSet.material));
  expect(() => selectMaterialEntries(sourceSet, { ...captured, "owned/source.ts": "different" })).toThrow("Historical inventory/hash changed");
  const absent = { ...captured }; delete (absent as Record<string, string>)["owned/source.ts"];
  expect(() => selectMaterialEntries(sourceSet, absent)).toThrow("membership changed");
  expect(() => selectMaterialEntries(sourceSet, { ...captured, "unreviewed/input.ts": "unknown" })).toThrow("membership changed");
  expect(() => selectMaterialEntries({ material: captured, incidental: sourceSet.incidental }, captured)).toThrow("Conflicting evidence classification");
  observations.membership = "Material hash changes/removal/unclassified additions fail; filename alone never excludes a source";
});

it("H38 NFC/NFD logical identity preserves exact bytes, rejects collisions and does not fold case", () => {
  const nfc = "evidence/sesión-3.md", nfd = nfc.normalize("NFD");
  expect(nfc).not.toBe(nfd);
  expect(logicalEvidencePath(nfd)).toBe(nfc);
  expect(selectMaterialEntries({ material: { [nfc]: "same" }, incidental: {} }, { [nfd]: "same" })).toEqual([[nfc, "same"]]);
  expect(() => selectMaterialEntries({ material: { [nfc]: "same" }, incidental: {} }, { [nfc]: "same", [nfd]: "same" })).toThrow("Ambiguous");
  expect(logicalEvidencePath("evidence/Sesión-3.md")).not.toBe(nfc);
  expect(() => logicalEvidencePath("../outside.ts")).toThrow("Invalid");
  expect(() => logicalEvidencePath("/absolute.ts")).toThrow("Invalid");
  const temporary = mkdtempSync(join(tmpdir(), "h38-unicode-"));
  const bytes = Buffer.from("Contenido con e\u0301 sin normalizar.\r\n");
  try {
    mkdirSync(join(temporary, "evidence"));
    writeFileSync(join(temporary, nfd), bytes);
    expect(readFileSync(join(temporary, nfc))).toEqual(bytes); // macOS/APFS observation, not universal filesystem claim.
    expect(sha(readFileSync(join(temporary, nfd)))).toBe(sha(bytes));
    observations.unicode = { platform: process.platform, normalization: "logical paths NFC; collision fail; case-sensitive", fileBytesPreserved: true };
  } finally { rmSync(temporary, { recursive: true }); }
});

it("H38 actual routing selects the older archive before newer/current shadows and never falls back when material is missing", () => {
  const temporary = mkdtempSync(join(tmpdir(), "h38-routing-"));
  const cwd = process.cwd();
  const logical = prefix + "artifacts.ts";
  const older = historicalH24Path(logical);
  const newer = prefix + "test-fixtures/h36/artifacts.ts.txt";
  const middle = prefix + "test-fixtures/h31/artifacts.ts";
  const put = (path: string, value: string) => { const absolute = resolve(temporary, path); mkdirSync(dirname(absolute), { recursive: true }); writeFileSync(absolute, value); };
  for (const [path, value] of [[logical, "CURRENT"], [older, "OLDER"], [newer, "NEWER"], [middle, "MIDDLE"]]) put(path, value);
  mkdirSync(resolve(temporary, "products/convercus-app/prototype"), { recursive: true });
  try {
    process.chdir(resolve(temporary, "products/convercus-app/prototype"));
    const selected = historicalH31Path(historicalH29Path(historicalH24Path(logical)));
    expect(selected).toBe(older);
    expect(readHistoricalH34FileSync(resolve(temporary, selected), "utf8")).toBe("OLDER");
    expect(readHistoricalH36FileSync(resolve(temporary, logical), "utf8")).toBe("NEWER");
    expect(readFileSync(resolve(temporary, logical), "utf8")).toBe("CURRENT");
    expect(readHistoricalH34FileSync(resolve(process.cwd(), "../../..", selected), "utf8")).toBe("OLDER");
    renameSync(resolve(temporary, older), resolve(temporary, older + ".hidden"));
    expect(() => readHistoricalH34FileSync(resolve(temporary, selected), "utf8")).toThrow(/ENOENT/);
    observations.routing = { selected, olderArchiveWins: true, newerAndCurrentExist: true, missingOldArchiveDoesNotFallBack: true, nativeCurrentReadIndependent: true };
  } finally { process.chdir(cwd); rmSync(temporary, { recursive: true }); }
});

it("H38 changes only import and preservation enumeration; original material assertion bodies are byte-identical", () => {
  for (const [session, name] of Object.entries(harnesses)) {
    const original = readFileSync(resolve(root, prefix, "test-fixtures/h37", name + ".txt"), "utf8");
    expect(sha(original)).toBe(baseline.files[prefix + name]);
    const expression = session === "H21" ? "Object.entries({ ...baseline.sharedFiles, ...baseline.protectedFiles })" : "Object.entries(baseline.files)";
    const replacement = 'materialBaselineEntries("' + session + '", ' + (session === "H21" ? "{ ...baseline.sharedFiles, ...baseline.protectedFiles }" : "baseline.files") + ")";
    const expected = original.replace('/// <reference types="node" />\n',
      '/// <reference types="node" />\nimport { materialBaselineEntries } from "./test-fixtures/h38/material-baseline";\n').replace(expression, replacement);
    expect(readFileSync(resolve(root, prefix, name), "utf8")).toBe(expected);
  }
  observations.historicalAssertions = "All unchanged; exact import/enumeration-only delta checked against pre-S38 sources";
});

it("H38 inherited product, historical evidence, routing, config and all other sources remain byte-identical", () => {
  const allowed = new Set(Object.values(harnesses).map((name) => prefix + name));
  let protectedCount = 0;
  for (const [path, hash] of Object.entries(baseline.files)) {
    if (allowed.has(path)) continue;
    expect(sha(readFileSync(resolve(root, path))), path).toBe(hash);
    protectedCount++;
  }
  expect(protectedCount).toBe(Object.keys(baseline.files).length - 3);
  observations.freeze = { protectedFiles: protectedCount, productDelta: "NONE", semanticDelta: "NONE", routingDelta: "NONE" };
  if (process.env.H38_RECORD_PATH) writeFileSync(resolve(process.env.H38_RECORD_PATH),
    JSON.stringify({ session: 38, recordedAt: new Date().toISOString(), observations }, null, 2) + "\n", { flag: "wx" });
});
