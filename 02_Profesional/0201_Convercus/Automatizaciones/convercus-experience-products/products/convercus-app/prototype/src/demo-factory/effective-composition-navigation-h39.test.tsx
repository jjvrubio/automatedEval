/// <reference types="node" />
import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { act } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { afterAll, afterEach, expect, it, vi } from "vitest";
import { App } from "@/app/App";
import { MockDataAdapter } from "@/demo/mock-adapter";
import { defaultDemoCatalogs, resolveDemo, selectDemoId, type DemoCatalogs } from "./bootstrap";
import type { ResolvedDemoRuntime } from "./contracts";

// Evidence only. Current App/bootstrap/provider are neither mocked nor edited.
// jsdom supports the actual BrowserRouter click/history path, NOT document reload.
// The generic entry-point boundary is intercepted and explicitly reconstructed.
Object.assign(globalThis, { IS_REACT_ACT_ENVIRONMENT: true });
const sha = (bytes: Buffer | string) => createHash("sha256").update(bytes).digest("hex");
const rootPath = resolve(process.cwd(), "../../..");
const evidence = resolve(process.cwd(), "../docs/evidence/session-39");
const appSource = readFileSync(resolve(process.cwd(), "src/app/App.tsx"), "utf8");
const rows: unknown[] = [];
const renameControls: unknown[] = [];
const canonicalIds = ["retail-baseline", "hospitality-stay", "hospitality-family-adventure", "hospitality-family-adventure-costa"];

afterEach(() => { vi.restoreAllMocks(); document.body.innerHTML = ""; window.history.replaceState(null, "", "/"); });

async function inspectNavigation(id: string, catalogs: DemoCatalogs = defaultDemoCatalogs) {
  const initialRoute = "/?demo=" + id;
  window.history.replaceState(null, "", initialRoute);
  let runtime = resolveDemo(selectDemoId(window.location.search), catalogs);
  const originalRuntime = runtime;
  const originalProvider = runtime.provider;
  expect(Object.getPrototypeOf(originalProvider)).toBe(MockDataAdapter.prototype);
  const initialSnapshot = await originalProvider.getSnapshot();
  const family = Boolean(initialSnapshot.guestPerspective);
  const selectedLabel = family ? "Mi aventura" : "Búsqueda del tesoro";
  const reset = vi.spyOn(originalProvider, "reset");
  const execute = vi.spyOn(originalProvider, "executeAction");
  const container = document.createElement("div"); document.body.append(container);
  let root = createRoot(container);
  const mount = async () => { await act(async () => root.render(<BrowserRouter><App runtime={runtime} /></BrowserRouter>)); };
  const location = () => window.location.pathname + window.location.search;
  const findLink = (label: string) => {
    const matches = [...container.querySelectorAll<HTMLAnchorElement>("a")].filter((node) => node.textContent === label);
    expect(matches, label).toHaveLength(1);
    return matches[0];
  };
  const visible = () => ({
    brand: container.querySelector(".brand-logo")?.getAttribute("alt"),
    title: container.querySelector("h1")?.textContent,
    framing: container.querySelector(".adventure-heading h1 + p")?.textContent ?? null,
    account: container.querySelector(".adventure-account")?.textContent ?? null,
    guestLabels: [...container.querySelectorAll(".adventure-guest h3")].map((node) => node.textContent),
    message: container.querySelector(".adventure-message")?.textContent ?? null,
    clueCount: container.querySelector(".adventure-count")?.textContent ?? null,
  });
  const assertIdentity = (expected: ResolvedDemoRuntime) => {
    expect(runtime.manifest.demoId).toBe(expected.manifest.demoId);
    expect(selectDemoId(window.location.search)).toBe(expected.manifest.demoId);
    expect(visible().brand).toBe(expected.brand.name);
  };
  try {
    await mount();
    const selected = findLink(selectedLabel);
    const before = { route: location(), urlDemoId: selectDemoId(window.location.search), runtimeDemoId: runtime.manifest.demoId,
      snapshot: initialSnapshot, visible: visible(), href: selected.getAttribute("href"), selectedDOM: selected.outerHTML };
    const phases = [];
    if (family) {
      expect(container.textContent).not.toContain("Búsqueda del tesoro");
      expect(selected.getAttribute("href")).toBe(initialRoute);
      expect(appSource).toContain('const demoSearch = `?demo=${runtime.manifest.demoId}`;');
      expect(appSource).toContain('<NavLink to={`/${demoSearch}`} end>Mi aventura</NavLink>');
      const navigate = async (phase: string) => {
        const snapshotBefore = await originalProvider.getSnapshot();
        const visibleBefore = visible();
        const urlBefore = location();
        const target = findLink("Mi aventura");
        const selectedDOM = target.outerHTML;
        const actionCountBefore = execute.mock.calls.length;
        let routerPreventedDefault: boolean | undefined;
        const observe = (event: MouseEvent) => { routerPreventedDefault = event.defaultPrevented; };
        document.addEventListener("click", observe, { once: true });
        try { await act(async () => target.click()); }
        finally { document.removeEventListener("click", observe); }
        expect(routerPreventedDefault).toBe(true);
        expect(runtime).toBe(originalRuntime);
        expect(runtime.provider).toBe(originalProvider);
        expect(await runtime.provider.getSnapshot()).toEqual(snapshotBefore);
        expect(reset).not.toHaveBeenCalled();
        expect(execute).toHaveBeenCalledTimes(actionCountBefore);
        expect(location()).toBe(initialRoute);
        assertIdentity(originalRuntime);
        if (phase !== "return-from-activity") expect(visible()).toEqual(visibleBefore);
        phases.push({ phase, urlBefore, urlAfter: location(), runtimeBefore: originalRuntime.manifest.demoId,
          runtimeAfter: runtime.manifest.demoId, href: target.getAttribute("href"), selectedDOM,
          browserRouterPreventedDefault: routerPreventedDefault, sameProvider: runtime.provider === originalProvider,
          resetCalls: reset.mock.calls.length, actionCallsDuringNavigation: execute.mock.calls.length - actionCountBefore,
          snapshotBefore, snapshotAfter: await runtime.provider.getSnapshot(), visibleBefore, visibleAfter: visible(),
          method: "Actual DOM click + BrowserRouter + jsdom history; no reload simulation" });
      };
      await navigate("initial-home");
      // Nonempty progress distinguishes provider preservation from an unnoticed reset.
      for (let index = 0; index < 2; index++) {
        const button = container.querySelector<HTMLButtonElement>(".adventure-next button");
        expect(button).not.toBeNull();
        await act(async () => button!.click());
      }
      expect(execute).toHaveBeenCalledTimes(2);
      const progressed = await originalProvider.getSnapshot();
      expect(progressed.activity.length).toBeGreaterThan(initialSnapshot.activity.length);
      expect(progressed.guestPerspective!.discoveredClueCount).toBe(1);
      await navigate("progressed-home");
      await act(async () => findLink("Actividad").click());
      expect(location()).toBe("/activity?demo=" + id);
      await navigate("return-from-activity");
      expect(await originalProvider.getSnapshot()).toEqual(progressed);
    } else {
      expect(container.querySelector(".adventure-nav")).toBeNull();
      expect(selected.getAttribute("href")).toBe("/?demo=hospitality-family-adventure");
      expect(appSource).toContain('<Link reloadDocument={!snapshot.guestPerspective} to="/?demo=hospitality-family-adventure">');
      let routerPreventedDefault: boolean | undefined;
      const interceptReload = (event: MouseEvent) => {
        routerPreventedDefault = event.defaultPrevented;
        event.preventDefault(); // jsdom cannot load a new document. Explicit test boundary.
      };
      document.addEventListener("click", interceptReload, { once: true });
      try { await act(async () => selected.click()); }
      finally { document.removeEventListener("click", interceptReload); }
      expect(routerPreventedDefault).toBe(false);
      expect(location()).toBe(initialRoute); // No fabricated claim that native reload occurred.
      expect(await originalProvider.getSnapshot()).toEqual(initialSnapshot);
      expect(reset).not.toHaveBeenCalled(); expect(execute).not.toHaveBeenCalled();
      await act(async () => root.unmount());
      window.history.replaceState(null, "", before.href!);
      runtime = resolveDemo(selectDemoId(window.location.search), catalogs);
      root = createRoot(container); await mount();
      expect(runtime.manifest.demoId).toBe("hospitality-family-adventure");
      expect(runtime.provider).not.toBe(originalProvider);
      assertIdentity(runtime);
      expect((await runtime.provider.getSnapshot()).guestPerspective).toBeDefined();
      phases.push({ phase: "intentional-entry-to-A", urlBefore: initialRoute,
        urlImmediatelyAfterInterceptedClick: initialRoute, urlAfter: location(),
        runtimeBefore: id, runtimeAfter: runtime.manifest.demoId, href: before.href,
        browserRouterPreventedDefault: routerPreventedDefault, sameProvider: false,
        originalProviderUnchanged: true, resetCalls: reset.mock.calls.length,
        snapshotBefore: initialSnapshot, snapshotAfter: await runtime.provider.getSnapshot(), visibleAfter: visible(),
        method: "Actual DOM click reaches document-navigation boundary; native reload NOT executed. Explicit unmount + URL update + current selectDemoId/resolveDemo + new App models existing main.tsx bootstrap." });
    }
    return { composition: id, manifestDemoId: originalRuntime.manifest.demoId, initialRoute,
      guestPerspective: family ? "PRESENT" : "ABSENT", selectedLabel,
      fixedGenericLinkRendered: !family, href: before.href, reloadDocument: !family,
      reloadDocumentEvidence: family ? "NavLink omits reloadDocument; click intercepted by BrowserRouter" : "Source expression !snapshot.guestPerspective is true; click not intercepted by BrowserRouter",
      runtimeBefore: originalRuntime.manifest.demoId, runtimeAfter: runtime.manifest.demoId,
      urlBefore: before.route, urlAfter: location(), urlCompositionBefore: before.urlDemoId,
      urlCompositionAfter: selectDemoId(window.location.search), visibleCompositionEvidenceAfter: visible(),
      targetSource: family ? "AppShell demoSearch consumes runtime.manifest.demoId" : "HomePage generic entry destination literal hospitality-family-adventure",
      sourceAuthority: family ? "Already resolved composition execution identity; NOT a universal routing relation" : "Existing intentional entry to A; NOT current-composition identity",
      before, phases,
    };
  } finally { await act(async () => root.unmount()); container.remove(); }
}

it.each(canonicalIds)("H39 pre-delta selected navigation: %s", async (id) => {
  rows.push(await inspectNavigation(id));
});

it.each(canonicalIds.slice(2))("H39 existing structural role with renamed identity, without a product registry: %s", async (sourceId) => {
  const catalogs = structuredClone(defaultDemoCatalogs);
  const renamedId = "h39-opaque-composition-" + (sourceId === canonicalIds[2] ? "x" : "y");
  const manifest = catalogs.manifests[sourceId];
  delete catalogs.manifests[sourceId];
  catalogs.manifests[renamedId] = { ...manifest, demoId: renamedId };
  const result = await inspectNavigation(renamedId, catalogs);
  expect(result.href).toBe("/?demo=" + renamedId);
  renameControls.push({ sourceId, renamedId, scope: "In-memory fixture only: manifest catalog key and demoId renamed; same structural role/artifacts. Not arbitrary-demo support.", result });
});

it("H39 STOP gate preserves every received material file and existing H37/H38 assertions", () => {
  const baseline = JSON.parse(readFileSync(resolve(evidence, "baseline.json"), "utf8")) as { files: Record<string, string> };
  for (const [path, hash] of Object.entries(baseline.files)) expect(sha(readFileSync(resolve(rootPath, path))), path).toBe(hash);
});

afterAll(() => {
  if (process.env.H39_RECORD_PATH) writeFileSync(resolve(process.env.H39_RECORD_PATH), JSON.stringify({
    session: 39, recordedAt: new Date().toISOString(), productState: "PRE-DELTA; NO PRODUCT CHANGES",
    method: "Current App, real providers, BrowserRouter and jsdom DOM clicks. Generic reload boundary explicitly modeled, not browser-executed.",
    browserVisualInspection: "NOT EXECUTED: in-app browser execution tool unavailable",
    sourceHashes: Object.fromEntries(["src/app/App.tsx", "src/main.tsx", "src/demo-factory/bootstrap.ts", "src/demo-factory/manifests.ts"].map((path) => [path, sha(readFileSync(resolve(process.cwd(), path)))])),
    harnessSha256: sha(readFileSync(resolve(process.cwd(), "src/demo-factory/effective-composition-navigation-h39.test.tsx"))),
    rows, renameControls,
    gate: "B-to-A problem assumption not reproduced; existing Family Adventure link already consumes effective identity. STOP / PRODUCT DELTA NONE.",
    qualification: "Read alongside test results; a trace alone does not imply assertions passed. No human/commercial/browser acceptance.",
  }, null, 2) + "\n", { flag: "wx" });
});
