# SpikeForge Illustrations

> Clean, structured illustrations that simplify complexity and guide coaches with visual clarity.

## Strategic Foundation

**Brand Alignment:** SpikeForge illustrations embody The Architect's precision and The Guide's clarity. They simplify operational concepts — workflows, coaching relationships, practice structures — into clean, approachable visuals. Illustrations are functional, not decorative. They explain what words alone can't, reduce cognitive load, and reinforce that a well-run practice feels organized, intentional, and calm.

## Illustration Style

### Overall Approach
- **Geometric and clean:** Built from simple shapes — circles, rectangles, lines — with consistent proportions
- **Flat with subtle depth:** Primarily flat design with minimal shadow for layering where needed
- **Brand-colored:** Drawn from the SpikeForge palette (teal, slate, amber accents)
- **Human but simplified:** People representations are abstract — silhouettes or minimal figures — not detailed portraits
- **Purposeful:** Every illustration explains a concept, guides a workflow, or represents a state

### Visual Characteristics

| Attribute | Value |
|-----------|-------|
| Line weight | 1.5px (consistent with icon stroke) |
| Corner radius | Rounded (matching `--radius-md` to `--radius-lg`) |
| Color palette | Brand colors at 100% and reduced opacities (10%, 20%, 40%) |
| Shadows | Minimal — soft, brand-colored shadows at 8-12% opacity |
| Backgrounds | Transparent or Slate 50 (`#F8FAFC`) |
| Grid alignment | Aligned to 8px grid |

## Illustration Types

### 1. Spot Illustrations
Small, focused illustrations that accompany UI elements and content.

| Attribute | Value |
|-----------|-------|
| Size | 48–120px |
| Complexity | Low — 1-2 elements |
| Color | 2-3 brand colors max |
| Format | SVG |

**Used for:**
- Empty states ("No sessions scheduled yet")
- Feature callouts in onboarding
- Status indicators on dashboards
- List item decorations

**Examples:**
- A calendar with a checkmark (session complete)
- Two simplified figures with a connection line (coach-client match)
- A clipboard with a progress bar (onboarding status)
- A chart with an upward trend (practice growth)

### 2. Scene Illustrations
Larger narrative illustrations that explain concepts, features, or workflows.

| Attribute | Value |
|-----------|-------|
| Size | 200–600px |
| Complexity | Medium — 3-5 elements |
| Color | Full brand palette |
| Format | SVG or PNG @2x |

**Used for:**
- Marketing landing page features
- Onboarding walkthroughs
- Help documentation headers
- Blog post headers

**Examples:**
- A practice lead viewing a dashboard with coach avatars and client health signals
- A coaching session workflow: preparation → session → notes → follow-up
- A prospect pipeline funnel from inquiry to enrolled client
- Multiple coaches connected to a central practice hub

### 3. Diagram Illustrations
Technical visual explanations of workflows, processes, and system relationships.

| Attribute | Value |
|-----------|-------|
| Size | 300–800px |
| Complexity | High — multiple connected elements |
| Color | Full brand palette with connector lines |
| Format | SVG |

**Used for:**
- Workflow documentation (session lifecycle, client journey)
- Feature comparison layouts
- Architecture overviews
- Process flowcharts

**Examples:**
- Client lifecycle: Prospect → Discovery → Onboarding → Active → Completion
- Session flow: Prepare → Conduct → Document → Follow Up
- Practice structure: Practice Lead → Coaches → Clients (hierarchy)
- Billing flow: Package enrollment → Session tracking → Invoice generation

## Character Style

Human figures in SpikeForge illustrations are abstract and inclusive.

### Approach
- **Simplified silhouettes:** No facial features, minimal detail
- **Geometric proportions:** Head, body, limbs as simple shapes
- **Skin tone agnostic:** Use brand colors (teal, slate, amber) rather than skin tones
- **Role differentiation:** Distinguish coaches, clients, and practice leads through context (desk vs. couch, dashboard vs. notebook) rather than appearance
- **Postures over faces:** Convey emotion through body language — leaning in (engaged), standing tall (confident), gesturing (guiding)

### Size Guidelines

| Context | Height | Detail Level |
|---------|--------|-------------|
| Spot illustration | 24–48px | Abstract shape only |
| Scene illustration | 60–120px | Simplified body, posture visible |
| Diagram | 32–64px | Icon-like, role-differentiated |

## Complexity Levels

### Level 1 — Simple
Single element, 2 colors, no background. For in-app micro-moments.

```
Elements: 1-2
Colors: 2 (primary + neutral)
Detail: Minimal
Example: A checkmark on a card (task completed)
```

### Level 2 — Moderate
Small scene, 3-4 colors, optional simple background. For features and states.

```
Elements: 3-5
Colors: 3-4 (primary + secondary + neutral)
Detail: Moderate — shapes suggest context
Example: A coach figure reviewing a dashboard widget
```

### Level 3 — Detailed
Full scene or workflow, full palette, background elements. For marketing and documentation.

```
Elements: 5+
Colors: Full palette
Detail: Higher — clear narrative or process
Example: End-to-end client journey with connected stages
```

## Color Application

### Primary Palette in Illustrations

| Color | Role in Illustrations |
|-------|----------------------|
| Cobalt Signal `#2E5BFF` | Primary subjects, active elements, connection lines |
| Teal 100 `#CCFBF1` | Teal background fills, highlight areas |
| Teal 50 `#F0FDFA` | Subtle fills, background panels |
| Midnight Ink `#0B1220` | Text elements, high-contrast lines |
| Slate 200 `#E2E8F0` | Background shapes, inactive elements |
| Slate 400 `#94A3B8` | Secondary elements, dashed lines |
| Momentum Amber `#D97706` | Accent moments, CTAs, highlights |
| Amber 100 `#FEF3C7` | Warm highlight fills |

### Opacity Usage
- 100% — Primary subject elements
- 40% — Secondary elements that support the narrative
- 20% — Background shapes and containers
- 10% — Subtle fills and atmosphere

## Accessibility

- Illustrations must not be the sole method of conveying critical information
- Provide descriptive `alt` text for all illustrations that convey meaning
- Use `alt=""` with `aria-hidden="true"` for purely decorative illustrations
- Ensure sufficient contrast between illustration elements and their backgrounds
- Avoid color as the only differentiator between elements — use shape and position

## Usage Guidelines

### Do
- Use illustrations to simplify complex coaching workflows
- Maintain consistent geometric style across all illustrations
- Align illustrations to the 8px grid
- Use brand colors at approved opacity levels
- Pair illustrations with clear text labels or descriptions
- Use spot illustrations in empty states to reduce visual emptiness

### Don't
- Create realistic or photographic-style illustrations
- Use illustrations as pure decoration without communicative purpose
- Mix illustration styles within the same context
- Use colors outside the brand palette
- Add excessive detail that competes with adjacent UI elements
- Use illustrations to replace UI content that should be interactive
