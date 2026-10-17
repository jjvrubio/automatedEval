import type { DemoManifest } from "./contracts";
import { sportsSeasonManifest } from "./sports-season/artifacts";

const sharedCapabilities = [
  { id: "member-profile", label: "Perfil", expectedStatus: "mocked" },
  { id: "loyalty-balance", label: "Saldo y nivel", expectedStatus: "mocked" },
  { id: "benefit-wallet", label: "Beneficios", expectedStatus: "mocked" },
  { id: "content-feed", label: "Contenido", expectedStatus: "mocked" },
  { id: "activity-feed", label: "Actividad", expectedStatus: "mocked" },
  { id: "demo-actions", label: "Acciones de demo", expectedStatus: "simulated" },
] as const;

export const retailManifest: DemoManifest = {
  schemaVersion: 1,
  demoId: "retail-baseline",
  prospectId: "convercus-retail-reference",
  locale: "es",
  brandRef: "brand:convercus@1",
  fixtureRef: "fixture:retail-baseline@1",
  visibleModules: ["home", "benefits", "activity", "profile"],
  requestedCapabilities: [...sharedCapabilities],
};

export const hospitalityManifest: DemoManifest = {
  schemaVersion: 1,
  demoId: "hospitality-stay",
  prospectId: "aurora-hospitality-group",
  locale: "es",
  brandRef: "brand:aurora-stay@1",
  fixtureRef: "fixture:hospitality-stay@1",
  scenarioRef: "scenario:arrival-and-stay@1",
  scriptRef: "script:hospitality-check-in@1",
  visibleModules: ["home", "benefits", "activity", "profile"],
  requestedCapabilities: [...sharedCapabilities],
};

export const familyAdventureManifest: DemoManifest = {
  schemaVersion: 1,
  demoId: "hospitality-family-adventure",
  prospectId: "aurora-hospitality-group",
  locale: "es",
  brandRef: "brand:aurora-stay@1",
  fixtureRef: "fixture:hospitality-stay@1",
  scenarioRef: "scenario:family-adventure@1",
  scriptRef: "script:family-adventure@1",
  visibleModules: ["home", "benefits", "activity", "profile"],
  requestedCapabilities: [...sharedCapabilities],
};

// H21 falsification composition; not an accepted product demo.
export const costaManifest: DemoManifest = {
  schemaVersion: 1,
  demoId: "hospitality-family-adventure-costa",
  prospectId: "costa-fixture",
  locale: "es",
  brandRef: "brand:costa-clara@1",
  fixtureRef: "fixture:family-adventure-costa@1",
  scenarioRef: "scenario:family-adventure-costa@1",
  scriptRef: "script:family-adventure-costa@1",
  visibleModules: ["home", "benefits", "activity", "profile"],
  requestedCapabilities: [...sharedCapabilities],
};

export const demoManifests: Record<string, DemoManifest> = {
  [sportsSeasonManifest.demoId]: sportsSeasonManifest,
  [costaManifest.demoId]: costaManifest,
  [retailManifest.demoId]: retailManifest,
  [hospitalityManifest.demoId]: hospitalityManifest,
  [familyAdventureManifest.demoId]: familyAdventureManifest,
};
