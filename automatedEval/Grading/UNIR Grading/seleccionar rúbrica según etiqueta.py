#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador TFM – Lectura de etiquetas Finder (compatible con OneDrive y nombres con tildes/ñ)

• Selector nativo de macOS (AppKit) o entrada por consola.
• Lee etiquetas Finder con mdls (-plist) y fallbacks.
• Compatible con rutas en OneDrive (hidrata el archivo si está “sólo en la nube”).
• Normaliza Unicode (NFC/NFD) para nombres con acentos y ñ.
• (Opcional) Selecciona una rúbrica según etiquetas detectadas.

Ajusta el mapeo en `RUBRICAS_POR_ETIQUETA` y `RUTA_RUBRICA_POR_DEFECTO` a tus rutas locales.

Probado en macOS (Apple Silicon) con Python 3.11/3.12/3.13.
"""

from __future__ import annotations
import os
import sys
import time
import json
import plistlib
import logging
import unicodedata
import subprocess
from pathlib import Path
from typing import Iterable, Set

# ---- UI nativa macOS (AppKit) para seleccionar archivo; fallback a CLI ----
try:
    from AppKit import NSOpenPanel, NSApplication
    _HAS_APPKIT = True
except Exception:
    _HAS_APPKIT = False

# ===================== CONFIGURACIÓN =====================
# Rúbrica por defecto (ajusta a tu ruta local)
RUTA_RUBRICA_POR_DEFECTO = "/ruta/a/rubricas/rubrica.xlsx"  # <-- AJUSTA ESTA RUTA

# Mapeo etiqueta → ruta de rúbrica (ajusta a tu organización)
RUBRICAS_POR_ETIQUETA: dict[str, str] = {
    "MUDPE": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MUDPE.xlsx",
    "MGPTD": "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica MGPTD.xlsx",
}

# =========================================================

# Configuración de entorno UTF-8
UTF8_ENV = dict(os.environ)
UTF8_ENV.setdefault("LC_ALL", "en_US.UTF-8")
UTF8_ENV.setdefault("LANG", "en_US.UTF-8")
# Variante conservadora (solo tipografías / codificación); descomenta si prefieres no tocar LC_ALL/LANG
# UTF8_ENV = dict(os.environ)
# UTF8_ENV.setdefault("LC_CTYPE", "en_US.UTF-8")

# ---------- Utilidades de ruta / OneDrive / Spotlight ----------

def _coerce_existing_path(p: Path) -> Path:
    """Devuelve un Path existente probando varias normalizaciones Unicode (NFC/NFD/NFKC/NFKD).
    No usa resolve() hasta confirmar existencia para evitar fallos con proveedores de archivos.
    """
    candidates = [str(p)]
    for form in ("NFC", "NFD", "NFKC", "NFKD"):
        candidates.append(unicodedata.normalize(form, str(p)))
    for cand in candidates:
        q = Path(cand).expanduser()
        if q.exists():
            try:
                return q.resolve()
            except Exception:
                return q
    return Path(unicodedata.normalize("NFC", str(p))).expanduser()


def _is_onedrive_path(p: Path) -> bool:
    s = str(p)
    return ("OneDrive" in s) or ("/Library/CloudStorage/" in s and "OneDrive-" in s)


def _hydrate_if_needed(path: Path) -> None:
    """Fuerza la descarga del archivo si está en Files On-Demand (OneDrive)."""
    try:
        with open(path, "rb", buffering=0) as f:
            _ = f.read(1024 * 64)  # 64 KB suele bastar para disparar la descarga
    except Exception:
        pass


def _mdls_plist(path: Path):
    proc = subprocess.run(
        ["mdls", "-name", "kMDItemUserTags", "-plist", str(path)],
        capture_output=True, env=UTF8_ENV
    )
    if proc.returncode != 0 or not proc.stdout:
        return None
    try:
        data = plistlib.loads(proc.stdout)
        if isinstance(data, dict):
            return data.get("kMDItemUserTags")
        if isinstance(data, list) and data and isinstance(data[0], dict):
            return data[0].get("kMDItemUserTags")
    except Exception:
        return None
    return None


def _finder_tags_via_osascript(path: Path) -> list[str]:
    """Fallback: leer nombres de etiquetas vía Finder/AppleScript (sin colores).
    Útil si Spotlight aún no refleja cambios.
    """
    script = f'''
    set p to POSIX file "{str(path)}"
    tell application "Finder"
        if exists p then
            set tgs to name of every tag of p
        else
            set tgs to {{}}
        end if
    end tell
    set AppleScript's text item delimiters to linefeed
    return tgs as string
    '''
    proc = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    if proc.returncode != 0:
        return []
    out = (proc.stdout or "").strip()
    return out.split("\n") if out else []


# ---------- API pública: leer etiquetas ----------

def get_finder_tags(path: Path) -> list[str]:
    path = _coerce_existing_path(path)
    if not path.exists():
        raise FileNotFoundError(f"No existe: {path}")

    # 1) Intento directo (plist): estable y limpio
    val = _mdls_plist(path)
    if val and val != "(null)":
        return [str(x) for x in val]

    # 2) Si está en OneDrive, hidrata y reintenta automáticamente
    if _is_onedrive_path(path):
        _hydrate_if_needed(path)
        for _ in range(3):
            time.sleep(0.25)
            val = _mdls_plist(path)
            if val and val != "(null)":
                return [str(x) for x in val]

    # 3) Fallback JSON
    try:
        proc = subprocess.run(
            ["mdls", "-name", "kMDItemUserTags", "-json", str(path)],
            capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV
        )
        if proc.returncode == 0 and proc.stdout.strip():
            data = json.loads(proc.stdout)
            if isinstance(data, dict):
                val = data.get("kMDItemUserTags")
            elif isinstance(data, list) and data and isinstance(data[0], dict):
                val = data[0].get("kMDItemUserTags")
            else:
                val = None
            if val and val != "(null)":
                return [str(x) for x in val]
    except Exception:
        pass

    # 4) Fallback RAW
    proc = subprocess.run(
        ["mdls", "-name", "kMDItemUserTags", "-raw", str(path)],
        capture_output=True, text=True, encoding="utf-8", env=UTF8_ENV
    )
    raw = (proc.stdout or "").strip()
    if raw and raw != "(null)":
        try:
            block = raw.strip().replace("(\n", "[").replace("\n)", "]").replace("(", "[").replace(")", "]")
            return [str(t) for t in json.loads(block)]
        except Exception:
            items = []
            for line in raw.splitlines():
                s = line.strip().strip(",")
                if s.startswith('"') and s.endswith('"'):
                    s = s[1:-1]
                if s not in ("(", ")", ""):
                    items.append(s)
            if items:
                return items

    # 5) Fallback Finder/AppleScript (nombres de etiquetas)
    try:
        return _finder_tags_via_osascript(path)
    except Exception:
        return []


# ---------- Lógica de selección de rúbrica por etiqueta ----------

def _normalize_tag_names(tags: Iterable[str]) -> Set[str]:
    """Devuelve el conjunto de nombres de etiqueta sin sufijo de color.
    Ej.: "Etiqueta\n6" → "Etiqueta".
    """
    norm: Set[str] = set()
    for t in tags:
        if not isinstance(t, str):
            continue
        name = t.partition('\n')[0]
        norm.add(name)
    return norm


def seleccionar_rubrica_por_tags(tags: list[str], logger: logging.Logger) -> str | None:
    """Selecciona la ruta de rúbrica según las etiquetas Finder detectadas.
    • Normaliza posibles etiquetas con sufijo de color (p. ej., "Etiqueta\n6").
    • Registra logs explícitos si detecta MUDPE o MGPTD.
    """
    if not tags:
        logger.info("No se encontraron etiquetas Finder en el archivo.")
        return None

    tags_set = _normalize_tag_names(tags)
    logger.info(f"Etiquetas normalizadas detectadas: {sorted(tags_set)}")

    # Logs explícitos para etiquetas clave
    if 'MUDPE' in tags_set:
        logger.info("Detectada etiqueta MUDPE → se intentará usar 'rubrica MUDPE.xlsx'.")
    if 'MGPTD' in tags_set:
        logger.info("Detectada etiqueta MGPTD → se intentará usar 'rubrica MGPTD.xlsx'.")

    for etiqueta, ruta in RUBRICAS_POR_ETIQUETA.items():
        if etiqueta in tags_set:
            if os.path.exists(ruta):
                logger.info(f"Rúbrica seleccionada por etiqueta '{etiqueta}': {ruta}")
                return ruta
            else:
                logger.warning(f"Etiqueta '{etiqueta}' coincide, pero la ruta de rúbrica no existe: {ruta}")
                return None

    logger.info("Ninguna etiqueta coincide con el mapeo definido; se usará la rúbrica por defecto.")
    return None


# ---------- (Ejemplo) Punto de entrada principal ----------

def _select_file_appkit() -> str | None:
    if not _HAS_APPKIT:
        return None
    try:
        # Asegura que exista una NSApplication (necesaria en algunos entornos CLI)
        NSApplication.sharedApplication()
        panel = NSOpenPanel.openPanel()
        panel.setCanChooseFiles_(True)
        panel.setCanChooseDirectories_(False)
        panel.setAllowsMultipleSelection_(False)
        panel.setAllowedFileTypes_(["pdf", "docx"])  # Restringe a .pdf y .docx
        panel.setTitle_("Selecciona el archivo TFM")
        if panel.runModal():
            url = panel.URL()
            if url:
                return url.path()
        return None
    except Exception:
        return None


# ------------------------- Self-tests -------------------------
# Ejecuta pruebas rápidas si la variable de entorno RUN_SELF_TESTS=1

def _run_self_tests() -> None:
    class _DummyLogger:
        def info(self, *a, **k):
            pass
        def warning(self, *a, **k):
            pass

    logger = _DummyLogger()

    # Test 1: normalización básica (sin sufijo)
    assert _normalize_tag_names(["MUDPE"]) == {"MUDPE"}

    # Test 2: normalización con sufijo de color "\n6"
    assert _normalize_tag_names(["Urgente\n6", "MGPTD"]) == {"Urgente", "MGPTD"}

    # Test 3: seleccionar_rubrica_por_tags no debe lanzar aunque las rutas no existan.
    # (El resultado puede ser None si las rutas no existen en el sistema del usuario.)
    try:
        _ = seleccionar_rubrica_por_tags(["MUDPE"], logger)
        _ = seleccionar_rubrica_por_tags(["MGPTD"], logger)
        _ = seleccionar_rubrica_por_tags(["Desconocida"], logger)
        _ = seleccionar_rubrica_por_tags([], logger)
    except Exception as e:
        raise AssertionError(f"seleccionar_rubrica_por_tags lanzó una excepción inesperada: {e}")


# --------------------------- Main ---------------------------

def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger("evaluador_tfm")

    # Self-tests opcionales
    if os.environ.get("RUN_SELF_TESTS") == "1":
        _run_self_tests()
        logger.info("Self-tests completados correctamente.")

    # 1) Obtener ruta del TFM (prioriza AppKit; luego CLI)
    if len(sys.argv) >= 2 and sys.argv[1]:
        ruta_tfm = sys.argv[1]
    else:
        ruta_tfm = _select_file_appkit()
        if not ruta_tfm:
            ruta_tfm = input("Ruta del archivo TFM (.pdf/.docx): ").strip()

    p_tfm = Path(ruta_tfm)
    p_tfm = _coerce_existing_path(p_tfm)
    if not p_tfm.exists() or not p_tfm.is_file():
        logger.error(f"Archivo no válido: {p_tfm}")
        sys.exit(1)

    logger.info(f"Archivo TFM: {p_tfm}")

    # 2) Leer etiquetas Finder (automático; soporta OneDrive y acentos)
    try:
        tags = get_finder_tags(p_tfm)
        logger.info(f"Etiquetas Finder: {tags}")
    except Exception as e:
        tags = []
        logger.warning(f"No se pudieron leer etiquetas Finder: {e}")

    # 3) Seleccionar rúbrica por etiqueta (si hay mapeo y coincide)
    ruta_rubrica = seleccionar_rubrica_por_tags(tags, logger) or RUTA_RUBRICA_POR_DEFECTO
    if not os.path.exists(ruta_rubrica):
        logger.warning(f"Rúbrica por defecto no encontrada: {ruta_rubrica} — ajusta la ruta en el script.")
    else:
        logger.info(f"Rúbrica final a usar: {ruta_rubrica}")

    # 4) Aquí iría la carga de rúbrica y la evaluación del TFM
    #    (stub / placeholder para conectar con tu evaluador real)
    # ---------------------------------------------------------
    # TODO: cargar rúbrica desde 'ruta_rubrica' (p.ej. pandas/openpyxl)
    # TODO: aplicar rúbrica al TFM seleccionado
    # ---------------------------------------------------------

    logger.info("Proceso finalizado.")


if __name__ == "__main__":
    main()
