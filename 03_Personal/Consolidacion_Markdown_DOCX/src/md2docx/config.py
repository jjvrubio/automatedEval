from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - fallback for bare Python setups.
    yaml = None


@dataclass
class ProfileConfig:
    name: str
    from_format: str | None = None
    to_format: str | None = None
    standalone: bool | None = None
    toc: bool | None = None
    toc_depth: int | None = None
    citeproc: bool = False
    defaults_file: Path | None = None
    lua_filters: list[Path] | None = None
    metadata_file: Path | None = None
    metadata: dict[str, Any] | None = None
    variables: dict[str, Any] | None = None
    bibliography: list[Path] | None = None
    csl: Path | None = None
    reference_doc: Path | None = None
    resource_path: list[Path] | None = None
    extra_args: list[str] | None = None
    style_template: Path | None = None
    cover_template: Path | None = None


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if key == "extends":
            continue
        if (
            isinstance(value, dict)
            and isinstance(merged.get(key), dict)
        ):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _strip_comment(line: str) -> str:
    quote: str | None = None
    for i, char in enumerate(line):
        if char in {'"', "'"}:
            if quote == char:
                quote = None
            elif quote is None:
                quote = char
        elif char == "#" and quote is None and (i == 0 or line[i - 1].isspace()):
            return line[:i].rstrip()
    return line.rstrip()


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    if value in {"true", "True", "TRUE"}:
        return True
    if value in {"false", "False", "FALSE"}:
        return False
    if (
        len(value) >= 2
        and value[0] == value[-1]
        and value[0] in {'"', "'"}
    ):
        return value[1:-1]
    try:
        return int(value)
    except ValueError:
        return value


def _minimal_yaml_load(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    pending: tuple[int, dict[str, Any], str] | None = None

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        line = _strip_comment(raw_line)
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()

        parent = stack[-1][1]

        if content.startswith("- "):
            if pending and pending[0] == indent:
                _, mapping, key = pending
                mapping[key] = []
                parent = mapping[key]
                stack.append((indent - 1, parent))
                pending = None
            if not isinstance(parent, list):
                raise ValueError(f"YAML no soportado cerca de: {raw_line}")
            parent.append(_parse_scalar(content[2:]))
            continue

        if ":" not in content:
            raise ValueError(f"YAML no soportado cerca de: {raw_line}")

        key, value = content.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not isinstance(parent, dict):
            raise ValueError(f"YAML no soportado cerca de: {raw_line}")

        if value:
            parent[key] = _parse_scalar(value)
            pending = None
        else:
            parent[key] = {}
            pending = (indent + 2, parent, key)
            stack.append((indent, parent[key]))

    return root


def _load_yaml(text: str) -> dict[str, Any]:
    if yaml is not None:
        return yaml.safe_load(text) or {}
    return _minimal_yaml_load(text)


def _load_profile_raw(
    profiles_dir: Path,
    profile_name: str,
    seen: set[str] | None = None,
) -> dict[str, Any]:
    seen = seen or set()
    if profile_name in seen:
        chain = " -> ".join([*seen, profile_name])
        raise ValueError(f"Herencia circular entre perfiles: {chain}")
    seen.add(profile_name)

    profile_file = profiles_dir / f"{profile_name}.yaml"
    if not profile_file.exists():
        raise FileNotFoundError(f"Perfil no encontrado: {profile_file}")

    raw = _load_yaml(profile_file.read_text(encoding="utf-8"))
    parent_names = raw.get("extends")
    if not parent_names:
        return raw

    if isinstance(parent_names, str):
        parent_names = [parent_names]

    merged: dict[str, Any] = {}
    for parent_name in parent_names:
        parent_raw = _load_profile_raw(profiles_dir, str(parent_name), seen=set(seen))
        merged = _deep_merge(merged, parent_raw)
    return _deep_merge(merged, raw)


def _resolve_optional_path(base_dir: Path, value: str | None) -> Path | None:
    if not value:
        return None
    p = Path(value)
    if not p.is_absolute():
        p = (base_dir / p).resolve()
    return p


def _resolve_path_list(base_dir: Path, values: Any) -> list[Path] | None:
    if not values:
        return None
    if isinstance(values, str):
        values = [values]
    paths = [_resolve_optional_path(base_dir, str(v)) for v in values if v]
    return [p for p in paths if p is not None] or None


def _read_bool(raw: dict[str, Any], key: str) -> bool | None:
    if key not in raw:
        return None
    value = raw[key]
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"1", "true", "yes", "si", "sí"}:
            return True
        if normalized in {"0", "false", "no"}:
            return False
    return None


def _read_int(raw: dict[str, Any], *keys: str) -> int | None:
    for key in keys:
        if key not in raw:
            continue
        value = raw[key]
        try:
            return int(value)
        except (TypeError, ValueError):
            return None
    return None


def _read_dict(raw: dict[str, Any], key: str) -> dict[str, Any] | None:
    value = raw.get(key)
    return value if isinstance(value, dict) else None


def _read_str_list(raw: dict[str, Any], key: str) -> list[str] | None:
    value = raw.get(key)
    if not value:
        return None
    if isinstance(value, str):
        return [value]
    return [str(v) for v in value if v]


def load_profile(project_root: Path, profile_name: str) -> ProfileConfig:
    profiles_dir = project_root / "configs" / "profiles"
    raw = _load_profile_raw(profiles_dir=profiles_dir, profile_name=profile_name)

    return ProfileConfig(
        name=profile_name,
        from_format=raw.get("from_format") or raw.get("from"),
        to_format=raw.get("to_format") or raw.get("to"),
        standalone=_read_bool(raw, "standalone"),
        toc=_read_bool(raw, "toc"),
        toc_depth=_read_int(raw, "toc_depth", "toc-depth"),
        citeproc=bool(_read_bool(raw, "citeproc")),
        defaults_file=_resolve_optional_path(project_root, raw.get("defaults_file")),
        lua_filters=_resolve_path_list(project_root, raw.get("lua_filters")),
        metadata_file=_resolve_optional_path(project_root, raw.get("metadata_file")),
        metadata=_read_dict(raw, "metadata"),
        variables=_read_dict(raw, "variables"),
        bibliography=_resolve_path_list(project_root, raw.get("bibliography")),
        csl=_resolve_optional_path(project_root, raw.get("csl")),
        reference_doc=_resolve_optional_path(project_root, raw.get("reference_doc")),
        resource_path=_resolve_path_list(project_root, raw.get("resource_path")),
        extra_args=_read_str_list(raw, "extra_args"),
        style_template=_resolve_optional_path(project_root, raw.get("style_template")),
        cover_template=_resolve_optional_path(project_root, raw.get("cover_template")),
    )


def resource_path_arg(paths: list[Path]) -> str:
    return os.pathsep.join(str(p) for p in paths)


def list_profiles(project_root: Path) -> list[str]:
    profiles_dir = project_root / "configs" / "profiles"
    return sorted(path.stem for path in profiles_dir.glob("*.yaml"))
