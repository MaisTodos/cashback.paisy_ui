from ..core import PUIStyleMixinABC


class PUITextColorMixin(PUIStyleMixinABC):
    @property
    def text_neutral(self):
        self.css("text-neutral")
        return self

    @property
    def text_neutral_content(self):
        self.css("text-neutral-content")
        return self

    @property
    def text_primary(self):
        self.css("text-primary")
        return self

    @property
    def text_primary_content(self):
        self.css("text-primary-content")
        return self

    @property
    def text_secondary(self):
        self.css("text-secondary")
        return self

    @property
    def text_secondary_content(self):
        self.css("text-secondary-content")
        return self

    @property
    def text_content(self):
        self.css("text-accent")
        return self

    @property
    def text_accent_content(self):
        self.css("text-accent-content")
        return self

    @property
    def text_success(self):
        self.css("text-success")
        return self

    @property
    def text_success_content(self):
        self.css("text-success-content")
        return self

    @property
    def text_info(self):
        self.css("text-info")
        return self

    @property
    def text_info_content(self):
        self.css("text-info-content")
        return self

    @property
    def text_warning(self):
        self.css("text-warning")
        return self

    @property
    def text_warning_content(self):
        self.css("text-warning-content")
        return self

    @property
    def text_error(self):
        self.css("text-error")
        return self

    @property
    def text_error_content(self):
        self.css("text-error-content")
        return self
