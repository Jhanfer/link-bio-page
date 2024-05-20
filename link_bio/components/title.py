import reflex as rx
import link_bio.styles.styles as styles
from typing import Optional

def title(text:str,padding:Optional[str] = None ) -> rx.Component:
    return rx.heading(text,
                    style=styles.TITLE_STYLE,
                    size="5",
                    padding_top=padding)