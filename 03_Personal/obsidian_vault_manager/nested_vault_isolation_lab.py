#!/usr/bin/env python3
"""Create and check a disposable nested-vault isolation laboratory.

This deliberately does not import Obsidian, start a server, read credentials, or
write outside a TemporaryDirectory. It checks filesystem boundaries only; it is
not evidence of dynamic REST/MCP isolation.
"""
import json
import tempfile
from pathlib import Path


def build_fixture(root: Path) -> dict[str, Path]:
    parent = root / "parent-vault"
    child = parent / "child-vault"
    for vault in (parent, child):
        (vault / ".obsidian").mkdir(parents=True)
    (parent / "parent-document.md").write_text("PARENT-FIXTURE\n", encoding="utf-8")
    (child / "child-document.md").write_text("CHILD-FIXTURE\n", encoding="utf-8")
    (parent / ".obsidian" / "parent-config.json").write_text(
        '{"fixture": "parent"}\n', encoding="utf-8"
    )
    (child / ".obsidian" / "child-config.json").write_text(
        '{"fixture": "child"}\n', encoding="utf-8"
    )
    return {"parent": parent, "child": child}


def classify(parent: Path, child: Path) -> list[dict[str, str]]:
    checks = [
        ("parent-sees-child-document", child / "child-document.md", True),
        ("parent-config-is-not-child-config", parent / ".obsidian" / "child-config.json", False),
        ("child-config-exists", child / ".obsidian" / "child-config.json", True),
        ("child-document-is-descendant-of-parent", child / "child-document.md", True),
    ]
    results = []
    for name, path, expected_exists in checks:
        actual = path.exists()
        results.append(
            {
                "check": name,
                "path": path.relative_to(parent).as_posix(),
                "expected": "PRESENT" if expected_exists else "ABSENT",
                "observed": "PRESENT" if actual else "ABSENT",
                "result": "PASS" if actual == expected_exists else "FAIL",
                "meaning": (
                    "filesystem descendant is reachable from parent"
                    if expected_exists
                    else "parent fixture has no child configuration file at its own config scope"
                ),
            }
        )
    return results


def run() -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="obsidian-bridge-nested-") as directory:
        root = Path(directory)
        paths = build_fixture(root)
        results = classify(paths["parent"], paths["child"])
        return {
            "fixture_root": str(root),
            "temporary_only": True,
            "obsidian_started": False,
            "servers_started": False,
            "credentials_read": False,
            "writes_outside_fixture": False,
            "results": results,
            "warning": (
                "Filesystem reachability is not REST/MCP authorization evidence. "
                "Dynamic tests require explicit approval."
            ),
        }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
