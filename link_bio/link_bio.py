import reflex as rx #importamos "reflex" como "rx"
from link_bio.components.nav_bar import nav_bar #se crea un módulo con la barra de navegación aparte
from link_bio.views.header.header import header
from link_bio.views.links.links import links
from link_bio.components.footer import footer
import link_bio.styles.styles as styles

class State(rx.State): #creamos la clase de estados
    pass

#lo que estamos haciendo aqui es llamar a un elemento que stackea los obejetos en vertical 
def index() -> rx.Component: 
    return rx.box(
        nav_bar(),
        rx.center( #se usa para centrar varios elementos
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


#en la instancia de la app, podemos meterle el estilo general de la página usando "styles=" y pasándole un mapa
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
) #creamos una instancia "App" de "reflex" o "rx"
app.add_page(index,
            title="uKory; | Streamer y programador",
            description="Hola, mi nombre es Jhan y soy un pequeño streamer y programador en Python. Actualmente, me dedico a estudiar más acerca de este increíble lenguaje...",
            image="icons/favicon.ico") 
#creamos una página usando ".add_page(función)"
#app.compile() #se compila. Nota: el ".compile" será eliminado en la siguente versión.


#"padding=" es un margen que dejamos hacia dentro del componente. Al ponerle "_y" o "_z" estaríamos trabajando con cada eje respectivamente
#"margin=" es un margen que dejamos hacia afuera del componente. Al ponerle "_y" o "_z" estaríamos trabajando con cada eje respectivamente

#hay que definir los margenes que vamos a utilizar en los proyectos. Por ejemplo: margen pequeño:15px, margen mediano:25px, margen grande:50p