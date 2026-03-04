# SpikeForge Date & Time

> Consistent, clear formatting for dates and times throughout the platform.

## Strategic Foundation

**Brand Alignment:** Coaching practices run on schedules — sessions, follow-ups, program timelines, billing cycles. Clear date and time formatting is essential to the Clarity value. Coaches should never misread a session date or misunderstand a due time. Every date and time in the platform should be immediately understandable and unambiguous.

## Date Formats

### Standard Formats

| Format | Pattern | Example | Usage |
|--------|---------|---------|-------|
| Full | [Weekday], [Month] [Day], [Year] | Monday, January 15, 2025 | Session details, formal contexts |
| Standard | [Month] [Day], [Year] | January 15, 2025 | Most UI contexts, invoices |
| Short | [Mon] [Day], [Year] | Jan 15, 2025 | Tables, compact views, lists |
| Numeric | [MM]/[DD]/[YYYY] | 01/15/2025 | Data exports, CSV files only |

### Rules
- Always spell out the month name when space allows — it prevents ambiguity
- Use the short format only in compact contexts (table cells, badges, breadcrumbs)
- Never use numeric-only dates in the UI — "01/02/2025" is ambiguous internationally
- Always include the year when the date could be in a different year than the current one
- Omit the year when the date is clearly within the current year and context confirms it

### Current Year
When the date is within the current calendar year and context makes it clear:

| Format | Example |
|--------|---------|
| Full | Monday, January 15 |
| Standard | January 15 |
| Short | Jan 15 |

## Time Formats

### Standard Formats

| Format | Pattern | Example | Usage |
|--------|---------|---------|-------|
| Full | [H]:[MM] [AM/PM] [TZ] | 2:00 PM EST | Scheduled sessions, calendar invites |
| Standard | [H]:[MM] [AM/PM] | 2:00 PM | Most UI contexts |
| Short | [H] [AM/PM] | 2 PM | Compact views, when minutes are 00 |

### Rules
- Use 12-hour format with AM/PM as the default
- Remove leading zeros: "2:00 PM" not "02:00 PM"
- Use uppercase AM/PM with no periods
- Always include minutes, even for on-the-hour times: "2:00 PM" not "2 PM" (exception: short format)
- Include timezone when the audience may be in different time zones

### Noon and Midnight
- 12:00 PM → "12:00 PM" or "noon"
- 12:00 AM → "12:00 AM" or "midnight"
- Prefer "noon" and "midnight" in natural language contexts

## Timezone Handling

### Display Rules
- Always show timezone when scheduling across time zones
- Use the coach's local timezone as the default display
- Show the client's timezone alongside when it differs
- Use standard abbreviations: EST, CST, MST, PST, UTC

### Format

```
2:00 PM EST
2:00 PM EST (11:00 AM PST for client)
```

### Timezone-Aware Contexts
- Session scheduling: Show both coach and client timezone
- Calendar views: Default to viewer's timezone
- Notifications: Use recipient's timezone
- Reports/exports: Include timezone or use UTC with label

## Relative Time

### Thresholds

| Time Elapsed | Display | Example |
|-------------|---------|---------|
| < 1 minute | "Just now" | "Just now" |
| 1–59 minutes | "[N] minutes ago" | "5 minutes ago" |
| 1–23 hours | "[N] hours ago" | "3 hours ago" |
| 1 day | "Yesterday" | "Yesterday" |
| 2–6 days | "[N] days ago" | "4 days ago" |
| 7+ days | Absolute date | "Jan 10, 2025" |

### Future Relative Time

| Time Until | Display | Example |
|-----------|---------|---------|
| < 1 hour | "In [N] minutes" | "In 15 minutes" |
| 1–23 hours | "In [N] hours" | "In 3 hours" |
| 1 day | "Tomorrow" | "Tomorrow" |
| 2–6 days | "In [N] days" | "In 4 days" |
| 7+ days | Absolute date | "Jan 20, 2025" |

### Where to Use Relative Time
- Activity feeds, notifications, and status indicators
- "Last session" timestamp on client cards
- "Last active" on engagement metrics

### Where to Use Absolute Time
- Scheduled sessions and calendar entries
- Invoices and billing dates
- Program start/end dates
- Official records and audit trails

## Combined Date and Time

### Standard Combined

| Format | Example | Usage |
|--------|---------|-------|
| Full | Monday, January 15, 2025 at 2:00 PM EST | Formal, session details page |
| Standard | January 15, 2025 at 2:00 PM | Most UI contexts |
| Short | Jan 15 at 2:00 PM | Lists, cards, compact views |
| Compact | Jan 15, 2:00 PM | Table cells, tight spaces |

### Separator
Use "at" to separate date and time in written contexts. Use a comma in compact contexts.

## Date Ranges

| Format | Example |
|--------|---------|
| Same month | January 15–20, 2025 |
| Different months | January 15 – February 8, 2025 |
| Different years | December 15, 2024 – January 30, 2025 |
| Time range | 2:00 PM – 3:30 PM |

Use an en dash (–) with spaces for ranges.

## Coaching-Specific Patterns

### Session Duration
Display duration alongside scheduled time.

```
Monday, January 15 at 2:00 PM (60 min)
2:00 PM – 3:00 PM EST (60 min)
```

### Program Timeline
```
Started: January 5, 2025
Sessions: 4 of 12 completed
Next session: January 22, 2025
Estimated completion: April 15, 2025
```

### Billing Period
```
Invoice period: January 1–31, 2025
Due date: February 15, 2025
```

### Client Engagement
```
Last session: 14 days ago
Next scheduled: January 22
Days since last contact: 28
```

## Internationalization

### ISO 8601 (Data Exchange)
Use ISO 8601 for data storage and API communication:
- Date: `2025-01-15`
- Time: `14:00:00`
- Combined: `2025-01-15T14:00:00-05:00`
- Duration: `PT60M` (60 minutes)

### Future Localization
Date and time formats should be configurable per user locale. Current defaults are US English. When expanding:
- Store all dates in UTC internally
- Format dates at the presentation layer using the user's locale
- Support 24-hour time format as a user preference
- Support date order preferences (DD/MM/YYYY for non-US locales)

## Usage Guidelines

### Do
- Use spelled-out month names in the UI — they prevent ambiguity
- Show timezone when coaches and clients may be in different zones
- Use relative time for recency indicators ("3 hours ago")
- Use absolute time for scheduled events and official records
- Include session duration alongside scheduled times

### Don't
- Use numeric-only dates (01/15/2025) in the UI
- Assume all users are in the same timezone
- Show seconds unless technically relevant
- Mix date formats within the same view
- Use relative time for events more than 7 days ago
