# OpenLife Designing Messages

> Write and format UI messages that inform, guide, and support users.

## Strategic Foundation

**Brand Alignment:** OpenLife messages embody our voice: confident, clear, helpful, and empowering. Every message is an opportunity to build trust. We treat errors as moments to help, not blame. We celebrate successes genuinely without excess. We warn users clearly without alarming them unnecessarily. Our messages respect users' time and intelligence.

## Message Types Overview

| Type | Purpose | Icon | Color |
|------|---------|------|-------|
| Information | Provide context and guidance | ℹ️ Info circle | Blue |
| Success | Confirm completed actions | ✓ Check circle | Green |
| Warning | Alert to potential issues | ⚠️ Triangle | Amber/Yellow |
| Error | Communicate problems | ✕ X circle | Red |
| Feature Discovery | Introduce new capabilities | ✨ Sparkle | Purple/Blue |

## Message Anatomy

### Standard Structure

```
┌─────────────────────────────────────────┐
│ [Icon] [Title]                     [×]  │
│                                         │
│ [Body text explaining the situation     │
│  and what the user can or should do]    │
│                                         │
│               [Secondary] [Primary]     │
└─────────────────────────────────────────┘
```

### Components

| Component | Required | Description |
|-----------|----------|-------------|
| Icon | Yes | Visual indicator of message type |
| Title | Recommended | Brief summary (2-5 words) |
| Body | Yes | Explanation and guidance |
| Actions | Situational | Buttons for user response |
| Dismiss | Situational | X button or auto-dismiss |

## Information Messages

**Purpose:** Provide additional context to help users understand or motivate action.

### Tone
- Helpful and supportive
- Neutral, not urgent
- Clear and concise

### Structure
- **Title:** States what the message is about
- **Body:** Provides helpful context
- **Action:** Optional—link to learn more

### Examples

**Onboarding Tip:**
> **ℹ️ Customize your dashboard**
> 
> Drag and drop widgets to arrange your dashboard. Your layout saves automatically.
>
> [Learn more]

**Contextual Help:**
> **ℹ️ API rate limits**
> 
> Your current plan allows 1,000 API requests per minute. Upgrade for higher limits.
>
> [View plans] [Dismiss]

**Status Update:**
> **ℹ️ Scheduled maintenance**
> 
> We'll perform system updates on Dec 28 from 2–4 AM EST. You may experience brief interruptions.

### Do
- Keep information relevant to current context
- Make it easy to dismiss
- Provide a path to more details

### Don't
- Overuse—reserve for genuinely helpful info
- Make users feel they must act immediately
- Bury critical information in info messages

## Success Messages

**Purpose:** Confirm that an action completed successfully and celebrate with users.

### Tone
- Positive but not excessive
- Brief and confident
- Clear about what happened

### Structure
- **Title:** Confirms the action
- **Body:** Optional—next steps or summary
- **Action:** Optional—view result, undo, continue

### Examples

**Simple Confirmation:**
> **✓ Policy saved**

**With Next Steps:**
> **✓ Environment created**
> 
> Your development environment is ready. Start building or configure integrations.
>
> [Go to dashboard] [Configure]

**With Summary:**
> **✓ Deployment complete**
> 
> Version 2.4.1 is now live in production. 3 services updated, 0 errors.
>
> [View logs]

### Timing
- Show immediately after action completes
- Auto-dismiss after 4-6 seconds for minor actions
- Persist for major actions until manually dismissed

### Do
- Be specific about what succeeded
- Offer logical next steps
- Keep it brief

### Don't
- Over-celebrate routine actions
- Use excessive punctuation (!!!)
- Leave users wondering what's next

## Warning Messages

**Purpose:** Alert users to potential issues before they result in errors or data loss.

### Tone
- Clear and direct
- Helpful, not alarming
- Action-oriented

### Structure
- **Title:** States the warning clearly
- **Body:** Explains the risk and recommended action
- **Action:** Clear path to resolve or proceed

### Examples

**Before Destructive Action:**
> **⚠️ Permanent deletion**
> 
> Deleting this environment will remove all policies, configurations, and history. This cannot be undone.
>
> [Cancel] [Delete environment]

**Potential Issue:**
> **⚠️ Unsaved changes**
> 
> You have unsaved changes that will be lost if you leave this page.
>
> [Stay on page] [Leave anyway]

**Approaching Limit:**
> **⚠️ Storage almost full**
> 
> You're using 95% of your storage quota. Consider archiving old data or upgrading your plan.
>
> [Manage storage] [Dismiss]

### When to Warn
- Before irreversible actions
- When approaching limits or quotas
- When an action may have unintended consequences
- When leaving data unsaved

### Do
- Explain the consequence clearly
- Provide a way to avoid the issue
- Make the safe option the default

### Don't
- Warn too frequently (warning fatigue)
- Use vague language ("Are you sure?")
- Make warnings difficult to dismiss

## Error Messages

**Purpose:** Inform users that something went wrong and guide them toward resolution.

### Tone
- Empathetic, never blaming
- Clear about what happened
- Helpful with solutions

### Structure
- **Title:** Describes the problem
- **Body:** Explains what went wrong (briefly) and how to fix it
- **Action:** Steps to resolve or get help

### Examples

**User-Fixable Error:**
> **✕ Invalid email format**
> 
> Enter a valid email address (example: name@company.com).

**Connection Error:**
> **✕ Connection failed**
> 
> Unable to reach the server. Check your internet connection and try again.
>
> [Retry] [Get help]

**System Error:**
> **✕ Something went wrong**
> 
> We couldn't complete your request. Our team has been notified. Please try again in a few minutes.
>
> [Try again] [Contact support]
> 
> Error reference: ERR-5012

### Error Message Framework

1. **State the problem** (what failed)
2. **Explain briefly** (why, if useful)
3. **Guide to solution** (what to do)
4. **Offer escape route** (help, support, try again)

### Do
- Take responsibility ("We couldn't..." not "You failed to...")
- Be specific about what went wrong
- Provide actionable next steps
- Include error codes for support

### Don't
- Use technical jargon without explanation
- Blame the user
- Leave users without options
- Show raw error messages or stack traces

## Feature Discovery Messages

**Purpose:** Introduce users to new or underused features that could help them.

### Tone
- Enthusiastic but not pushy
- Clear about the benefit
- Easy to dismiss

### Structure
- **Title:** Names the feature
- **Body:** Explains the benefit (not just what it is)
- **Action:** Try it or learn more; always dismissible

### Examples

**New Feature:**
> **✨ Introducing AI-assisted underwriting**
> 
> Automatically triage applications and get risk recommendations in seconds—not hours.
>
> [Try it now] [Learn more] [Maybe later]

**Contextual Discovery:**
> **✨ Did you know?**
> 
> You can duplicate this policy as a template for faster creation.
>
> [Show me how] [Got it]

**Upgrade Prompt:**
> **✨ Unlock team collaboration**
> 
> Upgrade to share environments, assign roles, and work together in real-time.
>
> [View plans] [Not now]

### Timing
- Show at relevant moments (not randomly)
- Limit frequency—don't pester
- Allow permanent dismissal for repeated prompts

### Do
- Focus on the benefit to the user
- Make it easy to dismiss
- Show at contextually relevant moments

### Don't
- Interrupt critical workflows
- Show the same message repeatedly
- Focus on features over benefits

## Message Formatting

### Writing Guidelines

| Element | Guideline |
|---------|-----------|
| Title | 2-5 words, sentence case, no period |
| Body | 1-3 sentences, complete sentences |
| Actions | 1-3 words, sentence case verbs |

### Action Button Labels

| Type | Primary Action | Secondary Action |
|------|----------------|------------------|
| Information | "Learn more", "Got it" | "Dismiss" |
| Success | "Continue", "View" | "Undo", "Dismiss" |
| Warning | "Cancel", Safe option | Dangerous option |
| Error | "Try again", "Fix" | "Get help", "Dismiss" |
| Discovery | "Try it", "Show me" | "Maybe later", "Dismiss" |

### Visual Hierarchy
1. Icon + Title draw initial attention
2. Body provides context
3. Actions are clearly visible and accessible

## Placement Guidelines

### Inline Messages
- Position near the relevant content or field
- Use for field validation and contextual help
- Don't block content unnecessarily

### Toast/Snackbar Messages
- Position at bottom or top of viewport
- Use for transient confirmations
- Auto-dismiss after 4-6 seconds

### Modal/Dialog Messages
- Use for critical warnings and confirmations
- Require user action before proceeding
- Reserve for high-stakes situations

### Banner Messages
- Position at top of page or section
- Use for system-wide announcements
- Make dismissible when appropriate

## Accessibility

- Ensure color is not the only indicator of message type
- Use appropriate ARIA roles (alert, status, log)
- Announce dynamic messages to screen readers
- Ensure sufficient color contrast
- Make dismiss buttons keyboard accessible
- Provide text alternatives for icons

### ARIA Roles

| Message Type | ARIA Role |
|--------------|-----------|
| Error | role="alert" |
| Warning | role="alert" |
| Success | role="status" |
| Information | role="status" |
| Discovery | role="status" |

## Usage Guidelines

### Do
- Be specific and actionable
- Match tone to message type
- Provide clear next steps
- Test messages with real users
- Consider timing and frequency

### Don't
- Use generic messages ("Error occurred")
- Stack multiple messages
- Interrupt critical flows unnecessarily
- Make messages difficult to dismiss
- Forget about screen reader users

## Examples in Context

### Form Validation
> **Field error (inline):**
> ✕ Password must be at least 12 characters

### Successful Save
> **Toast notification:**
> ✓ Changes saved

### Confirm Deletion
> **Modal dialog:**
> ⚠️ Delete "Production Environment"?
> 
> This will permanently delete all policies, data, and configurations. This action cannot be undone.
>
> [Cancel] [Delete permanently]

### System Outage
> **Page banner:**
> ⚠️ Some services are experiencing issues. We're working to resolve this. [Status page]
