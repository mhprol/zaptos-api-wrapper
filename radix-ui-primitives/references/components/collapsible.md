# Collapsible

An interactive component which expands/collapses a panel.

## Features

- Full keyboard navigation.

- Can be controlled or uncontrolled.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-collapsible
```

## [Anatomy](#anatomy)

Import the components and piece the parts together.

```jsx
import { Collapsible } from "radix-ui";

export default () => (
  <Collapsible.Root>
    <Collapsible.Trigger />

    <Collapsible.Content />
  </Collapsible.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a collapsible.

| Prop           | Type       | Default          |
| -------------- | ---------- | ---------------- |
| `asChild`      | `boolean`  | `false`          |
| `defaultOpen`  | `boolean`  | No default value |
| `open`         | `boolean`  | No default value |
| `onOpenChange` | `function` | No default value |
| `disabled`     | `boolean`  | No default value |

| Data attribute    | Values                |
| ----------------- | --------------------- |
| `[data-state]`    | `"open" \| "closed"`  |
| `[data-disabled]` | Present when disabled |

### [Trigger](#trigger)

The button that toggles the collapsible.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute    | Values                |
| ----------------- | --------------------- |
| `[data-state]`    | `"open" \| "closed"`  |
| `[data-disabled]` | Present when disabled |

### [Content](#content)

The component that contains the collapsible content.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute    | Values                |
| ----------------- | --------------------- |
| `[data-state]`    | `"open" \| "closed"`  |
| `[data-disabled]` | Present when disabled |

| CSS Variable                         | Description                                    |
| ------------------------------------ | ---------------------------------------------- |
| `--radix-collapsible-content-width`  | The width of the content when it opens/closes  |
| `--radix-collapsible-content-height` | The height of the content when it opens/closes |

## [Examples](#examples)

### [Animating content size](#animating-content-size)

Use the `--radix-collapsible-content-width` and/or `--radix-collapsible-content-height` CSS variables to animate the size of the content when it opens/closes. Here's a demo:

```jsx
// index.jsx

import { Collapsible } from "radix-ui";

import "./styles.css";

export default () => (
  <Collapsible.Root>
    <Collapsible.Trigger>…</Collapsible.Trigger>

    <Collapsible.Content className="CollapsibleContent">…</Collapsible.Content>
  </Collapsible.Root>
);
```

```css
/* styles.css */

.CollapsibleContent {
  overflow: hidden;
}

.CollapsibleContent[data-state="open"] {
  animation: slideDown 300ms ease-out;
}

.CollapsibleContent[data-state="closed"] {
  animation: slideUp 300ms ease-out;
}

@keyframes slideDown {
  from {
    height: 0;
  }

  to {
    height: var(--radix-collapsible-content-height);
  }
}

@keyframes slideUp {
  from {
    height: var(--radix-collapsible-content-height);
  }

  to {
    height: 0;
  }
}
```

## [Accessibility](#accessibility)

Adheres to the [Disclosure WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure).

### [Keyboard Interactions](#keyboard-interactions)

| Key     | Description                   |
| ------- | ----------------------------- |
| `Space` | Opens/closes the collapsible. |
| `Enter` | Opens/closes the collapsible. |
