import reflex as rx
import link_bio.styles.styles as styles
from link_bio.components.link_icon import icons
from link_bio.components.info_text import info_text
from link_bio.styles import constants
import link_bio.styles.fonts as fonts
from link_bio.components.stream_popup import stream_popup
from reflex_motion import motion

def header() -> rx.Component:
        return rx.vstack(
                rx.hstack(
                        rx.avatar(
                                fallback="JV",
                                src="/koryavatar.jpeg",
                                size="7",
                                radius="full",
                                color=styles.TextColor.BODY.value,
                                padding="2px"),
                        rx.vstack(
                                rx.heading("Jhan Vasquez",
                                        align="center",
                                        size="6",
                                        style=styles.TITLE_STYLE_NO_WIDTH),
                                rx.text(
                                        "@ukory",
                                        align="center",
                                        padding_y="0px",
                                        margin_top="0px !important",
                                        style=styles.USERNAME),
                                rx.hstack(
                                        icons("icons/spotify.svg",constants.SPOTIFY),
                                        icons("icons/github.svg",constants.GITHUB),
                                        icons("icons/tiktok.svg",constants.TIKTOK),
                                        icons("icons/x-twitter.svg",constants.TWITTER),
                                        width="100%",
                                        spacing=styles.SizeNoEm.DEFAULT.value,
                                        padding_top=styles.Size.MEDIUM.value),
                                spacing="0",
                                padding_y="0.5em"),
                                spacing=styles.SizeNoEm.SMALL.value,
                                width="100%",
                                padding_y="0em",
                                align_items="start"),
                rx.flex(
                        info_text("1","año de experiencia"),
                        rx.spacer(),
                        info_text("1","proyectos realizados"),
                        rx.spacer(),
                        info_text("0","tazas de café"),
                        width="100%",
                        align="start",
                        margin_bottom="0.8em"),
                
                stream_popup(),
                
                motion(
                        rx.text("""Soy un pequeño streamer y programador en Python. 
                                Actualmente, me dedico a estudiar más acerca de este increíble lenguaje,
                                además de realizar streams en mis tiempos libres. Mi meta es convertirme en
                                un programador profesional de Machine Learning, desarrollador web y de 
                                aplicaciones. ¡Gracias!""",
                                font_size=styles.Size.DEFAULT.value,
                                width="100%",
                                style=styles.BODY_STYLE_NO_WIDTH,
                                white_space="normal",
                                margin_top="0.8em"),
                        width="100%",
                        initial={"y":-50},
                        animate={"y":5},
                        transition={"type":"spring","delay":2,"stiffness": 260, "damping": 20}),
                align="start",
                spacing=styles.SizeNoEm.SMALL.value,
                width="95%")
