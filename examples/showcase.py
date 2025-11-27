from typing import List, Type

from paisy_ui import BaseComponent, BaseComponents, DaisyUI

BASE_VARIANTS = [
    "neutral",
    "primary",
    "secondary",
    "success",
    "warning",
    "error",
    "accent",
]


def build_card(title: str, grid: DaisyUI.LayoutGrid, code: DaisyUI.Code):
    return DaisyUI.Card()(
        DaisyUI.SubTitle()(title),
        BaseComponents.Div("grid", "grid-cols-2", "gap-4")(
            grid,
            code,
        ),
    )


def build_variant_example(
    component: Type[BaseComponent],
    variants: List[str] = BASE_VARIANTS,
    **kwargs,
):
    kwargs_code = ", ".join(
        [
            (f"{key}={value}" if str(value).isdigit() else f'{key}="{value}"')
            for key, value in kwargs.items()
        ]
    )
    component_code = component.__name__
    variants_code = "\n".join(
        [
            (
                f'    DaisyUI.{component_code}({kwargs_code}).{variant}()("{variant.title()}")'
                if variant != "neutral"
                else f'    DaisyUI.{component_code}({kwargs_code})("{variant.title()}")'
            )
            for variant in variants
        ]
    )
    code = DaisyUI.Code(data_prefix=">", data_lang="python")(
        f"""
    from paisy_ui import DaisyUI

    ...
{variants_code}
        """
    )

    grid = DaisyUI.LayoutGrid("h-min", "p-4", "bg-base-300", "rounded-lg")
    for variant in variants:
        if variant == "neutral":
            grid.append(component(**kwargs)(variant.title()))
        else:
            grid.append(getattr(component(**kwargs), variant)()(variant.title()))

    return build_card(title=component_code, code=code, grid=grid)


def build_kwargs_example(component: Type[BaseComponent], kwargs_list: List[dict]):
    component_code = component.__name__
    variants_code = []
    for kwargs in kwargs_list:
        kwargs_code = ", ".join(
            [
                (f"{key}={value}" if str(value).isdigit() else f'{key}="{value}"')
                for key, value in kwargs.items()
            ]
        )
        variants_code.append(f"    DaisyUI.{component_code}({kwargs_code})")

    variants_code = "\n".join(variants_code)

    code = DaisyUI.Code(data_prefix=">", data_lang="python")(
        f"""
    from paisy_ui import DaisyUI

    ...
{variants_code}
        """
    )

    grid = DaisyUI.LayoutGrid("h-min", "p-4", "bg-base-300", "rounded-lg")
    for kwargs in kwargs_list:
        grid.append(component(**kwargs))

    return build_card(title=component_code, grid=grid, code=code)


if __name__ == "__main__":
    page = DaisyUI.HTML()(
        DaisyUI.LayoutNavbar(
            title="Test",
        )(
            DaisyUI.Title("🌻 PasyUI Showcase"),
            DaisyUI.Divider()("Interactive"),
            build_variant_example(
                DaisyUI.Badge, variants=[*BASE_VARIANTS, "soft", "dash"]
            ),
            build_variant_example(
                DaisyUI.Button, variants=[*BASE_VARIANTS, "ghost", "dash"]
            ),
            build_variant_example(
                DaisyUI.Alert,
                variants=["neutral", "success", "warning", "error"],
                symbol="info",
            ),
            DaisyUI.Divider()("Typography"),
            build_variant_example(DaisyUI.SubTitle),
            build_variant_example(DaisyUI.Title),
            build_variant_example(DaisyUI.Text),
            build_kwargs_example(
                DaisyUI.Symbol,
                [
                    {"symbol": "star"},
                    {"symbol": "done_all"},
                    {"symbol": "dialpad"},
                    {"symbol": "info"},
                    {"symbol": "help"},
                    {"symbol": "wand_stars"},
                ],
            ),
            build_kwargs_example(
                DaisyUI.Input,
                [
                    {
                        "type": "number",
                    },
                    {
                        "type": "email",
                    },
                    {
                        "type": "date",
                    },
                    {
                        "type": "number",
                        "legend": "Number",
                        "symbol": "dialpad",
                        "help": "A value between 1 and 10",
                        "min": 1,
                        "max": 10,
                    },
                    {
                        "type": "email",
                        "legend": "E-mail",
                        "symbol": "email",
                        "help": "This is the help",
                    },
                    {
                        "type": "date",
                        "legend": "Birthdate",
                        "symbol": "cake",
                        "help": "This is the help",
                    },
                ],
            ),
        )
    )
    with open("examples/index.html", "w+") as file:
        file.write(str(page))
