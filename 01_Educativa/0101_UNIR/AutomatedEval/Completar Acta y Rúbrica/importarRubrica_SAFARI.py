import os
import shutil
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from AppKit import NSOpenPanel

# Ruta del directorio actual donde está el script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TRAZAS_DIR = os.path.join(BASE_DIR, "TFM_trazas")
os.makedirs(TRAZAS_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
RUTA_LOG = os.path.join(TRAZAS_DIR, f"traza_{timestamp}.txt")


def trazar(msg):
    linea = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"
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
        ruta = panel.URLs()[0].path()
        trazar(f"📎 PDF seleccionado: {ruta}")
        return ruta
    return None


def modificar_pdf(origen):
    nombre = os.path.basename(origen)
    destino = os.path.join("/tmp", nombre)
    shutil.copy(origen, destino)
    with open(destino, "ab") as f:
        f.write(b"\n%%Marca=" + datetime.now().strftime("%Y%m%d%H%M%S").encode("utf-8"))
    os.chmod(destino, 0o644)
    trazar(f"📄 Copiado y marcado: {destino}")
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
                    trazar(
                        f"✅ '{valor_buscado}' seleccionado en <select #{i}>: '{opt.text}'"
                    )
                    nombre_archivo = (
                        f"select_{valor_buscado.replace(' ', '_')}_{i}.html"
                    )
                    with open(
                        os.path.join(TRAZAS_DIR, nombre_archivo), "w", encoding="utf-8"
                    ) as f:
                        f.write(s.get_attribute("outerHTML"))
                    return True
        except Exception:
            continue
    trazar(f"❌ No se pudo seleccionar '{valor_buscado}' en ningún <select>")
    return False


def pedir_datos_alumno():
    import subprocess

    def pedir_por_dialogo(mensaje, valor_defecto=""):
        script = f'display dialog "{mensaje}" default answer "{valor_defecto}" buttons {{"OK"}} default button 1'
        resultado = subprocess.run(
            ["osascript", "-e", script], capture_output=True, text=True
        )
        # Buscar la línea que contiene 'text returned:' y extraer solo el valor
        for linea in resultado.stdout.splitlines():
            if "text returned:" in linea:
                # Ejemplo de línea: 'button returned:OK, text returned:060292642'
                partes = linea.split("text returned:")
                if len(partes) > 1:
                    return partes[1].strip()
        return valor_defecto

    nombre = pedir_por_dialogo("Introduce el nombre completo del alumno:")
    trazar(f"🧑 Nombre introducido: {nombre}")
    dni = pedir_por_dialogo("Introduce el DNI del alumno:")
    trazar(f"🪪 DNI introducido: {dni}")
    return {"nombre": nombre, "dni": dni}


def rellenar_campos_alumno(driver, datos_alumno):
    try:
        driver.find_element(By.ID, "NombreApellidos").clear()
        driver.find_element(By.ID, "NombreApellidos").send_keys(datos_alumno["nombre"])
        driver.find_element(By.ID, "DNI").clear()
        driver.find_element(By.ID, "DNI").send_keys(datos_alumno["dni"])
        trazar(f"✅ Campos del alumno rellenados: {datos_alumno}")
    except Exception as e:
        trazar(f"❌ Error rellenando campos del alumno: {e}")


def pulsar_boton_continuar(driver):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import subprocess

    try:
        wait = WebDriverWait(driver, 15)
        boton = None
        # Buscar por <button> cuyo texto contenga 'continuar'
        botones = wait.until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
        )
        for b in botones:
            if "continuar" in b.text.lower():
                boton = b
                break
        if boton:
            driver.execute_script("arguments[0].scrollIntoView(true);", boton)
            try:
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.XPATH,
                            "//button[contains(translate(text(),'CONTINUAR','continuar'),'continuar')]",
                        )
                    )
                )
                boton.click()
                trazar("✅ Botón 'Continuar' pulsado (click normal).")
            except Exception as e:
                trazar(f"⚠️ Click normal falló: {e}. Intentando con JavaScript...")
                try:
                    driver.execute_script("arguments[0].click();", boton)
                    trazar("✅ Botón 'Continuar' pulsado con JavaScript.")
                except Exception as js_e:
                    trazar(f"❌ Click JS también falló: {js_e}")
                    with open(
                        os.path.join(
                            TRAZAS_DIR, f"boton_continuar_error_{timestamp}.html"
                        ),
                        "w",
                        encoding="utf-8",
                    ) as f:
                        f.write(boton.get_attribute("outerHTML"))
                    with open(
                        os.path.join(
                            TRAZAS_DIR, f"pagina_completa_error_{timestamp}.html"
                        ),
                        "w",
                        encoding="utf-8",
                    ) as f:
                        f.write(driver.page_source)
                    return
            # Traer Safari al frente tras el click
            try:
                subprocess.run(
                    ["osascript", "-e", 'tell application "Safari" to activate']
                )
                trazar("Safari traído al frente tras pulsar 'Continuar'.")
            except Exception as e:
                trazar(f"⚠️ No se pudo traer Safari al frente: {e}")
            return
        # Si no, buscar <input type=submit> cuyo value contenga 'continuar'
        inputs = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
        for inp in inputs:
            if (
                inp.get_attribute("type") == "submit"
                and "continuar" in inp.get_attribute("value").lower()
            ):
                driver.execute_script("arguments[0].scrollIntoView(true);", inp)
                try:
                    wait.until(
                        EC.element_to_be_clickable(
                            (
                                By.XPATH,
                                "//input[@type='submit' and contains(translate(@value,'CONTINUAR','continuar'),'continuar')]",
                            )
                        )
                    )
                    inp.click()
                    trazar("✅ Input 'Continuar' pulsado (input submit, click normal).")
                    return
                except Exception as e:
                    trazar(
                        f"⚠️ Click normal en input falló: {e}. Intentando con JavaScript..."
                    )
                    try:
                        driver.execute_script("arguments[0].click();", inp)
                        trazar("✅ Input 'Continuar' pulsado con JavaScript.")
                        return
                    except Exception as js_e:
                        trazar(f"❌ Click JS en input también falló: {js_e}")
                        with open(
                            os.path.join(
                                TRAZAS_DIR, f"input_continuar_error_{timestamp}.html"
                            ),
                            "w",
                            encoding="utf-8",
                        ) as f:
                            f.write(inp.get_attribute("outerHTML"))
                        with open(
                            os.path.join(
                                TRAZAS_DIR, f"pagina_completa_error_{timestamp}.html"
                            ),
                            "w",
                            encoding="utf-8",
                        ) as f:
                            f.write(driver.page_source)
                        return
        trazar("❌ No se encontró el botón 'Continuar' tras esperar.")
    except Exception as e:
        trazar(f"❌ Error al pulsar el botón 'Continuar' (espera/click): {e}")


def main():
    trazar("▶ INICIO - SAFARI + TRAZAS LOCALES")
    datos_alumno = pedir_datos_alumno()
    pdf_path = seleccionar_pdf()
    if not pdf_path:
        trazar("⚠️ Cancelado por el usuario.")
        return
    pdf_local = modificar_pdf(pdf_path)

    # Cierra Safari completamente antes de iniciar una nueva sesión
    import os

    os.system("killall Safari || true")
    time.sleep(2)

    driver = webdriver.Safari()
    driver.get("https://verifirma.unir.net/Rubricas")
    # Borra cookies y localStorage para evitar residuos de sesión
    driver.delete_all_cookies()
    driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
    time.sleep(2)

    driver.find_element(By.ID, "fileupload").send_keys(pdf_local)
    time.sleep(2)

    rellenar_campos_alumno(driver, datos_alumno)
    time.sleep(1)

    # Traza sobre el estado del botón 'Continuar'
    try:
        boton_continuar = driver.find_element(
            By.XPATH,
            "//button[contains(translate(text(),'CONTINUAR','continuar'),'continuar')]",
        )
        trazar(
            f"Estado botón Continuar: enabled={boton_continuar.is_enabled()}, displayed={boton_continuar.is_displayed()}, html={boton_continuar.get_attribute('outerHTML')}"
        )
    except Exception as e:
        trazar(f"No se pudo obtener el estado del botón Continuar: {e}")

    valores = ["2024-2025", "Máster", "Dirección de Procesos Estratégicos", "Primavera"]
    for valor in valores:
        buscar_y_seleccionar(driver, valor)
        time.sleep(1)

    pulsar_boton_continuar(driver)
    trazar("✅ Proceso completado.")

    # Esperar a que aparezcan los campos de usuario y contraseña tras continuar
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    try:
        wait = WebDriverWait(driver, 40)  # Aumenta el timeout
        # Cambia a la última ventana si hay más de una
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[-1])
            trazar(f"🔀 Cambiado a la ventana: {driver.current_url}")
        # Si hay iframes, intenta cambiar a cada uno y buscar el campo
        usuario_input = None
        for _ in range(3):  # Prueba hasta 3 iframes anidados
            try:
                usuario_input = wait.until(
                    EC.presence_of_element_located((By.ID, "Usuario"))
                )
                break
            except Exception:
                iframes = driver.find_elements(By.TAG_NAME, "iframe")
                if iframes:
                    driver.switch_to.frame(iframes[0])
                    trazar("🔎 Cambiado a un iframe para buscar el campo Usuario.")
                else:
                    break
        if not usuario_input:
            raise Exception(
                "No se encontró el campo Usuario en ninguna ventana ni iframe"
            )
        # Guardar HTML real del campo usuario para depuración
        with open(
            os.path.join(TRAZAS_DIR, f"usuario_input_{timestamp}.html"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(usuario_input.get_attribute("outerHTML"))
        usuario_input.clear()
        usuario_input.send_keys("juanjose.vazquez@unir.net")
        from selenium.webdriver.common.keys import Keys

        usuario_input.send_keys(Keys.TAB)
        contrasena_input = wait.until(
            EC.presence_of_element_located((By.ID, "Contrasena"))
        )
        contrasena_input.clear()
        contrasena_input.send_keys("vaya-toalla1B")
        trazar("✅ Usuario y contraseña rellenados tras continuar.")
    except Exception as e:
        trazar(f"❌ Error esperando o rellenando usuario/contraseña: {e}")

    import subprocess

    subprocess.run(
        [
            "osascript",
            "-e",
            'display dialog "Pulsa Aceptar para cerrar Safari..." buttons {"Aceptar"} default button 1',
        ]
    )
    trazar("Cerrando Safari...")
    driver.quit()


if __name__ == "__main__":
    main()
