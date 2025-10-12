#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador TFM – Integrado (sin parámetros, 2 rúbricas fijas)
===========================================================

Qué hace (todo en un script, sin flags ni CLI):
1) Abre **selector AppKit (NSOpenPanel)** para elegir el TFM del alumno (PDF/DOCX).
2) Intenta **hidratar** el archivo si está en OneDrive (File Provider).
3) Lee **etiquetas Finder (kMDItemUserTags)** y decide la rúbrica:
   - Si hay etiqueta **MUDPE** → usa la rúbrica MUDPE.
   - Si hay etiqueta **MGPTD** → usa la rúbrica MGPTD.
   - Si no hay etiquetas válidas o hay ambigüedad → muestra un **diálogo AppKit** para elegir entre MUDPE/MGPTD.
4) Carga la rúbrica (xlsx), extrae el texto del TFM (PDF o DOCX) y ejecuta una **evaluación por criterio con OpenAI**.
5) Genera **CSV** y **Markdown** con el informe de evaluación en la misma carpeta del TFM.

Requisitos
----------
- macOS (Apple Silicon OK) con `mdls` y (opcional) `fileproviderctl`.
- Python 3.11+ (probado con 3.11/3.12/3.13).
- Paquetes: pdfplumber, python-docx, pandas, openai>=1.0, pyobjc (AppKit).
- Variable de entorno **MI_CLAVE_API_OPENAI** (o **OPENAI_API_KEY**) con tu API key.

Rúbricas fijas
--------------
- MUDPE → /Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MUDPE.xlsx
- MGPTD → /Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MGPTD.xlsx
"""
from __future__ import annotations

import os
import sys
import json
import logging
import plistlib
import subprocess
import unicodedata
from pathlib import Path
from typing import List, Optional, Tuple

# ----------------------------
# Configuración fija (sin parámetros)
# ----------------------------
RUBRICAS_POR_ETIQUETA: dict[str, str] = {
    "MUDPE": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MUDPE.xlsx",
    "MGPTD": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MGPTD.xlsx",
}

# Instrucciones internas por defecto (sin fichero MD)
INSTRUCCIONES_ULTRAESTRICTAS = (
    "Eres un evaluador académico experto en TFMs de UNIR. Modelo ultraestricto: "
    "asigna nivel 4 solo si todos los elementos esenciales se cumplen con coherencia profunda. "
    "Sigue exactamente el orden y redacción de los criterios de la rúbrica aportada. "
    "Para cada criterio devuelve: Nivel (1-4 o 'No evaluable'), Justificación estructurada y Áreas de mejora."
)

MODELO_POR_DEFECTO = "gpt-4o-mini"
TEMPERATURA_POR_DEFECTO = 0.0
FORZAR_NFC = True
ONEDRIVE_HINTS = ("OneDrive", "OneDrive - ")

# ----------------------------
# Logging
# ----------------------------

def configurar_logger(path_salida: Optional[str]) -> logging.Logger:
    logger = logging.getLogger("evaluador_tfm_integrado_sin_cli")
    logger.setLevel(logging.INFO)
    # Evitar handlers duplicados si se reimporta
    if logger.handlers:
        return logger
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
# Selector de archivo (AppKit obligatorio)
# ----------------------------

def seleccionar_archivo_pdf_docx(logger: logging.Logger) -> Optional[str]:
    try:
        from AppKit import NSApplication, NSOpenPanel  # type: ignore
        NSApp = NSApplication.sharedApplication()
        NSApp.activateIgnoringOtherApps_(True)
        panel = NSOpenPanel.openPanel()
        panel.setCanChooseFiles_(True)
        panel.setCanChooseDirectories_(False)
        panel.setAllowsMultipleSelection_(False)
        panel.setAllowedFileTypes_(["pdf", "docx"])  # TFM
        panel.setTitle_("Selecciona el TFM del alumno")
        panel.setMessage_("Elige el archivo PDF o DOCX del TFM")
        if panel.runModal() == 1:
            path = panel.URLs()[0].path()
            return normalize_path(path, nfc=FORZAR_NFC)
    except Exception as e:
        logger.error(f"El selector GUI de AppKit es requerido: {e}")
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


def seleccionar_rubrica_por_etiquetas(tags: List[str]) -> Optional[str]:
    # Prioridad: si hay MUDPE, luego MGPTD (o al revés). Aquí dejamos prioridad natural.
    for key in ("MUDPE", "MGPTD"):
        if key in tags:
            return RUBRICAS_POR_ETIQUETA[key]
    return None

# ----------------------------
# Diálogo para elegir rúbrica si no hay etiquetas
# ----------------------------

def elegir_rubrica_dialogo(logger: logging.Logger) -> Optional[str]:
    try:
        from AppKit import NSAlert, NSApplication  # type: ignore
        NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
        alert = NSAlert.alloc().init()
        alert.setMessageText_("Selecciona la rúbrica")
        alert.setInformativeText_("No se detectaron etiquetas Finder MUDPE/MGPTD o hay ambigüedad. Elige la rúbrica a aplicar.")
        alert.addButtonWithTitle_("MUDPE")  # 1000
        alert.addButtonWithTitle_("MGPTD")   # 1001
        resp = alert.runModal()
        if resp == 1000:
            return RUBRICAS_POR_ETIQUETA["MUDPE"]
        elif resp == 1001:
            return RUBRICAS_POR_ETIQUETA["MGPTD"]
    except Exception as e:
        logger.error(f"No se pudo abrir el diálogo de rúbrica: {e}")
    return None

# ----------------------------
# Carga de rúbrica (xlsx)
# ----------------------------

def cargar_rubrica_xlsx(path: str, logger: logging.Logger):
    import pandas as pd
    try:
        df = pd.read_excel(path)
        if df.shape[1] == 0:
            raise ValueError("La rúbrica está vacía")
        logger.info(f"Rúbrica cargada: {path} → {len(df)} filas / {len(df.columns)} columnas")
        return df
    except Exception as e:
        logger.error(f"Error cargando rúbrica: {e}")
        return None

# ----------------------------
# Lectura del TFM (PDF/DOCX)
# ----------------------------

def leer_tfm(path: str, logger: logging.Logger) -> str:
    ext = Path(path).suffix.lower()
    try:
        if ext == ".pdf":
            import pdfplumber
            logger.info("Extrayendo texto del PDF…")
            texto = []
            with pdfplumber.open(path) as pdf:
                for i, page in enumerate(pdf.pages):
                    try:
                        texto.append(page.extract_text() or "")
                    except Exception as e:
                        logger.warning(f"Página {i+1}: {e}")
            return "\n".join(texto)
        elif ext == ".docx":
            import docx
            logger.info("Extrayendo texto del DOCX…")
            d = docx.Document(path)
            return "\n".join(p.text for p in d.paragraphs)
        else:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()
    except Exception as e:
        logger.error(f"Error leyendo TFM: {e}")
        return ""

# ----------------------------
# OpenAI client (v1 o v0)
# ----------------------------

def crear_cliente_openai(logger: logging.Logger):
    api_key = os.getenv("MI_CLAVE_API_OPENAI") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Falta la variable de entorno MI_CLAVE_API_OPENAI u OPENAI_API_KEY")
    try:
        from openai import OpenAI  # type: ignore
        client = OpenAI(api_key=api_key)
        logger.info("OpenAI client (v1) inicializado")
        return ("v1", client)
    except Exception:
        import openai  # type: ignore
        openai.api_key = api_key
        logger.info("OpenAI client (v0.x) inicializado")
        return ("v0", openai)

# ----------------------------
# Construcción / evaluación de prompts
# ----------------------------

def text_tfm_recorte(texto: str, max_chars: int = 7000) -> str:
    if len(texto) <= max_chars:
        return texto
    head = texto[: max_chars // 2]
    tail = texto[-max_chars // 2 :]
    return head + "\n…\n" + tail


def construir_prompt(criterio: str, instrucciones_base: str, texto_tfm: str) -> str:
    return f"""
Evalúa el TFM según el criterio EXACTO de la rúbrica:

Criterio: {criterio}

Instrucciones del evaluador (ultraestricto):
{instrucciones_base}

Texto del TFM (extracto útil si es necesario):
---
{text_tfm_recorte(texto_tfm)}
---

Devuelve SOLO un bloque estructurado en español con:
- Nivel alcanzado: 1, 2, 3, 4 o "No evaluable"
- Justificación estructurada: Validación de elementos esperados
- Áreas de mejora (si no alcanza 4)
""".strip()


def evaluar_criterio(compat: str, client, modelo: str, temperatura: float, criterio: str, instrucciones: str, texto_tfm: str, logger: logging.Logger) -> str:
    prompt = construir_prompt(criterio, instrucciones, texto_tfm)
    logger.info(f"Evaluando criterio: {criterio}")
    try:
        if compat == "v1":
            resp = client.chat.completions.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura,
                max_tokens=600,
            )
            return resp.choices[0].message.content.strip()
        else:  # v0
            import openai  # type: ignore
            resp = openai.ChatCompletion.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura,
                max_tokens=600,
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

def exportar_resultados(resultados: List[dict], carpeta_salida: str, logger: logging.Logger) -> Tuple[str, str]:
    import pandas as pd
    csv_path = os.path.join(carpeta_salida, "evaluacion_tfm_resultado.csv")
    md_path = os.path.join(carpeta_salida, "evaluacion_tfm_informe.md")
    try:
        pd.DataFrame(resultados).to_csv(csv_path, index=False)
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# Informe de Evaluación TFM\n\n")
            for r in resultados:
                f.write(f"## {r['criterio']}\n\n{r['evaluacion']}\n\n")
        logger.info(f"CSV → {csv_path}")
        logger.info(f"Markdown → {md_path}")
        return csv_path, md_path
    except Exception as e:
        logger.error(f"Error exportando resultados: {e}")
        return csv_path, md_path

# ----------------------------
# Main (sin parámetros)
# ----------------------------

def main() -> int:
    # 1) Selector AppKit del TFM
    logger_tmp = configurar_logger(None)
    ruta_tfm = seleccionar_archivo_pdf_docx(logger_tmp)
    if not ruta_tfm:
        print("No se seleccionó TFM. Abortando.")
        return 1
    ruta_tfm = normalize_path(os.path.abspath(os.path.expanduser(ruta_tfm)), nfc=FORZAR_NFC)

    carpeta_salida = os.path.dirname(ruta_tfm)
    logger = configurar_logger(carpeta_salida)

    # 2) Hidratar si aplica
    ensure_hydrated(ruta_tfm, logger)

    # 3) Resolver rúbrica (etiquetas → diálogo si falta)
    tags = leer_etiquetas_finder(ruta_tfm, logger)
    logger.info(f"Etiquetas Finder: {tags}")
    ruta_rubrica = seleccionar_rubrica_por_etiquetas(tags)
    if not ruta_rubrica:
        ruta_rubrica = elegir_rubrica_dialogo(logger)
    if not ruta_rubrica:
        logger.error("No se seleccionó rúbrica. Abortando.")
        return 1

    if not Path(ruta_rubrica).exists():
        logger.error(f"No existe la rúbrica: {ruta_rubrica}")
        return 1

    # 4) Carga rúbrica + TFM
    rubrica_df = cargar_rubrica_xlsx(ruta_rubrica, logger)
    if rubrica_df is None:
        return 1

    texto_tfm = leer_tfm(ruta_tfm, logger)
    if not texto_tfm.strip():
        logger.error("El texto del TFM está vacío.")
        return 1

    # 5) OpenAI y evaluación
    compat, client = crear_cliente_openai(logger)
    resultados = evaluar_tfm_completo(
        compat=compat,
        client=client,
        modelo=MODELO_POR_DEFECTO,
        temperatura=TEMPERATURA_POR_DEFECTO,
        rubrica_df=rubrica_df,
        texto_tfm=texto_tfm,
        instrucciones=INSTRUCCIONES_ULTRAESTRICTAS,
        logger=logger,
    )

    # 6) Exportar
    exportar_resultados(resultados, carpeta_salida, logger)
    logger.info("✅ Evaluación finalizada correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
