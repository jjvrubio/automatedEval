import os
import pandas as pd
import openai
import pdfplumber
import docx
import logging
from dotenv import load_dotenv
from AppKit import NSOpenPanel, NSApplication

# ------------------------------
# CONFIGURACIÓN OPENAI (via .env)
# ------------------------------
def configurar_openai():
    print("Entrando en configurar_openai()")
    load_dotenv()
    api_key = os.getenv("MI_CLAVE_API_OPENAI")
    if not api_key:
        raise ValueError("❌ No se encontró la clave API en el archivo .env")
    return openai.OpenAI(api_key=api_key)

# ------------------------------
# CONFIGURACIÓN DEL LOGGER
# ------------------------------
def configurar_logger():
    print("Entrando en configurar_logger()")
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
    print("Entrando en seleccionar_archivo()")
    NSApp = NSApplication.sharedApplication()
    NSApp.activateIgnoringOtherApps_(True)
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(allowed_types)
    panel.setTitle_(titulo)
    panel.setMessage_(mensaje)

    if panel.runModal() == 1:
        print("Archivo seleccionado en seleccionar_archivo()")
        return panel.URLs()[0].path()
    print("No se seleccionó archivo en seleccionar_archivo()")
    return None

# ------------------------------
# CARGA DE RÚBRICA
# ------------------------------
def cargar_rubrica(path, logger):
    print("Entrando en cargar_rubrica()")
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
    print("Entrando en cargar_instrucciones_md_opcional()")
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
    print("Entrando en leer_tfm()")
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
    print("Entrando en evaluar_criterio()")
    prompt = f"{instrucciones_base.strip()}\n\n" if instrucciones_base.strip() else ""
    prompt += f"""Ahora evalúa el siguiente trabajo según el criterio:

Criterio:
{criterio}

Trabajo del TFM (solo para consulta, NO lo repitas en la respuesta):
{texto_tfm}

Responde SOLO con el nivel (Nivel 1, 2, 3 o 4) y una justificación crítica y detallada. NO repitas el texto del TFM en tu respuesta.
"""
    # Log del prompt antes de enviarlo a OpenAI
    logging.getLogger("evaluador_tfm").info(f"Prompt enviado a OpenAI para el criterio '{criterio}':\n{prompt[:2000]}... [truncado]")

    # Selección del modelo con mayor ventana de tokens
    modelo_llm = "gpt-4o"

    response = client.chat.completions.create(
        model=modelo_llm,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=400  # Limita la longitud de la respuesta
    )
    return response.choices[0].message.content.strip()

# ------------------------------
# EVALUACIÓN COMPLETA
# ------------------------------
def evaluar_tfm_completo(client, rubrica_df, texto_tfm, instrucciones_base, logger):
    print("Entrando en evaluar_tfm_completo()")
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
    print("Entrando en exportar_resultados()")
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
    print("Entrando en main()")
    logger = configurar_logger()
    logger.info("🟢 Inicio del proceso de evaluación")

    ruta_tfm = seleccionar_archivo(
        ["pdf", "docx"],
        titulo="Selecciona el TFM",
        mensaje="Elige el archivo del TFM (.pdf o .docx)"
    )
    print(f"ruta_tfm: {ruta_tfm}")
    if not ruta_tfm:
        logger.warning("❗ No se seleccionó ningún archivo de TFM.")
        return
    logger.info(f"📄 TFM seleccionado: {ruta_tfm}")

    client = configurar_openai()

    ruta_rubrica = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/rubrica.csv"
    logger.info(f"📁 Usando rúbrica fija: {ruta_rubrica}")

    if not ruta_rubrica:
        logger.warning("❗ No se seleccionó ninguna rúbrica.")
        return
    logger.info(f"📁 Rúbrica seleccionada: {ruta_rubrica}")

    rubrica = cargar_rubrica(ruta_rubrica, logger)
    if rubrica is None:
        return

    # 🔁 Cargar instrucciones ultraestrictas solo si existen
    ruta_instrucciones = "/Users/juanjo/Documents/Personal/JJVR/automatizaciones/automatedEval/TFM_Evaluator_Prompt_Package/Prompt en modo humano.md"
    instrucciones_base = cargar_instrucciones_md_opcional(ruta_instrucciones, logger)

    texto = leer_tfm(ruta_tfm, logger)
    print(f"Longitud del texto extraído del TFM: {len(texto)}")
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
