from .core import BaseComponent


class BaseComponents:
    """Raw HTML Components"""

    class HTML(BaseComponent):
        """<html></html>"""

    class Head(BaseComponent):
        """<head></head>"""

    class Script(BaseComponent):
        """<script></script>"""

    class Link(BaseComponent):
        """<link></link>"""

    class Body(BaseComponent):
        """<body></body>"""

    class A(BaseComponent):
        """<a></a>"""

    class P(BaseComponent):
        """<p></p>"""

    class Span(BaseComponent):
        """<span></span>"""

    class Label(BaseComponent):
        """<label></label>"""

    class Button(BaseComponent):
        """<button></button>"""

    class Div(BaseComponent):
        """<div></div>"""

    class Details(BaseComponent):
        """<details></details>"""

    class Summary(BaseComponent):
        """<summary></summary>"""

    class Li(BaseComponent):
        """<li></li>"""

    class Ul(BaseComponent):
        """<ul></ul>"""

    class Input(BaseComponent):
        """<input></input>"""

    class Legend(BaseComponent):
        """<legend></legend>"""

    class Form(BaseComponent):
        """<form></form>"""

    class Table(BaseComponent):
        "<table></table>"

    class TBody(BaseComponent):
        "<tbody></tbody>"

    class THead(BaseComponent):
        "<thead></thead>"

    class TR(BaseComponent):
        "<tr></tr>"

    class TH(BaseComponent):
        "<th></th>"

    class TD(BaseComponent):
        "<td></td>"

    class Symbol(BaseComponent):
        """<span class="material-symbols-outlined">{symbol}</span>"""

        tag_name = "span"

        @property
        def symbol(self) -> str:
            attr = self.attrs.get("symbol", None)
            if not attr:
                raise ValueError("Symbol requires symbol attribute")
            return str(attr)

        def _build(self):
            self.css("material-symbols-outlined")
            self.append(self.symbol)
