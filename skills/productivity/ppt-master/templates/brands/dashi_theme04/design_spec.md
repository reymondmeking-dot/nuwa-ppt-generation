---
brand_id: dashi_theme04
kind: brand
summary: 玻璃糖果风 (glass-candy) — 年轻化品牌 等
primary_color: "#FF9FE2"
provenance: |
  Inspired by dashiAI-ppt theme04 "玻璃糖果风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme04/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 玻璃糖果风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme04` |
| Display Name | 玻璃糖果风 |
| Use Cases | 年轻化品牌、消费产品、创意提案、社媒感内容 |
| Target Audience | 品牌团队、设计师、内容创作者、消费品团队 |
| Tone | playful, warm, expressive-yet-clean |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#FF9FE2` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#2a2a2a` | Body text on light bg / light text on dark bg |
| bg | `#fdf6ff` | Page background |
| surface | `#ffffff` | Card / panel background |
| accent (info) | `#15A7F0` | Process / flow / interactive elements |
| accent (positive) | `#27E021` | Success / recommended / KPI green |
| accent (alert) | `#FF5A5A` | Risk / caution / warning |
| border | `#f0dfef` | Card borders, dividers |
| muted-text | `#8a8f98` | Secondary text, chart labels |

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
- Emoji: sparingly OK (kinetic style)
- Abbreviations: spell-out-first-use

## VI. Icon Style

- Preference: filled

> Filled icons match the style's warmth / expression — prefer `tabler-filled` or `lucide` filled variants.
