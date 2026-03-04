---
name: brand-element-logo-builder
description: 'Build a complete logo asset set from a canonical logomark using Google AI Studio (Gemini). Use when asked to "build logo assets", "create logo variations", "create logo design sheet", "generate brand logo set", or produce the full set of logo files. Pairs with brand-element-logo-designer (which generates concept options first). Requires brand context provided by the user (strategy, colors, typography, logo guidelines).'
---

# Brand Element Logo Builder

Build a complete logo asset set — design sheet, individual logo variations, and platform-specific derivatives — for a brand using Google AI Studio's Gemini image generation and Pillow image processing. Uses a **phased generation approach**: a canonical logomark is created first (or provided by the user), then a design sheet, then all remaining variations reference both images, and finally derivative assets are produced by resizing/composing the generated images.

> **Tip:** Use the **brand-element-logo-designer** skill first to generate 5-10 concept logomark options. Once the user picks a favorite, attach that image when invoking this skill to build the full asset set.

## Prerequisites

- Python 3.11+
- A Google AI Studio API key (user provides in `.env` file in this skill folder)
- Brand context provided by the user (brand strategy, colors, typography, logo guidelines, etc.)

## Setup

1. Copy `.env.example` to `.env` in this skill folder and add the API key:
   ```
   GOOGLE_AI_STUDIO_API_KEY=your-key-here
   ```
2. Install dependencies:
   ```bash
   cd .github/skills/brand-element-logo-builder/scripts
   pip install -r requirements.txt
   ```

## Workflow

### Step 1: Gather Brand Context

Gather and absorb all brand context provided by the user. This may include brand strategy, color palettes, typography, logo guidelines, or any other brand documentation — whether supplied as files, conversation context, or direct descriptions.

Look for and deeply study:
- **Brand strategy** — brand name, tagline, purpose, vision, mission, values, positioning, personality, archetypes, voice, story
- **Color palette** — hex values, color names/meanings, primary action color, secondary accent, dark structural color, light surface color
- **Typography** — primary typeface family and weights
- **Logo guidelines** (if provided) — logo concept vision, design principles, symbolism, and any structural intent

**Do not skim the provided context.** Study it completely. If critical information is missing (brand name, color palette, primary typeface), ask the user before proceeding.

Extract and note these values for use in prompt construction:

- **Brand name**
- **Tagline**
- **Personality** — personality traits summary
- **Archetypes**
- **Values** — core values summary
- **Positioning**
- **Logo concept** — concept vision, if provided
- **Design principles** — logo design principles, if provided
- **Color palette** — all colors with names and hex values
- **Primary color** — the color designated as primary/action
- **Secondary/accent color** — the color designated as secondary or accent
- **Dark color** — the color designated as ink, dark, or midnight
- **Light color** — the color designated as white, surface, or light
- **Primary typeface** — font family name
- **Weights and styles** — available weights

### Step 2: Save User-Provided Logomark (if attached)

If the user attached a logomark image (e.g., a concept chosen from brand-element-logo-designer), save it to:

```
<output-dir>/logo-icon-full-color.png
```

Create the output directory if it does not exist. This image will serve as the canonical logomark, allowing Phase 1 to be skipped.

### Step 3: Generate Logo Images (Phases 1–3)

For each Phase 1–3 image in the Generated Images table, construct a prompt following the Prompt Construction Guidelines section below, write it to a temp file, and call the generation CLI:

```bash
cd .github/skills/brand-element-logo-builder/scripts

# Write the constructed prompt to a temp file, then generate:
python generate.py --prompt-file "<path-to-prompt.txt>" \
  --output "<output-dir>/<filename>"

# Or use inline prompt for shorter prompts:
python generate.py --prompt "<prompt-text>" \
  --output "<output-dir>/<filename>"

# With reference images (Phase 2 and 3):
python generate.py --prompt-file "<prompt.txt>" \
  --output "<output-dir>/<filename>" \
  --ref "<ref1.png>" "<ref2.png>"
```

**Phase 1 — Foundation:** Generate the canonical logomark. No reference images. If a logomark was saved in Step 2, skip this phase.

**Phase 2 — Design Sheet:** Generate the composite design sheet. Pass the Phase 1 logomark as `--ref`.

**Phase 3 — Variations:** Generate all remaining variations. Pass both the Phase 1 logomark and Phase 2 design sheet as `--ref`.

If Phase 1 fails (or is skipped without a logomark present), stop — the foundation logomark is required before anything else can be generated consistently.

### Step 4: Generate Derivative Assets (Phase 4)

Phase 4 produces platform-specific assets by programmatically resizing and composing Phase 1–3 outputs. No AI API calls are needed.

```bash
cd .github/skills/brand-element-logo-builder/scripts

# Favicons and avatar — resize from icon
python derivatives.py resize \
  --input "<output-dir>/logo-icon-full-color.png" \
  --output "<output-dir>/logo-favicon-32.png" \
  --width 32 --height 32 --remove-bg

python derivatives.py resize \
  --input "<output-dir>/logo-icon-full-color.png" \
  --output "<output-dir>/logo-favicon-180.png" \
  --width 180 --height 180 --remove-bg

python derivatives.py resize \
  --input "<output-dir>/logo-icon-full-color.png" \
  --output "<output-dir>/logo-social-avatar.png" \
  --width 400 --height 400 --remove-bg

# App icon — icon on solid brand-color background
python derivatives.py compose \
  --input "<output-dir>/logo-icon-full-color.png" \
  --output "<output-dir>/logo-app-icon.png" \
  --width 1024 --height 1024 \
  --bg-color "<primary-color-hex>" --padding 0.2

# Social banner — horizontal logo on dark background
python derivatives.py compose \
  --input "<output-dir>/logo-primary-horizontal-full-color-light.png" \
  --output "<output-dir>/logo-social-banner.png" \
  --width 1500 --height 500 \
  --bg-color "<dark-color-hex>"

# OG share card — logo + tagline on dark background
python derivatives.py compose \
  --input "<output-dir>/logo-primary-horizontal-full-color-light.png" \
  --output "<output-dir>/logo-og-share.png" \
  --width 1200 --height 630 \
  --bg-color "<dark-color-hex>" \
  --text "<tagline>" --font-name "<primary-typeface>" --font-dir "<font-dir>"

# Email signature — fit horizontal logo into compact dimensions
python derivatives.py fit \
  --input "<output-dir>/logo-primary-horizontal-full-color-light.png" \
  --output "<output-dir>/logo-email-signature.png" \
  --width 300 --height 100 --remove-bg
```

The `compose --text` command requires the brand typeface. It checks the font directory for a matching `.ttf`/`.otf` file first, then attempts to download from Google Fonts. If the user provided a font directory or font file, pass it via `--font-dir`. If neither succeeds, it fails with an error asking the user to provide the font file.

### Step 5: Report Results

List all generated files and their paths. If any failed, report the error and suggest re-running that specific step.

## Generated Images

The workflow produces these files in the output directory:

| Phase | Logo Type | Variant | Dimensions (px) | DPI | Background | Key Notes | Filename |
|---|---|---|---|---|---|---|---|
| 1 | Icon / Mark | Full color (canonical) | 512 x 512 | 300 | Transparent | Primary reference asset; all other variants derive from this | `logo-icon-full-color.png` |
| 2 | Design Sheet | Composite reference | 2400 x 1600 | 150 | White | All variants, palette, typography, spacing; brand reference only | `logo-design-sheet.png` |
| 3 | Primary Logo | Horizontal (full color, light) | 1200 x 400 | 300 | Transparent | Main logo; icon + wordmark side by side; for light backgrounds | `logo-primary-horizontal-full-color-light.png` |
| 3 | Primary Logo | Horizontal (full color, dark) | 1200 x 400 | 300 | Transparent | For dark backgrounds | `logo-primary-horizontal-full-color-dark.png` |
| 3 | Primary Logo | Horizontal (mono) | 1200 x 400 | 300 | Transparent | Single-color use | `logo-primary-horizontal-mono.png` |
| 3 | Stacked Logo | Vertical (full color, light) | 800 x 800 | 300 | Transparent | Icon above wordmark; for light backgrounds | `logo-stacked-vertical-full-color-light.png` |
| 3 | Stacked Logo | Vertical (full color, dark) | 800 x 800 | 300 | Transparent | For dark backgrounds | `logo-stacked-vertical-full-color-dark.png` |
| 3 | Stacked Logo | Vertical (mono) | 800 x 800 | 300 | Transparent | Single-color use | `logo-stacked-vertical-mono.png` |
| 3 | Wordmark Only | Dark text | 1200 x 300 | 300 | Transparent | Text only; no icon; for light backgrounds | `logo-wordmark-dark.png` |
| 3 | Wordmark Only | Light text | 1200 x 300 | 300 | Transparent | For dark backgrounds | `logo-wordmark-light.png` |
| 3 | Icon / Mark | White/reversed | 512 x 512 | 300 | Transparent | For dark backgrounds | `logo-icon-white.png` |
| 3 | Icon / Mark | Mono | 512 x 512 | 300 | Transparent | Single-color use | `logo-icon-mono.png` |
| 4 | Favicon | Standard | 32 x 32 | 72 | Transparent | Browser tab | `logo-favicon-32.png` |
| 4 | Favicon | HD / Apple touch | 180 x 180 | 72 | Transparent | Apple touch icon; covers most HD favicon needs | `logo-favicon-180.png` |
| 4 | Social Avatar | Square | 400 x 400 | 72 | Transparent | LinkedIn, X, GitHub profile images | `logo-social-avatar.png` |
| 4 | Social Cover / Banner | Horizontal | 1500 x 500 | 72 | Transparent or brand color | Twitter/X header; scale for LinkedIn | `logo-social-banner.png` |
| 4 | App Icon | Standard | 1024 x 1024 | 72 | Solid brand color | App stores and OG image use; no transparency | `logo-app-icon.png` |
| 4 | OG / Social Share | Card | 1200 x 630 | 72 | Brand color or scene | URL preview on LinkedIn, Slack, iMessage; logo + tagline | `logo-og-share.png` |
| 4 | Email / Signature | Horizontal | 300 x 100 | 72 | Transparent or white | Optimized for email clients | `logo-email-signature.png` |

## Prompt Construction Guidelines

### Base Context Block

Start every generation prompt with brand context (substitute extracted values from Step 1):

```
Brand: "{brand_name}"
Brand personality: {personality_summary}
Brand archetypes: {archetypes}
Core values: {values_summary}
Color palette: {up to 6 colors as "Name: #hex"}
Primary typeface: {primary_typeface}

This is a professional brand identity asset. The output must look like a polished, production-ready brand asset — not a sketch, mockup, or illustration. Clean geometric forms, precise typography rendering, and corporate-grade quality.
```

### Reference Image Instructions

**Phase 2** (design sheet) — add after the base context:

> The attached image is the CANONICAL LOGOMARK for "{brand_name}". Use this EXACT logomark — do not redesign it. Every logo variation on this sheet must use this same mark.

**Phase 3** (variations with a logomark) — add after the base context:

> The attached images are: (1) the CANONICAL LOGOMARK and (2) the BRAND DESIGN SHEET for "{brand_name}". You MUST use the EXACT same logomark shown in these reference images — do not redesign, reinterpret, or alter the mark in any way. Match its shape, proportions, and style precisely.

**Phase 3** (wordmark-only variations) — use a simpler reference:

> The attached images show the brand design sheet for "{brand_name}". Match the wordmark typography style shown in the design sheet exactly.

### Quality Requirements

Include in every prompt:
- Generous padding around the mark/logo
- Crisp vector-style rendering with sharp edges
- No decorative elements, no background texture, no gradients on the logo itself
- Professional brand asset quality

### Phase 1 — Foundation Prompt

Request the canonical logomark:
- "Generate a professional brand logo image: the CANONICAL LOGOMARK (icon/symbol only, no text)"
- Centered on a clean white background, square aspect ratio
- Primary brand color for the logomark
- Reference the logo concept and design principles from the brand context
- Emphasize this is the MASTER reference — all other variations derive from this exact mark
- "Simple enough to be recognizable at 16px but detailed enough to be interesting at 512px"

### Phase 2 — Design Sheet Prompt

Request a comprehensive brand logo design sheet. The prompt must specify this structured grid layout (landscape orientation, 2400x1600):

**TOP-LEFT:** "THE {BRAND_NAME} MARK & DESIGN PRINCIPLES"
- Large canonical logomark in primary color
- Design principle label
- Clear space diagrams with "1x" padding labels

**TOP-CENTER:** "LOGO VARIATIONS"
- Row of 4 treatments: Primary (horizontal), Stacked (vertical), Logomark Only, Wordmark Only

**MIDDLE-CENTER:** "COLOR APPLICATIONS & MINIMUM SIZES"
- Full color on light, monochrome, full color on dark, accent on dark, white on accent

**TOP-RIGHT:** "COLOR PALETTE & TYPOGRAPHY"
- 4 color swatches with hex values
- Typography sample: "{typeface} 700 (Bold)" with ABCDEFGHIJKLMNOPQRSTUVWXYZ and 1234567890

**RIGHT SIDE:** Minimum sizes table (Digital px and Print mm)

**BOTTOM:** "INCORRECT USAGE"
- 8 "don't" examples with red X marks: stretch, rotate, recolor, add effects, outline, busy backgrounds, rearrange, crop

Style: "Clean, professional, editorial quality. White overall background. Crisp vector-style rendering. Structured grid layout with clear section labels. The kind of sheet a brand designer would present to a client."

### Phase 3 — Variation Prompts

For each variation, construct a prompt specifying layout, colors, and background. All logomark variations must include the reference preamble and: "Use the EXACT logomark from the attached reference — same shape, same proportions, same style."

| Variation | Layout | Logomark Color | Text Color | Background |
|---|---|---|---|---|
| Primary horizontal (light) | Icon left + wordmark right | Primary color | Dark color | White/light |
| Primary horizontal (dark) | Icon left + wordmark right | Primary color | White | Dark color bg |
| Primary horizontal (mono) | Icon left + wordmark right | Dark color | Dark color | White |
| Stacked vertical (light) | Icon above wordmark, centered | Primary color | Dark color | White/light |
| Stacked vertical (dark) | Icon above wordmark, centered | Primary color | White | Dark color bg |
| Stacked vertical (mono) | Icon above wordmark, centered | Dark color | Dark color | White |
| Wordmark dark | Text only, no icon, centered | — | Dark color | White |
| Wordmark light | Text only, no icon, centered | — | White | Dark color bg |
| Icon white | Icon only, no text, centered | White | — | Dark color bg |
| Icon mono | Icon only, no text, centered | Dark color | — | White |

Wordmark typeface style for all text: "{primary_typeface}, Bold weight, geometric sans-serif"

## CLI Reference

### generate.py

Generates a single image using Google AI Studio (Gemini). Reads API key from `.env`.

```
python generate.py --prompt "<text>" --output <path.png> [--ref <img1.png> <img2.png>]
python generate.py --prompt-file <file.txt> --output <path.png> [--ref <img1.png> <img2.png>]
```

| Argument | Required | Description |
|---|---|---|
| `--prompt` | Yes* | Prompt text (mutually exclusive with `--prompt-file`) |
| `--prompt-file` | Yes* | Path to text file containing the prompt |
| `--output` | Yes | Output PNG file path |
| `--ref` | No | One or more reference image paths |

### derivatives.py

Image processing operations for Phase 4 derivative assets.

**resize** — Exact LANCZOS resize:
```
python derivatives.py resize --input <in.png> --output <out.png> --width <W> --height <H> [--remove-bg]
```

**compose** — Place image centered on a solid-color canvas, optionally with text:
```
python derivatives.py compose --input <in.png> --output <out.png> --width <W> --height <H> --bg-color "<#hex>" [--padding <0.15>] [--text "<text>" --font-name "<name>" --font-dir "<path>"]
```

**fit** — Fit image within bounds (maintaining aspect ratio, transparent padding):
```
python derivatives.py fit --input <in.png> --output <out.png> --width <W> --height <H> [--remove-bg]
```

| Argument | Commands | Description |
|---|---|---|
| `--input` | all | Source image path |
| `--output` | all | Output PNG path |
| `--width` | all | Target width in pixels |
| `--height` | all | Target height in pixels |
| `--remove-bg` | resize, fit | Remove dominant background color before processing |
| `--bg-color` | compose | Background hex color (e.g., `#2E5BFF`) |
| `--padding` | compose | Padding as fraction of canvas size (default: 0.15) |
| `--text` | compose | Text to render below the image |
| `--font-name` | compose | Font family name (required with `--text`) |
| `--font-dir` | compose | Directory containing font files for text rendering (required with `--text`) |

## Troubleshooting

- **API key error**: Verify `.env` file exists in this skill folder with a valid `GOOGLE_AI_STUDIO_API_KEY`
- **Model not available**: The script uses `gemini-3.1-flash-image-preview`. Verify model access at https://aistudio.google.com/
- **Rate limiting**: The AI client includes retry logic with exponential backoff. If persistent, wait a few minutes and re-run the failed generation.
- **Inconsistent logomark across variations**: Delete the output directory and re-run from Phase 1. The phased approach generates the canonical logomark first, then uses it as a visual reference for all subsequent images.
- **Low quality output**: Re-run the specific generation. The reference images from Phase 1 and 2 ensure consistency when provided via `--ref`.
- **Using a concept from logo-designer**: Save the chosen concept PNG to `<output-dir>/logo-icon-full-color.png` and skip Phase 1. The saved image will be used as the canonical mark for all subsequent phases.
- **Font not found (Phase 4)**: The `compose --text` command checks the font directory for `.ttf`/`.otf` files, then tries Google Fonts. If neither works, provide the brand typeface file path directly.
