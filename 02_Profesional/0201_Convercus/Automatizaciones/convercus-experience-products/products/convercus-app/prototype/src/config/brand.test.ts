import { describe, expect, it } from "vitest";
import { brand, brandAssets, getBrandCssVariables } from "./brand";

describe("shared Convercus brand", () => {
  it("loads the governed brand configuration", () => {
    expect(brand.brand_id).toBe("convercus");
    expect(brand.accessibility.target).toBe("WCAG_2_2_AA");
    expect(brand.typography.primary.runtime_status).toBe("available_offline");
    expect(brand.typography.secondary.runtime_status).toBe(
      "blocked_for_distribution_until_license_verified",
    );
  });

  it("maps accessible product roles to CSS variables", () => {
    const variables = getBrandCssVariables(brand);

    expect(variables["--color-primary"]).toBe("#090685");
    expect(variables["--color-on-primary"]).toBe("#FFFFFF");
    expect(variables["--color-on-accent"]).toBe("#000000");
  });

  it("bundles the two official logo variants", () => {
    expect(brandAssets.logoPrimaryUrl).toContain("Convercus");
    expect(brandAssets.logoReversedUrl).toContain("Convercus");
  });
});

