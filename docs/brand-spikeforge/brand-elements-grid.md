# SpikeForge Grid

> A structured, responsive grid system that organizes practice management interfaces with clarity and consistency.

## Strategic Foundation

**Brand Alignment:** SpikeForge's grid system reflects The Architect archetype — every element has a deliberate place, creating interfaces that feel organized and professional. The grid provides the invisible scaffolding that makes complex coaching workflows feel simple. Like a well-run practice, the grid handles structural complexity so that what the coach sees is clean, focused, and intuitive.

## Grid System

### 12-Column Grid
SpikeForge uses a 12-column grid with a consistent gutter and responsive breakpoints. The 12-column system provides maximum flexibility, supporting 2, 3, 4, and 6-column layouts.

| Attribute | Value |
|-----------|-------|
| Columns | 12 |
| Gutter | 24px (standard), 16px (compact) |
| Type | Fluid within max-width container |

## Breakpoints

| Name | Min Width | Container Max | Columns | Gutter |
|------|-----------|---------------|---------|--------|
| Mobile | 0px | 100% | 4 | 16px |
| Tablet | 640px | 100% | 8 | 24px |
| Desktop | 1024px | 1200px | 12 | 24px |
| Wide | 1280px | 1280px | 12 | 24px |
| Ultra | 1536px | 1440px | 12 | 32px |

### Container Widths

```css
.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: var(--space-4);
  padding-right: var(--space-4);
}

@media (min-width: 640px) {
  .container { padding-left: var(--space-6); padding-right: var(--space-6); }
}

@media (min-width: 1024px) {
  .container { max-width: 1200px; }
}

@media (min-width: 1280px) {
  .container { max-width: 1280px; }
}

@media (min-width: 1536px) {
  .container { max-width: 1440px; padding-left: var(--space-8); padding-right: var(--space-8); }
}
```

## Application Layout

### Standard App Layout (Sidebar + Content)

```
┌──────┬─────────────────────────────────────────┐
│      │  Top Bar                                 │
│      ├─────────────────────────────────────────┤
│ Side │                                         │
│ Nav  │  Page Header                            │
│      ├─────────────────────────────────────────┤
│ 260  │                                         │
│  px  │  Main Content Area                      │
│      │  (12-column grid)                       │
│      │                                         │
│      │                                         │
│      │                                         │
└──────┴─────────────────────────────────────────┘
```

| Region | Width | Position |
|--------|-------|----------|
| Sidebar | 260px fixed | Fixed left |
| Top Bar | calc(100% - 260px) | Fixed top, offset by sidebar |
| Content | calc(100% - 260px) | Scrollable, offset by sidebar |

### Common Content Layouts

#### Dashboard (3-Column Metrics + Full-Width)
```
┌──────────┬──────────┬──────────┐
│  4 col   │  4 col   │  4 col   │  ← Metric cards
├──────────┴──────────┴──────────┤
│         12 columns             │  ← Activity table
├────────────────────┬───────────┤
│     8 columns      │  4 col    │  ← Chart + sidebar
└────────────────────┴───────────┘
```

#### Detail Page (Content + Sidebar)
```
┌────────────────────┬───────────┐
│     8 columns      │  4 col    │
│                    │           │
│  Primary content   │  Related  │
│  (form, details)   │  info     │
│                    │           │
└────────────────────┴───────────┘
```

#### List / Table View (Full-Width)
```
┌────────────────────────────────┐
│ Filters / Search bar (12 col) │
├────────────────────────────────┤
│ Table / List (12 col)         │
│                                │
│                                │
├────────────────────────────────┤
│ Pagination (12 col)           │
└────────────────────────────────┘
```

#### Settings / Form Page (Centered)
```
┌────┬────────────────────┬──────┐
│ 2  │     8 columns      │  2   │
│col │                    │ col  │
│    │  Centered form     │      │
│    │  content           │      │
│    │                    │      │
└────┴────────────────────┴──────┘
```

## Responsive Behavior

### Mobile (0–639px)

| Layout | Behavior |
|--------|----------|
| Sidebar | Collapses to hamburger menu overlay |
| Content | Full-width, 4-column grid |
| Cards | Stack vertically, full-width |
| Tables | Horizontal scroll or card-based layout |
| Top Bar | Simplified — logo, hamburger, user avatar |

### Tablet (640–1023px)

| Layout | Behavior |
|--------|----------|
| Sidebar | Collapsed to icon-only (64px) or hidden |
| Content | Full-width minus sidebar, 8-column grid |
| Cards | 2-column grid |
| Tables | Horizontal scroll for wide tables |
| Top Bar | Full with search |

### Desktop (1024px+)

| Layout | Behavior |
|--------|----------|
| Sidebar | Full 260px sidebar visible |
| Content | 12-column grid within container |
| Cards | 2, 3, or 4-column grid |
| Tables | Full-width with all columns |
| Top Bar | Full with search, notifications, user menu |

## CSS Grid Implementation

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-6);
}

/* Mobile: 4-column */
@media (max-width: 639px) {
  .grid {
    grid-template-columns: repeat(4, 1fr);
    gap: var(--space-4);
  }
}

/* Tablet: 8-column */
@media (min-width: 640px) and (max-width: 1023px) {
  .grid {
    grid-template-columns: repeat(8, 1fr);
  }
}

/* Column spans */
.col-1 { grid-column: span 1; }
.col-2 { grid-column: span 2; }
.col-3 { grid-column: span 3; }
.col-4 { grid-column: span 4; }
.col-6 { grid-column: span 6; }
.col-8 { grid-column: span 8; }
.col-12 { grid-column: span 12; }

/* Full-width override on mobile */
@media (max-width: 639px) {
  .col-4, .col-6, .col-8, .col-12 {
    grid-column: 1 / -1;
  }
}
```

## CSS Tokens

```css
:root {
  /* Grid */
  --grid-columns: 12;
  --grid-gutter: 24px;
  --grid-gutter-compact: 16px;

  /* Sidebar */
  --sidebar-width: 260px;
  --sidebar-collapsed-width: 64px;

  /* Top Bar */
  --header-height: 64px;

  /* Containers */
  --container-sm: 640px;
  --container-md: 1024px;
  --container-lg: 1200px;
  --container-xl: 1280px;
  --container-2xl: 1440px;

  /* Breakpoints (for reference — use media queries) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 1024px;
  --breakpoint-lg: 1280px;
  --breakpoint-xl: 1536px;
}
```

## Accessibility

- Content must maintain readability at all breakpoints — never truncate essential content
- Grid layouts must support browser zoom to 200% without horizontal scroll on body content
- Touch targets maintain 44px minimum size regardless of grid compression
- Keyboard focus order follows visual order (left-to-right, top-to-bottom)
- Collapsed sidebar must be accessible via keyboard (hamburger menu, Escape to close)

## Usage Guidelines

### Do
- Use the 12-column grid for all page layouts
- Respect breakpoint-specific column counts (4 → 8 → 12)
- Use semantic layout regions (main, aside, nav) for accessibility
- Let content dictate column width — not the reverse
- Test all layouts at every breakpoint

### Don't
- Create layouts that require horizontal scrolling on body content
- Mix gutter sizes within the same grid
- Use absolute positioning for layout (use grid/flex)
- Force content into fewer columns than it needs to be readable
- Assume a specific viewport width — design for the range
