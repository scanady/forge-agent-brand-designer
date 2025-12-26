# OpenLife Date & Time

> Clear, consistent date and time formatting for global users.

## Strategic Foundation

**Brand Alignment:** OpenLife serves a global community. Our date and time formatting prioritizes clarity and reduces ambiguity, reflecting our commitment to transparency and precision. Consistent formatting across all touchpoints reinforces trust and professionalism.

## Date Formats

### Standard Formats

| Format | Pattern | Example | Usage |
|--------|---------|---------|-------|
| Short | MMM D | Dec 25 | Space-constrained UI, lists |
| Medium | MMM D, YYYY | Dec 25, 2025 | Default for most contexts |
| Long | MMMM D, YYYY | December 25, 2025 | Formal documents, emphasis |
| Numeric | YYYY-MM-DD | 2025-12-25 | Technical contexts, APIs, logs |

### Format Tokens

| Token | Meaning | Example |
|-------|---------|---------|
| YYYY | 4-digit year | 2025 |
| YY | 2-digit year | 25 |
| MMMM | Full month name | December |
| MMM | Abbreviated month | Dec |
| MM | 2-digit month | 12 |
| M | Month number | 12 |
| DD | 2-digit day | 05 |
| D | Day number | 5 |
| dddd | Full day name | Thursday |
| ddd | Abbreviated day | Thu |

### Day of Week
Include the day of week when it provides context:

| Format | Example | Usage |
|--------|---------|-------|
| With day (long) | Thursday, December 25, 2025 | Event dates, important dates |
| With day (short) | Thu, Dec 25 | Calendars, schedules |

### Date Ranges

| Context | Format | Example |
|---------|--------|---------|
| Same month | MMM D–D, YYYY | Dec 20–25, 2025 |
| Different months | MMM D – MMM D, YYYY | Nov 28 – Dec 5, 2025 |
| Different years | MMM D, YYYY – MMM D, YYYY | Dec 15, 2024 – Jan 15, 2025 |

Use an en dash (–) for ranges, with spaces on either side when months differ.

## Time Formats

### Standard Formats

| Format | Pattern | Example | Usage |
|--------|---------|---------|-------|
| Short (12h) | h:mm a | 3:30 PM | Default for US audiences |
| Short (24h) | HH:mm | 15:30 | Technical contexts, international |
| With seconds | h:mm:ss a | 3:30:45 PM | Logs, timestamps |
| ISO 8601 | HH:mm:ss | 15:30:45 | APIs, data exchange |

### 12-Hour vs. 24-Hour

| Context | Format | Notes |
|---------|--------|-------|
| US-focused UI | 12-hour | Use AM/PM (uppercase, with space) |
| International UI | User preference | Allow users to choose |
| Technical/logs | 24-hour | Avoids AM/PM ambiguity |
| APIs | 24-hour | ISO 8601 standard |

### Time Format Tokens

| Token | Meaning | Example |
|-------|---------|---------|
| HH | 24-hour, 2-digit | 09, 14 |
| H | 24-hour | 9, 14 |
| hh | 12-hour, 2-digit | 09, 02 |
| h | 12-hour | 9, 2 |
| mm | Minutes, 2-digit | 05, 30 |
| ss | Seconds, 2-digit | 05, 45 |
| a | AM/PM lowercase | am, pm |
| A | AM/PM uppercase | AM, PM |

### AM/PM Styling
- Use uppercase with a space: "3:30 PM"
- Use consistently throughout the application
- Never use periods: "3:30 PM" not "3:30 P.M."

## Timezone Handling

### Display Guidelines

| Context | Format | Example |
|---------|--------|---------|
| User's local time | Time only | 3:30 PM |
| Ambiguous context | Time + zone | 3:30 PM EST |
| International | Time + offset | 3:30 PM (UTC-5) |
| Technical | ISO 8601 | 2025-12-25T15:30:00-05:00 |

### Timezone Abbreviations

Use standard abbreviations:
- EST/EDT (Eastern)
- CST/CDT (Central)
- MST/MDT (Mountain)
- PST/PDT (Pacific)
- UTC (Coordinated Universal Time)

### Best Practices
- Always specify timezone when scheduling across regions
- Store times in UTC; display in user's local timezone
- Show timezone explicitly for scheduled events
- Allow users to set their preferred timezone

## Relative Time

Use relative time for recent or upcoming events when precision isn't critical.

### Relative Time Expressions

| Time Passed | Display |
|-------------|---------|
| < 1 minute | "Just now" |
| 1 minute | "1 minute ago" |
| 2–59 minutes | "X minutes ago" |
| 1 hour | "1 hour ago" |
| 2–23 hours | "X hours ago" |
| 1 day | "Yesterday" |
| 2–6 days | "X days ago" |
| 7+ days | Absolute date (Dec 18) |

### Future Relative Time

| Time Until | Display |
|------------|---------|
| < 1 hour | "In X minutes" |
| 1–23 hours | "In X hours" |
| 1 day | "Tomorrow" |
| 2–6 days | "In X days" |
| 7+ days | Absolute date |

### When to Use Relative vs. Absolute

| Relative Time | Absolute Time |
|---------------|---------------|
| Activity feeds | Scheduled events |
| Notifications | Deadlines |
| Recent updates | Historical records |
| Comments, replies | Legal documents |
| Status changes | Reports, analytics |

## Combined Date & Time

### Standard Combinations

| Context | Format | Example |
|---------|--------|---------|
| Default | MMM D, YYYY at h:mm a | Dec 25, 2025 at 3:30 PM |
| Compact | MMM D, h:mm a | Dec 25, 3:30 PM |
| With day | ddd, MMM D at h:mm a | Thu, Dec 25 at 3:30 PM |
| Technical | YYYY-MM-DD HH:mm:ss | 2025-12-25 15:30:00 |
| ISO 8601 | YYYY-MM-DDTHH:mm:ssZ | 2025-12-25T15:30:00Z |

Use "at" to separate date and time in user-facing content.

## Internationalization

### Localization Considerations

| Region | Date Format | Time Format |
|--------|-------------|-------------|
| United States | Dec 25, 2025 | 3:30 PM |
| United Kingdom | 25 Dec 2025 | 15:30 |
| Europe (most) | 25.12.2025 | 15:30 |
| Japan | 2025年12月25日 | 15:30 |
| ISO Standard | 2025-12-25 | 15:30:00 |

### Implementation Guidelines
- Store dates in ISO 8601 format (YYYY-MM-DD)
- Store times in UTC
- Use locale-aware formatting libraries
- Allow users to set date/time preferences
- Test with multiple locales

### Avoid Ambiguity
The format "12/05/2025" is ambiguous (December 5 or May 12?). Use:
- Named months: "Dec 5, 2025"
- ISO format for technical contexts: "2025-12-05"

## Usage Guidelines

### Do
- Be consistent within each product/context
- Use the user's preferred timezone when known
- Include timezone for cross-region communications
- Use relative time for recent activity
- Follow ISO 8601 for technical data

### Don't
- Use ambiguous numeric-only formats (12/05/25)
- Mix 12-hour and 24-hour formats inconsistently
- Forget to account for timezone differences
- Use relative time for important deadlines
- Hardcode date formats (use libraries)

## Accessibility

- Don't rely solely on color to indicate time urgency
- Provide full date/time on hover for relative times
- Use semantic HTML datetime attributes
- Ensure time-based content is understandable by screen readers
- Allow sufficient time for time-limited actions

## Examples

### Activity Feed
> "Policy updated **3 hours ago** by Sarah Chen"

### Scheduled Event
> "Deployment scheduled for **Thu, Dec 25 at 3:30 PM EST**"

### Notification
> "Build completed **just now**"

### Report Header
> "Report generated: **December 25, 2025 at 3:30:45 PM EST**"

### API Response
```json
{
  "created_at": "2025-12-25T15:30:45Z",
  "updated_at": "2025-12-25T20:15:00Z"
}
```
