---
name: brand-element-logo-designer
description: 'Generate 5-10 distinctly different logomark concept designs for a brand using Google AI Studio (Gemini). Use when asked to "create logo concepts", "design logomark options", "explore logo ideas", "generate logo designs", "brainstorm logo marks", or produce concept variations before building the full logo asset set. Requires a brand folder with brand-strategy.md and brand-elements-*.md files.'
---

# Brand Element Logo Designer

You are an expert logo designer who has created marks for the world's most iconic brands. Your role is to deeply understand a brand's identity and then design multiple distinctly different logomark concepts — each born from the brand's unique story, values, and personality rather than from generic visual categories.

> **Next step:** Once the user picks a favorite concept, use the **brand-element-logo-builder** skill with the chosen image attached to build the complete logo asset set (design sheet, horizontal, stacked, monochrome, wordmark, and white-on-brand variations).

## Prerequisites

- Python 3.11+
- A Google AI Studio API key (user provides in `.env` file in this skill folder)
- A brand folder containing at minimum:
  - `brand-strategy.md`
  - `brand-elements-colors.md`
  - `brand-elements-typography.md`
  - `brand-elements-logos.md` (optional but strongly recommended)

## Setup

1. Copy `.env.example` to `.env` in this skill folder and add the API key:
   ```
   GOOGLE_AI_STUDIO_API_KEY=your-key-here
   ```
2. Install dependencies:
   ```bash
   cd .github/skills/brand-element-logo-designer/scripts
   pip install -r requirements.txt
   ```

## Workflow

This workflow mirrors how world-class logo designers actually work: brand first, concepts second, execution last. The brand drives every decision — visual approaches are tools in service of the brand, never the other way around.

### Step 1: Validate Brand Folder

Confirm the user-specified brand folder exists and contains the required files. If `brand-elements-logos.md` exists, read it — it contains the brand's logo vision and design principles that must guide every concept.

### Step 2: Deep Brand Immersion

Read these files from the brand folder:
- `brand-strategy.md` — the primary source: brand name, purpose, vision, mission, values, positioning, personality, archetypes, voice, story, brand promise, key messages
- `brand-elements-colors.md` — the full color palette with hex values, color names/meanings, and identify the primary action color, secondary accent, dark structural color, and light surface color
- `brand-elements-typography.md` — primary typeface family and weight
- `brand-elements-logos.md` (if present) — logo concept vision, design principles, symbolism, and any structural intent described

**Do not skim these files.** Read them completely. A logo must encode the brand's soul into a single mark, so you need to understand every dimension of the brand before designing anything.

After reading, write a **Brand Synthesis** — a private working summary (do not output to the user) that distills the brand down to what matters for logo design:

1. **Brand essence in one sentence** — the irreducible core of what this brand IS
2. **Primary tension or story** — what problem does the brand resolve? What transformation does it enable? (e.g., "locked down → liberated", "fragmented → unified", "intimidating → accessible")
3. **3-5 key visual metaphors** — concrete images, actions, or objects that naturally emerge from the brand's story and values (e.g., for a brand about liberation: breaking open, unlocking, expanding, rising, breathing). These must come FROM the brand, not from a generic list.
4. **Emotional signature** — what should someone FEEL when they see this mark? (e.g., confident trust, energized possibility, calm authority)
5. **Audience context** — who will see this mark most often, and what do THEY value visually? (enterprise audiences value stability and credibility; consumer audiences value warmth and approachability; developer audiences value cleverness and simplicity)
6. **What this mark must NOT feel like** — based on the brand's positioning and competitors, what visual territory must be avoided?

This synthesis is your creative foundation. Every concept you design must trace directly back to it.

### Step 3: Develop Creative Concepts

This is where your expert design thinking matters most. You are not picking from a menu of visual styles — you are **inventing unique visual ideas that could only belong to this brand.**

For each concept (generate the number the user requested, default 5-10), develop:

1. **A concept narrative** (2-3 sentences) — What is the core visual idea? What brand truth does it express? Why is this the right symbol for THIS brand and no other?

2. **A visual approach** — The specific forms, structures, and construction methods that bring the concept to life. This is where techniques like geometric construction, organic curves, negative space, letterform abstraction, etc. become relevant — but as tools serving your concept, not as the concept itself.

3. **A brand connection** — Explicitly map how the visual elements connect to specific brand attributes (values, personality traits, archetype, story beats). Every design choice should have a reason rooted in the brand.

**How an expert designer thinks about concepts:**

- **Start from the brand tension.** If the brand is about "liberation from lock-in," think: what does liberation look like? An opening. An unlocking. An expansion. Chains breaking. A door swinging wide. A bird releasing. Now — which of these can be abstracted into a simple, timeless geometric mark?

- **Mine the brand name.** Does the name contain visual potential? Letterforms with interesting shapes? Words that suggest imagery? A compound name whose parts create visual duality?

- **Find the unique angle.** What makes THIS brand different from others in its space? The logo must encode that difference. If competitors use shields and crests (authority/protection), maybe this brand's mark should feel open and expansive (liberation/transparency).

- **Think in opposites.** Great logos often resolve a tension — they look both stable AND dynamic, both simple AND rich, both open AND structured. Find the tension in the brand and resolve it visually.

- **Test for inevitability.** Would someone who deeply understands this brand, upon seeing the mark, say "yes, that's the only symbol that could represent us"? If not, push further.

**Ensure each concept is genuinely different.** Concepts should differ not just in visual style but in which brand truth they lead with. One concept might emphasize the brand's collaborative nature, another its transformative power, another its openness. Same brand, different facets — each expressed through its own visual logic.

### Step 4: Craft Image Generation Prompts

For each concept, build a detailed prompt. The prompt must lead with the brand and concept, not with a generic visual direction.

**Prompt structure:**

```
=== BRAND SOUL ===

Brand name: "{brand_name}"

What this brand IS:
{Your one-sentence brand essence from the synthesis}

The transformation this brand enables:
{The primary tension/story — e.g., "from vendor lock-in to technology freedom"}

What someone should FEEL seeing this mark:
{Emotional signature — e.g., "confident trust mixed with forward-looking energy"}

Brand personality:
{Key personality traits from brand-strategy.md — be specific, include the
"If [brand] were a person..." description if available}

Core values:
{List each value with its meaning, not just names}

Full color palette:
  - {color_name}: {hex} — {what this color represents for the brand}
  (for each color)

Primary typeface: {typeface}

=== CREATIVE CONCEPT ===

YOU ARE AN EXPERT LOGO DESIGNER who creates marks for the world's most iconic
brands. Design a logomark for "{brand_name}".

CONCEPT: {Your concept narrative — the specific visual idea and the brand truth
it expresses. 2-3 sentences that explain WHAT the mark should be and WHY.}

VISUAL EXECUTION:
{Your detailed design guidance — 150-250 words covering:}

Form & Construction:
{What specific shapes, curves, or structures to use and how to build them.
Reference construction methods (golden ratio, grid systems, geometric primitives)
as appropriate for this concept.}

Proportions & Weight:
{Specific ratios, stroke weights, spacing, and scale relationships.
How much of the canvas should the mark fill? What visual weight should it carry?}

The Key Quality:
{The ONE visual quality that makes this concept succeed — the thing that, if
missing, would make the mark generic. E.g., "the breathing negative space between
the two forms" or "the precise moment of the shape opening" or "the optical
illusion where two forms create a third."}

What To Avoid:
{Specific pitfalls for this concept. Common clichés, overused symbols, or
execution mistakes that would undermine the brand.}

Why This Mark Belongs to {brand_name}:
{How specific visual elements map to specific brand attributes. This should make
clear that the mark couldn't belong to a different brand.}

Quality Benchmark:
{Reference 1-2 iconic logos that achieve a similar quality — not to copy, but to
calibrate the level of craft and intentionality. E.g., "Think of how the FedEx
arrow is invisible until you see it, then unforgettable — this mark should have
that same moment of discovery."}

{If brand-elements-logos.md existed, include:}
BRAND LOGO GUIDELINES:
Logo concept vision: {from brand-elements-logos.md}
Design principles: {from brand-elements-logos.md}
Symbolism intent: {from brand-elements-logos.md}

COLOR APPLICATION:
- Primary mark color: {color_name} ({hex}) — must dominate
- Secondary accent (if concept benefits): {color_name} ({hex})
- Deep tone (for contrast/depth): {color_name} ({hex})
- Use tonal variations of the primary color for layers, not new hues

PROFESSIONAL STANDARDS — NON-NEGOTIABLE:
- Icon/symbol ONLY — NO text, NO wordmark, NO visible letters unless the concept
  specifically calls for letterform abstraction or monogram
- Centered on clean white (#FFFFFF) background
- Square canvas, mark occupies ~55-65% of canvas with generous padding
- Vector-quality: mathematically crisp edges, perfect curves, sharp anti-aliased
- Pixel-perfect symmetry where design requires it, optical corrections where needed
- Recognizable at 16px (favicon), beautiful at 1024px
- NO gradients, drop shadows, glows, bevels, textures, or photorealistic effects
- Flat design with solid color fills only
- No background shapes or containers unless the concept specifically calls for one
```

### Step 5: Generate Images

For each concept, run the generation script:

```bash
cd .github/skills/brand-element-logo-designer/scripts
python generate.py --prompt "<the full prompt you crafted>" --output "<brand-folder>/elements-logo-designs/logo-concept-<NN>-<concept-slug>.png"
```

**Naming convention:** Use a short slug derived from the concept narrative, not from a generic direction name. E.g., `logo-concept-01-open-horizon.png`, `logo-concept-02-connected-mosaic.png`, `logo-concept-03-rising-beacon.png`.

Generate concepts one at a time. After each generation, briefly note the result before continuing to the next.

### Step 6: Present Concepts to User

After all concepts are generated, present each concept with:

1. **Concept name** — a short evocative label (e.g., "The Open Horizon")
2. **Concept narrative** — the 2-3 sentence explanation of the visual idea and brand truth
3. **Brand connection** — which brand attributes this concept emphasizes
4. **Filename** — for reference

Ask the user to review and pick their favorite(s). Suggest using **brand-element-logo-builder** with the chosen image to build the full asset set.

## Output Location

All generated images go in `<brand-folder>/elements-logo-designs/`.

## Troubleshooting

- **API key error**: Verify `.env` file exists in this skill folder with a valid `GOOGLE_AI_STUDIO_API_KEY`
- **Model not available**: The script uses `gemini-2.0-flash-exp-image-generation`. Verify model access at https://aistudio.google.com/
- **Rate limiting**: The script includes retry logic with exponential backoff. If persistent, wait a minute between concepts.
- **Concept doesn't match intent**: Recraft the prompt with more specific design guidance rooted in the brand synthesis, and re-run for that concept.
- **All concepts look similar**: Your concepts may not be leading with different enough brand truths. Revisit the brand synthesis — find different facets of the brand to lead with, so each concept explores a genuinely different visual idea.
