from typing import Optional, Tuple
from uuid import NAMESPACE_DNS, uuid4, uuid5

from bs4 import BeautifulSoup, Tag
from bs4.element import NavigableString

from .exceptions import PUIBuildError


def generate_unique_id(name: Optional[str] = None):
    name = name or str(uuid4())
    return str(uuid5(NAMESPACE_DNS, name)).replace("-", "")


def parse_html(
    raw_html: str, wrapper_content_indicator="[[content]]"
) -> Tuple[Tag, Optional[Tag]]:
    """Returns a `Tag` representing the root element, also returns a secondary `Tag` if there is a wrapper inside the html"""
    use_line_break = "script" in raw_html
    raw_html = "".join(
        f"{'\n' if use_line_break else ''}{s.strip()}" for s in raw_html.split("\n")
    ).strip()
    soup = BeautifulSoup(raw_html.strip("\n"), "html.parser")
    if not soup.contents:
        raise PUIBuildError("Empty HTML")

    first_element = soup.contents[0]
    if not isinstance(first_element, Tag):
        raise PUIBuildError(f"Tag expected (reveiced {type(first_element)})")

    tag: Tag = first_element

    wrapper: Optional[Tag] = None
    wrapper_element = tag.find(string=wrapper_content_indicator)
    if wrapper_element:
        if not isinstance(wrapper_element, NavigableString):
            raise PUIBuildError(
                f"NavigableString expected (received {type(wrapper_element)})"
            )
        parent = wrapper_element.parent
        if parent and isinstance(parent, Tag):
            wrapper_element.replace_with("")
            wrapper = parent

    return tag, wrapper


def add_css(tag: Tag, *classes) -> Tag:
    """Includes a list o classes in the Tag css without replacing it"""
    _class = tag.attrs.get("class", "")
    if isinstance(_class, list):
        _class = " ".join(_class)
    _classes = [_class, *classes]
    tag.attrs["class"] = " ".join(_classes).strip()
    return tag


def parse_attributes_dict(attributes: Optional[dict] = None) -> dict:
    return (
        {key.strip("_").replace("_", "-"): value for key, value in attributes.items()}
        if attributes
        else {}
    )
