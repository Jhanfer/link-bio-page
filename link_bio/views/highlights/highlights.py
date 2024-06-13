import reflex as rx
import link_bio.styles.styles as styles
from link_bio.styles.styles import Size, Color
from link_bio.model.featured import Featured


def featured_link(featured:Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                border_radius=Size.DEFAULT.value,
                background=Color.CONTENT.value,
                width="10em",
                height="11em",
                alt=f"Imagen destacada para: {featured.title}"
            ),
            rx.text(
                featured.title,
                size="1",
                style=styles.BUTTON_TITLE_STYLE
            ),
            spacing=styles.SizeNoEm.MEDIUM.value,
            align_items="start",
            #class_name=styles.FADEIN_ANIMATION
        ),
        href=featured.url,
        is_external=True,
        width="100%"
    )