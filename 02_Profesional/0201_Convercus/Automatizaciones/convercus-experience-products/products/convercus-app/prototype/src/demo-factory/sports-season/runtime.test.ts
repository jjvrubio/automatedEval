import { afterAll, describe, expect, it } from "vitest";
import { writeFileSync } from "node:fs";
import { defaultDemoCatalogs, resolveAppDemo, resolveDemo } from "../bootstrap";
import { sportsSeasonManifest, sportsSeasonScenario } from "./artifacts";
import type { SportsAction, SportsSnapshot } from "./contracts";
import { SportsSeasonProvider, sportsBadgeRuleRef } from "./runtime";

const now = () => "2026-09-27T09:30:00.000Z";
const personRef = sportsSeasonScenario.person.id;
const eventRef = sportsSeasonScenario.events[0].id;
const trace: unknown[] = [];
const make = (scenario = sportsSeasonScenario) => new SportsSeasonProvider(scenario, now);
const register = (selectedModality = "social"): SportsAction => ({ type: "sports-register", personRef, eventRef, selectedModality });
function checkIn(s: SportsSnapshot): SportsAction {
  return { type: "sports-check-in", personRef, eventRef, registrationRef: s.registration!.registrationId };
}
function effort(s: SportsSnapshot, level = "medio"): SportsAction {
  return { type: "sports-effort", personRef, eventRef, registrationRef: s.registration!.registrationId, level };
}
async function complete(p: SportsSeasonProvider, modality = "social", level = "medio") {
  const registered = await p.executeAction(register(modality));
  const present = await p.executeAction(checkIn(registered));
  return p.executeAction(effort(present, level));
}
async function rejectUnchanged(p: SportsSeasonProvider, action: SportsAction) {
  const before = await p.getSnapshot();
  await expect(p.executeAction(action)).rejects.toThrow();
  expect(await p.getSnapshot()).toEqual(before);
}

describe("BUILD 01 situated sports runtime", () => {
  it("starts with an external person, no member record, no registration or Evidence", async () => {
    const s = await make().getSnapshot();
    expect(s.scenario.person).toMatchObject({ membershipStatus: "external", customerRelationship: "not-established" });
    expect(s).not.toHaveProperty("member");
    expect(s.registration).toBeUndefined();
    expect(s.evidence).toEqual([]);
    expect(s.badge).toBeUndefined();
    expect(s.opportunity).toBeUndefined();
    expect(s.scenario.events.map((e) => e.discipline)).toEqual(["running", "sailing", "beach-volleyball"]);
  });

  for (const modality of ["social", "wellness"]) for (const level of ["suave", "medio", "intenso"]) {
    it(`preserves ${modality}/${level}, separate sources and correct individual recognition`, async () => {
      const p = make();
      const initial = await p.getSnapshot();
      const registered = await p.executeAction(register(modality));
      expect(registered.registration).toMatchObject({ personRef, eventRef, selectedModality: modality, status: "accepted" });
      expect(registered.scenario.person).not.toHaveProperty("selectedModality");
      expect(registered.evidence).toEqual([]);
      expect(registered.badge).toBeUndefined();
      const present = await p.executeAction(checkIn(registered));
      expect(present.evidence).toHaveLength(1);
      expect(present.evidence[0]).toMatchObject({ kind: "presence", source: "simulated-check-in", simulation: true, personRef, eventRef });
      expect(present.evidence[0]).not.toHaveProperty("level");
      expect(present.badge).toBeUndefined();
      expect(present.opportunity).toBeUndefined();
      const final = await p.executeAction(effort(present, level));
      expect(final.evidence).toHaveLength(2);
      expect(final.evidence[1]).toMatchObject({ kind: "effort", source: "participant-self-report", level, simulation: true, personRef, eventRef });
      expect(final.badge).toMatchObject({
        personRef, eventRef, registrationRef: registered.registration!.registrationId,
        ruleRef: sportsBadgeRuleRef, supportingEvidenceRefs: final.evidence.map((e) => e.evidenceId),
      });
      expect(final.badge?.reason).toBeTruthy();
      expect(final.opportunity).toMatchObject({ kind: "club-invitation", status: "available", personRef, badgeRef: final.badge!.badgeId });
      for (const s of [registered, present, final]) expect(s.scenario.person).toEqual(initial.scenario.person);
      trace.push({ modality, level, initial, registered, present, final });
    });
  }

  it("rejects invalid order, repetition and unknown actions without changing any facts", async () => {
    const p = make();
    await rejectUnchanged(p, { type: "sports-check-in", personRef, eventRef, registrationRef: "absent" });
    await rejectUnchanged(p, { type: "sports-effort", personRef, eventRef, registrationRef: "absent", level: "medio" });
    await rejectUnchanged(p, { ...register(), type: "unknown" } as unknown as SportsAction);
    const registered = await p.executeAction(register());
    await rejectUnchanged(p, register());
    await rejectUnchanged(p, effort(registered));
    const present = await p.executeAction(checkIn(registered));
    await rejectUnchanged(p, checkIn(registered));
    await p.executeAction(effort(present));
    await rejectUnchanged(p, effort(present));
    await rejectUnchanged(p, checkIn(present));
    expect((await p.getSnapshot()).evidence).toHaveLength(2);
  });

  it("rejects invalid modality and effort atomically, then accepts a correction", async () => {
    const p = make();
    for (const value of ["", "competition", "Social"]) await rejectUnchanged(p, register(value));
    const registered = await p.executeAction(register("wellness"));
    const present = await p.executeAction(checkIn(registered));
    for (const value of ["", "extreme", "Intenso"]) await rejectUnchanged(p, effort(present, value));
    expect((await p.executeAction(effort(present, "intenso"))).badge).toBeDefined();
  });

  it("rejects wrong person, event and registration at every public boundary", async () => {
    const p = make();
    await rejectUnchanged(p, { ...register(), personRef: sportsSeasonScenario.contrastPerson.id });
    await rejectUnchanged(p, { ...register(), eventRef: sportsSeasonScenario.events[1].id });
    await rejectUnchanged(p, { ...register(), eventRef: "missing-event" });
    const registered = await p.executeAction(register());
    for (const replacement of [{ personRef: "wrong" }, { eventRef: sportsSeasonScenario.events[2].id }, { registrationRef: "wrong" }]) {
      await rejectUnchanged(p, { ...checkIn(registered), ...replacement });
    }
    const present = await p.executeAction(checkIn(registered));
    for (const replacement of [{ personRef: "wrong" }, { eventRef: "wrong" }, { registrationRef: "wrong" }]) {
      await rejectUnchanged(p, { ...effort(present), ...replacement });
    }
  });

  it("isolates snapshots and incoming configuration, and resets all mutable state", async () => {
    const config = structuredClone(sportsSeasonScenario);
    const p = make(config);
    const initial = await p.getSnapshot();
    config.person.membershipStatus = "member";
    const final = await complete(p);
    final.scenario.person.membershipStatus = "member";
    final.evidence.length = 0;
    final.badge!.supportingEvidenceRefs.length = 0;
    expect((await p.getSnapshot()).evidence).toHaveLength(2);
    expect((await p.getSnapshot()).badge?.supportingEvidenceRefs).toHaveLength(2);
    expect(await p.reset()).toEqual(initial);
    expect((await complete(p, "wellness", "suave")).registration?.selectedModality).toBe("wellness");
  });

  it("copy, labels and display names cannot change facts, attribution or eligibility", async () => {
    const changed = structuredClone(sportsSeasonScenario);
    changed.person.name = "Nombre cambiado";
    changed.season.title = "Otro título";
    changed.modalities[0].label = "Otra etiqueta";
    changed.efforts[1].label = "Texto nuevo";
    changed.events[0].title = "Evento renombrado";
    changed.badge.title = "Insignia renombrada";
    changed.badge.reason = "Otro texto editorial";
    changed.club.invitation = "Otra invitación";
    const a = await complete(make());
    const b = await complete(make(changed));
    expect(b.registration).toEqual(a.registration);
    expect(b.evidence).toEqual(a.evidence);
    expect(b.opportunity).toEqual(a.opportunity);
    const facts = (s: SportsSnapshot) => ({
      badgeId: s.badge!.badgeId, personRef: s.badge!.personRef, eventRef: s.badge!.eventRef,
      registrationRef: s.badge!.registrationRef, ruleRef: s.badge!.ruleRef, supportingEvidenceRefs: s.badge!.supportingEvidenceRefs,
    });
    expect(facts(b)).toEqual(facts(a));
  });

  it("rejects a configuration that fabricates membership or other executable disciplines", () => {
    const member = structuredClone(sportsSeasonScenario);
    member.person.membershipStatus = "member";
    expect(() => make(member)).toThrow();
    const sailing = structuredClone(sportsSeasonScenario);
    sailing.events[1].executable = true;
    expect(() => make(sailing)).toThrow();
  });
});

describe("BUILD 01 composition boundary and legacy isolation", () => {
  it("resolves sports without any member fixture, TES Experience or hotel context", () => {
    const runtime = resolveAppDemo(sportsSeasonManifest.demoId);
    expect(runtime).toMatchObject({ kind: "sports-season", manifest: { demoId: sportsSeasonManifest.demoId } });
    expect(runtime).not.toHaveProperty("experience");
    expect(runtime.scenario).not.toHaveProperty("experienceRef");
    expect(runtime.scenario).not.toHaveProperty("contexts");
    expect(runtime.capabilities.every((c) => c.status === "simulated")).toBe(true);
    const renamed = { ...sportsSeasonManifest, demoId: "opaque-composition" };
    const catalogs = { ...defaultDemoCatalogs, manifests: { "opaque-composition": renamed } };
    expect(resolveAppDemo("opaque-composition", catalogs)).toMatchObject({ kind: "sports-season", manifest: { demoId: "opaque-composition" } });
  });

  it("fails explicitly for incompatible sports references and capability claims", () => {
    for (const replacement of [{ fixtureRef: "wrong" }, { scenarioRef: "wrong" }, { sportsSeasonRef: "wrong" },
      { requestedCapabilities: [{ id: "sports-participation", label: "Real", expectedStatus: "real" as const }] }]) {
      const manifest = { ...sportsSeasonManifest, ...replacement };
      expect(() => resolveAppDemo(manifest.demoId, { ...defaultDemoCatalogs, manifests: { [manifest.demoId]: manifest } })).toThrow();
    }
  });

  it("sports actions/reset leave R/H/A/B untouched, and their actions leave sports untouched", async () => {
    const legacy = ["retail-baseline", "hospitality-stay", "hospitality-family-adventure", "hospitality-family-adventure-costa"].map((id) => resolveDemo(id));
    const initial = await Promise.all(legacy.map((r) => r.provider.getSnapshot()));
    const sports = make();
    const sportsFinal = await complete(sports);
    expect(await Promise.all(legacy.map((r) => r.provider.getSnapshot()))).toEqual(initial);
    for (const runtime of legacy) for (const step of runtime.script?.steps ?? []) await runtime.provider.executeAction(step.action);
    expect(await sports.getSnapshot()).toEqual(sportsFinal);
    const legacyFinal = await Promise.all(legacy.map((r) => r.provider.getSnapshot()));
    await sports.reset();
    expect(await Promise.all(legacy.map((r) => r.provider.getSnapshot()))).toEqual(legacyFinal);
    for (const r of legacy) await r.provider.reset();
    expect(await Promise.all(legacy.map((r) => r.provider.getSnapshot()))).toEqual(initial);
    trace.push({ legacyIds: legacy.map((r) => r.manifest.demoId), initial, legacyFinal, sportsFinal, isolated: true });
  });
});

afterAll(() => {
  if (process.env.BUILD01_TRACE_PATH) writeFileSync(process.env.BUILD01_TRACE_PATH, JSON.stringify(trace, null, 2) + "\n", { flag: "wx" });
});
