import { describe, expect, it } from "vitest";
import evaluatorSource from "./evidence-relevance.ts?raw";
import {
  evaluateEvidenceRelevance,
  type ActivityClassificationAuthority,
  type ActivityCompletionEvidence,
  type ExperienceRelevanceContext,
} from "./evidence-relevance";

const cookingClassEvidence = Object.freeze({
  id: "evidence-cooking-class-stay-AS-8842",
  type: "activity.completed",
  participantRef: "guest-lucia-vega",
  stayRef: "stay-AS-8842",
  propertyRef: "aurora-lisboa",
  activityId: "cooking-class",
  occurredAt: "2026-09-13T11:30:00Z",
  source: "staff-validation",
  reliability: "confirmed",
} as const satisfies ActivityCompletionEvidence);

const scenario = {
  stayRef: "stay-AS-8842",
  propertyRef: "aurora-lisboa",
  catalogueVersion: "aurora-activities@1",
  activityCatalogue: ["cooking-class", "yoga"],
} as const;

const familyAdventureContext = Object.freeze({
  experience: {
    definitionRef: "product-experience:family-adventure@candidate-1",
    relevantActivityClassifications: ["shared-hotel-activity"],
  },
  scenario,
} as const satisfies ExperienceRelevanceContext);

const activeChallengeContext = Object.freeze({
  experience: {
    definitionRef: "product-experience:active-challenge@candidate-1",
    relevantActivityClassifications: ["sport-wellness"],
  },
  scenario,
} as const satisfies ExperienceRelevanceContext);

function authority(
  authorityRef: string,
  coverage: ActivityClassificationAuthority["coverage"],
  claims: ActivityClassificationAuthority["claims"],
): ActivityClassificationAuthority {
  return {
    authorityRef,
    competence: "activity-classification",
    scope: {
      propertyRef: scenario.propertyRef,
      catalogueVersion: scenario.catalogueVersion,
    },
    coverage,
    claims,
  };
}

const positiveFamilyAuthority = authority(
  "property-catalogue:aurora@1",
  "incomplete",
  [
    {
      activityId: "cooking-class",
      classification: "shared-hotel-activity",
      relation: "includes",
    },
  ],
);

const explicitActiveExclusion = authority(
  "property-catalogue:aurora@1",
  "incomplete",
  [
    {
      activityId: "cooking-class",
      classification: "sport-wellness",
      relation: "excludes",
    },
  ],
);

const incompleteSharedClassification = authority(
  "property-catalogue:aurora@1",
  "incomplete",
  [
    {
      activityId: "cooking-class",
      classification: "shared-hotel-activity",
      relation: "includes",
    },
  ],
);

const exhaustiveSharedClassification = authority(
  "property-catalogue:aurora@1",
  "exhaustive",
  incompleteSharedClassification.claims,
);

describe("authority-bounded contextual evidence relevance", () => {
  it("keeps Evidence and ExperienceContext constant across authority cases", () => {
    expect(cookingClassEvidence).not.toHaveProperty("experienceRef");
    expect(cookingClassEvidence).not.toHaveProperty("interpretation");
    expect(cookingClassEvidence).not.toHaveProperty("relevant");
    expect(activeChallengeContext).not.toHaveProperty("authority");
    expect(activeChallengeContext.scenario.activityCatalogue).toContain(
      "cooking-class",
    );
  });

  it("supports a positive determination from explicit competent membership", () => {
    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, familyAdventureContext, [
        positiveFamilyAuthority,
      ]),
    ).toEqual({
      evidenceRef: cookingClassEvidence.id,
      experienceRef: familyAdventureContext.experience.definitionRef,
      determination: "positive",
      reason: "authoritative-membership",
      authorityRefs: [positiveFamilyAuthority.authorityRef],
    });
  });

  it("supports a scoped negative from explicit competent exclusion", () => {
    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, activeChallengeContext, [
        explicitActiveExclusion,
      ]),
    ).toMatchObject({
      determination: "negative",
      reason: "explicit-exclusion",
    });
  });

  it("keeps absence in incomplete knowledge undetermined", () => {
    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, activeChallengeContext, [
        incompleteSharedClassification,
      ]),
    ).toMatchObject({
      determination: "undetermined",
      reason: "incomplete-classification-knowledge",
    });
  });

  it("allows a negative from absence only under scoped exhaustive coverage", () => {
    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, activeChallengeContext, [
        exhaustiveSharedClassification,
      ]),
    ).toMatchObject({
      determination: "negative",
      reason: "scoped-exhaustive-absence",
    });
  });

  it("keeps missing competent classification authority undetermined", () => {
    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, activeChallengeContext, []),
    ).toEqual({
      evidenceRef: cookingClassEvidence.id,
      experienceRef: activeChallengeContext.experience.definitionRef,
      determination: "undetermined",
      reason: "missing-classification-authority",
      authorityRefs: [],
    });

    const outOfScopeAuthority = {
      ...explicitActiveExclusion,
      scope: {
        ...explicitActiveExclusion.scope,
        catalogueVersion: "aurora-activities@another-version",
      },
    } satisfies ActivityClassificationAuthority;
    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, activeChallengeContext, [
        outOfScopeAuthority,
      ]),
    ).toMatchObject({
      determination: "undetermined",
      reason: "missing-classification-authority",
      authorityRefs: [],
    });
  });

  it("preserves unresolved conflict without inventing precedence", () => {
    const positiveActiveAuthority = authority(
      "activity-source:wellness@7",
      "incomplete",
      [
        {
          activityId: "cooking-class",
          classification: "sport-wellness",
          relation: "includes",
        },
      ],
    );

    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, activeChallengeContext, [
        positiveActiveAuthority,
        explicitActiveExclusion,
      ]),
    ).toMatchObject({
      determination: "undetermined",
      reason: "conflicting-classification-authority",
      authorityRefs: [
        positiveActiveAuthority.authorityRef,
        explicitActiveExclusion.authorityRef,
      ],
    });
  });

  it("changes the claim only when authority changes", () => {
    const incomplete = evaluateEvidenceRelevance(
      cookingClassEvidence,
      activeChallengeContext,
      [incompleteSharedClassification],
    );
    const exhaustive = evaluateEvidenceRelevance(
      cookingClassEvidence,
      activeChallengeContext,
      [exhaustiveSharedClassification],
    );

    expect(incomplete).toMatchObject({ determination: "undetermined" });
    expect(exhaustive).toMatchObject({ determination: "negative" });
    expect(cookingClassEvidence).toEqual(
      expect.objectContaining({ id: "evidence-cooking-class-stay-AS-8842" }),
    );
    expect(activeChallengeContext).toEqual(
      expect.objectContaining({ scenario }),
    );
  });

  it("does not branch on Experience IDs or use authority-laundering signals", () => {
    const renamedContext = {
      ...familyAdventureContext,
      experience: {
        ...familyAdventureContext.experience,
        definitionRef: "product-experience:renamed-for-test@candidate-1",
      },
    } satisfies ExperienceRelevanceContext;
    const original = evaluateEvidenceRelevance(
      cookingClassEvidence,
      familyAdventureContext,
      [positiveFamilyAuthority],
    );
    const renamed = evaluateEvidenceRelevance(
      cookingClassEvidence,
      renamedContext,
      [positiveFamilyAuthority],
    );

    expect(renamed).toMatchObject({
      determination: original.determination,
      reason: original.reason,
    });
    expect(evaluatorSource).not.toContain("family-adventure");
    expect(evaluatorSource).not.toContain("active-challenge");
    expect(evaluatorSource).not.toContain("tesBaseline");
    expect(evaluatorSource).not.toContain("ExperienceDefinition");
    expect(evaluatorSource).not.toContain("bootstrap");
  });

  it("leaves context gaps undetermined", () => {
    const anotherStay = {
      ...activeChallengeContext,
      scenario: { ...scenario, stayRef: "stay-another" },
    } satisfies ExperienceRelevanceContext;
    const scenarioWithoutActivity = {
      ...activeChallengeContext,
      scenario: { ...scenario, activityCatalogue: ["yoga"] },
    } satisfies ExperienceRelevanceContext;

    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, anotherStay, [
        explicitActiveExclusion,
      ]),
    ).toMatchObject({
      determination: "undetermined",
      reason: "context-insufficient",
    });
    expect(
      evaluateEvidenceRelevance(cookingClassEvidence, scenarioWithoutActivity, [
        explicitActiveExclusion,
      ]),
    ).toMatchObject({
      determination: "undetermined",
      reason: "activity-not-in-scenario",
    });
  });

  it("remains pure, repeatable and independent of evaluation order", () => {
    const evidenceBefore = structuredClone(cookingClassEvidence);
    const contextBefore = structuredClone(activeChallengeContext);
    const authorityBefore = structuredClone(incompleteSharedClassification);
    const first = evaluateEvidenceRelevance(
      cookingClassEvidence,
      activeChallengeContext,
      [incompleteSharedClassification],
    );
    const interleaved = evaluateEvidenceRelevance(
      cookingClassEvidence,
      familyAdventureContext,
      [positiveFamilyAuthority],
    );
    const repeated = evaluateEvidenceRelevance(
      cookingClassEvidence,
      activeChallengeContext,
      [incompleteSharedClassification],
    );

    expect(repeated).toEqual(first);
    expect(interleaved.determination).toBe("positive");
    expect(cookingClassEvidence).toEqual(evidenceBefore);
    expect(activeChallengeContext).toEqual(contextBefore);
    expect(incompleteSharedClassification).toEqual(authorityBefore);
  });

  it("keeps Activity downstream and unable to alter epistemic status", () => {
    const outcome = evaluateEvidenceRelevance(
      cookingClassEvidence,
      activeChallengeContext,
      [incompleteSharedClassification],
    );
    const projectedCopy = { label: "No determinado", sourceOutcome: outcome };

    expect(evaluatorSource).not.toContain("ActivityItem");
    expect(evaluatorSource).not.toContain("ActivitySourceRecord");
    expect(evaluatorSource).not.toContain("projectSnapshot");
    expect(projectedCopy.sourceOutcome).toBe(outcome);
    expect(projectedCopy.sourceOutcome.determination).toBe("undetermined");
  });
});
