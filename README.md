# Nuwa PPT Generation

> **Agentic SVG-to-PPTX deck generation for high-end presentations.**
>
> Nuwa PPT Generation turns structured source material, design direction, and visual assets into editable PowerPoint decks through a disciplined SVG-first pipeline: design strategy → hand-authored SVG pages → quality gates → native PPTX export with notes, media, transitions, and optional object animations.

<p align="center">
  <b>Source → Design Spec → SVG Pages → Quality Check → Native PPTX</b><br/>
  <sub>Beautiful enough for designers. Structured enough for agents. Editable enough for real business use.</sub>
</p>

---

## Table of contents

- [Why this exists](#why-this-exists)
- [Highlights](#highlights)
- [Repository layout](#repository-layout)
- [Demos included](#demos-included)
- [Quick start](#quick-start)
- [Run the included quick GIF demo](#run-the-included-quick-gif-demo)
- [Verify a generated PPTX](#verify-a-generated-pptx)
- [Install as a Hermes skill](#install-as-a-hermes-skill)
- [Create a new deck manually](#create-a-new-deck-manually)
- [Design philosophy](#design-philosophy)
- [Credits](#credits)
- [License](#license)
- [Security](#security)

---

## Why this exists

Most AI PPT tools stop at one of two unsatisfying outputs:

1. **Pretty screenshots** that are impossible to edit in PowerPoint.
2. **Editable but boring slides** limited by simple shape APIs.

Nuwa uses a different approach: **author the deck as high-fidelity SVG first, then export it to native PPTX**. This gives agents the freedom to design rich layouts while still producing a PowerPoint file that can be opened, edited, reviewed, and delivered.

This repository packages the `ppt-master` Hermes skill plus verified demo projects under the more memorable product name **Nuwa PPT Generation**.

---

## Highlights

- **SVG-first design system** — every slide is designed as a 16:9 SVG canvas before export.
- **Native PPTX export** — outputs real `.pptx` files, not just images.
- **Editable PowerPoint objects** — text, shapes, images, notes, transitions, and animations are written into OOXML.
- **High-design visual language** — supports dark tech, consulting, academic, brand, government, retro, and custom visual styles.
- **Quality gate before export** — checks viewBox, SVG compatibility, spec-lock drift, forbidden tags, fonts, and layout issues.
- **Speaker notes support** — `notes/total.md` is split into per-slide notes and embedded into the PPTX.
- **Animated GIF preservation** — with `--no-image-optimize`, real `.gif` media stays inside `ppt/media/`.
- **Page transitions + object animations** — supports PowerPoint transitions and per-element entrance effects via semantic `<g id="...">` groups.
- **Cross-platform guidance** — Windows and macOS usage notes are included in the skill.
- **Hermes-ready skill** — can be installed into Hermes Agent as a reusable productivity skill.

---

## Repository layout

```text
nuwa-ppt-generation/
├─ skills/productivity/ppt-master/     # Hermes skill: docs, scripts, templates, workflows
├─ demo-official-smoke/                # 5-page high-design demo with animated GIF + animations
├─ demo-quick-gif/                     # 1-page quick-mode GIF regression demo
├─ README.md                           # this file
├─ LICENSE                             # MIT license for this packaging repo
└─ .gitignore
```

The skill itself lives here:

```text
skills/productivity/ppt-master/SKILL.md
```

---

## Demos included

### 1. Official smoke demo — high-design animated deck

Final PPTX:

```text
demo-official-smoke/exports/official_smoke_20260630_234006.pptx
```

Verified properties:

```json
{
  "slides": 5,
  "notes_slides": 5,
  "has_gif_media": true,
  "has_transition_xml": true,
  "animation_effect_count": 25,
  "timing_sections": 5
}
```

Source artifacts:

```text
demo-official-smoke/design_spec.md
demo-official-smoke/spec_lock.md
demo-official-smoke/svg_output/*.svg
demo-official-smoke/notes/total.md
demo-official-smoke/images/dynamic_ai_orbit.gif
```

### 2. Quick GIF regression demo

Final PPTX:

```text
demo-quick-gif/exports/skill_patch_test_20260630_235721.pptx
```

Verified properties:

```json
{
  "slides": 1,
  "notes_slides": 1,
  "has_gif_media": true,
  "has_gif_content_type": true,
  "gif_relationships": 1,
  "has_transition_xml": true,
  "animation_effect_count": 3
}
```

This demo exists specifically to prove the animated-GIF rule: export with `--no-image-optimize`, then inspect the PPTX zip for `ppt/media/*.gif`.

---

## Quick start

### Windows / Git Bash

```bash
cd /d/AI/nuwa-ppt-generation
python -m venv .venv
. .venv/Scripts/activate
python -m pip install -U pip
python -m pip install -r skills/productivity/ppt-master/requirements.txt
```

### macOS / Linux

```bash
cd ~/AI/nuwa-ppt-generation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r skills/productivity/ppt-master/requirements.txt
```

Optional macOS dependencies for CairoSVG / compatibility raster preview:

```bash
brew install cairo pango gdk-pixbuf libffi
python -m pip install cairosvg
```

---

## Run the included quick GIF demo

```bash
cd /path/to/nuwa-ppt-generation
source .venv/bin/activate  # Windows Git Bash: . .venv/Scripts/activate

SKILL_DIR="$PWD/skills/productivity/ppt-master"
PROJECT="$PWD/demo-quick-gif"

python "$SKILL_DIR/scripts/svg_quality_checker.py" "$PROJECT"
python "$SKILL_DIR/scripts/total_md_split.py" "$PROJECT"
python "$SKILL_DIR/scripts/finalize_svg.py" "$PROJECT"
python "$SKILL_DIR/scripts/svg_to_pptx.py" "$PROJECT" \
  -t push --transition-duration 0.6 \
  -a auto --animation-trigger after-previous \
  --no-image-optimize
```

Why `--no-image-optimize`? Because animated GIFs must remain GIFs. Without it, image optimization may transcode them into static PNG/JPEG media.

---

## Verify a generated PPTX

A PPTX is a zip package. You can inspect it directly:

```python
from pathlib import Path
import zipfile, re, json

pptx = Path("demo-quick-gif/exports/skill_patch_test_20260630_235721.pptx")

with zipfile.ZipFile(pptx) as z:
    names = z.namelist()
    slides = [n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)]
    notes = [n for n in names if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)]
    media = [n for n in names if n.startswith("ppt/media/")]
    content = z.read("[Content_Types].xml").decode("utf-8", errors="replace")
    slide_xml = "\n".join(z.read(n).decode("utf-8", errors="replace") for n in slides)

print(json.dumps({
    "slides": len(slides),
    "notes_slides": len(notes),
    "media_files": media,
    "has_gif_media": any(n.lower().endswith(".gif") for n in media),
    "has_gif_content_type": "image/gif" in content or "Extension=\"gif\"" in content,
    "has_transition_xml": "<p:transition" in slide_xml,
    "animation_effect_count": slide_xml.count("<p:animEffect"),
}, indent=2))
```

---

## Install as a Hermes skill

Copy the skill folder into your Hermes skills directory.

### Windows

```bash
mkdir -p "$LOCALAPPDATA/hermes/skills/productivity"
cp -r skills/productivity/ppt-master "$LOCALAPPDATA/hermes/skills/productivity/"
```

### macOS / Linux

Depending on your Hermes profile setup, use one of:

```bash
mkdir -p ~/.hermes/skills/productivity
cp -r skills/productivity/ppt-master ~/.hermes/skills/productivity/
```

or your Hermes application support skills path.

Then start a fresh Hermes session and load/use:

```text
ppt-master
```

---

## Create a new deck manually

A project normally contains:

```text
my-project/
├─ design_spec.md
├─ spec_lock.md
├─ images/
├─ notes/total.md
├─ svg_output/*.svg
├─ svg_final/
└─ exports/
```

Minimum export sequence:

```bash
SKILL_DIR="/path/to/nuwa-ppt-generation/skills/productivity/ppt-master"
PROJECT="/path/to/my-project"

python "$SKILL_DIR/scripts/svg_quality_checker.py" "$PROJECT"
python "$SKILL_DIR/scripts/total_md_split.py" "$PROJECT"
python "$SKILL_DIR/scripts/finalize_svg.py" "$PROJECT"
python "$SKILL_DIR/scripts/svg_to_pptx.py" "$PROJECT"
```

With animation and GIF preservation:

```bash
python "$SKILL_DIR/scripts/svg_to_pptx.py" "$PROJECT" \
  -t push --transition-duration 0.6 \
  -a auto --animation-trigger after-previous \
  --no-image-optimize
```

---

## Design philosophy

Nuwa is built around a simple principle:

> **Slides are not documents with decoration. Slides are visual interfaces for decisions.**

That is why the pipeline keeps separate artifacts for:

- strategy (`design_spec.md`)
- execution lock (`spec_lock.md`)
- visual source (`svg_output/`)
- derived SVG snapshots (`svg_final/`)
- presenter logic (`notes/`)
- delivery package (`exports/*.pptx`)

This separation makes the system inspectable, repeatable, and repairable.

---

## Credits

This package is based on the excellent open-source `hugohe3/ppt-master` project and wraps it as a Hermes-ready, tested, demo-backed presentation-generation repository.

- Upstream: `hugohe3/ppt-master`
- Product/package name here: `nuwa-ppt-generation`
- Local skill name: `ppt-master`

---

## License

This packaging repository is released under the MIT License. Check upstream project files and dependencies for their respective licenses if you redistribute or embed them in another product.

---

## Security

Please report security issues privately — see [SECURITY.md](SECURITY.md) for the disclosure policy and reporting channels. Do not open public GitHub issues for vulnerabilities.
