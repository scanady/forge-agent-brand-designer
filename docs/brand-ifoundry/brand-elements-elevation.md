# iFoundry Media Elevation

> Layered surfaces that create depth and hierarchy, guiding attention through engineered precision.

## Strategic Foundation

**Brand Alignment:** iFoundry's elevation system reflects The Builder's understanding of structure and layering. Like well-architected software, the UI has clear layers — each surface at a deliberate depth. Elevation communicates hierarchy and interactive affordance without decoration. Shadows use Iron Slate (`#0F172A`) as their base to maintain the cool, professional tone of the brand.

## Shadow Definitions

iFoundry uses a 5-level elevation scale. Shadows are composed of multiple layers for natural depth.

### Elevation Scale

| Level | Token | Y-Offset | Blur | Spread | Opacity | Use Case |
|-------|-------|----------|------|--------|---------|----------|
| 0 | `--elevation-0` | 0 | 0 | 0 | 0% | Flat (flush with canvas) |
| 1 | `--elevation-1` | 1px | 3px | 0 | 5% | Subtle lift — cards, tiles |
| 2 | `--elevation-2` | 2px | 8px | -1px | 8% | Raised — hover states, dropdowns |
| 3 | `--elevation-3` | 4px | 16px | -2px | 12% | Floating — popovers, menus |
| 4 | `--elevation-4` | 8px | 24px | -4px | 16% | Overlay — modals, dialogs |
| 5 | `--elevation-5` | 16px | 48px | -8px | 20% | Highest — command palette, toasts |

### CSS Tokens

```css
:root {
  --shadow-color: 222 47% 11%;  /* Iron Slate #0F172A in HSL */

  --elevation-0: none;
  --elevation-1: 0 1px 3px 0 hsl(var(--shadow-color) / 0.05),
                 0 1px 2px -1px hsl(var(--shadow-color) / 0.05);
  --elevation-2: 0 2px 8px -1px hsl(var(--shadow-color) / 0.08),
                 0 1px 3px -1px hsl(var(--shadow-color) / 0.04);
  --elevation-3: 0 4px 16px -2px hsl(var(--shadow-color) / 0.12),
                 0 2px 6px -2px hsl(var(--shadow-color) / 0.06);
  --elevation-4: 0 8px 24px -4px hsl(var(--shadow-color) / 0.16),
                 0 4px 12px -4px hsl(var(--shadow-color) / 0.08);
  --elevation-5: 0 16px 48px -8px hsl(var(--shadow-color) / 0.20),
                 0 8px 24px -8px hsl(var(--shadow-color) / 0.10);
}
```

## Z-Index Scale

A predictable z-index scale prevents conflicts across layers.

| Token | Value | Use Case |
|-------|-------|----------|
| `--z-base` | 0 | Default content layer |
| `--z-raised` | 10 | Cards, raised surfaces |
| `--z-dropdown` | 100 | Dropdowns, menus |
| `--z-sticky` | 200 | Sticky headers, sidebars |
| `--z-overlay` | 300 | Overlays, scrims |
| `--z-modal` | 400 | Modals, dialogs |
| `--z-popover` | 500 | Popovers, tooltips |
| `--z-toast` | 600 | Toast notifications |
| `--z-command` | 700 | Command palette |

```css
:root {
  --z-base: 0;
  --z-raised: 10;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-overlay: 300;
  --z-modal: 400;
  --z-popover: 500;
  --z-toast: 600;
  --z-command: 700;
}
```

## Component Elevation Mapping

| Component | Resting | Hover | Active |
|-----------|---------|-------|--------|
| Page Canvas | 0 | — | — |
| Card | 1 | 2 | 1 |
| Button (Primary) | 1 | 2 | 0 |
| Button (Secondary) | 0 | 1 | 0 |
| Input Field | 0 | 0 | 0 |
| Sidebar Navigation | 0 | — | — |
| Top Bar | 1 | — | — |
| Dropdown Menu | 3 | — | — |
| Tooltip | 3 | — | — |
| Popover | 3 | — | — |
| Modal / Dialog | 4 | — | — |
| Toast | 5 | — | — |
| Command Palette | 5 | — | — |

## Interactive Elevation

### Hover Lift
Cards and interactive surfaces gain one elevation level on hover.

```css
.card {
  box-shadow: var(--elevation-1);
  transition: box-shadow 150ms ease-out;
}

.card:hover {
  box-shadow: var(--elevation-2);
}
```

### Press
Interactive elements drop to a lower elevation on press to reinforce tactile feedback.

```css
.button-primary {
  box-shadow: var(--elevation-1);
  transition: box-shadow 100ms ease-out;
}

.button-primary:hover {
  box-shadow: var(--elevation-2);
}

.button-primary:active {
  box-shadow: var(--elevation-0);
}
```

## Overlay & Scrim

Overlays use a semi-transparent scrim to separate floating surfaces from the content layer beneath.

| Element | Background | Backdrop |
|---------|------------|----------|
| Modal Scrim | `hsl(222 47% 11% / 0.5)` | `blur(4px)` |
| Dropdown Scrim | None | None |
| Command Palette | `hsl(222 47% 11% / 0.6)` | `blur(8px)` |
| Drawer Overlay | `hsl(222 47% 11% / 0.4)` | `blur(2px)` |

```css
.scrim {
  position: fixed;
  inset: 0;
  background: hsl(222 47% 11% / 0.5);
  backdrop-filter: blur(4px);
  z-index: var(--z-overlay);
}
```

## Dark Mode Shadows

In dark mode, shadows become subtler because the base surface is already dark. Use reduced opacity and add a faint light-edge (inset highlight) to create separation.

```css
[data-theme="dark"] {
  --shadow-color: 222 47% 5%;

  --elevation-1: 0 1px 3px 0 hsl(var(--shadow-color) / 0.3),
                 inset 0 1px 0 0 hsl(0 0% 100% / 0.04);
  --elevation-2: 0 2px 8px -1px hsl(var(--shadow-color) / 0.4),
                 inset 0 1px 0 0 hsl(0 0% 100% / 0.04);
  --elevation-3: 0 4px 16px -2px hsl(var(--shadow-color) / 0.5),
                 inset 0 1px 0 0 hsl(0 0% 100% / 0.04);
  --elevation-4: 0 8px 24px -4px hsl(var(--shadow-color) / 0.6),
                 inset 0 1px 0 0 hsl(0 0% 100% / 0.04);
  --elevation-5: 0 16px 48px -8px hsl(var(--shadow-color) / 0.7),
                 inset 0 1px 0 0 hsl(0 0% 100% / 0.04);
}
```

## Accessibility

- Never rely on elevation alone to communicate interactive states — pair with color, border, or icon changes
- Ensure sufficient contrast between surfaces at adjacent elevation levels
- Scrim opacity must allow users to identify that background content is obscured (not interactive)
- Respect `prefers-reduced-transparency` by using solid backgrounds instead of scrims where possible

## Usage Guidelines

### Do
- Use consistent elevation levels from the defined scale
- Transition smoothly between elevation states (150ms ease-out)
- Apply hover lift only to interactive surfaces (cards with actions, buttons)
- Use the z-index scale to prevent stacking conflicts

### Don't
- Invent custom shadow values outside the elevation scale
- Apply elevation to static, non-interactive text blocks
- Stack multiple elevated surfaces at the same z-index
- Use elevation changes without transition animations
- Apply hover lift to non-interactive content
