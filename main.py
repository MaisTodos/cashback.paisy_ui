from paisy_ui.components import (
    PUIHTML,
    PUIAvatar,
    PUIButton,
    PUICard,
    PUICollapse,
    PUICountdown,
    PUIDiv,
    PUIHover3dCard,
    PUIHover3dCardImg,
    PUIImg,
    PUIImgCarousel,
    PUIKbd,
    PUIList,
    PUIModal,
    PUIStat,
    PUIStatus,
    PUISwap,
    PUISymbol,
    PUIText,
    PUIThemeController,
    PUITitle,
)

# https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp

transacoes = [
    ("15/12/2025", 20.00),
    ("14/12/2025", -34.00),
    ("13/12/2025", 21.00),
    ("12/12/2025", -11.00),
    ("11/12/2025", 5.00),
    ("10/12/2025", 8.90),
]

modal = PUIModal(id="modal_01")[
    PUIDiv().display_flex_col.gap_md[
        PUIHover3dCard()[
            PUIDiv(
                "w-100", "h-60", "relative"
            ).padding_md.bg_primary.text_primary_content.display_grid.grid_cols_2.gap_md[
                PUIImg(
                    "absolute",
                    "inset-0",
                    "left-15",
                    "h-full",
                    "mix-blend-hard-light",
                    "grayscale",
                    src="https://i0.wp.com/parceiros.cartaodetodos.com.br/wp-content/uploads/2023/05/Sem-Titulo-1.png?fit=300%2C300&ssl=1",
                ),
                PUIDiv("mt-auto").display_flex_col[
                    "Alfredo da Silva", "126748126487112"
                ],
                PUIDiv("mt-auto").display_flex_col.items_end["Exp. 10/30", "CVV 12134"],
            ]
        ],
        PUITitle().text_primary["Este é o seu Cartão!"],
        PUIText()["Muito legal né?"],
        PUIList(title="Últimas Transações")[
            *(
                PUIDiv().display_flex_row.items_center.justify_between[
                    data,
                    (
                        PUIDiv().display_flex_row.items_center.gap_sm.text_error[
                            f"R$ {valor:.2f}", PUISymbol(symbol="more_down")
                        ]
                        if valor < 0
                        else PUIDiv().display_flex_row.items_center.gap_sm.text_success[
                            f"R$ {valor:.2f}", PUISymbol(symbol="more_up")
                        ]
                    ),
                ]
                for data, valor in transacoes
            )
        ],
        PUIButton().primary.soft["Histórico de Completo"],
        PUIButton().primary.dash["Bloquear Cartão"],
    ]
]

page = PUIHTML()[
    PUIDiv().padding_lg.margin_lg.display_flex_row.items_start.justify_center.gap_md[
        modal,
        PUIDiv().display_flex_col.gap_md[
            PUIThemeController(value="dark"),
            PUIDiv().display_flex_row.gap_sm.items_center[
                PUIStatus().success, "Tudo ok"
            ],
            PUIDiv().display_flex_row.gap_sm.items_center[
                PUIStatus().error, "Tem algo errado!"
            ],
            PUIDiv().display_flex_row.gap_sm.items_center[
                PUIStatus().warning, "Precisa ficar de olho"
            ],
            PUIDiv().display_grid.grid_cols_3.width_full.gap_md[
                PUIStat(
                    title="Usuários Ativos",
                    value="10.481",
                    desc="Nos últimos 30 dias",
                    symbol="deployed_code_account",
                ).primary,
                PUIStat(
                    title="Usuários Novos",
                    value="5.302",
                    desc="Nos últimos 30 dias",
                    symbol="star",
                ).success,
                PUIStat(
                    title="Erros",
                    value="231",
                    desc="Nos últimos 30 dias",
                    symbol="error",
                ).error,
            ],
            PUICollapse(title="Clique aqui para expandir!")[
                PUIText()["Aqui vai um texto"]
            ],
            PUICard().image_full(
                "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            )[
                PUITitle().text_primary_content["Eu sou um card!"],
                PUIText()["Aqui tem um texto"],
                PUIAvatar(
                    src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
                ).width_sm.height_sm,
            ],
            PUISwap(on="Clique Aqui! 😠", off="Clique Aqui 😁").text_4xl,
            PUICountdown(
                values=[
                    PUICountdown.Value(value=10, sufix="h"),
                    PUICountdown.Value(value=59, sufix="m"),
                    PUICountdown.Value(value=59, sufix="s"),
                ]
            ),
            PUIDiv()[
                PUIText()[
                    "Pressione ",
                    PUIKbd()["ALT"],
                    " + ",
                    PUIKbd()["R"],
                    " para fazer algo",
                ]
            ],
            PUIButton(onclick=f"{modal.id}.showModal()").primary.width_full.soft[
                PUISymbol(symbol="credit_card").text_lg, "Meu Cartão MT"
            ],
        ],
        PUIDiv("max-w-1/2").display_flex_col.gap_md[
            PUIHover3dCardImg(
                img_src="https://img.daisyui.com/images/stock/creditcard.webp"
            ),
            PUIImgCarousel(
                img_srcs=[
                    "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                    "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                    "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                    "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
                ]
            ),
        ],
    ],
]

with open("index.html", "w+") as file:
    file.write(str(page))
