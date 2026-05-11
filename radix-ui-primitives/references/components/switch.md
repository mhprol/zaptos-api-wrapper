# Switch

A control that allows the user to toggle between checked and not checked.

## Features

- Full keyboard navigation.

- Can be controlled or uncontrolled.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-switch
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Switch } from "radix-ui";

export default () => (
  <Switch.Root>
    <Switch.Thumb />
  </Switch.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a switch. An `input` will also render when used within a `form` to ensure events propagate correctly.

| Prop              | Type       | Default          |
| ----------------- | ---------- | ---------------- |
| `asChild`         | `boolean`  | `false`          |
| `defaultChecked`  | `boolean`  | No default value |
| `checked`         | `boolean`  | No default value |
| `onCheckedChange` | `function` | No default value |
| `disabled`        | `boolean`  | No default value |
| `required`        | `boolean`  | No default value |
| `name`            | `string`   | No default value |
| `value`           | `string`   | `on`             |

| Data attribute    | Values                     |
| ----------------- | -------------------------- |
| `[data-state]`    | `"checked" \| "unchecked"` |
| `[data-disabled]` | Present when disabled      |

### [Thumb](#thumb)

The thumb that is used to visually indicate whether the switch is on or off.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute    | Values                     |
| ----------------- | -------------------------- |
| `[data-state]`    | `"checked" \| "unchecked"` |
| `[data-disabled]` | Present when disabled      |

## [Accessibility](#accessibility)

Adheres to the [`switch` role requirements](https://www.w3.org/WAI/ARIA/apg/patterns/switch).

### [Keyboard Interactions](#keyboard-interactions)

| Key     | Description                    |
| ------- | ------------------------------ |
| `Space` | Toggles the component's state. |
| `Enter` | Toggles the component's state. |
