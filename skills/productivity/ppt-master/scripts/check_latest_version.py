"""Silent skill version check against GitHub releases / tags.

Contract:
  - Prints nothing when: (a) already on latest, (b) network fails, (c) API rate-limited,
    (d) no releases exist yet.
  - Prints a short user-facing update block ONLY when a newer version is available.
  - Never raises; never exits non-zero.

Called from SKILL.md rule #7 before the final delivery message. If output is non-empty,
the AI appends it verbatim to the end of its reply.
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

REPO = "reymondmeking-dot/nuwa-ppt-generation"
TIMEOUT_SEC = 3  # keep it snappy — silent-fail if slow


def _current_version() -> str:
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from skill_version import SKILL_VERSION  # type: ignore
        return SKILL_VERSION
    except Exception:
        return "0.0.0"


def _parse_semver(tag: str) -> tuple[int, ...]:
    """Parse 'v0.2.0' / '0.2.0' / '0.2.0-rc1' → (0, 2, 0). Returns (0,) on failure."""
    s = tag.lstrip("v").split("-")[0]
    try:
        return tuple(int(p) for p in s.split(".") if p.isdigit())
    except Exception:
        return (0,)


def _latest_release_tag() -> str | None:
    """Fetch latest release tag from GitHub API. Silent on any failure."""
    url = f"https://api.github.com/repos/{REPO}/releases/latest"
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
            if resp.status != 200:
                return None
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("tag_name")
    except Exception:
        return None


def main() -> int:
    current = _current_version()
    latest = _latest_release_tag()
    if not latest:
        return 0  # silent: no releases / offline / rate-limited
    if _parse_semver(latest) <= _parse_semver(current):
        return 0  # silent: already latest
    print(f"\n---\n> **ppt-master update available**: `{current}` → `{latest}`\n> Pull the latest from https://github.com/{REPO}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
