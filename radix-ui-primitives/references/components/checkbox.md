# Checkbox

A control that allows the user to toggle between checked and not checked.

## Features

- Supports indeterminate state.

- Full keyboard navigation.

- Can be controlled or uncontrolled.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-checkbox
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Checkbox } from "radix-ui";

export default () => (
  <Checkbox.Root>
    <Checkbox.Indicator />
  </Checkbox.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a checkbox. An `input` will also render when used within a `form` to ensure events propagate correctly.

| Prop              | Type                         | Default          |
| ----------------- | ---------------------------- | ---------------- |
| `asChild`         | `boolean`                    | `false`          |
| `defaultChecked`  | `boolean \| 'indeterminate'` | No default value |
| `checked`         | `boolean \| 'indeterminate'` | No default value |
| `onCheckedChange` | `function`                   | No default value |
| `disabled`        | `boolean`                    | No default value |
| `required`        | `boolean`                    | No default value |
| `name`            | `string`                     | No default value |
| `value`           | `string`                     | `on`             |

| Data attribute    | Values                                        |
| ----------------- | --------------------------------------------- |
| `[data-state]`    | `"checked" \| "unchecked" \| "indeterminate"` |
| `[data-disabled]` | Present when disabled                         |

### [Indicator](#indicator)

Renders when the checkbox is in a checked or indeterminate state. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute    | Values                                        |
| ----------------- | --------------------------------------------- |
| `[data-state]`    | `"checked" \| "unchecked" \| "indeterminate"` |
| `[data-disabled]` | Present when disabled                         |

## [Examples](#examples)

### [Indeterminate](#indeterminate)

You can set the checkbox to `indeterminate` by taking control of its state.

```jsx
import { DividerHorizontalIcon, CheckIcon } from "@radix-ui/react-icons";

import { Checkbox } from "radix-ui";

export default () => {
  const [checked, setChecked] = React.useState("indeterminate");

  return (
    <>
      <StyledCheckbox checked={checked} onCheckedChange={setChecked}>
        <Checkbox.Indicator>
          {checked === "indeterminate" && <DividerHorizontalIcon />}

          {checked === true && <CheckIcon />}
        </Checkbox.Indicator>
      </StyledCheckbox>

      <button
        type="button"
        onClick={() =>
          setChecked((prevIsChecked) =>
            prevIsChecked === "indeterminate" ? false : "indeterminate",
          )
        }
      >
        Toggle indeterminate
      </button>
    </>
  );
};
```

## [Accessibility](#accessibility)

Adheres to the [tri-state Checkbox WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/checkbox).

### [Keyboard Interactions](#keyboard-interactions)

| Key     | Description                   |
| ------- | ----------------------------- |
| `Space` | Checks/unchecks the checkbox. |
