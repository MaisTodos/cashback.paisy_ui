# 🌻 PaisyUI

A simple, extensible DaisyUI HTML renderer built on top of `bs4` — directly from Python.

![demo](./demo.png)

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

## ⬇️ Installation

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

foo = BaseComponents.Div(style="padding:8px; background:red;")(
    BaseComponents.Div(style="padding:8px; background:green;")(
        BaseComponents.Div(style="padding:8px; background:blue;")(
            BaseComponents.Div(style="padding:8px; background:yellow;")(
                BaseComponents.Div(style="padding:8px; background:pink;")(
                    BaseComponents.P()("Hello World"),
                    BaseComponents.P()("This is another text"),
                    BaseComponents.Button(onclick="alert('ok')")("Ok"),
                )
            )
        )
    )
)

print(foo)
'''
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
'''
```

---

---

## Examples

### 🛫 Pre-built examples

1. FastAPI:
```bash
poetry run python examples/with_fastapi.py
```

---

### 📦 BaseComponents Example

You can use `BaseComponents` to create custom HTML structures or extend them to define components with custom behavior:

```python
from paisy_ui import BaseComponents, BaseComponent

class CustomComponent(BaseComponent):
    tag_name = 'span'

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

print(page)
'''
<html>
    <head>
        <link href="./style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <p>Hello world</p>
        <span class="text-primary">Hello!</span>
    </body>
</html>
'''
```

---

### 🌻 DaisyUI Example

`DaisyUI` components provide convenient abstractions for complex structures:

> *It also automatically imports [DaisyUI](https://daisyui.com/) and [Google Material Symbols](https://fonts.google.com/icons?icon.query=unk) using `CDN`.*

```python
from paisy_ui import DaisyUI

page = DaisyUI.HTML()(
    DaisyUI.LayoutNavbar(
        title="Test",
        menu_items=[
            DaisyUI.LayoutNavbar.MenuItem(label="Home", href="/home", symbol="home"),
            DaisyUI.LayoutNavbar.MenuItem(label="Users", href="/users", symbol="groups"),
            DaisyUI.LayoutNavbar.MenuItem(label="Tasks", href="/tasks", symbol="done_all"),
        ],
    )(
        DaisyUI.Modal(id="myModal")(
            DaisyUI.Title().primary()("Modal Title"),
            DaisyUI.Text()("Modal content")
        ),
        DaisyUI.Alert(symbol="done_all").success()("Everything ok!"),
        DaisyUI.Card()(
            DaisyUI.Title()("Card Title"),
            DaisyUI.Text()("Card Content"),
            DaisyUI.Badge().primary().soft()("Foo"),
            DaisyUI.Button(onclick="myModal.openModal()")("Open Modal"),
        )
    )
)

print(page.prettify())
'''
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" rel="stylesheet" type="text/css" />
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4">
        </script>
        <script type="module">
            import { codeToHtml, createHighlighter } from 'https://esm.sh/shiki@3.0.0'

            document.querySelectorAll("code[data-lang='python']").forEach(async (el) => {
                el.innerHTML = await codeToHtml(el.innerHTML, { lang: 'python', theme: 'github-dark-default' });
            })
        </script>
        <style>
            .shiki {
                background: transparent !important;
            }
        </style>
    </head>

    <body data-theme="dark">
        <main class="drawer">
            <input class="drawer-toggle" id="drawer-toggle" type="checkbox" />
            <div class="drawer-content flex flex-col">
                <nav class="navbar bg-base-300 w-full">
                    <div class="flex-none lg:hidden">
                        <label class="btn btn-square btn-ghost" for="drawer-toggle">
                            <span class="material-symbols-outlined" symbol="menu">
                                menu
                            </span>
                        </label>
                    </div>
                    <div class="mx-2 flex-1 px-2 font-bold">
                        Test
                    </div>
                    <ul class="menu menu-horizontal hidden lg:flex">
                        <li class="text-base">
                            <a href="/home">
                                <span class="material-symbols-outlined" symbol="home">
                                    home
                                </span>
                                Home
                            </a>
                        </li>
                        <li class="text-base">
                            <a href="/users">
                                <span class="material-symbols-outlined" symbol="groups">
                                    groups
                                </span>
                                Users
                            </a>
                        </li>
                        <li class="text-base">
                            <a href="/tasks">
                                <span class="material-symbols-outlined" symbol="done_all">
                                    done_all
                                </span>
                                Tasks
                            </a>
                        </li>
                    </ul>
                </nav>
                <div class="p-4 flex flex-col gap-4">
                    <dialog class="modal" id="myModal">
                        <div class="modal-box">
                            <h3 class="text-xl font-bold flex flex-row gap-2 items-center text-primary">
                                Modal Title
                            </h3>
                            <p class="flex flex-row gap-2 items-center">
                                Modal content
                            </p>
                        </div>
                        <form class="modal-backdrop" method="dialog">
                            <button>
                                Fechar
                            </button>
                        </form>
                    </dialog>
                    <div class="alert alert-success">
                        <span class="material-symbols-outlined" symbol="done_all">
                            done_all
                        </span>
                        Everything ok!
                    </div>
                    <div class="card border border-base-300">
                        <div class="card-body">
                            <h3 class="text-xl font-bold flex flex-row gap-2 items-center">
                                Card Title
                            </h3>
                            <p class="flex flex-row gap-2 items-center">
                                Card Content
                            </p>
                            <span class="badge badge-primary badge-soft">
                                Foo
                            </span>
                            <button class="btn" onclick="myModal.openModal()">
                                Open Modal
                            </button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="drawer-side">
                <label aria-label="close sidebar" class="drawer-overlay" for="drawer-toggle">
                </label>
                <ul class="menu bg-base-200 min-h-full w-80 p-4">
                    <li class="mb-2 font-bold">
                        Test
                    </li>
                    <li class="text-base">
                        <a href="/home">
                            <span class="material-symbols-outlined" symbol="home">
                                home
                            </span>
                            Home
                        </a>
                    </li>
                    <li class="text-base">
                        <a href="/users">
                            <span class="material-symbols-outlined" symbol="groups">
                                groups
                            </span>
                            Users
                        </a>
                    </li>
                    <li class="text-base">
                        <a href="/tasks">
                            <span class="material-symbols-outlined" symbol="done_all">
                                done_all
                            </span>
                            Tasks
                        </a>
                    </li>
                </ul>
            </div>
        </main>
    </body>
</html>
'''
```
