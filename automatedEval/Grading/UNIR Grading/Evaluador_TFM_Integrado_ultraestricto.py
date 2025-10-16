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


def obtener_respuesta_openai(prompt: str, logger: logging.Logger) -> str:
    """
    Función para obtener respuesta de OpenAI utilizando el cliente configurado
    """
    try:
        compat, client = crear_cliente_openai(logger)
        
        if compat == "v1":
            resp = client.chat.completions.create(
                model=MODELO_POR_DEFECTO,
                messages=[{"role": "user", "content": prompt}],
                temperature=TEMPERATURA_POR_DEFECTO,
                max_tokens=1500,
            )
            return (resp.choices[0].message.content or "").strip()
        else:  # v0
            import openai  # type: ignore
            resp = openai.ChatCompletion.create(
                model=MODELO_POR_DEFECTO,
                messages=[{"role": "user", "content": prompt}],
                temperature=TEMPERATURA_POR_DEFECTO,
                max_tokens=1500,
            )
            return (resp["choices"][0]["message"]["content"] or "").strip()
    except Exception as e:
        logger.error(f"Error en obtener_respuesta_openai: {e}")
        raise e


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

def exportar_resultados(resultados: List[dict], carpeta_salida: str, problemas_contenido: List[dict], 
                       logger: logging.Logger, texto_tfm: str = "") -> Tuple[str, str]:
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

        # Exportar a Markdown y JSON con texto del TFM para preguntas específicas
        guardar_resultados(resultados, md_json_base, problemas_contenido, logger, texto_tfm)

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

def generar_preguntas_dinamicas(resultados: List[Dict[str, Any]], plantillas: Dict[str, Any], logger: logging.Logger, texto_tfm: str = "") -> List[str]:
    """
    Genera preguntas específicas mediante análisis crítico profundo del documento PDF,
    identificando inconsistencias, falta de claridad y criterios incorrectos.
    """
    config = plantillas.get("configuracion", {})
    num_preguntas = config.get("numero_preguntas", 3)
    
    if not texto_tfm or len(texto_tfm.strip()) < 100:
        logger.warning("Texto del TFM insuficiente para análisis crítico profundo")
        return generar_preguntas_respaldo(resultados, num_preguntas)
    
    logger.info("Iniciando análisis crítico profundo del documento")
    
    try:
        # FASE 1: ANÁLISIS CRÍTICO PROFUNDO CON IA
        preguntas_criticas = analizar_documento_profundamente(texto_tfm, resultados, logger)
        
        if len(preguntas_criticas) >= num_preguntas:
            logger.info(f"Generadas {len(preguntas_criticas)} preguntas mediante análisis crítico profundo")
            return preguntas_criticas[:num_preguntas]
        
        # FASE 2: RESPALDO SI EL ANÁLISIS IA FALLA
        logger.warning("Análisis IA insuficiente, completando con análisis local")
        preguntas_locales = analizar_inconsistencias_locales(texto_tfm, resultados, logger)
        
        preguntas_finales = preguntas_criticas + preguntas_locales
        return preguntas_finales[:num_preguntas]
        
    except Exception as e:
        logger.error(f"Error en análisis crítico: {e}")
        return generar_preguntas_respaldo(resultados, num_preguntas)


def analizar_documento_profundamente(texto_tfm: str, resultados: List[Dict], logger: logging.Logger) -> List[str]:
    """
    Utiliza OpenAI para analizar profundamente el documento y generar preguntas específicas
    con extractos textuales incluidos para evitar consultar páginas.
    """
    # Preparar contexto de la evaluación para el análisis
    problemas_detectados = []
    for resultado in resultados:
        if resultado.get('puntuacion', 4) <= 2:  # Solo problemas graves
            problemas_detectados.append({
                'criterio': resultado.get('criterio', ''),
                'comentario': resultado.get('comentario', ''),
                'justificacion': resultado.get('justificacion', ''),
                'evidencias': resultado.get('evidencias', [])
            })
    
    # Tomar una muestra representativa del texto (máximo 10000 caracteres para incluir más contexto)
    texto_muestra = extraer_muestra_representativa(texto_tfm, 10000)
    
    prompt_analisis = f"""
Actúa como un evaluador académico experto analizando un Trabajo Final de Máster (TFM).

DOCUMENTO A ANALIZAR:
{texto_muestra}

PROBLEMAS DETECTADOS EN LA EVALUACIÓN:
{json.dumps(problemas_detectados, indent=2, ensure_ascii=False)}

INSTRUCCIONES CRÍTICAS:
Analiza profundamente el documento y genera EXACTAMENTE 3 preguntas muy diferentes que:

1. IDENTIFIQUEN INCONSISTENCIAS ESPECÍFICAS: Contradicciones entre metodología declarada vs aplicada, datos vs conclusiones, teoría vs práctica
2. DETECTEN FALTA DE CLARIDAD: Conceptos mal definidos, argumentación confusa, conexiones lógicas débiles
3. ENCUENTREN CRITERIOS INCORRECTOS: Metodologías inadecuadas, sesgos no controlados, limitaciones no reconocidas

REQUISITOS ESENCIALES:
- Cada pregunta DEBE incluir extractos textuales ESPECÍFICOS y TÉCNICOS del documento en cursiva (*texto exacto del documento*)
- Los extractos deben contener DATOS CONCRETOS: números exactos, porcentajes, nombres técnicos, metodologías específicas
- PRIORIZAR fragmentos con cifras, ratios, métricas, nombres propios, términos técnicos especializados
- Los extractos deben ser EVIDENCIA DIRECTA del problema identificado, no descripciones generales
- Incluir MÚLTIPLES extractos específicos por pregunta para crear contexto técnico completo
- Mínimo 250 palabras por pregunta incluyendo múltiples extractos técnicos específicos

FORMATO OBLIGATORIO DE RESPUESTA:
```json
{{
  "preguntas": [
    {{
      "enfoque": "inconsistencia_metodologica|falta_claridad|criterio_incorrecto",
      "pregunta": "La pregunta completa que INCLUYE extractos del documento en cursiva *así*...",
      "extractos_utilizados": ["fragmento exacto 1", "fragmento exacto 2"],
      "datos_especificos": ["dato1", "dato2", "dato3"],
      "pagina_referencia": "XX"
    }}
  ]
}}
```

EJEMPLOS DE FORMATO ESPERADO CON EXTRACTOS TÉCNICOS ESPECÍFICOS:

EJEMPLO 1 (Datos numéricos específicos):
"El modelo TO-BE muestra *incremento en la ineficiencia del tiempo de ciclo para el subproceso 'Diseño de instrumentos de evaluación y acreditación' (CTE desciende del 32.88% en AS-IS al 29.97% en TO-BE)*, mientras que todos los otros subprocesos mejoran. El documento también indica que *la implementación de LEAN redujo desperdicios en un 15% en promedio*, pero contradictoriamente afirma que *todos los rediseños TO-BE fueron uniformemente exitosos*. ¿Cómo se justifica esta inconsistencia específica donde un subproceso empeora 2.91 puntos porcentuales mientras se declara éxito universal?"

EJEMPLO 2 (Términos técnicos específicos):
"El análisis financiero presenta *ROI del 23.5% y VAN de €2.4M calculado con WACC del 8.2%*, pero posteriormente menciona que *el análisis de sensibilidad no fue aplicado debido a limitaciones de tiempo*. Dado que el documento afirma usar *metodología Monte Carlo para modelar incertidumbre*, ¿por qué estos cálculos críticos no incorporan variabilidad en las tasas de descuento, especialmente cuando el WACC del 8.2% no refleja el perfil de riesgo del proyecto según las limitaciones reconocidas?"

REQUISITO: Usar SIEMPRE datos específicos (números exactos, nombres técnicos, metodologías concretas) en los extractos, NUNCA descripciones genéricas.
"""
    
    try:
        respuesta = obtener_respuesta_openai(prompt_analisis, logger)
        return procesar_respuesta_analisis(respuesta, logger)
    except Exception as e:
        logger.error(f"Error en análisis OpenAI: {e}")
        return []


def extraer_muestra_representativa(texto: str, max_chars: int) -> str:
    """
    Extrae una muestra representativa del documento priorizando secciones clave.
    """
    # Secciones clave a priorizar
    secciones_clave = [
        "metodología", "método", "análisis", "resultados", "conclusiones", 
        "limitaciones", "discusión", "marco teórico", "revisión", "literatura"
    ]
    
    parrafos = texto.split('\n\n')
    parrafos_priorizados = []
    parrafos_normales = []
    
    for parrafo in parrafos:
        if len(parrafo.strip()) < 50:  # Omitir párrafos muy cortos
            continue
            
        es_prioritario = any(seccion in parrafo.lower() for seccion in secciones_clave)
        if es_prioritario:
            parrafos_priorizados.append(parrafo)
        else:
            parrafos_normales.append(parrafo)
    
    # Construir muestra representativa
    muestra = ""
    
    # Añadir párrafos prioritarios primero
    for parrafo in parrafos_priorizados:
        if len(muestra) + len(parrafo) < max_chars * 0.7:  # 70% para contenido prioritario
            muestra += parrafo + "\n\n"
    
    # Añadir párrafos normales hasta completar
    for parrafo in parrafos_normales:
        if len(muestra) + len(parrafo) < max_chars:
            muestra += parrafo + "\n\n"
        else:
            break
    
    return muestra.strip()


def procesar_respuesta_analisis(respuesta: str, logger: logging.Logger) -> List[str]:
    """
    Procesa la respuesta JSON de OpenAI y extrae las preguntas con extractos integrados.
    """
    try:
        # Intentar extraer JSON de la respuesta
        if "```json" in respuesta:
            inicio = respuesta.find("```json") + 7
            fin = respuesta.find("```", inicio)
            json_texto = respuesta[inicio:fin].strip()
        else:
            json_texto = respuesta.strip()
        
        datos = json.loads(json_texto)
        preguntas_procesadas = []
        
        for item in datos.get("preguntas", []):
            pregunta = item.get("pregunta", "")
            enfoque = item.get("enfoque", "")
            extractos = item.get("extractos_utilizados", [])
            datos_especificos = item.get("datos_especificos", [])
            
            # Validar que la pregunta contenga extractos y sea sustancial
            if pregunta and len(pregunta) > 150 and ("*" in pregunta):
                preguntas_procesadas.append(pregunta)
                logger.info(f"✅ Pregunta con extractos - Enfoque: {enfoque}")
                logger.info(f"   📄 Extractos incluidos: {len(extractos)} fragmentos")
                logger.info(f"   📊 Datos específicos: {datos_especificos[:3]}")
            elif pregunta and len(pregunta) > 100:
                # Si no tiene extractos, intentar añadirlos desde el contexto
                pregunta_mejorada = mejorar_pregunta_con_extractos(pregunta, extractos, logger)
                preguntas_procesadas.append(pregunta_mejorada)
                logger.warning(f"⚠️ Pregunta mejorada post-procesamiento")
        
        return preguntas_procesadas
        
    except json.JSONDecodeError as e:
        logger.error(f"Error al procesar JSON de OpenAI: {e}")
        return extraer_preguntas_texto_plano(respuesta, logger)
    except Exception as e:
        logger.error(f"Error al procesar respuesta de análisis: {e}")
        return []


def mejorar_pregunta_con_extractos(pregunta: str, extractos: List[str], logger: logging.Logger) -> str:
    """
    Mejora una pregunta añadiendo extractos disponibles en formato de cursiva.
    """
    if not extractos:
        return pregunta
    
    # Insertar el primer extracto al inicio de la pregunta
    extracto_principal = extractos[0] if extractos else ""
    if extracto_principal and len(extracto_principal) > 10:
        pregunta_mejorada = f"El documento afirma que *{extracto_principal}*, sin embargo, {pregunta.lower()}"
        logger.info(f"✨ Pregunta mejorada con extracto integrado")
        return pregunta_mejorada
    
    return pregunta


def extraer_preguntas_texto_plano(respuesta: str, logger: logging.Logger) -> List[str]:
    """
    Extrae preguntas de texto plano si falla el parsing JSON.
    """
    preguntas = []
    lineas = respuesta.split('\n')
    pregunta_actual = ""
    
    for linea in lineas:
        linea = linea.strip()
        if '?' in linea and len(linea) > 50:
            if pregunta_actual:
                preguntas.append(pregunta_actual.strip())
            pregunta_actual = linea
        elif pregunta_actual and linea:
            pregunta_actual += " " + linea
    
    if pregunta_actual:
        preguntas.append(pregunta_actual.strip())
    
    logger.info(f"Extraídas {len(preguntas)} preguntas de texto plano")
    return preguntas[:3]


def analizar_inconsistencias_locales(texto_tfm: str, resultados: List[Dict], logger: logging.Logger) -> List[str]:
    """
    Análisis local de inconsistencias cuando OpenAI no está disponible.
    """
    preguntas_locales = []
    
    # Buscar inconsistencias numéricas con contexto
    import re
    numeros = re.findall(r'\d+(?:\.\d+)?%?', texto_tfm)
    metodologias = re.findall(r'(metodología|método|análisis|enfoque)\s+\w+', texto_tfm.lower())
    
    # Extraer fragmentos con números para incluir contexto
    fragmentos_numericos = extraer_fragmentos_con_numeros(texto_tfm, numeros[:3])
    
    if len(numeros) >= 3 and fragmentos_numericos:
        extracto_principal = fragmentos_numericos[0] if fragmentos_numericos else f"valores {numeros[0]}, {numeros[1]}, {numeros[2]}"
        pregunta_numerica = f"""El documento presenta *{extracto_principal}*, sin embargo, no se proporciona análisis de coherencia interna entre estas cifras ni validación cruzada de los cálculos. Considerando que la validez de los resultados cuantitativos depende de la consistencia metodológica en su obtención, ¿cómo se garantiza que estos valores fueron calculados bajo los mismos supuestos y criterios, y por qué no se incluye análisis de sensibilidad que evalúe el impacto de variaciones en los parámetros clave sobre la robustez de las conclusiones?"""
        preguntas_locales.append(pregunta_numerica)
    
    # Extraer fragmentos con metodologías
    fragmentos_metodologicos = extraer_fragmentos_con_metodologias(texto_tfm, metodologias[:2])
    
    if len(metodologias) >= 2 and fragmentos_metodologicos:
        extracto_metodologico = fragmentos_metodologicos[0] if fragmentos_metodologicos else f"enfoques {metodologias[0]} y {metodologias[1]}"
        pregunta_metodologica = f"""La investigación indica *{extracto_metodologico}*, pero no se explicita la justificación epistemológica para esta combinación ni se analizan las implicaciones de la triangulación metodológica. Dado que la coherencia paradigmática es fundamental en investigación rigurosa, ¿cómo se resuelven las posibles tensiones ontológicas entre estos enfoques, y qué criterios específicos se utilizaron para determinar su compatibilidad y complementariedad en el contexto particular del estudio?"""
        preguntas_locales.append(pregunta_metodologica)
    
    # Buscar fragmentos sobre limitaciones o conclusiones categóricas
    fragmento_limitaciones = extraer_fragmento_conclusiones_categoricas(texto_tfm)
    
    pregunta_limitaciones = f"""El trabajo concluye que *{fragmento_limitaciones}*, presentando afirmaciones categóricas sin reconocimiento explícito de limitaciones metodológicas o contextuales que podrían afectar la generalización de los hallazgos. Considerando que la transparencia sobre las limitaciones es un requisito de rigor académico, ¿por qué no se discuten los posibles sesgos de confirmación, restricciones muestrales o limitaciones temporales que podrían influir en la validez externa de las conclusiones, y cómo afecta esta omisión a la credibilidad y transferibilidad científica del trabajo?"""
    preguntas_locales.append(pregunta_limitaciones)
    
    logger.info(f"Generadas {len(preguntas_locales)} preguntas locales con extractos integrados")
    return preguntas_locales


def extraer_fragmentos_con_numeros(texto: str, numeros: List[str]) -> List[str]:
    """Extrae fragmentos que contienen números específicos con contexto."""
    import re
    fragmentos = []
    for numero in numeros[:2]:  # Solo los primeros 2 para no sobrecargar
        patron = rf'.{{0,50}}{re.escape(numero)}.{{0,80}}'
        matches = re.findall(patron, texto, re.IGNORECASE)
        if matches:
            fragmento_limpio = matches[0].strip()[:120]  # Máximo 120 caracteres
            if len(fragmento_limpio) > 20:
                fragmentos.append(fragmento_limpio)
    return fragmentos


def extraer_fragmentos_con_metodologias(texto: str, metodologias: List[str]) -> List[str]:
    """Extrae fragmentos que mencionan metodologías con contexto."""
    import re
    fragmentos = []
    for metodologia in metodologias[:2]:
        if len(metodologia) > 1:  # Asegurarse de que hay contenido
            patron = rf'.{{0,50}}{re.escape(metodologia[1])}.{{0,80}}'  # metodologia[1] porque viene con el patrón completo
            matches = re.findall(patron, texto, re.IGNORECASE)
            if matches:
                fragmento_limpio = matches[0].strip()[:120]
                if len(fragmento_limpio) > 20:
                    fragmentos.append(fragmento_limpio)
    return fragmentos


def extraer_fragmento_conclusiones_categoricas(texto: str) -> str:
    """Extrae fragmento representativo de conclusiones categóricas."""
    import re
    patrones_conclusiones = [
        r'se concluye que.{10,100}',
        r'los resultados demuestran.{10,100}',
        r'se puede afirmar.{10,100}',
        r'queda demostrado.{10,100}',
        r'se evidencia que.{10,100}'
    ]
    
    for patron in patrones_conclusiones:
        matches = re.findall(patron, texto, re.IGNORECASE)
        if matches:
            fragmento = matches[0].strip()[:100]  # Máximo 100 caracteres
            if len(fragmento) > 15:
                return fragmento
    
    # Fallback genérico
    return "los hallazgos confirman la hipótesis de manera concluyente"


def buscar_extracto_en_documento(texto: str, palabras_clave: List[str], max_chars: int = 180) -> str:
    """
    Busca y extrae fragmentos TÉCNICOS ESPECÍFICOS del documento con datos concretos.
    PRIORIZA: números exactos, porcentajes, términos técnicos, metodologías específicas.
    """
    if not texto or not palabras_clave:
        return "el análisis presenta datos específicos que requieren justificación técnica"
    
    import re
    
    # Limpiar palabras clave y crear patrones de búsqueda
    palabras_limpias = []
    for palabra in palabras_clave:
        if palabra and len(str(palabra).strip()) > 2:
            palabras_limpias.append(str(palabra).strip())
    
    if not palabras_limpias:
        return "los indicadores técnicos muestran valores específicos"
    
    # PRIORIDAD 1: Buscar fragmentos con DATOS NUMÉRICOS específicos
    for palabra in palabras_limpias:
        try:
            # Buscar contexto con números alrededor de la palabra clave
            palabra_escapada = re.escape(palabra.lower())
            # Patrón ampliado para captar números y contexto técnico
            patron_numerico = rf'.{{0,80}}{palabra_escapada}.{{0,100}}\d+(?:\.\d+)?[%€$]?.{{0,50}}'
            matches = re.findall(patron_numerico, texto, re.IGNORECASE)
            
            if matches:
                fragmento = matches[0].strip()
                if len(fragmento) > 30 and any(char.isdigit() for char in fragmento):
                    if len(fragmento) > max_chars:
                        fragmento = fragmento[:max_chars] + "..."
                    return fragmento
        except Exception:
            continue
    
    # PRIORIDAD 2: Buscar fragmentos con METODOLOGÍAS Y TÉRMINOS TÉCNICOS específicos
    for palabra in palabras_limpias:
        try:
            palabra_escapada = re.escape(palabra.lower())
            # Patrón para captar metodologías y términos técnicos con contexto
            patron_tecnico = rf'.{{0,70}}{palabra_escapada}[a-záéíóúñü\s]{{0,50}}(?:del?|de\s+|con\s+|mediante\s+)[^.].{{0,80}}'
            matches = re.findall(patron_tecnico, texto, re.IGNORECASE)
            
            if matches:
                fragmento = matches[0].strip()
                if len(fragmento) > 25:
                    if len(fragmento) > max_chars:
                        fragmento = fragmento[:max_chars] + "..."
                    return fragmento
        except Exception:
            continue
    
    # PRIORIDAD 3: Fallback con búsqueda estándar pero priorizando números
    for palabra in palabras_limpias:
        try:
            palabra_escapada = re.escape(palabra.lower())
            patron = rf'.{{0,60}}{palabra_escapada}.{{0,90}}'
            matches = re.findall(patron, texto, re.IGNORECASE)
            
            if matches:
                fragmento = matches[0].strip()
                if len(fragmento) > 20:
                    if len(fragmento) > max_chars:
                        fragmento = fragmento[:max_chars] + "..."
                    return fragmento
        except Exception:
            continue
    
    # ÚLTIMO RECURSO: Buscar cualquier fragmento técnico con números
    patrones_tecnicos = [
        r'.{0,60}\d+(?:\.\d+)?%[^.]{10,80}',  # Porcentajes con contexto
        r'.{0,60}[A-Z]{2,6}[^.]{20,80}',      # Siglas técnicas con contexto  
        r'.{0,60}(?:ROI|VAN|TIR|CTE|WACC|EVA)[^.]{10,80}',  # Indicadores financieros
        r'.{0,60}(?:metodología|análisis|modelo)[^.]{20,80}'  # Términos metodológicos
    ]
    
    for patron in patrones_tecnicos:
        matches = re.findall(patron, texto, re.IGNORECASE)
        if matches:
            fragmento = matches[0].strip()[:max_chars]
            if len(fragmento) > 25:
                return fragmento
    
    # Último recurso
    return "los indicadores técnicos específicos del análisis requieren mayor justificación metodológica"


def generar_preguntas_respaldo(resultados: List[Dict], num_preguntas: int) -> List[str]:
    """
    Sistema de respaldo cuando falla el análisis profundo.
    """
    preguntas_respaldo = [
        "El trabajo presenta metodología declarada que no se alinea completamente con la implementación práctica observada. ¿Cómo se justifica esta desconexión metodológica y qué implicaciones tiene para la validez de los resultados obtenidos?",
        
        "Los resultados se presentan sin análisis suficiente de factores confusores o variables intervinientes que podrían explicar los hallazgos. ¿Por qué no se controlan estas variables y cómo afecta esta omisión a la robustez de las conclusiones?",
        
        "Las conclusiones del estudio exceden el alcance de los datos presentados y la metodología aplicada. ¿Qué fundamenta estas generalizaciones y por qué no se reconocen explícitamente las limitaciones del diseño utilizado?"
    ]
    
    return preguntas_respaldo[:num_preguntas]

def extraer_datos_especificos_tfm(texto_tfm: str, resultados: List[Dict], logger: logging.Logger) -> Dict[str, Any]:
    """
    Extrae datos específicos, números, percentajes, nombres de metodologías,
    y evidencias concretas del texto del TFM para contextualizar preguntas.
    """
    import re
    
    datos = {
        "numeros_y_porcentajes": [],
        "metodologias_mencionadas": [],
        "nombres_herramientas": [],
        "empresas_organizaciones": [],
        "indicadores_problemas": [],
        "frases_contradictorias": [],
        "datos_temporales": [],
        "valores_financieros": [],
        "conceptos_teoricos": [],
        "variables_estudiadas": [],
        "hipotesis_planteadas": [],
        "resultados_cuantitativos": [],
        "fuentes_citadas": [],
        "limitaciones_reconocidas": [],
        "conclusiones_clave": [],
        "recomendaciones": [],
        "sectores_industrias": [],
        "terminos_tecnicos": [],
        "escalas_medicion": [],
        # NUEVOS CAMPOS FINANCIEROS ESPECÍFICOS
        "ratios_financieros": [],
        "indicadores_financieros": [],
        "metricas_rendimiento": [],
        "analisis_financiero_tipo": [],
        "proyecciones_financieras": [],
        "criterios_inversion": []
    }
    
    if not texto_tfm:
        if logger:
            logger.warning("No hay texto del TFM disponible para extracción específica")
        return datos
    
    # 1. Números, porcentajes y valores numéricos (EXPANDIDO PARA FINANZAS)
    datos["numeros_y_porcentajes"] = re.findall(r'\d+(?:\.\d+)?%', texto_tfm)
    
    # Valores financieros ampliados
    datos["valores_financieros"] = re.findall(r'[€$£¥S/]\s*\d+(?:,\d{3})*(?:\.\d+)?', texto_tfm)
    
    # Ratios financieros específicos
    ratios_pattern = r'(?:ratio|índice|coeficiente)\s+(?:de\s+)?([a-záéíóúñü\s]+?):\s*(\d+(?:\.\d+)?)'
    ratios_encontrados = re.findall(ratios_pattern, texto_tfm, re.IGNORECASE)
    datos["ratios_financieros"] = [f"{ratio.strip()}: {valor}" for ratio, valor in ratios_encontrados]
    
    # Indicadores financieros clave
    indicadores_financieros = [
        r'ROI[:=]\s*(\d+(?:\.\d+)?%?)',
        r'VAN[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
        r'NPV[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
        r'TIR[:=]\s*(\d+(?:\.\d+)?%)',
        r'IRR[:=]\s*(\d+(?:\.\d+)?%)',
        r'WACC[:=]\s*(\d+(?:\.\d+)?%)',
        r'EVA[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
        r'EBITDA[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
        r'payback[:=]\s*(\d+(?:\.\d+)?)\s*(?:años?|meses?)',
        r'punto de equilibrio[:=]\s*(\d+(?:,\d{3})*)',
        r'break\s*even[:=]\s*(\d+(?:,\d{3})*)'
    ]
    
    datos["indicadores_financieros"] = []
    for patron in indicadores_financieros:
        matches = re.findall(patron, texto_tfm, re.IGNORECASE)
        datos["indicadores_financieros"].extend(matches)
    
    datos["resultados_cuantitativos"] = re.findall(r'\d+(?:\.\d+)?\s*(?:puntos|grados|unidades|casos|participantes|muestras)', texto_tfm, re.IGNORECASE)
    datos["datos_temporales"] = re.findall(r'\b(?:20\d{2}|2\d{3})\b', texto_tfm)
    
    # 2. Metodologías y herramientas (ampliado para CUALQUIER DOMINIO)
    metodologias_amplias = [
        # Estratégicas
        'PESTEL', 'PORTER', 'DAFO', 'SWOT', 'VRIO', 'CANVAS', 'BALANCED SCORECARD',
        'MEFE', 'MEFI', 'MATRIZ BCG', 'CINCO FUERZAS', 'CADENA DE VALOR',
        'CORE COMPETENCE', 'BENCHMARKING', 'ANALISIS DE COMPETIDORES',
        # Financieras y Económicas
        'ROI', 'VAN', 'NPV', 'TIR', 'IRR', 'PAYBACK', 'EVA', 'EBITDA', 'WACC',
        'RATIO DE LIQUIDEZ', 'RATIO DE SOLVENCIA', 'RATIO DE RENTABILIDAD',
        'ANALISIS VERTICAL', 'ANALISIS HORIZONTAL', 'DUPONT', 'Z-SCORE',
        'CAPM', 'BETA', 'COEFICIENTE DE VARIACION', 'ANALISIS DE SENSIBILIDAD',
        'MONTE CARLO', 'ARBOL DE DECISION', 'VALOR PRESENTE NETO', 'TASA INTERNA',
        'FLUJO DE CAJA', 'CASH FLOW', 'PUNTO DE EQUILIBRIO', 'BREAK EVEN',
        'ANALISIS COSTO-BENEFICIO', 'ABC COSTING', 'MARGEN CONTRIBUCION',
        # Operacionales y Mejora
        'LEAN', 'SIX SIGMA', 'SCRUM', 'KANBAN', 'ISHIKAWA', 'KAIZEN',
        'JUST IN TIME', 'TOC', 'TEORIA DE RESTRICCIONES', 'ANALISIS DE PARETO',
        'FMEA', 'CAUSA RAIZ', '5 PORQUES', 'MAPEO DE PROCESOS',
        # Investigación científica
        'ENCUESTA', 'ENTREVISTA', 'OBSERVACIÓN', 'FOCUS GROUP', 'DELPHI',
        'ANÁLISIS FACTORIAL', 'REGRESIÓN', 'CORRELACIÓN', 'CHI-CUADRADO', 'ANOVA',
        'CRONBACH', 'KAISER', 'BARTLETT', 'LIKERT', 'SPSS', 'R STUDIO',
        'ANALISIS MULTIVARIANTE', 'REGRESION LOGISTICA', 'CLUSTER ANALYSIS',
        # Tecnológicas
        'MACHINE LEARNING', 'BIG DATA', 'BLOCKCHAIN', 'IOT', 'INTELIGENCIA ARTIFICIAL',
        'CRM', 'ERP', 'API', 'UX', 'UI', 'DEVOPS', 'CLOUD COMPUTING',
        'BUSINESS INTELLIGENCE', 'DATA MINING', 'ANALYTICS', 'DASHBOARD',
        # Educativas
        'CONSTRUCTIVISMO', 'CONDUCTISMO', 'COGNITIVISMO', 'BLOOM', 'KIRKPATRICK',
        'ADDIE', 'MOODLE', 'LMS', 'E-LEARNING', 'FLIPPED CLASSROOM',
        # Salud
        'ENSAYO CONTROLADO', 'PLACEBO', 'DOBLE CIEGO', 'META-ANÁLISIS', 'REVISIÓN SISTEMÁTICA',
        # Marketing
        'SEM', 'SEO', 'SOCIAL MEDIA', 'INBOUND', 'FUNNEL', 'KPI', 'CTR', 'CAC', 'LTV',
        # Psicología/Sociología
        'GROUNDED THEORY', 'FENOMENOLOGÍA', 'ETNOGRAFÍA', 'ANÁLISIS DE CONTENIDO'
    ]
    
    for metodologia in metodologias_amplias:
        if metodologia.lower() in texto_tfm.lower():
            datos["metodologias_mencionadas"].append(metodologia)
    
    # Extraer nombres de herramientas específicas
    herramientas_pattern = r'\b(?:matriz|análisis|modelo|framework|diagrama)\s+([A-Z][A-Za-z\s]+?)(?:\s|\.|\,)'
    herramientas_encontradas = re.findall(herramientas_pattern, texto_tfm, re.IGNORECASE)
    datos["nombres_herramientas"] = herramientas_encontradas[:5]  # Máximo 5
    
    # Extraer nombres de empresas u organizaciones (palabras en mayúsculas)
    empresas_pattern = r'\b[A-Z][A-Z\s&]{2,15}\b'
    empresas_encontradas = re.findall(empresas_pattern, texto_tfm)
    # Filtrar palabras comunes que no son empresas
    palabras_excluir = {'EL', 'LA', 'DE', 'CON', 'POR', 'PARA', 'QUE', 'DEL', 'LOS', 'LAS', 'UN', 'UNA'}
    datos["empresas_organizaciones"] = [emp for emp in empresas_encontradas[:5] 
                                       if len(emp.strip()) > 3 and emp.strip() not in palabras_excluir]
    
    # Buscar indicadores de problemas en justificaciones de resultados
    for resultado in resultados:
        justificacion = resultado.get("justificacion", "")
        if any(palabra in justificacion.lower() for palabra in 
               ["sin embargo", "pero", "no obstante", "contradice", "inconsistente", "falta", "ausencia"]):
            datos["indicadores_problemas"].append(justificacion[:150])
    
    # Buscar frases que indican contradicciones o problemas
    frases_problema_pattern = r'[^.]*(?:sin embargo|pero|no obstante|contradice|inconsistente|falta|ausencia)[^.]*\.'
    frases_contradictorias = re.findall(frases_problema_pattern, texto_tfm, re.IGNORECASE)
    datos["frases_contradictorias"] = frases_contradictorias[:3]  # Máximo 3
    
    # EXTRACCIONES AMPLIADAS PARA CUALQUIER DOMINIO
    
    # Conceptos teóricos y marcos conceptuales
    patrones_teoricos = [
        r'teoría\s+de\s+([A-Za-záéíóúñü\s]{3,25})(?:\s|\.|\,)',
        r'modelo\s+de\s+([A-Za-záéíóúñü\s]{3,25})(?:\s|\.|\,)',
        r'enfoque\s+([A-Za-záéíóúñü\s]{3,25})(?:\s|\.|\,)',
        r'paradigma\s+([A-Za-záéíóúñü\s]{3,25})(?:\s|\.|\,)'
    ]
    for patron in patrones_teoricos:
        conceptos = re.findall(patron, texto_tfm, re.IGNORECASE)
        datos["conceptos_teoricos"].extend([c.strip() for c in conceptos if len(c.strip()) > 3])
    
    # Variables e hipótesis de investigación
    datos["variables_estudiadas"] = re.findall(r'variable\s+(?:dependiente|independiente|moderadora):\s*([^.]{3,60})', texto_tfm, re.IGNORECASE)
    datos["hipotesis_planteadas"] = re.findall(r'hipótesis\s*(?:\d+)?:\s*([^.]{10,100})', texto_tfm, re.IGNORECASE)
    
    # Resultados cuantitativos y escalas
    datos["resultados_cuantitativos"] = re.findall(r'\d+(?:\.\d+)?\s*(?:puntos|grados|unidades|casos|participantes|muestras|respuestas)', texto_tfm, re.IGNORECASE)
    datos["escalas_medicion"] = re.findall(r'escala\s+(?:de\s+)?([A-Za-záéíóúñü\s]{3,20})(?:\s|\.|\,)', texto_tfm, re.IGNORECASE)
    
    # Sectores, industrias y dominios
    sectores_pattern = r'(?:sector|industria|área|campo|ámbito|dominio)\s+(?:de\s+)?([A-Za-záéíóúñü\s]{3,25})(?:\s|\.|\,)'
    sectores = re.findall(sectores_pattern, texto_tfm, re.IGNORECASE)
    datos["sectores_industrias"] = [s.strip() for s in sectores if len(s.strip()) > 3][:5]
    
    # Fuentes citadas
    fuentes_pattern = r'\(([A-Za-záéíóúñü\s&,]{3,30}),?\s*(\d{4})\)'
    fuentes = re.findall(fuentes_pattern, texto_tfm)
    datos["fuentes_citadas"] = [f"{autor.strip()} ({año})" for autor, año in fuentes[:8]]
    
    # Limitaciones explícitas
    limitaciones_patterns = [
        r'limitaci[oó]n[^.]{5,80}\.',
        r'no se (?:pudo|puede|considera)[^.]{5,60}\.',
        r'(?:falta|ausencia) de[^.]{5,60}\.'
    ]
    for patron in limitaciones_patterns:
        limitaciones = re.findall(patron, texto_tfm, re.IGNORECASE)
        datos["limitaciones_reconocidas"].extend(limitaciones[:2])
    
    # Conclusiones y recomendaciones
    datos["conclusiones_clave"] = re.findall(r'(?:se concluye|en conclusión|finalmente)[^.]{10,80}\.', texto_tfm, re.IGNORECASE)[:3]
    datos["recomendaciones"] = re.findall(r'(?:se recomienda|recomendación)[^.]{10,80}\.', texto_tfm, re.IGNORECASE)[:3]
    
    # Términos técnicos y siglas
    terminos_tecnicos = re.findall(r'\b[A-Z][a-z]+(?:[A-Z][a-z]+)+\b', texto_tfm)  # CamelCase
    terminos_tecnicos.extend(re.findall(r'\b[A-Z]{2,6}\b', texto_tfm))  # Siglas
    datos["terminos_tecnicos"] = list(set(terminos_tecnicos))[:10]
    
    # EXTRACCIONES FINANCIERAS AVANZADAS
    
    # Tipos de análisis financiero mencionados
    tipos_analisis = [
        'análisis vertical', 'análisis horizontal', 'análisis dupont', 'análisis de ratios',
        'análisis de sensibilidad', 'análisis de escenarios', 'simulación monte carlo',
        'análisis costo-beneficio', 'flujo de caja descontado', 'análisis de riesgo'
    ]
    for tipo in tipos_analisis:
        if tipo.lower() in texto_tfm.lower():
            datos["analisis_financiero_tipo"].append(tipo)
    
    # Métricas de rendimiento específicas
    metricas_pattern = r'(?:margen|rentabilidad|rendimiento)\s+(?:de\s+)?([a-záéíóúñü\s]+?):\s*(\d+(?:\.\d+)?%?)'
    metricas = re.findall(metricas_pattern, texto_tfm, re.IGNORECASE)
    datos["metricas_rendimiento"] = [f"{metrica.strip()}: {valor}" for metrica, valor in metricas]
    
    # Proyecciones y horizontes temporales
    proyecciones_pattern = r'(?:proyección|previsión|estimación)\s+(?:a\s+)?(\d+\s*años?)'
    proyecciones = re.findall(proyecciones_pattern, texto_tfm, re.IGNORECASE)
    datos["proyecciones_financieras"] = proyecciones[:3]
    
    # Criterios de inversión y evaluación
    criterios_inversion = [
        r'criterio de (?:aceptación|rechazo):\s*([^.]{10,60})',
        r'umbral mínimo:\s*(\d+(?:\.\d+)?%?)',
        r'tasa de descuento:\s*(\d+(?:\.\d+)?%)',
        r'costo de capital:\s*(\d+(?:\.\d+)?%)',
        r'beta:\s*(\d+(?:\.\d+)?)',
        r'prima de riesgo:\s*(\d+(?:\.\d+)?%)'
    ]
    for patron in criterios_inversion:
        matches = re.findall(patron, texto_tfm, re.IGNORECASE)
        datos["criterios_inversion"].extend(matches[:2])
    
    if logger:
        logger.info(f"Extraídos datos específicos: {len(datos['numeros_y_porcentajes'])} números, "
                    f"{len(datos['metodologias_mencionadas'])} metodologías, "
                    f"{len(datos['conceptos_teoricos'])} conceptos teóricos, "
                    f"{len(datos['variables_estudiadas'])} variables, "
                    f"{len(datos['sectores_industrias'])} sectores, "
                    f"{len(datos['empresas_organizaciones'])} organizaciones") if logger else None
    
    return datos

def generar_pregunta_con_datos_especificos(criterios: List[Dict], datos_documento: Dict, 
                                         analisis_global: Dict, seccion: str, texto_tfm: str = "") -> str:
    """
    Genera una pregunta específica usando datos concretos extraídos del documento,
    con extractos textuales integrados para evitar consultar páginas.
    """
    import random
    import time
    
    # Crear semilla única para cada llamada garantizando variación
    global _contador_llamadas, _patrones_usados
    if '_contador_llamadas' not in globals():
        _contador_llamadas = 0
    if '_patrones_usados' not in globals():
        _patrones_usados = []
    _contador_llamadas += 1
    
    # Reiniciar patrones usados cada 3 llamadas para permitir reutilización
    if len(_patrones_usados) >= 3:
        _patrones_usados = []
    
    # Semilla ultra-específica incluyendo contador y microsegundos
    seed_variacion = abs(hash(str(criterios) + seccion + str(time.time_ns()) + str(_contador_llamadas))) % 10000
    random.seed(seed_variacion)
    
    # Obtener TODOS los datos específicos del documento (claves originales del sistema)
    numeros = datos_documento.get("numeros_y_porcentajes", [])
    metodologias = datos_documento.get("metodologias_mencionadas", [])
    empresas = datos_documento.get("empresas_organizaciones", [])
    problemas = datos_documento.get("indicadores_problemas", [])
    valores_financieros = datos_documento.get("valores_financieros", [])
    frases_contradictorias = datos_documento.get("frases_contradictorias", [])
    
    # NUEVOS DATOS AMPLIADOS (incluidos financieros)
    conceptos_teoricos = datos_documento.get("conceptos_teoricos", [])
    variables = datos_documento.get("variables_estudiadas", [])
    hipotesis = datos_documento.get("hipotesis_planteadas", [])
    resultados_cuantitativos = datos_documento.get("resultados_cuantitativos", [])
    fuentes_citadas = datos_documento.get("fuentes_citadas", [])
    limitaciones = datos_documento.get("limitaciones_reconocidas", [])
    conclusiones = datos_documento.get("conclusiones_clave", [])
    sectores = datos_documento.get("sectores_industrias", [])
    terminos_tecnicos = datos_documento.get("terminos_tecnicos", [])
    escalas = datos_documento.get("escalas_medicion", [])
    
    # DATOS FINANCIEROS ESPECÍFICOS
    ratios_financieros = datos_documento.get("ratios_financieros", [])
    indicadores_financieros = datos_documento.get("indicadores_financieros", [])
    metricas_rendimiento = datos_documento.get("metricas_rendimiento", [])
    analisis_financiero_tipo = datos_documento.get("analisis_financiero_tipo", [])
    proyecciones_financieras = datos_documento.get("proyecciones_financieras", [])
    criterios_inversion = datos_documento.get("criterios_inversion", [])
    
    # Función auxiliar para selección aleatoria
    def seleccionar_aleatorio(lista):
        if not lista:
            return None
        return random.choice(lista)
    
    # Obtener problema específico del criterio
    criterio_principal = criterios[0] if criterios else {}
    justificacion = criterio_principal.get("justificacion", "")
    nivel = criterio_principal.get("nivel", "")
    evidencias = criterio_principal.get("evidencias", [])
    
    # SISTEMA DE ROTACIÓN FORZADA DE PATRONES PARA EVITAR REPETICIÓN
    patrones_disponibles = []
    
    # Evaluar qué patrones son aplicables
    if variables and hipotesis and metodologias and "PATRÓN_1" not in _patrones_usados:
        patrones_disponibles.append("INVESTIGACION_CIENTIFICA")
    
    if (ratios_financieros or indicadores_financieros) and "PATRÓN_2" not in _patrones_usados:
        patrones_disponibles.append("ANALISIS_FINANCIERO")
    
    if conceptos_teoricos and fuentes_citadas and "PATRÓN_6" not in _patrones_usados:
        patrones_disponibles.append("MARCOS_TEORICOS")
    
    if terminos_tecnicos and sectores and "PATRÓN_7" not in _patrones_usados:
        patrones_disponibles.append("ANALISIS_TECNOLOGICO")
    
    if limitaciones and frases_contradictorias and "PATRÓN_9" not in _patrones_usados:
        patrones_disponibles.append("LIMITACIONES_EXPLICITAS")
    
    # Si no hay patrones disponibles o ya se usaron todos, resetear
    if not patrones_disponibles:
        _patrones_usados = []
        patrones_disponibles = ["GENERICO_VARIADO"]
    
    # Seleccionar patrón aleatoriamente de los disponibles
    patron_seleccionado = seleccionar_aleatorio(patrones_disponibles)
    _patrones_usados.append(f"PATRÓN_{patron_seleccionado}")
    
    # EJECUTAR PATRÓN SELECCIONADO CON EXTRACTOS INTEGRADOS
    if patron_seleccionado == "INVESTIGACION_CIENTIFICA":
        variable_principal = seleccionar_aleatorio(variables)[:60] if seleccionar_aleatorio(variables) else "variable principal"
        hipotesis_principal = seleccionar_aleatorio(hipotesis)[:80] if seleccionar_aleatorio(hipotesis) else "hipótesis planteada"
        metodologia_principal = seleccionar_aleatorio(metodologias) or "metodología aplicada"
        evidencia_pagina = evidencias[0].get("pagina", "N/A") if evidencias else "N/A"
        
        # Extraer fragmento específico del documento para contexto
        extracto_metodologia = buscar_extracto_en_documento(texto_tfm, [metodologia_principal, variable_principal])
        
        return f"""El documento establece *{extracto_metodologia}* planteando la hipótesis "{hipotesis_principal}" para evaluar {variable_principal} mediante {metodologia_principal} (página {evidencia_pagina}), sin embargo, {justificacion.lower()[:120]} Dado que la validez interna requiere control riguroso de variables confusoras y la validez externa depende de la representatividad muestral, ¿cómo se garantiza que las limitaciones metodológicas identificadas no comprometen la generalización de los hallazgos, y por qué no se explicitan los posibles sesgos que afectan la interpretación de los resultados?"""
    
    elif patron_seleccionado == "ANALISIS_FINANCIERO":
        ratio_principal = seleccionar_aleatorio(ratios_financieros) or "ratio financiero"
        indicador_principal = seleccionar_aleatorio(indicadores_financieros) or "indicador clave"
        evidencia_pagina = evidencias[0].get("pagina", "N/A") if evidencias else "N/A"
        
        # Extraer fragmento específico con datos financieros
        extracto_financiero = buscar_extracto_en_documento(texto_tfm, [ratio_principal, indicador_principal, "ROI", "VAN", "TIR"])
        
        # Variaciones en enfoques financieros
        enfoques_financieros = [
            "análisis de Monte Carlo o árboles de decisión para modelar la incertidumbre",
            "análisis de sensibilidad multivariable y stress testing",
            "evaluación de opciones reales y flexibilidad estratégica",
            "análisis de escenarios probabilísticos y riesgo país/sector"
        ]
        enfoque_seleccionado = seleccionar_aleatorio(enfoques_financieros)
        
        return f"""El análisis financiero muestra *{extracto_financiero}* presentando {ratio_principal} y calculando {indicador_principal} (página {evidencia_pagina}), sin embargo, {justificacion.lower()[:120]} Dado que la evaluación de proyectos de inversión requiere análisis integral que incluya {enfoque_seleccionado}, ¿por qué no se incorpora esta metodología complementaria, especialmente cuando el WACC utilizado no refleja adecuadamente el perfil de riesgo del proyecto según las limitaciones reconocidas?"""
    
    elif patron_seleccionado == "MARCOS_TEORICOS":
        concepto_principal = seleccionar_aleatorio(conceptos_teoricos) or "marco teórico aplicado"
        fuente_principal = seleccionar_aleatorio(fuentes_citadas) if fuentes_citadas else "autores citados"
        
        # Extraer fragmento del marco teórico
        extracto_teorico = buscar_extracto_en_documento(texto_tfm, [concepto_principal, "teoría", "marco teórico"])
        
        return f"""El documento establece que *{extracto_teorico}* fundamentándose en {concepto_principal} basándose en {fuente_principal}, no obstante, {justificacion.lower()[:120]} Dado que la coherencia epistemológica requiere alineación entre paradigma, teoría y metodología, ¿cómo se justifica esta aparente desconexión entre la fundamentación teórica declarada y su operacionalización práctica, y qué implicaciones tiene para la validez constructual del estudio?"""
    
    elif patron_seleccionado == "ANALISIS_TECNOLOGICO":
        termino_principal = seleccionar_aleatorio(terminos_tecnicos) or "tecnología implementada"
        sector_principal = seleccionar_aleatorio(sectores) or "sector analizado"
        
        return f"""La implementación de {termino_principal} en el {sector_principal} muestra {justificacion.lower()[:100]}, sin embargo, no se abordan aspectos críticos como escalabilidad, interoperabilidad o ciberseguridad. Considerando que las soluciones tecnológicas requieren análisis de factibilidad técnica y organizacional, ¿por qué no se evalúan las dependencias tecnológicas, los riesgos de obsolescencia o los costos de migración, especialmente cuando estos factores determinan el éxito a largo plazo?"""
    
    elif patron_seleccionado == "LIMITACIONES_EXPLICITAS":
        limitacion_principal = seleccionar_aleatorio(limitaciones)[:100] if limitaciones else "limitaciones metodológicas"
        contradiccion = seleccionar_aleatorio(frases_contradictorias)[:120] if frases_contradictorias else "afirmaciones categóricas"
        
        # Variaciones en el análisis de limitaciones
        consecuencias_variadas = [
            f"credibilidad científica y rigor académico del estudio",
            f"aplicabilidad práctica y generalización de los hallazgos",
            f"transparencia metodológica y honestidad intelectual de la investigación",
            f"validez de conclusiones y solidez de las recomendaciones propuestas",
            f"confiabilidad de los resultados y su transferibilidad contextual"
        ]
        consecuencia_seleccionada = seleccionar_aleatorio(consecuencias_variadas)
        
        enfoques_limitaciones = [
            "matizar las afirmaciones categóricas realizadas",
            "contextualizar apropiadamente las conclusiones presentadas", 
            "relativizar la generalización de los resultados obtenidos",
            "ponderar adecuadamente las implicaciones prácticas derivadas",
            "calibrar el nivel de confianza de las recomendaciones formuladas"
        ]
        enfoque_seleccionado = seleccionar_aleatorio(enfoques_limitaciones)
        
        return f"""El documento reconoce explícitamente que "{limitacion_principal}", y además presenta "{contradiccion.lower()}" Dado que la transparencia metodológica es fundamental en investigación académica, ¿por qué estas limitaciones significativas no se incorporan en las conclusiones para {enfoque_seleccionado}, y qué implicaciones tiene esta omisión para la {consecuencia_seleccionada}?"""
    
    else:  # GENERICO_VARIADO
        # Crear contexto variado usando selección aleatoria
        if resultados_cuantitativos and metodologias:
            resultado_sel = seleccionar_aleatorio(resultados_cuantitativos) or "resultados obtenidos"
            metodologia_sel = seleccionar_aleatorio(metodologias) or "metodología aplicada"
            contexto = f"los hallazgos obtenidos mediante {metodologia_sel}"
        elif sectores and conceptos_teoricos:
            sector_sel = seleccionar_aleatorio(sectores) or "sector estudiado"  
            concepto_sel = seleccionar_aleatorio(conceptos_teoricos) or "marco teórico"
            contexto = f"la aplicación de {concepto_sel} en {sector_sel}"
        elif terminos_tecnicos and empresas:
            termino_sel = seleccionar_aleatorio(terminos_tecnicos) or "tecnología analizada"
            empresa_sel = seleccionar_aleatorio(empresas) or "organización estudiada"
            contexto = f"el análisis de {termino_sel} en {empresa_sel}"
        elif valores_financieros and numeros:
            valor_sel = seleccionar_aleatorio(valores_financieros) or "valores financieros"
            numero_sel = seleccionar_aleatorio(numeros) or "datos cuantitativos"
            if valor_sel != numero_sel and valor_sel not in numero_sel and numero_sel not in valor_sel:
                contexto = f"la evaluación de {valor_sel} con {numero_sel}"
            else:
                contexto = f"la evaluación financiera de {valor_sel}"
        else:
            contextos_genericos = [
                "el análisis desarrollado",
                "la metodología aplicada", 
                "los resultados presentados",
                "el enfoque utilizado",
                "la investigación realizada"
            ]
            contexto = seleccionar_aleatorio(contextos_genericos)
        
        # Múltiples plantillas genéricas variadas
        plantillas_genericas = [
            f"El documento presenta {contexto}, pero {justificacion.lower()[:120]} Considerando los estándares académicos de rigor metodológico, ¿qué factores explican esta inconsistencia y cómo afecta a la credibilidad del estudio?",
            
            f"Aunque el documento incluye {contexto}, {justificacion.lower()[:120]} Dado que la transparencia es fundamental, ¿por qué no se abordan estas limitaciones explícitamente?",
            
            f"El análisis incorpora {contexto}, no obstante {justificacion.lower()[:120]} Considerando la consistencia académica, ¿cómo se justifica esta desconexión metodológica?",
            
            f"Si bien el trabajo contempla {contexto}, {justificacion.lower()[:120]} Dado el rigor científico requerido, ¿qué explica esta brecha analítica?",
            
            f"El estudio presenta {contexto}, sin embargo {justificacion.lower()[:120]} Considerando la validez académica, ¿por qué persisten estas inconsistencias?"
        ]
        
        pregunta_seleccionada = seleccionar_aleatorio(plantillas_genericas)
        return pregunta_seleccionada


def generar_preguntas_contextuales(datos_extraidos: Dict[str, Any], 
                                 problemas_detectados: List[str], 
                                 logger: logging.Logger,
                                 texto_tfm: str = "",
                                 num_preguntas: int = 3) -> List[str]:
    """
    Genera preguntas contextuales diversas usando datos específicos del documento
    con extractos integrados para evitar consultar páginas.
    """
    preguntas = []
    logger.info(f"Generando preguntas contextuales con {len(problemas_detectados)} problemas detectados")
    
    # Crear variaciones de problemas para evitar duplicados
    patrones_base = [
        "Inconsistencia metodológica entre enfoque declarado y aplicación práctica",
        "Limitaciones de validez no reflejadas en conclusiones categóricas", 
        "Ausencia de justificación para criterios de selección utilizados",
        "Desconexión entre fundamentación teórica y operacionalización empírica",
        "Falta de transparencia en proceso de análisis de datos",
        "Omisión de análisis de sesgos potenciales en metodología aplicada",
        "Carencia de validación externa de instrumentos utilizados",
        "Insuficiente contextualización de hallazgos en literatura existente"
    ]
    
    # Asegurar que tenemos suficientes patrones únicos
    patrones_disponibles = list(set(problemas_detectados + patrones_base))
    
    intentos = 0
    max_intentos = num_preguntas * 3  # Evitar bucle infinito
    
    while len(preguntas) < num_preguntas and patrones_disponibles and intentos < max_intentos:
        intentos += 1
        
        # Seleccionar patrón diferente en cada iteración
        if patrones_disponibles:
            patron_problema = patrones_disponibles.pop(0)
        else:
            break
            
        # Generar pregunta con datos específicos
        try:
            pregunta_patron = generar_pregunta_con_datos_especificos([], datos_extraidos, {}, patron_problema, texto_tfm)
            
            # Verificar que la pregunta es única (comparación de contenido clave)
            es_duplicada = False
            for pregunta_existente in preguntas:
                # Extraer frases clave para comparación
                palabras_clave_nueva = set(pregunta_patron.split()[:20])  # Primeras 20 palabras
                palabras_clave_existente = set(pregunta_existente.split()[:20])
                
                # Si hay más del 70% de overlap, considerarla duplicada
                overlap = len(palabras_clave_nueva.intersection(palabras_clave_existente))
                if overlap > 0.7 * min(len(palabras_clave_nueva), len(palabras_clave_existente)):
                    es_duplicada = True
                    break
            
            if not es_duplicada and pregunta_patron:
                preguntas.append(pregunta_patron)
                logger.info(f"Pregunta {len(preguntas)} generada exitosamente")
            else:
                logger.debug(f"Pregunta duplicada detectada, reintentando...")
                
        except Exception as e:
            logger.warning(f"Error generando pregunta con patrón '{patron_problema}': {e}")
            continue
    
    # Si no tenemos suficientes preguntas, generar algunas genéricas con datos diferentes
    while len(preguntas) < num_preguntas:
        try:
            # Usar datos específicos disponibles para crear preguntas genéricas diversas
            if datos_extraidos.get('numeros') and datos_extraidos.get('metodologias'):
                numero = datos_extraidos['numeros'][len(preguntas) % len(datos_extraidos['numeros'])]
                metodologia = datos_extraidos['metodologias'][len(preguntas) % len(datos_extraidos['metodologias'])]
                
                pregunta_generica = f"""Los resultados muestran {numero} utilizando {metodologia}, sin embargo, no se explicita el proceso de validación metodológica. Considerando que la robustez académica requiere transparencia en los procedimientos analíticos, ¿qué criterios específicos justifican la selección de esta metodología particular, y cómo se controlan los sesgos inherentes que podrían afectar la interpretación de estos hallazgos numéricos?"""
                
                if pregunta_generica not in preguntas:
                    preguntas.append(pregunta_generica)
            else:
                break
                
        except (IndexError, KeyError):
            break
    
    logger.info(f"Generadas {len(preguntas)} preguntas contextuales únicas")
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
    Contextualiza la plantilla con datos específicos y evidencias concretas del TFM evaluado.
    Genera preguntas con contexto específico, datos numéricos y evidencias citables.
    """
    # Extraer datos específicos y evidencias concretas de los criterios
    contexto_especifico = {}
    datos_numericos = []
    citas_evidencia = []
    problemas_detectados = []
    
    for criterio in criterios:
        justificacion = criterio.get("justificacion", "")
        evidencias = criterio.get("evidencias", [])
        nivel = criterio.get("nivel", "")
        
        # Extraer datos numéricos y porcentajes de la justificación
        import re
        numeros = re.findall(r'\d+(?:\.\d+)?%?', justificacion)
        if numeros:
            datos_numericos.extend(numeros)
        
        # Extraer citas específicas con páginas
        for evidencia in evidencias[:2]:  # Máximo 2 evidencias por criterio
            frase = evidencia.get("frase", "")
            pagina = evidencia.get("pagina", "")
            if frase and pagina:
                cita_completa = f'"{frase}" (página {pagina})'
                citas_evidencia.append(cita_completa)
        
        # Identificar contradicciones o problemas específicos
        if nivel in ["insuficiente", "deficiente"] and justificacion:
            problemas_detectados.append({
                "problema": justificacion[:200],
                "seccion": criterio.get("criterio", ""),
                "nivel": nivel
            })
    
    # Construir pregunta con contexto específico y datos concretos
    if citas_evidencia and datos_numericos and problemas_detectados:
        # ESTILO 1: Pregunta con datos numéricos específicos
        evidencia_principal = citas_evidencia[0]
        dato_principal = datos_numericos[0] if datos_numericos else "N/A"
        problema_principal = problemas_detectados[0]["problema"]
        
        pregunta_contextualizada = f"""El documento presenta {evidencia_principal}, mostrando un valor de {dato_principal} en el análisis. Sin embargo, se detecta que {problema_principal.lower()}. Dado que este tipo de inconsistencias afectan la validez metodológica del estudio, ¿por qué no se abordan estas contradicciones explícitamente en el texto, y cómo afecta esto a la robustez de las conclusiones presentadas?"""
        
    elif citas_evidencia and problemas_detectados:
        # ESTILO 2: Pregunta basada en contradicciones específicas
        evidencia_principal = citas_evidencia[0]
        problema_principal = problemas_detectados[0]["problema"]
        seccion_problema = problemas_detectados[0]["seccion"]
        
        pregunta_contextualizada = f"""La sección "{seccion_problema}" muestra {evidencia_principal}, pero el análisis revela que {problema_principal.lower()}. Considerando que la coherencia metodológica es fundamental en investigación académica, ¿qué justificación epistemológica sustenta esta aparente discrepancia, y por qué no se reconocen estas limitaciones en el propio documento?"""
        
    elif datos_numericos and problemas_detectados:
        # ESTILO 3: Pregunta enfocada en análisis cuantitativo
        dato_principal = datos_numericos[0] if datos_numericos else "los valores presentados"
        problema_principal = problemas_detectados[0]["problema"]
        
        pregunta_contextualizada = f"""El análisis presenta {dato_principal} como resultado clave, sin embargo, se observa que {problema_principal.lower()}. Dado que la fundamentación cuantitativa requiere transparencia metodológica, ¿por qué no se explicitan los criterios de cálculo y las fuentes de estos datos, especialmente cuando su validez es cuestionable?"""
        
    else:
        # FALLBACK: Usar plantilla básica con mejora contextual
        problema_general = "se identifican inconsistencias metodológicas significativas"
        if problemas_detectados:
            problema_general = problemas_detectados[0]["problema"][:150]
        
        pregunta_contextualizada = f"""El documento muestra {problema_general.lower()}, lo cual plantea interrogantes sobre la rigurosidad del enfoque metodológico empleado. ¿Cómo se justifica esta aparente debilidad en el marco de las exigencias académicas esperadas para un trabajo de fin de máster?"""
    
    return pregunta_contextualizada

def generar_pregunta_por_patron(patron: str, resultados: List[Dict[str, Any]]) -> str:
    """
    Genera pregunta específica basada en un patrón problemático identificado,
    extrayendo datos concretos y evidencias específicas del análisis.
    """
    # Extraer evidencias específicas de los resultados para cada patrón
    evidencias_encontradas = []
    datos_numericos = []
    problemas_detectados = []
    
    for resultado in resultados:
        if "justificacion" in resultado:
            justificacion = resultado["justificacion"]
            # Extraer datos numéricos y porcentajes
            import re
            numeros = re.findall(r'\d+(?:\.\d+)?%?', justificacion)
            datos_numericos.extend(numeros)
            
            # Extraer problemas específicos
            if resultado.get("nivel") in ["insuficiente", "deficiente"]:
                problemas_detectados.append({
                    "texto": justificacion[:180],
                    "criterio": resultado.get("criterio", ""),
                    "nivel": resultado.get("nivel", "")
                })
        
        # Extraer evidencias específicas
        evidencias = resultado.get("evidencias", [])
        for evidencia in evidencias[:1]:  # Solo la primera evidencia por resultado
            if evidencia.get("frase") and evidencia.get("pagina"):
                evidencias_encontradas.append({
                    "frase": evidencia["frase"][:120],
                    "pagina": evidencia["pagina"],
                    "criterio": resultado.get("criterio", "")
                })
    
    preguntas_patron = {
        "desarticulacion_logica": generar_pregunta_desarticulacion(evidencias_encontradas, problemas_detectados),
        "secuencia_metodologica_incorrecta": generar_pregunta_metodologia(evidencias_encontradas, datos_numericos),
        "superficialidad_herramientas": generar_pregunta_superficialidad(evidencias_encontradas, datos_numericos, problemas_detectados)
    }
    
    return preguntas_patron.get(patron, generar_pregunta_generica(evidencias_encontradas, problemas_detectados))

def generar_pregunta_desarticulacion(evidencias: List[Dict], problemas: List[Dict]) -> str:
    """Genera pregunta específica sobre desarticulación lógica con evidencias concretas"""
    if evidencias and problemas:
        evidencia_principal = evidencias[0]
        problema_principal = problemas[0]
        
        return f"""El documento establece en la página {evidencia_principal['pagina']} que "{evidencia_principal['frase']}", sin embargo, el análisis del criterio "{problema_principal['criterio']}" revela que {problema_principal['texto'].lower()}. Dado que la coherencia argumentativa es fundamental en la investigación académica, ¿cómo se justifica esta aparente contradicción entre la formulación teórica y su desarrollo metodológico, y por qué no se abordan estas inconsistencias de manera explícita en el documento?"""
    
    return """Se detecta una desarticulación significativa entre la fundamentación teórica del problema y el desarrollo metodológico propuesto. ¿Cómo se garantiza la coherencia epistemológica entre la identificación del problema, la formulación de objetivos y la selección de herramientas de análisis?"""

def generar_pregunta_metodologia(evidencias: List[Dict], datos: List[str]) -> str:
    """Genera pregunta específica sobre problemas metodológicos con datos concretos"""
    if evidencias and datos:
        evidencia_principal = evidencias[0]
        dato_principal = datos[0] if datos else "los valores presentados"
        
        return f"""La metodología aplicada muestra "{evidencia_principal['frase']}" (página {evidencia_principal['pagina']}), resultando en valores como {dato_principal}, pero no se explicita la secuencia analítica seguida ni los criterios de validación empleados. Considerando que la rigurosidad metodológica requiere transparencia en los procedimientos, ¿por qué no se justifica la alteración de secuencias metodológicas estándar (PESTEL → Porter → DAFO), y cómo se garantiza la validez de los resultados obtenidos sin esta fundamentación?"""
    
    return """El análisis estratégico no sigue la secuencia metodológica prescrita, alterando el orden lógico de las herramientas analíticas. ¿Qué fundamentación epistemológica justifica esta variación metodológica y cómo se controla su impacto en la validez del diagnóstico?"""

def generar_pregunta_superficialidad(evidencias: List[Dict], datos: List[str], problemas: List[Dict]) -> str:
    """Genera pregunta específica sobre superficialidad en herramientas con evidencias múltiples"""
    if evidencias and datos and problemas:
        evidencia_principal = evidencias[0]
        dato_principal = datos[0] if datos else "las valoraciones"
        problema_principal = problemas[0]
        
        return f"""El análisis presenta {dato_principal} como resultado del "{evidencia_principal['criterio']}" (página {evidencia_principal['pagina']}), pero {problema_principal['texto'].lower()} Dado que las herramientas de análisis estratégico requieren fundamentación empírica sólida para ser válidas, ¿qué evidencia sustenta estas valoraciones específicas, cómo se controló la subjetividad inherente a estas evaluaciones, y por qué no se explicitan los criterios metodológicos que justifican la asignación de estos valores particulares?"""
    
    return """Las herramientas de análisis se aplican de manera formal pero sin demostrar rigor en los criterios de evaluación. ¿Qué evidencia empírica sustenta las valoraciones realizadas y cómo se controló la subjetividad inherente a estas evaluaciones?"""

def generar_pregunta_generica(evidencias: List[Dict], problemas: List[Dict]) -> str:
    """Genera pregunta genérica con contexto específico cuando no hay patrón específico"""
    if evidencias and problemas:
        evidencia = evidencias[0]
        problema = problemas[0]
        
        return f"""El documento presenta "{evidencia['frase']}" en la página {evidencia['pagina']}, sin embargo, el análisis revela que {problema['texto'].lower()} ¿Cómo se reconcilia esta discrepancia y qué implicaciones tiene para la validez metodológica del estudio completo?"""
    
    return """Se identifican inconsistencias metodológicas que requieren fundamentación adicional. ¿Cómo se justifican estas limitaciones en el marco de las exigencias académicas esperadas?"""
    
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

def guardar_resultados(resultados: List[Dict[str, Any]], ruta_base: str, problemas_contenido: List[Dict[str, Any]], 
                      logger: logging.Logger, texto_tfm: str = ""):
    """
    Guarda los resultados de la evaluación en dos archivos: .md y .json.
    Genera preguntas específicas con datos concretos del documento.
    """
    try:
        # Cargar plantillas de preguntas
        plantillas = cargar_plantillas_preguntas()
        
        # Generar preguntas dinámicas usando el nuevo sistema epistemológico CON TEXTO DEL TFM
        preguntas = generar_preguntas_dinamicas(resultados, plantillas, logger, texto_tfm)
        
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

    # 6) Exportar con texto del TFM para preguntas específicas
    exportar_resultados(resultados, carpeta_salida, problemas_contenido, logger, texto_tfm)
    logger.info("✅ Evaluación finalizada correctamente.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
