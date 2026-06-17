#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import json
import traceback
import AppKit
from PyPDF2 import PdfReader
from docx import Document as DocxDocument
from openai import OpenAI, BadRequestError


def select_tfe_file():
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
    text_chunks = []
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            try:
                t = page.extract_text() or ""
            except Exception:
                t = ""
            text_chunks.append(t)
    return "\n".join(text_chunks)


def extract_text_from_docx(file_path: str
                           ) -> str:
    if DocxDocument is None:
        raise RuntimeError("python-docx no está instalado. Instala con: pip install python-docx")
    doc = DocxDocument(file_path)
    return "\n".join(p.text for p in doc.paragraphs if p.text is not None)


def extract_full_text(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Formato de archivo no soportado. Usa PDF o DOCX.")


def parse_keywords_sections(text: str):
    # Busca secciones "Palabras clave:" y "Keywords:"
    # Captura la secuencia separada por comas que termina en punto.
    results = {"es": [], "en": []}
    patterns = [
        (r'(?is)\bpalabras\s*clave[s]?\s*:\s*(.+?)\.', "es"),
        (r'(?is)\bkeywords?\s*:\s*(.+?)\.', "en"),
    ]
    for pattern, lang in patterns:
        m = re.search(pattern, text)
        if m:
            segment = m.group(1)
            # Divide por comas y limpia espacios y puntuación sobrante
            kws = [
                re.sub(r'\s+', ' ', k).strip(" \t\n\r.,;:¡!¿?()-[]{}|/\\")
                for k in segment.split(",")
            ]
            kws = [k for k in kws if k]
            results[lang] = kws
    return results


FORBIDDEN_EXACT = {
    "gestión por procesos",
    "gestion por procesos",
    "gestión de procesos",
    "automatización",
    "automatizacion",
    "automatización de flujos",
    "automatizacion de flujos",
    "workflow automation",
    "eficiencia operativa",
    "eficiencia",
    "transformación digital",
    "transformacion digital",
}

ALLOWED_SINGLE_TOKENS = {
    "BPM",
    "RPA",
    "BPMN",
    "TOC",
    "KPI",
    "KPIs",
    "Lean",
}

GENERIC_SINGLE_ROOTS = {
    "gestión",
    "gestion",
    "automatización",
    "automatizacion",
    "transformación",
    "transformacion",
    "eficiencia",
    "optimización",
    "optimizacion",
    "digital",
    "proceso",
}


def build_representative_excerpt(text: str, segment_chars: int) -> str:
    """Construye un extracto representativo (inicio, medio y final) para documentos largos."""
    clean_text = re.sub(r"\s+", " ", text).strip()
    if not clean_text:
        return ""

    max_chars = max(segment_chars, 1) * 3
    if len(clean_text) <= max_chars:
        return clean_text

    seg = max(segment_chars, 1)
    start = clean_text[:seg]
    mid_start = max((len(clean_text) // 2) - (seg // 2), 0)
    middle = clean_text[mid_start:mid_start + seg]
    end = clean_text[-seg:]
    return "\n--- Extracto intermedio ---\n".join([start, middle, end])


def prepare_document_payload(text: str, limit_chars: int) -> tuple[str, bool]:
    """Devuelve el texto a enviar y si se tuvo que resumir para cumplir el límite."""
    limit_chars = max(limit_chars, 1)
    clean_text = re.sub(r"\s+", " ", text).strip()
    if not clean_text:
        return "", False

    if len(clean_text) <= limit_chars:
        return clean_text, False

    segment = max(limit_chars // 3, 1)
    excerpt = build_representative_excerpt(clean_text, segment)
    return excerpt, True


def evaluate_keywords(candidates: list[str], original_es: list, original_en: list) -> list[str]:
    """Valida la lista propuesta y devuelve observaciones si detecta problemas."""
    issues: list[str] = []
    normalized_seen: set[str] = set()
    originals_lower = {kw.strip().lower() for kw in (original_es or []) + (original_en or []) if kw.strip()}

    if len(candidates) != 6:
        issues.append("Debes entregar exactamente seis palabras clave distintas.")

    for kw in candidates:
        plain = kw.strip()
        if not plain:
            issues.append("Se detectó una entrada vacía en la lista de palabras clave.")
            continue

        lower_kw = plain.lower()
        if lower_kw in normalized_seen:
            issues.append(f"'{plain}' aparece duplicada; cada palabra clave debe ser única.")
        else:
            normalized_seen.add(lower_kw)

        if lower_kw in FORBIDDEN_EXACT:
            issues.append(
                f"'{plain}' es demasiado genérica. Añade calificadores que especifiquen objeto, contexto o método."
            )

        tokens = [tok for tok in re.split(r"[\s/,-]+", plain) if tok]
        if len(tokens) == 1:
            token_upper = tokens[0].upper()
            if token_upper not in ALLOWED_SINGLE_TOKENS:
                issues.append(
                    f"'{plain}' necesita al menos dos términos o un calificador adicional que lo haga inequívoco."
                )
        else:
            first_token = tokens[0].lower()
            if first_token in GENERIC_SINGLE_ROOTS and len(tokens) < 3:
                issues.append(
                    f"'{plain}' sigue siendo vaga. Añade detalles del proceso, institución, población o tecnología aplicada."
                )

        if lower_kw in originals_lower and lower_kw in FORBIDDEN_EXACT:
            issues.append(
                f"'{plain}' coincide con una palabra clave original poco discriminativa. Sustitúyela por una versión más precisa."
            )

    return issues


def format_feedback_for_model(issues: list[str], candidates: list[str]) -> str:
    """Convierte las observaciones en un mensaje conciso para el modelo."""
    if not issues:
        return ""
    lines = ["Se detectaron estas incidencias que debes corregir:"]
    for issue in issues:
        lines.append(f"- {issue}")
    if candidates:
        joined = "; ".join(c.strip() for c in candidates if c.strip())
        if joined:
            lines.append(f"Lista entregada anteriormente: {joined}.")
    lines.append("Genera una nueva propuesta aplicando las reglas originales.")
    return "\n".join(lines)


MAX_GENERATION_ATTEMPTS = 3


def generate_keywords_with_feedback(
    file_path: str,
    original_es: list,
    original_en: list,
    full_text: str,
):
    """Solicita palabras clave al modelo y aplica realimentación automática si son genéricas."""
    feedback = None
    attempt = 0
    last_result: dict | None = None

    while attempt < MAX_GENERATION_ATTEMPTS:
        result = ask_openai_with_file(
            file_path=file_path,
            original_es=original_es,
            original_en=original_en,
            full_text=full_text,
            feedback=feedback,
        )

        candidates = result.get("keywords") or []
        issues = evaluate_keywords(candidates, original_es, original_en)
        result["validation_issues"] = issues
        result["attempts"] = attempt + 1

        if not issues:
            return result

        feedback = format_feedback_for_model(issues, candidates)
        last_result = result
        attempt += 1

    if last_result is not None:
        return last_result

    return {
        "keywords": [],
        "explanation": "",
        "raw": "",
        "used_excerpt": False,
        "validation_issues": [
            "No se consiguió una propuesta válida tras varios intentos. Revisa el documento manualmente."
        ],
        "attempts": MAX_GENERATION_ATTEMPTS,
    }


def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY") or os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        raise RuntimeError("No hay clave para OpenAI…")
    return OpenAI(api_key=api_key)


def _collect_response_text(response) -> str:
    """Extrae contenido textual del formato de respuesta más reciente de la API."""
    chunks = []
    # Preferimos la propiedad output_text si está disponible
    text = getattr(response, "output_text", None)
    if isinstance(text, str) and text.strip():
        return text.strip()

    # Fallback a recorrer la estructura output
    output = getattr(response, "output", None)
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

    # Como última opción intentamos leer la propiedad 'text'
    fallback = getattr(response, "text", None)
    return fallback.strip() if isinstance(fallback, str) else ""


def ask_openai_with_file(
    file_path: str,
    original_es: list,
    original_en: list,
    full_text: str,
    feedback: str | None = None,
):
    """
        Usa la API Responses de OpenAI para analizar el TFE y solicitar:
            - 6 palabras clave idóneas
            - Explicación de la selección

    Devuelve un dict con:
      { "keywords": [...6...], "explanation": "..." }
    """
    client = get_openai_client()

    system_prompt = (
        "Actúas como documentalista académico especializado en indización de Trabajos Fin de Estudios. "
        "Tu objetivo es proponer seis palabras clave altamente discriminativas, alineadas con tesauros académicos y vocabularios controlados. "
        "Debes reflejar el objeto de estudio específico, el enfoque metodológico y la contribución principal. "
        "Responde exclusivamente en JSON válido."
    )

    original_es_display = original_es if original_es else ["N/D"]
    original_en_display = original_en if original_en else ["N/D"]

    user_prompt = (
        f"Archivo analizado: {os.path.basename(file_path)}\n\n"
        "Genera seis palabras clave que mejoren la indización académica del TFE siguiendo estas reglas:\n"
        "1. Objeto empírico: cada palabra debe identificar con precisión el proceso, sistema, población o fenómeno estudiado.\n"
        "2. Contexto institucional y geográfico: incorpora el organismo, sector o ubicación cuando aporte discriminación real.\n"
        "3. Enfoque metodológico: refleja marcos, métodos, modelos o tecnologías aplicadas (BPM, Lean, RPA, estudios de caso, etc.).\n"
        "4. Impacto buscado: indica la aportación operativa o de negocio (eficiencia administrativa, trazabilidad, ROI, seguridad, etc.).\n"
        "5. Exactitud: evita términos genéricos o redundantes como 'transformación digital' sin calificadores. Prioriza vocabularios normalizados y combinaciones de 1 a 4 palabras.\n"
        "6. Idioma: mantén exactamente seis palabras clave; al menos cuatro en español y hasta dos en inglés si el campo lo exige.\n"
        "7. Evaluación de las originales: conserva solo las palabras del alumno que cumplan los criterios anteriores y justifica cada retención o sustitución.\n\n"
        "Formato obligatorio de salida (JSON):\n"
        '{"keywords": ["kw1","kw2","kw3","kw4","kw5","kw6"],\n'
        ' "explanation": "- kwX: Objeto=...; Contexto=...; Método=...; Impacto=...; Sustituye=original|n/a; Evidencia=sección o pasaje de soporte.\\n..."}\n\n'
        f"Palabras clave del alumno (ES): {', '.join(original_es_display)}\n"
        f"Keywords del alumno (EN): {', '.join(original_en_display)}\n"
        "Recuerda: la explicación debe contener una viñeta por palabra clave siguiendo el formato indicado."
    )

    if feedback:
        user_prompt += (
            "\n\nCorrecciones obligatorias basadas en la validación automática:\n"
            + feedback
            + "\nRegenera la lista cumpliendo todas las reglas anteriores."
        )

    limits = [54000, 36000, 24000]
    response = None
    used_excerpt = False
    last_error: Exception | None = None

    for limit in limits:
        doc_text, truncated = prepare_document_payload(full_text, limit)
        if not doc_text:
            continue

        try:
            content_blocks = [{"type": "input_text", "text": user_prompt}]

            doc_label = "Extracto representativo del TFE" if truncated else "Contenido completo del TFE"
            content_blocks.append(
                {
                    "type": "input_text",
                    "text": f"{doc_label}:\n{doc_text}",
                }
            )

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
                max_output_tokens=650,
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
        kw = data.get("keywords", [])
        if isinstance(kw, list):
            kw = [str(x).strip() for x in kw if str(x).strip()]
        expl = data.get("explanation", "")
        return {
            "keywords": kw,
            "explanation": str(expl).strip(),
            "raw": combined,
            "used_excerpt": used_excerpt,
        }
    except Exception:
        return {
            "keywords": [],
            "explanation": "",
            "raw": combined,
            "used_excerpt": used_excerpt,
        }


def extract_first_json_object(text: str) -> str:
    """
    Extrae el primer objeto JSON bien balanceado encontrado en el texto.
    Útil cuando el modelo responde con texto adicional alrededor.
    """
    # Busca la primera llave
    start = text.find("{")
    if start == -1:
        raise ValueError("No se encontró objeto JSON en la respuesta.")
    # Recorre balanceo de llaves
    depth = 0
    for i in range(start, len(text)):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return text[start:i+1]
    raise ValueError("No se pudo extraer un objeto JSON completo.")


def write_markdown(output_path: str, src_file: str, original_es: list, original_en: list, best: dict):
    lines = []
    lines.append(f"# Evaluación de Palabras Clave del TFE\n")
    lines.append(f"- Archivo analizado: {os.path.basename(src_file)}\n")
    lines.append(f"## Palabras clave extraídas (originales)\n")
    lines.append(f"- ES: {', '.join(original_es) if original_es else 'N/D'}\n")
    lines.append(f"- EN: {', '.join(original_en) if original_en else 'N/D'}\n")
    lines.append(f"## Propuesta de 6 palabras clave idóneas\n")
    if best.get("keywords"):
        for k in best["keywords"]:
            lines.append(f"- {k}")
        lines.append("")
    else:
        lines.append("- N/D\n")
    lines.append(f"## Explicación de la selección\n")
    if best.get("explanation"):
        lines.append(best["explanation"])
        lines.append("")
    else:
        lines.append("N/D\n")

    if best.get("validation_issues"):
        lines.append("## Observaciones de la validación automática\n")
        for issue in best["validation_issues"]:
            lines.append(f"- {issue}")
        lines.append("")

    attempts = best.get("attempts")
    if attempts:
        lines.append(f"_Intentos realizados: {attempts}_\n")

    proposed = [kw.strip() for kw in best.get("keywords", []) if kw.strip()]
    original_pairs = [("ES", kw) for kw in original_es] + [("EN", kw) for kw in original_en]
    if original_pairs:
        lines.append("## Comparativa con las palabras clave originales\n")
        if proposed:
            normalized_new = {kw.lower() for kw in proposed}
            for lang, kw in original_pairs:
                marker = "✔" if kw.lower() in normalized_new else "✘"
                lines.append(f"- {marker} {lang}: {kw}")
        else:
            for lang, kw in original_pairs:
                lines.append(f"- {lang}: {kw}")
        lines.append("")

    if best.get("used_excerpt"):
        lines.append("_Nota: Se trabajó con un extracto representativo del TFE por límites de contexto del modelo._\n")
    # Guarda además la respuesta bruta por trazabilidad
    if best.get("raw"):
        lines.append("## Respuesta bruta del modelo (para trazabilidad)\n")
        lines.append("```")
        lines.append(best["raw"])
        lines.append("```")
        lines.append("")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
    except OSError as exc:
        raise RuntimeError(f"No se pudo escribir el informe en '{output_path}': {exc}")
    else:
        print(f"Informe guardado en: {output_path}")


def main():
    try:
        file_path = select_tfe_file()
        if not file_path:
            return

        # Extrae el texto para obtener las palabras clave declaradas por el alumno
        full_text = extract_full_text(file_path)
        sections = parse_keywords_sections(full_text)
        original_es = sections.get("es", [])
        original_en = sections.get("en", [])

        # Llama a OpenAI con instrucciones reforzadas y realimentación automática
        best = generate_keywords_with_feedback(
            file_path,
            original_es,
            original_en,
            full_text,
        )

        if best.get("used_excerpt"):
            print("Aviso: se utilizó un extracto representativo del TFE por límites de contexto.")

        if best.get("validation_issues"):
            print("Aviso: la validación automática detectó incidencias que requieren revisión:")
            for issue in best["validation_issues"]:
                print(f"  - {issue}")

        # Escribe el informe Markdown en la misma carpeta
        base_dir = os.path.dirname(file_path)
        stem = os.path.splitext(os.path.basename(file_path))[0]
        out_md = os.path.join(base_dir, f"{stem}.keywords.md")

        write_markdown(out_md, file_path, original_es, original_en, best)
        print("Proceso completado correctamente.")

    except Exception as e:
        # En caso de error, genera un log en el escritorio del usuario
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            with open(os.path.join(desktop, "tfe_keywords_error.log"), "w", encoding="utf-8") as logf:
                logf.write(f"Error: {e}\n\n")
                logf.write(traceback.format_exc())
        except Exception:
            pass
        # Informar en pantalla y asegurar que el proceso devuelva un código de error
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
