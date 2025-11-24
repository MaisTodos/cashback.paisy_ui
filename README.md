# 🌻 PaisyUI

A simple, extensible DaisyUI HTML renderer built on top of `bs4` — directly from Python.

## ✨ Why PaisyUI?

`paisy_ui` is a lightweight `42.6 kb` Python package powered by `BeautifulSoup` (`bs4`) that allows you to stop worrying about HTML templates and templating engines. By leveraging the beautiful [DaisyUI](https://daisyui.com) CSS framework, it makes UI building smoother and more intuitive.

PaisyUI offers:

- **100% pure Python** — no Node.js or frontend tooling required  
- **Fully extensible** — easily build custom components with custom behavior  
- **Compatible with any HTTP framework**, including:
  - [FastAPI](https://fastapi.tiangolo.com)  
  - [Flask](https://flask.palletsprojects.com/en/stable/)  
  - [Django](https://www.djangoproject.com/)  
- **CLI support** — generate HTML directly from your terminal (*⚙️ Work in Progress*)

---

## 📦 Installation

```bash
pip install paisy_ui
```

---

## ⚙️ Usage

### Basic Concepts

There are two component classes available:

- **BaseComponents** – raw HTML components without predefined classes or behaviors.
- **DaisyUI** – higher-level components styled with DaisyUI classes and/or made from multiple HTML elements.

Every component’s constructor accepts:

- **CSS classes** as positional arguments  
- **HTML attributes** as keyword arguments  

> Some DaisyUI components may also extract special attributes such as `title`, `menu_items`, and more.

All components inherit the `__call__` behavior from `BaseComponent`, which allows you to define children like this:

```python
from paisy_ui import BaseComponents

foo = BaseComponents.Div()(
    BaseComponents.Div()(
        BaseComponents.Div()(
            BaseComponents.Div()(
                BaseComponents.Div()(
                    BaseComponents.P()("Hello World"),
                    BaseComponents.P()("This is another text"),
                    BaseComponents.Button()("Ok"),
                )
            )
        )
    )
)

print(foo.prettify())
```

---

### BaseComponents Example

You can use `BaseComponents` to create custom HTML structures or extend them to define components with custom behavior:

```python
from paisy_ui import BaseComponents

class CustomComponent(BaseComponents.P):
    def _build(self):
        self.css("text-primary")

page = BaseComponents.HTML()(
    BaseComponents.Head()(
        BaseComponents.Link(
            href="./style.css",
            rel="stylesheet",
            type="text/css"
        )
    ),
    BaseComponents.Body()(
        BaseComponents.P()("Hello world"),
        CustomComponent()("Hello!")
    ),
)

print(page.prettify())
```

---

### DaisyUI Example

DaisyUI components provide convenient abstractions for complex structures:

```python
from paisy_ui import DaisyUI

modal = DaisyUI.Modal(id="myModal")(
    DaisyUI.Title().primary()("Modal Title"),
    DaisyUI.Text()("Modal content")
)

alert = DaisyUI.Alert(symbol="done_all").success()("Everything ok!")

page = DaisyUI.HTML()(
    DaisyUI.LayoutNavbar(
        title="Test",
        menu_items=menu_items,
    )(
        modal,
        alert,
        DaisyUI.Card()(
            DaisyUI.Title()("Card Title"),
            DaisyUI.Text()("Card Content"),
            DaisyUI.Badge().primary().soft()("Foo"),
            DaisyUI.Button(onclick=modal.js_open)("Open Modal"),
        )
    )
)

print(page.prettify())
```

---
