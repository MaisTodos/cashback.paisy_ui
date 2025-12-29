# 🌻 PaisyUI

**PaisyUI** is a simple, extensible HTML renderer for **DaisyUI**, built entirely in **Python** on top of `BeautifulSoup (bs4)`.

It allows you to build modern, component-based UIs **without templates, Node.js, or frontend build tools** — directly from Python. Write your entire UI in Python code, compose components declaratively, and generate production-ready HTML with zero frontend dependencies.

![demo](./demo.png)

---

## ✨ Why PaisyUI?

`paisy_ui` is a lightweight Python package (~42.6 KB) that removes the need for HTML templates or templating engines.
By leveraging the excellent [DaisyUI](https://daisyui.com) component system, it makes UI construction intuitive, expressive, and Pythonic.

### Key features

* **100% pure Python** — no Node.js, bundlers, or frontend tooling
* **Component-based API** inspired by modern UI frameworks (React, Vue)
* **Fully extensible** — create custom components with custom behavior
* **Type-safe composition** — build complex UIs through component nesting
* **Zero configuration** — works out of the box with `PUIHTML` wrapper
* **Framework-agnostic** — works with:

  * FastAPI
  * Flask
  * Django
  * Any HTTP framework that returns HTML
* **CLI support** — generate HTML from the terminal (*⚙️ Work in progress*)

---

## ⬇️ Installation

```bash
pip install paisy_ui
```

---

## 🚀 Quick Start

Get started in 3 steps:

### 1. Import and create a page

```python
from paisy_ui.components import PUIHTML, PUIText, PUIButton

page = PUIHTML()[
    PUIText("Welcome to PaisyUI!"),
    PUIButton().primary["Get Started"]
]
```

### 2. Render to HTML

```python
print(page)  # Outputs complete HTML document
```

### 3. Use with your framework

```python
# FastAPI example
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    page = PUIHTML()[
        PUIText("Hello from FastAPI!"),
        PUIButton().primary["Click me"]
    ]
    return str(page)
```

---

## ⚙️ Usage

### 🔎 Showcase

Check out the **complete component showcase**:

👉 [Components Showcase](https://maistodos.github.io/cashback.paisy_ui/examples)

---

## 🧠 Core Concepts

Every component constructor supports:

* **CSS classes** as positional arguments
* **HTML attributes** as keyword arguments
* **Child components or text** via `__getitem__`

```python
component = ComponentClass(*classes, **attributes)[
    ChildComponent(),
    "Plain text is allowed too",
]
```

> You don't need a `PUIText` component for simple text — strings are rendered automatically.

### Component Composition

Components can be nested and composed freely:

```python
from paisy_ui.components import PUICard, PUIButton, PUIBadge

card = PUICard()[
    PUIBadge("New")["Featured"],
    PUIButton().primary["Learn More"]
]
```

### Property Chaining

Many components support method chaining for styling:

```python
button = PUIButton().primary.lg.ghost["Click me"]
# Applies multiple classes: btn-primary btn-lg btn-ghost
```

---

## 🧩 Basic Example

```python
from paisy_ui.components import PUIDiv, PUIText, PUIButton

layout = PUIDiv(style="padding:8px; background:red;")[
    PUIDiv(style="padding:8px; background:green;")[
        PUIDiv(style="padding:8px; background:blue;")[
            PUIDiv(style="padding:8px; background:yellow;")[
                PUIDiv(style="padding:8px; background:pink;")[
                    "Hello World",
                    PUIText()["This is another text"],
                    PUIButton(onclick="alert('ok')")["Ok"],
                ]
            ]
        ]
    ]
]

print(layout)
```

Output:

```html
<div style="padding: 8px; background: red">
  <div style="padding: 8px; background: green">
    <div style="padding: 8px; background: blue">
      <div style="padding: 8px; background: yellow">
        <div style="padding: 8px; background: pink">
          <p>Hello World</p>
          <p>This is another text</p>
          <button onclick="alert('ok')">Ok</button>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 🪡 Custom Components

You can create custom components by subclassing `PUIComponentABC`.

### Rules

* The component’s **HTML structure must be defined in the docstring**
* `[[content]]` is replaced by child components

```python
from paisy_ui import PUIComponentABC
from paisy_ui.components import PUIHTML

class CustomComponent(PUIComponentABC):
    """<span>[[content]]</span>"""

    def __init__(self, *classes, **attributes):
        super().__init__(*classes, **attributes)
        self.css("text-primary")
```

Usage:

```python
page = PUIHTML()[
    "Hello World!",
    CustomComponent()["Hello!"]
]

print(page)
```

Output:

```html
<span>Hello World!</span>
<span class="text-primary">Hello!</span>
```

> 💡 Tip: Explore `paisy_ui.mixins` to quickly add reusable styling behaviors.

---

## 🌻 DaisyUI Integration

All built-in components assume that **DaisyUI is already loaded**.

The `PUIHTML` component abstracts:

* `<html>`, `<head>`, and `<body>`
* Automatically injects CDNs for:

  * DaisyUI
  * TailwindCSS
  * Shiki (syntax highlighting)
  * Material Symbols Outlined

```python
from paisy_ui.components import PUIHTML, PUIDivider, PUIText

page = PUIHTML()[
    PUIText("Hello world!"),
    PUIDivider(content="Divider"),
    PUIText("Hello!"),
]

print(page)
```

Output (simplified):

```html
<html class="preload">
  <head>
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  </head>

  <body>
    <p>Hello world!</p>
    <div class="divider">Divider</div>
    <p>Hello!</p>
  </body>
</html>
```

> Additional JavaScript and CSS are injected automatically to ensure proper component behavior.

---

## 🎨 Styling & Variants

### CSS Classes

All components accept CSS classes as positional arguments:

```python
PUIText("text-lg", "font-bold")["Hello"]
```

---

### ✨ Variant Properties (Mixins)

Many components expose **styling variants as properties**, powered by `paisy_ui.mixins`.

Example:

```python
from paisy_ui.components import PUIText, PUIButton

error_text = PUIText().error["This is an error"]
# <p class="text-error">This is an error</p>

button = PUIButton().primary.ghost.sm["OK"]
# <button class="btn btn-primary btn-ghost btn-sm">OK</button>
```

---

## 🧬 Creating Custom Variants

Use `PUIVariantMixin` to define your own variant system.

```python
from paisy_ui import PUIComponentABC
from paisy_ui.mixins import PUIVariantMixin

class CustomComponent(PUIComponentABC, PUIVariantMixin):
    """<div>[[content]]</div>"""

    _variant_prefix = "foo"
```

Usage:

```python
CustomComponent().ghost["Bar"]
# <div class="foo-ghost">Bar</div>

CustomComponent().success["Bar"]
# <div class="foo-success">Bar</div>

CustomComponent().primary["Bar"]
# <div class="foo-primary">Bar</div>
```

---

## 🎓 Next Steps

Now that you understand the basics:

1. **Explore Components** — Check out the [Component Reference](#-component-reference) for all available components
2. **Learn Advanced Patterns** — See [Advanced Usage](docs/advanced.md) for custom components and mixins
3. **View Examples** — Browse the [Examples Gallery](examples/) for real-world use cases
4. **Contribute** — Help improve PaisyUI by contributing components or documentation

### 📚 Documentation

* [Component Reference](#-component-reference) — Complete list of all components
* [Advanced Usage](docs/advanced.md) — Custom components, mixins, and patterns
* [API Reference](docs/api.md) — Detailed API documentation
* [Contributing Guide](CONTRIBUTING.md) — How to contribute to PaisyUI

---

## 📦 Component Reference

PaisyUI is currently **under active development**, which means not all DaisyUI components are available yet.

Below is the list of **currently implemented components**, along with their abstraction level and implementation status.

### Legend

* Components marked with `—` **will not be implemented** as built-in components
* Components marked as **Work in progress** are planned for future releases
* The **Status** column indicates feature completeness and known limitations

---

### 🧭 Components Overview

| Category         | DaisyUI Component                                                    | PaisyUI Abstraction                              | Status                                              |
| ---------------- | -------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------- |
| **Actions**      |                                                                      |                                                  |                                                     |
|                  | [Button](https://daisyui.com/components/button/)                     | `PUIButton`                                      | ✅ 100%                                              |
|                  | [Dropdown](https://daisyui.com/components/dropdown/)                 | —                                                | —                                                   |
|                  | [FAB / Speed Dial](https://daisyui.com/components/fab/)              | —                                                | —                                                   |
|                  | [Modal](https://daisyui.com/components/modal/)                       | `PUIModal`                                       | ✅ 100%                                              |
|                  | [Swap](https://daisyui.com/components/swap/)                         | `PUISwap`                                        | ✅ 100%                                              |
|                  | [Theme Controller](https://daisyui.com/components/theme-controller/) | `PUIThemeController`                             | ⚠️ 50% (*Icons cannot be changed*)                  |
| **Data Display** |                                                                      |                                                  |                                                     |
|                  | [Accordion](https://daisyui.com/components/accordion/)               | —                                                | —                                                   |
|                  | [Avatar](https://daisyui.com/components/avatar/)                     | `PUIAvatar`                                      | ✅ 100%                                              |
|                  | [Badge](https://daisyui.com/components/badge/)                       | `PUIBadge`                                       | ✅ 100%                                              |
|                  | [Card](https://daisyui.com/components/card/)                         | `PUICard`                                        | ⚠️ 80% (*Figure outside `card-body` not supported*) |
|                  | [Carousel](https://daisyui.com/components/carousel/)                 | `PUIImgCarousel`                                 | ⚠️ 50% (*Images only*)                              |
|                  | [Chat](https://daisyui.com/components/chat/)                         | —                                                | —                                                   |
|                  | [Collapse](https://daisyui.com/components/collapse/)                 | `PUICollapse`                                    | ✅ 100%                                              |
|                  | [Countdown](https://daisyui.com/components/countdown/)               | `PUICountdown`                                   | ✅ 100%                                              |
|                  | [Diff](https://daisyui.com/components/diff/)                         | —                                                | —                                                   |
|                  | [Hover 3D Card](https://daisyui.com/components/hover-3d/)            | `PUIHover3dCard`, `PUIHover3dCardImg`            | ✅ 100%                                              |
|                  | [Hover Gallery](https://daisyui.com/components/hover-gallery/)       | —                                                | —                                                   |
|                  | [KBD](https://daisyui.com/components/kbd/)                           | `PUIKbd`                                         | ✅ 100%                                              |
|                  | [List](https://daisyui.com/components/list/)                         | `PUIList`                                        | ✅ 100%                                              |
|                  | [Stat](https://daisyui.com/components/stat/)                         | `PUIStat`                                        | ✅ 100%                                              |
|                  | [Status](https://daisyui.com/components/status/)                     | `PUIStatus`                                      | ✅ 100%                                              |
|                  | [Table](https://daisyui.com/components/table/)                       | `PUITable`                                       | ✅ 100%                                              |
|                  | [Text Rotate](https://daisyui.com/components/text-rotate/)           | `PUITextRotate`                                  | ✅ 100%                                              |
|                  | [Timeline](https://daisyui.com/components/timeline/)                 | —                                                | —                                                   |
| **Navigation**   |                                                                      |                                                  |                                                     |
|                  | *Work in progress*                                                   |                                                  |                                                     |
| **Feedback**     |                                                                      |                                                  |                                                     |
|                  | [Alert](https://daisyui.com/components/alert/)                       | `PUIAlert`                                       | ✅ 100%                                              |
|                  | [Loading](https://daisyui.com/components/loading/)                   | `PUILoading`                                     | ✅ 100%                                              |
|                  | [Progress](https://daisyui.com/components/progress/)                 | `PUIProgress`                                    | ✅ 100%                                              |
|                  | [Radial Progress](https://daisyui.com/components/radial-progress/)   | `PUIRadialProgress`                              | ✅ 100%                                              |
|                  | [Skeleton](https://daisyui.com/components/skeleton/)                 | Available via `ComponentClass().skeleton`        | ✅ 100%                                              |
|                  | [Toast](https://daisyui.com/components/toast/)                       | `PUIToast`                                       | ✅ 100%                                              |
|                  | [Tooltip](https://daisyui.com/components/tooltip/)                   | Available via `ComponentClass().tooltip("text")` | ✅ 100%                                              |
| **Data Input**   |                                                                      |                                                  |                                                     |
|                  | [Checkbox](https://daisyui.com/components/checkbox/)                 | `PUICheckbox`                                    | ✅ 100%                                              |
|                  | [File Input](https://daisyui.com/components/file-input/)             | `PUIFileInput`                                   | ✅ 100%                                              |
|                  | [Filter](https://daisyui.com/components/filter/)                     | `PUIFilter`                                      | ✅ 100%                                              |
|                  | [Radio](https://daisyui.com/components/radio/)                        | `PUIRadio`                                       | ✅ 100%                                              |
|                  | [Range](https://daisyui.com/components/range/)                        | `PUIRange`                                       | ✅ 100%                                              |
|                  | [Select](https://daisyui.com/components/select/)                      | `PUISelect`                                      | ✅ 100%                                              |
|                  | [Text Input](https://daisyui.com/components/input/)                  | `PUITextInput`                                   | ✅ 100%                                              |
|                  | [Date Input](https://daisyui.com/components/input/)                  | `PUIDateInput`                                   | ✅ 100%                                              |
|                  | [Time Input](https://daisyui.com/components/input/)                  | `PUITimeInput`                                   | ✅ 100%                                              |
|                  | [DateTime Local Input](https://daisyui.com/components/input/)        | `PUIDateTimeLocalInput`                          | ✅ 100%                                              |
|                  | [Search Input](https://daisyui.com/components/input/)                | `PUISearchInput`                                 | ✅ 100%                                              |
|                  | [Email Input](https://daisyui.com/components/input/)                 | `PUIEmailInput`                                  | ✅ 100%                                              |
|                  | [Password Input](https://daisyui.com/components/input/)              | `PUIPasswordInput`                               | ✅ 100%                                              |
|                  | [Number Input](https://daisyui.com/components/input/)                | `PUINumberInput`                                 | ✅ 100%                                              |
|                  | [Telephone Input](https://daisyui.com/components/input/)             | `PUITelephoneInput`                              | ✅ 100%                                              |
|                  | [URL Input](https://daisyui.com/components/input/)                    | `PUIUrlInput`                                    | ✅ 100%                                              |
|                  | [Toggle](https://daisyui.com/components/toggle/)                     | `PUIToggle`                                      | ✅ 100%                                              |
| **Layout**       |                                                                      |                                                  |                                                     |
|                  | [Divider](https://daisyui.com/components/divider/)                   | `PUIDivider`                                     | ✅ 100%                                              |
|                  | [Drawer / Sidebar](https://daisyui.com/components/drawer/)           | `PUISidebarLayout`                               | ⚠️ 20% (*Currently too limiting*)                   |
|                  | *Work in progress*                                                   |                                                  |                                                     |
| **Mockup**       |                                                                      |                                                  |                                                     |
|                  | *Work in progress*                                                   |                                                  |                                                     |
| **Base**         |                                                                      |                                                  |                                                     |
|                  | *HTML wrapper*                                                       | `PUIHTML`                                        | ✅ 100%                                              |
|                  | *Generic div*                                                         | `PUIDiv`                                         | ✅ 100%                                              |
|                  | *Text/Paragraph*                                                      | `PUIText`                                        | ✅ 100%                                              |
|                  | *Title/Heading*                                                       | `PUITitle`                                       | ✅ 100%                                              |
|                  | *Image*                                                               | `PUIImg`                                         | ✅ 100%                                              |
|                  | *Material Symbol*                                                     | `PUISymbol`                                      | ✅ 100%                                              |

---

### 🧩 Notes

* Components intentionally marked as **not implemented** can still be built easily using **custom components**
* Feature limitations are documented explicitly to avoid surprises
* The goal is **API stability over rushed coverage**

More components will be added incrementally as the API matures 🌱

---

## 🔮 Roadmap & Future Improvements

PaisyUI is continuously evolving. Here's what we're planning:

### 🎯 Short-term (v0.x)

* **CLI Tool** — Generate HTML files from Python scripts
* **Navigation Components** — Menu, Breadcrumbs, Pagination
* **Mockup Components** — Phone, Browser, Code mockups
* **Enhanced Modal** — More customization options
* **Form Validation** — Built-in validation helpers
* **Theme Customization** — Easier theme switching and customization

### 🚀 Medium-term (v1.x)

* **Type Hints** — Full type annotations for better IDE support
* **Component Testing** — Testing utilities for components
* **Performance Optimizations** — Lazy rendering and caching
* **SSR Support** — Server-side rendering optimizations
* **Component Library** — Community-contributed components
* **Documentation Site** — Interactive documentation with live examples

### 💡 Long-term (v2.x+)

* **Component State Management** — Built-in state handling
* **Event System** — Declarative event handling
* **Build Tool** — Optimize and bundle HTML output
* **Visual Builder** — GUI for building UIs
* **Plugin System** — Extensible plugin architecture

### 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Priority Areas:**
- Navigation components (Menu, Breadcrumbs)
- Form validation helpers
- More examples and documentation
- Performance improvements

---

🌻 *Happy hacking with PaisyUI!*
