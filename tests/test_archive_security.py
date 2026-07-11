from __future__ import annotations

import importlib
import io
import sys
import zipfile
from pathlib import Path

import pytest


@pytest.fixture()
def archive_security():
    scripts = (
        Path(__file__).parents[1]
        / "skills"
        / "productivity"
        / "ppt-master"
        / "scripts"
    )
    sys.path.insert(0, str(scripts))
    try:
        yield importlib.import_module("archive_security")
    finally:
        sys.path.remove(str(scripts))


def _zip_bytes(entries: list[tuple[str, bytes]]) -> io.BytesIO:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in entries:
            archive.writestr(name, data)
    output.seek(0)
    return output


def test_archive_entry_member_and_total_limits(archive_security) -> None:
    limits = archive_security.ArchiveLimits(
        max_entries=1, max_member_bytes=4, max_total_bytes=6
    )
    with pytest.raises(ValueError, match="entries"):
        with archive_security.open_safe_zip(
            _zip_bytes([("a", b"1"), ("b", b"2")]), limits=limits
        ):
            pass

    with pytest.raises(ValueError, match="member"):
        with archive_security.open_safe_zip(
            _zip_bytes([("a", b"12345")]), limits=limits
        ):
            pass

    total_limits = archive_security.ArchiveLimits(
        max_entries=2, max_member_bytes=4, max_total_bytes=6
    )
    with pytest.raises(ValueError, match="expands"):
        with archive_security.open_safe_zip(
            _zip_bytes([("a", b"1234"), ("b", b"5678")]), limits=total_limits
        ):
            pass


def test_safe_extract_rejects_traversal(archive_security, tmp_path: Path) -> None:
    archive_data = _zip_bytes([("../escape.txt", b"no")])
    with zipfile.ZipFile(archive_data) as archive:
        with pytest.raises(ValueError, match="Unsafe archive member"):
            archive_security.safe_extractall(archive, tmp_path / "out")

    assert not (tmp_path / "escape.txt").exists()


def test_safe_extract_writes_regular_files(archive_security, tmp_path: Path) -> None:
    archive_data = _zip_bytes([("ppt/slides/slide1.xml", b"<slide/>")])
    with zipfile.ZipFile(archive_data) as archive:
        archive_security.safe_extractall(archive, tmp_path / "out")

    assert (tmp_path / "out" / "ppt" / "slides" / "slide1.xml").read_bytes() == b"<slide/>"
