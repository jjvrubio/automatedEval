export type DataMode = "mock" | "simulation" | "staging" | "production";

export type CapabilityStatus =
  | "real"
  | "simulated"
  | "mocked"
  | "proposed"
  | "unsupported";

export interface CapabilityDeclaration {
  id: string;
  label: string;
  status: CapabilityStatus;
  evidence?: string;
  limitation?: string;
}

export interface CapabilityManifest {
  version: string;
  capabilities: CapabilityDeclaration[];
}

export interface DataAdapter<TSnapshot, TEvent> {
  readonly mode: DataMode;
  getSnapshot(): Promise<TSnapshot>;
  dispatch(event: TEvent): Promise<TSnapshot>;
  reset(): Promise<TSnapshot>;
}

export interface ArchetypeReference {
  id: string;
  label: string;
  sourceDocument: string;
  sourceVersion: string;
}

export interface SectorOrdinalPropensity {
  sector: string;
  value: number;
  scale: string;
  sourceDocument: string;
  sourceVersion: string;
  rationale: string;
}

export interface ExperienceDefinition {
  id: string;
  name: string;
  purpose: string;
  transformationHypothesis: string;
  mediationField: string;
  archetype: ArchetypeReference;
  sectorPropensity: SectorOrdinalPropensity;
  initialState: string;
  intendedOutcome: string;
  tesBaseline: string;
}

export interface ExperienceParticipation {
  id: string;
  experienceId: string;
  memberId: string;
  state: string;
  progression: number;
  status: "available" | "active" | "completed" | "closed";
  updatedAt: string;
}

export interface SignificantEvent<TProperties = Record<string, unknown>> {
  id: string;
  type: string;
  occurredAt: string;
  source: string;
  reliability: "confirmed" | "estimated" | "unknown";
  properties: TProperties;
}

export interface ExperienceEffect {
  experienceId: string;
  participationId: string;
  ruleId: string;
  effect: "progression" | "state_change" | "intervention" | "none";
  explanation: string;
}

export interface EventEvaluationRule {
  id: string;
  experienceId: string;
  accepts(event: SignificantEvent, participation: ExperienceParticipation): boolean;
  evaluate(event: SignificantEvent, participation: ExperienceParticipation): ExperienceEffect;
}

export interface DemoPackage {
  schemaVersion: number;
  id: string;
  name: string;
  brandId: string;
  locale: string;
  dataMode: DataMode;
  tesApplicability: "not_applicable" | "conditional" | "required";
  tesBaseline?: string;
  capabilities: CapabilityManifest;
  experiences: ExperienceDefinition[];
}

