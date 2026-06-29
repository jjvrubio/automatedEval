# SVG to PPTX

Genera una presentacion PowerPoint con una diapositiva por cada SVG.

El flujo previsto es intermedio:

1. Crear el PPTX automaticamente con SVG vectoriales a pantalla completa.
2. Abrir el PPTX en PowerPoint.
3. Convertir/desagrupar los SVG desde PowerPoint cuando se necesiten objetos editables.

Esto mantiene el origen limpio y evita reimplementar todo SVG como DrawingML. Los SVG complejos pueden conservarse como vector si PowerPoint no los convierte bien.

## Requisitos

El repo ya declara `python-pptx==1.0.2` en `requirements.txt`. En este workspace funciona con:

```bash
venv_arm64/bin/python "03_Personal/Automatizaciones/svg_to_pptx/svg_to_pptx.py" --help
```

## Uso

Procesar una carpeta completa:

```bash
venv_arm64/bin/python "03_Personal/Automatizaciones/svg_to_pptx/svg_to_pptx.py" \
  "/ruta/a/carpeta_svg" \
  --output "03_Personal/Automatizaciones/svg_to_pptx/output/deck.pptx"
```

Procesar una lista concreta de SVG:

```bash
venv_arm64/bin/python "03_Personal/Automatizaciones/svg_to_pptx/svg_to_pptx.py" \
  "/ruta/01_slide.svg" \
  "/ruta/02_slide.svg" \
  "/ruta/03_slide.svg" \
  --output "03_Personal/Automatizaciones/svg_to_pptx/output/deck.pptx"
```

Los SVG se ordenan por el prefijo numerico inicial del nombre de archivo. Por ejemplo, `01_...svg`, `02_...svg`, `10_...svg`.

## Salida

El script genera:

- Un `.pptx`.
- Un `.manifest.json` junto al PPTX, con el orden final y diagnostico basico por SVG.

El manifiesto cuenta textos, paths, grupos, imagenes embebidas, gradientes, patrones, filtros, mascaras, clips y `foreignObject`. Estos datos ayudan a identificar diapositivas que PowerPoint podria convertir con menor fidelidad al desagrupar.

## Notas sobre editabilidad

El PPTX generado contiene cada SVG como imagen vectorial. Para convertirlo a objetos editables hay que usar PowerPoint: seleccionar el SVG y aplicar la conversion/desagrupado a formas. En SVG sencillos esto suele producir objetos editables; en SVG con patrones, imagenes embebidas, gradientes o efectos, puede haber perdida de fidelidad o elementos que permanezcan como imagen.
