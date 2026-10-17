from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
VENV_ROOT = ROOT.parents[1] / "venv_arm64"
VENV_PYTHON = VENV_ROOT / "bin" / "python"


def load_local_env() -> None:
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def ensure_venv_python() -> None:
    current_venv = Path(sys.prefix).resolve()
    if current_venv == VENV_ROOT.resolve():
        return
    if not VENV_PYTHON.exists():
        raise SystemExit(f"Missing shared virtual environment: {VENV_PYTHON}")
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), str(Path(__file__).resolve()), *sys.argv[1:]])


def main() -> None:
    os.chdir(ROOT)
    ensure_venv_python()
    load_local_env()
    sys.path.insert(0, str(ROOT / "src"))

    from p1_d2_engine.cli import main as cli_main

    if len(sys.argv) == 1:
        sys.argv.extend(
            [
                "run",
                "--input",
                "input/tickers_technical.csv",
                "--output",
                "output",
                "--limit",
                "20",
            ]
        )
    cli_main()


if __name__ == "__main__":
    main()
