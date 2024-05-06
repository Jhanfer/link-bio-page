import reflex as rx
import link_bio.styles.styles as styles


def icons(src:str, url:str) -> rx.Component:
    return rx.link(
        rx.image(src=src,
                style=styles.ICON_GHOST_STYLE,
                alt=f"Iconos de {src}."
                ),
        href=url,
        is_external=True,)
