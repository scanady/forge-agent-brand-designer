# Nexus Coach Border

> Clean, purposeful borders that define structure without adding visual noise.

## Strategic Foundation

**Brand Alignment:** Nexus Coach borders reflect The Architect's precision — clean lines that create order and separation without drawing attention to themselves. Borders define structure: where a card ends, where a section begins, where input fields sit. Like the operational framework Nexus Coach provides, borders are invisible when they work well — you notice their absence, not their presence.

## Border Width

| Token | Value | Usage |
|-------|-------|-------|
| `--border-0` | 0px | No border |
| `--border-1` | 1px | Standard borders (default) |
| `--border-2` | 2px | Emphasis borders, focus states |
| `--border-4` | 4px | Heavy accent borders, section indicators |

### Default
1px is the default border width for all standard UI elements. Use thicker borders only for emphasis or interactive states.

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-none` | 0px | Sharp edges, table cells |
| `--radius-sm` | 4px | Inline badges, small inputs |
| `--radius-md` | 6px | Buttons, form inputs, cards (default) |
| `--radius-lg` | 8px | Cards, modals, larger containers |
| `--radius-xl` | 12px | Featured cards, hero elements |
| `--radius-2xl` | 16px | Marketing sections, large panels |
| `--radius-full` | 9999px | Circles, pills, avatar badges |

### Component Radius Defaults

| Component | Radius Token |
|-----------|-------------|
| Buttons | `--radius-md` (6px) |
| Form inputs | `--radius-md` (6px) |
| Cards | `--radius-lg` (8px) |
| Modals | `--radius-xl` (12px) |
| Dropdowns | `--radius-md` (6px) |
| Badges | `--radius-full` (pill) |
| Avatars | `--radius-full` (circle) |
| Tooltips | `--radius-md` (6px) |
| Toast notifications | `--radius-lg` (8px) |
| Navigation items | `--radius-md` (6px) |
| Tags / Chips | `--radius-full` (pill) |
| Table rows | `--radius-none` (0px) |

## Border Colors

### Standard Borders

| Token | HEX | Usage |
|-------|-----|-------|
| `--border-default` | `#E2E8F0` (Slate 200) | Default borders, dividers, card outlines |
| `--border-muted` | `#F1F5F9` (Slate 100) | Subtle separators, inner borders |
| `--border-emphasis` | `#CBD5E1` (Slate 300) | Higher contrast borders, table headers |

### Interactive Borders

| Token | HEX | Usage |
|-------|-----|-------|
| `--border-focus` | `#0F766E` (Guide Teal) | Focus ring on interactive elements |
| `--border-hover` | `#94A3B8` (Slate 400) | Hover state on bordered elements |
| `--border-active` | `#0F766E` (Guide Teal) | Active/selected input borders |

### Semantic Borders

| Token | HEX | Usage |
|-------|-----|-------|
| `--border-success` | `#059669` | Success state borders |
| `--border-warning` | `#D97706` | Warning state borders |
| `--border-error` | `#DC2626` | Error state borders |
| `--border-info` | `#0284C7` | Information state borders |

## Focus States

All interactive elements use a consistent focus ring pattern.

```css
:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
}
```

### Input Focus

```css
.input:focus {
  border-color: var(--border-active);
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.15);
  outline: none;
}
```

### Error + Focus

```css
.input-error:focus {
  border-color: var(--border-error);
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.15);
  outline: none;
}
```

## Common Border Patterns

### Card

```css
.card {
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  background: var(--color-white);
}
```

### Interactive Card

```css
.card-interactive {
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  transition: border-color 150ms ease;
}

.card-interactive:hover {
  border-color: var(--border-hover);
}
```

### Divider

```css
.divider {
  border: 0;
  border-top: 1px solid var(--border-default);
  margin: var(--space-6) 0;
}

.divider-subtle {
  border-top-color: var(--border-muted);
}
```

### Form Input

```css
.input {
  border: 1px solid var(--border-default);
  border-radius: var(--radius-md);
  padding: 10px 12px;
  transition: border-color 150ms ease, box-shadow 150ms ease;
}

.input:hover {
  border-color: var(--border-hover);
}

.input:focus {
  border-color: var(--border-active);
  box-shadow: 0 0 0 3px rgba(15, 118, 110, 0.15);
  outline: none;
}

.input-error {
  border-color: var(--border-error);
}
```

### Accent Border (Left)
For callout boxes, feature highlights, and section indicators.

```css
.callout {
  border-left: 4px solid var(--color-primary);
  padding: var(--space-4) var(--space-6);
  background: var(--color-teal-50);
  border-radius: 0 var(--radius-md) var(--radius-md) 0;
}

.callout-warning {
  border-left-color: var(--color-warning);
  background: var(--color-warning-light);
}

.callout-error {
  border-left-color: var(--color-error);
  background: var(--color-error-light);
}
```

### Selected / Active State

```css
.item-selected {
  border-color: var(--color-primary);
  background: var(--color-teal-50);
}
```

## CSS Tokens

```css
:root {
  /* Border Width */
  --border-0: 0px;
  --border-1: 1px;
  --border-2: 2px;
  --border-4: 4px;

  /* Border Radius */
  --radius-none: 0px;
  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
  --radius-xl: 12px;
  --radius-2xl: 16px;
  --radius-full: 9999px;

  /* Border Colors */
  --border-default: #E2E8F0;
  --border-muted: #F1F5F9;
  --border-emphasis: #CBD5E1;
  --border-focus: #0F766E;
  --border-hover: #94A3B8;
  --border-active: #0F766E;
  --border-success: #059669;
  --border-warning: #D97706;
  --border-error: #DC2626;
  --border-info: #0284C7;
}
```

## Dark Mode

```css
[data-theme="dark"] {
  --border-default: #334155;
  --border-muted: #1E293B;
  --border-emphasis: #475569;
  --border-focus: #14B8A6;
  --border-hover: #64748B;
  --border-active: #14B8A6;
}
```

## Accessibility

- Focus rings must be visible against all backgrounds — the 2px outline with 2px offset ensures visibility
- Border color changes must not be the sole indicator of state — pair with icons, text, or background changes
- Ensure bordered elements have sufficient contrast (3:1 minimum for UI components per WCAG 2.1)
- Focus indicators must not be suppressed or hidden on interactive elements

## Usage Guidelines

### Do
- Use 1px borders as the default for all structural boundaries
- Apply `--radius-md` as the default radius for interactive elements
- Use focus rings consistently on all interactive elements
- Apply semantic border colors only for semantic states (error, success, warning)
- Use accent borders (left border) for callouts and emphasis

### Don't
- Use thick borders (4px) for standard UI elements — reserve for accents
- Mix border-radius scales within the same component group
- Apply border-radius to table rows or cells (use `--radius-none`)
- Use border color as the only indicator of state change
- Remove or override focus indicators for aesthetic reasons
