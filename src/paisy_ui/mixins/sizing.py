from ..core import PUIStyleMixinABC


class PUIWidthMixin(PUIStyleMixinABC):
    @property
    def width_sm(self):
        self.css("w-12")
        return self

    @property
    def width_md(self):
        self.css("w-36")
        return self

    @property
    def width_lg(self):
        self.css("w-64")
        return self

    @property
    def width_xl(self):
        self.css("w-128")
        return self

    @property
    def width_full(self):
        self.css("w-full")
        return self

    @property
    def width_min(self):
        self.css("w-min")
        return self

    @property
    def width_half(self):
        self.css("w-1/2")
        return self


class PUIHeightMixin(PUIStyleMixinABC):
    @property
    def height_sm(self):
        self.css("h-12")
        return self

    @property
    def height_md(self):
        self.css("h-36")
        return self

    @property
    def height_lg(self):
        self.css("h-64")
        return self

    @property
    def height_xl(self):
        self.css("h-128")
        return self

    @property
    def height_full(self):
        self.css("h-full")
        return self

    @property
    def height_min(self):
        self.css("h-min")
        return self

    @property
    def height_half(self):
        self.css("h-1/2")
        return self
