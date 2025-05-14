
import os
import traceback
import time
from AppKit import NSOpenPanel
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOG_PATH = os.path.expanduser("~/Desktop/traza_importar_acta.txt")

def trazar(msg):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(msg + "\\n")
    print("📝", msg)

def seleccionar_excel():
    panel = NSOpenPanel.openPanel()
    panel.setTitle_("Selecciona el archivo Excel")
    panel.setAllowedFileTypes_(["xlsx"])
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    if panel.runModal() == 1:
        ruta = panel.URLs()[0].path()
        trazar(f"✅ Excel seleccionado: {ruta}")
        return ruta
    else:
        trazar("❌ No se seleccionó ningún Excel.")
        return None

def leer_valores_excel(path):
    try:
        wb = load_workbook(path, data_only=True)
        ws = wb["Rubrica"]
        valores = {
            "Estructura": ws["J5"].value,
            "Contenido": ws["J7"].value,
            "Defensa": ws["J14"].value,
        }
        trazar(f"📊 Valores leídos del Excel: {valores}")
        return valores
    except Exception as e:
        trazar("❌ Error al leer el Excel:")
        trazar(traceback.format_exc())
        return None

def rellenar_campos(driver, valores):
    try:
        for campo_id, valor in valores.items():
            campo = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.ID, campo_id))
            )
            campo.clear()
            campo.send_keys(str(valor))
            trazar(f"✅ Rellenado campo {campo_id} con valor {valor}")
    except Exception as e:
        trazar("❌ Error al rellenar campos:")
        trazar(traceback.format_exc())

def main():
    print("🔁 Script importarActa iniciado")
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("🧪 TRAZA DE EJECUCIÓN INICIADA\\n\\n")

    excel_path = seleccionar_excel()
    if not excel_path:
        return

    valores = leer_valores_excel(excel_path)
    if not valores:
        return

    url = input("🔗 Pega aquí la URL del formulario UNIR: ").strip()
    if not url.startswith("http"):
        trazar("❌ URL inválida.")
        return

    try:
        trazar("🚀 Iniciando Safari...")
        driver = webdriver.Safari()
        driver.get(url)
        trazar(f"🌐 Página cargada: {url}")

        rellenar_campos(driver, valores)

        trazar("🟡 Safari listo para interacción manual (fecha + autenticación).")
        input("⏳ Pulsa ENTER cuando hayas terminado para cerrar Safari...")

        driver.quit()
        trazar("✅ Sesión finalizada.")
    except Exception as e:
        trazar("❌ Error general:")
        trazar(traceback.format_exc())

if __name__ == "__main__":
    import os
    print("📂 Ejecutando:", os.path.abspath(__file__))
    main()
