from dataclasses import dataclass
from typing import List, Literal, Optional, Union

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


class PUIProgress(PUIComponentABC, PUILayoutMixin, PUIVariantMixin):
    """<progress class="progress"></progress>"""

    _variant_prefix = "progress"

    def __init__(
        self,
        *classes,
        value: Optional[int] = None,
        max: Optional[int] = None,
        **attributes,
    ):
        super().__init__(*classes, **attributes)
        if value:
            self.tag.attrs.update(value=str(value))
        if max:
            self.tag.attrs.update(max=str(max))


class PUIRadialProgress(PUIComponentABC, PUIVariantMixin):
    """<div class="radial-progress" role="progressbar"></div>"""

    _variant_prefix = "text"

    def __init__(self, *classes, value: int, max: int, **attributes):
        super().__init__(*classes, **attributes)
        _value = int((value / max) * 100)
        attrs = {
            "style": f"--value:{_value}",
            "aria-valuenow": _value,
        }
        self.tag.attrs.update(**attrs)
        self.tag.append(f"{_value}%")


# TODO: Make disapear and able to close
class PUIToast(PUIComponentABC):
    """<div class="toast z-99"></div>"""

    @dataclass
    class Message:
        variant: Literal[
            "primary", "secondary", "accent", "success", "info", "warning", "error"
        ]
        content: str

    def __init__(self, *classes, messages: List[Message], **attributes):
        super().__init__(*classes, **attributes)
        for message in messages:
            span, _ = parse_html(
                f"""<div class="alert alert-{message.variant}"><span>{message.content}</span></div>"""
            )
            self.tag.append(span)

    @property
    def toast_top(self):
        self.css("toast-top")
        return self

    @property
    def toast_start(self):
        self.css("toast-start")
        return self

    @property
    def toast_end(self):
        self.css("toast-end")
        return self

    @property
    def toast_middle(self):
        self.css("toast-middle")
        return self

    @property
    def toast_center(self):
        self.css("toast-center")
        return self
