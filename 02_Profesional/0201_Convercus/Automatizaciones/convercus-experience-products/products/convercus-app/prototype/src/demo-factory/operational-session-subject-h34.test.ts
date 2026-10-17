/// <reference types="node" />
import { createHash } from "node:crypto";
import { writeFileSync } from "node:fs";
import { readHistoricalH34FileSync as readFileSync } from "./test-fixtures/h34/historical-read";
import { resolve } from "node:path";
import { act, createElement } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { afterEach, expect, it, vi } from "vitest";
import { App } from "@/app/App";
import { App as PreviousApp } from "./test-fixtures/h33/App";
import { MockDataAdapter } from "@/demo/mock-adapter";
import { defaultDemoCatalogs, resolveDemo, type DemoCatalogs } from "./bootstrap";
import type { AppSnapshot, DemoAction, DemoEnableAction, ResolvedDemoRuntime, SupervisionPerspectiveReadModel } from "./contracts";
import * as vertical from "./vertical-evaluation";
import * as joint from "./cross-subject-evidence-admissibility";

// Current App and actual provider/evaluators for every complete public journey.
// Only the explicitly isolated read-model observations substitute getSnapshot.
Object.assign(globalThis, { IS_REACT_ACT_ENVIRONMENT: true });
afterEach(() => { vi.restoreAllMocks(); document.body.innerHTML = ""; });
const clone = <T,>(value: T): T => structuredClone(value);
const sha = (value: string | Buffer) => createHash("sha256").update(value).digest("hex");
const evidenceDir = resolve(process.cwd(), "../docs/evidence");
const ids = ["hospitality-family-adventure", "hospitality-family-adventure-costa"];
const selector = '[aria-label="Sujetos existentes"] .adventure-guest';
const stableDOM = (element: HTMLElement): string => {
  const copy = element.cloneNode(true) as HTMLElement;
  for (const node of copy.querySelectorAll("*")) {
    const attributes = [...node.attributes].map(({ name, value }) => [name, value]).sort(([a], [b]) => a.localeCompare(b));
    for (const { name } of [...node.attributes]) node.removeAttribute(name);
    for (const [name, value] of attributes) node.setAttribute(name, value);
  }
  return copy.innerHTML;
};
const withoutSessionLabel = (html: string): string => {
  const element = document.createElement("div"); element.innerHTML = html;
  element.querySelectorAll('[aria-label="Evaluación compartida"] .system-list > div:first-child dt').forEach((n) => { n.textContent = ""; });
  return stableDOM(element);
};
type FactFrame = {
  phase: string; input?: DemoAction | DemoEnableAction; snapshot: AppSnapshot;
  verticalCalls: Parameters<typeof vertical.evaluateVerticalEvidence>[];
  verticalResults: vertical.VerticalEvaluationState[];
  jointEvaluationCalls: Parameters<typeof joint.evaluateCrossSubjectEvidenceSufficiency>[];
  jointEvaluationResults: ReturnType<typeof joint.evaluateCrossSubjectEvidenceSufficiency>[];
};
type Frame = FactFrame & {
  homeDOM: string; supervisionDOM: string; activityDOM: string;
  headings: string[]; diagnostics: string[]; sessionRepresentation: string[];
};
const facts = ({ phase, input, snapshot, verticalCalls, verticalResults, jointEvaluationCalls, jointEvaluationResults }: FactFrame): FactFrame => ({
  phase, ...(input ? { input } : {}), snapshot, verticalCalls, verticalResults, jointEvaluationCalls, jointEvaluationResults,
});

it("H34 historical S34 replay: existing session subject reference alone represents operational session across A/B and independent presentation perturbations", async () => {
  const baselineBytes = readFileSync(resolve(evidenceDir, "session-34/baseline.json"));
  const baseline = JSON.parse(baselineBytes.toString()) as { files: Record<string, string> };
  const projectRoot = resolve(process.cwd(), "../../..");
  const archived: Record<string, string> = {
    "products/convercus-app/prototype/src/app/App.tsx": "src/demo-factory/test-fixtures/h33/App.tsx",
    "products/convercus-app/prototype/src/demo-factory/operational-supervision-subject-h33.test.ts": "src/demo-factory/test-fixtures/h33/operational-supervision-subject-h33.test.ts.txt",
  };
  for (const [path, hash] of Object.entries(baseline.files)) {
    expect(sha(readFileSync(archived[path] ? resolve(process.cwd(), archived[path]) : resolve(projectRoot, path))), path).toBe(hash);
  }
  const appSource = readFileSync(resolve(process.cwd(), "src/app/App.tsx"), "utf8");
  const oldSource = readFileSync(resolve(process.cwd(), "src/demo-factory/test-fixtures/h33/App.tsx"), "utf8");
  const oldLabel = '<dt>Cuenta/sesión operativa</dt>';
  expect(oldSource.split(oldLabel)).toHaveLength(2);
  expect(appSource).toBe(oldSource.replace(oldLabel, '<dt>Sujeto de sesión operativa</dt>'));
  const h33 = JSON.parse(readFileSync(resolve(evidenceDir, "session-33/execution-trace.json"), "utf8")) as {
    controls: Array<{ original: { frames: Frame[]; resetFrame: Frame } }>;
    genericRegression: Array<{ demoId: string; current: { frames: Frame[]; resetFrame: Frame } }>;
  };
  const evaluate = vi.spyOn(vertical, "evaluateVerticalEvidence");
  const cross = vi.spyOn(joint, "evaluateCrossSubjectEvidenceSufficiency");
  const clear = () => { evaluate.mockClear(); cross.mockClear(); };
  const run = async (runtime: ResolvedDemoRuntime, component = App) => {
    expect(Object.getPrototypeOf(runtime.provider)).toBe(MockDataAdapter.prototype);
    const initial = await runtime.provider.getSnapshot(), family = Boolean(initial.guestPerspective);
    const container = document.createElement("div"); document.body.append(container);
    const root = createRoot(container);
    const execute = vi.spyOn(runtime.provider, "executeAction");
    const resetSpy = vi.spyOn(runtime.provider, "reset");
    const mount = async (key = "initial") => {
      await act(async () => root.render(createElement(MemoryRouter, {
        key, initialEntries: [family ? "/?demo=" + runtime.manifest.demoId : "/system"],
      }, createElement(component, { runtime }))));
    };
    const clickText = async (text: string) => {
      const target = [...container.querySelectorAll<HTMLElement>("a,button")].find((n) => n.textContent === text);
      expect(target, text).toBeDefined(); await act(async () => target!.click());
    };
    const capture = async (phase: string, input?: DemoAction | DemoEnableAction): Promise<Frame> => {
      const snapshot = await runtime.provider.getSnapshot();
      const fact: FactFrame = { phase, ...(input ? { input } : {}), snapshot,
        verticalCalls: clone(evaluate.mock.calls), verticalResults: clone(evaluate.mock.results.map((r) => r.value)),
        jointEvaluationCalls: clone(cross.mock.calls), jointEvaluationResults: clone(cross.mock.results.map((r) => r.value)),
      };
      let homeDOM: string, supervisionDOM: string, headings: string[] = [], diagnostics: string[] = [], sessionRepresentation: string[] = [];
      if (family) {
        const guest = snapshot.guestPerspective!;
        expect(container.querySelector("#adventure-title")?.textContent).toBe(guest.huntName);
        expect(container.querySelector(".adventure-heading .eyebrow")?.textContent).toBe("Mi aventura · " + runtime.brand.name);
        expect(container.querySelector(".adventure-heading h1 + p")?.textContent ?? null).toBe(runtime.script?.experimentalIntroductoryFraming || null);
        expect(container.querySelector(".adventure-message")?.textContent).toBe(guest.message);
        expect(container.querySelector(".adventure-session")?.textContent).toBe(guest.sessionLabel);
        expect(container.querySelector(".adventure-account")?.textContent).toBe("Cuenta de " + snapshot.member.name);
        const cards = [...container.querySelectorAll(".adventure-guest")];
        expect(cards.map((n) => n.querySelector("h3")?.textContent)).toEqual(guest.subjects.map((s) => s.label));
        cards.forEach((n, i) => expect(n.querySelector("p")?.textContent).toContain(guest.subjects[i].status));
        homeDOM = stableDOM(container);
        await clickText("Supervisión");
        const supervision = snapshot.supervisionPerspective!;
        const subjects = [...container.querySelectorAll(selector)];
        headings = subjects.map((n) => n.querySelector("h2")!.textContent!);
        diagnostics = subjects.map((n) => n.querySelector("p")!.textContent!);
        expect(headings).toEqual(supervision.subjects.map((s) => s.id));
        diagnostics.forEach((text, i) => {
          const s = supervision.subjects[i];
          expect(text).toBe(`${s.id} · exists: ${String(s.exists)} · ${s.operationalState} · Evidence: ${s.evidenceCount}`);
        });
        expect([...container.querySelectorAll(".system-list dt")].map((n) => n.textContent)).toEqual([
          component === App ? "Sujeto de sesión operativa" : "Cuenta/sesión operativa", "Criterio K", "Evidence recibida", "Admisibilidad conjunta", "Suficiencia K", "Afirmación derivada",
        ]);
        expect([...container.querySelectorAll(".system-list dd")].map((n) => n.textContent)).toEqual([
          supervision.sessionSubjectRef, "A AND (B OR C)", String(supervision.evidence.length), supervision.jointAdmissibility, supervision.sufficiency, supervision.derivedClaim,
        ]);
        expect([...container.querySelectorAll(".adventure-evidence li")].map((n) => n.textContent)).toEqual(
          supervision.evidence.map((e) => `${e.id} · ${e.subjectRefs.join(", ")} · ${e.provenance}`),
        );
        sessionRepresentation = [...container.querySelectorAll('[aria-label="Evaluación compartida"] .system-list > div:first-child dt, [aria-label="Evaluación compartida"] .system-list > div:first-child dd')].map((n) => n.textContent!);
        expect(sessionRepresentation).toEqual([component === App ? "Sujeto de sesión operativa" : "Cuenta/sesión operativa", supervision.sessionSubjectRef]);
        supervisionDOM = stableDOM(container);
      } else {
        expect(snapshot.supervisionPerspective).toBeUndefined();
        expect(snapshot.guestPerspective).toBeUndefined();
        expect(container.querySelector(selector)).toBeNull();
        expect(container.querySelector("#supervision-title")).toBeNull();
        supervisionDOM = stableDOM(container);
        await clickText("Inicio"); homeDOM = stableDOM(container);
        expect(container.querySelector(".adventure-heading")).toBeNull();
      }
      await clickText("Actividad");
      const activityDOM = stableDOM(container);
      expect([...container.querySelectorAll(".activity-item h3")].map((n) => n.textContent)).toEqual(snapshot.activity.map((a) => a.title));
      if (family) await clickText("Mi aventura"); else await mount("after-" + phase);
      expect(await runtime.provider.getSnapshot()).toEqual(snapshot);
      expect(evaluate.mock.calls).toEqual(fact.verticalCalls);
      expect(cross.mock.calls).toEqual(fact.jointEvaluationCalls);
      return { ...fact, homeDOM, supervisionDOM, activityDOM, headings, diagnostics, sessionRepresentation };
    };
    try {
      clear(); await mount(); const frames: Frame[] = [await capture("initial")];
      for (let count = 0; count < 8; count++) {
        const available = frames.at(-1)!.snapshot.scenario?.availableActionId;
        if (!available) break;
        const step = runtime.script!.steps.find((s) => s.action.actionId === available)!;
        const button = container.querySelector<HTMLButtonElement>(family ? ".adventure-next button" : ".system-panel button");
        expect(button?.textContent).toBe(step.presenterLabel); expect(button?.disabled).toBe(false);
        clear(); await act(async () => button!.click());
        expect(execute.mock.calls.at(-1)?.[0]).toEqual(step.action);
        frames.push(await capture(available, step.action));
      }
      expect(frames.at(-1)!.snapshot.scenario?.availableActionId).toBeUndefined();
      clear();
      if (family) await clickText("Reiniciar aventura"); else { await runtime.provider.reset(); await mount("reset"); }
      const resetFrame = await capture("reset");
      expect(resetFrame.snapshot).toEqual(initial); expect(resetSpy).toHaveBeenCalledOnce();
      expect(resetFrame.homeDOM).toBe(frames[0].homeDOM);
      expect(resetFrame.supervisionDOM).toBe(frames[0].supervisionDOM);
      expect(resetFrame.activityDOM).toBe(frames[0].activityDOM);
      return { component: component === App ? "ARCHIVED APP S34" : "ARCHIVED APP S33", demoId: runtime.manifest.demoId,
        scenario: clone(runtime.scenario), script: clone(runtime.script), brand: clone(runtime.brand),
        frames, resetFrame, executedActions: clone(execute.mock.calls.map(([action]) => action)),
      };
    } finally { await act(async () => root.unmount()); container.remove(); execute.mockRestore(); resetSpy.mockRestore(); }
  };
  type Run = Awaited<ReturnType<typeof run>>;
  const all = (r: Run) => [...r.frames, r.resetFrame];
  const compareApps = (current: Run, previous: Run) => {
    expect(all(current).map(facts)).toEqual(all(previous).map(facts));
    expect(current.executedActions).toEqual(previous.executedActions);
    expect(all(current).map((f) => f.homeDOM)).toEqual(all(previous).map((f) => f.homeDOM));
    expect(all(current).map((f) => f.activityDOM)).toEqual(all(previous).map((f) => f.activityDOM));
    expect(all(current).map((f) => withoutSessionLabel(f.supervisionDOM)))
      .toEqual(all(previous).map((f) => withoutSessionLabel(f.supervisionDOM)));
  };
  const controls = [];
  type Mutation = (c: DemoCatalogs, m: DemoCatalogs["manifests"][string]) => void;
  const mutations: Record<string, Mutation> = {
    subjects: (c, m) => { c.scripts[m.scriptRef!].subjectPresentations!.forEach((s, i) => { s.label = "Participante " + (i === 0 ? "Alfa" : "Beta"); }); },
    account: (c, m) => { c.fixtures[m.fixtureRef].member.name = "Cuenta H34"; },
    brand: (c, m) => { c.brands[m.brandRef].name = "Marca H34"; },
    intro: (c, m) => { c.scripts[m.scriptRef!].experimentalIntroductoryFraming = "Introducción H34 independiente."; },
    journey: (c, m) => { c.scripts[m.scriptRef!].experimentalJourneyPresentations!.forEach((j) => { j.message = "Narrativa H34 independiente."; }); },
    activity: (c, m) => { c.scripts[m.scriptRef!].steps.forEach((s) => { if (s.activityPresentation) s.activityPresentation = { title: "Activity H34", description: "Descripción H34" }; }); },
  };
  for (const [index, demoId] of ids.entries()) {
    const make = (mutation?: Mutation) => { const c = clone(defaultDemoCatalogs); mutation?.(c, c.manifests[demoId]); return resolveDemo(demoId, c); };
    const original = await run(make()), previousApp = await run(make(), PreviousApp);
    compareApps(original, previousApp);
    const old = h33.controls[index].original;
    expect(original.frames.map(facts)).toEqual(old.frames.map(facts));
    expect(facts(original.resetFrame)).toEqual(facts(old.resetFrame));
    expect(original.frames.map((f) => f.homeDOM)).toEqual(old.frames.map((f) => f.homeDOM));
    expect(original.resetFrame.homeDOM).toBe(old.resetFrame.homeDOM);
    expect(all(original).map((f) => withoutSessionLabel(f.supervisionDOM))).toEqual([...old.frames, old.resetFrame].map((f) => withoutSessionLabel(f.supervisionDOM)));
    expect(all(original).map((f) => f.activityDOM)).toEqual([...old.frames, old.resetFrame].map((f) => f.activityDOM));
    const variants: Record<string, Run> = {};
    for (const [name, mutation] of Object.entries(mutations)) {
      const variant = await run(make(mutation));
      expect(variant.scenario).toEqual(original.scenario);
      expect(all(variant).map((f) => f.sessionRepresentation)).toEqual(all(original).map((f) => f.sessionRepresentation));
      expect(variant.executedActions).toEqual(original.executedActions);
      expect(all(variant).map((f) => f.headings)).toEqual(all(original).map((f) => f.headings));
      expect(all(variant).map((f) => f.snapshot.supervisionPerspective)).toEqual(all(original).map((f) => f.snapshot.supervisionPerspective));
      const mask = (frame: FactFrame) => {
        const f = clone(facts(frame)), s = f.snapshot;
        if (name === "subjects") s.guestPerspective!.subjects.forEach((x) => { x.label = ""; });
        if (name === "account") { s.member.name = ""; s.guestPerspective!.sessionLabel = ""; }
        if (name === "journey") s.guestPerspective!.message = "";
        if (name === "activity") s.activity.forEach((x) => { x.title = ""; x.description = ""; });
        return f;
      };
      expect(all(variant).map(mask)).toEqual(all(original).map(mask));
      if (name === "subjects") expect(variant.frames[0].snapshot.guestPerspective!.subjects.map((s) => s.label)).toEqual(["Participante Alfa", "Participante Beta"]);
      if (name === "account") expect(variant.frames[0].snapshot.guestPerspective!.sessionLabel).toBe("Cuenta de Cuenta H34");
      if (name === "brand" || name === "intro") expect(variant.frames[0].homeDOM).not.toBe(original.frames[0].homeDOM);
      if (name === "journey") expect(variant.frames[1].snapshot.guestPerspective!.message).toBe("Narrativa H34 independiente.");
      if (name === "activity") expect(variant.frames[2].snapshot.activity[0].title).toBe("Activity H34");
      variants[name] = variant;
    }
    // State, Evidence and evaluation change via public actions; the session reference stays fixed.
    expect(all(original).map((f) => f.sessionRepresentation)).toEqual(Array.from({ length: 6 }, () => ["Sujeto de sesión operativa", "subject-p1"]));
    expect(original.frames[0].snapshot.supervisionPerspective!.derivedClaim).toBe("not-produced");
    expect(original.frames.at(-1)!.snapshot.supervisionPerspective!.derivedClaim).toBe("established");
    expect(original.frames.map((f) => f.headings)).toEqual(Array.from({ length: 5 }, () => ["subject-p1", "subject-p2"]));
    expect(original.frames.map((f) => f.snapshot.supervisionPerspective!.subjects.map((s) => s.operationalState))).toEqual([
      ["not-enlisted", "not-enabled"], ["enabled", "not-enabled"], ["enabled", "not-enabled"], ["enabled", "enabled"], ["enabled", "enabled"],
    ]);
    expect(original.frames.map((f) => f.snapshot.supervisionPerspective!.subjects.map((s) => s.evidenceCount))).toEqual([[0, 0], [0, 0], [1, 0], [1, 0], [1, 1]]);
    controls.push({ composition: index === 0 ? "A" : "B", original, previousApp, variants });
  }
  expect(all(controls[0].original).map((f) => f.headings)).toEqual(all(controls[1].original).map((f) => f.headings));
  expect(controls[0].original.frames[0].snapshot.guestPerspective!.subjects.map((s) => s.label)).not.toEqual(controls[1].original.frames[0].snapshot.guestPerspective!.subjects.map((s) => s.label));

  expect(all(controls[0].original).map((f) => f.sessionRepresentation)).toEqual(all(controls[1].original).map((f) => f.sessionRepresentation));

  // Isolated composition/projector transport observations: never execute actions.
  const observation = async (name: string, runtime: ResolvedDemoRuntime, override?: SupervisionPerspectiveReadModel) => {
    const snapshot = await runtime.provider.getSnapshot();
    if (override) snapshot.supervisionPerspective = override;
    const get = override ? vi.spyOn(runtime.provider, "getSnapshot").mockResolvedValue(snapshot) : undefined;
    const execute = vi.spyOn(runtime.provider, "executeAction");
    const container = document.createElement("div"); document.body.append(container); const root = createRoot(container);
    clear();
    try {
      await act(async () => root.render(createElement(MemoryRouter, { initialEntries: ["/system"] }, createElement(App, { runtime }))));
      const sessionRepresentation = [...container.querySelectorAll('[aria-label="Evaluación compartida"] .system-list > div:first-child dt, [aria-label="Evaluación compartida"] .system-list > div:first-child dd')].map((n) => n.textContent!);
      expect(sessionRepresentation).toEqual(["Sujeto de sesión operativa", snapshot.supervisionPerspective!.sessionSubjectRef]);
      expect([...container.querySelectorAll(selector + " h2")].map((n) => n.textContent)).toEqual(snapshot.supervisionPerspective!.subjects.map((s) => s.id));
      expect(execute).not.toHaveBeenCalled(); expect(evaluate).not.toHaveBeenCalled(); expect(cross).not.toHaveBeenCalled();
      expect(await runtime.provider.getSnapshot()).toEqual(snapshot);
      return { name, scope: override ? "ISOLATED PROJECTOR / READ MODEL; substituted getSnapshot" : "ISOLATED COMPOSITION OBSERVATION; harness-only Scenario copy; real provider; no actions", scenario: clone(runtime.scenario), snapshot, sessionRepresentation, executedActions: clone(execute.mock.calls), dom: stableDOM(container) };
    } finally { await act(async () => root.unmount()); container.remove(); get?.mockRestore(); execute.mockRestore(); }
  };
  const sessionVariations = [];
  for (const demoId of ids) {
    const observations = [];
    for (const reference of ["subject-p1", "subject-p2"]) {
      const c = clone(defaultDemoCatalogs), m = c.manifests[demoId];
      c.scenarios[m.scenarioRef!].operationalSessionSubjectRef = reference;
      const runtime = resolveDemo(demoId, c);
      expect(runtime.scenario).toEqual({ ...defaultDemoCatalogs.scenarios[m.scenarioRef!], operationalSessionSubjectRef: reference });
      const result = await observation(reference, runtime);
      expect(result.snapshot.supervisionPerspective!.sessionSubjectRef).toBe(reference);
      observations.push(result);
    }
    const normalized = observations.map((o) => { const s = clone(o.snapshot); s.supervisionPerspective!.sessionSubjectRef = ""; return s; });
    expect(normalized[0]).toEqual(normalized[1]);
    sessionVariations.push({ demoId, observations, reachableJourney: "NOT CLAIMED; subject-p2 variant conflicts with existing enlist guard; no actions executed" });
  }
  const baseRuntime = resolveDemo(ids[0]);
  const initialSnapshot = await baseRuntime.provider.getSnapshot();
  const opaqueRef = "opaque:session-subject/X";
  const opaqueSP = vertical.projectSupervisionPerspective(
    { evidence: [], jointAdmissibility: "cannot-currently-establish", sufficiency: "not-attempted" },
    baseRuntime.scenario!.subjects, baseRuntime.scenario!.initialSubjectStates, opaqueRef);
  expect(opaqueSP).toEqual({ ...initialSnapshot.supervisionPerspective, sessionSubjectRef: opaqueRef });
  const opaque = await observation("opaque reference only as projector argument", baseRuntime, opaqueSP);
  expect(opaque.sessionRepresentation).toEqual(["Sujeto de sesión operativa", opaqueRef]);

  const generic = [];
  for (const old of h33.genericRegression) {
    const current = await run(resolveDemo(old.demoId)), previous = await run(resolveDemo(old.demoId), PreviousApp);
    compareApps(current, previous);
    expect(all(current).map((f) => f.supervisionDOM)).toEqual(all(previous).map((f) => f.supervisionDOM));
    expect(current.frames.map(facts)).toEqual(old.current.frames.map(facts));
    expect(facts(current.resetFrame)).toEqual(facts(old.current.resetFrame));
    generic.push({ demoId: old.demoId, current, previous });
  }
  expect(generic.map((g) => g.demoId).sort()).toEqual(["hospitality-stay", "retail-baseline"]);
  const trace = {
    session: 34, recordedAt: new Date().toISOString(), verdict: "SUPPORTED WITH QUALIFICATION",
    method: "Historical S34 App/runtime createRoot/MemoryRouter/jsdom; public action clicks; real adapter; transparent evaluator spies; archived S33 App compared separately at every phase",
    baselineSha256: sha(baselineBytes), appSha256: sha(appSource),
    harnessSha256: sha(readFileSync(resolve(process.cwd(), "src/demo-factory/operational-session-subject-h34.test.ts"))),
    controls, sessionVariations, opaqueReadModelObservation: opaque, genericRegression: generic,
    domIntegrationVerification: "EXECUTED", browserVisualValidation: "NOT EXECUTED",
    noNewRelation: "SUFFICIENT for neutral diagnostic identification within tested scope",
    accountClaim: "REMOVED AS UNSUPPORTED; no account/viewer/authentication relation introduced",
    recurringPresentationPressure: "QUALIFIED BY H34 / NOT PROMOTED", nextPressure: "OBSERVED / NOT SELECTED; H35 NOT OPENED",
  };
  if (process.env.H34_REPLAY_RECORD_PATH) writeFileSync(resolve(process.env.H34_REPLAY_RECORD_PATH), JSON.stringify(trace, null, 2) + "\n", { flag: "wx" });
}, 60000);

// S35: historical replay only; frozen S34 sources fill unresolved archive paths.
// Existing earlier mocks retain precedence; current cumulative coverage is H35.
vi.mock("./bootstrap", () => import("./test-fixtures/h34/bootstrap"));
vi.mock("@/demo/mock-adapter", () => import("./test-fixtures/h34/mock-adapter"));
vi.mock("./vertical-evaluation", () => import("./test-fixtures/h34/vertical-evaluation"));

// S37: preserve historical H25 descriptions; current coverage is H37.
vi.mock("./artifacts", () => import("./test-fixtures/h36/artifacts"));
