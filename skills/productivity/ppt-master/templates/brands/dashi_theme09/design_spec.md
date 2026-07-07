---
brand_id: dashi_theme09
kind: brand
summary: 深蓝杂志风 (deep-blue-magazine) — 品牌故事 等
primary_color: "#165FE7"
provenance: |
  Inspired by dashiAI-ppt theme09 "深蓝杂志风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme09/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 深蓝杂志风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme09` |
| Display Name | 深蓝杂志风 |
| Use Cases | 品牌故事、人物访谈、企业形象册、深度专题 |
| Target Audience | 公关团队、媒体编辑、创始人、企业品牌部 |
| Tone | editorial-narrative, brand-story, magazine-cover |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#165FE7` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#f5f7fb` | Body text on light bg / light text on dark bg |
| bg | `#070d22` | Page background |
| surface | `#0c1430` | Card / panel background |
| accent (info) | `#3f78ff` | Process / flow / interactive elements |
| accent (positive) | `#1fb89b` | Success / recommended / KPI green |
| accent (alert) | `#e56b6b` | Risk / caution / warning |
| border | `#1a2350` | Card borders, dividers |
| muted-text | `#8a95b8` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Inter", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Inter", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
| mono (code / metrics) | "JetBrains Mono", "Consolas", monospace | 400–500 |

> Any proprietary faces from the source theme have been mapped to open-source equivalents. If the deck must ship on a viewer machine without these installed, the `Helvetica Neue` → `Arial` / `Microsoft YaHei` fallback chain kicks in. For guaranteed fidelity, embed the fonts into the PPTX at export.

## IV. Logo

Brand presets do not carry logos. When a deck using this style needs a client / product logo, place it via §VIII of `design_spec.md` and follow the source brand's logo guidelines.

## V. Voice & Tone

- Formality: professional-neutral
- Person: we / you (English), 我们 / 你 (Chinese)
- Emoji: avoid
- Abbreviations: spell-out-first-use

## VI. Icon Style

- Preference: stroke

> Outline / stroke icons read as "research / engineering" — prefer `tabler` or `lucide` stroke families from `templates/icons/`.
