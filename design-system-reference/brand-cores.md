# Design Quarks Explained

Design quarks are the single source of truth to name and store design decisions for consistent product experiences.

## What are design quarks?

Design quarks are name and value pairings that represent small, repeatable design decisions. A quark can be a color, font style, unit of white space, elevation shadow, or even a motion animation designed for a specific need.

Instead of choosing from hundreds of possible color values for an icon, you can apply a design quark that is consistent with all similar usages across your application:

```
color.icon.success
```

This ensures that success icons maintain the same visual treatment everywhere, and when the design evolves, you only need to update the quark value once.

## Why use design quarks?

### Simplified design and development
Design quarks streamline decision making and handover between design and development teams. No more debating which of 50 shades of blue to use—the quark tells you exactly which one fits your context.

### Centralized updates
As your visual language evolves, changes can be made once across the system and propagate throughout your application. No more finding and replacing hard-coded values in dozens of files.

### Enable theming
Features like global theming (dark mode), responsive design, and user customization are made possible with quarks. A theme is simply a collection of quark values designed to achieve a certain look or style.

### Consistency at scale
Quarks deliver visual consistency and quality improvements across your entire UI. Every team using the design system automatically inherits the same visual foundations.

### Reduced cognitive load
Designers and developers spend less time making micro-decisions about values and more time solving real user problems.

## Understanding quark names

A design quark's name describes how it should be used. Each part of the name communicates one piece of its usage.

### Naming structure

```
[foundation].[property].[variant].[state]
```

**Foundation**: The type of visual design attribute, such as:
- `color` - Color values
- `space` - Spacing values
- `elevation` - Shadow and layering
- `font` - Typography values

**Property**: The UI element the quark is being applied to, such as:
- `background` - Background colors
- `text` - Text colors
- `border` - Border styles
- `icon` - Icon colors

**Variant**: The specific use case or meaning:
- `success` - Positive outcomes
- `danger` - Errors or destructive actions
- `warning` - Cautionary states
- `information` - Neutral information
- `neutral` - Default or unbranded

**State**: The interaction state (optional):
- `hover` - Mouse hover state
- `pressed` - Active press state
- `disabled` - Inactive state

### Examples

```css
color.background.success.bold
/* A bold green background for success states */

color.text.danger
/* Red text color for error messages */

space.100
/* 8px spacing unit */

elevation.shadow.raised
/* Shadow for raised surfaces */

font.heading.large
/* Font settings for large headings */
```

## Types of design quarks

### Color quarks

Color quarks cover all color needs across your interface:

- **Text colors**: `color.text`, `color.text.subtle`, `color.text.inverse`
- **Background colors**: `color.background.neutral`, `color.background.selected`
- **Border colors**: `color.border`, `color.border.focused`
- **Icon colors**: `color.icon.success`, `color.icon.danger`
- **Link colors**: `color.link`, `color.link.visited`
- **Chart colors**: For data visualization
- **Skeleton colors**: For loading states

### Spacing quarks

Space quarks reduce decision making and allow for consistent spacing between elements:

```
space.0     /* 0px */
space.025   /* 2px */
space.050   /* 4px */
space.075   /* 6px */
space.100   /* 8px */
space.150   /* 12px */
space.200   /* 16px */
space.250   /* 20px */
space.300   /* 24px */
space.400   /* 32px */
space.500   /* 40px */
space.600   /* 48px */
```

These tokens are designed for both horizontal and vertical spacing in various contexts.

### Typography quarks

Typography quarks include font values for all text styles:

- **Font family**: Base font stacks for different contexts
- **Font size**: Standardized size scale
- **Font weight**: Weight values (regular, medium, bold)
- **Line height**: Leading for optimal readability

```
font.heading.xxlarge
font.heading.xlarge
font.heading.large
font.heading.medium
font.heading.small
font.body.large
font.body
font.body.small
```

### Elevation quarks

Elevation quarks control shadows and layering to create depth:

```
elevation.shadow.raised
elevation.shadow.overlay
elevation.shadow.modal
```

## How to choose the right quark

### Use semantic meaning, not appearance

**Do**: Choose quarks based on their intended meaning and purpose
```css
/* Good - semantic choice */
color: quark('color.text.danger')
```

**Don't**: Choose quarks just because the color looks right
```css
/* Bad - chosen only for appearance */
color: quark('color.background.success') /* Using a background color for text */
```

Choosing quarks by appearance alone can break the experience in different themes. Always match the quark's semantic purpose to your use case.

### Follow the token picker decision tree

When choosing a quark, ask yourself:

1. **What foundation am I working with?** (color, space, typography, etc.)
2. **What element am I styling?** (background, text, border, icon, etc.)
3. **What meaning does this convey?** (success, danger, neutral, etc.)
4. **What state is it in?** (default, hover, pressed, disabled, etc.)

### Check foundation-specific guidance

For detailed usage guidance, refer to the specific foundation pages:
- **Color foundation**: Color usage patterns and accessibility
- **Spacing foundation**: Layout and spacing principles
- **Typography foundation**: Text hierarchy and readability
- **Elevation foundation**: Depth and layering patterns

## Quarks in context

### Example: Success button

```jsx
// Using quarks for a success button
const SuccessButton = () => (
  <button
    style={{
      backgroundColor: quark('color.background.success.bold'),
      color: quark('color.text.inverse'),
      padding: `${quark('space.100')} ${quark('space.200')}`,
      borderRadius: quark('border.radius'),
      fontFamily: quark('font.body'),
    }}
  >
    Confirm
  </button>
);
```

### Example: Alert banner

```css
.alert-banner {
  background: var(--ds-background-danger);
  border-left: 4px solid var(--ds-border-danger);
  padding: var(--ds-space-200);
  border-radius: var(--ds-border-radius);
  color: var(--ds-text);
}
```

## Theming with quarks

A theme is a collection of quark values that work together to create a cohesive visual experience. With quarks, you can switch between themes globally:

**Light theme**:
- `color.background.neutral` → `#FFFFFF`
- `color.text` → `#172B4D`

**Dark theme**:
- `color.background.neutral` → `#1D2125`
- `color.text` → `#B6C2CF`

By using quarks instead of hard-coded values, your entire application can adapt to different themes automatically.

## Best practices

### Do's

✓ Use quarks that match your semantic intent
✓ Reference quarks by name, not by their current value
✓ Consult the token library when uncertain
✓ Use the token picker tool for guidance
✓ Follow foundation-specific recommendations
✓ Keep fallback values aligned with quark values during migration

### Don'ts

✗ Don't choose quarks just because colors look similar
✗ Don't use hard-coded values instead of quarks
✗ Don't create custom color values when a quark exists
✗ Don't ignore theme compatibility
✗ Don't mix old style values with quarks inconsistently

## Design quark lifecycle

Design quarks evolve over time through a managed lifecycle:

1. **Active**: Current, recommended quarks
2. **Deprecated**: Still functional but will be removed
3. **Soft-deleted**: Functional but raises warnings
4. **Deleted**: Removed from the system

Always use linting tools to stay informed about quark status and ensure smooth transitions during updates.

## Tools and resources

- **All design quarks**: Browse the complete quark library
- **Quark picker**: Interactive tool to find the right quark
- **Foundation guides**: Detailed usage for color, spacing, typography
- **Code examples**: Real-world implementation patterns
- **Linting plugins**: Automated quark validation and migration

## Getting help

When working with design quarks:
- Search the quark library for available options
- Use the quark picker for guided selection
- Review foundation-specific documentation
- Check component examples for patterns
- Consult with your design system team

---

**Next steps**: Learn how to [use quarks in code](./use-quarks-in-code.md) for implementation details.