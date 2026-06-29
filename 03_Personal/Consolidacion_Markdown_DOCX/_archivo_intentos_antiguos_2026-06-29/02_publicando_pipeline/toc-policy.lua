-- toc-policy.lua
-- Pandoc Lua filter: keep ToC only for selected doc_class values.

local longform_classes = {
  informe = true,
  capítulo = true,
  tésis = true,
  whitepaper = true
}

local allow_toc = false

-- Extrae un valor de metadato como string, manejando los diferentes tipos de Pandoc
-- @param meta: tabla de metadatos del documento
-- @param key: clave del metadato a extraer (ej: "doc_class", "title")
-- @return: string con el valor, o nil si no existe
local function get_meta_string(meta, key)
  local v = meta[key]
  
  -- Si el metadato no existe, devolver nil
  if not v then return nil end
  
  -- Caso 1: El valor ya es un string de Lua nativo
  if type(v) == "string" then return v end
  
  -- Caso 2: Es un objeto MetaString de Pandoc (tiene la propiedad .text)
  if v.t == "MetaString" then return v.text end
  
  -- Caso 3: Es una lista de elementos inline (MetaInlines)
  -- Por ejemplo: "doc_class: chapter" puede parsearse como Inlines
  if v.t == "MetaInlines" then
    return pandoc.utils.stringify(v)
  end
  
  -- Caso por defecto: intentar convertir cualquier otro tipo a string
  -- Funciona para MetaBlocks, MetaBool, etc.
  return pandoc.utils.stringify(v)
end



function Meta(meta)
  local category = get_meta_string(meta, "doc_class")
  if category and longform_classes[category] then
    allow_toc = true
  else
    allow_toc = false
  end
  return meta
end

-- HTML: Pandoc often renders TOC as a Div with identifier "TOC"
function Div(div)
  if not allow_toc and div.identifier == "TOC" then
    return {} -- remove it
  end
  return div
end

-- Cross-format: remove an explicit "Table of Contents" header if it exists
-- This helps in cases where templates render a heading for the TOC section.
local function is_toc_header(h)
  if h.t ~= "Header" then return false end
  local txt = pandoc.utils.stringify(h.content):lower()
  return (txt == "table of contents" or txt == "contents" or txt == "índice" or txt == "indice")
end

-- Remove the header and (optionally) the following bullet list if it looks like a TOC
function Blocks(blocks)
  if allow_toc then return blocks end

  local out = pandoc.List:new()
  local i = 1
  while i <= #blocks do
    local b = blocks[i]

    if is_toc_header(b) then
      -- skip this header
      i = i + 1

      -- If the next block is a BulletList or OrderedList (often the TOC),
      -- skip it too. If not, leave it.
      if i <= #blocks then
        local nb = blocks[i]
        if nb.t == "BulletList" or nb.t == "OrderedList" then
          i = i + 1
        end
      end

    else
      out:insert(b)
      i = i + 1
    end
  end

  return out
end
