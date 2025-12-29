# 🧬 Advanced Usage

This guide covers advanced patterns and techniques for working with PaisyUI, including custom components, mixins, and composition patterns.

---

## 🪡 Custom Components

### Basic Custom Component

The simplest way to create a custom component is by subclassing `PUIComponentABC` and defining the HTML structure in the docstring:

```python
from paisy_ui import PUIComponentABC
from paisy_ui.components import PUIHTML

class MyCard(PUIComponentABC):
    """<div class="card bg-base-100 shadow-xl">
        <div class="card-body">[[content]]</div>
    </div>"""

    def __init__(self, *classes, title: str, **attributes):
        super().__init__(*classes, **attributes)
        # Add title if needed
        if title:
            self.css("card-title")
```

Usage:

```python
page = PUIHTML()[
    MyCard(title="My Title")["Card content here"]
]
```

### Components with Dynamic Content

You can manipulate the component's structure in `__init__`:

```python
from paisy_ui import PUIComponentABC
from paisy_ui.utils import parse_html

class AlertBox(PUIComponentABC):
    """<div class="alert">[[content]]</div>"""

    def __init__(self, *classes, variant: str = "info", **attributes):
        super().__init__(*classes, **attributes)
        self.css(f"alert-{variant}")
        
        # Add icon
        icon, _ = parse_html('<span class="material-symbols-outlined">info</span>')
        self.tag.insert(0, icon)
```

---

## 🎨 Using Mixins

Mixins provide reusable styling behaviors. Here are the available mixins:

### Available Mixins

#### Layout Mixins
- `PUILayoutMixin` - Combines display, margin, padding, height, and width
- `PUIDisplayMixin` - Display properties (flex, grid, etc.)
- `PUIMarginMixin` - Margin utilities
- `PUIPaddingMixin` - Padding utilities
- `PUIHeightMixin` - Height utilities
- `PUIWidthMixin` - Width utilities

#### Color Mixins
- `PUIColorsMixins` - Combines text and background colors
- `PUITextColorMixin` - Text color variants
- `PUIBackgroundColorMixin` - Background color variants

#### Typography Mixins
- `PUITextSizeMixin` - Text size utilities
- `PUIFontWeightMixin` - Font weight utilities

#### Border Mixins
- `PUIBorderMixin` - Border radius utilities

#### Variant Mixin
- `PUIVariantMixin` - Create variant-based styling systems

### Example: Component with Mixins

```python
from paisy_ui import PUIComponentABC
from paisy_ui.mixins import (
    PUILayoutMixin,
    PUIColorsMixins,
    PUIBorderMixin,
    PUITextSizeMixin
)

class StyledBox(
    PUIComponentABC,
    PUILayoutMixin,
    PUIColorsMixins,
    PUIBorderMixin,
    PUITextSizeMixin
):
    """<div>[[content]]</div>"""

# Usage with chained properties
box = StyledBox().bg_primary.text_white.p_4.rounded["Content"]
```

---

## 🔗 Creating Custom Variants

Use `PUIVariantMixin` to create your own variant system:

```python
from paisy_ui import PUIComponentABC
from paisy_ui.mixins import PUIVariantMixin

class CustomButton(PUIComponentABC, PUIVariantMixin):
    """<button class="btn">[[content]]</button>"""
    
    _variant_prefix = "btn"

# Now you can use:
button = CustomButton().primary["Click me"]
# <button class="btn btn-primary">Click me</button>

button = CustomButton().success.lg["Save"]
# <button class="btn btn-success btn-lg">Save</button>
```

### Available Variants

The `PUIVariantMixin` automatically provides these variants:
- `primary`, `secondary`, `accent`
- `success`, `info`, `warning`, `error`
- `ghost`, `outline`, `link`
- `sm`, `md`, `lg`, `xl`
- `xs`, `2xl`, `3xl`

---

## 🧩 Composition Patterns

### Pattern 1: Wrapper Components

Create components that wrap other components:

```python
class Container(PUIComponentABC):
    """<div class="container mx-auto px-4">[[content]]</div>"""

class Section(PUIComponentABC):
    """<section class="py-8">[[content]]</section>"""

# Usage
page = PUIHTML()[
    Container()[
        Section()[
            PUIText("Content here")
        ]
    ]
]
```

### Pattern 2: Factory Functions

Create factory functions for common patterns:

```python
def create_form_field(label: str, input_type: str = "text"):
    from paisy_ui.components import PUITextInput, PUIText
    
    return PUIDiv()[
        PUIText(label),
        PUITextInput(name=label.lower(), id=label.lower(), type=input_type)
    ]

# Usage
form = PUIDiv()[
    create_form_field("Name"),
    create_form_field("Email", "email"),
    create_form_field("Password", "password")
]
```

### Pattern 3: Component Builders

Create builder classes for complex components:

```python
class TableBuilder:
    def __init__(self):
        self.columns = []
        self.rows = []
    
    def add_column(self, name: str):
        self.columns.append(name)
        return self
    
    def add_row(self, *values):
        self.rows.append(values)
        return self
    
    def build(self):
        from paisy_ui.components import PUITable
        return PUITable(columns=self.columns, rows=self.rows)

# Usage
table = (TableBuilder()
    .add_column("Name")
    .add_column("Age")
    .add_row("Alice", "30")
    .add_row("Bob", "25")
    .build())
```

---

## 🔄 Framework Integration

### FastAPI Integration

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from paisy_ui.components import PUIHTML, PUIText, PUIButton

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    page = PUIHTML()[
        PUIText("Welcome!"),
        PUIButton().primary["Get Started"]
    ]
    return str(page)
```

### Flask Integration

```python
from flask import Flask
from paisy_ui.components import PUIHTML, PUIText, PUIButton

app = Flask(__name__)

@app.route("/")
def home():
    page = PUIHTML()[
        PUIText("Welcome!"),
        PUIButton().primary["Get Started"]
    ]
    return str(page)
```

### Django Integration

```python
from django.http import HttpResponse
from paisy_ui.components import PUIHTML, PUIText, PUIButton

def home(request):
    page = PUIHTML()[
        PUIText("Welcome!"),
        PUIButton().primary["Get Started"]
    ]
    return HttpResponse(str(page))
```

---

## 💡 Best Practices

1. **Keep Components Simple** - Each component should have a single responsibility
2. **Use Mixins for Reusability** - Don't repeat styling logic
3. **Document Your Components** - Use docstrings to explain component structure
4. **Leverage Composition** - Build complex UIs from simple components
5. **Follow Naming Conventions** - Use `PUI` prefix for custom components

---

## 🚀 Next Steps

- Explore the [API Reference](api.md) for detailed component documentation
- Check out [examples](../examples/) for real-world use cases
- Read the [Contributing Guide](../CONTRIBUTING.md) to add new components

