-- Filtro para Pandoc: docprep.lua
-- Versión sin detección de TOC; se confía en el campo de índice de la plantilla Word

local pandoc = require("pandoc")

-- Triggers principales para insertar salto de sección
local triggers = {
  ["Título"] = true,
  ["Referencias"] = true,
  ["Bibliografía"] = true,
  ["Anexos"] = true,
  ["Agradecimientos"] = true
}

-- Función para insertar salto de sección (section break)
local function insert_section_break()
  return pandoc.RawBlock("openxml", [[
<w:p>
  <w:r>
    <w:br w:type="page"/>
  </w:r>
</w:p>
<w:sectPr/>
]])
end

-- Filtro para encabezados: inserta section break antes de encabezados clave
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
