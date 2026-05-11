# Radio Group

A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.

## Features

- Full keyboard navigation.

- Supports horizontal/vertical orientation.

- Can be controlled or uncontrolled.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-radio-group
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { RadioGroup } from "radix-ui";

export default () => (
  <RadioGroup.Root>
    <RadioGroup.Item>
      <RadioGroup.Indicator />
    </RadioGroup.Item>
  </RadioGroup.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a radio group.

| Prop            | Type       | Default          |
| --------------- | ---------- | ---------------- |
| `asChild`       | `boolean`  | `false`          |
| `defaultValue`  | `string`   | No default value |
| `value`         | `string`   | No default value |
| `onValueChange` | `function` | No default value |
| `disabled`      | `boolean`  | No default value |
| `name`          | `string`   | No default value |
| `required`      | `boolean`  | No default value |
| `orientation`   | `enum`     | `undefined`      |
| `dir`           | `enum`     | No default value |
| `loop`          | `boolean`  | `true`           |

| Data attribute    | Values                |
| ----------------- | --------------------- |
| `[data-disabled]` | Present when disabled |

### [Item](#item)

An item in the group that can be checked. An `input` will also render when used within a `form` to ensure events propagate correctly.

| Prop       | Type      | Default          |
| ---------- | --------- | ---------------- |
| `asChild`  | `boolean` | `false`          |
| `value`    | `string`  | No default value |
| `disabled` | `boolean` | No default value |
| `required` | `boolean` | No default value |

| Data attribute    | Values                     |
| ----------------- | -------------------------- |
| `[data-state]`    | `"checked" \| "unchecked"` |
| `[data-disabled]` | Present when disabled      |

### [Indicator](#indicator)

Renders when the radio item is in a checked state. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute    | Values                     |
| ----------------- | -------------------------- |
| `[data-state]`    | `"checked" \| "unchecked"` |
| `[data-disabled]` | Present when disabled      |

## [Accessibility](#accessibility)

Adheres to the [Radio Group WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/radio) and uses [roving tabindex](https://www.w3.org/WAI/ARIA/apg/patterns/radio/examples/radio) to manage focus movement among radio items.

### [Keyboard Interactions](#keyboard-interactions)

| Key          | Description                                                                        |
| ------------ | ---------------------------------------------------------------------------------- |
| `Tab`        | Moves focus to either the checked radio item or the first radio item in the group. |
| `Space`      | When focus is on an unchecked radio item, checks it.                               |
| `ArrowDown`  | Moves focus and checks the next radio item in the group.                           |
| `ArrowRight` | Moves focus and checks the next radio item in the group.                           |
| `ArrowUp`    | Moves focus to the previous radio item in the group.                               |
| `ArrowLeft`  | Moves focus to the previous radio item in the group.                               |
