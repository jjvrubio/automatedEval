import openai
import json
import os
import docx
import pdfplumber
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
    text_parts = [para.text for para in doc.paragraphs]
    return "\n".join(text_parts)

def main():
    api_key = os.environ.get("MI_CLAVE_API_OPENAI")
    if not api_key:
        print("ERROR: No se encontró la variable de entorno MI_CLAVE_API_OPENAI. Por favor, expórtala antes de ejecutar el script.")
        return
    ref_file = select_file(["json"], "Selecciona el archivo de referencias APA (JSON)")
    if not ref_file:
        print("No se seleccionó archivo de referencias.")
        return
    with open(ref_file, encoding='utf-8') as f:
        referencias = json.load(f)
    tfm_file = select_file(["pdf", "docx", "txt"], "Selecciona el archivo del TFM (PDF, DOCX o TXT)")
    if not tfm_file:
        print("No se seleccionó archivo de TFM.")
        return
    ext = os.path.splitext(tfm_file)[-1].lower()
    if ext == ".pdf":
        cuerpo = extract_text_from_pdf(tfm_file)
    elif ext == ".docx":
        cuerpo = extract_text_from_docx(tfm_file)
    elif ext == ".txt":
        with open(tfm_file, encoding='utf-8') as f:
            cuerpo = f.read()
    else:
        print("Formato no soportado.")
        return
    prompt = f"""
Dado el siguiente cuerpo de texto académico y la lista de referencias bibliográficas en formato APA 7, realiza lo siguiente:
1. Extrae todas las citas en formato APA (por ejemplo, (Apellido, año), (Apellido1 & Apellido2, año), (Apellido et al., año), etc.) que aparecen en el texto.
2. Indica para cada cita si existe una referencia correspondiente en la lista de referencias (por autor y año).
3. Indica para cada referencia si está citada en el texto.
4. Si detectas errores de formato o inconsistencias, indícalo.

Texto del TFM:
"""
    prompt += cuerpo[:12000]
    prompt += "\n\nLista de referencias APA:\n"
    prompt += '\n'.join(referencias)
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un experto en normas APA y revisión académica."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        temperature=0.2
    )
    print(response.choices[0].message.content)
    # Guardar resultado en un archivo .md
    output_dir = os.path.dirname(tfm_file)
    base_name = os.path.splitext(os.path.basename(tfm_file))[0]
    md_path = os.path.join(output_dir, f"{base_name}_VALIDACION_CITAS.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(response.choices[0].message.content)
    print(f"\nEl resultado también se ha guardado en: {md_path}")

if __name__ == "__main__":
    main()
