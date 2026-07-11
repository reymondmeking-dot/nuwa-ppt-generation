from __future__ import annotations

from pathlib import Path


def test_full_extra_contains_local_ui_runtime() -> None:
    pyproject = Path(__file__).parents[1] / "pyproject.toml"
    content = pyproject.read_text(encoding="utf-8")
    full = content.split("full = [", 1)[1].split("]", 1)[0]

    assert '"flask>=3.0,<4"' in full.lower()
