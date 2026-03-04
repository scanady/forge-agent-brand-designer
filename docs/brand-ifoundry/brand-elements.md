# iFoundry Media Brand Elements

> Design system elements forged for clarity, precision, and impact.

## Overview

iFoundry Media's brand elements form a cohesive design system that translates the brand's Builder personality and foundry metaphor into concrete, implementable specifications. Every element is engineered to support products that feel crafted, confident, and technically excellent — reflecting iFoundry's commitment to building software like they own it.

These elements work together to create interfaces that are information-dense without feeling cluttered, technically sophisticated without being cold, and professionally authoritative while remaining approachable.

## Element Categories

### Content
Guidelines for clear, consistent, action-oriented communication.

| Element | Description | Document |
|---------|-------------|----------|
| Content Overview | Principles for user-facing content that proves capability and drives action | [Content Overview](brand-elements-content.md) |
| Language & Grammar | Writing conventions for clear, localizable, technically confident copy | [Language & Grammar](brand-elements-content-language-and-grammar.md) |
| Voice & Tone | Brand voice characteristics and tone variations across contexts | [Voice & Tone](brand-elements-content-voice-and-tone.md) |
| Date & Time | Date, time, timezone, and duration formatting standards | [Date & Time](brand-elements-content-date-and-time.md) |
| Message Design | Success, error, warning, info, and feature discovery message patterns | [Designing Messages](brand-elements-content-designing-messages.md) |

### Visual Identity
Core visual components that define the iFoundry brand.

| Element | Description | Document |
|---------|-------------|----------|
| Colors | Color palette with Forge Blue, Ignite Orange, and Iron Slate as anchors | [Colors](brand-elements-colors.md) |
| Typography | Space Grotesk + JetBrains Mono type system | [Typography](brand-elements-typography.md) |
| Iconography | Lucide-based icon system with foundry-consistent styling | [Iconography](brand-elements-iconography.md) |
| Imagery | Photography direction: bold, high-contrast, technology-as-craft | [Imagery](brand-elements-imagery.md) |
| Illustrations | Geometric, node-connected illustration style echoing the logomark | [Illustrations](brand-elements-illustrations.md) |
| Logos | Logo variations, clear space, sizing, and usage rules | [Logos](brand-elements-logos.md) |

### Layout & Structure
Building blocks for consistent, responsive interfaces.

| Element | Description | Document |
|---------|-------------|----------|
| Spacing | 4px base unit spacing system with density scales | [Spacing](brand-elements-spacing.md) |
| Grid | 12-column responsive grid with 5 breakpoints | [Grid](brand-elements-grid.md) |
| Elevation | 5-level shadow system and z-index scale | [Elevation](brand-elements-elevation.md) |
| Border | Border widths, radii, colors, and focus state patterns | [Border](brand-elements-border.md) |

### UI Components
Patterns for navigation, interaction, and status communication.

| Element | Description | Document |
|---------|-------------|----------|
| UI Components | Navigation, menus, avatars, breadcrumbs, tabs, and badges | [UI Components](brand-elements-ui-components.md) |

### Foundation
Principles that underpin all elements.

| Element | Description | Document |
|---------|-------------|----------|
| Accessibility | WCAG 2.1 AA compliance, keyboard navigation, screen reader support | [Accessibility](brand-elements-accessibility.md) |

## Quick Reference

### Primary Colors

| Token | Value | Usage |
|-------|-------|-------|
| Forge Blue | `#1D4ED8` | Primary actions, links, brand accent |
| Ignite Orange | `#EA580C` | CTAs, energy moments, warnings |
| Iron Slate | `#0F172A` | Text, dark backgrounds, headings |
| White | `#FFFFFF` | Backgrounds, inverted text |

### Typography

| Style | Font | Size | Weight |
|-------|------|------|--------|
| Display | Space Grotesk | 72px | Bold |
| H1 | Space Grotesk | 36px | Bold |
| H2 | Space Grotesk | 30px | Semi-Bold |
| Body | Space Grotesk | 16px | Regular |
| Code | JetBrains Mono | 14px | Regular |

### Spacing Scale

| Token | Value | Token | Value |
|-------|-------|-------|-------|
| `--space-1` | 4px | `--space-6` | 24px |
| `--space-2` | 8px | `--space-8` | 32px |
| `--space-3` | 12px | `--space-10` | 40px |
| `--space-4` | 16px | `--space-12` | 48px |
| `--space-5` | 20px | `--space-16` | 64px |

### Breakpoints

| Name | Min Width | Columns |
|------|-----------|---------|
| Mobile | 0px | 4 |
| Tablet | 640px | 8 |
| Desktop | 1024px | 12 |
| Wide | 1280px | 12 |
| Ultra | 1536px | 12 |

### Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 4px | Badges, tags |
| `--radius-md` | 6px | Buttons, inputs, cards |
| `--radius-lg` | 8px | Modals, popovers |
| `--radius-full` | 9999px | Pills, avatars |

## Usage Principles

1. **Strategy First** — Every design decision traces back to the brand strategy. When in doubt, ask: "Does this reflect The Builder?"
2. **Precision Over Decoration** — Add elements that serve function. If it doesn't clarify hierarchy, guide attention, or improve usability, remove it.
3. **Consistency Is Craft** — Use tokens, not magic numbers. Every color, spacing value, and font size should reference a token from this system.
4. **Accessible by Default** — Accessibility is not a feature or phase — it's a requirement built into every component from the start.
5. **Dense but Clear** — iFoundry interfaces often handle complex data (deployments, architectures, timelines). Favor information density with clear hierarchy over artificial whitespace.

## Getting Started

### For Designers
- Reference the color, typography, and spacing tokens as your source of truth
- Use the grid and layout specifications when creating new page templates
- Apply component patterns from UI Components before creating custom designs

### For Developers
- Implement the CSS tokens defined in each element document
- Use semantic HTML first, ARIA second (see Accessibility)
- Follow the responsive breakpoint system for all layouts
- Use the elevation and border tokens for consistent surface styling

### For Content Writers
- Begin with Voice & Tone to understand iFoundry's communication style
- Reference Language & Grammar for formatting conventions
- Use Designing Messages for all UI copy patterns
