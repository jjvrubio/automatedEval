from pathlib import Path

import os
import traceback
import time
import subprocess
from AppKit import NSOpenPanel
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime


# Ruta del directorio actual donde está el script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAZAS_DIR = os.path.join(BASE_DIR, "TFM_trazas")
os.makedirs(TRAZAS_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
RUTA_LOG = os.path.join(TRAZAS_DIR, f"traza_{timestamp}.txt")


def trazar(mensaje):
    linea = f"[{datetime.now().strftime('%H:%M:%S')}] {mensaje}"
    with open(RUTA_LOG, "a", encoding="utf-8") as f:
        f.write(linea + "\n")
    print("🟨", linea)


def seleccionar_excel():
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["xlsx"])
    if panel.runModal():
        return panel.URLs()[0].path()
    return None


def pedir_url_formulario():
    script = 'display dialog "🔗 Pega aquí la URL del formulario UNIR:" default answer ""'
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    for line in result.stdout.split(','):
        if 'text returned:' in line:
            return line.split(':', 1)[1].strip()
    return ""


def pedir_fecha_defensa():
    import re
    while True:
        script = 'display dialog "📅 Introduce la fecha de defensa (dd/mm/aaaa):" default answer ""'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        for line in result.stdout.split(','):
            if 'text returned:' in line:
                fecha = line.split(':', 1)[1].strip()
                if re.match(r'^\d{2}/\d{2}/\d{4}$', fecha):
                    return fecha
        subprocess.run(['osascript', '-e', 'display alert "❌ Formato incorrecto. Usa dd/mm/aaaa (ej. 17/05/2025)."'])


def leer_valores_excel(path):
    libro = load_workbook(filename=path, data_only=True)
    hoja = libro["Rubrica"]

    valores = {}
    valores["Estructura"] = str(hoja["J5"].value)
    valores["Contenido"] = str(hoja["J7"].value)
    valores["Defensa"] = str(hoja["J14"].value)

    # Credenciales: leer de variables de entorno para evitar hardcoding.
    # Establece ACTA_EMAIL_SECRETARIO y ACTA_PASSWORD en el entorno o en un gestor de secretos.
    valores["Acta_EmailSecretario"] = os.environ.get("ACTA_EMAIL_SECRETARIO", "juanjose.vazquez@unir.net")
    valores["Contrasena"] = os.environ.get("ACTA_PASSWORD")
    # Si no hay contraseña en el entorno, pedirla de forma segura al usuario (oculta)
    if not valores["Contrasena"]:
        pw_script = 'display dialog "Introduce la contraseña para el Acta (se guardará sólo en memoria):" default answer "" with hidden answer'
        pw_result = subprocess.run(['osascript', '-e', pw_script], capture_output=True, text=True)
        for line in pw_result.stdout.split(','):
            if 'text returned:' in line:
                valores["Contrasena"] = line.split(':', 1)[1].strip()
        if not valores["Contrasena"]:
            trazar("❌ No se proporcionó contraseña en entorno ni por diálogo. Abortando.")
            raise ValueError("No password provided for Acta (ACTA_PASSWORD)")

    valores["FechaDefensa"] = pedir_fecha_defensa()
    return valores


def rellenar_campos(driver, valores):
    for clave, valor in valores.items():
        try:
            campo = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, clave))
            )
            # Guardar HTML real del campo antes de rellenar
            with open(os.path.join(TRAZAS_DIR, f"campo_{clave}_{timestamp}.html"), "w", encoding="utf-8") as f:
                f.write(campo.get_attribute("outerHTML"))
            campo.clear()
            campo.send_keys(valor)
            # Traza con el valor real tras el envío
            real_value = campo.get_attribute("value")
            trazar(f"Campo {clave} tras send_keys: '{real_value}' (esperado: '{valor}')")
            # Si el valor no coincide, forzar con JS
            if real_value != valor:
                driver.execute_script(f"arguments[0].value = '{valor}';", campo)
                trazar(f"Forzado valor de {clave} con JS a: '{valor}'")
        except Exception as e:
            trazar(f"❌ Error al rellenar {clave}: {e}")
    # Intentar hacer click en el botón de login si existe
    try:
        boton_login = driver.find_element(By.XPATH, "//button[contains(translate(text(),'login','LOGIN'),'login')] | //button[contains(translate(text(),'acceder','ACCEDER'),'acceder')] | //input[@type='submit']")
        # Guardar HTML real del botón de login
        with open(os.path.join(TRAZAS_DIR, f"boton_login_{timestamp}.html"), "w", encoding="utf-8") as f:
            f.write(boton_login.get_attribute("outerHTML"))
        boton_login.click()
        trazar("Se hizo click en el botón de login tras rellenar usuario/contraseña.")
    except Exception as e:
        trazar(f"No se pudo hacer click en el botón de login: {e}")


def main():
    try:
        ruta_excel = seleccionar_excel()
        if not ruta_excel:
            trazar("No se seleccionó ningún archivo Excel.")
            return

        valores = leer_valores_excel(ruta_excel)

        url = pedir_url_formulario()
        if not url:
            trazar("No se proporcionó ninguna URL.")
            return

        # Cierra Brave completamente antes de iniciar una nueva sesión
        import os
        os.system('killall "Brave Browser" || true')
        time.sleep(2)

        # Volver a usar Safari en vez de Brave
        try:
            trazar("Iniciando Safari WebDriver...")
            driver = webdriver.Safari()
            trazar("Safari iniciado correctamente.")
        except Exception as e:
            trazar(f"❌ Error al iniciar Safari: {e}")
            subprocess.run(['osascript', '-e', f'display alert "Error al iniciar Safari: {e}"'])
            return
        try:
            driver.get(url)
            driver.delete_all_cookies()
            driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
            time.sleep(2)
            rellenar_campos(driver, valores)
            subprocess.run([
                'osascript',
                '-e', 'display dialog "⏳ Pulsa Aceptar cuando hayas terminado para cerrar Safari..." buttons {"Aceptar"} default button 1'
            ])
            trazar("Cerrando Safari...")
            driver.quit()
            trazar("Safari cerrado correctamente.")
        except Exception as e:
            trazar(f"❌ Error durante la automatización: {e}")
            subprocess.run(['osascript', '-e', f'display alert "Error durante la automatización: {e}"'])

    except Exception as e:
        trazar("❌ Error inesperado:")
        traceback.print_exc()


if __name__ == "__main__":
    main()
