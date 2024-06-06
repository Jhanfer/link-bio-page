import reflex as rx
import datetime #también se pueden usar librerías de python
import link_bio.styles.styles as styles
import link_bio.styles.constants as const
from reflex.components import chakra as ch

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src=f"/favicon.ico",
                width="2em",
                height="2em",
                weight="2em",
                alt="Logotipo de Kory. Es una letra K morada"),
        ch.text(
            f"© 2024-{datetime.date.today().year}",
            ch.link(" \"uKory;\" ", href=const.WEBPAGE, is_external=False, color="gold",
                    _hover={"color":styles.Color.PRIMARY.value}),
            "by Kory v1.",
            as_="p",
            font_size=styles.Size.MEDIUM.value,
            color=styles.TextColor.HEADER.value
            ),
        align="center",
        bg=styles.Color.CONTENT.value,
        padding_top=styles.Size.DEFAULT.value,
        padding_bottom=styles.Size.BIG.value,
        margin_bottom="0"
    )