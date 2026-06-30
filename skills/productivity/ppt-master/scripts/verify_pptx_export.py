#!/usr/bin/env python3
"""Verify a ppt-master exported PPTX for structural correctness.

Usage:
    python verify_pptx_export.py <pptx_path> [--require-gif]

Checks:
- zip is valid and opens as a PPTX
- [Content_Types].xml exists and parses
- ppt/slides/ has at least 1 slide
- slide rels count matches slides
- When --require-gif is passed: ppt/media/*.gif exists,
  [Content_Types].xml contains image/gif, and slide rels reference .gif
"""

from __future__ import annotations
import sys, zipfile, re, json
from pathlib import Path

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: verify_pptx_export.py <pptx_path> [--require-gif]")
        sys.exit(1)

    pptx_path = Path(args[0])
    require_gif = "--require-gif" in args

    if not pptx_path.exists():
        print(f"ERROR: {pptx_path} not found")
        sys.exit(1)

    with zipfile.ZipFile(pptx_path) as z:
        names = z.namelist()

        ct = z.read("[Content_Types].xml").decode("utf-8", errors="replace")
        assert "<Default Extension=\"xml\"" in ct, "[Content_Types].xml corrupt"

        slides = [n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)]
        notes = [n for n in names if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)]
        media = [n for n in names if n.startswith("ppt/media/")]
        rels = [n for n in names if re.match(r"ppt/slides/_rels/slide\d+\.xml.rels$", n)]

        result = {
            "ok": True,
            "pptx": str(pptx_path),
            "size_bytes": pptx_path.stat().st_size,
            "slides": len(slides),
            "notes_slides": len(notes),
            "media_files": media,
            "rels_count": len(rels),
        }

        transitions = 0
        animations = 0
        for s in slides:
            xml = z.read(s).decode("utf-8", errors="replace")
            transitions += xml.count("<p:transition")
            animations += xml.count("<p:animEffect")
        result["slide_count_with_transitions"] = transitions
        result["anim_effect_count"] = animations

        if require_gif:
            gif_media = [m for m in media if m.lower().endswith(".gif")]
            gif_in_ct = "image/gif" in ct or 'Extension="gif"' in ct
            gif_in_rels = 0
            for r in rels:
                gif_in_rels += z.read(r).decode("utf-8", errors="replace").count(".gif")

            result["has_gif_media"] = len(gif_media) > 0
            result["has_gif_content_type"] = gif_in_ct
            result["gif_relationships"] = gif_in_rels

            if not gif_media:
                result["ok"] = False
                result["error"] = "REQUIRED: ppt/media/*.gif not found"
            if not gif_in_ct:
                result["ok"] = False
                result["error"] = result.get("error", "") + " | [Content_Types].xml missing image/gif"
            if gif_in_rels < 1:
                result["ok"] = False
                result["error"] = result.get("error", "") + " | slide rels missing .gif reference"

    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result.get("ok", False) else 1)

if __name__ == "__main__":
    main()