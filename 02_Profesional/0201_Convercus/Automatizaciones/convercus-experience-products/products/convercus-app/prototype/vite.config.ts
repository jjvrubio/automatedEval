import { fileURLToPath, URL } from "node:url";
import react from "@vitejs/plugin-react";
import { searchForWorkspaceRoot } from "vite";
import { VitePWA } from "vite-plugin-pwa";
import { defineConfig } from "vitest/config";

const sharedBrandRoot = fileURLToPath(
  new URL("../../../03-shared-assets/brands/convercus", import.meta.url),
);
const appConfigRoot = fileURLToPath(new URL("../config", import.meta.url));

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: "autoUpdate",
      includeAssets: [],
      manifest: {
        name: "Convercus App",
        short_name: "Convercus",
        description: "Superficie mobile-first de fidelización Convercus",
        theme_color: "#090685",
        background_color: "#FFFFFF",
        display: "standalone",
        start_url: "/",
        lang: "es",
      },
      workbox: {
        globPatterns: ["**/*.{js,css,html,svg,ttf,woff2}"],
        navigateFallback: "index.html",
      },
    }),
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
      "@convercus-brand": sharedBrandRoot,
    },
  },
  server: {
    fs: {
      allow: [searchForWorkspaceRoot(process.cwd()), sharedBrandRoot, appConfigRoot],
    },
  },
  test: {
    environment: "jsdom",
    setupFiles: [],
    coverage: {
      reporter: ["text", "html"],
    },
  },
});
