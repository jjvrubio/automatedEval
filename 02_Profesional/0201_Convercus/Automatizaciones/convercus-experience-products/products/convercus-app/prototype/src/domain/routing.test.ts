import { describe, expect, it } from "vitest";
import type {
  EventEvaluationRule,
  ExperienceParticipation,
  SignificantEvent,
} from "./contracts";
import { evaluateEventAcrossExperiences } from "./routing";

const event: SignificantEvent = {
  id: "event-1",
  type: "qr.scan.confirmed",
  occurredAt: "2026-07-17T10:00:00Z",
  source: "mock",
  reliability: "confirmed",
  properties: {},
};

const participations: ExperienceParticipation[] = [
  {
    id: "participation-a",
    experienceId: "experience-a",
    memberId: "member-1",
    state: "exploring",
    progression: 0.25,
    status: "active",
    updatedAt: "2026-07-17T09:00:00Z",
  },
  {
    id: "participation-b",
    experienceId: "experience-b",
    memberId: "member-1",
    state: "eligible",
    progression: 0,
    status: "active",
    updatedAt: "2026-07-17T09:00:00Z",
  },
];

function rule(experienceId: string, effect: "progression" | "none"): EventEvaluationRule {
  return {
    id: `rule-${experienceId}`,
    experienceId,
    accepts: () => true,
    evaluate: (_event, participation) => ({
      experienceId,
      participationId: participation.id,
      ruleId: `rule-${experienceId}`,
      effect,
      explanation: effect === "none" ? "Sin efecto en esta participación" : "Avance confirmado",
    }),
  };
}

describe("event routing", () => {
  it("evaluates a shared event independently for each Experience", () => {
    const effects = evaluateEventAcrossExperiences(event, participations, [
      rule("experience-a", "progression"),
      rule("experience-b", "none"),
    ]);

    expect(effects).toHaveLength(2);
    expect(effects.map(({ effect }) => effect)).toEqual(["progression", "none"]);
    expect(effects[0]?.participationId).not.toBe(effects[1]?.participationId);
  });
});

