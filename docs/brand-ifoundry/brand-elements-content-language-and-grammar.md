# iFoundry Media Language & Grammar

> Consistent writing conventions that signal precision and professionalism — the way great engineering signals quality.

## Strategic Foundation

**Brand Alignment:** iFoundry's language conventions reflect the Craftsmanship value. Consistent, precise writing signals the same attention to detail we bring to architecture and code. Like well-structured software, our language follows clear rules so the reader never has to parse ambiguity. These conventions reduce cognitive load and build trust through predictable, professional communication.

## Capitalization

### Sentence Case (Default)
Use sentence case for all UI text unless specified otherwise. Sentence case is more readable and more aligned with our direct, human voice.

| Element | Style | Example |
|---------|-------|---------|
| Page titles | Sentence case | "Project overview" |
| Section headings | Sentence case | "Current sprint" |
| Button labels | Sentence case | "Deploy build" |
| Menu items | Sentence case | "View architecture" |
| Tab labels | Sentence case | "Active projects" |
| Form labels | Sentence case | "Repository URL" |
| Column headers | Sentence case | "Last deployment" |
| Placeholder text | Sentence case | "Search projects..." |

### Title Case Exceptions
Use title case only for:
- The company name: "iFoundry Media" (note: lowercase "i")
- Product names when they're named offerings (e.g., "Forge Platform")
- Proper nouns: "React," "Node.js," "AWS," "Kubernetes"

### Uppercase Exceptions
Use uppercase only for:
- Abbreviations and acronyms (e.g., "API," "CI/CD," "SaaS," "CTO")
- Section labels in navigation (e.g., "PORTFOLIO" / "SERVICES")

### The "iFoundry" Name
The brand name always uses a lowercase "i" followed by an uppercase "F": **iFoundry**. Never capitalize the "i" — even at the start of a sentence. Restructure sentences to avoid starting with "iFoundry" when possible, but if unavoidable, maintain the lowercase "i."

```
✓ "At iFoundry, we build products that scale."
✓ "iFoundry Media partners with ambitious founders."
✗ "IFoundry Media partners with ambitious founders."
✗ "Ifoundry media partners with ambitious founders."
```

## Punctuation

### Oxford Comma
Always use the Oxford comma in lists of three or more items.

```
✓ Strategy, architecture, and engineering
✗ Strategy, architecture and engineering
```

### Periods
- **Use periods** in complete sentences, descriptions, help text, and body content
- **Omit periods** in headings, button labels, navigation items, placeholder text, and single-phrase descriptions

### Colons
Use colons to introduce related information. Capitalize the first word after a colon only if it starts a complete sentence.

```
✓ Tech stack: React, Node.js, PostgreSQL
✓ Result: The application handled 10x the expected load.
```

### Dashes
- **Em dash (—):** For emphasis or parenthetical breaks. No spaces on either side.
  ```
  "From concept to launch to scale — one team, one vision."
  ```
- **En dash (–):** For ranges (dates, times, numbers).
  ```
  "2–4 week sprints" / "Series A–C startups" / "3–5 engineers"
  ```

### Exclamation Points
Use sparingly — maximum one per page. Reserve for genuine enthusiasm about a launch or milestone, never for marketing emphasis.

```
✓ "Your product just shipped!"
✗ "We build amazing products!"
✗ "Error! Deployment failed!"
```

### Quotation Marks
Use double quotes for direct quotations. Use single quotes for quotes within quotes. Place commas and periods inside quotes.

## Abbreviations & Acronyms

### Common Abbreviations

| Abbreviation | Full Form | When to Use |
|-------------|-----------|-------------|
| API | Application programming interface | OK to use directly — audience knows it |
| CI/CD | Continuous integration / continuous deployment | OK to use directly |
| CTO | Chief technology officer | OK to use directly |
| MVP | Minimum viable product | OK to use directly |
| SaaS | Software as a service | OK to use directly |
| AI | Artificial intelligence | OK to use directly |
| UI/UX | User interface / user experience | OK to use directly |
| PR | Pull request | Developer contexts only |
| K8s | Kubernetes | Developer contexts only |

### Rules
- Our audience is technical — common tech abbreviations don't need expansion
- Spell out non-technical abbreviations on first use within a page
- Never abbreviate in a way that creates ambiguity
- Use the full name for business concepts that aren't universally abbreviated

## Numbers

### Formatting Rules

| Context | Rule | Example |
|---------|------|---------|
| One through nine | Spell out | "three sprints" |
| 10 and above | Use numerals | "12 engineers" |
| Starting a sentence | Always spell out | "Forty-seven percent of startups..." |
| Mixed in same context | Use numerals for all | "3 designers and 12 engineers" |
| Percentages | Numeral + symbol | "40% faster deployment" |
| Currency | Symbol + numeral | "$2.5M ARR" |
| Large numbers | Comma-separated or abbreviated | "1,250 requests/sec" or "2.5M users" |
| Technical metrics | Always numerals | "99.9% uptime," "sub-200ms latency" |
| Version numbers | Numerals with dots | "v2.1.0" |
| Multipliers | Numeral + "x" | "10x throughput" |

### Ordinals
Use numerals with ordinals in most contexts: "1st sprint," "3rd iteration." Spell out in formal or narrative content: "the first product we shipped together."

## Contractions

Contractions are encouraged — they keep the voice human and direct, consistent with The Builder's approachable confidence.

| Use | Instead of |
|-----|-----------|
| "We'll build it" | "We will build it" |
| "That's the architecture" | "That is the architecture" |
| "We don't ship until it's right" | "We do not ship until it is right" |
| "Here's your deployment status" | "Here is your deployment status" |

### When to Avoid Contractions
- Legal content, terms of service, privacy policies
- When emphasis requires the full form: "This decision *will not* be reversed after deployment"
- Content intended for translation

## Lists

### Bullet Lists
- Use for items with no specific order
- Keep items parallel in structure
- If items are fragments, omit end punctuation
- If items are complete sentences, use end punctuation on all of them

### Numbered Lists
Use when order matters — process steps, prioritized items, phased plans.

### List Capitalization
Capitalize the first word of each list item.

## Parallel Structure

Keep related items grammatically consistent.

```
✓ "We architect, build, and scale digital products."
✗ "We do architecture, building, and then we scale digital products."

✓ Services: Product Strategy, Engineering, AI Integration
✗ Services: Product Strategy, We Engineer, AI Integration Services
```

## Active Voice

Prefer active voice — it's direct, confident, and aligned with The Builder's action orientation.

```
✓ "We deployed the production build at midnight."
✗ "The production build was deployed at midnight."

✓ "Our engineers resolved the scaling bottleneck in 48 hours."
✗ "The scaling bottleneck was resolved within 48 hours."
```

Use passive voice only when the actor is irrelevant or unknown:
```
✓ "The application was stress-tested to 50,000 concurrent users." (Focus on the test, not who ran it)
```

## Technical Writing

### Code and Technical Terms
- Use backticks (`` ` ``) for inline code, file paths, and command names in documentation
- Use proper casing for technology names: "React," "Node.js," "PostgreSQL," "Kubernetes"
- Don't capitalize generic technical terms: "microservices," "serverless," "containerization"

### Version References
- Use semantic versioning format: "v2.1.0"
- Spell out when used in marketing: "version 2"

## Localization Considerations

For content that may be translated:
- Avoid idioms, slang, or culturally specific references
- Don't hardcode date/time formats (see Date & Time guidelines)
- Avoid contractions in localizable content
- Keep UI strings short — translated text can be 30–50% longer
- Use complete sentences rather than fragments that depend on word order

## Usage Guidelines

### Do
- Apply these conventions consistently across all content
- Use sentence case as the default for all UI text
- Write in active voice with specific, concrete language
- Keep the lowercase "i" in iFoundry consistent everywhere
- Treat technical terms with the respect they deserve — proper casing, no scare quotes

### Don't
- Capitalize words for emphasis (use bold or structure)
- Use abbreviations the audience wouldn't know
- Mix capitalization styles within the same screen
- Use jargon from agency/consulting culture ("deliverables," "stakeholder alignment")
- Start sentences with "iFoundry" at the expense of correct brand casing
