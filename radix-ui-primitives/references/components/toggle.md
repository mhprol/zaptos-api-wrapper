# Toggle

A two-state button that can be either on or off.

## Features

- Full keyboard navigation.

- Can be controlled or uncontrolled.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-toggle
```

## [Anatomy](#anatomy)

Import the component.

```jsx
import { Toggle } from "radix-ui";

export default () => <Toggle.Root />;
```

## [API Reference](#api-reference)

### [Root](#root)

The toggle.

| Prop              | Type       | Default          |
| ----------------- | ---------- | ---------------- |
| `asChild`         | `boolean`  | `false`          |
| `defaultPressed`  | `boolean`  | No default value |
| `pressed`         | `boolean`  | No default value |
| `onPressedChange` | `function` | No default value |
| `disabled`        | `boolean`  | No default value |

| Data attribute    | Values                |
| ----------------- | --------------------- |
| `[data-state]`    | `"on" \| "off"`       |
| `[data-disabled]` | Present when disabled |

## [Accessibility](#accessibility)

### [Keyboard Interactions](#keyboard-interactions)

| Key     | Description                       |
| ------- | --------------------------------- |
| `Space` | Activates/deactivates the toggle. |
| `Enter` | Activates/deactivates the toggle. |
