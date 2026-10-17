import { readFileSync } from "node:fs";
import { relative, resolve } from "node:path";
import archivePaths from "./archive-paths.json";

// Test-only S36 routing for the H37 scalar delta. Existing older routes win
// before this reader is called. Current H37 uses node:fs directly.
const paths: Record<string, string> = archivePaths;
export const readHistoricalH36FileSync = ((...args: Parameters<typeof readFileSync>) => {
  const [path, options] = args;
  const root = resolve(process.cwd(), "../../..");
  const archived = typeof path === "string" ? paths[relative(root, resolve(path))] : undefined;
  return readFileSync(archived ? resolve(root, archived) : path, options);
}) as typeof readFileSync;
