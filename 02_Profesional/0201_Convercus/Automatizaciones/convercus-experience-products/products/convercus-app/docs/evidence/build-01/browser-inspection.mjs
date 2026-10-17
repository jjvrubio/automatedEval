import { chromium } from "/Applications/Codex.app/Contents/Resources/cua_node/lib/node_modules/playwright-core/index.mjs";
import { mkdir, writeFile } from "node:fs/promises";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import assert from "node:assert/strict";
const out = join(dirname(fileURLToPath(import.meta.url)), "browser-final");
await mkdir(out);
const report = { tool: "Standalone Playwright 1.57.0 + installed Microsoft Edge, headless, temporary profile", reason: "In-app browser skill read; no node_repl js or discovery tool exposed in this session. No in-app browser controlled.", humanUXAcceptance: "NOT EXECUTED", phases: [], pageErrors: [], consoleErrors: [] };
let browser;
try {
  browser = await chromium.launch({ executablePath: "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge", headless: true });
  report.browserVersion = browser.version();
  for (const [layout, viewport, modality, level] of [["desktop", { width: 1280, height: 960 }, "Bienestar", "Intenso"], ["mobile", { width: 390, height: 844 }, "Social", "Suave"]]) {
    const context = await browser.newContext({ viewport, locale: "es-ES" });
    const page = await context.newPage();
    page.on("pageerror", e => report.pageErrors.push(String(e)));
    page.on("console", e => { if (e.type() === "error") report.consoleErrors.push(e.text()); });
    const record = async (phase, screenshot = false) => {
      const text = await page.locator(".sports-shell").innerText();
      const overflow = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth);
      assert.equal(overflow, false, layout + " horizontal overflow at " + phase);
      report.phases.push({ layout, phase, url: page.url(), text, horizontalOverflow: overflow });
      if (screenshot) { await page.evaluate(() => window.scrollTo(0, 0)); await page.screenshot({ path: join(out, layout + "-" + phase + ".png"), fullPage: true }); }
    };
    await page.goto("http://127.0.0.1:4173/?demo=sports-season-running");
    await page.getByRole("heading", { name: "Una temporada para moverse" }).waitFor();
    await record("initial", true);
    assert.equal(await page.getByText("Sólo informativo", { exact: true }).count(), 2);
    await page.getByRole("button", { name: "Elegir Carrera", exact: true }).click();
    await page.getByRole("button", { name: "Confirmar inscripción", exact: true }).click();
    await page.getByRole("alert").filter({ hasText: "Elige Social o Bienestar" }).waitFor();
    const alertBox = await page.getByRole("alert").boundingBox();
    assert.ok(alertBox && alertBox.y >= 0 && alertBox.y + alertBox.height <= viewport.height, "registration error visible without scrolling");
    await record("registration-error", true);
    await page.getByRole("radio", { name: new RegExp("^" + modality) }).check();
    await page.getByRole("button", { name: "Confirmar inscripción", exact: true }).click();
    await page.getByRole("heading", { name: "Inscripción confirmada" }).waitFor();
    await record("registered");
    await page.getByRole("button", { name: "Simular check-in", exact: true }).click();
    await page.getByText("Check-in simulado registrado. No acredita asistencia física real.", { exact: true }).waitFor();
    await record("presence");
    await page.getByRole("button", { name: "Registrar esfuerzo", exact: true }).click();
    await page.getByRole("alert").filter({ hasText: "Elige un esfuerzo" }).waitFor();
    const effortErrorBox = await page.getByRole("alert").boundingBox();
    assert.ok(effortErrorBox && effortErrorBox.y >= 0 && effortErrorBox.y + effortErrorBox.height <= viewport.height, "effort error visible without scrolling");
    await record("effort-error");
    await page.getByRole("radio", { name: level, exact: true }).check();
    await page.getByRole("button", { name: "Registrar esfuerzo", exact: true }).click();
    await page.getByRole("heading", { name: "Primeros kilómetros", exact: true }).waitFor();
    await record("badge", true);
    await page.getByRole("button", { name: "Conocer Club Brisa", exact: true }).click();
    await page.getByText(/sigues siendo participante externo/).waitFor();
    await record("invitation");
    await page.getByRole("button", { name: "Marketing / CRM", exact: true }).click();
    await page.getByRole("heading", { name: "La participación, con contexto." }).waitFor();
    const crm = await page.locator("#sports-main").innerText();
    for (const required of ["simulated-check-in", "participant-self-report", "Primeros kilómetros", modality, "Sin alta, consentimiento, conversión ni lead enviado."]) assert.ok(crm.includes(required), required);
    await record("crm", true);
    await page.getByRole("button", { name: "Participante", exact: true }).click();
    await page.getByRole("heading", { name: "Primeros kilómetros", exact: true }).waitFor();
    await record("return-to-participant");
    await page.getByRole("button", { name: "Reiniciar demo", exact: true }).click();
    await page.getByRole("button", { name: "Elegir Carrera", exact: true }).waitFor();
    assert.equal(await page.getByRole("heading", { name: "Primeros kilómetros", exact: true }).count(), 0);
    await record("reset", true);
    await context.close();
  }
  assert.deepEqual(report.pageErrors, []);
  assert.deepEqual(report.consoleErrors, []);
  report.status = "PASS";
} catch (e) {
  report.status = "FAIL";
  report.error = String(e.stack ?? e);
  process.exitCode = 1;
} finally {
  await browser?.close();
  await writeFile(join(out, "report.json"), JSON.stringify(report, null, 2) + "\n");
  console.log(JSON.stringify({ status: report.status, phases: report.phases.length, error: report.error, output: out }));
}
