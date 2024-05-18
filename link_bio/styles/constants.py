from enum import Enum
import link_bio.styles.styles as styles
from link_bio.routes import Rutas

##Enlaces LinkBio##
TWITCH="https://www.twitch.tv/ukory_"
YOUTUBE="https://www.youtube.com/channel/UCBiXuvbEJnbv66Wx24DOjAQ"
DISCORD="https://discord.gg/cuzecE5YzB"
GITHUB="https://github.com/Jhanfer"
BOOKS="n/a"
GITHUB_REPOS=Rutas.REPOS.value
COURSES=Rutas.COURSES.value
MY_PUBLIC_IMBOX="n/a"
WISHLIST="https://www.amazon.es/hz/wishlist/ls/16ZS1N3ZTGLY2?ref_=wl_share"
TIKTOK="https://www.tiktok.com/@koryless?_t=8lubxL9Mhay&_r=1"
TWITTER="https://x.com/koryunderg?s=09"
SPOTIFY="https://open.spotify.com/playlist/6CtrZ6xOlHIrKDog5RiMlq?si=9f38be1984264b23"
EMAIL="koryunderg@gmail.com"
WEBPAGE="http://ukory.es"

##Enlaces cusos##
PYTHON_1="https://www.youtube.com/watch?v=Kp4Mvapo5kc"
PYTHON_2="https://www.youtube.com/watch?v=TbcEqkabAWU"
PYTHON_BACKEND_1="https://www.youtube.com/watch?v=_y9qQZXE24A"
PYTHON_WEB_6HORAS="https://github.com/mouredev/python-web"
PYTHON_WEB_7HORAS="https://github.com/mouredev/python-web"

##Enlaces mis Repositorios##
LINK_BIO_REPO="https://github.com/Jhanfer/link-bio-page"
VIVAKITS_STORE_EXAMPLE="https://github.com/Jhanfer/vivakits-webpage-example"


##Botones##
BUTTON_DISABLED=True
BUTTON_ENABLED=False

HOVER_DISABLED={
    "background_color":"#784242"
    }
    
CUSTOM_HOVER={
    "background_color":styles.Color.PRIMARY.value
}

class CustomHoverPalett(Enum):
    TWITCH={"background_color":"#6441a5"}
    YOUTUBE={"background_color":"#FF0000"}
    DISCORD={"background_color":"#7289da"}
    AMAZON={"background_color":"#ff9900"}
    ALTERNATIVE={"background_color":styles.Color.SECONDARY.value}


##SCRIPTS##

ANALYTICS_SCRIPTS_1="https://www.googletagmanager.com/gtag/js?id=G-FLL2G6G6XR"
ANALYTICS_SCRIPTS_2="""window.dataLayer = window.dataLayer || [];
                    function gtag(){dataLayer.push(arguments);}
                    gtag('js', new Date());
                    gtag('config', 'G-FLL2G6G6XR');"""