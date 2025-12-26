# OpenLife Border

> Visual styling for edges and boundaries that define and separate content.

## Strategic Foundation

**Brand Alignment:** OpenLife's border system creates subtle definition without visual heaviness. Borders guide the eye, separate content, and define interactive elements—supporting our commitment to clarity. Rounded corners soften the technical aesthetic, making the interface more approachable.

## Border Width

### Width Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--border-0` | 0px | No border |
| `--border-1` | 1px | Standard borders |
| `--border-2` | 2px | Emphasis, active states |
| `--border-4` | 4px | Heavy emphasis, accents |

### Default
1px is the standard border width for most applications.

## Border Radius

### Radius Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-none` | 0px | Sharp corners |
| `--radius-sm` | 4px | Small elements, chips |
| `--radius-md` | 6px | Buttons, inputs |
| `--radius-lg` | 8px | Cards, containers |
| `--radius-xl` | 12px | Larger cards, modals |
| `--radius-2xl` | 16px | Hero cards, panels |
| `--radius-full` | 9999px | Pills, avatars, circles |

### Component Defaults

| Component | Radius |
|-----------|--------|
| Button | `--radius-md` (6px) |
| Input | `--radius-md` (6px) |
| Card | `--radius-lg` (8px) |
| Modal | `--radius-xl` (12px) |
| Badge/Chip | `--radius-full` |
| Avatar | `--radius-full` |
| Tooltip | `--radius-md` (6px) |

## Border Colors

### Standard Colors

| Token | Color | Usage |
|-------|-------|-------|
| `--border-default` | Gray 200 (`#E2E8F0`) | Standard borders |
| `--border-muted` | Gray 100 (`#F1F5F9`) | Subtle dividers |
| `--border-emphasis` | Gray 300 (`#CBD5E1`) | Emphasis borders |
| `--border-strong` | Gray 400 (`#94A3B8`) | Strong definition |

### Interactive Colors

| Token | Color | Usage |
|-------|-------|-------|
| `--border-focus` | Liberation Blue (`#0066CC`) | Focus states |
| `--border-hover` | Gray 300 (`#CBD5E1`) | Hover states |
| `--border-active` | Liberation Blue (`#0066CC`) | Active states |

### Semantic Colors

| Token | Color | Usage |
|-------|-------|-------|
| `--border-success` | `#059669` | Success states |
| `--border-warning` | `#D97706` | Warning states |
| `--border-error` | `#DC2626` | Error states |
| `--border-info` | `#0284C7` | Info states |

## CSS Tokens

```css
:root {
  /* Border Widths */
  --border-0: 0px;
  --border-1: 1px;
  --border-2: 2px;
  --border-4: 4px;
  
  /* Border Radius */
  --radius-none: 0px;
  --radius-sm: 0.25rem;   /* 4px */
  --radius-md: 0.375rem;  /* 6px */
  --radius-lg: 0.5rem;    /* 8px */
  --radius-xl: 0.75rem;   /* 12px */
  --radius-2xl: 1rem;     /* 16px */
  --radius-full: 9999px;
  
  /* Border Colors */
  --border-default: #E2E8F0;
  --border-muted: #F1F5F9;
  --border-emphasis: #CBD5E1;
  --border-strong: #94A3B8;
  --border-focus: #0066CC;
}
```

## Border Patterns

### Outline (Default)
Standard visible border around elements.

```css
.card {
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
}
```

### Inset
Colored left or top border for emphasis.

```css
.callout {
  border-left: 4px solid var(--color-primary);
  padding-left: var(--space-4);
}
```

### Divider
Horizontal or vertical separator.

```css
.divider {
  border: none;
  border-top: 1px solid var(--border-default);
  margin: var(--space-4) 0;
}
```

### Focus Ring
Visible focus indicator for accessibility.

```css
.button:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.3);
}
```

## Focus States

### Standard Focus Ring
```css
:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
}
```

### Focus within Inputs
```css
.input:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.15);
}
```

### Error State
```css
.input--error {
  border-color: var(--border-error);
}
.input--error:focus {
  box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.15);
}
```

## Component Examples

### Button
```css
.button {
  border: 1px solid var(--color-primary);
  border-radius: var(--radius-md);
}
.button-outline {
  border: 1px solid var(--border-emphasis);
  background: transparent;
}
.button-outline:hover {
  border-color: var(--color-primary);
}
```

### Input
```css
.input {
  border: 1px solid var(--border-default);
  border-radius: var(--radius-md);
}
.input:hover {
  border-color: var(--border-emphasis);
}
.input:focus {
  border-color: var(--border-focus);
}
```

### Card
```css
.card {
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
}
```

### Table
```css
.table {
  border-collapse: collapse;
}
.table td,
.table th {
  border-bottom: 1px solid var(--border-default);
}
```

### Divider
```css
.divider {
  height: 1px;
  background: var(--border-default);
  margin: var(--space-6) 0;
}
```

## Dark Mode

### Adjusted Colors

```css
[data-theme="dark"] {
  --border-default: #334155;
  --border-muted: #1E293B;
  --border-emphasis: #475569;
  --border-strong: #64748B;
}
```

## Usage Guidelines

### Do
- Use subtle borders (1px, light colors)
- Apply consistent radius per component type
- Use border color for semantic meaning
- Ensure visible focus states
- Soften corners for approachability

### Don't
- Over-border—creates visual noise
- Mix radius styles inconsistently
- Use dark borders when light works
- Skip focus states
- Use sharp corners on interactive elements

## Accessibility

- Ensure focus indicators are visible (3:1 contrast minimum)
- Don't rely on color alone for state changes
- Focus rings should be visible in both themes
- Maintain visible boundaries for interactive elements

## Examples

### Card with Sections
```css
.card {
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
}
.card-header {
  border-bottom: 1px solid var(--border-default);
  padding: var(--space-4);
}
.card-body {
  padding: var(--space-4);
}
```

### Form Field
```css
.form-group {
  margin-bottom: var(--space-4);
}
.input {
  width: 100%;
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-md);
  transition: border-color 150ms ease;
}
.input:focus {
  border-color: var(--border-focus);
  box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.15);
  outline: none;
}
```

### Callout Box
```css
.callout {
  border-left: 4px solid var(--color-primary);
  background: var(--color-gray-50);
  padding: var(--space-4);
  border-radius: 0 var(--radius-md) var(--radius-md) 0;
}
.callout--warning {
  border-left-color: var(--color-warning);
  background: var(--color-warning-light);
}
```
