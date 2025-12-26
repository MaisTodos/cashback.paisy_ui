from dataclasses import dataclass
from typing import List, Optional

from ..core import PUIComponentABC
from ..exceptions import PUIBuildError
from ..mixins import PUIVariantMixin
from ..utils import parse_html
from .base import PUISymbol


class PUIDivider(PUIComponentABC, PUIVariantMixin):
    """<div class="divider"></div>"""

    _variant_prefix = "divider"

    def __init__(self, *classes, content: Optional[str] = None, **attributes):
        super().__init__(*classes, **attributes)
        if content:
            self.tag.append(content)

    @property
    def divider_horizontal(self):
        self.css("divider-horizontal")
        return self

    @property
    def divider_start(self):
        self.css("divider-start")
        return self

    @property
    def divider_end(self):
        self.css("divider-end")
        return self


class PUISidebarLayout(PUIComponentABC):
    """
    <div class="drawer">
      <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
      <div class="drawer-content flex flex-col">
        <!-- Navbar -->
        <div class="navbar bg-base-300 w-full">
          <div class="flex-none lg:hidden">
            <label for="my-drawer-2" aria-label="open sidebar" class="btn btn-square btn-ghost">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                class="inline-block h-6 w-6 stroke-current"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
                ></path>
              </svg>
            </label>
          </div>
          <div class="mx-2 flex-1 px-2" id="navbar-title"></div>
          <div class="hidden flex-none lg:block">
            <ul class="menu menu-horizontal">
            </ul>
          </div>
        </div>
        [[content]]
      </div>
      <div class="drawer-side">
        <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label>
        <ul class="menu bg-base-200 min-h-full w-80 p-4">
        </ul>
      </div>
    </div>
    """

    @dataclass
    class MenuItem:
        href: str
        content: str
        symbol: Optional[str] = None

    def __init__(self, *classes, title: str, menu_items: List[MenuItem], **attributes):
        super().__init__(*classes, **attributes)
        _title = self.tag.find("div", {"id": "navbar-title"})
        if not _title:
            raise PUIBuildError
        _title.append(title)

        uls = self.tag.find_all("ul")
        for item in menu_items:
            for ul in uls:
                li, _ = parse_html(
                    f"""<li class="display-flex flex-row items-center gap-2"></li>"""
                )
                a, _ = parse_html(f"<a href={item.href}></a>")
                if item.symbol:
                    a.append(PUISymbol(symbol=item.symbol).tag)
                a.append(item.content)
                li.append(a)
                ul.append(li)
