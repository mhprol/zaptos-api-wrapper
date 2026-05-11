# Toolbar

A container for grouping a set of controls, such as buttons, toggle groups or dropdown menus.

## Features

- Full keyboard navigation.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-toolbar
```

## [Anatomy](#anatomy)

Import the component.

```jsx
import { Toolbar } from "radix-ui";

export default () => (
  <Toolbar.Root>
    <Toolbar.Button />

    <Toolbar.Separator />

    <Toolbar.Link />

    <Toolbar.ToggleGroup>
      <Toolbar.ToggleItem />
    </Toolbar.ToggleGroup>
  </Toolbar.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the toolbar component parts.

| Prop          | Type      | Default          |
| ------------- | --------- | ---------------- |
| `asChild`     | `boolean` | `false`          |
| `orientation` | `enum`    | `"horizontal"`   |
| `dir`         | `enum`    | No default value |
| `loop`        | `boolean` | `true`           |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Button](#button)

A button item.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Link](#link)

A link item.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [ToggleGroup](#togglegroup)

A set of two-state buttons that can be toggled on or off.

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

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [ToggleItem](#toggleitem)

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

### [Separator](#separator)

Used to visually separate items in the toolbar.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

## [Examples](#examples)

### [Use with other primitives](#use-with-other-primitives)

All our primitives which expose a `Trigger` part, such as `Dialog`, `AlertDialog`, `Popover`, `DropdownMenu` can be composed within a toolbar by using the [`asChild` prop](/primitives/docs/guides/composition).

Here is an example using our `DropdownMenu` primitive.

```jsx
import { Toolbar, DropdownMenu } from "radix-ui";

export default () => (
  <Toolbar.Root>
    <Toolbar.Button>Action 1</Toolbar.Button>

    <Toolbar.Separator />

    <DropdownMenu.Root>
      <Toolbar.Button asChild>
        <DropdownMenu.Trigger>Trigger</DropdownMenu.Trigger>
      </Toolbar.Button>

      <DropdownMenu.Content>…</DropdownMenu.Content>
    </DropdownMenu.Root>
  </Toolbar.Root>
);
```

## [Accessibility](#accessibility)

Uses [roving tabindex](https://www.w3.org/TR/wai-aria-practices-1.2/examples/radio/radio.html) to manage focus movement among items.

### [Keyboard Interactions](#keyboard-interactions)

| Key          | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| `Tab`        | Moves focus to the first item in the group.                  |
| `Space`      | Activates/deactivates the item.                              |
| `Enter`      | Activates/deactivates the item.                              |
| `ArrowDown`  | Moves focus to the next item depending on `orientation`.     |
| `ArrowRight` | Moves focus to the next item depending on `orientation`.     |
| `ArrowUp`    | Moves focus to the previous item depending on `orientation`. |
| `ArrowLeft`  | Moves focus to the previous item depending on `orientation`. |
| `Home`       | Moves focus to the first item.                               |
| `End`        | Moves focus to the last item.                                |
