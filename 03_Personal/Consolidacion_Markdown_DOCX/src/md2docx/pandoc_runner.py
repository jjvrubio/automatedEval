from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any

from .config import ProfileConfig, resource_path_arg


def _pandoc_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def build_pandoc_command(
    input_md: Path | list[Path],
    output_docx: Path,
    profile: ProfileConfig,
    metadata_file_override: Path | None = None,
    reference_doc_override: Path | None = None,
) -> list[str]:
    input_files = input_md if isinstance(input_md, list) else [input_md]
    cmd: list[str] = ["pandoc", *[str(p) for p in input_files], "-o", str(output_docx)]

    if profile.defaults_file:
        cmd.extend(["--defaults", str(profile.defaults_file)])

    if profile.from_format:
        cmd.extend(["--from", profile.from_format])

    if profile.to_format:
        cmd.extend(["--to", profile.to_format])

    if profile.standalone:
        cmd.append("--standalone")

    if profile.toc is not None:
        cmd.append("--toc" if profile.toc else "--no-toc")

    if profile.toc_depth is not None:
        cmd.extend(["--toc-depth", str(profile.toc_depth)])

    metadata_file = metadata_file_override or profile.metadata_file
    if metadata_file:
        cmd.extend(["--metadata-file", str(metadata_file)])

    for key, value in (profile.metadata or {}).items():
        cmd.extend(["--metadata", f"{key}={_pandoc_value(value)}"])

    for key, value in (profile.variables or {}).items():
        cmd.extend(["--variable", f"{key}={_pandoc_value(value)}"])

    reference_doc = reference_doc_override or profile.reference_doc
    if reference_doc:
        cmd.extend(["--reference-doc", str(reference_doc)])

    for lua_filter in profile.lua_filters or []:
        cmd.extend(["--lua-filter", str(lua_filter)])

    if profile.citeproc:
        cmd.append("--citeproc")

    for bibliography in profile.bibliography or []:
        cmd.extend(["--bibliography", str(bibliography)])

    if profile.csl:
        cmd.extend(["--csl", str(profile.csl)])

    if profile.resource_path:
        cmd.extend(["--resource-path", resource_path_arg(profile.resource_path)])

    cmd.extend(profile.extra_args or [])

    return cmd


def run_pandoc(command: list[str]) -> None:
    if shutil.which("pandoc") is None:
        raise RuntimeError("No se encontro pandoc en PATH.")

    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        stderr = result.stderr.strip() or "(sin stderr)"
        stdout = result.stdout.strip() or "(sin stdout)"
        raise RuntimeError(
            "Pandoc fallo durante la conversion.\n"
            f"Comando: {' '.join(command)}\n"
            f"STDOUT: {stdout}\n"
            f"STDERR: {stderr}"
        )
