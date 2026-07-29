"""Specialist web researchers for Stage 2."""

from __future__ import annotations

import json
from copy import deepcopy
from typing import Any

from stage1.csv_input import InputRow
from stage1.research import OpenAIWebResearcher, SOURCE_SCHEMA


FINDING_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "category": {"type": "string"},
        "title": {"type": "string"},
        "date": {"type": "string"},
        "status": {
            "type": "string",
            "enum": ["confirmed", "indicated", "unknown"],
        },
        "finding": {"type": "string"},
        "business_relevance": {"type": "string"},
        "evidence": {"type": "array", "items": SOURCE_SCHEMA},
    },
    "required": [
        "category",
        "title",
        "date",
        "status",
        "finding",
        "business_relevance",
        "evidence",
    ],
    "additionalProperties": False,
}

SIGNAL_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "strength": {"type": "string", "enum": ["high", "medium", "low"]},
        "rationale": {"type": "string"},
        "evidence_urls": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": ["title", "strength", "rationale", "evidence_urls"],
    "additionalProperties": False,
}

STAKEHOLDER_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "role": {"type": "string"},
        "relevance": {"type": "string"},
        "linkedin_url": {"type": "string"},
        "evidence": {"type": "array", "items": SOURCE_SCHEMA},
    },
    "required": ["name", "role", "relevance", "linkedin_url", "evidence"],
    "additionalProperties": False,
}

THEME_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "theme": {"type": "string"},
        "executive_summary": {"type": "string"},
        "current_state": {"type": "string"},
        "findings": {"type": "array", "items": FINDING_SCHEMA},
        "opportunity_signals": {"type": "array", "items": SIGNAL_SCHEMA},
        "risks": {"type": "array", "items": {"type": "string"}},
        "stakeholders": {"type": "array", "items": STAKEHOLDER_SCHEMA},
        "potentiality_score": {
            "type": "integer",
            "minimum": 0,
            "maximum": 10,
        },
        "score_rationale": {"type": "string"},
        "recommended_discovery_questions": {
            "type": "array",
            "items": {"type": "string"},
        },
        "evidence_quality": {
            "type": "string",
            "enum": ["high", "medium", "low"],
        },
        "missing_information": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": [
        "theme",
        "executive_summary",
        "current_state",
        "findings",
        "opportunity_signals",
        "risks",
        "stakeholders",
        "potentiality_score",
        "score_rationale",
        "recommended_discovery_questions",
        "evidence_quality",
        "missing_information",
    ],
    "additionalProperties": False,
}

SECTOR_PROFILES = [
    "fashion_retail",
    "food_retail",
    "furniture_retail",
    "pharmacy_retail",
    "other_retail",
    "hotel",
    "restaurant",
    "urban_transport",
    "other_allowed",
    "excluded_banking",
    "excluded_insurance",
    "excluded_security",
    "excluded_public_administration",
    "unknown",
]

class Stage2WebResearcher(OpenAIWebResearcher):
    """Three evidence-focused logical agents sharing one API client."""

    def research_technology(
        self,
        row: InputRow,
        eligibility_context: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        prompt = self._context(row, eligibility_context) + """
Rol: investigador especialista en tecnología retail y experiencia de cliente.

Objetivo: reconstruir con evidencia pública la tecnología y capacidades
digitales actuales de la compañía, y detectar necesidades relevantes para
Convercus sin inventar proveedores ni funcionalidades.

Explora en profundidad el dominio oficial, ecommerce, política de privacidad y
cookies, páginas de ayuda, checkout, empleo y notas de prensa; usa también
LinkedIn corporativo, app stores, ofertas de trabajo, casos de proveedores y
medios tecnológicos fiables. Realiza búsquedas de seguimiento.

Primero clasifica el sector. Son sectores excluidos: banca, seguros, cuerpos o
empresas de seguridad y administraciones públicas. Los operadores de autobús,
metro y transporte urbano están expresamente permitidos aunque tengan propiedad
pública.

Investiga siempre Martech, CRM, CDP, IA aplicada, fidelización, marketing
automation, atención al cliente, analítica/datos y pagos. Adapta después:
- retail de moda, alimentación, mobiliario, farmacia u otro: profundiza en
  TPV/POS, ERP, OMS, WMS, PIM, inventario, promociones, ecommerce, devoluciones
  y omnicanalidad;
- hoteles: PMS, CRS/motor de reservas, channel manager, RMS, reputación/reseñas,
  guest messaging, CRM/CDP y TPV de restauración;
- restauración: TPV/POS, reservas, KDS, delivery/agregadores, inventario,
  fidelización y CRM/CDP;
- transporte urbano: ticketing/AFC, validadores, pagos, MaaS/app, CRM,
  información al viajero y atención.

Distingue proveedor confirmado, indicio técnico y ausencia de evidencia.

Las oportunidades deben derivarse de hechos recuperados. No atribuyas pain
points, ROI, ACV ni capacidades de Convercus no demostradas. Puntúa 0-10 la
potencialidad comercial de esta dimensión, no la calidad general de la empresa.
Éxito: hallazgos recientes y citados, contradicciones visibles, preguntas de
discovery que cubran las lagunas y un límite claro cuando no haya evidencia.
""".strip()
        return self._call(
            "stage2_technology",
            prompt,
            schema=self._technology_schema(
                [
                    "ecommerce",
                    "crm",
                    "loyalty",
                    "customer_service",
                    "marketing_automation",
                    "data_analytics",
                    "erp",
                    "payments",
                    "mobile_app",
                    "omnichannel",
                    "infrastructure",
                    "pos_tpv",
                    "oms",
                    "wms",
                    "pim",
                    "inventory",
                    "ai",
                    "pms",
                    "booking_crs",
                    "channel_manager",
                    "rms",
                    "reputation_reviews",
                    "kds",
                    "reservations",
                    "delivery_aggregators",
                    "ticketing_afc",
                    "maas",
                    "other",
                ]
            ),
            max_tool_calls=12,
            reasoning_effort="low",
        )

    def research_corporate(
        self,
        row: InputRow,
        eligibility_context: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        prompt = self._context(row, eligibility_context) + """
Rol: investigador de inteligencia corporativa, liderazgo y cambio.

Objetivo: detectar durante los últimos 36 meses cambios directivos y
organizativos, resultados financieros, adquisiciones, financiación, alianzas,
reestructuraciones y declaraciones estratégicas que puedan abrir o cerrar una
oportunidad comercial.

Prioriza fuentes corporativas, registros, entrevistas, LinkedIn de la empresa y
directivos, y prensa económica reconocida. Confirma nombres, cargos y fechas;
no confundas nombramientos antiguos con actuales ni marca con sociedad o grupo.
Usa hechos anteriores solo como contexto explícito.

Relaciona cada señal con su relevancia comercial sin afirmar necesidades
internas no publicadas. No inventes contactos, emails, ROI o presupuestos.
Puntúa 0-10 la potencialidad de esta dimensión y formula preguntas concretas
para validar hipótesis en discovery.
""".strip()
        return self._call(
            "stage2_corporate",
            prompt,
            schema=self._schema(
                [
                    "leadership_change",
                    "financial_performance",
                    "organization",
                    "partnership",
                    "acquisition",
                    "funding",
                    "strategy",
                    "other",
                ]
            ),
            max_tool_calls=12,
            reasoning_effort="low",
        )

    def research_expansion(
        self,
        row: InputRow,
        eligibility_context: dict[str, Any],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        prompt = self._context(row, eligibility_context) + """
Rol: investigador de expansión, mercados y red de distribución.

Objetivo: reconstruir aperturas y cierres, entrada en países, franquicias,
corners, mayoristas, ecommerce, marketplaces, logística y planes anunciados,
priorizando los últimos 36 meses.

Explora el localizador y las noticias del sitio oficial, LinkedIn corporativo,
prensa retail y económica, socios, centros comerciales y distribuidores. Separa
hechos realizados de planes; deduplica aperturas; distingue tiendas propias,
franquicias, corners, terceros y canales digitales. Declara el perímetro.

Identifica señales de complejidad omnicanal o crecimiento que puedan justificar
una conversación comercial, sin convertir expansión en un problema supuesto.
No inventes países, fechas, volúmenes, ROI ni presupuestos. Puntúa 0-10 la
potencialidad de esta dimensión y deja preguntas para las lagunas materiales.
""".strip()
        return self._call(
            "stage2_expansion",
            prompt,
            schema=self._schema(
                [
                    "market_entry",
                    "store_opening",
                    "store_closure",
                    "franchise",
                    "corner",
                    "distribution",
                    "ecommerce",
                    "marketplace",
                    "logistics",
                    "internationalization",
                    "other",
                ]
            ),
            max_tool_calls=12,
            reasoning_effort="low",
        )

    @staticmethod
    def _schema(categories: list[str]) -> dict[str, Any]:
        schema = deepcopy(THEME_SCHEMA)
        schema["properties"]["findings"]["items"]["properties"]["category"] = {
            "type": "string",
            "enum": categories,
        }
        return schema

    @classmethod
    def _technology_schema(cls, categories: list[str]) -> dict[str, Any]:
        schema = cls._schema(categories)
        schema["properties"].update(
            {
                "sector_profile": {
                    "type": "string",
                    "enum": SECTOR_PROFILES,
                },
                "sector_eligibility": {
                    "type": "string",
                    "enum": ["allowed", "excluded", "review"],
                },
                "sector_rationale": {"type": "string"},
            }
        )
        schema["required"].extend(
            ["sector_profile", "sector_eligibility", "sector_rationale"]
        )
        return schema

    @staticmethod
    def _context(
        row: InputRow,
        eligibility_context: dict[str, Any],
    ) -> str:
        seeds = {
            "company_name": row.company_name,
            "website": row.values.get("Website", ""),
            "linkedin": row.values.get("Company Linkedin Url", ""),
        }
        return (
            "Semillas de identidad:\n"
            + json.dumps(seeds, ensure_ascii=False, indent=2)
            + "\n\nEvidencia validada en Etapa 1:\n"
            + json.dumps(eligibility_context, ensure_ascii=False, indent=2)
            + "\n\n"
        )
