# iFoundry Media UX Plan

> Marketing website with blog for iFoundry Media — a technology foundry that incubates, builds, and scales digital products.

## Application Overview

### Type
Corporate marketing website with integrated blog for iFoundry Media. The site communicates the brand's positioning as a technology foundry — a partner that incubates, builds, and scales digital products — to founders, product leaders, and enterprise decision-makers.

### Goals
1. Communicate iFoundry's unique value proposition: invested partnership, not outsourced development
2. Showcase the portfolio of products built, incubated, and scaled
3. Establish technical credibility through blog content and case studies
4. Convert visitors into discovery call conversations
5. Reinforce the "Forged to perform." brand identity at every touchpoint

### Target Users
- Founders with product ideas seeking expert engineering partners
- CTOs and product leaders evaluating technology partners for new builds or modernization
- Entrepreneurs exploring incubation partnerships
- General visitors discovering iFoundry through search, referral, or content

## Information Architecture

```
Home (/)
├── About (/about)
├── Services (/services)
├── Work (/work)
│   └── [Case Study] (/work/project-name) — future expansion
├── Blog (/blog)
│   └── [Post] (/blog/post-slug)
└── Contact (/contact)
```

## Navigation Structure

### Primary Navigation (Header)
- Logo (links to Home)
- About
- Services
- Work
- Blog
- Contact (CTA button style)

### Footer Navigation
- Column 1: Company — About, Services, Work, Blog
- Column 2: Connect — Contact, LinkedIn, GitHub
- Column 3: Legal — Privacy Policy, Terms of Service
- Tagline and copyright

## Pages to Create

| # | File | Page | Purpose |
|---|------|------|---------|
| 1 | `index.html` | Home | Hero, value proposition, services overview, portfolio highlights, CTA |
| 2 | `about.html` | About | Story, mission, values, team approach, partnership model |
| 3 | `services.html` | Services | Incubation, product engineering, modernization, AI/data — detailed capabilities |
| 4 | `work.html` | Work / Portfolio | Showcase of products built, incubated, and scaled |
| 5 | `blog.html` | Blog | Article listing with categories and search |
| 6 | `blog-post.html` | Blog Post | Individual article template with author, date, related posts |
| 7 | `contact.html` | Contact | Discovery call booking, contact form, direct outreach |
| 8 | `404.html` | Not Found | Branded 404 error page |
| 9 | `500.html` | Server Error | Branded 500 error page |

## Component Inventory

### Global Components
- **Header/Navigation:** Fixed top nav with logo, links, CTA button
- **Footer:** Multi-column footer with links, social, tagline
- **CTA Section:** Reusable call-to-action block ("Let's build something extraordinary")

### Home Page Components
- Hero section with headline, subline, and dual CTAs
- Services overview cards (3-4 cards)
- Portfolio highlight grid (2-3 featured projects)
- Stats/metrics bar (projects delivered, technologies, partnerships)
- Testimonial/quote block
- Blog preview (2-3 recent posts)
- Final CTA section

### About Page Components
- Mission/vision hero
- Values grid
- Partnership model explanation
- Team approach section
- Origin story narrative

### Services Page Components
- Services hero
- Service detail cards with icons
- Process/methodology section
- Technology stack showcase
- CTA section

### Work Page Components
- Portfolio hero
- Project cards with images, tags, descriptions
- Filter by category (Incubated, Client, Modernization)

### Blog Components
- Blog listing with card layout
- Category filter/tags
- Search bar
- Pagination
- Blog post with rich typography, author info, share links, related posts

### Contact Page Components
- Contact form (name, email, company, message, project type)
- Direct contact information
- Discovery call CTA

### Error Pages
- Branded illustration/message
- Navigation back to home

## User Flows

### Primary Flow: Visitor to Discovery Call
1. Land on Home → Read hero and value proposition
2. Explore Services → Understand capabilities
3. View Work → See portfolio proof
4. Navigate to Contact → Fill form or book call

### Secondary Flow: Content Discovery
1. Land on Blog (via search/social) → Read article
2. Explore related posts → Build trust through expertise
3. Navigate to Services or About → Learn about iFoundry
4. Convert via Contact

## Design Token Summary

| Token Category | Key Values |
|----------------|-----------|
| Primary Colors | Forge Blue `#1D4ED8`, Ignite Orange `#EA580C`, Iron Slate `#0F172A` |
| Typography | Space Grotesk (300-700), JetBrains Mono (code) |
| Spacing | 4px base unit, generous density for marketing |
| Border Radius | 6px default, 12px feature cards |
| Elevation | 5-level shadow system, Iron Slate base |
| Grid | 12-column, 1280px max container |
| Icons | Lucide, 1.5px stroke |
