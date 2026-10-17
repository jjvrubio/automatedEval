import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { afterEach, expect, it } from "vitest";
import { DemoApp } from "@/app/App";
import { resolveAppDemo } from "../bootstrap";

Object.assign(globalThis, { IS_REACT_ACT_ENVIRONMENT: true });
afterEach(() => { document.body.innerHTML = ""; });
async function mount() {
  const runtime = resolveAppDemo("sports-season-running");
  if (!("kind" in runtime)) throw new Error("Sports composition absent");
  const el = document.createElement("div"); document.body.append(el);
  const root = createRoot(el);
  await act(async () => root.render(<MemoryRouter initialEntries={["/?demo=sports-season-running"]}><DemoApp runtime={runtime} /></MemoryRouter>));
  const click = async (label: string) => {
    const b = [...el.querySelectorAll("button")].find(b => b.textContent?.trim() === label);
    expect(b, label).toBeDefined(); expect(b!.disabled).toBe(false);
    await act(async () => b!.click());
  };
  const radio = async (value: string) => {
    const input = el.querySelector<HTMLInputElement>(`input[type="radio"][value="${value}"]`);
    expect(input).not.toBeNull(); await act(async () => input!.click());
  };
  return { el, runtime, click, radio, close: () => act(async () => root.unmount()) };
}

it.each([["Lea Martín", "P01"], ["Diego Vidal", "P02"]])("BUILD 02 %s: UI facts, Self Service and new badge continuity", async (name, id) => {
  const { el, runtime, click, radio, close } = await mount();
  try {
    expect(el.textContent).toContain("P03");
    await click("Elegir a " + name);
    expect(el.querySelectorAll(".sports-purchases li")).toHaveLength(8);
    expect(el.textContent).toContain("Tienda"); expect(el.textContent).toContain("Web");
    await click("Self Service");
    if (id === "P01") {
      expect(el.querySelector(".sports-program")).toBeNull();
      expect(el.textContent).toContain("Sin saldo de puntos ni nivel asignado");
      expect(el.querySelector(".sports-counterfactual")?.textContent).toContain("511 puntos potenciales");
      expect(el.querySelector(".sports-counterfactual")?.textContent).toContain("Active");
      expect(el.textContent).toContain("Entrenamiento abierto de carrera urbana");
    } else {
      expect(el.querySelector(".sports-program")?.textContent).toContain("731 puntos · nivel Pro");
      expect(el.querySelector(".sports-counterfactual")).toBeNull();
      expect(el.textContent).toContain("Constancia deportiva");
      expect(el.textContent).toContain("Explorador multideporte");
      expect(el.textContent).toContain("15% en equipamiento running seleccionado");
      expect(el.textContent).toContain("Vóley playa Sunset Session");
    }
    expect(el.querySelectorAll(".sports-news-grid article")).toHaveLength(3);
    await click("Volver a la temporada");
    await click("Leer QR de inscripción");
    expect(el.textContent).toContain("Cliente reconocido");
    expect(el.querySelector('input[type="text"]')).toBeNull();
    await click("Participar");
    expect(el.querySelectorAll(".sports-equipment-grid article")).toHaveLength(4);
    await radio("wellness"); await click("Confirmar inscripción");
    expect(el.textContent).toContain("Información adicional voluntaria");
    await click("Continuar sin aportar información");
    expect(el.textContent).toContain("QR de presencia");
    await click("Simular check-in"); await radio("medio"); await click("Registrar esfuerzo");
    await click("Ver mi insignia en Self Service");
    expect(el.querySelector(".sports-badge-list")?.textContent).toContain("Primeros kilómetros");
    expect(el.querySelector(".sports-badge-list")?.textContent).toContain("Sports Season · obtenida en esta sesión");
    expect(el.textContent).toContain("Completado");
    expect((await runtime.provider.getSnapshot()).userPlane?.relationship?.loyalty.pointsBalance).toBe(id === "P01" ? null : 731);
    await click("Volver a la temporada");
    await click(id === "P01" ? "Elegir a Diego Vidal" : "Elegir a Lea Martín");
    await click("Elegir a " + name); await click("Self Service");
    expect(el.querySelectorAll(".sports-badge-list li")).toHaveLength(id === "P01" ? 1 : 3);
  } finally { await close(); }
});

it("BUILD 02 information branch is interactive and remains a declaration in Self Service", async () => {
  const { el, runtime, click, close } = await mount();
  try {
    await click("Elegir a Lea Martín");
    await click("No participar, pero quiero recibir información");
    const input = el.querySelector<HTMLInputElement>('input[type="checkbox"]')!;
    await act(async () => input.click());
    await click("Registrar intereses");
    expect(el.textContent).toContain("Interés declarado registrado");
    await click("Self Service");
    expect(el.textContent).toContain("Intereses: Carrera");
    expect(el.querySelectorAll(".sports-badge-list li")).toHaveLength(0);
    const s = await runtime.provider.getSnapshot();
    expect(s.registration).toBeUndefined(); expect(s.evidence).toEqual([]);
  } finally { await close(); }
});
