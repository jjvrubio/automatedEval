import type {
  EventEvaluationRule,
  ExperienceEffect,
  ExperienceParticipation,
  SignificantEvent,
} from "./contracts";

export function evaluateEventAcrossExperiences(
  event: SignificantEvent,
  participations: ExperienceParticipation[],
  rules: EventEvaluationRule[],
): ExperienceEffect[] {
  return participations.flatMap((participation) =>
    rules
      .filter(
        (rule) =>
          rule.experienceId === participation.experienceId &&
          rule.accepts(event, participation),
      )
      .map((rule) => rule.evaluate(event, participation)),
  );
}

