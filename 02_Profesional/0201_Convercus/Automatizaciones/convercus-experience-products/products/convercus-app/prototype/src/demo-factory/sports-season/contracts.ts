import type { BrandArtifact, DemoManifest, ResolvedCapability } from "../contracts";

// BUILD 01: local product constructs, experimental, not a TES contract.
export type SportsModality = "social" | "wellness";
export type EffortLevel = "suave" | "medio" | "intenso";

export interface SportsPerson {
  id: string;
  name: string;
  membershipStatus: "external" | "member";
  customerRelationship: "not-established" | "established";
}

export interface SportsEvent {
  id: string;
  seasonRef: string;
  discipline: "running" | "sailing" | "beach-volleyball";
  label: string;
  title: string;
  date: string;
  place: string;
  description: string;
  executable: boolean;
}

export interface SportsSeasonScenario {
  id: string;
  fixtureRef: string;
  person: SportsPerson;
  contrastPerson: SportsPerson;
  season: { id: string; title: string; dates: string; introduction: string };
  events: SportsEvent[];
  modalities: Array<{ value: SportsModality; label: string; description: string }>;
  efforts: Array<{ value: EffortLevel; label: string }>;
  badge: { id: string; title: string; reason: string };
  club: { name: string; invitation: string; description: string };
}

export interface SportsRegistration {
  registrationId: string;
  personRef: string;
  eventRef: string;
  selectedModality: SportsModality;
  status: "accepted";
}

interface SportsEvidenceBase {
  evidenceId: string;
  personRef: string;
  registrationRef: string;
  eventRef: string;
  occurredAt: string;
  simulation: true;
}

export type SportsEvidence =
  | (SportsEvidenceBase & { kind: "presence"; source: "simulated-check-in" })
  | (SportsEvidenceBase & { kind: "effort"; source: "participant-self-report"; level: EffortLevel });

export interface SportsBadge {
  badgeId: string;
  personRef: string;
  eventRef: string;
  registrationRef: string;
  ruleRef: string;
  supportingEvidenceRefs: string[];
  title: string;
  reason: string;
}

export interface CaptureOpportunity {
  id: string;
  personRef: string;
  registrationRef: string;
  badgeRef: string;
  kind: "club-invitation";
  status: "available";
}

export interface SportsSnapshot {
  scenario: SportsSeasonScenario;
  criterion: { ruleRef: string; explanation: string };
  registration?: SportsRegistration;
  evidence: SportsEvidence[];
  badge?: SportsBadge;
  opportunity?: CaptureOpportunity;
  // Operational demo position, never TES Progression/Completion.
  stage: "available" | "registered" | "presence-received" | "recognized";
  userPlane?: SportsUserSnapshot;
}

interface SportsActionSubject { personRef: string; eventRef: string }
export type SportsAction =
  | (SportsActionSubject & { type: "sports-register"; selectedModality: string })
  | (SportsActionSubject & { type: "sports-check-in"; registrationRef: string })
  | (SportsActionSubject & { type: "sports-effort"; registrationRef: string; level: string });

// BUILD 02: situated, fictitious user context. These records are not sports Evidence.
export interface SportsPurchase {
  id: string;
  date: string;
  description: string;
  amountCents: number;
}

export interface SportsDemoPerson extends SportsPerson {
  knownData?: { city: string; usualSport: string };
  purchases: SportsPurchase[];
  program?: { points: number; level: string; benefits: string[] };
}

export interface SportsUserConfiguration {
  people: SportsDemoPerson[];
  primaryPersonRef: string;
  counterfactualPointsPerEuro: number;
  interests: Array<{ value: string; label: string }>;
  frequencies: Array<{ value: string; label: string }>;
  goals: Array<{ value: string; label: string }>;
  incentive: { id: string; title: string; content: string[] };
  equipment: Array<{ eventRef: string; title: string; description: string }>;
}

export interface SportsUserSnapshot {
  relationship?: import("./relationship-contract").PersonRelationship;
  configuration: SportsUserConfiguration;
  person?: SportsDemoPerson;
  intention?: "participate" | "information";
  selectedEventRef?: string;
  registrationEntry?: { eventRef: string; source: "simulated-registration-qr"; recognized: boolean };
  visitorIdentified: boolean;
  declaredInterests?: { personRef: string; values: string[]; source: "person-declared" | "user_declared"; occurredAt: string };
  voluntary?: { personRef: string; decision: "provided" | "skipped"; frequency?: string; goal?: string; source: "person-declared" | "user_declared"; occurredAt: string };
  counterfactual?: { totalCents: number; potentialPoints: number; credited: false };
  incentive?: { id: string; personRef: string; title: string; content: string[]; source: "voluntary-information" };
  recommendations: SportsUserConfiguration["equipment"];
}

export type SportsUserAction =
  | { type: "sports-select-person"; personRef: string }
  | { type: "sports-registration-qr"; eventRef: string }
  | { type: "sports-identify-visitor"; personRef: string; name: string }
  | { type: "sports-intention"; personRef: string; intention: string }
  | (SportsActionSubject & { type: "sports-select-event" })
  | { type: "sports-interests"; personRef: string; values: string[] }
  | { type: "sports-voluntary"; personRef: string; decision: "provided" | "skipped"; frequency?: string; goal?: string };

export type SportsDemoAction = SportsAction | SportsUserAction;

export interface SportsProvider {
  getSnapshot(): Promise<SportsSnapshot>;
  executeAction(action: SportsDemoAction): Promise<SportsSnapshot>;
  reset(): Promise<SportsSnapshot>;
}

export interface SportsSeasonResolvedRuntime {
  kind: "sports-season";
  manifest: DemoManifest;
  brand: BrandArtifact;
  scenario: SportsSeasonScenario;
  provider: SportsProvider;
  capabilities: ResolvedCapability[];
}
