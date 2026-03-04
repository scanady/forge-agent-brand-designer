# iFoundry Media Designing Messages

> Craft clear, purposeful messages that keep builders moving and products shipping.

## Strategic Foundation

**Brand Alignment:** Messages are moments where iFoundry's voice meets the user's workflow. Every notification, confirmation, error, and prompt should feel like a trusted engineer giving you a status update — direct, specific, and focused on the next action. Aligned with the "Action Over Abstraction" and "Confidence Through Specificity" content principles. No filler, no blame, always a path forward.

## Message Anatomy

Every message follows a consistent structure:

```
┌─────────────────────────────────────────┐
│  [Icon]  Title                     [×]  │
│                                         │
│  Body text with context and next        │
│  steps when needed.                     │
│                                         │
│              [Secondary]  [Primary]     │
└─────────────────────────────────────────┘
```

| Element | Required | Purpose |
|---------|----------|---------|
| Icon | Yes | Visual category indicator (type-specific) |
| Title | Yes | Concise summary — what happened |
| Body | Conditional | Additional context when the title alone isn't enough |
| Actions | Conditional | One or two actionable buttons when a response is needed |
| Dismiss | When applicable | Close button for non-blocking messages |

### Title Guidelines
- Lead with what happened, not with a label
- Keep to one line (under 60 characters)
- Use sentence case
- Omit trailing periods on single-phrase titles

### Body Guidelines
- Provide enough context to act — no more, no less
- One to two sentences maximum
- Include a next step when the user needs to do something
- Never repeat the title

## Message Types

### Informational

**Purpose:** Neutral updates and status changes. No action required.

**Tone:** Calm, factual, specific.

**Icon:** `info` (Lucide) in Architect Blue (`#3B82F6`)

| Element | Content |
|---------|---------|
| Title | Describe what happened or what changed |
| Body | Provide supporting detail only if needed |
| Action | Optional — link to view details |

**Examples:**

| Context | Title | Body |
|---------|-------|------|
| Deployment | Build deployed to staging | v2.4.1 is running on staging — ready for review |
| Sprint | Sprint 12 starts Monday | Planning session at 9:00 AM EST with the full team |
| System | Your data export is ready | Download will be available for 7 days |

### Success

**Purpose:** Confirm a completed action. Reinforce progress and momentum.

**Tone:** Affirming, brief. Celebrate the ship, not the process.

**Icon:** `check-circle` (Lucide) in Launch Green (`#059669`)

| Element | Content |
|---------|---------|
| Title | Confirm what was accomplished |
| Body | Include relevant details or next steps |
| Action | Optional — "View" or link to the result |

**Examples:**

| Context | Title | Body |
|---------|-------|------|
| Deployment | Production deploy complete | v2.4.1 is live — zero downtime, all health checks passing |
| Project | Architecture review approved | The team can proceed to Sprint 1 |
| Integration | API integration test passed | All 47 endpoints returning expected responses |

### Warning

**Purpose:** Something needs attention before it becomes a problem.

**Tone:** Direct, helpful, not alarming. A signal, not a siren.

**Icon:** `alert-triangle` (Lucide) in Ignite Orange (`#EA580C`)

| Element | Content |
|---------|---------|
| Title | State what needs attention |
| Body | Explain why it matters and what to do |
| Action | Action button when there's a clear next step |

**Examples:**

| Context | Title | Body | Action |
|---------|-------|------|--------|
| Infrastructure | CPU usage at 85% on production | Sustained load over the past 2 hours. Consider scaling before the traffic peak. | Scale instances |
| Security | SSL certificate expires in 14 days | Auto-renewal is configured, but verify DNS records are current. | View certificate |
| Sprint | Sprint scope increased by 30% | 4 new tickets added mid-sprint. This may affect the delivery date. | Review scope |

### Error

**Purpose:** Something went wrong. Help the user recover.

**Tone:** Direct and honest, never blaming. Focus on the fix.

**Icon:** `x-circle` (Lucide) in Alert Red (`#DC2626`)

| Element | Content |
|---------|---------|
| Title | State what went wrong — plainly |
| Body | Explain what to do next |
| Action | Recovery action when possible |

**Examples:**

| Context | Title | Body | Action |
|---------|-------|------|--------|
| Build | Build failed — test suite error | 3 tests failed in the auth module. Check the test output for details. | View logs |
| Deploy | Deployment rolled back | Health check failures triggered automatic rollback. Previous version restored. | View incident |
| Integration | API connection lost | The payment gateway isn't responding. We'll retry automatically — no action needed yet. | — |

### Writing Error Messages
1. Never blame the user — say "couldn't be deployed" not "you broke the build"
2. Never use raw error codes — say "database connection timed out" not "ETIMEDOUT 5432"
3. Always provide a next step — even if it's "we're investigating"
4. Be specific about what failed — not just "something went wrong"

### Feature Discovery

**Purpose:** Introduce new capabilities or surface underused features.

**Tone:** Enthusiastic but grounded. Show the value, don't oversell.

**Icon:** `sparkles` (Lucide) in Forge Blue (`#1D4ED8`)

| Element | Content |
|---------|---------|
| Title | Describe the benefit, not the feature name |
| Body | Brief explanation with a clear value proposition |
| Action | "Try it" or "Learn more" — always dismissible |

**Examples:**

| Context | Title | Body | Action |
|---------|-------|------|--------|
| New feature | Deploy previews for every PR | See your changes live before merging — preview environments spin up automatically. | Enable previews |
| Optimization | Your build time dropped 40% | The new caching layer is active. Builds that took 8 minutes now finish in under 5. | View metrics |
| Tip | Set up deployment webhooks | Get notified in Slack or Teams when builds complete. Takes 2 minutes. | Set up |

## Placement

### Toast Notifications
- Position: Top-right corner, stacked
- Duration: 5 seconds for informational/success, persistent for warnings/errors
- Max visible: 3 stacked toasts
- Behavior: Auto-dismiss for non-critical; require manual dismiss for errors

### Inline Messages
- Position: Near the relevant content — above a form, within a card, below an input
- Use for: Contextual information, field-level validation, deployment status
- Persistence: Remain until the condition changes

### Banner Messages
- Position: Top of the page, below the top bar
- Use for: System-wide announcements, maintenance windows, account-level warnings
- Full-width, dismissible (unless critical)

### Empty State Messages
- Position: Center of the empty content area
- Use for: First-use education, zero-data states, no results
- Include: Clear title, brief explanation, primary action

## Message Flow

### Optimistic Actions
For actions likely to succeed (saving configurations, updating settings):
1. Show immediate success feedback
2. Revert with an error message only if the action fails
3. Keep the user in flow

### Destructive Actions
For irreversible actions (deleting a project, terminating an environment):
1. Require confirmation before acting
2. State the consequence clearly in the confirmation dialog
3. Show success confirmation after completion

### Multi-Step Processes
For actions with multiple stages (deploying, running migrations):
1. Show progress indicators during processing
2. Provide a success summary when complete
3. Surface any partial failures clearly

## Confirmation Dialogs

### Structure

```
┌─────────────────────────────────────────┐
│  [Icon]  Title                          │
│                                         │
│  Consequence description. What will     │
│  happen if they proceed.                │
│                                         │
│              [Cancel]  [Confirm verb]   │
└─────────────────────────────────────────┘
```

### Rules
- Title: State the action as a question — "Delete this environment?"
- Body: Describe the specific consequence — "All data, deployments, and logs for the staging environment will be permanently removed."
- Confirm button: Use a specific verb matching the action — "Delete environment" not "OK" or "Yes"
- Cancel button: Always labeled "Cancel" or "Keep [thing]"
- Destructive confirms: Use Alert Red for the confirm button

### Examples

| Action | Title | Body | Confirm |
|--------|-------|------|---------|
| Delete project | Delete this project? | All code, deployments, and history for this project will be permanently removed. This cannot be undone. | Delete project |
| Cancel deployment | Cancel this deployment? | The v2.4.1 build to production will be stopped. The current version will continue running. | Cancel deployment |
| Remove team member | Remove this engineer? | They will lose access to all project repositories and environments immediately. | Remove engineer |

## Usage Guidelines

### Do
- Lead with what happened, then explain what to do
- Give users a clear next step whenever possible
- Keep messages scannable — the title should be enough for quick reads
- Use technical specifics when the audience is technical (version numbers, service names)
- Match the tone to the severity — calm for info, direct for errors

### Don't
- Use technical jargon that doesn't help the user act (error codes, stack traces in UI)
- Stack multiple messages about the same event
- Use "Oops" or "Uh oh" — the user's time is valuable
- Show generic "Something went wrong" without context or a next step
- Use exclamation marks in error or warning messages
- Auto-dismiss error messages — they need to persist until addressed
