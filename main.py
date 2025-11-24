from paisy_ui import DaisyUI

if __name__ == "__main__":
    modal_teste = DaisyUI.Modal(id="modalTeste")(
        DaisyUI.Title().primary()("Modal Teste"), DaisyUI.Text()("Olá mundo!")
    )

    modal_logout = DaisyUI.Modal(id="modalLogout")(
        DaisyUI.Title().error()("Logout"), DaisyUI.Text()("Você tem certeza?")
    )

    menu_items = [
        DaisyUI.LayoutNavbar.MenuItem(label="Home", href="/home", symbol="home"),
        DaisyUI.LayoutNavbar.MenuItem(label="Tasks", href="/tasks", symbol="done_all"),
        DaisyUI.LayoutNavbar.MenuItem(
            label="Users",
            symbol="groups",
            subitems=[
                DaisyUI.LayoutNavbar.MenuItem(
                    label="Users", href="/users/list", symbol="group"
                ),
                DaisyUI.LayoutNavbar.MenuItem(
                    label="Permissions", href="/users/permissions", symbol="lock"
                ),
                DaisyUI.LayoutNavbar.MenuItem(
                    label="Historic",
                    symbol="update",
                    subitems=[
                        DaisyUI.LayoutNavbar.MenuItem(
                            label="Local",
                            href="/users/historic/local",
                            symbol="location_on",
                        ),
                        DaisyUI.LayoutNavbar.MenuItem(
                            label="Global",
                            href="/users/historic/local",
                            symbol="globe",
                        ),
                    ],
                ),
            ],
        ),
        DaisyUI.LayoutNavbar.MenuItem(
            label="Perfil",
            symbol="account_circle",
            subitems=[
                DaisyUI.LayoutNavbar.MenuItem(
                    label="Editar", href="/profile", symbol="person_edit"
                ),
                DaisyUI.LayoutNavbar.MenuItem(
                    label="Sair",
                    onclick=modal_logout.js_open,
                    symbol="logout",
                    variant="error",
                ),
            ],
        ),
    ]

    form = DaisyUI.Form()(
        DaisyUI.LayoutGrid()(
            DaisyUI.Input(
                legend="Nome Completo",
                help="Preencha com seu nome completo",
                symbol="signature",
                type="text",
                name="nome",
                id="nome",
                placeholder="Zé da Silva",
            ),
            DaisyUI.Input(
                legend="E-mail",
                help="Preencha com seu e-mail",
                symbol="email",
                type="email",
                name="email",
                id="email",
                placeholder="email@dominio.com",
            ),
            DaisyUI.Input(
                legend="Data de Nascimento",
                help="Preencha com sua data de nascimento",
                symbol="cake",
                type="date",
                name="idade",
                id="idade",
                placeholder="10/10/1990",
            ),
        ),
        DaisyUI.Button().accent()("Enviar"),
    )

    alert = DaisyUI.Alert(symbol="done_all").success()("Tudo certo!")

    table = DaisyUI.Table(
        collumns=[
            DaisyUI.Text()(DaisyUI.Symbol(symbol="tag"), "Id"),
            DaisyUI.Text()(DaisyUI.Symbol(symbol="signature"), "Nome"),
            DaisyUI.Text()(DaisyUI.Symbol(symbol="clock_loader_10"), "Status"),
        ],
        rows=[
            [0, "foo", DaisyUI.Badge().primary().soft()("Foo")],
            [1, "bar", DaisyUI.Badge().warning().soft()("Foo")],
            [2, "far", DaisyUI.Badge().warning().soft()("Foo")],
            [3, "boo", DaisyUI.Badge().primary().soft()("Foo")],
        ],
    )

    page = DaisyUI.HTML()(
        DaisyUI.LayoutNavbar(
            title="Test",
            menu_items=menu_items,
        )(
            modal_logout,
            modal_teste,
            alert,
            DaisyUI.Card()(
                DaisyUI.Title()("Título do card"),
                DaisyUI.Text()("Conteúdo do card"),
                table,
                DaisyUI.Button(onclick=modal_teste.js_open)("Abrir Modal"),
            ),
            DaisyUI.Card()(
                DaisyUI.Title()("Formulário"),
                form,
            ),
        )
    )
    with open("index.html", "w+") as file:
        file.write(page.prettify())
