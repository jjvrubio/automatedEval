import { describe, expect, it } from "vitest";
import evaluatorSource from "./evidence-sufficiency.ts?raw";
import {
  evaluateEvidenceSufficiency,
  type DistributedMarkerEvidence,
  type EvidenceSufficiencyContext,
  type TreasureHuntSufficiencyCriterion,
} from "./evidence-sufficiency";

const context = Object.freeze({
  subjectRef: "business-guest-p",
  huntRef: "treasure-hunt-t",
  stayRef: "stay-s",
  propertyRef: "business-hotel-h",
} as const satisfies EvidenceSufficiencyContext);

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
): DistributedMarkerEvidence {
  return Object.freeze({ evidenceRef, markerRef, ...context });
}

const evidenceA = evidence("evidence-a", "marker-a");
const evidenceB = evidence("evidence-b", "marker-b");
const evidenceC = evidence("evidence-c", "marker-c");
const duplicateEvidenceA = evidence("evidence-a-duplicate-record", "marker-a");

describe("distributed evidence sufficiency", () => {
  it("keeps each factual Evidence independent and neutral", () => {
    for (const item of [evidenceA, evidenceB, evidenceC]) {
      expect(item).not.toHaveProperty("sufficient");
      expect(item).not.toHaveProperty("progress");
      expect(item).not.toHaveProperty("percentage");
      expect(item).not.toHaveProperty("solved");
      expect(item).not.toHaveProperty("completed");
      expect(item).not.toHaveProperty("reward");
    }
  });

  it.each([
    ["A — no evidence", [], "not-established"],
    ["B — A only", [evidenceA], "not-established"],
    ["single B", [evidenceB], "not-established"],
    ["single C", [evidenceC], "not-established"],
    ["C — B + C", [evidenceB, evidenceC], "not-established"],
    ["D — A + B", [evidenceA, evidenceB], "established"],
    ["E — A + C", [evidenceA, evidenceC], "established"],
    ["F — A + A", [evidenceA, duplicateEvidenceA], "not-established"],
    ["H — A + B + C", [evidenceA, evidenceB, evidenceC], "established"],
  ] as const)("evaluates case %s under criterion K", (_case, items, expected) => {
    expect(evaluateEvidenceSufficiency(items, context, criterion)).toMatchObject({
      determination: expected,
      subjectRef: context.subjectRef,
      huntRef: context.huntRef,
      criterionRef: criterion.criterionRef,
      authorityRef: criterion.authorityRef,
    });
  });

  it("treats duplicate records as one semantic contribution", () => {
    const outcome = evaluateEvidenceSufficiency(
      [evidenceA, duplicateEvidenceA],
      context,
      criterion,
    );

    expect(outcome.consideredEvidenceRefs).toEqual([
      duplicateEvidenceA.evidenceRef,
      evidenceA.evidenceRef,
    ].sort());
    expect(outcome.distinctContributionRefs).toEqual(["marker-a"]);
    expect(outcome.determination).toBe("not-established");
  });

  it("is independent of Evidence order for unordered clues", () => {
    const forward = evaluateEvidenceSufficiency(
      [evidenceA, evidenceB],
      context,
      criterion,
    );
    const reverse = evaluateEvidenceSufficiency(
      [evidenceB, evidenceA],
      context,
      criterion,
    );

    expect(reverse).toEqual(forward);
  });

  it("does not strengthen the claim when extra Evidence is present", () => {
    const sufficient = evaluateEvidenceSufficiency(
      [evidenceA, evidenceB],
      context,
      criterion,
    );
    const withExtraEvidence = evaluateEvidenceSufficiency(
      [evidenceA, evidenceB, evidenceC],
      context,
      criterion,
    );

    expect(withExtraEvidence.determination).toBe(sufficient.determination);
    expect(withExtraEvidence.reason).toBe(sufficient.reason);
    expect(withExtraEvidence).not.toHaveProperty("strength");
    expect(withExtraEvidence).not.toHaveProperty("progress");
  });

  it("does not establish sufficiency from out-of-scope criteria or Evidence", () => {
    const outOfScopeCriterion = {
      ...criterion,
      scope: { ...criterion.scope, propertyRef: "another-property" },
    } satisfies TreasureHuntSufficiencyCriterion;
    const outOfContextEvidence = {
      ...evidenceB,
      propertyRef: "another-property",
    } satisfies DistributedMarkerEvidence;

    expect(
      evaluateEvidenceSufficiency(
        [evidenceA, evidenceB],
        context,
        outOfScopeCriterion,
      ).determination,
    ).toBe("not-established");
    expect(
      evaluateEvidenceSufficiency(
        [evidenceA, outOfContextEvidence],
        context,
        criterion,
      ).determination,
    ).toBe("not-established");
  });

  it("keeps relevance, Activity, incentives and TES semantics outside the boundary", () => {
    expect(evaluatorSource).not.toContain("evaluateEvidenceRelevance");
    expect(evaluatorSource).not.toContain("ActivityItem");
    expect(evaluatorSource).not.toContain("AppSnapshot");
    expect(evaluatorSource).not.toContain("ExperienceDefinition");
    expect(evaluatorSource).not.toContain("SignificantEvent");
    expect(evaluatorSource).not.toContain("Progression");
    expect(evaluatorSource).not.toContain("Completion");
    expect(evaluatorSource).not.toContain("Incentive");
    expect(evaluatorSource).not.toContain("Reward");
    expect(evaluatorSource).not.toContain("Engine");
    expect(evaluatorSource).not.toContain("marker-a");
  });
});
