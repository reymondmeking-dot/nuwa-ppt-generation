from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest


@pytest.fixture()
def config_module():
    scripts = (
        Path(__file__).parents[1]
        / "skills"
        / "productivity"
        / "ppt-master"
        / "scripts"
    )
    sys.path.insert(0, str(scripts))
    try:
        yield importlib.import_module("config")
    finally:
        sys.path.remove(str(scripts))


def test_untrusted_cwd_env_is_ignored_by_default(
    config_module, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    untrusted = tmp_path / "untrusted"
    project = tmp_path / "skill"
    repo = tmp_path / "repo"
    untrusted.mkdir()
    project.mkdir()
    repo.mkdir()
    (untrusted / ".env").write_text(
        "OPENAI_BASE_URL=http://127.0.0.1:9999\n", encoding="utf-8"
    )

    monkeypatch.chdir(untrusted)
    monkeypatch.setattr(config_module, "PROJECT_ROOT", project)
    monkeypatch.setattr(config_module, "REPO_ROOT", repo)
    monkeypatch.setattr(config_module, "USER_ENV_FILE", tmp_path / "user.env")
    monkeypatch.delenv(config_module.ENV_FILE_VARIABLE, raising=False)
    monkeypatch.delenv(config_module.TRUST_CWD_ENV_VARIABLE, raising=False)

    assert untrusted / ".env" not in config_module.get_env_candidates()
    assert config_module.resolve_env_path() == (project / ".env").resolve()


def test_cwd_env_requires_explicit_opt_in(
    config_module, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv(config_module.ENV_FILE_VARIABLE, raising=False)
    monkeypatch.setenv(config_module.TRUST_CWD_ENV_VARIABLE, "1")

    assert config_module.get_env_candidates()[0] == (tmp_path / ".env").resolve()
