from abc import ABC, abstractmethod
from typing import Optional, Union

from bs4 import Tag

from .exceptions import PUIBuildError, PUIFindError
from .utils import add_css, parse_attributes_dict, parse_html


class PUIComponentABC(ABC):
    tag: Tag
    _wrapper: Optional[Tag] = None

    def __init__(self, *classes, **attributes):
        raw_html = self.__doc__
        if not raw_html:
            raise NotImplementedError(
                f"{self.__class__.__name__} without __doc__ defined"
            )
        tag, wrapper = parse_html(raw_html)
        self.tag = tag
        self._wrapper = wrapper
        attrs = parse_attributes_dict(attributes=attributes)
        self.tag.attrs.update(**attrs)
        self.css(*classes)

    def __str__(self) -> str:
        return self.tag.prettify(formatter="html5")

    def _append(self, child: Union[str, "Tag"]) -> None:
        if self._wrapper is not None:
            self._wrapper.append(child)
        else:
            self.tag.append(child)

    def _format_child(self, child: Union[str, int, float, "PUIComponentABC"]) -> Tag:
        if isinstance(child, PUIComponentABC):
            return child.tag
        elif isinstance(child, (str, int, float)):
            tag, _ = parse_html(f"<span>{child}</span>")
            return tag
        else:
            raise ValueError(f"Can not append {child} to {self}")

    def append(self, child: Union[str, int, float, "PUIComponentABC"]):
        self._append(self._format_child(child=child))

    def __getitem__(self, children: Union[tuple, str, int, float, "PUIComponentABC"]) -> "PUIComponentABC":
        if isinstance(children, tuple):
            _children = children
        else:
            _children = (children,)

        for child in _children:
            self.append(child)
        return self

    def css(self, *classes: str) -> "PUIComponentABC":
        add_css(self.tag, *classes)
        return self

    def find(self, tag_name: Optional[str] = None, attrs: Optional[dict] = None) -> Tag:
        tag = self.tag.find(name=tag_name, attrs=attrs if attrs else {})
        if not tag:
            raise PUIFindError(f"{self} - {tag_name} ({attrs})")
        return tag

    @property
    def wrapper(self) -> Tag:
        if self._wrapper is None:
            raise PUIBuildError(f"{self}.wrapper")
        return self._wrapper

    @property
    def skeleton(self) -> "PUIComponentABC":
        self.css("skeleton")
        return self

    @property
    def skeleton_text(self) -> "PUIComponentABC":
        self.css("skeleton", "skeleton-text")
        return self

    def tooltip(self, content: str) -> "PUIComponentABC":
        add_css(self.tag, "tooltip")
        self.tag.attrs.update(**{"data-tip": content})
        return self


class PUIStyleMixinABC(ABC):
    @abstractmethod
    def css(self, *classes):
        pass
