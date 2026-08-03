import brandSource from "@convercus-brand/brand.yaml?raw";
import logoPrimaryUrl from "@convercus-brand/assets/Convercus Logo RGB.svg?url";
import logoReversedUrl from "@convercus-brand/assets/Convercus Logo White.svg?url";
import { parse } from "yaml";

type ColorMap = Record<string, string>;

export interface BrandConfig {
  schema_version: number;
  brand_id: string;
  name: string;
  colors: {
    primitives: ColorMap;
    roles: ColorMap;
    on_color: ColorMap;
  };
  accessibility: {
    target: string;
    minimum_normal_text_contrast: number;
  };
  typography: {
    primary: {
      family: string;
      fallback: string;
      runtime_status: string;
    };
    secondary: {
      family: string;
      fallback: string;
      runtime_status: string;
    };
  };
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function readBrandConfig(source: string): BrandConfig {
  const value: unknown = parse(source);

  if (!isRecord(value) || value.brand_id !== "convercus") {
    throw new Error("La configuración de marca Convercus no es válida.");
  }

  if (!isRecord(value.colors) || !isRecord(value.typography)) {
    throw new Error("La marca debe declarar colores y tipografía.");
  }

  return value as unknown as BrandConfig;
}

export const brand = readBrandConfig(brandSource);

export const brandAssets = {
  logoPrimaryUrl,
  logoReversedUrl,
} as const;

export function getBrandCssVariables(config: BrandConfig): Record<string, string> {
  const { roles, on_color: onColor } = config.colors;

  return {
    "--color-primary": roles.primary,
    "--color-primary-action": roles.primary_action,
    "--color-accent": roles.accent,
    "--color-highlight": roles.highlight,
    "--color-background": roles.background,
    "--color-surface": roles.surface,
    "--color-surface-tinted": roles.surface_tinted,
    "--color-text": roles.text,
    "--color-text-strong": roles.text_strong,
    "--color-text-muted": roles.text_muted,
    "--color-border": roles.border,
    "--color-focus": roles.focus_ring,
    "--color-on-primary": onColor.on_primary,
    "--color-on-action": onColor.on_primary_action,
    "--color-on-accent": onColor.on_accent,
    "--font-primary": `"${config.typography.primary.family}", ${config.typography.primary.fallback}`,
  };
}

export function applyBrandCssVariables(
  target: Pick<CSSStyleDeclaration, "setProperty">,
  config: BrandConfig = brand,
): void {
  Object.entries(getBrandCssVariables(config)).forEach(([property, value]) => {
    target.setProperty(property, value);
  });
}

