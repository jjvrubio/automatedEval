import type { SportsUserConfiguration } from "./contracts";

// Fictitious data for BUILD 02. No imported customer data or productive programme.
export const sportsUserConfiguration: SportsUserConfiguration = {
  primaryPersonRef: "person:lea",
  people: [
    {
      id: "person:lea", name: "Lea Martín", customerRelationship: "established", membershipStatus: "external",
      knownData: { city: "Valencia", usualSport: "Carrera" },
      purchases: [
        { id: "purchase:lea:1", date: "2026-07-12", description: "Zapatillas para correr", amountCents: 12990 },
        { id: "purchase:lea:2", date: "2026-08-03", description: "Camiseta técnica", amountCents: 3990 },
        { id: "purchase:lea:3", date: "2026-09-05", description: "Botella de hidratación", amountCents: 2500 },
      ],
    },
    {
      id: "person:diego", name: "Diego Vidal", customerRelationship: "established", membershipStatus: "member",
      knownData: { city: "Valencia", usualSport: "Vela y carrera" },
      purchases: [{ id: "purchase:diego:1", date: "2026-08-19", description: "Chaqueta para actividades al aire libre", amountCents: 8900 }],
      program: { points: 860, level: "Activo", benefits: ["Acceso a encuentros del club", "Novedades de actividades deportivas"] },
    },
    { id: "person:visitor", name: "Persona sin identificar", customerRelationship: "not-established", membershipStatus: "external", purchases: [] },
  ],
  counterfactualPointsPerEuro: 1,
  interests: [
    { value: "running", label: "Carrera" }, { value: "sailing", label: "Vela" },
    { value: "volleyball", label: "Vóley playa" }, { value: "next-events", label: "Próximas convocatorias" },
  ],
  frequencies: [
    { value: "occasional", label: "De vez en cuando" }, { value: "weekly", label: "Una vez por semana" },
    { value: "several-weekly", label: "Varias veces por semana" },
  ],
  goals: [
    { value: "wellbeing", label: "Sentirme bien" }, { value: "company", label: "Moverme en compañía" },
    { value: "habit", label: "Mantener el hábito" },
  ],
  incentive: {
    id: "incentive:running-guide", title: "Guía de preparación para 5 km",
    content: [
      "Revisa el lugar de salida y prepara tu equipamiento con antelación.",
      "Elige ropa y calzado que ya conozcas y con los que te sientas cómodo.",
      "Consulta el horario y los servicios disponibles del encuentro.",
      "Comparte el plan con quien vaya a acompañarte.",
    ],
  },
  equipment: [
    { eventRef: "event:running-01", title: "Calzado", description: "Zapatillas para correr que ya hayas utilizado y te resulten cómodas." },
    { eventRef: "event:running-01", title: "Textil técnico", description: "Ropa adecuada al tiempo previsto y al movimiento." },
    { eventRef: "event:running-01", title: "Hidratación", description: "Una botella reutilizable para llevar contigo." },
    { eventRef: "event:running-01", title: "Accesorios", description: "Una gorra o un cinturón para tus pequeños objetos, si los necesitas." },
  ],
};
