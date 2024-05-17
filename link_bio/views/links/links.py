import reflex as rx
from link_bio.components.link_button import link_button
import link_bio.styles.styles as styles
from link_bio.components.title import title
from link_bio.styles import constants


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(ext=True,image="icons/twitch.svg",title="Twitch",body="directos seguidos",url=constants.TWITCH,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.TWITCH.value),
        link_button(ext=True,image="icons/youtube.svg",title="Youtube",body="videos de cualquier tipo!",url=constants.YOUTUBE,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.YOUTUBE.value),
        link_button(ext=True,image="icons/discord.svg",title="Discord",body="únete a mi comunidad",url=constants.DISCORD,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.DISCORD.value),
        link_button(ext=True,image="icons/file-solid.svg",title="Mi Web",body="accede a mi web!",url=constants.WEBPAGE,disabled=constants.BUTTON_ENABLED),
        align="center",
        width="100%",
        padding=styles.Size.DEFAULT.value,
        spacing=styles.SizeNoEm.MEDIUM.value
        ),rx.vstack(
            title("Recursos y más"),
            link_button(ext=True,image="icons/book-solid.svg",title="Libros",body="libros y demás contenido",url=constants.BOOKS,hover=constants.HOVER_DISABLED,disabled=constants.BUTTON_DISABLED),
            link_button(ext=False,image="icons/book-bookmark-solid.svg",title="Cursos",body="cursos que he realizado",url=constants.COURSES,hover=constants.CustomHoverPalett.ALTERNATIVE.value),
            link_button(ext=True,image="icons/amazon.svg",title="Wishlist",body="mi lista de deseados",url=constants.WISHLIST,disabled=constants.BUTTON_ENABLED,hover=constants.CustomHoverPalett.AMAZON.value),
            align="center",
            width="100%",
            padding=styles.Size.DEFAULT.value,
            spacing=styles.SizeNoEm.MEDIUM.value
            ),rx.vstack(
                title("Contacto"),
                link_button(ext=True,image="icons/inbox-solid.svg",title="My PublicInbox",body="respuesta rápida y con preferencia",url=constants.MY_PUBLIC_IMBOX,disabled=constants.BUTTON_DISABLED,hover=constants.HOVER_DISABLED),
                link_button(ext=True,image="icons/envelope-regular.svg",title="Email",body=constants.EMAIL,url=f"mailto:{constants.EMAIL}?",disabled=constants.BUTTON_ENABLED),
                align="center",
                width="100%",
                padding=styles.Size.DEFAULT.value,
                spacing=styles.SizeNoEm.MEDIUM.value
                )