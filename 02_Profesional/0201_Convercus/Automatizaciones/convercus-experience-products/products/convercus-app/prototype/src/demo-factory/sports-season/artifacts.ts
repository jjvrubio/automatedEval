import type { BrandArtifact, DemoManifest } from "../contracts";
import type { SportsSeasonScenario } from "./contracts";
import logoUrl from "./brisa-logo.svg?url";

export const sportsBrand: BrandArtifact = {
  id: "brisa-sport",
  name: "Brisa Sport",
  logoUrl,
  cssVariables: {
    "--color-primary": "#090685",
    "--color-primary-action": "#092BFD",
    "--color-accent": "#0AEFFF",
    "--color-highlight": "#F72585",
    "--color-background": "#FFFFFF",
    "--color-surface": "#F1F1F1",
    "--color-text": "#333333",
    "--color-text-strong": "#000000",
    "--color-text-muted": "#5F5F5F",
    "--color-border": "#5F5F5F",
    "--color-focus": "#092BFD",
    "--color-on-primary": "#FFFFFF",
    "--color-on-action": "#FFFFFF",
    "--color-on-accent": "#000000",
    "--font-primary": '"Sofia Sans", system-ui, sans-serif',
  },
};

// One situated season, not a schema or editor for arbitrary sports programs.
export const sportsSeasonScenario: SportsSeasonScenario = {
  id: "scenario:brisa-sports-season@1",
  fixtureRef: "fixture:brisa-external-runner@1",
  person: { id: "person:lea", name: "Lea Martín", membershipStatus: "external", customerRelationship: "not-established" },
  contrastPerson: { id: "person:diego", name: "Diego Vidal", membershipStatus: "member", customerRelationship: "not-established" },
  season: {
    id: "season:brisa-autumn-2026",
    title: "Una temporada para moverse",
    dates: "Septiembre — noviembre 2026",
    introduction: "En tierra, en el agua o en la arena. Encuentra una forma de participar y hazla tuya.",
  },
  events: [
    { id: "event:running-01", seasonRef: "season:brisa-autumn-2026", discipline: "running", label: "Carrera", title: "Kilómetros en compañía", date: "2026-10-24", place: "Paseo del litoral · 5 km",
      description: "A tu ritmo. Una mañana para compartir o dedicarte tiempo.", executable: true },
    { id: "event:sailing-01", seasonRef: "season:brisa-autumn-2026", discipline: "sailing", label: "Vela", title: "Un horizonte compartido", date: "2026-10-17", place: "Escuela de vela",
      description: "Otra forma de vivir la temporada. Evento informativo en esta demo.", executable: false },
    { id: "event:volleyball-01", seasonRef: "season:brisa-autumn-2026", discipline: "beach-volleyball", label: "Vóley playa", title: "Nos vemos en la arena", date: "2026-11-07", place: "Playa deportiva",
      description: "Una jornada organizada por equipos. Evento informativo, sin juego ni reconocimientos colectivos en esta demo.", executable: false },
  ],
  modalities: [
    { value: "social", label: "Social", description: "Compartir el recorrido y disfrutar en compañía." },
    { value: "wellness", label: "Bienestar", description: "Dedicarte un momento y moverte a tu ritmo." },
  ],
  efforts: [{ value: "suave", label: "Suave" }, { value: "medio", label: "Medio" }, { value: "intenso", label: "Intenso" }],
  badge: {
    id: "badge:brisa-first-running@1",
    title: "Primeros kilómetros",
    reason: "Por inscribirte en Carrera, registrar el check-in simulado y compartir el esfuerzo de esta participación.",
  },
  club: {
    name: "Club Brisa",
    invitation: "La próxima salida puede ser el comienzo de algo más.",
    description: "Brisa Sport ya cuenta con un club. Conoce sus novedades y próximas actividades; participar en esta carrera no te da de alta.",
  },
};

export const sportsSeasonManifest: DemoManifest = {
  schemaVersion: 1,
  demoId: "sports-season-running",
  prospectId: "brisa-sport-fictional",
  locale: "es",
  brandRef: "brand:brisa-sport@1",
  fixtureRef: sportsSeasonScenario.fixtureRef,
  scenarioRef: sportsSeasonScenario.id,
  sportsSeasonRef: sportsSeasonScenario.id,
  visibleModules: ["home"],
  requestedCapabilities: [
    { id: "sports-participation", label: "Participación deportiva situada", expectedStatus: "simulated" },
    { id: "sports-crm-view", label: "Lectura Marketing / CRM", expectedStatus: "simulated" },
  ],
};
