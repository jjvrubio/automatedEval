import type { NormalizedSportsData, PersonRelationship } from "./relationship-contract";
import type { EffortLevel, SportsDemoAction, SportsBadge, SportsDemoPerson, SportsEvidence, SportsModality, SportsProvider, SportsRegistration, SportsSeasonScenario, SportsSnapshot, SportsUserAction, SportsUserConfiguration, SportsUserSnapshot } from "./contracts";

export const sportsBadgeRuleRef = "sports-season:accepted-registration-presence-effort@1";
const modalities: readonly string[] = ["social", "wellness"];
const efforts: readonly string[] = ["suave", "medio", "intenso"];

// LOCAL / EXPERIMENTAL / NOT PROMOTED. No TES or hotel evaluator dependency.
function recognize(
  registration: SportsRegistration,
  evidence: SportsEvidence[],
  scenario: SportsSeasonScenario,
): SportsBadge | undefined {
  const belongs = (item: SportsEvidence) => item.personRef === registration.personRef &&
    item.eventRef === registration.eventRef && item.registrationRef === registration.registrationId;
  const presence = evidence.find((item) => belongs(item) && item.kind === "presence" && item.source === "simulated-check-in");
  const effort = evidence.find((item) => belongs(item) && item.kind === "effort" &&
    item.source === "participant-self-report" && efforts.includes(item.level));
  if (registration.status !== "accepted" || !presence || !effort) return undefined;
  return {
    badgeId: scenario.badge.id, personRef: registration.personRef, eventRef: registration.eventRef,
    registrationRef: registration.registrationId, ruleRef: sportsBadgeRuleRef,
    supportingEvidenceRefs: [presence.evidenceId, effort.evidenceId],
    title: scenario.badge.title, reason: scenario.badge.reason,
  };
}

export class SportsSeasonProvider implements SportsProvider {
  private readonly scenario: SportsSeasonScenario;
  private registration?: SportsRegistration;
  private evidence: SportsEvidence[] = [];
  private badge?: SportsBadge;
  private readonly userConfiguration?: SportsUserConfiguration;
  private selectedPersonRef?: string;
  private intention?: SportsUserSnapshot["intention"];
  private selectedEventRef?: string;
  private registrationEntry?: SportsUserSnapshot["registrationEntry"];
  private visitorName?: string;
  private declaredInterests?: SportsUserSnapshot["declaredInterests"];
  private voluntary?: SportsUserSnapshot["voluntary"];
  private execution = 0;
  private readonly relationshipData?: NormalizedSportsData;
  private journeys = new Map<string, {
    registration?: SportsRegistration; evidence: SportsEvidence[]; badge?: SportsBadge;
    intention?: SportsUserSnapshot["intention"]; selectedEventRef?: string;
    registrationEntry?: SportsUserSnapshot["registrationEntry"]; visitorName?: string;
    declaredInterests?: SportsUserSnapshot["declaredInterests"]; voluntary?: SportsUserSnapshot["voluntary"];
  }>();

  constructor(scenario: SportsSeasonScenario, private readonly now: () => string = () => new Date().toISOString(), userConfiguration?: SportsUserConfiguration, relationshipData?: NormalizedSportsData) {
    this.relationshipData = relationshipData ? structuredClone(relationshipData) : undefined;
    const runnable = scenario.events.filter((event) => event.executable);
    if (scenario.person.membershipStatus !== "external" || scenario.contrastPerson.id === scenario.person.id ||
        runnable.length !== 1 || runnable[0].discipline !== "running" ||
        scenario.events.some((event) => event.seasonRef !== scenario.season.id) ||
        new Set(scenario.events.map((event) => event.id)).size !== scenario.events.length ||
        scenario.modalities.length !== 2 || new Set(scenario.modalities.map((item) => item.value)).size !== 2 ||
        scenario.modalities.some((item) => !modalities.includes(item.value)) ||
        scenario.efforts.length !== 3 || new Set(scenario.efforts.map((item) => item.value)).size !== 3 ||
        scenario.efforts.some((item) => !efforts.includes(item.value))) {
      throw new Error("Configuración incompatible con el corte local de Carrera.");
    }
    this.scenario = structuredClone(scenario);
    if (userConfiguration) {
      const people = userConfiguration.people;
      const primary = people.find((person) => person.id === userConfiguration.primaryPersonRef);
      if (!primary || primary.customerRelationship !== "established" || primary.membershipStatus !== "external" ||
          new Set(people.map((person) => person.id)).size !== people.length ||
          !people.some((person) => person.membershipStatus === "member") ||
          !people.some((person) => person.customerRelationship === "not-established") ||
          !Number.isSafeInteger(userConfiguration.counterfactualPointsPerEuro) || userConfiguration.counterfactualPointsPerEuro < 1 ||
          people.some((person) => !person.id || !person.name.trim() ||
            (person.membershipStatus === "member" && (person.customerRelationship !== "established" || (!person.program && !relationshipData?.loyaltyStates.some(l => l.personRef === person.id && l.membershipStatus === "active")))) ||
            (person.membershipStatus === "external" && person.program) ||
            (person.customerRelationship === "not-established" && (person.purchases.length > 0 || person.knownData)) ||
            person.purchases.some((purchase) => !Number.isSafeInteger(purchase.amountCents) || purchase.amountCents < 0)) ||
          userConfiguration.equipment.some((item) => item.eventRef !== runnable[0].id)) {
        throw new Error("Configuración de personas incompatible con el plano usuario.");
      }
      this.userConfiguration = structuredClone(userConfiguration);
    }
  }

  private person(): SportsDemoPerson | undefined {
    const person = this.userConfiguration?.people.find((item) => item.id === this.selectedPersonRef);
    return person ? { ...person, name: this.visitorName ?? person.name } : undefined;
  }

  private userSnapshot(): SportsUserSnapshot | undefined {
    const configuration = this.userConfiguration;
    if (!configuration) return undefined;
    const person = this.person();
    const totalCents = person?.purchases.reduce((sum, item) => sum + item.amountCents, 0) ?? 0;
    return {
      configuration, person, relationship: person ? this.relationship(person.id) : undefined, intention: this.intention, selectedEventRef: this.selectedEventRef,
      registrationEntry: this.registrationEntry, visitorIdentified: Boolean(this.visitorName),
      declaredInterests: this.declaredInterests, voluntary: this.voluntary,
      counterfactual: !this.relationshipData && person?.customerRelationship === "established" && person.membershipStatus === "external"
        ? { totalCents, potentialPoints: Math.floor(totalCents / 100 * configuration.counterfactualPointsPerEuro), credited: false } : undefined,
      incentive: person && this.voluntary?.decision === "provided" ? {
        ...configuration.incentive, personRef: person.id, source: "voluntary-information",
      } : undefined,
      recommendations: this.intention === "participate" ? configuration.equipment.filter((item) => item.eventRef === this.selectedEventRef) : [],
    };
  }

  private relationship(personRef: string): PersonRelationship | undefined {
    const data = this.relationshipData;
    if (!data) return undefined;
    const transactions = data.transactions.filter(t => t.personRef === personRef);
    const loyalty = data.loyaltyStates.find(l => l.personRef === personRef);
    if (!loyalty) throw new Error("No existe estado de fidelización para esta persona.");
    const badges = data.badges.filter(b => b.personRef === personRef);
    if (this.badge) badges.push({
      id: this.badge.registrationRef + ":badge", personRef, title: this.badge.title,
      origin: "sports_season", awardedAt: this.evidence.find(e => e.kind === "effort")!.occurredAt,
      eventRef: this.badge.eventRef, registrationRef: this.badge.registrationRef,
      supportingEvidenceRefs: [...this.badge.supportingEvidenceRefs],
    });
    const experiences = data.experiences.filter(e => e.personRef === personRef);
    const event = this.scenario.events.find(e => e.id === this.registration?.eventRef);
    if (event) experiences.push({ id: event.id, personRef, eventRef: event.id,
      name: event.title, eligibility: "OPEN",
      state: this.badge ? "completed" : this.evidence.length ? "active" : "enrolled" });
    return { program: data.program, transactions, totalCents: transactions.reduce((sum,t) => sum + t.grossCents,0),
      loyalty, counterfactual: data.counterfactuals.find(c => c.personRef === personRef),
      badges, coupons: data.coupons.filter(c => c.personRef === personRef), news: data.news, experiences };
  }

  async getSnapshot(): Promise<SportsSnapshot> {
    const person = this.person();
    const scenario = person ? { ...this.scenario, person: {
      id: person.id, name: person.name, membershipStatus: person.membershipStatus, customerRelationship: person.customerRelationship,
    } } : this.scenario;
    return structuredClone({
      scenario: this.relationshipData ? { ...scenario, club: { ...scenario.club, name: this.relationshipData.program.name } } : scenario,
      criterion: { ruleRef: sportsBadgeRuleRef, explanation: "Inscripción aceptada, presencia simulada y esfuerzo autodeclarado para la misma persona y el mismo evento." },
      registration: this.registration,
      evidence: this.evidence,
      badge: this.badge,
      opportunity: this.badge && scenario.person.membershipStatus === "external" ? {
        id: `invitation:${this.badge.registrationRef}`,
        personRef: this.badge.personRef, registrationRef: this.badge.registrationRef,
        badgeRef: this.badge.badgeId, kind: "club-invitation" as const, status: "available" as const,
      } : undefined,
      stage: this.badge ? "recognized" : this.evidence.length ? "presence-received" : this.registration ? "registered" : "available",
      userPlane: this.userSnapshot(),
    });
  }

  async executeAction(action: SportsDemoAction): Promise<SportsSnapshot> {
    if (!action) throw new Error("Esta acción no está disponible en la demo.");
    if (action.type !== "sports-register" && action.type !== "sports-check-in" && action.type !== "sports-effort") return this.executeUserAction(action);
    const person = this.person();
    if (this.userConfiguration && !person) throw new Error("Selecciona una persona antes de participar.");
    if (action.personRef !== (person ?? this.scenario.person).id) throw new Error("La acción no corresponde a este participante.");
    const event = this.scenario.events.find((item) => item.id === action.eventRef);
    if (!event?.executable || event.discipline !== "running") throw new Error("Elige el evento de Carrera disponible.");
    if (this.userConfiguration && (this.intention !== "participate" || this.selectedEventRef !== event.id)) {
      throw new Error("Elige Participar y selecciona Carrera antes de inscribirte.");
    }

    if (action.type === "sports-register") {
      if (this.registration) throw new Error("La inscripción ya está confirmada. Reinicia la demo para empezar de nuevo.");
      if (!modalities.includes(action.selectedModality)) throw new Error("Elige Social o Bienestar para confirmar la inscripción.");
      if (person?.customerRelationship === "not-established" && !this.visitorName) throw new Error("Indica un nombre ficticio para esta inscripción.");
      this.registration = {
        registrationId: `registration:${this.scenario.id}:${this.userConfiguration ? `${this.execution}:${action.personRef}` : "1"}`,
        personRef: action.personRef, eventRef: action.eventRef,
        selectedModality: action.selectedModality as SportsModality, status: "accepted",
      };
      return this.getSnapshot();
    }

    const registration = this.registration;
    if (!registration) throw new Error("Confirma la inscripción antes de registrar la participación.");
    if (registration.registrationId !== action.registrationRef || registration.eventRef !== action.eventRef) {
      throw new Error("La acción no corresponde a esta inscripción y evento.");
    }
    if (action.type === "sports-check-in") {
      if (this.evidence.length) throw new Error("El check-in simulado ya está registrado.");
      if (this.userConfiguration && !this.voluntary) throw new Error("Comparte la información voluntaria o elige continuar sin aportarla.");
      const presence: SportsEvidence = {
        evidenceId: `${registration.registrationId}:presence`, kind: "presence",
        personRef: action.personRef, eventRef: action.eventRef, registrationRef: action.registrationRef,
        occurredAt: this.now(), source: "simulated-check-in", simulation: true,
      };
      this.evidence = [presence];
    } else {
      if (!this.evidence.some((item) => item.kind === "presence")) throw new Error("Registra primero el check-in simulado.");
      if (this.badge || this.evidence.some((item) => item.kind === "effort")) throw new Error("El esfuerzo ya está registrado.");
      if (!efforts.includes(action.level)) throw new Error("Elige un esfuerzo: suave, medio o intenso.");
      const effort: SportsEvidence = {
        evidenceId: `${registration.registrationId}:effort`, kind: "effort",
        personRef: action.personRef, eventRef: action.eventRef, registrationRef: action.registrationRef,
        occurredAt: this.now(), source: "participant-self-report", simulation: true, level: action.level as EffortLevel,
      };
      const nextEvidence = [...this.evidence, effort];
      const badge = recognize(registration, nextEvidence, this.scenario);
      if (!badge) throw new Error("No se puede establecer el reconocimiento con estos registros.");
      this.evidence = nextEvidence;
      this.badge = badge;
    }
    return this.getSnapshot();
  }

  private async executeUserAction(action: SportsUserAction): Promise<SportsSnapshot> {
    const configuration = this.userConfiguration;
    if (!configuration) throw new Error("Esta acción no está disponible en la demo.");
    if (action.type === "sports-select-person") {
      if (!configuration.people.some((person) => person.id === action.personRef)) throw new Error("Elige una persona de esta demo.");
      if (this.selectedPersonRef === action.personRef) return this.getSnapshot();
      const entry = !this.selectedPersonRef ? this.registrationEntry : undefined;
      if (this.relationshipData && this.selectedPersonRef) this.journeys.set(this.selectedPersonRef, structuredClone({
        registration: this.registration, evidence: this.evidence, badge: this.badge,
        intention: this.intention, selectedEventRef: this.selectedEventRef, registrationEntry: this.registrationEntry,
        visitorName: this.visitorName, declaredInterests: this.declaredInterests, voluntary: this.voluntary,
      }));
      this.clear();
      this.selectedPersonRef = action.personRef;
      const saved = this.journeys.get(action.personRef);
      if (saved) {
        Object.assign(this, structuredClone(saved));
        this.journeys.delete(action.personRef); // The active journey has one owner.
      }
      if (entry) this.registrationEntry = { ...entry, recognized: this.person()?.customerRelationship === "established" };
      return this.getSnapshot();
    }
    if (action.type === "sports-registration-qr") {
      const event = this.scenario.events.find((item) => item.id === action.eventRef && item.executable);
      if (!event || this.registration || this.intention === "information") throw new Error("El QR de inscripción está disponible antes de inscribirte. Reinicia para probar otro recorrido.");
      this.registrationEntry = { eventRef: event.id, source: "simulated-registration-qr", recognized: this.person()?.customerRelationship === "established" };
      if (this.intention === "participate") this.selectedEventRef = event.id;
      return this.getSnapshot();
    }
    const person = this.person();
    if (!person || action.personRef !== person.id) throw new Error("La acción no corresponde a la persona seleccionada.");
    switch (action.type) {
      case "sports-identify-visitor": {
        if (person.customerRelationship === "established" || this.registration) throw new Error("Los datos de esta persona ya están disponibles.");
        const name = typeof action.name === "string" ? action.name.trim() : "";
        if (name.length < 2 || name.length > 80) throw new Error("Escribe un nombre ficticio de entre 2 y 80 caracteres.");
        this.visitorName = name;
        break;
      }
      case "sports-intention":
        if (!["participate", "information"].includes(action.intention)) throw new Error("Elige Participar o Recibir información.");
        if (this.intention && this.intention !== action.intention) throw new Error("Reinicia el recorrido para probar otra intención.");
        this.intention = action.intention as SportsUserSnapshot["intention"];
        if (this.intention === "participate" && this.registrationEntry) this.selectedEventRef = this.registrationEntry.eventRef;
        break;
      case "sports-select-event":
        if (this.intention !== "participate" || this.registration || !this.scenario.events.some((event) => event.id === action.eventRef && event.executable)) throw new Error("Elige Participar y el evento de Carrera disponible.");
        this.selectedEventRef = action.eventRef;
        break;
      case "sports-interests":
        if (this.intention !== "information" || !Array.isArray(action.values) || action.values.length === 0 ||
            new Set(action.values).size !== action.values.length || action.values.some((value) => !configuration.interests.some((item) => item.value === value))) throw new Error("Elige al menos un interés de la lista, dentro de Recibir información.");
        this.declaredInterests = { personRef: person.id, values: [...action.values], source: this.relationshipData ? "user_declared" : "person-declared", occurredAt: this.now() };
        break;
      case "sports-voluntary":
        if (!this.registration || this.intention !== "participate" || this.voluntary) throw new Error("La información voluntaria se decide una vez, después de la inscripción.");
        if (action.decision !== "provided" && action.decision !== "skipped") throw new Error("Elige compartir información o continuar sin aportarla.");
        if (action.decision === "skipped" && (action.frequency || action.goal)) throw new Error("Continuar sin información no registra respuestas.");
        if (action.decision === "provided" && ((!action.frequency && !action.goal) ||
            (action.frequency && !configuration.frequencies.some((item) => item.value === action.frequency)) ||
            (action.goal && !configuration.goals.some((item) => item.value === action.goal)))) throw new Error("Selecciona al menos una respuesta voluntaria válida o continúa sin aportarla.");
        this.voluntary = { personRef: person.id, decision: action.decision, frequency: action.frequency || undefined, goal: action.goal || undefined, source: this.relationshipData ? "user_declared" : "person-declared", occurredAt: this.now() };
        break;
      default: throw new Error("Esta acción no está disponible en la demo.");
    }
    return this.getSnapshot();
  }

  private clear(): void {
    this.registration = undefined;
    this.evidence = [];
    this.badge = undefined;
    this.selectedPersonRef = undefined;
    this.intention = undefined;
    this.selectedEventRef = undefined;
    this.registrationEntry = undefined;
    this.visitorName = undefined;
    this.declaredInterests = undefined;
    this.voluntary = undefined;
    this.execution += 1;
  }

  async reset(): Promise<SportsSnapshot> {
    this.journeys.clear();
    this.clear();
    return this.getSnapshot();
  }
}
