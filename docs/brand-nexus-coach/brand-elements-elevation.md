# Nexus Coach Elevation

> Subtle depth and layering that creates visual hierarchy without distraction.

## Strategic Foundation

**Brand Alignment:** Nexus Coach's elevation system reflects The Guide's clarity and The Architect's structure. Shadows and layering communicate hierarchy — what's important, what's interactive, and what sits above what. The approach is subtle and functional. Like a well-organized desk, every layer has a clear purpose. We avoid heavy shadows that create visual noise; instead, we use soft, barely-there depth cues that guide attention without demanding it.

## Shadow Scale

A 5-level shadow system from flat (no shadow) to highest (modal/dialog).

| Level | Name | Shadow | Token | Usage |
|-------|------|--------|-------|-------|
| 0 | Flat | none | `--shadow-none` | Flush elements, inline content |
| 1 | Low | `0 1px 2px rgba(15, 23, 42, 0.05)` | `--shadow-sm` | Subtle card lift, dropdown items |
| 2 | Medium | `0 2px 4px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04)` | `--shadow-md` | Cards, elevated containers |
| 3 | High | `0 4px 8px rgba(15, 23, 42, 0.08), 0 2px 4px rgba(15, 23, 42, 0.04)` | `--shadow-lg` | Dropdowns, popovers, floating elements |
| 4 | Higher | `0 8px 16px rgba(15, 23, 42, 0.10), 0 4px 8px rgba(15, 23, 42, 0.05)` | `--shadow-xl` | Modals, important overlays |
| 5 | Highest | `0 16px 32px rgba(15, 23, 42, 0.12), 0 8px 16px rgba(15, 23, 42, 0.06)` | `--shadow-2xl` | Full-screen overlays, critical dialogs |

### Shadow Color
All shadows use Structure Slate (`#0F172A` / `rgb(15, 23, 42)`) at low opacity. This creates cool, cohesive shadows that complement the slate-based neutral palette.

## Z-Index Scale

A structured z-index system that prevents stacking conflicts.

| Token | Value | Usage |
|-------|-------|-------|
| `--z-base` | 0 | Page content, default layer |
| `--z-raised` | 10 | Sticky elements within content |
| `--z-dropdown` | 20 | Dropdowns, select menus |
| `--z-sticky` | 30 | Sticky headers, top bar |
| `--z-sidebar` | 40 | Sidebar navigation |
| `--z-overlay` | 50 | Overlay backgrounds (scrims) |
| `--z-modal` | 60 | Modal dialogs |
| `--z-popover` | 70 | Popovers, tooltips |
| `--z-toast` | 80 | Toast notifications (topmost) |

### Stacking Context

```
┌──────────────────────────────────────┐
│ z-80: Toast Notifications            │  ← Always on top
├──────────────────────────────────────┤
│ z-70: Popovers / Tooltips           │
├──────────────────────────────────────┤
│ z-60: Modal Dialogs                 │
├──────────────────────────────────────┤
│ z-50: Overlay / Scrim               │
├──────────────────────────────────────┤
│ z-40: Sidebar Navigation            │
├──────────────────────────────────────┤
│ z-30: Sticky Top Bar                │
├──────────────────────────────────────┤
│ z-20: Dropdowns / Select Menus      │
├──────────────────────────────────────┤
│ z-10: Raised Content                │
├──────────────────────────────────────┤
│ z-0:  Page Content (base)           │
└──────────────────────────────────────┘
```

## Component Elevation Mapping

| Component | Shadow | Z-Index | Notes |
|-----------|--------|---------|-------|
| Page content | Flat | `--z-base` | No shadow |
| Cards | Low–Medium | `--z-base` | Medium on hover (interactive cards) |
| Top bar | Low | `--z-sticky` | Border-bottom preferred over shadow |
| Sidebar | Flat | `--z-sidebar` | Dark background, no shadow needed |
| Dropdowns | High | `--z-dropdown` | Clear separation from page |
| Popovers | High | `--z-popover` | Contextual overlays |
| Tooltips | High | `--z-popover` | Inline help |
| Modals | Higher | `--z-modal` | Full attention capture |
| Toast notifications | Medium | `--z-toast` | Non-blocking, topmost |
| Overlay scrim | Flat | `--z-overlay` | Background only, shadow on modal |

## Interactive Elevation

### Hover Lift
Interactive cards and elevated elements lift on hover to signal interactivity.

```css
.card-interactive {
  box-shadow: var(--shadow-sm);
  transition: box-shadow 150ms ease, transform 150ms ease;
}

.card-interactive:hover {
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}

.card-interactive:active {
  box-shadow: var(--shadow-sm);
  transform: translateY(0);
}
```

### Focus Elevation
Focus states use outline rings rather than shadow changes to maintain consistency with the focus system.

```css
.card-interactive:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

## Overlay & Scrim

### Background Scrim
For modals and full-screen overlays.

| Attribute | Value |
|-----------|-------|
| Background | `rgba(15, 23, 42, 0.5)` — 50% Structure Slate |
| Backdrop blur | `4px` (optional, for glass effect) |
| Z-index | `--z-overlay` |

```css
.scrim {
  position: fixed;
  inset: 0;
  background: rgba(15, 23, 42, 0.5);
  z-index: var(--z-overlay);
}

.scrim-blur {
  backdrop-filter: blur(4px);
}
```

## Motion & Transitions

### Elevation Transitions
All shadow and elevation changes should be animated for smooth perception.

| Property | Duration | Easing |
|----------|----------|--------|
| box-shadow | 150ms | ease |
| transform (translateY) | 150ms | ease |
| opacity (overlays) | 200ms | ease-in-out |

### Entrance Animations

| Element | Animation |
|---------|-----------|
| Dropdown | Fade in + slide down 4px, 150ms |
| Modal | Fade in + scale from 0.95, 200ms |
| Toast | Slide in from right/top, 250ms |
| Popover | Fade in + slide 4px from trigger, 150ms |

## Dark Mode

### Shadow Adjustments
On dark backgrounds, reduce shadow visibility and increase intensity.

```css
[data-theme="dark"] {
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.2);
  --shadow-md: 0 2px 4px rgba(0, 0, 0, 0.25), 0 1px 2px rgba(0, 0, 0, 0.15);
  --shadow-lg: 0 4px 8px rgba(0, 0, 0, 0.3), 0 2px 4px rgba(0, 0, 0, 0.15);
  --shadow-xl: 0 8px 16px rgba(0, 0, 0, 0.35), 0 4px 8px rgba(0, 0, 0, 0.15);
  --shadow-2xl: 0 16px 32px rgba(0, 0, 0, 0.4), 0 8px 16px rgba(0, 0, 0, 0.2);
}
```

### Dark Scrim
```css
[data-theme="dark"] .scrim {
  background: rgba(0, 0, 0, 0.6);
}
```

## CSS Tokens

```css
:root {
  /* Shadows */
  --shadow-none: none;
  --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.05);
  --shadow-md: 0 2px 4px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-lg: 0 4px 8px rgba(15, 23, 42, 0.08), 0 2px 4px rgba(15, 23, 42, 0.04);
  --shadow-xl: 0 8px 16px rgba(15, 23, 42, 0.10), 0 4px 8px rgba(15, 23, 42, 0.05);
  --shadow-2xl: 0 16px 32px rgba(15, 23, 42, 0.12), 0 8px 16px rgba(15, 23, 42, 0.06);

  /* Z-Index */
  --z-base: 0;
  --z-raised: 10;
  --z-dropdown: 20;
  --z-sticky: 30;
  --z-sidebar: 40;
  --z-overlay: 50;
  --z-modal: 60;
  --z-popover: 70;
  --z-toast: 80;

  /* Transitions */
  --transition-shadow: box-shadow 150ms ease;
  --transition-elevation: box-shadow 150ms ease, transform 150ms ease;
  --transition-overlay: opacity 200ms ease-in-out;
}
```

## Accessibility

- Elevation differences must not be the sole means of conveying hierarchy — use borders, color, or spacing as well
- Scrim overlays must trap focus within the topmost modal/dialog
- Toast notifications should use `role="status"` or `aria-live="polite"` to announce to screen readers
- Respect `prefers-reduced-motion` — disable transform animations, keep opacity transitions

## Usage Guidelines

### Do
- Use shadows sparingly — most content sits flat at Level 0
- Reserve higher elevations for temporary surfaces (dropdowns, modals, toasts)
- Animate elevation changes for smooth transitions
- Use the z-index scale to prevent stacking conflicts
- Test elevation behavior in both light and dark modes

### Don't
- Apply heavy shadows to static content
- Use shadows as decorative borders (use actual borders)
- Mix shadow and border for elevation on the same element
- Create custom z-index values outside the scale
- Use elevation to create "3D" or skeuomorphic effects
