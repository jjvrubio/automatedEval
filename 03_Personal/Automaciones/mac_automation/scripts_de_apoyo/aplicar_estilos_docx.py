#!/usr/bin/env python3
from __future__ import annotations

import argparse
import tempfile
import unicodedata
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import xml.etree.ElementTree as ET


DEFAULT_TEMAS = Path(
    "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/"
    "UNIR/Actualización de Contenidos/Ecosistema Digital y Tecnologías Disruptivas/"
    "Curso 2026/TEMAS"
)

PARTES_ESTILO = (
    "word/styles.xml",
    "word/stylesWithEffects.xml",
    "word/theme/theme1.xml",
    "word/numbering.xml",
    "word/fontTable.xml",
)

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": NS_W}


def normalizar_nombre_estilo(texto: str) -> str:
    t = texto.lower().strip()
    t = "".join(ch for ch in unicodedata.normalize("NFKD", t) if not unicodedata.combining(ch))
    return "".join(ch for ch in t if ch.isalnum())


def extraer_estilos_por_id(styles_xml: bytes) -> dict[str, str]:
    root = ET.fromstring(styles_xml)
    estilos: dict[str, str] = {}
    for estilo in root.findall("w:style", NS):
        sid = estilo.attrib.get(f"{{{NS_W}}}styleId")
        if not sid:
            continue
        nombre_node = estilo.find("w:name", NS)
        nombre = nombre_node.attrib.get(f"{{{NS_W}}}val", "") if nombre_node is not None else ""
        estilos[sid] = nombre
    return estilos


def extraer_ids_usados_documento(document_xml: bytes) -> set[str]:
    root = ET.fromstring(document_xml)
    usados: set[str] = set()
    for tag in (".//w:pStyle", ".//w:rStyle", ".//w:tblStyle"):
        for node in root.findall(tag, NS):
            val = node.attrib.get(f"{{{NS_W}}}val")
            if val:
                usados.add(val)
    return usados


def construir_remapeo_estilos(
    estilos_plantilla: dict[str, str],
    estilos_revisado: dict[str, str],
    ids_faltantes: set[str],
) -> dict[str, str]:
    por_nombre_plantilla: dict[str, str] = {}
    for sid, nombre in estilos_plantilla.items():
        clave = normalizar_nombre_estilo(nombre)
        if clave:
            por_nombre_plantilla[clave] = sid

    sinonimos: dict[str, list[str]] = {
        "author": ["author", "autor", "normal"],
        "date": ["date", "fecha", "normal"],
        "firstparagraph": ["firstparagraph", "primerparrafo", "normal"],
        "hyperlink": ["hyperlink", "hipervinculo"],
        "toc3": ["toc3", "tdc3", "heading3", "titulo3"],
        "title": ["title", "titulo", "heading1"],
        "tocheading": ["tocheading", "titulotdc", "encabezadotoc", "heading1"],
    }

    remapeo: dict[str, str] = {}
    for sid in sorted(ids_faltantes):
        nombre_rev = estilos_revisado.get(sid, "")
        clave_rev = normalizar_nombre_estilo(nombre_rev)

        candidatos = [clave_rev]
        candidatos.extend(sinonimos.get(clave_rev, []))

        elegido = None
        for c in candidatos:
            if c in por_nombre_plantilla:
                elegido = por_nombre_plantilla[c]
                break

        if not elegido and "Normal" in estilos_plantilla:
            elegido = "Normal"

        if elegido:
            remapeo[sid] = elegido

    return remapeo


def aplicar_remapeo_en_documento(document_xml: bytes, remapeo: dict[str, str]) -> bytes:
    if not remapeo:
        return document_xml
    root = ET.fromstring(document_xml)
    for tag in (".//w:pStyle", ".//w:rStyle", ".//w:tblStyle"):
        for node in root.findall(tag, NS):
            val = node.attrib.get(f"{{{NS_W}}}val")
            if val in remapeo:
                node.attrib[f"{{{NS_W}}}val"] = remapeo[val]
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def aplicar_estilos_docx(plantilla: Path, revisado: Path, salida: Path) -> list[str]:
    if not plantilla.exists():
        raise FileNotFoundError(f"No existe plantilla: {plantilla}")
    if not revisado.exists():
        raise FileNotFoundError(f"No existe revisado: {revisado}")

    aplicadas: list[str] = []

    with ZipFile(str(plantilla), "r") as z_tpl:
        blobs_tpl = {}
        nombres_tpl = set(z_tpl.namelist())
        for parte in PARTES_ESTILO:
            if parte in nombres_tpl:
                blobs_tpl[parte] = z_tpl.read(parte)

    estilos_tpl = extraer_estilos_por_id(blobs_tpl.get("word/styles.xml", b"<w:styles/>"))

    with ZipFile(str(revisado), "r") as z_src:
        styles_src_xml = z_src.read("word/styles.xml") if "word/styles.xml" in z_src.namelist() else b"<w:styles/>"
        doc_src_xml = z_src.read("word/document.xml")
        estilos_src = extraer_estilos_por_id(styles_src_xml)
        ids_usados_src = extraer_ids_usados_documento(doc_src_xml)
        ids_faltantes = {sid for sid in ids_usados_src if sid not in estilos_tpl}
        remapeo = construir_remapeo_estilos(estilos_tpl, estilos_src, ids_faltantes)

        fd, tmp_name = tempfile.mkstemp(suffix=".docx")
        _ = fd
        Path(tmp_name).unlink(missing_ok=True)
        tmp_path = Path(tmp_name)

        with ZipFile(str(tmp_path), "w", compression=ZIP_DEFLATED) as z_out:
            for info in z_src.infolist():
                nombre = info.filename
                if nombre == "word/document.xml":
                    z_out.writestr(nombre, aplicar_remapeo_en_documento(doc_src_xml, remapeo))
                    continue
                if nombre in blobs_tpl:
                    z_out.writestr(nombre, blobs_tpl[nombre])
                    aplicadas.append(nombre)
                else:
                    z_out.writestr(nombre, z_src.read(nombre))

            # Si falta alguna parte en el revisado, se anade desde plantilla.
            src_names = set(z_src.namelist())
            for nombre, contenido in blobs_tpl.items():
                if nombre not in src_names:
                    z_out.writestr(nombre, contenido)
                    aplicadas.append(nombre)

    salida.parent.mkdir(parents=True, exist_ok=True)
    tmp_path.replace(salida)
    return sorted(set(aplicadas))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Aplica estilos de un DOCX plantilla a un DOCX revisado, sin tocar el contenido principal."
    )
    parser.add_argument(
        "--plantilla",
        type=Path,
        default=DEFAULT_TEMAS / "TEMA 1.docx",
        help="DOCX origen de estilos",
    )
    parser.add_argument(
        "--revisado",
        type=Path,
        default=DEFAULT_TEMAS / "tema_1_rev.docx",
        help="DOCX con contenido revisado",
    )
    parser.add_argument(
        "--salida",
        type=Path,
        default=DEFAULT_TEMAS / "tema_1_rev_ESTILADO.docx",
        help="DOCX de salida",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    aplicadas = aplicar_estilos_docx(
        plantilla=args.plantilla,
        revisado=args.revisado,
        salida=args.salida,
    )

    print(f"Plantilla: {args.plantilla}")
    print(f"Revisado:  {args.revisado}")
    print(f"Salida:    {args.salida}")
    if aplicadas:
        print("Partes de estilo aplicadas:")
        for p in aplicadas:
            print(f" - {p}")
    else:
        print("No se encontraron partes de estilo para aplicar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
