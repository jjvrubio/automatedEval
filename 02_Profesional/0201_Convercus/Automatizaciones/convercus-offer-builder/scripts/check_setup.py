#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def read_simple_yaml(path: Path) -> dict[str, object]:
    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        yaml = None
    if yaml is not None:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    data: dict[str, object] = {}
    current_section: dict[str, object] | None = None
    current_list: list[str] | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()

        if line.startswith("- ") and current_list is not None:
            value = line[2:].strip().strip('"')
            current_list.append(value)
            continue

        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if indent == 0 and not value:
            current_section = {}
            data[key] = current_section
            current_list = None
            continue

        if current_section is None:
            continue

        if value:
            current_section[key] = value.strip('"')
            current_list = None
        else:
            current_list = []
            current_section[key] = current_list
    return data


def nested(data: dict[str, object], *keys: str) -> object:
    value: object = data
    for key in keys:
        if not isinstance(value, dict) or key not in value:
            raise KeyError(".".join(keys))
        value = value[key]
    return value


def main() -> int:
    skill_dir = Path(__file__).resolve().parents[1]
    capability_directory = skill_dir.parent
    config_path = skill_dir / "assets" / "convercus_offer_builder.yaml"
    config = read_simple_yaml(config_path)

    checks: list[tuple[str, bool, str]] = []

    def add(name: str, ok: bool, detail: str) -> None:
        checks.append((name, ok, detail))

    converter_root = Path(str(nested(config, "converter", "root")))
    trial_dir = Path(str(nested(config, "trial", "source_dir")))
    generated_dir = Path(str(nested(config, "workspace", "generated_dir")))

    add("skill manifest", (skill_dir / "SKILL.md").exists(), str(skill_dir / "SKILL.md"))
    add("openai yaml", (skill_dir / "agents" / "openai.yaml").exists(), str(skill_dir / "agents" / "openai.yaml"))
    add("assets config", config_path.exists(), str(config_path))
    add("converter root", converter_root.exists(), str(converter_root))
    add("converter cli", (converter_root / "md2docx.py").exists(), str(converter_root / "md2docx.py"))
    add("commercial profile", (converter_root / "configs" / "profiles" / "commercial_proposal.yaml").exists(), "commercial_proposal")
    add("convercus profile", (converter_root / "configs" / "profiles" / "docx_convercus_offer.yaml").exists(), "docx_convercus_offer")
    add("offer template", (converter_root / "assets" / "templates" / "plantilla_oferta.docx").exists(), "plantilla_oferta.docx")
    add("trial source dir", trial_dir.exists(), str(trial_dir))

    docs = nested(config, "trial", "documents")
    if isinstance(docs, list):
        for doc in docs:
            add(f"trial document: {doc}", (trial_dir / str(doc)).exists(), str(trial_dir / str(doc)))

    generated_dir.mkdir(parents=True, exist_ok=True)
    add("generated dir writable", generated_dir.exists() and generated_dir.is_dir(), str(generated_dir))

    print(json.dumps(
        {
            "skill_root": str(skill_dir),
            "capability_directory": str(capability_directory),
            "checks": [
                {"name": name, "ok": ok, "detail": detail}
                for name, ok, detail in checks
            ],
        },
        indent=2,
        ensure_ascii=False,
    ))

    return 0 if all(ok for _, ok, _ in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
