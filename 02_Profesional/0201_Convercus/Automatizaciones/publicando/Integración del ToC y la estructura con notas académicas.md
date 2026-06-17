# Paso C — Integración del ToC y la estructura con notas académicas basadas en Zotero

_(sin contaminar el texto ni romper la arquitectura)_

---

## 1. El problema de fondo (bien formulado)

Cuando se trabaja con Zotero + Obsidian, aparecen **tres tensiones clásicas**:

1. Las **notas de lectura** (Zotero) no tienen estructura editorial.
    
2. El **texto final** sí la necesita (encabezados, ToC, bloques).
    
3. El **ToC** no debe verse afectado por:
    
    - citas,
        
    - bibliografía,
        
    - comentarios marginales,
        
    - notas metodológicas internas.
        

La mayoría de flujos fallan porque **mezclan estos planos**.

Tu pipeline, tal como lo has diseñado, permite resolver esto limpiamente si aceptamos una premisa clave:

> **Zotero no alimenta el ToC.  
> Alimenta el argumento.**

---

## 2. Separación estricta de tipos de notas (regla estructural)

Para que Zotero y el ToC convivan sin fricción, hay que fijar **tres tipos de notas**, con roles no solapables.

### 2.1 Nota Zotero (fuente)

**Función**: registrar una obra, no producir texto final.

Características:

- una por referencia bibliográfica,
    
- ligada a un `citekey`,
    
- contiene:
    
    - resumen,
        
    - citas textuales,
        
    - ideas clave,
        
    - comentarios propios.
        

Ejemplo (esquemático):

```markdown
---
zotero_key: Smith2023Energy
note_type: source
---

## Thesis
## Key arguments
## Relevant quotes
## My commentary
```

⚠️ Importante:  
Estos `##` **no son estructurales** para el documento final.  
Son **organizadores internos** de la nota.

---

### 2.2 Nota conceptual (puente)

**Función**: abstraer ideas **fuera de una obra concreta**.

Aquí ocurre el verdadero trabajo intelectual.

Ejemplo:

```markdown
---
note_type: concept
related_sources:
  - Smith2023Energy
  - Zhao2022Scaling
---

## Exergía como límite cognitivo
Texto propio, síntesis, comparación entre fuentes.
```

Estas notas:

- **no llevan ToC**,
    
- **no se exportan**,
    
- **no contienen encabezados de nivel 1 (`#`)**.
    

Son _material de cantera_.

---

### 2.3 Documento long-form (producto)

**Función**: articular argumento completo y exportable.

Aquí sí aplican **Paso A y B**:

- encabezados canónicos,
    
- frontmatter semántico,
    
- ToC proyectado solo en exportación.
    

Ejemplo:

```markdown
---
title: "Mayor capacidad exige mayor energía"
doc_category: report
---

# Mayor capacidad exige mayor energía

## Exergía y límites biofísicos
Texto propio con citas.
```

---

## 3. Regla crítica para que Zotero no “rompa” el ToC

> **Nada que no sea parte del argumento debe usar encabezados estructurales.**

Esto implica:

### ❌ No hacer esto en el documento final

```markdown
## Referencias
```

(si ese `##` entra en el ToC y no lo deseas)

### ✅ Hacer esto en su lugar

**Opción A — encabezado no estructural**

```markdown
<hr />

**Referencias**
```

**Opción B — encabezado de nivel fuera de ToC (controlado por export)**

```markdown
#### Referencias
```

(si tu `toc-depth` es 2 o 3)

**Opción C — bibliografía gestionada solo por Pandoc**

```bash
--citeproc
--bibliography=refs.bib
```

En este caso, **no hay encabezado en el Markdown**: Pandoc se encarga.

👉 Esta última es la más limpia si usas Zotero de forma sistemática.

---

## 4. Cómo entran las citas Zotero en el texto (sin ruido estructural)

En el documento final, las citas:

- **no crean estructura**,
    
- **no afectan al ToC**,
    
- viven dentro de párrafos, listas o notas.
    

Ejemplo canónico:

```markdown
La expansión de capacidad computacional muestra rendimientos decrecientes claros
cuando se introduce el coste exergético marginal [@Smith2023Energy; @Zhao2022Scaling].
```

Pandoc + `citeproc`:

- resuelve citas,
    
- genera bibliografía,
    
- sin tocar encabezados.
    

El ToC queda **intacto**.

---

## 5. Uso estratégico de Lua en el Paso C (sin “programar de verdad”)

Aquí viene la parte tranquilizadora:  
**no necesitas “saber Lua” en general**, solo entender **patrones muy concretos**.

En el Paso C, Lua se usa para **tres cosas típicas**:

### 5.1 Excluir bloques del ToC por semántica

Ejemplo conceptual:

```text
Si un bloque tiene note_type != product → no exportar
```

Esto permite:

- mantener comentarios internos,
    
- notas metodológicas,
    
- secciones auxiliares,
    

dentro del mismo archivo **si lo deseas**, sin que entren en el ToC ni en el export.

---

### 5.2 Controlar encabezados “no estructurales”

Puedes marcar secciones así:

```markdown
#### [meta] Notas metodológicas
```

Y usar Lua para:

- excluir cualquier encabezado que empiece por `[meta]`,
    
- o que tenga una clase específica.
    

Esto es muchísimo más limpio que “inventar niveles”.

---

### 5.3 Ajustar comportamiento por `doc_category`

Ejemplo lógico:

```text
if doc_category == thesis:
    include appendices
else:
    drop appendices
```

Sin duplicar documentos.

---

## 6. Qué ganas cognitivamente (lo que ya has intuido)

Tu intuición es correcta: este enfoque **reduce carga cognitiva** porque:

- ya no decides “qué nivel pongo” pensando en el ToC,
    
- escribes **solo** pensando en el argumento,
    
- el ToC se convierte en una _vista_, no en una restricción,
    
- Zotero deja de “ensuciar” la estructura mental del texto.
    

Dicho de forma fuerte (pero cierta):

> Has pasado de _escribir para publicar_  
> a _escribir para pensar_,  
> y **publicar como una proyección automática**.

Eso es exactamente el punto de madurez del sistema.

---

## 7. Qué queda cerrado tras el Paso C

A estas alturas ya tienes:

- un esquema canónico de encabezados (Paso A),
    
- una política editorial clara de ToC (Paso B),
    
- una integración limpia con Zotero y notas académicas (Paso C),
    
- un pipeline Pandoc + Lua coherente y extensible.
    

No hay dependencias frágiles.  
No hay decisiones escondidas en el texto.  
No hay plugins “mágicos”.

---

## 8. Siguientes posibles pasos (elige solo si quieres)

A partir de aquí, las extensiones naturales serían:

```ad-todo
title: Más adelante
collapse: open

- **Paso D** — numeración automática de secciones _solo_ en ciertos exports
    
- **Paso E** — apéndices, figuras y tablas sin contaminar el ToC
    
- **Paso F** — conversión a formatos editoriales concretos (journal X, libro Y)
    
- **Paso G** — automatización por lotes (exportar toda una colección Obsidian)
    
```


Pero nada de eso es necesario para que el sistema ya funcione muy bien.

Si quieres, en el siguiente mensaje puedo proponerte:

- un **mapa mental resumido** del sistema completo,
    
- o un **primer filtro Lua mínimo** comentado línea a línea (didáctico, sin intimidar).
    

Tú decides el ritmo.