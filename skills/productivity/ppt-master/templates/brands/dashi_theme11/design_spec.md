---
brand_id: dashi_theme11
kind: brand
summary: 高能增长风 (high-energy-growth) — 增长复盘 等
primary_color: "#ff6a2b"
provenance: |
  Inspired by dashiAI-ppt theme11 "高能增长风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme11/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 高能增长风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme11` |
| Display Name | 高能增长风 |
| Use Cases | 增长复盘、商业计划、融资路演、市场扩张方案 |
| Target Audience | 创业者、增长团队、销售团队、VC/PE 路演团队 |
| Tone | pitch-deck, growth-story, momentum-forward |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#ff6a2b` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#1a1512` | Body text on light bg / light text on dark bg |
| bg | `#faf6ef` | Page background |
| surface | `#ffffff` | Card / panel background |
| accent (info) | `#2742ec` | Process / flow / interactive elements |
| accent (positive) | `#0dbf67` | Success / recommended / KPI green |
| accent (alert) | `#e5342e` | Risk / caution / warning |
| border | `#e8dccb` | Card borders, dividers |
| muted-text | `#7a6f60` | Secondary text, chart labels |

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

- Preference: filled

> Filled icons match the style's warmth / expression — prefer `tabler-filled` or `lucide` filled variants.
