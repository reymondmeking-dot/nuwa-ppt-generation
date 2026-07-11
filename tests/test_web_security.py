from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest


@pytest.fixture()
def web_to_md():
    scripts = (
        Path(__file__).parents[1]
        / "skills"
        / "productivity"
        / "ppt-master"
        / "scripts"
    )
    sys.path.insert(0, str(scripts))
    try:
        yield importlib.import_module("source_to_md.web_to_md")
    finally:
        sys.path.remove(str(scripts))


class FakeResponse:
    encoding = "utf-8"
    url = "https://1.1.1.1/"

    def __init__(self, status: int, headers: dict | None = None, chunks=()) -> None:
        self.status_code = status
        self.headers = headers or {}
        self._chunks = chunks
        self.closed = False

    def iter_content(self, chunk_size):
        yield from self._chunks

    def close(self):
        self.closed = True

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError("HTTP error")


def test_redirects_are_revalidated_and_tls_verification_stays_enabled(
    web_to_md, monkeypatch: pytest.MonkeyPatch
) -> None:
    seen_kwargs = []
    response = FakeResponse(302, {"Location": "http://127.0.0.1/private"})

    def fake_get(url, **kwargs):
        seen_kwargs.append(kwargs)
        return response

    monkeypatch.setattr(web_to_md, "curl_requests", None)
    monkeypatch.setattr(web_to_md.requests, "get", fake_get)

    with pytest.raises(ValueError, match="blocked"):
        web_to_md._http_get("https://1.1.1.1/page")

    assert seen_kwargs[0]["verify"] is True
    assert seen_kwargs[0]["allow_redirects"] is False
    assert response.closed is True


def test_web_response_size_is_bounded(
    web_to_md, monkeypatch: pytest.MonkeyPatch
) -> None:
    response = FakeResponse(200, chunks=(b"1234", b"5678"))
    monkeypatch.setattr(web_to_md, "curl_requests", None)
    monkeypatch.setattr(web_to_md.requests, "get", lambda *args, **kwargs: response)

    with pytest.raises(ValueError, match="exceeds"):
        web_to_md._http_get("https://1.1.1.1/page", max_bytes=6)
