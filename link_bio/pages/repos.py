import reflex as rx 
from link_bio.components.nav_bar import nav_bar 
from link_bio.views.header.header import header
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
import link_bio.styles.constants as cs
import link_bio.utils.utils as ut
from link_bio.views.links.courses import repos_links
from link_bio.routes import Rutas

@rx.page(
        route=Rutas.REPOS.value,
        title=ut.repos_title,
        description=ut.repos_description,
        meta=ut.repos_meta
)
def repos() -> rx.Component:
    return rx.box(
        ut.lang(),
        nav_bar(),
        rx.center(
            rx.vstack(
            header(details=False),
            repos_links(),
                align="center",
                direction="column",
                max_width="560px",
                width="100%",
                margin_y=styles.Size.BIG.value)),
        footer())
