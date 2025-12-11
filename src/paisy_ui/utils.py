from typing import Optional, Tuple
from uuid import NAMESPACE_DNS, uuid4, uuid5

from bs4 import BeautifulSoup, Tag


def generate_unique_id(name: Optional[str] = None):
    name = name if name else str(uuid4())
    return str(uuid5(NAMESPACE_DNS, name)).replace("-", "")


def parse_html(
    raw_html: str, wrapper_content_indicator="[[content]]"
) -> Tuple[Tag, Optional[Tag]]:
    """Returns a `Tag` representing the root element, also returns a secondary `Tag` if there is a wrapper inside the html"""
    use_line_break = "script" in raw_html
    raw_html = "".join(
        f"{'\n' if use_line_break else ''}{s.strip()}" for s in raw_html.split("\n")
    ).strip()
    tag: Tag = BeautifulSoup(raw_html.strip("\n"), "html.parser").contents[0]  # type: ignore

    wrapper: Optional[Tag] = None
    wrapper = tag.find(string=wrapper_content_indicator)  # type: ignore
    if wrapper:
        parent = wrapper.parent
        wrapper.replace_with("")
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
        else dict()
    )
