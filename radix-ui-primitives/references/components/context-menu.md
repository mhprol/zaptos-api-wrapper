# Context Menu

Displays a menu located at the pointer, triggered by a right click or a long press.

## Features

- Supports submenus with configurable reading direction.

- Supports items, labels, groups of items.

- Supports checkable items (single or multiple) with optional indeterminate state.

- Supports modal and non-modal modes.

- Customize side, alignment, offsets, collision handling.

- Focus is fully managed.

- Full keyboard navigation.

- Typeahead support.

- Dismissing and layering behavior is highly customizable.

- Triggers with a long press on touch devices

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-context-menu
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { ContextMenu } from "radix-ui";

export default () => (
  <ContextMenu.Root>
    <ContextMenu.Trigger />

    <ContextMenu.Portal>
      <ContextMenu.Content>
        <ContextMenu.Label />

        <ContextMenu.Item />

        <ContextMenu.Group>
          <ContextMenu.Item />
        </ContextMenu.Group>

        <ContextMenu.CheckboxItem>
          <ContextMenu.ItemIndicator />
        </ContextMenu.CheckboxItem>

        <ContextMenu.RadioGroup>
          <ContextMenu.RadioItem>
            <ContextMenu.ItemIndicator />
          </ContextMenu.RadioItem>
        </ContextMenu.RadioGroup>

        <ContextMenu.Sub>
          <ContextMenu.SubTrigger />

          <ContextMenu.Portal>
            <ContextMenu.SubContent />
          </ContextMenu.Portal>
        </ContextMenu.Sub>

        <ContextMenu.Separator />
      </ContextMenu.Content>
    </ContextMenu.Portal>
  </ContextMenu.Root>
);
```

## [API Reference](#api-reference)

Adheres to the [Menu WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/menu) and uses [roving tabindex](https://www.w3.org/TR/wai-aria-practices-1.2/examples/menu-button/menu-button-actions.html) to manage focus movement among menu items.

### [Root](#root)

Contains all the parts of a context menu.

| Prop           | Type       | Default          |
| -------------- | ---------- | ---------------- |
| `dir`          | `enum`     | No default value |
| `onOpenChange` | `function` | No default value |
| `modal`        | `boolean`  | `true`           |

### [Trigger](#trigger)

The area that opens the context menu. Wrap it around the target you want the context menu to open from when right-clicking (or using the relevant keyboard shortcuts).

| Prop       | Type      | Default |
| ---------- | --------- | ------- |
| `asChild`  | `boolean` | `false` |
| `disabled` | `boolean` | `false` |

| Data attribute | Values               |
| -------------- | -------------------- |
| `[data-state]` | `"open" \| "closed"` |

### [Portal](#portal)

When used, portals the content part into the `body`.

| Prop         | Type          | Default          |
| ------------ | ------------- | ---------------- |
| `forceMount` | `boolean`     | No default value |
| `container`  | `HTMLElement` | `document.body`  |

### [Content](#content)

The component that pops out in an open context menu.

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
| `alignOffset`          | `number`            | `0`              |
| `avoidCollisions`      | `boolean`           | `true`           |
| `collisionBoundary`    | `Boundary`          | `[]`             |
| `collisionPadding`     | `number \| Padding` | `0`              |
| `sticky`               | `enum`              | `"partial"`      |
| `hideWhenDetached`     | `boolean`           | `false`          |

| Data attribute | Values                                   |
| -------------- | ---------------------------------------- |
| `[data-state]` | `"open" \| "closed"`                     |
| `[data-side]`  | `"left" \| "right" \| "bottom" \| "top"` |
| `[data-align]` | `"start" \| "end" \| "center"`           |

| CSS Variable                                    | Description                                                                  |
| ----------------------------------------------- | ---------------------------------------------------------------------------- |
| `--radix-context-menu-content-transform-origin` | The `transform-origin` computed from the content and arrow positions/offsets |
| `--radix-context-menu-content-available-width`  | The remaining width between the trigger and the boundary edge                |
| `--radix-context-menu-content-available-height` | The remaining height between the trigger and the boundary edge               |
| `--radix-context-menu-trigger-width`            | The width of the trigger                                                     |
| `--radix-context-menu-trigger-height`           | The height of the trigger                                                    |

### [Arrow](#arrow)

An optional arrow element to render alongside a submenu. This can be used to help visually link the trigger item with the `ContextMenu.Content`. Must be rendered inside `ContextMenu.Content`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |
| `width`   | `number`  | `10`    |
| `height`  | `number`  | `5`     |

### [Item](#item)

The component that contains the context menu items.

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

Used to group multiple `ContextMenu.Item`s.

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

| Data attribute       | Values                                        |
| -------------------- | --------------------------------------------- |
| `[data-state]`       | `"checked" \| "unchecked" \| "indeterminate"` |
| `[data-highlighted]` | Present when highlighted                      |
| `[data-disabled]`    | Present when disabled                         |

### [RadioGroup](#radiogroup)

Used to group multiple `ContextMenu.RadioItem`s.

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

| Data attribute       | Values                                        |
| -------------------- | --------------------------------------------- |
| `[data-state]`       | `"checked" \| "unchecked" \| "indeterminate"` |
| `[data-highlighted]` | Present when highlighted                      |
| `[data-disabled]`    | Present when disabled                         |

### [ItemIndicator](#itemindicator)

Renders when the parent `ContextMenu.CheckboxItem` or `ContextMenu.RadioItem` is checked. You can style this element directly, or you can use it as a wrapper to put an icon into, or both.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute | Values                                        |
| -------------- | --------------------------------------------- |
| `[data-state]` | `"checked" \| "unchecked" \| "indeterminate"` |

### [Separator](#separator)

Used to visually separate items in the context menu.

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

An item that opens a submenu. Must be rendered inside `ContextMenu.Sub`.

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

The component that pops out when a submenu is open. Must be rendered inside `ContextMenu.Sub`.

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

| Data attribute | Values                                   |
| -------------- | ---------------------------------------- |
| `[data-state]` | `"open" \| "closed"`                     |
| `[data-side]`  | `"left" \| "right" \| "bottom" \| "top"` |
| `[data-align]` | `"start" \| "end" \| "center"`           |

| CSS Variable                                    | Description                                                                  |
| ----------------------------------------------- | ---------------------------------------------------------------------------- |
| `--radix-context-menu-content-transform-origin` | The `transform-origin` computed from the content and arrow positions/offsets |
| `--radix-context-menu-content-available-width`  | The remaining width between the trigger and the boundary edge                |
| `--radix-context-menu-content-available-height` | The remaining height between the trigger and the boundary edge               |
| `--radix-context-menu-trigger-width`            | The width of the trigger                                                     |
| `--radix-context-menu-trigger-height`           | The height of the trigger                                                    |

## [Examples](#examples)

### [With submenus](#with-submenus)

You can create submenus by using `ContextMenu.Sub` in combination with its parts.

```jsx
<ContextMenu.Root>
  <ContextMenu.Trigger>…</ContextMenu.Trigger>

  <ContextMenu.Portal>
    <ContextMenu.Content>
      <ContextMenu.Item>…</ContextMenu.Item>

      <ContextMenu.Item>…</ContextMenu.Item>

      <ContextMenu.Separator />

      <ContextMenu.Sub>
        <ContextMenu.SubTrigger>Sub menu →</ContextMenu.SubTrigger>

        <ContextMenu.Portal>
          <ContextMenu.SubContent>
            <ContextMenu.Item>Sub menu item</ContextMenu.Item>

            <ContextMenu.Item>Sub menu item</ContextMenu.Item>

            <ContextMenu.Arrow />
          </ContextMenu.SubContent>
        </ContextMenu.Portal>
      </ContextMenu.Sub>

      <ContextMenu.Separator />

      <ContextMenu.Item>…</ContextMenu.Item>
    </ContextMenu.Content>
  </ContextMenu.Portal>
</ContextMenu.Root>
```

### [With disabled items](#with-disabled-items)

You can add special styles to disabled items via the `data-disabled` attribute.

```jsx
// index.jsx

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (
  <ContextMenu.Root>
    <ContextMenu.Trigger>…</ContextMenu.Trigger>

    <ContextMenu.Portal>
      <ContextMenu.Content>
        <ContextMenu.Item className="ContextMenuItem" disabled>
          …
        </ContextMenu.Item>

        <ContextMenu.Item className="ContextMenuItem">…</ContextMenu.Item>
      </ContextMenu.Content>
    </ContextMenu.Portal>
  </ContextMenu.Root>
);
```

```css
/* styles.css */

.ContextMenuItem[data-disabled] {
  color: gainsboro;
}
```

### [With separators](#with-separators)

Use the `Separator` part to add a separator between items.

```jsx
<ContextMenu.Root>
  <ContextMenu.Trigger>…</ContextMenu.Trigger>

  <ContextMenu.Portal>
    <ContextMenu.Content>
      <ContextMenu.Item>…</ContextMenu.Item>

      <ContextMenu.Separator />

      <ContextMenu.Item>…</ContextMenu.Item>

      <ContextMenu.Separator />

      <ContextMenu.Item>…</ContextMenu.Item>
    </ContextMenu.Content>
  </ContextMenu.Portal>
</ContextMenu.Root>
```

### [With labels](#with-labels)

Use the `Label` part to help label a section.

```jsx
<ContextMenu.Root>
  <ContextMenu.Trigger>…</ContextMenu.Trigger>

  <ContextMenu.Portal>
    <ContextMenu.Content>
      <ContextMenu.Label>Label</ContextMenu.Label>

      <ContextMenu.Item>…</ContextMenu.Item>

      <ContextMenu.Item>…</ContextMenu.Item>

      <ContextMenu.Item>…</ContextMenu.Item>
    </ContextMenu.Content>
  </ContextMenu.Portal>
</ContextMenu.Root>
```

### [With checkbox items](#with-checkbox-items)

Use the `CheckboxItem` part to add an item that can be checked.

```jsx
import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { ContextMenu } from "radix-ui";

export default () => {
  const [checked, setChecked] = React.useState(true);

  return (
    <ContextMenu.Root>
      <ContextMenu.Trigger>…</ContextMenu.Trigger>

      <ContextMenu.Portal>
        <ContextMenu.Content>
          <ContextMenu.Item>…</ContextMenu.Item>

          <ContextMenu.Item>…</ContextMenu.Item>

          <ContextMenu.Separator />

          <ContextMenu.CheckboxItem checked={checked} onCheckedChange={setChecked}>
            <ContextMenu.ItemIndicator>
              <CheckIcon />
            </ContextMenu.ItemIndicator>
            Checkbox item
          </ContextMenu.CheckboxItem>
        </ContextMenu.Content>
      </ContextMenu.Portal>
    </ContextMenu.Root>
  );
};
```

### [With radio items](#with-radio-items)

Use the `RadioGroup` and `RadioItem` parts to add an item that can be checked amongst others.

```jsx
import * as React from "react";

import { CheckIcon } from "@radix-ui/react-icons";

import { ContextMenu } from "radix-ui";

export default () => {
  const [color, setColor] = React.useState("blue");

  return (
    <ContextMenu.Root>
      <ContextMenu.Trigger>…</ContextMenu.Trigger>

      <ContextMenu.Portal>
        <ContextMenu.Content>
          <ContextMenu.RadioGroup value={color} onValueChange={setColor}>
            <ContextMenu.RadioItem value="red">
              <ContextMenu.ItemIndicator>
                <CheckIcon />
              </ContextMenu.ItemIndicator>
              Red
            </ContextMenu.RadioItem>

            <ContextMenu.RadioItem value="blue">
              <ContextMenu.ItemIndicator>
                <CheckIcon />
              </ContextMenu.ItemIndicator>
              Blue
            </ContextMenu.RadioItem>

            <ContextMenu.RadioItem value="green">
              <ContextMenu.ItemIndicator>
                <CheckIcon />
              </ContextMenu.ItemIndicator>
              Green
            </ContextMenu.RadioItem>
          </ContextMenu.RadioGroup>
        </ContextMenu.Content>
      </ContextMenu.Portal>
    </ContextMenu.Root>
  );
};
```

### [With complex items](#with-complex-items)

You can add extra decorative elements in the `Item` parts, such as images.

```jsx
import { ContextMenu } from "radix-ui";

export default () => (
  <ContextMenu.Root>
    <ContextMenu.Trigger>…</ContextMenu.Trigger>

    <ContextMenu.Portal>
      <ContextMenu.Content>
        <ContextMenu.Item>
          <img src="…" />
          Adolfo Hess
        </ContextMenu.Item>

        <ContextMenu.Item>
          <img src="…" />
          Miyah Myles
        </ContextMenu.Item>
      </ContextMenu.Content>
    </ContextMenu.Portal>
  </ContextMenu.Root>
);
```

### [Constrain the content/sub-content size](#constrain-the-contentsub-content-size)

You may want to constrain the width of the content (or sub-content) so that it matches the trigger (or sub-trigger) width. You may also want to constrain its height to not exceed the viewport.

We expose several CSS custom properties such as `--radix-context-menu-trigger-width` and `--radix-context-menu-content-available-height` to support this. Use them to constrain the content dimensions.

```jsx
// index.jsx

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (
  <ContextMenu.Root>
    <ContextMenu.Trigger>…</ContextMenu.Trigger>

    <ContextMenu.Portal>
      <ContextMenu.Content className="ContextMenuContent">…</ContextMenu.Content>
    </ContextMenu.Portal>
  </ContextMenu.Root>
);
```

```css
/* styles.css */

.ContextMenuContent {
  width: var(--radix-context-menu-trigger-width);

  max-height: var(--radix-context-menu-content-available-height);
}
```

### [Origin-aware animations](#origin-aware-animations)

We expose a CSS custom property `--radix-context-menu-content-transform-origin`. Use it to animate the content from its computed origin based on `side`, `sideOffset`, `align`, `alignOffset` and any collisions.

```jsx
// index.jsx

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (
  <ContextMenu.Root>
    <ContextMenu.Trigger>…</ContextMenu.Trigger>

    <ContextMenu.Portal>
      <ContextMenu.Content className="ContextMenuContent">…</ContextMenu.Content>
    </ContextMenu.Portal>
  </ContextMenu.Root>
);
```

```css
/* styles.css */

.ContextMenuContent {
  transform-origin: var(--radix-context-menu-content-transform-origin);

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

import { ContextMenu } from "radix-ui";

import "./styles.css";

export default () => (
  <ContextMenu.Root>
    <ContextMenu.Trigger>…</ContextMenu.Trigger>

    <ContextMenu.Portal>
      <ContextMenu.Content className="ContextMenuContent">…</ContextMenu.Content>
    </ContextMenu.Portal>
  </ContextMenu.Root>
);
```

```css
/* styles.css */

.ContextMenuContent {
  animation-duration: 0.6s;

  animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1);
}

.ContextMenuContent[data-side="top"] {
  animation-name: slideUp;
}

.ContextMenuContent[data-side="bottom"] {
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

Uses [roving tabindex](https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/#kbd_roving_tabindex) to manage focus movement among menu items.

### [Keyboard Interactions](#keyboard-interactions)

| Key                     | Description                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| `Space`                 | Activates the focused item.                                                                            |
| `Enter`                 | Activates the focused item.                                                                            |
| `ArrowDown`             | Moves focus to the next item.                                                                          |
| `ArrowUp`               | Moves focus to the previous item.                                                                      |
| `ArrowRight``ArrowLeft` | When focus is on `ContextMenu.SubTrigger`, opens or closes the submenu depending on reading direction. |
| `Esc`                   | Closes the context menu                                                                                |
