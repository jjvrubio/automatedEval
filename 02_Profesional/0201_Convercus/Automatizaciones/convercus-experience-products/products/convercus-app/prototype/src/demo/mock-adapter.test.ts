import { describe, expect, it } from "vitest";
import type { DemoAction } from "@/demo-factory/contracts";
import { retailFixture } from "@/demo-factory/fixtures";
import { MockDataAdapter } from "./mock-adapter";

const action: DemoAction = {
  type: "scenario_action",
  actionId: "test-action",
  evidence: {
    id: "evidence-a0",
    type: "demo.started",
    occurredAt: "2026-08-03T10:00:00Z",
    source: "test",
    reliability: "confirmed",
    subjects: [],
    contexts: [],
  },
};

describe("MockDataAdapter", () => {
  it("isolates its internal state from returned snapshots", async () => {
    const adapter = new MockDataAdapter(retailFixture);
    const snapshot = await adapter.getSnapshot();

    snapshot.member.points = 0;
    snapshot.activity.length = 0;

    await expect(adapter.getSnapshot()).resolves.toMatchObject({
      member: { points: 1240 },
      activity: expect.arrayContaining([expect.objectContaining({ id: "activity-purchase" })]),
    });
  });

  it("rejects Scenario actions when no Scenario is configured", async () => {
    const adapter = new MockDataAdapter(retailFixture);

    await expect(adapter.executeAction(action)).rejects.toThrow(
      "Acción de Scenario no permitida",
    );
    await expect(adapter.reset()).resolves.toMatchObject({
      member: { id: "member-demo-001", points: 1240 },
      activity: expect.arrayContaining([expect.objectContaining({ id: "activity-purchase" })]),
    });
  });
});
