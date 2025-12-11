from abc import ABC, abstractmethod
from typing import Optional, Union

from bs4 import Tag

from .utils import add_css, parse_attributes_dict, parse_html


class PUIComponentABC(ABC):
    tag: Tag
    wrapper: Optional[Tag] = None

    def __init__(self, *classes, **attributes):
        raw_html = self.__doc__
        if not raw_html:
            raise NotImplementedError(
                f"{self.__class__.__name__} without __doc__ defined"
            )
        tag, wrapper = parse_html(raw_html)
        self.tag = tag
        self.wrapper = wrapper
        attrs = parse_attributes_dict(attributes=attributes)
        self.tag.attrs.update(**attrs)
        self.css(*classes)

    def __str__(self) -> str:
        return self.tag.prettify(formatter="html5")

    def _append(self, child: Union[str, "Tag"]):
        if self.wrapper is not None:
            self.wrapper.append(child)
        else:
            self.tag.append(child)

    def append(self, child: Union[str, int, float, "PUIComponentABC"]):
        if isinstance(child, PUIComponentABC):
            self._append(child.tag)
        elif isinstance(child, str):
            self._append(child)
        elif isinstance(child, int) or isinstance(child, float):
            self._append(str(child))
        else:
            raise ValueError(f"Can not append {child} to {self}")

    def __getitem__(self, children):
        if isinstance(children, tuple):
            _children = children
        else:
            _children = (children,)

        for child in _children:
            self.append(child)
        return self

    def css(self, *classes):
        add_css(self.tag, *classes)
        return self


class PUIStyleMixinABC(ABC):
    @abstractmethod
    def css(self, *classes):
        pass
