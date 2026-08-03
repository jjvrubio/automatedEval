import { describe, expect, it } from "vitest";
import { appConfig } from "./app-config";

describe("governed app configuration", () => {
  it("loads the product configuration from app.yaml", () => {
    expect(appConfig).toMatchObject({
      schemaVersion: 1,
      appId: "convercus-app",
      brandId: "convercus",
      dataMode: "mock",
      experienceSupport: "conditional",
    });
    expect(appConfig.tesBaseline).toBe("TES_CONVERCUS_BUILDER_2026_07_R1");
  });
});
