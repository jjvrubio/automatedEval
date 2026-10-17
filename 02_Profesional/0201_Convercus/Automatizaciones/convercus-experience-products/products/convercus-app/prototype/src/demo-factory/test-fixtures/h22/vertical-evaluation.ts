import {
  evaluateCrossSubjectEvidenceSufficiency,
  type AuthoritativePremise,
  type CrossSubjectEvaluationContext,
  type CrossSubjectMarkerEvidence,
} from "./cross-subject-evidence-admissibility";
import type {
  AdmittedEvidenceSufficiencyClaim,
  TreasureHuntSufficiencyCriterion,
} from "./evidence-sufficiency";
import type {
  DemoSubjectState,
  EvidenceInput,
  GuestPerspectiveReadModel,
  SupervisionPerspectiveReadModel,
  SubjectReference,
} from "./contracts";

export interface VerticalEvaluationState {
  readonly evidence: readonly EvidenceInput[];
  readonly jointAdmissibility:
    | "established"
    | "cannot-currently-establish";
  readonly sufficiency: "established" | "not-established" | "not-attempted";
  readonly claim?: AdmittedEvidenceSufficiencyClaim;
}

const evaluationContext: CrossSubjectEvaluationContext = {
  evaluationRef: "evaluation-family-adventure-1",
  huntRef: "hunt-family-adventure-1",
  stayRef: "stay-AS-8842",
  propertyRef: "aurora-resort",
  bookingRef: "AS-8842",
};

const criterion: TreasureHuntSufficiencyCriterion = {
  criterionRef: "criterion-family-adventure",
  authorityRef: "scenario-policy:family-adventure@1",
  scope: {
    huntRef: evaluationContext.huntRef,
    propertyRef: evaluationContext.propertyRef,
  },
  anchorMarkerRef: "marker-a",
  alternativeMarkerRefs: ["marker-b", "marker-c"],
};

const authoritativePremise: AuthoritativePremise = {
  premiseRef: "premise-family-adventure-p1-p2@1",
  authorityRef: "fixture-policy:resort-family-adventure@1",
  scope: evaluationContext,
  coveredSubjectRefs: ["subject-p1", "subject-p2"],
};

function toCrossSubjectEvidence(
  evidence: EvidenceInput,
): CrossSubjectMarkerEvidence {
  const markerRef = evidence.type.replace("treasure_hunt.", "");
  return {
    evidenceRef: evidence.id,
    subjectRef: evidence.subjects[0]?.id ?? "unknown-subject",
    huntRef: evaluationContext.huntRef,
    stayRef: evaluationContext.stayRef,
    propertyRef: evaluationContext.propertyRef,
    markerRef,
    bookingRef: evaluationContext.bookingRef,
  };
}

export function evaluateVerticalEvidence(
  evidence: readonly EvidenceInput[],
): VerticalEvaluationState {
  if (evidence.length === 0) {
    return {
      evidence,
      jointAdmissibility: "cannot-currently-establish",
      sufficiency: "not-attempted",
    };
  }

  const outcome = evaluateCrossSubjectEvidenceSufficiency(
    evidence.map(toCrossSubjectEvidence),
    evaluationContext,
    criterion,
    authoritativePremise,
  );

  if (!outcome.sufficiency.attempted) {
    return {
      evidence,
      jointAdmissibility: outcome.jointAdmissibility.determination,
      sufficiency: "not-attempted",
    };
  }

  return {
    evidence,
    jointAdmissibility: outcome.jointAdmissibility.determination,
    sufficiency: outcome.sufficiency.claim.determination,
    claim: outcome.sufficiency.claim,
  };
}

export function projectGuestPerspective(
  evaluation: VerticalEvaluationState,
  subjects: readonly SubjectReference[] = [],
  subjectStates: Record<string, DemoSubjectState> = {},
): GuestPerspectiveReadModel {
  const discoveredClueCount = evaluation.evidence.length;
  const complete = evaluation.sufficiency === "established";
  const enlisted = subjectStates["subject-p1"] === "enabled";
  return {
    huntName: "Aventura Familiar",
    sessionLabel: "Usas la cuenta de Lucía, huésped 1. El huésped 2 ya figura en esta estancia: puedes habilitarlo y registrar su hallazgo desde aquí.",
    subjects: subjects.map(({ id }) => ({
      id,
      label: id === "subject-p1" ? "Tú · huésped 1" : "Huésped 2 · ya existe en esta estancia",
      status: subjectStates[id] === "enabled"
        ? id === "subject-p1" ? "Alistada y habilitada" : "Habilitado por ti"
        : id === "subject-p1" ? "Sin alistar" : "Sin habilitar",
      clueCount: evaluation.evidence.filter((item) => item.subjects.some((subject) => subject.id === id)).length,
    })),
    state: complete ? "complete" : discoveredClueCount > 0 ? "exploring" : enlisted ? "active" : "ready",
    message: complete
      ? "Las pistas aportadas cumplen la condición de esta aventura."
      : discoveredClueCount > 0
        ? subjectStates["subject-p2"] === "enabled"
          ? "Has habilitado al huésped 2. Todavía no ha aportado pistas. Registra su hallazgo en la fuente cuando lo encuentre."
          : "Tu pista del jardín está aportada. Activa al huésped 2 para que pueda explorar; activarlo no aporta ninguna pista."
        : enlisted
          ? "Estás alistada y habilitada. Todavía no has encontrado ninguna pista. Explora el jardín y registra tu hallazgo."
          : "La aventura está disponible. Alístate para empezar a explorar. Todavía no has aportado pistas.",
    discoveredClueCount,
  };
}

export function projectSupervisionPerspective(
  evaluation: VerticalEvaluationState,
  subjects: readonly SubjectReference[] = [],
  subjectStates: Record<string, DemoSubjectState> = {},
  sessionSubjectRef?: string,
): SupervisionPerspectiveReadModel {
  return {
    sessionSubjectRef,
    subjects: subjects.map(({ id }) => ({
      id,
      exists: true,
      operationalState: subjectStates[id] ?? "not-enabled",
      evidenceCount: evaluation.evidence.filter((item) => item.subjects.some((subject) => subject.id === id)).length,
    })),
    evidence: evaluation.evidence.map((item) => ({
      id: item.id,
      subjectRefs: item.subjects.map(({ id }) => id),
      type: item.type,
      provenance: item.source,
    })),
    jointAdmissibility: evaluation.jointAdmissibility,
    sufficiency: evaluation.sufficiency,
    derivedClaim: evaluation.claim?.determination ?? "not-produced",
  };
}

export const verticalEvaluationContext = evaluationContext;
