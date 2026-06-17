Aquí tienes un **flujo de trabajo optimizado** para publicar desde **Obsidian + Pandoc** hacia **Substack y LinkedIn**, aprovechando Markdown y automatización:

---

### 🔥 **Paso 1: Preparar el Contenido en Obsidian**
1. **Escribe en Markdown** con formato compatible:
   - Usa encabezados `#`, `##` para títulos/subtítulos.
   - Añade imágenes con `![descripción](ruta/local)` (Substack requiere subirlas manualmente luego).
   - Listas, blockquotes (`>`) y enlaces se mantendrán.

2. **Metadatos clave** (al inicio del archivo):
   ```markdown
   ---
   title: "Mi Artículo"
   subtitle: "Subtítulo opcional"
   tags: [tag1, tag2]
   ---
   ```

---

### 🔄 **Paso 2: Convertir a HTML/Word con Pandoc**
1. **Instala Pandoc** (si no lo tienes):
   ```bash
   brew install pandoc  # En macOS
   ```

2. **Conversión a HTML** (ideal para Substack):
   ```bash
   pandoc -s archivo.md -o archivo.html --css=ruta/estilos.css
   ```
   - *Opcional*: Usa `--css` para estilos personalizados (Substack/LinkedIn pueden ignorarlos).

3. **Conversión a Word** (para LinkedIn si prefieres formato .docx):
   ```bash
   pandoc archivo.md -o archivo.docx --reference-doc=plantilla.docx
   ```
   - Usa `--reference-doc` para mantener estilos de tu plantilla.

---

### 🚀 **Paso 3: Publicar en Substack**
1. **Método A: Copiar HTML directo**:
   - Abre el `.html` generado en un navegador → **Ctrl+A/Cmd+A → Copiar**.
   - Pega en el editor de Substack (mantendrá formato básico).

2. **Método B: Markdown limpio**:
   - Usa tu `.md` original (Substack soporta Markdown básico).
   - **Ajusta manualmente** imágenes (Substack requiere subirlas desde su interfaz).

---

### 💼 **Paso 4: Publicar en LinkedIn**
1. **Desde Word (.docx)**:
   - Ve a LinkedIn → Crear publicación → **"Subir documento"**.
   - Selecciona tu `.docx` (convertirá a formato LinkedIn).

2. **Desde HTML/Markdown**:
   - Copia el contenido del `.html` o `.md` → Pega en el editor de LinkedIn.
   - **Revisa formato**: LinkedIn puede alterar encabezados y espaciado.

---

### ⚙️ **Automatización Avanzada (Opcional)**
1. **Script para convertir y publicar** (ejemplo en bash):
   ```bash
   #!/bin/bash
   pandoc "$1" -o "${1%.md}.html"
   open "${1%.md}.html"  # Para revisar antes de publicar
   ```

2. **Plugins de Obsidian útiles**:
   - **"Obsidian to HTML"**: Exporta con un clic.
   - **"Pandoc Plugin"**: Integra Pandoc directamente en Obsidian.

---

### 📌 **Notas Clave**
- **Imágenes**: Sube manualmente en Substack/LinkedIn (no se incrustan desde rutas locales).
- **Prueba antes**: LinkedIn y Substack pueden interpretar distinto el HTML/Markdown.
- **Plantillas personalizadas**: Crea una `.docx` base en Word con tus estilos para Pandoc.

---

**Ejemplo de comando todo-en-uno** (genera HTML y Word):
```bash
pandoc articulo.md -o articulo.html && pandoc articulo.md -o articulo.docx
```

¿Quieres ayuda para personalizar una plantilla de Pandoc o ajustar el CSS? 😊



## 💭 y cuando hay imágenes ...

Para reemplazar **rutas locales de imágenes** por **URLs públicas** (requerido en LinkedIn) y asegurar que se muestren correctamente en tu artículo, sigue estos pasos:

---

### 📌 **1. Sube las imágenes a un hosting público**
Necesitas que tus imágenes estén en línea. Opciones gratuitas/eficientes:
- **Imgur** (rápido y sin registro): [https://imgur.com/](https://imgur.com/)  
- **Google Drive** (comparte el enlace como "Cualquier persona con el enlace").  
- **Dropbox** (activa el enlace público).  
- **GitHub** (si tienes un repositorio, usa `https://raw.githubusercontent.com/...`).  

**Ejemplo con Imgur**:  
1. Ve a [Imgur](https://imgur.com/).  
2. Arrastra la imagen a la página.  
3. Copia el enlace directo (termina en `.jpg`, `.png`, etc.). Ejemplo:  
   ```plaintext
   https://i.imgur.com/TuCodigo.jpg
   ```

---

### ✨ **2. Modifica tu Markdown (`.md`)**
Reemplaza las rutas locales por las URLs públicas.  

**Antes** (ruta local en Obsidian):  
```markdown
![Loxodrómica](assets/loxodromica.png)
```

**Después** (URL pública):  
```markdown
![Loxodrómica](https://i.imgur.com/TuCodigo.png)
```

---

### ⚙️ **3. Automatización con Pandoc (opcional)**
Si tienes muchas imágenes, usa un **script** para reemplazar rutas automáticamente.  

#### **Ejemplo en Python** (`replace_images.py`):
```python
import re
import os

markdown_file = "De los Navegantes a Leibniz.md"
output_file = "LinkedIn_Ready.md"

# Diccionario de reemplazos: {"ruta_local": "url_publica"}
image_replacements = {
    "assets/loxodromica.png": "https://i.imgur.com/TuCodigo.png",
    "assets/mapa.jpg": "https://i.imgur.com/OtroCodigo.jpg"
}

with open(markdown_file, 'r', encoding='utf-8') as f:
    content = f.read()

for local_path, url in image_replacements.items():
    content = content.replace(f"]({local_path})", f"]({url})")

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Archivo '{output_file}' generado con URLs actualizadas.")
```

**Ejecútalo así**:  
```bash
python3 replace_images.py
```

---

### 📤 **4. Publica en LinkedIn**
1. **Si usas el `.docx` generado por Pandoc**:  
   - LinkedIn convertirá las imágenes **solo si están en URLs públicas**.  
   - Verifica que se vean en el Word antes de subirlo.  

2. **Si pegas directamente en el editor de LinkedIn**:  
   - Asegúrate de que el Markdown use URLs públicas.  
   - LinkedIn renderizará las imágenes automáticamente.  

---

### 🚨 **Notas importantes**  
- **Google Drive/Dropbox**: Si usas estos, cambia el enlace compartido a formato público. Ejemplo:  
  ```plaintext
  # Original (no funciona en LinkedIn):
  https://drive.google.com/file/d/1xYZ.../view?usp=sharing
  
  # Modificado (reemplaza 'view?usp=sharing' por 'uc?export=view'):
  https://drive.google.com/uc?export=view&id=1xYZ...
  ```
- **Tamaño de imágenes**: LinkedIn recomienda imágenes de **1200x627 px** para vista óptima.  

---

### 🔄 **Flujo completo automatizado**  
Combina todos los pasos en un script (`publish_linkedin.sh`):  
```bash
#!/bin/bash
# 1. Reemplaza rutas locales por URLs
python3 replace_images.py

# 2. Convierte a Word con Pandoc
pandoc LinkedIn_Ready.md -o Leibniz_LinkedIn.docx \
  --reference-doc=plantilla_pulse.docx \
  --lua-filter=linkedin.lua

# 3. Abre el archivo para revisión (macOS)
open Leibniz_LinkedIn.docx
```

Ejecuta:  
```bash
chmod +x publish_linkedin.sh
./publish_linkedin.sh
```

---

¿Necesitas ayuda para subir las imágenes a un hosting específico o ajustar el script? 😊



## ![git repo forked](/Users/juanjo/Library/Caches/com.rightfontapp.RightFont5/Glyphs/git repo forked.svg)Usando Github

¡Perfecto! Usar **GitHub como host de imágenes** es una excelente opción (gratis y con control de versiones). Aquí te detallo cómo adaptar el proceso:

---

### 📌 **1. Subir imágenes a GitHub y obtener URLs públicas**
#### **A) Opción Recomendada: Repositorio Público**
1. **Crea un repositorio público** (ej: `blog-images`) en tu GitHub.  
2. **Sube las imágenes** (arrástralas a la interfaz web o usa Git):  
   ```bash
   git clone https://github.com/tuusuario/blog-images.git
   cd blog-images
   cp /ruta/local/imagen.png ./
   git add .
   git commit -m "Añadir imagen para artículo"
   git push
   ```
3. **Obtén la URL RAW** de cada imagen:  
   - Ve a la imagen en GitHub → Haz clic en **"View Raw"** (o botón derecho → "Copiar dirección de la imagen").  
   - La URL debe tener este formato:  
     ```plaintext
     https://raw.githubusercontent.com/tuusuario/blog-images/main/imagen.png
     ```

#### **B) Opción Alternativa: Issues (sin repositorio extra)**
   - Crea un **issue** en cualquier repo tuyo → arrastra imágenes al cuadro de texto → GitHub las hosteará.  
   - URL tendrá formato:  
     ```plaintext
     https://user-images.githubusercontent.com/ID_IMAGEN/nombre.png
     ```

---

### ✨ **2. Modificar el Markdown para usar URLs de GitHub**
Reemplaza las rutas locales por las URLs de GitHub en tu `.md`:  
**Antes**:  
```markdown
![Loxodrómica](assets/loxodromica.png)
```
**Después**:  
```markdown
![Loxodrómica](https://raw.githubusercontent.com/tuusuario/blog-images/main/loxodromica.png)
```

---

### ⚙️ **3. Script Automatizado (Python) para Reemplazar Rutas**
Crea `github_images.py` para actualizar todas las imágenes:  
```python
import re

markdown_file = "De los Navegantes a Leibniz.md"
output_file = "LinkedIn_Ready.md"
repo_url = "https://raw.githubusercontent.com/tuusuario/blog-images/main/"

with open(markdown_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplaza rutas locales por URLs GitHub
content = re.sub(
    r'\!\[(.*?)\]\((assets\/.*?\.(png|jpg|jpeg))\)',
    f'![\\1]({repo_url}\\2)',
    content
)

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"✅ Markdown actualizado con URLs GitHub en '{output_file}'.")
```

**Ejecución**:  
```bash
python3 github_images.py
```

---

### 📤 **4. Generar el .docx con Pandoc (como antes)**
```bash
pandoc LinkedIn_Ready.md -o Leibniz_LinkedIn.docx \
  --reference-doc=plantilla_pulse.docx \
  --lua-filter=linkedin.lua
```

---

### 🔄 **Flujo Completo con GitHub (Script Todo-en-Uno)**
Crea `publish_linkedin_github.sh`:  
```bash
#!/bin/bash
# 1. Actualiza imágenes
python3 github_images.py

# 2. Convierte a Word
pandoc LinkedIn_Ready.md -o Leibniz_LinkedIn.docx \
  --reference-doc=plantilla_pulse.docx \
  --lua-filter=linkedin.lua

# 3. Sube imágenes a GitHub (opcional, si no lo hiciste antes)
cd /ruta/a/blog-images
git add .
git commit -m "Añadir imágenes para artículo LinkedIn"
git push origin main

# 4. Abre el documento (macOS)
open Leibniz_LinkedIn.docx
```

**Ejecuta**:  
```bash
chmod +x publish_linkedin_github.sh
./publish_linkedin_github.sh
```

---

### 🚨 **Notas Clave**  
- **Repositorio público**: GitHub solo sirve imágenes RAW desde repos públicos.  
- **Actualizaciones**: Si cambias una imagen, actualiza el archivo en GitHub y haz `git push`.  
- **Tamaños**: LinkedIn recomienda imágenes de **1200x627 px** para vista óptima.  

---

### 🌟 **Ventajas de Usar GitHub**  
- **Control de versiones**: Puedes revertir imágenes si algo falla.  
- **Gratis**: Sin límites de ancho de banda para uso personal.  
- **Integración con Obsidian**: Si usas Obsidian-Git, todo queda sincronizado.  

¿Necesitas ayuda para configurar el repositorio o ajustar el script? 😊