import reflex as rx
import link_bio.styles.styles as styles
import link_bio.styles.fonts as fonts
import link_bio.styles.constants as const

def nav_bar() -> rx.Component:
    return rx.hstack( #hstack se usa para crear barras horizontales
                    rx.link(
                        rx.text(
                            "u",
                            rx.text.strong(
                                "Kory;",
                                color=styles.Color.PRIMARY.value,
                                as_="span",
                                weight=fonts.FontWeight.BOLD.value
                                ),
                            width="100px",
                            height="auto",
                            color=styles.Color.PRIMARY.value,
                            font_family=fonts.Font.LOGO.value
                            ),
                        size="7",
                        href=const.WEBPAGE,
                        is_external=False
                        ),
                    position="sticky",
                    bg=styles.Color.CONTENT.value,
                    border_radius="0px",
                    width="100%",
                    padding_y=styles.Size.MEDIUM.value,
                    padding_x=styles.Size.MEDIUM.value,
                    top="0",
                    z_index = "999" #es la importancia del objeto(el como se va a superponer a otros)
                    )