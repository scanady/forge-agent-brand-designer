# OpenLife Spacing

> Consistent spacing that creates breathing room and visual hierarchy.

## Strategic Foundation

**Brand Alignment:** OpenLife's spacing system embodies our value of openness. Generous, consistent spacing creates room for content to breathe, reflects transparency, and establishes clear visual hierarchy. The system ensures cohesive layouts across all products.

## Base Unit

### 4px Base
All spacing derives from a 4px base unit.

| Multiplier | Value | Token |
|------------|-------|-------|
| 0.5× | 2px | `--space-0.5` |
| 1× | 4px | `--space-1` |
| 2× | 8px | `--space-2` |
| 3× | 12px | `--space-3` |
| 4× | 16px | `--space-4` |
| 5× | 20px | `--space-5` |
| 6× | 24px | `--space-6` |
| 8× | 32px | `--space-8` |
| 10× | 40px | `--space-10` |
| 12× | 48px | `--space-12` |
| 16× | 64px | `--space-16` |
| 20× | 80px | `--space-20` |
| 24× | 96px | `--space-24` |

**Rationale:** 4px aligns with common design tools and maintains consistent rhythm at any scale.

## Spacing Scale

### Compact Scale (UI Elements)
| Token | Value | Usage |
|-------|-------|-------|
| `--space-1` | 4px | Icon gaps, tight padding |
| `--space-2` | 8px | Button padding, input padding |
| `--space-3` | 12px | Card padding (small) |
| `--space-4` | 16px | Standard padding |

### Standard Scale (Components)
| Token | Value | Usage |
|-------|-------|-------|
| `--space-4` | 16px | Component padding |
| `--space-6` | 24px | Card padding, section gaps |
| `--space-8` | 32px | Section padding |

### Generous Scale (Layout)
| Token | Value | Usage |
|-------|-------|-------|
| `--space-12` | 48px | Section margins |
| `--space-16` | 64px | Page sections |
| `--space-20` | 80px | Hero spacing |
| `--space-24` | 96px | Major sections |

## Component Spacing

### Buttons
| Element | Value |
|---------|-------|
| Padding (SM) | 8px 12px |
| Padding (MD) | 10px 16px |
| Padding (LG) | 12px 24px |
| Icon gap | 8px |
| Button gap | 12px |

### Inputs
| Element | Value |
|---------|-------|
| Padding | 10px 12px |
| Label gap | 6px |
| Helper text gap | 4px |
| Field gap | 16px |

### Cards
| Element | Value |
|---------|-------|
| Padding (SM) | 12px |
| Padding (MD) | 16px |
| Padding (LG) | 24px |
| Header gap | 12px |
| Content gap | 16px |
| Card gap | 16px–24px |

### Lists
| Element | Value |
|---------|-------|
| Item padding | 12px 16px |
| Item gap | 0 (use borders) |
| Icon gap | 12px |

## Layout Primitives

### Stack (Vertical)
Vertical rhythm for content stacking.

```css
.stack > * + * {
  margin-top: var(--space-4);
}
.stack--sm > * + * {
  margin-top: var(--space-2);
}
.stack--lg > * + * {
  margin-top: var(--space-8);
}
```

### Inline (Horizontal)
Horizontal spacing for inline elements.

```css
.inline {
  display: flex;
  gap: var(--space-4);
}
.inline--sm { gap: var(--space-2); }
.inline--lg { gap: var(--space-6); }
```

### Cluster
Flexible wrapping layout.

```css
.cluster {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-4);
}
```

### Box
Consistent padding container.

```css
.box {
  padding: var(--space-4);
}
.box--sm { padding: var(--space-2); }
.box--lg { padding: var(--space-6); }
```

## Section Spacing

### Page Sections
| Context | Padding |
|---------|---------|
| Standard section | 64px vertical |
| Hero section | 80px–96px vertical |
| Footer | 48px vertical |

### Content Areas
| Context | Margin |
|---------|--------|
| Between sections | 48px–64px |
| Within sections | 24px–32px |
| Between components | 16px–24px |

## CSS Tokens

```css
:root {
  /* Base */
  --space-0: 0;
  --space-0-5: 0.125rem;  /* 2px */
  --space-1: 0.25rem;     /* 4px */
  --space-2: 0.5rem;      /* 8px */
  --space-3: 0.75rem;     /* 12px */
  --space-4: 1rem;        /* 16px */
  --space-5: 1.25rem;     /* 20px */
  --space-6: 1.5rem;      /* 24px */
  --space-8: 2rem;        /* 32px */
  --space-10: 2.5rem;     /* 40px */
  --space-12: 3rem;       /* 48px */
  --space-16: 4rem;       /* 64px */
  --space-20: 5rem;       /* 80px */
  --space-24: 6rem;       /* 96px */
}
```

## Responsive Spacing

### Scaling Approach
- Mobile: Use smaller end of scale
- Desktop: Use larger end of scale

| Viewport | Section Padding |
|----------|-----------------|
| Mobile (<640px) | 32px–48px |
| Tablet (640-1024px) | 48px–64px |
| Desktop (>1024px) | 64px–96px |

### Fluid Spacing
```css
.section {
  padding-block: clamp(2rem, 5vw, 4rem);
}
```

## Usage Guidelines

### Do
- Use spacing tokens consistently
- Apply generous spacing for readability
- Increase spacing for larger screens
- Group related items closely
- Separate distinct groups clearly

### Don't
- Use arbitrary pixel values
- Overcrowd content
- Mix spacing scales inconsistently
- Forget responsive adjustments
- Apply uniform spacing everywhere

## Accessibility

- Ensure sufficient spacing for touch targets (44px minimum)
- Don't rely on spacing alone for grouping
- Maintain logical reading order
- Support text scaling without overlap

## Examples

### Card Component
```css
.card {
  padding: var(--space-6);
}
.card-header {
  margin-bottom: var(--space-4);
}
.card-content > * + * {
  margin-top: var(--space-3);
}
.card-actions {
  margin-top: var(--space-6);
  display: flex;
  gap: var(--space-3);
}
```

### Page Section
```css
.section {
  padding: var(--space-16) 0;
}
.section-header {
  margin-bottom: var(--space-8);
}
.section-content {
  display: grid;
  gap: var(--space-6);
}
```
