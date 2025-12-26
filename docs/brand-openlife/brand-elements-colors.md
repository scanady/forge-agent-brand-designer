# OpenLife Colors

> Colors that embody liberation, openness, and forward-thinking innovation.

## Strategic Foundation

**Brand Alignment:** OpenLife's color palette reflects The Liberator archetype—confident, trustworthy, and forward-looking. Colors balance the credibility needed for enterprise audiences with the innovation and energy of a transformative platform. Open, breathable palettes communicate transparency, while confident accents convey ambition.

## Primary Colors

The primary palette forms the foundation of OpenLife's visual identity.

### Liberation Blue
The cornerstone of OpenLife's identity—representing trust, openness, and technology leadership.

| Format | Value |
|--------|-------|
| HEX | `#0066CC` |
| RGB | `rgb(0, 102, 204)` |
| HSL | `hsl(210, 100%, 40%)` |

**CSS Token:** `--color-primary`

**Usage:** Primary brand color, headers, primary buttons, links, key brand moments.

### Foundation Navy
Grounded confidence and technical credibility—the deep anchor of the palette.

| Format | Value |
|--------|-------|
| HEX | `#0D1B2A` |
| RGB | `rgb(13, 27, 42)` |
| HSL | `hsl(211, 53%, 11%)` |

**CSS Token:** `--color-primary-dark`

**Usage:** Text, dark backgrounds, footer areas, high-contrast elements.

### Open White
Clean, transparent space that lets content breathe—embodying openness and clarity.

| Format | Value |
|--------|-------|
| HEX | `#FFFFFF` |
| RGB | `rgb(255, 255, 255)` |
| HSL | `hsl(0, 0%, 100%)` |

**CSS Token:** `--color-white`

**Usage:** Backgrounds, text on dark surfaces, negative space.

## Secondary Colors

Extend the palette for variety and hierarchy without competing with primary colors.

### Collaboration Teal
Represents partnership, community, and shared success.

| Format | Value |
|--------|-------|
| HEX | `#0891B2` |
| RGB | `rgb(8, 145, 178)` |
| HSL | `hsl(192, 91%, 36%)` |

**CSS Token:** `--color-secondary`

**Usage:** Secondary CTAs, community features, collaboration content.

### Innovation Indigo
Depth and forward-thinking technology—AI and future capabilities.

| Format | Value |
|--------|-------|
| HEX | `#4F46E5` |
| RGB | `rgb(79, 70, 229)` |
| HSL | `hsl(243, 75%, 59%)` |

**CSS Token:** `--color-tertiary`

**Usage:** AI features, innovation highlights, technical documentation.

## Accent Colors

High-energy accents for emphasis, calls-to-action, and transformation moments.

### Transform Orange
Energy, action, and transformation—the catalyst for change.

| Format | Value |
|--------|-------|
| HEX | `#EA580C` |
| RGB | `rgb(234, 88, 12)` |
| HSL | `hsl(21, 90%, 48%)` |

**CSS Token:** `--color-accent`

**Usage:** Primary CTAs, important actions, transformation messaging, highlights.

### Progress Green
Growth, success, and forward momentum.

| Format | Value |
|--------|-------|
| HEX | `#059669` |
| RGB | `rgb(5, 150, 105)` |
| HSL | `hsl(161, 94%, 30%)` |

**CSS Token:** `--color-success`

**Usage:** Success states, positive metrics, growth indicators.

## Neutral Palette

Essential grays for UI, text, and structural elements.

| Name | HEX | Token | Usage |
|------|-----|-------|-------|
| Gray 50 | `#F8FAFC` | `--color-gray-50` | Light backgrounds |
| Gray 100 | `#F1F5F9` | `--color-gray-100` | Card backgrounds, zebra rows |
| Gray 200 | `#E2E8F0` | `--color-gray-200` | Borders, dividers |
| Gray 300 | `#CBD5E1` | `--color-gray-300` | Disabled states, placeholders |
| Gray 400 | `#94A3B8` | `--color-gray-400` | Secondary text, captions |
| Gray 500 | `#64748B` | `--color-gray-500` | Body text (light bg) |
| Gray 600 | `#475569` | `--color-gray-600` | Body text (standard) |
| Gray 700 | `#334155` | `--color-gray-700` | Headings, emphasis |
| Gray 800 | `#1E293B` | `--color-gray-800` | High-contrast text |
| Gray 900 | `#0F172A` | `--color-gray-900` | Near-black |

## Semantic Colors

Functional colors for UI states and feedback.

### Success

| Shade | HEX | Token | Usage |
|-------|-----|-------|-------|
| Light | `#D1FAE5` | `--color-success-light` | Success backgrounds |
| Default | `#059669` | `--color-success` | Success icons, text |
| Dark | `#065F46` | `--color-success-dark` | Success emphasis |

### Warning

| Shade | HEX | Token | Usage |
|-------|-----|-------|-------|
| Light | `#FEF3C7` | `--color-warning-light` | Warning backgrounds |
| Default | `#D97706` | `--color-warning` | Warning icons, text |
| Dark | `#92400E` | `--color-warning-dark` | Warning emphasis |

### Error

| Shade | HEX | Token | Usage |
|-------|-----|-------|-------|
| Light | `#FEE2E2` | `--color-error-light` | Error backgrounds |
| Default | `#DC2626` | `--color-error` | Error icons, text |
| Dark | `#991B1B` | `--color-error-dark` | Error emphasis |

### Info

| Shade | HEX | Token | Usage |
|-------|-----|-------|-------|
| Light | `#DBEAFE` | `--color-info-light` | Info backgrounds |
| Default | `#0284C7` | `--color-info` | Info icons, text |
| Dark | `#075985` | `--color-info-dark` | Info emphasis |

## Color Tokens (CSS)

```css
:root {
  /* Primary */
  --color-primary: #0066CC;
  --color-primary-dark: #0D1B2A;
  --color-white: #FFFFFF;
  
  /* Secondary */
  --color-secondary: #0891B2;
  --color-tertiary: #4F46E5;
  
  /* Accent */
  --color-accent: #EA580C;
  
  /* Semantic */
  --color-success: #059669;
  --color-success-light: #D1FAE5;
  --color-warning: #D97706;
  --color-warning-light: #FEF3C7;
  --color-error: #DC2626;
  --color-error-light: #FEE2E2;
  --color-info: #0284C7;
  --color-info-light: #DBEAFE;
  
  /* Neutrals */
  --color-gray-50: #F8FAFC;
  --color-gray-100: #F1F5F9;
  --color-gray-200: #E2E8F0;
  --color-gray-300: #CBD5E1;
  --color-gray-400: #94A3B8;
  --color-gray-500: #64748B;
  --color-gray-600: #475569;
  --color-gray-700: #334155;
  --color-gray-800: #1E293B;
  --color-gray-900: #0F172A;
}
```

## Color Ratios & Hierarchy

### 60-30-10 Rule
- **60% Neutrals:** White, grays—breathing room and readability
- **30% Primary:** Liberation Blue, Foundation Navy—brand presence
- **10% Accent:** Transform Orange, secondary colors—emphasis

### Application
1. **Liberation Blue** for primary actions and brand moments
2. **Transform Orange** for the most important CTAs
3. **Neutrals** for backgrounds and content
4. **Semantic colors** for status and feedback only

## Accessibility

### Contrast Ratios (WCAG 2.1)

| Combination | Ratio | Level |
|-------------|-------|-------|
| Foundation Navy on White | 16.7:1 | AAA ✓ |
| Liberation Blue on White | 4.5:1 | AA ✓ |
| Gray 600 on White | 5.7:1 | AA ✓ |
| White on Liberation Blue | 4.5:1 | AA ✓ |
| White on Foundation Navy | 16.7:1 | AAA ✓ |
| Transform Orange on White | 3.4:1 | AA Large ✓ |

### Guidelines
- **Body text:** Use Gray 600+ on light backgrounds
- **Large text (18pt+):** Can use 3:1 minimum
- **Interactive elements:** Minimum AA compliance (4.5:1)
- **Don't rely on color alone:** Pair with icons, text, patterns

## Dark Mode

### Palette Adjustments

| Light Mode | Dark Mode | Notes |
|------------|-----------|-------|
| White `#FFFFFF` | Gray 900 `#0F172A` | Background |
| Foundation Navy | White `#FFFFFF` | Text |
| Liberation Blue | `#3B82F6` | Lighter for dark bg |
| Gray 100 | Gray 800 | Cards |
| Gray 600 | Gray 300 | Body text |

### Dark Mode Tokens

```css
[data-theme="dark"] {
  --color-background: #0F172A;
  --color-text: #FFFFFF;
  --color-primary: #3B82F6;
  --color-card: #1E293B;
  --color-border: #334155;
}
```

## Usage Guidelines

### Do
- Use Liberation Blue as the dominant brand color
- Maintain generous white space
- Apply accent colors sparingly
- Test all combinations for accessibility
- Use semantic colors for their intended purpose

### Don't
- Use Transform Orange for large backgrounds
- Combine multiple accent colors closely
- Apply colors at low opacity that compromise contrast
- Use colors outside this system
- Forget dark mode considerations

## Examples

### Color in Context
- **Headers:** Liberation Blue or Foundation Navy text
- **Primary buttons:** Transform Orange with white text
- **Secondary buttons:** Liberation Blue outline or filled
- **Body text:** Gray 600 on white
- **Cards:** White on Gray 50 backgrounds
- **Success toast:** Progress Green icon with dark text
