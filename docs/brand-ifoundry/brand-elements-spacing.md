# iFoundry Media Spacing

> Consistent, intentional spacing that gives engineering content room to breathe and products room to speak.

## Strategic Foundation

**Brand Alignment:** iFoundry's spacing system reflects The Builder's precision and the Craftsmanship value. Every pixel of whitespace is deliberate — creating focus, establishing hierarchy, and letting technical content remain readable. Like well-structured code, the spacing system follows clear, predictable rules so interfaces feel both organized and spacious. Generous spacing communicates confidence; cramped layouts communicate compromise.

## Base Unit

All spacing in the iFoundry design system is built on a **4px base unit**. Every spacing value is a multiple of 4, creating a predictable, harmonious rhythm.

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
For dense data views — deployment dashboards, build logs, metric tables.

| Context | Value |
|---------|-------|
| Element gap | `--space-1` (4px) |
| Cell padding | `--space-2` (8px) |
| Row height | 36px |
| Section gap | `--space-4` (16px) |

### Standard (Default)
For general application views — project pages, settings, documentation.

| Context | Value |
|---------|-------|
| Element gap | `--space-2` (8px) |
| Cell padding | `--space-3` (12px) |
| Row height | 44px |
| Section gap | `--space-6` (24px) |

### Generous
For marketing pages, landing pages, and long-form reading.

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

## Responsive Spacing

### Mobile Adjustments
On smaller viewports, tighten spacing to maximize content area while maintaining proportional relationships.

| Desktop Token | Mobile Value | Reduction |
|---------------|-------------|-----------|
| `--space-24` (96px) | 48px | 50% |
| `--space-16` (64px) | 40px | 37% |
| `--space-10` (40px) | 24px | 40% |
| `--space-8` (32px) | 24px | 25% |
| `--space-6` (24px) | 16px | 33% |
| `--space-4` (16px) | 16px | 0% (floor) |

### Implementation

```css
@media (max-width: 639px) {
  :root {
    --space-section: var(--space-6);
    --space-page: var(--space-10);
  }
}

@media (min-width: 640px) {
  :root {
    --space-section: var(--space-10);
    --space-page: var(--space-16);
  }
}
```

## Accessibility

- Ensure touch targets are at least 44×44px with adequate spacing between interactive elements
- Maintain sufficient spacing around interactive elements for motor accessibility
- Don't reduce spacing below the compact density for any user-facing content
- Spacing should scale proportionally when browser zoom is applied

## Usage Guidelines

### Do
- Use the spacing scale consistently — never use arbitrary pixel values
- Apply the density system appropriately to the context (compact for data, standard for general, generous for marketing)
- Let technical content breathe — engineering dashboards need spacious card layouts
- Use layout primitives for consistent spacing patterns

### Don't
- Use spacing values outside the defined scale
- Mix density levels within the same section
- Reduce spacing to cram more content on screen — if it doesn't fit, restructure the layout
- Use margins for what gaps and padding handle better
- Ignore responsive spacing adjustments on mobile
