from ..core import PUIStyleMixinABC


class PUIDisplayMixin(PUIStyleMixinABC):
    @property
    def display_hidden(self):
        self.css("hidden")
        return self

    @property
    def sm__hidden(self):
        self.css("sm:hidden")
        return self

    @property
    def md__hidden(self):
        self.css("md:hidden")
        return self

    @property
    def lg__hidden(self):
        self.css("lg:hidden")
        return self

    @property
    def display_flex_col(self):
        self.css("flex flex-col")
        return self

    @property
    def display_flex_row(self):
        self.css("flex flex-row")
        return self

    @property
    def items_center(self):
        self.css("items-center")
        return self

    @property
    def justify_center(self):
        self.css("justify-center")
        return self

    @property
    def justify_between(self):
        self.css("justify-between")
        return self

    @property
    def items_start(self):
        self.css("items-start")
        return self

    @property
    def justify_start(self):
        self.css("justify-start")
        return self

    @property
    def items_end(self):
        self.css("items-end")
        return self

    @property
    def justify_end(self):
        self.css("justify-end")
        return self

    @property
    def display_grid(self):
        self.css("grid")
        return self

    @property
    def grid_cols_auto(self):
        self.css("grid-cols-auto")
        return self

    @property
    def grid_cols_2(self):
        self.css("grid-cols-2")
        return self

    @property
    def grid_cols_3(self):
        self.css("grid-cols-3")
        return self

    @property
    def grid_cols_4(self):
        self.css("grid-cols-4")
        return self

    @property
    def gap_sm(self):
        self.css("gap-2")
        return self

    @property
    def gap_md(self):
        self.css("gap-4")
        return self

    @property
    def gap_lg(self):
        self.css("gap-8")
        return self

    @property
    def gap_xl(self):
        self.css("gap-12")
        return self
