-- obsidian-docx.lua
-- Normalizes common Obsidian syntax for DOCX output.
--
-- The filter keeps the output in Pandoc's document model instead of emitting
-- raw OpenXML. Callouts use a built-in Word style by default so they render
-- acceptably with generic reference DOCX files.

local pandoc = require("pandoc")

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

local function style_name(kind)
  local k = kind:lower()
  local styles = {
    abstract = "Callout Note",
    attention = "Callout Attention",
    bug = "Callout Danger",
    caution = "Callout Warning",
    check = "Callout Success",
    cite = "Callout Quote",
    danger = "Callout Danger",
    done = "Callout Success",
    error = "Callout Danger",
    example = "Callout Example",
    fail = "Callout Danger",
    failure = "Callout Danger",
    faq = "Callout Question",
    help = "Callout Question",
    hint = "Callout Hint",
    important = "Callout Important",
    info = "Callout Info",
    missing = "Callout Warning",
    note = "Callout Note",
    question = "Callout Question",
    quote = "Callout Quote",
    success = "Callout Success",
    summary = "Callout Note",
    tip = "Callout Tip",
    tldr = "Callout Note",
    todo = "Callout Info",
    warning = "Callout Warning",
  }
  return styles[k] or "Callout Note"
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
  local title = title_inlines
  if not title or #title == 0 then
    title = { pandoc.Str(callout_label(kind)) }
  end

  local blocks = {
    pandoc.Para({ pandoc.Strong(title) }),
  }
  for _, block in ipairs(body_blocks) do
    blocks[#blocks + 1] = block
  end

  return pandoc.Div(
    blocks,
    pandoc.Attr(
      "",
      { "callout", "callout-" .. kind:lower() },
      { ["custom-style"] = style_name(kind) }
    )
  )
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
  strip_leading_breaks(rest)

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
