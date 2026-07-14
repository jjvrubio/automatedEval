from __future__ import annotations

import os
import re
import tempfile
import xml.etree.ElementTree as ET
from copy import deepcopy
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from .style_transfer import aplicar_estilos_docx


NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": NS_W}
W = f"{{{NS_W}}}"
NS_CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
NS_DC = "http://purl.org/dc/elements/1.1/"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
CALLOUT_RE = re.compile(r"\[MD2DOCX_CALLOUT:([\w-]+)\]")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")

# The Lua filter embeds the matching SF Symbols PNG. This map supplies the
# matching table colour and follows Obsidian's built-in aliases.
CALLOUT_GROUPS = {
    "note": ({"note", "abstract", "summary", "tldr"}, "2563EB"),
    "info": ({"info", "todo"}, "0284C7"),
    "tip": ({"tip", "hint"}, "16A34A"),
    "success": ({"success", "check", "done"}, "16A34A"),
    "question": ({"question", "help", "faq"}, "D97706"),
    "warning": ({"warning", "caution", "attention", "missing"}, "D97706"),
    "danger": ({"failure", "fail", "danger", "error", "bug", "important"}, "DC2626"),
    "example": ({"example"}, "9333EA"),
    "quote": ({"quote", "cite"}, "6B7280"),
}


@dataclass(frozen=True)
class CoverFields:
    title: str
    subtitle: str
    supporting_lines: tuple[str, ...]
    year: str


def _plain_markdown(text: str) -> str:
    text = text.strip().rstrip("\\").strip()
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"(`+|\*\*|__|~~|==)", "", text)
    return text.strip()


def extract_commercial_cover(markdown_path: Path) -> CoverFields:
    """Extrae la portada comercial del bloque inicial del Markdown."""
    text = markdown_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    frontmatter: list[str] = []
    content_start = 0
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                frontmatter = lines[1:index]
                content_start = index + 1
                break

    headings: list[tuple[int, int, str]] = []
    for index in range(content_start, len(lines)):
        match = HEADING_RE.match(lines[index])
        if match:
            headings.append((index, len(match.group(1)), _plain_markdown(match.group(2))))

    level_one = [heading for heading in headings if heading[1] == 1]
    if len(level_one) < 2:
        raise ValueError(
            "La portada comercial requiere dos encabezados `#`: "
            "primero el subtitulo y despues el titulo."
        )

    second_index = level_one[1][0]
    secondary = next(
        (heading for heading in headings if heading[1] == 2 and heading[0] > second_index),
        None,
    )
    if secondary is None:
        raise ValueError(
            "La portada comercial requiere un encabezado `##` despues del titulo."
        )

    supporting_lines = [secondary[2]]
    for line in lines[secondary[0] + 1 :]:
        stripped = line.strip()
        if stripped == "---":
            break
        if stripped.startswith(">"):
            value = _plain_markdown(stripped[1:].strip())
            if value:
                supporting_lines.append(value)

    year = str(date.today().year)
    for line in frontmatter:
        match = re.match(r"^date\s*:\s*[\"']?(\d{4})", line.strip(), re.IGNORECASE)
        if match:
            year = match.group(1)
            break

    return CoverFields(
        title=level_one[1][2],
        subtitle=level_one[0][2],
        supporting_lines=tuple(supporting_lines),
        year=year,
    )


def _replace_content_control_text(sdt: ET.Element, lines: tuple[str, ...]) -> None:
    sdt_pr = sdt.find("w:sdtPr", NS)
    if sdt_pr is not None:
        _remove_existing(sdt_pr, {"showingPlcHdr", "dataBinding"})

    content = sdt.find("w:sdtContent", NS)
    if content is None:
        return
    runs = content.findall(".//w:r", NS)
    if not runs:
        return

    first_run = runs[0]
    for run in runs:
        for node in list(run):
            if node.tag in {W + "t", W + "br"}:
                run.remove(node)

    for index, line in enumerate(lines or ("",)):
        if index:
            ET.SubElement(first_run, W + "br")
        text = ET.SubElement(first_run, W + "t")
        text.set(XML_SPACE, "preserve")
        text.text = line


def _fill_cover_controls(cover: ET.Element, fields: CoverFields) -> None:
    values = {
        "título": (fields.title,),
        "subtítulo": (fields.subtitle,),
        "autor": fields.supporting_lines,
        "año": (fields.year,),
    }
    for sdt in cover.findall(".//w:sdt", NS):
        alias = sdt.find("w:sdtPr/w:alias", NS)
        if alias is None:
            continue
        name = (alias.get(W + "val") or "").strip().lower()
        if name in values:
            _replace_content_control_text(sdt, values[name])


def apply_cover_page(docx_path: Path, template_path: Path, fields: CoverFields) -> None:
    """Inserta y completa la portada nativa de la plantilla Word."""
    with ZipFile(template_path, "r") as template_zip:
        template_root = ET.fromstring(template_zip.read("word/document.xml"))
        template_body = template_root.find("w:body", NS)
        if template_body is None:
            raise ValueError(f"La plantilla no contiene un cuerpo Word: {template_path}")
        cover = next(
            (child for child in template_body if child.tag == W + "sdt"),
            None,
        )
        if cover is None:
            raise ValueError(f"La plantilla no contiene una portada: {template_path}")
        cover = deepcopy(cover)
        _fill_cover_controls(cover, fields)

    with ZipFile(docx_path, "r") as source:
        root = ET.fromstring(source.read("word/document.xml"))
        body = root.find("w:body", NS)
        if body is None:
            raise ValueError(f"El DOCX no contiene un cuerpo Word: {docx_path}")
        body.insert(0, cover)

        replacements = {
            "word/document.xml": ET.tostring(
                root, encoding="utf-8", xml_declaration=True
            )
        }

        if "docProps/core.xml" in source.namelist():
            core = ET.fromstring(source.read("docProps/core.xml"))
            for tag, value in (
                (f"{{{NS_DC}}}title", fields.title),
                (f"{{{NS_DC}}}subject", fields.subtitle),
            ):
                node = core.find(tag)
                if node is None:
                    node = ET.SubElement(core, tag)
                node.text = value
            replacements["docProps/core.xml"] = ET.tostring(
                core, encoding="utf-8", xml_declaration=True
            )

        fd, tmp_name = tempfile.mkstemp(suffix=".docx")
        os.close(fd)
        Path(tmp_name).unlink(missing_ok=True)
        tmp_path = Path(tmp_name)
        with ZipFile(tmp_path, "w", compression=ZIP_DEFLATED) as target:
            for info in source.infolist():
                target.writestr(info, replacements.get(info.filename, source.read(info.filename)))
    tmp_path.replace(docx_path)


def _callout_color(kind: str) -> str:
    for aliases, color in CALLOUT_GROUPS.values():
        if kind in aliases:
            return color
    return "6B7280"


def _child(parent: ET.Element, tag: str) -> ET.Element:
    found = parent.find(f"w:{tag}", NS)
    if found is not None:
        return found
    node = ET.Element(W + tag)
    parent.insert(0, node)
    return node


def _set_val(node: ET.Element, value: str) -> None:
    node.set(W + "val", value)


def _remove_existing(parent: ET.Element, tags: set[str]) -> None:
    for node in list(parent):
        if node.tag in {W + tag for tag in tags}:
            parent.remove(node)


def _tint(color: str, strength: float = 0.12) -> str:
    channels = [int(color[i : i + 2], 16) for i in (0, 2, 4)]
    return "".join(f"{round(255 - (255 - channel) * strength):02X}" for channel in channels)


def _style_callout_table(table: ET.Element, kind: str, first_p: ET.Element) -> None:
    color = _callout_color(kind)

    tbl_pr = _child(table, "tblPr")
    _remove_existing(tbl_pr, {"tblBorders", "tblCellMar", "tblLayout"})
    layout = ET.SubElement(tbl_pr, W + "tblLayout")
    layout.set(W + "type", "autofit")
    borders = ET.SubElement(tbl_pr, W + "tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        border = ET.SubElement(borders, W + edge)
        _set_val(border, "nil")

    row = table.find("w:tr", NS)
    if row is not None:
        _set_val(_child(_child(row, "trPr"), "cantSplit"), "1")

    cell = table.find("w:tr/w:tc", NS)
    if cell is not None:
        tc_pr = _child(cell, "tcPr")
        _remove_existing(tc_pr, {"tcBorders", "shd", "tcMar", "vAlign"})
        shd = ET.SubElement(tc_pr, W + "shd")
        _set_val(shd, "clear")
        shd.set(W + "color", "auto")
        shd.set(W + "fill", _tint(color))
        tc_borders = ET.SubElement(tc_pr, W + "tcBorders")
        left = ET.SubElement(tc_borders, W + "left")
        _set_val(left, "single")
        left.set(W + "sz", "24")
        left.set(W + "space", "0")
        left.set(W + "color", color)
        margins = ET.SubElement(tc_pr, W + "tcMar")
        for edge, width in (("top", "100"), ("left", "160"), ("bottom", "100"), ("right", "160")):
            margin = ET.SubElement(margins, W + edge)
            margin.set(W + "w", width)
            margin.set(W + "type", "dxa")
        valign = ET.SubElement(tc_pr, W + "vAlign")
        _set_val(valign, "center")

    # Remove the private marker, wherever Pandoc split it into runs.
    for text in first_p.findall(".//w:t", NS):
        if text.text and CALLOUT_RE.search(text.text):
            text.text = CALLOUT_RE.sub("", text.text).lstrip()

    p_pr = _child(first_p, "pPr")
    spacing = _child(p_pr, "spacing")
    spacing.set(W + "before", "0")
    spacing.set(W + "after", "80")

    for run in first_p.findall("w:r", NS):
        # Image runs already contain the correctly coloured SF Symbol.
        if run.find("w:drawing", NS) is not None:
            continue
        props = _child(run, "rPr")
        _set_val(_child(props, "b"), "1")
        _child(props, "color").set(W + "val", color)


def apply_callout_formatting(docx_path: Path) -> int:
    """Replace Lua markers and style generated one-cell callout tables."""
    with ZipFile(docx_path, "r") as source:
        document_xml = source.read("word/document.xml")
        root = ET.fromstring(document_xml)
        count = 0
        for table in root.findall(".//w:tbl", NS):
            first_p = table.find("w:tr/w:tc/w:p", NS)
            if first_p is None:
                continue
            text = "".join(node.text or "" for node in first_p.findall(".//w:t", NS))
            marker = CALLOUT_RE.search(text)
            if not marker:
                continue
            _style_callout_table(table, marker.group(1).lower(), first_p)
            count += 1

        if not count:
            return 0

        fd, tmp_name = tempfile.mkstemp(suffix=".docx")
        os.close(fd)
        Path(tmp_name).unlink(missing_ok=True)
        tmp_path = Path(tmp_name)
        with ZipFile(tmp_path, "w", compression=ZIP_DEFLATED) as target:
            for info in source.infolist():
                if info.filename == "word/document.xml":
                    target.writestr(
                        info,
                        ET.tostring(root, encoding="utf-8", xml_declaration=True),
                    )
                else:
                    target.writestr(info, source.read(info.filename))
    tmp_path.replace(docx_path)
    return count


def maybe_apply_style_template(
    output_docx: Path,
    style_template: Path | None,
    project_root: Path,
    cover_template: Path | None = None,
    cover_fields: CoverFields | None = None,
) -> None:
    """Punto de extension para post-procesado DOCX.

    Reutiliza la utilidad heredada para copiar estilos desde una plantilla
    Word sin tocar el contenido principal generado por Pandoc.
    """
    if style_template:
        aplicar_estilos_docx(
            plantilla=style_template,
            revisado=output_docx,
            salida=output_docx,
        )

    if cover_template and cover_fields:
        apply_cover_page(output_docx, cover_template, cover_fields)

    # Direct formatting goes last, so replacing styles/theme cannot erase it.
    apply_callout_formatting(output_docx)
