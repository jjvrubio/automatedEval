import json
import os
from typing import List
from AppKit import NSOpenPanel, NSApplication

def read_json_file(file_path: str) -> List[str]:
    """Read the JSON file and return the references list."""
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Extract the references list from the dictionary
        if "references" in data and isinstance(data["references"], list):
            return data["references"]
        else:
            raise ValueError("El archivo JSON no contiene la clave 'references' o no es una lista.")

def write_markdown_file(file_path: str, content: str):
    """Write content to a Markdown file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def analyze_reference(reference: str) -> dict:
    """Analyze a reference string for APA compliance."""
    # Simple rules to check for APA elements (expand as needed)
    has_author = bool(reference.split('.')[0])  # Assume the first segment is the author
    has_year = "(" in reference and ")" in reference
    has_title = any(word.istitle() for word in reference.split())  # Check for capitalized words
    has_url = "http" in reference

    # Determine overall compliance
    is_compliant = has_author and has_year and has_title and has_url

    return {
        "reference": reference,
        "author": has_author,
        "year": has_year,
        "title": has_title,
        "url": has_url,
        "is_compliant": is_compliant
    }

def generate_markdown_report(references: List[str], report_path: str):
    """Generate a Markdown report from the analyzed references."""
    report_lines = ["# Informe de Cumplimiento de Referencias\n"]
    report_lines.append("Este informe detalla el estado de cumplimiento de las referencias en formato APA 7.\n")

    for i, reference in enumerate(references, start=1):
        analysis = analyze_reference(reference)
        # Add details to the Markdown report
        report_lines.append(f"## Referencia {i}\n")
        report_lines.append(f"**Texto:** {analysis['reference']}\n")
        report_lines.append(f"**Autor:** {'✔️' if analysis['author'] else '❌'}\n")
        report_lines.append(f"**Año:** {'✔️' if analysis['year'] else '❌'}\n")
        report_lines.append(f"**Título:** {'✔️' if analysis['title'] else '❌'}\n")
        report_lines.append(f"**URL:** {'✔️' if analysis['url'] else '❌'}\n")
        report_lines.append(f"**Cumplimiento APA 7:** {'✔️ Cumple' if analysis['is_compliant'] else '❌ No cumple'}\n")
        report_lines.append("\n")

    # Write the report to a Markdown file
    write_markdown_file(report_path, "\n".join(report_lines))

def select_file() -> str:
    """Open a file dialog to select a JSON file and return its path."""
    NSApplication.sharedApplication()
    panel = NSOpenPanel.alloc().init()
    panel.setTitle_("Seleccione el archivo JSON de referencias")
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["json"])
    
    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None

def main():
    # Select the JSON file
    input_path = select_file()
    if not input_path:
        print("No se seleccionó ningún archivo.")
        return

    # Generate the report path in the same folder as the input file
    report_path = os.path.splitext(input_path)[0] + '_informe_cumplimiento.md'

    try:
        # Read the JSON file
        references = read_json_file(input_path)
        if not references:
            print("No se encontraron referencias en el archivo JSON.")
            return

        # Generate the Markdown report
        generate_markdown_report(references, report_path)
        print(f"Informe de cumplimiento generado en {report_path}")
    except ValueError as e:
        print(f"Error en el formato del JSON: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
