from abc import abstractmethod
from typing import Optional

from bs4 import BeautifulSoup, Tag

_bs = BeautifulSoup(features="html")


class BaseComponent(Tag):
    tag_name: Optional[str] = None

    def __init__(self, *class_, **attributes):
        self.__popped_attrs = {}
        tag_name = self.tag_name if self.tag_name else self.__class__.__name__.lower()
        attrs = (
            {
                key.strip("_").replace("_", "-"): value
                for key, value in attributes.items()
            }
            if attributes
            else dict()
        )
        if class_:
            attrs["class"] = " ".join([c for c in class_ if type(c) == str])

        super().__init__(
            parser=_bs,
            name=tag_name,
            attrs=attrs,
        )
        self._build()

    def _build(self):
        pass

    def css(self, *classes):
        _class = self.attrs.get("class", "")
        _classes = [_class, *classes]
        self.attrs["class"] = " ".join(_classes).strip()
        return self

    def attrs_pop(self, attribute_name: str, default=None):
        if not attribute_name in self.__popped_attrs:
            self.__popped_attrs[attribute_name] = self.attrs.pop(
                attribute_name, default
            )
        value = self.__popped_attrs.get(attribute_name, default)
        return value

    def __call__(self, *components: "Tag | str"):
        for c in components:
            if c is None:
                continue
            self.append(c)
        return self


class SelfClosingBaseComponent(BaseComponent):
    @property
    def is_empty_element(self) -> bool:
        return True


class WrapperComponent(BaseComponent):
    wrapper: BaseComponent

    def __init__(self, *class_, **attributes):
        super().__init__(*class_, **attributes)
        self._build_wrapper()

    def __call__(self, *components: Tag | str):
        for c in components:
            self.wrapper.append(c)
        return self

    @abstractmethod
    def _build_wrapper(self):
        raise NotImplementedError
