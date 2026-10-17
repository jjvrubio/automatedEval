import { describe, expect, it } from "vitest";
import appSource from "@/app/App.tsx?raw";
import { projectSnapshot } from "@/demo/mock-adapter";
import { resolveDemo } from "./bootstrap";
import { hospitalityFixture, retailFixture } from "./fixtures";

describe("runtime state and Activity projection", () => {
  it("derives Activity visual fields instead of storing them as factual input", () => {
    const sourceRecord = hospitalityFixture.activityRecords[0];
    const activity = projectSnapshot(hospitalityFixture).activity[0];

    expect(sourceRecord).not.toHaveProperty("icon");
    expect(sourceRecord).not.toHaveProperty("tone");
    expect(activity).toMatchObject({
      id: sourceRecord.id,
      icon: "home",
      tone: "cyan",
      provenance: "mocked",
      displayDate: expect.any(String),
    });
  });

  it("projects distinct Activity read models for both fixtures", () => {
    expect(projectSnapshot(retailFixture).activity).toEqual(
      expect.arrayContaining([
        expect.objectContaining({ id: "activity-purchase", icon: "star" }),
      ]),
    );
    expect(projectSnapshot(hospitalityFixture).activity).toEqual(
      expect.arrayContaining([
        expect.objectContaining({ id: "stay-confirmed", icon: "home" }),
      ]),
    );
  });

  it("keeps evidence distinct from its optional TES Event interpretation", async () => {
    const runtime = resolveDemo("hospitality-stay");
    const action = runtime.script?.steps[0].action;

    if (!action) throw new Error("Hospitality Script ausente.");
    if (!("evidence" in action)) throw new Error("Evidence ausente.");
    expect(action.evidence).toMatchObject({
      id: "evidence-check-in-AS-8842",
      interpretation: {
        id: "event-arrival-AS-8842",
        experienceRef: "experience:arrival-welcome@1",
      },
    });

    const snapshot = await runtime.provider.executeAction(action);
    expect(snapshot.activity[0]).toMatchObject({
      id: action.evidence.id,
      title: "booking.checked_in",
      icon: "activity",
    });
  });

  it("resolves providers outside the application core", () => {
    expect(appSource).not.toContain("MockDataAdapter");
    expect(appSource).not.toContain("retailFixture");
    expect(appSource).not.toContain("hospitalityFixture");
  });
});
