# iFoundry Media Accessibility

> Enabling everyone to interact with and navigate iFoundry products, regardless of ability or context.

## Strategic Foundation

**Brand Alignment:** iFoundry's Craftsmanship value demands that products are built right — and building right means building for everyone. Accessibility is not an afterthought or a compliance checkbox; it is a core engineering discipline. The Builder archetype takes pride in structural integrity, and that includes the invisible structure that ensures assistive technologies, keyboard navigation, and diverse user needs are handled with the same rigor as any other requirement.

## Standards & Compliance

### Target Conformance

| Standard | Level | Scope |
|----------|-------|-------|
| WCAG 2.1 | AA (minimum) | All product interfaces |
| WCAG 2.1 | AAA (target) | Color contrast, focus indicators |
| Section 508 | Compliant | All public-facing content |
| ARIA 1.2 | Best practices | Dynamic content, custom components |

### Legal & Ethical Basis
Accessibility is both a legal requirement (ADA, Section 508, EU Accessibility Act) and an expression of iFoundry's Partnership value — building products that work for everyone on the team, not just the majority.

## Color & Contrast

### Minimum Contrast Ratios

| Element | WCAG Level | Ratio | Notes |
|---------|------------|-------|-------|
| Body text | AA | 4.5:1 | Normal text (<24px) |
| Large text | AA | 3:1 | ≥24px or ≥18.5px bold |
| UI components | AA | 3:1 | Borders, icons, form controls |
| Focus indicators | AAA | 3:1 | Against adjacent colors |
| Decorative elements | — | No minimum | Non-functional visuals |

### iFoundry Color Contrast Verification

| Combination | Ratio | Pass |
|-------------|-------|------|
| Iron Slate `#0F172A` on White `#FFFFFF` | 16.75:1 | AA, AAA |
| Forge Blue `#1D4ED8` on White `#FFFFFF` | 5.92:1 | AA |
| Ignite Orange `#EA580C` on White `#FFFFFF` | 3.98:1 | Large text only |
| Slate 600 `#475569` on White `#FFFFFF` | 5.51:1 | AA |
| White `#FFFFFF` on Forge Blue `#1D4ED8` | 5.92:1 | AA |
| White `#FFFFFF` on Iron Slate `#0F172A` | 16.75:1 | AA, AAA |

### Color Usage Rules

- **Never** use color alone to convey meaning — always pair with text, icons, or patterns
- Error states: Red + error icon + descriptive text
- Success states: Green + check icon + success text
- Warning states: Orange + warning icon + explanation text
- Links: Blue underline (not just color change)

## Focus Management

### Focus Indicator Specification

All interactive elements must display a visible focus indicator when navigated via keyboard.

```css
:focus-visible {
  outline: 2px solid var(--border-focus);  /* Forge Blue */
  outline-offset: 2px;
  border-radius: var(--radius-md);
}

:focus:not(:focus-visible) {
  outline: none;
}
```

### Focus Order

- Focus order must follow visual reading order (left to right, top to bottom)
- Modal and dialog focus must be trapped within the component
- When a modal closes, focus returns to the triggering element
- Skip-to-content link must be the first focusable element

```html
<body>
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <nav>...</nav>
  <main id="main-content">...</main>
</body>
```

```css
.skip-link {
  position: absolute;
  top: -100%;
  left: var(--space-4);
  padding: var(--space-2) var(--space-4);
  background: var(--color-forge-blue);
  color: var(--color-white);
  border-radius: var(--radius-md);
  z-index: var(--z-command);
  font-size: var(--text-sm);
  font-weight: var(--font-semibold);
}

.skip-link:focus {
  top: var(--space-4);
}
```

### Focus Trapping (Modals, Dialogs)

When a modal opens:
1. Move focus to the first focusable element inside the modal
2. Trap Tab/Shift+Tab within the modal boundary
3. Escape closes the modal
4. On close, return focus to the element that opened the modal

## Keyboard Navigation

### Global Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Tab` | Move focus to next interactive element |
| `Shift + Tab` | Move focus to previous interactive element |
| `Enter` / `Space` | Activate focused element |
| `Escape` | Close modal, dismiss popover, clear search |
| `Arrow Keys` | Navigate within menus, tabs, lists |

### Component-Specific Navigation

| Component | Keys | Behavior |
|-----------|------|----------|
| Dropdown Menu | `↑` `↓` | Navigate items |
| Dropdown Menu | `Enter` | Select item |
| Dropdown Menu | `Escape` | Close menu |
| Tabs | `←` `→` | Switch tabs |
| Tabs | `Home` / `End` | First / last tab |
| Modal | `Tab` / `Shift+Tab` | Cycle within modal |
| Modal | `Escape` | Close |
| Sidebar Nav | `↑` `↓` | Navigate items |
| Sidebar Nav | `Enter` | Activate item |
| Table | `↑` `↓` `←` `→` | Navigate cells |
| Combobox | `↑` `↓` | Navigate options |
| Combobox | `Enter` | Select option |
| Toast | Auto-dismiss or `Escape` | Dismiss |

## Screen Reader Support

### Semantic HTML
Use correct HTML elements before adding ARIA attributes. Semantic HTML provides built-in accessibility.

| Purpose | Use | Not |
|---------|-----|-----|
| Navigation | `<nav>` | `<div class="nav">` |
| Main content | `<main>` | `<div class="content">` |
| Page sections | `<section>` with heading | `<div>` |
| Headings | `<h1>`–`<h6>` in order | `<div class="heading">` |
| Buttons | `<button>` | `<div onclick>` |
| Links | `<a href>` | `<span onclick>` |
| Lists | `<ul>` / `<ol>` | Styled `<div>` groups |
| Tables | `<table>` with `<th>` | CSS grid mimicking tables |
| Forms | `<form>` with `<label>` | `<div>` wrappers |

### ARIA Usage

Use ARIA to enhance, not replace, semantic HTML.

```html
<!-- Landmark regions -->
<nav aria-label="Main navigation">...</nav>
<nav aria-label="Breadcrumb">...</nav>
<main aria-label="Project dashboard">...</main>

<!-- Live regions for dynamic content -->
<div aria-live="polite" aria-atomic="true">
  <!-- Toast messages, status updates -->
</div>

<!-- Loading states -->
<button aria-busy="true" aria-disabled="true">
  <span class="spinner" aria-hidden="true"></span>
  Deploying...
</button>

<!-- Form validation -->
<input
  type="email"
  aria-invalid="true"
  aria-describedby="email-error"
/>
<span id="email-error" role="alert">Enter a valid email address.</span>

<!-- Expandable sections -->
<button aria-expanded="false" aria-controls="details-panel">
  Project Details
</button>
<section id="details-panel" hidden>...</section>
```

### Announcements for Dynamic Content

| Event | Method | Priority |
|-------|--------|----------|
| Toast notification | `aria-live="polite"` | Normal |
| Error message | `role="alert"` | Assertive |
| Loading state | `aria-busy="true"` | — |
| Page navigation | Document title update | — |
| Form submission result | `aria-live="polite"` | Normal |
| Deployment status change | `role="status"` | Normal |

## Motion & Animation

### Respecting User Preferences

```css
/* Default: animations enabled */
.element {
  transition: transform 200ms ease, opacity 200ms ease;
}

/* Reduce animations for users who prefer it */
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

### Animation Guidelines

| Type | Duration | Easing | Reduce-Motion Fallback |
|------|----------|--------|------------------------|
| Micro-interactions | 100–200ms | ease-out | Instant |
| Page transitions | 200–300ms | ease-in-out | Instant |
| Loading spinners | Continuous | linear | Static indicator |
| Hover effects | 150ms | ease | No animation |
| Modal open/close | 200ms | ease-out / ease-in | Instant show/hide |

### Rules
- No animation should be required to understand content
- Avoid flashing content (3 flashes per second maximum)
- Auto-playing animations must have a visible pause/stop control
-Content carousels must be pausable and navigable with keyboard

## Responsive & Adaptive

### Zoom & Reflow
- Content must be functional at 200% zoom without horizontal scrolling
- Text must resize up to 200% without loss of content
- Touch targets must be at least 44×44px

### High Contrast Mode
- Test with Windows High Contrast Mode and `forced-colors: active`
- Don't override system colors in forced-colors mode — let the browser apply them

```css
@media (forced-colors: active) {
  .button {
    border: 1px solid ButtonText;
  }

  .badge {
    border: 1px solid;
  }
}
```

## Testing

### Automated Testing
| Tool | Purpose | Integration |
|------|---------|-------------|
| axe-core | Automated WCAG auditing | CI pipeline |
| eslint-plugin-jsx-a11y | JSX accessibility linting | Editor / Build |
| Lighthouse | Performance + accessibility audit | CI pipeline |
| Pa11y | Page-level accessibility testing | CI pipeline |

### Manual Testing Checklist

| Category | Test |
|----------|------|
| Keyboard | Navigate entire page using only keyboard |
| Keyboard | All interactive elements reachable via Tab |
| Keyboard | Focus indicators visible on every element |
| Keyboard | No keyboard traps (except intentional modal traps) |
| Screen Reader | All images have alt text (or `aria-hidden`) |
| Screen Reader | Form inputs have labels |
| Screen Reader | Dynamic content announced appropriately |
| Screen Reader | Page title updates on navigation |
| Visual | Color contrast passes 4.5:1 for text |
| Visual | Information not conveyed by color alone |
| Visual | Content reflows at 200% zoom |
| Visual | Animations respect `prefers-reduced-motion` |
| Touch | Touch targets ≥ 44×44px |
| Touch | No hover-only interactions on touch devices |

### Screen Reader Testing Matrix

| Screen Reader | Browser | Priority |
|---------------|---------|----------|
| VoiceOver | Safari (macOS) | Primary |
| NVDA | Firefox (Windows) | Primary |
| JAWS | Chrome (Windows) | Secondary |
| TalkBack | Chrome (Android) | Secondary |

## Usage Guidelines

### Do
- Use semantic HTML as the foundation for every component
- Test with keyboard navigation during development, not just after
- Write descriptive alt text for functional images
- Use `aria-label` for icon-only buttons
- Announce dynamic state changes with live regions
- Include accessibility acceptance criteria in all user stories

### Don't
- Use ARIA when semantic HTML provides the same information
- Remove focus outlines without providing an alternative indicator
- Use `tabindex` values greater than 0 (disrupts natural focus order)
- Rely on color alone to distinguish states or categories
- Auto-play audio or video without user controls
- Use generic alt text like "image" or "icon"
