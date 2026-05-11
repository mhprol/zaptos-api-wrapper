# Toast

A succinct message that is displayed temporarily.

## Features

- Automatically closes.

- Pauses closing on hover, focus and window blur.

- Supports hotkey to jump to toast viewport.

- Supports closing via swipe gesture.

- Exposes CSS variables for swipe gesture animations.

- Can be controlled or uncontrolled.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-toast
```

## [Anatomy](#anatomy)

Import the component.

```jsx
import { Toast } from "radix-ui";

export default () => (
  <Toast.Provider>
    <Toast.Root>
      <Toast.Title />

      <Toast.Description />

      <Toast.Action />

      <Toast.Close />
    </Toast.Root>

    <Toast.Viewport />
  </Toast.Provider>
);
```

## [API Reference](#api-reference)

### [Provider](#provider)

The provider that wraps your toasts and toast viewport. It usually wraps the application.

| Prop             | Type     | Default          |
| ---------------- | -------- | ---------------- |
| `duration`       | `number` | `5000`           |
| `label*`         | `string` | `"Notification"` |
| `swipeDirection` | `enum`   | `"right"`        |
| `swipeThreshold` | `number` | `50`             |

### [Viewport](#viewport)

The fixed area where toasts appear. Users can jump to the viewport by pressing a hotkey. It is up to you to ensure the discoverability of the hotkey for keyboard users.

| Prop      | Type       | Default                      |
| --------- | ---------- | ---------------------------- |
| `asChild` | `boolean`  | `false`                      |
| `hotkey`  | `string[]` | `["F8"]`                     |
| `label`   | `string`   | `"Notifications ({hotkey})"` |

### [Root](#root)

The toast that automatically closes. It should not be held open to [acquire a user response](/primitives/docs/components/toast#action).

| Prop              | Type       | Default          |
| ----------------- | ---------- | ---------------- |
| `asChild`         | `boolean`  | `false`          |
| `type`            | `enum`     | `"foreground"`   |
| `duration`        | `number`   | No default value |
| `defaultOpen`     | `boolean`  | `true`           |
| `open`            | `boolean`  | No default value |
| `onOpenChange`    | `function` | No default value |
| `onEscapeKeyDown` | `function` | No default value |
| `onPause`         | `function` | No default value |
| `onResume`        | `function` | No default value |
| `onSwipeStart`    | `function` | No default value |
| `onSwipeMove`     | `function` | No default value |
| `onSwipeEnd`      | `function` | No default value |
| `onSwipeCancel`   | `function` | No default value |
| `forceMount`      | `boolean`  | No default value |

| Data attribute           | Values                                   |
| ------------------------ | ---------------------------------------- |
| `[data-state]`           | `"open" \| "closed"`                     |
| `[data-swipe]`           | `"start" \| "move" \| "cancel" \| "end"` |
| `[data-swipe-direction]` | `"up" \| "down" \| "left" \| "right"`    |

| CSS Variable                 | Description                                                     |
| ---------------------------- | --------------------------------------------------------------- |
| `--radix-toast-swipe-move-x` | The offset position of the toast when horizontally swiping      |
| `--radix-toast-swipe-move-y` | The offset position of the toast when vertically swiping        |
| `--radix-toast-swipe-end-x`  | The offset end position of the toast after horizontally swiping |
| `--radix-toast-swipe-end-y`  | The offset end position of the toast after vertically swiping   |

### [Title](#title)

An optional title for the toast.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Description](#description)

The toast message.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Action](#action)

An action that is safe to ignore to ensure users are not expected to complete tasks with unexpected side effects as a result of a [time limit](https://www.w3.org/TR/UNDERSTANDING-WCAG20/time-limits-required-behaviors.html).

When obtaining a user response is necessary, portal an [`AlertDialog`](/primitives/docs/components/alert-dialog) styled as a toast into the viewport instead.

| Prop       | Type      | Default          |
| ---------- | --------- | ---------------- |
| `asChild`  | `boolean` | `false`          |
| `altText*` | `string`  | No default value |

### [Close](#close)

A button that allows users to dismiss the toast before its duration has elapsed.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

## [Examples](#examples)

### [Custom hotkey](#custom-hotkey)

Override the default hotkey using the `event.code` value for each key from [keycode.info](https://keycode.info/).

```jsx
<Toast.Provider>
  {/* ... */}

  <Toast.Viewport hotkey={["altKey", "KeyT"]} />
</Toast.Provider>
```

### [Custom duration](#custom-duration)

Customise the duration of a toast to override the provider value.

```jsx
<Toast.Root duration={3000}>
  <Toast.Description>Saved!</Toast.Description>
</Toast.Root>
```

### [Duplicate toasts](#duplicate-toasts)

When a toast must appear every time a user clicks a button, use state to render multiple instances of the same toast (see below). Alternatively, you can abstract the parts to create your own [imperative API](/primitives/docs/components/toast#imperative-api).

```jsx
export default () => {
  const [savedCount, setSavedCount] = React.useState(0);

  return (
    <div>
      <form onSubmit={() => setSavedCount((count) => count + 1)}>
        {/* ... */}

        <button>save</button>
      </form>

      {Array.from({ length: savedCount }).map((_, index) => (
        <Toast.Root key={index}>
          <Toast.Description>Saved!</Toast.Description>
        </Toast.Root>
      ))}
    </div>
  );
};
```

### [Animating swipe gesture](#animating-swipe-gesture)

Combine `--radix-toast-swipe-move-[x|y]` and `--radix-toast-swipe-end-[x|y]` CSS variables with `data-swipe="[start|move|cancel|end]"` attributes to animate a swipe to close gesture. Here's an example:

```jsx
// index.jsx

import { Toast } from "radix-ui";

import "./styles.css";

export default () => (
  <Toast.Provider swipeDirection="right">
    <Toast.Root className="ToastRoot">...</Toast.Root>

    <Toast.Viewport />
  </Toast.Provider>
);
```

```css
/* styles.css */

.ToastRoot[data-swipe="move"] {
  transform: translateX(var(--radix-toast-swipe-move-x));
}

.ToastRoot[data-swipe="cancel"] {
  transform: translateX(0);

  transition: transform 200ms ease-out;
}

.ToastRoot[data-swipe="end"] {
  animation: slideRight 100ms ease-out;
}

@keyframes slideRight {
  from {
    transform: translateX(var(--radix-toast-swipe-end-x));
  }

  to {
    transform: translateX(100%);
  }
}
```

## [Accessibility](#accessibility)

Adheres to the [`aria-live` requirements](https://www.w3.org/TR/wai-aria/#aria-live).

### [Sensitivity](#sensitivity)

Control the sensitivity of the toast for screen readers using the `type` prop.

For toasts that are the result of a user action, choose `foreground`. Toasts generated from background tasks should use `background`.

#### Foreground

Foreground toasts are announced immediately. Assistive technologies may choose to clear previously queued messages when a foreground toast appears. Try to avoid stacking distinct foreground toasts at the same time.

#### Background

Background toasts are announced at the next graceful opportunity, for example, when the screen reader has finished reading its current sentence. They do not clear queued messages so overusing them can be perceived as a laggy user experience for screen reader users when used in response to a user interaction.

```jsx
<Toast.Root type="foreground">

	<Toast.Description>File removed successfully.</Toast.Description>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>



<Toast.Root type="background">

	<Toast.Description>We've just released Radix 1.0.</Toast.Description>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>
```

### [Alternative action](#alternative-action)

Use the `altText` prop on the `Action` to instruct an alternative way of actioning the toast to screen reader users.

You can direct the user to a permanent place in your application where they can action it or implement your own custom hotkey logic. If implementing the latter, use `foreground` type to announce immediately and increase the duration to give the user ample time.

```jsx
<Toast.Root type="background">

	<Toast.Title>Upgrade Available!</Toast.Title>

	<Toast.Description>We've just released Radix 1.0.</Toast.Description>

	<Toast.Action altText="Goto account settings to upgrade">

		Upgrade

	</Toast.Action>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>



<Toast.Root type="foreground" duration={10000}>

	<Toast.Description>File removed successfully.</Toast.Description>

	<Toast.Action altText="Undo (Alt+U)">

		Undo <kbd>Alt</kbd>+<kbd>U</kbd>

	</Toast.Action>

	<Toast.Close>Dismiss</Toast.Close>

</Toast.Root>
```

### [Close icon button](#close-icon-button)

When providing an icon (or font icon), remember to label it correctly for screen reader users.

```jsx
<Toast.Root type="foreground">
  <Toast.Description>Saved!</Toast.Description>

  <Toast.Close aria-label="Close">
    <span aria-hidden>×</span>
  </Toast.Close>
</Toast.Root>
```

### [Keyboard Interactions](#keyboard-interactions)

| Key           | Description                                                                   |
| ------------- | ----------------------------------------------------------------------------- |
| `F8`          | Focuses toasts viewport.                                                      |
| `Tab`         | Moves focus to the next focusable element.                                    |
| `Shift + Tab` | Moves focus to the previous focusable element.                                |
| `Space`       | When focus is on a `Toast.Action` or<!-- --> `Toast.Close`, closes the toast. |
| `Enter`       | When focus is on a `Toast.Action` or<!-- --> `Toast.Close`, closes the toast. |
| `Esc`         | When focus is on a `Toast`, closes the toast.                                 |

## [Custom APIs](#custom-apis)

### [Abstract parts](#abstract-parts)

Create your own API by abstracting the primitive parts into your own component.

#### Usage

```jsx
import { Toast } from "./your-toast";

export default () => (
  <Toast title="Upgrade available" content="We've just released Radix 3.0!">
    <button onClick={handleUpgrade}>Upgrade</button>
  </Toast>
);
```

#### Implementation

```jsx
// your-toast.jsx

import { Toast as ToastPrimitive } from "radix-ui";

export const Toast = ({ title, content, children, ...props }) => {
  return (
    <ToastPrimitive.Root {...props}>
      {title && <ToastPrimitive.Title>{title}</ToastPrimitive.Title>}

      <ToastPrimitive.Description>{content}</ToastPrimitive.Description>

      {children && <ToastPrimitive.Action asChild>{children}</ToastPrimitive.Action>}

      <ToastPrimitive.Close aria-label="Close">
        <span aria-hidden>×</span>
      </ToastPrimitive.Close>
    </ToastPrimitive.Root>
  );
};
```

### [Imperative API](#imperative-api)

Create your own imperative API to allow [toast duplication](/primitives/docs/components/toast#duplicate-toasts) if preferred.

#### Usage

```jsx
import { Toast } from "./your-toast";

export default () => {
  const savedRef = React.useRef();

  return (
    <div>
      <form onSubmit={() => savedRef.current.publish()}>
        {/* ... */}

        <button>Save</button>
      </form>

      <Toast ref={savedRef}>Saved successfully!</Toast>
    </div>
  );
};
```

#### Implementation

```jsx
// your-toast.jsx

import * as React from "react";

import { Toast as ToastPrimitive } from "radix-ui";

export const Toast = React.forwardRef((props, forwardedRef) => {
  const { children, ...toastProps } = props;

  const [count, setCount] = React.useState(0);

  React.useImperativeHandle(forwardedRef, () => ({
    publish: () => setCount((count) => count + 1),
  }));

  return (
    <>
      {Array.from({ length: count }).map((_, index) => (
        <ToastPrimitive.Root key={index} {...toastProps}>
          <ToastPrimitive.Description>{children}</ToastPrimitive.Description>

          <ToastPrimitive.Close>Dismiss</ToastPrimitive.Close>
        </ToastPrimitive.Root>
      ))}
    </>
  );
});
```
