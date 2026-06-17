import argparse
import subprocess
import plistlib
from pathlib import Path
import unicodedata
import sys
import os

UTF8_ENV = dict(os.environ)
UTF8_ENV.setdefault("LC_ALL", "en_US.UTF-8")
UTF8_ENV.setdefault("LANG", "en_US.UTF-8")


# --- Detectar OneDrive ---
def _is_onedrive_path(p: Path) -> bool:
    sp = str(p)
    return ("OneDrive" in sp) or ("/Library/CloudStorage/" in sp and "OneDrive-" in sp)


# --- Hidratar (forzar descarga) ---
def _hydrate_if_needed(path: Path) -> None:
    """
    Intenta forzar la descarga del archivo si está “online-only”.
    Estrategia: abrir en rb y leer un bloque pequeño para que el
    File Provider traiga el contenido.
    """
    try:
        with open(path, "rb", buffering=0) as f:
            _ = f.read(1024 * 64)  # 64KB bastan para disparar la descarga
    except Exception:
        # Si falla, no reventamos; algunos placeholders permiten mdls igualmente.
        pass


def _mdls_plist(path: Path):
    proc = subprocess.run(
        ["mdls", "-name", "kMDItemUserTags", "-plist", str(path)],
        capture_output=True,
        env=UTF8_ENV,
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


def _coerce_existing_path(p: Path) -> Path:
    """
    Devuelve un Path existente probando distintas normalizaciones Unicode
    (tal cual, NFC, NFD, NFKC, NFKD). Expande ~ y resuelve si existe.
    """
    candidates = [str(p)]
    for form in ("NFC", "NFD", "NFKC", "NFKD"):
        candidates.append(unicodedata.normalize(form, str(p)))

    for cand in candidates:
        q = Path(cand).expanduser()
        # No uses resolve() antes de exists(); en APFS/OneDrive a veces falla.
        if q.exists():
            return q.resolve()
    # Si ninguna existe, devolvemos la versión NFC (para mensajes claros)
    return Path(unicodedata.normalize("NFC", str(p))).expanduser()


def list_tags_in_folder(folder: Path, recursive: bool = False):
    folder = _coerce_existing_path(folder)
    if not folder.is_dir():
        raise NotADirectoryError(f"No es carpeta: {folder}")
    it = folder.rglob("*") if recursive else folder.glob("*")
    for p in it:
        if p.is_file():
            try:
                tags = get_finder_tags(p)
                print(f"{p} -> {tags}")
            except Exception as e:
                print(f"{p} -> ERROR: {e}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description="Leer etiquetas de Finder (kMDItemUserTags)"
    )
    parser.add_argument(
        "ruta", help="Ruta de archivo o carpeta (admite caracteres especiales)"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recorrer recursivamente si es carpeta",
    )
    args = parser.parse_args()

    ruta = Path(args.ruta)
    if ruta.is_dir():
        list_tags_in_folder(ruta, recursive=args.recursive)
    else:
        tags = get_finder_tags(ruta)
        print(tags)


if __name__ == "__main__":
    main()
