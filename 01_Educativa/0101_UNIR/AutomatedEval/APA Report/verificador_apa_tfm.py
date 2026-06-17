import re
import pdfplumber
import docx
import os
import json
import zipfile
import xml.etree.ElementTree as ET
from AppKit import NSApplication
from Cocoa import NSOpenPanel


def select_file(allowed_types, title):
    NSApplication.sharedApplication()
    panel = NSOpenPanel.openPanel()
    panel.setAllowedFileTypes_(allowed_types)
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setTitle_(title)
    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None


def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text_parts = []
    # Extraer texto de párrafos normales
    text_parts.extend(para.text for para in doc.paragraphs)
    # Extraer texto de tablas
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                cell_text = cell.text.strip()
                if cell_text:
                    text_parts.append(cell_text)
    # Extraer texto de encabezados y pies de página
    for section in doc.sections:
        header = section.header
        footer = section.footer
        if header:
            text_parts.extend(
                para.text for para in header.paragraphs if para.text.strip()
            )
        if footer:
            text_parts.extend(
                para.text for para in footer.paragraphs if para.text.strip()
            )
    return "\n".join(text_parts)


def find_first_line_with_anex(lines):
    # Busca la primera línea que contenga 'anex' (sin tildes, sin importar mayúsculas/minúsculas)
    for i, line in enumerate(lines):
        # Normaliza la línea: minúsculas y sin tildes
        norm_line = line.lower()
        norm_line = (
            norm_line.replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
        )
        if "anex" in norm_line:
            print(
                f"[find_first_line_with_anex] Posible fin de referencias en la línea {i}: {repr(line)}"
            )
            return i
    return None


def extract_references_section(text):
    lines = text.splitlines()
    ref_indices = []
    for i, line in enumerate(lines):
        if re.search(
            r"REFERENCIAS|REFERENCIAS BIBLIOGRÁFICAS|BIBLIOGRAF[IÍ]A",
            line,
            re.IGNORECASE,
        ):
            print(f"Sección de referencias encontrada en la línea {i}: {repr(line)}")
            ref_indices.append(i)
    if not ref_indices:
        print("No se encontró la sección de referencias.")
        return []
    # Usar la última ocurrencia encontrada
    ref_start = ref_indices[-1]
    # Buscar la primera línea con 'anex' después de la sección de referencias
    ref_end = find_first_line_with_anex(lines[ref_start + 1 :])
    if ref_end is not None:
        ref_end = ref_start + 1 + ref_end
        print(
            f"Fin de referencias (por coincidencia parcial) en la línea {ref_end}: {repr(lines[ref_end])}"
        )
    return (
        lines[ref_start + 1 : ref_end]
        if ref_end is not None
        else lines[ref_start + 1 :]
    )


def extract_apa_citations(text):
    # APA: (Apellido, año), (Apellido1 & Apellido2, año), (Apellido et al., año), etc.
    # Permitir espacios, tildes, y variantes de separación
    # Ejemplo: (García & Pérez, 2020), (Smith et al., 2019), (López, 2021a)
    pattern = r"\(([^\)]+?),\s*(\d{4}[a-z]?)\)"
    matches = re.findall(pattern, text)
    citations = set()
    for match in matches:
        authors = match[0]
        year = match[1]
        # Normalizar autores: quitar tildes, minúsculas, quitar 'et al.' y espacios extra
        norm_authors = authors.lower()
        norm_authors = (
            norm_authors.replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
        )
        norm_authors = re.sub(r"et al\.|&", "", norm_authors)
        norm_authors = re.sub(r"[^a-zñ .,]", "", norm_authors)
        norm_authors = norm_authors.strip()
        # Tomar solo el primer apellido para el cruce, pero guardar la cita completa
        primer_apellido = norm_authors.split(",")[0].split()[0]
        citations.add(f"{primer_apellido}, {year}")
    return citations


def extract_apa_references(ref_lines):
    # Patrón flexible para referencias APA: varios autores, instituciones, fechas compuestas, et al., &
    pattern = re.compile(
        r"""
        ^([A-ZÁÉÍÓÚÑ][a-záéíóúñA-ZÁÉÍÓÚÑ][^()]*?)\s*\((\d{4}(?:,? [^\)]*)?)\)
    """,
        re.VERBOSE,
    )
    apa_references = set()
    non_apa_references = set()
    apa_keys = set()  # Para el cruce: primer apellido, año
    for line in ref_lines:
        m = pattern.match(line)
        if m:
            apa_references.add(line.strip())  # Guardar la referencia completa
            # Extraer primer apellido y año para el cruce
            authors = m.group(1)
            year = m.group(2)
            norm_authors = authors.lower()
            norm_authors = (
                norm_authors.replace("á", "a")
                .replace("é", "e")
                .replace("í", "i")
                .replace("ó", "o")
                .replace("ú", "u")
            )
            norm_authors = re.sub(r"et al\.|&", "", norm_authors)
            norm_authors = re.sub(r"[^a-zñ .,]", "", norm_authors)
            norm_authors = norm_authors.strip()
            primer_apellido = norm_authors.split(",")[0].split()[0]
            apa_keys.add(f"{primer_apellido}, {year}")
        elif line.strip():
            non_apa_references.add(line.strip())
    return apa_references, non_apa_references, apa_keys


def join_reference_lines(ref_lines, max_length=500):
    # Une líneas de referencia: nueva referencia si línea empieza con mayúscula y año entre paréntesis
    # Si una referencia unida supera max_length caracteres, lanza advertencia
    joined = []
    buffer = ""
    ref_start_pattern = re.compile(r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñA-ZÁÉÍÓÚÑ0-9 .,&-]+\(\d{4}")
    for line in ref_lines:
        if ref_start_pattern.match(line.strip()):
            if buffer:
                if len(buffer.strip()) > max_length:
                    print(
                        f"[ADVERTENCIA] Referencia sospechosamente larga ({len(buffer.strip())} caracteres): {repr(buffer.strip())[:200]}..."
                    )
                joined.append(buffer.strip())
            buffer = line.strip()
        else:
            buffer += " " + line.strip()
    if buffer:
        if len(buffer.strip()) > max_length:
            print(
                f"[ADVERTENCIA] Referencia sospechosamente larga ({len(buffer.strip())} caracteres): {repr(buffer.strip())[:200]}..."
            )
        joined.append(buffer.strip())
    return joined


def get_paragraphs_with_terms_from_docx_xml(docx_path, terms):
    """Devuelve una lista de (idx, texto) de párrafos/campos que contienen alguno de los términos (case-insensitive, sin tildes)."""

    def normalize(s):
        return (
            s.lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
        )

    with zipfile.ZipFile(docx_path) as docx_zip:
        with docx_zip.open("word/document.xml") as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            results = []
            idx = 0
            for para in root.findall(".//w:p", ns):
                texts = []
                for t in para.findall(".//w:t", ns):
                    texts.append(t.text or "")
                full_text = "".join(texts)
                norm_text = normalize(full_text)
                if any(term in norm_text for term in terms):
                    results.append((idx, full_text))
                # Buscar también en campos de numeración/caption
                for instr in para.findall(".//w:instrText", ns):
                    if instr.text:
                        norm_instr = normalize(instr.text)
                        if any(term in norm_instr for term in terms):
                            results.append((idx, instr.text))
                idx += 1
            return results


def extract_references_section_docx_xml(docx_path):
    """Extrae la sección de referencias usando el XML, cortando en la primera 'anex' tras la última referencia."""
    # Buscar índices de referencias y anexos
    ref_terms = ["referencias", "referencias bibliograficas", "bibliografia"]
    anex_terms = ["anex"]
    ref_paras = get_paragraphs_with_terms_from_docx_xml(docx_path, ref_terms)
    anex_paras = get_paragraphs_with_terms_from_docx_xml(docx_path, anex_terms)
    if not ref_paras:
        print("[XML] No se encontró la sección de referencias en el XML.")
        return []
    ref_start_idx = ref_paras[-1][0]
    # Buscar el primer 'anex' después de la última referencia
    anex_after_ref = [idx for idx, txt in anex_paras if idx > ref_start_idx]
    if anex_after_ref:
        ref_end_idx = anex_after_ref[0]
        print(
            f"[XML] Fin de referencias en el párrafo {ref_end_idx} (por 'anex'): {anex_paras[anex_after_ref.index(ref_end_idx)][1]}"
        )
    else:
        ref_end_idx = None
    # Extraer todos los párrafos entre ref_start_idx+1 y ref_end_idx
    with zipfile.ZipFile(docx_path) as docx_zip:
        with docx_zip.open("word/document.xml") as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
            all_paras = []
            for para in root.findall(".//w:p", ns):
                texts = []
                for t in para.findall(".//w:t", ns):
                    texts.append(t.text or "")
                full_text = "".join(texts)
                all_paras.append(full_text)
            if ref_end_idx is not None:
                return all_paras[ref_start_idx + 1 : ref_end_idx]
            else:
                return all_paras[ref_start_idx + 1 :]


def ref_key_from_reference(ref):
    m = re.match(r"^([A-ZÁÉÍÓÚÑ][a-záéíóúñA-ZÁÉÍÓÚÑ .,&-]+)\s*\((\d{4}[a-z]?)", ref)
    if m:
        autores = m.group(1)
        year = m.group(2)
        norm_autores = autores.lower()
        norm_autores = (
            norm_autores.replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
        )
        norm_autores = re.sub(r"et al\\.|&", "", norm_autores)
        norm_autores = re.sub(r"[^a-zñ .,]", "", norm_autores)
        norm_autores = norm_autores.strip()
        primer_apellido = norm_autores.split(",")[0].split()[0]
        return f"{primer_apellido}, {year}"
    return None


def debug_print_claves(apa_keys, citations):
    print("\n[DEBUG] Claves de referencias (primer apellido, año):", sorted(apa_keys))
    print(
        "[DEBUG] Claves de citas encontradas (primer apellido, año):", sorted(citations)
    )
    print("[DEBUG] Referencias NO citadas reales:", sorted(apa_keys - citations))
    print("[DEBUG] Citas SIN referencia real:", sorted(citations - apa_keys))


def main():
    file_path = select_file(["pdf", "docx"], "Selecciona el TFM (PDF o DOCX)")
    if not file_path:
        print("No file selected.")
        return
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
        ref_lines = extract_references_section(text)
    elif ext == ".docx":
        # Usar el XML para cortar referencias de forma robusta
        ref_lines = extract_references_section_docx_xml(file_path)
        text = extract_text_from_docx(file_path)
    else:
        print("Formato no soportado.")
        return
    print("Líneas extraídas de referencias:")
    for l in ref_lines:
        print(repr(l))
    joined_refs = join_reference_lines(ref_lines)
    print("\nReferencias unidas:")
    for l in joined_refs:
        print(repr(l))
    citations = extract_apa_citations(text)
    apa_references, non_apa_references, apa_keys = extract_apa_references(joined_refs)
    # Verificación cruzada usando solo primer apellido y año
    not_cited = apa_keys - citations
    not_referenced = citations - apa_keys
    debug_print_claves(apa_keys, citations)
    # Guardar claves para depuración
    out_dir = os.path.dirname(file_path)
    out_base = os.path.splitext(os.path.basename(file_path))[0]
    with open(
        os.path.join(out_dir, f"{out_base}_claves_referencias.json"),
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(sorted(list(apa_keys)), f, ensure_ascii=False, indent=2)
    with open(
        os.path.join(out_dir, f"{out_base}_claves_citas.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(sorted(list(citations)), f, ensure_ascii=False, indent=2)
    print(f"Citas encontradas: {len(citations)}")
    print(f"Referencias APA encontradas: {len(apa_references)}")
    print(f"Referencias NO citadas (APA): {not_cited}")
    print(f"Citas SIN referencia (APA): {not_referenced}")
    print(f"Referencias que NO cumplen APA: {len(non_apa_references)}")
    for ref in non_apa_references:
        print(f"NO APA: {ref}")
    # Guardar resultados
    print(f"[DEBUG] Guardando citas: {citations}")
    print(f"[DEBUG] Guardando referencias APA: {apa_references}")
    print(f"[DEBUG] Guardando referencias NO APA: {non_apa_references}")
    if not citations:
        print("[ADVERTENCIA] El conjunto de citas está vacío antes de guardar el JSON.")
    if not apa_references:
        print(
            "[ADVERTENCIA] El conjunto de referencias APA está vacío antes de guardar el JSON."
        )
    if not non_apa_references:
        print(
            "[ADVERTENCIA] El conjunto de referencias NO APA está vacío antes de guardar el JSON."
        )
    with open(
        os.path.join(out_dir, f"{out_base}_citas.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(sorted(list(citations)), f, ensure_ascii=False, indent=2)
    with open(
        os.path.join(out_dir, f"{out_base}_referencias_apa.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(sorted(list(apa_references)), f, ensure_ascii=False, indent=2)
    with open(
        os.path.join(out_dir, f"{out_base}_referencias_no_apa.json"),
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(sorted(list(non_apa_references)), f, ensure_ascii=False, indent=2)
    # Guardar referencias no citadas y citas sin referencia
    with open(
        os.path.join(out_dir, f"{out_base}_referencias_no_citadas.json"),
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(sorted(list(not_cited)), f, ensure_ascii=False, indent=2)
    with open(
        os.path.join(out_dir, f"{out_base}_citas_sin_referencia.json"),
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(sorted(list(not_referenced)), f, ensure_ascii=False, indent=2)
    print("Resultados guardados en JSON.")


if __name__ == "__main__":
    main()
