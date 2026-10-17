import { describe, expect, it } from "vitest";
import {
  defaultDemoCatalogs,
  resolveDemo,
  selectDemoId,
  type DemoCatalogs,
} from "./bootstrap";
import { hospitalityManifest, retailManifest } from "./manifests";

function catalogsWith(overrides: Partial<DemoCatalogs>): DemoCatalogs {
  return { ...defaultDemoCatalogs, ...overrides };
}

describe("Demo Factory bootstrap", () => {
  it("resolves materially different retail and hospitality demos", async () => {
    const retail = resolveDemo("retail-baseline");
    const hospitality = resolveDemo("hospitality-stay");

    expect(retail.brand.id).toBe("convercus");
    expect(hospitality.brand.id).toBe("aurora-stay");
    await expect(retail.provider.getSnapshot()).resolves.toMatchObject({
      member: { id: "member-demo-001", fullName: "Alex Martín" },
    });
    await expect(hospitality.provider.getSnapshot()).resolves.toMatchObject({
      member: { id: "guest-lucia-vega", fullName: "Lucía Vega" },
    });
  });

  it("keeps requested composition distinct from resolved capabilities", () => {
    const runtime = resolveDemo("hospitality-stay");

    expect(runtime.manifest.requestedCapabilities[0]).not.toHaveProperty("providerId");
    expect(runtime.capabilities).toEqual(
      expect.arrayContaining([
        expect.objectContaining({
          id: "activity-feed",
          status: "mocked",
          providerId: "mock-data-adapter",
          provenance: expect.stringContaining("fixture:hospitality-stay@1"),
        }),
        expect.objectContaining({ id: "demo-actions", status: "simulated" }),
      ]),
    );
  });

  it("keeps manifests declarative and permits several demos per prospect", () => {
    const secondRetail = {
      ...retailManifest,
      demoId: "retail-baseline-alternate",
    };
    const manifests = {
      ...defaultDemoCatalogs.manifests,
      [secondRetail.demoId]: secondRetail,
    };
    const alternate = resolveDemo(
      secondRetail.demoId,
      catalogsWith({ manifests }),
    );

    expect(alternate.manifest.prospectId).toBe(retailManifest.prospectId);
    expect(JSON.stringify([retailManifest, hospitalityManifest])).not.toMatch(
      /secret|password|token|providerId/i,
    );
  });

  it("uses an explicit query selection and rejects an unknown demo", () => {
    expect(selectDemoId("?demo=hospitality-stay")).toBe("hospitality-stay");
    expect(selectDemoId("")).toBe("retail-baseline");
    expect(() => resolveDemo("missing-demo")).toThrow(
      'Demo desconocida: "missing-demo".',
    );
  });

  it("fails explicitly for missing brand, fixture and capability", () => {
    expect(() =>
      resolveDemo(
        "retail-baseline",
        catalogsWith({ brands: {} }),
      ),
    ).toThrow("referencia de marca no resuelta");
    expect(() =>
      resolveDemo(
        "retail-baseline",
        catalogsWith({ fixtures: {} }),
      ),
    ).toThrow("referencia de fixture no resuelta");

    const invalidManifest = {
      ...retailManifest,
      requestedCapabilities: [
        ...retailManifest.requestedCapabilities,
        { id: "unknown-capability", label: "Unknown", expectedStatus: "mocked" as const },
      ],
    };
    expect(() =>
      resolveDemo(
        "retail-baseline",
        catalogsWith({
          manifests: { ...defaultDemoCatalogs.manifests, "retail-baseline": invalidManifest },
        }),
      ),
    ).toThrow("capability no resuelta: unknown-capability");
  });

  it("validates required brand assets and tokens", () => {
    const invalidBrand = {
      ...defaultDemoCatalogs.brands[retailManifest.brandRef],
      logoUrl: "",
    };
    expect(() =>
      resolveDemo(
        "retail-baseline",
        catalogsWith({ brands: { [retailManifest.brandRef]: invalidBrand } }),
      ),
    ).toThrow("la marca debe declarar id, name y logoUrl");

    const brandWithoutTokens = {
      ...defaultDemoCatalogs.brands[retailManifest.brandRef],
      cssVariables: {},
    };
    expect(() =>
      resolveDemo(
        "retail-baseline",
        catalogsWith({
          brands: { [retailManifest.brandRef]: brandWithoutTokens },
        }),
      ),
    ).toThrow("la marca no declara tokens requeridos");
  });

  it("preserves Scenario, Experience and Script as separate optional artifacts", () => {
    const retail = resolveDemo("retail-baseline");
    const hospitality = resolveDemo("hospitality-stay");

    expect(retail.scenario).toBeUndefined();
    expect(retail.script).toBeUndefined();
    expect(hospitality.experience?.tesBaseline).toBe(
      "TES_CONVERCUS_BUILDER_2026_07_R1",
    );
    expect(hospitality.scenario).toMatchObject({
      experienceRef: "experience:arrival-welcome@1",
      subjects: [
        expect.objectContaining({ type: "individual" }),
        expect.objectContaining({ type: "group" }),
      ],
      contexts: expect.arrayContaining([
        expect.objectContaining({ type: "booking" }),
        expect.objectContaining({ type: "stay" }),
      ]),
    });
    expect(hospitality.script).toMatchObject({
      scenarioRef: hospitality.manifest.scenarioRef,
      initialCheckpoint: "pre-arrival-confirmed",
      steps: [expect.objectContaining({ id: "confirm-check-in" })],
    });
    expect(JSON.stringify(hospitality.scenario)).not.toContain("memberId");
  });

  it("isolates fixture state and deterministic reset across demos", async () => {
    const retail = resolveDemo("retail-baseline");
    const hospitality = resolveDemo("hospitality-stay");
    const retailInitial = await retail.provider.getSnapshot();
    const hospitalityInitial = await hospitality.provider.getSnapshot();
    const hospitalityAction = hospitality.script?.steps[0].action;

    if (!hospitalityAction) throw new Error("Hospitality Script ausente.");
    await hospitality.provider.executeAction(hospitalityAction);

    await expect(retail.provider.getSnapshot()).resolves.toEqual(retailInitial);
    await expect(hospitality.provider.reset()).resolves.toEqual(hospitalityInitial);
    expect(retailInitial).not.toEqual(hospitalityInitial);
  });

  it("keeps prospect data out of the other resolved runtime", () => {
    const retail = JSON.stringify(resolveDemo("retail-baseline"));
    const hospitality = JSON.stringify(resolveDemo("hospitality-stay"));

    expect(retail).not.toMatch(/Aurora Stay|Lucía Vega|AS-8842/);
    expect(hospitality).not.toMatch(/Alex Martín|coupon-welcome|Compra registrada/);
  });
});
