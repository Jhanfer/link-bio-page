import reflex as rx 
from link_bio.components.nav_bar import nav_bar 
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
import link_bio.utils.utils as ut
from link_bio.routes import Rutas
from reflex_motion import motion
from link_bio.state.pagestate import PageState


@rx.page(
        route=Rutas.INDEX.value,
        title=ut.index_title,
        description=ut.index_description,
        image=ut.preview,
        meta=ut.index_meta,
        on_load=PageState.check_live
        
)

def index() -> rx.Component: 
    return rx.box(
        ut.lang(),
        nav_bar(),
        rx.center(
            rx.vstack(
                header(details=True),
                links(),
                    motion(
                        rx.container(rx.text("/Jhanfer/link-bio-page",size="3",color="white")),
                        initial={"scale":0},
                        while_in_view={"scale":2},
                        transition={"type":"spring","damping":10,"swiftness":20}),
                align="center",
                direction="column",
                max_width="560px",
                width="100%",
                margin_y=styles.Size.BIG.value)),
        footer()
        )

