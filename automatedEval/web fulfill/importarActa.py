from pathlib import Path

import os
import traceback
import time
from AppKit import NSOpenPanel
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


def trazar(mensaje):
    print("🟨 " + str(mensaje))


def seleccionar_excel():
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["xlsx"])
    if panel.runModal():
        return panel.URLs()[0].path()
    return None


def leer_valores_excel(path):
    libro = load_workbook(filename=path, data_only=True)
    hoja = libro["Rubrica"]

    valores = {}
    valores["Estructura"] = str(hoja["J5"].value)
    valores["Contenido"] = str(hoja["J7"].value)
    valores["Defensa"] = str(hoja["J14"].value)

    valores["Acta_EmailSecretario"] = "juanjose.vazquez@unir.net"
    valores["Contrasena"] = "vaya-toalla1A"

    import re
    while True:
        fecha = input("📅 Introduce la fecha de defensa (dd/mm/aaaa): ").strip()
        if re.match(r'^\d{2}/\d{2}/\d{4}$', fecha):
            valores["FechaDefensa"] = fecha
            break
        else:
            print("❌ Formato incorrecto. Usa dd/mm/aaaa (ej. 17/05/2025).")

    return valores


def rellenar_campos(driver, valores):
    for clave, valor in valores.items():
        try:
            campo = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, clave))
            )
            campo.clear()
            campo.send_keys(valor)
        except Exception as e:
            trazar(f"❌ Error al rellenar {clave}: {e}")


def main():
    try:
        ruta_excel = seleccionar_excel()
        if not ruta_excel:
            trazar("No se seleccionó ningún archivo Excel.")
            return

        valores = leer_valores_excel(ruta_excel)

        url = input("🔗 Pega aquí la URL del formulario UNIR: ").strip()
        if not url:
            trazar("No se proporcionó ninguna URL.")
            return

        driver = webdriver.Safari()
        driver.get(url)

        rellenar_campos(driver, valores)

        input("⏳ Pulsa ENTER cuando hayas terminado para cerrar Safari...")
        driver.quit()

    except Exception as e:
        trazar("❌ Error inesperado:")
        traceback.print_exc()


if __name__ == "__main__":
    main()
