from paisy_ui import DaisyUI

if __name__ == "__main__":
    try:
        import uvicorn
        from fastapi import FastAPI, responses
    except ImportError:
        raise ImportError(
            "PaisyUI examples/with_fastapi.py requires fastapi. Install it with 'pip install fastapi'"
        )

    app = FastAPI()

    @app.get("/")
    def get_login():
        return responses.HTMLResponse(
            DaisyUI.HTML()(
                DaisyUI.LayoutCentered()(
                    DaisyUI.Form(action="/dashboard", method="get")(
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
                            legend="Password",
                            help="At least 6 characters",
                            symbol="lock",
                            type="password",
                            name="password",
                            id="password",
                            placeholder="******",
                        ),
                        DaisyUI.Button().accent()("Submit"),
                    )
                )
            )
        )

    @app.get("/dashboard")
    def get_dashboard():
        alert = DaisyUI.Alert(symbol="done_all").success()("It's all fine!")
        modal_logout = DaisyUI.Modal(id="modalLogout")(
            DaisyUI.Title().error()("Logout"),
            DaisyUI.Text()("Are you sure?"),
            DaisyUI.Button("mt-4", href="/").error().small()("Logout"),
        )
        return responses.HTMLResponse(
            DaisyUI.HTML()(
                modal_logout,
                DaisyUI.LayoutNavbar(
                    title="FastAPI Example",
                    menu_items=[
                        DaisyUI.LayoutNavbar.MenuItem(
                            label="Dashboard", href="/dashboard", symbol="home"
                        ),
                        DaisyUI.LayoutNavbar.MenuItem(
                            label="Profile",
                            symbol="account_circle",
                            subitems=[
                                DaisyUI.LayoutNavbar.MenuItem(
                                    label="Logout",
                                    onclick=modal_logout.js_open,
                                    symbol="logout",
                                    variant="error",
                                ),
                            ],
                        ),
                    ],
                )(
                    alert,
                    DaisyUI.Title().primary()("Welcome!"),
                    DaisyUI.Table(
                        collumns=[
                            DaisyUI.Text()(DaisyUI.Symbol(symbol="tag"), "Id"),
                            DaisyUI.Text()(DaisyUI.Symbol(symbol="signature"), "Name"),
                            DaisyUI.Text()(
                                DaisyUI.Symbol(symbol="clock_loader_10"), "Status"
                            ),
                        ],
                        rows=[
                            [0, "foo", DaisyUI.Badge().primary().soft()("Foo")],
                            [1, "bar", DaisyUI.Badge().warning().soft()("Foo")],
                            [2, "far", DaisyUI.Badge().warning().soft()("Foo")],
                            [3, "boo", DaisyUI.Badge().primary().soft()("Foo")],
                        ],
                    ),
                ),
            )
        )

    uvicorn.run(app)
