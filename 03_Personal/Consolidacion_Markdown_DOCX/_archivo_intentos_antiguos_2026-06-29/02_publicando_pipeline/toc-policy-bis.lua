-- toc-policy.lua
-- Controla la presencia y profundidad del Table of Contents (ToC) en exportación Pandoc
-- en función de la categoría semántica declarada en frontmatter: doc_category.
--
-- Objetivo: NO ensuciar el Markdown con reglas de exportación.
-- El documento declara QUÉ es; la exportación decide CÓMO se proyecta.
--
-- Uso recomendado (CLI o plugin Pandoc de Obsidian):
--   --lua-filter=/ruta/a/toc-policy.lua
--
-- Nota: si llamas Pandoc con --toc, este filtro funciona igualmente:
--       - Mantendrá el ToC solo cuando proceda
--       - Lo bloqueará cuando no proceda (meta.toc=false + supresión de Div#TOC en HTML)

-- ========= Config =========

-- Política: doc_category -> toc-depth
-- Si una categoría NO está aquí, por defecto NO hay ToC.
local toc_policy = {
  ensayo   = 2,
  artículo = 2,
  informe  = 3,
  capítulo = 3,
  tesis  = 4, -- usa 3 si no quieres tanta granularidad
}

-- Si doc_category no está, pero deseas un fallback para ciertos tipos, puedes definirlo aquí:
-- local default_depth = nil

-- Logging (depuración): ponlo a true si quieres ver trazas en stderr.
local DEBUG = true

-- ========= Estado interno =========

local allow_toc = false
local effective_depth = nil

-- ========= Utilidades =========

local function log(msg)
  if DEBUG then
    io.stderr:write("[toc-policy] " .. msg .. "\n")
  end
end

-- Convierte un valor de metadata (MetaString, MetaInlines, etc.) en string de forma robusta
local function meta_to_string(v)
  if not v then return nil end
  return pandoc.utils.stringify(v)
end

-- Normaliza string: trim + minúsculas (para tolerar "Report", " report ", etc.)
local function normalize(s)
  if not s then return nil end
  -- trim
  s = s:gsub("^%s+", ""):gsub("%s+$", "")
  -- lower
  s = s:lower()
  return s
end

-- ========= Hooks Pandoc =========

-- Se ejecuta al leer el frontmatter
function Meta(meta)
  local category_raw = meta_to_string(meta.doc_category)
  local category = normalize(category_raw)

  log("doc_category(raw)=" .. tostring(category_raw))
  log("doc_category(norm)=" .. tostring(category))

  local depth = nil
  if category then
    depth = toc_policy[category]
  end

  if depth then
    allow_toc = true
    effective_depth = depth

    -- Inyectamos metadata que Pandoc entiende
    meta["toc"] = true
    meta["toc-depth"] = depth

    log("ALLOW ToC: toc=true, toc-depth=" .. tostring(depth))
  else
    allow_toc = false
    effective_depth = nil

    -- Modo defensivo: si alguien invocó Pandoc con --toc, esto ayuda a bloquearlo
    meta["toc"] = false

    log("BLOCK ToC: toc=false (category sin política)")
  end

  return meta
end

-- HTML: Pandoc suele crear un <div id="TOC">...</div>.
-- Si no se permite ToC, lo eliminamos.
function Div(div)
  if not allow_toc and div.identifier == "TOC" then
    log("Removing Div#TOC")
    return {}
  end
  return div
end
