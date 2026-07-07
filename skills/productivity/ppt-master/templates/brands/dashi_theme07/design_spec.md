---
brand_id: dashi_theme07
kind: brand
summary: 冷白调研风 (cool-white-research) — 调研报告 等
primary_color: "#2F7BFF"
provenance: |
  Inspired by dashiAI-ppt theme07 "冷白调研风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme07/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 冷白调研风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme07` |
| Display Name | 冷白调研风 |
| Use Cases | 调研报告、白皮书、竞品分析、学术/政策型表达 |
| Target Audience | 研究机构、咨询团队、政府/高校/智库、B2B 团队 |
| Tone | whitepaper-formal, evidence-first, institutional |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#2F7BFF` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#0D100A` | Body text on light bg / light text on dark bg |
| bg | `#ffffff` | Page background |
| surface | `#f7f8fa` | Card / panel background |
| accent (info) | `#2F7BFF` | Process / flow / interactive elements |
| accent (positive) | `#34B24A` | Success / recommended / KPI green |
| accent (alert) | `#e05a3e` | Risk / caution / warning |
| border | `#e4e6ec` | Card borders, dividers |
| muted-text | `#83877C` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Space Grotesk", "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Space Grotesk", "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
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
