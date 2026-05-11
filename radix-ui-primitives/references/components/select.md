# Select

Displays a list of options for the user to pick from—triggered by a button.

## Features

- Can be controlled or uncontrolled.

- Offers 2 positioning modes.

- Supports items, labels, groups of items.

- Focus is fully managed.

- Full keyboard navigation.

- Supports custom placeholder.

- Typeahead support.

- Supports Right to Left direction.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-select
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Select } from "radix-ui";

export default () => (
  <Select.Root>
    <Select.Trigger>
      <Select.Value />

      <Select.Icon />
    </Select.Trigger>

    <Select.Portal>
      <Select.Content>
        <Select.ScrollUpButton />

        <Select.Viewport>
          <Select.Item>
            <Select.ItemText />

            <Select.ItemIndicator />
          </Select.Item>

          <Select.Group>
            <Select.Label />

            <Select.Item>
              <Select.ItemText />

              <Select.ItemIndicator />
            </Select.Item>
          </Select.Group>

          <Select.Separator />
        </Select.Viewport>

        <Select.ScrollDownButton />

        <Select.Arrow />
      </Select.Content>
    </Select.Portal>
  </Select.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a select.

| Prop            | Type       | Default          |
| --------------- | ---------- | ---------------- |
| `defaultValue`  | `string`   | No default value |
| `value`         | `string`   | No default value |
| `onValueChange` | `function` | No default value |
| `defaultOpen`   | `boolean`  | No default value |
| `open`          | `boolean`  | No default value |
| `onOpenChange`  | `function` | No default value |
| `dir`           | `enum`     | No default value |
| `name`          | `string`   | No default value |
| `disabled`      | `boolean`  | No default value |
| `required`      | `boolean`  | No default value |

### [Trigger](#trigger)

The button that toggles the select. The `Select.Content` will position itself by aligning over the trigger.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-state]`       | `"open" \| "closed"`         |
| `[data-disabled]`    | Present when disabled        |
| `[data-placeholder]` | Present when has placeholder |

### [Value](#value)

The part that reflects the selected value. By default the selected item's text will be rendered. if you require more control, you can instead control the select and pass your own `children`. It should not be styled to ensure correct positioning. An optional `placeholder` prop is also available for when the select has no value.

| Prop          | Type        | Default          |
| ------------- | ----------- | ---------------- |
| `asChild`     | `boolean`   | `false`          |
| `placeholder` | `ReactNode` | No default value |

### [Icon](#icon)

A small icon often displayed next to the value as a visual affordance for the fact it can be open. By default renders ▼ but you can use your own icon via `asChild` or use `children`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Portal](#portal)

When used, portals the content part into the `body`.

| Prop        | Type          | Default         |
| ----------- | ------------- | --------------- |
| `container` | `HTMLElement` | `document.body` |

### [Content](#content)

The component that pops out when the select is open.

| Prop                   | Type                | Default          |
| ---------------------- | ------------------- | ---------------- |
| `asChild`              | `boolean`           | `false`          |
| `onCloseAutoFocus`     | `function`          | No default value |
| `onEscapeKeyDown`      | `function`          | No default value |
| `onPointerDownOutside` | `function`          | No default value |
| `position`             | `enum`              | `"item-aligned"` |
| `side`                 | `enum`              | `"bottom"`       |
| `sideOffset`           | `number`            | `0`              |
| `align`                | `enum`              | `"start"`        |
| `alignOffset`          | `number`            | `0`              |
| `avoidCollisions`      | `boolean`           | `true`           |
| `collisionBoundary`    | `Boundary`          | `[]`             |
| `collisionPadding`     | `number \| Padding` | `10`             |
| `arrowPadding`         | `number`            | `0`              |
| `sticky`               | `enum`              | `"partial"`      |
| `hideWhenDetached`     | `boolean`           | `false`          |

| Data attribute | Values                                   |
| -------------- | ---------------------------------------- |
| `[data-state]` | `"open" \| "closed"`                     |
| `[data-side]`  | `"left" \| "right" \| "bottom" \| "top"` |
| `[data-align]` | `"start" \| "end" \| "center"`           |

| CSS Variable                              | Description                                                                                                          |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `--radix-select-content-transform-origin` | The `transform-origin` computed from the content and arrow positions/offsets. Only present when `position="popper"`. |
| `--radix-select-content-available-width`  | The remaining width between the trigger and the boundary edge. Only present when `position="popper"`.                |
| `--radix-select-content-available-height` | The remaining height between the trigger and the boundary edge. Only present when `position="popper"`.               |
| `--radix-select-trigger-width`            | The width of the trigger. Only present when<!-- --> `position="popper"`.                                             |
| `--radix-select-trigger-height`           | The height of the trigger. Only present when<!-- --> `position="popper"`.                                            |

### [Viewport](#viewport)

The scrolling viewport that contains all of the items.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Item](#item)

The component that contains the select items.

| Prop        | Type      | Default          |
| ----------- | --------- | ---------------- |
| `asChild`   | `boolean` | `false`          |
| `value*`    | `string`  | No default value |
| `disabled`  | `boolean` | No default value |
| `textValue` | `string`  | No default value |

| Data attribute       | Values                     |
| -------------------- | -------------------------- |
| `[data-state]`       | `"checked" \| "unchecked"` |
| `[data-highlighted]` | Present when highlighted   |
| `[data-disabled]`    | Present when disabled      |

### [ItemText](#itemtext)

The textual part of the item. It should only contain the text you want to see in the trigger when that item is selected. It should not be styled to ensure correct positioning.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [ItemIndicator](#itemindicator)

Renders when the item is selected. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [ScrollUpButton](#scrollupbutton)

An optional button used as an affordance to show the viewport overflow as well as functionaly enable scrolling upwards.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [ScrollDownButton](#scrolldownbutton)

An optional button used as an affordance to show the viewport overflow as well as functionaly enable scrolling downwards.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Group](#group)

Used to group multiple items. use in conjunction with `Select.Label` to ensure good accessibility via automatic labelling.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Label](#label)

Used to render the label of a group. It won't be focusable using arrow keys.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Separator](#separator)

Used to visually separate items in the select.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Arrow](#arrow)

An optional arrow element to render alongside the content. This can be used to help visually link the trigger with the `Select.Content`. Must be rendered inside `Select.Content`. Only available when `position` is set to `popper`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |
| `width`   | `number`  | `10`    |
| `height`  | `number`  | `5`     |

## [Examples](#examples)

### [Change the positioning mode](#change-the-positioning-mode)

By default, `Select` will behave similarly to a native MacOS menu by positioning `Select.Content` relative to the active item. If you would prefer an alternative positioning approach similar to `Popover` or `DropdownMenu` then you can set `position` to `popper` and make use of additional alignment options such as `side`, `sideOffset` and more.

```jsx
// index.jsx

import { Select } from "radix-ui";

export default () => (
  <Select.Root>
    <Select.Trigger>…</Select.Trigger>

    <Select.Portal>
      <Select.Content position="popper" sideOffset={5}>
        …
      </Select.Content>
    </Select.Portal>
  </Select.Root>
);
```

### [Constrain the content size](#constrain-the-content-size)

When using `position="popper"` on `Select.Content`, you may want to constrain the width of the content so that it matches the trigger width. You may also want to constrain its height to not exceed the viewport.

We expose several CSS custom properties such as `--radix-select-trigger-width` and `--radix-select-content-available-height` to support this. Use them to constrain the content dimensions.

```jsx
// index.jsx

import { Select } from "radix-ui";

import "./styles.css";

export default () => (
  <Select.Root>
    <Select.Trigger>…</Select.Trigger>

    <Select.Portal>
      <Select.Content className="SelectContent" position="popper" sideOffset={5}>
        …
      </Select.Content>
    </Select.Portal>
  </Select.Root>
);
```

```css
/* styles.css */

.SelectContent {
  width: var(--radix-select-trigger-width);

  max-height: var(--radix-select-content-available-height);
}
```

### [With disabled items](#with-disabled-items)

You can add special styles to disabled items via the `data-disabled` attribute.

```jsx
// index.jsx

import { Select } from "radix-ui";

import "./styles.css";

export default () => (
  <Select.Root>
    <Select.Trigger>…</Select.Trigger>

    <Select.Portal>
      <Select.Content>
        <Select.Viewport>
          <Select.Item className="SelectItem" disabled>
            …
          </Select.Item>

          <Select.Item>…</Select.Item>

          <Select.Item>…</Select.Item>
        </Select.Viewport>
      </Select.Content>
    </Select.Portal>
  </Select.Root>
);
```

```css
/* styles.css */

.SelectItem[data-disabled] {
  color: "gainsboro";
}
```

### [With a placeholder](#with-a-placeholder)

You can use the `placeholder` prop on `Value` for when the select has no value. There's also a `data-placeholder` attribute on `Trigger` to help with styling.

```jsx
// index.jsx

import { Select } from "radix-ui";

import "./styles.css";

export default () => (
  <Select.Root>
    <Select.Trigger className="SelectTrigger">
      <Select.Value placeholder="Pick an option" />

      <Select.Icon />
    </Select.Trigger>

    <Select.Portal>
      <Select.Content>…</Select.Content>
    </Select.Portal>
  </Select.Root>
);
```

```css
/* styles.css */

.SelectTrigger[data-placeholder] {
  color: "gainsboro";
}
```

### [With separators](#with-separators)

Use the `Separator` part to add a separator between items.

```jsx
<Select.Root>
  <Select.Trigger>…</Select.Trigger>

  <Select.Portal>
    <Select.Content>
      <Select.Viewport>
        <Select.Item>…</Select.Item>

        <Select.Item>…</Select.Item>

        <Select.Item>…</Select.Item>

        <Select.Separator />

        <Select.Item>…</Select.Item>

        <Select.Item>…</Select.Item>
      </Select.Viewport>
    </Select.Content>
  </Select.Portal>
</Select.Root>
```

### [With grouped items](#with-grouped-items)

Use the `Group` and `Label` parts to group items in a section.

```jsx
<Select.Root>
  <Select.Trigger>…</Select.Trigger>

  <Select.Portal>
    <Select.Content>
      <Select.Viewport>
        <Select.Group>
          <Select.Label>Label</Select.Label>

          <Select.Item>…</Select.Item>

          <Select.Item>…</Select.Item>

          <Select.Item>…</Select.Item>
        </Select.Group>
      </Select.Viewport>
    </Select.Content>
  </Select.Portal>
</Select.Root>
```

### [With complex items](#with-complex-items)

You can use custom content in your items.

```jsx
import { Select } from "radix-ui";

export default () => (
  <Select.Root>
    <Select.Trigger>…</Select.Trigger>

    <Select.Portal>
      <Select.Content>
        <Select.Viewport>
          <Select.Item>
            <Select.ItemText>
              <img src="…" />
              Adolfo Hess
            </Select.ItemText>

            <Select.ItemIndicator>…</Select.ItemIndicator>
          </Select.Item>

          <Select.Item>…</Select.Item>

          <Select.Item>…</Select.Item>
        </Select.Viewport>
      </Select.Content>
    </Select.Portal>
  </Select.Root>
);
```

### [Controlling the value displayed in the trigger](#controlling-the-value-displayed-in-the-trigger)

By default the trigger will automatically display the selected item `ItemText`'s content. You can control what appears by chosing to put things inside/outside the `ItemText` part.

If you need more flexibility, you can control the component using `value`/`onValueChange` props and passing `children` to `SelectValue`. Remember to make sure what you put in there is accessible.

```jsx
const countries = { france: "🇫🇷", "united-kingdom": "🇬🇧", spain: "🇪🇸" };

export default () => {
  const [value, setValue] = React.useState("france");

  return (
    <Select.Root value={value} onValueChange={setValue}>
      <Select.Trigger>
        <Select.Value aria-label={value}>{countries[value]}</Select.Value>

        <Select.Icon />
      </Select.Trigger>

      <Select.Portal>
        <Select.Content>
          <Select.Viewport>
            <Select.Item value="france">
              <Select.ItemText>France</Select.ItemText>

              <Select.ItemIndicator>…</Select.ItemIndicator>
            </Select.Item>

            <Select.Item value="united-kingdom">
              <Select.ItemText>United Kingdom</Select.ItemText>

              <Select.ItemIndicator>…</Select.ItemIndicator>
            </Select.Item>

            <Select.Item value="spain">
              <Select.ItemText>Spain</Select.ItemText>

              <Select.ItemIndicator>…</Select.ItemIndicator>
            </Select.Item>
          </Select.Viewport>
        </Select.Content>
      </Select.Portal>
    </Select.Root>
  );
};
```

### [With custom scrollbar](#with-custom-scrollbar)

The native scrollbar is hidden by default as we recommend using the `ScrollUpButton` and `ScrollDownButton` parts for the best UX. If you do not want to use these parts, compose your select with our [Scroll Area](/primitives/docs/components/scroll-area) primitive.

```jsx
// index.jsx

import { Select, ScrollArea } from "radix-ui";

import "./styles.css";

export default () => (
  <Select.Root>
    <Select.Trigger>…</Select.Trigger>

    <Select.Portal>
      <Select.Content>
        <ScrollArea.Root className="ScrollAreaRoot" type="auto">
          <Select.Viewport asChild>
            <ScrollArea.Viewport className="ScrollAreaViewport">
              <StyledItem>…</StyledItem>

              <StyledItem>…</StyledItem>

              <StyledItem>…</StyledItem>
            </ScrollArea.Viewport>
          </Select.Viewport>

          <ScrollArea.Scrollbar className="ScrollAreaScrollbar" orientation="vertical">
            <ScrollArea.Thumb className="ScrollAreaThumb" />
          </ScrollArea.Scrollbar>
        </ScrollArea.Root>
      </Select.Content>
    </Select.Portal>
  </Select.Root>
);
```

```css
/* styles.css */

.ScrollAreaRoot {
  width: 100%;

  height: 100%;
}

.ScrollAreaViewport {
  width: 100%;

  height: 100%;
}

.ScrollAreaScrollbar {
  width: 4px;

  padding: 5px 2px;
}

.ScrollAreaThumb {
  background: rgba(0, 0, 0, 0.3);

  border-radius: 3px;
}
```

## [Accessibility](#accessibility)

Adheres to the [ListBox WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/listbox).

See the W3C [Select-Only Combobox](https://www.w3.org/TR/wai-aria-practices/examples/combobox/combobox-select-only.html) example for more information.

### [Keyboard Interactions](#keyboard-interactions)

| Key         | Description                                                                                                                            |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `Space`     | When focus is on `Select.Trigger`, opens the select and focuses the selected item. When focus is on an item, selects the focused item. |
| `Enter`     | When focus is on `Select.Trigger`, opens the select and focuses the first item. When focus is on an item, selects the focused item.    |
| `ArrowDown` | When focus is on `Select.Trigger`, opens the select. When focus is on an item, moves focus to the next item.                           |
| `ArrowUp`   | When focus is on `Select.Trigger`, opens the select. When focus is on an item, moves focus to the previous item.                       |
| `Esc`       | Closes the select and moves focus to `Select.Trigger`.                                                                                 |

### [Labelling](#labelling)

Use our [Label](/primitives/docs/components/label) component in order to offer a visual and accessible label for the select.

```jsx
import { Select, Label } from "radix-ui";

export default () => (
  <>
    <Label>
      Country
      <Select.Root>…</Select.Root>
    </Label>

    {/* or */}

    <Label htmlFor="country">Country</Label>

    <Select.Root>
      <Select.Trigger id="country">…</Select.Trigger>

      <Select.Portal>
        <Select.Content>…</Select.Content>
      </Select.Portal>
    </Select.Root>
  </>
);
```

## [Custom APIs](#custom-apis)

Create your own API by abstracting the primitive parts into your own component.

### [Abstract down to `Select` and `SelectItem`](#abstract-down-to-select-and-selectitem)

This example abstracts most of the parts.

#### Usage

```jsx
import { Select, SelectItem } from "./your-select";

export default () => (
  <Select defaultValue="2">
    <SelectItem value="1">Item 1</SelectItem>

    <SelectItem value="2">Item 2</SelectItem>

    <SelectItem value="3">Item 3</SelectItem>
  </Select>
);
```

#### Implementation

```jsx
// your-select.jsx

import * as React from "react";

import { Select as SelectPrimitive } from "radix-ui";

import { CheckIcon, ChevronDownIcon, ChevronUpIcon } from "@radix-ui/react-icons";

export const Select = React.forwardRef(({ children, ...props }, forwardedRef) => {
  return (
    <SelectPrimitive.Root {...props}>
      <SelectPrimitive.Trigger ref={forwardedRef}>
        <SelectPrimitive.Value />

        <SelectPrimitive.Icon>
          <ChevronDownIcon />
        </SelectPrimitive.Icon>
      </SelectPrimitive.Trigger>

      <SelectPrimitive.Portal>
        <SelectPrimitive.Content>
          <SelectPrimitive.ScrollUpButton>
            <ChevronUpIcon />
          </SelectPrimitive.ScrollUpButton>

          <SelectPrimitive.Viewport>{children}</SelectPrimitive.Viewport>

          <SelectPrimitive.ScrollDownButton>
            <ChevronDownIcon />
          </SelectPrimitive.ScrollDownButton>
        </SelectPrimitive.Content>
      </SelectPrimitive.Portal>
    </SelectPrimitive.Root>
  );
});

export const SelectItem = React.forwardRef(({ children, ...props }, forwardedRef) => {
  return (
    <SelectPrimitive.Item {...props} ref={forwardedRef}>
      <SelectPrimitive.ItemText>{children}</SelectPrimitive.ItemText>

      <SelectPrimitive.ItemIndicator>
        <CheckIcon />
      </SelectPrimitive.ItemIndicator>
    </SelectPrimitive.Item>
  );
});
```
