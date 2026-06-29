#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import hashlib
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from zipfile import BadZipFile, ZipFile
import xml.etree.ElementTree as ET


NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}
W_VAL = f"{{{NS['w']}}}val"
R_EMBED = f"{{{NS['r']}}}embed"
INDEX_SECTION_KEYS = {
    "indice",
    "indices",
    "tabladecontenido",
    "tabladecontenidos",
    "tablacontenido",
    "tablacontenidos",
    "contenidos",
    "sumario",
    "tableofcontents",
    "contents",
    "listadefiguras",
    "indicedefiguras",
    "tabladefiguras",
    "listadofiguras",
    "listadeimagenes",
    "indicedeimagenes",
    "tabladeimagenes",
    "listadoimagenes",
    "listadodeimagenes",
    "listadodefiguras",
    "listadetablas",
    "indicedetablas",
    "tabladetablas",
    "listadotablas",
    "listadodetablas",
    "listoftables",
    "listoffigures",
    "tableoffigures",
}
INDEX_STYLE_PREFIXES = ("toc", "tdc")
INDEX_STYLE_KEYS = {
    "tableoffigures",
    "captionedfigure",
    "captionedtable",
    "listoffigures",
    "listoftables",
    "indicedetablas",
    "indicedefiguras",
    "listadetablas",
    "listadefiguras",
    "listadeimagenes",
}


@dataclass
class Paragraph:
    text: str
    style_id: str | None
    style_name: str | None


@dataclass
class Chapter:
    title: str
    paragraphs: list[str]


@dataclass
class ImageRef:
    media_path: str
    digest: str
    size: int
    chapter: str
    ordinal: int


def normalize_key(text: str) -> str:
    clean = "".join(
        ch for ch in unicodedata.normalize("NFKD", text.lower().strip())
        if not unicodedata.combining(ch)
    )
    return re.sub(r"[^a-z0-9]+", "", clean)


def read_xml(docx_path: Path, member: str) -> ET.Element | None:
    try:
        with docx_path.open("rb") as fp:
            magic = fp.read(8)
        if magic == b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":
            raise ValueError(
                f"{docx_path} no es un DOCX abierto legible: parece un archivo Office cifrado "
                "o un contenedor binario. Guardalo desde Word como .docx sin cifrar/proteger."
            )
        with ZipFile(docx_path) as zf:
            if member not in zf.namelist():
                return None
            return ET.fromstring(zf.read(member))
    except ValueError:
        raise
    except (BadZipFile, OSError, TimeoutError) as exc:
        raise ValueError(
            f"No se pudo leer {docx_path} como DOCX valido. "
            "Comprueba que el archivo no este corrupto y que este descargado localmente."
        ) from exc


def extract_styles(docx_path: Path) -> dict[str, str]:
    root = read_xml(docx_path, "word/styles.xml")
    if root is None:
        return {}

    styles: dict[str, str] = {}
    for style in root.findall("w:style", NS):
        style_id = style.attrib.get(W_VAL) or style.attrib.get(f"{{{NS['w']}}}styleId")
        name_node = style.find("w:name", NS)
        if style_id and name_node is not None:
            styles[style_id] = name_node.attrib.get(W_VAL, "")
    return styles


def paragraph_text(p: ET.Element) -> str:
    parts: list[str] = []
    for node in p.iter():
        if node.tag == f"{{{NS['w']}}}t" and node.text:
            parts.append(node.text)
        elif node.tag == f"{{{NS['w']}}}tab":
            parts.append("\t")
        elif node.tag == f"{{{NS['w']}}}br":
            parts.append("\n")
    return "".join(parts).strip()


def paragraph_style(p: ET.Element, styles: dict[str, str]) -> tuple[str | None, str | None]:
    p_style = p.find("w:pPr/w:pStyle", NS)
    if p_style is None:
        return None, None
    style_id = p_style.attrib.get(W_VAL)
    return style_id, styles.get(style_id, style_id) if style_id else None


def extract_paragraphs(docx_path: Path) -> list[Paragraph]:
    root = read_xml(docx_path, "word/document.xml")
    if root is None:
        raise ValueError(f"No se pudo leer word/document.xml en {docx_path}")

    styles = extract_styles(docx_path)
    paragraphs: list[Paragraph] = []
    for p in root.findall(".//w:p", NS):
        text = paragraph_text(p)
        if not text:
            continue
        style_id, style_name = paragraph_style(p, styles)
        paragraphs.append(Paragraph(text=text, style_id=style_id, style_name=style_name))
    return paragraphs


def is_chapter_heading(paragraph: Paragraph, explicit_style: str | None) -> bool:
    style_candidates = [paragraph.style_id or "", paragraph.style_name or ""]
    normalized_styles = {normalize_key(s) for s in style_candidates if s}

    if explicit_style:
        return normalize_key(explicit_style) in normalized_styles

    heading_1_names = {
        "heading1",
        "titulo1",
        "ttulo1",
        "encabezado1",
        "capitulo",
        "chapter",
    }
    if normalized_styles & heading_1_names:
        return True

    return bool(re.match(r"^(cap[ií]tulo|chapter)\s+([0-9ivxlcdm]+|[a-z])\b", paragraph.text, re.I))


def is_index_style(paragraph: Paragraph) -> bool:
    style_candidates = [paragraph.style_id or "", paragraph.style_name or ""]
    normalized_styles = {normalize_key(s) for s in style_candidates if s}
    return any(style.startswith(INDEX_STYLE_PREFIXES) for style in normalized_styles) or bool(
        normalized_styles & INDEX_STYLE_KEYS
    )


def is_index_section_heading(paragraph: Paragraph) -> bool:
    key = normalize_key(paragraph.text)
    if key in INDEX_SECTION_KEYS:
        return True
    return bool(
        re.match(
            r"^(indice|índice|tabla de contenidos?|lista de (figuras|imagenes|imágenes|tablas)|"
            r"indice de (figuras|imagenes|imágenes|tablas)|índice de (figuras|imagenes|imágenes|tablas)|"
            r"table of contents|list of figures|list of tables)$",
            paragraph.text.strip(),
            re.I,
        )
    )


def is_index_paragraph(paragraph: Paragraph) -> bool:
    return is_index_style(paragraph) or is_index_section_heading(paragraph)


def split_chapters(paragraphs: list[Paragraph], explicit_style: str | None = None) -> list[Chapter]:
    chapters: list[Chapter] = []
    current_title = "Documento completo"
    current_paragraphs: list[str] = []
    found_heading = False
    skipping_index_section = False

    for paragraph in paragraphs:
        if is_index_paragraph(paragraph):
            skipping_index_section = True
            continue

        if is_chapter_heading(paragraph, explicit_style):
            skipping_index_section = False
            if found_heading or current_paragraphs:
                chapters.append(Chapter(current_title, current_paragraphs))
            current_title = paragraph.text
            current_paragraphs = []
            found_heading = True
        elif not skipping_index_section:
            current_paragraphs.append(paragraph.text)

    chapters.append(Chapter(current_title, current_paragraphs))
    if not found_heading:
        return [Chapter("Documento completo", [p.text for p in paragraphs if not is_index_paragraph(p)])]
    return chapters


def indexed_chapters(chapters: list[Chapter]) -> dict[str, Chapter]:
    result: dict[str, Chapter] = {}
    seen: Counter[str] = Counter()
    for chapter in chapters:
        key = normalize_key(chapter.title) or "capitulo"
        seen[key] += 1
        unique_key = key if seen[key] == 1 else f"{key}#{seen[key]}"
        result[unique_key] = chapter
    return result


def chapter_diff(old: Chapter, new: Chapter, context: int) -> list[str]:
    return list(
        difflib.unified_diff(
            old.paragraphs,
            new.paragraphs,
            fromfile="original",
            tofile="revisado",
            lineterm="",
            n=context,
        )
    )


def extract_relationships(docx_path: Path) -> dict[str, str]:
    root = read_xml(docx_path, "word/_rels/document.xml.rels")
    if root is None:
        return {}
    rels: dict[str, str] = {}
    for rel in root.findall("rel:Relationship", NS):
        rel_id = rel.attrib.get("Id")
        target = rel.attrib.get("Target", "")
        if rel_id and target.startswith("media/"):
            rels[rel_id] = f"word/{target}"
    return rels


def paragraph_embedded_images(p: ET.Element) -> list[str]:
    ids: list[str] = []
    for blip in p.findall(".//a:blip", NS):
        rel_id = blip.attrib.get(R_EMBED)
        if rel_id:
            ids.append(rel_id)
    return ids


def extract_images(docx_path: Path, explicit_style: str | None = None) -> list[ImageRef]:
    root = read_xml(docx_path, "word/document.xml")
    if root is None:
        raise ValueError(f"No se pudo leer word/document.xml en {docx_path}")

    styles = extract_styles(docx_path)
    rels = extract_relationships(docx_path)
    media_bytes: dict[str, bytes] = {}
    with ZipFile(docx_path) as zf:
        for name in zf.namelist():
            if name.startswith("word/media/"):
                media_bytes[name] = zf.read(name)

    images: list[ImageRef] = []
    current_chapter = "Documento completo"
    ordinal_by_media: defaultdict[str, int] = defaultdict(int)
    skipping_index_section = False

    for p in root.findall(".//w:p", NS):
        text = paragraph_text(p)
        style_id, style_name = paragraph_style(p, styles)
        paragraph = Paragraph(text=text, style_id=style_id, style_name=style_name)
        if is_index_paragraph(paragraph):
            skipping_index_section = True
            continue

        if text and is_chapter_heading(paragraph, explicit_style):
            skipping_index_section = False
            current_chapter = text

        if skipping_index_section:
            continue

        for rel_id in paragraph_embedded_images(p):
            media_path = rels.get(rel_id)
            if not media_path or media_path not in media_bytes:
                continue
            blob = media_bytes[media_path]
            ordinal_by_media[media_path] += 1
            images.append(
                ImageRef(
                    media_path=media_path,
                    digest=hashlib.sha256(blob).hexdigest(),
                    size=len(blob),
                    chapter=current_chapter,
                    ordinal=ordinal_by_media[media_path],
                )
            )
    return images


def image_key(image: ImageRef) -> str:
    return f"{image.media_path}#{image.ordinal}"


def compare_images(old_images: list[ImageRef], new_images: list[ImageRef]) -> tuple[list[str], list[str], list[str]]:
    old_by_key = {image_key(img): img for img in old_images}
    new_by_key = {image_key(img): img for img in new_images}
    changed: list[str] = []
    matched_old: set[str] = set()
    matched_new: set[str] = set()

    for key in sorted(old_by_key.keys() & new_by_key.keys()):
        old = old_by_key[key]
        new = new_by_key[key]
        if old.digest == new.digest:
            matched_old.add(key)
            matched_new.add(key)
        else:
            changed.append(f"{key} | capitulo original: {old.chapter} | capitulo revisado: {new.chapter}")
            matched_old.add(key)
            matched_new.add(key)

    remaining_old = [img for img in old_images if image_key(img) not in matched_old]
    remaining_new = [img for img in new_images if image_key(img) not in matched_new]

    old_by_digest: defaultdict[str, list[ImageRef]] = defaultdict(list)
    for img in remaining_old:
        old_by_digest[img.digest].append(img)

    truly_added: list[ImageRef] = []
    for img in remaining_new:
        same_content = old_by_digest.get(img.digest)
        if same_content:
            same_content.pop()
        else:
            truly_added.append(img)

    truly_removed = [img for imgs in old_by_digest.values() for img in imgs]
    added = [f"{image_key(img)} | capitulo: {img.chapter}" for img in truly_added]
    removed = [f"{image_key(img)} | capitulo: {img.chapter}" for img in truly_removed]

    return changed, added, removed


def markdown_report(
    original: Path,
    revised: Path,
    old_chapters: list[Chapter],
    new_chapters: list[Chapter],
    old_images: list[ImageRef],
    new_images: list[ImageRef],
    context: int,
    include_equal: bool,
) -> str:
    old_index = indexed_chapters(old_chapters)
    new_index = indexed_chapters(new_chapters)
    old_keys = set(old_index)
    new_keys = set(new_index)

    lines: list[str] = [
        "# Comparativa DOCX",
        "",
        f"- Original: `{original}`",
        f"- Revisado: `{revised}`",
        "",
        "## Resumen",
        "",
        f"- Capitulos en original: {len(old_chapters)}",
        f"- Capitulos en revisado: {len(new_chapters)}",
        f"- Capitulos adicionales en revisado: {len(new_keys - old_keys)}",
        f"- Capitulos eliminados en revisado: {len(old_keys - new_keys)}",
        "",
        "## Texto por capitulo",
        "",
    ]

    for key in sorted(old_keys | new_keys):
        old = old_index.get(key)
        new = new_index.get(key)
        title = (new or old).title if (new or old) else key
        lines.extend([f"### {title}", ""])

        if old is None:
            lines.extend(["Capitulo adicional en el revisado.", ""])
            continue
        if new is None:
            lines.extend(["Capitulo presente en el original y ausente en el revisado.", ""])
            continue

        diff = chapter_diff(old, new, context)
        if not diff:
            if include_equal:
                lines.extend(["Sin diferencias de texto detectadas.", ""])
            else:
                lines.pop()
                lines.pop()
            continue

        added_lines = sum(1 for line in diff if line.startswith("+") and not line.startswith("+++"))
        removed_lines = sum(1 for line in diff if line.startswith("-") and not line.startswith("---"))
        lines.extend(
            [
                f"- Parrafos anadidos/modificados: {added_lines}",
                f"- Parrafos eliminados/modificados: {removed_lines}",
                "",
                "```diff",
                *diff,
                "```",
                "",
            ]
        )

    changed, added, removed = compare_images(old_images, new_images)
    lines.extend(["## Imagenes", ""])
    if not changed and not added and not removed:
        lines.extend(["Sin cambios de imagen detectados.", ""])
    else:
        if changed:
            lines.extend(["### Cambiadas", ""])
            lines.extend(f"- {item}" for item in changed)
            lines.append("")
        if added:
            lines.extend(["### Aniadidas", ""])
            lines.extend(f"- {item}" for item in added)
            lines.append("")
        if removed:
            lines.extend(["### Eliminadas", ""])
            lines.extend(f"- {item}" for item in removed)
            lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compara dos archivos DOCX por capitulos y lista cambios de imagenes."
    )
    parser.add_argument("original", type=Path, help="Archivo DOCX original")
    parser.add_argument("revisado", type=Path, help="Archivo DOCX revisado")
    parser.add_argument(
        "-o",
        "--salida",
        type=Path,
        default=Path("comparativa_docx.md"),
        help="Informe Markdown de salida",
    )
    parser.add_argument(
        "--chapter-style",
        help="Nombre o ID del estilo que marca capitulos. Por defecto: Heading 1/Titulo 1 o texto 'Capitulo N'.",
    )
    parser.add_argument(
        "--context",
        type=int,
        default=2,
        help="Parrafos de contexto alrededor de cada diferencia.",
    )
    parser.add_argument(
        "--include-equal",
        action="store_true",
        help="Incluye tambien capitulos sin diferencias.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.original.exists():
        raise FileNotFoundError(f"No existe el archivo original: {args.original}")
    if not args.revisado.exists():
        raise FileNotFoundError(f"No existe el archivo revisado: {args.revisado}")

    old_chapters = split_chapters(extract_paragraphs(args.original), args.chapter_style)
    new_chapters = split_chapters(extract_paragraphs(args.revisado), args.chapter_style)
    old_images = extract_images(args.original, args.chapter_style)
    new_images = extract_images(args.revisado, args.chapter_style)

    report = markdown_report(
        original=args.original,
        revised=args.revisado,
        old_chapters=old_chapters,
        new_chapters=new_chapters,
        old_images=old_images,
        new_images=new_images,
        context=args.context,
        include_equal=args.include_equal,
    )
    args.salida.parent.mkdir(parents=True, exist_ok=True)
    args.salida.write_text(report, encoding="utf-8")
    print(f"Informe generado: {args.salida}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
