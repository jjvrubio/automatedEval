import { costaBrand, costaScenario, costaScript } from "./costa-artifacts";
import auroraStayLogoUrl from "./aurora-stay-logo.svg?url";
import { brand, brandAssets, getBrandCssVariables } from "@/config/brand";
import type {
  BrandArtifact,
  DemoScript,
  ExperienceDefinition,
  ScenarioDefinition,
} from "./contracts";

export const brands: Record<string, BrandArtifact> = {
  "brand:costa-clara@1": costaBrand,
  "brand:convercus@1": {
    id: "convercus",
    name: brand.name,
    logoUrl: brandAssets.logoPrimaryUrl,
    cssVariables: getBrandCssVariables(brand),
  },
  "brand:aurora-stay@1": {
    id: "aurora-stay",
    name: "Aurora Stay",
    logoUrl: auroraStayLogoUrl,
    cssVariables: {
      "--color-primary": "#173F3A",
      "--color-primary-action": "#236B60",
      "--color-accent": "#F6C177",
      "--color-highlight": "#D96C4F",
      "--color-background": "#FFFDF8",
      "--color-surface": "#F3EEE4",
      "--color-surface-tinted": "#E1F0EA",
      "--color-text": "#26332F",
      "--color-text-strong": "#102622",
      "--color-text-muted": "#586A65",
      "--color-border": "#C9D8D3",
      "--color-focus": "#236B60",
      "--color-on-primary": "#FFFFFF",
      "--color-on-action": "#FFFFFF",
      "--color-on-accent": "#102622",
      "--font-primary": "system-ui, -apple-system, BlinkMacSystemFont, sans-serif",
    },
  },
};

export const experiences: Record<string, ExperienceDefinition> = {
  "experience:arrival-welcome@1": {
    id: "arrival-welcome",
    name: "Llegada acompañada",
    tesBaseline: "TES_CONVERCUS_BUILDER_2026_07_R1",
  },
  "experience:family-adventure@1": {
    id: "family-adventure",
    name: "Aventura Familiar",
    tesBaseline: "TES_CONVERCUS_BUILDER_2026_07_R1",
  },
};

export const scenarios: Record<string, ScenarioDefinition> = {
  "scenario:family-adventure-costa@1": costaScenario,
  "scenario:arrival-and-stay@1": {
    id: "arrival-and-stay",
    experienceRef: "experience:arrival-welcome@1",
    subjects: [
      { type: "individual", id: "guest-lucia-vega", role: "booking-holder" },
      { type: "group", id: "travelling-party-8842", role: "accompanying-guests" },
    ],
    contexts: [
      { type: "property", id: "aurora-lisboa" },
      { type: "booking", id: "AS-8842" },
      { type: "stay", id: "stay-AS-8842" },
    ],
    checkpoints: ["pre-arrival-confirmed", "checked-in"],
    initialCheckpoint: "pre-arrival-confirmed",
    presenterAction: {
      actionId: "confirm-arrival",
      fromCheckpoint: "pre-arrival-confirmed",
      toCheckpoint: "checked-in",
    },
  },
  "scenario:family-adventure@1": {
    id: "family-adventure",
    experienceRef: "experience:family-adventure@1",
    subjects: [
      { type: "individual", id: "subject-p1", role: "guest" },
      { type: "individual", id: "subject-p2", role: "guest" },
    ],
    contexts: [
      { type: "property", id: "aurora-resort" },
      { type: "booking", id: "AS-8842" },
      { type: "stay", id: "stay-AS-8842" },
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
  },
};

export const scripts: Record<string, DemoScript> = {
  "script:family-adventure-costa@1": costaScript,
  "script:hospitality-check-in@1": {
    id: "hospitality-check-in",
    scenarioRef: "scenario:arrival-and-stay@1",
    initialCheckpoint: "pre-arrival-confirmed",
    steps: [
      {
        id: "confirm-check-in",
        presenterLabel: "Confirmar llegada",
        expectedCheckpoint: "checked-in",
        action: {
          type: "scenario_action",
          actionId: "confirm-arrival",
          evidence: {
            id: "evidence-check-in-AS-8842",
            type: "booking.checked_in",
            occurredAt: "2026-09-12T15:05:00Z",
            source: "demo-control",
            reliability: "confirmed",
            subjects: [
              { type: "individual", id: "guest-lucia-vega", role: "booking-holder" },
              { type: "group", id: "travelling-party-8842", role: "accompanying-guests" },
            ],
            contexts: [
              { type: "booking", id: "AS-8842" },
              { type: "stay", id: "stay-AS-8842" },
            ],
            interpretation: {
              id: "event-arrival-AS-8842",
              type: "guest_arrived",
              experienceRef: "experience:arrival-welcome@1",
            },
          },
        },
      },
    ],
  },
  "script:family-adventure@1": {
    id: "family-adventure",
    scenarioRef: "scenario:family-adventure@1",
    initialCheckpoint: "ready",
    subjectPresentations: [
      { subjectRef: "subject-p1", label: "Lucía" },
      { subjectRef: "subject-p2", label: "Huésped 2" },
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
        presenterLabel: "Encontrar la pista del jardín · yo",
        activityPresentation: {
          title: "Pista del jardín encontrada",
          description: "Hallazgo aportado por ti.",
        },
        expectedCheckpoint: "clue-a-discovered",
        action: {
          type: "scenario_action",
          actionId: "discover-clue-a",
          evidence: {
            id: "evidence-a-p1",
            type: "treasure_hunt.marker-a",
            occurredAt: "2026-09-12T10:00:00Z",
            source: "demo-control",
            reliability: "confirmed",
            subjects: [{ type: "individual", id: "subject-p1", role: "guest" }],
            contexts: [
              { type: "booking", id: "AS-8842" },
              { type: "stay", id: "stay-AS-8842" },
            ],
          },
        },
      },
      {
        id: "activate-p2",
        presenterLabel: "Activar al huésped 2 desde mi cuenta",
        expectedCheckpoint: "clue-a-discovered",
        action: {
          type: "scenario_action",
          actionId: "activate-p2",
          operation: "activate",
        },
      },
      {
        id: "discover-clue-b",
        presenterLabel: "Encontrar la pista de la fuente · huésped 2",
        activityPresentation: {
          title: "Pista de la fuente encontrada",
          description: "Hallazgo atribuido al huésped 2, registrado desde tu cuenta.",
        },
        expectedCheckpoint: "adventure-established",
        action: {
          type: "scenario_action",
          actionId: "discover-clue-b",
          evidence: {
            id: "evidence-b-p2",
            type: "treasure_hunt.marker-b",
            occurredAt: "2026-09-12T10:05:00Z",
            source: "demo-control",
            reliability: "confirmed",
            subjects: [{ type: "individual", id: "subject-p2", role: "guest" }],
            contexts: [
              { type: "booking", id: "AS-8842" },
              { type: "stay", id: "stay-AS-8842" },
            ],
          },
        },
      },
    ],
  },
};
