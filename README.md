# OpenLife Brand Designer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](#)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](#)

Comprehensive brand strategy and design system for **OpenLife**, the community-driven life insurance policy administration platform. This repository contains brand positioning, design tokens, style guides, and interactive mockups.

## Table of Contents

- [About](#about)
- [What's Included](#whats-included)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Agents & Tools](#agents--tools)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

OpenLife is liberating the life insurance industry from vendor lock-in through an open, AI-powered platform where the entire industry collaborates to innovate. This brand designer project documents:

- **Brand Strategy:** Market positioning, values, target audience, and competitive differentiation
- **Design System:** Complete brand elements including colors, typography, spacing, elevation, and accessibility guidelines
- **Design Agents:** AI-powered agents that create and manage brand content
- **Interactive Mockups:** HTML prototypes demonstrating the design system in action

**Tagline:** Collaborate. Innovate. Transform.

## What's Included

### 📋 Brand Documentation
- `docs/brand/brand-strategy.md` - Strategic positioning and brand foundation
- `docs/brand/brand-elements.md` - Master index of all brand elements
- `docs/brand/brand-elements-*.md` - 17 detailed brand element guides covering:
  - **Content:** Language, voice, tone, messaging guidelines
  - **Visual Identity:** Colors, typography, iconography, imagery, illustrations, logos
  - **Layout:** Spacing, grid, elevation, borders
  - **Foundation:** Accessibility standards

### 🤖 Design Agents
- `.github/agents/brand-strategist.agent.md` - Creates brand strategy documents
- `.github/agents/brand-element-designer.agent.md` - Generates design system elements

### 🎨 Interactive Mockups
- `docs/brand/mock/dashboard-mockup.html` - Application dashboard UI
- `docs/brand/mock/product-management-mockup.html` - Product management system
- `docs/brand/mock/website-mockup.html` - Marketing website homepage

### 📚 Supporting Materials
- `design-system-reference/` - Design system reference documents
- `.github/copilot-instructions.md` - Development environment guidelines

## Quick Start

### View the Brand System

1. **Read the Strategy:**
   ```bash
   cat docs/brand/brand-strategy.md
   ```

2. **Explore Design Elements:**
   - Open `docs/brand/brand-elements.md` for a complete index
   - Review individual element guides in `docs/brand/brand-elements-*.md`

3. **View Interactive Mockups:**
   - Open any HTML file in `docs/brand/mock/` in your web browser:
     - `dashboard-mockup.html` - Admin dashboard
     - `product-management-mockup.html` - Product catalog manager
     - `website-mockup.html` - Public marketing site

### Run Design Agents

To use the brand design agents, you'll need VS Code with GitHub Copilot enabled.

**Create Brand Strategy:**
```
/brand-strategist create a new brand concept for [your company]
```

**Generate Design Elements:**
```
/brand-element-designer create design system elements based on brand-strategy.md
```

For detailed instructions, see `.github/copilot-instructions.md`.

## Project Structure

```
forge-agent-brand-designer/
├── .github/
│   ├── agents/              # AI agent definitions
│   ├── prompts/             # Agent prompt templates
│   └── copilot-instructions.md
├── docs/
│   └── brand/
│       ├── brand-strategy.md
│       ├── brand-elements.md (master index)
│       ├── brand-elements-*.md (17 element guides)
│       └── mock/
│           ├── dashboard-mockup.html
│           ├── product-management-mockup.html
│           └── website-mockup.html
├── design-system-reference/
├── agent-design.md          # Agent specifications
└── README.md               # This file
```

## Agents & Tools

This project uses two primary agents:

### Brand Strategist Agent
Crafts brand positioning, messaging, and strategic direction.
- **Input:** Company details and positioning requirements
- **Output:** `docs/brand/brand-strategy.md`
- **Trigger:** `/brand-strategist [instructions]`

### Brand Element Designer Agent
Generates complete design systems from brand strategy.
- **Input:** `docs/brand/brand-strategy.md`
- **Output:** 17 brand element documents + `docs/brand/brand-elements.md`
- **Trigger:** `/brand-element-designer [instructions]`

For more details, see `agent-design.md`.

## Usage

### For Brand Teams

1. **Review the brand strategy** in `docs/brand/brand-strategy.md`
2. **Reference design tokens** in individual element guides (e.g., `brand-elements-colors.md`)
3. **Implement CSS tokens** from the design documents in your applications
4. **Check accessibility guidelines** in `brand-elements-accessibility.md`

### For Developers

1. **Extract CSS tokens** from the design guides
2. **Use Lucide icons** as specified in `brand-elements-iconography.md`
3. **Apply spacing scale** from `brand-elements-spacing.md`
4. **Follow the grid system** in `brand-elements-grid.md`
5. **Review mockups** for implementation patterns

### For Designers

1. **Study the brand strategy** to understand positioning and values
2. **Reference the design system** for consistency across projects
3. **Use the mockups** as starting points for new designs
4. **Generate new elements** using the Brand Element Designer agent

## Contributing

We welcome contributions to the OpenLife brand system!

### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/forge-agent-brand-designer.git
   cd forge-agent-brand-designer
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-update
   ```

3. **Make your changes**
   - Update brand documents
   - Refine design system elements
   - Improve mockups or guides

4. **Commit with clear messages**
   ```bash
   git commit -m "Update: [Description of changes]"
   ```

5. **Push to your fork and create a pull request**
   ```bash
   git push origin feature/your-update
   ```

### Guidelines

- Maintain consistency with the OpenLife brand values: Openness, Collaboration, Innovation, Fairness, Empowerment
- Follow the document templates already established
- Update `docs/brand/brand-elements.md` if adding new elements
- Test HTML mockups in modern browsers
- Ensure accessibility standards are met

## License

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

---

**OpenLife:** Liberate your technology. Collaborate with your industry. Transform life insurance.

For more information, visit the [OpenLife website](https://openlife.io) or read the [brand strategy](docs/brand/brand-strategy.md).
