from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest


@pytest.fixture()
def network_security():
    scripts = (
        Path(__file__).parents[1]
        / "skills"
        / "productivity"
        / "ppt-master"
        / "scripts"
    )
    sys.path.insert(0, str(scripts))
    try:
        yield importlib.import_module("network_security")
    finally:
        sys.path.remove(str(scripts))


def test_private_and_nonstandard_targets_are_blocked(network_security) -> None:
    with pytest.raises(ValueError, match="blocked"):
        network_security.validate_public_http_url("http://127.0.0.1/file")
    with pytest.raises(ValueError, match="ports"):
        network_security.validate_public_http_url("https://1.1.1.1:8443/file")


def test_explicit_private_network_opt_in_is_supported(network_security) -> None:
    assert (
        network_security.validate_public_http_url(
            "http://127.0.0.1:8080/file",
            allow_private=True,
            allow_nonstandard_ports=True,
        )
        == "http://127.0.0.1:8080/file"
    )


def test_response_reader_stops_at_limit(network_security) -> None:
    class Response:
        headers = {}

        def iter_content(self, chunk_size):
            yield b"1234"
            yield b"5678"

        def close(self):
            return None

    with pytest.raises(ValueError, match="exceeds"):
        network_security.read_limited_response(Response(), 6)
