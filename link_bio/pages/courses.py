import reflex as rx 
from link_bio.components.nav_bar import nav_bar 
from link_bio.views.header.header import header
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
from link_bio.views.links.courses import courses_links
import link_bio.utils.utils as ut
from link_bio.routes import Rutas

@rx.page(
        route=Rutas.COURSES.value,
        title=ut.courses_title,
        description=ut.courses_description,
        meta=ut.courses_meta)

def courses() -> rx.Component:
    return rx.box(
        ut.lang(),
        nav_bar(),
        rx.center(
            rx.vstack(
            header(),
            courses_links(),
                align="center",
                direction="column",
                max_width="560px",
                width="100%",
                margin_y=styles.Size.BIG.value)),
        footer())