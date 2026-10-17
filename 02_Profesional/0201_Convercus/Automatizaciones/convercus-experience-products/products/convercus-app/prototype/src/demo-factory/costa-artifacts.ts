// Composition B for the frozen-baseline H21 experiment. Data only.
import costaLogoUrl from "./costa-clara-logo.svg?url";
import type { BrandArtifact, ScenarioDefinition, DemoScript } from "./contracts";

export const costaBrand: BrandArtifact = {
  id: "costa-clara",
  name: "Costa Clara Resort",
  logoUrl: costaLogoUrl,
  cssVariables: {
    "--color-primary": "#173D59",
    "--color-primary-action": "#245F7D",
    "--color-accent": "#EBC88A",
    "--color-highlight": "#BC7658",
    "--color-background": "#FFFCF6",
    "--color-surface": "#F0EAE0",
    "--color-surface-tinted": "#E5F1F6",
    "--color-text": "#2B3D48",
    "--color-text-strong": "#153044",
    "--color-text-muted": "#576C79",
    "--color-border": "#C4D6DE",
    "--color-focus": "#245F7D",
    "--color-on-primary": "#FFFFFF",
    "--color-on-action": "#FFFFFF",
    "--color-on-accent": "#153044",
    "--font-primary": "system-ui, -apple-system, BlinkMacSystemFont, sans-serif",
  },
};

export const costaScenario: ScenarioDefinition = {
    id: "family-adventure-costa",
    experienceRef: "experience:family-adventure@1",
    subjects: [
      { type: "individual", id: "subject-p1", role: "guest" },
      { type: "individual", id: "subject-p2", role: "guest" },
    ],
    contexts: [
      { type: "property", id: "costa-clara-resort" },
      { type: "booking", id: "CC-205" },
      { type: "stay", id: "stay-CC-205" },
    ],
    checkpoints: ["ready", "clue-a-discovered", "adventure-established"],
    initialCheckpoint: "ready",
    operationalSessionSubjectRef: "subject-p1",
    initialSubjectStates: { "subject-p1": "not-enlisted", "subject-p2": "not-enabled" },
    presenterAction: {
      actionId: "enlist-p1",
      fromCheckpoint: "ready",
      toCheckpoint: "ready",
    },
    actions: [
      {
        actionId: "enlist-p1",
        fromCheckpoint: "ready",
        toCheckpoint: "ready",
        kind: "enlist",
        subjectRef: "subject-p1",
      },
      {
        actionId: "discover-clue-a",
        fromCheckpoint: "ready",
        toCheckpoint: "clue-a-discovered",
        kind: "evidence",
        subjectRef: "subject-p1",
        requiresEnabledSubject: true,
        evidenceType: "treasure_hunt.marker-a",
      },
      {
        actionId: "activate-p2",
        fromCheckpoint: "clue-a-discovered",
        toCheckpoint: "clue-a-discovered",
        kind: "activate",
        subjectRef: "subject-p2",
      },
      {
        actionId: "discover-clue-b",
        fromCheckpoint: "clue-a-discovered",
        toCheckpoint: "adventure-established",
        kind: "evidence",
        subjectRef: "subject-p2",
        requiresEnabledSubject: true,
        evidenceType: "treasure_hunt.marker-b",
      },
    ],
  };

export const costaScript: DemoScript = {
    id: "family-adventure-costa",
    scenarioRef: "scenario:family-adventure-costa@1",
    initialCheckpoint: "ready",
    experimentalIntroductoryFraming: "Una aventura de pistas entre el mirador y el patio.",
    subjectPresentations: [
      { subjectRef: "subject-p1", label: "Inés" },
      { subjectRef: "subject-p2", label: "Mateo" },
    ],
    experimentalJourneyPresentations: [
      { availableActionId: "discover-clue-a", message: "Exploración disponible en el mirador." },
      { availableActionId: "activate-p2", message: "Pista del mirador registrada. La siguiente acción está disponible." },
      { availableActionId: "discover-clue-b", message: "Nueva exploración disponible en el patio." },
    ],
    steps: [
      {
        id: "enlist-p1",
        presenterLabel: "Alistarme",
        expectedCheckpoint: "ready",
        action: {
          type: "scenario_action",
          actionId: "enlist-p1",
          operation: "enlist",
        },
      },
      {
        id: "discover-clue-a",
        presenterLabel: "Encontrar la pista del mirador · Inés",
        activityPresentation: {
          title: "Pista del mirador encontrada",
          description: "Hallazgo registrado.",
        },
        expectedCheckpoint: "clue-a-discovered",
        action: {
          type: "scenario_action",
          actionId: "discover-clue-a",
          evidence: {
            id: "evidence-costa-a-p1",
            type: "treasure_hunt.marker-a",
            occurredAt: "2026-09-12T10:00:00Z",
            source: "demo-control",
            reliability: "confirmed",
            subjects: [{ type: "individual", id: "subject-p1", role: "guest" }],
            contexts: [
              { type: "booking", id: "CC-205" },
              { type: "stay", id: "stay-CC-205" },
            ],
          },
        },
      },
      {
        id: "activate-p2",
        presenterLabel: "Activar a Mateo desde mi cuenta",
        expectedCheckpoint: "clue-a-discovered",
        action: {
          type: "scenario_action",
          actionId: "activate-p2",
          operation: "activate",
        },
      },
      {
        id: "discover-clue-b",
        presenterLabel: "Encontrar la pista del patio · Mateo",
        activityPresentation: {
          title: "Pista del patio encontrada",
          description: "Hallazgo atribuido a Mateo.",
        },
        expectedCheckpoint: "adventure-established",
        action: {
          type: "scenario_action",
          actionId: "discover-clue-b",
          evidence: {
            id: "evidence-costa-b-p2",
            type: "treasure_hunt.marker-b",
            occurredAt: "2026-09-12T10:05:00Z",
            source: "demo-control",
            reliability: "confirmed",
            subjects: [{ type: "individual", id: "subject-p2", role: "guest" }],
            contexts: [
              { type: "booking", id: "CC-205" },
              { type: "stay", id: "stay-CC-205" },
            ],
          },
        },
      },
    ],
  };
