#!/usr/bin/env python3
"""
Classify whether companies sell through physical stores or physical points of sale.

The script reads Company Name from the first column of the Apollo CSV, researches
each company with OpenAI web search, and writes a CSV plus a summary count.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_INPUT = Path(__file__).with_name("apollo-accounts-export.csv")
DEFAULT_OUTPUT = Path(__file__).with_name("physical-pos-research-results.csv")
DEFAULT_JSONL = Path(__file__).with_name("physical-pos-research-results.jsonl")
DEFAULT_SUMMARY = Path(__file__).with_name("physical-pos-research-summary.json")

OUTPUT_FIELDS = [
    "researched_at",
    "source_row",
    "company_name",
    "canonical_name",
    "website",
    "classification",
    "sells_through_physical_pos",
    "physical_pos_type",
    "evidence_summary",
    "store_count_estimate",
    "countries_or_regions",
    "confidence",
    "sources",
    "status",
    "error",
]

CLASSIFICATION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "canonical_name": {"type": "string"},
        "website": {"type": "string"},
        "classification": {
            "type": "string",
            "enum": [
                "yes_owned_physical_pos",
                "yes_third_party_physical_pos",
                "yes_mixed_physical_pos",
                "no_ecommerce_or_b2b_only",
                "unclear",
            ],
        },
        "sells_through_physical_pos": {"type": "boolean"},
        "physical_pos_type": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "own_stores",
                    "franchise_stores",
                    "pharmacies",
                    "beauty_salon_or_hairdresser",
                    "retail_chains",
                    "department_stores",
                    "supermarkets",
                    "clinics_or_spas",
                    "showrooms",
                    "distributors_to_physical_retail",
                    "other_physical_pos",
                    "none_found",
                ],
            },
        },
        "evidence_summary": {"type": "string"},
        "store_count_estimate": {"type": "string"},
        "countries_or_regions": {
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
        "classification",
        "sells_through_physical_pos",
        "physical_pos_type",
        "evidence_summary",
        "store_count_estimate",
        "countries_or_regions",
        "confidence",
        "sources",
    ],
    "additionalProperties": False,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Count companies that sell through physical stores or physical points of sale."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--jsonl", type=Path, default=DEFAULT_JSONL)
    parser.add_argument("--summary", type=Path, default=DEFAULT_SUMMARY)
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--start", type=int, default=0, help="Zero-based input row offset.")
    parser.add_argument("--limit", type=int, help="Maximum number of companies to process.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Seconds between requests.")
    parser.add_argument("--force", action="store_true", help="Research companies already completed.")
    parser.add_argument("--dry-run", action="store_true", help="Show companies to process without API calls.")
    parser.add_argument("--no-web", action="store_true", help="Disable web_search for prompt debugging.")
    parser.add_argument(
        "--transport",
        choices=["direct", "sdk"],
        default="direct",
        help="Use direct HTTPS calls or the OpenAI Python SDK.",
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
        "Keywords",
        "Technologies",
        "Short Description",
        "Lists",
        "Store Count Check 5824 0513101740",
    ]
    return {field: (row.get(field) or "").strip() for field in fields if row.get(field)}


def build_prompt(row: dict[str, str]) -> str:
    company = row["Company Name"].strip()
    context = json.dumps(compact_context(row), ensure_ascii=False, indent=2)
    return f"""
Necesito clasificar si esta compañía vende a través de tiendas físicas o puntos de venta físicos.

Compañía: {company}
Datos disponibles del CSV:
{context}

Definición práctica:
- Marca como `sells_through_physical_pos=true` si hay evidencia de que la empresa vende productos o servicios en tiendas, salones, farmacias, clínicas, spas, showrooms, cadenas retail, supermercados, franquicias, distribuidores con presencia física, o cualquier punto de venta físico.
- Incluye tanto tiendas propias como venta en terceros.
- Marca `false` si la evidencia apunta a ecommerce puro, fabricante B2B sin canal físico verificable, software/servicios sin punto de venta físico, o no hay venta a través de espacios físicos.
- Usa `unclear` cuando no puedas resolverlo con evidencia suficiente.

Instrucciones de investigación:
- Usa búsqueda web activa.
- Prioriza web oficial, localizador de tiendas, secciones "dónde comprar", LinkedIn, notas de prensa y distribuidores reconocidos.
- No infieras solo por sector. Por ejemplo, "cosmética" no basta; busca evidencia de tienda, salón, farmacia, distribuidor físico o punto de venta.
- Si encuentras número de tiendas o ubicaciones, inclúyelo en `store_count_estimate`; si no, déjalo vacío.
- Responde en español salvo nombres propios.
- Devuelve solo el JSON que cumple el esquema.
""".strip()


def response_to_dict(response: Any) -> dict[str, Any]:
    if hasattr(response, "model_dump"):
        return response.model_dump()
    if hasattr(response, "to_dict"):
        return response.to_dict()
    return json.loads(response.model_dump_json())


def response_payload(row: dict[str, str], model: str, use_web: bool) -> dict[str, Any]:
    tools = []
    tool_choice: Any = "auto"
    if use_web:
        tools = [{"type": "web_search", "search_context_size": "low"}]
        tool_choice = "required"

    return {
        "model": model,
        "instructions": (
            "Eres un analista de canales retail. Clasificas empresas según evidencia verificable "
            "de venta en tiendas físicas o puntos de venta físicos. Eres conservador: si no hay "
            "evidencia clara, usas `unclear` o `false` según corresponda."
        ),
        "input": build_prompt(row),
        "tools": tools,
        "tool_choice": tool_choice,
        "reasoning": {"effort": "low"},
        "text": {
            "format": {
                "type": "json_schema",
                "name": "physical_pos_classification",
                "strict": True,
                "schema": CLASSIFICATION_SCHEMA,
            }
        },
    }


def extract_output_text(raw: dict[str, Any]) -> str:
    if raw.get("output_text"):
        return str(raw["output_text"])

    for item in raw.get("output", []):
        if item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if content.get("type") in {"output_text", "text"} and content.get("text"):
                return str(content["text"])

    raise RuntimeError("Could not find output text in OpenAI response")


def call_openai_sdk(client: Any, row: dict[str, str], model: str, use_web: bool) -> tuple[dict[str, Any], dict[str, Any]]:
    response = client.responses.create(**response_payload(row, model, use_web))
    raw = response_to_dict(response)
    parsed = json.loads(extract_output_text(raw))
    return parsed, raw


def call_openai_direct(row: dict[str, str], model: str, use_web: bool) -> tuple[dict[str, Any], dict[str, Any]]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY in the environment")

    body = json.dumps(response_payload(row, model, use_web)).encode("utf-8")
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=240) as response:
            raw = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI HTTP {exc.code}: {detail}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"OpenAI connection error: {exc}") from exc

    parsed = json.loads(extract_output_text(raw))
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


def write_summary(results_path: Path, summary_path: Path) -> dict[str, Any]:
    if not results_path.exists():
        summary = {"total_researched": 0}
        summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
        return summary

    with results_path.open(newline="", encoding="utf-8") as fh:
        rows = [row for row in csv.DictReader(fh) if (row.get("status") or "").lower() == "ok"]

    yes_rows = [row for row in rows if (row.get("sells_through_physical_pos") or "").lower() == "true"]
    counter = Counter(row.get("classification") or "unknown" for row in rows)
    confidence = Counter(row.get("confidence") or "unknown" for row in rows)
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_researched": len(rows),
        "sells_through_physical_pos_count": len(yes_rows),
        "sells_through_physical_pos_share": round(len(yes_rows) / len(rows), 4) if rows else 0,
        "classification_counts": dict(counter),
        "confidence_counts": dict(confidence),
        "output_csv": str(results_path),
    }
    summary_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary


def main() -> int:
    args = parse_args()
    companies = read_companies(args.input)
    done = already_done(args.output) if not args.force else set()
    selected = [
        row
        for row in companies[args.start :]
        if row["Company Name"].strip().casefold() not in done
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

    if not os.getenv("OPENAI_API_KEY"):
        print("Missing OPENAI_API_KEY in the environment.", file=sys.stderr)
        return 2

    client = None
    if args.transport == "sdk":
        try:
            from openai import OpenAI
        except ImportError:
            print("Missing dependency: install the OpenAI SDK with `python3 -m pip install openai`.", file=sys.stderr)
            return 2
        client = OpenAI()

    ensure_output(args.output)

    for position, row in enumerate(selected, start=1):
        company = row["Company Name"].strip()
        researched_at = datetime.now(timezone.utc).isoformat()
        print(f"[{position}/{len(selected)}] Classifying {company}")

        try:
            if args.transport == "sdk":
                result, raw = call_openai_sdk(client, row, args.model, use_web=not args.no_web)
            else:
                result, raw = call_openai_direct(row, args.model, use_web=not args.no_web)
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
        except Exception as exc:
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

    summary = write_summary(args.output, args.summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
