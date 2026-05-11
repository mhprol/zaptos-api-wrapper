# Toggle Group

A set of two-state buttons that can be toggled on or off.

## Features

- Full keyboard navigation.

- Supports horizontal/vertical orientation.

- Support single and multiple pressed buttons.

- Can be controlled or uncontrolled.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-toggle-group
```

## [Anatomy](#anatomy)

Import the component.

```jsx
import { ToggleGroup } from "radix-ui";

export default () => (
  <ToggleGroup.Root>
    <ToggleGroup.Item />
  </ToggleGroup.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a toggle group.

| Prop            | Type       | Default          |
| --------------- | ---------- | ---------------- |
| `asChild`       | `boolean`  | `false`          |
| `type*`         | `enum`     | No default value |
| `value`         | `string`   | No default value |
| `defaultValue`  | `string`   | No default value |
| `onValueChange` | `function` | No default value |
| `value`         | `string[]` | `[]`             |
| `defaultValue`  | `string[]` | `[]`             |
| `onValueChange` | `function` | No default value |
| `disabled`      | `boolean`  | `false`          |
| `rovingFocus`   | `boolean`  | `true`           |
| `orientation`   | `enum`     | `undefined`      |
| `dir`           | `enum`     | No default value |
| `loop`          | `boolean`  | `true`           |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Item](#item)

An item in the group.

| Prop       | Type      | Default          |
| ---------- | --------- | ---------------- |
| `asChild`  | `boolean` | `false`          |
| `value*`   | `string`  | No default value |
| `disabled` | `boolean` | No default value |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-state]`       | `"on" \| "off"`              |
| `[data-disabled]`    | Present when disabled        |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

## [Examples](#examples)

### [Ensuring there is always a value](#ensuring-there-is-always-a-value)

You can control the component to ensure a value.

```jsx
import * as React from "react";

import { ToggleGroup } from "radix-ui";

export default () => {
  const [value, setValue] = React.useState("left");

  return (
    <ToggleGroup.Root
      type="single"
      value={value}
      onValueChange={(value) => {
        if (value) setValue(value);
      }}
    >
      <ToggleGroup.Item value="left">
        <TextAlignLeftIcon />
      </ToggleGroup.Item>

      <ToggleGroup.Item value="center">
        <TextAlignCenterIcon />
      </ToggleGroup.Item>

      <ToggleGroup.Item value="right">
        <TextAlignRightIcon />
      </ToggleGroup.Item>
    </ToggleGroup.Root>
  );
};
```

## [Accessibility](#accessibility)

Uses [roving tabindex](https://www.w3.org/TR/wai-aria-practices-1.2/examples/radio/radio.html) to manage focus movement among items.

### [Keyboard Interactions](#keyboard-interactions)

| Key          | Description                                                            |
| ------------ | ---------------------------------------------------------------------- |
| `Tab`        | Moves focus to either the pressed item or the first item in the group. |
| `Space`      | Activates/deactivates the item.                                        |
| `Enter`      | Activates/deactivates the item.                                        |
| `ArrowDown`  | Moves focus to the next item in the group.                             |
| `ArrowRight` | Moves focus to the next item in the group.                             |
| `ArrowUp`    | Moves focus to the previous item in the group.                         |
| `ArrowLeft`  | Moves focus to the previous item in the group.                         |
| `Home`       | Moves focus to the first item.                                         |
| `End`        | Moves focus to the last item.                                          |
