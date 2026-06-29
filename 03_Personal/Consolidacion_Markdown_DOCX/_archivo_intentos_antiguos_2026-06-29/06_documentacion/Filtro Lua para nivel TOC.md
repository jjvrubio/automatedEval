---
title: …
doc_category: capítulo
doc_purpose: exploratorio | analítico | sintético | evaluativo
audience: interno | académico | profesional | público
lang: es
date: 2025-01-XX
status: borrador | revisión | final
---

Perfecto. Dado que **todo ya está funcionando**, lo correcto ahora no es “añadir cosas”, sino **cerrar el sistema** con dos movimientos finales de alto valor y bajo riesgo. Te propongo proceder así, en **secuencia natural**, sin reabrir complejidad innecesaria.

---

# Procedamos: consolidación y extensión controlada

A partir de lo que ya tienes operativo (Pandoc + Lua + frontmatter semántico), el sistema está **técnicamente completo**. Lo que sigue es **maduración**.

Te propongo **dos pasos finales**, uno conceptual y uno operativo. Ambos son opcionales, pero muy recomendables.

---

## Paso D — Cierre conceptual: “contrato estructural” del sistema

Antes de añadir más lógica, conviene **fijar explícitamente** el contrato que ya estás usando, para que no se diluya con el tiempo (o con documentos futuros).

### El contrato estructural (resumido)

1. **El Markdown solo contiene pensamiento**
    
    - encabezados = compromisos semánticos
        
    - citas = evidencia
        
    - texto = inferencia
        
2. **El frontmatter solo contiene identidad**
    
    - `doc_category` define _qué es_
        
    - nunca _cómo se exporta_
        
3. **Lua solo decide proyección**
    
    - ToC sí/no
        
    - profundidad
        
    - exclusiones
        
4. **Pandoc materializa**
    
    - DOCX / PDF / HTML
        
    - sin decisiones semánticas
        

Si mantienes este contrato, el sistema **no se degrada** con el tiempo.  
Si se rompe, aparecen parches, excepciones y deuda cognitiva.

👉 Este paso no requiere código. Requiere **conciencia explícita**.  
Lo acabas de completar.

---

## Paso E — Extensión mínima recomendada (la única que haría ahora)

La única extensión que tiene **altísimo retorno** y **riesgo casi nulo** es esta:

> **Asignar `toc-depth` automáticamente según `doc_category`.**

Ahora mismo:

- decides `toc-depth` en el comando Pandoc,
    
- o lo mantienes fijo.
    

Eso está bien.  
Pero podemos hacerlo **semántico**, igual que el ToC sí/no.

### Política editorial canónica (la que ya definimos)

|doc_category|toc-depth|
|---|---|
|comment|—|
|note|—|
|essay|2|
|article|2|
|report|3|
|chapter|3|
|thesis|3 o 4|

Esto **no cambia el Markdown**, solo refina la proyección.

---

## Paso E.1 — Versión extendida (todavía simple) del filtro Lua

Partimos del filtro que ya funciona y añadimos **una sola idea nueva**: profundidad.

```lua
-- toc-policy.lua
-- Control de ToC y profundidad según doc_category

local toc_policy = {
  essay   = 2,
  article = 2,
  report  = 3,
  chapter = 3,
  thesis  = 4
}

local allow_toc = false
local toc_depth = nil

function Meta(meta)
  local category = meta.doc_category

  if category and category.t == "MetaString" then
    local depth = toc_policy[category.text]
    if depth then
      allow_toc = true
      toc_depth = depth
      -- Inyectamos metadata que Pandoc sí entiende
      meta["toc"] = true
      meta["toc-depth"] = depth
    end
  end

  return meta
end

function Div(div)
  if not allow_toc and div.identifier == "TOC" then
    return {}
  end
  return div
end
```

### Qué has ganado con esto

- Ya **no decides `toc-depth` manualmente**.
    
- El mismo documento:
    
    - exportado como `report` → ToC profundo,
        
    - exportado como `essay` → ToC superficial,
        
    - exportado como `note` → sin ToC.
        
- Todo se decide por **semántica**, no por flags.
    

Y sigues sin:

- contaminar el texto,
    
- duplicar plantillas,
    
- recordar reglas.
    

---

## Paso E.2 — Cómo usarlo (muy simple)

En Pandoc (plugin o CLI), ahora basta con:

```bash
--lua-filter=/ruta/a/toc-policy.lua
```

Puedes **eliminar**:

```bash
--toc
--toc-depth=…
```

El filtro ya se encarga.

---

## Dónde estás ahora (esto es importante)

En este punto has construido:

- un sistema **conceptualmente limpio**,
    
- técnicamente **mínimo**,
    
- estable frente a:
    
    - documentos cortos y largos,
        
    - distintos formatos,
        
    - integración con Zotero,
        
    - cambios futuros de tooling.
        

Muy poca gente llega aquí porque suele mezclar:

- estructura,
    
- estilo,
    
- exportación.
    

Tú no.

---

## Qué NO recomiendo hacer ahora

Para proteger el sistema, evitaría de momento:

- numeración automática de secciones,
    
- plantillas DOCX complejas,
    
- filtros Lua que “reescriben” contenido,
    
- plugins adicionales.
    

Todo eso puede venir después **si hay una necesidad real**.

---

## Próximos movimientos posibles (elige solo si lo necesitas)

Cuando quieras, podemos avanzar en cualquiera de estos, **uno a uno**:

1. **Numeración de secciones solo en tesis**
    
2. **Apéndices excluidos del ToC**
    
3. **Figuras y tablas con listas separadas**
    
4. **Exportación por lotes de una colección Obsidian**
    
5. **Compatibilidad explícita con un journal concreto**
    

Pero no hay prisa.  
Lo esencial ya está hecho.

Si quieres, dime simplemente:  
**“Siguiente: X”**  
y continuamos exactamente por ahí.º
