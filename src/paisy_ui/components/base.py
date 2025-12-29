from ..core import PUIComponentABC
from ..mixins import (
    PUIBorderMixin,
    PUIColorsMixins,
    PUIFontWeightMixin,
    PUILayoutMixin,
    PUITextSizeMixin,
)


class PUIHTML(PUIComponentABC):
    """
    <html class="preload">
    <head>
        <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
        <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
        <script type="module">
            import { codeToHtml, createHighlighter } from 'https://esm.sh/shiki@3.0.0'

            document.querySelectorAll("code[data-lang='python']").forEach(async (el) => {
                el.innerHTML = await codeToHtml(el.innerHTML, { lang: 'python', theme: 'github-dark-default' });
            });
        </script>
        <style>
            .shiki {
                background: transparent !important;
            }
            @font-face {
                font-family: 'Material Symbols Outlined';
                font-style: normal;
                font-weight: 100 700;
                src: url(https://fonts.gstatic.com/s/materialsymbolsoutlined/v303/kJEhBvYX7BgnkSrUwT8OhrdQw4oELdPIeeII9v6oFsI.woff2) format('woff2');
            }

            .material-symbols-outlined {
                font-family: 'Material Symbols Outlined';
                font-weight: normal;
                font-style: normal;
                line-height: 1;
                letter-spacing: normal;
                text-transform: none;
                display: inline-block;
                white-space: nowrap;
                word-wrap: normal;
                direction: ltr;
                -webkit-font-feature-settings: 'liga';
                -webkit-font-smoothing: antialiased;
            }

            html.preload body > * {
                opacity: 0;
            }
            html:not(.preload) body > * {
                transition: opacity .3s ease;
            }

        </style>
    </head>

    <body>
    <script>
        let intervalUpdateCountdowns = null;

        const shouldUpdateCountdowns = () => {
            return document.querySelectorAll('span.countdown span:not([aria-label="0"])').length > 0;
        }


        const updateCountdowns = () => {
            document.querySelectorAll('span.countdown').forEach(wrapper => {
                const segments = Array.from(wrapper.querySelectorAll('span[aria-label]'));
                if (segments.length === 0) return;

                for (let i = segments.length - 1; i >= 0; i--) {
                    const el = segments[i];
                    let currentValue = parseInt(el.getAttribute('aria-label'));

                    if (currentValue > 0) {
                        currentValue -= 1;
                        el.setAttribute('aria-label', currentValue);
                        el.style.setProperty('--value', currentValue);
                        break;
                    }

                    if (i > 0) {
                        const startValue = el.innerHTML
                        el.setAttribute('aria-label', startValue);
                        el.style.setProperty('--value', startValue);
                    }
                }
            });
        };


        const clearUpdateCountdownsInterval = () => {
            clearInterval(intervalUpdateCountdowns);
            intervalUpdateCountdowns = null;
        }

        const setUpdateCountdowndsInterval = () => {
            intervalUpdateCountdowns = setInterval(() => {
                if(!shouldUpdateCountdowns()) {
                    return clearUpdateCountdownsInterval();
                }
                updateCountdowns();
            }, 1000)
        }
        const setTheme = (theme) => {
            document.documentElement.setAttribute("data-theme", theme);
            localStorage.setItem("theme", theme)
        }

        const themeSaved = localStorage.getItem("theme");
        const themePrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
        const themeDefault = themePrefersDark ? "dark" : "light";
        const theme = themeSaved || themeDefault;
        setTheme(theme);

        window.addEventListener('load', () => {
            setUpdateCountdowndsInterval();
            document.documentElement.classList.remove('preload');

            const themeToggle = document.querySelector('input.theme-controller[type="checkbox"]');
            themeToggle.checked = theme == "dark";
            themeToggle.addEventListener('change', (ev) => {
                setTheme(ev.target.checked ? 'dark' : 'light');
            })
        });


    </script>
    </body>
    </html>
    """

    def __init__(self, *classes, **attributes):
        super().__init__(*classes, **attributes)
        self._wrapper = self.find("body")


class PUIDiv(
    PUIComponentABC, PUIColorsMixins, PUILayoutMixin, PUIBorderMixin, PUIFontWeightMixin
):
    """<div></div>"""


class PUIText(
    PUIComponentABC,
    PUIColorsMixins,
    PUILayoutMixin,
    PUIBorderMixin,
    PUITextSizeMixin,
    PUIFontWeightMixin,
):
    """<p></p>"""


class PUITitle(PUIComponentABC, PUIColorsMixins, PUILayoutMixin, PUIBorderMixin):
    """<h5 class="font-bold text-xl"></h5>"""


class PUIImg(PUIComponentABC):
    """<img src="">"""

    def __init__(self, *classes, src: str, **attributes):
        super().__init__(*classes, **attributes)
        self.tag.attrs.update(src=src)


class PUISymbol(PUIComponentABC, PUIColorsMixins, PUILayoutMixin, PUITextSizeMixin):
    """<span class="material-symbols-outlined"></span>"""

    def __init__(self, *classes, symbol: str, **attributes):
        super().__init__(*classes, **attributes)
        self.tag.append(symbol)
