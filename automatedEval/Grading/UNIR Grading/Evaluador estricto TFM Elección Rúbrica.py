import os
import pandas as pd
import openai
import pdfplumber
import docx
import logging
from dotenv import load_dotenv
from AppKit import NSApplication, NSOpenPanel

# Inicializando AppKit (puede tardar unos segundos la primera vez)...
NSApp = NSApplication.sharedApplication()

def configurar_openai():
# #     print("Entrando en configurar_openai()")
    load_dotenv()
    api_key = os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        raise ValueError("❌ No se encontró la clave API en el archivo .env")
    return openai.OpenAI(api_key=api_key)

def configurar_logger():
#     print("Entrando en configurar_logger()")
    log_path = "evaluador_tfm.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_path, mode='w', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("evaluador_tfm")

def seleccionar_archivo(allowed_types, titulo, mensaje):
#     print("Entrando en seleccionar_archivo()")
    NSApp.activateIgnoringOtherApps_(True)
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(allowed_types)
    panel.setTitle_(titulo)
    panel.setMessage_(mensaje)
    if panel.runModal() == 1:
#         print("Archivo seleccionado en seleccionar_archivo()")
        return panel.URLs()[0].path()
#     print("No se seleccionó archivo en seleccionar_archivo()")
    return None

def cargar_rubrica(path, logger):
#     print("Entrando en cargar_rubrica()")
    ext = os.path.splitext(path)[-1].lower()
    try:
        if ext == ".csv":
            with open(path, 'r', encoding='utf-8-sig') as f:
                first_line = f.readline()
                delimiter = ";" if ";" in first_line else ","
            df = pd.read_csv(path, encoding='utf-8-sig', delimiter=delimiter)
        elif ext in [".xlsx", ".xls"]:
            df = pd.read_excel(path)
        else:
            raise ValueError("Formato no soportado.")
        logger.info("✅ Rúbrica cargada correctamente.")
        return df
    except Exception as e:
        logger.error(f"❌ Error cargando rúbrica: {e}")
        return None

def cargar_instrucciones_md_opcional(ruta_md, logger):
#     print("Entrando en cargar_instrucciones_md_opcional()")
    if os.path.exists(ruta_md):
        try:
            with open(ruta_md, "r", encoding="utf-8") as f:
                instrucciones = f.read()
            logger.info(f"📘 Instrucciones ultraestrictas cargadas desde: {ruta_md}")
            return instrucciones
        except Exception as e:
            logger.error(f"❌ Error leyendo el archivo de instrucciones: {e}")
    else:
        logger.warning(f"⚠️ No se encontró el archivo de instrucciones en: {ruta_md}")
    return ""

def leer_tfm(path, logger):
#     print("Entrando en leer_tfm()")
    ext = os.path.splitext(path)[-1].lower()
    texto = ""
    try:
        if ext == ".pdf":
            logger.info("📥 Leyendo PDF...")
            logging.getLogger("pdfminer").setLevel(logging.ERROR)
            with pdfplumber.open(path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    contenido = page.extract_text()
                    if contenido:
                        texto += f"\n--- Página {page_num + 1} ---\n{contenido}\n"
        elif ext == ".docx":
            logger.info("📥 Leyendo DOCX...")
            doc = docx.Document(path)
            texto = "\n".join(para.text for para in doc.paragraphs)
        else:
            raise ValueError("Formato no soportado (solo PDF o DOCX).")
        logger.info("✅ Lectura del TFM completada.")
    except Exception as e:
        logger.error(f"❌ Error leyendo el TFM: {e}")
    return texto

def evaluar_criterio(client, criterio, texto_tfm, instrucciones_base):
#     print("Entrando en evaluar_criterio()")
    prompt = f"{instrucciones_base.strip()}\n\n" if instrucciones_base.strip() else ""
    prompt += f"""Ahora evalúa el siguiente trabajo según el criterio:

Criterio:
{criterio}

Trabajo del TFM (solo para consulta, NO lo repitas en la respuesta):
{texto_tfm}

Responde SOLO con el nivel (Nivel 1, 2, 3 o 4) y una justificación crítica y detallada. NO repitas el texto del TFM en tu respuesta.
"""
    logging.getLogger("evaluador_tfm").info(f"Prompt enviado a OpenAI para el criterio '{criterio}':\n{prompt[:2000]}... [truncado]")
    modelo_llm = "gpt-4o"
    response = client.chat.completions.create(
        model=modelo_llm,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

def evaluar_tfm_completo(client, rubrica_df, texto_tfm, instrucciones_base, logger):
#     print("Entrando en evaluar_tfm_completo()")
    resultados = []
    palabras_excluir = [
        "presentación", "exposición", "comunicación", "tribunal", "formato de la presentación"
    ]
    for criterio in rubrica_df.iloc[:, 0]:
        criterio_lower = criterio.lower()
        if any(palabra in criterio_lower for palabra in palabras_excluir):
            logger.info(f"⏩ Criterio excluido de la evaluación automática: {criterio}")
            continue
        logger.info(f"🧠 Evaluando criterio: {criterio}")
        evaluacion = evaluar_criterio(client, criterio, texto_tfm, instrucciones_base)
        resultados.append({"criterio": criterio, "evaluacion": evaluacion})
    return resultados

def exportar_resultados(resultados, csv_path, md_path, logger):
#     print("Entrando en exportar_resultados()")
    try:
        pd.DataFrame(resultados).to_csv(csv_path, index=False)
        logger.info(f"💾 CSV generado: {csv_path}")
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# Informe de Evaluación TFM\n\n")
            for res in resultados:
                f.write(f"## Criterio: {res['criterio']}\n")
                f.write(f"**Evaluación:** {res['evaluacion']}\n\n")
        logger.info(f"📝 Markdown generado: {md_path}")
    except Exception as e:
        logger.error(f"❌ Error exportando resultados: {e}")

def main():
#     print("Entrando en main()")
    logger = configurar_logger()
    logger.info("🟢 Inicio del proceso de evaluación")

    ruta_tfm = seleccionar_archivo(
        ["pdf", "docx"],
        titulo="Selecciona el TFM",
        mensaje="Elige el archivo del TFM (.pdf o .docx)"
    )
#     print(f"ruta_tfm: {ruta_tfm}")
    if not ruta_tfm:
        logger.warning("❗ No se seleccionó ningún archivo de TFM.")
        return
    logger.info(f"📄 TFM seleccionado: {ruta_tfm}")

    # Selección de la rúbrica por el usuario
    ruta_rubrica = seleccionar_archivo(
        ["csv", "xlsx", "xls"],
        titulo="Selecciona la rúbrica",
        mensaje="Elige el archivo de la rúbrica (.csv, .xlsx, .xls)"
    )
#     print(f"ruta_rubrica: {ruta_rubrica}")
    if not ruta_rubrica:
        logger.warning("❗ No se seleccionó ninguna rúbrica.")
        return
    logger.info(f"📁 Rúbrica seleccionada: {ruta_rubrica}")

    rubrica = cargar_rubrica(ruta_rubrica, logger)
    if rubrica is None:
        return

    client = configurar_openai()

    ruta_instrucciones = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/Prompt en modo humano.md"
    instrucciones_base = cargar_instrucciones_md_opcional(ruta_instrucciones, logger)

    texto = leer_tfm(ruta_tfm, logger)
#     print(f"Longitud del texto extraído del TFM: {len(texto)}")
    logger.info(f"Longitud del texto extraído del TFM: {len(texto)}")
    logger.info(f"Primeros 500 caracteres del texto extraído:\n{texto[:500]}")
    if not texto.strip():
        logger.error("⚠️ El texto del TFM está vacío.")
        return

    resultados = evaluar_tfm_completo(client, rubrica, texto, instrucciones_base, logger)

    directorio_salida = os.path.dirname(ruta_tfm)
    csv_path = os.path.join(directorio_salida, "evaluacion_tfm_resultado.csv")
    md_path = os.path.join(directorio_salida, "evaluacion_tfm_informe.md")

    exportar_resultados(resultados, csv_path, md_path, logger)

    logger.info("✅ Evaluación finalizada correctamente.")

if __name__ == "__main__":
    main()