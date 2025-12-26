# Agents

## Brand Strategist Agent
Brand Strategist - creates the voice, story, and positioning

```
/nexus-meta-prompt-generator
Expert brand strategist that assists the user with creating the voice, story, and positioning for the brand. The agent creates a markdown formatted document with the strategy for the brand. The strategy output follows a template that follows industry best practices but is lightweight. The output is saved to /docs/brand/brand-strategy.md
```

### Brand Strategist Agent Usage
```
/brand-strategist create a new brand concept that is modeled after Atlassian, harness.io

company details:
OpenLife
*Collaborate. Innovate. Transform.*

## Transforming Life Insurance with Open Collaboration and AI
OpenLife is a cutting-edge, **community-driven** life insurance Policy Administration System (PAS) that fundamentally reimagines life insurance technology. Unlike proprietary systems that lock insurers into vendor dependencies, OpenLife is **source-available** with **fair use licensing** offering royalty-free rights to use, modify, and distribute for internal applications while protecting against resale as competing managed services.

### Differentiating Features

**Composable & Pluggable Architecture**
- **AI and API-First Design**: Foundational platform with policy administration at the core, designed for intelligent automation
- **Modular Components**: Mix and match capabilities; easily integrate, extend, or swap components without system disruption
- **Pluggable Interfaces**: Add custom business logic, AI services, blockchain, and third-party integrations without modifying core platform code
- **Standardized Integration Points**: Seamlessly incorporate marketing automation, external data providers, and emerging technologies

**Collaborative Ecosystem**
- **Community-Driven Development**: Platform designed, developed, and supported by a collaborative community
- **Network Effect Value**: Each contribution benefits all participants; shared ownership amplifies ecosystem value
- **Marketplace for Innovation**: Hub for specialized third-party services and integrations
- **Fair Compensation**: Contributors benefit from collective innovation with sustainable economics

**Open & Transparent**
- **Full Source Code Access**: Complete auditability and transparency for security and compliance verification
- **No Vendor Lock-In**: Architectural flexibility to customize and integrate without dependency constraints
- **Fair Use Licensed**: Royalty-free, permissive rights for internal use with ecosystem protection

### 🎯 Strategic Benefits

Beyond quantifiable returns, the OpenLife ecosystem delivers transformative advantages:

- **AI-Powered Innovation**: Pluggable AI integration across workflows enables intelligent automation, predictive analytics, and conversational interfaces
- **Ecosystem Network Effects**: Each contribution amplifies value for all participants; community-wide enhancements benefit everyone through fair licensing
- **Solution Marketplace**: Growing array of specialized third-party services through standardized APIs and pluggable interfaces
- **Collaborative Development**: Tap into collective problem-solving while maintaining influence over standards and priorities
- **Talent Acquisition**: Attract top technology talent eager to work with cutting-edge, fair-code technologies
- **Strategic Agility**: Rapidly adapt by swapping components or integrating new capabilities without platform-wide changes
- **Organizational Transformation**: Enable frontier firm evolution with composable architecture supporting human-AI collaboration
- **Resource Optimization**: Redirect resources from vendor management to developing distinctive customer experiences
- **True Flexibility**: No vendor lock-in; customize, extend, or replace any component while preserving your investment
```

Follow-up response:
```
1. AI changed the software landscape and is unlocking opportunties for insurers and technology companies to take a different approach to their technology ecosystems.
2. OpenLife is community- and collaboration focused, modern, AI forward, open, transformational. The tagline 'Collaborate. Innovate. Transform' says it all.
3. In control and Innovative.
4. competitors: Verisk Fast, Accenture Life Insurance Platform (ALIP). They can't claim to have an open, extensible platform.
5. CxOs wanting to break free of vendor lock in and legacy technology.
6. The sustainable licensing and fair use model is a core differentiator.

the assumptions are good.
```

## Brand Designer Agent
Brand Designer - designs the brand elements (content, colors, typography, iconography, imagery, illustrations, logos, spacing, grid, elevation, border, accessibility).

```
/nexus-meta-prompt-generator
Expert brand conceptualizer and designer that designs the core brand elements based on the brand strategy in /docs/brand/brand-strategy.md. If the brand-strategy.md does not exist, then tell the user to create it first. If it exists, use it to create the following brand elements one at a time, in order. The agent create markdown formatted documents for each of the elements for the brand. The output will use standard templates that follow industry best practices but are lightweight. The output is saved to /docs/brand/. A master markdown document with links to the elements is saved to /docs/brand/brand-elements.md.

The brand elements to create are:
- **Content** (brand-elements-content.md) - Clear, concise, and conversational language to guide users
    - **Language and grammar** (brand-elements-content-language-and-grammar.md) - Conventions to make writing clear, consistent, and localizable.
    - **Voice and tone** (brand-elements-content-voice-and-tone.md) Content that aligns with the brand voice and tone.
    - **Date and time** (brand-elements-content-date-and-time.md) Date and time presented in a clear and consistent way for global customers.
    - **Designing messages** (brand-elements-content-designing-messages.md) Write and format success and error messages, and other types of alerts. Types of messages include:
        - Information message — provides additional information to motivate users.
        - Error message — alerts users of a problem that has occurred and informs them what to do next.
        - Success message — celebrates success along with the users of the apps.
        - Warning message — gives advanced notice of a potential change that may result in loss of data or an error state.
        - Feature discovery — lets users know about a new feature.
- **Colors** (brand-elements-colors.md) - Distinguishes brand and reinforces consistent experiences across apps (color palette)
- **Typography** (brand-elements-typography.md) - System of fonts and text styles
- **Iconography** (brand-elements-iconography.md) - Visual representations of commands and common actions
- **Imagery** (brand-elements-imagery.md) - Photography style that reflects brand personality
- **Illustrations** (brand-elements-illustrations.md) - Help convey complex ideas in a simple way
- **Logos** (brand-elements-logos.md) - Visual representation of the brand and/or app
- **Spacing** (brand-elements-spacing.md) - System that simplifies the creation of page layouts and UI. Including layout primitives and grids to create consistent structure
- **Grid** (brand-elements-grid.md) - Used to position content and create consistent page layouts
- **Elevation** (brand-elements-elevation.md) - Layered surfaces that form the foundation of UI
- **Border** (brand-elements-border.md) - Visual styling for edges and boundaries
- **Accessibility** (brand-elements-accessibility.md) - Enable everyone to interact with, understand, and navigate apps
```

### Brand Designer Agent Usage
```
/brand-asset-designer 
```

## UX Designer Agent
UX Designer - creates comprehensive application mockups with all views, pages, and components for complete user experience design.

```
/nexus-meta-prompt-generator
Expert UX designer that creates comprehensive application templates and mockups for all different views/pages in the application. The agent works from the brand strategy in /docs/brand/brand-strategy.md and the brand elements in /docs/brand/brand-elements.md to create interactive HTML mockups. The agent first creates a UX plan document outlining the complete application structure, information architecture, and all views to be created. Then creates each mockup view/page one at a time, ensuring navigation and other links properly link between the views/pages.

The mockups include examples of components like:
- Navigation (main navigation, sidebar navigation, breadcrumbs, footer)
- User interface (avatar, preferences, settings, notifications, alerts, tasks)
- Forms and inputs (text fields, select boxes, checkboxes, radio buttons)
- Data display (tables, cards, lists, statistics, charts)
- Feedback (success messages, error messages, warnings, info alerts, toasts)
- Interactive elements (buttons, modals, dropdowns, accordions, tooltips)

All mockups use design tokens extracted from the brand elements (colors, typography, spacing, borders, elevation, grid) and are saved to /docs/brand-[brandName]/mock/ux/. The agent creates a UX plan first, then creates each view sequentially, ensuring consistent navigation and component usage across all views.
```

### UX Designer Agent Usage
```
/ux-designer create application mockups for a [application type] with [key features]
```

## Future (if needed)

### Brand Conceptualizer Agent
Brand Conceptualizer - creates the visual identity and mood board

### Brand Core Designer Agent
Brand Core Designer - Designs the core elements (Design Cores). These are the design decisions that will impact every component.

```
/nexus-meta-prompt-generator
Expert brand designer that designs and documents the core elements (Design Cores) for the brand - Cores are the design decisions that will impact every component. The design of the cores is based on the brand strategy in /docs/brand/brand-strategy.md and the brand assets in /docs/brand/brand-assets.md. The agent creates a markdown formatted document with the core elements for the brand. The output will use standard templates that follow industry best practices but are lightweight. The output is saved to /docs/brand/brand-cores.md. A output includes an index of the cores with links to the cores sections at the top of the document. Use the information in the brand design reference to help create the agent - /docs/brand/brand-cores.md
```

### Technology Component Architect - selects the technical components (ex. shadcn/ui, Radix UI)

Technology Component Designer - designs reusable building blocks (using the chosen technology components) that can be used to build the application UI. These are the components that will be used to build the application UI.
- forms, buttons, calendar, etc. 
- images, icons, logos, titles
- layout and structure
- loading - progress bar, spinner, etc.
- messaging - banner, flag, inline message, error message, modal dialog, etc.
- navigation - breadcrumbs, links, menu, navigation, pagination, side navigation, tabs
- overlays and layering
- primitives
- data display - avatar, badge, card, chip, divider, list, statistic, table, tooltip
- feedback - toast, popover, accordion, collapsible, hover card
- charts - bar chart, line chart, pie chart, etc.