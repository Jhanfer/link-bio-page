import reflex as rx
import reflex.components.radix.themes as rdxt
from link_bio.components.link_button import link_button
from link_bio.components.title import title
import link_bio.styles.styles as styles 
import link_bio.styles.constants as constants

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos","0em"),
        link_button(ext=True,image="/icons/youtube.svg",title="Python Basics",body="Curso básico sobre python",url=constants.PYTHON_1,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.YOUTUBE.value),
        link_button(ext=True,image="/icons/youtube.svg",title="Python Intermedio",body="Curso intermedio sobre python",url=constants.PYTHON_2,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.YOUTUBE.value),
        link_button(ext=True,image="/icons/youtube.svg",title="Python Backend",body="Curso Backend en python",url=constants.PYTHON_BACKEND_1,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.YOUTUBE.value),
        rdxt.separator(color_scheme="mint",decorative=True),
        link_button(ext=True,image="/icons/github.svg",title="Python Web Basic",body="Curso de Reflex-python",url=constants.PYTHON_WEB_6HORAS,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.ALTERNATIVE.value),
        link_button(ext=True,image="/icons/github.svg",title="Python Web Intermedio",body="Curso de Reflex-python intermedio",url=constants.PYTHON_WEB_7HORAS,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.ALTERNATIVE.value),
        align="center",
        width="100%",
        padding=styles.Size.DEFAULT.value,
        spacing=styles.SizeNoEm.MEDIUM.value
        )

def repos_links() -> rx.Component:
    return rx.vstack(
        title("Python Web","0em"),
        link_button(ext=True,image="/icons/github.svg",title="Link Bio Webpage",body="tarjeta de presentación con enlaces",url=constants.LINK_BIO_REPO,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.ALTERNATIVE.value),
        link_button(ext=True,image="/icons/github.svg",title="Webstore Example",body="ejemplo de tienda web (no utilizable)",url=constants.VIVAKITS_STORE_EXAMPLE,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.ALTERNATIVE.value),
        align="center",
        width="100%",
        padding=styles.Size.DEFAULT.value,
        spacing=styles.SizeNoEm.MEDIUM.value,
        padding_bottom="20em"
        )