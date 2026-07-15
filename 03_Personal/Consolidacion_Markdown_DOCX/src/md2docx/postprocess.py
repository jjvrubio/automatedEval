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

from .config import _load_yaml
from .style_transfer import aplicar_estilos_docx


NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": NS_W}
W = f"{{{NS_W}}}"
NS_CP = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
NS_DC = "http://purl.org/dc/elements/1.1/"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"
CALLOUT_RE = re.compile(r"\[MD2DOCX_CALLOUT:([\w-]+)\]")
HEADING_RE = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
INDEX_FIELD_RE = re.compile(r"^\s*(?:TOC|INDEX)(?:\s|$)", re.IGNORECASE)

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
    creator: str | None = None


@dataclass(frozen=True)
class DocumentControlFields:
    heading: str
    rows: tuple[tuple[str, str], ...]


def _plain_markdown(text: str) -> str:
    text = text.strip().rstrip("\\").strip()
    text = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"(`+|\*\*|__|~~|==)", "", text)
    return text.strip()


def _frontmatter_metadata(markdown_path: Path) -> dict[str, object]:
    lines = markdown_path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return _load_yaml("\n".join(lines[1:index]))
    return {}


def _metadata_text(metadata: dict[str, object], *keys: str) -> str:
    value = next((metadata[key] for key in keys if metadata.get(key)), None)
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(_plain_markdown(str(item)) for item in value if item)
    return _plain_markdown(str(value))


def extract_metadata_cover(markdown_path: Path) -> CoverFields:
    """Build a native Word cover from YAML metadata.

    English keys are canonical; Spanish aliases keep existing vault documents
    compatible while they are migrated.
    """
    metadata = _frontmatter_metadata(markdown_path)
    title = _metadata_text(metadata, "title", "titulo", "título")
    if not title:
        raise ValueError(
            "La portada requiere `title` en el frontmatter "
            "(tambien se acepta `titulo`)."
        )

    subtitle = _metadata_text(metadata, "subtitle", "subtitulo", "subtítulo")
    author = _metadata_text(metadata, "author", "autor")
    raw_date = _metadata_text(metadata, "date", "fecha")
    year_match = re.search(r"\b(\d{4})\b", raw_date)
    year = year_match.group(1) if year_match else str(date.today().year)

    return CoverFields(
        title=title,
        subtitle=subtitle,
        supporting_lines=(author,) if author else (),
        year=year,
        creator=author or None,
    )


def _control_bool(value: object, default: bool = False) -> bool:
    if value is None:
        return default
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {
        "true",
        "yes",
        "si",
        "sí",
        "1",
        "on",
        "activo",
        "active",
    }


def extract_document_control(markdown_path: Path) -> DocumentControlFields | None:
    """Read the optional final document-control page configuration from YAML."""
    metadata = _frontmatter_metadata(markdown_path)
    raw = metadata.get("document_control")
    if raw is None:
        raw = metadata.get("control_documento")
    if raw is None:
        return None

    options = raw if isinstance(raw, dict) else {}
    enabled = (
        _control_bool(options.get("enabled", options.get("generar")), default=True)
        if options
        else _control_bool(raw)
    )
    if not enabled:
        return None

    heading = _metadata_text(
        options, "heading", "page_title", "titulo_pagina", "título_página"
    ) or "Control del documento"
    include_standard = _control_bool(
        options.get(
            "include_standard_fields",
            options.get("incluir_campos_estandar"),
        ),
        default=True,
    )

    standard_fields = (
        ("Título", ("title", "titulo", "título")),
        ("Subtítulo", ("subtitle", "subtitulo", "subtítulo")),
        ("Idioma", ("language", "idioma", "lang")),
        ("Fecha", ("date", "fecha")),
        ("Versión", ("version", "versión")),
        ("Estado", ("status", "estado")),
        ("Tags", ("tags", "etiquetas")),
    )
    rows: list[tuple[str, str]] = []
    if include_standard:
        for label, keys in standard_fields:
            value = _metadata_text(metadata, *keys)
            if value:
                rows.append((label, value))

    custom_fields = options.get("fields", options.get("campos", {}))
    if isinstance(custom_fields, dict):
        for label, value in custom_fields.items():
            rendered = _plain_markdown(str(value)) if value is not None else ""
            if rendered:
                rows.append((_plain_markdown(str(label)), rendered))

    if not rows:
        raise ValueError(
            "`document_control` esta activado, pero no hay campos de control "
            "reconocidos ni campos personalizados."
        )
    return DocumentControlFields(heading=heading, rows=tuple(rows))


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

    metadata = _load_yaml("\n".join(frontmatter)) if frontmatter else {}

    cover_end = next(
        (
            index
            for index in range(content_start, len(lines))
            if lines[index].strip() == "---"
        ),
        len(lines),
    )

    headings: list[tuple[int, int, str]] = []
    for index in range(content_start, cover_end):
        match = HEADING_RE.match(lines[index])
        if match:
            headings.append((index, len(match.group(1)), _plain_markdown(match.group(2))))

    level_one = [heading for heading in headings if heading[1] == 1]
    yaml_title = metadata.get("title")
    minimum_level_one = 1 if yaml_title else 2
    if len(level_one) < minimum_level_one:
        requirement = (
            "un encabezado `#` para el subtitulo"
            if yaml_title
            else "dos encabezados `#`: primero el subtitulo y despues el titulo"
        )
        raise ValueError(f"La portada comercial requiere {requirement}.")

    title_anchor = level_one[1][0] if len(level_one) >= 2 else level_one[0][0]
    secondary = next(
        (heading for heading in headings if heading[1] == 2 and heading[0] > title_anchor),
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

    title = _plain_markdown(str(yaml_title)) if yaml_title else level_one[1][2]

    return CoverFields(
        title=title,
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
            core_values = [
                (f"{{{NS_DC}}}title", fields.title),
                (f"{{{NS_DC}}}subject", fields.subtitle),
            ]
            if fields.creator:
                core_values.append((f"{{{NS_DC}}}creator", fields.creator))
            for tag, value in core_values:
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


def _field_instructions(element: ET.Element) -> list[str]:
    instructions: list[str] = []
    simple_fields = element.findall(f".//{{{NS_W}}}fldSimple")
    instructions.extend(
        node.get(W + "instr", "") for node in simple_fields if node.get(W + "instr")
    )

    instruction_parts = [
        node.text or "" for node in element.findall(f".//{{{NS_W}}}instrText")
    ]
    if instruction_parts:
        instructions.append("".join(instruction_parts))
    return instructions


def _contains_index_field(element: ET.Element) -> bool:
    return any(INDEX_FIELD_RE.match(value) for value in _field_instructions(element))


def _contains_complex_field_marker(element: ET.Element, marker: str) -> bool:
    return any(
        node.get(W + "fldCharType") == marker
        for node in element.findall(f".//{{{NS_W}}}fldChar")
    )


def _is_next_page_section_break(element: ET.Element) -> bool:
    section = element.find("w:pPr/w:sectPr", NS)
    if section is None:
        return False
    section_type = section.find("w:type", NS)
    return section_type is None or section_type.get(W + "val") == "nextPage"


def _next_page_section_break() -> ET.Element:
    paragraph = ET.Element(W + "p")
    properties = ET.SubElement(paragraph, W + "pPr")
    section = ET.SubElement(properties, W + "sectPr")
    section_type = ET.SubElement(section, W + "type")
    section_type.set(W + "val", "nextPage")
    return paragraph


def apply_index_section_breaks(docx_path: Path) -> int:
    """Start a next-page Word section after every TOC or INDEX field.

    Word represents the table of contents, lists of figures/tables and the
    alphabetical index with TOC/INDEX fields. The cached field result may live
    inside a content control or span multiple body elements, so the break is
    placed after the field's closing element.
    """
    with ZipFile(docx_path, "r") as source:
        root = ET.fromstring(source.read("word/document.xml"))
        body = root.find("w:body", NS)
        if body is None:
            raise ValueError(f"El DOCX no contiene un cuerpo Word: {docx_path}")

        children = list(body)
        insert_after: list[int] = []
        for index, child in enumerate(children):
            if not _contains_index_field(child):
                continue

            end_index = index
            spans_children = (
                child.tag != W + "sdt"
                and _contains_complex_field_marker(child, "begin")
                and not _contains_complex_field_marker(child, "end")
            )
            if spans_children:
                for candidate_index in range(index + 1, len(children)):
                    end_index = candidate_index
                    if _contains_complex_field_marker(children[candidate_index], "end"):
                        break

            next_index = end_index + 1
            if next_index < len(children) and _is_next_page_section_break(children[next_index]):
                continue
            insert_after.append(end_index)

        if not insert_after:
            return 0

        for offset, index in enumerate(insert_after, start=1):
            body.insert(index + offset, _next_page_section_break())

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
    return len(insert_after)


def _document_control_paragraph(
    text: str,
    *,
    bold: bool = False,
    size: str = "22",
    color: str = "1F2937",
) -> ET.Element:
    paragraph = ET.Element(W + "p")
    properties = ET.SubElement(paragraph, W + "pPr")
    spacing = ET.SubElement(properties, W + "spacing")
    spacing.set(W + "before", "0")
    spacing.set(W + "after", "80")
    run = ET.SubElement(paragraph, W + "r")
    run_properties = ET.SubElement(run, W + "rPr")
    if bold:
        ET.SubElement(run_properties, W + "b")
    run_color = ET.SubElement(run_properties, W + "color")
    run_color.set(W + "val", color)
    for tag in ("sz", "szCs"):
        node = ET.SubElement(run_properties, W + tag)
        node.set(W + "val", size)
    text_node = ET.SubElement(run, W + "t")
    text_node.set(XML_SPACE, "preserve")
    text_node.text = text
    return paragraph


def _document_control_table(fields: DocumentControlFields) -> ET.Element:
    table = ET.Element(W + "tbl")
    properties = ET.SubElement(table, W + "tblPr")
    width = ET.SubElement(properties, W + "tblW")
    width.set(W + "w", "5000")
    width.set(W + "type", "pct")
    borders = ET.SubElement(properties, W + "tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        border = ET.SubElement(borders, W + edge)
        border.set(W + "val", "single")
        border.set(W + "sz", "6")
        border.set(W + "space", "0")
        border.set(W + "color", "CBD5E1")

    for label, value in fields.rows:
        row = ET.SubElement(table, W + "tr")
        for column, text in enumerate((label, value)):
            cell = ET.SubElement(row, W + "tc")
            cell_properties = ET.SubElement(cell, W + "tcPr")
            cell_width = ET.SubElement(cell_properties, W + "tcW")
            cell_width.set(W + "w", "1800" if column == 0 else "7200")
            cell_width.set(W + "type", "dxa")
            margins = ET.SubElement(cell_properties, W + "tcMar")
            for edge in ("top", "left", "bottom", "right"):
                margin = ET.SubElement(margins, W + edge)
                margin.set(W + "w", "100" if edge in {"top", "bottom"} else "140")
                margin.set(W + "type", "dxa")
            if column == 0:
                shading = ET.SubElement(cell_properties, W + "shd")
                shading.set(W + "val", "clear")
                shading.set(W + "fill", "E8F1F8")
            cell.append(
                _document_control_paragraph(
                    text,
                    bold=column == 0,
                    size="20",
                    color="215868" if column == 0 else "1F2937",
                )
            )
    return table


def apply_document_control_page(
    docx_path: Path, fields: DocumentControlFields | None
) -> bool:
    """Append an optional next-page document-control section to a DOCX."""
    if fields is None:
        return False

    with ZipFile(docx_path, "r") as source:
        root = ET.fromstring(source.read("word/document.xml"))
        body = root.find("w:body", NS)
        if body is None:
            raise ValueError(f"El DOCX no contiene un cuerpo Word: {docx_path}")
        if any(
            node.get(W + "name") == "_MD2DOCX_DOCUMENT_CONTROL"
            for node in root.findall(".//w:bookmarkStart", NS)
        ):
            return False

        heading = _document_control_paragraph(
            fields.heading, bold=True, size="36", color="17365D"
        )
        bookmark_ids = [
            int(node.get(W + "id", "0"))
            for node in root.findall(".//w:bookmarkStart", NS)
            if node.get(W + "id", "0").isdigit()
        ]
        bookmark_id = str(max(bookmark_ids, default=0) + 1)
        start = ET.Element(W + "bookmarkStart")
        start.set(W + "id", bookmark_id)
        start.set(W + "name", "_MD2DOCX_DOCUMENT_CONTROL")
        end = ET.Element(W + "bookmarkEnd")
        end.set(W + "id", bookmark_id)
        heading.insert(1, start)
        heading.append(end)

        insert_at = len(body)
        if insert_at and body[insert_at - 1].tag == W + "sectPr":
            insert_at -= 1
        for element in (
            _next_page_section_break(),
            heading,
            _document_control_table(fields),
        ):
            body.insert(insert_at, element)
            insert_at += 1

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
    return True


def maybe_apply_style_template(
    output_docx: Path,
    style_template: Path | None,
    project_root: Path,
    cover_template: Path | None = None,
    cover_fields: CoverFields | None = None,
    document_control_fields: DocumentControlFields | None = None,
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

    apply_index_section_breaks(output_docx)
    apply_document_control_page(output_docx, document_control_fields)

    # Direct formatting goes last, so replacing styles/theme cannot erase it.
    apply_callout_formatting(output_docx)
