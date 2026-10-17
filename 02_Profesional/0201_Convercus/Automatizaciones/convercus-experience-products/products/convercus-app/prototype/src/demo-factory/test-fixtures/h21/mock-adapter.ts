import type {
  ActivityItem,
  ActivityKind,
  AppSnapshot,
  DemoAction,
  DemoFixture,
  DemoProvider,
  DemoEnableAction,
  DemoSubjectState,
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

  if (scenario?.id === "family-adventure") {
    snapshot.guestPerspective = projectGuestPerspective(evaluation, scenario.subjects, subjectStates);
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
  private checkpoint?: string;
  private evidence: DemoAction["evidence"][] = [];
  private subjectStates: Record<string, DemoSubjectState> = {};
  private evaluation = evaluateVerticalEvidence([]);

  constructor(fixture: DemoFixture, scenario?: ScenarioDefinition) {
    this.initialFixture = structuredClone(fixture);
    this.fixture = structuredClone(fixture);
    this.scenario = scenario ? structuredClone(scenario) : undefined;
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
      if (this.scenario?.id === "family-adventure") this.evaluation = evaluateVerticalEvidence(this.evidence);
      this.fixture.activityRecords.unshift({
        id: evidence.id,
        kind: "evidence",
        title: configuredAction?.requiresEnabledSubject
          ? subjectRef === "subject-p1" ? "Pista del jardín encontrada" : "Pista de la fuente encontrada"
          : evidence.type,
        description: configuredAction?.requiresEnabledSubject
          ? subjectRef === "subject-p1" ? "Hallazgo aportado por ti." : "Hallazgo atribuido al huésped 2, registrado desde tu cuenta."
          : `Evidencia recibida desde ${evidence.source}.`,
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
