# OpenLife Typography

> Type that speaks with confident clarity—technically credible without being cold.

## Strategic Foundation

**Brand Alignment:** OpenLife's typography embodies our voice: confident, clear, and refreshingly direct. The type system balances technical credibility with approachability. Clean, open letterforms reflect transparency, while strong weights convey the conviction of The Liberator archetype.

## Primary Typeface

### Inter

**Rationale:** Inter was designed for screens, embodying OpenLife's technology-forward identity. Its open letterforms communicate clarity, the weight range supports hierarchy, and its adoption in modern tech signals innovation without alienating enterprise audiences.

| Attribute | Value |
|-----------|-------|
| Family | Inter |
| Classification | Neo-grotesque sans-serif |
| License | SIL Open Font License |
| Source | [Google Fonts](https://fonts.google.com/specimen/Inter) |

### Weights

| Weight | Value | Token | Usage |
|--------|-------|-------|-------|
| Light | 300 | `--font-light` | Large display, subtle |
| Regular | 400 | `--font-regular` | Body text |
| Medium | 500 | `--font-medium` | UI elements, emphasis |
| Semi-Bold | 600 | `--font-semibold` | Subheadings, navigation |
| Bold | 700 | `--font-bold` | Headings, CTAs |
| Extra-Bold | 800 | `--font-extrabold` | Hero headlines |

## Monospace Typeface

### JetBrains Mono

**Rationale:** For code and technical content, JetBrains Mono offers excellent readability and character differentiation, essential for developer audiences.

| Attribute | Value |
|-----------|-------|
| Family | JetBrains Mono |
| Classification | Monospace |
| License | SIL Open Font License |
| Source | [Google Fonts](https://fonts.google.com/specimen/JetBrains+Mono) |

### Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Code blocks |
| Medium | 500 | Inline code, emphasis |
| Bold | 700 | Code headings |

## Type Scale

Based on 1.25 ratio (Major Third) for harmonious rhythm.

### Headings

| Level | Size | Weight | Line Height | Letter Spacing | Token |
|-------|------|--------|-------------|----------------|-------|
| Display | 4.5rem (72px) | 800 | 1.1 | -0.02em | `--text-display` |
| H1 | 3rem (48px) | 700 | 1.2 | -0.02em | `--text-h1` |
| H2 | 2.25rem (36px) | 700 | 1.25 | -0.01em | `--text-h2` |
| H3 | 1.75rem (28px) | 600 | 1.3 | -0.01em | `--text-h3` |
| H4 | 1.5rem (24px) | 600 | 1.35 | 0 | `--text-h4` |
| H5 | 1.25rem (20px) | 600 | 1.4 | 0 | `--text-h5` |
| H6 | 1.125rem (18px) | 600 | 1.4 | 0 | `--text-h6` |

### Body

| Style | Size | Weight | Line Height | Token |
|-------|------|--------|-------------|-------|
| Body Large | 1.125rem (18px) | 400 | 1.6 | `--text-lg` |
| Body | 1rem (16px) | 400 | 1.6 | `--text-base` |
| Body Small | 0.875rem (14px) | 400 | 1.5 | `--text-sm` |
| Caption | 0.75rem (12px) | 400 | 1.4 | `--text-xs` |

### Special Styles

| Style | Size | Weight | Usage |
|-------|------|--------|-------|
| Overline | 0.75rem | 600 | Section labels, uppercase |
| Quote | 1.5rem | 400 italic | Testimonials, pull quotes |
| Stat | 3rem | 700 | Key metrics, numbers |
| Button | 1rem | 600 | CTA buttons |
| Label | 0.875rem | 500 | Form labels |
| Link | inherit | 500 | Inline links |

## CSS Tokens

```css
:root {
  /* Font Families */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
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
  --font-extrabold: 800;
  
  /* Line Heights */
  --leading-none: 1;
  --leading-tight: 1.2;
  --leading-snug: 1.35;
  --leading-normal: 1.5;
  --leading-relaxed: 1.6;
  
  /* Letter Spacing */
  --tracking-tight: -0.02em;
  --tracking-normal: 0;
  --tracking-wide: 0.05em;
}
```

## Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
```

## System Fallbacks

```css
/* Sans-serif fallback */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 
             'Helvetica Neue', Arial, sans-serif;

/* Monospace fallback */
font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
```

## Responsive Typography

### Fluid Scaling

| Viewport | Base Size | Scale |
|----------|-----------|-------|
| Mobile (<640px) | 16px | 1.2 ratio |
| Tablet (640-1024px) | 16px | 1.225 ratio |
| Desktop (>1024px) | 16px | 1.25 ratio |

### Mobile Adjustments
- Display: 2.5rem (40px)
- H1: 2rem (32px)
- H2: 1.5rem (24px)
- Increase line height slightly on mobile

## Usage Guidelines

### Do
- Use Inter for all primary content
- Establish clear hierarchy with size and weight
- Maintain consistent spacing
- Use JetBrains Mono for code only
- Let headings breathe with margins

### Don't
- Use more than 2 font families
- Set body below 14px for reading
- Stretch or compress typefaces
- Use decorative fonts
- Skip heading levels (H1 to H3)

## Accessibility

- Minimum 16px for body text
- Maximum line length: 66 characters
- Sufficient contrast for all text
- Support browser zoom to 200%
- Proper heading hierarchy for screen readers

## Examples

### Hero Headline
```css
.hero-title {
  font-family: var(--font-sans);
  font-size: var(--text-6xl);
  font-weight: var(--font-extrabold);
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
  color: var(--color-gray-600);
}
```

### Code Block
```css
.code {
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  background: var(--color-gray-100);
  padding: 1rem;
  border-radius: 0.5rem;
}
```
