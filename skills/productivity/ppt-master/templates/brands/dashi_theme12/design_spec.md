---
brand_id: dashi_theme12
kind: brand
summary: 声波霓虹风 (soundwave-neon) — 音乐娱乐 等
primary_color: "#3bb6ec"
provenance: |
  Inspired by dashiAI-ppt theme12 "声波霓虹风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme12/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 声波霓虹风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme12` |
| Display Name | 声波霓虹风 |
| Use Cases | 音乐娱乐、潮流活动、直播内容、年轻化发布 |
| Target Audience | 娱乐品牌、活动策划、内容团队、潮流消费品牌 |
| Tone | youth-culture, event-poster, kinetic |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#3bb6ec` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#f0f4f8` | Body text on light bg / light text on dark bg |
| bg | `#1b1518` | Page background |
| surface | `#2a2024` | Card / panel background |
| accent (info) | `#3bb6ec` | Process / flow / interactive elements |
| accent (positive) | `#7ce38b` | Success / recommended / KPI green |
| accent (alert) | `#ff6b9a` | Risk / caution / warning |
| border | `#3a2f34` | Card borders, dividers |
| muted-text | `#8a7f85` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
| mono (code / metrics) | "Space Mono", "JetBrains Mono", "Consolas", monospace | 400–500 |

> Any proprietary faces from the source theme have been mapped to open-source equivalents. If the deck must ship on a viewer machine without these installed, the `Helvetica Neue` → `Arial` / `Microsoft YaHei` fallback chain kicks in. For guaranteed fidelity, embed the fonts into the PPTX at export.

## IV. Logo

Brand presets do not carry logos. When a deck using this style needs a client / product logo, place it via §VIII of `design_spec.md` and follow the source brand's logo guidelines.

## V. Voice & Tone

- Formality: professional-neutral
- Person: we / you (English), 我们 / 你 (Chinese)
- Emoji: sparingly OK (kinetic style)
- Abbreviations: spell-out-first-use

## VI. Icon Style

- Preference: filled

> Filled icons match the style's warmth / expression — prefer `tabler-filled` or `lucide` filled variants.
