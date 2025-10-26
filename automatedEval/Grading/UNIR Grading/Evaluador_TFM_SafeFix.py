#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador TFM - SafeFix

Objetivo:
- No tocar la versión en Git.
- Mantener `temperature=0.0` (determinismo), pero garantizar que el prompt 
  incorpora elementos únicos del documento (hash, frases clave) para que
  respuestas idénticas no se deban a prompts idénticos por error.
- Limpiar variables globales usadas por el script original.
- Añadir logging detallado de selección/lectura/prompt-hash.
- Usar los YAML de configuración existentes.

Uso:
  /Users/juanjo/.../venv_arm64/bin/python Evaluador_TFM_SafeFix.py

"""
from __future__ import annotations

import os
import sys
import json
import hashlib
import time
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

# Rutas relativas basadas en la ubicación del script
ROOT_AUTOMATED = Path(__file__).resolve().parents[2]
TFM_PACKAGE = ROOT_AUTOMATED / "TFM_Evaluator_Prompt_Package"

CONFIG_SISTEMA = TFM_PACKAGE / "configuracion_sistema_tfm.yaml"
CONFIG_PROMPT = TFM_PACKAGE / "TFM_Evaluator_Prompt.yaml"
PLANTILLAS_PREG = TFM_PACKAGE / "plantillas_preguntas.yaml"

# Carpeta para resultados propia (no sobrescribe original)
DIR_SELF = Path(__file__).resolve().parent
RESULTS_DIR = DIR_SELF / "resultados_safe"
RESULTS_DIR.mkdir(exist_ok=True)

# Globals we will reset to avoid cross-run contamination
def reset_globals():
    globals_to_reset = ["_contador_llamadas", "_patrones_usados"]
    for g in globals_to_reset:
        if g in globals():
            try:
                del globals()[g]
            except Exception:
                globals()[g] = None

# Logger
def configurar_logger():
    """Devuelve un logger nulo (no hace nada). Eliminamos uso de logs para simplificar.
    Mantener la función para compatibilidad con llamadas existentes.
    """
    class NullLogger:
        def info(self, *args, **kwargs):
            return None
        def error(self, *args, **kwargs):
            return None
        def exception(self, *args, **kwargs):
            return None
        def warning(self, *args, **kwargs):
            return None
    return NullLogger()

# Carga configuración YAML mínima
def cargar_config_yaml() -> Dict[str, Any]:
    cfg = {}
    for key, path in ("sistema", CONFIG_SISTEMA), ("evaluador", CONFIG_PROMPT), ("plantillas", PLANTILLAS_PREG):
        try:
            with open(path, "r", encoding="utf-8") as f:
                cfg[key] = yaml.safe_load(f) or {}
        except Exception:
            cfg[key] = {}
    return cfg


def validar_config_minima(cfg: Dict[str, Any]) -> None:
    """Verifica que existan las secciones esenciales en los YAML. Si falta, lanza RuntimeError.
    Requisito: al menos la sección 'sistema' y 'evaluador' deben contener datos.
    """
    sistema = cfg.get("sistema") or {}
    evaluador = cfg.get("evaluador") or {}
    if not sistema or not evaluador:
        raise RuntimeError("Faltan archivos YAML de configuración o están vacíos. Se requiere 'sistema' y 'evaluador'.")

# Selector (AppKit NSOpenPanel) - funciona sólo en macOS
def seleccionar_archivo_pdf_docx(logger: Any) -> Optional[str]:
    if logger is None:
        logger = configurar_logger()
    try:
        from AppKit import NSOpenPanel, NSModalResponseOK
    except Exception as e:
        logger.error("AppKit no disponible: selección de archivo no funcionará aquí. Error: %s", e)
        return None
    panel = NSOpenPanel.openPanel()
    # Aceptar tanto PDF como DOCX
    panel.setAllowedFileTypes_(["pdf", "docx"])  # <--- corregido: lista de extensiones
    panel.setAllowsMultipleSelection_(False)
    panel.setMessage_("Selecciona el TFM (PDF o DOCX)")
    if panel.runModal() == NSModalResponseOK:
        url = panel.URLs()[0]
        path = url.path()
        logger.info(f"Archivo seleccionado: {path}")
        return path
    return None

# Lectura PDF/DOCX con hash
def leer_tfm(path: str, logger: Any) -> str:
    if logger is None:
        logger = configurar_logger()
    if not os.path.exists(path):
        logger.error("No existe archivo: %s", path)
        return ""
    ext = Path(path).suffix.lower()
    contenido = ""
    try:
        if ext == ".pdf":
            import pdfplumber
            with pdfplumber.open(path) as pdf:
                logger.info("Páginas PDF: %s", len(pdf.pages))
                for i, page in enumerate(pdf.pages, 1):
                    text = page.extract_text() or ""
                    if text.strip():
                        contenido += f"[P{i}] " + text + "\n"
        elif ext == ".docx":
            from docx import Document
            doc = Document(path)
            logger.info("Párrafos DOCX: %s", len(doc.paragraphs))
            for p in doc.paragraphs:
                if p.text.strip():
                    contenido += p.text + "\n"
        else:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                contenido = f.read()
    except Exception as e:
        logger.exception("Error extrayendo texto: %s", e)
        return ""

    h = hashlib.md5(contenido.encode("utf-8")).hexdigest()
    logger.info("MD5 contenido: %s | longitud: %d", h, len(contenido))
    logger.info("Primeros 200 chars: %s", repr(contenido[:200]))
    return contenido

# Extracción rápida de frases clave (n-grams simples)
def extraer_frases_clave(texto: str, n: int = 5) -> List[str]:
    tokens = re.findall(r"\w+", texto.lower())
    frec: Dict[str, int] = {}
    for t in tokens:
        if len(t) > 3:
            frec[t] = frec.get(t, 0) + 1
    items = sorted(frec.items(), key=lambda x: -x[1])[:n]
    return [w for w, _ in items]


# Helper para calcular rutas de exportación (intenta crear subcarpeta en la carpeta del TFM)
def paths_para_exportar(ruta_tfm: Optional[str], ts: str, config: Optional[Dict[str, Any]] = None):
    """Devuelve rutas de salida para csv/json/md.
    Si la configuración YAML contiene `sistema.archivos_config.nombres_salida`, se usan
    los nombres definidos allí. En otro caso, se usan los nombres por defecto.
    Siempre escribe directamente en la carpeta del TFM (sin subcarpeta).
    """
    if not ruta_tfm:
        raise RuntimeError("No se proporcionó ruta del TFM para exportar")

    tfm_dir = Path(ruta_tfm).resolve().parent

    # Valores por defecto (coinciden con convención existente)
    default_names = {
        "csv": "evaluacion_tfm_resultado.csv",
        "json": "evaluacion_tfm_informe.json",
        "markdown": "evaluacion_tfm_informe.md",
    }

    try:
        nombres = (config or {}).get("sistema", {}).get("archivos_config", {}).get("nombres_salida", {})
        csv_name = nombres.get("csv") or default_names["csv"]
        json_name = nombres.get("json") or default_names["json"]
        md_name = nombres.get("markdown") or default_names["markdown"]
    except Exception:
        csv_name = default_names["csv"]
        json_name = default_names["json"]
        md_name = default_names["markdown"]

    csv_direct = tfm_dir / csv_name
    json_direct = tfm_dir / json_name
    md_direct = tfm_dir / md_name
    return csv_direct, json_direct, md_direct

# Construir prompt incluyendo hash y frases clave para diferenciación
def construir_prompt(criterio: str, instrucciones: str, texto_tfm: str, doc_hash: str, phrases: List[str]) -> str:
    sample = texto_tfm[:6000]
    prompt = (
        f"Eres un evaluador académico. Criterio: {criterio}\n"
        f"Instrucciones: {instrucciones}\n"
        f"Documento hash: {doc_hash}\n"
        f"Frases clave: {', '.join(phrases)}\n"
        f"Texto relevante (recorte):\n{sample}\n"
        "Responde en formato JSON con campos: criterio, nivel(1-4), justificacion, areas_mejora, evidencias."
    )
    return prompt

# Llamada a OpenAI (compatible con distintas versiones)
def obtener_respuesta_openai(prompt: str, config: Dict[str, Any], logger: Any) -> str:
    if logger is None:
        logger = configurar_logger()
    openai_cfg = config.get("sistema", {}).get("openai_config", {})
    variables_api = openai_cfg.get("variables_api_key", ["MI_CLAVE_API_OPENAI", "OPENAI_API_KEY"])
    api_key = None
    for v in variables_api:
        api_key = os.getenv(v)
        if api_key:
            break
    if not api_key:
        # No continuar sin clave: lanzar excepción para que el script pare según la política del usuario
        raise RuntimeError(f"No API key encontrada en variables de entorno: {variables_api}")

    temperatura = openai_cfg.get("temperatura_por_defecto", 0.0)
    max_tokens_eval = openai_cfg.get("max_tokens_evaluacion", 900)
    modelo = openai_cfg.get("modelo_por_defecto", "gpt-4o-mini")

    try:
        import openai
        # Prefer new client style
        try:
            client = openai.OpenAI(api_key=api_key)
            logger.info("Usando cliente openai.OpenAI, modelo=%s temp=%s", modelo, temperatura)
            resp = client.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura,
                max_tokens=max_tokens_eval,
            )
            return getattr(resp.choices[0].message, "content", resp.choices[0].message.content)
        except Exception:
            # Fallback histórico
            logger.info("Fallback a openai.ChatCompletion.create")
            resp = openai.ChatCompletion.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura,
                max_tokens=max_tokens_eval,
            )
            return resp.choices[0].message.content if hasattr(resp.choices[0], 'message') else resp.choices[0].text
    except Exception as e:
        logger.exception("Error llamando OpenAI: %s", e)
        raise


def obtener_api_key_desde_config(config: Dict[str, Any]) -> str:
    """Devuelve la API key encontrada en entorno según las variables configuradas en YAML.
    Lanza RuntimeError si no encuentra ninguna clave.
    """
    openai_cfg = config.get("sistema", {}).get("openai_config", {})
    variables_api = openai_cfg.get("variables_api_key", ["MI_CLAVE_API_OPENAI", "OPENAI_API_KEY"])
    for v in variables_api:
        val = os.getenv(v)
        if val:
            return val
    raise RuntimeError(f"No API key encontrada en variables de entorno: {variables_api}")

# Evaluación minimalista usando rúbrica en xlsx
def cargar_rubrica_por_defecto(config: Dict[str, Any], logger: Any):
    if logger is None:
        logger = configurar_logger()
    rutas = config.get("sistema", {}).get("rutas_sistema", {}).get("rubricas", {})
    if not rutas:
        logger.error("No hay rúbricas configuradas en YAML")
        return None
    primera = list(rutas.values())[0]
    try:
        import pandas as pd
        df = pd.read_excel(primera)
        logger.info("Rúbrica cargada: %s (filas=%d)", primera, len(df))
        return df
    except Exception as e:
        logger.exception("Error cargando rúbrica: %s", e)
        return None

def evaluar_tfm_minimal(texto_tfm: str, rubrica_df, config: Dict[str, Any], logger: Any) -> List[Dict[str, Any]]:
    resultados = []
    if logger is None:
        logger = configurar_logger()
    if rubrica_df is None or not texto_tfm.strip():
        return resultados
    doc_hash = hashlib.md5(texto_tfm.encode("utf-8")).hexdigest()
    phrases = extraer_frases_clave(texto_tfm, n=6)
    instrucciones = (config.get("evaluador", {}).get("context")
                     or "Evalúa el criterio con rigor académico.")

    for _, row in rubrica_df.iterrows():
        criterio = str(row.iloc[0]).strip()
        if not criterio or criterio.lower() in {"nan", "none", ""}:
            continue
        # Intentar extraer las 4 descripciones de nivel desde la rúbrica
        descripcion_niveles: List[str] = []
        try:
            # Si la rúbrica tiene al menos 5 columnas, asumimos: [criterio, nivel1, nivel2, nivel3, nivel4, ...]
            if len(row) >= 5:
                # Tomar las siguientes 4 columnas tras la primera
                descripcion_niveles = [str(x).strip() for x in row.iloc[1:5]]
            else:
                # Intentar buscar columnas cuyo nombre sugiera 'nivel' o 'level'
                cols = list(rubrica_df.columns)
                cand = []
                for c in cols[1:]:
                    if isinstance(c, str) and re.search(r"nivel|level|score|descriptor", c, re.I):
                        cand.append(c)
                if cand:
                    for c in cand[:4]:
                        descripcion_niveles.append(str(row[c]).strip())
        except Exception:
            descripcion_niveles = []

        # Construir prompt incluyendo las descripciones numeradas si existen
        if descripcion_niveles and len(descripcion_niveles) == 4:
            niveles_text = "\n".join([f"{i+1}. {d}" for i, d in enumerate(descripcion_niveles)])
            prompt_extra = (
                "A continuación se proporcionan 4 descripciones de niveles para este criterio. "
                "Responde indicando únicamente el número (1-4) que mejor describe el trabajo, y justifica la elección.\n"
                f"Descripciones:\n{niveles_text}\n"
            )
        else:
            prompt_extra = "Indica el nivel del trabajo (1-4) y justifica la elección."

        prompt = construir_prompt(criterio, instrucciones + "\n" + prompt_extra, texto_tfm, doc_hash, phrases)
        prompt_hash = hashlib.md5(prompt.encode("utf-8")).hexdigest()
        logger.info("Evaluando criterio: %s | prompt_hash: %s", criterio, prompt_hash)
        resp = obtener_respuesta_openai(prompt, config, logger)
        # Intentar parsear JSON, fallback básico
        if not resp:
            logger.error("Respuesta vacía para criterio: %s", criterio)
            continue
        resp_cand = resp.strip()
        try:
            # Some models return ```json blocks
            if resp_cand.startswith("```json"):
                resp_cand = resp_cand[7:]
                if resp_cand.endswith("```"):
                    resp_cand = resp_cand[:-3]
            elif resp_cand.startswith("```"):
                resp_cand = resp_cand[3:]
                if resp_cand.endswith("```"):
                    resp_cand = resp_cand[:-3]
            parsed = json.loads(resp_cand)
            # Normalizar: asegurarnos de que existe 'descripcion_nivel' con el texto correspondiente
            nivel_elegido = parsed.get("nivel")
            try:
                nivel_idx = int(nivel_elegido) - 1 if nivel_elegido is not None else None
            except Exception:
                nivel_idx = None
            if nivel_idx is not None and descripcion_niveles and 0 <= nivel_idx < len(descripcion_niveles):
                parsed.setdefault("descripcion_nivel", descripcion_niveles[nivel_idx])
            else:
                # Si no pudimos deducir, dejar descripcion_nivel vacía o tomar la que venga en parsed
                parsed.setdefault("descripcion_nivel", parsed.get("descripcion_nivel") or "")

            # Añadir las descripciones de los 4 niveles al resultado para que JSON y CSV contengan
            # las mismas columnas/valores y sea posible sincronizarlos.
            for i in range(4):
                key = f"nivel_{i+1}"
                parsed.setdefault(key, descripcion_niveles[i] if i < len(descripcion_niveles) else "")

            resultados.append(parsed)
            logger.info("Parse OK criterio %s -> nivel %s", criterio, parsed.get("nivel"))
        except Exception:
            logger.exception("No se pudo parsear JSON. Respuesta: %s", resp)
            # Guardar fallback
            resultados.append({"criterio": criterio, "nivel": None, "justificacion": resp_cand, "descripcion_nivel": ""})
        time.sleep(0.5)
    return resultados

# Exportar resultados
def _generar_markdown(resultados: List[Dict[str, Any]], preguntas: Optional[List[Dict[str, Any]]] = None) -> str:
    """Genera un informe en Markdown a partir de la lista de resultados.
    Estructura similar al archivo `evaluacion_tfm_informe.md` adjunto.
    """
    lines = ["# Informe de Evaluación TFM", ""]
    # Añadir secciones por criterio
    for r in resultados:
        criterio = r.get('criterio') or ''
        nivel = r.get('nivel') or ''
        just = r.get('justificacion') or ''
        evid = r.get('evidencias') or ''
        areas = r.get('areas_mejora') or ''
        lines.append(f"## {criterio}\n")
        lines.append(f"- **Nivel alcanzado**: {nivel}")
        if just:
            lines.append(f"- **Justificación**: {just}")
        if evid:
            lines.append(f"- **Evidencias**: {evid}")
        if areas:
            lines.append(f"- **Áreas de mejora**: {areas}")
        lines.append("")
    # Tabla resumen
    lines.append("## Tabla de Evaluación")
    lines.append("")
    lines.append("| Criterio | Nivel |")
    lines.append("|----------|-------|")
    for r in resultados:
        criterio = (r.get('criterio') or '').replace('\n', ' ')
        nivel = r.get('nivel') or ''
        lines.append(f"| {criterio} | {nivel} |")
    lines.append("")
    # Preguntas de clarificación (si las hay)
    if preguntas:
        lines.append("## Preguntas de clarificación")
        lines.append("")
        for i, p in enumerate(preguntas, 1):
            q = p.get('question') or p.get('pregunta') or ''
            mot = p.get('motivation') or p.get('motivacion') or ''
            hints = p.get('hints') or p.get('pistas') or ''
            lines.append(f"### Pregunta {i}")
            if q:
                lines.append(f"- **Pregunta**: {q}")
            if mot:
                lines.append(f"- **Motivación**: {mot}")
            if hints:
                lines.append(f"- **Hints**: {hints}")
            lines.append("")
    return '\n'.join(lines)


def exportar(resultados: List[Dict[str, Any]], texto_tfm: str, ruta_tfm: Optional[str], config: Optional[Dict[str, Any]], logger: Any) -> None:
    # No hay fallback: se escriben directamente en la carpeta del TFM o se lanza excepción
    csv_path, json_path, md_path = paths_para_exportar(ruta_tfm, time.strftime("%Y%m%d_%H%M%S"), config)
    # CSV
    import pandas as pd
    try:
        # Normalizar y ordenar columnas: intentar imponer un esquema útil y estable
        df = pd.DataFrame(resultados)
        # Columnas preferidas en el CSV para compatibilidad con automatización externa
        preferred = [
            "criterio",
            "nivel",
            "descripcion_nivel",
            "nivel_1",
            "nivel_2",
            "nivel_3",
            "nivel_4",
            "justificacion",
            "areas_mejora",
            "evidencias",
        ]
        # Añadir columnas faltantes con cadena vacía
        for c in preferred:
            if c not in df.columns:
                df[c] = ""
        df = df[preferred + [c for c in df.columns if c not in preferred]]
        df.to_csv(csv_path, index=False, encoding="utf-8")
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar CSV en {csv_path}: {e}")
    # JSON
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar JSON en {json_path}: {e}")
    # MD
    try:
        # Preguntas no se serializan al CSV/JSON, solo al MD si se han generado
        md_content = _generar_markdown(resultados, preguntas=None)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar MD en {md_path}: {e}")


def generar_preguntas_clarificacion(texto_tfm: str, resultados: List[Dict[str, Any]], config: Dict[str, Any], logger: Any) -> List[Dict[str, Any]]:
    """Genera preguntas de clarificación académica usando las plantillas.
    Reglas: generar exactamente el número definido en plantillas (por defecto 3). Si falla el parseo JSON
    se debe lanzar excepción (no fallback).
    """
    if logger is None:
        logger = configurar_logger()
    # Cargar plantilla
    plant = (config or {}).get("plantillas", {})
    analisis_cfg = plant.get("analisis_critico") or {}
    numero = analisis_cfg.get("numero_preguntas_exactas") or analisis_cfg.get("numero_preguntas") or 3
    # Crear prompt usando plantilla si existe
    try:
        plantilla_text = analisis_cfg.get("analisis_profundo")
    except Exception:
        plantilla_text = None

    phrases = extraer_frases_clave(texto_tfm, n=6)
    doc_hash = hashlib.md5(texto_tfm.encode("utf-8")).hexdigest()

    if plantilla_text:
        prompt = plantilla_text.format(numero_preguntas=numero, numero_preguntas_exactas=numero)
        # Añadir contexto único
        prompt = (
            f"{prompt}\nDocumento hash: {doc_hash}\nFrases clave: {', '.join(phrases)}\n"
            "Responde en JSON con una lista llamada 'questions' donde cada elemento tiene: question, motivation, hints."
        )
    else:
        prompt = (
            f"Genera EXACTAMENTE {numero} preguntas académicas de clarificación sobre el documento. "
            "Cada pregunta debe incluir: question, motivation, hints. Usa elementos únicos del documento y sé concreto.\n"
            f"Documento hash: {doc_hash}\nFrases clave: {', '.join(phrases)}\n"
            "Responde en JSON con una lista llamada 'questions'."
        )

    resp = obtener_respuesta_openai(prompt, config, logger)
    if not resp:
        raise RuntimeError("No se obtuvo respuesta para generación de preguntas")
    # Limpiar bloque ```json si existe
    rc = resp.strip()
    if rc.startswith("```json"):
        rc = rc[7:]
        if rc.endswith("```"):
            rc = rc[:-3]
    elif rc.startswith("```"):
        rc = rc[3:]
        if rc.endswith("```"):
            rc = rc[:-3]

    parsed = json.loads(rc)
    questions = parsed.get("questions") or parsed.get("questions_list") or parsed.get("questions")
    if not isinstance(questions, list):
        raise RuntimeError("La respuesta del modelo no contiene una lista 'questions' en JSON")

    # Normalizar claves de cada pregunta
    normalized: List[Dict[str, Any]] = []
    for q in questions:
        if not isinstance(q, dict):
            raise RuntimeError("Elemento de 'questions' no es un objeto JSON")
        normalized.append({
            "question": q.get("question") or q.get("pregunta") or "",
            "motivation": q.get("motivation") or q.get("motivacion") or "",
            "hints": q.get("hints") or q.get("pistas") or "",
        })

    # Verificar unicidad simple: comparar texto de pregunta con preguntas previas en resultados (si existieran)
    seen = set()
    uniq: List[Dict[str, Any]] = []
    for q in normalized:
        key = (q.get("question") or "").strip()
        if not key:
            continue
        if key in seen:
            # Repetición en la propia lista: considerar esto un error según la política
            raise RuntimeError("Modelo generó preguntas duplicadas")
        seen.add(key)
        uniq.append(q)

    if len(uniq) < numero:
        raise RuntimeError(f"Se generaron {len(uniq)} preguntas únicas, se esperaban {numero}")

    return uniq[:numero]

# Main
def main() -> int:
    reset_globals()
    logger = configurar_logger()
    config = cargar_config_yaml()

    logger.info("=== Evaluador TFM SafeFix (no modifica Git) ===")
    # Validar que los YAML mínimos existan y contengan datos
    try:
        validar_config_minima(config)
    except RuntimeError as e:
        logger.error(str(e))
        print(f"ERROR: {e}")
        return 1

    # Validar que exista API key para OpenAI antes de comenzar
    try:
        _ = obtener_api_key_desde_config(config)
    except RuntimeError as e:
        logger.error(str(e))
        print(f"ERROR: {e}")
        return 1

    ruta = seleccionar_archivo_pdf_docx(logger)
    if not ruta:
        logger.error("No se seleccionó archivo. Abortando.")
        return 1
    texto = leer_tfm(ruta, logger)
    if not texto.strip():
        logger.error("Texto vacío después de leer. Abortando.")
        return 1
    rubrica = cargar_rubrica_por_defecto(config, logger)
    if rubrica is None:
        logger.error("No se pudo cargar rúbrica. Abortando.")
        return 1
    resultados = evaluar_tfm_minimal(texto, rubrica, config, logger)
    # Generar preguntas de clarificación y escribir solo en el MD
    try:
        preguntas = generar_preguntas_clarificacion(texto, resultados, config, logger)
    except Exception as e:
        logger.error("Generación de preguntas falló: %s", e)
        # Seguir la política: no usar fallbacks, señalizar error y abortar
        print(f"ERROR: Generación de preguntas falló: {e}")
        return 1

    # Guardar la última ruta leída para que la función exportar pueda escribir junto al TFM
    exportar(resultados, texto, ruta, config, logger)
    # Reescribir MD incluyendo las preguntas
    csv_path, json_path, md_path = paths_para_exportar(ruta, time.strftime("%Y%m%d_%H%M%S"), config)
    md_content = _generar_markdown(resultados, preguntas=preguntas)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    logger.info("Evaluación completada. Archivos guardados en la carpeta del TFM.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
