---
titulo: TES — Sistema refactorizado (estado operativo)
idioma: es
fecha: '2026-04-21'
version: v2.2
estado: activo
estado_edicion: actualizado
tipo: mapa_de_estado_operativo
capa: gobernanza_y_estabilizacion
alcance: nucleo_irreducible_externalizacion_funcional_y_compresion_del_sistema
funcion: fijar el mapa vigente del TES tras refactorización, declarar su núcleo irreducible y externalizar herramientas, registro de validación y medición
canonico: false
rige:
  - mapa_operativo_vigente
  - compresion_estructural
  - externalizacion_funcional
  - unificacion_lexica
  - reubicacion_de_medicion
dominio_precedencia: mapa_de_estado_operativo_y_compresion_del_sistema
depende_de:
  - TES_Ontologia_Accion_Situada
  - TES_Telar_Omnimentalidad
  - TES_Experience_Ledger
  - TES_Telar_Editorial_Situado
  - TES_Politica_Realizacion_Editorial
  - TES_Guia_Produccion_Visual
  - TES_Protocolo_Validacion
  - TES_Gobernanza_Documental
  - TES_Lexico
documentos_relacionados:
  - TES_Constituyente
  - TES_KPI_Dictionary
  - TES_KPI_Sectores
  - TES_Ecosistema_Sujetos_Participantes
  - TES_Anexo_Inventario_Figuras_Subjetivas
  - léeme_herramientas
  - léeme_registro_validación
  - léeme_medición
tags:
  - TES
  - estado-operativo
  - refactorizacion
  - nucleo
  - medicion
  - lexico
---

# TES — Sistema refactorizado (estado operativo)

## Enlaces Obsidian

### Núcleo irreducible
- [[TES_Ontologia_Accion_Situada]]
- [[TES_Telar_Omnimentalidad]]
- [[TES_Experience_Ledger]]
- [[TES_Telar_Editorial_Situado]]
- [[TES_Politica_Realizacion_Editorial]]
- [[TES_Guia_Produccion_Visual]]
- [[TES_Protocolo_Validacion]]
- [[TES_Gobernanza_Documental]]
- [[TES_Lexico]]

### Zonas externalizadas
- [[herramientas_operativas/léeme_herramientas|herramientas_operativas]]
- [[registro_validacion/léeme_registro_validación|registro_validacion]]
- [[medicion/léeme_medición|medicion]]
- [[medicion/TES_KPI_Dictionary]]
- [[medicion/TES_KPI_Sectores]]

### Desarrollos subordinados compatibles
- [[TES_Ecosistema_Sujetos_Participantes]]
- [[TES_Anexo_Inventario_Figuras_Subjetivas]]

## Naturaleza de esta pieza

Este documento fija el **mapa vigente del TES** tras la refactorización del sistema.

Su función no es redefinir la ontología primaria ni sustituir la gobernanza documental detallada. Su tarea es más concreta: declarar con claridad qué piezas forman hoy el **núcleo irreducible**, qué funciones han sido externalizadas y qué integraciones deben considerarse cerradas en el régimen operativo actual.

## 1. Núcleo irreducible del sistema

El núcleo irreducible vigente del TES queda compuesto por estas piezas:

- `TES_Ontologia_Accion_Situada.md`
- `TES_Telar_Omnimentalidad.md`
- `TES_Experience_Ledger.md`
- `TES_Telar_Editorial_Situado.md`
- `TES_Politica_Realizacion_Editorial.md`
- `TES_Guia_Produccion_Visual.md`
- `TES_Protocolo_Validacion.md`
- `TES_Gobernanza_Documental.md`
- `TES_Lexico.md`

### Lectura funcional del núcleo

- **Ontología** → `TES_Ontologia_Accion_Situada` + `TES_Telar_Omnimentalidad`
- **Operación** → `TES_Experience_Ledger`
- **Método** → `TES_Telar_Editorial_Situado` + `TES_Politica_Realizacion_Editorial`
- **Ejecución** → `TES_Guia_Produccion_Visual`
- **Control** → `TES_Protocolo_Validacion`
- **Gobernanza** → `TES_Gobernanza_Documental`
- **Lenguaje** → `TES_Lexico`

## 2. Fuera del núcleo: externalización funcional

### 2.1. Herramientas operativas

Ruta:

`/herramientas_operativas/`

Documento visible de clasificación:

`léeme_herramientas.md`

Subespacios admitidos:

- `instrucciones/`
- `matrices/`
- `plantillas/`

Función:

instanciar el sistema en casos de uso concretos sin ganar soberanía definicional.

### 2.2. Registro de validación

Ruta:

`/registro_validacion/`

Documento visible de clasificación:

`léeme_registro_validación.md`

Función:

evidencia empírica, dictámenes, observaciones y aprendizaje reutilizable.

### 2.3. Medición

Ruta:

`/medicion/`

Documento visible de clasificación:

`léeme_medición.md`

Piezas visibles de este espacio:

- `TES_KPI_Dictionary`
- `TES_KPI_Sectores`

Función:

desarrollar la capa analítica del sistema, incluyendo diccionarios KPI, módulos sectoriales, bibliotecas de métricas y especializaciones de contraste cuantitativo.

Relación interna de la medición externalizada:

- `TES_KPI_Dictionary` fija la gramática KPI, la trazabilidad mínima y la matriz de definición de la capa analítica.
- `TES_KPI_Sectores` desarrolla la especialización sectorial compatible con esa gramática y concentra los despliegues verticales vigentes.

La medición no desaparece del TES. Se **externaliza funcionalmente** para evitar que la extensión analítica vuelva a ocupar el centro irreducible del sistema.

## 2.4. Desarrollos subordinados compatibles

Además del núcleo irreducible y de las zonas externalizadas, el TES puede admitir **desarrollos subordinados compatibles** cuando no redefinen la ontología primaria, no duplican funciones nucleares ya absorbidas y no alteran la precedencia funcional del sistema comprimido.

En el estado actual se reconocen dos piezas de este tipo:

- `TES_Ecosistema_Sujetos_Participantes`, como formulación canónica de integración específica del ecosistema de sujetos;
- `TES_Anexo_Inventario_Figuras_Subjetivas`, como anexo tipológico no normativo y repertorio de instanciación.

Estas piezas no forman parte del núcleo irreducible, pero tampoco deben tratarse como residuos del régimen expandido ni como herramientas externas indiferenciadas. Su estatuto es **subordinado, compatible y no invasivo**.

## 3. Integraciones declaradas como realizadas

A partir de este estado operativo, deben considerarse integradas las siguientes funciones previamente dispersas:

- **Bloqueo** → integrado en `TES_Guia_Produccion_Visual`
- **Vertebración** → integrada en `TES_Guia_Produccion_Visual`
- **Resolución** → integrada en `TES_Politica_Realizacion_Editorial`
- **Lenguaje nuclear** → concentrado funcionalmente en `TES_Lexico`
- **Gobernanza** → unificada en `TES_Gobernanza_Documental`

## 4. Estatuto de piezas desplazadas

### 4.1. TES_Constituyente

`TES_Constituyente` conserva estatuto de referencia constituyente o fundacional del sistema, pero **no forma parte del núcleo irreducible operativo**.

Su función es de marco constituyente y trazabilidad alta, no de pieza central de uso diario en el régimen comprimido.

### 4.2. TES_Glosario

`TES_Glosario` deja de operar como nodo nuclear autónomo.

Su contenido útil queda absorbido funcionalmente por `TES_Lexico` o, cuando convenga conservarlo, por archivo auxiliar o trazabilidad terminológica.

### 4.3. TES_KPI_Dictionary

`TES_KPI_Dictionary` deja de figurar en el núcleo irreducible y pasa a la ruta `/medicion/` como pieza matriz de extensión analítica y de definición KPI.

### 4.4. TES_KPI_Sectores

`TES_KPI_Sectores` vive en `/medicion/` como despliegue sectorial de la capa analítica del TES.

Su función es desarrollar la diferenciación por sectores sin reclamar soberanía sobre el núcleo irreducible ni duplicar la precedencia funcional de `TES_KPI_Dictionary`. Cuando exista duda entre ambos nodos, `TES_KPI_Dictionary` rige la definición matriz y `TES_KPI_Sectores` rige la especialización sectorial compatible con esa matriz.

## 5. Nomenclatura adoptada

Se fijan como nombres de los espacios externos:

- `herramientas_operativas`
- `registro_validacion`
- `medicion`

Y como documentos visibles de clasificación de dichos espacios:

- `léeme_herramientas`
- `léeme_registro_validación`
- `léeme_medición`

Regla:

los nombres deben expresar **función** y no metáfora, estilo o jerga circunstancial.

## 6. Propiedades estructurales del sistema comprimido

El estado operativo comprimido del TES se rige por estas propiedades:

- **un concepto → un nodo**
- **una función → un documento**
- **sin duplicación innecesaria**
- **sin nodos fantasma**
- **sin ambigüedad de estatuto**

## 7. Principio rector

> La superficie puede variar; la arquitectura profunda no.

## 8. Criterio de uso

Este documento debe utilizarse:

- para leer el estado actual del sistema;
- para decidir qué pertenece al núcleo y qué no;
- para impedir reexpansiones no justificadas;
- y para orientar la limpieza de dependencias, frontmatter y mapas documentales.

No debe utilizarse:

- para reabrir discusiones ya absorbidas por integración;
- para devolver al núcleo herramientas o extensiones que ya fueron externalizadas;
- ni para justificar duplicaciones léxicas o métricas en nombre de la completitud.

## 9. Estado

El TES se declara en **estado operativo comprimido**.

La tarea pendiente no es expandirlo de nuevo, sino mantener la compresión sin pérdida de inteligibilidad ni de capacidad de uso.
