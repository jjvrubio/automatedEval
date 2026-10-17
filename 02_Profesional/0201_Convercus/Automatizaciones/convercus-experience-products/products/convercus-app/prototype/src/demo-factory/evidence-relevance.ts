import type { EvidenceInput } from "./contracts";

export type ActivityClassification =
  | "shared-hotel-activity"
  | "sport-wellness";

export interface ActivityCompletionEvidence {
  readonly id: string;
  readonly type: "activity.completed";
  readonly participantRef: string;
  readonly stayRef: string;
  readonly propertyRef: string;
  readonly activityId: string;
  readonly occurredAt: string;
  readonly source: string;
  readonly reliability: EvidenceInput["reliability"];
}

export interface ExperienceRelevanceContext {
  readonly experience: {
    readonly definitionRef: string;
    readonly relevantActivityClassifications: readonly ActivityClassification[];
  };
  readonly scenario: {
    readonly stayRef: string;
    readonly propertyRef: string;
    readonly catalogueVersion: string;
    readonly activityCatalogue: readonly string[];
  };
}

export interface ActivityClassificationAuthority {
  readonly authorityRef: string;
  readonly competence: "activity-classification";
  readonly scope: {
    readonly propertyRef: string;
    readonly catalogueVersion: string;
  };
  readonly coverage: "incomplete" | "exhaustive";
  readonly claims: readonly {
    readonly activityId: string;
    readonly classification: ActivityClassification;
    readonly relation: "includes" | "excludes";
  }[];
}

interface EvidenceRelevanceOutcomeBase {
  readonly evidenceRef: string;
  readonly experienceRef: string;
  readonly authorityRefs: readonly string[];
}

export type EvidenceRelevanceOutcome =
  | (EvidenceRelevanceOutcomeBase & {
      readonly determination: "positive";
      readonly reason: "authoritative-membership";
    })
  | (EvidenceRelevanceOutcomeBase & {
      readonly determination: "negative";
      readonly reason: "explicit-exclusion" | "scoped-exhaustive-absence";
    })
  | (EvidenceRelevanceOutcomeBase & {
      readonly determination: "undetermined";
      readonly reason:
        | "context-insufficient"
        | "activity-not-in-scenario"
        | "missing-classification-authority"
        | "incomplete-classification-knowledge"
        | "conflicting-classification-authority";
    });

export function evaluateEvidenceRelevance(
  evidence: ActivityCompletionEvidence,
  context: ExperienceRelevanceContext,
  availableAuthorities: readonly ActivityClassificationAuthority[],
): EvidenceRelevanceOutcome {
  const outcome = (
    determination: EvidenceRelevanceOutcome["determination"],
    reason: EvidenceRelevanceOutcome["reason"],
    authorityRefs: readonly string[] = [],
  ): EvidenceRelevanceOutcome => ({
    evidenceRef: evidence.id,
    experienceRef: context.experience.definitionRef,
    determination,
    reason,
    authorityRefs,
  }) as EvidenceRelevanceOutcome;

  if (
    evidence.stayRef !== context.scenario.stayRef ||
    evidence.propertyRef !== context.scenario.propertyRef
  ) {
    return outcome("undetermined", "context-insufficient");
  }

  if (!context.scenario.activityCatalogue.includes(evidence.activityId)) {
    return outcome("undetermined", "activity-not-in-scenario");
  }

  const scopedAuthorities = availableAuthorities.filter(
    (authority) =>
      authority.scope.propertyRef === context.scenario.propertyRef &&
      authority.scope.catalogueVersion === context.scenario.catalogueVersion,
  );

  if (scopedAuthorities.length === 0) {
    return outcome("undetermined", "missing-classification-authority");
  }

  const relevantClassifications =
    context.experience.relevantActivityClassifications;
  const authorityRefs = scopedAuthorities.map(({ authorityRef }) => authorityRef);
  const hasPositive = scopedAuthorities.some((authority) =>
    authority.claims.some(
      (claim) =>
        claim.activityId === evidence.activityId &&
        claim.relation === "includes" &&
        relevantClassifications.includes(claim.classification),
    ),
  );
  const hasExplicitNegative = relevantClassifications.every((classification) =>
    scopedAuthorities.some((authority) =>
      authority.claims.some(
        (claim) =>
          claim.activityId === evidence.activityId &&
          claim.classification === classification &&
          claim.relation === "excludes",
      ),
    ),
  );
  const hasExhaustiveNegative = scopedAuthorities.some(
    (authority) =>
      authority.coverage === "exhaustive" &&
      !authority.claims.some(
        (claim) =>
          claim.activityId === evidence.activityId &&
          claim.relation === "includes" &&
          relevantClassifications.includes(claim.classification),
      ),
  );

  if (hasPositive && (hasExplicitNegative || hasExhaustiveNegative)) {
    return outcome(
      "undetermined",
      "conflicting-classification-authority",
      authorityRefs,
    );
  }

  if (hasPositive) {
    return outcome("positive", "authoritative-membership", authorityRefs);
  }

  if (hasExplicitNegative) {
    return outcome("negative", "explicit-exclusion", authorityRefs);
  }

  if (hasExhaustiveNegative) {
    return outcome("negative", "scoped-exhaustive-absence", authorityRefs);
  }

  return outcome(
    "undetermined",
    "incomplete-classification-knowledge",
    authorityRefs,
  );
}
