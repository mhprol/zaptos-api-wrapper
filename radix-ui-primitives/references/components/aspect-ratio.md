# Aspect Ratio

Displays content within a desired ratio.

## Features

- Accepts any custom ratio.

## [Installation](#installation)

Install the component from your command line.

```bash
npm install @radix-ui/react-aspect-ratio
```

## [Anatomy](#anatomy)

Import the component.

```jsx
import { AspectRatio } from "radix-ui";

export default () => <AspectRatio.Root />;
```

## [API Reference](#api-reference)

### [Root](#root)

Contains the content you want to constrain to a given ratio.

| Prop      | Type      | Default |
| --------- | --------- | ------- |
| `asChild` | `boolean` | `false` |
| `ratio`   | `number`  | `1`     |
