import { afterAll, describe, expect, it } from "vitest";
import { writeFileSync } from "node:fs";
import { resolveAppDemo } from "../bootstrap";
import { sportsSeasonScenario } from "./artifacts";
import { SportsSeasonProvider, sportsBadgeRuleRef } from "./runtime";
import { sportsUserConfiguration } from "./user-plane-artifacts";
import type { SportsDemoAction, SportsSnapshot } from "./contracts";

const now = () => "2026-09-27T09:30:00.000Z";
const eventRef = sportsSeasonScenario.events[0].id;
const make = () => new SportsSeasonProvider(sportsSeasonScenario, now, sportsUserConfiguration);
const trace: unknown[] = [];
async function choose(p: SportsSeasonProvider, personRef = "person:lea", intention = "participate") {
  await p.executeAction({ type: "sports-select-person", personRef });
  await p.executeAction({ type: "sports-intention", personRef, intention });
  if (intention === "participate") await p.executeAction({ type: "sports-select-event", personRef, eventRef });
}
async function register(p: SportsSeasonProvider, personRef = "person:lea", selectedModality = "social") {
  return p.executeAction({ type: "sports-register", personRef, eventRef, selectedModality });
}
async function checkIn(p: SportsSeasonProvider, s: SportsSnapshot) {
  return p.executeAction({ type: "sports-check-in", personRef: s.registration!.personRef, eventRef, registrationRef: s.registration!.registrationId });
}
async function finish(p: SportsSeasonProvider, s: SportsSnapshot, level = "medio") {
  return p.executeAction({ type: "sports-effort", personRef: s.registration!.personRef, eventRef, registrationRef: s.registration!.registrationId, level });
}
async function unchanged(p: SportsSeasonProvider, action: SportsDemoAction) {
  const before = await p.getSnapshot();
  await expect(p.executeAction(action)).rejects.toThrow();
  expect(await p.getSnapshot()).toEqual(before);
}
const sportsFacts = (s: SportsSnapshot) => ({ registration: s.registration, evidence: s.evidence, badge: s.badge, opportunity: s.opportunity });

describe("BUILD 02 user plane — one situated sports provider", () => {
  it("starts with selectable people, no assumed participant, intention, registration or credited value", async () => {
    const runtime = resolveAppDemo("sports-season-running");
    const s = await runtime.provider.getSnapshot() as SportsSnapshot;
    expect(s.userPlane?.person).toBeUndefined();
    expect(s.userPlane?.configuration.people).toHaveLength(3);
    expect(s.userPlane?.intention).toBeUndefined();
    expect(s.registration).toBeUndefined();
    expect(s.evidence).toEqual([]);
    expect(s.userPlane?.counterfactual).toBeUndefined();
  });

  it("keeps the nonmember's 194 potential points separate from programme balance and declared information", async () => {
    const p = make();
    const selected = await p.executeAction({ type: "sports-select-person", personRef: "person:lea" });
    expect(selected.userPlane?.person).toMatchObject({ customerRelationship: "established", membershipStatus: "external" });
    expect(selected.userPlane?.counterfactual).toEqual({ totalCents: 19480, potentialPoints: 194, credited: false });
    expect(selected.userPlane?.person?.program).toBeUndefined();
    expect(selected.userPlane?.person?.purchases).toHaveLength(3);
    expect(selected.scenario.person.id).toBe("person:lea");
    trace.push({ case: "known nonmember", selected });
  });

  it("registration QR recognizes the selected customer, selects only the event context and creates no presence", async () => {
    const p = make();
    const entry = await p.executeAction({ type: "sports-registration-qr", eventRef });
    expect(entry.userPlane?.registrationEntry?.recognized).toBe(false);
    expect(entry.userPlane?.person).toBeUndefined();
    expect(entry.evidence).toEqual([]);
    const selected = await p.executeAction({ type: "sports-select-person", personRef: "person:lea" });
    expect(selected.userPlane?.registrationEntry).toEqual({ eventRef, source: "simulated-registration-qr", recognized: true });
    expect(selected.userPlane?.selectedEventRef).toBeUndefined();
    const intended = await p.executeAction({ type: "sports-intention", personRef: "person:lea", intention: "participate" });
    expect(intended.userPlane?.selectedEventRef).toBe(eventRef);
    expect(intended.userPlane?.recommendations).toHaveLength(4);
    expect(intended.registration).toBeUndefined();
    expect(intended.evidence).toEqual([]);
    await unchanged(p, { type: "sports-identify-visitor", personRef: "person:lea", name: "Overwrite known name" });
    const registered = await register(p);
    expect(registered.evidence).toEqual([]);
    await unchanged(p, { type: "sports-registration-qr", eventRef });
    trace.push({ case: "registration QR", entry, selected, intended, registered });
  });

  it("unknown visitor can identify a fictitious name and participate without becoming a customer or member", async () => {
    const p = make();
    await p.executeAction({ type: "sports-registration-qr", eventRef });
    await p.executeAction({ type: "sports-select-person", personRef: "person:visitor" });
    await p.executeAction({ type: "sports-intention", personRef: "person:visitor", intention: "participate" });
    await unchanged(p, { type: "sports-register", personRef: "person:visitor", eventRef, selectedModality: "social" });
    await unchanged(p, { type: "sports-identify-visitor", personRef: "person:visitor", name: " " });
    const identified = await p.executeAction({ type: "sports-identify-visitor", personRef: "person:visitor", name: "  Alex Prueba  " });
    expect(identified.userPlane?.person?.name).toBe("Alex Prueba");
    expect(identified.userPlane?.registrationEntry?.recognized).toBe(false);
    const s = await register(p, "person:visitor");
    await p.executeAction({ type: "sports-voluntary", personRef: "person:visitor", decision: "skipped" });
    const final = await finish(p, await checkIn(p, s));
    expect(final.scenario.person).toMatchObject({ id: "person:visitor", name: "Alex Prueba", customerRelationship: "not-established", membershipStatus: "external" });
    expect(final.userPlane?.person?.purchases).toEqual([]);
    expect(final.userPlane?.counterfactual).toBeUndefined();
    expect(final.badge?.personRef).toBe("person:visitor");
    expect(final.opportunity?.personRef).toBe("person:visitor");
    trace.push({ case: "unknown visitor", identified, final });
  });

  for (const personRef of ["person:lea", "person:diego", "person:visitor"]) {
    it(`records interests for ${personRef} without creating sports facts or inferring purchase intent`, async () => {
      const p = make();
      await choose(p, personRef, "information");
      await unchanged(p, { type: "sports-interests", personRef, values: [] });
      await unchanged(p, { type: "sports-interests", personRef, values: ["running", "running"] });
      await unchanged(p, { type: "sports-interests", personRef, values: ["unsupported"] });
      const s = await p.executeAction({ type: "sports-interests", personRef, values: ["sailing", "next-events"] });
      expect(s.userPlane?.declaredInterests).toEqual({ personRef, values: ["sailing", "next-events"], source: "person-declared", occurredAt: now() });
      expect(sportsFacts(s)).toEqual({ registration: undefined, evidence: [], badge: undefined, opportunity: undefined });
      expect(s.userPlane?.recommendations).toEqual([]);
      expect(s.userPlane?.incentive).toBeUndefined();
      await unchanged(p, { type: "sports-register", personRef, eventRef, selectedModality: "social" });
      await unchanged(p, { type: "sports-select-event", personRef, eventRef });
      await unchanged(p, { type: "sports-intention", personRef, intention: "participate" });
      await unchanged(p, { type: "sports-voluntary", personRef, decision: "provided", frequency: "weekly" });
      trace.push({ case: "information only", personRef, final: s });
    });
  }

  for (const modality of ["social", "wellness"]) for (const level of ["suave", "medio", "intenso"]) {
    it(`preserves the badge rule for ${modality}/${level} whether voluntary information is given or skipped`, async () => {
      const finals: SportsSnapshot[] = [];
      for (const decision of ["provided", "skipped"] as const) {
        const p = make();
        await choose(p);
        const s = await register(p, "person:lea", modality);
        await unchanged(p, { type: "sports-check-in", personRef: "person:lea", eventRef, registrationRef: s.registration!.registrationId });
        const voluntary = await p.executeAction({ type: "sports-voluntary", personRef: "person:lea", decision, ...(decision === "provided" ? { frequency: "weekly", goal: "habit" } : {}) });
        expect(voluntary.evidence).toEqual([]);
        expect(voluntary.badge).toBeUndefined();
        expect(Boolean(voluntary.userPlane?.incentive)).toBe(decision === "provided");
        const present = await checkIn(p, s);
        expect(present.evidence).toHaveLength(1);
        expect(present.badge).toBeUndefined();
        const final = await finish(p, present, level);
        expect(final.badge?.ruleRef).toBe(sportsBadgeRuleRef);
        expect(final.badge?.supportingEvidenceRefs).toEqual(final.evidence.map(item => item.evidenceId));
        expect(final.evidence.map(item => item.source)).toEqual(["simulated-check-in", "participant-self-report"]);
        expect(final.userPlane?.counterfactual?.credited).toBe(false);
        expect(final.userPlane?.person?.program).toBeUndefined();
        finals.push(final);
        trace.push({ case: "participation", modality, level, decision, final });
      }
      expect(sportsFacts(finals[0])).toEqual(sportsFacts(finals[1]));
    });
  }

  it("member participates with an independent modality, unchanged points and no invitation to join again", async () => {
    const p = make();
    await choose(p, "person:diego");
    const selected = await p.getSnapshot();
    expect(selected.userPlane?.counterfactual).toBeUndefined();
    expect(selected.userPlane?.person?.program?.points).toBe(860);
    const s = await register(p, "person:diego", "wellness");
    await p.executeAction({ type: "sports-voluntary", personRef: "person:diego", decision: "skipped" });
    const final = await finish(p, await checkIn(p, s), "suave");
    expect(final.registration?.selectedModality).toBe("wellness");
    expect(final.badge?.personRef).toBe("person:diego");
    expect(final.userPlane?.person?.program).toEqual(selected.userPlane?.person?.program);
    expect(final.opportunity).toBeUndefined();
    trace.push({ case: "member", final });
  });

  it("rejects invalid values, wrong attribution and out-of-order declarations atomically", async () => {
    const p = make();
    await unchanged(p, { type: "sports-select-person", personRef: "absent" });
    await unchanged(p, { type: "sports-registration-qr", eventRef: "event:sailing-01" });
    await unchanged(p, { type: "sports-intention", personRef: "person:lea", intention: "participate" });
    await choose(p);
    await unchanged(p, { type: "sports-intention", personRef: "person:lea", intention: "purchase" });
    await unchanged(p, { type: "sports-interests", personRef: "person:lea", values: ["running"] });
    await unchanged(p, { type: "sports-voluntary", personRef: "person:lea", decision: "provided", frequency: "weekly" });
    const s = await register(p);
    for (const payload of [{ decision: "provided" as const }, { decision: "provided" as const, goal: "invalid" }, { decision: "skipped" as const, frequency: "weekly" }]) {
      await unchanged(p, { type: "sports-voluntary", personRef: "person:lea", ...payload });
    }
    await unchanged(p, { type: "sports-voluntary", personRef: "person:diego", decision: "skipped" });
    await p.executeAction({ type: "sports-voluntary", personRef: "person:lea", decision: "provided", goal: "company" });
    await unchanged(p, { type: "sports-voluntary", personRef: "person:lea", decision: "skipped" });
    await unchanged(p, { type: "sports-effort", personRef: "person:lea", eventRef, registrationRef: s.registration!.registrationId, level: "medio" });
    await checkIn(p, s);
    await unchanged(p, { type: "sports-check-in", personRef: "person:lea", eventRef, registrationRef: s.registration!.registrationId });
    await unchanged(p, { type: "sports-effort", personRef: "person:diego", eventRef, registrationRef: s.registration!.registrationId, level: "medio" });
  });

  it("changing person and reset clear the journey; stale registrations cannot contaminate later runs", async () => {
    const p = make();
    const initial = await p.getSnapshot();
    await choose(p);
    const old = await register(p);
    await p.executeAction({ type: "sports-voluntary", personRef: "person:lea", decision: "provided", frequency: "weekly" });
    await finish(p, await checkIn(p, old));
    const selected = await p.executeAction({ type: "sports-select-person", personRef: "person:diego" });
    expect(sportsFacts(selected)).toEqual({ registration: undefined, evidence: [], badge: undefined, opportunity: undefined });
    expect(selected.userPlane?.incentive).toBeUndefined();
    expect(selected.userPlane?.voluntary).toBeUndefined();
    expect(selected.userPlane?.intention).toBeUndefined();
    expect(await p.executeAction({ type: "sports-select-person", personRef: "person:diego" })).toEqual(selected);
    expect(await p.reset()).toEqual(initial);
    await choose(p);
    const next = await register(p);
    expect(next.registration!.registrationId).not.toBe(old.registration!.registrationId);
    await p.executeAction({ type: "sports-voluntary", personRef: "person:lea", decision: "skipped" });
    await unchanged(p, { type: "sports-check-in", personRef: "person:lea", eventRef, registrationRef: old.registration!.registrationId });
    expect((await checkIn(p, next)).evidence).toHaveLength(1);
  });

  it("clones configuration and snapshots and isolates separate demo instances", async () => {
    const configuration = structuredClone(sportsUserConfiguration);
    const p = new SportsSeasonProvider(sportsSeasonScenario, now, configuration);
    const other = make();
    const untouched = await other.getSnapshot();
    configuration.people[0].purchases[0].amountCents = 1;
    await choose(p);
    const view = await p.getSnapshot();
    view.userPlane!.person!.purchases[0].amountCents = 1;
    view.userPlane!.configuration.people.length = 0;
    expect((await p.getSnapshot()).userPlane?.counterfactual?.potentialPoints).toBe(194);
    expect((await p.getSnapshot()).userPlane?.configuration.people).toHaveLength(3);
    expect(await other.getSnapshot()).toEqual(untouched);
  });

  it("rejects contradictory commercial fixture data before creating a journey", () => {
    const badMember = structuredClone(sportsUserConfiguration);
    badMember.people[0].program = { points: 1, level: "Invalid", benefits: [] };
    expect(() => new SportsSeasonProvider(sportsSeasonScenario, now, badMember)).toThrow();
    const badVisitor = structuredClone(sportsUserConfiguration);
    badVisitor.people[2].purchases.push({ id: "fake", date: "2026-01-01", description: "not known", amountCents: 1 });
    expect(() => new SportsSeasonProvider(sportsSeasonScenario, now, badVisitor)).toThrow();
  });
});

afterAll(() => {
  if (process.env.BUILD02_TRACE_PATH) writeFileSync(process.env.BUILD02_TRACE_PATH, JSON.stringify(trace, null, 2) + "\n", { flag: "wx" });
});
