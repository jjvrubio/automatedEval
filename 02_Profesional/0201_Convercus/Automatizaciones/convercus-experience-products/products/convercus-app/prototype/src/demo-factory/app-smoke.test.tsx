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

async function renderDemo(demoId: string): Promise<string> {
  const container = document.createElement("div");
  document.body.append(container);
  const root = createRoot(container);

  await act(async () => {
    root.render(
      <MemoryRouter>
        <App runtime={resolveDemo(demoId)} />
      </MemoryRouter>,
    );
  });

  const rendered = container.innerHTML;
  await act(async () => root.unmount());
  return rendered;
}

describe("one application core, two demos", () => {
  it("renders Retail without Hospitality identity or content", async () => {
    const rendered = await renderDemo("retail-baseline");

    expect(rendered).toContain("Alex");
    expect(rendered).toContain('alt="Convercus"');
    expect(rendered).not.toMatch(/Aurora Stay|Lucía|Estancia confirmada/);
  });

  it("renders Hospitality without Retail identity or content", async () => {
    const rendered = await renderDemo("hospitality-stay");

    expect(rendered).toContain("Lucía");
    expect(rendered).toContain('alt="Aurora Stay"');
    expect(rendered).toContain("Lisboa empieza en Aurora");
    expect(rendered).not.toMatch(/Alex|Compra registrada|20% de bienvenida/);
  });
});
