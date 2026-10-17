import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { registerSW } from "virtual:pwa-register";
import { DemoApp } from "@/app/App";
import {
  applyResolvedBrand,
  resolveAppDemo,
  selectDemoId,
} from "@/demo-factory/bootstrap";
import "@/styles/fonts.css";
import "@/styles/global.css";

registerSW({ immediate: true });

const root = document.getElementById("root");

if (!root) {
  throw new Error("No se encontró el contenedor raíz de Demo Factory.");
}

try {
  const runtime = resolveAppDemo(selectDemoId(window.location.search));
  applyResolvedBrand(document.documentElement.style, runtime.brand);
  document.title = `${runtime.brand.name} — Demo`;
  if ("kind" in runtime) {
    const icon = document.createElement("link");
    icon.rel = "icon";
    icon.href = runtime.brand.logoUrl;
    document.head.append(icon);
  }

  createRoot(root).render(
    <StrictMode>
      <BrowserRouter>
        <DemoApp runtime={runtime} />
      </BrowserRouter>
    </StrictMode>,
  );
} catch (error) {
  const message = error instanceof Error ? error.message : "Error de configuración desconocido.";
  createRoot(root).render(
    <main className="feedback-state feedback-state--page" role="alert">
      <h1>No se pudo iniciar la demo</h1>
      <p>{message}</p>
    </main>,
  );
}
