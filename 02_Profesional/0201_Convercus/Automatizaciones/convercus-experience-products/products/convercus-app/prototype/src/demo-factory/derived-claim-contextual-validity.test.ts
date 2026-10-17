import { describe, expect, it } from "vitest";
import {
  evaluateDerivedClaimContextualApplicability,
  type AuthoritativeContextualUseBasis,
  type ExperimentalClaimContext,
} from "./derived-claim-contextual-validity";
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

const sharedEvaluationContext = Object.freeze({
  evaluationRef: "evaluation-t-1",
  huntRef: "treasure-hunt-t",
  stayRef: "stay-s",
  propertyRef: "business-hotel-h",
  bookingRef: "booking-b17",
} as const satisfies CrossSubjectEvaluationContext);

const criterion = Object.freeze({
  criterionRef: "criterion-k",
  authorityRef: "scenario-policy:t@experiment-1",
  scope: {
    huntRef: sharedEvaluationContext.huntRef,
    propertyRef: sharedEvaluationContext.propertyRef,
  },
  anchorMarkerRef: "marker-a",
  alternativeMarkerRefs: ["marker-b", "marker-c"],
} as const satisfies TreasureHuntSufficiencyCriterion);

const claimContexts = {
  S1: Object.freeze({
    scopeRef: "S1",
    ...sharedEvaluationContext,
  }),
  S2: Object.freeze({
    scopeRef: "S2",
    ...sharedEvaluationContext,
  }),
  S3: Object.freeze({
    scopeRef: "S3",
    ...sharedEvaluationContext,
  }),
} as const satisfies Record<string, ExperimentalClaimContext>;

function evidence(
  evidenceRef: string,
  markerRef: string,
  subjectRef: string,
): CrossSubjectMarkerEvidence {
  return Object.freeze({
    evidenceRef,
    markerRef,
    subjectRef,
    huntRef: sharedEvaluationContext.huntRef,
    stayRef: sharedEvaluationContext.stayRef,
    propertyRef: sharedEvaluationContext.propertyRef,
    bookingRef: sharedEvaluationContext.bookingRef,
  });
}

const evidenceAFromP1 = evidence("evidence-a-p1", "marker-a", "subject-p1");
const evidenceBFromP2 = evidence("evidence-b-p2", "marker-b", "subject-p2");

const premiseForS1 = Object.freeze({
  premiseRef: "premise-joint-admissibility-p1-p2-s1",
  authorityRef: "product-policy:cross-subject-evaluation@experiment-1",
  scope: sharedEvaluationContext,
  coveredSubjectRefs: ["subject-p1", "subject-p2"],
} as const satisfies AuthoritativePremise);

const useBasisS1ToS2 = Object.freeze({
  basisRef: "claim-use:s1-to-s2",
  authorityRef: "product-policy:claim-use@experiment-1",
  claimCriterionRef: "criterion-k",
  fromScopeRef: "S1",
  toScopeRef: "S2",
} as const satisfies AuthoritativeContextualUseBasis);

const useBasisS1ToS3 = Object.freeze({
  ...useBasisS1ToS2,
  basisRef: "claim-use:s1-to-s3",
  toScopeRef: "S3",
} as const satisfies AuthoritativeContextualUseBasis);

function deriveClaimInS1(): AdmittedEvidenceSufficiencyClaim {
  const outcome = evaluateCrossSubjectEvidenceSufficiency(
    [evidenceAFromP1, evidenceBFromP2],
    sharedEvaluationContext,
    criterion,
    premiseForS1,
  );

  expect(outcome.jointAdmissibility.determination).toBe("established");
  expect(outcome.sufficiency).toMatchObject({ attempted: true });

  if (!outcome.sufficiency.attempted) {
    throw new Error("Expected an established claim for the S1 fixture");
  }

  return outcome.sufficiency.claim;
}

describe("Session 18 — derived claim contextual validity", () => {
  it("A — applies an established claim in its derivation context", () => {
    const result = evaluateDerivedClaimContextualApplicability(
      deriveClaimInS1(),
      claimContexts.S1,
      claimContexts.S1,
    );

    expect(result).toMatchObject({
      determination: "established",
      reason: "same-derivation-context",
      derivationScopeRef: "S1",
      requestedScopeRef: "S1",
    });
  });

  it("B — does not transfer the S1 claim to distinct S2 without a use basis", () => {
    const result = evaluateDerivedClaimContextualApplicability(
      deriveClaimInS1(),
      claimContexts.S1,
      claimContexts.S2,
    );

    expect(result).toMatchObject({
      determination: "cannot-currently-establish",
      reason: "no-applicable-directional-use-basis",
      derivationScopeRef: "S1",
      requestedScopeRef: "S2",
    });
  });

  it("C — establishes S1 to S2 use with an explicit directional basis", () => {
    const result = evaluateDerivedClaimContextualApplicability(
      deriveClaimInS1(),
      claimContexts.S1,
      claimContexts.S2,
      useBasisS1ToS2,
    );

    expect(result).toMatchObject({
      determination: "established",
      reason: "authoritative-directional-use-basis",
      basisRef: useBasisS1ToS2.basisRef,
      authorityRef: useBasisS1ToS2.authorityRef,
      derivationScopeRef: "S1",
      requestedScopeRef: "S2",
    });
  });

  it("D — rejects a basis authorized for another destination", () => {
    const result = evaluateDerivedClaimContextualApplicability(
      deriveClaimInS1(),
      claimContexts.S1,
      claimContexts.S2,
      useBasisS1ToS3,
    );

    expect(result).toMatchObject({
      determination: "cannot-currently-establish",
      reason: "no-applicable-directional-use-basis",
    });
  });

  it("E — keeps identical Evidence, subjects and booking from transferring without a basis", () => {
    const claim = deriveClaimInS1();
    const subjects = [evidenceAFromP1.subjectRef, evidenceBFromP2.subjectRef];
    const result = evaluateDerivedClaimContextualApplicability(
      claim,
      claimContexts.S1,
      claimContexts.S2,
    );

    expect(subjects).toEqual(["subject-p1", "subject-p2"]);
    expect(claim.consideredEvidenceRefs).toHaveLength(2);
    expect(claimContexts.S1.bookingRef).toBe(claimContexts.S2.bookingRef);
    expect(result).toMatchObject({
      determination: "cannot-currently-establish",
      reason: "no-applicable-directional-use-basis",
    });
  });

  it("F — does not make an unestablished claim applicable", () => {
    const unestablishedClaim: AdmittedEvidenceSufficiencyClaim = {
      ...deriveClaimInS1(),
      determination: "not-established",
      reason: "criterion-not-established-by-available-evidence",
    };

    const result = evaluateDerivedClaimContextualApplicability(
      unestablishedClaim,
      claimContexts.S1,
      claimContexts.S1,
      useBasisS1ToS2,
    );

    expect(result).toMatchObject({
      determination: "cannot-currently-establish",
      reason: "claim-not-established",
    });
  });
});
