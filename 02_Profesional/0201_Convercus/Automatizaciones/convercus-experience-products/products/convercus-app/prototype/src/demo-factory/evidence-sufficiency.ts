export interface DistributedMarkerEvidence {
  readonly evidenceRef: string;
  readonly subjectRef: string;
  readonly huntRef: string;
  readonly stayRef: string;
  readonly propertyRef: string;
  readonly markerRef: string;
}

export interface EvidenceSufficiencyContext {
  readonly subjectRef: string;
  readonly huntRef: string;
  readonly stayRef: string;
  readonly propertyRef: string;
}

export interface TreasureHuntSufficiencyCriterion {
  readonly criterionRef: string;
  readonly authorityRef: string;
  readonly scope: {
    readonly huntRef: string;
    readonly propertyRef: string;
  };
  readonly anchorMarkerRef: string;
  readonly alternativeMarkerRefs: readonly [string, string];
}

export interface AdmittedEvidenceSufficiencyContext {
  readonly huntRef: string;
  readonly propertyRef: string;
}

export interface AdmittedEvidenceSufficiencyClaim {
  readonly determination: "established" | "not-established";
  readonly reason:
    | "criterion-satisfied"
    | "criterion-not-established-by-available-evidence";
  readonly huntRef: string;
  readonly criterionRef: string;
  readonly authorityRef: string;
  readonly consideredEvidenceRefs: readonly string[];
  readonly distinctContributionRefs: readonly string[];
}

export interface EvidenceSufficiencyClaim
  extends AdmittedEvidenceSufficiencyClaim {
  readonly subjectRef: string;
}

export function evaluateAdmittedEvidenceSufficiency(
  admittedEvidence: readonly DistributedMarkerEvidence[],
  context: AdmittedEvidenceSufficiencyContext,
  criterion: TreasureHuntSufficiencyCriterion,
): AdmittedEvidenceSufficiencyClaim {
  const criterionApplies =
    criterion.scope.huntRef === context.huntRef &&
    criterion.scope.propertyRef === context.propertyRef;
  const distinctContributionRefs = [
    ...new Set(admittedEvidence.map(({ markerRef }) => markerRef)),
  ].sort();
  const established =
    criterionApplies &&
    distinctContributionRefs.includes(criterion.anchorMarkerRef) &&
    criterion.alternativeMarkerRefs.some((markerRef) =>
      distinctContributionRefs.includes(markerRef),
    );

  return {
    determination: established ? "established" : "not-established",
    reason: established
      ? "criterion-satisfied"
      : "criterion-not-established-by-available-evidence",
    huntRef: context.huntRef,
    criterionRef: criterion.criterionRef,
    authorityRef: criterion.authorityRef,
    consideredEvidenceRefs: admittedEvidence
      .map(({ evidenceRef }) => evidenceRef)
      .sort(),
    distinctContributionRefs,
  };
}

export function evaluateEvidenceSufficiency(
  availableEvidence: readonly DistributedMarkerEvidence[],
  context: EvidenceSufficiencyContext,
  criterion: TreasureHuntSufficiencyCriterion,
): EvidenceSufficiencyClaim {
  const consideredEvidence = availableEvidence.filter(
    (evidence) =>
      evidence.subjectRef === context.subjectRef &&
      evidence.huntRef === context.huntRef &&
      evidence.stayRef === context.stayRef &&
      evidence.propertyRef === context.propertyRef,
  );
  const claim = evaluateAdmittedEvidenceSufficiency(
    consideredEvidence,
    context,
    criterion,
  );

  return {
    ...claim,
    subjectRef: context.subjectRef,
  };
}
