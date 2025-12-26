# OpenLife Accessibility

> Enabling everyone to interact with and navigate OpenLife applications effectively.

## Strategic Foundation

**Brand Alignment:** OpenLife's mission of democratizing life insurance technology extends to everyone—regardless of ability. Our value of Empowerment means designing inclusive experiences that don't exclude. Accessibility isn't an afterthought; it's a core requirement aligned with our Liberator archetype.

## Core Principles

### 1. Perceivable
Information and interface components must be presentable in ways users can perceive.

### 2. Operable
Interface components and navigation must be operable by everyone.

### 3. Understandable
Information and operation of the interface must be understandable.

### 4. Robust
Content must be robust enough to be interpreted by assistive technologies.

## Color Contrast

### Minimum Requirements

| Content Type | Ratio | Standard |
|-------------|-------|----------|
| Normal text | 4.5:1 | WCAG AA |
| Large text (18px+) | 3:1 | WCAG AA |
| UI components | 3:1 | WCAG AA |
| Enhanced (AAA) | 7:1 | WCAG AAA |

### OpenLife Palette Contrast

| Combination | Ratio | Passes |
|-------------|-------|--------|
| Liberation Blue on White | 4.6:1 | AA ✓ |
| Foundation Navy on White | 15.2:1 | AAA ✓ |
| White on Liberation Blue | 4.6:1 | AA ✓ |
| White on Foundation Navy | 15.2:1 | AAA ✓ |
| Transform Orange on White | 3.2:1 | Large text only |

### Color Independence
Never rely on color alone to convey information.

**Do:**
- Pair color with icons, patterns, or text labels
- Use text descriptions alongside status colors
- Include icons with colored badges

**Don't:**
- Use only red/green for error/success
- Rely on color to indicate required fields
- Use color as the only differentiator in charts

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

- Ensure logical tab order (follows visual flow)
- Use `tabindex="0"` for custom interactive elements
- Avoid `tabindex` values greater than 0
- Group related controls logically

### Focus Trapping

For modals and dialogs:
- Trap focus within the modal when open
- Return focus to trigger element on close
- First focusable element receives focus on open

### Skip Links

Provide skip navigation for keyboard users.

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
| Menus | Arrow keys, Enter, Escape |
| Modals | Tab (trapped), Escape (close) |
| Autocomplete | Arrow keys, Enter, Escape |

### Custom Components

For custom interactive elements:
- Add `role` attribute
- Add `tabindex="0"`
- Handle keyboard events
- Announce state changes

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

## Screen Reader Support

### Semantic HTML

Use native HTML elements whenever possible.

| Purpose | Element |
|---------|---------|
| Navigation | `<nav>` |
| Main content | `<main>` |
| Headings | `<h1>` - `<h6>` |
| Lists | `<ul>`, `<ol>`, `<li>` |
| Buttons | `<button>` |
| Links | `<a>` |
| Forms | `<form>`, `<label>`, `<input>` |

### ARIA Labels

When semantic HTML isn't sufficient:

```html
<!-- Icon-only button -->
<button aria-label="Close modal">
  <CloseIcon aria-hidden="true" />
</button>

<!-- Form field with description -->
<input 
  id="email"
  aria-describedby="email-hint email-error"
/>
<p id="email-hint">We'll use this for notifications</p>
<p id="email-error" role="alert">Please enter a valid email</p>
```

### Live Regions

Announce dynamic content changes:

```html
<!-- Polite announcement (waits) -->
<div aria-live="polite">
  Changes saved successfully
</div>

<!-- Assertive announcement (interrupts) -->
<div aria-live="assertive" role="alert">
  Error: Unable to save changes
</div>
```

### Landmark Regions

Structure pages with landmarks:

```html
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<aside role="complementary">...</aside>
<footer role="contentinfo">...</footer>
```

### Heading Hierarchy

Maintain proper heading structure:

- One `<h1>` per page
- Don't skip heading levels
- Use headings for structure, not styling

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
- Avoid flashing content (no more than 3 flashes/second)
- Provide pause controls for auto-playing content
- Use subtle, functional animations

### Essential vs Decorative

| Type | Treatment |
|------|-----------|
| Essential (loading indicators) | Keep, but simplify |
| Functional (transitions) | Reduce duration/distance |
| Decorative (parallax) | Remove completely |

## Form Accessibility

### Labels

Every input needs an associated label.

```html
<!-- Explicit association -->
<label for="username">Username</label>
<input id="username" type="text" />

<!-- Implicit association -->
<label>
  Username
  <input type="text" />
</label>
```

### Error Handling

Make errors discoverable and understandable.

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
    Please enter a valid email address
  </p>
</div>
```

### Required Fields

Indicate required fields clearly.

```html
<label for="name">
  Name <span aria-hidden="true">*</span>
  <span class="visually-hidden">(required)</span>
</label>
<input id="name" type="text" required aria-required="true" />
```

### Form Instructions

Provide clear instructions before the form.

```html
<form>
  <p id="form-instructions">
    Fields marked with * are required.
  </p>
  <!-- form fields -->
</form>
```

## Touch & Pointer

### Target Size

Minimum touch target: 44×44 pixels (WCAG 2.5.5)

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
  margin-left: var(--space-2); /* 8px minimum */
}
```

### Pointer Gestures

- Provide alternatives to complex gestures
- Don't require path-based gestures for essential functions
- Support single-pointer alternatives

## Images & Media

### Alternative Text

Provide meaningful alt text for images.

| Image Type | Alt Text |
|------------|----------|
| Informative | Describe content/function |
| Decorative | Empty (`alt=""`) |
| Functional | Describe action |
| Complex | Detailed description |

```html
<!-- Informative -->
<img src="chart.png" alt="Q3 revenue: $2.4M, up 15% from Q2" />

<!-- Decorative -->
<img src="decorative-line.svg" alt="" />

<!-- Functional -->
<img src="search.svg" alt="Search" />
```

### Video Content

- Provide captions for all video content
- Offer transcripts for audio content
- Include audio descriptions when visual content isn't described in dialogue

## Testing Recommendations

### Automated Testing

| Tool | Purpose |
|------|---------|
| axe DevTools | Browser extension |
| Lighthouse | Chrome audit |
| WAVE | Accessibility evaluation |
| Pa11y | CI/CD integration |

### Manual Testing

| Test | Method |
|------|--------|
| Keyboard navigation | Tab through entire page |
| Screen reader | Test with NVDA/VoiceOver |
| Zoom | Test at 200% zoom |
| Color contrast | Use contrast checker tools |
| Motion | Enable reduced motion |

### Testing Checklist

- [ ] All images have appropriate alt text
- [ ] Form fields have visible labels
- [ ] Error messages are associated with fields
- [ ] Color is not the only indicator
- [ ] Focus is visible on all interactive elements
- [ ] Page is navigable by keyboard alone
- [ ] Heading hierarchy is logical
- [ ] ARIA labels are accurate
- [ ] Animations respect reduced motion
- [ ] Touch targets are adequately sized

## Utility Classes

### Visually Hidden

Hide content visually while keeping it accessible.

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

### Skip Navigation

Visible only on focus.

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: 16px;
  padding: 8px 16px;
  background: var(--color-primary);
  color: white;
  z-index: 9999;
}
.skip-link:focus {
  top: 16px;
}
```

## Usage Guidelines

### Do
- Test with real assistive technologies
- Use semantic HTML first
- Provide text alternatives
- Ensure keyboard operability
- Maintain visible focus states
- Document accessibility features

### Don't
- Disable zoom or scaling
- Remove focus outlines without replacement
- Rely on color alone
- Use non-descriptive link text ("click here")
- Auto-play audio or video
- Create keyboard traps

## Accessibility Statement

Include an accessibility statement on your site:

- Commitment to accessibility
- Conformance level (WCAG 2.1 AA)
- Known limitations
- Contact information for feedback
- Date of last review
