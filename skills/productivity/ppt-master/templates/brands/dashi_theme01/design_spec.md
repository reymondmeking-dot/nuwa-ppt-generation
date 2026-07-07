---
brand_id: dashi_theme01
kind: brand
summary: 轻拟态风 (soft-neumorphic) — 产品介绍 等
primary_color: "#5b8def"
provenance: |
  Inspired by dashiAI-ppt theme01 "轻拟态风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme01/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 轻拟态风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme01` |
| Display Name | 轻拟态风 |
| Use Cases | 产品介绍、企业汇报、方案说明、轻量级发布 |
| Target Audience | 创业团队、产品经理、销售顾问、企业内部汇报者 |
| Tone | restrained, product-first, conversational-professional |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#5b8def` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#2b2b30` | Body text on light bg / light text on dark bg |
| bg | `#f6f7fb` | Page background |
| surface | `#ffffff` | Card / panel background |
| accent (info) | `#5b8def` | Process / flow / interactive elements |
| accent (positive) | `#46b083` | Success / recommended / KPI green |
| accent (alert) | `#e56b5a` | Risk / caution / warning |
| border | `#e2e4ec` | Card borders, dividers |
| muted-text | `#7e7f8a` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Noto Sans SC", "Inter", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Noto Sans SC", "Inter", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
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
