import type {
  ActivityItem,
  ActivityKind,
  AppSnapshot,
  DemoAction,
  DemoFixture,
  DemoProvider,
  DemoEnableAction,
  DemoSubjectState,
  DemoScript,
  ScenarioDefinition,
} from "@/demo-factory/contracts";
import {
  evaluateVerticalEvidence,
  type VerticalEvaluationState,
  projectGuestPerspective,
  projectSupervisionPerspective,
} from "@/demo-factory/vertical-evaluation";

const visualByKind: Record<
  ActivityKind,
  Pick<ActivityItem, "tone" | "icon">
> = {
  purchase: { tone: "cyan", icon: "star" },
  benefit: { tone: "pink", icon: "gift" },
  profile: { tone: "blue", icon: "user" },
  stay: { tone: "cyan", icon: "home" },
  service: { tone: "pink", icon: "sparkles" },
  evidence: { tone: "blue", icon: "activity" },
};

function formatActivityDate(occurredAt: string): string {
  return new Intl.DateTimeFormat("es-ES", {
    day: "numeric",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
    timeZone: "UTC",
  }).format(new Date(occurredAt));
}

export function projectSnapshot(
  fixture: DemoFixture,
  scenario?: ScenarioDefinition,
  checkpoint?: string,
  evaluation: VerticalEvaluationState = { evidence: [], jointAdmissibility: "cannot-currently-establish", sufficiency: "not-attempted" },
  subjectStates: Record<string, DemoSubjectState> = {},
  subjectPresentations: DemoScript["subjectPresentations"] = [],
): AppSnapshot {
  const snapshot: AppSnapshot = {
    member: structuredClone(fixture.member),
    coupons: structuredClone(fixture.coupons),
    news: structuredClone(fixture.news),
    activity: fixture.activityRecords.map((record) => ({
      id: record.id,
      title: record.title,
      description: record.description,
      occurredAt: record.occurredAt,
      displayDate: formatActivityDate(record.occurredAt),
      points: record.points,
      provenance: record.provenance,
      ...visualByKind[record.kind],
    })),
  };

  if (scenario && checkpoint) {
    const configuredAction = scenario.actions?.find((action) =>
      action.fromCheckpoint === checkpoint &&
      (!action.subjectRef || (action.kind === "enlist"
        ? subjectStates[action.subjectRef] === "not-enlisted"
        : action.kind === "activate"
          ? subjectStates[action.subjectRef] === "not-enabled" && subjectStates[scenario.operationalSessionSubjectRef ?? ""] === "enabled"
          : !action.requiresEnabledSubject || subjectStates[action.subjectRef] === "enabled")),
    );
    snapshot.scenario = {
      checkpoint,
      availableActionId: scenario.actions
        ? configuredAction?.actionId
        : checkpoint === scenario.presenterAction.fromCheckpoint ? scenario.presenterAction.actionId : undefined,
    };
  }

  if (scenario?.experienceRef === "experience:family-adventure@1") {
    snapshot.guestPerspective = projectGuestPerspective(evaluation, scenario.subjects, subjectStates, subjectPresentations, fixture.member.name);
    snapshot.supervisionPerspective = projectSupervisionPerspective(
      evaluation, scenario.subjects, subjectStates, scenario.operationalSessionSubjectRef,
    );
  }

  return snapshot;
}

export class MockDataAdapter implements DemoProvider {
  readonly mode = "mock" as const;
  private readonly initialFixture: DemoFixture;
  private fixture: DemoFixture;
  private readonly scenario?: ScenarioDefinition;
  // H25 presentation dependency only; Scenario and public action still govern acceptance.
  private readonly script?: DemoScript;
  private checkpoint?: string;
  private evidence: DemoAction["evidence"][] = [];
  private subjectStates: Record<string, DemoSubjectState> = {};
  private evaluation = evaluateVerticalEvidence([]);

  constructor(fixture: DemoFixture, scenario?: ScenarioDefinition, script?: DemoScript) {
    this.initialFixture = structuredClone(fixture);
    this.fixture = structuredClone(fixture);
    this.scenario = scenario ? structuredClone(scenario) : undefined;
    this.script = script ? structuredClone(script) : undefined;
    this.checkpoint = scenario?.initialCheckpoint;
    this.subjectStates = structuredClone(scenario?.initialSubjectStates ?? {});
  }

  async getSnapshot(): Promise<AppSnapshot> {
    return projectSnapshot(
      this.fixture,
      this.scenario,
      this.checkpoint,
      this.evaluation,
      this.subjectStates,
      this.script?.subjectPresentations,
    );
  }

  async executeAction(action: DemoAction | DemoEnableAction): Promise<AppSnapshot> {
    const transition = this.scenario?.actions?.find(
      ({ actionId }) => actionId === action.actionId,
    ) ?? this.scenario?.presenterAction;
    if (!transition || action.actionId !== transition.actionId) {
      throw new Error(`Acción de Scenario no permitida: ${action.actionId}.`);
    }
    if (this.checkpoint !== transition.fromCheckpoint) {
      throw new Error(
        `Acción ${action.actionId} no permitida desde checkpoint ${this.checkpoint ?? "ausente"}.`,
      );
    }

    const configuredAction = this.scenario?.actions?.find(
      ({ actionId }) => actionId === action.actionId,
    );
    const subjectRef = configuredAction?.subjectRef;
    if (configuredAction?.kind === "enlist" || configuredAction?.kind === "activate") {
      const expectedState = configuredAction.kind === "enlist" ? "not-enlisted" : "not-enabled";
      if (!subjectRef || !this.scenario?.subjects.some(({ id }) => id === subjectRef) || this.subjectStates[subjectRef] !== expectedState) {
        throw new Error(`Habilitación no permitida para sujeto ${subjectRef ?? "ausente"}.`);
      }
      if (!("operation" in action) || action.operation !== configuredAction.kind || "evidence" in action) {
        throw new Error("El alistamiento y la activación no producen Evidence.");
      }
      const sessionSubject = this.scenario.operationalSessionSubjectRef;
      if (!sessionSubject || (configuredAction.kind === "enlist"
        ? sessionSubject !== subjectRef
        : this.subjectStates[sessionSubject] !== "enabled" || sessionSubject === subjectRef)) {
        throw new Error("La operación requiere la sesión de P1 habilitada.");
      }
      this.subjectStates[subjectRef] = "enabled";
    } else {
      if (!("evidence" in action) || "operation" in action) {
        throw new Error("La acción de exploración requiere Evidence.");
      }
      const { evidence } = action;
      if (configuredAction?.requiresEnabledSubject) {
        if (!subjectRef || this.subjectStates[subjectRef] !== "enabled") {
          throw new Error(`El sujeto ${subjectRef ?? "ausente"} aún no está habilitado.`);
        }
        if (evidence.subjects.length !== 1 || evidence.subjects[0].id !== subjectRef || evidence.subjects[0].type !== "individual" || evidence.type !== configuredAction.evidenceType || evidence.interpretation) {
          throw new Error("Evidence incompatible con la acción y su atribución configurada.");
        }
      }
      this.evidence.push(structuredClone(evidence));
      if (this.scenario?.experienceRef === "experience:family-adventure@1") this.evaluation = evaluateVerticalEvidence(this.evidence, this.scenario.contexts);
      // H25 local experimental absence behavior, not a product fallback policy:
      // an accepted enabled-subject Evidence action without presentation adds no
      // situated Activity record. Generic Activity retains its existing behavior.
      const presentation = configuredAction?.requiresEnabledSubject
        ? this.script?.steps.find((step) => step.action.actionId === action.actionId)?.activityPresentation
        : { title: evidence.type, description: `Evidencia recibida desde ${evidence.source}.` };
      if (presentation) this.fixture.activityRecords.unshift({
        id: evidence.id,
        kind: "evidence",
        title: presentation.title,
        description: presentation.description,
        occurredAt: evidence.occurredAt,
        provenance: "simulated",
      });
    }
    this.checkpoint = transition.toCheckpoint;
    return this.getSnapshot();
  }

  async reset(): Promise<AppSnapshot> {
    this.fixture = structuredClone(this.initialFixture);
    this.checkpoint = this.scenario?.initialCheckpoint;
    this.evidence = [];
    this.subjectStates = structuredClone(this.scenario?.initialSubjectStates ?? {});
    this.evaluation = evaluateVerticalEvidence([]);
    return this.getSnapshot();
  }
}
