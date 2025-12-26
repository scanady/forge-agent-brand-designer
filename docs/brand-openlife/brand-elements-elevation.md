# OpenLife Elevation

> Layered surfaces that create depth and establish visual hierarchy.

## Strategic Foundation

**Brand Alignment:** OpenLife's elevation system creates subtle depth that guides attention without overwhelming. Elevation reinforces information hierarchy—more important or interactive elements appear "closer" to the user. The restrained approach reflects our value of clarity.

## Elevation Scale

### Shadow Definitions

| Level | Name | Shadow | Z-Index | Usage |
|-------|------|--------|---------|-------|
| 0 | Flat | none | 0 | Base surfaces |
| 1 | Low | `0 1px 2px rgba(0,0,0,0.05)` | 10 | Cards, subtle lift |
| 2 | Medium | `0 4px 6px rgba(0,0,0,0.07)` | 20 | Dropdowns, popovers |
| 3 | High | `0 10px 15px rgba(0,0,0,0.1)` | 30 | Modals, dialogs |
| 4 | Highest | `0 20px 25px rgba(0,0,0,0.15)` | 40 | Floating panels |

### Detailed Shadow Values

#### Level 1 (Low)
```css
box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
```
Cards, list items, subtle interactive states.

#### Level 2 (Medium)
```css
box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07),
            0 2px 4px -1px rgba(0, 0, 0, 0.04);
```
Dropdowns, popovers, tooltips, floating buttons.

#### Level 3 (High)
```css
box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
            0 4px 6px -2px rgba(0, 0, 0, 0.05);
```
Modals, dialogs, side panels.

#### Level 4 (Highest)
```css
box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
            0 10px 10px -5px rgba(0, 0, 0, 0.04);
```
Full-screen overlays, priority notifications.

## Z-Index Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--z-base` | 0 | Page content |
| `--z-raised` | 10 | Cards, slightly elevated |
| `--z-dropdown` | 20 | Dropdowns, popovers |
| `--z-sticky` | 30 | Sticky headers, nav |
| `--z-modal` | 40 | Modals, dialogs |
| `--z-popover` | 50 | Tooltips over modals |
| `--z-toast` | 60 | Toast notifications |
| `--z-max` | 100 | Top-priority overlays |

## CSS Tokens

```css
:root {
  /* Shadows */
  --shadow-none: none;
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07),
               0 2px 4px -1px rgba(0, 0, 0, 0.04);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
               0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
               0 10px 10px -5px rgba(0, 0, 0, 0.04);
  
  /* Z-Index */
  --z-base: 0;
  --z-raised: 10;
  --z-dropdown: 20;
  --z-sticky: 30;
  --z-modal: 40;
  --z-popover: 50;
  --z-toast: 60;
  --z-max: 100;
}
```

## Layer Hierarchy

### Stacking Contexts

```
┌─────────────────────────────────────┐ z-toast (60)
│  Toast Notifications                │
├─────────────────────────────────────┤ z-popover (50)
│  Tooltips, Popovers over Modals     │
├─────────────────────────────────────┤ z-modal (40)
│  Modals, Dialogs                    │
├─────────────────────────────────────┤ z-sticky (30)
│  Sticky Header, Navigation          │
├─────────────────────────────────────┤ z-dropdown (20)
│  Dropdowns, Select Menus            │
├─────────────────────────────────────┤ z-raised (10)
│  Cards, Panels                      │
├─────────────────────────────────────┤ z-base (0)
│  Page Content                       │
└─────────────────────────────────────┘
```

## Usage by Component

| Component | Shadow | Z-Index |
|-----------|--------|---------|
| Card | `--shadow-sm` | `--z-raised` |
| Button (hover) | `--shadow-md` | `--z-raised` |
| Dropdown menu | `--shadow-md` | `--z-dropdown` |
| Tooltip | `--shadow-md` | `--z-popover` |
| Modal | `--shadow-lg` | `--z-modal` |
| Dialog | `--shadow-lg` | `--z-modal` |
| Toast | `--shadow-lg` | `--z-toast` |
| Sticky header | `--shadow-sm` | `--z-sticky` |
| Floating button | `--shadow-lg` | `--z-dropdown` |

## Dark Mode

### Adjusted Shadows
In dark mode, shadows are less visible. Use:
- Lighter borders for definition
- Reduced opacity shadows
- Background color differentiation

```css
[data-theme="dark"] {
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
}
```

### Alternative: Border Definition
```css
[data-theme="dark"] .card {
  box-shadow: none;
  border: 1px solid var(--color-gray-700);
}
```

## Motion & Elevation

### Elevation Transitions
When elevation changes (e.g., on hover), animate smoothly.

```css
.card {
  box-shadow: var(--shadow-sm);
  transition: box-shadow 200ms ease-out;
}
.card:hover {
  box-shadow: var(--shadow-md);
}
```

### Focus States
Elevate focused elements slightly for visibility.

```css
.button:focus-visible {
  box-shadow: var(--shadow-md), 0 0 0 3px rgba(0, 102, 204, 0.3);
}
```

## Overlays

### Background Overlays
For modals and dialogs, use a semi-transparent backdrop.

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(13, 27, 42, 0.5);
  z-index: calc(var(--z-modal) - 1);
}
```

### Scrim Opacity
| Context | Opacity |
|---------|---------|
| Light overlay | 30% |
| Standard modal | 50% |
| Critical dialog | 70% |

## Usage Guidelines

### Do
- Use elevation to indicate interactivity
- Apply consistent shadows per component type
- Increase elevation for overlapping elements
- Animate elevation changes smoothly
- Consider dark mode alternatives

### Don't
- Over-elevate—too many shadows create noise
- Use inconsistent shadow styles
- Skip z-index management (leads to bugs)
- Animate elevation excessively
- Forget about accessibility focus states

## Accessibility

- Don't rely on shadows alone for interactive states
- Ensure elevated elements are keyboard accessible
- Focus trapping for modals
- Proper ARIA roles for overlay content
- Maintain sufficient contrast with shadows

## Examples

### Card with Hover
```css
.card {
  background: var(--color-white);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  box-shadow: var(--shadow-sm);
  transition: box-shadow 200ms ease-out, transform 200ms ease-out;
}
.card:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-2px);
}
```

### Dropdown Menu
```css
.dropdown {
  position: absolute;
  background: var(--color-white);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-md);
  z-index: var(--z-dropdown);
}
```

### Modal
```css
.modal {
  position: fixed;
  background: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  z-index: var(--z-modal);
}
```
