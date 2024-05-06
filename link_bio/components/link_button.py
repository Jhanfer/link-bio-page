import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles import constants
from typing import Optional
from reflex_motion import motion


def link_button(image:str,title:str, body:str, url:str, disabled:Optional[bool] = None, hover:Optional[dict] = None) -> rx.Component:
    return motion(
        rx.link(
            rx.button(
                rx.hstack(
                    rx.image(
                        src=image,
                        width=styles.Size.BIG.value,
                        height=styles.Size.BIG.value,
                        weight=styles.Size.BIG.value,
                        margin=styles.Size.MEDIUM.value,
                        alt=f"Logos {image}."),
                    rx.vstack(
                        rx.text(
                            title,
                            style=styles.BUTTON_TITLE_STYLE,
                            width="100%"),
                        rx.text(
                            body,
                            width="100%",
                            style=styles.BODY_STYLE),
                        spacing="0",
                        margin_top=styles.Size.SMALL.value,
                        align="center",
                        justify="center")),
                width="100%",
                disabled=disabled,
                _hover=hover),
            href=url,
            width="100%",
            is_external=True),
        while_hover={"scale": 1.05},
        while_tap={"scale": 0.9},
        transition={"type": "spring", "stiffness": 400, "damping": 17},
        width="100%")


"""    return rx.link(
        rx.button(text,
                    color_scheme="purple",
                    variant="surface",
                    padding_x="100px",
                    radius="large",
                    width="100%"),
                
    )"""