import { appConfig } from "@/config/app-config";
import type { DemoPackage } from "@/domain/contracts";
import { assertValidDemoPackage } from "@/domain/demo-package";

const canonicalDemoPackageDefinition = {
  schemaVersion: 1,
  id: "convercus-canonical-demo",
  name: "Convercus Canonical Demo",
  brandId: appConfig.brandId,
  locale: appConfig.defaultLocale,
  dataMode: appConfig.dataMode,
  tesApplicability: appConfig.experienceSupport,
  tesBaseline: appConfig.tesBaseline,
  capabilities: {
    version: "1",
    capabilities: [
      { id: "member-profile", label: "Perfil de miembro", status: "mocked" },
      { id: "loyalty-balance", label: "Saldo y nivel", status: "mocked" },
      { id: "coupon-wallet", label: "Cupones", status: "mocked" },
      { id: "news-feed", label: "Noticias", status: "mocked" },
      { id: "activity-feed", label: "Actividad", status: "mocked" },
      {
        id: "experience-simulation",
        label: "Simulación de Experiences",
        status: "proposed",
        limitation: "Se implementará durante A3.",
      },
    ],
  },
  experiences: [],
} satisfies DemoPackage;

export const canonicalDemoPackage = assertValidDemoPackage(
  canonicalDemoPackageDefinition,
);
