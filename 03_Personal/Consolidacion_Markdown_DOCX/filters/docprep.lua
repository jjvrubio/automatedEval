-- docprep.lua
-- Insert a Word TOC field for docx output.

local pandoc = require("pandoc")

local toc_depth = 3
local want_toc = false
local saw_toc_marker = false

local function insert_toc_field()
  local instr = string.format('TOC \\o "1-%d" \\h \\z \\u', toc_depth)
  return pandoc.RawBlock("openxml", string.format([[
<w:p>
  <w:r>
    <w:fldSimple w:instr="%s"/>
  </w:r>
</w:p>
]], instr))
end

local function get_meta_bool(meta, key)
  local v = meta[key]
  if v == nil then return nil end
  if type(v) == "boolean" then return v end
  if v.t == "MetaBool" then return v.c end
  local s = pandoc.utils.stringify(v):lower()
  if s == "true" or s == "yes" or s == "1" then return true end
  if s == "false" or s == "no" or s == "0" then return false end
  return nil
end

local function get_meta_int(meta, key)
  local v = meta[key]
  if v == nil then return nil end
  if type(v) == "number" then return v end
  local s = pandoc.utils.stringify(v)
  return tonumber(s)
end

local function has_class(div, name)
  for _, c in ipairs(div.classes) do
    if c == name then
      return true
    end
  end
  return false
end

function Meta(meta)
  local depth = get_meta_int(meta, "toc-depth") or get_meta_int(meta, "toc_depth")
  if depth then toc_depth = depth end

  local want = get_meta_bool(meta, "toc")
  if want ~= nil then want_toc = want end
  return meta
end

function Div(div)
  if not FORMAT:match("docx") then return div end
  if div.identifier == "toc" or has_class(div, "toc") then
    saw_toc_marker = true
    return { insert_toc_field() }
  end
  return div
end

function Pandoc(doc)
  if not FORMAT:match("docx") then return doc end
  if want_toc and not saw_toc_marker then
    table.insert(doc.blocks, 1, insert_toc_field())
  end
  return doc
end
