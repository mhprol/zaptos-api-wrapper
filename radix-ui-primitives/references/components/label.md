# Label

Renders an accessible label associated with controls.

## Features

- Text selection is prevented when double clicking label.

- Supports nested controls.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-label
```

## [Anatomy](#anatomy)

Import the component.

```jsx
import { Label } from "radix-ui";

export default () => <Label.Root />;
```

## [API Reference](#api-reference)

### [Root](#root)

Contains the content for the label.

| Prop      | Type      | Default          |
| --------- | --------- | ---------------- |
| `asChild` | `boolean` | `false`          |
| `htmlFor` | `string`  | No default value |

## [Accessibility](#accessibility)

This component is based on the native `label` element, it will automatically apply the correct labelling when wrapping controls or using the `htmlFor` attribute. For your own custom controls to work correctly, ensure they use native elements such as `button` or `input` as a base.
