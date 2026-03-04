# iFoundry Media Border

> Precise edges and boundaries that define structure, reinforce interaction states, and echo the engineered clarity of the brand.

## Strategic Foundation

**Brand Alignment:** iFoundry's border system reflects The Builder's precision and attention to craft. Borders are structural — they define containers, separate content, and highlight interactive elements. Like clean code, they serve a clear purpose and never appear without reason. The radius system balances the brand's technical authority (sharp, engineered) with approachability (softened, not harsh).

## Border Width

| Token | Value | Use Case |
|-------|-------|----------|
| `--border-0` | 0px | No border |
| `--border-1` | 1px | Default — cards, inputs, dividers |
| `--border-2` | 2px | Emphasis — active tabs, selected items, focus rings |
| `--border-4` | 4px | Accent — left border highlights, feature callouts |

## Border Radius

The radius scale keeps corners controlled and purposeful. iFoundry avoids overly rounded ("bubbly") shapes — the aesthetic is precise, with just enough rounding to feel approachable.

| Token | Value | Use Case |
|-------|-------|----------|
| `--radius-none` | 0px | Sharp corners — code blocks, data tables |
| `--radius-sm` | 4px | Subtle rounding — badges, tags, inline elements |
| `--radius-md` | 6px | Default — buttons, inputs, cards |
| `--radius-lg` | 8px | Containers — modals, popovers, dialogs |
| `--radius-xl` | 12px | Feature — hero cards, marketing callouts |
| `--radius-full` | 9999px | Pill — toggle buttons, search pills, avatars |

## Border Color

| Token | Value (Light) | Value (Dark) | Use Case |
|-------|---------------|--------------|----------|
| `--border-default` | Slate 200 `#E2E8F0` | Slate 700 `#334155` | Default borders |
| `--border-subtle` | Slate 100 `#F1F5F9` | Slate 800 `#1E293B` | Dividers, subtle separators |
| `--border-strong` | Slate 300 `#CBD5E1` | Slate 600 `#475569` | Emphasized borders |
| `--border-focus` | Forge Blue `#1D4ED8` | Blue 400 `#60A5FA` | Focus rings |
| `--border-active` | Forge Blue `#1D4ED8` | Blue 400 `#60A5FA` | Active/selected states |
| `--border-success` | Green 600 `#059669` | Green 400 `#34D399` | Success states |
| `--border-warning` | Ignite Orange `#EA580C` | Orange 400 `#FB923C` | Warning states |
| `--border-error` | Red 600 `#DC2626` | Red 400 `#F87171` | Error states |
| `--border-brand` | Forge Blue `#1D4ED8` | Blue 400 `#60A5FA` | Brand accent borders |

## CSS Tokens

```css
:root {
  /* Width */
  --border-0: 0px;
  --border-1: 1px;
  --border-2: 2px;
  --border-4: 4px;

  /* Radius */
  --radius-none: 0px;
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-full: 9999px;

  /* Color — Light Mode */
  --border-default: #E2E8F0;
  --border-subtle: #F1F5F9;
  --border-strong: #CBD5E1;
  --border-focus: #1D4ED8;
  --border-active: #1D4ED8;
  --border-success: #059669;
  --border-warning: #EA580C;
  --border-error: #DC2626;
  --border-brand: #1D4ED8;
}

[data-theme="dark"] {
  --border-default: #334155;
  --border-subtle: #1E293B;
  --border-strong: #475569;
  --border-focus: #60A5FA;
  --border-active: #60A5FA;
  --border-success: #34D399;
  --border-warning: #FB923C;
  --border-error: #F87171;
  --border-brand: #60A5FA;
}
```

## Focus States

Visible focus indicators are critical for keyboard navigation and accessibility. iFoundry uses a double-ring focus style: a 2px brand-colored ring with a 2px offset.

```css
:focus-visible {
  outline: var(--border-2) solid var(--border-focus);
  outline-offset: 2px;
  border-radius: var(--radius-md);
}

/* Remove default outline for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}
```

### Focus by Component

| Component | Focus Style |
|-----------|-------------|
| Button | 2px Forge Blue ring, 2px offset |
| Input | 2px Forge Blue ring, 0px offset (sits on border) |
| Link | 2px Forge Blue ring, 2px offset |
| Card (interactive) | 2px Forge Blue ring, 2px offset |
| Checkbox / Radio | 2px Forge Blue ring, 2px offset |
| Tab | 2px bottom border, Forge Blue |

## Common Border Patterns

### Card
```css
.card {
  border: var(--border-1) solid var(--border-default);
  border-radius: var(--radius-md);
}

.card:hover {
  border-color: var(--border-strong);
}
```

### Divider
```css
.divider {
  border: none;
  border-top: var(--border-1) solid var(--border-subtle);
  margin: var(--space-4) 0;
}
```

### Input
```css
.input {
  border: var(--border-1) solid var(--border-default);
  border-radius: var(--radius-md);
  transition: border-color 150ms ease;
}

.input:hover {
  border-color: var(--border-strong);
}

.input:focus {
  border-color: var(--border-focus);
  outline: var(--border-1) solid var(--border-focus);
  outline-offset: 0;
}

.input[aria-invalid="true"] {
  border-color: var(--border-error);
}
```

### Accent Border (Left)
Used for callouts, quotes, and feature highlights.

```css
.callout {
  border-left: var(--border-4) solid var(--border-brand);
  padding-left: var(--space-4);
}

.callout--warning {
  border-left-color: var(--border-warning);
}

.callout--error {
  border-left-color: var(--border-error);
}

.callout--success {
  border-left-color: var(--border-success);
}
```

### Selected / Active Item
```css
.tab--active {
  border-bottom: var(--border-2) solid var(--border-active);
}

.sidebar-item--active {
  border-left: var(--border-2) solid var(--border-active);
  background: hsl(217 91% 60% / 0.08);
}
```

### Table
```css
.table {
  border: var(--border-1) solid var(--border-default);
  border-radius: var(--radius-md);
  overflow: hidden;
}

.table th {
  border-bottom: var(--border-2) solid var(--border-default);
}

.table td {
  border-bottom: var(--border-1) solid var(--border-subtle);
}
```

## Accessibility

- Focus rings must be visible on all interactive elements (minimum 2px, 3:1 contrast against adjacent colors)
- Don't rely on border color alone to convey state — pair with background color, icons, or text
- Ensure border contrast meets WCAG 1.4.11 (3:1 against adjacent colors) for all UI component boundaries
- Focus indicators must not be suppressed or hidden for keyboard users

## Usage Guidelines

### Do
- Use `--border-1` as the default weight for most elements
- Apply `--radius-md` (6px) as the standard corner radius
- Use accent borders (left 4px) for callouts and feature highlights
- Pair border color changes with other visual indicators
- Maintain visible focus indicators on all interactive elements

### Don't
- Use borders purely for decoration — every border should serve structure or interaction
- Mix multiple border radii on the same component
- Apply `--radius-full` to rectangular containers (use for pills and avatars only)
- Remove or hide focus outlines without providing an alternative
- Use overly thick borders (>4px) for UI chrome
