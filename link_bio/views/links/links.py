import reflex as rx
from link_bio.components.link_button import link_button
import link_bio.styles.styles as styles
from link_bio.components.title import title
from link_bio.styles import constants
from link_bio.views.highlights.highlights import featured_link
from link_bio.state.pagestate import PageState

def links() -> rx.Component:
    return rx.box(
                rx.vstack(
                    title("Comunidad"),
                    link_button(ext=True,image="icons/twitch.svg",title="Twitch",body="directos seguidos",url=constants.TWITCH,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.TWITCH.value),
                    link_button(ext=True,image="icons/youtube.svg",title="Youtube",body="videos de cualquier tipo!",url=constants.YOUTUBE,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.YOUTUBE.value),
                    link_button(ext=True,image="icons/discord.svg",title="Discord",body="únete a mi comunidad",url=constants.DISCORD,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.DISCORD.value),
                    link_button(ext=True,image="icons/file-solid.svg",title="Mi Web",body="accede a mi web!",url=constants.WEBPAGE,disabled=constants.BUTTON_ENABLED),
                    align="center",
                    width="100%",
                    padding=styles.Size.DEFAULT.value,
                    spacing=styles.SizeNoEm.MEDIUM.value),

                #se agrega la función de highlights
                rx.cond(PageState.feature_info,
                    rx.vstack(
                        title("Destacado"),
                        rx.hstack(
                            rx.flex(
                                rx.foreach( #iteradir
                                    PageState.feature_info, #elemento iterado (lista)
                                    featured_link), #llama a la función y le pasa como argumento cada elemento iterado
                                spacing="5",
                                width="100%",
                                justify="center"),
                            align="center"),

                        align="center",
                        width="100%",
                        padding=styles.Size.DEFAULT.value,
                        spacing=styles.SizeNoEm.MEDIUM.value
                        )),
                    
                rx.vstack(
                    title("Recursos y más"),
                    link_button(ext=False,image="icons/book-solid.svg",title="Repositorios",body="mis repositorios de github",url=constants.GITHUB_REPOS,hover=constants.CustomHoverPalett.ALTERNATIVE.value),
                    link_button(ext=False,image="icons/book-bookmark-solid.svg",title="Cursos",body="cursos que he realizado",url=constants.COURSES,hover=constants.CustomHoverPalett.ALTERNATIVE.value),
                    link_button(ext=True,image="icons/amazon.svg",title="Wishlist",body="mi lista de deseados",url=constants.WISHLIST,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.AMAZON.value),
                    align="center",
                    width="100%",
                    padding=styles.Size.DEFAULT.value,
                    spacing=styles.SizeNoEm.MEDIUM.value
                    ),
                        
                rx.vstack(
                    title("Contacto"),
                    link_button(ext=True,image="icons/inbox-solid.svg",title="My PublicInbox",body="respuesta rápida y con preferencia",url=constants.MY_PUBLIC_IMBOX,disabled=constants.BUTTON_DISABLED,hover=constants.HOVER_DISABLED),
                    link_button(ext=True,image="icons/envelope-regular.svg",title="Email",body=constants.EMAIL,url=f"mailto:{constants.EMAIL}?",disabled=constants.BUTTON_ENABLED),
                    align="center",
                    width="100%",
                    padding=styles.Size.DEFAULT.value,
                    spacing=styles.SizeNoEm.MEDIUM.value
                    ),

                width="100%",
                on_mount=PageState.feature_links)