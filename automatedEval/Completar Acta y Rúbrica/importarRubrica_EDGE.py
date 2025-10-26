import os
import shutil
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from AppKit import NSOpenPanel

RUTA_LOG = os.path.expanduser("~/Desktop/traza_seleccion.txt")

def trazar(msg):
    timestamp = datetime.now().strftime('%H:%M:%S')
    linea = f"[{timestamp}] {msg}"
    with open(RUTA_LOG, "a", encoding="utf-8") as f:
        f.write(linea + "\n")
    print("📝", linea)

def seleccionar_pdf():
    panel = NSOpenPanel.openPanel()
    panel.setTitle_("Selecciona un archivo PDF")
    panel.setAllowedFileTypes_(["pdf"])
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None

def modificar_pdf(origen):
    nombre = os.path.basename(origen)
    destino = os.path.join("/tmp", nombre)
    shutil.copy(origen, destino)
    with open(destino, "ab") as f:
        f.write(b"\n%%Marca=" + datetime.now().strftime("%Y%m%d%H%M%S").encode("utf-8"))
    os.chmod(destino, 0o644)
    return destino

def buscar_y_seleccionar(driver, valor_buscado):
    selects = driver.find_elements(By.TAG_NAME, "select")
    for i, s in enumerate(selects):
        try:
            select = Select(s)
            for opt in select.options:
                if valor_buscado.strip().lower() == opt.text.strip().lower():
                    driver.execute_script("arguments[0].scrollIntoView(true);", s)
                    select.select_by_visible_text(opt.text)
                    trazar(f"✅ '{valor_buscado}' seleccionado en <select #{i}> con texto exacto: '{opt.text}'")
                    with open(f"seleccion_{valor_buscado.replace(' ', '_')}.html", "w", encoding="utf-8") as f:
                        f.write(s.get_attribute("outerHTML"))
                    return True
        except Exception as e:
            continue
    trazar(f"❌ No se pudo seleccionar '{valor_buscado}' en ningún <select>",)
    return False

def main():
    trazar("▶ INICIO - SELECCIÓN POR CONTENIDO")
    pdf_path = seleccionar_pdf()
    if not pdf_path:
        return
    pdf_local = modificar_pdf(pdf_path)

    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Edge(service=Service(), options=options)
    driver.get("https://verifirma.unir.net/Rubricas")

    time.sleep(5)
    driver.find_element(By.ID, "fileupload").send_keys(pdf_local)
    time.sleep(5)

    valores = ["2024-2025", "Máster", "Dirección de Procesos Estratégicos", "Primavera"]
    for valor in valores:
        buscar_y_seleccionar(driver, valor)
        time.sleep(1)

    input("✅ Proceso finalizado. Pulsa ENTER para cerrar...")
    driver.quit()

if __name__ == "__main__":
    main()