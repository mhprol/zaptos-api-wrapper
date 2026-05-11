# Avatar

An image element with a fallback for representing the user.

## Features

- Automatic and manual control over when the image renders.

- Fallback part accepts any children.

- Optionally delay fallback rendering to avoid content flashing.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-avatar
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Avatar } from "radix-ui";

export default () => (
  <Avatar.Root>
    <Avatar.Image />

    <Avatar.Fallback />
  </Avatar.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of an avatar.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Image](#image)

The image to render. By default it will only render when it has loaded. You can use the `onLoadingStatusChange` handler if you need more control.

| Prop                    | Type       | Default          |
| ----------------------- | ---------- | ---------------- |
| `asChild`               | `boolean`  | `false`          |
| `onLoadingStatusChange` | `function` | No default value |

### [Fallback](#fallback)

An element that renders when the image hasn't loaded. This means whilst it's loading, or if there was an error. If you notice a flash during loading, you can provide a `delayMs` prop to delay its rendering so it only renders for those with slower connections. For more control, use the `onLoadingStatusChange` handler on `Avatar.Image`.

| Prop      | Type      | Default          |
| --------- | --------- | ---------------- |
| `asChild` | `boolean` | `false`          |
| `delayMs` | `number`  | No default value |

## [Examples](#examples)

### [Clickable Avatar with tooltip](#clickable-avatar-with-tooltip)

You can compose the Avatar with a [Tooltip](/primitives/docs/components/tooltip) to display extra information.

```jsx
import { Avatar, Tooltip } from "radix-ui";

export default () => (
  <Tooltip.Root>
    <Tooltip.Trigger>
      <Avatar.Root>…</Avatar.Root>
    </Tooltip.Trigger>

    <Tooltip.Content side="top">
      Tooltip content
      <Tooltip.Arrow />
    </Tooltip.Content>
  </Tooltip.Root>
);
```
