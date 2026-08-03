import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { registerSW } from "virtual:pwa-register";
import { App } from "@/app/App";
import { applyBrandCssVariables } from "@/config/brand";
import "@/styles/fonts.css";
import "@/styles/global.css";

applyBrandCssVariables(document.documentElement.style);
registerSW({ immediate: true });

const root = document.getElementById("root");

if (!root) {
  throw new Error("No se encontró el contenedor raíz de Convercus App.");
}

createRoot(root).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);

