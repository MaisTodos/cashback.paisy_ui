from ..core import PUIStyleMixinABC


class PUIPaddingMixin(PUIStyleMixinABC):
    @property
    def padding_sm(self):
        self.css("p-2")
        return self

    @property
    def padding_md(self):
        self.css("p-4")
        return self

    @property
    def padding_lg(self):
        self.css("p-8")
        return self

    @property
    def padding_xl(self):
        self.css("p-12")
        return self


class PUIMarginMixin(PUIStyleMixinABC):
    @property
    def margin_sm(self):
        self.css("m-2")
        return self

    @property
    def margin_md(self):
        self.css("m-4")
        return self

    @property
    def margin_lg(self):
        self.css("m-8")
        return self

    @property
    def margin_xl(self):
        self.css("m-12")
        return self
