#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera preguntas críticas para la revisión de un TFE."""

import os
import re
import sys
import json
import textwrap
import traceback
from typing import List, Dict, Any, Optional

import AppKit
from PyPDF2 import PdfReader
from docx import Document as DocxDocument
from openai import OpenAI, BadRequestError

SAMPLE_STYLE = textwrap.dedent(
    """
    Las preguntas deben evidenciar dónde se rompe la continuidad epistemológica del TFE y qué prueba concreta falta para cerrarla.

    ### Ejemplo de formato
    - Eje: enfoque metodológico
    - Ruptura del flujo (pp. 75-78): El objetivo afirma medir el impacto causal, pero el modelo econométrico sólo describe correlaciones y omite los supuestos de identificación, lo que contradice la pretensión causal.
    - Qué debe demostrar el estudiante: Explicar el mecanismo causal propuesto, detallar las restricciones de exclusión y aportar resultados de pruebas de validez de instrumentos.
    → **¿Puedes detallar los supuestos de identificación que sustentan la inferencia causal y mostrar los contrastes estadísticos que verifican la validez de los instrumentos especificados?**
    """
)

FORBIDDEN_PHRASES = {
    "gestión por procesos",
    "gestion por procesos",
    "automatización",
    "automatizacion",
    "automatización de flujos",
    "automatizacion de flujos",
    "eficiencia operativa",
    "eficiencia",
    "transformación digital",
    "transformacion digital",
    "mejora continua",
    "optimización",
    "optimizacion",
}

MANDATORY_AXES = {
    "objeto empírico",
    "contexto institucional y geográfico",
    "enfoque metodológico",
    "impacto operativo o de negocio",
}


def select_tfe_file() -> Optional[str]:
    if AppKit is None:
        raise RuntimeError(
            "No se puede abrir el selector de archivos porque 'AppKit' no está disponible. "
            "Instala PyObjC con: pip install pyobjc-framework-Cocoa"
        )
    panel = AppKit.NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["pdf", "docx"])
    response = panel.runModal()
    if response == AppKit.NSModalResponseOK:
        url = panel.URL()
        if url is not None:
            return str(url.path())
    return None


def extract_text_from_pdf(file_path: str) -> str:
    if PdfReader is None:
        raise RuntimeError("PyPDF2 no está instalado. Instala con: pip install PyPDF2")
    text_chunks: List[str] = []
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            try:
                t = page.extract_text() or ""
            except Exception:
                t = ""
            text_chunks.append(t)
    return "\n".join(text_chunks)


def extract_text_from_docx(file_path: str) -> str:
    if DocxDocument is None:
        raise RuntimeError("python-docx no está instalado. Instala con: pip install python-docx")
    doc = DocxDocument(file_path)
    return "\n".join(p.text for p in doc.paragraphs if p.text is not None)


def extract_full_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    if ext == ".docx":
        return extract_text_from_docx(file_path)
    raise ValueError("Formato de archivo no soportado. Usa PDF o DOCX.")


def build_representative_excerpt(text: str, segment_chars: int) -> str:
    clean_text = re.sub(r"\s+", " ", text).strip()
    if not clean_text:
        return ""
    segment_chars = max(segment_chars, 1)
    max_chars = segment_chars * 3
    if len(clean_text) <= max_chars:
        return clean_text
    start = clean_text[:segment_chars]
    mid_start = max((len(clean_text) // 2) - (segment_chars // 2), 0)
    middle = clean_text[mid_start : mid_start + segment_chars]
    end = clean_text[-segment_chars:]
    return "\n--- Extracto intermedio ---\n".join([start, middle, end])


def prepare_document_payload(text: str, limit_chars: int) -> tuple[str, bool]:
    limit_chars = max(limit_chars, 1)
    clean_text = re.sub(r"\s+", " ", text).strip()
    if not clean_text:
        return "", False
    if len(clean_text) <= limit_chars:
        return clean_text, False
    segment = max(limit_chars // 3, 1)
    excerpt = build_representative_excerpt(clean_text, segment)
    return excerpt, True


def get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        raise RuntimeError("No hay clave para OpenAI…")
    return OpenAI(api_key=api_key)


def _collect_response_text(response: Any) -> str:
    text = getattr(response, "output_text", None)
    if isinstance(text, str) and text.strip():
        return text.strip()
    output = getattr(response, "output", None)
    chunks: List[str] = []
    if output:
        for item in output:
            item_type = getattr(item, "type", "")
            if item_type == "message":
                for content in getattr(item, "content", []) or []:
                    if getattr(content, "type", "") == "output_text":
                        chunks.append(getattr(content, "text", ""))
            elif item_type == "output_text":
                chunks.append(getattr(item, "text", ""))
    if chunks:
        return "\n".join(chunks).strip()
    fallback = getattr(response, "text", None)
    return fallback.strip() if isinstance(fallback, str) else ""


def ask_openai_for_questions(
    file_path: str,
    full_text: str,
    feedback: Optional[str] = None,
) -> Dict[str, Any]:
    client = get_openai_client()

    system_prompt = (
        "Actúas como miembro de un tribunal académico experto en evaluación de Trabajos Fin de Estudios. "
        "Identificas brechas argumentales, incoherencias y riesgos del proyecto para formular preguntas incisivas. "
        "Tus preguntas deben facilitar un diálogo profundo durante la defensa."\
    )

    user_prompt = (
        f"Archivo analizado: {os.path.basename(file_path)}\n\n"
        "Genera exactamente cuatro preguntas críticas en español que sigan estas pautas:\n"
        "1. Cada pregunta debe centrarse en uno de los ejes: objeto empírico, contexto institucional/geográfico, enfoque metodológico y impacto operativo o de negocio.\n"
        "2. Identifica para cada eje dónde se rompe el flujo epistemológico: objetivos que no enlazan con métodos, métodos que no justifican datos, resultados que contradicen conclusiones, etc. Describe la evidencia con citas de páginas o secciones concretas.\n"
        "3. Explica qué demostración, cálculo, contraste empírico o documentación debe aportar el estudiante para restablecer la coherencia.\n"
        "4. Formula una pregunta incisiva, larga y específica que obligue al estudiante a defender el tramo lógico en cuestión (supuestos, métricas, estimaciones, evidencia empírica). La pregunta debe terminar con signo de interrogación.\n"
        "5. No utilices expresiones genéricas como 'gestión por procesos' o 'transformación digital' sin calificadores específicos; sé preciso con el contenido del TFE.\n"
        "6. Devuelve exclusivamente un JSON con la forma:\n"
        '{"items": [\n'
        '  {"axis": "objeto empírico",\n'
        '   "gap": "Brecha detectada (pp. ...): ...",\n'
        '   "clarification_needed": "Prueba o demostración requerida",\n'
        '   "question": "Pregunta incisiva en español?"},\n'
        '  ...\n'
        ' ]}\n'
        "donde 'axis' debe ser uno de los cuatro ejes descritos, 'gap' sintetiza la ruptura del flujo argumental con referencias, 'clarification_needed' detalla la evidencia técnica o cálculo que falta y 'question' termina con signo de interrogación.\n\n"
        "Referencia de estilo (no la copies literalmente):\n"
        f"{SAMPLE_STYLE}\n\n"
    )

    if feedback:
        user_prompt += ("\n\n" + feedback.strip())

    limits = [48000, 36000, 24000]
    response = None
    used_excerpt = False
    last_error: Optional[Exception] = None

    for limit in limits:
        doc_text, truncated = prepare_document_payload(full_text, limit)
        if not doc_text:
            continue
        try:
            content_blocks = [
                {"type": "input_text", "text": user_prompt},
                {
                    "type": "input_text",
                    "text": (
                        ("Extracto representativo del TFE" if truncated else "Contenido completo del TFE")
                        + ":\n"
                        + doc_text
                    ),
                },
            ]

            response = client.responses.create(
                model="gpt-4o",
                input=[
                    {
                        "role": "system",
                        "content": [{"type": "input_text", "text": system_prompt}],
                    },
                    {
                        "role": "user",
                        "content": content_blocks,
                    },
                ],
                max_output_tokens=750,
                temperature=0.3,
            )
            used_excerpt = used_excerpt or truncated
            break
        except BadRequestError as api_err:
            message = str(getattr(api_err, "message", "") or api_err)
            if "context" in message.lower() and "exceed" in message.lower():
                used_excerpt = True
                last_error = api_err
                continue
            raise

    if response is None:
        raise RuntimeError(
            "El modelo no pudo procesar el TFE debido a los límites de contexto."
        ) from last_error

    combined = _collect_response_text(response)
    if not combined:
        raise RuntimeError("La respuesta del modelo llegó vacía o en un formato inesperado.")

    try:
        json_text = extract_first_json_object(combined)
        data = json.loads(json_text)
        items = data.get("items", [])
        return {
            "items": items,
            "raw": combined,
            "used_excerpt": used_excerpt,
        }
    except Exception as exc:
        raise RuntimeError(
            "No se pudo interpretar la respuesta del modelo como JSON válido."
        ) from exc


def extract_first_json_object(text: str) -> str:
    start = text.find("{")
    if start == -1:
        raise ValueError("No se encontró objeto JSON en la respuesta.")
    depth = 0
    for idx in range(start, len(text)):
        ch = text[idx]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start : idx + 1]
    raise ValueError("No se pudo extraer un objeto JSON completo.")


def evaluate_questions(items: List[Dict[str, Any]]) -> List[str]:
    issues: List[str] = []
    if len(items) != 4:
        issues.append("Debes devolver exactamente cuatro objetos 'items'.")

    axes_received = set()
    for idx, item in enumerate(items, start=1):
        axis = str(item.get("axis", "")).strip().lower()
        gap = str(item.get("gap", "")).strip()
        clarification = str(item.get("clarification_needed", "")).strip()
        question = str(item.get("question", "")).strip()

        if not axis:
            issues.append(f"Item {idx}: falta el campo 'axis'.")
        else:
            axes_received.add(axis)

        if not gap:
            issues.append(f"Item {idx}: falta describir la brecha en 'gap'.")
        else:
            lower_gap = gap.lower()
            if not re.search(r"\b(p\.|pp\.|cap[ií]tulo|secci[oó]n)\b", lower_gap):
                issues.append(
                    f"Item {idx}: incluye referencias explícitas a páginas o secciones en 'gap' (p. ej. 'p. 120' o 'capítulo 3')."
                )
            if len(gap.split()) < 25:
                issues.append(
                    f"Item {idx}: la descripción de la brecha es demasiado breve; aporta más contexto técnico."
                )
            if gap.count(".") + gap.count(";") < 1:
                issues.append(
                    f"Item {idx}: desarrolla la brecha en al menos dos oraciones para mostrar la ruptura del flujo argumental."
                )

        if not clarification:
            issues.append(f"Item {idx}: falta 'clarification_needed' con la demostración requerida.")
        else:
            if len(clarification.split()) < 15:
                issues.append(
                    f"Item {idx}: especifica con mayor detalle la demostración o evidencia que debe aportar el estudiante."
                )
            if not re.search(r"\b(model|c[oó]mput|demostr|valid|c[aá]lcul|medici[oó]n|hip[oó]tesis|supuest)\b", clarification.lower()):
                issues.append(
                    f"Item {idx}: especifica con qué procedimiento, cálculo o validación debe sustentarse la aclaración."
                )

        if not question:
            issues.append(f"Item {idx}: falta la pregunta.")
        else:
            if not question.endswith("?"):
                issues.append(f"Item {idx}: la pregunta debe terminar con signo de interrogación.")
            if len(question.split()) < 12:
                issues.append(f"Item {idx}: la pregunta es demasiado corta; precisa la comprobación que exiges.")
            if len(question) < 60:
                issues.append(
                    f"Item {idx}: amplía la pregunta para aclarar qué aspecto del flujo argumental debe defender el estudiante."
                )

        normalized_question = question.lower()
        for forbidden in FORBIDDEN_PHRASES:
            if forbidden in normalized_question:
                issues.append(
                    f"Item {idx}: evita la expresión genérica '{forbidden}'. Añade calificadores específicos."
                )

    missing_axes = {axis.lower() for axis in MANDATORY_AXES} - axes_received
    if missing_axes:
        formatted = ", ".join(sorted(missing_axes))
        issues.append(
            "Debe haber exactamente una pregunta por cada eje obligatorio. Faltan: " + formatted
        )

    return issues


def format_feedback_for_model(issues: List[str], current_items: List[Dict[str, Any]]) -> str:
    if not issues:
        return ""
    lines = ["Correcciones necesarias detectadas por la validación automática:"]
    for issue in issues:
        lines.append(f"- {issue}")
    if current_items:
        try:
            rendered = json.dumps(current_items, ensure_ascii=False)
        except Exception:
            rendered = ""
        if rendered:
            lines.append("Propuesta anterior (para referencia, no la repitas literalmente):")
            lines.append(rendered)
    lines.append("Regenera los 'items' ajustando cada problema indicado.")
    return "\n".join(lines)


MAX_GENERATION_ATTEMPTS = 3


def generate_questions_with_feedback(
    file_path: str,
    full_text: str,
) -> Dict[str, Any]:
    feedback = None
    attempt = 0
    last_result: Optional[Dict[str, Any]] = None

    while attempt < MAX_GENERATION_ATTEMPTS:
        result = ask_openai_for_questions(
            file_path=file_path,
            full_text=full_text,
            feedback=feedback,
        )

        items = result.get("items") or []
        issues = evaluate_questions(items)
        result["validation_issues"] = issues
        result["attempts"] = attempt + 1

        if not issues:
            return result

        feedback = format_feedback_for_model(issues, items)
        last_result = result
        attempt += 1

    if last_result is not None:
        return last_result

    return {
        "items": [],
        "raw": "",
        "used_excerpt": False,
        "validation_issues": [
            "No se consiguió una propuesta válida tras varios intentos. Revisa el documento manualmente."
        ],
        "attempts": MAX_GENERATION_ATTEMPTS,
    }


def write_markdown(
    output_path: str,
    src_file: str,
    result: Dict[str, Any],
) -> None:
    items = result.get("items") or []
    lines: List[str] = []
    lines.append("# Preguntas críticas para la defensa del TFE\n")
    lines.append(f"- Archivo analizado: {os.path.basename(src_file)}\n")

    for idx, item in enumerate(items, start=1):
        axis = str(item.get("axis", "")).strip()
        gap = str(item.get("gap", "")).strip()
        clarification = str(item.get("clarification_needed", "")).strip()
        question = str(item.get("question", "")).strip()
        lines.append(f"## {idx}. {axis if axis else 'Eje sin especificar'}\n")
        if gap:
            lines.append(f"**Brecha:** {gap}\n")
        if clarification:
            lines.append(f"**Demostración requerida:** {clarification}\n")
        lines.append(f"→ **Pregunta:** {question}\n")

    issues = result.get("validation_issues") or []
    if issues:
        lines.append("## Observaciones de la validación automática\n")
        for issue in issues:
            lines.append(f"- {issue}")
        lines.append("")

    attempts = result.get("attempts")
    if attempts:
        lines.append(f"_Intentos realizados: {attempts}_\n")

    if result.get("used_excerpt"):
        lines.append(
            "_Nota: Se utilizó un extracto representativo del TFE por límites de contexto del modelo._\n"
        )

    raw = result.get("raw")
    if raw:
        lines.append("## Respuesta bruta del modelo (trazabilidad)\n")
        lines.append("```\n" + raw + "\n```\n")

    try:
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    except OSError as exc:
        raise RuntimeError(f"No se pudo escribir el informe en '{output_path}': {exc}")


def main() -> None:
    try:
        file_path = select_tfe_file()
        if not file_path:
            return

        full_text = extract_full_text(file_path)

        result = generate_questions_with_feedback(
            file_path=file_path,
            full_text=full_text,
        )

        if result.get("used_excerpt"):
            print("Aviso: se utilizó un extracto representativo del TFE por límites de contexto.")

        if result.get("validation_issues"):
            print("Aviso: la validación automática detectó incidencias a revisar:")
            for issue in result["validation_issues"]:
                print(f"  - {issue}")

        base_dir = os.path.dirname(file_path)
        stem = os.path.splitext(os.path.basename(file_path))[0]
        out_md = os.path.join(base_dir, f"{stem}.questions.md")
        write_markdown(out_md, file_path, result)
        print(f"Informe de preguntas guardado en: {out_md}")

    except Exception as exc:
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            with open(os.path.join(desktop, "tfe_questions_error.log"), "w", encoding="utf-8") as logf:
                logf.write(f"Error: {exc}\n\n")
                logf.write(traceback.format_exc())
        except Exception:
            pass
        sys.stderr.write(f"Error: {exc}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
