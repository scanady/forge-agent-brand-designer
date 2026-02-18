# OpenLife UI Components

> Modern, accessible components that create intuitive and professional interfaces.

## Strategic Foundation

**Brand Alignment:** OpenLife's UI components embody our Liberator archetype—they are clear, direct, and empowering. Every component is designed to reduce complexity, guide users confidently through workflows, and create a professional yet approachable experience. Our components prioritize accessibility, consistency, and modern design aesthetics.

## Navigation System

OpenLife uses a structured navigation system that combines a persistent sidebar for primary navigation with contextual breadcrumbs for location awareness.

### Navigation Architecture

| Layer | Purpose | Position |
|-------|---------|----------|
| Top Bar | Global actions, search, user menu | Fixed top |
| Side Navigation | Primary app navigation | Fixed left |
| Breadcrumbs | Hierarchical location | Page header |
| Tabs | Content-level navigation | Within page |

### Side Navigation

The primary navigation for OpenLife applications. A dark-themed vertical sidebar provides consistent access to all major sections.

#### Structure

```
┌────────────────────────┐
│  Logo + Brand          │  ← Brand identity
├────────────────────────┤
│  Primary Navigation    │  ← Main sections
│  ├─ Dashboard          │
│  ├─ Products           │
│  └─ Analytics          │
├────────────────────────┤
│  Secondary Navigation  │  ← Supporting sections
│  ├─ Settings           │
│  └─ Help               │
├────────────────────────┤
│  User / AI Actions     │  ← Bottom actions
└────────────────────────┘
```

#### Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Width | 260px | `--sidebar-width` |
| Background | Foundation Navy | `--color-primary-dark` |
| Text Color | Gray 300 | `--color-gray-300` |
| Active Color | White | `--color-white` |
| Padding | 24px | `--space-6` |

#### Navigation Item States

| State | Background | Text | Icon |
|-------|------------|------|------|
| Default | Transparent | Gray 300 | Gray 400 |
| Hover | White 8% opacity | White | White |
| Active | Liberation Blue | White | White |
| Focused | White 8% opacity + ring | White | White |
| Disabled | Transparent | Gray 500 | Gray 500 |

#### CSS Implementation

```css
.nav-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3);
  border-radius: var(--radius-md);
  color: var(--color-gray-300);
  text-decoration: none;
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  transition: all 150ms ease;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.08);
  color: var(--color-white);
}

.nav-item.active {
  background: var(--color-primary);
  color: var(--color-white);
}

.nav-item:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

.nav-item svg {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}
```

### Top Navigation Bar

A horizontal bar for global actions, search, and user-related controls.

#### Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Height | 64px | `--header-height` |
| Background | White | `--color-white` |
| Border | 1px solid Gray 200 | `--border-default` |
| Padding | 16px 24px | `--space-4` `--space-6` |
| Position | Sticky top | `z-index: 30` |

#### Components

| Component | Position | Function |
|-----------|----------|----------|
| Search | Left/Center | Global search |
| Notifications | Right | Alert indicator |
| Help | Right | Support access |
| User Menu | Right | Account actions |

### Navigation Sections

Organize navigation items into logical groups with section headers.

| Attribute | Value |
|-----------|-------|
| Section Title | Uppercase, 12px, Gray 400, 0.05em tracking |
| Section Gap | 24px between sections |
| Item Gap | 4px between items |

```css
.nav-section {
  margin-bottom: var(--space-6);
}

.nav-section-title {
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-gray-400);
  margin-bottom: var(--space-2);
  padding: 0 var(--space-3);
}
```

## Breadcrumbs

Breadcrumbs show the user's location within the application hierarchy and provide quick navigation to parent pages.

### Purpose

- **Location awareness:** Help users understand where they are
- **Quick navigation:** Enable jumping to parent sections
- **Reduce cognitive load:** Show hierarchy without overwhelming

### Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Font Size | 14px | `--text-sm` |
| Text Color | Gray 600 | `--color-gray-600` |
| Link Color | Liberation Blue | `--color-primary` |
| Separator | Chevron right, 16px | `--icon-xs` |
| Gap | 8px | `--space-2` |
| Margin Bottom | 24px | `--space-6` |

### Structure

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li><a href="/home">Home</a></li>
    <li><a href="/products">Products</a></li>
    <li><a href="/products/term-life">Term Life</a></li>
    <li aria-current="page">Edit Coverage</li>
  </ol>
</nav>
```

### Behavior

| Scenario | Behavior |
|----------|----------|
| 8+ items | Auto-collapse with ellipsis button |
| Long text | Truncate with tooltip at 200px max |
| Last item | Non-interactive, current page indicator |
| Overflow | Wrap to next line when expanded |

### Collapse Rules

| Visible Items | Before Collapse | After Collapse |
|---------------|-----------------|----------------|
| ≤8 items | All visible | N/A |
| >8 items | First + Last | Ellipsis between |

### CSS Implementation

```css
.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-6);
  font-size: var(--text-sm);
  color: var(--color-gray-600);
  list-style: none;
  padding: 0;
  margin: 0;
}

.breadcrumb li {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.breadcrumb li:not(:last-child)::after {
  content: '';
  display: block;
  width: 16px;
  height: 16px;
  background: url('chevron-right.svg') center/contain no-repeat;
  opacity: 0.5;
}

.breadcrumb a {
  color: var(--color-primary);
  text-decoration: none;
  max-width: 200px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.breadcrumb a:hover {
  text-decoration: underline;
}

.breadcrumb a:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}

.breadcrumb [aria-current="page"] {
  color: var(--color-gray-800);
  font-weight: var(--font-medium);
}
```

### With Icons

Breadcrumb items can include icons for additional context:

```html
<li>
  <a href="/products">
    <svg class="breadcrumb-icon" aria-hidden="true">...</svg>
    Products
  </a>
</li>
```

```css
.breadcrumb-icon {
  width: 16px;
  height: 16px;
  margin-right: var(--space-1);
}
```

## Menu Components

Menus provide lists of actions or navigation options. OpenLife uses structured menus with clear hierarchy and visual organization.

### Menu Types

| Type | Use Case | Trigger |
|------|----------|---------|
| Dropdown Menu | Actions list | Button click |
| Context Menu | Right-click actions | Right-click |
| Navigation Menu | Section navigation | Hover/Click |

### Dropdown Menu

A triggered overlay containing a list of actions.

#### Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Min Width | 160px | — |
| Max Width | 320px | — |
| Max Height | Viewport - 32px | — |
| Background | White | `--color-white` |
| Border | 1px solid Gray 200 | `--border-default` |
| Border Radius | 8px | `--radius-lg` |
| Shadow | Large | `--shadow-lg` |
| Padding | 8px | `--space-2` |

#### Menu Item Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Height | 40px (cozy) / 32px (compact) | — |
| Padding | 8px 12px | `--space-2` `--space-3` |
| Font Size | 14px | `--text-sm` |
| Icon Size | 16px–20px | `--icon-xs` `--icon-sm` |
| Icon Gap | 12px | `--space-3` |

#### Menu Item States

| State | Background | Text |
|-------|------------|------|
| Default | Transparent | Gray 700 |
| Hover | Gray 50 | Gray 900 |
| Active | Primary 10% | Primary |
| Selected | Primary 10% | Primary |
| Disabled | Transparent | Gray 400 |
| Destructive | Transparent | Error Red |
| Destructive Hover | Error 10% | Error Red |

#### Structure

```html
<div class="dropdown-menu" role="menu">
  <div class="menu-section">
    <div class="menu-heading">Actions</div>
    <button class="menu-item" role="menuitem">
      <svg aria-hidden="true">...</svg>
      Edit
    </button>
    <button class="menu-item" role="menuitem">
      <svg aria-hidden="true">...</svg>
      Duplicate
    </button>
  </div>
  <div class="menu-divider"></div>
  <div class="menu-section">
    <button class="menu-item destructive" role="menuitem">
      <svg aria-hidden="true">...</svg>
      Delete
    </button>
  </div>
</div>
```

#### CSS Implementation

```css
.dropdown-menu {
  min-width: 160px;
  max-width: 320px;
  background: var(--color-white);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-lg);
  padding: var(--space-2);
  z-index: 50;
}

.menu-section {
  padding: var(--space-1) 0;
}

.menu-heading {
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  color: var(--color-gray-500);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: var(--space-2) var(--space-3);
}

.menu-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  width: 100%;
  padding: var(--space-2) var(--space-3);
  border: none;
  background: transparent;
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  color: var(--color-gray-700);
  cursor: pointer;
  transition: all 100ms ease;
  text-align: left;
}

.menu-item:hover {
  background: var(--color-gray-50);
  color: var(--color-gray-900);
}

.menu-item:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: -2px;
}

.menu-item.selected {
  background: rgba(0, 102, 204, 0.1);
  color: var(--color-primary);
}

.menu-item.destructive {
  color: var(--color-error);
}

.menu-item.destructive:hover {
  background: rgba(220, 38, 38, 0.1);
}

.menu-item:disabled {
  color: var(--color-gray-400);
  cursor: not-allowed;
}

.menu-item svg {
  width: 16px;
  height: 16px;
  flex-shrink: 0;
}

.menu-divider {
  height: 1px;
  background: var(--border-default);
  margin: var(--space-2) 0;
}
```

### Menu Density

| Density | Item Height | Use Case |
|---------|-------------|----------|
| Cozy (default) | 40px | General use |
| Compact | 32px | Dense interfaces, tables |

```css
.dropdown-menu.compact .menu-item {
  padding: var(--space-1) var(--space-3);
}
```

### Menu with Descriptions

For items needing additional context:

```html
<button class="menu-item with-description" role="menuitem">
  <svg aria-hidden="true">...</svg>
  <div class="menu-item-content">
    <span class="menu-item-label">Export to PDF</span>
    <span class="menu-item-description">Download as printable document</span>
  </div>
</button>
```

```css
.menu-item.with-description {
  align-items: flex-start;
  padding: var(--space-3);
}

.menu-item-content {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.menu-item-label {
  font-weight: var(--font-medium);
}

.menu-item-description {
  font-size: var(--text-xs);
  color: var(--color-gray-500);
}
```

### Keyboard Navigation

| Key | Action |
|-----|--------|
| `↓` / `↑` | Move between items |
| `Enter` / `Space` | Select item |
| `Escape` | Close menu |
| `Home` / `End` | Jump to first/last |
| `A-Z` | Jump to matching item |

## Avatar

Avatars are visual representations of users, teams, or entities. They provide quick identification and add a human element to the interface.

### Shapes

| Shape | Use Case |
|-------|----------|
| Circle | People (users, team members) |
| Square | Entities (projects, products, companies) |
| Rounded Square | AI agents, automated systems |

### Sizes

| Size | Pixels | Token | Use Case |
|------|--------|-------|----------|
| XS | 16px | `--avatar-xs` | Inline metadata, dense lists |
| SM | 24px | `--avatar-sm` | Compact UI, dropdowns |
| MD | 32px | `--avatar-md` | Standard (comments, lists) |
| LG | 40px | `--avatar-lg` | User menus, cards |
| XL | 48px | `--avatar-xl` | Profile headers |
| XXL | 64px | `--avatar-xxl` | Profile pages |

### Specifications

| Attribute | Value |
|-----------|-------|
| Fallback BG | Liberation Blue |
| Fallback Text | White, semibold |
| Border | 2px solid white (in groups) |
| Font Size | 40% of avatar size |

### Default/Fallback Avatar

When no image is available, show initials:

```html
<!-- Image available -->
<div class="avatar avatar-md">
  <img src="user.jpg" alt="Sarah Chen" />
</div>

<!-- Fallback with initials -->
<div class="avatar avatar-md" aria-label="Sarah Chen">
  <span>SC</span>
</div>

<!-- Default (no name available) -->
<div class="avatar avatar-md">
  <svg aria-hidden="true"><!-- user icon --></svg>
</div>
```

### CSS Implementation

```css
.avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-full);
  background: var(--color-primary);
  color: var(--color-white);
  font-weight: var(--font-semibold);
  overflow: hidden;
  flex-shrink: 0;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Sizes */
.avatar-xs { width: 16px; height: 16px; font-size: 6px; }
.avatar-sm { width: 24px; height: 24px; font-size: 10px; }
.avatar-md { width: 32px; height: 32px; font-size: 12px; }
.avatar-lg { width: 40px; height: 40px; font-size: 14px; }
.avatar-xl { width: 48px; height: 48px; font-size: 16px; }
.avatar-xxl { width: 64px; height: 64px; font-size: 20px; }

/* Shapes */
.avatar-square { border-radius: var(--radius-md); }
.avatar-rounded { border-radius: var(--radius-lg); }

/* Interactive */
.avatar-interactive {
  cursor: pointer;
  transition: transform 150ms ease, box-shadow 150ms ease;
}

.avatar-interactive:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-md);
}

.avatar-interactive:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

### Presence Indicators

Show user online status with a presence dot:

| Status | Color | Token |
|--------|-------|-------|
| Online | Green | `--color-success` |
| Busy | Red | `--color-error` |
| Away | Amber | `--color-warning` |
| Offline | Gray | `--color-gray-400` |

```html
<div class="avatar avatar-md with-presence">
  <img src="user.jpg" alt="Sarah Chen" />
  <span class="presence-indicator online"></span>
</div>
```

```css
.avatar.with-presence {
  position: relative;
}

.presence-indicator {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 25%;
  height: 25%;
  min-width: 8px;
  min-height: 8px;
  border-radius: var(--radius-full);
  border: 2px solid var(--color-white);
}

.presence-indicator.online { background: var(--color-success); }
.presence-indicator.busy { background: var(--color-error); }
.presence-indicator.away { background: var(--color-warning); }
.presence-indicator.offline { background: var(--color-gray-400); }
```

### Status Indicators

Show approval or access status:

| Status | Icon | Color |
|--------|------|-------|
| Approved | Check | Success Green |
| Declined | X | Error Red |
| Locked | Lock | Gray |

### Avatar Groups

Display multiple avatars as a stacked group:

| Layout | Max Visible | Use Case |
|--------|-------------|----------|
| Stack | 5 | Compact displays |
| Grid | 11 | Expanded views |

```html
<div class="avatar-group">
  <div class="avatar avatar-sm"><img src="user1.jpg" alt="User 1" /></div>
  <div class="avatar avatar-sm"><img src="user2.jpg" alt="User 2" /></div>
  <div class="avatar avatar-sm"><img src="user3.jpg" alt="User 3" /></div>
  <div class="avatar avatar-sm overflow-indicator">+5</div>
</div>
```

```css
.avatar-group {
  display: flex;
  flex-direction: row-reverse;
  justify-content: flex-end;
}

.avatar-group .avatar {
  margin-left: -8px;
  border: 2px solid var(--color-white);
  box-shadow: var(--shadow-sm);
}

.avatar-group .avatar:last-child {
  margin-left: 0;
}

.avatar-group .overflow-indicator {
  background: var(--color-gray-100);
  color: var(--color-gray-600);
  font-size: var(--text-xs);
}
```

### Tooltips

Interactive avatars should display a tooltip with the user's name on hover:

```html
<div class="avatar avatar-md" data-tooltip="Sarah Chen">
  <img src="user.jpg" alt="" />
</div>
```

## Page Header Component

Combines breadcrumbs, page title, and actions into a cohesive header.

### Structure

```
┌──────────────────────────────────────────────────────────────┐
│  Home > Products > Term Life                                  │  ← Breadcrumbs
├──────────────────────────────────────────────────────────────┤
│  Term Life Insurance                   [ Edit ] [ Publish ]  │  ← Title + Actions
│  Configure coverage options and pricing                       │  ← Subtitle
└──────────────────────────────────────────────────────────────┘
```

### CSS Implementation

```css
.page-header {
  margin-bottom: var(--space-8);
}

.page-header-content {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-4);
}

.page-title {
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  color: var(--color-gray-800);
  margin-bottom: var(--space-2);
  line-height: 1.2;
}

.page-subtitle {
  font-size: var(--text-lg);
  color: var(--color-gray-600);
}

.page-actions {
  display: flex;
  gap: var(--space-3);
  flex-shrink: 0;
}
```

## CSS Tokens Reference

```css
:root {
  /* Navigation */
  --sidebar-width: 260px;
  --header-height: 64px;
  
  /* Avatar Sizes */
  --avatar-xs: 16px;
  --avatar-sm: 24px;
  --avatar-md: 32px;
  --avatar-lg: 40px;
  --avatar-xl: 48px;
  --avatar-xxl: 64px;
  
  /* Menu */
  --menu-min-width: 160px;
  --menu-max-width: 320px;
  --menu-item-height: 40px;
  --menu-item-height-compact: 32px;
  
  /* Z-Index Scale */
  --z-dropdown: 50;
  --z-sticky: 30;
  --z-modal: 100;
  --z-tooltip: 150;
}
```

## Accessibility Requirements

### Keyboard Navigation

All interactive components must be fully keyboard accessible:

| Component | Tab Stop | Enter/Space | Escape | Arrows |
|-----------|----------|-------------|--------|--------|
| Nav Item | Yes | Activate | — | — |
| Menu | Yes | Open/Select | Close | Navigate |
| Avatar (interactive) | Yes | Activate | — | — |
| Breadcrumb | Yes | Follow link | — | — |

### ARIA Requirements

| Component | Required ARIA |
|-----------|---------------|
| Navigation | `role="navigation"`, `aria-label` |
| Breadcrumb | `aria-label="Breadcrumb"`, `aria-current="page"` |
| Menu | `role="menu"`, `role="menuitem"` |
| Avatar | `alt` text or `aria-label` |

### Focus Management

- Focus rings visible (2px solid primary, 2px offset)
- Focus trap in modals and dropdowns
- Focus returns to trigger on close
- Skip links for main content

### Screen Reader Considerations

- Decorative icons hidden with `aria-hidden="true"`
- Interactive icons have accessible labels
- Status changes announced with `aria-live`
- Meaningful link text (not "click here")

## Usage Examples

### Complete Navigation

```html
<aside class="sidebar">
  <div class="logo">
    <img src="logo.svg" alt="OpenLife" />
  </div>
  
  <nav class="nav-section" aria-label="Main navigation">
    <div class="nav-section-title">Overview</div>
    <a href="/dashboard" class="nav-item active">
      <svg aria-hidden="true"><!-- dashboard icon --></svg>
      Dashboard
    </a>
    <a href="/products" class="nav-item">
      <svg aria-hidden="true"><!-- package icon --></svg>
      Products
    </a>
  </nav>
  
  <nav class="nav-section" aria-label="Settings">
    <div class="nav-section-title">Settings</div>
    <a href="/settings" class="nav-item">
      <svg aria-hidden="true"><!-- settings icon --></svg>
      Settings
    </a>
  </nav>
</aside>
```

### User Menu with Avatar

```html
<div class="user-menu">
  <button class="user-menu-trigger" aria-haspopup="true" aria-expanded="false">
    <div class="avatar avatar-md with-presence">
      <img src="user.jpg" alt="" />
      <span class="presence-indicator online"></span>
    </div>
    <span class="user-name">Sarah Chen</span>
    <svg aria-hidden="true"><!-- chevron-down --></svg>
  </button>
  
  <div class="dropdown-menu" role="menu" hidden>
    <div class="menu-section">
      <a href="/profile" class="menu-item" role="menuitem">
        <svg aria-hidden="true"><!-- user icon --></svg>
        Profile
      </a>
      <a href="/settings" class="menu-item" role="menuitem">
        <svg aria-hidden="true"><!-- settings icon --></svg>
        Settings
      </a>
    </div>
    <div class="menu-divider"></div>
    <div class="menu-section">
      <button class="menu-item" role="menuitem">
        <svg aria-hidden="true"><!-- logout icon --></svg>
        Sign out
      </button>
    </div>
  </div>
</div>
```
