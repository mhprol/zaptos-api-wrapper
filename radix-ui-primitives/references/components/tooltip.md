# Tooltip

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

## Features

- Provider to control display delay globally.

- Opens when the trigger is focused or hovered.

- Closes when the trigger is activated or when pressing escape.

- Supports custom timings.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-tooltip
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Tooltip } from "radix-ui";

export default () => (
  <Tooltip.Provider>
    <Tooltip.Root>
      <Tooltip.Trigger />

      <Tooltip.Portal>
        <Tooltip.Content>
          <Tooltip.Arrow />
        </Tooltip.Content>
      </Tooltip.Portal>
    </Tooltip.Root>
  </Tooltip.Provider>
);
```

## [API Reference](#api-reference)

### [Provider](#provider)

Wraps your app to provide global functionality to your tooltips.

| Prop                      | Type      | Default          |
| ------------------------- | --------- | ---------------- |
| `delayDuration`           | `number`  | `700`            |
| `skipDelayDuration`       | `number`  | `300`            |
| `disableHoverableContent` | `boolean` | No default value |

### [Root](#root)

Contains all the parts of a tooltip.

| Prop                      | Type       | Default          |
| ------------------------- | ---------- | ---------------- |
| `defaultOpen`             | `boolean`  | No default value |
| `open`                    | `boolean`  | No default value |
| `onOpenChange`            | `function` | No default value |
| `delayDuration`           | `number`   | `700`            |
| `disableHoverableContent` | `boolean`  | No default value |

### [Trigger](#trigger)

The button that toggles the tooltip. By default, the `Tooltip.Content` will position itself against the trigger.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute | Values                                         |
| -------------- | ---------------------------------------------- |
| `[data-state]` | `"closed" \| "delayed-open" \| "instant-open"` |

### [Portal](#portal)

When used, portals the content part into the `body`.

| Prop         | Type          | Default          |
| ------------ | ------------- | ---------------- |
| `forceMount` | `boolean`     | No default value |
| `container`  | `HTMLElement` | `document.body`  |

### [Content](#content)

The component that pops out when the tooltip is open.

| Prop                   | Type                | Default          |
| ---------------------- | ------------------- | ---------------- |
| `asChild`              | `boolean`           | `false`          |
| `aria-label`           | `string`            | No default value |
| `onEscapeKeyDown`      | `function`          | No default value |
| `onPointerDownOutside` | `function`          | No default value |
| `forceMount`           | `boolean`           | No default value |
| `side`                 | `enum`              | `"top"`          |
| `sideOffset`           | `number`            | `0`              |
| `align`                | `enum`              | `"center"`       |
| `alignOffset`          | `number`            | `0`              |
| `avoidCollisions`      | `boolean`           | `true`           |
| `collisionBoundary`    | `Boundary`          | `[]`             |
| `collisionPadding`     | `number \| Padding` | `0`              |
| `arrowPadding`         | `number`            | `0`              |
| `sticky`               | `enum`              | `"partial"`      |
| `hideWhenDetached`     | `boolean`           | `false`          |

| Data attribute | Values                                         |
| -------------- | ---------------------------------------------- |
| `[data-state]` | `"closed" \| "delayed-open" \| "instant-open"` |
| `[data-side]`  | `"left" \| "right" \| "bottom" \| "top"`       |
| `[data-align]` | `"start" \| "end" \| "center"`                 |

| CSS Variable                               | Description                                                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------- |
| `--radix-tooltip-content-transform-origin` | The `transform-origin` computed from the content and arrow positions/offsets |
| `--radix-tooltip-content-available-width`  | The remaining width between the trigger and the boundary edge                |
| `--radix-tooltip-content-available-height` | The remaining height between the trigger and the boundary edge               |
| `--radix-tooltip-trigger-width`            | The width of the trigger                                                     |
| `--radix-tooltip-trigger-height`           | The height of the trigger                                                    |

### [Arrow](#arrow)

An optional arrow element to render alongside the tooltip. This can be used to help visually link the trigger with the `Tooltip.Content`. Must be rendered inside `Tooltip.Content`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |
| `width`   | `number`  | `10`    |
| `height`  | `number`  | `5`     |

## [Examples](#examples)

### [Configure globally](#configure-globally)

Use the `Provider` to control `delayDuration` and `skipDelayDuration` globally.

```jsx
import { Tooltip } from "radix-ui";

export default () => (
  <Tooltip.Provider delayDuration={800} skipDelayDuration={500}>
    <Tooltip.Root>
      <Tooltip.Trigger>…</Tooltip.Trigger>

      <Tooltip.Content>…</Tooltip.Content>
    </Tooltip.Root>

    <Tooltip.Root>
      <Tooltip.Trigger>…</Tooltip.Trigger>

      <Tooltip.Content>…</Tooltip.Content>
    </Tooltip.Root>
  </Tooltip.Provider>
);
```

### [Show instantly](#show-instantly)

Use the `delayDuration` prop to control the time it takes for the tooltip to open.

```jsx
import { Tooltip } from "radix-ui";

export default () => (
  <Tooltip.Root delayDuration={0}>
    <Tooltip.Trigger>…</Tooltip.Trigger>

    <Tooltip.Content>…</Tooltip.Content>
  </Tooltip.Root>
);
```

### [Constrain the content size](#constrain-the-content-size)

You may want to constrain the width of the content so that it matches the trigger width. You may also want to constrain its height to not exceed the viewport.

We expose several CSS custom properties such as `--radix-tooltip-trigger-width` and `--radix-tooltip-content-available-height` to support this. Use them to constrain the content dimensions.

```jsx
// index.jsx

import { Tooltip } from "radix-ui";

import "./styles.css";

export default () => (
  <Tooltip.Root>
    <Tooltip.Trigger>…</Tooltip.Trigger>

    <Tooltip.Portal>
      <Tooltip.Content className="TooltipContent" sideOffset={5}>
        …
      </Tooltip.Content>
    </Tooltip.Portal>
  </Tooltip.Root>
);
```

```css
/* styles.css */

.TooltipContent {
  width: var(--radix-tooltip-trigger-width);

  max-height: var(--radix-tooltip-content-available-height);
}
```

### [Origin-aware animations](#origin-aware-animations)

We expose a CSS custom property `--radix-tooltip-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```jsx
// index.jsx

import { Tooltip } from "radix-ui";

import "./styles.css";

export default () => (
  <Tooltip.Root>
    <Tooltip.Trigger>…</Tooltip.Trigger>

    <Tooltip.Content className="TooltipContent">…</Tooltip.Content>
  </Tooltip.Root>
);
```

```css
/* styles.css */

.TooltipContent {
  transform-origin: var(--radix-tooltip-content-transform-origin);

  animation: scaleIn 0.5s ease-out;
}

@keyframes scaleIn {
  from {
    opacity: 0;

    transform: scale(0);
  }

  to {
    opacity: 1;

    transform: scale(1);
  }
}
```

### [Collision-aware animations](#collision-aware-animations)

We expose `data-side` and `data-align` attributes. Their values will change at runtime to reflect collisions. Use them to create collision and direction-aware animations.

```jsx
// index.jsx

import { Tooltip } from "radix-ui";

import "./styles.css";

export default () => (
  <Tooltip.Root>
    <Tooltip.Trigger>…</Tooltip.Trigger>

    <Tooltip.Content className="TooltipContent">…</Tooltip.Content>
  </Tooltip.Root>
);
```

```css
/* styles.css */

.TooltipContent {
  animation-duration: 0.6s;

  animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

.TooltipContent[data-side="top"] {
  animation-name: slideUp;
}

.TooltipContent[data-side="bottom"] {
  animation-name: slideDown;
}

@keyframes slideDown {
  from {
    opacity: 0;

    transform: translateY(-10px);
  }

  to {
    opacity: 1;

    transform: translateY(0);
  }
}

@keyframes slideUp {
  from {
    opacity: 0;

    transform: translateY(10px);
  }

  to {
    opacity: 1;

    transform: translateY(0);
  }
}
```

## [Accessibility](#accessibility)

### [Keyboard Interactions](#keyboard-interactions)

| Key      | Description                                |
| -------- | ------------------------------------------ |
| `Tab`    | Opens/closes the tooltip without delay.    |
| `Space`  | If open, closes the tooltip without delay. |
| `Enter`  | If open, closes the tooltip without delay. |
| `Escape` | If open, closes the tooltip without delay. |

## [Custom APIs](#custom-apis)

Create your own API by abstracting the primitive parts into your own component.

### [Abstract parts and introduce a content prop](#abstract-parts-and-introduce-a-content-prop)

This example abstracts all of the `Tooltip` parts and introduces a new `content` prop.

#### Usage

```jsx
import { Tooltip } from "./your-tooltip";

export default () => (
  <Tooltip content="Tooltip content">
    <button>Tooltip trigger</button>
  </Tooltip>
);
```

#### Implementation

Use the [`asChild` prop](/primitives/docs/guides/composition) to convert the trigger part into a slottable area. It will replace the trigger with the child that gets passed to it.

```jsx
// your-tooltip.jsx

import * as React from "react";

import { Tooltip as TooltipPrimitive } from "radix-ui";

export function Tooltip({ children, content, open, defaultOpen, onOpenChange, ...props }) {
  return (
    <TooltipPrimitive.Root open={open} defaultOpen={defaultOpen} onOpenChange={onOpenChange}>
      <TooltipPrimitive.Trigger asChild>{children}</TooltipPrimitive.Trigger>

      <TooltipPrimitive.Content side="top" align="center" {...props}>
        {content}

        <TooltipPrimitive.Arrow width={11} height={5} />
      </TooltipPrimitive.Content>
    </TooltipPrimitive.Root>
  );
}
```
