import reflex as rx
from link_bio.components.link_button import link_button
import link_bio.styles.styles as styles
from link_bio.components.title import title
from link_bio.styles import constants


def links() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button("icons/twitch.svg","Twitch","directos seguidos", constants.TWITCH, constants.BUTTON_ENABLED, constants.CustomHoverPalett.TWITCH.value),
        link_button("icons/youtube.svg","Youtube","videos de cualquier tipo!", constants.YOUTUBE, constants.BUTTON_ENABLED,constants.CustomHoverPalett.YOUTUBE.value),
        link_button("icons/discord.svg","Discord","únete a mi comunidad", constants.DISCORD, constants.BUTTON_ENABLED,constants.CustomHoverPalett.DISCORD.value),
        link_button("icons/file-solid.svg","Mi Web","accede a mi web!", constants.WEBPAGE, constants.BUTTON_ENABLED),
        align="center",
        width="100%",
        padding=styles.Size.DEFAULT.value,
        spacing=styles.SizeNoEm.MEDIUM.value
        ),rx.vstack(
            title("Recursos y más"),
            link_button("icons/book-solid.svg","Libros","libros", constants.BOOKS, True, constants.HOVER_DISABLED),
            link_button("icons/book-bookmark-solid.svg","Cursos","cursos que he realizado", constants.COURSES,constants.BUTTON_DISABLED, constants.HOVER_DISABLED),
            link_button("icons/amazon.svg","Wishlist","mi lista de deseados", constants.WISHLIST, constants.BUTTON_ENABLED, constants.CustomHoverPalett.AMAZON.value),
            align="center",
            width="100%",
            padding=styles.Size.DEFAULT.value,
            spacing=styles.SizeNoEm.MEDIUM.value
            ),rx.vstack(
                title("Contacto"),
                link_button("icons/inbox-solid.svg","My PublicInbox","respuesta rápida y con preferencia", constants.MY_PUBLIC_IMBOX, constants.BUTTON_DISABLED, constants.HOVER_DISABLED),
                link_button("icons/envelope-regular.svg","Email",constants.EMAIL, f"mailto:{constants.EMAIL}?",constants.BUTTON_ENABLED),
                align="center",
                width="100%",
                padding=styles.Size.DEFAULT.value,
                spacing=styles.SizeNoEm.MEDIUM.value
                )