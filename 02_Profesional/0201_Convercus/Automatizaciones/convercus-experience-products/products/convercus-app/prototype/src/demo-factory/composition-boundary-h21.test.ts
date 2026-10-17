/// <reference types="node" />
import { materialBaselineEntries } from "./test-fixtures/h38/material-baseline";
import { historicalH31Path } from "./test-fixtures/h31/source-path";
import { historicalH29Path } from "./test-fixtures/h29/source-path";
import { createHash } from "node:crypto";
import { writeFileSync } from "node:fs";
import { readHistoricalH34FileSync as readFileSync } from "./test-fixtures/h34/historical-read";
import { resolve } from "node:path";
import { describe, expect, it, vi } from "vitest";
import { resolveDemo } from "./bootstrap";
import { historicalH24Path } from "./test-fixtures/h24/source-path";
import type { DemoScript, ResolvedDemoRuntime } from "./contracts";

// H22 changes the live selector. Replay H21 with its byte-identical archived
// adapter through the unchanged resolver; never reinterpret the historical trace.
vi.mock("@/demo/mock-adapter", () => import("./test-fixtures/h21/mock-adapter"));
// H23 changes context integration; this exact H21/H22 integration stays frozen.
vi.mock("@/demo-factory/vertical-evaluation", () => import("./test-fixtures/h22/vertical-evaluation"));
// H25 adds Script presentation; replay the pre-H25 resolver and composition.
vi.mock("./bootstrap", () => import("./test-fixtures/h24/bootstrap"));

// Experimental observation of a frozen baseline, not a test claiming B works.
// There are deliberately no executeAction/reset calls after the first falsifier.
const sha256 = (value: string | Buffer) => createHash("sha256").update(value).digest("hex");
const root = resolve(process.cwd(), "../../..");
const baseline = JSON.parse(readFileSync(resolve(process.cwd(), "../docs/session-21-frozen-baseline.json"), "utf8")) as {
  frozenBaselineSha256: string;
  sharedFiles: Record<string, string>;
  protectedFiles: Record<string, string>;
  bootstrapBeforeSha256: string;
};

function actionSemantics(script: DemoScript) {
  return script.steps.map(({ expectedCheckpoint, action }) => ({
    expectedCheckpoint,
    actionId: action.actionId,
    type: action.type,
    ...( "evidence" in action
      ? { evidenceType: action.evidence.type, subjects: action.evidence.subjects,
          reliability: action.evidence.reliability, source: action.evidence.source }
      : { operation: action.operation }),
  }));
}

function composition(runtime: ResolvedDemoRuntime) {
  return {
    demoId: runtime.manifest.demoId,
    brand: runtime.brand.name,
    brandRef: runtime.manifest.brandRef,
    fixtureRef: runtime.manifest.fixtureRef,
    scenarioRef: runtime.manifest.scenarioRef,
    scenarioId: runtime.scenario?.id,
    scriptRef: runtime.manifest.scriptRef,
    experienceRef: runtime.scenario?.experienceRef,
    contexts: runtime.scenario?.contexts,
    subjects: runtime.scenario?.subjects,
    sessionSubjectRef: runtime.scenario?.operationalSessionSubjectRef,
    initialSubjectStates: runtime.scenario?.initialSubjectStates,
  };
}

describe("H21 frozen-baseline falsification experiment", () => {
  it("records the first material falsifier and stops at B's initial read-model boundary", async () => {
    for (const [path, hash] of materialBaselineEntries("H21", { ...baseline.sharedFiles, ...baseline.protectedFiles })) {
      const frozenPath = path === "products/convercus-app/prototype/src/demo/mock-adapter.ts"
        ? "products/convercus-app/prototype/src/demo-factory/test-fixtures/h21/mock-adapter.ts"
        : path === "products/convercus-app/prototype/src/demo-factory/vertical-evaluation.ts"
          ? "products/convercus-app/prototype/src/demo-factory/test-fixtures/h22/vertical-evaluation.ts"
          : historicalH24Path(path);
      expect(sha256(readFileSync(resolve(root, historicalH31Path(historicalH29Path(frozenPath))))), `Frozen file: ${path}`).toBe(hash);
    }
    const bootstrap = readFileSync(resolve(root, historicalH31Path(historicalH29Path(historicalH24Path("products/convercus-app/prototype/src/demo-factory/bootstrap.ts")))), "utf8");
    const withoutBRegistration = bootstrap
      .replace('import { costaFixture, hospitalityFixture, retailFixture } from "./fixtures";',
        'import { hospitalityFixture, retailFixture } from "./fixtures";')
      .replace('    [costaFixture.id]: costaFixture,\n', "");
    expect(sha256(withoutBRegistration)).toBe(baseline.bootstrapBeforeSha256);

    // Stage 1: actual existing resolver. It also constructs the providers.
    const a = resolveDemo("hospitality-family-adventure");
    const b = resolveDemo("hospitality-family-adventure-costa");
    expect(a).not.toBe(b);
    expect(a.manifest).not.toBe(b.manifest);
    expect(a.experience).toBe(b.experience);
    expect(a.scenario!.experienceRef).toBe(b.scenario!.experienceRef);
    for (const key of ["brandRef", "fixtureRef", "scenarioRef", "scriptRef"] as const) {
      expect(a.manifest[key]).not.toBe(b.manifest[key]);
    }
    expect(a.brand.name).toBe("Aurora Stay");
    expect(b.brand.name).toBe("Costa Clara Resort");
    expect(b.scenario!.id).toBe("family-adventure-costa");
    expect(b.scenario!.id).not.toBe(a.scenario!.id);
    expect(b.scenario!.contexts).toEqual([
      { type: "property", id: "costa-clara-resort" },
      { type: "booking", id: "CC-205" },
      { type: "stay", id: "stay-CC-205" },
    ]);
    expect(b.scenario!.contexts.every(({ id }) => !a.scenario!.contexts.some((context) => context.id === id))).toBe(true);
    expect(b.scenario!.subjects).toEqual(a.scenario!.subjects);
    expect(b.scenario!.initialSubjectStates).toEqual(a.scenario!.initialSubjectStates);
    expect(b.scenario!.operationalSessionSubjectRef).toBe("subject-p1");
    expect(b.scenario!.actions).toEqual(a.scenario!.actions);
    expect(b.scenario!.checkpoints).toEqual(a.scenario!.checkpoints);
    expect(actionSemantics(b.script!)).toEqual(actionSemantics(a.script!));

    // Stage 2: distinct instances of the same machinery, no action has run.
    expect(a.provider).not.toBe(b.provider);
    expect(Object.getPrototypeOf(a.provider)).toBe(Object.getPrototypeOf(b.provider));
    const initialA = await a.provider.getSnapshot();
    const initialB = await b.provider.getSnapshot();
    expect(initialA.member.name).toBe("Lucía");
    expect(initialB.member.name).toBe("Inés");
    expect(initialA.scenario).toEqual({ checkpoint: "ready", availableActionId: "enlist-p1" });
    expect(initialB.scenario).toEqual(initialA.scenario);
    expect(initialA.guestPerspective).toBeDefined();
    expect(initialA.supervisionPerspective).toBeDefined();

    const missing = ["guestPerspective", "supervisionPerspective"] as const;
    const absent = missing.filter((key) => initialB[key] === undefined);
    if (absent.length > 0) {
      const observation = {
        experiment: "H21 — Composition Boundary / Factory Reusability",
        recordedAt: new Date().toISOString(),
        frozenBaselineSha256: baseline.frozenBaselineSha256,
        sharedFilesUnchanged: true,
        bootstrapBehaviorUnchanged: true,
        compositionA: composition(a),
        compositionB: composition(b),
        resolvedRuntimesDistinct: a !== b,
        providersDistinct: a.provider !== b.provider,
        providerImplementationSame: Object.getPrototypeOf(a.provider) === Object.getPrototypeOf(b.provider),
        experienceSame: a.experience === b.experience,
        inputAction: "resolveDemo(B).provider.getSnapshot()",
        expected: "Initial guest and supervision perspectives for B, P1 not-enlisted, P2 not-enabled, no Evidence and no produced claim.",
        observed: { absentReadModels: absent, initialA, initialB },
        lastSuccessfulBoundary: "Both compositions resolve; distinct providers of the same implementation return generic initial snapshots with their own fixture data and initial action.",
        firstFailingBoundary: "B initial runtime snapshot -> guest/supervision read models",
        responsibleFile: "prototype/src/demo/mock-adapter.ts:81",
        guard: 'scenario?.id === "family-adventure"',
        actionsExecuted: [],
        resetCalls: 0,
        stoppedBefore: "enlist P1 / Evidence / evaluation / presentation / interleaved isolation",
        isolationResult: "NOT REACHED beyond distinct provider instances",
        contextIntegrityResult: "DECLARED CONTEXTS DISTINCT; EVALUATION CONTEXT NOT REACHED",
        contentLeakageResult: "INITIAL GENERIC FIXTURE DATA DISTINCT; GUEST/SUPERVISION PRESENTATION NOT REACHED",
        executionConfirmed: ["L2: projection selection gate"],
        inspectionOnly: ["L1", "L3", "L4", "L5", "L2: evaluation selection gate at executeAction"],
        verdict: "FALSIFIED",
        stop: "FIRST MATERIAL FALSIFIER; NO SHARED MODIFICATION",
      };
      if (process.env.H21_RECORD_PATH) {
        writeFileSync(resolve(process.env.H21_RECORD_PATH), JSON.stringify(observation, null, 2) + "\n");
      }
      console.info("H21: FALSIFIED; L2 confirmed at initial projections; STOP before any executeAction/reset.");
      expect(absent).toEqual(["guestPerspective", "supervisionPerspective"]);
      return;
    }
    throw new Error("Frozen-baseline observation changed: no initial falsifier. Review the protocol before advancing this harness.");
  });
});

// S35: historical replay only; frozen S34 sources fill unresolved archive paths.
// Existing earlier mocks retain precedence; current cumulative coverage is H35.
