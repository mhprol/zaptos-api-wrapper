# Scroll Area

Augments native scroll functionality for custom, cross-browser styling.

## Features

- Scrollbar sits on top of the scrollable content, taking up no space.

- Scrolling is native; no underlying position movements via CSS transformations.

- Shims pointer behaviors only when interacting with the controls, so keyboard controls are unaffected.

- Supports Right to Left direction.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-scroll-area
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { ScrollArea } from "radix-ui";

export default () => (
  <ScrollArea.Root>
    <ScrollArea.Viewport />

    <ScrollArea.Scrollbar orientation="horizontal">
      <ScrollArea.Thumb />
    </ScrollArea.Scrollbar>

    <ScrollArea.Scrollbar orientation="vertical">
      <ScrollArea.Thumb />
    </ScrollArea.Scrollbar>

    <ScrollArea.Corner />
  </ScrollArea.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a scroll area.

| Prop              | Type      | Default          |
| ----------------- | --------- | ---------------- |
| `asChild`         | `boolean` | `false`          |
| `type`            | `enum`    | `"hover"`        |
| `scrollHideDelay` | `number`  | `600`            |
| `dir`             | `enum`    | No default value |
| `nonce`           | `string`  | No default value |

### [Viewport](#viewport)

The viewport area of the scroll area.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Scrollbar](#scrollbar)

The vertical scrollbar. Add a second `Scrollbar` with an `orientation` prop to enable horizontal scrolling.

| Prop          | Type      | Default          |
| ------------- | --------- | ---------------- |
| `asChild`     | `boolean` | `false`          |
| `forceMount`  | `boolean` | No default value |
| `orientation` | `enum`    | `vertical`       |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-state]`       | `"visible" \| "hidden"`      |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Thumb](#thumb)

The thumb to be used in `ScrollArea.Scrollbar`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute | Values                  |
| -------------- | ----------------------- |
| `[data-state]` | `"visible" \| "hidden"` |

### [Corner](#corner)

The corner where both vertical and horizontal scrollbars meet.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

## [Accessibility](#accessibility)

In most cases, it's best to rely on native scrolling and work with the customization options available in CSS. When that isn't enough, `ScrollArea` provides additional customizability while maintaining the browser's native scroll behavior (as well as accessibility features, like keyboard scrolling).

### [Keyboard Interactions](#keyboard-interactions)

Scrolling via keyboard is supported by default because the component relies on native scrolling. Specific keyboard interactions may differ between platforms, so we do not specify them here or add specific event listeners to handle scrolling via key events.
