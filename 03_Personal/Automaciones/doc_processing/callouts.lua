-- callouts.lua
-- Convierte callouts de Obsidian (>[!tipo] titulo / cuerpo) y bloques de
-- admonition (```ad-tipo ... ```) en cajas tcolorbox `callout` (definidas en
-- la plantilla LaTeX). Cada tipo se mapea a un color; los desconocidos usan gris.

local type_color = {
  tip = "green", hint = "green", success = "green", check = "green", done = "green",
  note = "blue", info = "blue", abstract = "blue", summary = "blue", tldr = "blue",
  todo = "blue", question = "blue", help = "blue", faq = "blue",
  important = "red", danger = "red", error = "red", bug = "red",
  failure = "red", fail = "red", missing = "red",
  warning = "orange", caution = "orange", attention = "orange",
  example = "violet", quote = "gray", cite = "gray",
}

local function color_for(t)
  return type_color[string.lower(t)] or "gray"
end

local function capitalize(t)
  return t:sub(1, 1):upper() .. t:sub(2)
end

-- Renderiza una lista de inlines a una cadena LaTeX (escapada por pandoc).
local function inlines_to_latex(inlines)
  if not inlines or #inlines == 0 then return nil end
  local s = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), "latex")
  return (s:gsub("%s+$", ""))
end

-- Renderiza una cadena Markdown a LaTeX (para titulos provenientes de texto).
local function text_to_latex(str)
  local s = pandoc.write(pandoc.read(str, "markdown"), "latex")
  return (s:gsub("%s+$", ""))
end

local function wrap_callout(color, title_latex, body_blocks)
  local out = {}
  out[#out + 1] = pandoc.RawBlock("latex",
    "\\begin{callout}{" .. color .. "}{" .. (title_latex or "") .. "}")
  for _, b in ipairs(body_blocks) do out[#out + 1] = b end
  out[#out + 1] = pandoc.RawBlock("latex", "\\end{callout}")
  return out
end

-- Callouts de Obsidian: blockquote cuyo primer inline es Str "[!tipo]".
function BlockQuote(el)
  local first = el.content[1]
  if not first or first.t ~= "Para" then return nil end
  local marker = first.content[1]
  if not marker or marker.t ~= "Str" then return nil end
  local typ = marker.text:match("^%[!([%w%-]+)%][%+%-]?$")
  if not typ then return nil end

  -- inlines tras el marcador (saltando espacios/saltos iniciales)
  local rest = {}
  for i = 2, #first.content do rest[#rest + 1] = first.content[i] end
  while rest[1] and (rest[1].t == "Space" or rest[1].t == "SoftBreak") do
    table.remove(rest, 1)
  end

  -- separar titulo (hasta el primer salto de linea) y cuerpo en linea
  local title_inlines, body_inlines, hit = {}, {}, false
  for _, il in ipairs(rest) do
    if not hit and (il.t == "SoftBreak" or il.t == "LineBreak") then
      hit = true
    elseif hit then
      body_inlines[#body_inlines + 1] = il
    else
      title_inlines[#title_inlines + 1] = il
    end
  end

  local body = {}
  if #body_inlines > 0 then body[#body + 1] = pandoc.Para(body_inlines) end
  for i = 2, #el.content do body[#body + 1] = el.content[i] end

  local title = inlines_to_latex(title_inlines) or capitalize(typ)
  return wrap_callout(color_for(typ), title, body)
end

-- Admonition: ```ad-tipo  con posible "title:" en la primera linea.
function CodeBlock(el)
  local typ
  for _, c in ipairs(el.classes) do
    local m = c:match("^ad%-(.+)$")
    if m then typ = m; break end
  end
  if not typ then return nil end

  local text = el.text or ""
  local title, body_md = nil, text
  local firstline, remainder = text:match("^([^\n]*)\n?(.*)$")
  if firstline then
    local t = firstline:match("^%s*[Tt]itle:%s*(.*)$")
    if t then
      title = t
      body_md = remainder:gsub("^%s+", "")
    end
  end

  local title_latex
  if title and title ~= "" then
    title_latex = text_to_latex(title)
  else
    title_latex = capitalize(typ)
  end

  local body_blocks = pandoc.read(body_md, "markdown").blocks
  return wrap_callout(color_for(typ), title_latex, body_blocks)
end
