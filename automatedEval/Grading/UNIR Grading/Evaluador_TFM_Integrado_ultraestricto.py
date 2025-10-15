#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador TFM – Integrado (sin parámetros, 2 rúbricas fijas, ultraestricto)
===========================================================================

- macOS (NSOpenPanel, AppKit) para elegir el TFM (PDF/DOCX).
- OneDrive: intenta hidratar archivos "solo en la nube".
- Detecta etiquetas Finder (kMDItemUserTags) → selecciona rúbrica (MUDPE/MUGPTD). Si no hay, muestra diálogo.
- Lee instrucciones estrictas desde fichero externo `Ultraestricto.md` (fallback a internas).
- Extrae texto con marcas de página [P#] para evidencias citables.
- Prompt ultraestricto con salida JSON (nivel/justificacion/areas_mejora/evidencias).
- Exporta CSV + Markdown en la carpeta del TFM.

Requisitos: pdfplumber, python-docx, pandas, openai>=0.28 o >=1.0, pyobjc (AppKit)
Variable de entorno: MI_CLAVE_API_OPENAI o OPENAI_API_KEY
"""
from __future__ import annotations

import os
import sys
import json
import logging
import plistlib
import subprocess
import unicodedata
import yaml
import random
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ----------------------------
# Configuración fija
# ----------------------------
RUBRICAS_POR_ETIQUETA: dict[str, str] = {
    "MUDPE": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MUDPE.xlsx",
    "MUGPTD": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MUGPTD.xlsx",
}

# Fichero externo con instrucciones estrictas
RUTA_INSTRUCCIONES_MD: str = (
    "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/Ultraestricto.md"
)

MODELO_POR_DEFECTO = "gpt-4o-mini"
TEMPERATURA_POR_DEFECTO: float = 0.0
FORZAR_NFC: bool = True
ONEDRIVE_HINTS = ("OneDrive", "OneDrive - ")

# Rúbrica por defecto si no hay etiquetas y el usuario cancela el diálogo (mantener None para forzar diálogo)
RUTA_RUBRICA_POR_DEFECTO: Optional[str] = None

# ----------------------------
# Logging
# ----------------------------

def configurar_logger(path_salida: Optional[str]) -> logging.Logger:
    logger = logging.getLogger("evaluador_tfm_integrado_sin_cli")
    logger.setLevel(logging.INFO)
    # Evita duplicados si se reimporta
    if not logger.handlers:
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
# Utilidades OneDrive / rutas
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
    except Exception:
        if is_onedrive_path(path):
            fpctl = "/usr/bin/fileproviderctl"
            if Path(fpctl).exists():
                rc, out, err = _run([fpctl, "materialize", "-p", path])
                if rc != 0:
                    logger.warning(f"fileproviderctl falló (rc={rc}). {err}")
            else:
                logger.info("'fileproviderctl' no disponible. Intento de lectura directa.")
        # intento final
        try:
            with open(path, "rb") as f:
                _ = f.read(1)
        except Exception as e2:
            logger.warning(f"No se pudo hidratar el archivo: {e2}")

# ----------------------------
# Selector AppKit (obligatorio)
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
# Etiquetas Finder (mdls)
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
                        clean.append(t.split("", 1)[0])  # sin sufijo de color
                return clean
        except Exception:
            pass
    # fallback -raw
    rc, out, err = _run(["/usr/bin/mdls", "-name", "kMDItemUserTags", "-raw", path])
    if rc == 0:
        line = out.strip().strip("()")
        if not line or line == "(null)":
            return []
        tags = []
        for raw in line.split(","):
            t = raw.strip()
            if not t:
                continue
            # Eliminar el uso de split con separador vacío
            tags.append(t)
        return tags
    logger.warning(f"No se pudieron leer etiquetas Finder: {err}")
    return []


def seleccionar_rubrica_por_etiquetas(tags: List[str]) -> Optional[str]:
    # Prioridad: MUDPE, luego MUGPTD
    if "MUDPE" in tags:
        return RUBRICAS_POR_ETIQUETA["MUDPE"]
    if "MUGPTD" in tags:
        return RUBRICAS_POR_ETIQUETA["MUGPTD"]
    return RUTA_RUBRICA_POR_DEFECTO

# ----------------------------
# Diálogo de rúbrica
# ----------------------------

def elegir_rubrica_dialogo(logger: logging.Logger) -> Optional[str]:
    try:
        from AppKit import NSAlert, NSApplication  # type: ignore
        NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
        alert = NSAlert.alloc().init()
        alert.setMessageText_("Selecciona la rúbrica")
        alert.setInformativeText_(
            "No se detectaron etiquetas Finder MUDPE/MUGPTD o hay ambigüedad. Elige la rúbrica a aplicar."
        )
        alert.addButtonWithTitle_("MUDPE")   # 1000
        alert.addButtonWithTitle_("MUGPTD")  # 1001
        resp = alert.runModal()
        if resp == 1000:
            return RUBRICAS_POR_ETIQUETA["MUDPE"]
        if resp == 1001:
            return RUBRICAS_POR_ETIQUETA["MUGPTD"]
    except Exception as e:
        logger.error(f"No se pudo abrir el diálogo de rúbrica: {e}")
    return None

# ----------------------------
# Carga rúbrica (xlsx)
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
# Lectura TFM (con marcas [P#])
# ----------------------------

def leer_tfm(path: str, logger: logging.Logger) -> str:
    """
    Extrae texto del TFM y añade marcas de página [P#] para evidencias citables.
    Soporta archivos PDF y DOCX.
    """
    from pathlib import Path
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
        elif ext == ".docx":
            import docx
            logger.info("Extrayendo texto del DOCX… (sin paginación fiable)")
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
# Instrucciones estrictas
# ----------------------------

def cargar_instrucciones_md_opcional(path_md: Optional[str], logger: logging.Logger) -> str:
    """
    Devuelve el contenido de instrucciones estrictas.
    Si existe un fichero externo (MD), se usa tal cual. Si no, se usa el bloque interno.
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


def text_tfm_recorte(texto: str, max_chars: int = 7000) -> str:
    """
    Recorta el texto del TFM para que no exceda el límite de caracteres.
    Devuelve los primeros y últimos caracteres del texto.
    """
    if len(texto) <= max_chars:
        return texto
    head = texto[: max_chars // 2]
    tail = texto[-max_chars // 2 :]
    return head + "\n…\n" + tail


def construir_prompt_v2(criterio: str, instrucciones_base: str, texto_tfm: str) -> str:
    """
    Construye el prompt para evaluar un criterio del TFM.
    """
    partes = [
        "Evalúa el TFM según el criterio EXACTO de la rúbrica, en modo ultraestricto.",
        "",
        "Criterio a evaluar:",
        criterio,
        "",
        "Guía del evaluador:",
        instrucciones_base,
        "",
        "Formato de salida (JSON estricto, sin texto adicional):",
        '{ "nivel": "1|2|3|4|No evaluable", "justificacion": "texto", "areas_mejora": "texto o vacio si nivel=4", "evidencias": [{"frase": "cita breve", "pagina": "P#"}] }',
        "",
        "Reglas de evidencias: incluye al menos 2 evidencias literales del TFM con su etiqueta de página [P#]. Si no puedes, responde con nivel=\"No evaluable\".",
        "",
        "Texto del TFM (con marcas de página [P#]):",
        "---",
        text_tfm_recorte(texto_tfm),
        "---",
    ]
    return "\n".join(partes) + "\n"


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


def evaluar_criterio(
    compat: str,
    client,
    modelo: str,
    temperatura: float,
    criterio: str,
    instrucciones: str,
    texto_tfm: str,
    logger: logging.Logger,
) -> str:
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
            return (resp.choices[0].message.content or "").strip()
        else:  # v0
            import openai  # type: ignore
            resp = openai.ChatCompletion.create(
                model=modelo,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperatura,
                max_tokens=900,
            )
            return (resp["choices"][0]["message"]["content"] or "").strip()
    except Exception as e:
        logger.error(f"Error del modelo en criterio '{criterio}': {e}")
        return "{\"nivel\": \"No evaluable\", \"justificacion\": \"Error del modelo\", \"areas_mejora\": \"Reintentar\", \"evidencias\": []}"


# Ajuste para descomponer la evaluación y extraer las claves necesarias

def evaluar_tfm_completo(
    compat: str,
    client,
    modelo: str,
    temperatura: float,
    rubrica_df,
    texto_tfm: str,
    instrucciones: str,
    logger: logging.Logger,
):
    resultados: List[dict] = []
    # Criterios típicamente no automatizables (si aparecen):
    excluir = {"presentación", "exposición", "comunicación", "tribunal", "formato de la presentación"}
    criterios = [str(c) for c in rubrica_df.iloc[:, 0].tolist()]
    niveles = rubrica_df.columns[1:].tolist()  # Asumimos que las columnas después de la primera son los niveles

    for criterio in criterios:
        low = criterio.lower()
        if any(p in low for p in excluir):
            logger.info(f"⏩ Criterio excluido: {criterio}")
            continue
        evaluacion = evaluar_criterio(
            compat=compat,
            client=client,
            modelo=modelo,
            temperatura=temperatura,
            criterio=criterio,
            instrucciones=instrucciones,
            texto_tfm=texto_tfm,
            logger=logger,
        )
        try:
            evaluacion_json = json.loads(evaluacion)
            nivel = evaluacion_json.get("nivel", "No evaluable")
            
            # Normalizar niveles para comparación (asegurando que comiencen con 'N')
            niveles_normalizados = [n.strip() for n in niveles]
            nivel = evaluacion_json.get("nivel", "No evaluable").strip()

            # Asegurar que el nivel devuelto comienza con 'N'
            if not nivel.startswith("N"):
                logger.warning(f"Nivel '{nivel}' no válido para el criterio '{criterio}'.")
                nivel = "No evaluable"

            # Excluir criterios relacionados con la exposición del alumno
            if "exposición" in criterio.lower():
                logger.info(f"⏩ Criterio relacionado con exposición excluido: {criterio}")
                continue

            resultados.append({
                "criterio": criterio,
                "nivel": nivel,
                "justificacion": evaluacion_json.get("justificacion", ""),
                "areas_mejora": evaluacion_json.get("areas_mejora", ""),
                "evidencias": evaluacion_json.get("evidencias", []),
            })
        except json.JSONDecodeError:
            logger.error(f"Error al decodificar la evaluación para el criterio '{criterio}': {evaluacion}")
            resultados.append({
                "criterio": criterio,
                "nivel": "No evaluable",
                "justificacion": "Error al procesar la evaluación.",
                "areas_mejora": "Revisar el criterio manualmente.",
                "evidencias": [],
            })
    return resultados

# ----------------------------
# Exportes
# ----------------------------

# Modificación para integrar guardar_resultados en el flujo principal

def exportar_resultados(resultados: List[dict], carpeta_salida: str, logger: logging.Logger) -> Tuple[str, str]:
    """
    Exporta los resultados en formato CSV, Markdown y JSON.
    """
    import pandas as pd
    csv_path = os.path.join(carpeta_salida, "evaluacion_tfm_resultado.csv")
    md_json_base = os.path.join(carpeta_salida, "evaluacion_tfm_informe")
    try:
        # Exportar a CSV
        pd.DataFrame(resultados).to_csv(csv_path, index=False)
        logger.info(f"CSV → {csv_path}")

        # Exportar a Markdown y JSON
        guardar_resultados(resultados, md_json_base, logger)

        return csv_path, f"{md_json_base}.md"
    except Exception as e:
        logger.error(f"Error exportando resultados: {e}")
        return csv_path, f"{md_json_base}.md"


# ----------------------------
# Generación de preguntas dinámicas
# ----------------------------

def cargar_plantillas_preguntas(ruta_plantillas: Optional[str] = None) -> Dict[str, Any]:
    """
    Carga las plantillas de preguntas desde un archivo YAML.
    """
    if ruta_plantillas is None:
        ruta_plantillas = os.path.join(os.path.dirname(__file__), "plantillas_preguntas.yaml")
    
    try:
        with open(ruta_plantillas, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        # Fallback a plantillas por defecto
        return {
            "configuracion": {"numero_preguntas": 3, "criterios_minimos": 2},
            "plantillas_preguntas": {
                "nivel_bajo": [
                    "¿Podría explicar con mayor detalle cómo aborda el aspecto de '{criterio}' en su trabajo?",
                    "¿Qué evidencias adicionales podría proporcionar para fortalecer el desarrollo de '{criterio}'?",
                    "¿Cómo podría mejorar la argumentación relacionada con '{criterio}' para hacerla más sólida?"
                ],
                "generales": [
                    "¿Qué aspectos de su metodología considera que podrían clarificarse para mejorar la comprensión del trabajo?",
                    "¿Cómo podría fortalecer la conexión entre los objetivos planteados y los resultados obtenidos?",
                    "¿Qué evidencias adicionales considera que serían más convincentes para apoyar sus conclusiones?"
                ]
            }
        }

def generar_preguntas_dinamicas(resultados: List[Dict[str, Any]], plantillas: Dict[str, Any], logger: logging.Logger) -> List[str]:
    """
    Genera preguntas dinámicas basadas en los resultados de la evaluación.
    """
    config = plantillas.get("configuracion", {})
    num_preguntas = config.get("numero_preguntas", 3)
    plantillas_preguntas = plantillas.get("plantillas_preguntas", {})
    
    preguntas = []
    criterios_problematicos = []
    
    # Identificar criterios con problemas (nivel bajo o no evaluable)
    for resultado in resultados:
        nivel = resultado.get("nivel", "").strip()
        criterio = resultado.get("criterio", "")
        
        if nivel in ["N1", "N2"] or "1" in nivel or "2" in nivel:
            criterios_problematicos.append(("nivel_bajo", criterio))
        elif nivel == "No evaluable":
            criterios_problematicos.append(("no_evaluable", criterio))
    
    # Generar preguntas específicas para criterios problemáticos
    for tipo_problema, criterio in criterios_problematicos[:num_preguntas]:
        plantillas_tipo = plantillas_preguntas.get(tipo_problema, [])
        if plantillas_tipo:
            plantilla = random.choice(plantillas_tipo)
            pregunta = plantilla.format(criterio=criterio)
            preguntas.append(pregunta)
    
    # Completar con preguntas generales si es necesario
    while len(preguntas) < num_preguntas:
        plantillas_generales = plantillas_preguntas.get("generales", [])
        if plantillas_generales:
            pregunta = random.choice(plantillas_generales)
            if pregunta not in preguntas:
                preguntas.append(pregunta)
            else:
                # Si ya tenemos esa pregunta, intentar con otra
                intentos = 0
                while pregunta in preguntas and intentos < 10:
                    pregunta = random.choice(plantillas_generales)
                    intentos += 1
                if pregunta not in preguntas:
                    preguntas.append(pregunta)
                else:
                    break
        else:
            break
    
    logger.info(f"Generadas {len(preguntas)} preguntas dinámicas")
    return preguntas[:num_preguntas]

# Modificación para generar dos archivos de salida: .md y .json

def guardar_resultados(resultados: List[Dict[str, Any]], ruta_base: str, logger: logging.Logger):
    """
    Guarda los resultados de la evaluación en dos archivos: .md y .json.
    """
    try:
        # Cargar plantillas de preguntas
        plantillas = cargar_plantillas_preguntas()
        
        # Generar preguntas dinámicas
        preguntas = generar_preguntas_dinamicas(resultados, plantillas, logger)
        
        # Generar archivo .md
        ruta_md = f"{ruta_base}.md"
        with open(ruta_md, "w", encoding="utf-8") as f_md:
            f_md.write("# Informe de Evaluación TFM\n\n")
            for criterio in resultados:
                f_md.write(f"## {criterio['criterio']}\n\n")
                f_md.write(f"- **Nivel alcanzado**: {criterio['nivel']}\n")
                f_md.write(f"- **Justificación**: {criterio['justificacion']}\n")
                f_md.write("- **Evidencias**:\n")
                for evidencia in criterio['evidencias']:
                    f_md.write(f"  - {evidencia['frase']} (Página: {evidencia['pagina']})\n")
                f_md.write(f"- **Áreas de mejora**: {criterio['areas_mejora'] or 'Ninguna'}\n\n")

            # Tabla de evaluación
            f_md.write("## Tabla de Evaluación\n\n")
            f_md.write("| Criterio | Nivel |\n")
            f_md.write("|----------|-------|\n")
            for criterio in resultados:
                f_md.write(f"| {criterio['criterio']} | {criterio['nivel']} |\n")

            # Preguntas dinámicas sobre aspectos menos claros
            f_md.write("\n## Preguntas sobre aspectos menos claros\n\n")
            for i, pregunta in enumerate(preguntas, 1):
                f_md.write(f"{i}. {pregunta}\n")

        logger.info(f"Resultados guardados en {ruta_md}")

        # Generar archivo .json
        ruta_json = f"{ruta_base}.json"
        with open(ruta_json, "w", encoding="utf-8") as f_json:
            json.dump(
                [{"criterio": c["criterio"], "nivel": c["nivel"]} for c in resultados],
                f_json,
                ensure_ascii=False,
                indent=4,
            )
        logger.info(f"Resultados guardados en {ruta_json}")

    except Exception as e:
        logger.error(f"Error al guardar los resultados: {e}")

# ----------------------------
# Main
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

    instrucciones = cargar_instrucciones_md_opcional(RUTA_INSTRUCCIONES_MD, logger)

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
        instrucciones=instrucciones,
        logger=logger,
    )

    # 6) Exportar
    exportar_resultados(resultados, carpeta_salida, logger)
    logger.info("✅ Evaluación finalizada correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
