# Slider

An input where the user selects a value from within a given range.

## Features

- Can be controlled or uncontrolled.

- Supports multiple thumbs.

- Supports a minimum value between thumbs.

- Supports touch or click on track to update value.

- Supports Right to Left direction.

- Full keyboard navigation.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-slider
```

## [Anatomy](#anatomy)

Import all parts and piece them together.

```jsx
import { Slider } from "radix-ui";

export default () => (
  <Slider.Root>
    <Slider.Track>
      <Slider.Range />
    </Slider.Track>

    <Slider.Thumb />
  </Slider.Root>
);
```

## [API Reference](#api-reference)

### [Root](#root)

Contains all the parts of a slider. It will render an `input` for each thumb when used within a `form` to ensure events propagate correctly.

| Prop                    | Type       | Default          |
| ----------------------- | ---------- | ---------------- |
| `asChild`               | `boolean`  | `false`          |
| `defaultValue`          | `number[]` | No default value |
| `value`                 | `number[]` | No default value |
| `onValueChange`         | `function` | No default value |
| `onValueCommit`         | `function` | No default value |
| `name`                  | `string`   | No default value |
| `disabled`              | `boolean`  | `false`          |
| `orientation`           | `enum`     | `"horizontal"`   |
| `dir`                   | `enum`     | No default value |
| `inverted`              | `boolean`  | `false`          |
| `min`                   | `number`   | `0`              |
| `max`                   | `number`   | `100`            |
| `step`                  | `number`   | `1`              |
| `minStepsBetweenThumbs` | `number`   | `0`              |
| `form`                  | `string`   | No default value |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-disabled]`    | Present when disabled        |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Track](#track)

The track that contains the `Slider.Range`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-disabled]`    | Present when disabled        |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Range](#range)

The range part. Must live inside `Slider.Track`.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-disabled]`    | Present when disabled        |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

### [Thumb](#thumb)

A draggable thumb. You can render multiple thumbs.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |

| Data attribute       | Values                       |
| -------------------- | ---------------------------- |
| `[data-disabled]`    | Present when disabled        |
| `[data-orientation]` | `"vertical" \| "horizontal"` |

## [Examples](#examples)

### [Vertical orientation](#vertical-orientation)

Use the `orientation` prop to create a vertical slider.

```jsx
// index.jsx

import { Slider } from "radix-ui";

import "./styles.css";

export default () => (
  <Slider.Root className="SliderRoot" defaultValue={[50]} orientation="vertical">
    <Slider.Track className="SliderTrack">
      <Slider.Range className="SliderRange" />
    </Slider.Track>

    <Slider.Thumb className="SliderThumb" />
  </Slider.Root>
);
```

```css
/* styles.css */

.SliderRoot {
  position: relative;

  display: flex;

  align-items: center;
}

.SliderRoot[data-orientation="vertical"] {
  flex-direction: column;

  width: 20px;

  height: 100px;
}

.SliderTrack {
  position: relative;

  flex-grow: 1;

  background-color: grey;
}

.SliderTrack[data-orientation="vertical"] {
  width: 3px;
}

.SliderRange {
  position: absolute;

  background-color: black;
}

.SliderRange[data-orientation="vertical"] {
  width: 100%;
}

.SliderThumb {
  display: block;

  width: 20px;

  height: 20px;

  background-color: black;
}
```

### [Create a range](#create-a-range)

Add multiple thumbs and values to create a range slider.

```jsx
import { Slider } from "radix-ui";

export default () => (
  <Slider.Root defaultValue={[25, 75]}>
    <Slider.Track>
      <Slider.Range />
    </Slider.Track>

    <Slider.Thumb />

    <Slider.Thumb />
  </Slider.Root>
);
```

### [Define step size](#define-step-size)

Use the `step` prop to increase the stepping interval.

```jsx
import { Slider } from "radix-ui";

export default () => (
  <Slider.Root defaultValue={[50]} step={10}>
    <Slider.Track>
      <Slider.Range />
    </Slider.Track>

    <Slider.Thumb />
  </Slider.Root>
);
```

### [Prevent thumb overlap](#prevent-thumb-overlap)

Use `minStepsBetweenThumbs` to avoid thumbs with equal values.

```jsx
import { Slider } from "radix-ui";

export default () => (
  <Slider.Root defaultValue={[25, 75]} step={10} minStepsBetweenThumbs={1}>
    <Slider.Track>
      <Slider.Range />
    </Slider.Track>

    <Slider.Thumb />

    <Slider.Thumb />
  </Slider.Root>
);
```

## [Accessibility](#accessibility)

Adheres to the [Slider WAI-ARIA design pattern](https://www.w3.org/WAI/ARIA/apg/patterns/slider-multithumb).

### [Keyboard Interactions](#keyboard-interactions)

| Key                 | Description                                                                   |
| ------------------- | ----------------------------------------------------------------------------- |
| `ArrowRight`        | Increments/decrements by the `step` value depending on<!-- --> `orientation`. |
| `ArrowLeft`         | Increments/decrements by the `step` value depending on<!-- --> `orientation`. |
| `ArrowUp`           | Increases the value by the `step` amount.                                     |
| `ArrowDown`         | Decreases the value by the `step` amount.                                     |
| `PageUp`            | Increases the value by a larger `step`.                                       |
| `PageDown`          | Decreases the value by a larger `step`.                                       |
| `Shift + ArrowUp`   | Increases the value by a larger `step`.                                       |
| `Shift + ArrowDown` | Decreases the value by a larger `step`.                                       |
| `Home`              | Sets the value to its minimum.                                                |
| `End`               | Sets the value to its maximum.                                                |

## [Custom APIs](#custom-apis)

Create your own API by abstracting the primitive parts into your own component.

### [Abstract all parts](#abstract-all-parts)

This example abstracts all of the `Slider` parts so it can be used as a self closing element.

#### Usage

```jsx
import { Slider } from "./your-slider";

export default () => <Slider defaultValue={[25]} />;
```

#### Implementation

```jsx
// your-slider.jsx

import { Slider as SliderPrimitive } from "radix-ui";

export const Slider = React.forwardRef((props, forwardedRef) => {
  const value = props.value || props.defaultValue;

  return (
    <SliderPrimitive.Slider {...props} ref={forwardedRef}>
      <SliderPrimitive.Track>
        <SliderPrimitive.Range />
      </SliderPrimitive.Track>

      {value.map((_, i) => (
        <SliderPrimitive.Thumb key={i} />
      ))}
    </SliderPrimitive.Slider>
  );
});
```

## [Caveats](#caveats)

### [Mouse events are not fired](#mouse-events-are-not-fired)

Because of [a limitation](https://github.com/radix-ui/primitives/blob/83a8c13bf66f3d9f17d77caeb187a69eb146930b/packages/react/slider/src/Slider.tsx#L383-L384) we faced during implementation, the following example won't work as expected and the `onMouseDown` and `onMouseUp` event handlers won't be fired:

```jsx
<Slider.Root
  onMouseDown={() => console.log("onMouseDown")}
  onMouseUp={() => console.log("onMouseUp")}
>
  …
</Slider.Root>
```

We recommend using pointer events instead (eg. `onPointerDown`, `onPointerUp`). Regardless of the above limitation, these events are better suited for cross-platform/device handling as they are fired for all pointer input types (mouse, touch, pen, etc.).
