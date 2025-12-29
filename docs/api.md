# 📚 API Reference

Complete API documentation for PaisyUI components, mixins, and utilities.

---

## 🧩 Core Components

### Base Components

#### `PUIHTML`
Main wrapper component that generates a complete HTML document.

```python
from paisy_ui.components import PUIHTML

page = PUIHTML()[...]
```

**Features:**
- Automatically injects DaisyUI, TailwindCSS, Shiki, and Material Symbols CDNs
- Handles theme management
- Includes countdown update scripts

---

#### `PUIDiv`
Generic div component with mixin support.

```python
from paisy_ui.components import PUIDiv

div = PUIDiv("class1", "class2", id="my-id")["Content"]
```

**Mixins:** `PUIColorsMixins`, `PUILayoutMixin`, `PUIBorderMixin`, `PUIFontWeightMixin`

---

#### `PUIText`
Paragraph/text component.

```python
from paisy_ui.components import PUIText

text = PUIText("text-lg", "font-bold")["Hello World"]
```

**Mixins:** `PUIColorsMixins`, `PUILayoutMixin`, `PUIBorderMixin`, `PUITextSizeMixin`, `PUIFontWeightMixin`

---

#### `PUITitle`
Heading component (defaults to `<h5>`).

```python
from paisy_ui.components import PUITitle

title = PUITitle("font-bold", "text-xl")["My Title"]
```

**Mixins:** `PUIColorsMixins`, `PUILayoutMixin`, `PUIBorderMixin`

---

#### `PUIImg`
Image component.

```python
from paisy_ui.components import PUIImg

img = PUIImg(src="image.jpg", alt="Description")
```

**Parameters:**
- `src` (str, required): Image source URL
- `alt` (str, optional): Alt text

---

#### `PUISymbol`
Material Symbols icon component.

```python
from paisy_ui.components import PUISymbol

icon = PUISymbol(symbol="home").text_2xl
```

**Parameters:**
- `symbol` (str, required): Material Symbol name

**Mixins:** `PUIColorsMixins`, `PUILayoutMixin`, `PUITextSizeMixin`

---

## 🎯 Action Components

### `PUIButton`
Button component with variant support.

```python
from paisy_ui.components import PUIButton

button = PUIButton().primary.ghost.sm["Click me"]
```

**Properties:**
- `link` - Makes button a link style
- `active` - Active state
- `disabled` - Disabled state
- `sm` - Small size

**Mixins:** `PUIVariantMixin`, `PUILayoutMixin`, `PUIBorderMixin`

---

### `PUIModal`
Modal dialog component.

```python
from paisy_ui.components import PUIModal

modal = PUIModal(id="my-modal")[
    PUIText("Modal content")
]

# Add close button
modal.with_close_button
```

**Parameters:**
- `id` (str, required): Unique identifier for the modal

**Properties:**
- `with_close_button` - Adds a close button to the modal

---

### `PUISwap`
Swap component for toggling between two states.

```python
from paisy_ui.components import PUISwap

swap = PUISwap(
    on="ON",
    off="OFF"
)
```

**Parameters:**
- `on` (str | PUIComponentABC): Content to show when active
- `off` (str | PUIComponentABC): Content to show when inactive

---

### `PUIThemeController`
Theme toggle component.

```python
from paisy_ui.components import PUIThemeController

theme_toggle = PUIThemeController(value="dark")
```

**Parameters:**
- `value` (str, required): Theme value

**Note:** Icons cannot be changed (50% implementation).

---

## 📊 Data Display Components

### `PUIAvatar`
Avatar component with size variants.

```python
from paisy_ui.components import PUIAvatar

avatar = PUIAvatar(src="avatar.jpg").md.online
```

**Parameters:**
- `src` (str, required): Avatar image source

**Properties:**
- `sm`, `md`, `lg`, `xl` - Size variants
- `online`, `offline` - Status indicators

---

### `PUIBadge`
Badge component.

```python
from paisy_ui.components import PUIBadge

badge = PUIBadge().primary["New"]
```

**Mixins:** `PUIBorderMixin`, `PUILayoutMixin`, `PUIVariantMixin`

---

### `PUICard`
Card component.

```python
from paisy_ui.components import PUICard

card = PUICard()[
    PUIText("Card content")
]

# Add full-width image
card.image_full("image.jpg")
```

**Methods:**
- `image_full(img_src: str)` - Adds a full-width image above the card

**Note:** Figure outside `card-body` not supported (80% implementation).

---

### `PUITable`
Table component with columns and rows.

```python
from paisy_ui.components import PUITable

table = PUITable(
    columns=["Name", "Age", "City"],
    rows=[
        ["Alice", "30", "New York"],
        ["Bob", "25", "London"]
    ]
)
```

**Parameters:**
- `columns` (List[Union[str, PUIComponentABC]]): Column headers
- `rows` (List[List[Union[str, PUIComponentABC]]]): Table rows

---

### `PUIStat`
Stat component for displaying statistics.

```python
from paisy_ui.components import PUIStat

stat = PUIStat(
    title="Total Users",
    value="1,234",
    desc="+20% from last month",
    symbol="people"
)
```

**Parameters:**
- `title` (str, required): Stat title
- `value` (str, required): Stat value
- `desc` (str, required): Stat description
- `symbol` (str, optional): Material Symbol name

---

## 📝 Data Input Components

All input components follow a similar pattern:

```python
from paisy_ui.components import PUITextInput, PUIEmailInput, PUIPasswordInput

# Text input
text_input = PUITextInput(
    name="username",
    id="username",
    label="Username",
    legend="User Information"
)

# Email input
email_input = PUIEmailInput(
    name="email",
    id="email",
    label="Email"
)

# Password input
password_input = PUIPasswordInput(
    name="password",
    id="password",
    label="Password"
)
```

**Common Parameters:**
- `name` (str, required): Input name attribute
- `id` (str, required): Input ID
- `label` (str, optional): Input label
- `legend` (str, optional): Fieldset legend
- `pattern` (str, optional): Validation pattern
- `validator_hint` (str, optional): Validation hint message

**Available Input Types:**
- `PUITextInput` - Text input
- `PUIEmailInput` - Email input
- `PUIPasswordInput` - Password input
- `PUINumberInput` - Number input
- `PUIDateInput` - Date input
- `PUITimeInput` - Time input
- `PUIDateTimeLocalInput` - DateTime input
- `PUISearchInput` - Search input
- `PUITelephoneInput` - Telephone input
- `PUIUrlInput` - URL input
- `PUICheckbox` - Checkbox
- `PUIRadio` - Radio button
- `PUIRange` - Range slider
- `PUIToggle` - Toggle switch
- `PUIFileInput` - File input
- `PUISelect` - Select dropdown
- `PUIFilter` - Filter buttons

---

## 💬 Feedback Components

### `PUIAlert`
Alert component for notifications.

```python
from paisy_ui.components import PUIAlert

alert = PUIAlert(
    symbol="info",
    message="This is an alert",
    close_button=True
).info
```

**Parameters:**
- `symbol` (str, required): Material Symbol name
- `message` (str, required): Alert message
- `close_button` (bool, optional): Show close button

**Mixins:** `PUIVariantMixin`

---

### `PUILoading`
Loading indicator component.

```python
from paisy_ui.components import PUILoading

loading = PUILoading().spinner.lg
```

**Properties:**
- `spinner`, `bars`, `ball`, `ring`, `dots` - Loading styles
- `sm`, `md`, `lg`, `xl` - Size variants

---

### `PUIProgress`
Progress bar component.

```python
from paisy_ui.components import PUIProgress

progress = PUIProgress(value=50, max=100).primary
```

**Parameters:**
- `value` (int, optional): Current value
- `max` (int, optional): Maximum value

---

### `PUIRadialProgress`
Radial progress indicator.

```python
from paisy_ui.components import PUIRadialProgress

radial = PUIRadialProgress(value=75, max=100).primary
```

**Parameters:**
- `value` (int, required): Current value
- `max` (int, required): Maximum value

---

### `PUIToast`
Toast notification container.

```python
from paisy_ui.components import PUIToast
from paisy_ui.components.feedback import PUIToast

toast = PUIToast(messages=[
    PUIToast.Message(variant="success", content="Saved!"),
    PUIToast.Message(variant="error", content="Error occurred")
]).toast_top.toast_end
```

**Properties:**
- `toast_top`, `toast_middle`, `toast_bottom` - Vertical position
- `toast_start`, `toast_center`, `toast_end` - Horizontal position

---

## 🎨 Mixins Reference

### Layout Mixins

#### `PUILayoutMixin`
Combines display, margin, padding, height, and width utilities.

#### `PUIDisplayMixin`
Display properties: `flex`, `grid`, `block`, `inline`, etc.

#### `PUIMarginMixin`
Margin utilities: `m_1`, `m_2`, `mx_auto`, `mt_4`, etc.

#### `PUIPaddingMixin`
Padding utilities: `p_1`, `p_2`, `px_4`, `py_2`, etc.

#### `PUIHeightMixin`
Height utilities: `h_full`, `h_screen`, `h_64`, etc.

#### `PUIWidthMixin`
Width utilities: `w_full`, `w_1_2`, `w_64`, etc.

### Color Mixins

#### `PUIColorsMixins`
Combines text and background color mixins.

#### `PUITextColorMixin`
Text color variants: `text_primary`, `text_secondary`, `text_error`, etc.

#### `PUIBackgroundColorMixin`
Background color variants: `bg_primary`, `bg_secondary`, `bg_error`, etc.

### Typography Mixins

#### `PUITextSizeMixin`
Text size utilities: `text_xs`, `text_sm`, `text_lg`, `text_2xl`, etc.

#### `PUIFontWeightMixin`
Font weight utilities: `font_normal`, `font_bold`, `font_medium`, etc.

### Border Mixins

#### `PUIBorderMixin`
Border radius utilities: `rounded`, `rounded_lg`, `rounded_full`, etc.

### Variant Mixin

#### `PUIVariantMixin`
Creates variant-based styling systems. Requires `_variant_prefix` class attribute.

---

## 🔧 Utilities

### Component Methods

All components inherit from `PUIComponentABC` and support:

- `css(*classes)` - Add CSS classes
- `__getitem__(children)` - Add child components
- `__str__()` - Render to HTML string

---

## 📖 More Information

- See [Advanced Usage](advanced.md) for custom components and patterns
- Check the [Component Reference](../README.md#-component-reference) for a complete list
- Browse [examples](../examples/) for real-world usage

