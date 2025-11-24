from paisy_ui import DaisyUI

if __name__ == "__main__":
    modal_test = DaisyUI.Modal(id="modal_test")(
        DaisyUI.Title().primary()("Modal Test"), DaisyUI.Text()("Hello World!")
    )

    modal_logout = DaisyUI.Modal(id="modalLogout")(
        DaisyUI.Title().error()("Logout"), DaisyUI.Text()("Are you sure?")
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
            label="Profile",
            symbol="account_circle",
            subitems=[
                DaisyUI.LayoutNavbar.MenuItem(
                    label="Edit", href="/profile", symbol="person_edit"
                ),
                DaisyUI.LayoutNavbar.MenuItem(
                    label="Logout",
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
                legend="Full Name",
                help="Both your first and last names",
                symbol="signature",
                type="text",
                name="nome",
                id="nome",
                placeholder="Jack Silva",
            ),
            DaisyUI.Input(
                legend="E-mail",
                help="Your best e-mail",
                symbol="email",
                type="email",
                name="email",
                id="email",
                placeholder="email@domain.com",
            ),
            DaisyUI.Input(
                legend="Birthdate",
                help="Including the year",
                symbol="cake",
                type="date",
                name="idade",
                id="idade",
                placeholder="10/10/1990",
            ),
        ),
        DaisyUI.Button().accent()("Submit"),
    )

    alert = DaisyUI.Alert(symbol="done_all").success()("It's all fine!")

    table = DaisyUI.Table(
        collumns=[
            DaisyUI.Text()(DaisyUI.Symbol(symbol="tag"), "Id"),
            DaisyUI.Text()(DaisyUI.Symbol(symbol="signature"), "Name"),
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
            modal_test,
            alert,
            DaisyUI.Card()(
                DaisyUI.Title()("Card Title"),
                DaisyUI.Text()("Card content"),
                table,
                DaisyUI.Button(onclick=modal_test.js_open)("Open Modal"),
            ),
            DaisyUI.Card()(
                DaisyUI.Title()("Form"),
                form,
            ),
        )
    )
    with open("index.html", "w+") as file:
        file.write(page.prettify())
