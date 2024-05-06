from enum import Enum
import link_bio.styles.styles as styles

##Enlaces##
TWITCH="https://www.twitch.tv/ukory_"
YOUTUBE="https://www.youtube.com/channel/UCBiXuvbEJnbv66Wx24DOjAQ"
DISCORD="https://discord.gg/cuzecE5YzB"
GITHUB="https://github.com/Jhanfer"
BOOKS="n/a"
COURSES="n/a"
MY_PUBLIC_IMBOX="n/a"
WISHLIST="https://www.amazon.es/hz/wishlist/ls/16ZS1N3ZTGLY2?ref_=wl_share"
TIKTOK="https://www.tiktok.com/@koryless?_t=8lubxL9Mhay&_r=1"
TWITTER="https://x.com/koryunderg?s=09"
SPOTIFY="https://open.spotify.com/playlist/6CtrZ6xOlHIrKDog5RiMlq?si=9f38be1984264b23"
EMAIL="koryunderg@gmail.com"
WEBPAGE="http://ukory.es"


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