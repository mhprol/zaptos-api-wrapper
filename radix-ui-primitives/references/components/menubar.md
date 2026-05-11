# Menu Bar

A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.

## Features

- Can be controlled or uncontrolled.

- Supports submenus with configurable reading direction.

- Supports items, labels, groups of items.

- Supports checkable items (single or multiple).

- Customize side, alignment, offsets, collision handling.

- Optionally render a pointing arrow.

- Focus is fully managed.

- Full keyboard navigation.

- Typeahead support.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-menubar
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Menubar } from "radix-ui";

export default () => (
  <Menubar.Root>
    <Menubar.Menu>
      <Menubar.Trigger />

      <Menubar.Portal>
        <Menubar.Content>
          <Menubar.Label />

          <Menubar.Item />

          <Menubar.Group>
            <Menubar.Item />
          </Menubar.Group>

          <Menubar.CheckboxItem>
            <Menubar.ItemIndicator />
          </Menubar.CheckboxItem>

          <Menubar.RadioGroup>
            <Menubar.RadioItem>
              <Menubar.ItemIndicator />
            </Menubar.RadioItem>
          </Menubar.RadioGroup>

          <Menubar.Sub>
            <Menubar.SubTrigger />

            <Menubar.Portal>
              <Menubar.SubContent />
            </Menubar.Portal>
          </Menubar.Sub>

          <Menubar.Separator />

          <Menubar.Arrow />
        </Menubar.Content>
      </Menubar.Portal>
    </Menubar.Menu>
  </Menubar.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a menubar.

| Prop            | Type       | Default          |
| --------------- | ---------- | ---------------- |
| `asChild`       | `boolean`  | `false`          |
| `defaultValue`  | `string`   | No default value |
| `value`         | `string`   | No default value |
| `onValueChange` | `function` | No default value |
| `dir`           | `enum`     | No default value |
| `loop`          | `boolean`  | `false`          |

### [Menu](#menu)

A top level menu item, contains a trigger with content combination.

| Prop      | Type      | Default          |
| --------- | --------- | ---------------- |
| `asChild` | `boolean` | `false`          |
| `value`   | `string`  | No default value |

### [Trigger](#trigger)

The button that toggles the content. By default, the `Menubar.Content` will position itself against the trigger.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                   |
| -------------------- | ------------------------ |
| `[data-state]`       | `"open" \| "closed"`     |
| `[data-highlighted]` | Present when highlighted |
| `[data-disabled]`    | Present when disabled    |

### [Portal](#portal)

When used, portals the content part into the `body`.

| Prop         | Type          | Default          |
| ------------ | ------------- | ---------------- |
| `forceMount` | `boolean`     | No default value |
| `container`  | `HTMLElement` | `document.body`  |

### [Content](#content)

The component that pops out when a menu is open.

| Prop                   | Type                | Default          |
| ---------------------- | ------------------- | ---------------- |
| `asChild`              | `boolean`           | `false`          |
| `loop`                 | `boolean`           | `false`          |
| `onCloseAutoFocus`     | `function`          | No default value |
| `onEscapeKeyDown`      | `function`          | No default value |
| `onPointerDownOutside` | `function`          | No default value |
| `onFocusOutside`       | `function`          | No default value |
| `onInteractOutside`    | `function`          | No default value |
| `forceMount`           | `boolean`           | No default value |
| `side`                 | `enum`              | `"bottom"`       |
| `sideOffset`           | `number`            | `0`              |
| `align`                | `enum`              | `"center"`       |
| `alignOffset`          | `number`            | `0`              |
| `avoidCollisions`      | `boolean`           | `true`           |
| `collisionBoundary`    | `Boundary`          | `[]`             |
| `collisionPadding`     | `number \| Padding` | `0`              |
| `arrowPadding`         | `number`            | `0`              |
| `sticky`               | `enum`              | `"partial"`      |
| `hideWhenDetached`     | `boolean`           | `false`          |

| Data attribute | Values                                   |
| -------------- | ---------------------------------------- |
| `[data-state]` | `"open" \| "closed"`                     |
| `[data-side]`  | `"left" \| "right" \| "bottom" \| "top"` |
| `[data-align]` | `"start" \| "end" \| "center"`           |

| CSS Variable                               | Description                                                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------- |
| `--radix-menubar-content-transform-origin` | The `transform-origin` computed from the content and arrow positions/offsets |
| `--radix-menubar-content-available-width`  | The remaining width between the trigger and the boundary edge                |
| `--radix-menubar-content-available-height` | The remaining height between the trigger and the boundary edge               |
| `--radix-menubar-trigger-width`            | The width of the trigger                                                     |
| `--radix-menubar-trigger-height`           | The height of the trigger                                                    |

### [Arrow](#arrow)

An optional arrow element to render alongside a menubar menu. This can be used to help visually link the trigger with the `Menubar.Content`. Must be rendered inside `Menubar.Content`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |
| `width`   | `number`  | `10`    |
| `height`  | `number`  | `5`     |

### [Item](#item)

The component that contains the menubar items.

| Prop        | Type       | Default          |
| ----------- | ---------- | ---------------- |
| `asChild`   | `boolean`  | `false`          |
| `disabled`  | `boolean`  | No default value |
| `onSelect`  | `function` | No default value |
| `textValue` | `string`   | No default value |

| Data attribute       | Values                   |
| -------------------- | ------------------------ |
| `[data-highlighted]` | Present when highlighted |
| `[data-disabled]`    | Present when disabled    |

### [Group](#group)

Used to group multiple `Menubar.Item`s.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Label](#label)

Used to render a label. It won't be focusable using arrow keys.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [CheckboxItem](#checkboxitem)

An item that can be controlled and rendered like a checkbox.

| Prop              | Type                         | Default          |
| ----------------- | ---------------------------- | ---------------- |
| `asChild`         | `boolean`                    | `false`          |
| `checked`         | `boolean \| 'indeterminate'` | No default value |
| `onCheckedChange` | `function`                   | No default value |
| `disabled`        | `boolean`                    | No default value |
| `onSelect`        | `function`                   | No default value |
| `textValue`       | `string`                     | No default value |

| Data attribute       | Values                     |
| -------------------- | -------------------------- |
| `[data-state]`       | `"checked" \| "unchecked"` |
| `[data-highlighted]` | Present when highlighted   |
| `[data-disabled]`    | Present when disabled      |

### [RadioGroup](#radiogroup)

Used to group multiple `Menubar.RadioItem`s.

| Prop            | Type       | Default          |
| --------------- | ---------- | ---------------- |
| `asChild`       | `boolean`  | `false`          |
| `value`         | `string`   | No default value |
| `onValueChange` | `function` | No default value |

### [RadioItem](#radioitem)

An item that can be controlled and rendered like a radio.

| Prop        | Type       | Default          |
| ----------- | ---------- | ---------------- |
| `asChild`   | `boolean`  | `false`          |
| `value*`    | `string`   | No default value |
| `disabled`  | `boolean`  | No default value |
| `onSelect`  | `function` | No default value |
| `textValue` | `string`   | No default value |

| Data attribute       | Values                     |
| -------------------- | -------------------------- |
| `[data-state]`       | `"checked" \| "unchecked"` |
| `[data-highlighted]` | Present when highlighted   |
| `[data-disabled]`    | Present when disabled      |

### [ItemIndicator](#itemindicator)

Renders when the parent `Menubar.CheckboxItem` or `Menubar.RadioItem` is checked. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute | Values                     |
| -------------- | -------------------------- |
| `[data-state]` | `"checked" \| "unchecked"` |

### [Separator](#separator)

Used to visually separate items in a menubar menu.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Sub](#sub)

Contains all the parts of a submenu.

| Prop           | Type       | Default          |
| -------------- | ---------- | ---------------- |
| `defaultOpen`  | `boolean`  | No default value |
| `open`         | `boolean`  | No default value |
| `onOpenChange` | `function` | No default value |

### [SubTrigger](#subtrigger)

An item that opens a submenu. Must be rendered inside `Menubar.Sub`.

| Prop        | Type      | Default          |
| ----------- | --------- | ---------------- |
| `asChild`   | `boolean` | `false`          |
| `disabled`  | `boolean` | No default value |
| `textValue` | `string`  | No default value |

| Data attribute       | Values                   |
| -------------------- | ------------------------ |
| `[data-state]`       | `"open" \| "closed"`     |
| `[data-highlighted]` | Present when highlighted |
| `[data-disabled]`    | Present when disabled    |

### [SubContent](#subcontent)

The component that pops out when a submenu is open. Must be rendered inside `Menubar.Sub`.

| Prop                   | Type                | Default          |
| ---------------------- | ------------------- | ---------------- |
| `asChild`              | `boolean`           | `false`          |
| `loop`                 | `boolean`           | `false`          |
| `onEscapeKeyDown`      | `function`          | No default value |
| `onPointerDownOutside` | `function`          | No default value |
| `onFocusOutside`       | `function`          | No default value |
| `onInteractOutside`    | `function`          | No default value |
| `forceMount`           | `boolean`           | No default value |
| `sideOffset`           | `number`            | `0`              |
| `alignOffset`          | `number`            | `0`              |
| `avoidCollisions`      | `boolean`           | `true`           |
| `collisionBoundary`    | `Boundary`          | `[]`             |
| `collisionPadding`     | `number \| Padding` | `0`              |
| `arrowPadding`         | `number`            | `0`              |
| `sticky`               | `enum`              | `"partial"`      |
| `hideWhenDetached`     | `boolean`           | `false`          |

| Data attribute       | Values                                   |
| -------------------- | ---------------------------------------- |
| `[data-state]`       | `"open" \| "closed"`                     |
| `[data-side]`        | `"left" \| "right" \| "bottom" \| "top"` |
| `[data-align]`       | `"start" \| "end" \| "center"`           |
| `[data-orientation]` | `"vertical" \| "horizontal"`             |

| CSS Variable                               | Description                                                                  |
| ------------------------------------------ | ---------------------------------------------------------------------------- |
| `--radix-menubar-content-transform-origin` | The `transform-origin` computed from the content and arrow positions/offsets |
| `--radix-menubar-content-available-width`  | The remaining width between the trigger and the boundary edge                |
| `--radix-menubar-content-available-height` | The remaining height between the trigger and the boundary edge               |
| `--radix-menubar-trigger-width`            | The width of the trigger                                                     |
| `--radix-menubar-trigger-height`           | The height of the trigger                                                    |

## [Examples](#examples)

### [With submenus](#with-submenus)

You can create submenus by using `Menubar.Sub` in combination with its parts.

```jsx
<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>…</Menubar.Trigger>

    <Menubar.Portal>
      <Menubar.Content>
        <Menubar.Item>…</Menubar.Item>

        <Menubar.Item>…</Menubar.Item>

        <Menubar.Separator />

        <Menubar.Sub>
          <Menubar.SubTrigger>Sub menu →</Menubar.SubTrigger>

          <Menubar.Portal>
            <Menubar.SubContent>
              <Menubar.Item>Sub menu item</Menubar.Item>

              <Menubar.Item>Sub menu item</Menubar.Item>

              <Menubar.Arrow />
            </Menubar.SubContent>
          </Menubar.Portal>
        </Menubar.Sub>

        <Menubar.Separator />

        <Menubar.Item>…</Menubar.Item>
      </Menubar.Content>
    </Menubar.Portal>
  </Menubar.Menu>
</Menubar.Root>
```

### [With disabled items](#with-disabled-items)

You can add special styles to disabled items via the `data-disabled` attribute.

```jsx
// index.jsx

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (
  <Menubar.Root>
    <Menubar.Menu>
      <Menubar.Trigger>…</Menubar.Trigger>

      <Menubar.Portal>
        <Menubar.Content>
          <Menubar.Item className="MenubarItem" disabled>
            …
          </Menubar.Item>

          <Menubar.Item className="MenubarItem">…</Menubar.Item>
        </Menubar.Content>
      </Menubar.Portal>
    </Menubar.Menu>
  </Menubar.Root>
);
```

```css
/* styles.css */

.MenubarItem[data-disabled] {
  color: gainsboro;
}
```

### [With separators](#with-separators)

Use the `Separator` part to add a separator between items.

```jsx
<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>…</Menubar.Trigger>

    <Menubar.Portal>
      <Menubar.Content>
        <Menubar.Item>…</Menubar.Item>

        <Menubar.Separator />

        <Menubar.Item>…</Menubar.Item>

        <Menubar.Separator />

        <Menubar.Item>…</Menubar.Item>
      </Menubar.Content>
    </Menubar.Portal>
  </Menubar.Menu>
</Menubar.Root>
```

### [With labels](#with-labels)

Use the `Label` part to help label a section.

```jsx
<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>…</Menubar.Trigger>

    <Menubar.Portal>
      <Menubar.Content>
        <Menubar.Label>Label</Menubar.Label>

        <Menubar.Item>…</Menubar.Item>

        <Menubar.Item>…</Menubar.Item>

        <Menubar.Item>…</Menubar.Item>
      </Menubar.Content>
    </Menubar.Portal>
  </Menubar.Menu>
</Menubar.Root>
```

### [With checkbox items](#with-checkbox-items)

Use the `CheckboxItem` part to add an item that can be checked.

```jsx
import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { Menubar } from "radix-ui";

export default () => {
  const [checked, setChecked] = React.useState(true);

  return (
    <Menubar.Root>
      <Menubar.Menu>
        <Menubar.Trigger>…</Menubar.Trigger>

        <Menubar.Portal>
          <Menubar.Content>
            <Menubar.Item>…</Menubar.Item>

            <Menubar.Item>…</Menubar.Item>

            <Menubar.Separator />

            <Menubar.CheckboxItem checked={checked} onCheckedChange={setChecked}>
              <Menubar.ItemIndicator>
                <CheckIcon />
              </Menubar.ItemIndicator>
              Checkbox item
            </Menubar.CheckboxItem>
          </Menubar.Content>
        </Menubar.Portal>
      </Menubar.Menu>
    </Menubar.Root>
  );
};
```

### [With radio items](#with-radio-items)

Use the `RadioGroup` and `RadioItem` parts to add an item that can be checked amongst others.

```jsx
import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { Menubar } from "radix-ui";

export default () => {
  const [color, setColor] = React.useState("blue");

  return (
    <Menubar.Root>
      <Menubar.Menu>
        <Menubar.Trigger>…</Menubar.Trigger>

        <Menubar.Portal>
          <Menubar.Content>
            <Menubar.RadioGroup value={color} onValueChange={setColor}>
              <Menubar.RadioItem value="red">
                <Menubar.ItemIndicator>
                  <CheckIcon />
                </Menubar.ItemIndicator>
                Red
              </Menubar.RadioItem>

              <Menubar.RadioItem value="blue">
                <Menubar.ItemIndicator>
                  <CheckIcon />
                </Menubar.ItemIndicator>
                Blue
              </Menubar.RadioItem>
            </Menubar.RadioGroup>
          </Menubar.Content>
        </Menubar.Portal>
      </Menubar.Menu>
    </Menubar.Root>
  );
};
```

### [With complex items](#with-complex-items)

You can add extra decorative elements in the `Item` parts, such as images.

```jsx
import { Menubar } from "radix-ui";

export default () => (
  <Menubar.Root>
    <Menubar.Menu>
      <Menubar.Trigger>…</Menubar.Trigger>

      <Menubar.Portal>
        <Menubar.Content>
          <Menubar.Item>
            <img src="…" />
            Adolfo Hess
          </Menubar.Item>

          <Menubar.Item>
            <img src="…" />
            Miyah Myles
          </Menubar.Item>
        </Menubar.Content>
      </Menubar.Portal>
    </Menubar.Menu>
  </Menubar.Root>
);
```

### [Constrain the content/sub-content size](#constrain-the-contentsub-content-size)

You may want to constrain the width of the content (or sub-content) so that it matches the trigger (or sub-trigger) width. You may also want to constrain its height to not exceed the viewport.

We expose several CSS custom properties such as `--radix-menubar-trigger-width` and `--radix-menubar-content-available-height` to support this. Use them to constrain the content dimensions.

```jsx
// index.jsx

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (
  <Menubar.Root>
    <Menubar.Trigger>…</Menubar.Trigger>

    <Menubar.Portal>
      <Menubar.Content className="MenubarContent" sideOffset={5}>
        …
      </Menubar.Content>
    </Menubar.Portal>
  </Menubar.Root>
);
```

```css
/* styles.css */

.MenubarContent {
  width: var(--radix-menubar-trigger-width);

  max-height: var(--radix-menubar-content-available-height);
}
```

### [Origin-aware animations](#origin-aware-animations)

We expose a CSS custom property `--radix-menubar-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```jsx
// index.jsx

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (
  <Menubar.Root>
    <Menubar.Menu>
      <Menubar.Trigger>…</Menubar.Trigger>

      <Menubar.Portal>
        <Menubar.Content className="MenubarContent">…</Menubar.Content>
      </Menubar.Portal>
    </Menubar.Menu>
  </Menubar.Root>
);
```

```css
/* styles.css */

.MenubarContent {
  transform-origin: var(--radix-menubar-content-transform-origin);

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

import { Menubar } from "radix-ui";

import "./styles.css";

export default () => (
  <Menubar.Root>
    <Menubar.Menu>
      <Menubar.Trigger>…</Menubar.Trigger>

      <Menubar.Portal>
        <Menubar.Content className="MenubarContent">…</Menubar.Content>
      </Menubar.Portal>
    </Menubar.Menu>
  </Menubar.Root>
);
```

```css
/* styles.css */

.MenubarContent {
  animation-duration: 0.6s;

  animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

.MenubarContent[data-side="top"] {
  animation-name: slideUp;
}

.MenubarContent[data-side="bottom"] {
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

Adheres to the [Menu Button WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/) and uses [roving tabindex](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/#kbd_roving_tabindex) to manage focus movement among menu items.

### [Keyboard Interactions](#keyboard-interactions)

| Key                     | Description                                                                                                                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Space`                 | When focus is on `Menubar.Trigger`, opens the menubar and focuses the first item. When focus is on an item, activates the focused item.                                                                                                                            |
| `Enter`                 | When focus is on `Menubar.Trigger`, opens the associated menu. When focus is on an item, activates the focused item.                                                                                                                                               |
| `ArrowDown`             | When focus is on `Menubar.Trigger`, opens the associated menu. When focus is on an item, moves focus to the next item.                                                                                                                                             |
| `ArrowUp`               | When focus is on an item, moves focus to the previous item.                                                                                                                                                                                                        |
| `ArrowRight``ArrowLeft` | When focus is on a `Menubar.Trigger`, moves focus to the next or previous item. When focus is on a `Menubar.SubTrigger`, opens or closes the submenu depending on reading direction. When focus is within a `Menubar.Content`, opens the next menu in the menubar. |
| `Esc`                   | Closes the currently open menu and moves focus to its<!-- --> `Menubar.Trigger`.                                                                                                                                                                                   |
