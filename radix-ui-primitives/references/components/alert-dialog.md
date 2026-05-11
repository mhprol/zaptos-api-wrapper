# Alert Dialog

A modal dialog that interrupts the user with important content and expects a response.

## Features

- Focus is automatically trapped.

- Can be controlled or uncontrolled.

- Manages screen reader announcements with `Title` and<!-- --> `Description` components.

- Esc closes the component automatically.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-alert-dialog
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { AlertDialog } from "radix-ui";

export default () => (
  <AlertDialog.Root>
    <AlertDialog.Trigger />

    <AlertDialog.Portal>
      <AlertDialog.Overlay />

      <AlertDialog.Content>
        <AlertDialog.Title />

        <AlertDialog.Description />

        <AlertDialog.Cancel />

        <AlertDialog.Action />
      </AlertDialog.Content>
    </AlertDialog.Portal>
  </AlertDialog.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of an alert dialog.

| Prop           | Type       | Default          |
| -------------- | ---------- | ---------------- |
| `defaultOpen`  | `boolean`  | No default value |
| `open`         | `boolean`  | No default value |
| `onOpenChange` | `function` | No default value |

### [Trigger](#trigger)

A button that opens the dialog.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute | Values               |
| -------------- | -------------------- |
| `[data-state]` | `"open" \| "closed"` |

### [Portal](#portal)

When used, portals your overlay and content parts into the `body`.

| Prop         | Type          | Default          |
| ------------ | ------------- | ---------------- |
| `forceMount` | `boolean`     | No default value |
| `container`  | `HTMLElement` | `document.body`  |

### [Overlay](#overlay)

A layer that covers the inert portion of the view when the dialog is open.

| Prop         | Type      | Default          |
| ------------ | --------- | ---------------- |
| `asChild`    | `boolean` | `false`          |
| `forceMount` | `boolean` | No default value |

| Data attribute | Values               |
| -------------- | -------------------- |
| `[data-state]` | `"open" \| "closed"` |

### [Content](#content)

Contains content to be rendered when the dialog is open.

| Prop               | Type       | Default          |
| ------------------ | ---------- | ---------------- |
| `asChild`          | `boolean`  | `false`          |
| `forceMount`       | `boolean`  | No default value |
| `onOpenAutoFocus`  | `function` | No default value |
| `onCloseAutoFocus` | `function` | No default value |
| `onEscapeKeyDown`  | `function` | No default value |

| Data attribute | Values               |
| -------------- | -------------------- |
| `[data-state]` | `"open" \| "closed"` |

### [Cancel](#cancel)

A button that closes the dialog. This button should be distinguished visually from `AlertDialog.Action` buttons.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Action](#action)

A button that closes the dialog. These buttons should be distinguished visually from the `AlertDialog.Cancel` button.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Title](#title)

An accessible name to be announced when the dialog is opened. Alternatively, you can provide `aria-label` or `aria-labelledby` to `AlertDialog.Content` and exclude this component.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

### [Description](#description)

An accessible description to be announced when the dialog is opened. Alternatively, you can provide `aria-describedby` to `AlertDialog.Content` and exclude this component.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

## [Examples](#examples)

### [Close after asynchronous form submission](#close-after-asynchronous-form-submission)

Use the controlled props to programmatically close the Alert Dialog after an async operation has completed.

```jsx
import * as React from "react";

import { AlertDialog } from "radix-ui";

const wait = () => new Promise((resolve) => setTimeout(resolve, 1000));

export default () => {
  const [open, setOpen] = React.useState(false);

  return (
    <AlertDialog.Root open={open} onOpenChange={setOpen}>
      <AlertDialog.Trigger>Open</AlertDialog.Trigger>

      <AlertDialog.Portal>
        <AlertDialog.Overlay />

        <AlertDialog.Content>
          <form
            onSubmit={(event) => {
              wait().then(() => setOpen(false));
              event.preventDefault();
            }}
          >
            {/** some inputs */}

            <button type="submit">Submit</button>
          </form>
        </AlertDialog.Content>
      </AlertDialog.Portal>
    </AlertDialog.Root>
  );
};
```

### [Custom portal container](#custom-portal-container)

Customise the element that your alert dialog portals into.

```jsx
export default () => {
  const [container, setContainer] = React.useState(null);

  return (
    <div>
      <AlertDialog.Root>
        <AlertDialog.Trigger />

        <AlertDialog.Portal container={container}>
          <AlertDialog.Overlay />

          <AlertDialog.Content>...</AlertDialog.Content>
        </AlertDialog.Portal>
      </AlertDialog.Root>

      <div ref={setContainer} />
    </div>
  );
};
```

## [Accessibility](#accessibility)

Adheres to the [Alert and Message Dialogs WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/alertdialog).

### [Keyboard Interactions](#keyboard-interactions)

| Key           | Description                                                 |
| ------------- | ----------------------------------------------------------- |
| `Space`       | Opens/closes the dialog.                                    |
| `Enter`       | Opens/closes the dialog.                                    |
| `Tab`         | Moves focus to the next focusable element.                  |
| `Shift + Tab` | Moves focus to the previous focusable element.              |
| `Esc`         | Closes the dialog and moves focus to `AlertDialog.Trigger`. |
