# Navigation Menu

A collection of links for navigating websites.

## Features

- Can be controlled or uncontrolled.

- Flexible layout structure with managed tab focus.

- Supports submenus.

- Optional active item indicator.

- Full keyboard navigation.

- Exposes CSS variables for advanced animation.

- Supports custom timings.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-navigation-menu
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { NavigationMenu } from "radix-ui";

export default () => (
  <NavigationMenu.Root>
    <NavigationMenu.List>
      <NavigationMenu.Item>
        <NavigationMenu.Trigger />

        <NavigationMenu.Content>
          <NavigationMenu.Link />
        </NavigationMenu.Content>
      </NavigationMenu.Item>

      <NavigationMenu.Item>
        <NavigationMenu.Link />
      </NavigationMenu.Item>

      <NavigationMenu.Item>
        <NavigationMenu.Trigger />

        <NavigationMenu.Content>
          <NavigationMenu.Sub>
            <NavigationMenu.List />

            <NavigationMenu.Viewport />
          </NavigationMenu.Sub>
        </NavigationMenu.Content>
      </NavigationMenu.Item>

      <NavigationMenu.Indicator />
    </NavigationMenu.List>

    <NavigationMenu.Viewport />
  </NavigationMenu.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a navigation menu.

| Prop                | Type       | Default          |
| ------------------- | ---------- | ---------------- |
| `defaultValue`      | `string`   | No default value |
| `value`             | `string`   | No default value |
| `onValueChange`     | `function` | No default value |
| `delayDuration`     | `number`   | `200`            |
| `skipDelayDuration` | `number`   | `300`            |
| `dir`               | `enum`     | No default value |
| `orientation`       | `enum`     | `"horizontal"`   |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Sub](#sub)

Signifies a submenu. Use it in place of the root part when nested to create a submenu.

| Prop            | Type       | Default          |
| --------------- | ---------- | ---------------- |
| `defaultValue`  | `string`   | No default value |
| `value`         | `string`   | No default value |
| `onValueChange` | `function` | No default value |
| `orientation`   | `enum`     | `"horizontal"`   |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [List](#list)

Contains the top level menu items.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Item](#item)

A top level menu item, contains a link or trigger with content combination.

| Prop      | Type      | Default          |
| --------- | --------- | ---------------- |
| `asChild` | `boolean` | `false`          |
| `value`   | `string`  | No default value |

### [Trigger](#trigger)

The button that toggles the content.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute    | Values                |
| ----------------- | --------------------- |
| `[data-state]`    | `"open" \| "closed"`  |
| `[data-disabled]` | Present when disabled |

### [Content](#content)

Contains the content associated with each trigger.

| Prop                   | Type       | Default          |
| ---------------------- | ---------- | ---------------- |
| `asChild`              | `boolean`  | `false`          |
| `onEscapeKeyDown`      | `function` | No default value |
| `onPointerDownOutside` | `function` | No default value |
| `onFocusOutside`       | `function` | No default value |
| `onInteractOutside`    | `function` | No default value |
| `forceMount`           | `boolean`  | No default value |

| Data attribute       | Values                                                 |
| -------------------- | ------------------------------------------------------ |
| `[data-state]`       | `"open" \| "closed"`                                   |
| `[data-motion]`      | `"to-start" \| "to-end" \| "from-start" \| "from-end"` |
| `[data-orientation]` | `"vertical" \| "horizontal"`                           |

### [Link](#link)

A navigational link.

| Prop       | Type       | Default          |
| ---------- | ---------- | ---------------- |
| `asChild`  | `boolean`  | `false`          |
| `active`   | `boolean`  | `false`          |
| `onSelect` | `function` | No default value |

| Data attribute  | Values              |
| --------------- | ------------------- |
| `[data-active]` | Present when active |

### [Indicator](#indicator)

An optional indicator element that renders below the list, is used to highlight the currently active trigger.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-state]`       | `"visible" \| "hidden"`      |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Viewport](#viewport)

An optional viewport element that is used to render active content outside of the list.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-state]`       | `"open" \| "closed"`         |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

| CSS Variable                              | Description                                                                      |
| ----------------------------------------- | -------------------------------------------------------------------------------- |
| `--radix-navigation-menu-viewport-width`  | The width of the viewport when visible/hidden, computed from the active content  |
| `--radix-navigation-menu-viewport-height` | The height of the viewport when visible/hidden, computed from the active content |

## [Examples](#examples)

### [Vertical](#vertical)

You can create a vertical menu by using the `orientation` prop.

```jsx
<NavigationMenu.Root orientation="vertical">
  <NavigationMenu.List>
    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

      <NavigationMenu.Content>Item one content</NavigationMenu.Content>
    </NavigationMenu.Item>

    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

      <NavigationMenu.Content>Item Two content</NavigationMenu.Content>
    </NavigationMenu.Item>
  </NavigationMenu.List>
</NavigationMenu.Root>
```

### [Flexible layouts](#flexible-layouts)

Use the `Viewport` part when you need extra control over where `Content` is rendered. This can be helpful when your design requires an adjusted DOM structure or if you need flexibility to achieve [advanced animation](/primitives/docs/components/navigation-menu#advanced-animation). Tab focus will be maintained automatically.

```jsx
<NavigationMenu.Root>
  <NavigationMenu.List>
    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

      <NavigationMenu.Content>Item one content</NavigationMenu.Content>
    </NavigationMenu.Item>

    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

      <NavigationMenu.Content>Item two content</NavigationMenu.Content>
    </NavigationMenu.Item>
  </NavigationMenu.List>

  {/* NavigationMenu.Content will be rendered here when active */}

  <NavigationMenu.Viewport />
</NavigationMenu.Root>
```

### [With indicator](#with-indicator)

You can use the optional `Indicator` part to highlight the currently active `Trigger`, this is useful when you want to provide an animated visual cue such as an arrow or highlight to accompany the `Viewport`.

```jsx
// index.jsx

import { NavigationMenu } from "radix-ui";

import "./styles.css";

export default () => (
  <NavigationMenu.Root>
    <NavigationMenu.List>
      <NavigationMenu.Item>
        <NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

        <NavigationMenu.Content>Item one content</NavigationMenu.Content>
      </NavigationMenu.Item>

      <NavigationMenu.Item>
        <NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

        <NavigationMenu.Content>Item two content</NavigationMenu.Content>
      </NavigationMenu.Item>

      <NavigationMenu.Indicator className="NavigationMenuIndicator" />
    </NavigationMenu.List>

    <NavigationMenu.Viewport />
  </NavigationMenu.Root>
);
```

```css
/* styles.css */

.NavigationMenuIndicator {
  background-color: grey;
}

.NavigationMenuIndicator[data-orientation="horizontal"] {
  height: 3px;

  transition:
    width,
    transform,
    250ms ease;
}
```

### [With submenus](#with-submenus)

Create a submenu by nesting your `NavigationMenu` and using the `Sub` part in place of its `Root`. Submenus work differently to `Root` navigation menus and are similar to [`Tabs`](/primitives/docs/components/tabs) in that one item should always be active, so be sure to assign and set a `defaultValue`.

```jsx
<NavigationMenu.Root>
  <NavigationMenu.List>
    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

      <NavigationMenu.Content>Item one content</NavigationMenu.Content>
    </NavigationMenu.Item>

    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

      <NavigationMenu.Content>
        <NavigationMenu.Sub defaultValue="sub1">
          <NavigationMenu.List>
            <NavigationMenu.Item value="sub1">
              <NavigationMenu.Trigger>Sub item one</NavigationMenu.Trigger>

              <NavigationMenu.Content>Sub item one content</NavigationMenu.Content>
            </NavigationMenu.Item>

            <NavigationMenu.Item value="sub2">
              <NavigationMenu.Trigger>Sub item two</NavigationMenu.Trigger>

              <NavigationMenu.Content>Sub item two content</NavigationMenu.Content>
            </NavigationMenu.Item>
          </NavigationMenu.List>
        </NavigationMenu.Sub>
      </NavigationMenu.Content>
    </NavigationMenu.Item>
  </NavigationMenu.List>
</NavigationMenu.Root>
```

### [With client side routing](#with-client-side-routing)

If you need to use the `Link` component provided by your routing package then we recommend composing with `NavigationMenu.Link` via a custom component. This will ensure accessibility and consistent keyboard control is maintained. Here's an example using Next.js:

```jsx
// index.jsx

import { usePathname } from "next/navigation";

import NextLink from "next/link";

import { NavigationMenu } from "radix-ui";

import "./styles.css";

const Link = ({ href, ...props }) => {
  const pathname = usePathname();

  const isActive = href === pathname;

  return (
    <NavigationMenu.Link asChild active={isActive}>
      <NextLink href={href} className="NavigationMenuLink" {...props} />
    </NavigationMenu.Link>
  );
};

export default () => (
  <NavigationMenu.Root>
    <NavigationMenu.List>
      <NavigationMenu.Item>
        <Link href="/">Home</Link>
      </NavigationMenu.Item>

      <NavigationMenu.Item>
        <Link href="/about">About</Link>
      </NavigationMenu.Item>
    </NavigationMenu.List>
  </NavigationMenu.Root>
);
```

```css
/* styles.css */

.NavigationMenuLink {
  text-decoration: none;
}

.NavigationMenuLink[data-active] {
  text-decoration: "underline";
}
```

### [Advanced animation](#advanced-animation)

We expose `--radix-navigation-menu-viewport-[width|height]` and `data-motion['from-start'|'to-start'|'from-end'|'to-end']` attributes to allow you to animate `Viewport` size and `Content` position based on the enter/exit direction.

Combining these with `position: absolute;` allows you to create smooth overlapping animation effects when moving between items.

```jsx
// index.jsx

import { NavigationMenu } from "radix-ui";

import "./styles.css";

export default () => (
  <NavigationMenu.Root>
    <NavigationMenu.List>
      <NavigationMenu.Item>
        <NavigationMenu.Trigger>Item one</NavigationMenu.Trigger>

        <NavigationMenu.Content className="NavigationMenuContent">
          Item one content
        </NavigationMenu.Content>
      </NavigationMenu.Item>

      <NavigationMenu.Item>
        <NavigationMenu.Trigger>Item two</NavigationMenu.Trigger>

        <NavigationMenu.Content className="NavigationMenuContent">
          Item two content
        </NavigationMenu.Content>
      </NavigationMenu.Item>
    </NavigationMenu.List>

    <NavigationMenu.Viewport className="NavigationMenuViewport" />
  </NavigationMenu.Root>
);
```

```css
/* styles.css */

.NavigationMenuContent {
  position: absolute;

  top: 0;

  left: 0;

  animation-duration: 250ms;

  animation-timing-function: ease;
}

.NavigationMenuContent[data-motion="from-start"] {
  animation-name: enterFromLeft;
}

.NavigationMenuContent[data-motion="from-end"] {
  animation-name: enterFromRight;
}

.NavigationMenuContent[data-motion="to-start"] {
  animation-name: exitToLeft;
}

.NavigationMenuContent[data-motion="to-end"] {
  animation-name: exitToRight;
}

.NavigationMenuViewport {
  position: relative;

  width: var(--radix-navigation-menu-viewport-width);

  height: var(--radix-navigation-menu-viewport-height);

  transition:
    width,
    height,
    250ms ease;
}

@keyframes enterFromRight {
  from {
    opacity: 0;

    transform: translateX(200px);
  }

  to {
    opacity: 1;

    transform: translateX(0);
  }
}

@keyframes enterFromLeft {
  from {
    opacity: 0;

    transform: translateX(-200px);
  }

  to {
    opacity: 1;

    transform: translateX(0);
  }
}

@keyframes exitToRight {
  from {
    opacity: 1;

    transform: translateX(0);
  }

  to {
    opacity: 0;

    transform: translateX(200px);
  }
}

@keyframes exitToLeft {
  from {
    opacity: 1;

    transform: translateX(0);
  }

  to {
    opacity: 0;

    transform: translateX(-200px);
  }
}
```

## [Accessibility](#accessibility)

Adheres to the [`navigation` role requirements](https://www.w3.org/TR/wai-aria-1.2/#navigation).

### [Differences to menubar](#differences-to-menubar)

`NavigationMenu` should not be confused with `menubar`, although this primitive shares the name `menu` in the colloquial sense to refer to a set of navigation links, it does not use the WAI-ARIA `menu` role. This is because `menu` and `menubars` behave like native operating system menus most commonly found in desktop application windows, as such they feature complex functionality like composite focus management and first-character navigation.

These features are often considered [unnecessary for website navigation](https://github.com/w3c/aria-practices/issues/353) and at worst can confuse users who are familiar with established website patterns.

See the W3C [Disclosure Navigation Menu](https://w3c.github.io/aria-practices/examples/disclosure/disclosure-navigation.html) example for more information.

### [Link usage and aria-current](#link-usage-and-aria-current)

It's important to use `NavigationMenu.Link` for all navigational links within a menu, this not only applies to the main list but also within any content rendered via `NavigationMenu.Content`. This will ensure consistent keyboard interactions and accessibility while also giving access to the `active` prop for setting `aria-current` and the active styles. See [this example](/primitives/docs/components/navigation-menu#with-client-side-routing) for more information on usage with third party routing components.

### [Keyboard Interactions](#keyboard-interactions)

| Key                     | Description                                                                                                                                                                                                                    |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Space``Enter`          | When focus is on `NavigationMenu.Trigger`, opens the content.                                                                                                                                                                  |
| `Tab`                   | Moves focus to the next focusable element.                                                                                                                                                                                     |
| `ArrowDown`             | When `horizontal` and focus is on an open<!-- --> `NavigationMenu.Trigger`, moves focus into<!-- --> `NavigationMenu.Content`. Moves focus to the next `NavigationMenu.Trigger` or<!-- --> `NavigationMenu.Link`.              |
| `ArrowUp`               | Moves focus to the previous `NavigationMenu.Trigger` or<!-- --> `NavigationMenu.Link`.                                                                                                                                         |
| `ArrowRight``ArrowLeft` | When `vertical` and focus is on an open<!-- --> `NavigationMenu.Trigger`, moves focus into its<!-- --> `NavigationMenu.Content`. Moves focus to the next / previous `NavigationMenu.Trigger` <!-- -->or `NavigationMenu.Link`. |
| `Home``End`             | Moves focus to the first/last `NavigationMenu.Trigger` or<!-- --> `NavigationMenu.Link`.                                                                                                                                       |
| `Esc`                   | Closes open `NavigationMenu.Content` and moves focus to its<!-- --> `NavigationMenu.Trigger`.                                                                                                                                  |
