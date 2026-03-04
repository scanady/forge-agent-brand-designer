# iFoundry Media Date & Time

> Consistent, unambiguous formatting for dates and times — because projects run on deadlines.

## Strategic Foundation

**Brand Alignment:** Product development runs on timelines — sprint cycles, deployment windows, launch dates, milestone reviews. The Momentum value demands that dates and times are immediately clear. Engineers and founders should never misread a due date or mistake a deployment window. Precision in temporal formatting reflects the same precision we bring to architecture and code.

## Date Formats

### Standard Formats

| Format | Pattern | Example | Usage |
|--------|---------|---------|-------|
| Full | [Weekday], [Month] [Day], [Year] | Monday, January 15, 2026 | Milestone details, formal contexts |
| Standard | [Month] [Day], [Year] | January 15, 2026 | Most UI contexts, proposals |
| Short | [Mon] [Day], [Year] | Jan 15, 2026 | Tables, compact views, sprint boards |
| Numeric | [YYYY]-[MM]-[DD] | 2026-01-15 | Data exports, logs, API responses (ISO 8601) |

### Rules
- Always spell out the month name when space allows — it eliminates ambiguity
- Use the short format only in compact contexts (table cells, badges, sprint cards)
- Use ISO 8601 numeric format for data exports and developer-facing logs — never for user-facing UI
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
| Full | [H]:[MM] [AM/PM] [TZ] | 2:00 PM EST | Scheduled meetings, deployment windows |
| Standard | [H]:[MM] [AM/PM] | 2:00 PM | Most UI contexts |
| Short | [H] [AM/PM] | 2 PM | Compact views, when minutes are :00 |
| 24-hour | [HH]:[MM] | 14:00 | Logs, developer tools, CI/CD timestamps |

### Rules
- Use 12-hour format with AM/PM as the default for client-facing UI
- Support 24-hour format as a user preference — especially for engineering tools
- Remove leading zeros: "2:00 PM" not "02:00 PM"
- Use uppercase AM/PM with no periods
- Always include minutes, even for on-the-hour times in standard format

### Noon and Midnight
- 12:00 PM → "12:00 PM" or "noon"
- 12:00 AM → "12:00 AM" or "midnight"
- Prefer "noon" and "midnight" in natural language contexts

## Timezone Handling

### Display Rules
- Always show timezone for cross-timezone collaboration (distributed teams are the norm)
- Default to the viewer's local timezone
- Show the collaborator's timezone alongside when it differs
- Use standard abbreviations: EST, CST, PST, UTC, IST, CET

### Format

```
2:00 PM EST
2:00 PM EST (11:30 PM IST for partner)
```

### Timezone-Aware Contexts
- Sprint ceremonies: Show all participants' timezones
- Deployment windows: Use UTC with local conversion
- Calendar views: Default to viewer's timezone
- Notifications: Use recipient's timezone
- Logs and audit trails: Always UTC

## Relative Time

### Thresholds

| Time Elapsed | Display | Example |
|-------------|---------|---------|
| < 1 minute | "Just now" | "Just now" |
| 1–59 minutes | "[N] minutes ago" | "5 minutes ago" |
| 1–23 hours | "[N] hours ago" | "3 hours ago" |
| 1 day | "Yesterday" | "Yesterday" |
| 2–6 days | "[N] days ago" | "4 days ago" |
| 7+ days | Absolute date | "Jan 10, 2026" |

### Future Relative Time

| Time Until | Display | Example |
|-----------|---------|---------|
| < 1 hour | "In [N] minutes" | "In 15 minutes" |
| 1–23 hours | "In [N] hours" | "In 3 hours" |
| 1 day | "Tomorrow" | "Tomorrow" |
| 2–6 days | "In [N] days" | "In 4 days" |
| 7+ days | Absolute date | "Jan 20, 2026" |

### Where to Use Relative Time
- Activity feeds, commit timestamps, deployment history
- "Last deployed" indicators on project dashboards
- Notification timestamps

### Where to Use Absolute Time
- Sprint start/end dates, milestone deadlines
- Deployment schedules and maintenance windows
- Proposals, contracts, invoices
- Audit trails and compliance records

## Combined Date and Time

### Standard Combined

| Format | Example | Usage |
|--------|---------|-------|
| Full | Monday, January 15, 2026 at 2:00 PM EST | Formal, milestone details |
| Standard | January 15, 2026 at 2:00 PM | Most UI contexts |
| Short | Jan 15 at 2:00 PM | Sprint boards, cards, compact views |
| Compact | Jan 15, 2:00 PM | Table cells, tight spaces |

### Separator
Use "at" to separate date and time in written contexts. Use a comma in compact contexts.

## Date Ranges

| Format | Example |
|--------|---------|
| Same month | January 15–29, 2026 |
| Different months | January 15 – February 12, 2026 |
| Different years | December 15, 2025 – January 30, 2026 |
| Time range | 2:00 PM – 3:30 PM |

Use an en dash (–) with spaces for ranges.

## Product Development Patterns

### Sprint Duration
```
Sprint 12: January 13–24, 2026 (2 weeks)
Sprint planning: Monday, Jan 13 at 9:00 AM EST
Sprint review: Friday, Jan 24 at 3:00 PM EST
```

### Deployment Window
```
Scheduled: January 15, 2026 at 2:00 AM UTC
Estimated duration: 45 minutes
Status: Pending
```

### Milestone Timeline
```
Discovery: Complete
Architecture: January 6–17, 2026
Sprint 1: January 20 – February 7, 2026
MVP launch: March 15, 2026
```

### Project Proposal
```
Engagement start: February 1, 2026
Estimated MVP: 12 weeks (May 2026)
Team: 3 engineers, 1 architect, 1 designer
```

## Internationalization

### ISO 8601 (Data Exchange)
Use ISO 8601 for all data storage, APIs, and machine-readable contexts:
- Date: `2026-01-15`
- Time: `14:00:00`
- Combined: `2026-01-15T14:00:00-05:00`
- Duration: `P2W` (2 weeks), `PT45M` (45 minutes)

### Future Localization
Date and time formats should be configurable per user locale. Current defaults are US English. When expanding:
- Store all dates in UTC internally
- Format at the presentation layer using user locale
- Support 24-hour time as a user preference
- Support DD/MM/YYYY for non-US locales

## Usage Guidelines

### Do
- Use spelled-out month names in user-facing UI
- Show timezone when collaborating across time zones
- Use relative time for recency indicators
- Use absolute time for scheduled events and deadlines
- Use UTC consistently in logs and developer tooling

### Don't
- Use ambiguous numeric-only dates (01/02/2026) in UI
- Assume all team members are in the same timezone
- Show seconds unless technically relevant (logs, CI/CD)
- Mix date formats within the same view
- Use relative time for events more than 7 days ago
