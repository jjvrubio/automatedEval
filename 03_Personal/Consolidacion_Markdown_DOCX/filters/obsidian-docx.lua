-- obsidian-docx.lua
-- Normalizes common Obsidian syntax for DOCX output.
--
-- Callouts are wrapped in a one-cell Word table.  A private text marker lets
-- the Python postprocessor apply the final colour and Apple Symbols icon while
-- all body blocks remain normal Pandoc content (lists, links, images, etc.).

local pandoc = require("pandoc")

local script_dir = PANDOC_SCRIPT_FILE and PANDOC_SCRIPT_FILE:match("^(.*[/\\])") or "filters/"
local sf_symbols_dir = script_dir .. "../assets/icons/sf-symbols/"

local callout_icons = {
  abstract = "note", attention = "warning", bug = "danger", caution = "warning",
  check = "success", cite = "quote", danger = "danger", done = "success",
  error = "danger", example = "example", fail = "danger", failure = "danger",
  faq = "question", help = "question", hint = "tip", important = "danger",
  info = "info", missing = "warning", note = "note", question = "question",
  quote = "quote", success = "success", summary = "note", tip = "tip",
  tldr = "note", todo = "info", warning = "warning",
}

local callout_titles = {
  abstract = "Resumen",
  attention = "Atencion",
  bug = "Error",
  caution = "Cautela",
  check = "Correcto",
  cite = "Cita",
  danger = "Peligro",
  done = "Completado",
  error = "Error",
  example = "Ejemplo",
  fail = "Fallo",
  failure = "Fallo",
  faq = "Pregunta",
  help = "Ayuda",
  hint = "Sugerencia",
  important = "Importante",
  info = "Informacion",
  missing = "Falta",
  note = "Nota",
  question = "Pregunta",
  quote = "Cita",
  success = "Exito",
  summary = "Resumen",
  tip = "Consejo",
  tldr = "Resumen",
  todo = "Pendiente",
  warning = "Advertencia",
}

local function titlecase(value)
  if not value or value == "" then return "Callout" end
  return value:sub(1, 1):upper() .. value:sub(2):lower()
end

local function callout_label(kind)
  return callout_titles[kind:lower()] or titlecase(kind)
end

local function is_image_target(target)
  local lower = target:lower()
  return lower:match("%.png$") or lower:match("%.jpe?g$") or lower:match("%.gif$")
    or lower:match("%.webp$") or lower:match("%.svg$")
end

local function image_from_obsidian_target(target)
  local path, caption = target:match("^([^|]+)|(.+)$")
  if path then
    target = path
  end

  if not is_image_target(target) then return nil end

  local alt = caption or target:gsub("^.*/", ""):gsub("%.[^.]+$", "")
  return pandoc.Image({ pandoc.Str(alt) }, target)
end

local function as_callout(kind, title_inlines, body_blocks)
  kind = kind:lower()
  local title = title_inlines
  if not title or #title == 0 then
    title = { pandoc.Str(callout_label(kind)) }
  end

  local marker = "[MD2DOCX_CALLOUT:" .. kind .. "]"
  local icon_name = callout_icons[kind] or "info"
  local icon = pandoc.Image(
    {},
    sf_symbols_dir .. icon_name .. ".png",
    "",
    pandoc.Attr("", { "sf-symbol", "sf-symbol-" .. icon_name }, {
      width = "0.18in",
      height = "0.18in",
    })
  )
  local blocks = {
    pandoc.RawBlock("openxml", [[
<w:tbl>
  <w:tblPr><w:tblW w:w="5000" w:type="pct"/></w:tblPr>
  <w:tr><w:tc><w:tcPr><w:tcW w:w="5000" w:type="pct"/></w:tcPr>
]]),
    pandoc.Para({
      pandoc.Str(marker), pandoc.Space(), icon, pandoc.Space(), pandoc.Strong(title)
    }),
  }
  for _, block in ipairs(body_blocks) do
    blocks[#blocks + 1] = block
  end
  blocks[#blocks + 1] = pandoc.RawBlock("openxml", "</w:tc></w:tr></w:tbl>")
  return blocks
end

local function strip_leading_breaks(inlines)
  while inlines[1] and (inlines[1].t == "Space" or inlines[1].t == "SoftBreak" or inlines[1].t == "LineBreak") do
    table.remove(inlines, 1)
  end
  return inlines
end

function BlockQuote(el)
  if not FORMAT:match("docx") then return nil end

  local first = el.content[1]
  if not first or first.t ~= "Para" then return nil end

  local marker = first.content[1]
  if not marker or marker.t ~= "Str" then return nil end

  local kind = marker.text:match("^%[!([%w%-]+)%][%+%-]?$")
  if not kind then return nil end

  local rest = {}
  for i = 2, #first.content do
    rest[#rest + 1] = first.content[i]
  end
  -- A Space means a custom title on the marker line. A SoftBreak means the
  -- next line is body content and must remain as the title/body separator.
  while rest[1] and rest[1].t == "Space" do
    table.remove(rest, 1)
  end

  local title_inlines = {}
  local body_inlines = {}
  local in_body = false
  for _, inline in ipairs(rest) do
    if not in_body and (inline.t == "SoftBreak" or inline.t == "LineBreak") then
      in_body = true
    elseif in_body then
      body_inlines[#body_inlines + 1] = inline
    else
      title_inlines[#title_inlines + 1] = inline
    end
  end

  local body = {}
  strip_leading_breaks(body_inlines)
  if #body_inlines > 0 then
    body[#body + 1] = pandoc.Para(body_inlines)
  end
  for i = 2, #el.content do
    body[#body + 1] = el.content[i]
  end

  return as_callout(kind, title_inlines, body)
end

function CodeBlock(el)
  if not FORMAT:match("docx") then return nil end

  local kind
  for _, class in ipairs(el.classes) do
    local match = class:match("^ad%-(.+)$")
    if match then
      kind = match
      break
    end
  end
  if not kind then return nil end

  local text = el.text or ""
  local firstline, remainder = text:match("^([^\n]*)\n?(.*)$")
  local title_text
  local body_md = text

  if firstline then
    title_text = firstline:match("^%s*[Tt]itle:%s*(.*)$")
    if title_text then
      body_md = remainder:gsub("^%s+", "")
    end
  end

  local title_inlines
  if title_text and title_text ~= "" then
    title_inlines = pandoc.read(title_text, "markdown").blocks[1].content
  end

  local body = pandoc.read(body_md, "markdown+fenced_divs").blocks
  return as_callout(kind, title_inlines, body)
end

function Mark(el)
  if not FORMAT:match("docx") then return nil end
  return nil
end

function Para(el)
  if not FORMAT:match("docx") then return nil end

  local text = pandoc.utils.stringify(el)
  local target = text:match("^!%[%[([^%]]+)%]%]$")
  if not target then return nil end

  local image = image_from_obsidian_target(target)
  if not image then return nil end
  return pandoc.Para({ image })
end

function Str(el)
  if not FORMAT:match("docx") then return nil end

  local target = el.text:match("^!%[%[([^%]]+)%]%]$")
  if not target then return nil end

  return image_from_obsidian_target(target)
end
