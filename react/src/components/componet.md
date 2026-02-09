# Component Library Documentation

## 1\. Button Component (`buttons.tsx`)

margin

A highly reusable primitive button component that allows for easy styling via props while maintaining a consistent base appearance.

### 1.1 Overview

The `Button` component accepts functional and structural props, along with an optional `style` object to customize its appearance. Custom styles are merged with the component's default styles, prioritizing user-defined properties.

### 1.2 Props Reference (`ButtonProps`)

| Prop Name | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **`text`** | `string` | `"Button"` | The visible text displayed inside the button. |
| **`command`** | `() => void` | `undefined` | The function executed when the user clicks the button. Maps to the HTML `onClick` handler. |
| **`type`** | `"button" \| "submit" \| "reset"` | `undefined` | The standard HTML button type. **Required for form submission.** |
| **`style`** | `React.CSSProperties` | `{...}` | Custom inline CSS styles to override or extend the component's default appearance. |
| **`id`** | `string` | `undefined` | Standard HTML `id` attribute. |
| **`title`** | `string` | `undefined` | Standard HTML `title` attribute (tooltip text). |
| **`className`** | `string` | `"Button"` | Standard HTML class attribute. |

### 1.3 Usage Example

This example shows how to override the default background and text, and define a submission action.

```tsx
import Button from "./components/buttons";

const SaveForm = () => (
  <Button 
    text="Confirm & Send" 
    command={() => alert('Form Submitted!')} 
    type="submit"
    title="Click to finalize the form"
    style={{ 
        backgroundColor: '#1E90FF', 
        borderRadius: '5px',
        fontWeight: 600
    }}
  />
);
```

-----

## 2\. Search Bar Component (`searchBar.tsx`)

A **Controlled Component** for handling search input. It manages its own input state, provides dynamic filtering via user-defined styling, and uses a callback function to return the search term upon submission.

### 2.1 Overview

The Search Bar component is composed of a `<form>` container styled with Flexbox, an image, an input field, and a dedicated `Button` component for submission. It is optimized for performance and style customization.

### 2.2 Props Reference (`SearchBarProps`)

| Prop Name | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **`onSearch`** | `(value: string) => void` | **(Required)** | The **primary callback**. Executed when the form is submitted, returning the final search value. |
| **`placeholder`** | `string` | `"Search anything you want"` | Text displayed in the input field when empty. |
| **`barStyle`** | `React.CSSProperties` | `{...}` | Custom styles for the **main container** (`<form>` element). Used for setting overall size, border, and background. |
| **`inputStyle`** | `React.CSSProperties` | `{...}` | Custom styles for the internal **text input** field. |
| **`id`** | `string` | `undefined` | Standard HTML `id` for the `<form>` wrapper. |
| **`image`** | `string` | `'/search.png'` | The URL path for the search icon image displayed on the left. |

### 2.3 Component Flow & Behavior

1. **Typing:** The component tracks the input value internally using `useState`.
2. **Submission:** When the user clicks the "Search" button or presses Enter:
      * The `handleSubmit` function prevents page reload.
      * The external `onSearch` prop is called with the current `text` value.
      * The input is immediately cleared (`textChanger("")`) for the next search.

### 2.4 Usage Example

This example demonstrates using the `onSearch` callback and applying custom dimensions.

```tsx
import SearchBar from "./components/searchBar";

const SearchDashboard = () => {
  const handleSearch = (term: string) => {
    console.log(`New Search initiated for: ${term}`);
    // Logic to filter data, fetch API, etc.
  };

  return (
    <SearchBar 
      onSearch={handleSearch}
      placeholder="Search students by name..."
      barStyle={{ 
        width: '400px', 
        height: '45px',
        backgroundColor: '#404040' 
      }}
      inputStyle={{
        color: '#FFFFFF' 
      }}
    />
  );
};
```
