# design_spec.md — official_smoke

## I. Project Brief
- Project: PPT Master 官方测试 / High-design dynamic deck
- Canvas: PPT 16:9, 1280×720
- Audience: AI 产品 / 设计 / 技术演示观众
- Style: 深色高级科技感、霓虹渐变、玻璃拟态、清晰信息层级

## II. Deck Outline
1. Cover — 动态主视觉与标题
2. System — SVG 到原生 PPTX 的生成架构
3. Motion — 页面级转场与对象级动画验证
4. Quality — 导出链路和可编辑性验证
5. Close — 输出路径和复用方式

## III. Color Scheme
- Background: #050816
- Secondary background: #0B1026
- Surface: #101A3F
- Primary: #00E5FF
- Accent: #7C3AED
- Secondary accent: #FF2E88
- Body text: #EAF2FF
- Muted text: #8DA2C0

## IV. Typography
- Font stack: "Microsoft YaHei", "Arial", sans-serif
- Title: 52–76 px
- Heading: 30–42 px
- Body: 20–24 px
- Label: 14–16 px

## V. Image Resource List
| ID | Filename | Type | Acquire Via | Status | Usage |
|---|---|---|---|---|---|
| hero_dynamic | dynamic_ai_orbit.gif | Animated GIF / dynamic image | generated locally | Generated | Cover hero background and motion evidence |
| hero_poster | dynamic_ai_orbit_poster.jpg | Static fallback | generated locally | Generated | fallback poster |

## VI. Animation Plan
- Page transition: push, 0.6s
- Element animation: auto, after-previous cascade
- Top-level semantic groups: title, hero, cards, pipeline, metrics, closing
