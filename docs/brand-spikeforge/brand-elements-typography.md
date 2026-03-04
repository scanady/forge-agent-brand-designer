# SpikeForge Typography

> Editorial clarity plus product precision.

## Strategic Foundation

SpikeForge typography blends mission-grade readability with enterprise product clarity: expressive headlines, disciplined UI text, and practical data typography.

## Typeface System

### Primary UI Typeface: Manrope

A geometric sans-serif for product interfaces with excellent clarity at dashboard sizes.

| Attribute | Value |
|-----------|-------|
| Family | Manrope |
| Use | Navigation, forms, tables, buttons, body |
| Weights | 400, 500, 600, 700, 800 |

### Editorial Display Typeface: Instrument Serif

Used selectively for campaign and narrative headlines.

| Attribute | Value |
|-----------|-------|
| Family | Instrument Serif |
| Use | Marketing hero headlines, testimonial pull quotes |
| Weights | 400 |

### Monospace Typeface: IBM Plex Mono

For numerical density and technical values.

| Attribute | Value |
|-----------|-------|
| Family | IBM Plex Mono |
| Use | Metrics, IDs, code, compact system labels |
| Weights | 400, 500, 600 |

## Type Scale

### Product UI Scale

| Style | Size | Weight | Line Height | Token |
|-------|------|--------|-------------|-------|
| Display XL | 64px | 800 | 1.08 | `--text-display-xl` |
| Display L | 52px | 800 | 1.1 | `--text-display-l` |
| H1 | 40px | 700 | 1.15 | `--text-h1` |
| H2 | 32px | 700 | 1.2 | `--text-h2` |
| H3 | 26px | 700 | 1.25 | `--text-h3` |
| H4 | 22px | 600 | 1.3 | `--text-h4` |
| Body L | 18px | 500 | 1.6 | `--text-lg` |
| Body M | 16px | 500 | 1.6 | `--text-base` |
| Body S | 14px | 500 | 1.5 | `--text-sm` |
| Caption | 12px | 600 | 1.4 | `--text-xs` |

### Data and Metric Scale

| Style | Size | Weight | Family | Use |
|-------|------|--------|--------|-----|
| Metric XL | 48px | 700 | Manrope | Dashboard hero KPI |
| Metric L | 36px | 700 | Manrope | Section KPI |
| Metric M | 28px | 700 | Manrope | Card metrics |
| Data Label | 11px | 600 | IBM Plex Mono | Axis labels, compact tags |

## Typographic Behavior

1. Headlines are concise and high-contrast.
2. Body copy avoids long blocks in product views.
3. Metric text uses tighter tracking and stronger weight.
4. Serif is reserved for moments of narrative emphasis.

## Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

## CSS Tokens

```css
:root {
  --font-ui: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-display: 'Instrument Serif', Georgia, 'Times New Roman', serif;
  --font-mono: 'IBM Plex Mono', 'SFMono-Regular', Consolas, monospace;

  --text-display-xl: 4rem;
  --text-display-l: 3.25rem;
  --text-h1: 2.5rem;
  --text-h2: 2rem;
  --text-h3: 1.625rem;
  --text-h4: 1.375rem;
  --text-lg: 1.125rem;
  --text-base: 1rem;
  --text-sm: 0.875rem;
  --text-xs: 0.75rem;

  --font-regular: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;
  --font-extrabold: 800;
}
```

## Accessibility

- Minimum product body size: 16px on desktop, 15px on compact surfaces only.
- Line length target: 50-75 characters.
- Avoid all-caps body labels except compact overlines.
- Preserve semantic heading order for assistive technologies.

## Usage Guidelines

### Do
- Use Manrope for all core product UI.
- Use Instrument Serif sparingly for brand storytelling moments.
- Use IBM Plex Mono for dense data labels and IDs.
- Keep metric typography strong and legible.

### Don't
- Mix multiple display styles in the same hero region.
- Use serif for dense dashboard UI.
- Drop body text below 14px.
- Use lightweight text on low-contrast surfaces.
