-- page-section-breaks.lua
--
-- Convierte separadores horizontales Markdown en saltos de Word:
--   ---       -> salto de pagina
--   --- + --- -> salto de seccion en pagina siguiente
--
-- Pandoc ya ha consumido el frontmatter YAML antes de ejecutar los filtros,
-- por lo que sus delimitadores `---` no llegan aqui como HorizontalRule.

local page_break = [[
<w:p>
  <w:r><w:br w:type="page"/></w:r>
</w:p>
]]

local next_page_section_break = [[
<w:p>
  <w:pPr>
    <w:sectPr>
      <w:type w:val="nextPage"/>
    </w:sectPr>
  </w:pPr>
</w:p>
]]

function Blocks(blocks)
  local result = pandoc.Blocks({})
  local index = 1

  while index <= #blocks do
    if blocks[index].t ~= "HorizontalRule" then
      result:insert(blocks[index])
      index = index + 1
    elseif index < #blocks and blocks[index + 1].t == "HorizontalRule" then
      result:insert(pandoc.RawBlock("openxml", next_page_section_break))
      index = index + 2
    else
      result:insert(pandoc.RawBlock("openxml", page_break))
      index = index + 1
    end
  end

  return result
end
