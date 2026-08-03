---
titulo: TES_Protocolo_Validacion
aliases:
  - Protocolo de validación del TES
  - Validación metodológica TES
idioma: es
fecha: 2026-04-16
version: v2.1
estado: activo
estado_edicion: revisado
tipo: protocolo_de_validacion_metodologica
capa: nucleo_irreducible
alcance: verificacion_de_reconstruibilidad_coherencia_de_capas_integridad_de_activos_y_cierre_de_dictamen
funcion: verificar la consistencia metodológica de piezas, experiencias, activos y configuraciones derivadas del TES sin sustituir la ontología ni la arquitectura operativa del sistema
canonico: false
rige:
  - verificacion_de_reconstruibilidad
  - verificacion_de_coherencia_de_capas
  - verificacion_de_integridad_de_activos
  - clasificacion_de_hallazgos
  - emision_de_dictamen_metodologico
  - cierre_de_validacion_y_registro
  - compatibilidad_con_leeme_y_gobernanza
  - control_de_deriva_en_piezas_derivadas
  - condiciones_de_no_conformidad
  - relacion_entre_validacion_y_aprendizaje
  - umbrales_minimos_de_suficiencia
  - articulacion_con_guia_y_politica
  - uso_de_evidencias
  - lectura_de_casos_y_materiales
  - distincion_entre_fallo_mayor_y_ajuste_menor
  - no_sustitucion_de_ontologia
  - no_sustitucion_de_realizacion
  - no_sustitucion_de_medicion
  - criterios_de_rechazo
  - criterios_de_reapertura
  - condicion_de_cierre_documental
  - compatibilidad_con_registro_validacion
  - exigencia_de_trazabilidad
  - uso_no_retorico_de_resultados
  - preservacion_de_la_arquitectura_profunda
  - validacion_de_superficie_subordinada
  - verificacion_de_relacion_entre_pieza_y_sistema
  - control_de_deriva_por_omision
  - control_de_deriva_por_exceso
  - lectura_integrada_de_nucleo
  - salida_operativa_de_revision
  - criterios_de_priorizacion_de_correcciones
  - condicion_de_reutilizacion
  - suficiencia_para_escalado
  - suficiencia_para_aprendizaje
  - explicacion_del_fallo
  - proteccion_de_nucleo_irreducible
  - relacion_con_registro_de_validacion
  - validacion_de_piezas_visuales_y_textuales
  - validacion_de_configuraciones_intermodales
  - validacion_de_herramientas_operativas
  - verificacion_de_externalizacion_correcta
  - verificacion_de_integracion_de_nodos
  - verificacion_de_dependencias
  - verificacion_de_nomenclatura_funcional
  - verificacion_de_estado_operativo_comprimido
  - compatibilidad_con_leeme_refactorizado
  - criterio_de_no_soberania_de_metadata
  - control_de_duplicacion_y_ambiguedad
  - exigencia_de_congruencia_sistemica
  - cierre_reproducible
  - validacion_no_arbitraria
  - minima_carga_de_evidencia
  - relacion_con_ledger
  - relacion_con_telar_editorial
  - relacion_con_omnimentalidad
  - relacion_con_ontologia
  - relacion_con_politica_de_realizacion
  - relacion_con_guia_de_produccion_visual
  - relacion_con_lexico
  - obligacion_de_remision_al_nodo_superior
  - criterio_de_revision_iterativa
  - apertura_de_hallazgos_pendientes
  - clausura_de_hallazgos_resueltos
dominio_precedencia: verificacion_metodologica_y_emision_de_dictamen_sobre_materiales_del_tes
depende_de:
  - LEEME
  - TES_Ontologia_Accion_Situada
  - TES_Telar_Omnimentalidad
  - TES_Experience_Ledger
  - TES_Telar_Editorial_Situado
  - TES_Politica_Realizacion_Editorial
  - TES_Lexico
  - TES_Gobernanza_Documental
documentos_relacionados:
  - TES_Guia_Produccion_Visual
  - léeme_registro_validación
  - léeme_herramientas
tags:
  - TES
  - validacion
  - protocolo
  - nucleo-irreducible
  - coherencia
  - reconstruibilidad
---

# TES_Protocolo_Validacion

## Naturaleza de esta pieza

`TES_Protocolo_Validacion` regula la verificación metodológica del TES.

No redefine la ontología. No sustituye al [[TES_Experience_Ledger]]. No reemplaza al [[TES_Telar_Editorial_Situado]], a la política de realización ni a la guía de producción visual. Su función es otra: determinar si una pieza, una experiencia, un activo o una configuración derivada **conservan suficiente coherencia con el sistema** como para considerarse compatibles, corregibles o no conformes.

En el TES, validar no significa “opinar sobre calidad general”. Significa comprobar, con criterios explícitos, si algo sigue siendo reconstruible dentro de la arquitectura del sistema.

## Principio rector

> El protocolo no valida impresiones.
>
> Valida reconstruibilidad, coherencia de capas e integridad de activos.

Toda validación debe terminar en un dictamen justificable, no en una impresión dispersa.

## Problema que resuelve

Sin protocolo de validación, el TES queda expuesto a cinco derivas principales:

1. aceptar piezas formalmente atractivas pero estructuralmente lesionadas;
2. tratar como equivalentes fallos menores y fallos arquitectónicos;
3. declarar resultados sin comprobar su cadena reconstructiva;
4. introducir correcciones sin priorización ni criterio común;
5. y acumular materiales derivados sin saber si siguen perteneciendo al sistema.

El protocolo existe para impedir esos desplazamientos.

## Relación con el núcleo irreducible

- [[TES_Ontologia_Accion_Situada]] fija el plano conceptual primario.
- [[TES_Telar_Omnimentalidad]] permite leer ese plano en clave estratégica.
- [[TES_Experience_Ledger]] fija la cadena operativa experiencial.
- [[TES_Telar_Editorial_Situado]] traduce ontología y ledger a composición.
- [[TES_Politica_Realizacion_Editorial]] regula la superficie de la pieza.
- [[TES_Guia_Produccion_Visual]] regula la traducción a activos e instrucción.
- [[TES_Lexico]] protege la precisión verbal de la acción.
- [[TES_Gobernanza_Documental]] determina el estrato y la posición del material evaluado.

El protocolo no absorbe ninguno de esos dominios. Los articula en el momento del dictamen.

## Qué define

Este documento define:

- los criterios mínimos de validación;
- el orden de lectura validativa;
- los tipos de hallazgo;
- los niveles de dictamen;
- el modo de cierre de una validación;
- y la relación entre hallazgo, corrección y reapertura.

## Qué no define

Este documento no define:

- conceptos primarios del TES;
- reglas completas de composición;
- formas de superficie;
- fórmulas de medición analítica;
- ni plantillas de producción derivada por sí solo.

## Objeto de validación

Pueden someterse a validación metodológica, entre otros:

- documentos del núcleo y sus reescrituras;
- piezas editoriales derivadas;
- secuencias o experiencias reconstruidas;
- guías, matrices o instrucciones;
- activos visuales y configuraciones intermodales;
- registros de evidencia;
- y reorganizaciones documentales del sistema.

## Criterios obligatorios de validación

### 1. Reconstruibilidad

La pieza debe permitir reconstruir su cadena estructural mínima.

Según el tipo de material, esa reconstrucción deberá alcanzar lo que corresponda de:

- campo o ecosistema;
- evento;
- patrón;
- secuencia;
- progresión;
- resultado;
- medición;
- aprendizaje;
- o composición equivalente dentro del telar editorial.

La reconstruibilidad es el primer filtro. Si falla por completo, el material no puede considerarse conforme.

### 2. Coherencia de capas

Las capas del sistema no deben invadirse entre sí.

La validación debe comprobar, al menos:

- que la ontología no haya sido redefinida por una pieza derivada;
- que la superficie no haya sustituido a la arquitectura profunda;
- que la medición no se use como sustituto de la validación;
- que la guía visual no actúe como doctrina;
- y que las herramientas operativas no reclamen soberanía de núcleo.

### 3. Integridad de activos

Cuando existan activos, escenas, tablas, diagramas, piezas visuales o instrucciones, la validación debe comprobar que:

- están clasificados de forma reconocible;
- conservan relación con la secuencia o con el resultado que dicen representar;
- no mezclan ecosistema con secuencia;
- y no lesionan el criterio de reconstrucción.

## Criterios complementarios

Además de los tres criterios obligatorios, la validación puede verificar:

- precisión verbal cuando la acción esté en juego;
- consistencia terminológica con el léxico nuclear;
- posición documental correcta según `LEEME` y gobernanza;
- suficiencia de soporte métrico cuando se invoque resultado, impacto o aprendizaje;
- y compatibilidad de una pieza con la función que declara cumplir.

## Secuencia de lectura validativa

## Verificación de entregabilidad

Cuando el objeto validado tenga forma de archivo, artefacto visual, diagrama, infografía, presentación, SVG, PDF, imagen, plantilla o configuración intermodal exportable, la validación deberá comprobar su entregabilidad material.

La verificación de entregabilidad consiste en determinar si el soporte final conserva la reconstruibilidad, la coherencia de capas y la integridad de activos que el material declaraba tener.

No sustituye los criterios obligatorios de validación. Los aterriza en una pregunta material:

```text
¿El archivo final permite leer, inspeccionar y usar aquello que metodológicamente decía organizar?
```

La verificación de entregabilidad deberá comprobar, como mínimo:

1. formato final comprometido;
    
2. apertura correcta del archivo;
    
3. existencia de render, exportación o previsualización revisada;
    
4. legibilidad textual;
    
5. ausencia de solapes;
    
6. ausencia de desbordamientos;
    
7. proporcionalidad caja/texto;
    
8. correspondencia entre jerarquía semántica y composición visual;
    
9. ubicación correcta de pies, créditos, fuentes y referencias;
    
10. correspondencia entre versión revisada y versión entregada;
    
11. editabilidad suficiente cuando el formato lo requiera;
    
12. y registro explícito de deuda si queda algún límite material pendiente.
    

Un material puede ser metodológicamente reconstruible y, sin embargo, no entregable si su archivo final impide o degrada la lectura de la estructura que declara representar.

La falta de entregabilidad deberá clasificarse como:

- hallazgo menor, cuando el defecto material no impide reconstrucción ni uso razonable;
    
- hallazgo mayor, cuando la lesión material compromete legibilidad, integridad de activos o uso del archivo;
    
- hallazgo crítico, cuando el archivo entregado impide por completo la reconstrucción, contradice el formato comprometido o no corresponde a la versión validada.

Toda validación debe seguir, como mínimo, este orden:
### Paso 1. Identificación del objeto

Determinar:

- qué tipo de material se valida;
- a qué estrato pertenece;
- qué función declara;
- y qué nodo superior rige su dominio.

### Paso 2. Reconstrucción mínima

Intentar reconstruir la cadena que el material presupone.

Si la reconstrucción básica fracasa, el hallazgo es mayor.

### Paso 3. Verificación de capas

Comprobar si el material respeta la distribución funcional del sistema.

### Paso 4. Verificación de activos o soportes

Cuando existan activos o traducción visual, comprobar clasificación, integridad y relación con la secuencia.

### Paso 5. Verificación de superficie

Si el material tiene superficie discursiva o visual, comprobar si sigue subordinada a la arquitectura profunda.

### Paso 6. Verificación de evidencia

Si el material invoca resultado, progreso, eficacia o aprendizaje, comprobar qué evidencia presenta y si su uso es compatible con el sistema.

### Paso 7. Emisión de dictamen

Cerrar la validación con uno de los dictámenes previstos y con acciones requeridas.

## Tipos de hallazgo

### Hallazgo menor

No compromete la pertenencia metodológica del material al TES.

Ejemplos:

- desajuste de nombre;
- omisión de remisión documental;
- formulación verbal mejorable;
- clasificación incompleta de un activo sin lesión estructural.

### Hallazgo mayor

Compromete reconstruibilidad, coherencia de capas o integridad de activos.

Ejemplos:

- confusión entre ecosistema y secuencia;
- sustitución de resultado por promesa;
- ausencia total de validación en una pieza que reclama efecto;
- uso soberano de una herramienta operativa;
- superficie que colapsa la arquitectura profunda.

### Hallazgo crítico

Rompe la compatibilidad del material con el sistema en su estado actual.

Ejemplos:

- redefinición implícita de la ontología desde una pieza derivada;
- desaparición de la cadena experiencial;
- contradicción frontal con el mapa operativo del `LEEME`;
- o lesión estructural de activos que impide toda reconstrucción.

## Dictámenes posibles

### 1. Conforme

La pieza es compatible con el TES y no requiere corrección metodológica sustantiva.

### 2. Conforme con ajuste menor

La pieza es compatible, pero necesita correcciones acotadas para mejorar precisión, remisión o clasificación.

### 3. No conforme con ajuste mayor

La pieza no puede considerarse metodológicamente suficiente en su estado actual, pero puede reingresar tras corrección estructural.

### 4. No válida

La pieza no es compatible con el TES en su estado actual y no debe seguir operando como material vigente.

## Regla de justificación del dictamen

Todo dictamen debe responder, de forma explícita, a estas cuatro preguntas:

1. ¿Qué se ha validado?
2. ¿Contra qué nodos se ha validado?
3. ¿Qué hallazgos se han detectado?
4. ¿Qué acción se exige para cerrar la revisión?

Sin esas cuatro respuestas, la validación queda incompleta.

## Regla de evidencia mínima

Para que una validación sea metodológicamente suficiente, debe apoyarse al menos en:

- el material examinado;
- el nodo o nodos de precedencia pertinentes;
- una reconstrucción mínima de cadena o función;
- y una justificación del hallazgo.

La validación no exige siempre una prueba cuantitativa. Pero sí exige **evidencia suficiente para no decidir arbitrariamente**.

## Relación con `registro_validacion/`

El protocolo emite dictamen.

El directorio `registro_validacion/` conserva:

- evidencia empírica;
- decisiones tomadas;
- reaperturas;
- y aprendizaje derivado.

No deben confundirse ambos planos.

## Relación con herramientas operativas

Las herramientas operativas pueden instanciar el sistema, pero nunca validarse a sí mismas como si fueran fuente soberana.

Toda matriz, instrucción o plantilla debe remitirse hacia arriba cuando se revise su consistencia.

## Umbrales de no conformidad automática

Debe declararse al menos **no conforme con ajuste mayor** cuando ocurra cualquiera de estas condiciones:

1. no pueda reconstruirse una secuencia mínima allí donde sea necesaria;
2. se confunda ecosistema con secuencia;
3. se invoque resultado sin mostrar qué lo produce;
4. se use una cifra como sustituto de validación;
5. la superficie se comporte como criterio soberano;
6. un activo no esté clasificado y no pueda relacionarse con la pieza que dice servir;
7. o una pieza derivada reclame autoridad de núcleo.

Debe declararse **no válida** cuando además exista contradicción frontal con el núcleo irreducible o con el mapa operativo vigente.

## Criterio de reapertura

Una validación puede reabrirse cuando:

- cambie materialmente el documento o activo validado;
- aparezca evidencia nueva suficiente;
- se reubique el documento en otro estrato;
- o se detecte que el dictamen anterior se basó en un nodo de referencia incorrecto.

## Criterio de cierre

La validación se considera bien cerrada cuando produce simultáneamente:

- un dictamen;
- una explicación del hallazgo;
- una acción requerida;
- y una decisión sobre vigencia, corrección o externalización.

## Nota final

El protocolo de validación no existe para endurecer burocráticamente el TES.

Existe para impedir que el sistema acepte como compatibles materiales que ya no puede reconstruir.
