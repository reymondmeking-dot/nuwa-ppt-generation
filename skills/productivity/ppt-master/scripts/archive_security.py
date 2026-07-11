"""Bounded ZIP/OOXML readers shared by PPTX, DOCX, EPUB, and XLSX tools."""

from __future__ import annotations

import stat
import zipfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import BinaryIO, Iterator


@dataclass(frozen=True)
class ArchiveLimits:
    max_entries: int = 10_000
    max_member_bytes: int = 256 * 1024 * 1024
    max_total_bytes: int = 1024 * 1024 * 1024


DEFAULT_ARCHIVE_LIMITS = ArchiveLimits()


def _validated_member_path(name: str) -> PurePosixPath:
    if not name or "\x00" in name or "\\" in name:
        raise ValueError(f"Unsafe archive member path: {name!r}")
    path = PurePosixPath(name)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise ValueError(f"Unsafe archive member path: {name!r}")
    return path


def validate_zip_archive(
    archive: zipfile.ZipFile,
    limits: ArchiveLimits = DEFAULT_ARCHIVE_LIMITS,
) -> list[zipfile.ZipInfo]:
    """Validate metadata before any member is read or extracted."""
    infos = archive.infolist()
    if len(infos) > limits.max_entries:
        raise ValueError(
            f"Archive contains {len(infos)} entries; limit is {limits.max_entries}"
        )

    total = 0
    names: set[str] = set()
    for info in infos:
        path = _validated_member_path(info.filename.rstrip("/") or info.filename)
        normalized = path.as_posix()
        if normalized in names:
            raise ValueError(f"Archive contains a duplicate member: {normalized}")
        names.add(normalized)

        if info.flag_bits & 0x1:
            raise ValueError(f"Encrypted archive members are not supported: {normalized}")
        mode = info.external_attr >> 16
        if stat.S_ISLNK(mode):
            raise ValueError(f"Archive symlinks are not supported: {normalized}")
        if info.file_size < 0 or info.file_size > limits.max_member_bytes:
            raise ValueError(
                f"Archive member {normalized!r} exceeds the "
                f"{limits.max_member_bytes}-byte limit"
            )
        total += info.file_size
        if total > limits.max_total_bytes:
            raise ValueError(
                f"Archive expands beyond the {limits.max_total_bytes}-byte limit"
            )
    return infos


@contextmanager
def open_safe_zip(
    source: str | Path | BinaryIO,
    *,
    limits: ArchiveLimits = DEFAULT_ARCHIVE_LIMITS,
) -> Iterator[zipfile.ZipFile]:
    archive = zipfile.ZipFile(source, "r")
    try:
        validate_zip_archive(archive, limits)
        yield archive
    finally:
        archive.close()


def validate_zip_path(
    source: str | Path | BinaryIO,
    *,
    limits: ArchiveLimits = DEFAULT_ARCHIVE_LIMITS,
) -> None:
    """Validate a package before handing it to a third-party OOXML reader."""
    with open_safe_zip(source, limits=limits):
        return


def safe_extractall(
    archive: zipfile.ZipFile,
    destination: str | Path,
    *,
    limits: ArchiveLimits = DEFAULT_ARCHIVE_LIMITS,
) -> None:
    """Extract validated regular files without delegating path handling."""
    infos = validate_zip_archive(archive, limits)
    root = Path(destination).resolve()
    root.mkdir(parents=True, exist_ok=True)
    total_written = 0

    for info in infos:
        relative = _validated_member_path(info.filename.rstrip("/") or info.filename)
        target = (root / Path(*relative.parts)).resolve()
        try:
            target.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"Archive member escapes destination: {info.filename!r}") from exc

        if info.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        member_written = 0
        with archive.open(info, "r") as source, target.open("wb") as output:
            while True:
                chunk = source.read(64 * 1024)
                if not chunk:
                    break
                member_written += len(chunk)
                total_written += len(chunk)
                if member_written > limits.max_member_bytes:
                    raise ValueError(f"Archive member grew beyond its size limit: {info.filename}")
                if total_written > limits.max_total_bytes:
                    raise ValueError("Archive extraction exceeded its total size limit")
                output.write(chunk)


def copy_zip_member(
    archive: zipfile.ZipFile,
    info: zipfile.ZipInfo,
    output: BinaryIO,
    *,
    max_bytes: int = DEFAULT_ARCHIVE_LIMITS.max_member_bytes,
) -> int:
    """Copy one member with an actual-byte guard; return bytes written."""
    if info.file_size > max_bytes:
        raise ValueError(f"Archive member exceeds the {max_bytes}-byte limit")
    with archive.open(info, "r") as source:
        copied = 0
        while True:
            chunk = source.read(64 * 1024)
            if not chunk:
                break
            copied += len(chunk)
            if copied > max_bytes:
                raise ValueError(f"Archive member exceeds the {max_bytes}-byte limit")
            output.write(chunk)
    return copied
