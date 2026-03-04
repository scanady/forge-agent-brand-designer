# SpikeForge UI Components

> Refined components for high-trust, high-clarity coaching operations.

## Strategic Foundation

SpikeForge components are designed for two complementary modes:

1. Narrative mode: mission-forward, editorial sections for acquisition and trust.
2. Operational mode: dense, calm, and legible interfaces for day-to-day execution.

## Core Layout System

### Global Shell

| Region | Purpose | Spec |
|--------|---------|------|
| Utility bar | Contextual alerts and global status | 40px height |
| Top bar | Search, actions, profile, quick create | 64px height |
| Side nav | Primary product navigation | 272px width |
| Main content | Work surface with sectional hierarchy | Max 1320px content grid |

### Surface Hierarchy

| Level | Token | Typical Use |
|-------|-------|-------------|
| Level 0 | `--color-surface-50` | App background |
| Level 1 | `--color-white` | Cards, forms, tables |
| Level 2 | `--color-ink-900` | Structural rails, dark utility zones |
| Accent | `--gradient-brand` | Hero strips, campaign blocks |

## Navigation

### Side Navigation

- Width: 272px
- Visual style: dark structural rail with clear icon + label pairs
- Section labels: compact mono overlines
- Active item: cobalt fill with white text
- Hover: translucent white wash

### Top Navigation

- Left: global search with command-style affordance
- Right: quick actions, notification center, profile switcher
- Sticky behavior with subtle shadow and border lock

## Components by Role

### Hero Strip

A campaign-ready band used for mission statements, launch messaging, or strategic announcements.

- Background: brand gradient or deep ink
- Content width: max 1200px
- Left: headline + support copy
- Right: one primary CTA + one secondary CTA

### KPI Rail

A horizontal metric strip for critical operating signals.

| Element | Behavior |
|---------|----------|
| Metric label | compact, uppercase mono |
| Metric value | large, bold numeric style |
| Delta indicator | semantic arrow + percentage |
| Drill-through | optional deep-link affordance |

### Data Cards

- Border radius: 14px
- Border: 1px neutral
- Padding: 20-24px
- Optional top accent rule for status context
- Internal spacing uses 8px base rhythm

### Workflow Stepper

For onboarding and multi-stage flows.

- Horizontal on desktop, vertical on mobile
- Every step has explicit status: not started, in progress, complete, blocked
- Includes estimated effort and next-action text

### Action Panel

A persistent right-rail module for next actions.

- Shows prioritized tasks, deadlines, and owner
- Supports inline complete/defer actions
- Encourages operational follow-through without modal interruptions

## Form Components

### Inputs

| Attribute | Spec |
|-----------|------|
| Height | 44px default |
| Radius | 12px |
| Border | neutral 1px |
| Focus | 2px cobalt ring + subtle halo |
| Error | red border + inline helper text |

### Buttons

| Type | Visual |
|------|--------|
| Primary | cobalt fill, white text |
| Secondary | white fill, neutral border |
| Tertiary | text-only with subtle hover wash |
| Destructive | red text, tinted hover |

## Data Display

### Tables

- Header row has elevated contrast and sticky behavior.
- Numeric columns right aligned.
- Row states: default, hover, selected, warning.
- Bulk actions appear in contextual action bar.

### Status Badges

| Status | Treatment |
|--------|-----------|
| Active | success surface + success text |
| Needs attention | warning surface + warning text |
| Blocked | error surface + error text |
| Draft | neutral surface + neutral text |

## Motion Guidance

1. Functional motion only.
2. Duration bands:
   - micro feedback: 120-160ms
   - panel and dropdown: 180-220ms
   - modal transitions: 220-280ms
3. Honor `prefers-reduced-motion` with instant alternatives.

## Accessibility Expectations

- Keyboard-first operation for all primary workflows.
- Clear focus treatment on all interactive elements.
- Color is never the only status cue.
- Data tables remain navigable with assistive tech.
- Toasts and inline alerts announce via live regions.

## Component Tokens

```css
:root {
  --sidebar-width: 272px;
  --topbar-height: 64px;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 14px;
  --radius-xl: 18px;

  --shadow-sm: 0 1px 2px rgba(11, 18, 32, 0.06);
  --shadow-md: 0 6px 18px rgba(11, 18, 32, 0.08);
  --shadow-lg: 0 16px 32px rgba(11, 18, 32, 0.12);
}
```

## Usage Guidelines

### Do
- Use strong visual hierarchy before adding new UI complexity.
- Keep workflows inline where possible to reduce mode switching.
- Pair every metric with context or trend direction.
- Design for both high-level scanning and detailed inspection.

### Don't
- Use gradients as default card backgrounds.
- Hide critical actions behind nested menus.
- Overload a single panel with mixed intent actions.
- Introduce decorative motion without functional meaning.
