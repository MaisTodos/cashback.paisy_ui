from .background_color import PUIBackgroundColorMixin
from .border import PUIRoundedMixin
from .display import PUIDisplayMixin
from .sizing import PUIHeightMixin, PUIWidthMixin
from .spacing import PUIMarginMixin, PUIPaddingMixin
from .text_color import PUITextColorMixin
from .typography import PUITextSizeMixin
from .variant import PUIVariantMixin


class PUIColorsMixins(PUITextColorMixin, PUIBackgroundColorMixin):
    pass


class PUILayoutMixin(
    PUIDisplayMixin, PUIMarginMixin, PUIPaddingMixin, PUIHeightMixin, PUIWidthMixin
):
    pass


class PUIBorderMixin(PUIRoundedMixin):
    pass


__all__ = [
    "PUIColorsMixins",
    "PUILayoutMixin",
    "PUIVariantMixin",
    "PUIBackgroundColorMixin",
    "PUITextColorMixin",
    "PUIDisplayMixin",
    "PUIMarginMixin",
    "PUIRoundedMixin",
    "PUIPaddingMixin",
    "PUIHeightMixin",
    "PUIWidthMixin",
    "PUITextSizeMixin",
    "PUIBorderMixin",
]
