# 🌻 PaisyUI

**PaisyUI** is a simple, extensible HTML renderer for **DaisyUI**, built entirely in **Python** on top of `BeautifulSoup (bs4)`.

It allows you to build modern, component-based UIs **without templates, Node.js, or frontend build tools** — directly from Python.

![demo](./demo.png)

---

## ✨ Why PaisyUI?

`paisy_ui` is a lightweight Python package (~42.6 KB) that removes the need for HTML templates and templating engines.
By leveraging the excellent [DaisyUI](https://daisyui.com) component system, it makes UI construction intuitive, expressive, and Pythonic.

### Key features

* **100% pure Python** — no Node.js, bundlers, or frontend tooling
* **Component-based API** inspired by modern UI frameworks
* **Fully extensible** — create custom components with custom behavior
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

> You don’t need a `PUIText` component for simple text — strings are rendered automatically.

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

## 📦 Custom Components

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

## 🚀 Summary

**PaisyUI** lets you:

* Build DaisyUI-powered interfaces
* Stay entirely in Python
* Avoid HTML templates and frontend build chains
* Extend and compose UI components freely

Perfect for backend-driven UIs, internal tools, dashboards, and rapid prototyping.

---

🌻 *Happy hacking with PaisyUI!*
