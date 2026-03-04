# Nexus Coach Accessibility

> Enabling every coach, practice lead, and client to interact with the platform effectively.

## Strategic Foundation

**Brand Alignment:** Nexus Coach's value of Empowerment extends to every user, regardless of ability. Our mission is to make coaching practices run professionally — and that means the platform itself must be professionally inclusive. Accessibility isn't an enhancement; it's a core requirement that reflects The Guide archetype: we illuminate the path for everyone. If a coach can't navigate their dashboard, or a client can't complete onboarding, the platform has failed its purpose.

## Core Principles

### 1. Perceivable
Information and interface components must be presentable in ways all users can perceive — through sight, sound, or touch.

### 2. Operable
Interface components and navigation must be operable by everyone — keyboard, mouse, touch, voice, and assistive technologies.

### 3. Understandable
Information and operation of the interface must be understandable — clear language, predictable patterns, helpful error recovery.

### 4. Robust
Content must be robust enough to be interpreted reliably by a wide variety of user agents and assistive technologies.

## Color Contrast

### Minimum Requirements

| Content Type | Ratio | Standard |
|-------------|-------|----------|
| Normal text (<18px) | 4.5:1 | WCAG AA |
| Large text (18px+ or 14px bold) | 3:1 | WCAG AA |
| UI components and graphical objects | 3:1 | WCAG AA |
| Enhanced normal text | 7:1 | WCAG AAA |

### Nexus Coach Palette Contrast

| Combination | Ratio | Passes |
|-------------|-------|--------|
| Guide Teal on White | 5.5:1 | AA ✓ |
| Structure Slate on White | 16.7:1 | AAA ✓ |
| White on Guide Teal | 5.5:1 | AA ✓ |
| White on Structure Slate | 16.7:1 | AAA ✓ |
| Structure Slate on Momentum Amber | 5.3:1 | AA ✓ |
| Momentum Amber on White | 3.2:1 | Large text only |
| Slate 600 on White | 5.7:1 | AA ✓ |
| Slate 400 on White | 3.4:1 | Large text only |

### Color Independence
Never rely on color alone to convey information.

**Do:**
- Pair color with icons, patterns, or text labels
- Use text descriptions alongside status colors (e.g., "At Risk" label + amber icon)
- Include icons with colored client health badges
- Add underlines or other visual cues to text links

**Don't:**
- Use only red/green for error/success states
- Rely on color to indicate required form fields
- Use color as the sole differentiator in charts or data visualizations
- Assume users can distinguish between teal, blue, and green without labels

## Focus Management

### Visible Focus

Every interactive element must have a visible focus indicator.

```css
:focus-visible {
  outline: 2px solid var(--border-focus);
  outline-offset: 2px;
}
```

### Focus Order

- Ensure logical tab order follows visual flow (left-to-right, top-to-bottom)
- Use `tabindex="0"` for custom interactive elements that need keyboard access
- Avoid `tabindex` values greater than 0 — they disrupt natural flow
- Group related controls logically (form fields, navigation sections)

### Focus Trapping

For modals, drawers, and overlay dialogs:
- Trap focus within the modal when open
- Return focus to the trigger element on close
- First focusable element receives focus on open
- Escape key closes the modal

### Skip Links

Provide skip navigation for keyboard users to bypass the sidebar.

```html
<a href="#main-content" class="skip-link">
  Skip to main content
</a>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  padding: var(--space-2) var(--space-4);
  background: var(--color-primary);
  color: white;
  z-index: var(--z-toast);
  border-radius: 0 0 var(--radius-md) 0;
}

.skip-link:focus {
  top: 0;
}
```

## Keyboard Navigation

### Required Keyboard Support

| Element | Keys |
|---------|------|
| Links | Enter |
| Buttons | Enter, Space |
| Checkboxes | Space |
| Radio buttons | Arrow keys |
| Tabs | Arrow keys, Tab |
| Menus / Dropdowns | Arrow keys, Enter, Escape |
| Modals | Tab (trapped), Escape (close) |
| Sidebar navigation | Tab, Arrow keys, Enter |
| Date pickers | Arrow keys, Enter, Escape |
| Autocomplete / Search | Arrow keys, Enter, Escape |

### Custom Components

For custom interactive elements built with `<div>` or `<span>`:

```html
<div
  role="button"
  tabindex="0"
  aria-pressed="false"
  onkeydown="handleKeydown(event)"
>
  Toggle Option
</div>
```

Always provide:
- Appropriate `role` attribute
- `tabindex="0"` for focusability
- Keyboard event handlers (Enter, Space, Escape as needed)
- ARIA state attributes reflecting current state

## Screen Reader Support

### Semantic HTML

Use native HTML elements whenever possible — they provide built-in accessibility.

| Purpose | Element |
|---------|---------|
| Navigation | `<nav>` |
| Main content | `<main>` |
| Headings | `<h1>` – `<h6>` |
| Lists | `<ul>`, `<ol>`, `<li>` |
| Buttons | `<button>` |
| Links | `<a>` |
| Forms | `<form>`, `<label>`, `<input>` |
| Tables | `<table>`, `<thead>`, `<tbody>`, `<th>`, `<td>` |

### ARIA Labels

When semantic HTML isn't sufficient:

```html
<!-- Icon-only button -->
<button aria-label="Schedule session">
  <CalendarIcon aria-hidden="true" />
</button>

<!-- Form field with description -->
<input
  id="session-notes"
  aria-describedby="notes-hint notes-error"
/>
<p id="notes-hint">Summarize the key discussion points</p>
<p id="notes-error" role="alert">Session notes are required</p>
```

### Live Regions

Announce dynamic content changes to screen readers:

```html
<!-- Polite announcement (waits for pause) -->
<div aria-live="polite">
  Session notes saved successfully
</div>

<!-- Assertive announcement (interrupts) -->
<div aria-live="assertive" role="alert">
  Error: Unable to save session notes
</div>
```

### Landmark Regions

Structure pages with semantic landmarks:

```html
<header role="banner">...</header>
<nav role="navigation" aria-label="Main">...</nav>
<main role="main" id="main-content">...</main>
<aside role="complementary">...</aside>
<footer role="contentinfo">...</footer>
```

### Heading Hierarchy

- One `<h1>` per page (page title)
- Don't skip heading levels (H1 → H2 → H3, never H1 → H3)
- Use headings for structure, not styling — apply visual styles via CSS classes

## Motion & Animation

### Reduce Motion

Respect user preferences for reduced motion.

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Safe Animation Guidelines

- Keep animations under 5 seconds
- No flashing content (maximum 3 flashes per second)
- Provide pause/stop controls for auto-playing content
- Use subtle, functional animations — not decorative motion

### Animation Categories

| Type | Treatment with `prefers-reduced-motion` |
|------|----------------------------------------|
| Essential (loading spinners) | Keep, but simplify |
| Functional (page transitions) | Reduce duration, remove movement |
| Decorative (hover effects) | Remove completely |

## Form Accessibility

### Labels

Every input must have an associated label.

```html
<!-- Explicit association (preferred) -->
<label for="client-name">Client name</label>
<input id="client-name" type="text" />

<!-- Implicit association -->
<label>
  Client name
  <input type="text" />
</label>
```

### Error Handling

Make form errors discoverable and actionable.

```html
<div class="form-group">
  <label for="email">Email address</label>
  <input
    id="email"
    type="email"
    aria-invalid="true"
    aria-describedby="email-error"
  />
  <p id="email-error" class="error" role="alert">
    Enter a valid email address (example: jane@coachingfirm.com)
  </p>
</div>
```

### Required Fields

Indicate required fields clearly — not just with an asterisk.

```html
<label for="name">
  Name <span aria-hidden="true">*</span>
  <span class="visually-hidden">(required)</span>
</label>
<input id="name" type="text" required aria-required="true" />
```

### Form Instructions

Provide clear instructions before the form begins.

```html
<form aria-describedby="form-instructions">
  <p id="form-instructions">
    Fields marked with * are required. Session notes support plain text only.
  </p>
  <!-- form fields -->
</form>
```

## Touch & Pointer

### Target Size

Minimum touch target: 44×44 pixels (WCAG 2.5.5).

```css
.button,
.link,
.interactive {
  min-height: 44px;
  min-width: 44px;
}
```

### Spacing Between Targets

Maintain adequate spacing to prevent accidental activation.

```css
.button + .button {
  margin-left: var(--space-2); /* minimum 8px */
}
```

### Pointer Gestures

- Provide alternatives to complex gestures (pinch, swipe)
- Don't require path-based gestures for essential functions
- Support single-pointer alternatives for all interactions

## Images & Media

### Alternative Text

| Image Type | Alt Text |
|------------|----------|
| Informative | Describe the content or function |
| Decorative | Empty (`alt=""`) with `aria-hidden="true"` |
| Functional (icon/button) | Describe the action it performs |
| Complex (chart/diagram) | Provide detailed description or link to text equivalent |

```html
<!-- Informative -->
<img src="practice-health.png" alt="Practice health: 85% client engagement, 12 active coaches" />

<!-- Decorative -->
<img src="coaching-pattern.svg" alt="" aria-hidden="true" />

<!-- Functional -->
<button>
  <img src="schedule.svg" alt="Schedule session" />
</button>
```

## Testing Recommendations

### Automated Testing

| Tool | Purpose |
|------|---------|
| axe DevTools | Browser extension for automated checks |
| Lighthouse | Chrome built-in accessibility audit |
| WAVE | Visual accessibility evaluation |
| Pa11y | CI/CD pipeline integration |

### Manual Testing

| Test | Method |
|------|--------|
| Keyboard navigation | Tab through entire page without mouse |
| Screen reader | Test with NVDA (Windows) or VoiceOver (macOS) |
| Zoom | Verify layout at 200% browser zoom |
| Color contrast | Verify with contrast checker tools |
| Reduced motion | Enable `prefers-reduced-motion` and verify |

### Testing Checklist

- [ ] All images have appropriate alt text
- [ ] All form fields have visible, associated labels
- [ ] Error messages are programmatically associated with fields
- [ ] Color is not the only indicator of state or meaning
- [ ] Focus is visible on all interactive elements
- [ ] Page is fully navigable by keyboard alone
- [ ] Heading hierarchy is logical (no skipped levels)
- [ ] ARIA labels are accurate and descriptive
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Touch targets are at least 44×44px
- [ ] Skip link is present and functional
- [ ] Modals trap focus and return focus on close

## Utility Classes

### Visually Hidden

Hide content visually while keeping it accessible to screen readers.

```css
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## Usage Guidelines

### Do
- Test with real assistive technologies, not just automated tools
- Use semantic HTML elements first — reach for ARIA only when needed
- Provide text alternatives for all non-text content
- Ensure full keyboard operability for every interactive element
- Maintain visible focus states — never suppress them
- Include accessibility testing in the development workflow, not as an afterthought

### Don't
- Rely on automated testing alone — it catches roughly 30% of issues
- Use ARIA roles to override or replace semantic HTML elements
- Suppress focus outlines for visual aesthetics
- Assume all users navigate with a mouse
- Add `tabindex` values greater than 0
- Use placeholder text as a replacement for labels
