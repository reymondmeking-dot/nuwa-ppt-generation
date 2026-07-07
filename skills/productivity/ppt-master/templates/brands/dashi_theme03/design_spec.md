---
brand_id: dashi_theme03
kind: brand
summary: 深浅代码风 (dev-terminal) — 技术方案 等
primary_color: "#2742ec"
provenance: |
  Inspired by dashiAI-ppt theme03 "深浅代码风" use-case bucket (public README).
  Color anchors sampled from the public source tree at
  chuspeeism/dashiAI-ppt-skill/project/src/components/themes/theme03/source/.
  Proprietary fonts (Perplexity, LIANTONG GROUP, INTERCONNECT) are replaced with
  open-source fallbacks (Inter, Space Grotesk, Archivo). No verbatim SVG/JSX assets
  are reproduced here — this preset is an identity segment (color / typography /
  voice / icon style) only, per ppt-master brand-kind contract.
---

# 深浅代码风 — Brand Specification

> Identity-only preset. No SVG page roster — pages are composed freely under these constraints.

## I. Brand Overview

| Property | Value |
|---|---|
| Style ID | `dashi_theme03` |
| Display Name | 深浅代码风 |
| Use Cases | 技术方案、开发者大会、系统架构、AI 工程实践 |
| Target Audience | 工程师、技术管理者、架构师、开发者社区 |
| Tone | engineering-precise, conclusion-first, no fluff |

## II. Color Scheme

| Role | HEX | Notes |
|---|---|---|
| primary | `#2742ec` | Signature accent — headings, key marks, chart primaries |
| neutral-dark | `#1a1916` | Body text on light bg / light text on dark bg |
| bg | `#f4f1eb` | Page background |
| surface | `#ffffff` | Card / panel background |
| accent (info) | `#2742ec` | Process / flow / interactive elements |
| accent (positive) | `#0d8a3e` | Success / recommended / KPI green |
| accent (alert) | `#c94a3e` | Risk / caution / warning |
| border | `#e4dfd4` | Card borders, dividers |
| muted-text | `#5c5b57` | Secondary text, chart labels |

Strategist may rotate accent dominance per page while keeping `primary` and `neutral-dark` stable across the deck.

## III. Typography

| Role | Family | Weight |
|---|---|---|
| title | "Archivo", "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 600–700 |
| body | "Archivo", "Noto Sans SC", "Helvetica Neue", Arial, "Microsoft YaHei", sans-serif | 400 |
| mono (code / metrics) | "Space Mono", "SF Mono", "JetBrains Mono", "Consolas", monospace | 400–500 |

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
