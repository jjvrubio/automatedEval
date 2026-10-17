import { describe, expect, it } from "vitest";
import evaluatorSource from "./cross-subject-evidence-admissibility.ts?raw";
import {
  evaluateCrossSubjectEvidenceSufficiency,
  type AuthoritativePremise,
  type CrossSubjectEvaluationContext,
  type CrossSubjectMarkerEvidence,
} from "./cross-subject-evidence-admissibility";
import type { TreasureHuntSufficiencyCriterion } from "./evidence-sufficiency";

const context = Object.freeze({
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
    huntRef: context.huntRef,
    propertyRef: context.propertyRef,
  },
  anchorMarkerRef: "marker-a",
  alternativeMarkerRefs: ["marker-b", "marker-c"],
} as const satisfies TreasureHuntSufficiencyCriterion);

function evidence(
  evidenceRef: string,
  markerRef: string,
  subjectRef: string,
): CrossSubjectMarkerEvidence {
  return Object.freeze({
    evidenceRef,
    markerRef,
    subjectRef,
    huntRef: context.huntRef,
    stayRef: context.stayRef,
    propertyRef: context.propertyRef,
    bookingRef: context.bookingRef,
  });
}

const evidenceAFromP1 = evidence("evidence-a-p1", "marker-a", "subject-p1");
const evidenceBFromP1 = evidence("evidence-b-p1", "marker-b", "subject-p1");
const evidenceBFromP2 = evidence("evidence-b-p2", "marker-b", "subject-p2");
const evidenceCFromP2 = evidence("evidence-c-p2", "marker-c", "subject-p2");
const evidenceBFromP3 = evidence("evidence-b-p3", "marker-b", "subject-p3");

const applicablePremise = Object.freeze({
  premiseRef: "premise-joint-admissibility-p1-p2",
  authorityRef: "product-policy:cross-subject-evaluation@experiment-1",
  scope: context,
  coveredSubjectRefs: ["subject-p1", "subject-p2"],
} as const satisfies AuthoritativePremise);

describe("authority-bounded cross-subject evidence composition", () => {
  it("A — preserves same-subject Session 15 sufficiency without a cross-subject premise", () => {
    const outcome = evaluateCrossSubjectEvidenceSufficiency(
      [evidenceAFromP1, evidenceBFromP1],
      context,
      criterion,
    );

    expect(outcome.jointAdmissibility).toMatchObject({
      determination: "established",
      reason: "same-subject-control",
      premiseRefs: [],
      authorityRefs: [],
    });
    expect(outcome.sufficiency).toMatchObject({
      attempted: true,
      claim: { determination: "established" },
    });
  });

  it("B — evaluates K only after an applicable premise establishes cross-subject admissibility", () => {
    const outcome = evaluateCrossSubjectEvidenceSufficiency(
      [evidenceAFromP1, evidenceBFromP2],
      context,
      criterion,
      applicablePremise,
    );

    expect(outcome.jointAdmissibility).toMatchObject({
      determination: "established",
      reason: "applicable-authoritative-premise",
      premiseRefs: [applicablePremise.premiseRef],
      authorityRefs: [applicablePremise.authorityRef],
    });
    expect(outcome.sufficiency).toMatchObject({
      attempted: true,
      claim: { determination: "established" },
    });
  });

  it("C — does not attempt sufficiency when cross-subject authority is absent", () => {
    const outcome = evaluateCrossSubjectEvidenceSufficiency(
      [evidenceAFromP1, evidenceBFromP2],
      context,
      criterion,
    );

    expect(outcome.jointAdmissibility).toMatchObject({
      determination: "cannot-currently-establish",
      reason: "no-applicable-authoritative-premise",
    });
    expect(outcome.sufficiency).toEqual({ attempted: false });
  });

  it("D — rejects authority laundering from a premise with the wrong scope", () => {
    const wrongScopePremise = {
      ...applicablePremise,
      scope: { ...context, evaluationRef: "evaluation-another" },
    } satisfies AuthoritativePremise;
    const outcome = evaluateCrossSubjectEvidenceSufficiency(
      [evidenceAFromP1, evidenceBFromP2],
      context,
      criterion,
      wrongScopePremise,
    );

    expect(outcome.jointAdmissibility.determination).toBe(
      "cannot-currently-establish",
    );
    expect(outcome.sufficiency.attempted).toBe(false);
  });

  it("E — does not generalize a P1/P2 premise to P1/P3", () => {
    const outcome = evaluateCrossSubjectEvidenceSufficiency(
      [evidenceAFromP1, evidenceBFromP3],
      context,
      criterion,
      applicablePremise,
    );

    expect(outcome.jointAdmissibility.determination).toBe(
      "cannot-currently-establish",
    );
    expect(outcome.sufficiency.attempted).toBe(false);
  });

  it("F — keeps a shared authoritative booking fact distinct from admissibility authority", () => {
    expect(evidenceAFromP1.bookingRef).toBe(context.bookingRef);
    expect(evidenceBFromP2.bookingRef).toBe(context.bookingRef);

    const outcome = evaluateCrossSubjectEvidenceSufficiency(
      [evidenceAFromP1, evidenceBFromP2],
      context,
      criterion,
    );

    expect(outcome.jointAdmissibility.determination).toBe(
      "cannot-currently-establish",
    );
    expect(outcome.sufficiency.attempted).toBe(false);
  });

  it("does not manufacture authority from extra cross-subject Evidence", () => {
    const outcome = evaluateCrossSubjectEvidenceSufficiency(
      [evidenceAFromP1, evidenceBFromP2, evidenceCFromP2],
      context,
      criterion,
    );

    expect(outcome.jointAdmissibility.determination).toBe(
      "cannot-currently-establish",
    );
    expect(outcome.sufficiency.attempted).toBe(false);
  });

  it("keeps attribution, authority, K and collective semantics separate", () => {
    expect(evidenceAFromP1).not.toHaveProperty("premiseRef");
    expect(evidenceAFromP1).not.toHaveProperty("admissible");
    expect(criterion).not.toHaveProperty("coveredSubjectRefs");
    expect(applicablePremise).not.toHaveProperty("anchorMarkerRef");
    expect(applicablePremise).not.toHaveProperty("alternativeMarkerRefs");
    expect(evaluatorSource).not.toContain("composeEvidence");
    expect(evaluatorSource).not.toContain("Group");
    expect(evaluatorSource).not.toContain("Membership");
    expect(evaluatorSource).not.toContain("Participant");
    expect(evaluatorSource).not.toContain("Contributor");
    expect(evaluatorSource).not.toContain("Progression");
    expect(evaluatorSource).not.toContain("Completion");
    expect(evaluatorSource).not.toContain("SignificantEvent");
    expect(evaluatorSource).not.toContain("ActivityItem");
    expect(evaluatorSource).not.toContain("AppSnapshot");
    expect(evaluatorSource).not.toContain("Service");
    expect(evaluatorSource).not.toContain("Registry");
    expect(evaluatorSource).not.toContain("Repository");
  });
});
