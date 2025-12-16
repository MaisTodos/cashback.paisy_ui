from ..core import PUIStyleMixinABC


class PUIBackgroundColorMixin(PUIStyleMixinABC):
    _bg_color_mixin_prefix: str = "bg"

    @property
    def bg_base(self):
        self.css(f"{self._bg_color_mixin_prefix}-base-300")
        return self

    @property
    def bg_base_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-base-300-content")
        return self

    @property
    def bg_neutral(self):
        self.css(f"{self._bg_color_mixin_prefix}-neutral")
        return self

    @property
    def bg_neutral_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-neutral-content")
        return self

    @property
    def bg_primary(self):
        self.css(f"{self._bg_color_mixin_prefix}-primary")
        return self

    @property
    def bg_primary_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-primary-content")
        return self

    @property
    def bg_secondary(self):
        self.css(f"{self._bg_color_mixin_prefix}-secondary")
        return self

    @property
    def bg_secondary_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-secondary-content")
        return self

    @property
    def bg_accent(self):
        self.css(f"{self._bg_color_mixin_prefix}-accent")
        return self

    @property
    def bg_accent_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-accent-content")
        return self

    @property
    def bg_success(self):
        self.css(f"{self._bg_color_mixin_prefix}-success")
        return self

    @property
    def bg_success_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-success-content")
        return self

    @property
    def bg_info(self):
        self.css(f"{self._bg_color_mixin_prefix}-info")
        return self

    @property
    def bg_info_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-info-content")
        return self

    @property
    def bg_warning(self):
        self.css(f"{self._bg_color_mixin_prefix}-warning")
        return self

    @property
    def bg_warning_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-warning-content")
        return self

    @property
    def bg_error(self):
        self.css(f"{self._bg_color_mixin_prefix}-error")
        return self

    @property
    def bg_error_content(self):
        self.css(f"{self._bg_color_mixin_prefix}-error-content")
        return self
