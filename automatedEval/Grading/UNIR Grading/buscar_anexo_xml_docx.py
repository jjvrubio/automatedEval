import zipfile
import xml.etree.ElementTree as ET
import os
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

def find_anexo_in_docx_xml(docx_path):
    with zipfile.ZipFile(docx_path) as docx_zip:
        with docx_zip.open('word/document.xml') as xml_file:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            anexo_lines = []
            for para in root.findall('.//w:p', ns):
                texts = []
                for t in para.findall('.//w:t', ns):
                    texts.append(t.text or '')
                full_text = ''.join(texts)
                if full_text and 'anex' in full_text.lower():
                    print(f"[ANEXO] {full_text}")
                    anexo_lines.append(full_text)
                # Buscar también en campos de numeración/caption
                for instr in para.findall('.//w:instrText', ns):
                    if instr.text and 'anex' in instr.text.lower():
                        print(f"[ANEXO-FIELD] {instr.text}")
                        anexo_lines.append(instr.text)
            if not anexo_lines:
                print("No se encontró ninguna línea/campo con 'anex' en el XML del DOCX.")
            return anexo_lines

def main():
    file_path = select_file(["docx"], "Selecciona el DOCX para buscar 'Anexo' en el XML")
    if not file_path:
        print("No file selected.")
        return
    print(f"Buscando 'Anexo' en el XML de: {file_path}")
    find_anexo_in_docx_xml(file_path)

if __name__ == "__main__":
    main()
