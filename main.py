from paisy_ui.components import (
    PUIHTML,
    PUIAvatar,
    PUIButton,
    PUICard,
    PUICollapse,
    PUICountdown,
    PUIDiv,
    PUIHover3dCard,
    PUIImgCarousel,
    PUIKbd,
    PUIModal,
    PUISwap,
    PUIText,
    PUIThemeController,
    PUITitle,
)

# https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp

modal = PUIModal(id="modal_01")[
    PUIDiv().display_flex_col.gap_md[
        PUIHover3dCard(img_src="https://img.daisyui.com/images/stock/creditcard.webp"),
        PUITitle().text_secondary["Este é o seu Cartão!"],
        PUIText()["Muito legal né?"],
        PUIButton().secondary.soft["Histórico de Transações"],
        PUIButton().secondary.dash["Bloquear Cartão"],
    ]
]

page = PUIHTML()[
    PUIDiv().padding_lg.margin_lg.display_flex_col.items_start.justify_center[
        modal,
        PUIThemeController(value="dark"),
        PUIHover3dCard(img_src="https://img.daisyui.com/images/stock/creditcard.webp"),
        PUICollapse(title="Clique aqui para expandir!")[PUIText()["Aqui vai um texto"]],
        PUIImgCarousel(
            img_srcs=[
                "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
            ]
        ),
        PUICard().image_full(
            "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
        )[
            PUITitle().text_primary_content["Eu sou um card!"],
            PUIText()["Aqui tem um texto"],
            PUIAvatar(
                src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            ).width_sm.height_sm,
        ],
        PUISwap(on="Clique Aqui 😠", off="Clique Aqui 😁").text_4xl,
        PUICountdown(
            values=[
                PUICountdown.Value(value=10, sufix="h"),
                PUICountdown.Value(value=59, sufix="m"),
                PUICountdown.Value(value=59, sufix="s"),
            ]
        ),
        PUIDiv()[
            PUIText()[
                "Pressione ", PUIKbd()["ALT"], " + ", PUIKbd()["R"], " para fazer algo"
            ]
        ],
        PUIButton(onclick=f"{modal.id}.showModal()").primary.width_full.soft[
            "Abrir Modal"
        ],
    ],
]

with open("index.html", "w+") as file:
    file.write(str(page))
