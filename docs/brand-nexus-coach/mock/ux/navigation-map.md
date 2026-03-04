# Nexus Coach Navigation Map

> This document describes how all 22 mockup pages link to each other, the navigation hierarchy, and primary user flows.

## Page Inventory (22 pages)

| # | File | Page Title | Layout Type |
|---|------|-----------|-------------|
| 1 | login.html | Sign In | Auth (split panel) |
| 2 | signup.html | Create Account | Auth (split panel) |
| 3 | password-reset.html | Reset Password | Auth (split panel) |
| 4 | home.html | Welcome Home | App (sidebar + header) |
| 5 | dashboard.html | Practice Dashboard | App (sidebar + header) |
| 6 | clients.html | Clients | App (sidebar + header) |
| 7 | client-detail.html | Client Detail | App (sidebar + header) |
| 8 | sessions.html | Sessions | App (sidebar + header) |
| 9 | session-detail.html | Session Detail | App (sidebar + header) |
| 10 | programs.html | Programs | App (sidebar + header) |
| 11 | program-detail.html | Program Detail | App (sidebar + header) |
| 12 | prospects.html | Prospect Pipeline | App (sidebar + header) |
| 13 | prospect-detail.html | Prospect Detail | App (sidebar + header) |
| 14 | billing.html | Billing | App (sidebar + header) |
| 15 | analytics.html | Analytics | App (sidebar + header) |
| 16 | coach-performance.html | Coach Performance | App (sidebar + header) |
| 17 | profile.html | Account > Profile | App (sidebar + header + settings tabs) |
| 18 | settings.html | Account > Settings | App (sidebar + header + settings tabs) |
| 19 | preferences.html | Account > Preferences | App (sidebar + header + settings tabs) |
| 20 | notifications.html | Account > Notifications | App (sidebar + header + settings tabs) |
| 21 | 404.html | Page Not Found | Standalone (centered) |
| 22 | 500.html | Server Error | Standalone (centered) |

## Navigation Hierarchy

### Sidebar Navigation (all app pages)
```
Practice
  ├── Dashboard         → dashboard.html
  ├── Clients           → clients.html
  ├── Sessions          → sessions.html
  ├── Programs          → programs.html
  └── Prospects         → prospects.html

Business
  └── Billing           → billing.html

Insights
  ├── Analytics         → analytics.html
  └── Coach Performance → coach-performance.html

Bottom
  └── Settings          → settings.html
```

### Logo Link
All pages: Logo → home.html

### Settings Sub-Navigation (tab bar)
```
Profile      → profile.html
Settings     → settings.html
Preferences  → preferences.html
Notifications → notifications.html
```

## Page-to-Page Links

### Authentication Flow
```
login.html
  → signup.html (Create account link)
  → password-reset.html (Forgot password link)
  → home.html (after successful login)

signup.html
  → login.html (Already have account link)

password-reset.html
  → login.html (Back to sign in link)
```

### Main Application Navigation
Every app page (4-20) contains:
- **Sidebar links** to: dashboard, clients, sessions, programs, prospects, billing, analytics, coach-performance, settings
- **Logo** link to home.html
- **Header** notification bell and user avatar

### Detail Page Breadcrumbs
```
client-detail.html    ← clients.html (Clients breadcrumb)
session-detail.html   ← sessions.html (Sessions breadcrumb)
program-detail.html   ← programs.html (Programs breadcrumb)
prospect-detail.html  ← prospects.html (Prospects breadcrumb)
```

### List → Detail Navigation
```
clients.html       → client-detail.html (click client row)
sessions.html      → session-detail.html (click session block)
programs.html      → program-detail.html (click program card)
prospects.html     → prospect-detail.html (click prospect card)
```

### Error Pages
```
404.html → home.html (Go Home button)
404.html → dashboard.html (Dashboard button)
500.html → home.html (Go Home button)
500.html → [current page] (Try Again / reload)
```

## Primary User Flows

### Flow 1: Coach Daily Workflow
```
login.html → home.html → dashboard.html → sessions.html → session-detail.html
```
Coach logs in, views welcome overview, checks practice dashboard, opens today's sessions, prepares notes for upcoming session.

### Flow 2: Client Management
```
home.html → clients.html → client-detail.html
```
Coach navigates to client roster, searches/filters for a client, views their profile with session history, notes, and billing.

### Flow 3: New Prospect Conversion
```
prospects.html → prospect-detail.html → (Convert to Client) → clients.html
```
Coach reviews pipeline, opens prospect detail, conducts discovery, converts prospect to active client.

### Flow 4: Session Documentation
```
sessions.html → session-detail.html → (complete notes) → client-detail.html
```
Coach opens calendar, selects a session, documents notes and action items, then reviews client record.

### Flow 5: Program Management
```
programs.html → program-detail.html → (view enrolled clients) → client-detail.html
```
Practice lead reviews program catalog, opens a program, checks enrolled clients and progress.

### Flow 6: Business Review
```
dashboard.html → billing.html → analytics.html → coach-performance.html
```
Practice lead reviews dashboard KPIs, checks invoice status, reviews practice analytics, evaluates coach performance.

### Flow 7: Account Setup
```
settings.html → profile.html → preferences.html → notifications.html
```
User configures their practice settings, updates profile information, sets preferences, and configures notification channels.

## Active States

Each page sets the `.active` class on its corresponding sidebar nav item:
- home.html: No sidebar active (logo highlights instead)
- dashboard.html: Dashboard
- clients.html, client-detail.html: Clients
- sessions.html, session-detail.html: Sessions
- programs.html, program-detail.html: Programs
- prospects.html, prospect-detail.html: Prospects
- billing.html: Billing
- analytics.html: Analytics
- coach-performance.html: Coach Performance
- profile.html, settings.html, preferences.html, notifications.html: Settings
