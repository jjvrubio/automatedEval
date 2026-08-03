import { describe, expect, it } from "vitest";
import type { SignificantEvent } from "@/domain/contracts";
import { MockDataAdapter } from "./mock-adapter";

const event: SignificantEvent = {
  id: "event-a0",
  type: "demo.started",
  occurredAt: "2026-08-03T10:00:00Z",
  source: "test",
  reliability: "confirmed",
  properties: { deterministic: true },
};

describe("MockDataAdapter", () => {
  it("isolates its internal state from returned snapshots", async () => {
    const adapter = new MockDataAdapter();
    const snapshot = await adapter.getSnapshot();

    snapshot.member.points = 0;
    snapshot.activity.length = 0;

    await expect(adapter.getSnapshot()).resolves.toMatchObject({
      member: { points: 1240 },
      activity: expect.arrayContaining([expect.objectContaining({ id: "activity-purchase" })]),
    });
  });

  it("dispatches events and resets deterministically", async () => {
    const adapter = new MockDataAdapter();

    const dispatched = await adapter.dispatch(event);
    expect(dispatched.activity[0]).toMatchObject({ id: event.id, title: event.type });
    await expect(adapter.reset()).resolves.toMatchObject({
      member: { id: "member-demo-001", points: 1240 },
      activity: expect.arrayContaining([expect.objectContaining({ id: "activity-purchase" })]),
    });
  });
});
