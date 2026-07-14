# Actualizar temas DOCX en lote (Word VBA)

Este flujo no usa Aspose ni Xcode.
Tampoco usa componentes ActiveX/COM (evita el error 429 en Word para Mac).

## 1) Importar la macro en Word

1. Abre Microsoft Word.
2. Ve a `Herramientas > Macro > Editor de Visual Basic`.
3. En el proyecto `Normal`, importa el archivo:
   - `scripts de apoyo/actualizar_temas_word_vba.bas`

## 2) Ejecutar

1. En Word, ve a `Herramientas > Macro > Macros...`.
2. Abre primero cualquier archivo de la carpeta `TEMAS` (por ejemplo `TEMA 1.docx`).
3. Ejecuta `ActualizarTemasLote`.
## Prueba rapida (solo primer par)

Si quieres depurar solo el primer caso, ejecuta la macro:

- `ProbarPrimerParHardcoded`

Esta prueba procesa solo:

- `TEMA 1.docx`
- `tema_1_rev.docx`

Y genera:

- `TEMA 1_ACTUALIZADO_TEST.docx`

4. La macro intentara usar la carpeta del documento activo (mas fiable en macOS).
5. Si no puede, intentara selector y deteccion automatica.

Si el selector no aparece, la macro usa un campo manual como alternativa.

## 3) Resultado

- Guarda los resultados en la misma carpeta `TEMAS`.
- Genera `TEMA X_ACTUALIZADO_yyyymmdd_hhnnss.docx` para cada par encontrado.
- Escribe `proceso_actualizacion_yyyymmdd_hhnnss.log`.

## Notas

- Solo procesa `.docx`.
- No modifica los originales.
- Empareja SOLO nombres exactos:
   - `TEMA 1.docx` con `tema_1_rev.docx`
   - `TEMA 2.docx` con `tema_2_rev.docx`
   - ...
- Usa el motor de Word para comparar y luego recalcula campos, TOC y tablas de figuras.
