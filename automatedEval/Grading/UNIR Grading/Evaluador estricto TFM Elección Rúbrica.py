#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador TFM Integrado – Finder + OneDrive + OpenAI
===================================================

Integra en un único script:
1) **Selector de archivo** (AppKit/NSOpenPanel) y lectura de **etiquetas Finder** (kMDItemUserTags) con soporte OneDrive (hidratar).
2) **Selección automática de rúbrica** según etiquetas Finder → ruta de rúbrica.
3) **Extracción de texto** del TFM (PDF / DOCX).
4) **Evaluación con OpenAI** por criterios de la rúbrica (CSV + Markdown).

Probado en macOS (Apple Silicon) con Python 3.11/3.12/3.13.

Uso rápido
----------
$ python evaluador_tfm_integrado.py \
    [--pdf /ruta/TFM.pdf|.docx] \
    [--rubrica /ruta/rubrica.(xlsx|csv|json)] \
    [--instrucciones /ruta/Prompt_ultraestricto.md] \
    [--modelo gpt-4o-mini] \
    [--temperatura 0.0]

Si no se proporcionan rutas, el script abre un selector para elegir el TFM y resuelve la rúbrica por etiquetas Finder.

Requisitos
----------
- pdfplumber, python-docx (docx), pandas, openai>=1.0, python-dotenv (opcional), AppKit (pyobjc),
- macOS con utilidades `mdls` y (opcional) `fileproviderctl`.
- Variable de entorno **MI_CLAVE_API_OPENAI** con tu API key.
"""
from __future__ import annotations

import os
import sys
import json
import csv
import logging
import plistlib
import subprocess
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

# ----------------------------
# Configuración editable
# ----------------------------
RUBRICAS_POR_ETIQUETA: dict[str, str] = {
    "MUDPE": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MUDPE.xlsx",
    "MUGPTD": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MUGPTD.xlsx",
}

RUTA_RUBRICA_POR_DEFECTO = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica.csv"  # <- existe en tu proyecto
RUTA_INSTRUCCIONES_POR_DEFECTO = "/Users/juanjo/Documents/Personal/JJVR/...matedEval/TFM_Evaluator_Prompt_Package/Prompt en modo humano.md"
MODELO_POR_DEFECTO = "gpt-4o-mini"
# Ruta opcional a un fichero externo (.md) con las INSTRUCCIONES ESTRICTAS.
# Si existe, se usará este contenido en lugar de las instrucciones internas.
RUTA_INSTRUCCIONES_MD = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/Ultraestricto.md"
TEMPERATURA_POR_DEFECTO = 0.0
FORZAR_NFC = True
ONEDRIVE_HINTS = ("OneDrive", "OneDrive - ")

# ----------------------------
# Logging
# ----------------------------

def configurar_logger(path_salida: Optional[str]) -> logging.Logger:
    logger = logging.getLogger("evaluador_tfm_integrado")
    logger.setLevel(logging.INFO)
    handlers: List[logging.Handler] = [logging.StreamHandler()]
    if path_salida:
        log_path = os.path.join(path_salida, "evaluador_tfm_integrado.log")
        handlers.append(logging.FileHandler(log_path, mode="w", encoding="utf-8"))
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    for h in handlers:
        h.setFormatter(fmt)
        logger.addHandler(h)
    return logger

# ----------------------------
# Utilidades de ruta/OneDrive
# ----------------------------

def normalize_path(p: str | Path, nfc: bool = True) -> str:
    s = str(p)
    return unicodedata.normalize("NFC" if nfc else "NFD", s)


def is_onedrive_path(p: str | Path) -> bool:
    s = str(p)
    return any(h in s for h in ONEDRIVE_HINTS)


def _run(cmd: List[str]) -> Tuple[int, str, str]:
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def ensure_hydrated(path: str, logger: logging.Logger) -> None:
    try:
        with open(path, "rb") as f:
            _ = f.read(1)
        return
    except Exception as e:
        if is_onedrive_path(path):
            fpctl = "/usr/bin/fileproviderctl"
            if Path(fpctl).exists():
                rc, out, err = _run([fpctl, "materialize", "-p", path])
                if rc != 0:
                    logger.warning(f"No se pudo materializar con fileproviderctl (rc={rc}). {err}")
            else:
                logger.warning("'fileproviderctl' no disponible. Continuamos.")
        # intento final
        try:
            with open(path, "rb") as f:
                _ = f.read(1)
        except Exception as e2:
            logger.warning(f"No se pudo hidratar el archivo: {e2}")

# ----------------------------
# Selector de archivo (NSOpenPanel con fallback a consola)
# ----------------------------

def seleccionar_archivo(allowed_types: List[str], titulo: str, mensaje: str, logger: logging.Logger) -> Optional[str]:
    # GUI con AppKit
    try:
        from AppKit import NSApplication, NSOpenPanel  # type: ignore
        NSApp = NSApplication.sharedApplication()
        NSApp.activateIgnoringOtherApps_(True)
        panel = NSOpenPanel.openPanel()
        panel.setCanChooseFiles_(True)
        panel.setCanChooseDirectories_(False)
        panel.setAllowsMultipleSelection_(False)
        panel.setAllowedFileTypes_(allowed_types)
        panel.setTitle_(titulo)
        panel.setMessage_(mensaje)
        if panel.runModal() == 1:
            path = panel.URLs()[0].path()
            return normalize_path(path, nfc=FORZAR_NFC)
    except Exception as e:
        logger.info(f"Selector GUI no disponible, fallback a consola ({e})")

    # Consola
    try:
        ruta = input("Introduce la ruta del archivo: ").strip()
        if ruta:
            return normalize_path(ruta, nfc=FORZAR_NFC)
    except (EOFError, KeyboardInterrupt):
        return None
    return None

# ----------------------------
# Lectura de etiquetas Finder (mdls)
# ----------------------------

def leer_etiquetas_finder(path: str, logger: logging.Logger) -> List[str]:
    rc, out, err = _run(["/usr/bin/mdls", "-plist", "-name", "kMDItemUserTags", path])
    if rc == 0 and out.strip():
        try:
            d = plistlib.loads(out.encode("utf-8"))
            tags = d.get("kMDItemUserTags")
            if isinstance(tags, list):
                clean = []
                for t in tags:
                    if isinstance(t, str):
                        clean.append(t.split("\n", 1)[0])  # sin sufijo de color
                return clean
        except Exception:
            pass
    # fallback -raw
    rc, out, err = _run(["/usr/bin/mdls", "-name", "kMDItemUserTags", "-raw", path])
    if rc == 0:
        line = out.strip().strip("()\n ")
        if not line or line == "(null)":
            return []
        tags = []
        for raw in line.split(","):
            t = raw.strip()
            if not t:
                continue
            t = t.split("\n", 1)[0]
            tags.append(t)
        return tags
    logger.warning(f"No se pudieron leer etiquetas Finder: {err}")
    return []


def seleccionar_rubrica_por_etiquetas(tags: List[str], logger: logging.Logger) -> str:
    """
    Selecciona la rúbrica basada en las etiquetas Finder. Si no se encuentra una rúbrica correspondiente,
    solicita al usuario que seleccione una manualmente.

    Parámetros:
        tags (List[str]): Lista de etiquetas Finder.
        logger (logging.Logger): Logger para registrar eventos.

    Retorna:
        str: Ruta de la rúbrica seleccionada.
    """
    for t in tags:
        if t in RUBRICAS_POR_ETIQUETA:
            logger.info(f"Rúbrica encontrada para la etiqueta '{t}': {RUBRICAS_POR_ETIQUETA[t]}")
            return RUBRICAS_POR_ETIQUETA[t]

    logger.warning("No se encontró una rúbrica correspondiente a las etiquetas. Se solicitará al usuario que seleccione una.")
    ruta_rubrica = seleccionar_archivo(["xlsx", "csv", "json"], "Selecciona una rúbrica", "Elige el archivo de la rúbrica", logger)
    if not ruta_rubrica:
        raise FileNotFoundError("No se seleccionó ninguna rúbrica y no se puede continuar sin una.")

    logger.info(f"Rúbrica seleccionada manualmente: {ruta_rubrica}")
    return ruta_rubrica

# ----------------------------
# Carga de rúbrica
# ----------------------------

def cargar_rubrica(path: str, logger: logging.Logger):
    import pandas as pd
    ext = Path(path).suffix.lower()
    try:
        if ext in (".xlsx", ".xls"):
            df = pd.read_excel(path)
        elif ext == ".csv":
            df = pd.read_csv(path)
        elif ext == ".json":
            import json
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            df = pd.DataFrame(data)
        else:
            raise ValueError("Formato de rúbrica no soportado. Usa .xlsx, .csv o .json")
        # Validación mínima: primera columna son los criterios
        if df.shape[1] == 0:
            raise ValueError("La rúbrica está vacía")
        logger.info(f"Rúbrica cargada: {path} → {len(df)} filas / {len(df.columns)} columnas")
        return df
    except Exception as e:
        logger.error(f"Error cargando rúbrica: {e}")
        return None

# ----------------------------
# Carga de instrucciones (MD opcional)
# ----------------------------

def cargar_instrucciones_md_opcional(path_md: Optional[str], logger: logging.Logger) -> str:
    """Devuelve el contenido de instrucciones estrictas.
    Preferencia: si existe un fichero externo (MD), se usa tal cual. Si no, se usa el bloque interno.
    """
    base = (
        "Actúa como evaluador académico experto en TFMs de UNIR con MODELO ULTRAESTRICTO. "
        "Solo asigna NIVEL 4 si TODOS los elementos esenciales del criterio se cumplen SIN EXCEPCIÓN y con coherencia profunda. "
        "Si el texto no aporta evidencia suficiente, responde 'No evaluable'. "
        "Mantén exactamente el ORDEN y REDACCIÓN de la rúbrica. "
        "Incluye reflexión crítica y congruencia diagnóstica (diagnóstico↔justificación↔objetivos↔metodología↔propuesta↔resultados). "
        "Cuando el criterio lo permita, evalúa relación AS‑IS/TO‑BE."
    )
    if path_md and Path(path_md).exists():
        try:
            externo = Path(path_md).read_text(encoding="utf-8")
            logger.info(f"Usando instrucciones externas desde: {path_md}")
            return externo
        except Exception as e:
            logger.warning(f"No se pudo leer el MD de instrucciones externo: {e}. Usando internas.")
    logger.info("Usando instrucciones internas ultraestrictas.")
    return base

# ----------------------------
# Extracción de texto del TFM
# ----------------------------

def leer_tfm(path: str, logger: logging.Logger) -> str:
    """Extrae texto y añade marcas de página [P#] para evidencias citables."""
    ext = Path(path).suffix.lower()
    try:
        if ext == ".pdf":
            import pdfplumber
            logger.info("Extrayendo texto del PDF con marcas de página…")
            partes = []
            with pdfplumber.open(path) as pdf:
                for i, page in enumerate(pdf.pages):
                    try:
                        t = (page.extract_text() or "").strip()
                        partes.append(f"[P{i+1}]\n" + (t if t else "(sin texto extraíble)"))
                    except Exception as e:
                        logger.warning(f"Página {i+1}: {e}")
                        partes.append(f"[P{i+1}] (error de extracción)")
            return "\n".join(partes)
        elif ext in (".docx", ".doc"):
            import docx
            logger.info("Extrayendo texto del DOC/DOCX… (sin paginación fiable)")
            d = docx.Document(path)
            cuerpo = "\n".join(p.text for p in d.paragraphs)
            return "[P1]\n" + cuerpo
        else:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                contenido = f.read()
            return "[P1]\n" + contenido
    except Exception as e:
        logger.error(f"Error leyendo TFM: {e}")
        return ""

# ----------------------------
# Cliente OpenAI (compatibilidad v0.x y v1.x)

def crear_cliente_openai(logger: logging.Logger):
    api_key = os.getenv("MI_CLAVE_API_OPENAI") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Falta la variable de entorno MI_CLAVE_API_OPENAI u OPENAI_API_KEY")
    try:
        # Nuevo SDK (>=1.0)
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        logger.info("OpenAI client (v1) inicializado")
        return ("v1", client)
    except Exception:
        import openai
        openai.api_key = api_key
        logger.info("OpenAI client (v0.x) inicializado")
        return ("v0", openai)

# ----------------------------
# Evaluación por criterio
# ----------------------------

def construir_prompt(criterio: str, instrucciones_base: str, texto_tfm: str) -> str:
    schema = (
        "Devuelve SOLO JSON con este esquema exacto: {"
        "\"nivel\": \"1|2|3|4|No evaluable\", "
        "\"justificacion\": \"texto\", "
        "\"areas_mejora\": \"texto o vacio si nivel=4\", "
        "\"evidencias\": [{\"frase\": \"cita breve\", \"pagina\": \"P#\"}] }"
    )
    evidencias_rule = (
        "OBLIGATORIO: incluye ≥2 evidencias extraídas literalmente del TFM con su etiqueta de página [P#]. "
        "Si no puedes aportar 2 evidencias válidas, fija nivel=\"No evaluable\". Prohibido inventar páginas."
    )
    return f"""
Evalúa el TFM según el criterio EXACTO de la rúbrica, en modo ultraestricto.

Criterio a evaluar:
{criterio}

Guía del evaluador:
{instrucciones_base}

Formato de salida:
- {schema}
- {evidencias_rule}
- Idioma: español.

Texto del TFM (con marcas de página [P#]):
---
{text_tfm_recorte(texto_tfm)}
---
""".strip()

def text_tfm_recorte(texto: str, max_chars: int = 7000) -> str:
    if len(texto) <= max_chars:
        return texto
    # Preferir comienzos + finales del documento para contexto
    head = texto[: max_chars // 2]
    tail = texto[-max_chars // 2 :]
    return head + "\n…\n" + tail



def construir_prompt_v2(criterio: str, instrucciones_base: str, texto_tfm: str) -> str:
    """Construcción segura del prompt."""
    partes: List[str] = []
    partes.append("Evalúa el TFM según el criterio EXACTO de la rúbrica, en modo ultraestricto.")
    partes.append("")
    partes.append("Criterio a evaluar:")
    partes.append(criterio)
    partes.append("")
    partes.append("Guía del evaluador:")
    partes.append(instrucciones_base)
    partes.append("")
    partes.append("Formato de salida (JSON estricto, sin texto adicional):")
    partes.append('{ "nivel": "1|2|3|4|No evaluable", "justificacion": "texto", "areas_mejora": "texto o vacio si nivel=4", "evidencias": [{"frase": "cita breve", "pagina": "P#"}] }')
    partes.append("")
    partes.append("Reglas de evidencias: incluye al menos 2 evidencias literales del TFM con su etiqueta de página [P#]. Si no puedes, responde con nivel=\"No evaluable\".")
    partes.append("")
    partes.append("Texto del TFM (con marcas de página [P#]):\n---")
    partes.append(text_tfm_recorte(texto_tfm))
    partes.append("---")
    return "\n".join(partes) + "\n"


def evaluar_criterio(compat: str, client, modelo: str, temperatura: float, criterio: str, instrucciones: str, texto_tfm: str, logger: logging.Logger) -> str:
    prompt = construir_prompt_v2(criterio, instrucciones, texto_tfm)
    logger.info(f"Evaluando criterio: {criterio}")
    try:
        if compat == "v1":
            resp = client.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura,
                max_tokens=900,
            )
            return resp.choices[0].message.content.strip()
        else:  # v0
            import openai  # type: ignore
            resp = openai.ChatCompletion.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura,
                max_tokens=900,
            )
            return resp["choices"][0]["message"]["content"].strip()
    except Exception as e:
        logger.error(f"Error del modelo en criterio '{criterio}': {e}")
        return "[ERROR] No se pudo evaluar este criterio."


def evaluar_tfm_completo(compat: str, client, modelo: str, temperatura: float, rubrica_df, texto_tfm: str, instrucciones: str, logger: logging.Logger):
    resultados = []
    # Criterios que típicamente no se evalúan automáticamente (presentación oral, etc.)
    excluir = {"presentación", "exposición", "comunicación", "tribunal", "formato de la presentación"}
    criterios = [str(c) for c in rubrica_df.iloc[:, 0].tolist()]
    for criterio in criterios:
        low = criterio.lower()
        if any(p in low for p in excluir):
            logger.info(f"⏩ Criterio excluido: {criterio}")
            continue
        evaluacion = evaluar_criterio(compat, client, modelo, temperatura, criterio, instrucciones, texto_tfm, logger)
        resultados.append({"criterio": criterio, "evaluacion": evaluacion})
    return resultados

# ----------------------------
# Exportar resultados
# ----------------------------

def exportar_resultados(resultados: List[dict], carpeta_salida: str, logger: logging.Logger) -> Tuple[str, str, str]:
    """
    Genera los archivos de salida (.md, .csv, .json) con los resultados de la evaluación.

    - El archivo `.md` es un informe redactado con un tono formal y pedagógico, incluyendo:
        - Nivel alcanzado.
        - Justificación del nivel.
        - Evidencias (1 o 2).
        - Áreas de mejora.
        - Preguntas finales para el estudiante.
    - El archivo `.json` contiene únicamente el criterio y el nivel alcanzado.

    Parámetros:
        resultados (List[dict]): Lista de resultados de la evaluación.
        carpeta_salida (str): Carpeta donde se guardarán los archivos.
        logger (logging.Logger): Logger para registrar eventos.

    Retorna:
        Tuple[str, str, str]: Rutas de los archivos generados (.csv, .md, .json).
    """
    import pandas as pd
    csv_path = os.path.join(carpeta_salida, "evaluacion_tfm_resultado.csv")
    md_path = os.path.join(carpeta_salida, "evaluacion_tfm_informe.md")
    json_path = os.path.join(carpeta_salida, "evaluacion_tfm_informe.json")
    try:
        # Exportar a CSV
        pd.DataFrame(resultados).to_csv(csv_path, index=False)

        # Exportar a Markdown con redacción formal y pedagógica
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# Informe de Evaluación TFM\n\n")
            for r in resultados:
                f.write(f"## {r['criterio']}\n\n")
                evaluacion = json.loads(r['evaluacion'])
                f.write(f"**Nivel alcanzado:** {evaluacion['nivel']}\n\n")
                f.write(f"**Justificación:** {evaluacion['justificacion']}\n\n")
                if evaluacion['evidencias']:
                    f.write("**Evidencias:**\n")
                    for evidencia in evaluacion['evidencias']:
                        f.write(f"- {evidencia['frase']} ({evidencia['pagina']})\n")
                if evaluacion['areas_mejora']:
                    f.write(f"\n**Áreas de mejora:** {evaluacion['areas_mejora']}\n\n")
                f.write("\n")

            # Añadir preguntas finales para el estudiante
            f.write("## Preguntas para el estudiante\n\n")
            f.write("1. ¿Qué aspectos de tu trabajo consideras que podrían haber sido explicados con mayor claridad?\n")
            f.write("2. ¿Qué análisis o secciones crees que podrían haberse desarrollado con mayor profundidad?\n")
            f.write("3. ¿Qué cambios implementarías para mejorar la coherencia entre los objetivos, la metodología y los resultados?\n")

        # Exportar a JSON con solo criterio y nivel
        criterios_niveles = [
            {"criterio": r['criterio'], "nivel": json.loads(r['evaluacion'])['nivel']}
            for r in resultados
        ]
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(criterios_niveles, f, ensure_ascii=False, indent=2)

        logger.info(f"CSV → {csv_path}")
        logger.info(f"Markdown → {md_path}")
        logger.info(f"JSON → {json_path}")
        return csv_path, md_path, json_path
    except Exception as e:
        logger.error(f"Error exportando resultados: {e}")
        return csv_path, md_path, json_path

# ----------------------------
# CLI
# ----------------------------

def parse_args(argv: List[str]):
    import argparse
    p = argparse.ArgumentParser(description="Evaluador TFM Integrado – Finder + OneDrive + OpenAI")
    p.add_argument("--pdf", dest="ruta_tfm", help="Ruta del TFM (.pdf/.docx)")
    p.add_argument("--rubrica", dest="ruta_rubrica", help="Ruta de la rúbrica (.xlsx/.csv/.json)")
    p.add_argument("--instrucciones", dest="ruta_md", help="Ruta .md con instrucciones ultraestrictas")
    p.add_argument("--modelo", dest="modelo", default=MODELO_POR_DEFECTO)
    p.add_argument("--temperatura", dest="temperatura", type=float, default=TEMPERATURA_POR_DEFECTO)
    return p.parse_args(argv)

# ----------------------------
# Main
# ----------------------------

def main(argv: List[str]) -> int:
    args = parse_args(argv)

    # Resolución de rutas (selector si faltan)
    ruta_tfm = args.ruta_tfm
    if not ruta_tfm:
        logger_tmp = configurar_logger(None)
        ruta_tfm = seleccionar_archivo(["pdf", "docx"], "Selecciona el TFM", "Elige el archivo PDF o DOCX", logger_tmp)
        if not ruta_tfm:
            print("No se seleccionó TFM. Abortando.")
            return 1
    ruta_tfm = normalize_path(os.path.abspath(os.path.expanduser(ruta_tfm)), nfc=FORZAR_NFC)

    carpeta_salida = os.path.dirname(ruta_tfm)
    logger = configurar_logger(carpeta_salida)

    ensure_hydrated(ruta_tfm, logger)

    # Rúbrica: si no se proporciona, se decide por etiquetas Finder
    ruta_rubrica = args.ruta_rubrica
    if not ruta_rubrica:
        tags = leer_etiquetas_finder(ruta_tfm, logger)
        logger.info(f"Etiquetas Finder: {tags}")
        ruta_rubrica = seleccionar_rubrica_por_etiquetas(tags, logger)
        logger.info(f"Rúbrica sugerida por etiquetas: {ruta_rubrica}")
    ruta_rubrica = normalize_path(os.path.abspath(os.path.expanduser(ruta_rubrica)), nfc=FORZAR_NFC)

    if not Path(ruta_rubrica).exists():
        logger.error(f"No existe la rúbrica: {ruta_rubrica}")
        return 1

    rubrica_df = cargar_rubrica(ruta_rubrica, logger)
    if rubrica_df is None:
        return 1

    instrucciones = cargar_instrucciones_md_opcional(RUTA_INSTRUCCIONES_MD, logger)

    texto_tfm = leer_tfm(ruta_tfm, logger)
    if not texto_tfm.strip():
        logger.error("El texto del TFM está vacío.")
        return 1

    compat, client = crear_cliente_openai(logger)

    resultados = evaluar_tfm_completo(
        compat=compat,
        client=client,
        modelo=args.modelo,
        temperatura=args.temperatura,
        rubrica_df=rubrica_df,
        texto_tfm=texto_tfm,
        instrucciones=instrucciones,
        logger=logger,
    )

    exportar_resultados(resultados, carpeta_salida, logger)
    logger.info("✅ Evaluación finalizada correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
