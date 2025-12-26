# OpenLife Iconography

> Clear, purposeful icons that communicate with confident simplicity.

## Strategic Foundation

**Brand Alignment:** OpenLife's iconography reflects our commitment to clarity and openness. Icons feel approachable yet professional—simple enough to understand instantly, refined enough for enterprise contexts. The outlined style supports The Liberator archetype: direct, honest, and empowering rather than decorative.

## Icon Style

### Primary: Outlined

OpenLife uses outlined (stroke-based) icons as the primary style.

| Attribute | Value |
|-----------|-------|
| Style | Outlined / Stroke-based |
| Stroke Weight | 1.5px–2px |
| Corner Radius | 2px |
| End Caps | Rounded |
| Line Joins | Rounded |

**Rationale:**
- Outlined icons feel lighter and more transparent
- Clean lines support quick recognition
- Consistent with modern tech aesthetics
- Works on any background

### Secondary: Filled

Use filled icons for:
- Active/selected states
- Small sizes (16px or below)
- Higher visual weight needs

## Grid System

### Base Grid

```
┌────────────────────────┐
│  2px padding           │
│  ┌──────────────────┐  │
│  │                  │  │
│  │   20px × 20px    │  │
│  │   live area      │  │
│  │                  │  │
│  └──────────────────┘  │
│                        │
└────────────────────────┘
        24px × 24px
```

| Attribute | Value |
|-----------|-------|
| Canvas | 24px × 24px |
| Padding | 2px all sides |
| Live Area | 20px × 20px |

### Size Scale

| Size | Pixels | Token | Usage |
|------|--------|-------|-------|
| XS | 16px | `--icon-xs` | Dense UI, inline |
| SM | 20px | `--icon-sm` | Lists, secondary |
| MD | 24px | `--icon-md` | Standard (default) |
| LG | 32px | `--icon-lg` | Feature callouts |
| XL | 48px | `--icon-xl` | Empty states |

## Color Usage

### Icon Colors

| Context | Color | Token |
|---------|-------|-------|
| Default | Gray 600 | `--color-gray-600` |
| Interactive | Liberation Blue | `--color-primary` |
| Active | Liberation Blue | `--color-primary` |
| Hover | Foundation Navy | `--color-primary-dark` |
| Disabled | Gray 300 | `--color-gray-300` |
| Inverse | White | `--color-white` |
| Success | Progress Green | `--color-success` |
| Warning | Amber | `--color-warning` |
| Error | Red | `--color-error` |

### Guidelines
- Icons are single-color (monochromatic)
- Color reinforces meaning
- Minimum 3:1 contrast against background

## Recommended Library

### Lucide Icons

| Attribute | Value |
|-----------|-------|
| Library | Lucide Icons |
| Website | [lucide.dev](https://lucide.dev) |
| License | ISC (free commercial use) |
| Count | 1000+ icons |
| Style | Outlined, 24px, 2px stroke |

**Customization:**
- Adjust stroke to 1.5px for lighter feel
- Apply OpenLife brand colors
- Maintain 2px corner radius

### Alternatives
- Heroicons (Tailwind team)
- Phosphor Icons (multiple weights)
- Feather Icons (minimal)

## Usage Contexts

### Navigation
- **Size:** 24px (desktop), 28px (mobile)
- **Color:** Gray 600 default, Blue active
- **Style:** Outlined default, filled when active

### Actions
- **Size:** 20px–24px
- **Position:** Before or after label
- **Gap:** 8px from text

### Status
- **Size:** 16px–20px
- **Color:** Semantic (success/warning/error)
- **Pair with:** Descriptive text

### Features
- **Size:** 32px–48px
- **Background:** Optional subtle circle
- **Color:** Liberation Blue

## CSS Tokens

```css
:root {
  /* Icon Sizes */
  --icon-xs: 1rem;      /* 16px */
  --icon-sm: 1.25rem;   /* 20px */
  --icon-md: 1.5rem;    /* 24px */
  --icon-lg: 2rem;      /* 32px */
  --icon-xl: 3rem;      /* 48px */
  
  /* Icon Stroke */
  --icon-stroke: 1.5px;
}
```

## Animation

### Micro-interactions

| Animation | Duration | Easing | Usage |
|-----------|----------|--------|-------|
| Hover scale | 150ms | ease-out | Buttons |
| State change | 200ms | ease-in-out | Toggles |
| Loading spin | Continuous | linear | Progress |

### Example

```css
.icon {
  transition: transform 150ms ease-out;
}
.icon:hover {
  transform: scale(1.1);
}

@media (prefers-reduced-motion: reduce) {
  .icon { transition: none; }
}
```

## Accessibility

### Requirements
- Decorative icons: `aria-hidden="true"`
- Standalone icons: `aria-label` required
- Icons with text: Icon hidden from assistive tech
- Never rely on icons alone for meaning

### Example

```html
<!-- Decorative -->
<svg aria-hidden="true">...</svg>

<!-- Standalone button -->
<button aria-label="Close dialog">
  <svg aria-hidden="true">...</svg>
</button>

<!-- With label (preferred) -->
<button>
  <svg aria-hidden="true">...</svg>
  Download
</button>
```

## Usage Guidelines

### Do
- Use icons consistently across contexts
- Pair icons with text labels
- Maintain consistent sizing
- Use brand colors appropriately
- Test at actual sizes

### Don't
- Mix outlined and filled inconsistently
- Use icons as pure decoration
- Create overly complex icons
- Use multiple colors per icon
- Scale non-proportionally

## Examples

### Navigation Item
```html
<a href="/dashboard" class="nav-item active">
  <svg class="icon" aria-hidden="true"><!-- home icon --></svg>
  Dashboard
</a>
```

### Action Button
```html
<button class="btn-primary">
  <svg class="icon" aria-hidden="true"><!-- plus icon --></svg>
  Create Policy
</button>
```

### Status Indicator
```html
<div class="status success">
  <svg class="icon" aria-hidden="true"><!-- check icon --></svg>
  Deployment complete
</div>
```
