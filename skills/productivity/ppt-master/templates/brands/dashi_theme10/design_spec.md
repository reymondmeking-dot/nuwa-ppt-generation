---
brand_id: dashi_theme10
kind: brand
summary: 金色指数风 (golden-index) — 金融数据 等
primary_color: "#d8a85b"
provenance: |
  Inspired by dashiAI-ppt theme10 "金色指数风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme10/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 金色指数风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme10` |
| Display Name | 金色指数风 |
| Use Cases | 金融数据、投资报告、商业指数、年度榜单 |
| Target Audience | 投资机构、金融分析师、咨询公司、商业媒体 |
| Tone | financial-authority, index-annual, ranking-formal |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#d8a85b` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#1a1815` | Body text on light bg / light text on dark bg |
| bg | `#fbf8f0` | Page background |
| surface | `#ffffff` | Card / panel background |
| accent (info) | `#4f7ff0` | Process / flow / interactive elements |
| accent (positive) | `#16b88c` | Success / recommended / KPI green |
| accent (alert) | `#d27d58` | Risk / caution / warning |
| border | `#e8dcc0` | Card borders, dividers |
| muted-text | `#7e7669` | Secondary text, chart labels |

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
