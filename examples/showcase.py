from paisy_ui import DaisyUI


def build_button_example():
    code = DaisyUI.Code(data_prefix=">", data_lang="python")(
        """
    from paisy_ui import DaisyUI

    DaisyUI.Button()("Default"),
    DaisyUI.Button().primary()("Primary"),
    DaisyUI.Button().secondary()("Secondary"),
    DaisyUI.Button().success()("Success"),
    DaisyUI.Button().warning()("Warning"),
    DaisyUI.Button().error()("Error"),
    DaisyUI.Button().accent()("Accent"),
    DaisyUI.Button().primary().ghost()("Primary Ghost"),
    DaisyUI.Button().primary().dash()("Primary Dash"),
        """
    )
    return DaisyUI.Card()(
        DaisyUI.SubTitle()("Button"),
        DaisyUI.LayoutGrid()(
            DaisyUI.Button()("Default"),
            DaisyUI.Button().primary()("Primary"),
            DaisyUI.Button().secondary()("Secondary"),
            DaisyUI.Button().success()("Success"),
            DaisyUI.Button().warning()("Warning"),
            DaisyUI.Button().error()("Error"),
            DaisyUI.Button().accent()("Accent"),
            DaisyUI.Button().primary().ghost()("Primary Ghost"),
            DaisyUI.Button().primary().dash()("Primary Dash"),
        ),
        code,
    )


if __name__ == "__main__":
    page = DaisyUI.HTML()(
        DaisyUI.LayoutNavbar(
            title="Test",
        )(DaisyUI.Title("🌻 PasyUI Showcase"), build_button_example())
    )
    with open("examples/showcase.html", "w+") as file:
        file.write(str(page))
