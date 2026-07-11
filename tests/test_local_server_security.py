from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest


@pytest.fixture()
def server_modules():
    scripts = (
        Path(__file__).parents[1]
        / "skills"
        / "productivity"
        / "ppt-master"
        / "scripts"
    )
    sys.path.insert(0, str(scripts))
    try:
        yield (
            importlib.import_module("server_common"),
            importlib.import_module("confirm_ui.server"),
            importlib.import_module("svg_editor.server"),
        )
    finally:
        sys.path.remove(str(scripts))


def test_confirm_ui_rejects_host_origin_and_missing_session(
    server_modules, tmp_path: Path
) -> None:
    common, confirm_server, _ = server_modules
    token = common.new_local_session_token()
    app = confirm_server.create_app(
        str(tmp_path), idle_timeout=0, session_token=token
    )
    app.config.update(TESTING=True)

    fresh = app.test_client()
    assert fresh.get("/", headers={"Host": "attacker.example"}).status_code == 403
    assert fresh.get(
        "/api/catalogs", headers={"Origin": "http://attacker.example"}
    ).status_code == 403
    assert fresh.post("/api/confirm", json={"stage": "tier1"}).status_code == 403

    browser = app.test_client()
    index = browser.get("/")
    assert index.status_code == 200
    assert "HttpOnly" in index.headers["Set-Cookie"]
    confirmed = browser.post(
        "/api/confirm",
        json={"stage": "tier1"},
        headers={"Origin": "http://localhost"},
    )
    assert confirmed.status_code == 200

    cli = app.test_client()
    direct = cli.post(
        "/api/confirm",
        json={"stage": "tier1"},
        headers={common.LOCAL_TOKEN_HEADER: token},
    )
    assert direct.status_code == 200


def test_svg_editor_uses_the_same_loopback_guard(server_modules, tmp_path: Path) -> None:
    common, _, svg_server = server_modules
    token = common.new_local_session_token()
    app = svg_server.create_app(
        str(tmp_path), idle_timeout=0, session_token=token
    )
    app.config.update(TESTING=True)
    client = app.test_client()

    assert client.get("/api/config", headers={"Host": "example.com"}).status_code == 403
    assert client.get("/").status_code == 200
    assert client.get("/api/config").status_code == 200


def test_project_lock_persists_private_session_token(
    server_modules, tmp_path: Path
) -> None:
    common, _, _ = server_modules
    token = common.new_local_session_token()
    lock = tmp_path / "server.lock"

    assert common.claim_lock(lock, 5050, token=token) is None
    assert common.read_lock(lock)["token"] == token
