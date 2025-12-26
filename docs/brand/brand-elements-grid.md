# OpenLife Grid

> Consistent layouts that position content with precision and flexibility.

## Strategic Foundation

**Brand Alignment:** OpenLife's grid system creates the structural foundation for open, balanced layouts. Consistent grids reinforce professionalism and ensure a cohesive experience across products. The system is flexible enough for varied content while maintaining visual harmony.

## Grid System

### 12-Column Grid
Primary grid for layouts at all breakpoints.

| Attribute | Value |
|-----------|-------|
| Columns | 12 |
| Gutter | 24px (desktop), 16px (mobile) |
| Type | Fluid (percentage-based) |

**Rationale:** 12 divides evenly by 2, 3, 4, and 6, enabling flexible layouts.

## Breakpoints

| Name | Min Width | Columns | Gutter | Container |
|------|-----------|---------|--------|-----------|
| Mobile | 0 | 4 | 16px | 100% - 32px |
| Tablet | 640px | 8 | 24px | 100% - 48px |
| Desktop | 1024px | 12 | 24px | 100% - 64px |
| Wide | 1280px | 12 | 32px | 1200px max |
| Ultra | 1536px | 12 | 32px | 1400px max |

## Container Widths

| Token | Max Width | Usage |
|-------|-----------|-------|
| `--container-sm` | 640px | Narrow content, forms |
| `--container-md` | 768px | Article content |
| `--container-lg` | 1024px | Standard pages |
| `--container-xl` | 1200px | Wide layouts |
| `--container-2xl` | 1400px | Full-width dashboards |

## Column Spans

### Common Layouts

| Layout | Columns | Usage |
|--------|---------|-------|
| Full width | 12 | Hero, sections |
| Two-thirds | 8 | Main content |
| One-third | 4 | Sidebar |
| Half | 6 | Two-column |
| Quarter | 3 | Four-column, cards |
| Third | 4 | Three-column |

### Responsive Patterns

| Mobile | Tablet | Desktop | Pattern |
|--------|--------|---------|---------|
| 4 | 8 | 8 + 4 | Content + sidebar |
| 4 | 4 + 4 | 4 + 4 + 4 | Three columns |
| 4 | 4 + 4 | 3 + 3 + 3 + 3 | Four columns |
| 4 | 8 | 6 + 6 | Two equal columns |

## CSS Tokens

```css
:root {
  /* Breakpoints */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
  
  /* Containers */
  --container-sm: 640px;
  --container-md: 768px;
  --container-lg: 1024px;
  --container-xl: 1200px;
  --container-2xl: 1400px;
  
  /* Gutters */
  --gutter-sm: 1rem;    /* 16px */
  --gutter-md: 1.5rem;  /* 24px */
  --gutter-lg: 2rem;    /* 32px */
}
```

## Grid Implementation

### CSS Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--gutter-md);
}

.col-4 { grid-column: span 4; }
.col-6 { grid-column: span 6; }
.col-8 { grid-column: span 8; }
.col-12 { grid-column: span 12; }

@media (max-width: 1023px) {
  .grid { grid-template-columns: repeat(8, 1fr); }
}
@media (max-width: 639px) {
  .grid { grid-template-columns: repeat(4, 1fr); }
}
```

### Container

```css
.container {
  width: 100%;
  max-width: var(--container-xl);
  margin-inline: auto;
  padding-inline: var(--gutter-md);
}

@media (max-width: 639px) {
  .container {
    padding-inline: var(--gutter-sm);
  }
}
```

## Common Layouts

### Content + Sidebar
```
Desktop (12 col):  [  Content (8)  ] [ Sidebar (4) ]
Tablet (8 col):    [     Content (8)     ]
                   [     Sidebar (8)     ]
Mobile (4 col):    [   Content (4)   ]
                   [   Sidebar (4)   ]
```

### Three Column
```
Desktop (12 col):  [ Col (4) ] [ Col (4) ] [ Col (4) ]
Tablet (8 col):    [ Col (4) ] [ Col (4) ]
                   [     Col (8)     ]
Mobile (4 col):    [  Col (4)  ]
                   [  Col (4)  ]
                   [  Col (4)  ]
```

### Two Column
```
Desktop (12 col):  [   Col (6)   ] [   Col (6)   ]
Tablet (8 col):    [  Col (4)  ] [  Col (4)  ]
Mobile (4 col):    [    Col (4)    ]
                   [    Col (4)    ]
```

## Offset & Alignment

### Column Offset
```css
.col-offset-2 { grid-column-start: 3; }
.col-offset-3 { grid-column-start: 4; }
.col-offset-4 { grid-column-start: 5; }
```

### Content Alignment
```css
.grid--center { justify-items: center; }
.grid--start { justify-items: start; }
.grid--end { justify-items: end; }
```

## Responsive Behavior

### Fluid Columns
Columns scale proportionally within the grid.

### Stacking
On smaller viewports, columns stack vertically.

### Reordering
Content order may change responsively for optimal UX.

```css
@media (max-width: 639px) {
  .sidebar { order: 2; }
  .main-content { order: 1; }
}
```

## Usage Guidelines

### Do
- Use the 12-column grid consistently
- Plan responsive behavior upfront
- Maintain consistent gutters
- Use containers for centered content
- Test at all breakpoints

### Don't
- Create arbitrary column widths
- Ignore mobile layouts
- Mix grid systems
- Exceed container maximums
- Forget about edge padding

## Accessibility

- Ensure logical reading order in markup
- Don't break semantic structure for layout
- Test with screen readers
- Maintain focus order that matches visual order

## Examples

### Dashboard Layout
```css
.dashboard {
  display: grid;
  grid-template-columns: 240px 1fr;
  gap: var(--gutter-md);
}
.dashboard-nav {
  grid-column: 1;
}
.dashboard-main {
  grid-column: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--gutter-md);
}
```

### Card Grid
```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: var(--space-6);
}
```

### Content Page
```css
.content-page {
  display: grid;
  grid-template-columns: 1fr min(65ch, 100%) 1fr;
}
.content-page > * {
  grid-column: 2;
}
.content-page .full-bleed {
  grid-column: 1 / -1;
}
```
