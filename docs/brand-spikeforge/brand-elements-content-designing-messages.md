# SpikeForge Designing Messages

> Craft clear, purposeful messages that help coaches act with confidence.

## Strategic Foundation

**Brand Alignment:** Messages are moments of micro-interaction between the platform and the coach. Every notification, confirmation, error, and prompt reflects the brand's voice — calm, confident, empowering. Messages should feel like a capable colleague sharing information, never like a system issuing commands. Aligned with the "Clarity Over Cleverness" and "Respect Time" content principles.

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
| Title | Yes | Concise summary of the message |
| Body | Conditional | Additional context when the title alone is insufficient |
| Actions | Conditional | One or two actionable buttons when a response is needed |
| Dismiss | When applicable | Close button for non-blocking messages |

### Title Guidelines
- Lead with what happened, not with a label
- Keep to one line (under 60 characters)
- Use sentence case
- Do not end with a period if it's a single sentence fragment

### Body Guidelines
- Provide enough context to act — no more, no less
- One to two sentences maximum
- Include a next step when the user needs to do something
- Never repeat information already in the title

## Message Types

### Informational

**Purpose:** Neutral updates and status changes. No action required.

**Tone:** Calm, factual.

**Icon:** `info` (Lucide) in Clarity Sky (`#0284C7`)

| Element | Content |
|---------|---------|
| Title | Describe what happened or what changed |
| Body | Provide supporting detail only if needed |
| Action | Optional — link to view details |

**Examples:**

| Context | Title | Body |
|---------|-------|------|
| Session rescheduled | Session with Alex moved to Thursday | January 23 at 2:00 PM EST |
| Client update | New intake form submitted | Alex Rivera completed their onboarding questionnaire |
| System | Your data export is ready | Download will be available for 7 days |

### Success

**Purpose:** Confirm a completed action. Reinforce positive progress.

**Tone:** Warm, affirming. Brief celebration without excess.

**Icon:** `check-circle` (Lucide) in Growth Emerald (`#059669`)

| Element | Content |
|---------|---------|
| Title | Confirm what was accomplished |
| Body | Include next steps or a brief reinforcement |
| Action | Optional — "View" or link to the result |

**Examples:**

| Context | Title | Body |
|---------|-------|------|
| Invoice sent | Invoice sent to Alex Rivera | $250.00 for January coaching — they'll receive it shortly |
| Session logged | Session notes saved | 45-minute session with Alex on January 15 |
| Client added | Alex Rivera added to your practice | You can now schedule their first session |

### Warning

**Purpose:** Something needs attention but isn't critical. Prevent problems before they escalate.

**Tone:** Helpful, not alarming. A gentle nudge.

**Icon:** `alert-triangle` (Lucide) in Momentum Amber (`#D97706`)

| Element | Content |
|---------|---------|
| Title | State what needs attention |
| Body | Explain why it matters and what to do |
| Action | Action button when there's a clear next step |

**Examples:**

| Context | Title | Body | Action |
|---------|-------|------|--------|
| Engagement | No session with Alex in 3 weeks | Their last session was December 28. Consider reaching out. | Schedule session |
| Billing | Alex's payment method is expiring | Their card on file expires in February. Reaching out now avoids a missed payment. | View details |
| Capacity | You have 2 sessions scheduled in the same hour | Thursday at 2:00 PM has overlapping sessions. | Review schedule |

### Error

**Purpose:** Something went wrong. Help the user recover.

**Tone:** Direct and honest, never blaming. Focus on the fix, not the failure.

**Icon:** `x-circle` (Lucide) in Error Red (`#DC2626`)

| Element | Content |
|---------|---------|
| Title | State what went wrong — plainly |
| Body | Explain what to do next |
| Action | Recovery action when possible |

**Examples:**

| Context | Title | Body | Action |
|---------|-------|------|--------|
| Payment failed | Payment of $250.00 couldn't be processed | Alex Rivera's card was declined. You can update their payment method or reach out to them. | Update payment |
| Save failed | Your changes couldn't be saved | Check your connection and try again. If this continues, your work has been saved locally. | Try again |
| Access | You don't have access to this page | This section is available to practice leads. Contact your admin if you need access. | — |

### Writing Error Messages
1. Never blame the user — say "couldn't be saved" not "you failed to save"
2. Never use technical jargon — say "check your connection" not "network timeout (504)"
3. Always provide a next step — even if it's "try again"
4. Be specific about what failed — not just "something went wrong"

### Feature Discovery

**Purpose:** Introduce new capabilities or surface underused features. Help coaches get more value from the platform.

**Tone:** Enthusiastic but measured. Helpful, not pushy.

**Icon:** `sparkles` (Lucide) in Insight Indigo (`#6366F1`)

| Element | Content |
|---------|---------|
| Title | Describe the benefit, not the feature |
| Body | Brief explanation with a clear value proposition |
| Action | "Try it" or "Learn more" — always dismissible |

**Examples:**

| Context | Title | Body | Action |
|---------|-------|------|--------|
| New feature | Track session outcomes over time | See how your clients are progressing with the new outcome trends view. | Try it |
| Underused | Save time with session templates | Create reusable templates for your session notes — set them up once, use them every time. | Set up templates |
| Tip | You can schedule recurring sessions | Instead of booking one at a time, create a recurring series with Alex. | Learn more |

## Placement

### Toast Notifications
- Position: Top-right corner, stacked
- Duration: 5 seconds for informational/success, persistent for warnings/errors
- Max visible: 3 stacked toasts
- Behavior: Auto-dismiss for non-critical; require manual dismiss for errors

### Inline Messages
- Position: Near the relevant content — above a form, within a card, below an input
- Use for: Contextual information, field-level validation, section-specific status
- Persistence: Remain until the condition changes or the user addresses it

### Banner Messages
- Position: Top of the page, below the top bar
- Use for: System-wide announcements, maintenance notices, account-level warnings
- Full-width, dismissible (unless critical)

### Empty State Messages
- Position: Center of the empty content area
- Use for: First-use education, zero-data states, search with no results
- Include: Friendly illustration, clear title, brief explanation, primary action

## Message Flow

### Optimistic Actions
For actions likely to succeed (saving notes, updating a setting):
1. Show immediate success feedback
2. Revert with an error message only if the action fails
3. Keep the user in flow

### Destructive Actions
For irreversible actions (deleting a client, canceling a session):
1. Require confirmation before acting
2. State the consequence clearly in the confirmation dialog
3. Show success confirmation after completion

### Multi-Step Processes
For actions with multiple stages (sending invoices, importing clients):
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
- Title: State the action as a question — "Cancel this session?"
- Body: Describe the specific consequence — "Alex Rivera will be notified and this session will be removed from both calendars."
- Confirm button: Use a specific verb matching the action — "Cancel session" not "OK" or "Yes"
- Cancel button: Always labeled "Cancel" or "Keep [thing]"
- Destructive confirms: Use error red for the confirm button

### Examples

| Action | Title | Body | Confirm |
|--------|-------|------|---------|
| Delete client | Remove Alex Rivera? | All session history and notes for this client will be permanently deleted. This cannot be undone. | Remove client |
| Cancel session | Cancel this session? | Alex Rivera will be notified and the January 22 session will be removed from both calendars. | Cancel session |
| Discard changes | Discard unsaved changes? | Your changes to session notes haven't been saved. | Discard |

## Usage Guidelines

### Do
- Lead with what happened, then explain why it matters
- Give users a clear next step whenever possible
- Keep messages scannable — title should be enough for quick reads
- Use the coach's and client's names to personalize messages
- Match the tone to the severity — calm for info, warm for success, direct for errors

### Don't
- Use technical language, error codes, or system-level terminology
- Stack multiple messages about the same event
- Use "Oops" or cutesy language for errors — the user's time is valuable
- Show generic "Something went wrong" without context or a next step
- Use exclamation marks in error or warning messages
- Auto-dismiss error messages — they need to persist until addressed
