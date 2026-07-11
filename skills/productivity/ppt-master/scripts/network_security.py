"""Shared network safety helpers for source and asset downloaders."""

from __future__ import annotations

import ipaddress
import os
import socket
from urllib.parse import urljoin, urlparse

DEFAULT_ALLOWED_PORTS = frozenset({80, 443})
REDIRECT_STATUSES = frozenset({301, 302, 303, 307, 308})


def _env_flag(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}


def validate_public_http_url(
    url: object,
    *,
    allow_private: bool | None = None,
    allow_nonstandard_ports: bool | None = None,
) -> str:
    """Validate an HTTP(S) URL and reject local/private network targets."""
    if not isinstance(url, str):
        raise ValueError("URL must be a string")
    value = url.strip()
    if not value or len(value) > 4096:
        raise ValueError("URL is empty or too long")

    try:
        parsed = urlparse(value)
        hostname = parsed.hostname
        port = parsed.port or (443 if parsed.scheme.lower() == "https" else 80)
    except ValueError as exc:
        raise ValueError("URL contains an invalid host or port") from exc

    if parsed.scheme.lower() not in {"http", "https"} or not hostname:
        raise ValueError("Only absolute HTTP(S) URLs are supported")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("Credentials embedded in URLs are not allowed")

    if allow_nonstandard_ports is None:
        allow_nonstandard_ports = _env_flag(
            "PPT_MASTER_ALLOW_NONSTANDARD_PORTS"
        )
    if not allow_nonstandard_ports and port not in DEFAULT_ALLOWED_PORTS:
        raise ValueError("Non-standard URL ports are disabled")

    if allow_private is None:
        allow_private = _env_flag("PPT_MASTER_ALLOW_PRIVATE_NETWORK")
    if allow_private:
        return value

    try:
        literal = ipaddress.ip_address(hostname.split("%", 1)[0])
        addresses = [literal]
    except ValueError:
        try:
            resolved = socket.getaddrinfo(
                hostname,
                port,
                type=socket.SOCK_STREAM,
                proto=socket.IPPROTO_TCP,
            )
        except OSError as exc:
            raise ValueError(f"Unable to resolve URL host: {hostname}") from exc
        addresses = []
        for item in resolved:
            try:
                addresses.append(
                    ipaddress.ip_address(item[4][0].split("%", 1)[0])
                )
            except ValueError as exc:
                raise ValueError("URL host resolved to an invalid address") from exc

    if not addresses or any(not address.is_global for address in addresses):
        raise ValueError("Private, loopback, link-local, and reserved hosts are blocked")
    return value


def redirect_url(current_url: str, response) -> str | None:
    if getattr(response, "status_code", None) not in REDIRECT_STATUSES:
        return None
    location = response.headers.get("Location") or response.headers.get("location")
    if not location:
        raise ValueError("Redirect response is missing a Location header")
    return urljoin(current_url, location)


def read_limited_response(response, max_bytes: int) -> bytes:
    """Read a streamed response without exceeding ``max_bytes``."""
    content_length = response.headers.get("Content-Length") or response.headers.get(
        "content-length"
    )
    if content_length:
        try:
            declared_length = int(content_length)
        except (TypeError, ValueError):
            declared_length = None
        if declared_length is not None and declared_length > max_bytes:
            raise ValueError(f"Response exceeds the {max_bytes}-byte limit")

    body = bytearray()
    try:
        for chunk in response.iter_content(chunk_size=64 * 1024):
            if not chunk:
                continue
            body.extend(chunk)
            if len(body) > max_bytes:
                raise ValueError(f"Response exceeds the {max_bytes}-byte limit")
    finally:
        close = getattr(response, "close", None)
        if callable(close):
            close()
    return bytes(body)


class BufferedResponse:
    """Small response proxy whose body has already been bounded and buffered."""

    def __init__(self, response, content: bytes) -> None:
        self._response = response
        self.content = content
        self.headers = response.headers
        self.status_code = response.status_code
        self.encoding = getattr(response, "encoding", None)
        self.apparent_encoding = None
        self.url = getattr(response, "url", None)

    def raise_for_status(self) -> None:
        self._response.raise_for_status()

    def __getattr__(self, name: str):
        return getattr(self._response, name)
