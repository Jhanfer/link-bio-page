import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles import constants
from typing import Optional
from reflex_motion import motion



def stream_popup() -> rx.Component:
    return motion(
                motion(
                    rx.link(
                        rx.button(
                            rx.hstack(
                                rx.image(
                                    src="icons/twitch.svg",
                                    width=styles.Size.BIG.value,
                                    height=styles.Size.BIG.value,
                                    weight=styles.Size.BIG.value,
                                    margin=styles.Size.MEDIUM.value,
                                    alt=f"Logo de Twitch."),
                                
                                rx.vstack(
                                    rx.text(
                                        "Próximo directo",
                                        style=styles.BUTTON_TITLE_STYLE,
                                        width="100%"),
                                    
                                    rx.text(
                                        "Aún no hay fecha definida",
                                        width="100%",
                                        style=styles.BODY_STYLE),
                                    
                                    spacing="0",
                                    margin_top=styles.Size.SMALL.value,
                                    align="center",
                                    justify="center")),
                            
                            width="100%",
                            _hover=constants.CustomHoverPalett.TWITCH.value,
                            border_radius=styles.Size.MEDIUM.value,
                            border=f"{"2px"} solid {styles.Color.PRIMARY.value}"),
                        
                        href=constants.TWITCH,
                        width="100%",
                        is_external=True,
                        padding_top=styles.Size.BIG.value),
                    
                    while_hover={"scale": 1.05},
                    while_tap={"scale": 0.9},
                    transition={"type": "spring", "stiffness": 400, "damping": 17},
                    width="100%"),
                width="100%",
                initial={"scale":0},
                animate={"scale":1},
                transition={"type":"spring","delay":2,"stiffness": 260, "damping": 20}
                )