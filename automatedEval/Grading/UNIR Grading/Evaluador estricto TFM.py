import os
import pandas as pd
import openai
import pdfplumber
import docx
import logging
from dotenv import load_dotenv
from AppKit import NSOpenPanel

# ------------------------------
# CONFIGURACIÓN OPENAI (via .env)
# ------------------------------
def configurar_openai():
    load_dotenv()
    api_key = os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        raise ValueError("❌ No se encontró la clave API en el archivo .env")
    return openai.OpenAI(api_key=api_key)

# ------------------------------
# CONFIGURACIÓN DEL LOGGER
# ------------------------------
def configurar_logger():
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

# ------------------------------
# SELECCIÓN DE ARCHIVO (AppKit)
# ------------------------------
def seleccionar_archivo(allowed_types, titulo, mensaje):
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(allowed_types)
    panel.setTitle_(titulo)
    panel.setMessage_(mensaje)

    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None

# ------------------------------
# CARGA DE RÚBRICA
# ------------------------------
def cargar_rubrica(path, logger):
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

# ------------------------------
# CARGA OPCIONAL DE INSTRUCCIONES
# ------------------------------
def cargar_instrucciones_md_opcional(ruta_md, logger):
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

# ------------------------------
# LECTURA DEL TFM
# ------------------------------
def leer_tfm(path, logger):
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

# ------------------------------
# EVALUACIÓN CON OPENAI
# ------------------------------
def evaluar_criterio(client, criterio, texto_tfm, instrucciones_base):
    prompt = f"{instrucciones_base.strip()}\n\n" if instrucciones_base.strip() else ""
    prompt += f"""Ahora evalúa el siguiente trabajo según el criterio:

Criterio:
{criterio}

Trabajo del TFM:
{texto_tfm}

Responde estrictamente con Nivel 1, Nivel 2, Nivel 3 o Nivel 4 seguido de una justificación crítica y detallada.
"""
    # Log del prompt antes de enviarlo a OpenAI
    logging.getLogger("evaluador_tfm").info(f"Prompt enviado a OpenAI para el criterio '{criterio}':\n{prompt[:2000]}... [truncado]")

    # Selección del modelo con mayor ventana de tokens
    # gpt-4o: 128k tokens (OpenAI, 2024)
    # gpt-4-turbo: 128k tokens
    # gpt-4-32k: 32k tokens
    # gpt-3.5-turbo-16k: 16k tokens
    # Usamos gpt-4o si está disponible
    modelo_llm = "gpt-4o"

    response = client.chat.completions.create(
        model=modelo_llm,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content

# ------------------------------
# EVALUACIÓN COMPLETA
# ------------------------------
def evaluar_tfm_completo(client, rubrica_df, texto_tfm, instrucciones_base, logger):
    resultados = []
    for criterio in rubrica_df.iloc[:, 0]:
        logger.info(f"🧠 Evaluando criterio: {criterio}")
        evaluacion = evaluar_criterio(client, criterio, texto_tfm, instrucciones_base)
        resultados.append({"criterio": criterio, "evaluacion": evaluacion})
    return resultados

# ------------------------------
# EXPORTAR RESULTADOS
# ------------------------------
def exportar_resultados(resultados, csv_path, md_path, logger):
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

# ------------------------------
# MAIN
# ------------------------------
def main():
    logger = configurar_logger()
    client = configurar_openai()

    logger.info("🟢 Inicio del proceso de evaluación")

    ruta_rubrica = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica.csv"
    logger.info(f"📁 Usando rúbrica fija: {ruta_rubrica}")

    if not ruta_rubrica:
        logger.warning("❗ No se seleccionó ninguna rúbrica.")
        return
    logger.info(f"📁 Rúbrica seleccionada: {ruta_rubrica}")

    rubrica = cargar_rubrica(ruta_rubrica, logger)
    if rubrica is None:
        return

    ruta_tfm = seleccionar_archivo(
        ["pdf", "docx"],
        titulo="Selecciona el TFM",
        mensaje="Elige el archivo del TFM (.pdf o .docx)"
    )
    if not ruta_tfm:
        logger.warning("❗ No se seleccionó ningún archivo de TFM.")
        return
    logger.info(f"📄 TFM seleccionado: {ruta_tfm}")

    # 🔁 Cargar instrucciones ultraestrictas solo si existen
    ruta_instrucciones = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/Prompt en modo humano.md"
    instrucciones_base = cargar_instrucciones_md_opcional(ruta_instrucciones, logger)

    texto = leer_tfm(ruta_tfm, logger)
    logger.info(f"Longitud del texto extraído del TFM: {len(texto)}")
    logger.info(f"Primeros 500 caracteres del texto extraído:\n{texto[:500]}")
    if not texto.strip():
        logger.error("⚠️ El texto del TFM está vacío.")
        return

    resultados = evaluar_tfm_completo(client, rubrica, texto, instrucciones_base, logger)

    # ✅ Exportar en la carpeta del TFM
    directorio_salida = os.path.dirname(ruta_tfm)
    csv_path = os.path.join(directorio_salida, "evaluacion_tfm_resultado.csv")
    md_path = os.path.join(directorio_salida, "evaluacion_tfm_informe.md")

    exportar_resultados(resultados, csv_path, md_path, logger)

    logger.info("✅ Evaluación finalizada correctamente.")

# ------------------------------
# EJECUCIÓN
# ------------------------------
if __name__ == "__main__":
    main()
