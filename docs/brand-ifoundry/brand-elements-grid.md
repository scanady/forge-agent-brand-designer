# iFoundry Media Grid

> A structured, responsive grid system that organizes complex engineering interfaces with clarity.

## Strategic Foundation

**Brand Alignment:** iFoundry's grid system reflects The Builder's structural discipline. Every element has a deliberate place, creating interfaces that feel engineered — not just designed. The grid provides the invisible scaffolding that makes complex product dashboards, project views, and architecture documentation feel organized and navigable. Like good architecture, the grid handles complexity so users experience simplicity.

## Grid System

### 12-Column Grid
iFoundry uses a 12-column grid with a consistent gutter and responsive breakpoints. The 12-column system provides maximum flexibility for engineering dashboards, documentation layouts, and marketing pages.

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
│ 240  │                                         │
│  px  │  Main Content Area                      │
│      │  (12-column grid)                       │
│      │                                         │
│      │                                         │
│      │                                         │
└──────┴─────────────────────────────────────────┘
```

| Region | Width | Position |
|--------|-------|----------|
| Sidebar | 240px fixed | Fixed left |
| Top Bar | calc(100% - 240px) | Fixed top, offset by sidebar |
| Content | calc(100% - 240px) | Scrollable, offset by sidebar |

### Common Content Layouts

#### Project Dashboard (3-Column Metrics + Full-Width)
```
┌──────────┬──────────┬──────────┐
│  4 col   │  4 col   │  4 col   │  ← Metric cards (builds, uptime, velocity)
├──────────┴──────────┴──────────┤
│         12 columns             │  ← Deployment history / activity
├────────────────────┬───────────┤
│     8 columns      │  4 col    │  ← Sprint board + team sidebar
└────────────────────┴───────────┘
```

#### Detail Page (Content + Sidebar)
```
┌────────────────────┬───────────┐
│     8 columns      │  4 col    │
│                    │           │
│  Primary content   │  Related  │
│  (project details, │  info     │
│   documentation)   │           │
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

#### Documentation / Form Page (Centered)
```
┌────┬────────────────────┬──────┐
│ 2  │     8 columns      │  2   │
│col │                    │ col  │
│    │  Centered content  │      │
│    │  or form           │      │
│    │                    │      │
└────┴────────────────────┴──────┘
```

#### Marketing Landing Page (Full-Width Sections)
```
┌────────────────────────────────┐
│ Full-width hero (12 col)      │
├──────────────────┬─────────────┤
│   6 columns      │  6 columns  │  ← Feature + visual
├──────────────────┴─────────────┤
│ 3 × 4-column cards             │  ← Value propositions
├────────────────────────────────┤
│ Full-width CTA (12 col)       │
└────────────────────────────────┘
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
| Sidebar | Full 240px sidebar visible |
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
  /* Breakpoints (for reference — use in media queries) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 1024px;
  --breakpoint-lg: 1280px;
  --breakpoint-xl: 1536px;

  /* Container */
  --container-max-md: 1200px;
  --container-max-lg: 1280px;
  --container-max-xl: 1440px;

  /* Sidebar */
  --sidebar-width: 240px;
  --sidebar-collapsed: 64px;

  /* Top Bar */
  --topbar-height: 56px;
}
```

## Accessibility

- Ensure content reflows properly at 200% zoom without horizontal scrolling
- Maintain readable line lengths (max ~66 characters) within grid columns
- Don't rely on grid position to convey meaning — use proper semantic order in HTML
- Test that the responsive layout functions correctly with screen readers

## Usage Guidelines

### Do
- Use the 12-column grid for all layout decisions
- Respect breakpoints — don't create custom breakpoints arbitrarily
- Use the standard app layout for authenticated product views
- Test layouts at all five breakpoints
- Use the compact gutter (16px) for dense data views

### Don't
- Break out of the grid for one-off layouts
- Use fixed pixel widths for content areas (use column spans)
- Create layouts that require horizontal scrolling on desktop
- Nest grids more than one level deep
- Ignore the mobile layout — most stakeholder demos happen on laptops, but users are everywhere
