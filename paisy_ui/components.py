from dataclasses import dataclass
from typing import List, Optional, Union

from .base import BaseComponents
from .core import BaseComponent, WrapperComponent

CDN_DAISYUI = "https://cdn.jsdelivr.net/npm/daisyui@5"
CDN_MATERIAL_SYMBOLS = "https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"
CDN_TAILWIND = "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"


class DaisyUI:
    """DaisyUI Components, check the [full documentation](https://daisyui.com)"""

    class Symbol(BaseComponents.Symbol): ...

    class HTML(WrapperComponent):
        """Base HTML with DaisyUI, Tailwind and Material Symbols Outlined CDNs"""

        tag_name = "html"

        def _build_wrapper(self):
            head = BaseComponents.Head()(
                BaseComponents.Link(
                    href=CDN_DAISYUI,
                    rel="stylesheet",
                    type="text/css",
                ),
                BaseComponents.Link(
                    href=CDN_MATERIAL_SYMBOLS,
                    rel="stylesheet",
                    type="text/css",
                ),
                BaseComponents.Script(src=CDN_TAILWIND),
            )
            self.append(head)
            self.wrapper = BaseComponents.Body()
            self.append(self.wrapper)

    class VariantComponent(BaseComponent):
        """A component that have a `primary`, `success`, `danger`, `warning`, `error` or `accent` variant"""

        base_class: str

        def _build(self):
            self.css(self.base_class)

        def primary(self):
            return self.css(f"{self.base_class}-primary")

        def success(self):
            return self.css(f"{self.base_class}-success")

        def danger(self):
            return self.css(f"{self.base_class}-danger")

        def warning(self):
            return self.css(f"{self.base_class}-warning")

        def error(self):
            return self.css(f"{self.base_class}-error")

        def accent(self):
            return self.css(f"{self.base_class}-accent")

    class Text(VariantComponent):
        """<p class="text flex flex-row gap-2 items-center"></p>"""

        tag_name = "p"
        base_class = "text"

        def _build(self):
            self.css("text", "flex", "flex-row", "gap-2", "items-center")

    class Title(VariantComponent):
        """<h5 class="text-lg font-bold"></h5>"""

        tag_name = "h5"
        base_class = "text"

        def _build(self):
            self.css("text-lg font-bold")

    class Form(BaseComponents.Form):
        """<form class="flex flex-col gap-4"></form>"""

        def _build(self):
            self.css("flex", "flex-col", "gap-4")

    class Input(BaseComponent):
        """A complete fieldset with optional symbol, optional legend and optional help"""

        tag_name = "fieldset"

        @property
        def legend(self) -> Optional[str]:
            attr = self.attrs_pop("legend", None)
            return str(attr) if attr else None

        @property
        def symbol(self) -> Optional[str]:
            attr = self.attrs_pop("symbol", None)
            return str(attr) if attr else None

        @property
        def help(self) -> Optional[str]:
            attr = self.attrs_pop("help", None)
            return str(attr) if attr else None

        def _build(self):
            self.css("fieldset")
            if self.legend:
                self.append(BaseComponents.Legend("fieldset-legend")(self.legend))

            input_wrapper = BaseComponents.Label("input", "w-full")
            if self.symbol:
                input_wrapper.append(
                    BaseComponents.Symbol("text-sm", "opacity-50", symbol=self.symbol)
                )
            input_wrapper.append(BaseComponents.Input("grow", **self.attrs))
            self.append(input_wrapper)

            if self.help:
                self.append(BaseComponents.P("label")(str(self.help)))

    class Table(BaseComponents.Div):
        """A complete table"""

        tag_name = "div"

        @property
        def collumns(self) -> List[Union[BaseComponent, str]]:
            attr = self.attrs_pop("collumns", None)
            if not isinstance(attr, list):
                raise ValueError("Table collumns must be a List[str]")
            return attr

        @property
        def rows(self) -> List[List[Union[BaseComponent, str]]]:
            attr = self.attrs_pop("rows", None)
            if not isinstance(attr, list):
                raise ValueError("Table rows must be a List[List[str]]")
            if not isinstance(attr[0], list):
                raise ValueError("Table rows must be a List[List[str]]")
            return attr

        def _build(self):
            self.css("overflow-x-auto")
            table = BaseComponents.Table("table")(
                BaseComponents.THead()(
                    BaseComponents.TR()(
                        *[BaseComponents.TH()(col) for col in self.collumns]
                    )
                ),
                BaseComponents.TBody()(
                    *[
                        BaseComponents.TR()(
                            *[
                                BaseComponents.TD()(
                                    col if isinstance(col, BaseComponent) else str(col)
                                )
                                for col in row
                            ]
                        )
                        for row in self.rows
                    ]
                ),
            )
            self.append(table)

    class Button(VariantComponent):
        """<button class="btn"></button>"""

        base_class = "btn"

        def small(self):
            return self.css(f"{self.base_class}-sm")

    class Badge(VariantComponent):
        """<span class="badge"></span>"""

        tag_name = "span"
        base_class = "badge"

        def soft(self):
            return self.css("badge-soft")

    class Alert(VariantComponent):
        """<div class="alert"></div>"""

        tag_name = "div"
        base_class = "alert"

        @property
        def symbol(self) -> Optional[str]:
            attr = self.attrs_pop("symbol", None)
            return str(attr) if attr else None

        def _build(self):
            self.css("alert")
            if self.symbol:
                self.append(BaseComponents.Symbol(symbol=self.symbol))

    class Card(WrapperComponent):
        """<div class="card shadow-sm"><div class="card-body"></div></div>"""

        tag_name = "div"

        def _build(self):
            self.css("card", "shadow-sm")

        def _build_wrapper(self):
            self.wrapper = BaseComponents.Div("card-body")
            self.append(self.wrapper)

    class Modal(WrapperComponent):
        """A modal dialog that can be opened with `Modal.js_open` JavaScript function"""

        tag_name = "dialog"

        @property
        def id(self) -> str:
            attr = self.attrs_pop("id")
            if not attr:
                raise ValueError("Modal requires id attribute")
            return attr

        @property
        def js_open(self) -> str:
            return f"{self.id}.showModal()"

        def _build_wrapper(self):
            self.wrapper = BaseComponents.Div("modal-box")
            self.append(self.wrapper)
            self.append(
                BaseComponents.Form("modal-backdrop", method="dialog")(
                    BaseComponents.Button()("Fechar")
                )
            )

        def _build(self):
            self.css("modal")
            self.attrs.update(id=self.id)

    class NavBar(BaseComponent):
        """A simple navbar"""

        @property
        def title(self) -> Optional[str]:
            attr = self.attrs_pop("title", None)
            return str(attr) if attr else None

        def _build(self):
            self.css("navbar", "bg-base-300", "w-full")

            self.append(
                BaseComponents.Div("flex-none", "lg:hidden")(
                    BaseComponents.Label(
                        "btn", "btn-square", "btn-ghost", for_="drawer-toggle"
                    )(BaseComponents.Symbol(symbol="menu"))
                )
            )

            if self.title:
                self.append(
                    BaseComponents.Div("mx-2", "flex-1", "px-2", "font-bold")(
                        self.title
                    )
                )

    class LayoutGrid(BaseComponent):
        """<div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4"></div>"""

        tag_name = "div"

        def _build(self):
            self.css("grid", "md:grid-cols-2", "lg:grid-cols-3", "gap-4")

    class LayoutNavbar(WrapperComponent):
        """A complete responsive layout with a navbar and a sidebar for small screens"""

        tag_name = "main"

        @dataclass
        class MenuItem:
            label: str
            href: Optional[str] = None
            onclick: Optional[str] = None
            symbol: Optional[str] = "expand_circle_right"
            subitems: Optional[List["DaisyUI.LayoutNavbar.MenuItem"]] = None
            variant: Optional[str] = "base"

            def to_component(self, *classnames) -> BaseComponents.Li:

                if not self.subitems:
                    component = BaseComponents.Li(f"text-{self.variant}")(
                        BaseComponents.A(href=self.href, onclick=self.onclick)(
                            BaseComponents.Symbol(symbol=self.symbol),
                            self.label,
                        ),
                    )
                else:
                    component = BaseComponents.Li(f"text-{self.variant}")(
                        BaseComponents.Details()(
                            BaseComponents.Summary()(
                                BaseComponents.Symbol(symbol=self.symbol),
                                self.label,
                            ),
                            BaseComponents.Ul(
                                "bg-base-100",
                                "rounded-t-none",
                                "p-2",
                                "z-10",
                            )(
                                *[
                                    subitem.to_component("text-sm")
                                    for subitem in self.subitems
                                ]
                            ),
                        )
                    )

                return component.css(" ".join(classnames))

        @property
        def title(self) -> Optional[str]:
            attr = self.attrs_pop("title", None)
            return str(attr) if attr else None

        @property
        def menu_items(self) -> List[MenuItem]:
            attr = self.attrs_pop("menu-items", [])
            if not isinstance(attr, list):
                raise ValueError(f"MenuItems must be a List[MenuItem]")
            if not all(issubclass(m.__class__, self.MenuItem) for m in attr):
                raise ValueError(f"MenuItems must be a List[MenuItem]")
            return attr

        def _build(self):
            self.css("drawer")

        def _build_wrapper(self):
            # Wrapper
            self.wrapper = BaseComponents.Div("p-4", "flex", "flex-col", "gap-4")

            # Drawer Content
            drawer_content = BaseComponents.Div("drawer-content", "flex", "flex-col")(
                DaisyUI.NavBar(title=self.title)(
                    BaseComponents.Ul("menu", "menu-horizontal", "hidden", "lg:flex")(
                        *[item.to_component() for item in self.menu_items],
                    )
                ),
                self.wrapper,
            )
            # Drawer Side
            drawer_side = BaseComponents.Div("drawer-side")(
                BaseComponents.Label(
                    "drawer-overlay", aria_label="close sidebar", for_="drawer-toggle"
                ),
                BaseComponents.Ul("menu", "bg-base-200", "min-h-full", "w-80", "p-4")(
                    BaseComponents.Li("mb-2", "font-bold")(str(self.title)),
                    *[item.to_component() for item in self.menu_items],
                ),
            )
            # Drawer State Input
            drawer_input = BaseComponents.Input(
                "drawer-toggle", id="drawer-toggle", type="checkbox"
            )
            self.append(drawer_input)
            self.append(drawer_content)
            self.append(drawer_side)
