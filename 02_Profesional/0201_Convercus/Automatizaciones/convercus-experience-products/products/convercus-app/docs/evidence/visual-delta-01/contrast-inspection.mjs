import { chromium } from "/Applications/Codex.app/Contents/Resources/cua_node/lib/node_modules/playwright-core/index.mjs";
import { writeFile } from "node:fs/promises";
import assert from "node:assert/strict";

const report = { states: [], checks: [], limitations: "Local colour checks, not a general accessibility audit. Solid computed backgrounds; disabled controls excluded. Decorative SVG and phone hardware reviewed visually." };
const browser = await chromium.launch({ executablePath: "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge", headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1280, height: 960 } });
  await page.goto("http://127.0.0.1:4173/?demo=sports-season-running");
  await page.getByRole("heading", { name: "Una temporada para moverse" }).waitFor();
  await page.evaluate(() => document.fonts.ready);
  const inspect = async (state) => {
    const result = await page.locator(".sports-shell").evaluate(shell => {
      const parse = value => value.match(/[\d.]+/g).map(Number);
      const composite = (top, bottom) => top.slice(0, 3).map((v, i) => v * (top[3] ?? 1) + bottom[i] * (1 - (top[3] ?? 1)));
      const bg = el => el ? composite(parse(getComputedStyle(el).backgroundColor), bg(el.parentElement)) : [255, 255, 255];
      const luminance = color => color.slice(0, 3).map(v => v / 255).map(v => v <= .04045 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4).reduce((sum, v, i) => sum + v * [.2126, .7152, .0722][i], 0);
      const contrast = (a, b) => (Math.max(luminance(a), luminance(b)) + .05) / (Math.min(luminance(a), luminance(b)) + .05);
      const texts = [...shell.querySelectorAll("*")].filter(el => el.checkVisibility() && !el.closest(":disabled") && [...el.childNodes].some(node => node.nodeType === 3 && node.textContent.trim())).map(el => {
        const style = getComputedStyle(el);
        const background = bg(el);
        const foreground = composite(parse(style.color), background);
        const ratio = contrast(foreground, background);
        const minimum = parseFloat(style.fontSize) >= 24 || (parseFloat(style.fontSize) >= 18.66 && Number(style.fontWeight) >= 700) ? 3 : 4.5;
        return { text: el.textContent.trim().slice(0, 100), foreground, background, ratio, minimum, pass: ratio >= minimum };
      });
      const graphicChecks = [];
      const medal = shell.querySelector(".sports-medallion");
      if (medal) graphicChecks.push({ role: "recognition symbol", ratio: contrast(parse(getComputedStyle(medal).color), bg(medal)) });
      const selected = shell.querySelector(".sports-option.is-selected");
      if (selected) graphicChecks.push({ role: "selected option border", ratio: contrast(parse(getComputedStyle(selected).borderTopColor), bg(selected)) });
      const focused = document.activeElement;
      if (focused?.matches(":focus-visible") && shell.contains(focused)) graphicChecks.push({ role: "keyboard focus against surrounding surface", ratio: contrast(parse(getComputedStyle(focused).outlineColor), bg(focused.parentElement)), width: getComputedStyle(focused).outlineWidth });
      return { texts, graphicChecks };
    });
    report.states.push({ state, ...result });
    assert.deepEqual(result.texts.filter(item => !item.pass), [], state + " text contrast");
    for (const check of result.graphicChecks) assert.ok(check.ratio >= 3, state + ": " + check.role);
  };
  await page.keyboard.press("Tab");
  await page.keyboard.press("Tab");
  await inspect("initial with keyboard focus");
  await page.getByRole("button", { name: "Elegir Carrera", exact: true }).click();
  await page.getByRole("button", { name: "Confirmar inscripción", exact: true }).click();
  await page.getByRole("alert").waitFor();
  await inspect("registration error");
  await page.getByRole("radio", { name: /^Bienestar/ }).check();
  await inspect("selected modality");
  await page.getByRole("button", { name: "Confirmar inscripción", exact: true }).click();
  await page.getByRole("button", { name: "Simular check-in", exact: true }).click();
  await page.getByRole("button", { name: "Registrar esfuerzo", exact: true }).click();
  await page.getByRole("alert").waitFor();
  await inspect("effort error");
  await page.getByRole("radio", { name: "Intenso", exact: true }).check();
  await page.getByRole("button", { name: "Registrar esfuerzo", exact: true }).click();
  await page.getByRole("heading", { name: "Primeros kilómetros", exact: true }).waitFor();
  await inspect("recognition");
  await page.getByRole("button", { name: "Marketing / CRM", exact: true }).click();
  await page.getByRole("heading", { name: "La participación, con contexto." }).waitFor();
  await inspect("CRM");
  await page.goto("http://127.0.0.1:4173/showcase?demo=sports-season-running");
  const phone = page.frameLocator("iframe");
  await phone.getByRole("heading", { name: "Una temporada para moverse" }).waitFor();
  await page.evaluate(() => document.fonts.ready);
  await phone.locator("html").evaluate(() => document.fonts.ready);
  assert.equal(await phone.locator("html").evaluate(el => el.scrollWidth > innerWidth), false);
  await page.screenshot({ path: new URL("./phone-after.png", import.meta.url).pathname, fullPage: true });
  report.checks.push("Phone entry renders the same composition without horizontal overflow.");
  report.status = "PASS";
} catch (error) {
  report.status = "FAIL";
  report.error = String(error.stack ?? error);
  process.exitCode = 1;
} finally {
  await browser.close();
  await writeFile(new URL("./contrast-report.json", import.meta.url), JSON.stringify(report, null, 2) + "\n");
  console.log(JSON.stringify({ status: report.status, states: report.states.length, samples: report.states.reduce((n, s) => n + s.texts.length, 0), error: report.error }));
}
