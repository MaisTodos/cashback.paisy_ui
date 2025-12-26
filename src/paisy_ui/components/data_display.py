from dataclasses import dataclass
from typing import List, Optional, Union

from ..core import PUIComponentABC, Tag
from ..exceptions import PUIBuildError
from ..mixins import PUIBorderMixin, PUILayoutMixin, PUIVariantMixin
from ..utils import add_css, generate_unique_id, parse_html
from .base import PUISymbol

# TODO: Implement
# class PUIAccordion(PUIComponentABC):
#     pass


class PUIAvatar(PUIComponentABC, PUIBorderMixin):
    """
    <div class="avatar">
        <div class="rounded-full">
            [[content]]
            <img src="" />
        </div>
    </div>
    """

    def __init__(self, *classes, src: str, **attributes):
        super().__init__(*classes, **attributes)
        img = self.tag.find("img")
        if not img:
            raise PUIBuildError
        img.attrs.update(src=src)

    @property
    def sm(self):
        if not self.wrapper:
            raise PUIBuildError
        add_css(self.wrapper, "w-8", "h-8")
        return self

    @property
    def md(self):
        if not self.wrapper:
            raise PUIBuildError
        add_css(self.wrapper, "w-12", "h-12")
        return self

    @property
    def lg(self):
        if not self.wrapper:
            raise PUIBuildError
        add_css(self.wrapper, "w-24", "h-24")
        return self

    @property
    def xl(self):
        if not self.wrapper:
            raise PUIBuildError
        add_css(self.wrapper, "w-48", "h-48")
        return self

    @property
    def online(self):
        self.css("avatar-online")
        return self

    @property
    def offline(self):
        self.css("avatar-offline")
        return self


class PUIBadge(PUIComponentABC, PUIBorderMixin, PUILayoutMixin, PUIVariantMixin):
    """<span class="badge">[[content]]</span>"""

    _variant_prefix = "badge"


class PUICard(PUIComponentABC, PUIBorderMixin, PUILayoutMixin):
    """
    <div class="card card-border bg-base-100 w-96 shadow-sm">
        <div class="card-body">[[content]]</div>
    </div>
    """

    def __init__(self, *classes, **attributes):
        super().__init__(*classes, **attributes)

    def image_full(self, img_src: str) -> "PUICard":
        self.css("image-full")
        img, _ = parse_html(
            f"""
        <figure>
            <img src="{img_src}" alt="Shoes" />
        </figure>
        """
        )
        if not self.wrapper:
            raise PUIBuildError
        self.wrapper.insert_before(img)
        return self


class PUICarouselABC(PUIComponentABC):
    """
    <div class="carousel w-full rounded">[[content]]</div>
    """

    def __init__(self, *classes, items: List[Tag], **attributes):
        super().__init__(*classes, **attributes)
        if not self.wrapper:
            raise PUIBuildError
        for index, tag in enumerate(items):
            item = self.build_item(tag=tag, index=index)
            self.wrapper.append(item)

    def build_item(self, tag: Tag, index: int = 0) -> Tag:
        item, _ = parse_html(
            f"""<div id="slide{index}" class="carousel-item relative w-full"></div>"""
        )
        item.append(tag)
        return tag


class PUIImgCarousel(PUICarouselABC):
    """
    <div class="carousel w-full">[[content]]</div>
    """

    def __init__(self, *classes, img_srcs: List[str], **attributes):
        items = []
        for index, img_src in enumerate(img_srcs):
            item, _ = parse_html(
                f"""
            <div id="slide{index}" class="carousel-item relative w-full">
                <img src="{img_src}" class="w-full" />
                <div class="absolute left-5 right-5 top-1/2 flex -translate-y-1/2 transform justify-between">
                <a href="#slide{index-1}" class="btn btn-circle">❮</a>
                <a href="#slide{index+1}" class="btn btn-circle">❯</a>
                </div>
            </div>"""
            )
            items.append(item)

        super().__init__(
            *classes,
            items=items,
            **attributes,
        )


class PUICollapse(PUIComponentABC, PUIBorderMixin, PUILayoutMixin):
    """
    <div tabindex="0" class="collapse collapse-arrow">
        <div class="collapse-content text-sm">[[content]]</div>
    </div>
    """

    def __init__(self, *classes, title: str, **attributes):
        super().__init__(*classes, **attributes)
        if not self.wrapper:
            raise PUIBuildError
        collapse_title, _ = parse_html(
            f'<div class="collapse-title font-semibold">{title}</div>'
        )
        self.wrapper.insert_before(collapse_title)


class PUICountdown(PUIComponentABC):
    """
    <span class="countdown">
    </span>
    """

    @dataclass
    class Value:
        value: int
        sufix: Optional[str] = None

    def __init__(
        self, *classes, values: List[Value], id: Optional[str] = None, **attributes
    ):
        id = id if id else generate_unique_id()
        attributes.update(id=id)
        super().__init__(*classes, **attributes)
        for value in values:
            span, _ = parse_html(
                f'<span style="--value:{value.value};" aria-live="polite" aria-label="{value.value}">{value.value}</span>'
            )
            self.tag.append(span)
            if value.sufix:
                self.tag.append(value.sufix)


# TODO: Implement
# class PUIDiff(PUIComponentABC):
#     pass


class PUIHover3dCard(PUIComponentABC):
    """
    <div class="hover-3d mx-auto">
        <!-- content -->
        <figure class="max-w-100 rounded-2xl">
            [[content]]
        </figure>
        <!-- 8 empty divs needed for the 3D effect -->
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
    </div>
    """


class PUIHover3dCardImg(PUIComponentABC):
    """
    <div class="hover-3d mx-auto">
        <!-- content -->
        <figure class="max-w-100 rounded-2xl">
            <img src="" alt="3D card" />
        </figure>
        <!-- 8 empty divs needed for the 3D effect -->
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
    </div>
    """

    def __init__(self, *classes, img_src: str, **attributes):
        super().__init__(*classes, **attributes)
        img = self.tag.find("img")
        if not img:
            raise PUIBuildError
        img.attrs.update(src=img_src)


# TODO: Implement
# class PUIHoverGallery(PUIComponentABC):
#     pass


class PUIKbd(PUIComponentABC):
    """<kbd class="kbd"></kbd>"""


class PUIList(PUIComponentABC):
    """<ul class="list rounded-box shadow-md">[[content]]</ul>"""

    def __init__(self, *classes, title: Optional[str] = None, **attributes):
        super().__init__(*classes, **attributes)
        if title:
            li_title, _ = parse_html(
                f'<li class="p-4 pb-2 text-xs opacity-60 tracking-wide">{title}</li>'
            )
            self.tag.append(li_title)

    def _format_child(self, child: str | int | float | PUIComponentABC) -> Tag:
        tag = super()._format_child(child)
        return add_css(tag, "list-row")


class PUIStat(PUIComponentABC, PUIVariantMixin):
    """
    <div class="stats shadow">
        <div class="stat">
            [[content]]
            <div class="stat-title"></div>
            <div class="stat-value"></div>
            <div class="stat-desc"></div>
        </div>
    </div>
    """

    _variant_prefix = "text"

    @property
    def title(self) -> Tag:
        _title = self.tag.find(attrs={"class": "stat-title"})
        if not _title:
            raise PUIBuildError
        return _title

    @property
    def value(self) -> Tag:
        _value = self.tag.find(attrs={"class": "stat-value"})
        if not _value:
            raise PUIBuildError
        return _value

    @property
    def desc(self) -> Tag:
        _desc = self.tag.find(attrs={"class": "stat-desc"})
        if not _desc:
            raise PUIBuildError
        return _desc

    @property
    def figure(self) -> Optional[Tag]:
        return self.tag.find(attrs={"class": "stat-figure"})

    def __init__(
        self,
        *classes,
        title: str,
        value: str,
        desc: str,
        symbol: Optional[str] = None,
        **attributes,
    ):
        super().__init__(*classes, **attributes)
        if symbol:
            _symbol_wrapper, _ = parse_html('<div class="stat-figure"></div>')
            if not self.wrapper:
                raise PUIBuildError
            self.wrapper.append(
                PUISymbol(symbol=symbol).text_4xl.tag.wrap(_symbol_wrapper)
            )
        self.title.append(title)
        self.value.append(value)
        self.desc.append(desc)

    def css(self, *classes):
        if self.figure:
            add_css(self.figure, *classes)
        add_css(self.value, *classes)
        return self


class PUIStatus(PUIComponentABC, PUIVariantMixin):
    """<div class="status"></div>"""

    _variant_prefix = "status"


class PUITable(PUIComponentABC):
    """<div class="overflow-x-auto rounded-box card-border shadow-sm"><table class="table table-zebra">[[content]]</tabe></div>"""

    def __build_thead(self, columns: List[Union[str, PUIComponentABC]]) -> Tag:
        thead, _ = parse_html("<thead></thead>")
        for col in columns:
            _col, _ = parse_html("<th></th>")
            if isinstance(col, PUIComponentABC):
                _col.append(col.tag)
            else:
                _col.append(col)
            thead.append(_col)
        return thead

    def __build_tbody(self, rows: List[List[Union[str, PUIComponentABC]]]) -> Tag:
        tbody, _ = parse_html("<tbody></tbody>")
        for columns in rows:
            row, _ = parse_html(
                '<tr class="hover:bg-base-300 transition-all ease-in-out"></tr>'
            )
            for col in columns:
                _col, _ = parse_html("<td></td>")
                if isinstance(col, PUIComponentABC):
                    _col.append(col.tag)
                else:
                    _col.append(col)
                row.append(_col)
            tbody.append(row)
        return tbody

    def __init__(
        self,
        *classes,
        columns: List[Union[str, PUIComponentABC]],
        rows: List[List[Union[str, PUIComponentABC]]],
        **attributes,
    ):
        super().__init__(*classes, **attributes)
        thead = self.__build_thead(columns=columns)
        tbody = self.__build_tbody(rows=rows)
        if not self.wrapper:
            raise PUIBuildError
        self.wrapper.append(thead)
        self.wrapper.append(tbody)


class PUITextRotate(PUIComponentABC):
    """<span class="text-rotate text-7xl leading-[2]"><span class="justify-items-center">[[content]]</span></span>"""


# TODO: Implement
# class PUITimeline(PUIComponentABC):
#     """foo"""
