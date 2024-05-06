import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import icons

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.text(
            rx.text.strong(
                    title,
                    font_weight="bold",
                    color=styles.Color.PRIMARY.value,
                    as_="span"),
            f" {body}",
            font_size=styles.Size.MEDIUM.value,
            style=styles.BODY_STYLE_NO_WIDTH
            )
    )