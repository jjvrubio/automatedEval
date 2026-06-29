# 📄 Documentación Técnica – Sistema de Conversión Pandoc

Esta documentación describe el sistema utilizado para convertir archivos `.md` en documentos `.docx` con formato académico avanzado, incluyendo portada, saltos de sección, y una tabla de contenidos dinámica compatible con Microsoft Word.

---

## 📁 Estructura del Proyecto

```
automatizaciones/
│
├── convertir-a-word.sh            # Script principal de conversión
├── portada.lua                    # Filtro Lua para insertar portada
├── docprep.lua                    # Filtro Lua para insertar saltos y campos TOC
├── substack.yaml                 # Metadatos del documento
├── plantilla_pulse_vacia.docx    # Plantilla Word personalizada
└── De los Navegantes a Leibniz.md  # Archivo fuente Markdown
```

---

## 🧩 1. Script Shell – `convertir-a-word.sh`

Este script ejecuta `pandoc` con filtros y configuraciones específicas.

```bash
pandoc "$MD" -o "$DOCX" \
  --metadata-file="$YAML" \
  --metadata link-citations=true \
  --from markdown+fenced_divs \
  --lua-filter="$LUA_PORTADA" \
  --lua-filter="$LUA_DOCPREP" \
  --citeproc \
  --bibliography="$BIB" \
  --csl="$CSL" \
  --resource-path="$IMGS" \
  "${REFERENCE_OPTION[@]}" \
  --verbose
```

🔍 **Nota**: No se usa `--toc` porque el índice se inserta como campo dinámico OpenXML desde el filtro `docprep.lua`.

---

## 📄 2. Filtro Lua – `docprep.lua`

Responsable de:
- Insertar saltos de sección antes de encabezados clave
- Insertar un campo de tabla de contenidos Word si se encuentra `:::toc:::`

```lua
local pandoc = require("pandoc")

local triggers = {
  ["Título"] = true,
  ["Referencias"] = true,
  ["Bibliografía"] = true,
  ["Anexos"] = true,
  ["Agradecimientos"] = true
}

local function insert_section_break()
  return pandoc.RawBlock("openxml", [[
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
<w:sectPr/>
]])
end

local function insert_toc_field()
  return pandoc.RawBlock("openxml", [[
<w:p>
  <w:r>
    <w:fldSimple w:instr="TOC \o \"1-3\" \h"/>
  </w:r>
</w:p>
]])
end

function Header(elem)
  local text = pandoc.utils.stringify(elem)
  print("📌 Encabezado detectado: '" .. text .. "'")
  for k, _ in pairs(triggers) do
    if text:match(k) then
      print("✅ Coincidencia parcial con: " .. k)
      return { insert_section_break(), elem }
    end
  end
  return elem
end
```

---

## 🧾 3. Filtro Lua – `portada.lua`

Este filtro prepara metainformación y elementos de portada, en coherencia con `substack.yaml`.

---

## 📑 4. Plantilla Word – `plantilla_pulse_vacia.docx`

Contiene:
- Estilos personalizados
- Campo de contenido dinámico (TOC) insertado manualmente
- Márgenes, fuente y diseño coherente con presentación académica profesional

📌 **Importante**: No debe contener ya un campo de índice si se usará `:::toc:::`. En caso contrario, debe tener el marcador TOC si se genera desde Pandoc.

---

## 📘 5. YAML – `substack.yaml`

Archivo de metadatos que alimenta la portada y configuraciones base.

```yaml
title: "De los Navegantes a Leibniz"
author: "Juan José Vázquez Rubio"
date: "2025-06-11"
lang: "es"
```

---

## ✅ Resultado Esperado

- Documento `.docx` limpio, con:
  - Portada personalizada
  - Tabla de contenidos que Word puede actualizar
  - Saltos de sección antes de bloques estructurales
  - Bibliografía automática con estilo APA 7

---

## 🧪 Recomendaciones Finales

- Revisar que `:::toc:::` se incluya en el `.md` si se desea insertar el campo TOC
- Asegurarse de que la plantilla `.docx` tiene un marcador TOC para actualizar manualmente
- Desactivar `--toc` en el `.sh` para evitar conflictos

---

© 2025 – Sistema de Publicación Automatizada Pandoc + Lua + Word
