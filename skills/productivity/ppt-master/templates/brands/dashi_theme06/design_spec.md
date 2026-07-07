---
brand_id: dashi_theme06
kind: brand
summary: 深色图谱风 (dark-atlas) — 高密度数据展示 等
primary_color: "#c8f135"
provenance: |
  Inspired by dashiAI-ppt theme06 "深色图谱风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme06/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 深色图谱风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme06` |
| Display Name | 深色图谱风 |
| Use Cases | 高密度数据展示、战略分析、科技/金融/产业报告 |
| Target Audience | 战略团队、投资人、产业研究团队、高管汇报者 |
| Tone | high-density, strategic, executive-briefing |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#c8f135` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#f5f5f5` | Body text on light bg / light text on dark bg |
| bg | `#0d0d0d` | Page background |
| surface | `#1a1a1a` | Card / panel background |
| accent (info) | `#3ca0ff` | Process / flow / interactive elements |
| accent (positive) | `#c8f135` | Success / recommended / KPI green |
| accent (alert) | `#ff5a3c` | Risk / caution / warning |
| border | `#2a2a2a` | Card borders, dividers |
| muted-text | `#888888` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Archivo", "Inter", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Archivo", "Inter", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
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
