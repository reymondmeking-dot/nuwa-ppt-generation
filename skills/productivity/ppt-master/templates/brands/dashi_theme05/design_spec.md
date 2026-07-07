---
brand_id: dashi_theme05
kind: brand
summary: 色谱图表风 (chart-spectrum) — 数据报告 等
primary_color: "#2742C2"
provenance: |
  Inspired by dashiAI-ppt theme05 "色谱图表风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme05/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 色谱图表风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme05` |
| Display Name | 色谱图表风 |
| Use Cases | 数据报告、市场分析、KPI 复盘、行业研究 |
| Target Audience | 数据分析师、咨询顾问、研究员、业务负责人 |
| Tone | analytical, data-forward, consulting-neutral |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#2742C2` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#14130f` | Body text on light bg / light text on dark bg |
| bg | `#fafaf5` | Page background |
| surface | `#ffffff` | Card / panel background |
| accent (info) | `#2742C2` | Process / flow / interactive elements |
| accent (positive) | `#2F9450` | Success / recommended / KPI green |
| accent (alert) | `#c94a3e` | Risk / caution / warning |
| border | `#e5e3d8` | Card borders, dividers |
| muted-text | `#5b584f` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Noto Sans SC", "Hiragino Sans GB", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Noto Sans SC", "Hiragino Sans GB", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
| mono (code / metrics) | "JetBrains Mono", "Space Mono", "Consolas", monospace | 400–500 |

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
