# Nexus Coach Spacing

> Consistent, intentional spacing that creates breathing room and visual order.

## Strategic Foundation

**Brand Alignment:** Nexus Coach's spacing system reflects The Architect's precision and The Guide's clarity. Generous, consistent spacing communicates that a well-run practice is organized without being cramped. White space is a design tool — it creates focus, establishes hierarchy, and lets content breathe. Like the operational structure Nexus Coach provides, the spacing system handles complexity so coaches don't have to think about it.

## Base Unit

All spacing in the Nexus Coach design system is built on a **4px base unit**. Every spacing value is a multiple of 4, creating a predictable, harmonious rhythm.

| Attribute | Value |
|-----------|-------|
| Base unit | 4px |
| System | Multiples of 4px |
| Naming | Numeric tokens (--space-1 through --space-24) |

## Spacing Scale

| Token | Multiplier | Value | Usage |
|-------|------------|-------|-------|
| `--space-0.5` | 0.5× | 2px | Hairline gaps, icon adjustments |
| `--space-1` | 1× | 4px | Tight inline spacing, badge padding |
| `--space-2` | 2× | 8px | Compact element spacing, icon gaps |
| `--space-3` | 3× | 12px | Button padding (vertical), form input padding |
| `--space-4` | 4× | 16px | Standard element spacing, card padding |
| `--space-5` | 5× | 20px | Comfortable element spacing |
| `--space-6` | 6× | 24px | Section padding, card content areas |
| `--space-8` | 8× | 32px | Large section spacing, generous padding |
| `--space-10` | 10× | 40px | Section separation within pages |
| `--space-12` | 12× | 48px | Large section gaps |
| `--space-16` | 16× | 64px | Page-level section spacing |
| `--space-20` | 20× | 80px | Major layout separation |
| `--space-24` | 24× | 96px | Hero/marketing section spacing |

## Density Scales

Three density levels accommodate different content types and viewport sizes.

### Compact
For dense data views — coach dashboards, client lists, session tables.

| Context | Value |
|---------|-------|
| Element gap | `--space-1` (4px) |
| Cell padding | `--space-2` (8px) |
| Row height | 36px |
| Section gap | `--space-4` (16px) |

### Standard (Default)
For general application views — forms, detail pages, settings.

| Context | Value |
|---------|-------|
| Element gap | `--space-2` (8px) |
| Cell padding | `--space-3` (12px) |
| Row height | 44px |
| Section gap | `--space-6` (24px) |

### Generous
For marketing, onboarding, and reading-heavy views.

| Context | Value |
|---------|-------|
| Element gap | `--space-4` (16px) |
| Cell padding | `--space-6` (24px) |
| Row height | 56px |
| Section gap | `--space-10` (40px) |

## Component Spacing

### Buttons

| Property | Compact | Standard | Large |
|----------|---------|----------|-------|
| Padding (v × h) | 6px × 12px | 10px × 16px | 12px × 24px |
| Gap (icon to text) | 6px | 8px | 8px |
| Height | 32px | 40px | 48px |

### Form Inputs

| Property | Value |
|----------|-------|
| Padding (v × h) | 10px × 12px |
| Height | 40px |
| Label to input gap | `--space-1` (4px) |
| Input to help text gap | `--space-1` (4px) |
| Field to field gap | `--space-4` (16px) |
| Section to section gap | `--space-8` (32px) |

### Cards

| Property | Value |
|----------|-------|
| Padding | `--space-6` (24px) |
| Header to content gap | `--space-4` (16px) |
| Content to footer gap | `--space-4` (16px) |
| Card to card gap | `--space-4` (16px) |

### Lists

| Property | Compact | Standard |
|----------|---------|----------|
| Item padding (v × h) | 8px × 12px | 12px × 16px |
| Item gap | 0 (border-separated) | 0 (border-separated) |
| List top/bottom padding | `--space-2` (8px) | `--space-2` (8px) |

### Navigation

| Property | Value |
|----------|-------|
| Sidebar padding | `--space-4` (16px) |
| Nav item padding | 10px × 12px |
| Nav item gap | `--space-1` (4px) |
| Section title margin bottom | `--space-2` (8px) |
| Section gap | `--space-6` (24px) |

## Layout Primitives

Reusable layout patterns that apply spacing consistently.

### Stack (Vertical)
Consistent vertical spacing between stacked elements.

```css
.stack {
  display: flex;
  flex-direction: column;
}

.stack > * + * {
  margin-top: var(--space-4);
}

.stack-tight > * + * { margin-top: var(--space-2); }
.stack-loose > * + * { margin-top: var(--space-6); }
.stack-section > * + * { margin-top: var(--space-8); }
```

### Inline (Horizontal)
Consistent horizontal spacing between inline elements.

```css
.inline {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-2);
}

.inline-tight { gap: var(--space-1); }
.inline-loose { gap: var(--space-4); }
```

### Cluster (Wrapped Group)
For tag groups, badge sets, and wrapped button groups.

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
}
```

### Box (Padded Container)
For content containers with consistent internal padding.

```css
.box {
  padding: var(--space-6);
}

.box-compact { padding: var(--space-4); }
.box-generous { padding: var(--space-8); }
```

## CSS Tokens

```css
:root {
  /* Spacing Scale */
  --space-0-5: 2px;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;
  --space-20: 80px;
  --space-24: 96px;
}
```

## Accessibility

- Touch targets must be at least 44×44px (see Accessibility guidelines)
- Spacing between interactive elements should prevent accidental activation (minimum 8px gap)
- Generous spacing improves readability for users with cognitive disabilities
- Consistent spacing creates predictable patterns for screen reader navigation

## Usage Guidelines

### Do
- Use spacing tokens consistently — never use arbitrary pixel values
- Choose the density scale appropriate to the content type (data-heavy = compact, narrative = generous)
- Let content breathe — when in doubt, use more space
- Maintain consistent spacing within component types (all cards use the same padding)
- Use the Stack and Inline primitives for layout rather than ad-hoc margins

### Don't
- Mix density scales within the same view section
- Use spacing values outside the token scale
- Rely on padding alone for layout — combine with flex gap
- Compress spacing to fit more content on screen (remove content instead)
- Use margins for component-internal spacing (use padding)
