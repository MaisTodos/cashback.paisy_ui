from daisy_ui import DaisyUI

if __name__ == "__main__":
    menu_items = [
        DaisyUI.LayoutNavbar.MenuItem(label="Home", href="/home", symbol="home"),
        DaisyUI.LayoutNavbar.MenuItem(label="Users", href="/users", symbol="groups"),
        DaisyUI.LayoutNavbar.MenuItem(label="Tasks", href="/tasks", symbol="done_all"),
    ]

    modal_teste = DaisyUI.Modal(id="modalTeste")(
        DaisyUI.Title().primary()("Modal Teste"), DaisyUI.Text()("Olá mundo!")
    )

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

    page = DaisyUI.HTML()(
        DaisyUI.LayoutNavbar(
            title="Test",
            menu_items=menu_items,
        )(
            modal_teste,
            alert,
            DaisyUI.Card()(
                DaisyUI.Title()("Título do card"),
                DaisyUI.Text()("Conteúdo do card"),
                DaisyUI.Badge().primary().soft()("Foo"),
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
