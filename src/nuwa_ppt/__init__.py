"""Nuwa PPT Generation — cross-platform CLI wrapper for the ppt-master skill.

The heavy lifting lives inside ``skills/productivity/ppt-master/scripts``.
This package only exposes a thin CLI so ``pip install -e .`` gives users a
convenient ``nuwa-ppt`` entry point on both macOS and Windows without
relocating any of the skill's files.
"""

__version__ = "1.0.0"
__author__ = "ReyMao"
__license__ = "MIT"
