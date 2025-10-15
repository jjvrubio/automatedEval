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


def construir_prompt_v2(criterio: str, instrucciones_base: str, texto_tfm: str, niveles_rubrica: List[str]) -> str:
    """
    Construye el prompt para evaluar un criterio del TFM e identificar problemas específicos del contenido.
    """
    
    partes = [
        "Eres un evaluador académico experto que debe evaluar un TFM según criterios específicos de rúbrica.",
        "",
        "CRITERIO A EVALUAR:",
        criterio,
        "",
        "INSTRUCCIONES DEL EVALUADOR:",
        instrucciones_base,
        "",
        f"NIVELES VÁLIDOS PARA ESTE CRITERIO (debes elegir EXACTAMENTE uno de estos):",
    ]
    
    # Agregar cada nivel válido con claridad
    for i, nivel in enumerate(niveles_rubrica, 1):
        partes.append(f"- {nivel}")
    partes.append("- No evaluable (solo si no hay evidencia suficiente)")
    
    partes.extend([
        "",
        "REGLAS DE EVALUACIÓN:",
        "1. Debes elegir EXACTAMENTE uno de los niveles listados arriba",
        "2. Proporciona una justificación clara y específica",
        "3. Incluye al menos 2 evidencias con citas exactas del texto",
        "4. Cada evidencia debe incluir el número de página [P#]",
        "",
        "FORMATO DE RESPUESTA (JSON válido):",
        "{",
        f'  "nivel": "DEBE ser exactamente uno de: {" | ".join(niveles_rubrica)} | No evaluable",',
        '  "justificacion": "Explicación detallada de por qué se asigna este nivel",',
        '  "areas_mejora": "Recomendaciones específicas para mejorar (vacío si nivel máximo)",',
        '  "evidencias": [',
        '    {"frase": "Cita exacta del texto", "pagina": "P#"},',
        '    {"frase": "Otra cita exacta del texto", "pagina": "P#"}',
        '  ],',
        '  "problemas_contenido": [',
        '    {',
        '      "tipo": "CONTRADICCION|METODOLOGIA_POCO_CLARA|CONTENIDO_AMBIGUO|etc",',
        '      "descripcion": "Breve descripción del problema",',
        '      "fragmento1": "Texto problemático exacto",',
        '      "pagina1": "P#"',
        '    }',
        '  ]',
        '}',
        "",
        "IMPORTANTE: Responde SOLO con el JSON válido, sin texto adicional antes o después.",
        "",
        "TEXTO DEL TFM PARA EVALUAR:",
        "---",
        text_tfm_recorte(texto_tfm),
        "---",
    ])
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
    niveles_rubrica: List[str],
    logger: logging.Logger,
) -> str:
    prompt = construir_prompt_v2(criterio, instrucciones, texto_tfm, niveles_rubrica)
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
    problemas_contenido_globales: List[dict] = []  # Almacenar todos los problemas de contenido
    
    criterios = [str(c) for c in rubrica_df.iloc[:, 0].tolist()]
    
    # EXTRACCIÓN CORRECTA DE NIVELES DE LA RÚBRICA
    # En lugar de usar nombres de columnas, extraer los niveles reales del contenido
    primera_fila = rubrica_df.iloc[0]  # Usar primera fila como ejemplo
    niveles_reales = []
    
    # Detectar formato de rúbrica basado en el contenido
    for col in rubrica_df.columns[1:]:  # Saltar primera columna (criterios)
        contenido_col = str(primera_fila[col]).strip()
        if contenido_col and contenido_col.lower() not in ['nan', 'none', '']:
            # Para MUDPE: buscar "Nivel X" en el contenido
            if "Nivel" in contenido_col:
                # Extraer "Nivel 1", "Nivel 2", etc.
                if "1" in contenido_col:
                    niveles_reales.append("Nivel 1")
                elif "2" in contenido_col:
                    niveles_reales.append("Nivel 2")
                elif "3" in contenido_col:
                    niveles_reales.append("Nivel 3")
                elif "4" in contenido_col:
                    niveles_reales.append("Nivel 4")
            # Para MUGPTD: buscar términos específicos
            elif any(term in contenido_col.lower() for term in ["suspenso", "aprobado", "notable", "sobresaliente"]):
                if "suspenso" in contenido_col.lower():
                    niveles_reales.append("Suspenso (0-4)")
                elif "aprobado" in contenido_col.lower():
                    niveles_reales.append("Aprobado (5-6)")
                elif "notable" in contenido_col.lower():
                    niveles_reales.append("Notable (7-8)")
                elif "sobresaliente" in contenido_col.lower():
                    niveles_reales.append("Sobresaliente (9-10)")
            else:
                # Fallback: usar nombres de columnas
                niveles_reales.append(col)
    
    # Si no se detectaron niveles reales, usar nombres de columnas como fallback
    if not niveles_reales:
        niveles_reales = rubrica_df.columns[1:].tolist()
    
    # Debug: mostrar información detallada de la rúbrica
    logger.info(f"Columnas de la rúbrica: {list(rubrica_df.columns)}")
    logger.info(f"Criterios encontrados: {len(criterios)} criterios")
    logger.info(f"Niveles reales detectados: {niveles_reales}")
    
    # Detectar tipo de rúbrica y definir criterios a excluir
    num_criterios = len(criterios)
    if num_criterios == 8:
        # MUGPTD - 8 criterios: excluir 7 y 8 (presentación oral)
        criterios_excluir = [7, 8]
        tipo_rubrica = "MUGPTD"
    elif num_criterios in [12, 13]:
        # MUDPE - 12-13 criterios: excluir los últimos 4 (presentación oral)
        criterios_excluir = list(range(num_criterios - 3, num_criterios + 1))  # Últimos 4 criterios
        tipo_rubrica = "MUDPE"
    else:
        # Rúbrica desconocida - no excluir ningún criterio
        criterios_excluir = []
        tipo_rubrica = "DESCONOCIDA"
    
    logger.info(f"Rúbrica detectada: {tipo_rubrica} ({num_criterios} criterios)")
    logger.info(f"Criterios de presentación oral a excluir: {criterios_excluir}")

    for i, criterio in enumerate(criterios, 1):  # Enumerar desde 1 para identificar criterios
        
        # Marcar como "No evaluable" los criterios de presentación oral según la rúbrica
        if i in criterios_excluir:
            logger.info(f"⏩ Criterio {i} (presentación oral) marcado como No evaluable: {criterio}")
            resultados.append({
                "criterio": criterio,
                "nivel": "No evaluable",
                "justificacion": "Criterio de presentación oral, no evaluable desde el documento escrito.",
                "areas_mejora": "Se evaluará durante la defensa oral.",
                "evidencias": [],
                "problemas_contenido": [],
            })
            continue
            
        logger.info(f"🔄 Iniciando evaluación del criterio {i}: {criterio}")
        
        evaluacion = evaluar_criterio(
            compat=compat,
            client=client,
            modelo=modelo,
            temperatura=temperatura,
            criterio=criterio,
            instrucciones=instrucciones,
            texto_tfm=texto_tfm,
            niveles_rubrica=niveles_reales,  # Usar niveles reales detectados
            logger=logger,
        )
        
        logger.debug(f"Respuesta cruda del modelo para criterio {i}: {evaluacion}")
        
        try:
            evaluacion_json = json.loads(evaluacion)
            nivel = evaluacion_json.get("nivel", "No evaluable").strip()
            
            logger.info(f"Nivel devuelto por el modelo para '{criterio}': '{nivel}'")
            
            # Validar que el nivel esté en los niveles de la rúbrica
            if nivel not in niveles_reales and nivel != "No evaluable":
                logger.warning(f"Nivel '{nivel}' no encontrado en rúbrica para '{criterio}'. Niveles válidos: {niveles_reales}")
                nivel = "No evaluable"

            # Capturar problemas de contenido específicos
            problemas_contenido = evaluacion_json.get("problemas_contenido", [])
            if problemas_contenido:
                for problema in problemas_contenido:
                    problema['criterio_origen'] = criterio  # Añadir referencia al criterio
                problemas_contenido_globales.extend(problemas_contenido)
                logger.info(f"Identificados {len(problemas_contenido)} problemas de contenido en '{criterio}'")

            resultados.append({
                "criterio": criterio,
                "nivel": nivel,
                "justificacion": evaluacion_json.get("justificacion", ""),
                "areas_mejora": evaluacion_json.get("areas_mejora", ""),
                "evidencias": evaluacion_json.get("evidencias", []),
                "problemas_contenido": problemas_contenido,  # Incluir problemas específicos del criterio
            })
            
            logger.info(f"✅ Criterio {i} evaluado - '{criterio}': {nivel}")
            
        except json.JSONDecodeError:
            logger.error(f"Error al decodificar la evaluación para el criterio '{criterio}': {evaluacion}")
            resultados.append({
                "criterio": criterio,
                "nivel": "No evaluable",
                "justificacion": "Error al procesar la evaluación.",
                "areas_mejora": "Revisar el criterio manualmente.",
                "evidencias": [],
                "problemas_contenido": [],
            })
    
    # Añadir los problemas globales a los resultados para usar en la generación de preguntas
    logger.info(f"Total de problemas de contenido identificados: {len(problemas_contenido_globales)}")
    return resultados, problemas_contenido_globales

# ----------------------------
# Exportes
# ----------------------------

# Modificación para integrar guardar_resultados en el flujo principal

def exportar_resultados(resultados: List[dict], carpeta_salida: str, problemas_contenido: List[dict], logger: logging.Logger) -> Tuple[str, str]:
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
        guardar_resultados(resultados, md_json_base, problemas_contenido, logger)

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
        ruta_plantillas = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/plantillas_preguntas.yaml"
    
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
    Genera preguntas epistemológicamente sofisticadas basadas en análisis metodológico integral.
    """
    config = plantillas.get("configuracion", {})
    num_preguntas = config.get("numero_preguntas", 3)
    criterios_evaluacion = plantillas.get("criterios_evaluacion", {})
    patrones_problemas = plantillas.get("patrones_problemas", {})
    instrucciones = plantillas.get("instrucciones_modelo", {})
    
    # DETECTAR FORMATO DE RÚBRICA AUTOMÁTICAMENTE
    formato_rubrica = detectar_formato_rubrica(resultados)
    logger.info(f"Formato de rúbrica detectado: {formato_rubrica.upper()}")
    
    preguntas = []
    logger.info("Iniciando análisis epistemológico para generación de preguntas expertas")
    
    # FASE 1: ANÁLISIS PRELIMINAR GLOBAL según instrucciones
    analisis_global = realizar_analisis_preliminar(resultados, formato_rubrica, logger)
    
    # FASE 2: IDENTIFICACIÓN DE PATRONES PROBLEMÁTICOS
    problemas_detectados = identificar_patrones_problemas(resultados, patrones_problemas, formato_rubrica, logger)
    
    # FASE 3: GENERACIÓN DE PREGUNTAS ESPECÍFICAS POR SECCIÓN
    secciones_criticas = determinar_secciones_criticas(resultados, criterios_evaluacion, formato_rubrica)
    
    for seccion, criterios in secciones_criticas.items():
        if len(preguntas) >= num_preguntas:
            break
            
        seccion_config = criterios_evaluacion.get(seccion, {})
        plantillas_seccion = seccion_config.get("plantillas_pregunta", [])
        
        if plantillas_seccion and criterios:
            # Seleccionar plantilla más relevante para los problemas detectados
            plantilla_seleccionada = seleccionar_plantilla_por_problemas(
                plantillas_seccion, problemas_detectados, criterios
            )
            
            if plantilla_seleccionada:
                # Contextualizar la plantilla con datos específicos del TFM
                pregunta_contextualizada = contextualizar_pregunta_experta(
                    plantilla_seleccionada, criterios, analisis_global
                )
                preguntas.append(pregunta_contextualizada)
                logger.info(f"Generada pregunta experta para sección: {seccion}")
    
    # FASE 4: COMPLETAR CON PREGUNTAS DE PATRONES ESPECÍFICOS
    while len(preguntas) < num_preguntas and problemas_detectados:
        patron_problema = problemas_detectados.pop(0)
        pregunta_patron = generar_pregunta_por_patron(patron_problema, resultados)
        if pregunta_patron and pregunta_patron not in preguntas:
            preguntas.append(pregunta_patron)
    
    logger.info(f"Generadas {len(preguntas)} preguntas con rigor epistemológico")
    return preguntas[:num_preguntas]

def realizar_analisis_preliminar(resultados: List[Dict[str, Any]], formato_rubrica: str, logger: logging.Logger) -> Dict[str, Any]:
    """
    Realiza análisis global de cadena de pensamiento y coherencia metodológica.
    """
    analisis = {
        "cadena_pensamiento": {},
        "secuencia_metodologica": {},
        "rigor_aplicacion": {},
        "problemas_detectados": []
    }
    
    # Analizar coherencia en objetivos, metodología y conclusiones
    criterios_objetivos = [r for r in resultados if "objetivo" in r.get("criterio", "").lower()]
    criterios_metodologia = [r for r in resultados if any(term in r.get("criterio", "").lower() 
                           for term in ["metodolog", "método", "diseño", "desarrollo", "marco teórico"])]
    
    # Verificar problemas en objetivos
    if criterios_objetivos:
        for crit in criterios_objetivos:
            nivel = crit.get("nivel", "")
            if es_nivel_problematico(nivel, formato_rubrica) or nivel_es_mejorable(nivel, formato_rubrica):
                analisis["problemas_detectados"].append("objetivos_debiles")
    
    # Verificar problemas metodológicos
    if criterios_metodologia:
        for crit in criterios_metodologia:
            nivel = crit.get("nivel", "")
            if es_nivel_problematico(nivel, formato_rubrica):
                analisis["problemas_detectados"].append("metodologia_deficiente")
    
    # Verificar problemas estructurales generales
    problemas_graves = len([r for r in resultados if es_nivel_problematico(r.get("nivel", ""), formato_rubrica)])
    if problemas_graves >= 1:
        analisis["problemas_detectados"].append("problemas_estructurales")
    
    logger.debug(f"Análisis preliminar detectó: {len(analisis['problemas_detectados'])} problemas")
    return analisis

def identificar_patrones_problemas(resultados: List[Dict[str, Any]], patrones: Dict[str, Any], formato_rubrica: str, logger: logging.Logger) -> List[str]:
    """
    Identifica patrones específicos de problemas metodológicos.
    """
    problemas_encontrados = []
    
    # Verificar desarticulación lógica - buscar niveles bajos o suspensos
    niveles_bajos = len([r for r in resultados if es_nivel_problematico(r.get("nivel", ""), formato_rubrica)])
    if niveles_bajos >= 1:  # Con cualquier suspenso ya hay problemas
        problemas_encontrados.append("desarticulacion_logica")
    
    # Verificar problemas estructurales específicos
    criterios_estructura = [r for r in resultados if any(term in r.get("criterio", "").lower() 
                          for term in ["estructura", "apartados", "organiz"])]
    if criterios_estructura and any(es_nivel_problematico(r.get("nivel", ""), formato_rubrica) for r in criterios_estructura):
        problemas_encontrados.append("secuencia_metodologica_incorrecta")
    
    # Verificar problemas de desarrollo y contribución
    criterios_desarrollo = [r for r in resultados if any(term in r.get("criterio", "").lower() 
                          for term in ["desarrollo", "contribución", "marco teórico"])]
    if criterios_desarrollo and any(nivel_es_mejorable(r.get("nivel", ""), formato_rubrica) for r in criterios_desarrollo):
        problemas_encontrados.append("superficialidad_herramientas")
    
    # Verificar problemas de coherencia entre objetivos y desarrollo
    criterios_coherencia = [r for r in resultados if any(term in r.get("criterio", "").lower() 
                          for term in ["relación", "objetivos", "coherencia", "alcance"])]
    if criterios_coherencia and any(nivel_es_mejorable(r.get("nivel", ""), formato_rubrica) for r in criterios_coherencia):
        problemas_encontrados.append("incongruencia_cuantitativa")
    
    logger.info(f"Patrones problemáticos identificados: {problemas_encontrados}")
    return problemas_encontrados

def determinar_secciones_criticas(resultados: List[Dict[str, Any]], criterios_evaluacion: Dict[str, Any], formato_rubrica: str) -> Dict[str, List[Dict]]:
    """
    Determina qué secciones requieren preguntas específicas basadas en problemas detectados.
    """
    secciones = {}
    
    # Mapear criterios a secciones
    for resultado in resultados:
        criterio_texto = resultado.get("criterio", "").lower()
        nivel = resultado.get("nivel", "")
        
        # Solo considerar criterios problemáticos o mejorables
        if not (es_nivel_problematico(nivel, formato_rubrica) or nivel_es_mejorable(nivel, formato_rubrica)):
            continue
            
        if any(term in criterio_texto for term in ["resumen", "abstract"]):
            secciones.setdefault("resumen", []).append(resultado)
        elif any(term in criterio_texto for term in ["justificación", "justificacion", "marco teórico", "referencias"]):
            secciones.setdefault("justificacion", []).append(resultado)
        elif any(term in criterio_texto for term in ["objetivo", "relación", "coherencia"]):
            secciones.setdefault("objetivos", []).append(resultado)
        elif any(term in criterio_texto for term in ["desarrollo", "contribución", "estructura", "apartados"]):
            secciones.setdefault("analisis_estrategico", []).append(resultado)
        else:
            # Categoría general para otros criterios problemáticos
            secciones.setdefault("general", []).append(resultado)
    
    return secciones

def detectar_formato_rubrica(resultados: List[Dict[str, Any]]) -> str:
    """
    Detecta automáticamente el formato de niveles usado en la rúbrica.
    Retorna: 'mudpe' para formato Nivel 1-4, 'mugptd' para formato Suspenso/Aprobado
    """
    if not resultados:
        return 'mugptd'  # Por defecto
    
    # Analizar los niveles presentes
    niveles_encontrados = [r.get("nivel", "") for r in resultados if r.get("nivel")]
    texto_niveles = " ".join(niveles_encontrados).lower()
    
    # Detectar formato MUDPE (Nivel 1, Nivel 2, etc.)
    if any(patron in texto_niveles for patron in ["nivel 1", "nivel 2", "nivel 3", "nivel 4"]):
        return 'mudpe'
    
    # Detectar formato MUGPTD (Suspenso, Aprobado, etc.)
    if any(patron in texto_niveles for patron in ["suspenso", "aprobado", "notable", "sobresaliente"]):
        return 'mugptd'
    
    # Por defecto, asumir MUGPTD
    return 'mugptd'

def es_nivel_problematico(nivel: str, formato_rubrica: str = None) -> bool:
    """Determina si un nivel indica problemas serios según el formato de rúbrica."""
    nivel_lower = nivel.lower()
    
    if formato_rubrica == 'mudpe':
        # Formato MUDPE: Nivel 1 y Nivel 2 son problemáticos
        return any(indicador in nivel_lower for indicador in [
            "nivel 1", "nivel 2", "n1", "n2", "no evaluable"
        ])
    else:
        # Formato MUGPTD: Suspenso es problemático
        return any(indicador in nivel_lower for indicador in [
            "suspenso", "0-4", "insuficiente", "no evaluable"
        ])

def nivel_es_mejorable(nivel: str, formato_rubrica: str = None) -> bool:
    """Determina si un nivel indica que necesita mejoras según el formato de rúbrica."""
    nivel_lower = nivel.lower()
    
    if formato_rubrica == 'mudpe':
        # Formato MUDPE: Nivel 1, 2 y 3 son mejorables
        return any(indicador in nivel_lower for indicador in [
            "nivel 1", "nivel 2", "nivel 3", "n1", "n2", "n3"
        ])
    else:
        # Formato MUGPTD: Suspenso y Aprobado son mejorables
        return any(indicador in nivel_lower for indicador in [
            "suspenso", "0-4", "aprobado (5-6)", "5-6", "aprobado"
        ])

def seleccionar_plantilla_por_problemas(plantillas: List[str], problemas: List[str], criterios: List[Dict]) -> str:
    """
    Selecciona la plantilla más adecuada según los problemas específicos detectados.
    """
    if not plantillas:
        return ""
    
    # Lógica de selección basada en problemas específicos
    if "desarticulacion_logica" in problemas:
        # Buscar plantillas que mencionen "derivación lógica" o "cadena de pensamiento"
        for plantilla in plantillas:
            if any(term in plantilla.lower() for term in ["derivación lógica", "cadena de pensamiento", "articulación"]):
                return plantilla
    
    if "secuencia_metodologica_incorrecta" in problemas:
        # Buscar plantillas sobre secuencia metodológica
        for plantilla in plantillas:
            if any(term in plantilla.lower() for term in ["secuencia", "metodológica", "pestel"]):
                return plantilla
                
    # Por defecto, seleccionar la primera plantilla disponible
    return plantillas[0] if plantillas else ""

def contextualizar_pregunta_experta(plantilla: str, criterios: List[Dict], analisis: Dict[str, Any]) -> str:
    """
    Contextualiza la plantilla con datos específicos del TFM evaluado.
    """
    # Extraer datos específicos de los criterios para llenar los placeholders
    contexto = {}
    
    for criterio in criterios:
        criterio_texto = criterio.get("criterio", "")
        justificacion = criterio.get("justificacion", "")
        evidencias = criterio.get("evidencias", [])
        
        # Extraer información específica para contextualizacion
        if evidencias:
            contexto["evidencia_especifica"] = evidencias[0].get("frase", "")[:100] + "..."
        
        contexto["nivel_detectado"] = criterio.get("nivel", "")
        contexto["problema_identificado"] = justificacion[:150] + "..." if len(justificacion) > 150 else justificacion
    
    # Aplicar contextualizacion básica
    pregunta_contextualizada = plantilla
    
    # Reemplazar placeholders específicos comunes
    replacements = {
        "{metodologias_empleadas}": "las herramientas de análisis disponibles",
        "{objetivos_especificos}": "los objetivos formulados", 
        "{problema_inicial}": "la problemática identificada",
        "{metodologia_empleada}": "la metodología seleccionada",
        "{justificacion_resumida}": "la fundamentación presentada",
        "{objetivos_enunciados}": "los objetivos establecidos",
        "{resultados_obtenidos}": "los resultados alcanzados",
        "{objetivos_planteados}": "los objetivos planteados",
        "{puntuacion_externa}": "la puntuación del análisis externo",
        "{puntuacion_interna}": "la puntuación del análisis interno",
        "{matriz_dafo}": "la matriz DAFO resultante",
        "{evaluacion_vrio}": "la evaluación VRIO realizada"
    }
    
    # Aplicar reemplazos de placeholders
    for placeholder, valor in replacements.items():
        pregunta_contextualizada = pregunta_contextualizada.replace(placeholder, valor)
    
    # Aplicar contexto específico del criterio
    for clave, valor in contexto.items():
        placeholder = "{" + clave + "}"
        if placeholder in pregunta_contextualizada:
            pregunta_contextualizada = pregunta_contextualizada.replace(placeholder, valor)
    
    return pregunta_contextualizada

def generar_pregunta_por_patron(patron: str, resultados: List[Dict[str, Any]]) -> str:
    """
    Genera pregunta específica basada en un patrón problemático identificado.
    """
    preguntas_patron = {
        "desarticulacion_logica": "**Falta de coherencia estructural**: Se observa desconexión entre la justificación del problema, los objetivos formulados y la metodología aplicada. ¿Cómo se garantiza que existe una línea argumental coherente que conecte lógicamente la identificación del problema con la formulación de objetivos y la selección metodológica?",
        
        "secuencia_metodologica_incorrecta": "**Alteración de secuencia analítica**: El análisis estratégico no sigue la secuencia metodológica prescrita (PESTEL → Porter → Competidores → MEFE → DAFO). ¿Qué fundamentación epistemológica justifica esta variación y cómo se garantiza la validez del diagnóstico estratégico resultante?",
        
        "superficialidad_herramientas": "**Aplicación superficial de herramientas**: Las herramientas de análisis se aplican de manera formal pero sin demostrar rigor metodológico en los criterios de evaluación. ¿Qué evidencia empírica sustenta las valoraciones realizadas y cómo se controló la subjetividad inherente a estas evaluaciones?"
    }
    
    return preguntas_patron.get(patron, "")
    
    logger.info(f"Generadas {len(preguntas)} preguntas con enfoque epistemológico crítico")
    return preguntas[:num_preguntas]


def mapear_problema_a_enfoque(tipo_problema: str) -> str:
    """
    Mapea tipos de problemas detectados a enfoques epistemológicos específicos.
    """
    mapeo = {
        "contradiccion": "coherencia_interna",
        "metodologia_poco_clara": "validacion_empirica", 
        "formula_sin_justificacion": "fundamentacion_teorica",
        "contenido_ambiguo": "fundamentacion_teorica",
        "datos_sin_explicacion": "validacion_empirica",
        "salto_logico": "coherencia_interna"
    }
    return mapeo.get(tipo_problema, "coherencia_interna")

# Modificación para generar dos archivos de salida: .md y .json

def guardar_resultados(resultados: List[Dict[str, Any]], ruta_base: str, problemas_contenido: List[Dict[str, Any]], logger: logging.Logger):
    """
    Guarda los resultados de la evaluación en dos archivos: .md y .json.
    """
    try:
        # Cargar plantillas de preguntas
        plantillas = cargar_plantillas_preguntas()
        
        # Generar preguntas dinámicas usando el nuevo sistema epistemológico
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
    resultados, problemas_contenido = evaluar_tfm_completo(
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
    exportar_resultados(resultados, carpeta_salida, problemas_contenido, logger)
    logger.info("✅ Evaluación finalizada correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
