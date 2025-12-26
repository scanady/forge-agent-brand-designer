# OpenLife UX Navigation Map

> Complete navigation structure and page relationships for the OpenLife Life Insurance Product Management system

## Overview

This document maps all 24 mockup pages and their relationships, showing how users navigate through the OpenLife system.

## Site Structure

```
OpenLife Product Management System
├── Authentication (Public)
│   ├── login.html
│   ├── signup.html
│   └── password-reset.html
│
├── Main Application (Authenticated)
│   ├── Home & Dashboard
│   │   ├── home.html (Landing/Overview)
│   │   └── dashboard.html (Main Workspace)
│   │
│   ├── Analytics & Insights
│   │   └── analytics.html (Performance Analytics)
│   │
│   ├── Product Management
│   │   ├── manage-products.html (Product Catalog)
│   │   ├── create-product.html (Create New Product)
│   │   ├── product-details.html (View Product)
│   │   ├── edit-product.html (Edit Product)
│   │   └── product-versions.html (Version History)
│   │
│   ├── Coverage Management
│   │   ├── view-coverages.html (View Coverages)
│   │   └── edit-coverages.html (Edit Coverages)
│   │
│   ├── Configuration
│   │   ├── pricing-configuration.html (Pricing Setup)
│   │   └── underwriting-rules.html (Underwriting Rules)
│   │
│   ├── Compliance & Documentation
│   │   ├── audit-trail.html (Audit Log)
│   │   └── document-management.html (Documents)
│   │
│   ├── Collaboration
│   │   ├── team-activity.html (Team Activity)
│   │   └── notifications.html (Notification Center)
│   │
│   └── User Management
│       ├── profile.html (User Profile)
│       ├── preferences.html (User Preferences)
│       └── settings.html (Account Settings)
│
└── Utility Pages
    ├── 404.html (Page Not Found)
    └── 500.html (Server Error)
```

## Primary Navigation (Sidebar)

The sidebar navigation is consistent across all authenticated pages:

### Main Section
- **Home** → home.html
- **Dashboard** → dashboard.html
- **Analytics** → analytics.html

### Product Management Section
- **Products** → manage-products.html
- **Coverages** → view-coverages.html

### Configuration Section
- **Pricing** → pricing-configuration.html
- **Underwriting** → underwriting-rules.html

### Compliance Section
- **Audit Trail** → audit-trail.html
- **Documents** → document-management.html

### Collaboration Section
- **Team Activity** → team-activity.html
- **Notifications** → notifications.html

### Global Actions
- **AI Assistant** → Modal/Overlay (always available)

## Secondary Navigation (Top Header)

Available on all authenticated pages:

- **Search Bar** → Global search (stays on current page, shows results)
- **Notifications Bell** → notifications.html
- **Help Icon** → Help documentation (external or modal)
- **User Menu** → Dropdown with:
  - Profile → profile.html
  - Preferences → preferences.html
  - Settings → settings.html
  - Logout → login.html

## Page-to-Page Relationships

### User Flows

#### Flow 1: Unauthenticated User
```
login.html
  ├─> [Sign up link] → signup.html
  ├─> [Forgot password] → password-reset.html
  └─> [Successful login] → home.html or dashboard.html
```

#### Flow 2: New User Onboarding
```
signup.html
  └─> [Account created] → home.html (Welcome)
        └─> [Get started] → dashboard.html
```

#### Flow 3: Product Creation Journey
```
home.html or dashboard.html
  └─> [Create Product button] → create-product.html
        └─> [Step 1: Basic Info] → create-product.html (step 2)
              └─> [Step 2: Coverage] → create-product.html (step 3)
                    └─> [Step 3: Pricing] → create-product.html (step 4)
                          └─> [Step 4: Review & Submit] → product-details.html (new product)
```

#### Flow 4: Product Management
```
manage-products.html
  ├─> [View product] → product-details.html
  │     ├─> [Edit] → edit-product.html
  │     │     └─> [Save] → product-details.html (updated)
  │     ├─> [View versions] → product-versions.html
  │     └─> [Configure coverages] → edit-coverages.html
  │
  ├─> [Create product] → create-product.html
  └─> [Filter/Search] → manage-products.html (filtered results)
```

#### Flow 5: Coverage Configuration
```
view-coverages.html
  └─> [Edit coverage] → edit-coverages.html
        └─> [Save] → view-coverages.html (updated)
```

#### Flow 6: Analytics & Reporting
```
dashboard.html
  └─> [View detailed analytics] → analytics.html
        ├─> [Filter by product] → analytics.html (filtered)
        └─> [View product details] → product-details.html
```

#### Flow 7: Compliance & Audit
```
audit-trail.html
  ├─> [Filter by date/user/action] → audit-trail.html (filtered)
  ├─> [View related product] → product-details.html
  └─> [Export audit report] → Download file
```

#### Flow 8: Document Management
```
document-management.html
  ├─> [Upload document] → document-management.html (modal)
  ├─> [View document] → External viewer or modal
  └─> [Associate with product] → product-details.html
```

#### Flow 9: Team Collaboration
```
team-activity.html
  ├─> [View activity details] → Related page (product-details.html, audit-trail.html, etc.)
  └─> [Filter by user/date] → team-activity.html (filtered)
```

#### Flow 10: User Settings
```
profile.html
  ├─> [Edit profile] → profile.html (edit mode)
  └─> [Change settings] → settings.html

preferences.html
  └─> [Save preferences] → preferences.html (updated)

settings.html
  ├─> [Change password] → settings.html (modal)
  └─> [Account settings] → settings.html (updated)
```

## Breadcrumb Navigation

Pages with breadcrumbs (showing hierarchy):

### Two-Level Breadcrumbs
- Dashboard: `Home > Dashboard`
- Analytics: `Home > Analytics`
- Notifications: `Home > Notifications`
- Profile: `Home > Profile`
- Preferences: `Home > Preferences`
- Settings: `Home > Settings`

### Three-Level Breadcrumbs
- Manage Products: `Home > Products > Manage Products`
- Create Product: `Home > Products > Create Product`
- Product Details: `Home > Products > [Product Name]`
- Edit Product: `Home > Products > [Product Name] > Edit`
- Product Versions: `Home > Products > [Product Name] > Versions`

- View Coverages: `Home > Coverages > View Coverages`
- Edit Coverages: `Home > Coverages > Edit Coverage`

- Pricing Configuration: `Home > Configuration > Pricing`
- Underwriting Rules: `Home > Configuration > Underwriting Rules`

- Audit Trail: `Home > Compliance > Audit Trail`
- Document Management: `Home > Compliance > Documents`

- Team Activity: `Home > Collaboration > Team Activity`

## Action Links & CTAs

### From home.html
- **Hero CTA "Create New Product"** → create-product.html
- **Hero CTA "Go to Dashboard"** → dashboard.html
- **"View detailed analytics"** → analytics.html
- **"Browse products"** → manage-products.html
- **"Start creating"** → create-product.html
- **"View analytics"** → analytics.html
- **"Manage coverages"** → view-coverages.html
- **"View all activity"** → team-activity.html

### From dashboard.html
- **"Create New Product"** → create-product.html
- **"View Analytics"** → analytics.html
- **"Manage Products"** → manage-products.html
- **Quick action cards** → Respective pages

### From manage-products.html
- **"Create Product" button** → create-product.html
- **"View" link** → product-details.html
- **Product name link** → product-details.html

### From create-product.html
- **"Cancel" button** → manage-products.html
- **"Next Step" button** → create-product.html (next step)
- **"Submit" button (final step)** → product-details.html

### From product-details.html
- **"Edit" button** → edit-product.html
- **"View Versions" link** → product-versions.html
- **"Configure Coverages" link** → edit-coverages.html
- **"View in Analytics" link** → analytics.html

### From edit-product.html
- **"Cancel" button** → product-details.html
- **"Save" button** → product-details.html

### From view-coverages.html
- **"Edit Coverage" button** → edit-coverages.html
- **Coverage item link** → edit-coverages.html

### From edit-coverages.html
- **"Cancel" button** → view-coverages.html
- **"Save" button** → view-coverages.html

### From analytics.html
- **Product name in chart** → product-details.html
- **"View Product" link** → product-details.html

### From audit-trail.html
- **Related product link** → product-details.html
- **User name link** → profile.html (view other user's profile)

### From document-management.html
- **"Upload Document" button** → document-management.html (modal)
- **"View Document" link** → External viewer or modal
- **Associated product link** → product-details.html

### From team-activity.html
- **Activity item link** → Related page (varies by activity type)
- **User avatar** → profile.html (view user's profile)

### From notifications.html
- **Notification item** → Related page (varies by notification type)
- **"Mark all as read" button** → notifications.html (updated)

## Error Handling

### 404 Error (404.html)
Triggered when:
- User navigates to non-existent page
- Broken link or mistyped URL

**Available actions:**
- "Go to Home" → home.html
- "Go to Dashboard" → dashboard.html
- Search bar (to find what they're looking for)

### 500 Error (500.html)
Triggered when:
- Server error occurs
- Application crashes
- Database connection fails

**Available actions:**
- "Try Again" button → Reload current page
- "Go to Home" → home.html
- "Contact Support" → External support link

## Special Interactions

### Modal/Overlay Interactions
These don't navigate away from the current page:
- AI Assistant (opened from any page)
- Confirmation dialogs (delete, submit, etc.)
- Quick edit modals
- Image/document viewers
- Help tooltips and popovers

### External Links
These navigate away from the application:
- Help documentation (opens in new tab)
- Support contact (email or external system)
- Rate table downloads
- Report exports
- External compliance documents

## Navigation States

### Active State
The currently active page is highlighted in the sidebar navigation with:
- Background: Liberation Blue (#0066CC)
- Text: White
- Icon: White

### Hover State
Navigation items show hover state with:
- Background: rgba(255, 255, 255, 0.08)
- Text: White
- Smooth transition (150ms)

### Focus State
Keyboard navigation shows focus with:
- Visible focus ring
- 2px outline in Liberation Blue
- 2px offset

## Responsive Navigation

### Desktop (1024px+)
- Full sidebar visible (260px width)
- All navigation items visible
- Top header with search bar
- Full breadcrumbs

### Tablet (640-1024px)
- Collapsible sidebar
- Hamburger menu icon
- Condensed top header
- Abbreviated breadcrumbs

### Mobile (<640px)
- Bottom navigation bar
- Overlay sidebar menu
- Minimal top header
- No breadcrumbs (back button instead)

## Search Functionality

### Global Search (Top Header)
Available on all authenticated pages:
- **Input:** Search products, coverages, or documentation
- **Results:** Dropdown with:
  - Products → product-details.html
  - Coverages → view-coverages.html
  - Documents → document-management.html
  - Help articles → Help documentation
- **No results:** Suggestions for refining search

## Deep Linking

All pages support direct URL access (when authenticated):
- `/home` → home.html
- `/dashboard` → dashboard.html
- `/products` → manage-products.html
- `/products/create` → create-product.html
- `/products/[id]` → product-details.html
- `/products/[id]/edit` → edit-product.html
- `/analytics` → analytics.html
- `/coverages` → view-coverages.html
- And so on...

## User Journey Summary

### First-Time User
```
Login → Home (Welcome) → Dashboard → Create Product → Product Details → Analytics
```

### Daily User
```
Login → Dashboard → [Daily tasks: View products, Check analytics, Review notifications]
```

### Product Manager
```
Dashboard → Manage Products → Create/Edit Products → Configure Coverages → View Analytics
```

### Compliance Officer
```
Dashboard → Audit Trail → Document Management → Review Activities
```

### Administrator
```
Dashboard → Settings → Team Activity → Manage All Areas
```

## Summary Statistics

- **Total Pages:** 24
- **Authenticated Pages:** 21
- **Public Pages:** 3 (login, signup, password-reset)
- **Error Pages:** 2 (404, 500)
- **Main Navigation Items:** 11
- **Primary User Flows:** 10
- **Action CTAs:** 50+

---

**Document Version:** 1.0  
**Last Updated:** 2025-12-26  
**Status:** Complete
