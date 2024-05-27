import reflex as rx 
from link_bio.components.nav_bar import nav_bar 
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles
import link_bio.utils.utils as ut
from link_bio.routes import Rutas
from reflex_motion import motion


class IndexState(rx.State):
    @rx.var
    def say_hello(self):
        pass

@rx.page(
        route=Rutas.INDEX.value,
        title=ut.index_title,
        description=ut.index_description,
        image=ut.preview,
        meta=ut.index_meta 
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
                        rx.container(rx.text("/ukory/programmer",size="4",color="white")),
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

"""   responsive_carousel(
                    rx.link(rx.button(rx.image(src="/icons/amazon.svg")),href="/cursos"),
                    rx.link(rx.button(rx.image(src="/icons/amazon.svg")),href="/repositorios"),
                    rx.link(rx.button(rx.image(src="/icons/amazon.svg")),href="/coso"),
                    axis="horizontal",
                    infinite_loop=True,
                    auto_play=True,
                    swipeable=True,
                    width="50%",
                    height="50%"),"""