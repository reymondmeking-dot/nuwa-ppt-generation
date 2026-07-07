---
brand_id: dashi_theme08
kind: brand
summary: 黑金实验风 (black-gold-lab) — 高端发布 等
primary_color: "#c96442"
provenance: |
  Inspired by dashiAI-ppt theme08 "黑金实验风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme08/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 黑金实验风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme08` |
| Display Name | 黑金实验风 |
| Use Cases | 高端发布、品牌提案、实验性概念、奢华科技叙事 |
| Target Audience | 高端品牌、创意总监、科技品牌、发布会策划团队 |
| Tone | editorial-luxury, understated, cinematic |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#c96442` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#f5efe0` | Body text on light bg / light text on dark bg |
| bg | `#0a0a0a` | Page background |
| surface | `#1a1512` | Card / panel background |
| accent (info) | `#c96442` | Process / flow / interactive elements |
| accent (positive) | `#d4a952` | Success / recommended / KPI green |
| accent (alert) | `#b3261e` | Risk / caution / warning |
| border | `#2a2018` | Card borders, dividers |
| muted-text | `#8a7f70` | Secondary text, chart labels |

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
