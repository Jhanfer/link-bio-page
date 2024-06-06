from enum import Enum
import reflex as rx
import link_bio.styles.fonts as fonts
##Constantes para los estilos##

##colores##
class Color(Enum):
    PRIMARY="#7947ff"
    SECONDARY="#578349"
    BACKGROUND="#242424"
    CONTENT="#333333"
    
class TextColor(Enum):
    HEADER="#F8F8F8"
    BODY="#C3C7CB"
    FOOTER="#1F1F1F"
    ALT_TEXT_COLOR="#56405D"
##colores##

##Stylesheets## esto es para llamar a las fuentes y que pueda ser usado en cualquier navegador
STYLESHEETS=[
    "https://fonts.googleapis.com/css?family=JetBrains+Mono:weight@100&display=swap",
    "https://fonts.googleapis.com/css?family=Nunito+Sans:weight@400&display=swap",
    "/css/styles.css"
]


##Medidas##
MAX_WIDTH="600px"

##Objeto de medidas Spacer##
class Size(Enum):
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    INTERMEDIATE="1.3em"
    BIG="2em"
#1 em toma en cuenta el tamaño de fuente de la aplicación

class SizeNoEm(Enum):
    VERYSMALL="1"
    SMALL="3"
    MEDIUM="5"
    DEFAULT="7"
    BIG="9"


##Estilo base##

BASE_STYLE={
    "background_color":Color.BACKGROUND.value,
    rx.button:{
        "width":"100%",
        "height":"100%",
        "display":"block",
        "padding":Size.MEDIUM.value,
        "border_radius":Size.DEFAULT.value,
        "text":TextColor.HEADER,
        "background_color":Color.CONTENT.value,
        "white_space":"normal",  #propiedad para estrechar los textos
        "align":"start",
        "cursor":"pointer",
        "_hover":{
            "background_color":Color.SECONDARY.value},
            "variant":"surface"
        },
    rx.link:{
        "text_decoration":"none",
        "_hover":{
            "color":Color.PRIMARY.value}
        },
    rx.avatar:{
        "bg":Color.SECONDARY.value,
        "font_size":"5em"
        }
    }

TITLE_STYLE=dict(
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    font_family=fonts.Font.TITLE.value,
    font_weight=fonts.FontWeight.BOLD.value
    )
BODY_STYLE_NO_WIDTH=dict(
    color=TextColor.BODY.value,
    font_family=fonts.Font.DEFAULT.value,
    font_weight=fonts.FontWeight.LIGHT.value
    )
TITLE_STYLE_NO_WIDTH=dict(
    color=TextColor.HEADER.value,
    font_family=fonts.Font.TITLE.value,
    font_weight=fonts.FontWeight.BOLD.value
    )
USERNAME=dict(
    color=Color.PRIMARY.value,
    font_family=fonts.Font.TITLE.value,
    font_weight=fonts.FontWeight.MEDIUM.value
)
BUTTON_TITLE_STYLE=dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    font_family=fonts.Font.TITLE.value,
    font_weight=fonts.FontWeight.BOLD.value
    )
BODY_STYLE=dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
    font_family=fonts.Font.DEFAULT.value
    )
ICON_GHOST_STYLE=dict(
    width=Size.INTERMEDIATE.value,
    height=Size.INTERMEDIATE.value,
    weight=Size.INTERMEDIATE.value,
    gap="1em",
    color=TextColor.HEADER.value
    )

