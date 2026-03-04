# Nexus Coach UI Components

> Modern, accessible components that create clear, professional coaching practice interfaces.

## Strategic Foundation

**Brand Alignment:** Nexus Coach UI components embody The Guide's clarity and The Architect's precision. Every component is designed to reduce cognitive load, guide coaches through operational workflows, and present information with professional confidence. Components prioritize consistency, accessibility, and the calm, organized experience that a well-run practice provides.

## Navigation System

Nexus Coach uses a structured navigation system combining a persistent sidebar for primary navigation with contextual breadcrumbs and a top bar for global actions.

### Navigation Architecture

| Layer | Purpose | Position |
|-------|---------|----------|
| Top Bar | Global actions, search, user menu | Fixed top |
| Side Navigation | Primary app navigation | Fixed left |
| Breadcrumbs | Hierarchical location | Page header |
| Tabs | Content-level navigation | Within page |

### Side Navigation

The primary navigation for Nexus Coach — a dark-themed vertical sidebar providing consistent access to all practice areas.

#### Structure

```
┌────────────────────────┐
│  Logo + Brand          │  ← Nexus Coach mark + wordmark
├────────────────────────┤
│  Practice Navigation   │  ← Core practice sections
│  ├─ Dashboard          │
│  ├─ Clients            │
│  ├─ Sessions           │
│  ├─ Programs           │
│  ├─ Prospects          │
│  └─ Billing            │
├────────────────────────┤
│  Insights              │  ← Analytics & oversight
│  ├─ Analytics          │
│  └─ Coach Performance  │
├────────────────────────┤
│  Settings & Help       │  ← Bottom-anchored
│  ├─ Settings           │
│  └─ Help               │
├────────────────────────┤
│  User Avatar + Name    │  ← Current user
└────────────────────────┘
```

#### Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Width | 260px | `--sidebar-width` |
| Background | Structure Slate `#0F172A` | `--color-primary-dark` |
| Text Color | Slate 300 `#CBD5E1` | `--color-slate-300` |
| Active Text | White `#FFFFFF` | `--color-white` |
| Padding | 16px | `--space-4` |

#### Navigation Item States

| State | Background | Text | Icon |
|-------|------------|------|------|
| Default | Transparent | Slate 300 | Slate 400 |
| Hover | `rgba(255, 255, 255, 0.08)` | White | White |
| Active | Guide Teal `#0F766E` | White | White |
| Focused | `rgba(255, 255, 255, 0.08)` + focus ring | White | White |
| Disabled | Transparent | Slate 500 | Slate 500 |

#### CSS Implementation

```css
.nav-item {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: 10px var(--space-3);
  border-radius: var(--radius-md);
  color: var(--color-slate-300);
  text-decoration: none;
  font-family: var(--font-sans);
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
  outline: 2px solid var(--color-teal-500);
  outline-offset: 2px;
}

.nav-item svg {
  width: 20px;
  height: 20px;
  flex-shrink: 0;
}
```

### Navigation Sections

| Attribute | Value |
|-----------|-------|
| Section Title | Uppercase, 12px, Slate 400, 0.05em tracking |
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
  color: var(--color-slate-400);
  margin-bottom: var(--space-2);
  padding: 0 var(--space-3);
}
```

### Top Navigation Bar

A horizontal bar for global actions, search, and user controls.

#### Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Height | 64px | `--header-height` |
| Background | White | `--color-white` |
| Border | 1px solid Slate 200 | `--border-default` |
| Padding | 16px 24px | `--space-4` `--space-6` |
| Position | Sticky top | `z-index: var(--z-sticky)` |

#### Components

| Component | Position | Function |
|-----------|----------|----------|
| Search | Left/Center | Global search (clients, sessions, coaches) |
| Notifications | Right | Activity alerts, session reminders |
| Help | Right | Support access |
| User Menu | Right | Account, preferences, sign out |

## Breadcrumbs

Breadcrumbs show the user's location within the practice management hierarchy.

### Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Font Size | 14px | `--text-sm` |
| Text Color | Slate 600 | `--color-slate-600` |
| Link Color | Guide Teal | `--color-primary` |
| Separator | Chevron right, 16px | `--icon-xs` |
| Gap | 8px | `--space-2` |
| Margin Bottom | 24px | `--space-6` |

### Structure

```html
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li><a href="/dashboard">Dashboard</a></li>
    <li><a href="/clients">Clients</a></li>
    <li><a href="/clients/sarah-chen">Sarah Chen</a></li>
    <li aria-current="page">Session Notes</li>
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

### CSS Implementation

```css
.breadcrumb {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-6);
  font-size: var(--text-sm);
  color: var(--color-slate-600);
  list-style: none;
  padding: 0;
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
  color: var(--color-slate-800);
  font-weight: var(--font-medium);
}
```

## Menu Components

### Menu Types

| Type | Use Case | Trigger |
|------|----------|---------|
| Dropdown Menu | Actions list | Button click |
| Context Menu | Right-click actions | Right-click |
| Navigation Menu | Section navigation | Hover/Click |

### Dropdown Menu Specifications

| Attribute | Value | Token |
|-----------|-------|-------|
| Min Width | 160px | — |
| Max Width | 320px | — |
| Background | White | `--color-white` |
| Border | 1px solid Slate 200 | `--border-default` |
| Shadow | `--shadow-lg` | High elevation |
| Border Radius | `--radius-md` | 6px |
| Z-Index | `--z-dropdown` | 20 |
| Item Height | 40px (cozy), 32px (compact) | — |
| Padding | 4px | `--space-1` |

### Menu Item States

| State | Background | Text |
|-------|------------|------|
| Default | Transparent | Slate 700 |
| Hover | Slate 100 | Slate 900 |
| Active | Teal 50 | Guide Teal |
| Focused | Slate 100 + focus ring | Slate 900 |
| Disabled | Transparent | Slate 300 |
| Destructive | Transparent | Error Red |
| Destructive Hover | Error Light | Error Dark |

### Menu CSS

```css
.menu {
  min-width: 160px;
  max-width: 320px;
  background: var(--color-white);
  border: 1px solid var(--border-default);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-lg);
  padding: var(--space-1);
  z-index: var(--z-dropdown);
}

.menu-item {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: 8px var(--space-3);
  border-radius: var(--radius-sm);
  font-size: var(--text-sm);
  color: var(--color-slate-700);
  cursor: pointer;
  transition: background 100ms ease;
}

.menu-item:hover {
  background: var(--color-slate-100);
  color: var(--color-slate-900);
}

.menu-item.destructive {
  color: var(--color-error);
}

.menu-item.destructive:hover {
  background: var(--color-error-light);
  color: var(--color-error-dark);
}

.menu-divider {
  height: 1px;
  background: var(--border-default);
  margin: var(--space-1) 0;
}
```

## Avatar

Avatars represent coaches, clients, and practice leads throughout the platform.

### Sizes

| Size | Dimension | Font Size | Token | Usage |
|------|-----------|-----------|-------|-------|
| XS | 20px | 10px | `--avatar-xs` | Inline mentions, compact lists |
| SM | 28px | 12px | `--avatar-sm` | Navigation, small cards |
| MD | 36px | 14px | `--avatar-md` | List items, comments |
| LG | 44px | 16px | `--avatar-lg` | Card headers, profiles |
| XL | 56px | 20px | `--avatar-xl` | Detail pages, settings |
| 2XL | 80px | 28px | `--avatar-2xl` | Profile pages, hero cards |

### Variants

| Variant | Description |
|---------|------------|
| Image | Profile photo, cropped to circle |
| Initials | First + last initial on colored background |
| Icon | Generic person icon fallback |

### Initials Color Assignment
Assign consistent background colors based on the user's name to create visual distinction.

| Slot | Background | Text |
|------|------------|------|
| 1 | Teal 100 `#CCFBF1` | Teal 800 `#115E59` |
| 2 | Sky 100 `#E0F2FE` | Sky 800 `#075985` |
| 3 | Indigo 100 `#E0E7FF` | Indigo 800 `#3730A3` |
| 4 | Amber 100 `#FEF3C7` | Amber 800 `#92400E` |
| 5 | Rose 100 `#FFE4E6` | Rose 800 `#9F1239` |
| 6 | Emerald 100 `#D1FAE5` | Emerald 800 `#065F46` |

### Presence Indicator

| Status | Color | Size |
|--------|-------|------|
| Online | `#059669` (Emerald) | 25% of avatar |
| Away | `#D97706` (Amber) | 25% of avatar |
| Busy / In Session | `#DC2626` (Red) | 25% of avatar |
| Offline | `#94A3B8` (Slate 400) | 25% of avatar |

### Avatar CSS

```css
.avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-full);
  font-family: var(--font-sans);
  font-weight: var(--font-semibold);
  overflow: hidden;
  flex-shrink: 0;
}

.avatar-md {
  width: 36px;
  height: 36px;
  font-size: 14px;
}

.avatar-lg {
  width: 44px;
  height: 44px;
  font-size: 16px;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-presence {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 25%;
  height: 25%;
  border-radius: var(--radius-full);
  border: 2px solid var(--color-white);
}
```

## Page Header

The page header appears at the top of every content area, providing context and primary actions.

### Structure

```
┌─────────────────────────────────────────┐
│ Breadcrumbs                             │
│                                         │
│ Page Title                   [Actions]  │
│ Optional description                    │
└─────────────────────────────────────────┘
```

### Specifications

| Attribute | Value |
|-----------|-------|
| Title | H1 — Plus Jakarta Sans, Bold, 30px |
| Description | Body — Slate 500, 16px |
| Margin bottom | `--space-8` (32px) |
| Actions alignment | Right, vertically centered with title |

### Page Header CSS

```css
.page-header {
  margin-bottom: var(--space-8);
}

.page-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
}

.page-header-title {
  font-family: var(--font-sans);
  font-size: var(--text-4xl);
  font-weight: var(--font-bold);
  color: var(--color-primary-dark);
  line-height: var(--leading-tight);
}

.page-header-description {
  font-size: var(--text-base);
  color: var(--color-slate-500);
  margin-top: var(--space-1);
}

.page-header-actions {
  display: flex;
  gap: var(--space-2);
  flex-shrink: 0;
}
```

## Tabs

Content-level navigation for switching between related views within a page.

### Specifications

| Attribute | Value |
|-----------|-------|
| Font Size | 14px, Semi-Bold |
| Inactive Color | Slate 500 |
| Active Color | Guide Teal |
| Indicator | 2px bottom border, Guide Teal |
| Gap | 24px between tabs |
| Padding | 12px 0 (vertical for bottom border hit area) |

### Tab States

| State | Text | Border |
|-------|------|--------|
| Default | Slate 500 | None |
| Hover | Slate 700 | 2px Slate 300 |
| Active | Guide Teal | 2px Guide Teal |
| Focused | Slate 700 + focus ring | None |
| Disabled | Slate 300 | None |

### Tab CSS

```css
.tabs {
  display: flex;
  gap: var(--space-6);
  border-bottom: 1px solid var(--border-default);
}

.tab {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
  color: var(--color-slate-500);
  padding: var(--space-3) 0;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: color 150ms ease, border-color 150ms ease;
}

.tab:hover {
  color: var(--color-slate-700);
  border-bottom-color: var(--color-slate-300);
}

.tab.active {
  color: var(--color-primary);
  border-bottom-color: var(--color-primary);
}

.tab:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
  border-radius: var(--radius-sm);
}
```

## Badges & Status Indicators

### Badge Variants

| Variant | Background | Text | Usage |
|---------|------------|------|-------|
| Default | Slate 100 | Slate 700 | Neutral counts, labels |
| Primary | Teal 50 | Guide Teal | Active/featured status |
| Success | Success Light | Success Dark | Completed, active |
| Warning | Warning Light | Warning Dark | At risk, pending |
| Error | Error Light | Error Dark | Failed, overdue |
| Info | Info Light | Info Dark | Informational |

### Badge CSS

```css
.badge {
  display: inline-flex;
  align-items: center;
  gap: var(--space-1);
  padding: 2px 8px;
  border-radius: var(--radius-full);
  font-family: var(--font-sans);
  font-size: var(--text-xs);
  font-weight: var(--font-semibold);
  line-height: 1.4;
  white-space: nowrap;
}

.badge-default {
  background: var(--color-slate-100);
  color: var(--color-slate-700);
}

.badge-success {
  background: var(--color-success-light);
  color: var(--color-success-dark);
}

.badge-warning {
  background: var(--color-warning-light);
  color: var(--color-warning-dark);
}

.badge-error {
  background: var(--color-error-light);
  color: var(--color-error-dark);
}
```

## Usage Guidelines

### Do
- Use the sidebar for primary practice navigation consistently
- Apply breadcrumbs on all pages deeper than the top level
- Use avatars with consistent sizing across the same view
- Apply badges for status indicators, not decoration
- Maintain keyboard navigability for all interactive components

### Don't
- Mix navigation patterns (sidebar + top nav for the same purpose)
- Use more than 6 top-level navigation items in the sidebar
- Place critical actions only in context menus — provide primary access elsewhere
- Use destructive menu items without confirmation for irreversible actions
- Create custom components when a standard one exists
