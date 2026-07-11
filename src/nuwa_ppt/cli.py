"""Thin cross-platform CLI wrapper around the ppt-master skill scripts.

Design principle: DO NOT relocate or duplicate the skill's scripts. This
module locates the skill folder relative to the current working directory
(or an explicit ``--repo`` argument) and delegates to the existing
scripts via ``subprocess`` using the current Python interpreter. That
keeps a single source of truth in
``skills/productivity/ppt-master/scripts``.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

from . import __version__


SKILL_REL_PATH = Path("skills") / "productivity" / "ppt-master"


def _find_repo_root(explicit: Optional[str]) -> Path:
    """Locate the nuwa-ppt-generation repository root.

    Order of resolution:
      1. Explicit ``--repo`` argument.
      2. ``NUWA_PPT_REPO`` environment variable.
      3. Walk up from CWD looking for ``skills/productivity/ppt-master``.
      4. Walk up from this file (works when installed in editable mode).
      5. Fallback: CWD.
    """
    if explicit:
        # An explicit override is authoritative.  Returning it even when the
        # skill directory is missing lets the caller report the actual typo or
        # stale path instead of silently selecting an unrelated checkout from
        # the current working directory.
        return Path(explicit).expanduser().resolve()

    candidates: List[Path] = []
    env = os.environ.get("NUWA_PPT_REPO")
    if env:
        candidates.append(Path(env).expanduser().resolve())

    def _walk_up(start: Path) -> Optional[Path]:
        for parent in [start, *start.parents]:
            if (parent / SKILL_REL_PATH).is_dir():
                return parent
        return None

    for start in (Path.cwd(), Path(__file__).resolve()):
        found = _walk_up(start)
        if found:
            candidates.append(found)

    for c in candidates:
        if (c / SKILL_REL_PATH).is_dir():
            return c

    # Fall back to CWD — commands that don't need the skill still work.
    return Path.cwd()


def _skill_scripts_dir(repo_root: Path) -> Path:
    return repo_root / SKILL_REL_PATH / "scripts"


def _run_script(script_name: str, args: List[str], repo_root: Path) -> int:
    scripts_dir = _skill_scripts_dir(repo_root)
    script_path = scripts_dir / script_name
    if not script_path.is_file():
        print(
            f"[nuwa-ppt] ERROR: expected script not found: {script_path}",
            file=sys.stderr,
        )
        print(
            "           Are you inside a nuwa-ppt-generation checkout? "
            "Pass --repo <path> or set NUWA_PPT_REPO.",
            file=sys.stderr,
        )
        return 2
    # Add the scripts dir to PYTHONPATH so local imports (e.g.
    # ``console_encoding``) resolve the same way as running the script
    # directly.
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = (
        f"{scripts_dir}{os.pathsep}{existing}" if existing else str(scripts_dir)
    )
    cmd = [sys.executable, str(script_path), *args]
    proc = subprocess.run(cmd, env=env)
    return proc.returncode


# ─────────────────────────── subcommands ────────────────────────────


def cmd_version(_args: argparse.Namespace) -> int:
    print(__version__)
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    repo_root = _find_repo_root(args.repo)
    return _run_script("svg_quality_checker.py", [args.path], repo_root)


def cmd_split(args: argparse.Namespace) -> int:
    repo_root = _find_repo_root(args.repo)
    return _run_script("total_md_split.py", [args.project], repo_root)


def cmd_finalize(args: argparse.Namespace) -> int:
    repo_root = _find_repo_root(args.repo)
    return _run_script("finalize_svg.py", [args.project], repo_root)


def cmd_build(args: argparse.Namespace) -> int:
    """Full pipeline: quality-check → split notes → finalize → export."""
    repo_root = _find_repo_root(args.repo)
    project = args.project
    steps = [
        ("svg_quality_checker.py", [project]),
        ("total_md_split.py", [project]),
        ("finalize_svg.py", [project]),
    ]
    if not args.skip_pipeline:
        for script, script_args in steps:
            rc = _run_script(script, script_args, repo_root)
            if rc != 0:
                print(
                    f"[nuwa-ppt] step {script} failed (exit {rc}); aborting.",
                    file=sys.stderr,
                )
                return rc

    export_args: List[str] = [project]
    if args.transition:
        export_args += ["-t", args.transition]
    if args.animation:
        export_args += ["-a", args.animation]
    if args.no_image_optimize:
        export_args.append("--no-image-optimize")
    if args.extra:
        export_args += args.extra
    return _run_script("svg_to_pptx.py", export_args, repo_root)


def cmd_demo(_args: argparse.Namespace) -> int:
    print(
        """\
nuwa-ppt demo — how to run the included demos

Quick GIF demo (single page, animated GIF regression):
    nuwa-ppt build demo-quick-gif --no-image-optimize \\
        --transition push --animation auto

Official smoke demo (5-page high-design deck):
    nuwa-ppt build demo-official-smoke --no-image-optimize \\
        --transition push --animation auto

Both commands run:
    svg_quality_checker.py → total_md_split.py → finalize_svg.py → svg_to_pptx.py

Outputs land in <project>/exports/*.pptx. See README for details.
"""
    )
    return 0


def cmd_info(args: argparse.Namespace) -> int:
    repo_root = _find_repo_root(args.repo)
    print(f"nuwa-ppt         : {__version__}")
    print(f"python           : {sys.version.split()[0]} ({sys.executable})")
    print(f"platform         : {sys.platform}")
    print(f"resolved repo    : {repo_root}")
    scripts_dir = _skill_scripts_dir(repo_root)
    print(f"skill scripts    : {scripts_dir}")
    print(f"skill available  : {scripts_dir.is_dir()}")
    return 0


# ───────────────────────────── parser ───────────────────────────────


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="nuwa-ppt",
        description=(
            "Nuwa PPT Generation — cross-platform CLI for the SVG-to-PPTX "
            "pipeline (macOS / Windows / Linux)."
        ),
    )
    p.add_argument(
        "--repo",
        help=(
            "Path to the nuwa-ppt-generation repo (contains "
            "skills/productivity/ppt-master). Defaults to auto-detect."
        ),
    )
    sub = p.add_subparsers(dest="command", metavar="<command>")

    s = sub.add_parser("version", help="Print the nuwa-ppt version.")
    s.set_defaults(func=cmd_version)

    s = sub.add_parser(
        "validate",
        help="Run the SVG quality checker on a project folder.",
    )
    s.add_argument("path", help="Project folder or SVG source path.")
    s.set_defaults(func=cmd_validate)

    s = sub.add_parser("split", help="Split notes/total.md into per-slide notes.")
    s.add_argument("project", help="Project folder containing notes/total.md.")
    s.set_defaults(func=cmd_split)

    s = sub.add_parser(
        "finalize",
        help="Run finalize_svg.py (icon embed + image alignment).",
    )
    s.add_argument("project", help="Project folder.")
    s.set_defaults(func=cmd_finalize)

    s = sub.add_parser(
        "build",
        help="Full pipeline: validate → split → finalize → export PPTX.",
    )
    s.add_argument("project", help="Project folder.")
    s.add_argument("--transition", "-t", default=None, help="PPT transition (e.g. push).")
    s.add_argument("--animation", "-a", default=None, help="Animation preset (e.g. auto).")
    s.add_argument(
        "--no-image-optimize",
        action="store_true",
        help="Preserve original image bytes (required for animated GIF).",
    )
    s.add_argument(
        "--skip-pipeline",
        action="store_true",
        help="Skip pre-export steps and run svg_to_pptx.py only.",
    )
    s.add_argument(
        "extra",
        nargs="*",
        help=(
            "Extra positional args forwarded to svg_to_pptx.py. Prefix "
            "option-like passthrough args with '--'."
        ),
    )
    s.set_defaults(func=cmd_build)

    s = sub.add_parser("demo", help="Print instructions for running the bundled demos.")
    s.set_defaults(func=cmd_demo)

    s = sub.add_parser("info", help="Print resolved paths / environment info.")
    s.set_defaults(func=cmd_info)

    return p


def _parse_args(
    parser: argparse.ArgumentParser, argv: Optional[List[str]]
) -> argparse.Namespace:
    """Parse CLI args while reserving ``--`` for build-script passthrough."""
    raw = list(argv) if argv is not None else sys.argv[1:]
    passthrough: List[str] = []
    if "--" in raw:
        separator = raw.index("--")
        passthrough = raw[separator + 1 :]
        raw = raw[:separator]

    args = parser.parse_args(raw)
    if passthrough:
        if getattr(args, "command", None) != "build":
            parser.error("arguments after '--' are only supported by the build command")
        args.extra.extend(passthrough)
    return args


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    args = _parse_args(parser, argv)
    if not getattr(args, "command", None):
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
