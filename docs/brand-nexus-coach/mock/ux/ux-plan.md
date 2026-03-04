# Nexus Coach UX Plan

> Complete application mockup plan for the Nexus Coach coaching practice management platform.

## Application Overview

**Application Type:** Coaching practice management platform (B2B SaaS)

**Key Features:**
- Client management and engagement tracking
- Session scheduling, documentation, and follow-through
- Program/package lifecycle management
- Prospect pipeline and discovery call workflow
- Billing and invoicing
- Practice analytics and coach performance oversight
- Multi-role support (Coach, Practice Lead, Client)

**Target Users:**
- Solo coaches managing their own practice
- Practice leads overseeing multiple coaches and clients
- Coaches within a firm handling their client roster

**Brand Personality:** Guide archetype + Architect precision. Calm, confident, organized. Dark sidebar navigation with teal accents. Clean white content areas.

## Information Architecture

```
Nexus Coach
├── Authentication
│   ├── Login
│   ├── Sign Up
│   └── Password Reset
├── Home (Welcome + Quick Access)
├── Dashboard (Practice Overview)
├── Practice Management
│   ├── Clients
│   │   └── Client Detail
│   ├── Sessions
│   │   └── Session Detail
│   ├── Programs
│   │   └── Program Detail
│   └── Prospects
│       └── Prospect Detail
├── Billing
│   └── Invoice Detail
├── Insights
│   ├── Analytics
│   └── Coach Performance
├── User
│   ├── Profile
│   ├── Settings
│   ├── Preferences
│   └── Notifications
└── Error Pages
    ├── 404
    └── 500
```

## Navigation Structure

### Primary Navigation (Sidebar)
- **Logo** — Nexus Coach mark
- **Practice** — Dashboard, Clients, Sessions, Programs, Prospects
- **Business** — Billing
- **Insights** — Analytics, Coach Performance
- **Bottom** — Settings, Help, User avatar

### Top Bar
- Global search
- Notifications bell with badge
- Help button
- User menu with avatar

## Views to Create

### Authentication (3 pages)
1. `login.html` — Email/password sign in
2. `signup.html` — Registration form
3. `password-reset.html` — Password recovery

### Core Application (3 pages)
4. `home.html` — Welcome page with quick stats vs quick access cards
5. `dashboard.html` — Practice dashboard with KPIs, upcoming sessions, client health
6. `notifications.html` — Notification center

### Practice Management (8 pages)
7. `clients.html` — Client roster with search, filters, health indicators
8. `client-detail.html` — Individual client view (profile, sessions, notes, billing)
9. `sessions.html` — Session calendar/list with status tracking
10. `session-detail.html` — Session view (prep, notes, action items)
11. `programs.html` — Program/package management
12. `program-detail.html` — Individual program view
13. `prospects.html` — Prospect pipeline with stages
14. `prospect-detail.html` — Individual prospect with discovery call workflow

### Business (1 page)
15. `billing.html` — Invoices, payments, revenue overview

### Insights (2 pages)
16. `analytics.html` — Practice metrics and trends
17. `coach-performance.html` — Coach utilization, compliance, performance

### User Settings (3 pages)
18. `profile.html` — User profile and account
19. `settings.html` — Practice settings
20. `preferences.html` — Personal preferences

### Utility (2 pages)
21. `404.html` — Page not found
22. `500.html` — Server error

**Total: 22 HTML mockups**

## Component Inventory

### Navigation
- Dark sidebar with grouped sections
- Sticky top bar with search, notifications, user menu
- Breadcrumbs on detail pages

### Data Display
- Stat cards (KPIs with trend indicators)
- Data tables (sortable, filterable)
- Client health cards with status badges
- Session timeline
- Activity feed
- Analytics charts (represented as placeholders)

### Forms
- Login/signup forms
- Search and filter bars
- Session note editor area
- Settings forms with grouped controls

### Feedback
- Toast notifications
- Status badges (engaged, at-risk, disengaged)
- Empty states with illustrations
- Loading states

### Interactive
- Tabs for content sections
- Dropdown menus
- Modals (implied through button states)
- Pagination

## User Flows

### Coach Daily Workflow
Home → Dashboard → Today's Sessions → Session Detail (prep) → Log Notes → Next Session

### Practice Lead Oversight
Dashboard → Client Health Overview → At-Risk Client → Review Engagement → Coach Performance

### New Prospect Flow
Prospects → Add Prospect → Schedule Discovery → Log Discovery Outcome → Convert to Client

### Client Management
Clients → Client Detail → View Sessions → Add Session Notes → Track Action Items

## Design Tokens Summary

Colors: Guide Teal `#0F766E`, Structure Slate `#0F172A`, Momentum Amber `#D97706`, Clarity Sky `#0284C7`, Insight Indigo `#6366F1`, Growth Emerald `#059669`

Typography: Plus Jakarta Sans (300–800), IBM Plex Mono (400–600)

Spacing: 4px base, scale from 2px to 96px

Border Radius: 4px (sm), 6px (md), 8px (lg), 12px (xl)

Shadows: 5-level scale from none to 2xl
