# OpenLife UX Mockups

> Comprehensive UI/UX mockups for the OpenLife Life Insurance Product Management System

## Overview

This directory contains 24 interactive HTML mockups demonstrating the complete user experience of the OpenLife platform. Each mockup is a fully-styled, navigable HTML page that showcases the design system, user flows, and functionality of the application.

**Tagline:** *Collaborate. Innovate. Transform.*

## Quick Start

### Viewing the Mockups

1. Open `home.html` in a web browser to start
2. Navigate through the application using the sidebar and links
3. All pages are interconnected and demonstrate real user flows

### Recommended Viewing Path

```
home.html → dashboard.html → manage-products.html → create-product.html → analytics.html
```

## Contents

### Documentation (2 files)

- **`ux-plan.md`** - Comprehensive UX planning document with:
  - Application overview and goals
  - Complete information architecture
  - List of all 24 views with descriptions
  - Component inventory
  - User flows
  - Design tokens and specifications
  
- **`navigation-map.md`** - Navigation structure document showing:
  - Site hierarchy
  - Page-to-page relationships
  - User journeys
  - Breadcrumb patterns
  - Deep linking structure

### HTML Mockups (24 files)

#### Core Application (6 pages)
- `home.html` - Landing page with overview and quick access
- `dashboard.html` - Main workspace with metrics and actions
- `analytics.html` - Performance insights and charts
- `manage-products.html` - Product catalog with search/filter
- `create-product.html` - Multi-step product creation wizard
- `product-details.html` - Detailed product view

#### Product & Coverage Management (5 pages)
- `edit-product.html` - Product editing form
- `view-coverages.html` - Coverage options display
- `edit-coverages.html` - Coverage editing form
- `pricing-configuration.html` - Pricing setup
- `underwriting-rules.html` - Underwriting rules management

#### Compliance & Documentation (3 pages)
- `audit-trail.html` - System audit log
- `document-management.html` - Document repository
- `product-versions.html` - Version history

#### Collaboration (2 pages)
- `team-activity.html` - Team collaboration view
- `notifications.html` - Notification center

#### User Management (3 pages)
- `profile.html` - User profile
- `preferences.html` - User preferences
- `settings.html` - Account settings

#### Authentication (3 pages)
- `login.html` - Sign in page
- `signup.html` - Registration page
- `password-reset.html` - Password recovery

#### Utility (2 pages)
- `404.html` - Page not found error
- `500.html` - Server error page

## Design System

### Brand Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Liberation Blue | `#0066CC` | Primary brand color, links, CTAs |
| Foundation Navy | `#0D1B2A` | Headings, dark backgrounds |
| Transform Orange | `#EA580C` | Accents, important actions |
| Collaboration Teal | `#0891B2` | Secondary features |
| Innovation Indigo | `#4F46E5` | AI features |
| Progress Green | `#059669` | Success states |

### Typography

- **Primary Font:** Inter (Google Fonts)
- **Monospace Font:** JetBrains Mono (Google Fonts)
- **Base Size:** 16px (1rem)
- **Scale:** 1.25 ratio (Major Third)

### Spacing

- **Base Unit:** 4px
- **Scale:** 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px
- **CSS Variables:** `--space-1` through `--space-16`

### Icons

- **Library:** Lucide Icons (unpkg.com)
- **Style:** Outlined (stroke-based)
- **Sizes:** 16px, 20px, 24px, 32px, 48px

## Features Demonstrated

### Navigation
- ✅ Consistent sidebar navigation across all pages
- ✅ Top header with search, notifications, and user menu
- ✅ Breadcrumb navigation on content pages
- ✅ Active state indicators
- ✅ Hover and focus states

### Components
- ✅ Cards with hover effects
- ✅ Data tables with sorting headers
- ✅ Forms with validation states
- ✅ Buttons (primary, secondary, icon)
- ✅ Stats cards with trend indicators
- ✅ Activity/timeline lists
- ✅ Multi-step wizard (product creation)
- ✅ Modals and overlays (AI Assistant)
- ✅ Alerts and notifications
- ✅ User avatars and badges

### User Flows
- ✅ Product creation journey (multi-step)
- ✅ Product management workflow
- ✅ Coverage configuration flow
- ✅ Analytics and reporting
- ✅ Compliance and audit trail
- ✅ Team collaboration
- ✅ User authentication

### AI Integration
- ✅ AI Assistant button (global access)
- ✅ AI-powered insights on dashboard
- ✅ Smart suggestions in forms
- ✅ AI innovation indicators (Indigo color)

### Accessibility
- ✅ Semantic HTML5 structure
- ✅ ARIA labels and roles
- ✅ Focus indicators (keyboard navigation)
- ✅ Color contrast compliance (WCAG AA)
- ✅ Icon + text labels
- ✅ Descriptive link text

### Responsive Considerations
- ✅ Flexible grid layouts
- ✅ Responsive spacing
- ✅ Mobile-friendly navigation patterns
- ✅ Touch-target sizing
- ✅ Scalable typography

## Technical Details

### Dependencies

- **Fonts:** Google Fonts (Inter, JetBrains Mono)
- **Icons:** Lucide Icons (CDN)
- **CSS:** Inline styles using CSS custom properties
- **JavaScript:** Minimal - only for icon initialization

### Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

### File Structure

```
ux/
├── README.md                      # This file
├── ux-plan.md                     # UX planning document
├── navigation-map.md              # Navigation structure
│
├── home.html                      # Landing/overview
├── dashboard.html                 # Main workspace
├── analytics.html                 # Analytics view
│
├── manage-products.html           # Product catalog
├── create-product.html            # Create product wizard
├── product-details.html           # Product details
├── edit-product.html              # Edit product
├── product-versions.html          # Version history
│
├── view-coverages.html            # View coverages
├── edit-coverages.html            # Edit coverages
│
├── pricing-configuration.html     # Pricing setup
├── underwriting-rules.html        # Underwriting rules
│
├── audit-trail.html               # Audit log
├── document-management.html       # Documents
│
├── team-activity.html             # Team activity
├── notifications.html             # Notifications
│
├── profile.html                   # User profile
├── preferences.html               # Preferences
├── settings.html                  # Settings
│
├── login.html                     # Sign in
├── signup.html                    # Registration
├── password-reset.html            # Password reset
│
├── 404.html                       # Not found error
└── 500.html                       # Server error
```

## Usage Guidelines

### For Designers

1. **Review the Design System:** Start with `ux-plan.md` to understand design tokens
2. **Explore Components:** View different pages to see component variations
3. **Study Flows:** Follow the user journeys documented in `navigation-map.md`
4. **Iterate:** These are mockups - use them as a foundation for refinement

### For Developers

1. **Extract Patterns:** Reuse the component HTML structures
2. **Use Tokens:** Implement the CSS custom properties in your system
3. **Follow Navigation:** Implement routing based on `navigation-map.md`
4. **Maintain Consistency:** Keep the design system intact across implementations

### For Stakeholders

1. **Experience the Flow:** Click through the pages to understand user journeys
2. **Provide Feedback:** Focus on functionality, not pixel-perfect design
3. **Identify Gaps:** Note any missing features or unclear workflows
4. **Validate Business Logic:** Ensure product workflows match business requirements

## Key User Journeys

### 1. Product Creation
```
Home → Dashboard → Create Product (4 steps) → Product Details
```

### 2. Product Management
```
Dashboard → Manage Products → Product Details → Edit Product → Save
```

### 3. Analytics Review
```
Dashboard → Analytics → Filter by Product → View Insights
```

### 4. Compliance Audit
```
Dashboard → Audit Trail → Filter → View Details → Export
```

### 5. Team Collaboration
```
Dashboard → Team Activity → View Updates → Notifications
```

## Design Principles

These mockups embody OpenLife's core principles:

1. **Clarity First** - Every interface is clean and easy to understand
2. **Confident Design** - Professional aesthetics that inspire trust
3. **Collaborative Spirit** - Features that enable teamwork
4. **AI-Forward** - Natural integration of AI capabilities
5. **Open & Transparent** - Clear visibility into all operations

## Brand Alignment

✅ **Liberator Archetype:** Empowering users with control and transparency  
✅ **Voice:** Confident, clear, collaborative, technically credible  
✅ **Values:** Openness, collaboration, innovation, fairness, empowerment  
✅ **Visual Language:** Liberation Blue, generous spacing, rounded corners  

## Next Steps

### For Development
1. Convert mockups to React/Vue/Angular components
2. Implement backend API integration
3. Add real-time data updates
4. Implement full authentication flow
5. Add loading states and error handling
6. Implement search functionality
7. Add data visualization (charts)
8. Implement file upload for documents
9. Add AI Assistant integration
10. Build responsive layouts

### For Testing
1. Usability testing with target users (CxOs)
2. Accessibility audit (WCAG 2.1 AA compliance)
3. Cross-browser testing
4. Mobile device testing
5. Performance optimization
6. SEO optimization (for public pages)

### For Iteration
1. Gather user feedback
2. Refine based on real data patterns
3. Add additional features as needed
4. Enhance AI integration points
5. Expand analytics capabilities

## Feedback & Iteration

These mockups are living documents. As you review them:

- **Note what works well** - Patterns to keep and expand
- **Identify improvements** - Areas that need refinement
- **Suggest additions** - Missing features or workflows
- **Question assumptions** - Challenge design decisions

## Credits

**Created:** 2025-12-26  
**Version:** 1.0  
**Design System:** OpenLife Brand Elements  
**Brand Strategy:** OpenLife Brand Strategy  

## Support

For questions or feedback about these mockups:

1. Review the documentation files first
2. Check the navigation map for page relationships
3. Examine the UX plan for detailed specifications
4. Provide structured feedback on specific pages or flows

---

**Remember:** These mockups demonstrate the vision for OpenLife. They should inspire and guide development, not constrain it. As you learn from users and iterate, the design will evolve. The goal is to empower insurers to own their technology destiny through clear, confident, and collaborative design.

**Collaborate. Innovate. Transform.**
