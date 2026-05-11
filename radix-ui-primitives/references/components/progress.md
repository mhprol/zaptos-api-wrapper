# Progress

Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

## Features

- Provides context for assistive technology to read the progress of a task.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-progress
```

### [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Progress } from "radix-ui";

export default () => (
  <Progress.Root>
    <Progress.Indicator />
  </Progress.Root>
);
```

## [Accessibility](#accessibility)

Adheres to the [`progressbar` role requirements](https://www.w3.org/WAI/ARIA/apg/patterns/meter).

## [API Reference](#api-reference)

### [Root](#root)

Contains all of the progress parts.

| Prop            | Type             | Default          |
| --------------- | ---------------- | ---------------- |
| `asChild`       | `boolean`        | `false`          |
| `value`         | `number \| null` | No default value |
| `max`           | `number`         | No default value |
| `getValueLabel` | `function`       | No default value |

| Data attribute | Values                                       |
| -------------- | -------------------------------------------- |
| `[data-state]` | `"complete" \| "indeterminate" \| "loading"` |
| `[data-value]` | The current value                            |
| `[data-max]`   | The max value                                |

### [Indicator](#indicator)

Used to show the progress visually. It also makes progress accessible to assistive technologies.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute | Values                                       |
| -------------- | -------------------------------------------- |
| `[data-state]` | `"complete" \| "indeterminate" \| "loading"` |
| `[data-value]` | The current value                            |
| `[data-max]`   | The max value                                |
