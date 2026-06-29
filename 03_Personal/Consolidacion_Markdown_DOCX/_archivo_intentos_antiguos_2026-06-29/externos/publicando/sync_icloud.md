# 📸 Sincronización de imágenes desde iCloud a GitHub – `pulse_images`

Este documento describe el flujo de trabajo para sincronizar imágenes almacenadas en iCloud hacia el repositorio GitHub `pulse_images`, utilizando un script bash flexible y organizado mediante la variable `TARGET`.

---
## 🔧 Script principal: `sync_from_icloud.sh`
### 📍 Ruta:
`pulse_images/sync_from_icloud.sh`

### 📋 Descripción:
Este script permite copiar archivos de imagen desde una carpeta en iCloud (por defecto: `imágenes para LinkedIn`) a una carpeta de destino dentro del repositorio, indicada mediante la variable `TARGET`.

### 🧩 Estructura del script:
    # Ruta al repositorio local
    REPO=~/Desktop/pulse_images
    # Ruta a carpeta en iCloud
    SOURCE="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Research/imágenes para LinkedIn"
    # Carpeta destino dentro del repositorio (por defecto: raíz)
    TARGET="linkedin_2025"

---
## 🚀 Instrucciones de uso
### ✅ 1. Configurar el valor de `TARGET`
    TARGET="."
- Esto sincroniza las imágenes directamente a la **raíz** del repositorio.
    TARGET="linkedin_2025"
- Esto sincroniza a una **subcarpeta organizada por campaña**.

### ✅ 2. Ejecutar el script
    ./sync_from_icloud.sh

---
## 📦 Archivos que se copian
Extensiones permitidas:
    .jpg, .jpeg, .png, .gif, .webp, .bmp, .svg, .tiff

---
## 🔁 Comportamiento inteligente
- No hace commit ni push si no hay cambios.
- Commits incluyen fecha automática y nombre de `TARGET`.
- Admite múltiples carpetas destino como:
  - `linkedin_2025`
  - `campaña_navidad`
  - `eventos_2024`

---
## 🧠 Buenas prácticas
| Práctica | Recomendación |
|---------|----------------|
| 🗂️ Nombres de `TARGET` | Minúsculas, sin espacios, guiones bajos (`linkedin_2025`) |
| 📝 Commits claros | Generados automáticamente con fecha y nombre |
| 🧼 Mantenimiento | Archivar/eliminar carpetas antiguas tras cada campaña |
| ✅ VS Code | Usa `tasks.json` para `Cmd + Shift + B` |

---
## 🧪 Ejemplo de ejecución
    cd ~/Desktop/pulse_images
    ./sync_from_icloud.sh
Resultado típico:
    Copiando imágenes desde iCloud a linkedin_2025...
    Sincronización desde 'imágenes para LinkedIn' → 'linkedin_2025': 2025-06-10 19:10
    Push realizado con éxito.

---
## 🧾 Historial de campañas sincronizadas
| TARGET           | Fecha inicio | Descripción breve             |
|------------------|--------------|-------------------------------|
| `linkedin_2025`  | 2025-06-10   | Campaña de contenido Q2 2025 |
| `eventos_mayo`   | 2025-05-02   | Imágenes de eventos regionales |
| `.` (raíz)       | 2025-04-15   | Usado para pruebas sueltas    |

---
## 🛠️ Posibles extensiones futuras
- Argumento `TARGET` al invocar
- Filtrado por fecha automática
- Sincronización inversa GitHub → local

---
## 🔐 Avisos de seguridad
- Asegúrate de tener `.gitignore` actualizado.
- No uses `TARGET="."` si prefieres mantener organización.

---
## ✍️ Autor y fecha
Configuración mantenida por: **Juanjo**
Última actualización: `2025-06-10`