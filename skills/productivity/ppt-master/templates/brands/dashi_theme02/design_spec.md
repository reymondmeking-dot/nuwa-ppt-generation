---
brand_id: dashi_theme02
kind: brand
summary: 炫光紫绿风 (glow-purple-green) — 科技发布会 等
primary_color: "#2fe07f"
provenance: |
  Inspired by dashiAI-ppt theme02 "炫光紫绿风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme02/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 炫光紫绿风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme02` |
| Display Name | 炫光紫绿风 |
| Use Cases | 科技发布会、AI/自动驾驶/机器人主题、增长故事、创新项目展示 |
| Target Audience | 科技公司创始人、技术负责人、品牌市场团队、投资路演团队 |
| Tone | cinematic, tech-forward, high-energy |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#2fe07f` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#f5f7fa` | Body text on light bg / light text on dark bg |
| bg | `#0a0a1e` | Page background |
| surface | `#141433` | Card / panel background |
| accent (info) | `#a17bff` | Process / flow / interactive elements |
| accent (positive) | `#2fe07f` | Success / recommended / KPI green |
| accent (alert) | `#ff6b6b` | Risk / caution / warning |
| border | `#2a2a4a` | Card borders, dividers |
| muted-text | `#8888a8` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Space Grotesk", "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Space Grotesk", "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
| mono (code / metrics) | "Space Mono", "JetBrains Mono", "Consolas", monospace | 400–500 |

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
