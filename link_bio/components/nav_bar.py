import reflex as rx
import link_bio.styles.styles as styles
import link_bio.styles.fonts as fonts
import link_bio.styles.constants as const
from link_bio.components.ant_components import float_button
from reflex_motion import motion

def nav_bar() -> rx.Component:
    return rx.hstack( 
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
                        is_external=False),
                        float_button(href=const.INVITEME_A_COFFEE,
                            icon=rx.image(src="/icons/mug-hot-solid.svg"),
                            target="_blank",
                            shape="square",
                            badge={"dot":True,"color":styles.Color.PRIMARY.value,"ribon":{"placement":"start"}}),
                    position="sticky",
                    bg=styles.Color.CONTENT.value,
                    border_radius="0px",
                    width="100%",
                    padding_y=styles.Size.MEDIUM.value,
                    padding_x=styles.Size.MEDIUM.value,
                    top="0",
                    z_index = "999")