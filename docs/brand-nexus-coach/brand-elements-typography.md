# Nexus Coach Typography

> Type that speaks with calm confidence — organized, clear, and human.

## Strategic Foundation

**Brand Alignment:** Nexus Coach's typography embodies the Guide archetype — approachable, authoritative, and clear. Plus Jakarta Sans brings geometric precision (The Architect) with warm, open letterforms (The Guide). The type system communicates that coaching is both structured and deeply human. Strong weights convey confidence without shouting, while generous spacing reflects the breathing room a well-organized practice provides.

## Primary Typeface

### Plus Jakarta Sans

**Rationale:** Plus Jakarta Sans is a modern geometric sans-serif with warm, open letterforms that balance professionalism with approachability. Its slightly rounded terminals soften what could feel corporate, while its geometric structure communicates the operational precision of a well-run practice. The weight range supports clear hierarchy, and its contemporary design signals modern software without alienating non-technical coaches.

| Attribute | Value |
|-----------|-------|
| Family | Plus Jakarta Sans |
| Classification | Geometric sans-serif |
| License | SIL Open Font License |
| Source | [Google Fonts](https://fonts.google.com/specimen/Plus+Jakarta+Sans) |

### Weights

| Weight | Value | Token | Usage |
|--------|-------|-------|-------|
| Light | 300 | `--font-light` | Large display text, subtle emphasis |
| Regular | 400 | `--font-regular` | Body text, descriptions |
| Medium | 500 | `--font-medium` | UI elements, form labels, navigation |
| Semi-Bold | 600 | `--font-semibold` | Subheadings, active navigation |
| Bold | 700 | `--font-bold` | Headings, CTA buttons |
| Extra-Bold | 800 | `--font-extrabold` | Hero headlines, marketing display |

## Monospace Typeface

### IBM Plex Mono

**Rationale:** For code snippets, data tables, and technical content, IBM Plex Mono offers clear character differentiation and a structured, professional appearance that complements Plus Jakarta Sans's geometric nature. Its slightly humanist touch keeps technical content feeling approachable.

| Attribute | Value |
|-----------|-------|
| Family | IBM Plex Mono |
| Classification | Monospace |
| License | SIL Open Font License |
| Source | [Google Fonts](https://fonts.google.com/specimen/IBM+Plex+Mono) |

### Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Code blocks, data fields |
| Medium | 500 | Inline code, emphasis |
| Semi-Bold | 600 | Code headings, API references |

## Type Scale

Based on a 1.25 ratio (Major Third) for clean, harmonious rhythm.

### Headings

| Level | Size | Weight | Line Height | Letter Spacing | Token |
|-------|------|--------|-------------|----------------|-------|
| Display | 4.5rem (72px) | 800 | 1.1 | -0.025em | `--text-display` |
| H1 | 3rem (48px) | 700 | 1.2 | -0.02em | `--text-h1` |
| H2 | 2.25rem (36px) | 700 | 1.25 | -0.015em | `--text-h2` |
| H3 | 1.75rem (28px) | 600 | 1.3 | -0.01em | `--text-h3` |
| H4 | 1.5rem (24px) | 600 | 1.35 | 0 | `--text-h4` |
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
| Overline | 0.75rem | 600 | Section labels, uppercase, wide tracking |
| Quote | 1.5rem | 400 italic | Testimonials, client quotes, pull quotes |
| Stat | 3rem | 700 | Key metrics, dashboard numbers |
| Button | 1rem | 600 | CTA buttons, action labels |
| Label | 0.875rem | 500 | Form labels, field names |
| Link | inherit | 500 | Inline links, navigation text |
| Badge | 0.75rem | 600 | Status badges, tags, counts |

## CSS Tokens

```css
:root {
  /* Font Families */
  --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'IBM Plex Mono', 'Fira Code', 'Consolas', monospace;

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
  --font-extrabold: 800;

  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.2;
  --leading-snug: 1.35;
  --leading-normal: 1.5;
  --leading-relaxed: 1.6;
  --leading-loose: 1.7;

  /* Letter Spacing */
  --tracking-tighter: -0.025em;
  --tracking-tight: -0.02em;
  --tracking-normal: 0;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
}
```

## Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

## System Fallbacks

```css
/* Sans-serif fallback stack */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
             'Helvetica Neue', Arial, sans-serif;

/* Monospace fallback stack */
font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
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
- Use Plus Jakarta Sans for all primary content and UI
- Establish clear hierarchy with size and weight differentiation
- Maintain consistent line height across similar content types
- Use IBM Plex Mono only for code, data, or technical reference content
- Let headings breathe with generous top margins
- Use the Body Large style for lead paragraphs and featured descriptions
- Keep dashboard metrics in the Stat style for scanability

### Don't
- Use more than 2 font families in any single view
- Set body text below 14px for sustained reading
- Stretch, compress, or artificially modify typefaces
- Use decorative or script fonts — they undermine the professional tone
- Skip heading levels (e.g., jump from H1 to H3)
- Use Light weight for body text — reserve it for large display contexts
- Over-use Extra-Bold — it's for hero moments, not everyday headings

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
  font-weight: var(--font-extrabold);
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

### Dashboard Stat
```css
.stat-value {
  font-family: var(--font-sans);
  font-size: var(--text-5xl);
  font-weight: var(--font-bold);
  line-height: var(--leading-none);
  letter-spacing: var(--tracking-tight);
  color: var(--color-primary);
}
```

### Code Block
```css
.code {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  font-weight: var(--font-regular);
  line-height: var(--leading-normal);
  background: var(--color-slate-100);
  padding: var(--space-4);
  border-radius: var(--radius-md);
  color: var(--color-slate-800);
}
```

### Navigation Label
```css
.nav-label {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: var(--leading-normal);
  letter-spacing: var(--tracking-normal);
}
```
