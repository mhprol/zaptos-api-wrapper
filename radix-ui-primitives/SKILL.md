---
name: radix-ui-primitives
description: Knowledge base for Radix UI primitives. Use this skill when asked to build, implement, or style accessible React components using Radix UI, or when you need reference material for Radix component APIs and architecture.
license: MIT
metadata:
  framework: react
  target: web
  version: "1.0.0"
---

# Radix UI Primitives Skill

This skill serves as a comprehensive knowledge base for implementing React components using [Radix UI Primitives](https://www.radix-ui.com/primitives). Radix Primitives is an unstyled, accessible component library for building high-quality design systems and web apps in React.

When utilizing this skill, follow the **Progressive Disclosure** principle: read the specific reference files relevant to the current component you are implementing rather than trying to memorize everything at once.

## How to use this skill

1. **Understand the Basics**: If you are new to Radix UI or need to setup the project, read the overview files.
2. **Review Guides**: If you need to understand how to style, animate, or compose components, refer to the guides.
3. **Implement Components**: When asked to implement a specific UI component (e.g., a Dropdown Menu or a Dialog), look up the specific component reference file first to understand its API, expected DOM structure, and accessibility features.

## Reference Index

All reference documentation has been mirrored directly from the Radix UI website. Access the relevant files using the paths below:

### Overview
- [Introduction](references/overview/introduction.md)
- [Getting Started](references/overview/getting-started.md)
- [Accessibility](references/overview/accessibility.md)
- [Releases](references/overview/releases.md)

### Guides
- [Styling](references/guides/styling.md)
- [Animation](references/guides/animation.md)
- [Composition](references/guides/composition.md)
- [Server-side Rendering](references/guides/server-side-rendering.md)

### Components
- [Accordion](references/components/accordion.md)
- [Alert Dialog](references/components/alert-dialog.md)
- [Aspect Ratio](references/components/aspect-ratio.md)
- [Avatar](references/components/avatar.md)
- [Checkbox](references/components/checkbox.md)
- [Collapsible](references/components/collapsible.md)
- [Context Menu](references/components/context-menu.md)
- [Dialog](references/components/dialog.md)
- [Dropdown Menu](references/components/dropdown-menu.md)
- [Form](references/components/form.md)
- [Hover Card](references/components/hover-card.md)
- [Label](references/components/label.md)
- [Menubar](references/components/menubar.md)
- [Navigation Menu](references/components/navigation-menu.md)
- [Popover](references/components/popover.md)
- [Progress](references/components/progress.md)
- [Radio Group](references/components/radio-group.md)
- [Scroll Area](references/components/scroll-area.md)
- [Select](references/components/select.md)
- [Separator](references/components/separator.md)
- [Slider](references/components/slider.md)
- [Switch](references/components/switch.md)
- [Tabs](references/components/tabs.md)
- [Toast](references/components/toast.md)
- [Toggle Group](references/components/toggle-group.md)
- [Toggle](references/components/toggle.md)
- [Toolbar](references/components/toolbar.md)
- [Tooltip](references/components/tooltip.md)

## Implementation Advice

* **Composition**: Radix heavily uses the `asChild` prop to delegate rendering to your own components. Pay close attention to this pattern in the `composition.md` guide.
* **Styling**: Radix primitives are completely unstyled. You are expected to provide your own CSS classes (e.g., using Tailwind CSS or standard CSS modules). Use the `data-*` attributes (like `data-state="open"`) to style different states of the components.
* **Accessibility**: Radix handles the complex ARIA attributes, keyboard navigation, and focus management automatically. Do not try to override these unless absolutely necessary.
