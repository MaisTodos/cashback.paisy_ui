from ..core import PUIComponentABC
from ..mixins import PUIBorderMixin, PUIColorsMixins, PUILayoutMixin


class PUIHTML(PUIComponentABC):
    """
    <html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
        <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0"
            rel="stylesheet" type="text/css" />
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

        window.addEventListener('load', () => {
            setUpdateCountdowndsInterval();
        });
    </script>
    </body>
    </html>
    """


class PUIDiv(PUIComponentABC, PUIColorsMixins, PUILayoutMixin, PUIBorderMixin):
    """<div></div>"""


class PUIText(PUIComponentABC, PUIColorsMixins, PUILayoutMixin, PUIBorderMixin):
    """<p></p>"""


class PUITitle(PUIComponentABC, PUIColorsMixins, PUILayoutMixin, PUIBorderMixin):
    """<h5 class="font-bold text-xl"></h5>"""
