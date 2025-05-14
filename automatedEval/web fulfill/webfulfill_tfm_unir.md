
# Evaluación Automatizada de TFMs – UNIR (Dirección de Procesos Estratégicos)

## 🎯 Objetivo

Automatizar la carga y preparación del formulario Verifirma de UNIR para evaluar Trabajos de Fin de Máster (TFM), específicamente para la maestría en **Dirección de Procesos Estratégicos**.

---

## ⚙️ Tecnología usada

- Python 3.13
- Selenium (controlador web)
- SafariDriver (automatización de Safari)
- PyObjC (AppKit.NSOpenPanel) para selector de archivos nativo de macOS

---

## 🧪 Flujo automatizado

1. **Selección de PDF**: Se abre una ventana nativa para elegir el archivo del TFM.
2. **Copia del archivo**: El PDF se guarda temporalmente en `/tmp` para garantizar permisos de lectura.
3. **Acceso a Verifirma**: El script abre `https://verifirma.unir.net/Rubricas` con Safari.
4. **Carga del PDF**: El archivo es subido automáticamente al sistema.
5. **Carga dinámica de campos**: El script espera a que aparezcan los campos de selección.
6. **Relleno automatizado de 4 campos desplegables**:
   - Año académico: `2024-2025`
   - Periodo: `Primavera`
   - Tipo de estudio: `Máster`
   - Titulación: `Dirección de Procesos Estratégicos`
7. **Pausa para edición manual**: Safari **permanece abierto con la sesión activa** para que el usuario rellene manualmente 2 campos adicionales.
8. **Finalización**: El script se reanuda solo cuando el usuario pulsa ENTER en la consola.

---

## 🧱 Requisitos previos

- macOS con Safari instalado.
- SafariDriver activado:
  - Preferencias de Safari > Avanzado > Habilitar menú de desarrollo.
  - Develop > ✅ Allow Remote Automation
- Entorno virtual Python con:
  ```bash
  pip install selenium pyobjc
  ```

---

## 📂 Archivos generados

- `traza_nativa.txt`: Registro paso a paso en el Escritorio.
- `captura_post_upload.png`: Imagen del estado visual tras subir el PDF.
- (opcional) `error_carga_nativo.png` si ocurre un error crítico.

---

## 🖐 Interacción manual

Tras el paso 6, el script **no cierra Safari**. El usuario puede:
- Completar los 2 campos restantes directamente en la página.
- Validar manualmente el formulario.
- Pulsar ENTER en terminal para finalizar.

---

## 🔁 Adaptabilidad

Esta versión está optimizada para **"Dirección de Procesos Estratégicos"**, pero puede adaptarse fácilmente a otras titulaciones cambiando los valores en la función `asignar_valores()`.

