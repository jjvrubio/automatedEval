#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import tempfile
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

from docx import Document


BASE_DIR = Path(
    "/Users/juanjo/Library/CloudStorage/OneDrive-UNIRUniversidadInternacionaldeLaRioja/"
    "UNIR CSEU - Documentos/Práctica docente/TEMAS"
)


@dataclass(frozen=True)
class ParTema:
    numero: int
    plantilla: Path
    revisado: Path


def extraer_numero_tema(nombre: str) -> int | None:
    match = re.match(r"^TEMA\s+(\d+)\.docx$", nombre, flags=re.IGNORECASE)
    if not match:
        return None
    return int(match.group(1))


def construir_pares(carpeta: Path) -> list[ParTema]:
    plantillas: dict[int, Path] = {}
    revisados: dict[int, Path] = {}

    for p in carpeta.glob("*.docx"):
        nombre = p.name
        n = extraer_numero_tema(nombre)
        if n is not None:
            plantillas[n] = p
            continue

        match_rev = re.match(r"^tema_(\d+)_rev\.docx$", nombre, flags=re.IGNORECASE)
        if match_rev:
            revisados[int(match_rev.group(1))] = p

    pares: list[ParTema] = []
    for n in sorted(set(plantillas) & set(revisados)):
        pares.append(ParTema(numero=n, plantilla=plantillas[n], revisado=revisados[n]))

    return pares


def reemplazar_cuerpo_contenido(plantilla: Path, revisado: Path, salida: Path) -> None:
    doc_dst = Document(str(plantilla))
    doc_src = Document(str(revisado))

    body_dst = doc_dst._element.body
    body_src = doc_src._element.body

    sect_pr = None
    for child in list(body_dst):
        if child.tag.endswith("}sectPr"):
            sect_pr = child
            continue
        body_dst.remove(child)

    insert_index = len(body_dst)
    if sect_pr is not None:
        insert_index = list(body_dst).index(sect_pr)

    for child in list(body_src):
        if child.tag.endswith("}sectPr"):
            continue
        body_dst.insert(insert_index, deepcopy(child))
        insert_index += 1

    salida.parent.mkdir(parents=True, exist_ok=True)
    doc_dst.save(str(salida))


def es_ruta_onedrive(path: Path) -> bool:
    s = str(path)
    return ("/Library/CloudStorage/" in s and "OneDrive" in s) or ("OneDrive" in s)


def copiar_a_staging(archivo: Path, staging_dir: Path) -> Path:
    staging_dir.mkdir(parents=True, exist_ok=True)
    destino = staging_dir / archivo.name
    shutil.copy2(archivo, destino)
    return destino


def procesar_temas(
    carpeta: Path,
    solo_tema: int | None,
    sufijo: str,
    out_dir: str,
    usar_staging: bool,
) -> int:
    if not carpeta.exists():
        raise FileNotFoundError(f"No existe la carpeta: {carpeta}")

    pares = construir_pares(carpeta)
    if solo_tema is not None:
        pares = [p for p in pares if p.numero == solo_tema]

    if not pares:
        print("No hay pares TEMA n.docx + tema_n_rev.docx para procesar.")
        return 1

    salida_base = carpeta / out_dir
    ok = 0
    ko = 0

    for par in pares:
        salida = salida_base / f"TEMA {par.numero}{sufijo}.docx"
        try:
            plantilla_origen = par.plantilla
            revisado_origen = par.revisado

            if usar_staging and (es_ruta_onedrive(plantilla_origen) or es_ruta_onedrive(revisado_origen)):
                staging_root = Path(tempfile.gettempdir()) / "actualizar_temas_sin_vba"
                staging_tema = staging_root / f"tema_{par.numero}"
                plantilla_origen = copiar_a_staging(par.plantilla, staging_tema)
                revisado_origen = copiar_a_staging(par.revisado, staging_tema)

            reemplazar_cuerpo_contenido(plantilla_origen, revisado_origen, salida)
            ok += 1
            print(f"OK  TEMA {par.numero}: {salida}")
        except Exception as exc:
            ko += 1
            print(f"ERR TEMA {par.numero}: {exc}")

    print(f"\nResumen -> OK: {ok} | ERR: {ko} | Total: {len(pares)}")
    print("Nota: Word puede requerir actualizar campos (TOC/TOF) al abrir el archivo.")
    return 0 if ko == 0 else 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Actualizar temas DOCX sin VBA, manteniendo estructura de la plantilla."
    )
    parser.add_argument("--carpeta", type=Path, default=BASE_DIR, help="Carpeta TEMAS")
    parser.add_argument("--tema", type=int, default=None, help="Procesar solo un numero de tema")
    parser.add_argument(
        "--sufijo",
        type=str,
        default="_ACTUALIZADO",
        help="Sufijo para el nombre de salida",
    )
    parser.add_argument(
        "--out-dir",
        type=str,
        default="_actualizados_sin_vba",
        help="Subcarpeta de salida dentro de TEMAS",
    )
    parser.add_argument(
        "--sin-staging",
        action="store_true",
        help="Desactiva copia temporal local para rutas OneDrive",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return procesar_temas(
        carpeta=args.carpeta,
        solo_tema=args.tema,
        sufijo=args.sufijo,
        out_dir=args.out_dir,
        usar_staging=not args.sin_staging,
    )


if __name__ == "__main__":
    raise SystemExit(main())
