import { describe, expect, it } from "vitest";
import { canonicalDemoPackage } from "@/demo/canonical-demo-package";
import type { DemoPackage } from "./contracts";
import { assertValidDemoPackage, validateDemoPackage } from "./demo-package";

describe("DemoPackage contract", () => {
  it("accepts the canonical A0 package and declares every capability honestly", () => {
    expect(validateDemoPackage(canonicalDemoPackage)).toEqual([]);
    expect(canonicalDemoPackage.capabilities.capabilities).toHaveLength(6);
    expect(
      canonicalDemoPackage.capabilities.capabilities.every(({ status }) =>
        ["real", "simulated", "mocked", "proposed", "unsupported"].includes(status),
      ),
    ).toBe(true);
  });

  it("rejects a TES-required package without baseline or Experiences", () => {
    const invalidPackage: DemoPackage = {
      ...canonicalDemoPackage,
      id: "invalid-required-package",
      tesApplicability: "required",
      tesBaseline: undefined,
      experiences: [],
    };

    expect(() => assertValidDemoPackage(invalidPackage)).toThrow(
      "Una demo TES obligatoria debe declarar tesBaseline",
    );
    expect(validateDemoPackage(invalidPackage)).toHaveLength(2);
  });

  it("rejects duplicated capability identifiers", () => {
    const firstCapability = canonicalDemoPackage.capabilities.capabilities[0];
    const invalidPackage: DemoPackage = {
      ...canonicalDemoPackage,
      capabilities: {
        ...canonicalDemoPackage.capabilities,
        capabilities: [firstCapability, firstCapability],
      },
    };

    expect(validateDemoPackage(invalidPackage)).toContain(
      `La capacidad ${firstCapability.id} está duplicada.`,
    );
  });
});
