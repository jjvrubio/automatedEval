
# Paso B — Alineación de profundidad de ToC con estándares editoriales

_(incluyendo frontmatter para todo el espectro: comentario → tesis)_

---

## 1. El problema real que resolvemos en el Paso B

El problema **no** es técnico (“cómo poner `toc-depth`”), sino epistemológico:

> ¿Cómo representar, con una sola estructura interna coherente,  
> documentos que editorialmente pertenecen a _clases radicalmente distintas_?

Ejemplos extremos:

- un **comentario conceptual** de 2 páginas,
    
- una **tesis doctoral** de 300 páginas,
    

…sin:

- duplicar plantillas,
    
- contaminar el texto con instrucciones de exportación,
    
- ni romper la trazabilidad académica.
    

La solución es separar **tres planos**:

1. **Plano semántico** → _qué es este documento_
    
2. **Plano estructural** → _qué niveles existen_ (Paso A, ya fijado)
    
3. **Plano editorial** → _qué niveles se muestran en el ToC_
    

El _frontmatter_ pertenece **solo al plano 1**.

---

## 2. Frontmatter canónico para TODO el espectro documental

Este es el _frontmatter_ **único y suficiente**, válido desde comentario hasta tesis:

```yaml
---
title: "…"
doc_category: comment | note | essay | article | report | chapter | thesis
doc_purpose: exploratory | analytical | synthetic | evaluative
audience: internal | academic | professional | public
lang: es
date: 2025-01-XX
status: draft | review | final
---
```

### Por qué este esquema funciona

- `doc_category` define **clase editorial** (no técnica)
    
- `doc_purpose` define **modo cognitivo dominante**
    
- `audience` define **nivel de explicitación esperado**
    

⚠️ Observa lo que **no** aparece:

- no hay `toc: true`
    
- no hay `toc-depth`
    
- no hay nada específico de Pandoc
    

Este _frontmatter_ es:

- estable en el tiempo,
    
- reutilizable,
    
- legible por humanos,
    
- interpretable por Lua, Pandoc o cualquier otro sistema futuro.
    

---

## 3. Taxonomía editorial: de comentario a tesis

A continuación, fijamos el **mapa editorial completo**, con correspondencia directa a ToC depth.

### 3.1 Tabla canónica de alineación

|`doc_category`|Tipo editorial real|ToC|`toc-depth` recomendado|
|---|---|---|---|
|`comment`|Comentario / nota pública|❌ No|—|
|`note`|Nota de investigación|❌ No|—|
|`essay`|Ensayo largo|⚠️ Opcional|2|
|`article`|Artículo académico|⚠️ Opcional|2|
|`report`|Informe / whitepaper|✅ Sí|2–3|
|`chapter`|Capítulo de libro|✅ Sí|3|
|`thesis`|Tesis / manuscrito largo|✅ Sí|3–4*|

* `toc-depth = 4` **solo** en tesis o manuscritos de muy alta densidad técnica.

---

## 4. Qué significa esto en la práctica (sin cambiar el texto)

Con el esquema del **Paso A**, el mismo documento:

```markdown
# Bloque argumental
## Sección
### Desarrollo
#### Unidad técnica
```

puede producir:

### Exportación como **ensayo**

```bash
--toc-depth=2
```

Resultado:

```
Bloque argumental
  Sección
```

---

### Exportación como **whitepaper**

```bash
--toc-depth=3
```

Resultado:

```
Bloque argumental
  Sección
    Desarrollo
```

---

### Exportación como **tesis**

```bash
--toc-depth=4
```

Resultado:

```
Bloque argumental
  Sección
    Desarrollo
      Unidad técnica
```

👉 **El texto no cambia.**  
👉 Cambia únicamente la _proyección editorial_.

---

## 5. Regla editorial clave (muy importante)

> **La profundidad del ToC nunca debe determinar la estructura del texto.**  
> Debe ser siempre al revés.

Si al poner `toc-depth=2` “faltan cosas importantes”, el problema es:

- o un `##` mal definido,
    
- o un abuso de `###`.
    

No se soluciona aumentando `toc-depth`.

---

## 6. Integración directa con Pandoc + Lua (sin ensuciar frontmatter)

Aquí encaja perfectamente tu decisión previa de usar Lua.

### Política canónica (conceptual)

```text
if doc_category in {report, chapter, thesis}:
    enable ToC
    set toc-depth according to category
else:
    disable ToC
```

Esto se implementa:

- **fuera del documento**
    
- en un **Lua filter**
    
- o en perfiles de exportación Pandoc
    

El _frontmatter_ solo declara **qué es** el documento, no **cómo se imprime**.

---

## 7. Ejemplos completos de frontmatter por categoría

### Comentario / nota breve

```yaml
---
title: "Nota marginal sobre escalado energético"
doc_category: comment
doc_purpose: exploratory
audience: academic
lang: es
status: draft
---
```

➡️ Exportación sin ToC.

---

### Ensayo largo

```yaml
---
title: "Inteligencia, energía y límite físico"
doc_category: essay
doc_purpose: analytical
audience: academic
lang: es
status: review
---
```

➡️ ToC opcional, `toc-depth=2`.

---

### Whitepaper / informe

```yaml
---
title: "Energy Constraints in Large-Scale AI Systems"
doc_category: report
doc_purpose: evaluative
audience: professional
lang: en
status: final
---
```

➡️ ToC obligatorio, `toc-depth=3`.

---

### Tesis

```yaml
---
title: "Biofísical Constraints of Cognitive Expansion"
doc_category: thesis
doc_purpose: synthetic
audience: academic
lang: en
status: final
---
```

➡️ ToC obligatorio, `toc-depth=3` o `4` (caso justificado).

---

## 8. Qué queda cerrado tras el Paso B

Con este paso quedan **formalmente resueltos**:

- alineación estructura ↔ estándares editoriales,
    
- uso de un **único frontmatter** para todo el espectro,
    
- política clara de ToC sin contaminar el contenido,
    
- compatibilidad total con Pandoc, Word, LaTeX y futuros sistemas.
    

No hay nada “ad hoc”.  
Todo es declarativo y escalable.

---

## 9. Próximo paso natural (Paso C)

El siguiente paso lógico es:

> **Paso C — Integración con Zotero y notas académicas sin romper estructura ni ToC**

Ahí veremos:

- cómo usar notas Zotero como _pre-estructura_,
    
- cómo evitar que citas y bibliografía distorsionen el ToC,
    
- cómo mantener trazabilidad académica limpia en Obsidian.
    

Cuando quieras, avanzamos.