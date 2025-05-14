import re
import os
from typing import List
from AppKit import NSOpenPanel, NSApplication

def read_markdown_file(file_path: str) -> str:
    """Leer el contenido de un archivo Markdown."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_markdown_file(file_path: str, content: str):
    """Escribir contenido en un archivo Markdown."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def check_apa_compliance(reference: str) -> str:
    """Verificar si una referencia cumple con el formato APA 7."""
    # Patrones simples de expresiones regulares para el formato APA 7
    patterns = {
        'autor': r'^[A-Z][a-z]+, [A-Z]\.',
        'año': r'\(\d{4}\)',
        'título': r'\. [A-Z][a-z]+',
        'fuente': r'\. [A-Z][a-z]+'
    }
    
    problemas = []
    for clave, patron in patterns.items():
        if not re.search(patron, reference):
            problemas.append(f"Falta o es incorrecto el formato de {clave}.")
    
    if problemas:
        return "Problemas encontrados: " + "; ".join(problemas)
    else:
        return "Cumple con el formato APA 7."

def filter_references(references: List[str]) -> List[str]:
    """Filtrar líneas que comienzan con 'Bibliography Section' o son cabeceras de sección."""
    filtered_references = []
    skip_next = False  # Flag to skip the line following "Bibliography Section"

    for ref in references:
        ref = ref.strip()  # Remove leading/trailing whitespace
        if skip_next:
            skip_next = False  # Reset the flag
            continue
        # Skip lines starting with "Bibliography Section" or Markdown headers
        if ref.lower().startswith("bibliography section") or ref.startswith("#"):
            skip_next = True  # Skip the next line
            continue
        if ref:  # Exclude empty lines
            filtered_references.append(ref)

    return filtered_references

def generate_report(references: List[str], report_path: str):
    """Generar un informe de cumplimiento en formato Markdown."""
    # Filtrar referencias antes de procesarlas
    filtered_references = filter_references(references)
    
    report_lines = ["# Informe de Cumplimiento APA 7\n"]
    
    for i, reference in enumerate(filtered_references, start=1):
        compliance_result = check_apa_compliance(reference)
        report_lines.append(f"## Referencia {i}\n")
        report_lines.append(f"**Referencia:** {reference}\n")
        report_lines.append(f"**Verificación de Cumplimiento:** {compliance_result}\n")
        report_lines.append("\n")
    
    write_markdown_file(report_path, "\n".join(report_lines))

def select_file() -> str:
    """Abrir un cuadro de diálogo para seleccionar un archivo y devolver la ruta del archivo."""
    NSApplication.sharedApplication()
    panel = NSOpenPanel.alloc().init()
    panel.setTitle_("Seleccione el archivo de bibliografía")
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["md"])
    
    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None

def main():
    # Seleccionar el archivo de bibliografía
    input_path = select_file()
    if not input_path:
        print("No se seleccionó ningún archivo.")
        return

    # Generar la ruta del informe en la misma carpeta que el archivo fuente
    report_path = os.path.splitext(input_path)[0] + '_informe_cumplimiento.md'

    # Leer el archivo de bibliografía
    bibliography_content = read_markdown_file(input_path)
    
    # Dividir el contenido en referencias individuales (suponiendo que cada referencia está en una nueva línea)
    references = bibliography_content.split('\n')
    
    # Generar el informe de cumplimiento
    generate_report(references, report_path)
    
    print(f"Informe de cumplimiento generado en {report_path}")

if __name__ == "__main__":
    main()
