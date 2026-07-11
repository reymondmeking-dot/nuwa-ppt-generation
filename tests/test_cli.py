from __future__ import annotations

from pathlib import Path

import pytest

from nuwa_ppt import cli


def test_build_options_after_project_are_parsed() -> None:
    args = cli._build_parser().parse_args(
        [
            "build",
            "demo-quick-gif",
            "--transition",
            "push",
            "--animation",
            "auto",
            "--no-image-optimize",
            "--skip-pipeline",
        ]
    )

    assert args.project == "demo-quick-gif"
    assert args.transition == "push"
    assert args.animation == "auto"
    assert args.no_image_optimize is True
    assert args.skip_pipeline is True
    assert args.extra == []


def test_build_forwards_option_like_args_after_separator(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    calls: list[tuple[str, list[str], Path]] = []

    def fake_run(script: str, args: list[str], repo_root: Path) -> int:
        calls.append((script, args, repo_root))
        return 0

    monkeypatch.setattr(cli, "_run_script", fake_run)

    result = cli.main(
        [
            "--repo",
            str(tmp_path),
            "build",
            "deck",
            "--skip-pipeline",
            "--",
            "--workers",
            "2",
        ]
    )

    assert result == 0
    assert calls == [
        ("svg_to_pptx.py", ["deck", "--workers", "2"], tmp_path.resolve())
    ]


def test_explicit_repo_override_is_authoritative(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    fallback = tmp_path / "fallback"
    (fallback / cli.SKILL_REL_PATH).mkdir(parents=True)
    requested = tmp_path / "missing"
    monkeypatch.chdir(fallback)

    assert cli._find_repo_root(str(requested)) == requested.resolve()
