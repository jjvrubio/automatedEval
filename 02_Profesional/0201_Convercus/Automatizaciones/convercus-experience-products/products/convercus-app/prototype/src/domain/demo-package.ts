import type { DemoPackage } from "./contracts";

function duplicatedIds(ids: string[]): string[] {
  const seen = new Set<string>();
  const duplicates = new Set<string>();

  ids.forEach((id) => {
    if (seen.has(id)) duplicates.add(id);
    seen.add(id);
  });

  return [...duplicates];
}

export function validateDemoPackage(candidate: DemoPackage): string[] {
  const issues: string[] = [];

  if (!Number.isInteger(candidate.schemaVersion) || candidate.schemaVersion < 1) {
    issues.push("schemaVersion debe ser un entero positivo.");
  }

  if (!candidate.id.trim() || !candidate.name.trim() || !candidate.brandId.trim()) {
    issues.push("El paquete debe declarar id, name y brandId.");
  }

  duplicatedIds(candidate.capabilities.capabilities.map(({ id }) => id)).forEach((id) => {
    issues.push(`La capacidad ${id} está duplicada.`);
  });

  duplicatedIds(candidate.experiences.map(({ id }) => id)).forEach((id) => {
    issues.push(`La Experience ${id} está duplicada.`);
  });

  if (candidate.tesApplicability === "required") {
    if (!candidate.tesBaseline) {
      issues.push("Una demo TES obligatoria debe declarar tesBaseline.");
    }
    if (candidate.experiences.length === 0) {
      issues.push("Una demo TES obligatoria debe declarar al menos una Experience.");
    }
  }

  if (candidate.tesApplicability === "not_applicable" && candidate.experiences.length > 0) {
    issues.push("Una demo sin aplicabilidad TES no puede declarar Experiences.");
  }

  return issues;
}

export function assertValidDemoPackage(candidate: DemoPackage): DemoPackage {
  const issues = validateDemoPackage(candidate);

  if (issues.length > 0) {
    throw new Error(`DemoPackage no válido:\n- ${issues.join("\n- ")}`);
  }

  return candidate;
}
