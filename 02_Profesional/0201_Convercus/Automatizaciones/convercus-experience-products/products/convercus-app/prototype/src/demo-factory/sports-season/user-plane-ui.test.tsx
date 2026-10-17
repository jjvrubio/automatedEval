import { act } from "react";
import { createRoot } from "react-dom/client";
import { MemoryRouter } from "react-router-dom";
import { afterEach, expect, it, vi } from "vitest";
import { DemoApp } from "@/app/App";
import { resolveAppDemo } from "../bootstrap";

Object.assign(globalThis, { IS_REACT_ACT_ENVIRONMENT: true });
afterEach(() => { document.body.innerHTML = ""; vi.restoreAllMocks(); });

async function mount() {
  const runtime = resolveAppDemo("sports-season-running");
  if (!("kind" in runtime)) throw new Error("Sports composition absent");
  const container = document.createElement("div"); document.body.append(container);
  const root = createRoot(container);
  const click = async (text: string) => {
    const button = [...container.querySelectorAll("button")].find(item => item.textContent?.trim() === text);
    expect(button, text).toBeDefined();
    expect(button!.disabled, text + " enabled").toBe(false);
    await act(async () => button!.click());
  };
  const radio = async (value: string) => {
    const input = container.querySelector<HTMLInputElement>(`input[type="radio"][value="${value}"]`);
    expect(input).not.toBeNull();
    await act(async () => input!.click());
  };
  await act(async () => root.render(<MemoryRouter initialEntries={["/?demo=sports-season-running"]}><DemoApp runtime={runtime} /></MemoryRouter>));
  return { runtime, container, click, radio, close: () => act(async () => root.unmount()) };
}

it("BUILD 02 visible primary path: recognized customer, counterfactual, required data, optional skip, unchanged badge and shared CRM", async () => {
  const { runtime, container, click, radio, close } = await mount();
  const provider = runtime.provider;
  const execute = vi.spyOn(provider, "executeAction");
  try {
    expect(container.textContent).toContain("¿Con quién quieres probar la demo?");
    expect(container.textContent).toContain("Vela");
    expect(container.textContent).toContain("Vóley playa");
    await click("Leer QR de inscripción");
    await click("Elegir a Lea Martín");
    expect(container.textContent).toContain("Cliente reconocido");
    expect(container.textContent).toContain("194 puntos potenciales");
    expect(container.textContent).toContain("no es saldo disponible");
    expect(container.querySelector('input[type="text"]')).toBeNull();
    expect(container.textContent).toContain("No participar, pero quiero recibir información");
    await click("Participar");
    expect(container.textContent).toContain("Equipamiento para Carrera");
    expect(container.textContent).toContain("Datos necesarios para inscribirse");
    await click("Confirmar inscripción");
    expect(container.querySelector('[role="alert"]')?.textContent).toContain("Elige Social o Bienestar");
    await radio("wellness");
    await click("Confirmar inscripción");
    expect(container.textContent).toContain("Información adicional voluntaria");
    await click("Compartir información y obtener la guía");
    expect(container.querySelector('[role="alert"]')?.textContent).toContain("Selecciona al menos una respuesta");
    await click("Continuar sin aportar información");
    expect((await provider.getSnapshot()).userPlane?.incentive).toBeUndefined();
    await click("Simular check-in");
    await radio("medio");
    await click("Registrar esfuerzo");
    expect(container.textContent).toContain("Primeros kilómetros");
    expect(container.textContent).toContain("194 puntos potenciales");
    const final = await provider.getSnapshot();
    const actions = execute.mock.calls.length;
    await click("Conocer Club Brisa");
    await click("Marketing / CRM");
    expect(container.textContent).toContain("Cliente conocido");
    expect(container.textContent).toContain("Externo · no pertenece al club");
    expect(container.textContent).toContain("participant-self-report");
    expect(await provider.getSnapshot()).toEqual(final);
    expect(execute).toHaveBeenCalledTimes(actions);
    await click("Reiniciar demo");
    expect(container.textContent).toContain("¿Con quién quieres probar la demo?");
    expect(container.textContent).not.toContain("194 puntos potenciales");
    expect((await provider.getSnapshot()).userPlane?.person).toBeUndefined();
  } finally { await close(); }
});

it("BUILD 02 visible member contrast and information-only branch produce declared interests without a registration", async () => {
  const { runtime, container, click, close } = await mount();
  try {
    await click("Elegir a Diego Vidal");
    expect(container.textContent).toContain("860 puntos · nivel Activo");
    expect(container.querySelector('.sports-counterfactual')).toBeNull();
    await click("No participar, pero quiero recibir información");
    await click("Registrar intereses");
    expect(container.querySelector('[role="alert"]')?.textContent).toContain("Elige al menos un interés");
    const checkbox = container.querySelector<HTMLInputElement>('input[type="checkbox"]');
    await act(async () => checkbox!.click());
    await click("Registrar intereses");
    expect(container.textContent).toContain("Interés declarado registrado");
    expect(container.textContent).toContain("No se envían comunicaciones");
    const snapshot = await runtime.provider.getSnapshot();
    expect(snapshot.userPlane?.declaredInterests?.values).toEqual(["running"]);
    expect(snapshot.registration).toBeUndefined();
    expect(snapshot.evidence).toEqual([]);
    expect(snapshot.badge).toBeUndefined();
    expect(snapshot.userPlane?.person?.program?.points).toBe(860);
    await click("Elegir a Lea Martín");
    const changed = await runtime.provider.getSnapshot();
    expect(changed.userPlane?.intention).toBeUndefined();
    expect(changed.userPlane?.declaredInterests).toBeUndefined();
    expect(container.textContent).not.toContain("Interés declarado registrado");
  } finally { await close(); }
});
