/// <reference types="node" />
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { act, createElement } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { afterEach, expect, it, vi } from "vitest";
import { App } from "@/app/App";
import { MockDataAdapter, projectSnapshot } from "@/demo/mock-adapter";
import { defaultDemoCatalogs, resolveDemo, type DemoCatalogs } from "./bootstrap";
import type { AppSnapshot, DemoAction, DemoEnableAction, ResolvedDemoRuntime } from "./contracts";
import * as vertical from "./vertical-evaluation";
import * as joint from "./cross-subject-evidence-admissibility";

// Current App and actual provider/evaluators for every complete public journey.
// No provider/getSnapshot substitution or historical runtime in this harness.
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

it("H37 current App: reduce unsupported Activity attribution without new relations or factual changes", async () => {
  const baselineBytes = readFileSync(resolve(evidenceDir, "session-37/baseline.json"));
  const baseline = JSON.parse(baselineBytes.toString()) as { files: Record<string, string> };
  const sourcePaths = ["src/app/App.tsx", "src/demo-factory/contracts.ts", "src/demo-factory/bootstrap.ts",
    "src/demo/mock-adapter.ts", "src/demo-factory/vertical-evaluation.ts", "src/demo-factory/fixtures.ts",
    "src/demo-factory/manifests.ts", "src/demo-factory/cross-subject-evidence-admissibility.ts",
    "src/demo-factory/evidence-sufficiency.ts", "vite.config.ts", "package.json", "package-lock.json"];
  const sourceHashes = Object.fromEntries(sourcePaths.map((p) => [p, sha(readFileSync(resolve(process.cwd(), p)))]));
  for (const [path, hash] of Object.entries(sourceHashes)) {
    expect(hash, path).toBe(baseline.files["products/convercus-app/prototype/" + path]);
  }
  const replacements: Record<string, Array<[string, string]>> = {
    "artifacts.ts": [
      ["Hallazgo aportado por ti.", "Hallazgo registrado."],
      ["Hallazgo atribuido al huésped 2, registrado desde tu cuenta.", "Hallazgo atribuido al huésped 2."],
    ],
    "costa-artifacts.ts": [
      ["Hallazgo aportado por Inés.", "Hallazgo registrado."],
      ["Hallazgo atribuido a Mateo, registrado desde la cuenta de Inés.", "Hallazgo atribuido a Mateo."],
    ],
  };
  for (const [file, edits] of Object.entries(replacements)) {
    const old = readFileSync(resolve(process.cwd(), "src/demo-factory/test-fixtures/h36/" + file + ".txt"), "utf8");
    expect(sha(old)).toBe(baseline.files["products/convercus-app/prototype/src/demo-factory/" + file]);
    let expected = old;
    for (const [before, after] of edits) {
      expect(expected.split('description: "' + before + '"')).toHaveLength(2);
      expected = expected.replace('description: "' + before + '"', 'description: "' + after + '"');
    }
    const current = readFileSync(resolve(process.cwd(), "src/demo-factory/" + file), "utf8");
    expect(current).toBe(expected); // Exactly four scalar edits; no structural or relation delta.
    sourceHashes["src/demo-factory/" + file] = sha(current);
  }
  const h35Bytes = readFileSync(resolve(evidenceDir, "session-35/execution-trace.json"));
  const h35 = JSON.parse(h35Bytes.toString()) as {
    controls: Array<{ original: { frames: Frame[]; resetFrame: Frame } }>;
    genericRegression: Array<{ demoId: string; current: { frames: Frame[]; resetFrame: Frame } }>;
  };
  const evaluate = vi.spyOn(vertical, "evaluateVerticalEvidence");
  const cross = vi.spyOn(joint, "evaluateCrossSubjectEvidenceSufficiency");
  const clear = () => { evaluate.mockClear(); cross.mockClear(); };
  const run = async (runtime: ResolvedDemoRuntime) => {
    expect(Object.getPrototypeOf(runtime.provider)).toBe(MockDataAdapter.prototype);
    const initial = await runtime.provider.getSnapshot(), family = Boolean(initial.guestPerspective);
    const container = document.createElement("div"); document.body.append(container);
    const root = createRoot(container);
    const execute = vi.spyOn(runtime.provider, "executeAction");
    const resetSpy = vi.spyOn(runtime.provider, "reset");
    const mount = async (key = "initial") => {
      await act(async () => root.render(createElement(MemoryRouter, {
        key, initialEntries: [family ? "/?demo=" + runtime.manifest.demoId : "/system"],
      }, createElement(App, { runtime }))));
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
        expect(guest.huntName).toBe(runtime.experience!.name);
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
          "Sujeto de sesión operativa", "Criterio K", "Evidence recibida", "Admisibilidad conjunta", "Suficiencia K", "Afirmación derivada",
        ]);
        expect([...container.querySelectorAll(".system-list dd")].map((n) => n.textContent)).toEqual([
          supervision.sessionSubjectRef, "A AND (B OR C)", String(supervision.evidence.length), supervision.jointAdmissibility, supervision.sufficiency, supervision.derivedClaim,
        ]);
        expect([...container.querySelectorAll(".adventure-evidence li")].map((n) => n.textContent)).toEqual(
          supervision.evidence.map((e) => `${e.id} · ${e.subjectRefs.join(", ")} · ${e.provenance}`),
        );
        sessionRepresentation = [...container.querySelectorAll('[aria-label="Evaluación compartida"] .system-list > div:first-child dt, [aria-label="Evaluación compartida"] .system-list > div:first-child dd')].map((n) => n.textContent!);
        expect(sessionRepresentation).toEqual(["Sujeto de sesión operativa", supervision.sessionSubjectRef]);
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
      const rows = [...container.querySelectorAll(".activity-item")];
      expect(rows).toHaveLength(snapshot.activity.length);
      rows.forEach((row, i) => {
        expect(row.querySelector(".activity-item__content > p")?.textContent).toBe(snapshot.activity[i].description);
        expect(row.querySelector("time")?.getAttribute("dateTime")).toBe(snapshot.activity[i].occurredAt);
        expect(row.querySelector("time")?.textContent).toBe(snapshot.activity[i].displayDate);
      });
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
      return { component: "CURRENT APP H37", demoId: runtime.manifest.demoId,
        experience: clone(runtime.experience), scenario: clone(runtime.scenario), script: clone(runtime.script), brand: clone(runtime.brand),
        frames, resetFrame, executedActions: clone(execute.mock.calls.map(([action]) => action)),
      };
    } finally { await act(async () => root.unmount()); container.remove(); execute.mockRestore(); resetSpy.mockRestore(); }
  };
  type Run = Awaited<ReturnType<typeof run>>;
  const all = (r: { frames: Frame[]; resetFrame: Frame }) => [...r.frames, r.resetFrame];
  const controls = [];
  const sessionObservations = [];
  const occurrenceNegatives: Array<{
    demoId: string; name: string; action: DemoAction | DemoEnableAction;
    error: string | undefined; before: AppSnapshot; after: AppSnapshot;
  }> = [];
  type Mutation = (c: DemoCatalogs, m: DemoCatalogs["manifests"][string]) => void;
  const descriptionMutation = (description: string): Mutation => (c, m) => {
    c.scripts[m.scriptRef!].steps.forEach((s) => { if (s.activityPresentation) s.activityPresentation.description = description; });
  };
  const mutations: Record<string, Mutation> = {
    account: (c, m) => { c.fixtures[m.fixtureRef].member.name = "Cuenta X H37"; },
    subjects: (c, m) => { c.scripts[m.scriptRef!].subjectPresentations!.forEach((s, i) => { s.label = "Etiqueta H37 " + (i + 1); }); },
    neutralX: descriptionMutation("Hallazgo registrado. Texto situado X."),
    neutralY: descriptionMutation("Hallazgo registrado. Texto situado Y."),
    contradiction: descriptionMutation("No se ha registrado ningún hallazgo."),
  };
  const activityContent = (f: Frame) => {
    const el = document.createElement("div"); el.innerHTML = f.activityDOM;
    return el.querySelector(".activity-list")?.outerHTML;
  };
  for (const [index, demoId] of ids.entries()) {
    const make = (mutation?: Mutation) => { const c = clone(defaultDemoCatalogs); mutation?.(c, c.manifests[demoId]); return resolveDemo(demoId, c); };
    const original = await run(make()), old = h35.controls[index].original;
    const selected = new Set(original.executedActions.flatMap((a) => "evidence" in a ? [a.evidence.id] : []));
    const mask = (frame: FactFrame, name = "") => {
      const f = clone(facts(frame));
      f.snapshot.activity.forEach((a) => { if (selected.has(a.id)) a.description = ""; });
      if (name === "account") { f.snapshot.member.name = ""; f.snapshot.guestPerspective!.sessionLabel = ""; }
      if (name === "subjects") f.snapshot.guestPerspective!.subjects.forEach((s) => { s.label = ""; });
      return f;
    };
    const maskDOM = (frame: Frame) => {
      const el = document.createElement("div"); el.innerHTML = frame.activityDOM;
      [...el.querySelectorAll(".activity-item")].forEach((n, i) => {
        if (selected.has(frame.snapshot.activity[i].id)) n.querySelector(".activity-item__content > p")!.textContent = "";
      });
      return stableDOM(el);
    };
    expect(original.frames.map((f) => f.phase)).toEqual(["initial", "enlist-p1", "discover-clue-a", "activate-p2", "discover-clue-b"]);
    expect(all(original).map((f) => mask(f))).toEqual(all(old).map((f) => mask(f)));
    expect(all(original).map((f) => f.homeDOM)).toEqual(all(old).map((f) => f.homeDOM));
    expect(all(original).map((f) => f.supervisionDOM)).toEqual(all(old).map((f) => f.supervisionDOM));
    expect(all(original).map(maskDOM)).toEqual(all(old).map(maskDOM));
    const expectedDescriptions = ["Hallazgo registrado.", index ? "Hallazgo atribuido a Mateo." : "Hallazgo atribuido al huésped 2."];
    expect(original.script!.steps.flatMap((s) => s.activityPresentation ? [s.activityPresentation.description] : [])).toEqual(expectedDescriptions);
    expect(original.frames[2].snapshot.activity[0].description).toBe(expectedDescriptions[0]);
    expect(original.frames[4].snapshot.activity[0].description).toBe(expectedDescriptions[1]);
    expect(original.frames[2].activityDOM).not.toBe(old.frames[2].activityDOM);
    expect(original.frames[4].activityDOM).not.toBe(old.frames[4].activityDOM);
    for (const description of expectedDescriptions) {
      expect(description).not.toMatch(/por ti|tu cuenta|cuenta de|desde.*cuenta|registrado por|aportado por|ejecutad|realizado por/i);
    }
    // Lexical check supplements, never replaces, pre/post semantic claim analysis.
    const initialCount = original.frames[0].snapshot.activity.length;
    expect(original.frames.map((f) => f.snapshot.activity.length)).toEqual([initialCount, initialCount, initialCount + 1, initialCount + 1, initialCount + 2]);
    expect(original.resetFrame.snapshot.activity).toEqual(original.frames[0].snapshot.activity);
    expect(original.frames.map((f) => f.snapshot.supervisionPerspective!.evidence.map((e) => e.subjectRefs))).toEqual([
      [], [], [["subject-p1"]], [["subject-p1"]], [["subject-p1"], ["subject-p2"]],
    ]);
    expect(original.frames[4].snapshot.supervisionPerspective!.derivedClaim).toBe("established");
    // Original evaluator calls include full Evidence, context, premise, criterion K and derived claim.
    const variants: Record<string, Run> = {};
    for (const [name, mutation] of Object.entries(mutations)) {
      const variant = await run(make(mutation));
      expect(variant.executedActions).toEqual(original.executedActions);
      expect(variant.scenario).toEqual(original.scenario);
      expect(variant.experience).toEqual(original.experience);
      expect(variant.brand).toEqual(original.brand);
      expect(all(variant).map((f) => mask(f, name))).toEqual(all(original).map((f) => mask(f, name)));
      expect(all(variant).map((f) => f.snapshot.supervisionPerspective)).toEqual(all(original).map((f) => f.snapshot.supervisionPerspective));
      const stripDescriptions = (script: NonNullable<Run["script"]>) => {
        const copy = clone(script);
        copy.steps.forEach((s) => { if (s.activityPresentation) s.activityPresentation.description = ""; });
        return copy;
      };
      if (name === "account" || name === "subjects") {
        expect(all(variant).map((f) => f.snapshot.activity)).toEqual(all(original).map((f) => f.snapshot.activity));
        expect(all(variant).map(activityContent)).toEqual(all(original).map(activityContent));
        if (name === "account") {
          expect(variant.script).toEqual(original.script);
          expect(variant.frames[0].snapshot.guestPerspective!.sessionLabel).toBe("Cuenta de Cuenta X H37");
        } else {
          expect(variant.frames[0].snapshot.guestPerspective!.subjects.map((s) => s.label)).toEqual(["Etiqueta H37 1", "Etiqueta H37 2"]);
          expect(variant.frames[4].snapshot.activity[0].description).toBe(expectedDescriptions[1]);
        }
      } else {
        expect(stripDescriptions(variant.script!)).toEqual(stripDescriptions(original.script!));
        expect(all(variant).map((f) => f.homeDOM)).toEqual(all(original).map((f) => f.homeDOM));
        expect(all(variant).map((f) => f.supervisionDOM)).toEqual(all(original).map((f) => f.supervisionDOM));
        expect(all(variant).map(maskDOM)).toEqual(all(original).map(maskDOM));
        expect(variant.frames[2].activityDOM).not.toBe(original.frames[2].activityDOM);
      }
      variants[name] = variant;
    }
    expect(variants.neutralX.frames[2].snapshot.activity[0].description).not.toBe(variants.neutralY.frames[2].snapshot.activity[0].description);
    expect(all(variants.neutralX).map((f) => mask(f))).toEqual(all(variants.neutralY).map((f) => mask(f)));
    expect(variants.contradiction.frames[4].snapshot.activity[0].description).toBe("No se ha registrado ningún hallazgo.");
    expect(variants.contradiction.frames[4].snapshot.supervisionPerspective!.sufficiency).toBe("established");
    controls.push({ composition: index ? "B" : "A", original, variants, baselineComparison: "Only selected Activity.description differs from immutable S35; complete fact/evaluator frames and Home/Supervision DOM equal" });

    // Negative occurrence controls use the current public provider, not edited snapshots.
    const runtime = make(), steps = runtime.script!.steps;
    const reject = async (name: string, action: DemoAction | DemoEnableAction) => {
      const before = await runtime.provider.getSnapshot(); clear();
      let error: string | undefined;
      try { await runtime.provider.executeAction(action); } catch (e) { error = (e as Error).message; }
      expect(error, name).toBeDefined();
      const after = await runtime.provider.getSnapshot();
      expect(after).toEqual(before);
      expect(evaluate).not.toHaveBeenCalled(); expect(cross).not.toHaveBeenCalled();
      occurrenceNegatives.push({ demoId, name, action: clone(action), error, before, after });
    };
    const clueA = clone(steps[1].action) as DemoAction, clueB = clone(steps[3].action) as DemoAction;
    await reject("subject not enlisted", clueA);
    await reject("wrong checkpoint", clueB);
    await reject("unknown action", { ...clueA, actionId: "unknown-h37" });
    await runtime.provider.executeAction(steps[0].action);
    const badSubject = clone(clueA); badSubject.evidence.subjects[0].id = "subject-p2";
    await reject("incompatible subject attribution", badSubject);
    const badType = clone(clueA); badType.evidence.type = "treasure_hunt.marker-b";
    await reject("incompatible Evidence type", badType);
    const badInterpretation = clone(clueA);
    badInterpretation.evidence.interpretation = { id: "probe-h37", type: "unsupported", experienceRef: runtime.scenario!.experienceRef };
    await reject("interpretation not admitted", badInterpretation);
    await runtime.provider.executeAction(clueA);
    await reject("subject-p2 not enabled", clueB);
    await runtime.provider.executeAction(steps[2].action);
    await runtime.provider.executeAction(clueB);
    await reject("duplicate after terminal checkpoint", clueB);

    // Nonempty Activity generated by the actual canonical journey above is supplied
    // to the actual projector. Only Scenario.operationalSessionSubjectRef varies.
    // No public journey is run with changed guards. App receives projected snapshots
    // through an explicitly substituted getSnapshot, counted separately from runs.
    const final = original.frames[4];
    const fixture = clone(defaultDemoCatalogs.fixtures[runtime.manifest.fixtureRef]);
    fixture.activityRecords = [
      ...final.snapshot.activity.filter((a) => selected.has(a.id)).map((a) => ({
        id: a.id, kind: "evidence" as const, title: a.title, description: a.description,
        occurredAt: a.occurredAt, provenance: a.provenance,
      })),
      ...fixture.activityRecords,
    ];
    const evaluation = final.verticalResults.at(-1)!;
    const states = Object.fromEntries(final.snapshot.supervisionPerspective!.subjects.map((s) => [s.id, s.operationalState]));
    const observations = [];
    for (const sessionSubject of ["subject-p1", "subject-p2", "opaque:session-h37"]) {
      const scenario = clone(runtime.scenario!); scenario.operationalSessionSubjectRef = sessionSubject;
      const snapshot = projectSnapshot(fixture, scenario, final.snapshot.scenario!.checkpoint, evaluation, states,
        runtime.script!.subjectPresentations, runtime.script!.experimentalJourneyPresentations, runtime.experience!.name);
      const comparable = clone(snapshot); comparable.supervisionPerspective!.sessionSubjectRef = "subject-p1";
      expect(comparable).toEqual(final.snapshot);
      const isolated = make();
      const get = vi.spyOn(isolated.provider, "getSnapshot").mockResolvedValue(snapshot);
      const execute = vi.spyOn(isolated.provider, "executeAction");
      const container = document.createElement("div"); document.body.append(container); const root = createRoot(container);
      clear();
      try {
        await act(async () => root.render(createElement(MemoryRouter, { initialEntries: ["/activity"] }, createElement(App, { runtime: isolated }))));
        const activityDOM = stableDOM(container);
        expect([...container.querySelectorAll(".activity-item__content > p")].map((n) => n.textContent)).toEqual(final.snapshot.activity.map((a) => a.description));
        const link = [...container.querySelectorAll<HTMLAnchorElement>("a")].find((n) => n.textContent === "Supervisión")!;
        await act(async () => link.click());
        const sessionRepresentation = [...container.querySelectorAll('[aria-label="Evaluación compartida"] .system-list > div:first-child dt, [aria-label="Evaluación compartida"] .system-list > div:first-child dd')].map((n) => n.textContent);
        expect(sessionRepresentation).toEqual(["Sujeto de sesión operativa", sessionSubject]);
        expect(execute).not.toHaveBeenCalled(); expect(evaluate).not.toHaveBeenCalled(); expect(cross).not.toHaveBeenCalled();
        observations.push({ sessionSubject, scenario, snapshot, activityDOM, supervisionDOM: stableDOM(container), sessionRepresentation, publicActions: 0 });
      } finally { await act(async () => root.unmount()); container.remove(); get.mockRestore(); execute.mockRestore(); }
    }
    expect(observations.map((o) => o.activityDOM)).toEqual(Array(3).fill(observations[0].activityDOM));
    sessionObservations.push({ demoId, scope: "ISOLATED TRANSPORT/COMPOSITION OBSERVATION; actual projector + current App; getSnapshot substituted; nonempty canonical accepted Activity; no changed-guard journey", observations });
  }
  const generic = [];
  for (const old of h35.genericRegression) {
    const current = await run(resolveDemo(old.demoId));
    expect(current.frames.map(facts)).toEqual(old.current.frames.map(facts));
    expect(facts(current.resetFrame)).toEqual(facts(old.current.resetFrame));
    for (const field of ["homeDOM", "supervisionDOM", "activityDOM"] as const) {
      expect(all(current).map((f) => f[field])).toEqual(all(old.current).map((f) => f[field]));
    }
    generic.push({ demoId: old.demoId, current });
  }
  expect(generic.map((g) => g.demoId).sort()).toEqual(["hospitality-stay", "retail-baseline"]);
  const runs = [...controls.flatMap((c) => [c.original, ...Object.values(c.variants)]), ...generic.map((g) => g.current)];
  const trace = {
    session: 37, recordedAt: new Date().toISOString(), verdict: "SUPPORTED WITH QUALIFICATION",
    method: "CURRENT App createRoot/MemoryRouter/jsdom; actual public-action clicks, adapter, guards and evaluators; immutable S35 comparison masks only four selected descriptions. Isolated session transport explicitly separated.",
    baselineSha256: sha(baselineBytes), priorTraceSha256: sha(h35Bytes), sourceHashes,
    harnessSha256: sha(readFileSync(resolve(process.cwd(), "src/demo-factory/activity-attribution-reduction-h37.test.ts"))),
    controls, genericRegression: generic, sessionObservations, occurrenceNegatives,
    currentAppRuns: runs.length, currentAppFrames: runs.reduce((n, r) => n + all(r).length, 0),
    currentAppDOMCaptures: runs.reduce((n, r) => n + all(r).length * 3, 0),
    isolatedAppObservations: sessionObservations.reduce((n, s) => n + s.observations.length, 0),
    domIntegrationVerification: "EXECUTED", browserVisualValidation: "NOT EXECUTED",
    noNewRelation: "SUFFICIENT within four canonical descriptions; no viewer/actor/account relation",
    historicalH36Verdict: "PRESERVED / FALSIFIED", promotion: "CLOSED / NOT PROMOTED",
  };
  if (process.env.H37_RECORD_PATH) writeFileSync(resolve(process.env.H37_RECORD_PATH), JSON.stringify(trace, null, 2) + "\n", { flag: "wx" });
}, 60000);
