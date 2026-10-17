import { MockDataAdapter } from "@/demo/mock-adapter";
import { brands, experiences, scenarios, scripts } from "./artifacts";
import type {
  BrandArtifact,
  DemoFixture,
  DemoManifest,
  DemoScript,
  ExperienceDefinition,
  ResolvedCapability,
  ResolvedDemoRuntime,
  ScenarioDefinition,
} from "./contracts";
import { costaFixture, hospitalityFixture, retailFixture } from "./fixtures";
import { demoManifests } from "./manifests";
import { sportsBrand, sportsSeasonScenario } from "./sports-season/artifacts";
import { SportsSeasonProvider } from "./sports-season/runtime";
import { FixtureAdapter, userConfigurationFor } from "./sports-season/fixture-adapter";
import type { SportsSeasonResolvedRuntime } from "./sports-season/contracts";

const requiredBrandVariables = [
  "--color-primary",
  "--color-primary-action",
  "--color-background",
  "--color-text",
] as const;

const supportedCapabilities = new Set([
  "member-profile",
  "loyalty-balance",
  "benefit-wallet",
  "content-feed",
  "activity-feed",
  "demo-actions",
]);

export interface DemoCatalogs {
  manifests: Record<string, DemoManifest>;
  brands: Record<string, BrandArtifact>;
  fixtures: Record<string, DemoFixture>;
  experiences: Record<string, ExperienceDefinition>;
  scenarios: Record<string, ScenarioDefinition>;
  scripts: Record<string, DemoScript>;
}

export const defaultDemoCatalogs: DemoCatalogs = {
  manifests: demoManifests,
  brands: { ...brands, "brand:brisa-sport@1": sportsBrand },
  fixtures: {
    [retailFixture.id]: retailFixture,
    [hospitalityFixture.id]: hospitalityFixture,
    [costaFixture.id]: costaFixture,
  },
  experiences,
  scenarios,
  scripts,
};

function requiredArtifact<T>(
  artifacts: Record<string, T>,
  reference: string,
  kind: string,
  demoId: string,
): T {
  const artifact = artifacts[reference];
  if (!artifact) {
    throw new Error(`Demo "${demoId}": referencia de ${kind} no resuelta: ${reference}.`);
  }
  return artifact;
}

function validateBrand(brand: BrandArtifact, demoId: string): void {
  if (!brand.id.trim() || !brand.name.trim() || !brand.logoUrl.trim()) {
    throw new Error(`Demo "${demoId}": la marca debe declarar id, name y logoUrl.`);
  }
  const missing = requiredBrandVariables.filter(
    (variable) => !brand.cssVariables[variable]?.trim(),
  );
  if (missing.length > 0) {
    throw new Error(
      `Demo "${demoId}": la marca no declara tokens requeridos: ${missing.join(", ")}.`,
    );
  }
}

function resolveCapabilities(manifest: DemoManifest): ResolvedCapability[] {
  return manifest.requestedCapabilities.map((request) => {
    if (!supportedCapabilities.has(request.id)) {
      throw new Error(
        `Demo "${manifest.demoId}": capability no resuelta: ${request.id}.`,
      );
    }
    return {
      ...request,
      providerId: "mock-data-adapter",
      status: request.expectedStatus,
      provenance: `${manifest.fixtureRef} via mock-data-adapter`,
    };
  });
}

export function resolveDemo(
  demoId: string,
  catalogs: DemoCatalogs = defaultDemoCatalogs,
): ResolvedDemoRuntime {
  const manifest = catalogs.manifests[demoId];
  if (!manifest) {
    throw new Error(`Demo desconocida: "${demoId}".`);
  }
  if (manifest.schemaVersion !== 1) {
    throw new Error(`Demo "${demoId}": schemaVersion incompatible.`);
  }

  const brand = requiredArtifact(
    catalogs.brands,
    manifest.brandRef,
    "marca",
    demoId,
  );
  validateBrand(brand, demoId);
  const fixture = requiredArtifact(
    catalogs.fixtures,
    manifest.fixtureRef,
    "fixture",
    demoId,
  );

  const scenario = manifest.scenarioRef
    ? requiredArtifact(catalogs.scenarios, manifest.scenarioRef, "Scenario", demoId)
    : undefined;
  const experience = scenario
    ? requiredArtifact(
        catalogs.experiences,
        scenario.experienceRef,
        "Experience",
        demoId,
      )
    : undefined;
  const script = manifest.scriptRef
    ? requiredArtifact(catalogs.scripts, manifest.scriptRef, "Demo Script", demoId)
    : undefined;

  if (script && (!scenario || script.scenarioRef !== manifest.scenarioRef)) {
    throw new Error(`Demo "${demoId}": Demo Script incompatible con Scenario.`);
  }
  if (script && !scenario?.checkpoints.includes(script.initialCheckpoint)) {
    throw new Error(`Demo "${demoId}": checkpoint inicial no resuelto.`);
  }
  if (scenario && !scenario.checkpoints.includes(scenario.initialCheckpoint)) {
    throw new Error(`Demo "${demoId}": checkpoint inicial de Scenario no resuelto.`);
  }
  const scriptStep = script?.steps[0];
  if (
    scriptStep &&
    scenario &&
    (scriptStep.action.actionId !== scenario.presenterAction.actionId ||
      scriptStep.expectedCheckpoint !== scenario.presenterAction.toCheckpoint)
  ) {
    throw new Error(`Demo "${demoId}": acción o checkpoint esperado incompatibles.`);
  }

  return {
    manifest,
    brand,
    experience,
    scenario,
    script,
    provider: new MockDataAdapter(fixture, scenario, script, experience?.name),
    capabilities: resolveCapabilities(manifest),
  };
}

export function selectDemoId(search: string): string {
  return new URLSearchParams(search).get("demo") || "retail-baseline";
}

// BUILD 01: one explicit local composition, preserving the existing resolver.
// No invented member, hotel context, Experience reference or general provider API.
export function resolveAppDemo(
  demoId: string,
  catalogs: DemoCatalogs = defaultDemoCatalogs,
): ResolvedDemoRuntime | SportsSeasonResolvedRuntime {
  const manifest = catalogs.manifests[demoId];
  if (!manifest?.sportsSeasonRef) return resolveDemo(demoId, catalogs);
  if (manifest.schemaVersion !== 1) throw new Error("Versión de composición deportiva incompatible.");
  const scenario = requiredArtifact(
    { [sportsSeasonScenario.id]: sportsSeasonScenario }, manifest.sportsSeasonRef, "Sports Scenario", demoId,
  );
  if (manifest.scenarioRef !== scenario.id || manifest.fixtureRef !== scenario.fixtureRef || manifest.scriptRef) {
    throw new Error("Referencias de la composición deportiva incompatibles.");
  }
  const brand = requiredArtifact(catalogs.brands, manifest.brandRef, "marca", demoId);
  validateBrand(brand, demoId);
  const capabilities: ResolvedCapability[] = manifest.requestedCapabilities.map((request) => {
    if (!["sports-participation", "sports-crm-view"].includes(request.id) || request.expectedStatus !== "simulated") {
      throw new Error(`Capability deportiva no resuelta: ${request.id}.`);
    }
    return { ...request, providerId: "sports-season-local", status: "simulated", provenance: `${scenario.fixtureRef} · local simulation` };
  });
  const data = new FixtureAdapter().load();
  return {
    kind: "sports-season", manifest, brand, scenario: structuredClone(scenario),
    provider: new SportsSeasonProvider(scenario, undefined, userConfigurationFor(data), data), capabilities,
  };
}

export function applyResolvedBrand(
  target: Pick<CSSStyleDeclaration, "setProperty">,
  brand: BrandArtifact,
): void {
  Object.entries(brand.cssVariables).forEach(([property, value]) => {
    target.setProperty(property, value);
  });
}
