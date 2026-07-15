from __future__ import annotations

import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import quoteattr
from zipfile import ZipFile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from md2docx.postprocess import (  # noqa: E402
    NS,
    W,
    apply_document_control_page,
    apply_index_section_breaks,
    extract_commercial_cover,
    extract_document_control,
    extract_metadata_cover,
)


def _document_xml(body_content: str) -> bytes:
    return (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W[1:-1]}"><w:body>{body_content}'
        "<w:sectPr/></w:body></w:document>"
    ).encode()


class CommercialCoverTests(unittest.TestCase):
    def test_yaml_title_is_the_commercial_cover_title(self) -> None:
        markdown = """---
title: "Título canónico del YAML"
date: "2026-07-15"
---

# Propuesta comercial
# Título antiguo del bloque
## Línea secundaria

> **Cliente:** Ejemplo

---
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proposal.md"
            path.write_text(markdown, encoding="utf-8")
            fields = extract_commercial_cover(path)

        self.assertEqual(fields.title, "Título canónico del YAML")
        self.assertEqual(fields.subtitle, "Propuesta comercial")

    def test_yaml_title_removes_need_for_repeated_title_heading(self) -> None:
        markdown = """---
title: "Oferta sin título repetido"
---

# Propuesta comercial
## Caso de prueba

---
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proposal.md"
            path.write_text(markdown, encoding="utf-8")
            fields = extract_commercial_cover(path)

        self.assertEqual(fields.title, "Oferta sin título repetido")
        self.assertEqual(fields.subtitle, "Propuesta comercial")


class MetadataCoverTests(unittest.TestCase):
    def test_spanish_aliases_fill_native_cover(self) -> None:
        markdown = """---
titulo: De puntos a experiencias
subtitulo: Un artículo Beyond Trade
autor: Convercus
fecha: '2026-06-15'
---
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "article.md"
            path.write_text(markdown, encoding="utf-8")
            fields = extract_metadata_cover(path)

        self.assertEqual(fields.title, "De puntos a experiencias")
        self.assertEqual(fields.subtitle, "Un artículo Beyond Trade")
        self.assertEqual(fields.supporting_lines, ("Convercus",))
        self.assertEqual(fields.year, "2026")
        self.assertEqual(fields.creator, "Convercus")


class DocumentControlTests(unittest.TestCase):
    def test_missing_or_false_switch_does_not_generate_page(self) -> None:
        documents = (
            "---\ntitle: Documento\n---\n",
            "---\ntitle: Documento\ndocument_control: false\n---\n",
            "---\ntitle: Documento\ncontrol_documento: no\n---\n",
        )
        for markdown in documents:
            with self.subTest(markdown=markdown), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "document.md"
                path.write_text(markdown, encoding="utf-8")
                self.assertIsNone(extract_document_control(path))

    def test_true_switch_collects_standard_spanish_fields(self) -> None:
        markdown = """---
titulo: Documento de prueba
subtitulo: Subtítulo de prueba
idioma: es
version: v1.2
estado: final
fecha: '2026-07-15'
tags:
  - publicación
  - fidelización
document_control: activo
---
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.md"
            path.write_text(markdown, encoding="utf-8")
            fields = extract_document_control(path)

        assert fields is not None
        self.assertEqual(fields.heading, "Control del documento")
        self.assertEqual(
            fields.rows,
            (
                ("Título", "Documento de prueba"),
                ("Subtítulo", "Subtítulo de prueba"),
                ("Idioma", "es"),
                ("Fecha", "2026-07-15"),
                ("Versión", "v1.2"),
                ("Estado", "final"),
                ("Tags", "publicación, fidelización"),
            ),
        )

    def test_custom_control_fields_can_replace_standard_fields(self) -> None:
        markdown = """---
title: Documento de prueba
document_control:
  enabled: true
  heading: Ficha de publicación
  include_standard_fields: false
  fields:
    Propietario: Equipo editorial
    Canal: Web
---
"""
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.md"
            path.write_text(markdown, encoding="utf-8")
            fields = extract_document_control(path)

        assert fields is not None
        self.assertEqual(fields.heading, "Ficha de publicación")
        self.assertEqual(
            fields.rows,
            (("Propietario", "Equipo editorial"), ("Canal", "Web")),
        )

    def test_page_is_appended_once_before_final_section_properties(self) -> None:
        markdown = """---
title: Documento de prueba
version: v1.0
document_control: true
---
"""
        with tempfile.TemporaryDirectory() as directory:
            markdown_path = Path(directory) / "document.md"
            markdown_path.write_text(markdown, encoding="utf-8")
            fields = extract_document_control(markdown_path)
            docx_path = Path(directory) / "document.docx"
            with ZipFile(docx_path, "w") as archive:
                archive.writestr(
                    "word/document.xml",
                    _document_xml('<w:p><w:r><w:t>Contenido</w:t></w:r></w:p>'),
                )

            self.assertTrue(apply_document_control_page(docx_path, fields))
            self.assertFalse(apply_document_control_page(docx_path, fields))
            with ZipFile(docx_path) as archive:
                root = ET.fromstring(archive.read("word/document.xml"))

        body = root.find("w:body", NS)
        assert body is not None
        children = list(body)
        self.assertEqual(children[-1].tag, W + "sectPr")
        self.assertEqual(children[-2].tag, W + "tbl")
        self.assertIsNotNone(children[-4].find("w:pPr/w:sectPr/w:type", NS))
        self.assertEqual(
            len(root.findall(".//w:bookmarkStart[@w:name='_MD2DOCX_DOCUMENT_CONTROL']", NS)),
            1,
        )


class IndexSectionBreakTests(unittest.TestCase):
    def _make_docx(self, body_content: str, directory: str) -> Path:
        path = Path(directory) / "document.docx"
        with ZipFile(path, "w") as archive:
            archive.writestr("word/document.xml", _document_xml(body_content))
        return path

    def _body(self, path: Path) -> ET.Element:
        with ZipFile(path) as archive:
            root = ET.fromstring(archive.read("word/document.xml"))
        body = root.find("w:body", NS)
        assert body is not None
        return body

    def test_break_after_supported_simple_index_fields(self) -> None:
        instructions = (
            'TOC \\o "1-3" \\h',
            'TOC \\c "Figure" \\h',
            'TOC \\c "Table" \\h',
            'INDEX \\e "  " \\h "A"',
        )
        for instruction in instructions:
            with self.subTest(instruction=instruction), tempfile.TemporaryDirectory() as directory:
                body_content = (
                    f'<w:p><w:fldSimple w:instr={quoteattr(instruction)}/></w:p>'
                    '<w:p><w:r><w:t>Contenido</w:t></w:r></w:p>'
                )
                path = self._make_docx(body_content, directory)

                self.assertEqual(apply_index_section_breaks(path), 1)

                children = list(self._body(path))
                section = children[1].find("w:pPr/w:sectPr/w:type", NS)
                self.assertIsNotNone(section)
                self.assertEqual(section.get(W + "val"), "nextPage")

    def test_break_follows_end_of_complex_field(self) -> None:
        body_content = (
            '<w:p><w:r><w:fldChar w:fldCharType="begin"/></w:r>'
            '<w:r><w:instrText>TOC \\o "1-3"</w:instrText></w:r></w:p>'
            '<w:p><w:r><w:t>Resultado almacenado</w:t></w:r>'
            '<w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>'
            '<w:p><w:r><w:t>Contenido</w:t></w:r></w:p>'
        )
        with tempfile.TemporaryDirectory() as directory:
            path = self._make_docx(body_content, directory)
            self.assertEqual(apply_index_section_breaks(path), 1)
            children = list(self._body(path))

        self.assertIsNotNone(children[2].find("w:pPr/w:sectPr/w:type", NS))

    def test_existing_next_page_section_is_not_duplicated(self) -> None:
        body_content = (
            '<w:p><w:fldSimple w:instr="TOC \\o &quot;1-3&quot;"/></w:p>'
            '<w:p><w:pPr><w:sectPr><w:type w:val="nextPage"/>'
            '</w:sectPr></w:pPr></w:p>'
        )
        with tempfile.TemporaryDirectory() as directory:
            path = self._make_docx(body_content, directory)
            self.assertEqual(apply_index_section_breaks(path), 0)


if __name__ == "__main__":
    unittest.main()
