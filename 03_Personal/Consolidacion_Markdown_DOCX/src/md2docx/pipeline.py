from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .config import load_profile
from .pandoc_runner import build_pandoc_command, run_pandoc
from .postprocess import maybe_apply_style_template


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}


def _collect_markdown_image_dirs(md_parent: Path) -> list[Path]:
    """Recolecta carpetas locales con imagenes bajo el directorio del markdown.

    Permite resolver embeds de Obsidian con nombre corto (`![[imagen.svg]]`)
    cuando los binarios viven en subcarpetas (p. ej. `visual_system_*`).
    """
    if not md_parent.exists():
        return []

    image_dirs: set[Path] = {md_parent}
    for ext in IMAGE_EXTENSIONS:
        for image_path in md_parent.rglob(f"*{ext}"):
            image_dirs.add(image_path.parent)
    return sorted(image_dirs)


@dataclass
class BuildOptions:
    input_md: Path | list[Path]
    output_docx: Path
    profile_name: str
    metadata_file: Path | None = None
    reference_doc: Path | None = None
    style_template: Path | None = None


def run_build(project_root: Path, opts: BuildOptions) -> None:
    input_files = opts.input_md if isinstance(opts.input_md, list) else [opts.input_md]
    for input_md in input_files:
        if not input_md.exists():
            raise FileNotFoundError(f"No existe el markdown de entrada: {input_md}")

    opts.output_docx.parent.mkdir(parents=True, exist_ok=True)

    profile = load_profile(project_root=project_root, profile_name=opts.profile_name)
    resource_paths = list(profile.resource_path or [])
    for input_md in input_files:
        parent = input_md.parent
        for image_dir in _collect_markdown_image_dirs(parent):
            if image_dir not in resource_paths:
                resource_paths.append(image_dir)
    profile.resource_path = resource_paths or None

    command = build_pandoc_command(
        input_md=input_files,
        output_docx=opts.output_docx,
        profile=profile,
        metadata_file_override=opts.metadata_file,
        reference_doc_override=opts.reference_doc,
    )
    run_pandoc(command)

    # Si no se fuerza --style-template, reutilizamos la plantilla de referencia
    # para que el DOCX final herede estilos reales del documento base.
    style_template = (
        opts.style_template
        or profile.style_template
        or opts.reference_doc
        or profile.reference_doc
    )
    maybe_apply_style_template(
        output_docx=opts.output_docx,
        style_template=style_template,
        project_root=project_root,
    )
