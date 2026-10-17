import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { afterEach, describe, expect, it } from "vitest";
import { App } from "@/app/App";
import { resolveDemo } from "./bootstrap";

Object.assign(globalThis, { IS_REACT_ACT_ENVIRONMENT: true });

afterEach(() => {
  document.body.innerHTML = "";
});

describe("public presenter action", () => {
  it("starts Hospitality at its deterministic Scenario checkpoint", async () => {
    const runtime = resolveDemo("hospitality-stay");

    await expect(runtime.provider.getSnapshot()).resolves.toMatchObject({
      scenario: {
        checkpoint: "pre-arrival-confirmed",
        availableActionId: "confirm-arrival",
      },
    });
  });

  it("lets the Script invoke a public action owned by Scenario/runtime", async () => {
    const runtime = resolveDemo("hospitality-stay");
    const step = runtime.script?.steps[0];

    if (!step) throw new Error("Hospitality Script ausente.");
    if (!("evidence" in step.action)) throw new Error("Evidence ausente.");
    expect(step.action).not.toHaveProperty("fromCheckpoint");
    expect(step.action).not.toHaveProperty("toCheckpoint");
    expect(runtime.scenario?.presenterAction).toMatchObject({
      actionId: step.action.actionId,
      fromCheckpoint: "pre-arrival-confirmed",
      toCheckpoint: step.expectedCheckpoint,
    });

    await expect(runtime.provider.executeAction(step.action)).resolves.toMatchObject({
      scenario: { checkpoint: "checked-in" },
      activity: expect.arrayContaining([
        expect.objectContaining({
          id: step.action.evidence.id,
          provenance: "simulated",
        }),
      ]),
    });
  });

  it("produces the same read model from the same fixture and action", async () => {
    const first = resolveDemo("hospitality-stay");
    const second = resolveDemo("hospitality-stay");
    const action = first.script?.steps[0].action;

    if (!action) throw new Error("Hospitality Script ausente.");
    if (!("evidence" in action)) throw new Error("Evidence ausente.");
    const firstResult = await first.provider.executeAction(action);
    const secondResult = await second.provider.executeAction(action);

    expect(firstResult).toEqual(secondResult);
  });

  it("rejects a repeated action from an invalid checkpoint", async () => {
    const runtime = resolveDemo("hospitality-stay");
    const action = runtime.script?.steps[0].action;

    if (!action) throw new Error("Hospitality Script ausente.");
    if (!("evidence" in action)) throw new Error("Evidence ausente.");
    await runtime.provider.executeAction(action);
    await expect(runtime.provider.executeAction(action)).rejects.toThrow(
      "no permitida desde checkpoint checked-in",
    );
    await expect(runtime.provider.getSnapshot()).resolves.toMatchObject({
      scenario: { checkpoint: "checked-in" },
    });
  });

  it("resets Hospitality and cannot mutate Retail", async () => {
    const hospitality = resolveDemo("hospitality-stay");
    const retail = resolveDemo("retail-baseline");
    const retailBefore = await retail.provider.getSnapshot();
    const action = hospitality.script?.steps[0].action;

    if (!action) throw new Error("Hospitality Script ausente.");
    if (!("evidence" in action)) throw new Error("Evidence ausente.");
    await hospitality.provider.executeAction(action);
    await expect(hospitality.provider.reset()).resolves.toMatchObject({
      scenario: {
        checkpoint: "pre-arrival-confirmed",
        availableActionId: "confirm-arrival",
      },
      activity: expect.arrayContaining([
        expect.objectContaining({ id: "stay-confirmed" }),
      ]),
    });
    await expect(retail.provider.getSnapshot()).resolves.toEqual(retailBefore);
  });

  it("exposes the Script action and resulting checkpoint in the existing UI", async () => {
    const container = document.createElement("div");
    document.body.append(container);
    const root = createRoot(container);

    await act(async () => {
      root.render(
        <MemoryRouter initialEntries={["/system"]}>
          <App runtime={resolveDemo("hospitality-stay")} />
        </MemoryRouter>,
      );
    });

    const checkpointValue = () =>
      [...container.querySelectorAll("dt")]
        .find((term) => term.textContent === "Checkpoint")
        ?.nextElementSibling?.textContent;
    const actionButton = [...container.querySelectorAll("button")].find(
      (button) => button.textContent === "Confirmar llegada",
    );

    expect(checkpointValue()).toBe("pre-arrival-confirmed");
    expect(actionButton).toBeDefined();
    expect(actionButton?.disabled).toBe(false);

    await act(async () => actionButton?.click());

    expect(checkpointValue()).toBe("checked-in");
    expect(actionButton?.disabled).toBe(true);

    const activityLink = [...container.querySelectorAll("a")].find(
      (link) =>
        link.getAttribute("href") === "/activity" &&
        link.textContent?.trim() === "Actividad",
    );
    await act(async () => activityLink?.click());
    expect(container.textContent).toContain("booking.checked_in");

    await act(async () => root.unmount());
  });
});
