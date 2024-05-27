import reflex as rx 
import link_bio.styles.styles as styles
import link_bio.styles.constants as cs
from link_bio.pages.index import index
from link_bio.pages.repos import repos
from link_bio.pages.courses import courses
from link_bio.api.api import live,repo

class State(rx.State):
    """Hola!"""

    
##Reflex App##
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src=cs.ANALYTICS_SCRIPTS_1),
        rx.script(cs.ANALYTICS_SCRIPTS_2)]
) 


app.api.add_api_route("/live/{user}",live)
app.api.add_api_route("/repo",repo)

#old page add
"""def index() -> rx.Component: 
    return rx.box(
        ut.lang(),
        nav_bar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                align="center",
                direction="column",
                max_width="560px",
                width="100%",
                margin_y=styles.Size.BIG.value)),
        footer()
        )
        
        
app.add_page(
    title=
    route=
    description=
    meta=
    image=
)"""