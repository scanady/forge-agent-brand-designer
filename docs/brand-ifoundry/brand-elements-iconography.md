# iFoundry Media Iconography

> Precise, functional icons that guide builders through products with engineering clarity.

## Strategic Foundation

**Brand Alignment:** iFoundry icons reflect The Builder's pragmatism and The Sage's clarity. Every icon serves a function — guiding users through workflows without cognitive overhead. The icon style is clean and geometric with angular precision that echoes the logo's connected-node motif. Icons communicate structure (navigation, status) and capability (technology, deployment, architecture) with equal reliability.

## Icon Library

### Lucide Icons

iFoundry uses the **Lucide** icon library — a modern, open-source icon set with consistent geometry, clean 24px grid, and excellent stroke consistency that aligns with Space Grotesk's geometric character.

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
- Clean, geometric forms that complement Space Grotesk
- Comprehensive set covering engineering and SaaS UI needs
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
| `--icon-emphasis` | `#0F172A` (Iron Slate) | High-emphasis, headings |
| `--icon-primary` | `#1D4ED8` (Forge Blue) | Active states, brand icons |
| `--icon-accent` | `#EA580C` (Ignite Orange) | Accent moments, CTAs |
| `--icon-on-dark` | `#CBD5E1` (Slate 300) | Icons on dark backgrounds |
| `--icon-on-dark-active` | `#FFFFFF` (White) | Active icons on dark backgrounds |
| `--icon-success` | `#059669` (Launch Green) | Success states |
| `--icon-warning` | `#EA580C` (Ignite Orange) | Warning states |
| `--icon-error` | `#DC2626` (Alert Red) | Error states |
| `--icon-info` | `#3B82F6` (Architect Blue) | Information states |

## Curated Icon Reference

Icons organized by function within iFoundry's product ecosystem.

### Navigation

| Icon | Name | Usage |
|------|------|-------|
| LayoutDashboard | Dashboard | Project overview |
| FolderKanban | Projects | Project management |
| GitBranch | Repositories | Code and version control |
| Rocket | Deployments | Build and deploy |
| BarChart3 | Analytics | Metrics and insights |
| Settings | Settings | Application settings |
| Users | Team | Team management |
| HelpCircle | Help | Help and documentation |
| Search | Search | Global search |
| Bell | Notifications | Alerts and notifications |

### Engineering Actions

| Icon | Name | Usage |
|------|------|-------|
| Play | Build | Trigger a build |
| Rocket | Deploy | Deploy to environment |
| RotateCcw | Rollback | Rollback a deployment |
| GitPullRequest | Pull Request | Code review |
| GitMerge | Merge | Merge branches |
| Terminal | Console | Terminal / CLI access |
| Database | Data | Database operations |
| Cloud | Infrastructure | Cloud resources |
| Cpu | Compute | Processing resources |
| Lock | Security | Security settings |

### Status & Health

| Icon | Name | Usage |
|------|------|-------|
| CheckCircle | Healthy | System/service healthy |
| AlertTriangle | Warning | Needs attention |
| XCircle | Error | Failure state |
| Clock | Pending | Waiting / in progress |
| Activity | Performance | System performance |
| Shield | Secure | Security verified |
| Zap | Fast | Performance optimized |
| TrendingUp | Growth | Positive metrics |
| TrendingDown | Decline | Declining metrics |
| CircleDot | Active | Currently running |

### Product Development

| Icon | Name | Usage |
|------|------|-------|
| Lightbulb | Idea | Concept / ideation phase |
| PenTool | Design | Design phase |
| Code | Engineering | Development phase |
| TestTube | Testing | QA and testing |
| Rocket | Launch | Product launch |
| ArrowUpRight | Scale | Growth and scaling |
| Layers | Architecture | System architecture |
| Workflow | Pipeline | CI/CD pipeline |
| Package | Package | Build artifacts |
| Globe | Production | Live/production environment |

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
  --icon-default: var(--color-slate-500);
  --icon-muted: var(--color-slate-400);
  --icon-emphasis: var(--color-primary-dark);
  --icon-primary: var(--color-primary);
  --icon-accent: var(--color-accent);
  --icon-on-dark: var(--color-slate-300);
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

For icons that need a background treatment (feature highlights, status indicators).

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
  background: var(--color-blue-50);
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
  <RocketIcon aria-hidden="true" />
  Deploy
</button>

<!-- Icon-only button (accessible) -->
<button aria-label="View deployment logs">
  <TerminalIcon aria-hidden="true" />
</button>
```

## Usage Guidelines

### Do
- Use Lucide icons consistently throughout all products
- Match icon size to context (navigation = small, page headers = large)
- Use semantic colors for status icons (green = success, red = error)
- Keep icon-only interactive elements to a minimum — prefer icon + text
- Use decorative tile sizes for empty states and feature highlights

### Don't
- Mix icon libraries or styles within the same view
- Use icons as decoration without functional purpose
- Create new icons when a suitable Lucide icon exists
- Use filled/solid icon variants — maintain the stroke style
- Apply color to icons that don't carry semantic meaning
- Use icons smaller than 12px — they become illegible
