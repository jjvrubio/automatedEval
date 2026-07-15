#!/usr/bin/env python3
"""
Research companies from the first column of an Apollo CSV using OpenAI web search.

Outputs:
- CSV: flattened fields for sorting and filtering.
- JSONL: one full structured record per company, including sources.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_INPUT = Path(__file__).with_name("apollo-accounts-export.csv")
DEFAULT_OUTPUT = Path(__file__).with_name("company-research-results.csv")
DEFAULT_JSONL = Path(__file__).with_name("company-research-results.jsonl")

OUTPUT_FIELDS = [
    "researched_at",
    "source_row",
    "company_name",
    "canonical_name",
    "website",
    "linkedin_url",
    "country",
    "industry",
    "employee_count_estimate",
    "short_description",
    "business_model",
    "products_services",
    "target_customers",
    "brands_or_clients",
    "locations",
    "recent_signals",
    "partner_fit_score",
    "partner_fit_rationale",
    "suggested_convercus_angle",
    "qualification",
    "next_steps",
    "confidence",
    "sources",
    "status",
    "error",
]


RESEARCH_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "canonical_name": {"type": "string"},
        "website": {"type": "string"},
        "linkedin_url": {"type": "string"},
        "country": {"type": "string"},
        "industry": {"type": "string"},
        "employee_count_estimate": {"type": "string"},
        "short_description": {"type": "string"},
        "business_model": {"type": "string"},
        "products_services": {
            "type": "array",
            "items": {"type": "string"},
        },
        "target_customers": {
            "type": "array",
            "items": {"type": "string"},
        },
        "brands_or_clients": {
            "type": "array",
            "items": {"type": "string"},
        },
        "locations": {
            "type": "array",
            "items": {"type": "string"},
        },
        "recent_signals": {
            "type": "array",
            "items": {"type": "string"},
        },
        "partner_fit_score": {
            "type": "integer",
            "minimum": 0,
            "maximum": 100,
        },
        "partner_fit_rationale": {"type": "string"},
        "suggested_convercus_angle": {"type": "string"},
        "qualification": {
            "type": "string",
            "enum": ["High", "Medium", "Low", "Disqualify"],
        },
        "next_steps": {
            "type": "array",
            "items": {"type": "string"},
        },
        "confidence": {
            "type": "string",
            "enum": ["high", "medium", "low"],
        },
        "sources": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "url": {"type": "string"},
                    "evidence": {"type": "string"},
                },
                "required": ["title", "url", "evidence"],
                "additionalProperties": False,
            },
        },
    },
    "required": [
        "canonical_name",
        "website",
        "linkedin_url",
        "country",
        "industry",
        "employee_count_estimate",
        "short_description",
        "business_model",
        "products_services",
        "target_customers",
        "brands_or_clients",
        "locations",
        "recent_signals",
        "partner_fit_score",
        "partner_fit_rationale",
        "suggested_convercus_angle",
        "qualification",
        "next_steps",
        "confidence",
        "sources",
    ],
    "additionalProperties": False,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Research companies from an Apollo CSV with AI and internet search."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--start", type=int, default=0, help="Zero-based input row offset.")
    parser.add_argument("--limit", type=int, help="Maximum number of companies to process.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Seconds between requests.")
    parser.add_argument("--force", action="store_true", help="Research companies already in output.")
    parser.add_argument("--dry-run", action="store_true", help="Show companies to process without API calls.")
    parser.add_argument(
        "--no-web",
        action="store_true",
        help="Disable the hosted web_search tool. Useful only for debugging prompts.",
    )
    return parser.parse_args()


def read_companies(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames or "Company Name" not in reader.fieldnames:
            raise SystemExit(f"Input CSV must contain a 'Company Name' column: {path}")

        rows = []
        seen = set()
        for index, row in enumerate(reader, start=1):
            company = (row.get("Company Name") or "").strip()
            if not company:
                continue
            key = company.casefold()
            if key in seen:
                continue
            seen.add(key)
            rows.append({"__row_number": str(index), **row})
        return rows


def already_done(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return {
            (row.get("company_name") or "").strip().casefold()
            for row in reader
            if (row.get("status") or "").lower() == "ok"
        }


def compact_context(row: dict[str, str]) -> dict[str, str]:
    fields = [
        "Company Name",
        "Website",
        "Company Linkedin Url",
        "Company Country",
        "Company City",
        "Company State",
        "# Employees",
        "Industry",
        "Keywords",
        "Technologies",
        "Annual Revenue",
        "Short Description",
        "Lists",
    ]
    return {field: (row.get(field) or "").strip() for field in fields if row.get(field)}


def build_prompt(row: dict[str, str]) -> str:
    company = row["Company Name"].strip()
    context = json.dumps(compact_context(row), ensure_ascii=False, indent=2)
    return f"""
Investiga esta compañía para un equipo de partnerships de Convercus.

Compañía objetivo: {company}
Datos iniciales de Apollo:
{context}

Instrucciones:
- Usa búsqueda web activa para confirmar identidad, web oficial, actividad y señales recientes.
- Prioriza fuentes oficiales: web corporativa, LinkedIn, páginas de producto, notas de prensa, registros o medios reconocidos.
- No inventes datos. Si no encuentras algo, deja el campo vacío o usa una formulación prudente.
- Evalúa encaje como partner para Convercus: agencias, distribuidores, consultoras, empresas con clientes retail/consumer/loyalty/CRM/ecommerce, o capacidad de activar proyectos conjuntos.
- Responde en español, salvo nombres propios.
- Devuelve solo el objeto JSON que cumple el esquema.
""".strip()


def response_to_dict(response: Any) -> dict[str, Any]:
    if hasattr(response, "model_dump"):
        return response.model_dump()
    if hasattr(response, "to_dict"):
        return response.to_dict()
    return json.loads(response.model_dump_json())


def call_openai(client: Any, row: dict[str, str], model: str, use_web: bool) -> tuple[dict[str, Any], dict[str, Any]]:
    tools = []
    tool_choice: Any = "auto"
    if use_web:
        tools = [{"type": "web_search", "search_context_size": "low"}]
        tool_choice = "required"

    response = client.responses.create(
        model=model,
        instructions=(
            "Eres un analista senior de partnerships B2B. "
            "Tu trabajo es investigar empresas con fuentes web y devolver datos estructurados, "
            "útiles para priorización comercial. Sé preciso, escéptico y conciso."
        ),
        input=build_prompt(row),
        tools=tools,
        tool_choice=tool_choice,
        reasoning={"effort": "low"},
        text={
            "format": {
                "type": "json_schema",
                "name": "company_research",
                "strict": True,
                "schema": RESEARCH_SCHEMA,
            }
        },
    )

    raw = response_to_dict(response)
    parsed = json.loads(response.output_text)
    return parsed, raw


def flatten(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        if value and isinstance(value[0], dict):
            return " | ".join(
                f"{item.get('title', '')} - {item.get('url', '')} - {item.get('evidence', '')}".strip(" -")
                for item in value
            )
        return " | ".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


def ensure_output(path: Path) -> None:
    if path.exists():
        return
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()


def append_csv(path: Path, row: dict[str, Any]) -> None:
    ensure_output(path)
    with path.open("a", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_FIELDS, extrasaction="ignore")
        writer.writerow({field: flatten(row.get(field, "")) for field in OUTPUT_FIELDS})


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> int:
    args = parse_args()
    companies = read_companies(args.input)
    done = already_done(args.output) if not args.force else set()

    selected = [
        row
        for row in companies[args.start :]
        if (row["Company Name"].strip().casefold() not in done)
    ]
    if args.limit is not None:
        selected = selected[: args.limit]

    print(f"Input: {args.input}")
    print(f"Total unique companies: {len(companies)}")
    print(f"Already researched: {len(done)}")
    print(f"Selected for this run: {len(selected)}")

    if args.dry_run:
        for row in selected[:25]:
            print(f"- row {row['__row_number']}: {row['Company Name']}")
        if len(selected) > 25:
            print(f"... {len(selected) - 25} more")
        return 0

    try:
        from openai import OpenAI
    except ImportError:
        print("Missing dependency: install the OpenAI SDK with `python3 -m pip install openai`.", file=sys.stderr)
        return 2

    if not os.getenv("OPENAI_API_KEY"):
        print("Missing OPENAI_API_KEY in the environment.", file=sys.stderr)
        return 2

    client = OpenAI()
    ensure_output(args.output)

    for position, row in enumerate(selected, start=1):
        company = row["Company Name"].strip()
        researched_at = datetime.now(timezone.utc).isoformat()
        print(f"[{position}/{len(selected)}] Researching {company}")

        try:
            result, raw = call_openai(client, row, args.model, use_web=not args.no_web)
            csv_row = {
                "researched_at": researched_at,
                "source_row": row["__row_number"],
                "company_name": company,
                **result,
                "status": "ok",
                "error": "",
            }
            append_csv(args.output, csv_row)
            append_jsonl(
                args.jsonl,
                {
                    "researched_at": researched_at,
                    "source_row": row["__row_number"],
                    "company_name": company,
                    "input_context": compact_context(row),
                    "result": result,
                    "response": raw,
                },
            )
        except Exception as exc:  # Keep long runs resumable after individual failures.
            append_csv(
                args.output,
                {
                    "researched_at": researched_at,
                    "source_row": row["__row_number"],
                    "company_name": company,
                    "status": "error",
                    "error": repr(exc),
                },
            )
            print(f"  ERROR: {exc}", file=sys.stderr)

        if args.sleep > 0 and position < len(selected):
            time.sleep(args.sleep)

    print(f"CSV written to: {args.output}")
    print(f"JSONL written to: {args.jsonl}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
