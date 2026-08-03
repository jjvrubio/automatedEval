import appConfigSource from "../../../config/app.yaml?raw";
import type { DataMode } from "@/domain/contracts";
import { parse } from "yaml";

const dataModes = ["mock", "simulation", "staging", "production"] as const;
const experienceSupportValues = ["not_applicable", "conditional", "required"] as const;

interface AppConfigSource {
  schema_version: number;
  app_id: string;
  name: string;
  default_locale: string;
  brand_id: string;
  default_data_mode: DataMode;
  tes_baseline: string;
  experience_support: (typeof experienceSupportValues)[number];
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function readAppConfig(source: string): AppConfigSource {
  const value: unknown = parse(source);

  if (
    !isRecord(value) ||
    value.schema_version !== 1 ||
    typeof value.app_id !== "string" ||
    typeof value.name !== "string" ||
    typeof value.default_locale !== "string" ||
    typeof value.brand_id !== "string" ||
    typeof value.tes_baseline !== "string" ||
    !dataModes.includes(value.default_data_mode as DataMode) ||
    !experienceSupportValues.includes(
      value.experience_support as AppConfigSource["experience_support"],
    )
  ) {
    throw new Error("La configuración de Convercus App no es válida.");
  }

  return value as unknown as AppConfigSource;
}

const source = readAppConfig(appConfigSource);

export const appConfig = {
  schemaVersion: source.schema_version,
  appId: source.app_id,
  name: source.name,
  defaultLocale: source.default_locale,
  brandId: source.brand_id,
  dataMode: source.default_data_mode,
  tesBaseline: source.tes_baseline,
  experienceSupport: source.experience_support,
} as const;
