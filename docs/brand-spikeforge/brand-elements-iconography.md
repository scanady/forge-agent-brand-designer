# SpikeForge Iconography

> Clear, purposeful icons that guide coaches through their practice with confidence.

## Strategic Foundation

**Brand Alignment:** SpikeForge icons reflect The Guide's clarity and The Architect's precision. Every icon serves a purpose — guiding coaches through workflows without cognitive overhead. The icon style is clean and geometric, avoiding decoration for its own sake. Icons communicate structure (navigation, status) and connection (coaching relationships, client health) with equal reliability.

## Icon Library

### Lucide Icons

SpikeForge uses the **Lucide** icon library as its foundation — a modern, open-source icon set with consistent geometry, clean 24px grid, and excellent stroke consistency.

| Attribute | Value |
|-----------|-------|
| Library | Lucide Icons |
| License | ISC License (open source) |
| Source | [lucide.dev](https://lucide.dev) |
| Grid | 24×24px |
| Stroke Width | 1.5px (default) |
| Corner Radius | Rounded joins and caps |

### Why Lucide
- Consistent 1.5px stroke across all icons
- Clean, geometric forms that match Manrope
- Comprehensive set covering SaaS UI needs
- Active maintenance and growing library
- Framework-agnostic with React, Vue, and Svelte packages

## Icon Specifications

### Standard Sizes

| Size | Dimension | Stroke | Token | Usage |
|------|-----------|--------|-------|-------|
| Extra Small | 12×12px | 1.5px | `--icon-xs` | Inline text, breadcrumb separators |
| Small | 16×16px | 1.5px | `--icon-sm` | Navigation items, form inputs, compact UI |
| Default | 20×20px | 1.5px | `--icon-md` | Standard UI, buttons, menus |
| Large | 24×24px | 1.5px | `--icon-lg` | Page headers, cards, prominent actions |

### Decorative Tiles

Larger icon formats for empty states, onboarding, and feature highlights.

| Size | Dimension | Stroke | Usage |
|------|-----------|--------|-------|
| Small Tile | 32×32px | 2px | Cards, feature lists |
| Medium Tile | 48×48px | 2px | Empty states, onboarding steps |
| Large Tile | 64×64px | 2px | Hero features, marketing blocks |

## Icon Colors

| Token | HEX | Usage |
|-------|-----|-------|
| `--icon-default` | `#64748B` (Slate 500) | Standard UI icons |
| `--icon-muted` | `#94A3B8` (Slate 400) | Secondary, inactive icons |
| `--icon-emphasis` | `#0B1220` (Midnight Ink) | High-emphasis, headings |
| `--icon-primary` | `#2E5BFF` (Cobalt Signal) | Active states, brand icons |
| `--icon-on-dark` | `#CBD5E1` (Slate 300) | Icons on dark backgrounds |
| `--icon-on-dark-active` | `#FFFFFF` (White) | Active icons on dark backgrounds |
| `--icon-success` | `#059669` (Growth Emerald) | Success states |
| `--icon-warning` | `#D97706` (Momentum Amber) | Warning states |
| `--icon-error` | `#DC2626` (Error) | Error states |
| `--icon-info` | `#0284C7` (Clarity Sky) | Information states |

## Curated Icon Reference

Icons organized by function within the SpikeForge platform.

### Navigation

| Icon | Name | Usage |
|------|------|-------|
| LayoutDashboard | Dashboard | Practice overview |
| Users | Clients | Client management |
| UserCog | Coaches | Coach management |
| Calendar | Sessions | Session scheduling |
| FileText | Programs | Program management |
| CreditCard | Billing | Invoicing and payments |
| BarChart3 | Analytics | Practice analytics |
| Settings | Settings | Application settings |
| HelpCircle | Help | Help and support |
| Search | Search | Global search |
| Bell | Notifications | Alerts and notifications |

### Coaching Actions

| Icon | Name | Usage |
|------|------|-------|
| PhoneCall | Discovery Call | Prospect discovery calls |
| UserPlus | Onboard Client | New client onboarding |
| ClipboardList | Session Notes | Session documentation |
| Target | Goals | Client goal tracking |
| CheckSquare | Action Items | Follow-up actions |
| RefreshCw | Re-engage | Client re-engagement |
| ArrowRightLeft | Reassign | Coach reassignment |
| GraduationCap | Complete | Program completion |

### Client Health & Status

| Icon | Name | Usage |
|------|------|-------|
| HeartPulse | Engagement | Client engagement signal |
| TrendingUp | Growing | Positive engagement trend |
| TrendingDown | Declining | Declining engagement |
| AlertTriangle | At Risk | Client at risk of disengagement |
| CheckCircle | Active | Active client status |
| Clock | Pending | Pending action |
| XCircle | Inactive | Inactive or disengaged |
| Pause | Paused | Paused engagement |
| CircleDot | In Session | Currently in session |

### Practice Operations

| Icon | Name | Usage |
|------|------|-------|
| Briefcase | Practice | Practice-level view |
| PieChart | Utilization | Coach utilization metrics |
| DollarSign | Revenue | Revenue tracking |
| TrendingUp | Pipeline | Prospect pipeline |
| Shield | Compliance | Documentation compliance |
| Download | Export | Export data |
| Upload | Import | Import data |
| Filter | Filter | Filter controls |
| SortAsc | Sort | Sort controls |

### UI Controls

| Icon | Name | Usage |
|------|------|-------|
| ChevronDown | Expand | Dropdown, accordion expand |
| ChevronRight | Navigate | Breadcrumb, navigation |
| ChevronLeft | Back | Back navigation |
| X | Close | Close, dismiss |
| Plus | Add | Create new item |
| MoreHorizontal | More | Overflow menu |
| ExternalLink | External | Opens in new window |
| Copy | Copy | Copy to clipboard |
| Edit | Edit | Edit mode |
| Trash2 | Delete | Remove item |
| Eye | View | View details |
| EyeOff | Hide | Hide content |

## CSS Tokens

```css
:root {
  /* Icon Sizes */
  --icon-xs: 12px;
  --icon-sm: 16px;
  --icon-md: 20px;
  --icon-lg: 24px;

  /* Decorative Tile Sizes */
  --icon-tile-sm: 32px;
  --icon-tile-md: 48px;
  --icon-tile-lg: 64px;

  /* Icon Colors */
  --icon-default: var(--color-ink-500);
  --icon-muted: var(--color-ink-400);
  --icon-emphasis: var(--color-ink-900);
  --icon-primary: var(--color-primary);
  --icon-on-dark: var(--color-ink-300);
  --icon-on-dark-active: var(--color-white);
  --icon-success: var(--color-success);
  --icon-warning: var(--color-warning);
  --icon-error: var(--color-error);
  --icon-info: var(--color-info);

  /* Stroke */
  --icon-stroke: 1.5px;
  --icon-stroke-tile: 2px;
}
```

## Icon Containers

For icons that need a background treatment (e.g., feature highlights, status badges).

### Subtle Container
Tinted background matching the icon's semantic color at 10% opacity.

```css
.icon-container-subtle {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  background: var(--color-primary-100);
  color: var(--color-primary);
}
```

### Filled Container
Solid background with white icon.

```css
.icon-container-filled {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: var(--radius-md);
  background: var(--color-primary);
  color: var(--color-white);
}
```

## Accessibility

- Always include accessible text for icon-only interactive elements (`aria-label` or visually hidden text)
- Decorative icons accompanying text should use `aria-hidden="true"`
- Ensure icon color meets 3:1 contrast ratio against backgrounds (WCAG 2.1 for non-text elements)
- Never rely on icons alone to convey critical information — pair with text labels
- Provide tooltips for icon-only controls

```html
<!-- Icon with text label (decorative) -->
<button>
  <CalendarIcon aria-hidden="true" />
  Sessions
</button>

<!-- Icon-only button (accessible) -->
<button aria-label="Edit session notes">
  <EditIcon aria-hidden="true" />
</button>
```

## Usage Guidelines

### Do
- Use Lucide icons consistently throughout the platform
- Match icon size to context (navigation = small, page headers = large)
- Use semantic colors for status icons (green = success, red = error)
- Keep icon-only interactive elements to a minimum — prefer icon + text
- Use decorative tile sizes for empty states and onboarding

### Don't
- Mix icon libraries or styles within the same view
- Use icons as decoration without functional purpose
- Create new icons when a suitable Lucide icon exists
- Use filled/solid icon variants — maintain the stroke style
- Apply color to icons that don't carry semantic meaning
- Use icons smaller than 12px — they become illegible
