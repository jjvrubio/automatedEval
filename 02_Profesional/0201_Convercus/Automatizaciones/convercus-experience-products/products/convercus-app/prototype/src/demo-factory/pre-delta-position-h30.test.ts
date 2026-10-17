/// <reference types="node" />
import { historicalH31Path } from "./test-fixtures/h31/source-path";
import { createHash } from "node:crypto";
import { writeFileSync } from "node:fs";
import { readHistoricalH34FileSync as readFileSync } from "./test-fixtures/h34/historical-read";
import { resolve } from "node:path";
import { expect, it, vi } from "vitest";
import { resolveDemo } from "./bootstrap";
import type { AppSnapshot } from "./contracts";
import { historicalH29Path } from "./test-fixtures/h29/source-path";

// Byte-identical received H29 runtime. First executed before the H30 app delta.
vi.mock("@/demo/mock-adapter", () => import("./test-fixtures/h29/mock-adapter"));
vi.mock("./vertical-evaluation", () => import("./test-fixtures/h29/vertical-evaluation"));
vi.mock("./artifacts", () => import("./test-fixtures/h29/artifacts"));

it("H30 pre-delta: records and compares all six operational positions in A/B", async () => {
  const root = resolve(process.cwd(), "../../..");
  const baseline = JSON.parse(readFileSync(resolve(process.cwd(), "../docs/evidence/session-30/baseline.json"), "utf8"));
  for (const [path, digest] of Object.entries(baseline.files)) {
    expect(createHash("sha256").update(readFileSync(resolve(root, historicalH31Path(historicalH29Path(path))))).digest("hex"), path).toBe(digest);
  }
  const rows = [];
  for (const demoId of ["hospitality-family-adventure", "hospitality-family-adventure-costa"]) {
    const runtime = resolveDemo(demoId);
    const capture = (phase: string, snapshot: AppSnapshot) => {
      const supervision = snapshot.supervisionPerspective!;
      return {
        composition: demoId.endsWith("costa") ? "B" : "A", phase,
        checkpoint: snapshot.scenario!.checkpoint,
        availableActionId: snapshot.scenario!.availableActionId ?? null,
        state: snapshot.guestPerspective!.state,
        subjectStates: supervision.subjects.map((s) => ({ id: s.id, state: s.operationalState })),
        evidenceCount: supervision.evidence.length,
        subjectEvidenceCounts: supervision.subjects.map((s) => ({ id: s.id, count: s.evidenceCount })),
        sufficiency: supervision.sufficiency, claim: supervision.derivedClaim,
        message: snapshot.guestPerspective!.message,
        nextPresenterLabel: runtime.script!.steps.find((s) => s.action.actionId === snapshot.scenario!.availableActionId)?.presenterLabel ?? null,
        snapshot,
      };
    };
    rows.push(capture("initial", await runtime.provider.getSnapshot()));
    for (const step of runtime.script!.steps) rows.push(capture(step.action.actionId, await runtime.provider.executeAction(step.action)));
    rows.push(capture("reset", await runtime.provider.reset()));
  }
  expect(rows).toHaveLength(12);
  for (let i = 0; i < 6; i++) {
    for (const key of ["checkpoint", "availableActionId", "state", "subjectStates", "evidenceCount", "subjectEvidenceCounts", "sufficiency", "claim"] as const) {
      expect(rows[i][key]).toEqual(rows[i + 6][key]);
    }
  }
  // Required different narratives collapse on checkpoint, state and Evidence/evaluation.
  expect(rows[2].checkpoint).toBe(rows[3].checkpoint);
  expect(rows[2].state).toBe(rows[3].state);
  expect(rows[2].sufficiency).toBe(rows[3].sufficiency);
  expect(rows[2].evidenceCount).toBe(rows[3].evidenceCount);
  expect(rows[2].availableActionId).not.toBe(rows[3].availableActionId);
  expect(rows[1].subjectStates).toEqual(rows[2].subjectStates);
  expect(rows.slice(0, 5).map((r) => r.availableActionId)).toEqual(["enlist-p1", "discover-clue-a", "activate-p2", "discover-clue-b", null]);
  if (process.env.H30_MATRIX_PATH) writeFileSync(resolve(process.env.H30_MATRIX_PATH), JSON.stringify({
    capturedAt: new Date().toISOString(), method: "executed byte-identical received H29 provider before H30 application delta",
    nullMeaning: "absent existing affordance; not a runtime sentinel", rows,
  }, null, 2) + "\n", { flag: "wx" });
});

// S35: historical replay only; frozen S34 sources fill unresolved archive paths.
// Existing earlier mocks retain precedence; current cumulative coverage is H35.
vi.mock("./bootstrap", () => import("./test-fixtures/h34/bootstrap"));
