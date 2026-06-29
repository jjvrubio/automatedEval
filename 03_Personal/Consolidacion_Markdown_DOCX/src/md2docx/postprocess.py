from pathlib import Path

from .style_transfer import aplicar_estilos_docx


def maybe_apply_style_template(
    output_docx: Path,
    style_template: Path | None,
    project_root: Path,
) -> None:
    """Punto de extension para post-procesado DOCX.

    Reutiliza la utilidad heredada para copiar estilos desde una plantilla
    Word sin tocar el contenido principal generado por Pandoc.
    """
    if not style_template:
        return

    aplicar_estilos_docx(
        plantilla=style_template,
        revisado=output_docx,
        salida=output_docx,
    )
