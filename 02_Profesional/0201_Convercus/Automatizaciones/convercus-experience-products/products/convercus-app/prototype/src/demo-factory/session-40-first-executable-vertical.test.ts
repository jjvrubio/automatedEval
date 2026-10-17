import { describe, expect, it } from "vitest";
import { resolveAppDemo } from "./bootstrap";

describe("Session 40 — first executable Sports Season vertical", () => {
  it("resolves the situated composition with a future Carrera event and honest simulated capabilities", () => {
    const runtime = resolveAppDemo("sports-season-running");

    expect("kind" in runtime && runtime.kind).toBe("sports-season");
    if (!("kind" in runtime)) throw new Error("Sports Season composition was not resolved");
    expect(runtime.manifest.demoId).toBe("sports-season-running");
    expect(runtime.capabilities.every((item) => item.status === "simulated")).toBe(true);
    expect(runtime.scenario.person).toMatchObject({
      membershipStatus: "external",
      customerRelationship: "not-established",
    });
    const running = runtime.scenario.events.find((event) => event.discipline === "running");
    expect(running).toMatchObject({ id: "event:running-01", date: "2026-10-24", executable: true });
    expect(runtime.scenario.events.filter((event) => event.executable)).toHaveLength(1);
  });

  it("runs enrollment, simulated presence and self-reported effort as distinct records", async () => {
    const runtime = resolveAppDemo("sports-season-running");
    if (!("kind" in runtime)) throw new Error("Sports Season composition was not resolved");
    const initial = await runtime.provider.getSnapshot();
    const personRef = initial.scenario.person.id;
    const eventRef = initial.scenario.events.find((event) => event.discipline === "running")!.id;

    expect(initial.registration).toBeUndefined();
    expect(initial.evidence).toEqual([]);
    expect(initial.scenario.person.membershipStatus).toBe("external");

    const enrolled = await runtime.provider.executeAction({
      type: "sports-register", personRef, eventRef, selectedModality: "social",
    });
    expect(enrolled.registration).toMatchObject({ personRef, eventRef, selectedModality: "social", status: "accepted" });
    expect(enrolled.evidence).toEqual([]);
    expect(enrolled.badge).toBeUndefined();

    const present = await runtime.provider.executeAction({
      type: "sports-check-in", personRef, eventRef, registrationRef: enrolled.registration!.registrationId,
    });
    expect(present.evidence).toHaveLength(1);
    expect(present.evidence[0]).toMatchObject({ kind: "presence", source: "simulated-check-in", simulation: true, personRef, eventRef });
    expect(present.evidence[0]).not.toHaveProperty("level");
    expect(present.badge).toBeUndefined();

    const recognized = await runtime.provider.executeAction({
      type: "sports-effort", personRef, eventRef,
      registrationRef: enrolled.registration!.registrationId, level: "medio",
    });
    expect(recognized.evidence).toHaveLength(2);
    expect(recognized.evidence[1]).toMatchObject({ kind: "effort", source: "participant-self-report", level: "medio", simulation: true, personRef, eventRef });
    expect(recognized.evidence[1].evidenceId).not.toBe(recognized.evidence[0].evidenceId);
    expect(recognized.badge?.supportingEvidenceRefs).toEqual(recognized.evidence.map((item) => item.evidenceId));
    expect(recognized.opportunity).toMatchObject({ kind: "club-invitation", status: "available", personRef });
    expect(recognized.scenario.person.membershipStatus).toBe("external");

    expect(await runtime.provider.reset()).toEqual(initial);
  });
});