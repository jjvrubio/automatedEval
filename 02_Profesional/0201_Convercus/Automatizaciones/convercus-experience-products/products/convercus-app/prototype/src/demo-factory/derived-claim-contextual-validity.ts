import type {
  AdmittedEvidenceSufficiencyClaim,
} from "./evidence-sufficiency";

export interface ExperimentalClaimContext {
  readonly scopeRef: string;
  readonly evaluationRef: string;
  readonly huntRef: string;
  readonly stayRef: string;
  readonly propertyRef: string;
  readonly bookingRef: string;
}

export interface AuthoritativeContextualUseBasis {
  readonly basisRef: string;
  readonly authorityRef: string;
  readonly claimCriterionRef: string;
  readonly fromScopeRef: string;
  readonly toScopeRef: string;
}

export type DerivedClaimContextualApplicability =
  | {
      readonly determination: "established";
      readonly reason:
        | "same-derivation-context"
        | "authoritative-directional-use-basis";
      readonly claimCriterionRef: string;
      readonly derivationScopeRef: string;
      readonly requestedScopeRef: string;
      readonly basisRef?: string;
      readonly authorityRef?: string;
    }
  | {
      readonly determination: "cannot-currently-establish";
      readonly reason:
        | "claim-not-established"
        | "different-context-without-applicable-authority"
        | "no-applicable-directional-use-basis";
      readonly claimCriterionRef: string;
      readonly derivationScopeRef: string;
      readonly requestedScopeRef: string;
      readonly basisRef?: string;
      readonly authorityRef?: string;
    };

function hasSameExperimentalContext(
  first: ExperimentalClaimContext,
  second: ExperimentalClaimContext,
): boolean {
  return (
    first.scopeRef === second.scopeRef &&
    first.evaluationRef === second.evaluationRef &&
    first.huntRef === second.huntRef &&
    first.stayRef === second.stayRef &&
    first.propertyRef === second.propertyRef &&
    first.bookingRef === second.bookingRef
  );
}

export function evaluateDerivedClaimContextualApplicability(
  claim: AdmittedEvidenceSufficiencyClaim,
  derivationContext: ExperimentalClaimContext,
  requestedContext: ExperimentalClaimContext,
  authoritativeUseBasis?: AuthoritativeContextualUseBasis,
): DerivedClaimContextualApplicability {
  const base = {
    claimCriterionRef: claim.criterionRef,
    derivationScopeRef: derivationContext.scopeRef,
    requestedScopeRef: requestedContext.scopeRef,
  } as const;

  if (claim.determination !== "established") {
    return {
      ...base,
      determination: "cannot-currently-establish",
      reason: "claim-not-established",
    };
  }

  if (!hasSameExperimentalContext(derivationContext, requestedContext)) {
    const basisApplies =
      authoritativeUseBasis !== undefined &&
      authoritativeUseBasis.claimCriterionRef === claim.criterionRef &&
      authoritativeUseBasis.fromScopeRef === derivationContext.scopeRef &&
      authoritativeUseBasis.toScopeRef === requestedContext.scopeRef;

    if (basisApplies) {
      return {
        ...base,
        determination: "established",
        reason: "authoritative-directional-use-basis",
        basisRef: authoritativeUseBasis.basisRef,
        authorityRef: authoritativeUseBasis.authorityRef,
      };
    }

    return {
      ...base,
      determination: "cannot-currently-establish",
      reason: "no-applicable-directional-use-basis",
    };
  }

  return {
    ...base,
    determination: "established",
    reason: "same-derivation-context",
  };
}
