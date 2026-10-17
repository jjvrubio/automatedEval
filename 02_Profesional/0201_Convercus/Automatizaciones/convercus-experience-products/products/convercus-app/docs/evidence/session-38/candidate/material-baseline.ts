import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { posix, resolve } from "node:path";
import sourceSets from "./material-source-set.json";

type SourceSet = { material: Record<string, string>; incidental: Record<string, string> };

// S38 local evidence rule. Normalize logical identity only, never file bytes.
// Reject collisions/traversal; no case folding or extension-based blacklist.
export function logicalEvidencePath(path: string): string {
  if (!path || posix.isAbsolute(path) || path.split("/").includes("..") || path.includes("\\")) {
    throw new Error("Invalid logical evidence path: " + path);
  }
  const normalized = posix.normalize(path).normalize("NFC");
  if (normalized === ".") throw new Error("Invalid logical evidence path: " + path);
  return normalized;
}

function normalizedEntries(files: Record<string, string>): Map<string, string> {
  const result = new Map<string, string>();
  for (const [path, hash] of Object.entries(files)) {
    const key = logicalEvidencePath(path);
    if (result.has(key)) throw new Error("Ambiguous evidence path normalization: " + key);
    result.set(key, hash);
  }
  return result;
}

export function selectMaterialEntries(sourceSet: SourceSet, captured: Record<string, string>): Array<[string, string]> {
  const material = normalizedEntries(sourceSet.material);
  const incidental = normalizedEntries(sourceSet.incidental);
  for (const path of incidental.keys()) {
    if (material.has(path)) throw new Error("Conflicting evidence classification: " + path);
  }
  const declared = new Map([...material, ...incidental]);
  const received = normalizedEntries(captured);
  if (declared.size !== received.size) throw new Error("Historical inventory membership changed");
  for (const [path, hash] of received) {
    if (!declared.has(path) || declared.get(path) !== hash) {
      throw new Error("Historical inventory/hash changed or unclassified: " + path);
    }
  }
  // Only the positively declared set is returned. Original SHA assertions and
  // session-specific allowedChangedFiles/archived routing remain at the caller.
  return [...material];
}

export function materialBaselineEntries(session: keyof typeof sourceSets.sessions, captured: Record<string, string>): Array<[string, string]> {
  const sourceSet = sourceSets.sessions[session];
  const baseline = readFileSync(resolve(process.cwd(), "../../..", sourceSet.baseline));
  const hash = createHash("sha256").update(baseline).digest("hex");
  if (hash !== sourceSet.baselineSha256) throw new Error("Original historical baseline changed: " + session);
  return selectMaterialEntries(sourceSet, captured);
}
