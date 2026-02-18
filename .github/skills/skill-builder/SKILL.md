---
name: skill-builder
description: 'Create new Agent Skills from prompts or by duplicating this template. Use when asked to "create a skill", "make a new skill", "scaffold a skill", or when building specialized AI capabilities with bundled resources. Generates SKILL.md files with proper frontmatter, directory structure, and optional scripts/references/assets folders.'
---

# Skill Builder

A meta-skill for creating effective Agent Skills. Skills are modular, self-contained packages that extend an AI agent's capabilities by providing specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific domains—they transform a general-purpose agent into a specialized one equipped with procedural knowledge.

## Core Principles

### Concise is Key

The context window is a shared resource. Skills share it with the system prompt, conversation history, other skills' metadata, and user requests.

**Default assumption: The AI is already very smart.** Only add context it doesn't already have. Challenge each piece of information: "Does the AI really need this?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match specificity to the task's fragility and variability:

- **High freedom (text-based instructions)**: Multiple approaches valid, decisions depend on context
- **Medium freedom (pseudocode or parameterized scripts)**: Preferred pattern exists, some variation acceptable
- **Low freedom (specific scripts, few parameters)**: Operations are fragile, consistency critical

Think of exploration: a narrow bridge needs guardrails (low freedom), while an open field allows many routes (high freedom).

## Anatomy of a Skill

Every skill consists of a required SKILL.md file and optional bundled resources:

```
skill-name/
├── SKILL.md              # Required
└── Bundled Resources     # Optional
    ├── scripts/          # Executable code
    ├── references/       # Documentation loaded into context as needed
    └── assets/           # Files used in output (templates, icons, fonts)
```

### SKILL.md (Required)

- **Frontmatter** (YAML): `name` and `description` fields. These determine when the skill triggers—be clear and comprehensive.
- **Body** (Markdown): Instructions loaded AFTER the skill triggers.

### Bundled Resources (Optional)

| Folder | Purpose | When to Include |
|--------|---------|-----------------|
| `scripts/` | Executable code (Python, Bash, JS) | Same code rewritten repeatedly; deterministic reliability needed |
| `references/` | Documentation the agent reads | Schemas, API docs, domain knowledge, policies |
| `assets/` | Files used AS-IS in output | Templates, images, icons, fonts, boilerplate |

**Key principle for references:** Keep SKILL.md lean. Move detailed reference material to separate files. Information should live in either SKILL.md OR references—not both.

## Progressive Disclosure

Skills use a three-level loading system:

1. **Metadata (name + description)** — Always in context (~100 words)
2. **SKILL.md body** — When skill triggers (<5k words target)
3. **Bundled resources** — As needed (unlimited)

Keep SKILL.md under 500 lines. When splitting content into other files, clearly reference them from SKILL.md with guidance on when to read them.

### Splitting Patterns

**Pattern 1: High-level guide with references**

```markdown
## Quick start
[Core workflow]

## Advanced features
- **Form filling**: See [FORMS.md](references/FORMS.md)
- **API reference**: See [REFERENCE.md](references/REFERENCE.md)
```

**Pattern 2: Domain-specific organization**

```
bigquery-skill/
├── SKILL.md (overview + navigation)
└── references/
    ├── finance.md
    ├── sales.md
    └── product.md
```

When user asks about sales, only sales.md gets loaded.

**Pattern 3: Framework variants**

```
cloud-deploy/
├── SKILL.md (workflow + selection guidance)
└── references/
    ├── aws.md
    ├── gcp.md
    └── azure.md
```

## Skill Creation Process

### Step 1: Understand with Concrete Examples

Clarify how the skill will be used:
- "What functionality should this skill support?"
- "Give examples of how it would be used."
- "What would a user say that should trigger this skill?"

### Step 2: Plan Reusable Contents

For each example, identify:
1. What code/process would be repeated?
2. What scripts, references, or assets would help?

**Examples:**
- PDF rotation → `scripts/rotate_pdf.py`
- Frontend webapp → `assets/hello-world/` template
- BigQuery queries → `references/schema.md`

### Step 3: Create the Skill Directory

```
skills/<skill-name>/
└── SKILL.md
```

Folder name: lowercase with hyphens, must match the `name` field.

### Step 4: Write SKILL.md

#### Frontmatter

```yaml
---
name: <skill-name>
description: '<WHAT it does>. Use when <triggers, scenarios, keywords>.'
---
```

| Field | Required | Constraints |
|-------|----------|-------------|
| `name` | **Yes** | 1-64 chars, lowercase letters/numbers/hyphens, matches folder |
| `description` | **Yes** | 1-1024 chars, describes WHAT and WHEN |
| `license` | No | License name or reference to LICENSE.txt |

**Description is the PRIMARY trigger mechanism.** Include:
1. **WHAT** the skill does (capabilities)
2. **WHEN** to use it (triggers, scenarios)
3. **Keywords** users might mention

**Good:**
```yaml
description: 'Toolkit for testing web apps with Playwright. Use when asked to verify frontend functionality, debug UI behavior, capture screenshots, or view console logs. Supports Chrome, Firefox, WebKit.'
```

**Poor:**
```yaml
description: 'Web testing helpers'
```

#### Body

Use imperative form. Recommended sections:

| Section | Purpose |
|---------|---------|
| `# Title` | Brief overview |
| `## Prerequisites` | Required tools, dependencies |
| `## Workflows` | Numbered steps for tasks |
| `## Troubleshooting` | Common issues and solutions |

**Do NOT include in skills:** README.md, CHANGELOG.md, INSTALLATION_GUIDE.md, or other auxiliary documentation. Skills contain only what the AI needs to do the job.

### Step 5: Add Bundled Resources

Implement scripts, references, and assets identified in Step 2. Delete any example directories not needed.

For references: If files are large (>10k words), include grep search patterns in SKILL.md to help the agent find relevant sections.

### Step 6: Iterate

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Update SKILL.md or bundled resources
4. Test again

## Design Patterns

For skills with multi-step processes or specific output requirements, consult these guides:

- **Multi-step processes**: See [references/workflows.md](references/workflows.md) for sequential and conditional workflow patterns
- **Output formats or quality standards**: See [references/output-patterns.md](references/output-patterns.md) for template and example patterns

## Validation Checklist

- [ ] Folder name is lowercase with hyphens
- [ ] `name` field matches folder name exactly
- [ ] `description` is 10-1024 characters
- [ ] `description` explains WHAT and WHEN
- [ ] Body content under 500 lines
- [ ] Bundled assets under 5MB each
- [ ] No duplicate info between SKILL.md and references

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Skill not discovered | Add more keywords and triggers to description |
| Validation fails on name | Lowercase, no consecutive hyphens, match folder |
| Description too short | Add capabilities, triggers, keywords |
| Assets not found | Use relative paths from skill root |

## References

- https://docs.github.com/copilot/concepts/agents/about-agent-skills
- https://code.visualstudio.com/docs/copilot/customization/agent-skills