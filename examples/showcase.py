import os

from paisy_ui.components import (
    PUIHTML,
    PUIAlert,
    PUIAvatar,
    PUIButton,
    PUICard,
    PUICheckbox,
    PUICollapse,
    PUICountdown,
    PUIDateInput,
    PUIDateTimeLocalInput,
    PUIDiv,
    PUIDivider,
    PUIEmailInput,
    PUIFileInput,
    PUIFilter,
    PUIHover3dCard,
    PUIHover3dCardImg,
    PUIImg,
    PUIImgCarousel,
    PUIKbd,
    PUIList,
    PUILoading,
    PUIModal,
    PUINumberInput,
    PUIPasswordInput,
    PUIProgress,
    PUIRadialProgress,
    PUIRadio,
    PUIRange,
    PUISearchInput,
    PUISelect,
    PUISidebarLayout,
    PUIStat,
    PUIStatus,
    PUISwap,
    PUISymbol,
    PUITable,
    PUITelephoneInput,
    PUIText,
    PUITextInput,
    PUITextRotate,
    PUIThemeController,
    PUITimeInput,
    PUITitle,
    PUIToast,
    PUIToggle,
    PUIUrlInput,
)

transacoes = [
    ("15/12/2025", 20.00),
    ("14/12/2025", -34.00),
    ("13/12/2025", 21.00),
    ("12/12/2025", -11.00),
    ("11/12/2025", 5.00),
    ("10/12/2025", 8.90),
]


modal_card = PUIHover3dCard()[
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
        PUIDiv("mt-auto").display_flex_col["Alfredo da Silva", "126748126487112"],
        PUIDiv("mt-auto").display_flex_col.items_end["Exp. 10/30", "CVV 12134"],
    ]
]

modal_title = PUITitle().text_primary["Este é o seu Cartão!"]

modal_list = PUIList(title="Últimas Transações")[
    *(
        PUIDiv().display_flex_row.items_center.justify_between[
            data,
            (
                PUIDiv().display_flex_row.items_center.gap_sm.text_error.font_bold[
                    f"- R$ {abs(valor):.2f}", PUISymbol(symbol="more_down")
                ]
                if valor < 0
                else PUIDiv().display_flex_row.items_center.gap_sm.text_success.font_bold[
                    f"R$ {abs(valor):.2f}", PUISymbol(symbol="more_up")
                ]
            ),
        ]
        for data, valor in transacoes
    )
]

modal = PUIModal(id="modal_01")[
    PUIDiv().display_flex_col.gap_md[
        modal_card,
        modal_title,
        "Muito legal né?",
        modal_list,
        PUIButton().primary.soft["Histórico de Completo"],
        PUIButton().primary.dash["Bloquear Cartão"],
    ]
]

modal_edit = PUIModal(id="modal_02")[
    PUIDiv().display_flex_col.gap_md[
        PUITitle().text_primary["Detalhes"],
        PUICheckbox(
            name="checkbox",
            id="checkbox",
            label="Isso é um checkbox",
            legend="Checkbox",
        ),
        PUIFileInput(
            name="file", id="file", label="Insira um Arquivo", legend="Arquivo"
        ),
        PUIFilter(
            name="filter", id="filter", options=["Opcao 01", "Opcao 02", "Opcao 03"]
        ),
        PUIRadio(
            name="radio", id="radio", label="Explicação Opção 01", legend="Opção 01"
        ).primary,
        PUIRadio(
            name="radio", id="radio", label="Explicação Opção 02", legend="Opção 02"
        ).accent,
        PUIRadio(
            name="radio", id="radio", label="Explicação Opção 03", legend="Opção 03"
        ).info,
        PUIToggle(
            name="toggle1",
            id="toggle1",
            legend="Toggle",
            label="Instrução sobre toggle",
        ).primary,
        PUIToggle(
            name="toggle2",
            id="toggle2",
            legend="Toggle",
            label="Instrução sobre toggle",
        ).accent,
        PUIRange(name="range", id="range", legend="Range").accent,
        PUIRange(name="range", id="range", legend="Range").primary,
        PUISelect(
            name="select",
            id="select",
            legend="Select",
            options=[
                "Opção 01",
                "Opção 02",
                "Opção 03",
            ],
        ),
        PUITextInput(
            name="text1", id="text1", legend="Text", label="Instrução de como preencher"
        ),
        PUITextInput(
            name="text2",
            id="text2",
            legend="Text Pattern",
            pattern="[A-Za-z][A-Za-z0-9\\-]*",
            minlength=3,
            maxlength=30,
            required=True,
            validator_hint="Apenas letras, números ou traços",
        ),
        PUITextInput(
            name="text3",
            id="text3",
            legend="Text Datalist",
            datalist=[
                "Sugestão 01",
                "Sugestão 02",
                "Sugestão 03",
            ],
        ),
        PUIDateInput(name="date", id="date", legend="Date"),
        PUITimeInput(name="time", id="time", legend="Time"),
        PUIDateTimeLocalInput(
            name="datetime-local", id="datetime-local", legend="Datetime Local"
        ),
        PUISearchInput(
            name="search", id="search", legend="Search", placeholder="Buscar..."
        ),
        PUIEmailInput(
            name="email", id="email", legend="E-mail", placeholder="Digite seu e-mail"
        ),
        PUIPasswordInput(name="password", id="password", legend="Password"),
        PUINumberInput(name="password", id="password", legend="Number"),
        PUITelephoneInput(name="password", id="password", legend="Telephone"),
        PUIUrlInput(name="url", id="url", legend="URL"),
    ]
]

page_left_side_content = PUIDiv().display_flex_col.gap_md[
    PUIThemeController(value="dark"),
    PUITextRotate()["10% CASHBACK", "CASHBACK ESPECIAL"],
    PUIDiv().display_flex_row.gap_md[
        PUILoading().sm.primary.spinner,
        PUILoading().md.primary.spinner,
        PUILoading().lg.primary.spinner,
        PUILoading().secondary.bars,
        PUILoading().accent.ball,
        PUILoading().ring,
        PUILoading().info.dots,
    ],
    PUIProgress().primary,
    PUIProgress(value=10, max=50).secondary,
    PUIDiv().display_flex_row.gap_md[
        PUIRadialProgress(value=15, max=20).accent,
        PUIRadialProgress(value=10, max=20).secondary,
        PUIRadialProgress(value=5, max=20).primary,
    ],
    PUIDivider(content="Misc").primary.divider_end,
    PUIDiv().display_flex_row.gap_md[
        PUIDiv().width_md.height_md.skeleton,
        PUIDiv().width_md.height_md.skeleton_text["Eu sou um conteúdo carregando..."],
    ],
    PUIDivider(content="Avisos").accent.divider_start,
    PUIAlert(
        symbol="info",
        message="Isso é um aviso informativo",
        close_button=True,
    ).info,
    PUIAlert(symbol="bomb", message="Isso é um aviso de erro", close_button=True).error,
    PUIAlert(
        symbol="check", message="Isso é um aviso sucesso", close_button=True
    ).success,
    PUIDiv().display_flex_row.gap_sm.items_center[PUIStatus().success, "Tudo ok"],
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
    PUITable(
        columns=["#", "Nome", "Saldo", ""],
        rows=[
            [
                "1",
                "Zé da Silva",
                PUIText().font_bold.text_success["31.90"],
                PUIButton(onclick=f"{modal_edit.id}.showModal()")
                .sm.ghost[PUISymbol(symbol="edit").text_lg]
                .tooltip("Editar"),
            ],
            [
                "2",
                "João Pereira",
                PUIText().font_bold.text_success["123.44"],
                PUIButton(onclick=f"{modal_edit.id}.showModal()")
                .sm.ghost[PUISymbol(symbol="edit").text_lg]
                .tooltip("Editar"),
            ],
            [
                "3",
                "Márcia Fagundes",
                PUIText().font_bold.text_error["-51.12"],
                PUIButton(onclick=f"{modal_edit.id}.showModal()")
                .sm.ghost[PUISymbol(symbol="edit").text_lg]
                .tooltip("Editar"),
            ],
        ],
    ),
]

page_right_side_content = PUIDiv("max-w-1/2").display_flex_col.gap_md[
    PUICollapse(title="Clique aqui para expandir!")[PUIText()["Aqui vai um texto"]],
    PUIDiv().display_flex_row.gap_md[
        PUICard().image_full(
            "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
        )[
            PUITitle().text_primary_content["Eu sou um card!"],
            PUIText()["Aqui tem um texto"],
            PUIAvatar(
                src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            ).sm,
        ],
        PUIDiv().display_flex_col.gap_sm[
            PUIAvatar(
                src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            ).sm,
            PUIAvatar(
                src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            ).md,
            PUIAvatar(
                src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            ).lg,
            PUIAvatar(
                src="https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp"
            ).xl,
        ],
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
    PUIHover3dCardImg(img_src="https://img.daisyui.com/images/stock/creditcard.webp"),
    PUIImgCarousel(
        img_srcs=[
            "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
            "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
            "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
            "https://img.daisyui.com/images/stock/photo-1606107557195-0e29a4b5b4aa.webp",
        ]
    ),
]

page_content = (
    PUIDiv().padding_lg.margin_lg.display_flex_row.items_start.justify_center.gap_md[
        modal,
        modal_edit,
        PUIToast(
            messages=[
                PUIToast.Message(variant="primary", content="Isso é uma mensagem"),
                PUIToast.Message(variant="error", content="Isso é um erro"),
            ]
        ).toast_end,
        page_left_side_content,
        PUIDivider(content="Foo").divider_horizontal,
        page_right_side_content,
    ]
)

page = PUIHTML()[
    PUISidebarLayout(
        title="Teste",
        menu_items=[
            PUISidebarLayout.MenuItem(
                href="https://google.com.br", content="Google", symbol="globe"
            ),
            PUISidebarLayout.MenuItem(
                href="https://google.com.br", content="Google", symbol="globe"
            ),
            PUISidebarLayout.MenuItem(
                href="https://google.com.br", content="Google", symbol="globe"
            ),
        ],
    )[page_content]
]


current_dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{current_dir}/index.html", "w+") as file:
    file.write(str(page))
