# SpikeForge Colors

> A trust-first palette with premium contrast and calm energy.

## Strategic Foundation

SpikeForge uses a light, editorial base with confident deep anchors. The palette is designed to feel clear and reliable in day-to-day operations, with selective high-energy moments for action and momentum.

## Core Palette

### Midnight Ink
Primary structural color for headers, navigation, and high-emphasis text.

| Format | Value |
|--------|-------|
| HEX | `#0B1220` |
| RGB | `rgb(11, 18, 32)` |
| Token | `--color-ink-900` |

### Cloud Surface
Primary application background.

| Format | Value |
|--------|-------|
| HEX | `#F6F8FC` |
| RGB | `rgb(246, 248, 252)` |
| Token | `--color-surface-50` |

### Paper White
Card and content surface.

| Format | Value |
|--------|-------|
| HEX | `#FFFFFF` |
| RGB | `rgb(255, 255, 255)` |
| Token | `--color-white` |

### Cobalt Signal
Primary action color.

| Format | Value |
|--------|-------|
| HEX | `#2E5BFF` |
| RGB | `rgb(46, 91, 255)` |
| Token | `--color-primary` |

### Teal Trust
Secondary accent for product confidence and positive intent.

| Format | Value |
|--------|-------|
| HEX | `#0E9384` |
| RGB | `rgb(14, 147, 132)` |
| Token | `--color-teal-600` |

### Amber Momentum
Attention and emphasis color for high-priority prompts.

| Format | Value |
|--------|-------|
| HEX | `#F59E0B` |
| RGB | `rgb(245, 158, 11)` |
| Token | `--color-amber-500` |

## Neutral Scale

| Name | HEX | Token |
|------|-----|-------|
| Ink 900 | `#0B1220` | `--color-ink-900` |
| Ink 800 | `#1A2438` | `--color-ink-800` |
| Ink 700 | `#2B3752` | `--color-ink-700` |
| Ink 600 | `#415170` | `--color-ink-600` |
| Ink 500 | `#5B6C8D` | `--color-ink-500` |
| Ink 400 | `#8090AC` | `--color-ink-400` |
| Ink 300 | `#A9B4C8` | `--color-ink-300` |
| Ink 200 | `#D5DCE8` | `--color-ink-200` |
| Ink 100 | `#E9EEF5` | `--color-ink-100` |
| Surface 50 | `#F6F8FC` | `--color-surface-50` |

## Semantic Colors

| State | Base | Surface |
|-------|------|---------|
| Success | `#0F9F6E` | `#DFF7EC` |
| Warning | `#D18A00` | `#FFF4D9` |
| Error | `#D92D20` | `#FEE4E2` |
| Info | `#1D4ED8` | `#E4ECFF` |

## Gradient System

Use gradients sparingly for hero zones, data storytelling cards, and campaign moments.

```css
--gradient-brand: linear-gradient(135deg, #2E5BFF 0%, #0E9384 55%, #7BD8CB 100%);
--gradient-ink: linear-gradient(160deg, #0B1220 0%, #1A2438 100%);
--gradient-soft: linear-gradient(180deg, #FFFFFF 0%, #F6F8FC 100%);
```

## Application Rules

1. Light-first canvases: default app screens use `--color-surface-50` + white cards.
2. Dark anchors: use `--color-ink-900` for side nav, utility bands, and footer zones.
3. One primary action per view: reserve cobalt for dominant action intent.
4. Metrics hierarchy: neutral text + one semantic or brand accent per metric block.
5. Gradients are directional: use only in hero or sectional emphasis, never as body background.

## Accessibility Baseline

- Primary text on white: minimum 7:1 preferred.
- Interactive controls: minimum 4.5:1.
- Non-text indicators: minimum 3:1.
- Never use color as the sole status signal.

## CSS Tokens

```css
:root {
  --color-ink-900: #0B1220;
  --color-ink-800: #1A2438;
  --color-ink-700: #2B3752;
  --color-ink-600: #415170;
  --color-ink-500: #5B6C8D;
  --color-ink-400: #8090AC;
  --color-ink-300: #A9B4C8;
  --color-ink-200: #D5DCE8;
  --color-ink-100: #E9EEF5;

  --color-surface-50: #F6F8FC;
  --color-white: #FFFFFF;

  --color-primary: #2E5BFF;
  --color-primary-700: #2448CF;
  --color-primary-100: #E4ECFF;

  --color-teal-600: #0E9384;
  --color-teal-100: #DCF6F2;

  --color-amber-500: #F59E0B;
  --color-amber-100: #FFF4D9;

  --color-success: #0F9F6E;
  --color-success-100: #DFF7EC;
  --color-warning: #D18A00;
  --color-warning-100: #FFF4D9;
  --color-error: #D92D20;
  --color-error-100: #FEE4E2;
  --color-info: #1D4ED8;
  --color-info-100: #E4ECFF;
}
```
