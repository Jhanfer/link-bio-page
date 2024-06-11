import reflex as rx 
import os
import dotenv
import link_bio.styles.styles as styles
import link_bio.styles.constants as cs
from link_bio.pages.index import index
from link_bio.pages.repos import repos
from link_bio.pages.courses import courses
from link_bio.api.api import live,repo


##Reflex App##
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src=cs.ANALYTICS_SCRIPTS_1),
        rx.script(cs.ANALYTICS_SCRIPTS_2)]
) 


# API ROUTES PRIVATE
class APIRoutes():
    dotenv.load_dotenv()  # se carga el entorno
    def routes() -> dict:
        LIVE_ROUTE:str= os.environ.get("LIVE")  # se cargan las variables
        REPO_ROUTE:str= os.environ.get("REPO")
        if LIVE_ROUTE and REPO_ROUTE:
            return {"live":LIVE_ROUTE,"route":REPO_ROUTE}
        else:
            return {"live":"na","route":"na"}


app.api.add_api_route(APIRoutes.routes()["live"],live) #se agrega la ruta de API
app.api.add_api_route(APIRoutes.routes()["route"],repo)


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