import {
  evaluateAdmittedEvidenceSufficiency,
  type AdmittedEvidenceSufficiencyClaim,
  type DistributedMarkerEvidence,
  type TreasureHuntSufficiencyCriterion,
} from "./evidence-sufficiency";

export interface CrossSubjectEvaluationContext {
  readonly evaluationRef: string;
  readonly huntRef: string;
  readonly stayRef: string;
  readonly propertyRef: string;
  readonly bookingRef: string;
}

export interface CrossSubjectMarkerEvidence
  extends DistributedMarkerEvidence {
  readonly bookingRef: string;
}

export interface AuthoritativePremise {
  readonly premiseRef: string;
  readonly authorityRef: string;
  readonly scope: CrossSubjectEvaluationContext;
  readonly coveredSubjectRefs: readonly string[];
}

export type JointAdmissibilityOutcome =
  | {
      readonly determination: "established";
      readonly reason:
        | "same-subject-control"
        | "applicable-authoritative-premise";
      readonly evidenceRefs: readonly string[];
      readonly premiseRefs: readonly string[];
      readonly authorityRefs: readonly string[];
    }
  | {
      readonly determination: "cannot-currently-establish";
      readonly reason: "no-applicable-authoritative-premise";
      readonly evidenceRefs: readonly string[];
      readonly premiseRefs: readonly string[];
      readonly authorityRefs: readonly string[];
    };

export type CrossSubjectSufficiencyEvaluation = {
  readonly jointAdmissibility: JointAdmissibilityOutcome;
  readonly sufficiency:
    | { readonly attempted: false }
    | {
        readonly attempted: true;
        readonly claim: AdmittedEvidenceSufficiencyClaim;
      };
};

function hasSameScope(
  first: CrossSubjectEvaluationContext,
  second: CrossSubjectEvaluationContext,
): boolean {
  return (
    first.evaluationRef === second.evaluationRef &&
    first.huntRef === second.huntRef &&
    first.stayRef === second.stayRef &&
    first.propertyRef === second.propertyRef &&
    first.bookingRef === second.bookingRef
  );
}

export function evaluateJointAdmissibility(
  availableEvidence: readonly CrossSubjectMarkerEvidence[],
  context: CrossSubjectEvaluationContext,
  authoritativePremise?: AuthoritativePremise,
): JointAdmissibilityOutcome {
  const situatedEvidence = availableEvidence.filter(
    (evidence) =>
      evidence.huntRef === context.huntRef &&
      evidence.stayRef === context.stayRef &&
      evidence.propertyRef === context.propertyRef &&
      evidence.bookingRef === context.bookingRef,
  );
  const evidenceRefs = situatedEvidence
    .map(({ evidenceRef }) => evidenceRef)
    .sort();
  const subjectRefs = [
    ...new Set(situatedEvidence.map(({ subjectRef }) => subjectRef)),
  ];

  if (subjectRefs.length <= 1) {
    return {
      determination: "established",
      reason: "same-subject-control",
      evidenceRefs,
      premiseRefs: [],
      authorityRefs: [],
    };
  }

  const premiseApplies =
    authoritativePremise !== undefined &&
    hasSameScope(authoritativePremise.scope, context) &&
    subjectRefs.every((subjectRef) =>
      authoritativePremise.coveredSubjectRefs.includes(subjectRef),
    );

  if (premiseApplies) {
    return {
      determination: "established",
      reason: "applicable-authoritative-premise",
      evidenceRefs,
      premiseRefs: [authoritativePremise.premiseRef],
      authorityRefs: [authoritativePremise.authorityRef],
    };
  }

  return {
    determination: "cannot-currently-establish",
    reason: "no-applicable-authoritative-premise",
    evidenceRefs,
    premiseRefs: [],
    authorityRefs: [],
  };
}

export function evaluateCrossSubjectEvidenceSufficiency(
  availableEvidence: readonly CrossSubjectMarkerEvidence[],
  context: CrossSubjectEvaluationContext,
  criterion: TreasureHuntSufficiencyCriterion,
  authoritativePremise?: AuthoritativePremise,
): CrossSubjectSufficiencyEvaluation {
  const jointAdmissibility = evaluateJointAdmissibility(
    availableEvidence,
    context,
    authoritativePremise,
  );

  if (jointAdmissibility.determination !== "established") {
    return { jointAdmissibility, sufficiency: { attempted: false } };
  }

  const admittedRefs = new Set(jointAdmissibility.evidenceRefs);
  const admittedEvidence = availableEvidence.filter(({ evidenceRef }) =>
    admittedRefs.has(evidenceRef),
  );

  return {
    jointAdmissibility,
    sufficiency: {
      attempted: true,
      claim: evaluateAdmittedEvidenceSufficiency(
        admittedEvidence,
        context,
        criterion,
      ),
    },
  };
}
