from __future__ import annotations

import base64
import importlib
import sys
from pathlib import Path

import pytest


@pytest.fixture()
def doc_to_md():
    scripts = (
        Path(__file__).parents[1]
        / "skills"
        / "productivity"
        / "ppt-master"
        / "scripts"
    )
    sys.path.insert(0, str(scripts))
    try:
        yield importlib.import_module("source_to_md.doc_to_md")
    finally:
        sys.path.remove(str(scripts))


def test_local_images_cannot_escape_document_directory(doc_to_md, tmp_path: Path) -> None:
    source = tmp_path / "document"
    media = tmp_path / "media"
    source.mkdir()
    media.mkdir()
    safe = source / "safe.png"
    outside = tmp_path / "private.png"
    safe.write_bytes(b"png")
    outside.write_bytes(b"private")

    assert doc_to_md._copy_local_image("safe.png", source, media, 1) == "image_001.png"
    assert doc_to_md._copy_local_image("../private.png", source, media, 2) is None
    assert doc_to_md._copy_local_image(outside.as_uri(), source, media, 3) is None


def test_private_remote_images_are_rejected(doc_to_md, tmp_path: Path) -> None:
    assert doc_to_md._download_remote_image("http://127.0.0.1/a.png", tmp_path, 1) is None


def test_data_uri_size_is_bounded(
    doc_to_md, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(doc_to_md, "MAX_EMBED_IMAGE_BYTES", 3)
    payload = base64.b64encode(b"1234").decode("ascii")

    assert doc_to_md._save_data_uri(f"data:image/png;base64,{payload}", tmp_path, 1) is None
