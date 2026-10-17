import { readHistoricalH36FileSync as readFileSync } from "../h36/historical-read";
import { relative, resolve } from "node:path";
import archivePaths from "./archive-paths.json";

// Explicit, test-only S34 source routing. Earlier archive paths are untouched.
// No global fs mock; unresolved paths continue through the S36 archive reader.
const paths: Record<string, string> = archivePaths;
export const readHistoricalH34FileSync = ((...args: Parameters<typeof readFileSync>) => {
  const [path, options] = args;
  const root = resolve(process.cwd(), "../../..");
  const archived = typeof path === "string" ? paths[relative(root, resolve(path))] : undefined;
  return readFileSync(archived ? resolve(root, archived) : path, options);
}) as typeof readFileSync;
