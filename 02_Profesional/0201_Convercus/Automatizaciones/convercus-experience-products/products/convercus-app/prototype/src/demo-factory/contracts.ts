import type { IconName } from "@/ui/Icon";
import type { CapabilityStatus } from "@/domain/contracts";

export type { CapabilityStatus } from "@/domain/contracts";

export interface MemberReadModel {
  id: string;
  name: string;
  fullName: string;
  initials: string;
  level: string;
  nextLevel: string;
  points: number;
  progress: number;
  pointsToNextLevel: number;
  memberSince: string;
}

export interface CouponReadModel {
  id: string;
  title: string;
  description: string;
  validUntil: string;
  tag: string;
  tone: "cyan" | "pink" | "blue";
  icon: IconName;
}

export interface NewsReadModel {
  id: string;
  category: string;
  title: string;
  summary: string;
}

export interface ActivityItem {
  id: string;
  title: string;
  description: string;
  occurredAt: string;
  displayDate: string;
  points?: number;
  tone: "cyan" | "pink" | "blue";
  icon: IconName;
  provenance: "mocked" | "simulated";
}

export interface AppSnapshot {
  member: MemberReadModel;
  coupons: CouponReadModel[];
  news: NewsReadModel[];
  activity: ActivityItem[];
  scenario?: {
    checkpoint: string;
    availableActionId?: string;
  };
  guestPerspective?: GuestPerspectiveReadModel;
  supervisionPerspective?: SupervisionPerspectiveReadModel;
}

// Local experimental demo state, not a productive enlistment contract.
export type DemoSubjectState = "not-enlisted" | "not-enabled" | "enabled";

export interface GuestPerspectiveReadModel {
  huntName: string;
  state: "ready" | "active" | "exploring" | "complete";
  message: string;
  discoveredClueCount: number;
  sessionLabel: string;
  subjects: Array<{ id: string; label: string; status: string; clueCount: number }>;
}

export interface SupervisionPerspectiveReadModel {
  subjects: Array<{
    id: string;
    exists: true;
    operationalState: DemoSubjectState;
    evidenceCount: number;
  }>;
  sessionSubjectRef?: string;
  evidence: Array<{
    id: string;
    subjectRefs: string[];
    type: string;
    provenance: string;
  }>;
  jointAdmissibility: "established" | "cannot-currently-establish";
  sufficiency: "established" | "not-established" | "not-attempted";
  derivedClaim: "established" | "not-established" | "not-produced";
}

export type ActivityKind =
  | "purchase"
  | "benefit"
  | "profile"
  | "stay"
  | "service"
  | "evidence";

export interface ActivitySourceRecord {
  id: string;
  kind: ActivityKind;
  title: string;
  description: string;
  occurredAt: string;
  points?: number;
  provenance: "mocked" | "simulated";
}

export interface DemoFixture {
  id: string;
  member: MemberReadModel;
  coupons: CouponReadModel[];
  news: NewsReadModel[];
  activityRecords: ActivitySourceRecord[];
}

export interface SubjectReference {
  type: "individual" | "group";
  id: string;
  role: string;
}

export interface ContextReference {
  type: "booking" | "stay" | "property";
  id: string;
}

export interface TesEventInterpretation {
  id: string;
  type: string;
  experienceRef: string;
}

export interface EvidenceInput {
  id: string;
  type: string;
  occurredAt: string;
  source: string;
  reliability: "confirmed" | "estimated" | "unknown";
  subjects: SubjectReference[];
  contexts: ContextReference[];
  interpretation?: TesEventInterpretation;
}

export type DemoAction = {
  type: "scenario_action";
  actionId: string;
  evidence: EvidenceInput;
};

export type DemoEnableAction = {
  type: "scenario_action";
  actionId: string;
  operation: "enlist" | "activate";
};

export interface DemoProvider {
  getSnapshot(): Promise<AppSnapshot>;
  executeAction(action: DemoAction | DemoEnableAction): Promise<AppSnapshot>;
  reset(): Promise<AppSnapshot>;
}

export type DemoModule = "home" | "benefits" | "activity" | "profile";

export interface CapabilityRequest {
  id: string;
  label: string;
  expectedStatus: CapabilityStatus;
}

export interface DemoManifest {
  schemaVersion: 1;
  demoId: string;
  prospectId: string;
  locale: string;
  brandRef: string;
  fixtureRef: string;
  scenarioRef?: string;
  scriptRef?: string;
  // BUILD 01 local composition selector; not a provider registry or TES relation.
  sportsSeasonRef?: string;
  visibleModules: DemoModule[];
  requestedCapabilities: CapabilityRequest[];
}

export interface ExperienceDefinition {
  id: string;
  name: string;
  tesBaseline: string;
}

export interface ScenarioDefinition {
  id: string;
  experienceRef: string;
  subjects: SubjectReference[];
  contexts: ContextReference[];
  checkpoints: string[];
  // Checkpoints describe controlled demo runtime state, not TES Progression.
  initialCheckpoint: string;
  operationalSessionSubjectRef?: string;
  initialSubjectStates?: Record<string, DemoSubjectState>;
  presenterAction: {
    actionId: string;
    fromCheckpoint: string;
    toCheckpoint: string;
  };
  actions?: Array<{
    actionId: string;
    fromCheckpoint: string;
    toCheckpoint: string;
    kind?: "enlist" | "activate" | "evidence";
    subjectRef?: string;
    requiresEnabledSubject?: boolean;
    evidenceType?: string;
  }>;
}

export interface DemoScript {
  id: string;
  scenarioRef: string;
  initialCheckpoint: string;
  // H27: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
  // Display relation only; no account, authentication or subject identity claim.
  subjectPresentations?: Array<{ subjectRef: string; label: string }>;
  // H30: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
  // Existing available affordance -> situated message, never runtime authority.
  // Available action is not journey state; no viewer or TES Progression relation.
  experimentalJourneyPresentations?: Array<{ availableActionId: string; message: string }>;
  // H32: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
  // Static introduction for the selected demonstration, not runtime truth,
  // branding, journey state or a viewer/subject/stay relationship.
  experimentalIntroductoryFraming?: string;
  steps: Array<{
    id: string;
    presenterLabel: string;
    // H25: EXPERIMENTAL / LOCAL / REVERSIBLE / NOT PROMOTED.
    // Presentation after an accepted Evidence action, never factual authority.
    // Independent of presenterLabel (the before-action affordance).
    activityPresentation?: {
      title: string;
      description: string;
    };
    expectedCheckpoint: string;
    action: DemoAction | DemoEnableAction;
  }>;
}

export interface BrandArtifact {
  id: string;
  name: string;
  logoUrl: string;
  cssVariables: Record<string, string>;
}

export interface ResolvedCapability extends CapabilityRequest {
  providerId: string;
  status: CapabilityStatus;
  provenance: string;
}

export interface ResolvedDemoRuntime {
  manifest: DemoManifest;
  brand: BrandArtifact;
  experience?: ExperienceDefinition;
  scenario?: ScenarioDefinition;
  script?: DemoScript;
  provider: DemoProvider;
  capabilities: ResolvedCapability[];
}
