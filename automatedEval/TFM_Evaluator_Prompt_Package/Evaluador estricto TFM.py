import os
import pandas as pd
import openai
import pdfplumber
import docx
import logging
from dotenv import load_dotenv
from AppKit import NSOpenPanel  # ✅ USO EXPLÍCITO DE AppKit

# ------------------------------
# CONFIGURACIÓN OPENAI
# ------------------------------
def configurar_openai():
    load_dotenv()
    return openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ------------------------------
# UI NATIVA MAC (AppKit)
# ------------------------------
def seleccionar_archivo(allowed_types, titulo="Selecciona un archivo"):
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(allowed_types)
    panel.setTitle_(titulo)

    if panel.runModal() == 1:  # NSModalResponseOK == 1
        return panel.URLs()[0].path()
    return None

# ------------------------------
# CARGAR RÚBRICA
# ------------------------------
def cargar_rubrica(path):
    ext = os.path.splitext(path)[-1].lower()
    try:
        if ext == ".csv":
            with open(path, 'r', encoding='utf-8-sig') as f:
                first_line = f.readline()
                delimiter = ";" if ";" in first_line else ","
            return pd.read_csv(path, encoding='utf-8-sig', delimiter=delimiter)
        elif ext in [".xlsx", ".xls"]:
            return pd.read_excel(path)
        else:
            raise ValueError("Formato no soportado.")
    except Exception as e:
        print(f"❌ Error cargando rúbrica: {e}")
        return None

# ------------------------------
# LEER TFM (PDF O DOCX)
# ------------------------------
def leer_tfm(path):
    ext = os.path.splitext(path)[-1].lower()
    texto = ""

    if ext == ".pdf":
        logging.getLogger("pdfminer").setLevel(logging.ERROR)
        with pdfplumber.open(path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                contenido = page.extract_text()
                if contenido:
                    texto += f"\n--- Página {page_num + 1} ---\n{contenido}\n"
    elif ext == ".docx":
        doc = docx.Document(path)
        texto = "\n".join(para.text for para in doc.paragraphs)
    else:
        raise ValueError("Formato no soportado (solo PDF o DOCX).")

    return texto

# ------------------------------
# EVALUAR UN CRITERIO CON OPENAI
# ------------------------------
def evaluar_criterio(client, criterio, texto_tfm):
    prompt = f"""Eres un evaluador académico experto siguiendo los criterios de UNIR. Evalúa el siguiente trabajo según el criterio:

Criterio:
{criterio}

Trabajo del TFM:
{texto_tfm}

Responde estrictamente con Nivel 1, Nivel 2, Nivel 3 o Nivel 4 seguido de una justificación crítica y detallada.

Ejemplo:
Nivel 3: La respuesta presenta adecuación parcial...
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content

# ------------------------------
# EVALUAR TFM COMPLETO
# ------------------------------
def evaluar_tfm_completo(client, rubrica_df, texto_tfm):
    resultados = []
    for criterio in rubrica_df.iloc[:, 0]:
        print(f"\n🧠 Evaluando criterio: {criterio}")
        evaluacion = evaluar_criterio(client, criterio, texto_tfm)
        resultados.append({"criterio": criterio, "evaluacion": evaluacion})
    return resultados

# ------------------------------
# EXPORTAR RESULTADOS
# ------------------------------
def exportar_resultados(resultados, csv_path, md_path):
    pd.DataFrame(resultados).to_csv(csv_path, index=False)
    print(f"✅ CSV generado: {csv_path}")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Informe de Evaluación TFM\n\n")
        for res in resultados:
            f.write(f"## Criterio: {res['criterio']}\n")
            f.write(f"**Evaluación:** {res['evaluacion']}\n\n")
    print(f"✅ Markdown generado: {md_path}")

# ------------------------------
# MAIN
# ------------------------------
def main():
    client = configurar_openai()

    ruta_rubrica = seleccionar_archivo(["xlsx", "xls", "csv"], "Selecciona la rúbrica")
    if not ruta_rubrica:
        print("❗ No se seleccionó ninguna rúbrica.")
        return

    rubrica = cargar_rubrica(ruta_rubrica)
    if rubrica is None:
        return

    ruta_tfm = seleccionar_archivo(["pdf", "docx"], "Selecciona el TFM (PDF o DOCX)")
    if not ruta_tfm:
        print("❗ No se seleccionó ningún archivo de TFM.")
        return

    texto = leer_tfm(ruta_tfm)

    resultados = evaluar_tfm_completo(client, rubrica, texto)

    exportar_resultados(resultados, "evaluacion_tfm_resultado.csv", "evaluacion_tfm_informe.md")

# ------------------------------
# EJECUCIÓN
# ------------------------------
if __name__ == "__main__":
    main()
