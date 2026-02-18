# OpenLife Iconography

> Simple, universal icons designed for clarity and quick comprehension.

## Icon Principles

Follow these principles to design and use OpenLife icons consistently.

### Design for Universal Understanding

Use widely recognized symbols and established visual metaphors. Ensure icons are easily understood by a diverse audience—avoid cultural or language-specific elements that may confuse users.

### Balance Simplicity and Clarity

Icons should be simple enough for instant recognition, yet detailed enough to convey meaning at small sizes. The goal is quick comprehension—excess detail distracts.

### Maintain Visual Harmony

All icons work together as a cohesive system. Adhere to consistent size, shape, and style guidelines across the entire set.

### Use Icons Intentionally

Icons aid comprehension and navigation, but can add clutter when overused. Always pair icons with text labels where possible. Don't use icons where they aren't necessary.

## Visual Style

OpenLife icons use a **1.5px stroke weight** with shapes that pair **rounded exterior corners** with **sharp interior corners** and **square end caps**. This creates a clean, flat, professional appearance.

### Core Specifications

| Attribute | Value |
|-----------|-------|
| Stroke Weight | 1.5px |
| Exterior Corners | Rounded (2px radius) |
| Interior Corners | Sharp (no radius) |
| End Caps | Square (not rounded) |
| Perspective | Flat / straight-on |
| Style | Monochromatic, single color |

### Simplicity

Use simplified shapes with the minimum detail required to express a concept. Fine details are hard to see at small sizes.

| ✓ Do | ✗ Don't |
|------|---------|
| Use simple shapes with minimum detail | Add excess detail that reduces legibility |
| Use familiar symbols with clear associations | Create icons that could be confused with other concepts |
| Reuse existing metaphors for consistency | Create new icons when suitable ones exist |

### Perspective

All icons should appear **flat and straight-on**. Avoid diagonal perspectives or 3D shapes—these are hard to discern at a glance, especially for users with cognitive disabilities.

| ✓ Do | ✗ Don't |
|------|---------|
| Use shapes that appear straight-on | Use diagonal perspectives to create 3D effects |
| Keep icons flat without dimensionality | Add shadows or gradients for depth |

### Corners and End Caps

| Element | Style |
|---------|-------|
| Exterior corners | Rounded (2px radius) |
| Interior angles | Sharp (no radius) |
| End points | Square / flat (not rounded) |

Square end caps ensure paths align with pixel edges, preventing blurry rendering. Internal sharp angles maintain clarity and legibility.

## Size System

Icons are drawn within a **16×16px bounding box** and are available in two primary sizes.

### Icon Sizes

| Size | Pixels | Token | Usage |
|------|--------|-------|-------|
| Medium | 16px | `--icon-md` | Default size for most UI contexts |
| Small | 12px | `--icon-sm` | Compact elements, secondary actions |

### Medium Icons (16px) — Default

Use 16px icons in most cases. This size balances well with body text and standard UI density.

- Navigation items
- Buttons and actions
- Form elements
- List items
- Status indicators

### Small Icons (12px) — Use Sparingly

12px icons are downscaled from 16px and should be used sparingly due to reduced legibility.

**Appropriate uses:**
- Chevrons in buttons and dropdowns
- Field validation messaging (info, warning, error)
- Tags, badges, and compact status indicators
- Secondary/supporting actions
- Inline metadata

### Decorative Icon Tiles

When larger icons are needed for decorative purposes (empty states, feature highlights), place icons on a colored background tile rather than scaling up the icon.

| Tile Size | Icon Size | Usage |
|-----------|-----------|-------|
| 32px | 16px | Cards, list headers |
| 48px | 24px | Feature callouts |
| 64px | 32px | Empty states, onboarding |

## Color Usage

Icons use design tokens for colors to ensure consistency and accessibility.

### Icon Color Tokens

| Context | Color | Token |
|---------|-------|-------|
| Default | Gray 600 | `--color-icon-default` |
| Subtle | Gray 500 | `--color-icon-subtle` |
| Primary | Liberation Blue | `--color-icon-primary` |
| Success | Green | `--color-icon-success` |
| Warning | Amber | `--color-icon-warning` |
| Error | Red | `--color-icon-error` |
| Disabled | Gray 300 | `--color-icon-disabled` |
| Inverse | White | `--color-icon-inverse` |

### Color Guidelines

- Icons are **monochromatic** (single color only)
- Match icon color to adjacent text when paired
- Ensure minimum **3:1 contrast** against background
- Use semantic colors to reinforce meaning (success, warning, error)

## Recommended Library

### Lucide Icons

OpenLife uses **Lucide Icons** as the primary icon library for its clean, consistent, flat design.

| Attribute | Value |
|-----------|-------|
| Library | Lucide Icons |
| Website | [lucide.dev](https://lucide.dev) |
| License | ISC (free for commercial use) |
| Icon Count | 1,400+ icons |
| Default Size | 24px |

**Customization for OpenLife:**
- Set stroke-width to `1.5` for standard weight
- Apply OpenLife color tokens
- Use 16px as default rendered size

### Installation

```bash
npm install lucide-react
# or
npm install lucide
```

### Usage

```jsx
import { Home, Settings, User } from 'lucide-react';

<Home size={16} strokeWidth={1.5} />
<Settings size={16} strokeWidth={1.5} />
<User size={16} strokeWidth={1.5} />
```

```html
<!-- HTML with Lucide CDN -->
<i data-lucide="home" style="width: 16px; height: 16px;"></i>
<script src="https://unpkg.com/lucide@latest"></script>
<script>lucide.createIcons();</script>
```

## Icon Reference

A curated set of standard icons for consistent OpenLife interfaces.

### Navigation

| Icon | Name | Usage |
|------|------|-------|
| Home | `home` | Home / Dashboard |
| Layout Dashboard | `layout-dashboard` | Dashboard view |
| Bar Chart | `bar-chart-2` | Analytics / Reports |
| Package | `package` | Products |
| File Text | `file-text` | Documents |
| Settings | `settings` | Settings / Preferences |
| User | `user` | Profile / Account |
| Users | `users` | Team / Users |
| Bell | `bell` | Notifications |
| Help Circle | `help-circle` | Help / Support |
| Search | `search` | Search |

### Actions

| Icon | Name | Usage |
|------|------|-------|
| Plus | `plus` | Add / Create |
| Pencil | `pencil` | Edit |
| Trash 2 | `trash-2` | Delete |
| Copy | `copy` | Copy / Duplicate |
| Download | `download` | Download |
| Upload | `upload` | Upload |
| External Link | `external-link` | Open external |
| Refresh CW | `refresh-cw` | Refresh |
| X | `x` | Close / Cancel |
| Check | `check` | Confirm / Complete |

### Status

| Icon | Name | Usage |
|------|------|-------|
| Check Circle | `check-circle` | Success |
| X Circle | `x-circle` | Error |
| Alert Triangle | `alert-triangle` | Warning |
| Info | `info` | Information |
| Clock | `clock` | Pending / Time |
| Lock | `lock` | Locked / Secure |
| Unlock | `unlock` | Unlocked |
| Eye | `eye` | Visible |
| Eye Off | `eye-off` | Hidden |

### UI Controls

| Icon | Name | Usage |
|------|------|-------|
| Chevron Down | `chevron-down` | Dropdown / Expand |
| Chevron Right | `chevron-right` | Navigate / Breadcrumb |
| Chevron Left | `chevron-left` | Back |
| Chevron Up | `chevron-up` | Collapse |
| More Horizontal | `more-horizontal` | More actions |
| More Vertical | `more-vertical` | More actions (vertical) |
| Menu | `menu` | Menu toggle |
| Arrow Left | `arrow-left` | Back navigation |
| Arrow Right | `arrow-right` | Forward navigation |

### Data & Content

| Icon | Name | Usage |
|------|------|-------|
| Trending Up | `trending-up` | Increase |
| Trending Down | `trending-down` | Decrease |
| Folder | `folder` | Folder |
| File | `file` | File |
| Calendar | `calendar` | Date |
| Tag | `tag` | Tag / Label |
| Link | `link` | Link |
| Clipboard | `clipboard` | Clipboard |

## CSS Tokens

```css
:root {
  /* Icon Sizes */
  --icon-sm: 0.75rem;   /* 12px */
  --icon-md: 1rem;      /* 16px */
  
  /* Decorative Tile Sizes */
  --icon-tile-sm: 2rem;    /* 32px */
  --icon-tile-md: 3rem;    /* 48px */
  --icon-tile-lg: 4rem;    /* 64px */
  
  /* Icon Stroke */
  --icon-stroke: 1.5;
  
  /* Icon Colors */
  --color-icon-default: var(--color-gray-600);
  --color-icon-subtle: var(--color-gray-500);
  --color-icon-primary: var(--color-primary);
  --color-icon-success: var(--color-success);
  --color-icon-warning: var(--color-warning);
  --color-icon-error: var(--color-error);
  --color-icon-disabled: var(--color-gray-300);
  --color-icon-inverse: var(--color-white);
}
```

## Accessibility

### Requirements

| Scenario | Implementation |
|----------|----------------|
| Decorative icon | `aria-hidden="true"` |
| Icon-only button | `aria-label` on button |
| Icon with text label | Icon hidden from assistive tech |
| Status icon | Include text alternative |

### Examples

```html
<!-- Decorative icon (hidden from screen readers) -->
<svg aria-hidden="true" class="icon">...</svg>

<!-- Icon-only button -->
<button aria-label="Close dialog">
  <svg aria-hidden="true">...</svg>
</button>

<!-- Icon with visible label (preferred) -->
<button>
  <svg aria-hidden="true">...</svg>
  Download
</button>

<!-- Status with redundant text -->
<div class="status status-success">
  <svg aria-hidden="true">...</svg>
  <span>Saved successfully</span>
</div>
```

### Key Guidelines

- **Never rely on icons alone** to convey meaning
- Always provide text alternatives for critical information
- Use semantic colors with accompanying text for status
- Test with screen readers to ensure icons don't add noise

## Usage Guidelines

### Do

- Use icons from the standard library consistently
- Pair icons with text labels wherever possible
- Maintain the 1.5px stroke weight
- Use 16px as the default size
- Apply brand color tokens
- Test at actual rendered sizes

### Don't

- Create custom icons when standard ones exist
- Use icons purely for decoration
- Mix different icon styles or libraries
- Add multiple colors to a single icon
- Scale icons disproportionally
- Use 3D effects, shadows, or gradients

## Examples

### Navigation Item

```html
<a href="/dashboard" class="nav-item active">
  <i data-lucide="layout-dashboard" aria-hidden="true"></i>
  Dashboard
</a>
```

### Button with Icon

```html
<button class="btn btn-primary">
  <i data-lucide="plus" aria-hidden="true"></i>
  Create Product
</button>
```

### Status Indicator

```html
<div class="status status-success">
  <i data-lucide="check-circle" aria-hidden="true"></i>
  Changes saved
</div>
```

### Icon Tile (Decorative)

```html
<div class="icon-tile icon-tile-md">
  <i data-lucide="package" aria-hidden="true"></i>
</div>
```

```css
.icon-tile {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-lg);
  background: rgba(0, 102, 204, 0.1);
  color: var(--color-primary);
}

.icon-tile-md {
  width: var(--icon-tile-md);
  height: var(--icon-tile-md);
}

.icon-tile i, .icon-tile svg {
  width: 50%;
  height: 50%;
}
```
