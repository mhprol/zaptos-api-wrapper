# Styling

Radix Primitives are unstyled—and compatible with any styling solution—giving you complete control over styling.

## [Styling overview](#styling-overview)

### [Functional styles](#functional-styles)

You are in control of all aspects of styling, including functional styles. For example—by default—a [Dialog Overlay](/primitives/docs/components/dialog) won't cover the entire viewport. You're responsible for adding those styles, plus any presentation styles.

### [Classes](#classes)

All components and their parts accept a `className` prop. This class will be passed through to the DOM element. You can use it in CSS as expected.

### [Data attributes](#data-attributes)

When components are stateful, their state will be exposed in a `data-state` attribute. For example, when an [Accordion Item](/primitives/docs/components/accordion) is opened, it includes a `data-state="open"` attribute.

## [Styling with CSS](#styling-with-css)

### [Styling a part](#styling-a-part)

You can style a component part by targeting the `className` that you provide.

```jsx
import * as React from "react";

import { Accordion } from "radix-ui";

import "./styles.css";

const AccordionDemo = () => (
  <Accordion.Root>
    <Accordion.Item className="AccordionItem" value="item-1" />

    {/* … */}
  </Accordion.Root>
);

export default AccordionDemo;
```

### [Styling a state](#styling-a-state)

You can style a component state by targeting its `data-state` attribute.

```css
.AccordionItem {
  border-bottom: 1px solid gainsboro;
}

.AccordionItem[data-state="open"] {
  border-bottom-width: 2px;
}
```

## [Styling with CSS-in-JS](#styling-with-css-in-js)

The examples below are using [styled-components](https://styled-components.com/), but you can use any CSS-in-JS library of your choice.

### [Styling a part](#styling-a-part-1)

Most CSS-in-JS libraries export a function for passing components and their styles. You can provide the Radix primitive component directly.

```jsx
import * as React from "react";

import { Accordion } from "radix-ui";

import styled from "styled-components";

const StyledItem = styled(Accordion.Item)`
  border-bottom: 1px solid gainsboro;
`;

const AccordionDemo = () => (
  <Accordion.Root>
    <StyledItem value="item-1" />

    {/* … */}
  </Accordion.Root>
);

export default AccordionDemo;
```

### [Styling a state](#styling-a-state-1)

You can style a component state by targeting its `data-state` attribute.

```jsx
import { Accordion } from "radix-ui";

import styled from "styled-components";

const StyledItem = styled(Accordion.Item)`
  border-bottom: 1px solid gainsboro;

  &[data-state="open"] {
    border-bottom-width: 2px;
  }
`;
```

## [Extending a primitive](#extending-a-primitive)

Extending a primitive is done the same way you extend any React component.

```tsx
import * as React from "react";

import { Accordion as AccordionPrimitive } from "radix-ui";

const AccordionItem = React.forwardRef<
  React.ElementRef<typeof AccordionPrimitive.Item>,
  React.ComponentPropsWithoutRef<typeof AccordionPrimitive.Item>
>((props, forwardedRef) => <AccordionPrimitive.Item {...props} ref={forwardedRef} />);

AccordionItem.displayName = "AccordionItem";
```

## [Summary](#summary)

Radix Primitives were designed to encapsulate accessibility concerns and other complex functionalities, while ensuring you retain complete control over styling.

For convenience, stateful components include a `data-state` attribute.
