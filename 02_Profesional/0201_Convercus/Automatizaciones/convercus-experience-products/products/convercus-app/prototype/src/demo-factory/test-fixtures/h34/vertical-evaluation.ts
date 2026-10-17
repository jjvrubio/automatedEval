import {
  evaluateCrossSubjectEvidenceSufficiency,
  type AuthoritativePremise,
  type CrossSubjectEvaluationContext,
  type CrossSubjectMarkerEvidence,
} from "@/demo-factory/cross-subject-evidence-admissibility";
import type {
  AdmittedEvidenceSufficiencyClaim,
  TreasureHuntSufficiencyCriterion,
} from "@/demo-factory/evidence-sufficiency";
import type {
  ContextReference,
  DemoSubjectState,
  DemoScript,
  EvidenceInput,
  GuestPerspectiveReadModel,
  SupervisionPerspectiveReadModel,
  SubjectReference,
} from "@/demo-factory/contracts";

export interface VerticalEvaluationState {
  readonly evidence: readonly EvidenceInput[];
  readonly jointAdmissibility:
    | "established"
    | "cannot-currently-establish";
  readonly sufficiency: "established" | "not-established" | "not-attempted";
  readonly claim?: AdmittedEvidenceSufficiencyClaim;
}

function contextReference(
  contexts: readonly ContextReference[],
  type: ContextReference["type"],
): string | undefined {
  const matches = contexts.filter((context) => context.type === type);
  return matches.length === 1 && matches[0].id.trim() ? matches[0].id : undefined;
}

function toCrossSubjectEvidence(
  evidence: EvidenceInput,
  evaluationContext: CrossSubjectEvaluationContext,
): CrossSubjectMarkerEvidence | undefined {
  const bookingRef = contextReference(evidence.contexts, "booking");
  const stayRef = contextReference(evidence.contexts, "stay");
  const propertyRef = contextReference(evidence.contexts, "property");
  // Missing/ambiguous facts and contradictions cannot select evaluation scope
  // or be silently rewritten. Current Scripts supply booking/stay, not property.
  if (bookingRef !== evaluationContext.bookingRef || stayRef !== evaluationContext.stayRef ||
      (evidence.contexts.some(({ type }) => type === "property") && propertyRef !== evaluationContext.propertyRef)) {
    return undefined;
  }
  const markerRef = evidence.type.replace("treasure_hunt.", "");
  return {
    evidenceRef: evidence.id,
    subjectRef: evidence.subjects[0]?.id ?? "unknown-subject",
    huntRef: evaluationContext.huntRef,
    stayRef,
    propertyRef: propertyRef ?? evaluationContext.propertyRef,
    markerRef,
    bookingRef,
  };
}

export function evaluateVerticalEvidence(
  evidence: readonly EvidenceInput[],
  situatedContexts: readonly ContextReference[] = [],
): VerticalEvaluationState {
  const unavailable: VerticalEvaluationState = {
    evidence,
    jointAdmissibility: "cannot-currently-establish",
    sufficiency: "not-attempted",
  };
  if (evidence.length === 0) return unavailable;

  const propertyRef = contextReference(situatedContexts, "property");
  const bookingRef = contextReference(situatedContexts, "booking");
  const stayRef = contextReference(situatedContexts, "stay");
  if (!propertyRef || !bookingRef || !stayRef) return unavailable;

  const evaluationContext: CrossSubjectEvaluationContext = {
    evaluationRef: "evaluation-family-adventure-1",
    huntRef: "hunt-family-adventure-1",
    propertyRef, bookingRef, stayRef,
  };
  const converted: CrossSubjectMarkerEvidence[] = [];
  for (const item of evidence) {
    const input = toCrossSubjectEvidence(item, evaluationContext);
    if (!input) return unavailable;
    converted.push(input);
  }
  const criterion: TreasureHuntSufficiencyCriterion = {
    criterionRef: "criterion-family-adventure",
    authorityRef: "scenario-policy:family-adventure@1",
    scope: { huntRef: evaluationContext.huntRef, propertyRef },
    anchorMarkerRef: "marker-a",
    alternativeMarkerRefs: ["marker-b", "marker-c"],
  };
  // Existing experimental premise, explicitly assumed for this situated run.
  // Its authority and fixed P1/P2 coverage are not inferred from Evidence or
  // context equality. H17 still checks applicability separately before K.
  const authoritativePremise: AuthoritativePremise = {
    premiseRef: "premise-family-adventure-p1-p2@1",
    authorityRef: "fixture-policy:resort-family-adventure@1",
    scope: evaluationContext,
    coveredSubjectRefs: ["subject-p1", "subject-p2"],
  };

  const outcome = evaluateCrossSubjectEvidenceSufficiency(
    converted,
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
  subjectPresentations: DemoScript["subjectPresentations"] = [],
  // H28: existing account display source only, never subject/viewer identity.
  accountName = "",
  availableActionId?: string,
  experimentalJourneyPresentations: DemoScript["experimentalJourneyPresentations"] = [],
): GuestPerspectiveReadModel {
  const discoveredClueCount = evaluation.evidence.length;
  const complete = evaluation.sufficiency === "established";
  const enlisted = subjectStates["subject-p1"] === "enabled";
  return {
    huntName: "Aventura Familiar",
    sessionLabel: `Cuenta de ${accountName}`,
    subjects: subjects.map(({ id }) => ({
      id,
      // H27 local absence: no supplied label means no display text. The subject
      // still comes from Scenario; this is not a general product fallback policy.
      label: subjectPresentations.find(({ subjectRef }) => subjectRef === id)?.label ?? "",
      // H29: present operational state only; no actor, viewer or personal gender.
      status: ({
        "not-enlisted": "Estado: sin alistar",
        "not-enabled": "Estado: sin habilitar",
        enabled: "Estado: habilitado",
      })[subjectStates[id]] ?? "",
      clueCount: evaluation.evidence.filter((item) => item.subjects.some((subject) => subject.id === id)).length,
    })),
    state: complete ? "complete" : discoveredClueCount > 0 ? "exploring" : enlisted ? "active" : "ready",
    message: complete
      ? "Las pistas aportadas cumplen la condición de esta aventura."
      : discoveredClueCount === 0 && subjectStates["subject-p1"] === "not-enlisted"
        ? "La aventura está disponible. Alistamiento pendiente."
        // H30 local presentation lookup only. Missing affordance/declaration
        // means no situated copy; absence is not a product UX policy.
        : availableActionId
          ? experimentalJourneyPresentations.find((item) => item.availableActionId === availableActionId)?.message ?? ""
          : "",
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
