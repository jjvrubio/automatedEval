# Nota sobre la ventana de texto enviada al modelo

- El evaluador lee y normaliza el **TFM completo** para detectar etiquetas Finder, seleccionar la rúbrica y localizar palabras clave de metodologías (Lean, Six Sigma, TOC, GMP, FDA, TCO, BPMN, etc.). Esa búsqueda se almacena en `config["_runtime"]["cobertura_metodologias"]`.
- Al construir cada prompt se envía una **ventana acotada (~6.000 caracteres)** del TFM, formada por fragmentos que rodean las palabras clave asociadas al criterio (por ejemplo, capítulos Lean o Six Sigma cuando se evalúa `Proyecto`). Así evitamos truncar los apartados relevantes aunque estén lejos del inicio, pero seguimos dentro de los límites de tokens del modelo.
- Si un criterio no tiene coincidencias, el fallback es usar el arranque del documento, igual que antes.
- Los parámetros de recorte (`max_length` y `ventana` en `_extraer_fragmentos_relevantes`) se pueden ajustar si se dispone de mayor ventana de tokens o si se desea cubrir más contexto.
- Para pruebas donde quieras forzar el envío del TFM completo, basta con reemplazar la llamada a `_extraer_fragmentos_relevantes` por `texto_tfm[:max_length]` o eliminar el recorte dentro de `evaluar_tfm_minimal`.
