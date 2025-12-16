from dataclasses import dataclass
from typing import List, Optional, Union

from ..core import PUIComponentABC, Tag
from ..mixins import PUIBorderMixin, PUILayoutMixin, PUIVariantMixin
from ..utils import add_css, generate_unique_id, parse_html
from .base import PUISymbol


class PUIAlert(PUIComponentABC, PUIVariantMixin):
    """<div role="alert" class="alert"></div>"""

    _variant_prefix = "alert"

    def __init__(
        self,
        *classes,
        symbol: str,
        message: str,
        close_button: bool = False,
        **attributes,
    ):
        super().__init__(*classes, **attributes)
        if symbol:
            self.tag.append(PUISymbol(symbol=symbol).text_2xl.tag)
        span, _ = parse_html(f"<span>{message}</span>")
        self.tag.append(span)

        if close_button:
            btn, _ = parse_html(
                '<button class="btn btn-neutral btn-sm btn-ghost" onclick=""><span class="material-symbols-outlined text-lg">close</span></button>'
            )
            self.tag.append(btn)


class PUILoading(PUIComponentABC, PUIVariantMixin):
    """<span class="loading"></span>"""

    _variant_prefix = "text"

    @property
    def spinner(self):
        self.css("loading-spinner")
        return self

    @property
    def bars(self):
        self.css("loading-bars")
        return self

    @property
    def ball(self):
        self.css("loading-ball")
        return self

    @property
    def ring(self):
        self.css("loading-ring")
        return self

    @property
    def dots(self):
        self.css("loading-dots")
        return self

    @property
    def sm(self):
        self.css("loading-sm")
        return self

    @property
    def md(self):
        self.css("loading-md")
        return self

    @property
    def lg(self):
        self.css("loading-lg")
        return self

    @property
    def xl(self):
        self.css("loading-xl")
        return self
