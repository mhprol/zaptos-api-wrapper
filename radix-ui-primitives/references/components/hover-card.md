# Hover Card

For sighted users to preview content available behind a link.

## Features

- Can be controlled or uncontrolled.

- Customize side, alignment, offsets, collision handling.

- Optionally render a pointing arrow.

- Supports custom open and close delays.

- Ignored by screen readers.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-hover-card
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { HoverCard } from "radix-ui";

export default () => (
  <HoverCard.Root>
    <HoverCard.Trigger />

    <HoverCard.Portal>
      <HoverCard.Content>
        <HoverCard.Arrow />
      </HoverCard.Content>
    </HoverCard.Portal>
  </HoverCard.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a hover card.

| Prop           | Type       | Default          |
| -------------- | ---------- | ---------------- |
| `defaultOpen`  | `boolean`  | No default value |
| `open`         | `boolean`  | No default value |
| `onOpenChange` | `function` | No default value |
| `openDelay`    | `number`   | `700`            |
| `closeDelay`   | `number`   | `300`            |

### [Trigger](#trigger)

The link that opens the hover card when hovered.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute | Values               |
| -------------- | -------------------- |
| `[data-state]` | `"open" \| "closed"` |

### [Portal](#portal)

When used, portals the content part into the `body`.

| Prop         | Type          | Default          |
| ------------ | ------------- | ---------------- |
| `forceMount` | `boolean`     | No default value |
| `container`  | `HTMLElement` | `document.body`  |

### [Content](#content)

The component that pops out when the hover card is open.

| Prop                | Type                | Default          |
| ------------------- | ------------------- | ---------------- |
| `asChild`           | `boolean`           | `false`          |
| `forceMount`        | `boolean`           | No default value |
| `side`              | `enum`              | `"bottom"`       |
| `sideOffset`        | `number`            | `0`              |
| `align`             | `enum`              | `"center"`       |
| `alignOffset`       | `number`            | `0`              |
| `avoidCollisions`   | `boolean`           | `true`           |
| `collisionBoundary` | `Boundary`          | `[]`             |
| `collisionPadding`  | `number \| Padding` | `0`              |
| `arrowPadding`      | `number`            | `0`              |
| `sticky`            | `enum`              | `"partial"`      |
| `hideWhenDetached`  | `boolean`           | `false`          |

| Data attribute | Values                                   |
| -------------- | ---------------------------------------- |
| `[data-state]` | `"open" \| "closed"`                     |
| `[data-side]`  | `"left" \| "right" \| "bottom" \| "top"` |
| `[data-align]` | `"start" \| "end" \| "center"`           |

| CSS Variable                                  | Description                                                                  |
| --------------------------------------------- | ---------------------------------------------------------------------------- |
| `--radix-hover-card-content-transform-origin` | The `transform-origin` computed from the content and arrow positions/offsets |
| `--radix-hover-card-content-available-width`  | The remaining width between the trigger and the boundary edge                |
| `--radix-hover-card-content-available-height` | The remaining height between the trigger and the boundary edge               |
| `--radix-hover-card-trigger-width`            | The width of the trigger                                                     |
| `--radix-hover-card-trigger-height`           | The height of the trigger                                                    |

### [Arrow](#arrow)

An optional arrow element to render alongside the hover card. This can be used to help visually link the trigger with the `HoverCard.Content`. Must be rendered inside `HoverCard.Content`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |
| `width`   | `number`  | `10`    |
| `height`  | `number`  | `5`     |

## [Examples](#examples)

### [Show instantly](#show-instantly)

Use the `openDelay` prop to control the time it takes for the hover card to open.

```jsx
import { HoverCard } from "radix-ui";

export default () => (
  <HoverCard.Root openDelay={0}>
    <HoverCard.Trigger>…</HoverCard.Trigger>

    <HoverCard.Content>…</HoverCard.Content>
  </HoverCard.Root>
);
```

### [Constrain the content size](#constrain-the-content-size)

You may want to constrain the width of the content so that it matches the trigger width. You may also want to constrain its height to not exceed the viewport.

We expose several CSS custom properties such as `--radix-hover-card-trigger-width` and `--radix-hover-card-content-available-height` to support this. Use them to constrain the content dimensions.

```jsx
// index.jsx

import { HoverCard } from "radix-ui";

import "./styles.css";

export default () => (
  <HoverCard.Root>
    <HoverCard.Trigger>…</HoverCard.Trigger>

    <HoverCard.Portal>
      <HoverCard.Content className="HoverCardContent" sideOffset={5}>
        …
      </HoverCard.Content>
    </HoverCard.Portal>
  </HoverCard.Root>
);
```

```css
/* styles.css */

.HoverCardContent {
  width: var(--radix-hover-card-trigger-width);

  max-height: var(--radix-hover-card-content-available-height);
}
```

### [Origin-aware animations](#origin-aware-animations)

We expose a CSS custom property `--radix-hover-card-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```jsx
// index.jsx

import { HoverCard } from "radix-ui";

import "./styles.css";

export default () => (
  <HoverCard.Root>
    <HoverCard.Trigger>…</HoverCard.Trigger>

    <HoverCard.Content className="HoverCardContent">…</HoverCard.Content>
  </HoverCard.Root>
);
```

```css
/* styles.css */

.HoverCardContent {
  transform-origin: var(--radix-hover-card-content-transform-origin);

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

import { HoverCard } from "radix-ui";

import "./styles.css";

export default () => (
  <HoverCard.Root>
    <HoverCard.Trigger>…</HoverCard.Trigger>

    <HoverCard.Content className="HoverCardContent">…</HoverCard.Content>
  </HoverCard.Root>
);
```

```css
/* styles.css */

.HoverCardContent {
  animation-duration: 0.6s;

  animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

.HoverCardContent[data-side="top"] {
  animation-name: slideUp;
}

.HoverCardContent[data-side="bottom"] {
  animation-name: slideDown;
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
```

## [Accessibility](#accessibility)

The hover card is intended for sighted users only, the content will be inaccessible to keyboard users.

### [Keyboard Interactions](#keyboard-interactions)

| Key     | Description                  |
| ------- | ---------------------------- |
| `Tab`   | Opens/closes the hover card. |
| `Enter` | Opens the hover card link    |
