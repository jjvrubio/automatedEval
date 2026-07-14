-- commercial-cover.lua
--
-- El perfil commercial_proposal usa el bloque inicial del Markdown como
-- contenido de portada. Python extrae sus textos antes de ejecutar Pandoc;
-- este filtro elimina el bloque original para que no se repita en el cuerpo.
--
-- Estructura esperada:
--   # Subtitulo
--   # Titulo
--   ## Linea secundaria
--   > Control documental opcional
--   ---

function Pandoc(doc)
  local level_one_count = 0
  local found_secondary = false
  local boundary = nil

  for index, block in ipairs(doc.blocks) do
    if block.t == "Header" and block.level == 1 then
      level_one_count = level_one_count + 1
    elseif block.t == "Header" and block.level == 2 and level_one_count >= 2 then
      found_secondary = true
    elseif block.t == "HorizontalRule" and found_secondary then
      boundary = index
      break
    end
  end

  if not boundary then
    return doc
  end

  local remaining = pandoc.Blocks({})
  for index = boundary + 1, #doc.blocks do
    remaining:insert(doc.blocks[index])
  end
  doc.blocks = remaining

  -- La portada nativa ya representa estos metadatos. Si permanecen, el
  -- escritor DOCX de Pandoc añade un segundo bloque de titulo antes del TOC.
  doc.meta.title = nil
  doc.meta.subtitle = nil
  doc.meta.author = nil
  doc.meta.date = nil
  return doc
end
