from ..core import PUIStyleMixinABC


class PUIFontWeightMixin(PUIStyleMixinABC):
    @property
    def font_bold(self):
        self.css("font-bold")
        return self


class PUITextSizeMixin(PUIStyleMixinABC):
    @property
    def text_sm(self):
        self.css("text-sm")
        return self

    @property
    def text_md(self):
        self.css("text-md")
        return self

    @property
    def text_lg(self):
        self.css("text-lg")
        return self

    @property
    def text_xl(self):
        self.css("text-xl")
        return self

    @property
    def text_2xl(self):
        self.css("text-2xl")
        return self

    @property
    def text_3xl(self):
        self.css("text-3xl")
        return self

    @property
    def text_4xl(self):
        self.css("text-4xl")
        return self

    @property
    def text_5xl(self):
        self.css("text-5xl")
        return self

    @property
    def text_6xl(self):
        self.css("text-6xl")
        return self
        return self
