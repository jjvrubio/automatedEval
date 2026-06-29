-- === portada.lua (versión robusta y visible) ===

local portada = {}

-- Salto de sección (Word: nueva sección en página siguiente)
local function sectionBreak()
  return pandoc.RawBlock("openxml", [[
<w:p>
  <w:pPr>
    <w:sectPr>
      <w:type w:val="nextPage"/>
    </w:sectPr>
  </w:pPr>
</w:p>
]])
end

-- Construcción de portada desde metadatos
function Meta(meta)
  -- Inicia nueva sección para la portada
  table.insert(portada, sectionBreak())

  -- Título (Header 1)
  if meta.title then
    local texto = pandoc.utils.stringify(meta.title)
    table.insert(portada, pandoc.Header(1, { pandoc.Str(texto) }))
  end

  -- Autor (Header 2 + párrafo)
  if meta.author then
    local texto = pandoc.utils.stringify(meta.author)
    table.insert(portada, pandoc.Header(2, { pandoc.Str("Autor") }))
    table.insert(portada, pandoc.Para({ pandoc.Str(texto) }))
  end

  -- Destino (Header 2 + párrafo)
  if meta.destination then
    local texto = pandoc.utils.stringify(meta.destination)
    table.insert(portada, pandoc.Header(2, { pandoc.Str("Destino") }))
    table.insert(portada, pandoc.Para({ pandoc.Str(texto) }))
  end

  -- Fecha (Header 2 + párrafo)
  if meta.date then
    local texto = pandoc.utils.stringify(meta.date)
    table.insert(portada, pandoc.Header(2, { pandoc.Str("Fecha") }))
    table.insert(portada, pandoc.Para({ pandoc.Str(texto) }))
  end

  -- Cierra la sección de portada
  table.insert(portada, sectionBreak())

  -- Elimina metadatos
  meta.title = nil
  meta.author = nil
  meta.date = nil

  return meta
end

-- Inserta la portada al principio
function Pandoc(doc)
  local nuevos_bloques = {}
  for _, block in ipairs(portada) do
    table.insert(nuevos_bloques, block)
  end
  for _, block in ipairs(doc.blocks) do
    table.insert(nuevos_bloques, block)
  end
  return pandoc.Pandoc(nuevos_bloques, doc.meta)
end
