import csv from "./data/sports_season_transactions_v0_1.csv?raw";
import loyaltyJson from "./data/sports_season_loyalty_dataset_v0_1.json?raw";
import type loyaltyShape from "./data/sports_season_loyalty_dataset_v0_1.json";
import type { CommerceTransaction, NormalizedSportsData, Person, SportsDataAdapter } from "./relationship-contract";
import type { SportsUserConfiguration } from "./contracts";
import { sportsUserConfiguration } from "./user-plane-artifacts";

// Identity is situated configuration: neither supplied dataset contains names.
const people: Person[] = [
  { id: "P01", name: "Lea Martín", customerRelationship: "established", knownData: { city: "Valencia", usualSport: "Carrera" } },
  { id: "P02", name: "Diego Vidal", customerRelationship: "established", knownData: { city: "Valencia", usualSport: "Vela y carrera" } },
  { id: "P03", name: "Persona sin identificar", customerRelationship: "not-established" },
];
function requireData(condition: unknown, detail: string): asserts condition {
  if (!condition) throw new Error(`Fixtures incompatibles: ${detail}. Carga detenida; no se reconcilian datos.`);
}
const cents = (value: string | number) => {
  const text = String(value);
  requireData(/^\d+(\.\d{1,2})?$/.test(text), "importe no válido");
  const [whole, fraction = ""] = text.split(".");
  const result = Number(whole) * 100 + Number(fraction.padEnd(2, "0"));
  requireData(Number.isSafeInteger(result), "importe fuera de rango");
  return result;
};
const sameRefs = (left: string[], right: string[]) =>
  left.length === right.length && new Set(left).size === left.length && [...left].sort().join("|") === [...right].sort().join("|");

// Quoted cells, escaped quotes, CRLF and UTF-8 BOM supported. Malformed records stop loading.
export function parseTransactionCSV(text: string): CommerceTransaction[] {
  const rows: string[][] = [];
  let row: string[] = [], cell = "", quoted = false, closed = false;
  const input = text.replace(/^\uFEFF/, "").replace(/\r\n/g, "\n");
  for (let i = 0; i < input.length; i++) {
    const ch = input[i];
    if (ch === '"') {
      if (quoted && input[i + 1] === '"') { cell += '"'; i++; }
      else if (quoted) { quoted = false; closed = true; }
      else { requireData(!cell && !closed, "comillas CSV"); quoted = true; }
    } else if (!quoted && (ch === "," || ch === "\n")) {
      row.push(cell); cell = ""; closed = false;
      if (ch === "\n") { rows.push(row); row = []; }
    } else {
      requireData(!closed, "texto tras cierre CSV");
      cell += ch;
    }
  }
  requireData(!quoted, "celda CSV sin cerrar");
  if (cell || row.length) { row.push(cell); rows.push(row); }
  const headers = rows.shift() ?? [];
  const expected = ["transaction_id","person_id","occurred_at","channel","store_id","currency","gross_amount","product_category","product_name","quantity","unit_amount","line_amount","source","observed_at"];
  requireData(headers.join(",") === expected.join(","), "cabecera CSV");
  return rows.map(values => {
    requireData(values.length === headers.length, "columnas CSV");
    const r = Object.fromEntries(headers.map((key, i) => [key, values[i]]));
    requireData(r.transaction_id && r.person_id && r.product_name && r.product_category, "campos comerciales vacíos");
    requireData(Number.isFinite(Date.parse(r.occurred_at)) && Number.isFinite(Date.parse(r.observed_at)), "fecha comercial");
    const quantity = Number(r.quantity), grossCents = cents(r.gross_amount), unitCents = cents(r.unit_amount);
    requireData(Number.isSafeInteger(quantity) && quantity > 0 && quantity * unitCents === cents(r.line_amount) && grossCents === cents(r.line_amount), "importe de línea");
    requireData(r.currency === "EUR" && ["store", "web", "app"].includes(r.channel) && r.source === "fixture", "canal, moneda o procedencia");
    return { id: r.transaction_id, personRef: r.person_id, occurredAt: r.occurred_at, channel: r.channel, storeRef: r.store_id, currency: r.currency, grossCents, category: r.product_category, product: r.product_name, quantity, unitCents, observedAt: r.observed_at };
  });
}

export class FixtureAdapter implements SportsDataAdapter {
  constructor(private readonly transactionCSV = csv, private readonly loyaltyJSON = loyaltyJson) {}
  load(): NormalizedSportsData {
    const transactions = parseTransactionCSV(this.transactionCSV);
    let raw: typeof loyaltyShape;
    try { raw = JSON.parse(this.loyaltyJSON); } catch { throw new Error("JSON de fidelización inválido. Carga detenida."); }
    requireData(raw && raw.program && raw.dataset && ["loyalty_states", "commercial_summaries", "loyalty_counterfactuals", "badges", "coupons", "news", "experiences"].every(key => Array.isArray(raw[key as keyof typeof raw])), "estructura JSON");
    requireData(raw.dataset.currency === "EUR" && raw.dataset.basis_transaction_dataset === "sports_season_transactions_v0_1.csv", "dataset de base");
    const rule = raw.program.points_rule;
    requireData(rule.points_per_full_eur === 1 && rule.rounding === "floor" && rule.calculation_basis === "aggregate_eligible_gross_spend" && rule.eligible_currency === "EUR" && rule.eligible_categories === "all_categories_in_transaction_fixture", "regla situada no soportada");
    requireData(Array.isArray(raw.program.levels) && raw.program.levels.length > 0, "niveles");
    const levels = raw.program.levels.map(l => ({ id: l.level_id, name: l.name, minPoints: l.min_points, maxPoints: l.max_points, benefits: l.benefits }));
    const levelFor = (points: number) => levels.find(l => points >= l.minPoints && (l.maxPoints === null || points <= l.maxPoints));
    const personIds = new Set(people.map(p => p.id));
    const unique = (ids: string[], label: string) => requireData(ids.every(Boolean) && new Set(ids).size === ids.length, label + " duplicados");
    unique(transactions.map(t => t.id), "transacciones");
    unique(raw.loyalty_states.map(l => l.person_id), "estados");
    unique(raw.commercial_summaries.map(s => s.person_id), "resúmenes");
    unique(raw.loyalty_counterfactuals.map(c => c.person_id), "contrafactuales");
    unique(raw.badges.map(b => b.badge_id), "insignias");
    unique(raw.coupons.map(c => c.coupon_id), "cupones");
    unique(raw.news.map(n => n.news_id), "noticias");
    unique(raw.experiences.map(e => e.person_id + ":" + e.experience_id), "Experiences");
    for (const ref of [...transactions.map(t => t.personRef), ...[raw.loyalty_states, raw.commercial_summaries, raw.loyalty_counterfactuals, raw.badges, raw.coupons, raw.experiences].flatMap(items => items.map(i => i.person_id))]) requireData(personIds.has(ref), "person_id desconocido");
    const loyaltyStates = raw.loyalty_states.map(l => {
      requireData(l.program_id === raw.program.program_id, "program_id");
      requireData(l.membership_status === "active" || l.membership_status === "non_member", "membresía");
      if (l.membership_status === "non_member") requireData(l.points_balance === null && l.level === null && l.membership_id === null, "no miembro con saldo o nivel");
      else requireData(Number.isSafeInteger(l.points_balance) && l.points_balance! >= 0 && l.level && levelFor(l.points_balance!)?.id === l.level.level_id && levelFor(l.points_balance!)?.name === l.level.name && l.membership_id, "saldo o nivel de miembro");
      return { personRef: l.person_id, membershipStatus: l.membership_status as "active" | "non_member", membershipId: l.membership_id, joinedAt: l.joined_at, pointsBalance: l.points_balance, actualLevel: l.level ? { id: l.level.level_id, name: l.level.name } : null };
    });
    for (const person of people) {
      requireData(loyaltyStates.some(l => l.personRef === person.id), "persona sin fidelización");
      const txs = transactions.filter(t => t.personRef === person.id);
      const summary = raw.commercial_summaries.find(s => s.person_id === person.id);
      requireData(person.customerRelationship === "established" ? txs.length > 0 && summary : txs.length === 0, "relación comercial");
      if (summary) requireData(summary.transaction_count === txs.length && cents(summary.gross_spend) === txs.reduce((n,t) => n + t.grossCents,0) && summary.currency === "EUR" && sameRefs(summary.basis_transaction_ids, txs.map(t => t.id)), "CSV / resumen JSON " + person.id);
    }
    const counterfactuals = raw.loyalty_counterfactuals.map(c => {
      const txs = transactions.filter(t => t.personRef === c.person_id && rule.eligible_channels.includes(t.channel));
      const total = txs.reduce((n,t) => n + t.grossCents,0);
      const points = Math.floor(total / 100) * rule.points_per_full_eur;
      requireData(loyaltyStates.find(l => l.personRef === c.person_id)?.membershipStatus === "non_member" && c.program_id === raw.program.program_id && c.currency === "EUR", "atribución contrafactual");
      requireData(sameRefs(c.basis_transaction_ids, txs.map(t => t.id)) && cents(c.basis_amount) === total && c.hypothetical_points === points && c.hypothetical_level.level_id === levelFor(points)?.id && c.hypothetical_level.name === levelFor(points)?.name && c.rule_set_version === rule.rule_set_version, "CSV / contrafactual JSON");
      return { id: c.counterfactual_id, personRef: c.person_id, basisTransactionRefs: c.basis_transaction_ids, basisCents: total, hypotheticalPoints: c.hypothetical_points, hypotheticalLevel: { id: c.hypothetical_level.level_id, name: c.hypothetical_level.name }, hypotheticalBenefits: c.hypothetical_benefits, disclaimer: c.display_disclaimer, credited: false as const };
    });
    requireData(counterfactuals.some(c => c.personRef === "P01"), "falta contrafactual primario");
    requireData(loyaltyStates.find(l => l.personRef === "P01")?.membershipStatus === "non_member" && loyaltyStates.find(l => l.personRef === "P02")?.membershipStatus === "active" && loyaltyStates.find(l => l.personRef === "P03")?.membershipStatus === "non_member", "situaciones de persona");
    const experiences = raw.experiences.map(e => {
      requireData(["available","enrolled","active","completed"].includes(e.person_state), "estado Experience");
      return { id: e.experience_id, personRef: e.person_id, name: e.name, state: e.person_state as NormalizedSportsData["experiences"][number]["state"], eligibility: e.eligibility };
    });
    return structuredClone({
      people, transactions, loyaltyStates, counterfactuals,
      program: { id: raw.program.program_id, name: raw.program.name, pointsPerFullEuro: rule.points_per_full_eur, levels },
      badges: raw.badges.map(b => ({ id: b.badge_id, personRef: b.person_id, title: b.name, awardedAt: b.awarded_at, origin: "loyalty_program" as const })),
      coupons: raw.coupons.map(c => ({ id: c.coupon_id, personRef: c.person_id, title: c.title, status: c.status, validFrom: c.valid_from, validUntil: c.valid_until })),
      news: raw.news.filter(n => n.status === "published").map(n => ({ id: n.news_id, title: n.title, summary: n.summary, publishedAt: n.published_at })),
      experiences,
    });
  }
}

// Keep the earlier user-plane fixture for historical replay; only editorial configuration is reused.
export function userConfigurationFor(data: NormalizedSportsData): SportsUserConfiguration {
  return {
    ...structuredClone(sportsUserConfiguration),
    primaryPersonRef: data.people[0].id,
    people: data.people.map(person => ({
      ...person, purchases: [],
      membershipStatus: data.loyaltyStates.find(l => l.personRef === person.id)?.membershipStatus === "active" ? "member" : "external",
    })),
    counterfactualPointsPerEuro: data.program.pointsPerFullEuro,
    interests: [...sportsUserConfiguration.interests, { value: "improvement", label: "Sesiones de mejora" }, { value: "sports-news", label: "Novedades deportivas" }],
  };
}
