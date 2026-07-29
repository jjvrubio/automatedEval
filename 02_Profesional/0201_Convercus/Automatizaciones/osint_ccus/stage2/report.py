"""Deterministic, evidence-linked Markdown synthesis for Stage 2."""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

from stage1.presentation import (
    effective_criterion_decision,
    original_decision_note,
)

THEMES = (
    ("technology_json", "Tecnología y experiencia de cliente", 0.40),
    ("corporate_json", "Cambios corporativos y liderazgo", 0.25),
    ("expansion_json", "Expansión y distribución", 0.35),
)
STRENGTH_ORDER = {"high": 0, "medium": 1, "low": 2}


def build_potentiality_report(
    record: dict[str, Any],
    output_dir: Path,
    provided_meddicc_snapshot: Path | None = None,
) -> Path:
    company = str(record["company_name"])
    reports_dir = Path(output_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "Informe de potencialidad.md"

    score = _aggregate_score(record)
    recommendation = _recommendation(score)
    lines = [
        "---",
        f'company: "{_yaml(company)}"',
        f"record_id: {record['record_id']}",
        f"generated_utc: {datetime.now(timezone.utc).isoformat()}",
        "stage: 2",
        f"potentiality_score: {score:.1f}",
        f"recommendation: {recommendation}",
        "---",
        "",
        f"# Informe de potencialidad: {company}",
        "",
        "## Resumen ejecutivo",
        "",
        f"**Recomendación:** `{recommendation}`  ",
        f"**Puntuación heurística:** **{score:.1f}/10**",
        "",
    ]
    for key, title, _ in THEMES:
        result = record.get(key) or {}
        if result.get("executive_summary"):
            lines.append(f"- **{title}:** {result['executive_summary']}")
    technology = record.get("technology_json") or {}
    if technology.get("sector_profile"):
        lines.extend(
            [
                "",
                f"**Perfil sectorial:** `{technology['sector_profile']}` · "
                f"`{technology.get('sector_eligibility', 'review')}`",
                "",
                str(technology.get("sector_rationale") or ""),
            ]
        )

    lines.extend(_eligibility_section(record.get("eligibility_json") or {}))
    lines.extend(_scorecard(record, score))

    for key, title, _ in THEMES:
        lines.extend(_theme_section(title, record.get(key) or {}))

    lines.extend(_signals_section(record))
    lines.extend(_stakeholders_section(record))
    if record.get("provided_meddicc_markdown"):
        lines.extend(
            _provided_meddicc_section(record, provided_meddicc_snapshot)
        )
    lines.extend(_discovery_section(record))
    lines.extend(_risks_and_gaps(record))
    lines.extend(_sources_section(record))
    lines.extend(
        [
            "## Metodología y límites",
            "",
            "- La investigación utiliza únicamente información pública recuperable.",
            "- `confirmed` significa que una fuente recuperada respalda directamente "
            "el hallazgo; `indicated` identifica una señal que requiere validación.",
            "- La puntuación es una heurística de priorización comercial, no una "
            "previsión de cierre ni una valoración financiera.",
            "- No se calculan ACV, ROI o payback sin datos internos verificables.",
            "- La ausencia de evidencia pública no demuestra que una tecnología o "
            "capacidad no exista.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def _eligibility_section(eligibility: dict[str, Any]) -> list[str]:
    employees = eligibility.get("employees") or {}
    locations = eligibility.get("locations") or {}
    revenue = eligibility.get("revenue") or {}
    final = eligibility.get("final_decision") or {}
    lines = [
        "",
        "## Base de elegibilidad validada",
        "",
        "| Criterio | Valor validado | Decisión |",
        "|---|---:|---|",
        f"| Empleados | {_value(employees)} | "
        f"{_cell(effective_criterion_decision(eligibility, 'employees'))} |",
        f"| Puntos de venta/servicio | {_value(locations)} | "
        f"{_cell(effective_criterion_decision(eligibility, 'locations'))} |",
        f"| Facturación anual EUR | {_value(revenue)} | "
        f"{_cell(final.get('revenue_decision', ''))} |",
        f"| **Elegibilidad final** |  | "
        f"**{_cell(final.get('eligibility_decision', ''))}** |",
        "",
    ]
    note = original_decision_note(eligibility)
    if note:
        lines.extend(
            [
                f"_{note}_",
                "",
            ]
        )
    return lines


def _scorecard(record: dict[str, Any], total: float) -> list[str]:
    lines = [
        "## Scorecard de potencialidad",
        "",
        "| Dimensión | Peso | Puntuación | Calidad de evidencia |",
        "|---|---:|---:|---|",
    ]
    for key, title, weight in THEMES:
        result = record.get(key) or {}
        lines.append(
            f"| {_cell(title)} | {weight:.0%} | "
            f"{int(result.get('potentiality_score') or 0)}/10 | "
            f"{_cell(result.get('evidence_quality', ''))} |"
        )
    lines.extend(
        [
            f"| **Total ponderado** | **100%** | **{total:.1f}/10** | |",
            "",
            "La puntuación ordena prioridades; las razones y evidencias de cada "
            "dimensión prevalecen sobre el número agregado.",
            "",
        ]
    )
    return lines


def _theme_section(title: str, result: dict[str, Any]) -> list[str]:
    lines = [f"## {title}", ""]
    if result.get("current_state"):
        lines.extend([str(result["current_state"]), ""])
    lines.extend(
        [
            f"**Puntuación:** {int(result.get('potentiality_score') or 0)}/10  ",
            f"**Razonamiento:** {result.get('score_rationale') or 'No disponible.'}",
            "",
            "### Hallazgos",
            "",
        ]
    )
    findings = result.get("findings") or []
    if not findings:
        lines.extend(["- No se recuperaron hallazgos suficientes.", ""])
    for finding in findings:
        status = finding.get("status", "unknown")
        date = f" — {finding['date']}" if finding.get("date") else ""
        lines.append(
            f"#### {finding.get('title') or finding.get('category', 'Hallazgo')}"
        )
        lines.extend(
            [
                "",
                f"**Categoría:** `{finding.get('category', '')}` · "
                f"**Estado:** `{status}`{date}",
                "",
                str(finding.get("finding") or ""),
                "",
                f"**Relevancia comercial:** "
                f"{finding.get('business_relevance') or 'No determinada.'}",
                "",
            ]
        )
        evidence = _dedupe_sources(finding.get("evidence") or [])
        if evidence:
            lines.append("**Evidencia:**")
            lines.append("")
            lines.extend(f"- {_source_link(source)}" for source in evidence)
            lines.append("")
    return lines


def _signals_section(record: dict[str, Any]) -> list[str]:
    signals: list[tuple[str, dict[str, Any]]] = []
    for key, title, _ in THEMES:
        for signal in (record.get(key) or {}).get("opportunity_signals", []):
            signals.append((title, signal))
    signals.sort(key=lambda item: STRENGTH_ORDER.get(item[1].get("strength"), 9))
    lines = ["## Señales de oportunidad priorizadas", ""]
    if not signals:
        return lines + ["- No se identificaron señales suficientemente respaldadas.", ""]
    for theme, signal in signals:
        lines.extend(
            [
                f"### [{str(signal.get('strength', 'unknown')).upper()}] "
                f"{signal.get('title', 'Señal')}",
                "",
                f"**Dimensión:** {theme}  ",
                str(signal.get("rationale") or ""),
                "",
            ]
        )
        urls = signal.get("evidence_urls") or []
        if urls:
            lines.append("Fuentes: " + " · ".join(f"[enlace]({url})" for url in urls))
            lines.append("")
    return lines


def _stakeholders_section(record: dict[str, Any]) -> list[str]:
    by_name: dict[str, dict[str, Any]] = {}
    for key, _, _ in THEMES:
        for person in (record.get(key) or {}).get("stakeholders", []):
            identity = _normalized_name(person.get("name", ""))
            existing = by_name.get(identity)
            if existing is None:
                by_name[identity] = dict(person)
                continue
            preferred, secondary = (
                (person, existing)
                if _stakeholder_rank(person) > _stakeholder_rank(existing)
                else (existing, person)
            )
            merged = dict(preferred)
            if not merged.get("linkedin_url") and secondary.get("linkedin_url"):
                merged["linkedin_url"] = secondary["linkedin_url"]
            merged["evidence"] = _dedupe_sources(
                list(preferred.get("evidence") or [])
                + list(secondary.get("evidence") or [])
            )
            by_name[identity] = merged
    stakeholders = list(by_name.values())
    lines = [
        "## Stakeholders públicos identificados",
        "",
        "| Nombre | Cargo | Relevancia | Perfil |",
        "|---|---|---|---|",
    ]
    if not stakeholders:
        return lines + ["| No identificado | | | |", ""]
    for person in stakeholders:
        linkedin = person.get("linkedin_url") or ""
        profile = f"[LinkedIn]({linkedin})" if linkedin else ""
        lines.append(
            f"| {_cell(person.get('name', ''))} | {_cell(person.get('role', ''))} | "
            f"{_cell(person.get('relevance', ''))} | {profile} |"
        )
    lines.append("")
    return lines


def _discovery_section(record: dict[str, Any]) -> list[str]:
    questions: list[str] = []
    for key, _, _ in THEMES:
        for question in (record.get(key) or {}).get(
            "recommended_discovery_questions", []
        ):
            if question and question not in questions:
                questions.append(str(question))
    lines = ["## Preguntas recomendadas para discovery", ""]
    lines.extend(f"{index}. {question}" for index, question in enumerate(questions, 1))
    if not questions:
        lines.append("1. No se generaron preguntas por falta de evidencia.")
    lines.append("")
    return lines


def _provided_meddicc_section(
    record: dict[str, Any],
    snapshot_override: Path | None = None,
) -> list[str]:
    source_path = Path(str(record.get("provided_meddicc_path") or ""))
    snapshot_path = Path(
        str(record.get("provided_meddicc_snapshot_path") or "")
    )
    effective_snapshot = snapshot_override or snapshot_path
    relative_snapshot = (
        Path("Fuentes aportadas") / effective_snapshot.name
    ).as_posix()
    metadata = _frontmatter_metadata(
        str(record.get("provided_meddicc_markdown") or "")
    )
    lines = [
        "## MEDDPICC aportado",
        "",
        "Este documento fue generado con el modelo canónico del usuario y es la "
        "única fuente MEDDICC/MEDDPICC utilizada por `osint_ccus`.",
        "",
        f"- **Documento original:** `{source_path.name}`",
        f"- **Instantánea utilizada:** [abrir](<{relative_snapshot}>)",
        f"- **SHA-256:** `{record.get('provided_meddicc_sha256', '')}`",
    ]
    for key, label in (
        ("meddpicc_stage", "Etapa declarada"),
        ("last_reviewed", "Última revisión"),
        ("author", "Autor"),
        ("version", "Versión"),
        ("status", "Estado"),
    ):
        if metadata.get(key):
            lines.append(f"- **{label}:** {metadata[key]}")
    lines.extend(
        [
            "",
            "La instantánea conserva íntegramente MEDDPICC, Paper Process, "
            "interacciones internas, hipótesis, métricas y notas técnicas. "
            "No se reproduce dentro de este informe para evitar duplicación y "
            "pérdida de su estructura original.",
            "",
        ]
    )
    return lines


def _risks_and_gaps(record: dict[str, Any]) -> list[str]:
    risks: list[str] = []
    gaps: list[str] = []
    for key, title, _ in THEMES:
        risks.extend(
            f"**{title}:** {risk}"
            for risk in (record.get(key) or {}).get("risks", [])
        )
        gaps.extend(
            f"**{title}:** {gap}"
            for gap in (record.get(key) or {}).get("missing_information", [])
        )
    lines = ["## Riesgos, contradicciones y lagunas", "", "### Riesgos", ""]
    lines.extend(f"- {risk}" for risk in risks)
    if not risks:
        lines.append("- No se declararon riesgos específicos.")
    lines.extend(["", "### Información pendiente", ""])
    lines.extend(f"- {gap}" for gap in gaps)
    if not gaps:
        lines.append("- No se declararon lagunas materiales.")
    lines.append("")
    return lines


def _sources_section(record: dict[str, Any]) -> list[str]:
    sources: dict[str, dict[str, Any]] = {}
    for result in _theme_results(record):
        for finding in result.get("findings", []):
            for source in finding.get("evidence", []):
                if source.get("url"):
                    sources.setdefault(str(source["url"]), source)
        for stakeholder in result.get("stakeholders", []):
            for source in stakeholder.get("evidence", []):
                if source.get("url"):
                    sources.setdefault(str(source["url"]), source)
    lines = ["## Fuentes consultadas", ""]
    lines.extend(
        f"{index}. {_source_link(source)}"
        for index, source in enumerate(sources.values(), 1)
    )
    if not sources:
        lines.append("1. No se recuperaron fuentes.")
    lines.append("")
    return lines


def _theme_results(record: dict[str, Any]) -> Iterable[dict[str, Any]]:
    for key, _, _ in THEMES:
        yield record.get(key) or {}


def _aggregate_score(record: dict[str, Any]) -> float:
    return round(
        sum(
            float((record.get(key) or {}).get("potentiality_score") or 0) * weight
            for key, _, weight in THEMES
        ),
        1,
    )


def _recommendation(score: float) -> str:
    if score >= 7:
        return "PRIORIDAD_ALTA"
    if score >= 4.5:
        return "PRIORIDAD_MEDIA"
    return "MONITORIZAR"


def _value(result: dict[str, Any]) -> str:
    value_type = result.get("value_type")
    if value_type == "minimum":
        return f"≥{result.get('lower_bound', '')}"
    if value_type == "range":
        return f"{result.get('lower_bound', '')}–{result.get('upper_bound', '')}"
    return str(result.get("value") if result.get("value") is not None else "")


def _source_link(source: dict[str, Any]) -> str:
    title = str(source.get("title") or source.get("publisher") or "Fuente")
    url = str(source.get("url") or "")
    publisher = str(source.get("publisher") or "")
    date = str(source.get("published_date") or "")
    suffix = " · ".join(value for value in (publisher, date) if value)
    link = f"[{title}]({url})" if url else title
    return f"{link} — {suffix}" if suffix else link


def _dedupe_sources(sources: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    for source in sources:
        url = str(source.get("url") or "")
        key = url or repr(sorted(source.items()))
        unique.setdefault(key, source)
    return list(unique.values())


def _normalized_name(value: Any) -> str:
    ascii_name = unicodedata.normalize("NFKD", str(value).casefold()).encode(
        "ascii", "ignore"
    ).decode("ascii")
    tokens = re.findall(r"[a-z0-9]+", ascii_name)
    collapsed: list[str] = []
    for token in tokens:
        if not collapsed or collapsed[-1] != token:
            collapsed.append(token)
    return "".join(collapsed)


def _stakeholder_rank(person: dict[str, Any]) -> int:
    role = str(person.get("role") or "").casefold()
    evidence = person.get("evidence") or []
    source_score = max(
        (
            {
                "official": 4,
                "registry": 4,
                "reputable_media": 3,
                "linkedin": 2,
            }.get(str(source.get("source_type")), 1)
            for source in evidence
        ),
        default=0,
    )
    role_score = 2 if any(
        term in role
        for term in ("ceo", "consejero delegado", "directora general", "director general")
    ) else 0
    return source_score + role_score + bool(person.get("linkedin_url"))


def _frontmatter_metadata(markdown: str) -> dict[str, str]:
    if not markdown.startswith("---\n"):
        return {}
    end = markdown.find("\n---", 4)
    if end < 0:
        return {}
    metadata: dict[str, str] = {}
    for line in markdown[4:end].splitlines():
        if ":" not in line or line[:1].isspace():
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip("\"'")
    return metadata


def _cell(value: Any) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ")


def _slug(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")
    return slug or "company"


def _yaml(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')
