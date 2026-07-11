#!/usr/bin/env python3
"""
PPT Master - Local Preview Server Helpers

Shared per-project mutual-exclusion (lock) and liveness helpers for the local
Flask preview servers (`svg_editor/server.py`, `confirm_ui/server.py`). Each
server keeps its own lock filename and Flask app; this module owns only the
cross-platform process-liveness check and the claim/read/release lock logic so
the two servers cannot drift apart.

Usage:
    from server_common import process_alive, read_lock, claim_lock, release_lock, find_free_port

Dependencies:
    None (only uses standard library)
"""

import json
import hmac
import ipaddress
import os
import secrets
import socket
from pathlib import Path
from typing import Optional
from urllib.parse import urlsplit


LOCAL_TOKEN_HEADER = 'X-PPT-Master-Token'
UNSAFE_METHODS = frozenset({'POST', 'PUT', 'PATCH', 'DELETE'})


def find_free_port(preferred: int, host: str = '127.0.0.1', span: int = 50) -> int:
    """Return ``preferred`` if it is bindable, else the next free port within
    ``span``. Lets a new project's UI server coexist with another project's
    server already holding the default port, instead of crashing on bind — each
    project ends up on its own port serving its own data. Falls back to
    ``preferred`` if the whole span is taken (let the caller's bind surface it).
    """
    for port in range(preferred, preferred + span):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            probe.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                probe.bind((host, port))
                return port
            except OSError:
                continue
    return preferred


def process_alive(pid: int) -> bool:
    """Return True if a process with this pid is reachable.

    On POSIX, ``os.kill(pid, 0)`` succeeds when the process exists even without
    permission to signal it; ``PermissionError`` therefore still counts as
    alive. On Windows there is no ``os.kill(pid, 0)`` equivalent, so probe via
    ``OpenProcess`` + ``WaitForSingleObject``.
    """
    if pid <= 0:
        return False
    if os.name == 'nt':
        import ctypes
        import ctypes.wintypes

        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel32.OpenProcess.argtypes = [
            ctypes.wintypes.DWORD,
            ctypes.wintypes.BOOL,
            ctypes.wintypes.DWORD,
        ]
        kernel32.OpenProcess.restype = ctypes.wintypes.HANDLE
        kernel32.WaitForSingleObject.argtypes = [
            ctypes.wintypes.HANDLE,
            ctypes.wintypes.DWORD,
        ]
        kernel32.WaitForSingleObject.restype = ctypes.wintypes.DWORD
        kernel32.CloseHandle.argtypes = [ctypes.wintypes.HANDLE]
        kernel32.CloseHandle.restype = ctypes.wintypes.BOOL

        process_query_limited_information = 0x1000
        synchronize = 0x00100000
        wait_timeout = 0x00000102
        wait_object_0 = 0x00000000
        wait_failed = 0xFFFFFFFF

        handle = kernel32.OpenProcess(
            process_query_limited_information | synchronize,
            False,
            pid,
        )
        if not handle:
            return ctypes.get_last_error() == 5  # ERROR_ACCESS_DENIED
        try:
            result = kernel32.WaitForSingleObject(handle, 0)
            if result == wait_timeout:
                return True
            if result in (wait_object_0, wait_failed):
                return False
            return False
        finally:
            kernel32.CloseHandle(handle)

    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


def read_lock(lock_file: Path) -> Optional[dict]:
    """Read a lock file, returning the lock dict or None if absent/corrupt."""
    try:
        data = json.loads(lock_file.read_text(encoding='utf-8'))
        return data if isinstance(data, dict) else None
    except (OSError, json.JSONDecodeError):
        return None


def claim_lock(lock_file: Path, port: int, token: str | None = None) -> Optional[dict]:
    """Try to claim the per-project preview slot.

    Returns ``None`` on success. If another live process already holds the
    slot, returns the existing lock dict (caller surfaces it as an error).
    A stale lock (pointing at a dead pid) is silently overwritten.
    """
    existing = read_lock(lock_file)
    if existing and process_alive(int(existing.get('pid', 0))):
        return existing
    payload = {'pid': os.getpid(), 'port': port}
    if token:
        payload['token'] = token
    lock_file.write_text(json.dumps(payload), encoding='utf-8')
    try:
        lock_file.chmod(0o600)
    except OSError:
        pass
    return None


def release_lock(lock_file: Path) -> None:
    """Best-effort cleanup: only delete the lock if it still names *us*."""
    try:
        current = read_lock(lock_file)
        if current and int(current.get('pid', 0)) == os.getpid():
            lock_file.unlink(missing_ok=True)
    except OSError:
        pass


def new_local_session_token() -> str:
    return secrets.token_urlsafe(32)


def _loopback_host(host_header: str) -> bool:
    try:
        parsed = urlsplit(f'//{host_header}')
        if parsed.username is not None or parsed.password is not None:
            return False
        hostname = parsed.hostname
        _ = parsed.port
    except ValueError:
        return False
    if not hostname:
        return False
    if hostname.lower() == 'localhost':
        return True
    try:
        return ipaddress.ip_address(hostname.split('%', 1)[0]).is_loopback
    except ValueError:
        return False


def install_local_request_guard(app, token: str | None = None) -> str:
    """Protect a loopback Flask UI against DNS rebinding and cross-site writes."""
    from flask import jsonify, request

    session_token = token or new_local_session_token()
    cookie_name = f'ppt_master_{session_token[:12]}'
    app.config['LOCAL_SESSION_TOKEN'] = session_token
    app.config['LOCAL_SESSION_COOKIE'] = cookie_name

    @app.before_request
    def _guard_local_request():
        if not _loopback_host(request.host):
            return jsonify({'error': 'invalid host'}), 403

        origin = request.headers.get('Origin')
        if origin:
            try:
                parsed_origin = urlsplit(origin)
            except ValueError:
                return jsonify({'error': 'invalid origin'}), 403
            if (
                parsed_origin.scheme.lower() != 'http'
                or parsed_origin.netloc.lower() != request.host.lower()
            ):
                return jsonify({'error': 'invalid origin'}), 403

        if request.method in UNSAFE_METHODS:
            supplied = request.headers.get(LOCAL_TOKEN_HEADER) or request.cookies.get(
                cookie_name
            )
            if not supplied or not hmac.compare_digest(supplied, session_token):
                return jsonify({'error': 'invalid local session'}), 403
        return None

    @app.after_request
    def _local_security_headers(response):
        response.headers.setdefault('X-Content-Type-Options', 'nosniff')
        response.headers.setdefault('X-Frame-Options', 'DENY')
        response.headers.setdefault('Referrer-Policy', 'no-referrer')
        response.headers.setdefault('Cache-Control', 'no-store')
        return response

    return session_token


def set_local_session_cookie(app, response):
    response.set_cookie(
        app.config['LOCAL_SESSION_COOKIE'],
        app.config['LOCAL_SESSION_TOKEN'],
        httponly=True,
        samesite='Strict',
        secure=False,
    )
    return response
