import os
import shutil
import traceback
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from AppKit import NSOpenPanel

RUTA_LOG = os.path.expanduser("~/Desktop/traza_nativa.txt")

def trazar(mensaje):
    with open(RUTA_LOG, "a", encoding="utf-8") as f:
        f.write(mensaje + "\n")
    print("📝", mensaje)

def seleccionar_pdf():
    panel = NSOpenPanel.openPanel()
    panel.setTitle_("Selecciona un archivo PDF")
    panel.setAllowedFileTypes_(["pdf"])
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)

    if panel.runModal() == 1:
        ruta = panel.URLs()[0].path()
        trazar(f"✅ PDF seleccionado: {ruta}")
        return ruta
    else:
        trazar("❌ No se seleccionó archivo.")
        return None

def preparar_archivo(pdf_path):
    nombre = os.path.basename(pdf_path)
    destino = os.path.join("/tmp", nombre)
    try:
        shutil.copy(pdf_path, destino)
        os.chmod(destino, 0o644)
        trazar(f"📁 Archivo copiado a ubicación segura: {destino}")
        return destino
    except Exception as e:
        trazar("❌ Error al copiar el archivo:")
        trazar(traceback.format_exc())
        return None

def asignar_valores():
    return {
        "Año académico": "2024-2025",
        "Periodo": "Primavera",
        "Tipo de estudio": "Máster",
        "Titulación": "Dirección de Procesos Estratégicos",
    }

def esperar_y_seleccionar(driver, campo_id, valor_visible):
    try:
        campo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, campo_id))
        )
        WebDriverWait(driver, 10).until(
            lambda d: valor_visible in [o.text for o in Select(campo).options]
        )
        for o in Select(campo).options:
            trazar(f"📋 Opción en {campo_id}: {o.text}")
        Select(campo).select_by_visible_text(valor_visible)
        trazar(f"✅ Seleccionado {campo_id}: {valor_visible}")
    except Exception as e:
        trazar(f"❌ Error seleccionando {campo_id} = {valor_visible}")
        trazar(traceback.format_exc())

def rellenar_desplegables(driver, valores):
    trazar("🧾 Rellenando todos los desplegables...")

    campos = [
        ("IdRubricaAnoAcademico", "Año académico"),
        ("IdRubricaPeriodo", "Periodo"),
        ("IdRuctTipoEstudio", "Tipo de estudio"),
        ("IdRuctTitulacion", "Titulación"),
    ]

    for campo_id, clave_valor in campos:
        esperar_y_seleccionar(driver, campo_id, valores[clave_valor])

def cargar_pdf_y_rellenar(driver, pdf_path, valores):
    try:
        trazar("🌐 Abriendo Verifirma Rubricas...")
        driver.get("https://verifirma.unir.net/Rubricas")

        campo_archivo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        trazar(f"📤 Subiendo PDF desde: {pdf_path}")
        campo_archivo.send_keys(pdf_path)
        trazar("✅ PDF subido. Esperando aparición de campos...")

        time.sleep(3)

        url_actual = driver.current_url
        trazar(f"🌐 URL actual: {url_actual}")

        captura_path = os.path.expanduser("~/Desktop/captura_post_upload.png")
        driver.save_screenshot(captura_path)
        trazar(f"📸 Captura visual guardada: {captura_path}")

        rellenar_desplegables(driver, valores)

        trazar("🟡 Pausa indefinida: completa manualmente los campos restantes en Safari.")
        input("⏳ Pulsa ENTER aquí en consola cuando hayas terminado en Safari...")

        trazar("✅ Interacción manual completada. Safari puede cerrarse manualmente si lo deseas.")

    except Exception as e:
        trazar("❌ Error durante carga y relleno:")
        trazar(traceback.format_exc())
        try:
            driver.save_screenshot(os.path.expanduser("~/Desktop/error_carga_nativo.png"))
        except:
            pass
        trazar("⚠️ SafariDriver permanece abierto para inspección manual.")

def main():
    with open(RUTA_LOG, "w", encoding="utf-8") as f:
        f.write("🧪 INICIO DE TRAZA\n\n")

    trazar("🔁 Ejecutando script")
    ruta_original = seleccionar_pdf()
    if not ruta_original:
        trazar("🚫 Selección cancelada.")
        return

    ruta_local = preparar_archivo(ruta_original)
    if not ruta_local:
        trazar("🚫 Copia del PDF fallida.")
        return

    try:
        trazar("🚀 Iniciando SafariDriver...")
        driver = webdriver.Safari()
        trazar("✅ Safari iniciado.")
    except Exception as e:
        trazar("❌ No se pudo iniciar Safari.")
        trazar(traceback.format_exc())
        return

    valores = asignar_valores()
    cargar_pdf_y_rellenar(driver, ruta_local, valores)

if __name__ == "__main__":
    main()
