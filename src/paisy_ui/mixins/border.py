from ..core import PUIStyleMixinABC


class PUIRoundedMixin(PUIStyleMixinABC):
    @property
    def rounded_sm(self):
        self.css("rounded-sm")
        return self

    @property
    def rounded_md(self):
        self.css("rounded-md")
        return self

    @property
    def rounded_lg(self):
        self.css("rounded-lg")
        return self

    @property
    def rounded_xl(self):
        self.css("rounded-xl")
        return self

    @property
    def rounded_full(self):
        self.css("rounded-full")
        return self
