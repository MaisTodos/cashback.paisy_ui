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
