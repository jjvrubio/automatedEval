import { describe, expect, it } from "vitest";
import csv from "./data/sports_season_transactions_v0_1.csv?raw";
import json from "./data/sports_season_loyalty_dataset_v0_1.json?raw";
import { FixtureAdapter, parseTransactionCSV, userConfigurationFor } from "./fixture-adapter";
import { SportsSeasonProvider } from "./runtime";
import { sportsSeasonScenario } from "./artifacts";
import type { SportsDemoAction } from "./contracts";

const now = () => "2026-09-30T12:00:00Z";
const eventRef = "event:running-01";
const make = () => {
  const data = new FixtureAdapter().load();
  return new SportsSeasonProvider(sportsSeasonScenario, now, userConfigurationFor(data), data);
};
async function start(p: SportsSeasonProvider, personRef: string) {
  await p.executeAction({ type: "sports-select-person", personRef });
  await p.executeAction({ type: "sports-registration-qr", eventRef });
  await p.executeAction({ type: "sports-intention", personRef, intention: "participate" });
  if (personRef === "P03") await p.executeAction({ type: "sports-identify-visitor", personRef, name: "Alex Demo" });
  return p.executeAction({ type: "sports-register", personRef, eventRef, selectedModality: "social" });
}
async function finish(p: SportsSeasonProvider, personRef: string, provided = false) {
  const registered = await start(p, personRef);
  await p.executeAction({ type: "sports-voluntary", personRef, decision: provided ? "provided" : "skipped", frequency: provided ? "weekly" : undefined });
  const subject = { personRef, eventRef, registrationRef: registered.registration!.registrationId };
  await p.executeAction({ type: "sports-check-in", ...subject });
  return p.executeAction({ type: "sports-effort", ...subject, level: "medio" });
}

describe("BUILD 02 normalized fixture integrity", () => {
  it("loads CSV BOM/CRLF, amounts in cents, products, channels and categories", () => {
    const tx = parseTransactionCSV(csv);
    expect(tx).toHaveLength(16);
    expect(tx[1]).toMatchObject({ personRef: "P01", channel: "web", category: "running_apparel", grossCents: 5480, unitCents: 2740, quantity: 2 });
    const quoted = csv.replace("Zapatillas running AeroRun 5", '"Zapatillas, ""AeroRun"" 5"');
    expect(parseTransactionCSV(quoted)[0].product).toBe('Zapatillas, "AeroRun" 5');
  });
  it.each([["P01", 51175], ["P02", 73120]])("verifies %s commercial totals against JSON", (id, total) => {
    const data = new FixtureAdapter().load();
    const tx = data.transactions.filter(t => t.personRef === id);
    expect(tx).toHaveLength(8);
    expect(tx.reduce((sum,t) => sum + t.grossCents,0)).toBe(total);
  });
  it("loads actual loyalty, distinct counterfactual, all Self Service content and P03", () => {
    const d = new FixtureAdapter().load();
    expect(d.loyaltyStates.find(l => l.personRef === "P01")).toMatchObject({ membershipStatus: "non_member", pointsBalance: null, actualLevel: null });
    expect(d.counterfactuals[0]).toMatchObject({ personRef: "P01", hypotheticalPoints: 511, hypotheticalLevel: { name: "Active" }, credited: false });
    expect(d.loyaltyStates.find(l => l.personRef === "P02")).toMatchObject({ membershipStatus: "active", pointsBalance: 731, actualLevel: { name: "Pro" } });
    expect(d.transactions.filter(t => t.personRef === "P03")).toEqual([]);
    expect(d.badges).toHaveLength(2); expect(d.coupons).toHaveLength(2); expect(d.news).toHaveLength(3); expect(d.experiences).toHaveLength(4);
  });
  it.each(["summary", "counterfactual", "foreign-person", "foreign-badge", "foreign-experience", "duplicate", "nonmember-balance", "missing-state", "tier", "basis-refs"])("stops contradictory fixtures: %s", problem => {
    const d = JSON.parse(json);
    if (problem === "summary") d.commercial_summaries[0].gross_spend += 1;
    if (problem === "counterfactual") d.loyalty_counterfactuals[0].hypothetical_points += 1;
    if (problem === "foreign-person") d.loyalty_states[0].person_id = "UNKNOWN";
    if (problem === "foreign-badge") d.badges[0].person_id = "UNKNOWN";
    if (problem === "foreign-experience") d.experiences[0].person_id = "UNKNOWN";
    if (problem === "duplicate") d.coupons.push(d.coupons[0]);
    if (problem === "nonmember-balance") d.loyalty_states[0].points_balance = 511;
    if (problem === "missing-state") d.loyalty_states.pop();
    if (problem === "tier") d.loyalty_states[1].level.name = "Active";
    if (problem === "basis-refs") d.loyalty_counterfactuals[0].basis_transaction_ids[0] = "TX-P02-001";
    expect(() => new FixtureAdapter(csv, JSON.stringify(d)).load()).toThrow(/Carga detenida/);
  });
  it("rejects unknown transaction person, malformed JSON and malformed CSV without fallback", () => {
    expect(() => new FixtureAdapter(csv.replace("TX-P01-001,P01", "TX-P01-001,UNKNOWN"), json).load()).toThrow();
    expect(() => new FixtureAdapter(csv, "{").load()).toThrow();
    expect(() => parseTransactionCSV(csv.replace("89.90", "bad"))).toThrow();
    expect(() => parseTransactionCSV(csv + '"unfinished')).toThrow();
  });
});

describe("BUILD 02 shared user and Self Service state", () => {
  it.each(["P01", "P02", "P03"])("%s completes Carrera and projects exactly one new Sports Season badge", async personRef => {
    const p = make();
    const initial = await p.executeAction({ type: "sports-select-person", personRef });
    const final = await finish(p, personRef, true);
    const relation = final.userPlane!.relationship!;
    expect(final.evidence.map(e => e.kind)).toEqual(["presence", "effort"]);
    expect(final.userPlane?.voluntary?.source).toBe("user_declared");
    expect(final.userPlane?.incentive?.source).toBe("voluntary-information");
    expect(relation.badges).toHaveLength(initial.userPlane!.relationship!.badges.length + 1);
    expect(relation.badges.at(-1)).toMatchObject({ personRef, origin: "sports_season", registrationRef: final.registration!.registrationId, supportingEvidenceRefs: final.evidence.map(e => e.evidenceId) });
    expect(relation.loyalty).toEqual(initial.userPlane!.relationship!.loyalty);
    expect(relation.coupons).toEqual(initial.userPlane!.relationship!.coupons);
    expect(relation.experiences.at(-1)?.state).toBe("completed");
    expect(final.scenario.person.customerRelationship).toBe(personRef === "P03" ? "not-established" : "established");
  });
  it.each(["P01", "P02", "P03"])("%s information branch records user_declared without sporting facts", async personRef => {
    const p = make();
    await p.executeAction({ type: "sports-select-person", personRef });
    await p.executeAction({ type: "sports-intention", personRef, intention: "information" });
    const s = await p.executeAction({ type: "sports-interests", personRef, values: ["running", "improvement", "sports-news"] });
    expect(s.userPlane?.declaredInterests?.source).toBe("user_declared");
    expect(s.registration).toBeUndefined(); expect(s.evidence).toEqual([]); expect(s.badge).toBeUndefined();
    expect(s.userPlane?.relationship?.badges.some(b => b.origin === "sports_season")).toBe(false);
  });
  it("registration QR recognizes customers without presence or redundant identification", async () => {
    const p = make();
    await p.executeAction({ type: "sports-registration-qr", eventRef });
    const s = await p.executeAction({ type: "sports-select-person", personRef: "P01" });
    expect(s.userPlane?.registrationEntry?.recognized).toBe(true);
    expect(s.registration).toBeUndefined(); expect(s.evidence).toEqual([]);
    await expect(p.executeAction({ type: "sports-identify-visitor", personRef: "P01", name: "Other" })).rejects.toThrow();
    await p.executeAction({ type: "sports-intention", personRef: "P01", intention: "participate" });
    expect((await p.getSnapshot()).userPlane?.recommendations).toHaveLength(4);
  });
  it("optional omission grants the same badge without an incentive; Experiences track participation", async () => {
    const p = make();
    const registered = await start(p, "P01");
    expect(registered.userPlane?.relationship?.experiences.at(-1)?.state).toBe("enrolled");
    await p.executeAction({ type: "sports-voluntary", personRef: "P01", decision: "skipped" });
    const subject = { personRef: "P01", eventRef, registrationRef: registered.registration!.registrationId };
    const present = await p.executeAction({ type: "sports-check-in", ...subject });
    expect(present.userPlane?.relationship?.experiences.at(-1)?.state).toBe("active");
    expect(present.userPlane?.relationship?.badges).toEqual([]);
    const final = await p.executeAction({ type: "sports-effort", ...subject, level: "suave" });
    expect(final.userPlane?.incentive).toBeUndefined(); expect(final.badge).toBeDefined();
  });
  it("switching people retains isolated journeys, declarations, name and badges; explicit reset clears them", async () => {
    const p = make();
    const first = await finish(p, "P01", true);
    await finish(p, "P03");
    expect((await p.executeAction({ type: "sports-select-person", personRef: "P02" })).badge).toBeUndefined();
    const restored = await p.executeAction({ type: "sports-select-person", personRef: "P01" });
    expect(restored).toEqual(first);
    const visitor = await p.executeAction({ type: "sports-select-person", personRef: "P03" });
    expect(visitor.userPlane?.person?.name).toBe("Alex Demo");
    expect(visitor.userPlane?.relationship?.badges).toHaveLength(1);
    await p.reset();
    const reset = await p.executeAction({ type: "sports-select-person", personRef: "P01" });
    expect(reset.badge).toBeUndefined(); expect(reset.userPlane?.relationship?.badges).toEqual([]);
    expect(reset.userPlane?.relationship?.loyalty.pointsBalance).toBeNull();
  });
  it("wrong-person, wrong-event, stale and duplicate evidence cannot grant another badge", async () => {
    const p = make();
    const final = await finish(p, "P02");
    const action = { type: "sports-effort", personRef: "P02", eventRef, registrationRef: final.registration!.registrationId, level: "medio" } as SportsDemoAction;
    for (const a of [action, { ...action, personRef: "P01" }, { ...action, eventRef: "event:sailing-01" }, { ...action, registrationRef: "old" }]) {
      await expect(p.executeAction(a)).rejects.toThrow();
      expect(await p.getSnapshot()).toEqual(final);
    }
  });
  it("adapter and runtime snapshots are isolated and never credit a counterfactual on reads", async () => {
    const p = make();
    const s = await p.executeAction({ type: "sports-select-person", personRef: "P01" });
    s.userPlane!.relationship!.loyalty.pointsBalance = 999;
    s.userPlane!.relationship!.transactions.length = 0;
    const intact = await p.getSnapshot();
    expect(intact.userPlane?.relationship?.loyalty.pointsBalance).toBeNull();
    expect(intact.userPlane?.relationship?.transactions).toHaveLength(8);
    expect(intact.userPlane?.relationship?.counterfactual?.hypotheticalPoints).toBe(511);
    expect((await make().getSnapshot()).userPlane?.person).toBeUndefined();
  });
});
