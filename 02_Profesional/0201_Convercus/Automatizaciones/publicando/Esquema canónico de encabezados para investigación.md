
# Paso A — Esquema canónico de encabezados para investigación _long-form_

## 1. Principio rector (antes de cualquier esquema)

Un texto de investigación long-form **no se organiza para el lector**, sino para:

1. **sostener inferencia acumulativa**,
    
2. **permitir navegación estructural sin pérdida semántica**,
    
3. **mantener independencia entre argumento, presentación y exportación**.
    

De ahí se deriva una regla fundamental:

> **Los encabezados son compromisos semánticos, no recursos tipográficos.**

Esto implica:

- no se usan para “respirar” el texto,
    
- no se usan para énfasis,
    
- no se usan para ordenar visualmente ideas sueltas.
    

Un encabezado declara: _“a partir de aquí, cambia el tipo de operación cognitiva”_.

---

## 2. Número óptimo de niveles (decisión explícita)

Para investigación long-form robusta, el esquema **canónico** es de **4 niveles estructurales**, con un **5º nivel excepcional**(operativo, no argumental).

|Nivel|Markdown|Rol semántico|Uso permitido|
|---|---|---|---|
|Nivel 0|_(Frontmatter)_|Identidad del documento|Título, autor, clase|
|Nivel 1|`#`|Macro-estructura|Bloques argumentales|
|Nivel 2|`##`|Estructura principal|Secciones mayores|
|Nivel 3|`###`|Desarrollo analítico|Subargumentos|
|Nivel 4|`####`|Unidades técnicas|Modelos, métodos|
|Nivel 5|`#####`|Operativo (excepcional)|Apéndices internos|

**Regla estricta**:  
Un documento bien diseñado **funciona perfectamente con ToC depth = 3**.  
El Nivel 4 existe para _trabajar_, no para _navegar_.

---

## 3. Significado preciso de cada nivel

### 3.1 Nivel 1 (`#`) — Bloques argumentales mayores

**Qué es**  
Cada encabezado de nivel 1 representa un **bloque de tesis**, no una sección editorial.

Ejemplos válidos:

- `# La inteligencia odia el desperdicio`
    
- `# Mayor capacidad exige mayor energía`
    
- `# La industria como vértice sistémico`
    

Ejemplos inválidos:

- `# Introducción`
    
- `# Marco teórico`
    
- `# Resultados`
    

> Nota importante:  
> “Introducción”, “Conclusión”, etc. **no son bloques argumentales**; son funciones editoriales. Pueden existir, pero no deben dominar el nivel 1 en textos de pensamiento original.

**Regla**  
Un documento long-form serio rara vez tiene más de **3–6 encabezados de nivel 1**.

---

### 3.2 Nivel 2 (`##`) — Secciones estructurales del bloque

**Qué es**  
Descompone el bloque argumental en **vectores conceptuales coherentes**.

Ejemplo:

```markdown
# Mayor capacidad exige mayor energía

## Exergía y límites biofísicos
## Escalado computacional y consumo marginal
## Distribución energética y fricción sistémica
```

Aquí cada `##`:

- podría ser un paper por sí mismo,
    
- tiene autonomía conceptual,
    
- mantiene coherencia con el bloque padre.
    

**Regla**

- No más de **5–7 secciones** por bloque.
    
- Todas deben estar en el **mismo plano lógico** (paralelismo semántico).
    

---

### 3.3 Nivel 3 (`###`) — Desarrollo analítico

**Qué es**  
Es el nivel donde ocurre el **trabajo cognitivo principal**:

- derivaciones,
    
- comparaciones,
    
- inferencias,
    
- encadenamientos empíricos.
    

Ejemplo:

```markdown
## Escalado computacional y consumo marginal

### Leyes de escalado en modelos de lenguaje
### Coste energético por parámetro entrenado
### Rendimientos decrecientes y saturación
```

Este nivel:

- **sí** debe aparecer en el ToC de documentos largos,
    
- **no** debe fragmentarse en exceso.
    

**Regla**  
Si necesitas más de 4–5 `###` dentro de un mismo `##`, probablemente el `##` está mal definido.

---

### 3.4 Nivel 4 (`####`) — Unidades técnicas o metodológicas

**Qué es**  
Es el nivel de **precisión**, no de navegación:

- modelos matemáticos,
    
- supuestos,
    
- definiciones técnicas,
    
- metodología concreta,
    
- notas de implementación.
    

Ejemplo:

```markdown
### Coste energético por parámetro entrenado

#### Definición de parámetro efectivo
#### Hipótesis de consumo marginal
```

**Regla crítica**  
Este nivel **no debe aparecer en el ToC estándar**.  
Si aparece, el ToC se convierte en ruido.

---

### 3.5 Nivel 5 (`#####`) — Uso excepcional

Solo se admite para:

- apéndices internos,
    
- notas metodológicas extensas,
    
- listados operativos.
    

Si necesitas este nivel con frecuencia, el documento está **mal segmentado**.

---

## 4. Separación clave: estructura vs función editorial

Un error muy común es confundir **estructura del pensamiento** con **funciones editoriales**.

### Funciones editoriales legítimas

- Introducción
    
- Conclusión
    
- Notas metodológicas
    
- Referencias
    
- Apéndices
    

### Regla canónica

Estas funciones **no deben competir** con los bloques argumentales.

Dos estrategias válidas:

#### Estrategia A — Funciones como nivel 1 secundario

```markdown
# Introducción
# Bloque argumental 1
# Bloque argumental 2
# Conclusión
```

#### Estrategia B — Funciones fuera del eje argumental (preferida)

- Introducción breve sin `#`
    
- Conclusión como último bloque, pero semántico
    
- Referencias sin encabezado jerárquico (`## References` fuera del ToC)
    

Lo importante no es la forma, sino que el ToC refleje **el argumento**, no la logística editorial.

---

## 5. Reglas de oro (no negociables)

1. **No se salta ningún nivel**  
    Nunca `##` → `####`.
    
2. **Un encabezado = una promesa semántica**  
    Si el texto no cumple esa promesa, el encabezado sobra.
    
3. **El ToC es una proyección, no un diseño**  
    No se escribe pensando “qué quedará bonito en el ToC”.
    
4. **Si el ToC se vuelve ilegible, el problema es estructural**  
    No se arregla con `toc-depth`, sino replanteando encabezados.
    

---

## 6. Ejemplo completo (canónico)

```markdown
---
title: "Mayor capacidad exige mayor energía"
doc_class: report
lang: es
---

# Mayor capacidad exige mayor energía

## Exergía y límites biofísicos

### Energía útil frente a energía total
### Restricciones termodinámicas

## Escalado computacional y consumo marginal

### Leyes de escalado en modelos de lenguaje
#### Definición de parámetro efectivo
#### Hipótesis de consumo marginal

### Saturación y rendimientos decrecientes

## Distribución energética y fricción sistémica

### Infraestructura, latencia y centralización
### Coste social del consumo concentrado

# Conclusión: implicaciones industriales
```

Con este esquema:

- `toc-depth = 2` → visión ejecutiva
    
- `toc-depth = 3` → navegación académica completa
    
- `toc-depth = 4` → **desaconsejado**
    

---

## 7. Qué hemos fijado (importante)

Con este paso A hemos fijado:

- número de niveles,
    
- significado exacto de cada nivel,
    
- reglas de uso,
    
- separación entre argumento y editorial,
    
- compatibilidad directa con Pandoc, Word, LaTeX y Zotero.
    

Nada de esto depende de plugins.

---

## 8. Próximo paso lógico (Paso B)

Una vez aceptado este esquema, el siguiente paso natural es:

> **Paso B — [[Alineación del ToC con estándares editoriales|Alineación TOC]] Alinear profundidad del ToC (`toc-depth`) con estándares editoriales concretos**

Ahí traduciremos esta estructura a:

- artículos académicos,
    
- whitepapers,
    
- capítulos de libro,
    
- tesis,
    

sin cambiar **ni una línea** del contenido.

Si estás de acuerdo con este esquema (o quieres ajustarlo mínimamente), pasamos directamente al **Paso B**.