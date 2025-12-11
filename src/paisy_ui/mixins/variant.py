from ..core import PUIStyleMixinABC


class PUIVariantMixin(PUIStyleMixinABC):
    _variant_prefix: str = "bg"

    @property
    def dash(self):
        self.css(f"{self._variant_prefix}-dash")
        return self

    @property
    def soft(self):
        self.css(f"{self._variant_prefix}-soft")
        return self

    @property
    def ghost(self):
        self.css(f"{self._variant_prefix}-ghost")
        return self

    @property
    def base(self):
        self.css(f"{self._variant_prefix}-base-300")
        return self

    @property
    def neutral(self):
        self.css(f"{self._variant_prefix}-neutral")
        return self

    @property
    def primary(self):
        self.css(f"{self._variant_prefix}-primary")
        return self

    @property
    def secondary(self):
        self.css(f"{self._variant_prefix}-secondary")
        return self

    @property
    def accent(self):
        self.css(f"{self._variant_prefix}-accent")
        return self

    @property
    def success(self):
        self.css(f"{self._variant_prefix}-success")
        return self

    @property
    def info(self):
        self.css(f"{self._variant_prefix}-info")
        return self

    @property
    def warning(self):
        self.css(f"{self._variant_prefix}-warning")
        return self

    @property
    def error(self):
        self.css(f"{self._variant_prefix}-error")
        return self
