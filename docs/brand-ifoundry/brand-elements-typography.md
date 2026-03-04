# iFoundry Media Typography

> Type that speaks with the precision of great engineering and the confidence of a team that ships.

## Strategic Foundation

**Brand Alignment:** iFoundry's typography embodies The Builder's directness and The Sage's authority. Space Grotesk brings geometric, technical precision with a modern, slightly unconventional character — the kind of typeface that signals engineering confidence without feeling cold. Its angular, monospaced-inspired letterforms align with the foundry's technical DNA while remaining warm enough for partnership-oriented communication. Strong weights carry the bold confidence of a team that builds.

## Primary Typeface

### Space Grotesk

**Rationale:** Space Grotesk is a proportional sans-serif evolved from Space Mono, carrying DNA from the monospaced world into a modern, geometric typeface. Its slightly technical character — angular terminals, geometric construction, and distinct letterforms — signals engineering expertise. It's contemporary without being trendy, technical without being cold, and bold without being aggressive. The perfect voice for a technology foundry.

| Attribute | Value |
|-----------|-------|
| Family | Space Grotesk |
| Classification | Geometric sans-serif |
| License | SIL Open Font License |
| Source | [Google Fonts](https://fonts.google.com/specimen/Space+Grotesk) |

### Weights

| Weight | Value | Token | Usage |
|--------|-------|-------|-------|
| Light | 300 | `--font-light` | Large display text, subtle emphasis |
| Regular | 400 | `--font-regular` | Body text, descriptions |
| Medium | 500 | `--font-medium` | UI elements, form labels, navigation |
| Semi-Bold | 600 | `--font-semibold` | Subheadings, active navigation |
| Bold | 700 | `--font-bold` | Headings, CTA buttons, hero text |

## Monospace Typeface

### JetBrains Mono

**Rationale:** For code blocks, technical documentation, terminal output, and data displays, JetBrains Mono is purpose-built for developer readability. Its increased x-height, programming ligatures, and clear character differentiation make it the ideal companion for a technology company. It reinforces iFoundry's engineering credibility in every code sample and technical context.

| Attribute | Value |
|-----------|-------|
| Family | JetBrains Mono |
| Classification | Monospace |
| License | SIL Open Font License |
| Source | [Google Fonts](https://fonts.google.com/specimen/JetBrains+Mono) |

### Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Code blocks, terminal output, data fields |
| Medium | 500 | Inline code, emphasis |
| Bold | 700 | Code headings, highlighted syntax |

## Type Scale

Based on a 1.25 ratio (Major Third) for clean, authoritative rhythm.

### Headings

| Level | Size | Weight | Line Height | Letter Spacing | Token |
|-------|------|--------|-------------|----------------|-------|
| Display | 4.5rem (72px) | 700 | 1.1 | -0.03em | `--text-display` |
| H1 | 3rem (48px) | 700 | 1.15 | -0.025em | `--text-h1` |
| H2 | 2.25rem (36px) | 700 | 1.2 | -0.02em | `--text-h2` |
| H3 | 1.75rem (28px) | 600 | 1.3 | -0.015em | `--text-h3` |
| H4 | 1.5rem (24px) | 600 | 1.35 | -0.01em | `--text-h4` |
| H5 | 1.25rem (20px) | 600 | 1.4 | 0 | `--text-h5` |
| H6 | 1.125rem (18px) | 600 | 1.4 | 0 | `--text-h6` |

### Body

| Style | Size | Weight | Line Height | Token |
|-------|------|--------|-------------|-------|
| Body Large | 1.125rem (18px) | 400 | 1.7 | `--text-lg` |
| Body | 1rem (16px) | 400 | 1.6 | `--text-base` |
| Body Small | 0.875rem (14px) | 400 | 1.5 | `--text-sm` |
| Caption | 0.75rem (12px) | 400 | 1.4 | `--text-xs` |

### Special Styles

| Style | Size | Weight | Usage |
|-------|------|--------|-------|
| Overline | 0.75rem | 600 | Section labels, uppercase, wide tracking (0.08em) |
| Tagline | 1.5rem | 500 | "Forged to perform." and similar brand phrases |
| Stat | 3rem | 700 | Key metrics, dashboard numbers, impact figures |
| Button | 1rem | 600 | CTA buttons, action labels |
| Label | 0.875rem | 500 | Form labels, field names |
| Link | inherit | 500 | Inline links, navigation text |
| Badge | 0.75rem | 600 | Status badges, tags, version numbers |
| Code Inline | 0.875rem | 500 | Inline code references (JetBrains Mono) |

## CSS Tokens

```css
:root {
  /* Font Families */
  --font-sans: 'Space Grotesk', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace;

  /* Font Sizes */
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.75rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  --text-6xl: 4.5rem;

  /* Font Weights */
  --font-light: 300;
  --font-regular: 400;
  --font-medium: 500;
  --font-semibold: 600;
  --font-bold: 700;

  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.15;
  --leading-snug: 1.35;
  --leading-normal: 1.5;
  --leading-relaxed: 1.6;
  --leading-loose: 1.7;

  /* Letter Spacing */
  --tracking-tighter: -0.03em;
  --tracking-tight: -0.02em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.08em;
}
```

## Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

## System Fallbacks

```css
/* Sans-serif fallback stack */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
             'Helvetica Neue', Arial, sans-serif;

/* Monospace fallback stack */
font-family: 'Fira Code', 'Consolas', 'Monaco', 'Courier New', monospace;
```

## Responsive Typography

### Fluid Scaling

| Viewport | Base Size | Scale Ratio |
|----------|-----------|-------------|
| Mobile (<640px) | 16px | 1.2 (Minor Third) |
| Tablet (640–1024px) | 16px | 1.225 |
| Desktop (>1024px) | 16px | 1.25 (Major Third) |

### Mobile Adjustments

| Style | Desktop | Mobile |
|-------|---------|--------|
| Display | 4.5rem (72px) | 2.5rem (40px) |
| H1 | 3rem (48px) | 2rem (32px) |
| H2 | 2.25rem (36px) | 1.5rem (24px) |
| H3 | 1.75rem (28px) | 1.375rem (22px) |
| Body | 1rem (16px) | 1rem (16px) |

### Fluid Type (CSS Clamp)

```css
.display {
  font-size: clamp(2.5rem, 5vw + 1rem, 4.5rem);
}

.h1 {
  font-size: clamp(2rem, 3vw + 1rem, 3rem);
}

.h2 {
  font-size: clamp(1.5rem, 2vw + 0.75rem, 2.25rem);
}
```

## Usage Guidelines

### Do
- Use Space Grotesk for all primary content and UI
- Establish clear hierarchy with size and weight differentiation
- Maintain consistent line height across similar content types
- Use JetBrains Mono for all code, terminal, and technical reference content
- Let headings breathe with generous top margins
- Use tight letter spacing on large headings for visual density and impact
- Use the Stat style for key metrics and impact numbers

### Don't
- Use more than 2 font families in any single view
- Set body text below 14px for sustained reading
- Stretch, compress, or artificially modify typefaces
- Use decorative or script fonts — they undermine the technical tone
- Skip heading levels (e.g., jump from H1 to H3)
- Use Light weight for body text — reserve it for large display contexts
- Mix Space Grotesk with other sans-serif fonts in the same layout

## Accessibility

- Minimum 16px for body text in reading contexts
- Maximum line length: 66 characters (approximately 600px at body size)
- Sufficient contrast for all text per WCAG AA (see Colors)
- Support browser zoom to 200% without layout breakage
- Proper heading hierarchy (H1 → H6) for screen reader navigation
- Avoid justified text — it creates uneven word spacing
- Ensure adequate line height (1.5+ for body) for readability

## Examples

### Hero Headline
```css
.hero-title {
  font-family: var(--font-sans);
  font-size: var(--text-6xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tighter);
  color: var(--color-primary-dark);
}
```

### Page Heading
```css
.page-heading {
  font-family: var(--font-sans);
  font-size: var(--text-5xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-tight);
  letter-spacing: var(--tracking-tight);
  color: var(--color-primary-dark);
}
```

### Body Text
```css
.body {
  font-family: var(--font-sans);
  font-size: var(--text-base);
  font-weight: var(--font-regular);
  line-height: var(--leading-relaxed);
  color: var(--color-slate-600);
}
```

### Code Block
```css
.code-block {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: var(--font-regular);
  line-height: var(--leading-relaxed);
  color: var(--color-slate-200);
  background: var(--color-slate-900);
  padding: var(--space-4);
  border-radius: var(--radius-md);
}
```

### Stat / Metric
```css
.stat {
  font-family: var(--font-sans);
  font-size: var(--text-5xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tight);
  color: var(--color-primary);
}
```
